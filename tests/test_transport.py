# ==============================================================
# VERSION: 0.4
# Unit tests for the pluggable target transports (local | git | ssh).
#
# CHANGE LOG
# v0.4 — 2026-10-12 — PLAN-019: _capture also records the env each command ran with; new tests —
#         git fail-fast ssh (every git command; the operator's GIT_SSH_COMMAND / core.sshCommand
#         kept as the base; legacy GIT_SSH left alone), rsync unchanged, the 300 s run cap.
# v0.3 — 2026-10-05 — PLAN-016 (D-4): ssh rsyncs carry the fail-fast remote shell
#         (`-e "ssh -o ConnectTimeout=10 -o BatchMode=yes"`); operand indices shift by 2.
# v0.2 — 2026-08-16 — PLAN-008: full=True sessions — git sparse set adds archive; ssh
#         materializes archive/ + root CLAUDE.md alongside docs/.
# v0.1 — 2026-06-20 — Initial: make_target dispatch + Local/Git/Ssh materialize/flush + _run errors.
# ==============================================================
"""Tests for standard_document_updater.transport."""
from __future__ import annotations

import subprocess
from collections.abc import Callable
from pathlib import Path

import pytest

from standard_document_updater import transport
from standard_document_updater.registry import Project


class _FakeProc:
    """Minimal stand-in for subprocess.CompletedProcess."""

    def __init__(self, returncode: int, stdout: str = "", stderr: str = "") -> None:
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def _capture(
    cmds: list[list[str]], envs: list[dict[str, str] | None] | None = None
) -> Callable[..., None]:
    """A drop-in for transport._run that records the argv (and env) it was called with."""

    def _fake(cmd: list[str], env: dict[str, str] | None = None) -> None:
        cmds.append(cmd)
        if envs is not None:
            envs.append(env)

    return _fake


# --- make_target dispatch (QA I) -------------------------------------------------

def test_make_target_local() -> None:
    t = transport.make_target(Project(name="a", path=Path("/x")))
    assert isinstance(t, transport.LocalTarget)


def test_make_target_git() -> None:
    t = transport.make_target(Project(name="b", transport="git", git_url="git@h:r.git"))
    assert isinstance(t, transport.GitTarget)


def test_make_target_ssh() -> None:
    t = transport.make_target(Project(name="c", transport="ssh", ssh_host="h", ssh_path="/p"))
    assert isinstance(t, transport.SshTarget)


def test_make_target_unknown_raises() -> None:
    with pytest.raises(transport.TransportError, match="unknown transport"):
        transport.make_target(Project(name="d", transport="bogus"))


# --- LocalTarget (QA J) ----------------------------------------------------------

