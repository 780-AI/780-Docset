# ==============================================================
# VERSION: 0.3
# Unit tests for the pluggable target transports (local | git | ssh).
#
# CHANGE LOG
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


def _capture(cmds: list[list[str]]) -> Callable[[list[str]], None]:
    """A drop-in for transport._run that records the argv it was called with."""

    def _fake(cmd: list[str]) -> None:
        cmds.append(cmd)

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
