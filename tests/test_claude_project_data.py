# ==============================================================
# VERSION: 0.1
# Behavior tests for scripts/claude_project_data.sh (CLAUDE.md Rule 14 locality tool).
#
# CHANGE LOG
# v0.1 — 2026-10-05 — Initial (PLAN-017): the script runs for real against throwaway repo +
#         HOME trees — POSIX status / link / adopt, the pre-v1.5 memory layout, the E002
#         folder-move merge — and its Windows branch through stand-in uname / cygpath / cmd
#         commands (a junction is simulated by a symlink; cmd calls are logged).
# ==============================================================
"""Tests for scripts/claude_project_data.sh — run the real script in temp trees."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "claude_project_data.sh"
OLD = time.time() - 3600  # an mtime well outside the live-session window

pytestmark = pytest.mark.skipif(shutil.which("bash") is None, reason="bash not available")


@dataclass
class Tree:
    repo: Path
    home: Path
    env: dict[str, str]
    log: Path | None = None

    @property
    def data(self) -> Path:
        return self.repo / ".claude" / "project-data"

    def run(self, verb: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["bash", str(self.repo / "scripts" / "claude_project_data.sh"), verb],
            env=self.env, capture_output=True, text=True, check=False,
        )

    def harness(self) -> Path:
        out = self.run("status").stdout
        match = re.search(r"^harness path:\s+(.+)$", out, re.MULTILINE)
        assert match, out
        return Path(match.group(1))


def _write(path: Path, text: str = "x", mtime: float | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if mtime is not None:
        os.utime(path, (mtime, mtime))


def _make_repo(repo: Path) -> None:
    (repo / "scripts").mkdir(parents=True)
    shutil.copy2(SCRIPT, repo / "scripts" / "claude_project_data.sh")


@pytest.fixture
def posix(tmp_path: Path) -> Tree:
    repo = tmp_path / "work" / "my repo"
    home = tmp_path / "home"
    home.mkdir()
    _make_repo(repo)
    env = {**os.environ, "HOME": str(home)}
    return Tree(repo=repo, home=home, env=env)


_SHIMS = {
    "uname": '#!/bin/bash\necho "MINGW64_NT-10.0-19045"\n',
    "cygpath": (
        "#!/bin/bash\n"
        'p="$2"; rest="${p#"$FAKE_WINROOT"/}"\n'
        '[ "$rest" != "$p" ] || exit 1\n'
        'drive="$(printf \'%s\' "${rest:0:1}" | tr \'[:lower:]\' \'[:upper:]\')"\n'
        'out="$drive:${rest:1}"\n'
        '[ "$1" = "-w" ] && out="${out//\\//\\\\}"\n'
        "printf '%s\\n' \"$out\"\n"
    ),
    "cmd": (
        "#!/bin/bash\n"
        'echo "cmd $*" >> "$SHIM_LOG"\n'
        "topath() {\n"
        '  p="${1//\\\\//}"\n'
        '  d="$(printf \'%s\' "${p:0:1}" | tr \'[:upper:]\' \'[:lower:]\')"\n'
        "  printf '%s/%s%s' \"$FAKE_WINROOT\" \"$d\" \"${p:2}\"\n"
        "}\n"
        'case "$2" in\n'
        '  mklink) ln -s "$(topath "$5")" "$(topath "$4")" ;;\n'
        '  rmdir) t="$(topath "$3")"; if [ -L "$t" ]; then rm "$t"; else rmdir "$t"; fi ;;\n'
        "  *) exit 1 ;;\n"
        "esac\n"
    ),
}


@pytest.fixture
def windows(tmp_path: Path) -> Tree:
    root = tmp_path / "win"
    repo = root / "e" / "Work_Area" / "demo-repo"
    home = root / "c" / "Users" / "someone"
    home.mkdir(parents=True)
    _make_repo(repo)
    shims = tmp_path / "shims"
    shims.mkdir()
    for name, body in _SHIMS.items():
        (shims / name).write_text(body, encoding="utf-8")
        (shims / name).chmod(0o755)
    log = tmp_path / "cmd.log"
    log.touch()
    env = {
        **os.environ, "HOME": str(home), "PATH": f"{shims}{os.pathsep}{os.environ['PATH']}",
        "FAKE_WINROOT": str(root), "SHIM_LOG": str(log),
    }
    return Tree(repo=repo, home=home, env=env, log=log)


# ---- POSIX (macOS / Linux) -------------------------------------------------


def test_posix_empty_then_link_is_idempotent(posix: Tree) -> None:
    first = posix.run("status")
    assert first.returncode == 1 and "STATUS: EMPTY" in first.stdout
    linked = posix.run("link")
    assert linked.returncode == 0 and "STATUS: OK" in linked.stdout
    harness = posix.harness()
    assert harness.is_symlink() and os.readlink(harness) == str(posix.data)
    again = posix.run("link")
    assert again.returncode == 0 and "Already linked." in again.stdout


def test_posix_adopt_moves_harness_data_in(posix: Tree) -> None:
    harness = posix.harness()
    _write(harness / "memory" / "a.md")
    _write(harness / "s1.jsonl")
    assert "Run: adopt" in posix.run("status").stdout
    out = posix.run("adopt")
    assert out.returncode == 0 and "STATUS: OK" in out.stdout
    assert (posix.data / "memory" / "a.md").is_file() and (posix.data / "s1.jsonl").is_file()
    assert harness.is_symlink()


def test_posix_adopt_absorbs_pre_v15_memory_layout(posix: Tree) -> None:
    old_store = posix.repo / ".claude" / "memory"
    _write(old_store / "a.md")
    _write(old_store / "b.md")
    harness = posix.harness()
    harness.mkdir(parents=True)
    (harness / "memory").symlink_to(old_store)
    _write(harness / "s1.jsonl")
    out = posix.run("adopt")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "absorbed old in-repo memory store" in out.stdout
    assert "(2 memory files)" in out.stdout
    assert not old_store.exists() and (posix.data / "s1.jsonl").is_file()


def test_posix_e002_folder_move_merges_harness_created_dir(posix: Tree) -> None:
    for name in ("a.md", "b.md", "c.md"):
        _write(posix.data / "memory" / name)
    harness = posix.harness()
    (harness / "memory").mkdir(parents=True)  # what Claude Code creates on session start
    _write(harness / "new.jsonl")
    status = posix.run("status")
    assert status.returncode == 1 and "Run: link" in status.stdout and "adopt" not in status.stdout
    out = posix.run("link")
    assert out.returncode == 0 and "(3 memory files)" in out.stdout, out.stdout
    assert (posix.data / "new.jsonl").is_file() and harness.is_symlink()


def test_posix_merge_recurses_into_same_name_dirs(posix: Tree) -> None:
    _write(posix.data / "memory" / "a.md")
    harness = posix.harness()
    _write(harness / "memory" / "c.md")
    out = posix.run("link")
    assert out.returncode == 0, out.stdout
    assert sorted(p.name for p in (posix.data / "memory").iterdir()) == ["a.md", "c.md"]


def test_posix_file_collision_still_aborts_without_loss(posix: Tree) -> None:
    _write(posix.data / "f.txt", "in-repo")
    harness = posix.harness()
    _write(harness / "f.txt", "harness")
    out = posix.run("link")
    assert out.returncode == 1 and "ABORT" in out.stdout
    assert (posix.data / "f.txt").read_text(encoding="utf-8") == "in-repo"
    assert (harness / "f.txt").read_text(encoding="utf-8") == "harness"


def test_posix_stale_symlink_is_repointed(posix: Tree, tmp_path: Path) -> None:
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    posix.data.mkdir(parents=True)
    harness = posix.harness()
    harness.parent.mkdir(parents=True)
    harness.symlink_to(elsewhere)
    assert "STATUS: BROKEN" in posix.run("status").stdout
    out = posix.run("link")
    assert out.returncode == 0 and "Re-pointing stale symlink" in out.stdout
    assert os.readlink(harness) == str(posix.data)


# ---- Windows (Git Bash) through stand-in uname / cygpath / cmd ---------------


def test_windows_path_key_uses_the_lowercased_drive_form(windows: Tree) -> None:
    out = windows.run("status").stdout
    assert re.search(r"^path-key:\s+e--Work-Area-demo-repo$", out, re.MULTILINE), out
    expected = windows.home / ".claude" / "projects" / "e--Work-Area-demo-repo"
    assert windows.harness() == expected


def test_windows_adopt_migrates_the_old_junction_layout(windows: Tree) -> None:
    old_store = windows.repo / ".claude" / "memory"
    _write(old_store / "m1.md", mtime=OLD)
    _write(old_store / "m2.md", mtime=OLD)
    harness = windows.harness()
    harness.mkdir(parents=True)
    (harness / "memory").symlink_to(old_store)  # bootstrap_memory.sh's junction
    _write(harness / "old.jsonl", "transcript", mtime=OLD)
    out = windows.run("adopt")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "STATUS: OK" in out.stdout and "(2 memory files)" in out.stdout
    assert harness.is_symlink() and harness.resolve() == windows.data.resolve()
    assert (windows.data / "old.jsonl").read_text(encoding="utf-8") == "transcript"
    backups = list(harness.parent.glob(f"{harness.name}.pre-locality-*"))
    assert len(backups) == 1 and (backups[0] / "old.jsonl").is_file()
    assert windows.log is not None
    calls = windows.log.read_text(encoding="utf-8")
    assert "cmd //c rmdir " in calls and "\\memory" in calls  # junction dropped via rmdir
    assert "cmd //c mklink //J " in calls


def test_windows_refuses_while_a_session_is_live(windows: Tree) -> None:
    harness = windows.harness()
    _write(harness / "live.jsonl")  # mtime = now
    out = windows.run("adopt")
    assert out.returncode == 1 and "looks active" in out.stdout
    assert harness.is_dir() and not harness.is_symlink()
    assert not list(harness.parent.glob(f"{harness.name}.pre-locality-*"))


def test_windows_e002_link_after_move_keeps_memories(windows: Tree) -> None:
    for name in ("a.md", "b.md"):
        _write(windows.data / "memory" / name)
    harness = windows.harness()
    (harness / "memory").mkdir(parents=True)
    _write(harness / "s.jsonl", mtime=OLD)
    assert "Run: link" in windows.run("status").stdout
    out = windows.run("link")
    assert out.returncode == 0 and "(2 memory files)" in out.stdout, out.stdout + out.stderr
    assert (windows.data / "s.jsonl").is_file()
    again = windows.run("link")
    assert again.returncode == 0 and "Already linked." in again.stdout
    assert "junction:" in again.stdout