def test_local_session_yields_path_in_place(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    t = transport.make_target(Project(name="a", path=repo))
    with t.session() as root:
        assert root == repo  # in place; no temp dir
    # flush + dispose are inherited no-ops — calling flush must not error or touch the repo
    t.flush(repo, [Path("docs/x.md")], "msg")
    assert repo.exists()


def test_local_missing_path_raises(tmp_path: Path) -> None:
    t = transport.make_target(Project(name="a", path=tmp_path / "nope"))
    with pytest.raises(transport.TransportError, match="path not found"):
        with t.session():
            pass


# --- GitTarget read/write/flush (QA K, L) ---------------------------------------

def test_git_read_materialize_is_shallow_blobless_sparse(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(
        Project(name="b", transport="git", git_url="git@h:r.git", git_branch="main")
    )
    with t.session():
        pass
    assert cmds[0][:2] == ["git", "clone"]
    assert "--depth" in cmds[0] and "--filter=blob:none" in cmds[0]
    assert "--no-checkout" in cmds[0] and "--branch" in cmds[0]
    assert cmds[1][3:] == ["sparse-checkout", "set", "docs"]
    assert cmds[2][3] == "checkout"


def test_git_read_full_sparse_includes_archive(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(Project(name="b", transport="git", git_url="git@h:r.git"))
    with t.session(full=True):
        pass
    assert cmds[1][3:] == ["sparse-checkout", "set", "docs", "archive"]


def test_ssh_full_materializes_archive_and_root_claude(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(
        Project(name="c", transport="ssh", ssh_host="devbox", ssh_path="/home/me/repo/")
    )
    with t.session(full=True) as root:
        assert cmds[0][4] == "devbox:/home/me/repo/docs/"
        assert cmds[1][4] == "devbox:/home/me/repo/archive/"
        assert cmds[1][5] == f"{root / 'archive'}/"
        assert cmds[2][4] == "devbox:/home/me/repo/CLAUDE.md"
        assert cmds[2][5] == f"{root / 'CLAUDE.md'}"


def test_git_write_materialize_is_full_clone(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(Project(name="b", transport="git", git_url="u", git_branch="main"))
    with t.session(writable=True):
        pass
    assert len(cmds) == 1  # one full clone; no sparse-checkout/checkout
    assert cmds[0][:2] == ["git", "clone"]
    assert "--no-checkout" not in cmds[0] and "--filter=blob:none" not in cmds[0]


def test_git_flush_commits_and_pushes(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(Project(name="b", transport="git", git_url="u", git_branch="main"))
    t.flush(Path("/root"), [Path("docs/STANDARDS_LOG.md")], "msg")
    assert cmds[0] == ["git", "-C", "/root", "add", "docs/STANDARDS_LOG.md"]
    assert "commit" in cmds[1] and "user.name=Standard DocSet" in cmds[1]
    assert cmds[2] == ["git", "-C", "/root", "push", "origin", "HEAD:main"]


def test_git_flush_default_branch_refspec(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(Project(name="b", transport="git", git_url="u"))  # no branch
    t.flush(Path("/root"), [Path("docs/x.md")], "msg")
    assert cmds[2] == ["git", "-C", "/root", "push", "origin", "HEAD"]


def test_git_missing_url_raises() -> None:
    t = transport.make_target(Project(name="b", transport="git"))  # git_url defaults to None
    with pytest.raises(transport.TransportError, match="missing git_url"):
        with t.session():
            pass


# --- SshTarget materialize/flush (QA M) -----------------------------------------

def test_ssh_materialize_rsyncs_docs_down(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(
        Project(name="c", transport="ssh", ssh_host="devbox", ssh_path="/home/me/repo/")
    )
    with t.session() as root:
        assert cmds[0][:4] == ["rsync", "-az", "-e", "ssh -o ConnectTimeout=10 -o BatchMode=yes"]
        assert cmds[0][4] == "devbox:/home/me/repo/docs/"
        assert cmds[0][5] == f"{root / 'docs'}/"


def test_ssh_flush_rsyncs_each_changed_file_up(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(
        Project(name="c", transport="ssh", ssh_host="devbox", ssh_path="/home/me/repo")
    )
    t.flush(Path("/tmp/x"), [Path("docs/STANDARDS_LOG.md")], "msg")
    assert cmds[0][:4] == ["rsync", "-az", "-e", "ssh -o ConnectTimeout=10 -o BatchMode=yes"]
    assert cmds[0][4] == str(Path("/tmp/x") / "docs/STANDARDS_LOG.md")
    assert cmds[0][5] == "devbox:/home/me/repo/docs/STANDARDS_LOG.md"


def test_ssh_missing_endpoint_raises() -> None:
    t = transport.make_target(Project(name="c", transport="ssh", ssh_host="h"))  # ssh_path None
    with pytest.raises(transport.TransportError, match="missing ssh_host or ssh_path"):
        with t.session():
            pass


# --- _run error handling ---------------------------------------------------------

def test_run_raises_on_nonzero_exit(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake(*args: object, **kwargs: object) -> _FakeProc:
        return _FakeProc(1, stderr="boom")

    monkeypatch.setattr(subprocess, "run", fake)
    with pytest.raises(transport.TransportError, match="boom"):
        transport._run(["git", "status"])


def test_run_ok_on_zero_exit(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake(*args: object, **kwargs: object) -> _FakeProc:
        return _FakeProc(0)

    monkeypatch.setattr(subprocess, "run", fake)
    transport._run(["true"])  # must not raise


def test_run_raises_when_binary_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    def boom(*args: object, **kwargs: object) -> _FakeProc:
        raise OSError("not found")

    monkeypatch.setattr(subprocess, "run", boom)
    with pytest.raises(transport.TransportError, match="could not run"):
        transport._run(["nonexistent-binary-xyz"])


# --- git fail-fast ssh + run cap (PLAN-019) ----------------------------------------

_FAIL_FAST = (
    "-o ConnectTimeout=10 -o BatchMode=yes -o ServerAliveInterval=10 -o ServerAliveCountMax=3"
)


def _git_session_envs(
    monkeypatch: pytest.MonkeyPatch, configured: str | None
) -> list[dict[str, str] | None]:
    """Run a git read session + a flush; return the env of every git command (6 commands)."""
    cmds: list[list[str]] = []
    envs: list[dict[str, str] | None] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds, envs))
    monkeypatch.setattr(transport, "_configured_ssh_command", lambda: configured)
    t = transport.make_target(Project(name="b", transport="git", git_url="u", git_branch="main"))
    with t.session():
        pass
    t.flush(Path("/root"), [Path("docs/x.md")], "msg")
    assert len(envs) == 6  # clone, sparse-checkout, checkout, add, commit, push
    return envs


def test_git_commands_run_fail_fast_ssh(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GIT_SSH_COMMAND", raising=False)
    monkeypatch.delenv("GIT_SSH", raising=False)
    for env in _git_session_envs(monkeypatch, None):
        assert env is not None
        assert env["GIT_SSH_COMMAND"] == f"ssh {_FAIL_FAST}"


def test_git_ssh_keeps_operator_env_command(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GIT_SSH_COMMAND", "/opt/ssh -i key")
    for env in _git_session_envs(monkeypatch, "ignored-config"):  # env beats config, as in git
        assert env is not None
        assert env["GIT_SSH_COMMAND"] == f"/opt/ssh -i key {_FAIL_FAST}"


def test_git_ssh_keeps_operator_core_sshcommand(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GIT_SSH_COMMAND", raising=False)
    monkeypatch.setenv("GIT_SSH", "/opt/legacy")  # core.sshCommand beats GIT_SSH, as in git
    for env in _git_session_envs(monkeypatch, "C:/Windows/System32/OpenSSH/ssh.exe"):
        assert env is not None
        assert env["GIT_SSH_COMMAND"] == f"C:/Windows/System32/OpenSSH/ssh.exe {_FAIL_FAST}"


def test_git_legacy_git_ssh_left_alone(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GIT_SSH_COMMAND", raising=False)
    monkeypatch.setenv("GIT_SSH", "/opt/legacy")
    assert _git_session_envs(monkeypatch, None) == [None] * 6  # inherit; the run cap still applies


def test_configured_ssh_command_reads_git_config(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: list[list[str]] = []

    def fake(cmd: list[str], **kwargs: object) -> _FakeProc:
        seen.append(cmd)
        return _FakeProc(0, stdout="/opt/ssh -F cfg\n")

    monkeypatch.setattr(subprocess, "run", fake)
    assert transport._configured_ssh_command() == "/opt/ssh -F cfg"
    assert seen == [["git", "config", "--get", "core.sshCommand"]]


def test_configured_ssh_command_unset_is_none(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake(*args: object, **kwargs: object) -> _FakeProc:
        return _FakeProc(1)  # git config --get: exit 1 when the key is unset

    monkeypatch.setattr(subprocess, "run", fake)
    assert transport._configured_ssh_command() is None


def test_rsync_commands_keep_inherited_env(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    envs: list[dict[str, str] | None] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds, envs))
    t = transport.make_target(Project(name="c", transport="ssh", ssh_host="h", ssh_path="/p"))
    with t.session():
        pass
    assert envs == [None]  # rsync carries its own `-e ssh ...`; no git env


def test_run_passes_cap_and_env(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: dict[str, object] = {}

    def fake(cmd: list[str], **kwargs: object) -> _FakeProc:
        seen.update(kwargs)
        return _FakeProc(0)

    monkeypatch.setattr(subprocess, "run", fake)
    transport._run(["true"], {"K": "V"})
    assert seen["timeout"] == 300 and seen["env"] == {"K": "V"}


def test_run_raises_on_timeout(monkeypatch: pytest.MonkeyPatch) -> None:
    def slow(cmd: list[str], **kwargs: object) -> _FakeProc:
        raise subprocess.TimeoutExpired(cmd, 300)

    monkeypatch.setattr(subprocess, "run", slow)
    with pytest.raises(transport.TransportError, match="timed out after 300 s"):
        transport._run(["git", "clone", "u", "d"])
