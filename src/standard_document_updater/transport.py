# ==============================================================
# VERSION: 0.2
# Pluggable target transports (local | git | ssh): materialize -> operate -> flush.
#
# CHANGE LOG
# v0.2 — 2026-08-16 — PLAN-008 (sync): sessions grow a `full` scope — full=True materializes the
#         whole sync footprint (docs/ + archive/ + root CLAUDE.md); git read path adds `archive`
#         to the sparse set (cone mode already includes root files); ssh adds two rsyncs.
# v0.1 — 2026-06-20 — Initial: Target ABC + Local/Git/Ssh drivers + make_target.
# ==============================================================
"""Reach a target repo wherever it lives, keeping the engine transport-agnostic.

D1 (materialize-to-local-root): each Target fetches the target repo to a local
root; the engine performs its existing Path-based I/O against that root; on the
write path the Target flushes the changes back to the source.

Transports (chosen per-target in config/projects.toml):
  local — a folder on this machine (default; reads/writes happen in place).
  git   — clone/fetch from a forge remote over SSH; write-back = commit + push (D2/D5).
  ssh   — rsync from a remote host; write-back = rsync the changed files back.
"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from abc import ABC, abstractmethod
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from standard_document_updater.errors import StandardDocSetError
from standard_document_updater.registry import Project

_DOCS = "docs"        # the subtree status/drift/harvest/integrate touch (full=False sessions)
_ARCHIVE = "archive"  # + root CLAUDE.md: the wider footprint `sync` needs (full=True sessions)
_ROOT_FILE = "CLAUDE.md"
_COMMIT_NAME = "Standard DocSet"
_COMMIT_EMAIL = "standard-docset@localhost"


class TransportError(StandardDocSetError):
    """A transport operation (clone / fetch / push / rsync) failed."""


def _run(cmd: list[str]) -> None:
    """Run a subprocess; raise TransportError with captured output on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except OSError as exc:  # the binary is missing / not executable
        raise TransportError(f"could not run {cmd[0]}: {exc}") from exc
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()
        raise TransportError(f"{' '.join(cmd)} failed (exit {proc.returncode}): {detail}")


class Target(ABC):
    """A managed repo reachable through some transport. Materialize -> operate -> flush."""

    def __init__(self, project: Project) -> None:
        self.project = project

    @property
    def name(self) -> str:
        return self.project.name

    @property
    def location(self) -> str:
        return self.project.location

    @contextmanager
    def session(self, *, writable: bool = False, full: bool = False) -> Iterator[Path]:
        """Yield a local repo root for the target; clean up any temp copy on exit.

        full=True materializes the whole sync footprint (docs/ + archive/ + root
        CLAUDE.md) instead of docs/ only — required by `sync`, whose targets
        include files outside docs/.
        """
        root = self._materialize(writable=writable, full=full)
        try:
            yield root
        finally:
            self._dispose(root)

    @abstractmethod
    def _materialize(self, *, writable: bool, full: bool) -> Path:
        """Fetch the repo to a local root (in place for local; a temp dir otherwise)."""

    def flush(self, root: Path, changed: list[Path], message: str) -> None:  # noqa: B027
        """Push changed files (repo-relative) back to the source. No-op default (local)."""

    def _dispose(self, root: Path) -> None:  # noqa: B027
        """Remove a temporary materialization. No-op default (in-place local root)."""


class LocalTarget(Target):
    """A repo that is a folder on this machine. Reads and writes happen in place."""

    def _materialize(self, *, writable: bool, full: bool) -> Path:
        path = self.project.path
        if path is None or not path.exists():
            raise TransportError(f"local target {self.name!r}: path not found: {path}")
        return path


class GitTarget(Target):
    """A repo fetched from a forge remote over SSH. Write-back = direct push (D2/D5)."""

    def _materialize(self, *, writable: bool, full: bool) -> Path:
        url = self.project.git_url
        if not url:
            raise TransportError(f"git target {self.name!r}: missing git_url")
        branch = self.project.git_branch
        dest = Path(tempfile.mkdtemp(prefix="stddocset-git-"))
        base = ["git", "clone", "--depth", "1"]
        if branch:
            base += ["--branch", branch]
        if writable:  # full branch tip so a commit can be pushed
            _run([*base, url, str(dest)])
        else:  # read path: shallow + blobless + sparse (D4); cone mode keeps root files
            _run([*base, "--filter=blob:none", "--no-checkout", url, str(dest)])
            sparse = [_DOCS, _ARCHIVE] if full else [_DOCS]
            _run(["git", "-C", str(dest), "sparse-checkout", "set", *sparse])
            _run(["git", "-C", str(dest), "checkout"])
        return dest

    def flush(self, root: Path, changed: list[Path], message: str) -> None:
        rels = [p.as_posix() for p in changed]
        _run(["git", "-C", str(root), "add", *rels])
        _run([
            "git", "-C", str(root),
            "-c", f"user.name={_COMMIT_NAME}", "-c", f"user.email={_COMMIT_EMAIL}",
            "commit", "-m", message,
        ])
        branch = self.project.git_branch
        refspec = f"HEAD:{branch}" if branch else "HEAD"
        _run(["git", "-C", str(root), "push", "origin", refspec])

    def _dispose(self, root: Path) -> None:
        shutil.rmtree(root, ignore_errors=True)


class SshTarget(Target):
    """A repo on a remote host reached via rsync over SSH. Only docs/ is materialized."""

    def _materialize(self, *, writable: bool, full: bool) -> Path:
        host, base = self._endpoint()
        dest = Path(tempfile.mkdtemp(prefix="stddocset-ssh-"))
        (dest / _DOCS).mkdir(parents=True, exist_ok=True)
        _run(["rsync", "-az", f"{host}:{base}/{_DOCS}/", f"{dest / _DOCS}/"])
        if full:  # the sync footprint reaches outside docs/ — hard-fail if absent
            (dest / _ARCHIVE).mkdir(parents=True, exist_ok=True)
            _run(["rsync", "-az", f"{host}:{base}/{_ARCHIVE}/", f"{dest / _ARCHIVE}/"])
            _run(["rsync", "-az", f"{host}:{base}/{_ROOT_FILE}", f"{dest / _ROOT_FILE}"])
        return dest

    def flush(self, root: Path, changed: list[Path], message: str) -> None:
        host, base = self._endpoint()
        for rel in changed:
            _run(["rsync", "-az", str(root / rel), f"{host}:{base}/{rel.as_posix()}"])

    def _endpoint(self) -> tuple[str, str]:
        host = self.project.ssh_host
        path = self.project.ssh_path
        if not host or not path:
            raise TransportError(f"ssh target {self.name!r}: missing ssh_host or ssh_path")
        return host, path.rstrip("/")

    def _dispose(self, root: Path) -> None:
        shutil.rmtree(root, ignore_errors=True)


_DRIVERS: dict[str, type[Target]] = {
    "local": LocalTarget,
    "git": GitTarget,
    "ssh": SshTarget,
}


def make_target(project: Project) -> Target:
    """Build the Target driver for a project's declared transport."""
    driver = _DRIVERS.get(project.transport)
    if driver is None:
        raise TransportError(
            f"project {project.name!r}: unknown transport {project.transport!r} "
            f"(expected one of: {', '.join(sorted(_DRIVERS))})"
        )
    return driver(project)
