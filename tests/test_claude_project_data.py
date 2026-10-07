# ==============================================================
# VERSION: 0.2
# Behavior tests for scripts/claude_project_data.sh (CLAUDE.md Rule 14 locality tool).
#
# CHANGE LOG
# v0.2 — 2026-10-07 — PLAN-017 Phase 3b: an empty store is reported, never recommended for
#         link; Windows backups live in ~/.claude/locality-backups/ (not beside the link);
#         the new cleanup verb removes only fully covered backups, never follows a link, and
#         moves a kept old-location backup away from the link.
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


def _backups(tree: Tree) -> list[Path]:
    return sorted((tree.home / ".claude" / "locality-backups").glob("*.pre-locality-*"))


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


def test_posix_empty_store_is_reported_not_recommended(posix: Tree) -> None:
    posix.data.mkdir(parents=True)  # the store exists but its files are gone
    harness = posix.harness()
    (harness / "memory").mkdir(parents=True)  # what Claude Code creates on session start
    out = posix.run("status")
    assert out.returncode == 1, out.stdout
    assert "in-repo store is EMPTY" in out.stdout and "STOP" in out.stdout
    assert "holds 0 memory files" in out.stdout
    assert "in-repo data exists" not in out.stdout


def test_posix_empty_store_without_harness_says_stop(posix: Tree) -> None:
    posix.data.mkdir(parents=True)
    out = posix.run("status")
    assert out.returncode == 1
    assert "STATUS: EMPTY — the in-repo store exists but holds no files" in out.stdout
    assert "STOP" in out.stdout and "in-repo data exists" not in out.stdout


def test_posix_ok_with_no_memory_files_warns(posix: Tree) -> None:
    linked = posix.run("link")
    assert linked.returncode == 0 and "never move, rename or delete" in linked.stdout
    out = posix.run("status")
    assert out.returncode == 0 and "(0 memory files)" in out.stdout
    assert "WARNING: no memory files" in out.stdout
    _write(posix.data / "memory" / "a.md")
    again = posix.run("status")
    assert "(1 memory files)" in again.stdout and "WARNING" not in again.stdout


def test_posix_cleanup_with_no_backups_is_a_no_op(posix: Tree) -> None:
    assert posix.run("link").returncode == 0
    out = posix.run("cleanup")
    assert out.returncode == 0 and "No backups to clean up" in out.stdout


def test_cleanup_refused_unless_status_is_ok(posix: Tree) -> None:
    harness = posix.harness()
    _write(harness / "s.jsonl")  # data still outside the project folder: not adopted
    backup = posix.home / ".claude" / "locality-backups" / f"{harness.name}.pre-locality-1"
    _write(backup / "s.jsonl")
    assert f"backup kept:   {backup}" in posix.run("status").stdout
    out = posix.run("cleanup")
    assert out.returncode == 1 and "cleanup refused" in out.stdout
    assert (backup / "s.jsonl").is_file()


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
    assert not list(harness.parent.glob(f"{harness.name}.pre-locality-*"))  # not beside the link
    backups = _backups(windows)
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
    assert _backups(windows) == []


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


def _adopt_with_session(windows: Tree) -> Path:
    harness = windows.harness()
    _write(harness / "memory" / "m1.md", "memory one", mtime=OLD)
    _write(harness / "s1.jsonl", "line1\n", mtime=OLD)
    out = windows.run("adopt")
    assert out.returncode == 0, out.stdout + out.stderr
    return harness


def test_windows_backup_goes_to_the_backup_root_not_beside_the_link(windows: Tree) -> None:
    harness = _adopt_with_session(windows)
    assert harness.is_symlink()
    assert not list(harness.parent.glob(f"{harness.name}.pre-locality-*"))
    backups = _backups(windows)
    assert len(backups) == 1 and (backups[0] / "s1.jsonl").is_file()
    assert f"backup kept:   {backups[0]}" in windows.run("status").stdout


def test_windows_adopt_output_points_to_cleanup_not_to_deleting(windows: Tree) -> None:
    harness = windows.harness()
    _write(harness / "s1.jsonl", mtime=OLD)
    out = windows.run("adopt").stdout
    assert "bash scripts/claude_project_data.sh cleanup" in out
    assert "delete it once" not in out
    assert "never move, rename or delete" in out


def test_windows_cleanup_removes_a_fully_covered_backup(windows: Tree) -> None:
    harness = _adopt_with_session(windows)
    with (windows.data / "s1.jsonl").open("a", encoding="utf-8") as fh:
        fh.write("line2\n")  # the resumed session grew its transcript
    out = windows.run("cleanup")
    assert out.returncode == 0 and "removed:" in out.stdout, out.stdout + out.stderr
    assert _backups(windows) == []
    assert (windows.data / "memory" / "m1.md").read_text(encoding="utf-8") == "memory one"
    assert (windows.data / "s1.jsonl").read_text(encoding="utf-8") == "line1\nline2\n"
    assert harness.is_symlink()


def test_windows_cleanup_keeps_a_backup_the_store_does_not_cover(windows: Tree) -> None:
    _adopt_with_session(windows)
    (windows.data / "memory" / "m1.md").unlink()  # the store lost a file the backup still has
    _write(windows.data / "s1.jsonl", "rewritten\n")  # and holds other bytes for another
    out = windows.run("cleanup")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "KEPT" in out.stdout
    assert "missing from the project folder: memory/m1.md" in out.stdout
    assert "differs from the project folder copy: s1.jsonl" in out.stdout
    backups = _backups(windows)
    assert len(backups) == 1 and (backups[0] / "memory" / "m1.md").is_file()


def test_cleanup_never_follows_a_link_inside_a_backup(windows: Tree) -> None:
    harness = _adopt_with_session(windows)
    trap = harness.parent / f"{harness.name}.pre-locality-20261006-093516"  # the v0.2 spot
    trap.mkdir()
    (trap / "memory").symlink_to(windows.data / "memory")  # a junction into the real store
    out = windows.run("cleanup")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "link (never followed): memory" in out.stdout
    assert (windows.data / "memory" / "m1.md").read_text(encoding="utf-8") == "memory one"
    assert not (windows.data / "memory").is_symlink()
    moved = windows.home / ".claude" / "locality-backups" / trap.name
    assert not trap.exists() and (moved / "memory").is_symlink()


def test_cleanup_keeps_a_backup_entry_that_is_itself_a_link(windows: Tree) -> None:
    harness = _adopt_with_session(windows)
    fake = harness.parent / f"{harness.name}.pre-locality-20261006-000000"
    fake.symlink_to(windows.data)  # what renaming a mis-detected junction would leave
    out = windows.run("cleanup")
    assert out.returncode == 0 and "KEPT (a link" in out.stdout, out.stdout + out.stderr
    assert fake.is_symlink() and (windows.data / "memory" / "m1.md").is_file()


def test_cleanup_handles_backups_left_beside_the_link_by_v02(windows: Tree) -> None:
    harness = _adopt_with_session(windows)
    covered = harness.parent / f"{harness.name}.pre-locality-20261006-093516"
    _write(covered / "s1.jsonl", "line1\n")
    unique = harness.parent / f"{harness.name}.pre-locality-20261006-101010"
    _write(unique / "only-here.jsonl", "unique")
    out = windows.run("cleanup")
    assert out.returncode == 0, out.stdout + out.stderr
    assert not covered.exists() and not unique.exists()
    assert "moved away from the link" in out.stdout
    moved = windows.home / ".claude" / "locality-backups" / unique.name
    assert (moved / "only-here.jsonl").read_text(encoding="utf-8") == "unique"
    assert [b.name for b in _backups(windows)] == [unique.name]
