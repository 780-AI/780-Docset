<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-06-20 -->
<!-- Status: DRAFT -->
<!--
CHANGE LOG
v0.1a — 2026-06-20 — Rule 13 senior-review pass (last task of Phase 1; per L051 the tools were ACTUALLY
RUN, not eyeballed). The § 5 code was materialized in src/ + a real tests/test_transport.py written, then
`ruff check`, `mypy --strict` (MYPYPATH=src), and `pytest` were run, then the scratch was removed. Named
findings, all fixed in § 5: ruff E501 ×2 in § 5C (the `projects = [...]` line and the `message = f"…"`
line, both 101 > 100) → reflowed via a `registry_path` local + a `count` local; ruff B027 ×2 on the § 5A
`Target.flush` / `Target._dispose` no-op ABC hooks → annotated `# noqa: B027` (intentional concrete
no-op defaults, overridden by git/ssh); ruff I001 (import-block spacing in § 5B registry.py) →
auto-fixed; ruff E501 ×2 + a `no_implicit_reexport` issue in the new test (shortened the CHANGE-LOG line
+ the `GitTarget(Project(...))` line; switched the subprocess monkeypatch to the string-target form);
the `_run`-failure test was rewritten to monkeypatch `subprocess.run` (the prior real-git command was
unreliable). Two process slips of my own, corrected: mypy was first mis-invoked without `MYPYPATH=src`
(QA B in § 8 now states it), and a stale `.mypy_cache` produced phantom test-file errors (cleared → clean).
Final: ruff clean; mypy --strict 0 issues across 20 files; 71 tests pass (57 prior + 14 new). No new design
decision beyond D1–D4 / DD-1…DD-6. Plan finalized → ready for Phase 2.
v0.1 — 2026-06-20 — Initial DRAFT. Phase 0 (Audit) + Phase 1 (Design) for the remote-target transport
layer. Operator decisions settled: D1 = materialize-to-local-root; D2 = git write-back is a direct push;
D3 = all commands transport-aware in one plan; D4 = git read fetch is shallow + blobless + sparse docs/.
Sibling tracker: PLAN-007_tracker.md.
-->

# PLAN-007 — Remote-target transport (local | git | ssh)

> **Type:** Major / new engine module (`src/standard_document_updater/`, a Critical File per § 4) + a
> registry-schema change + edits to `CLAUDE.md` § 1 (Critical File). Runs under the § 15 plan workflow.
> **Sibling tracker:** [`PLAN-007_tracker.md`](PLAN-007_tracker.md).
> **Operator decisions settled:** D1 = materialize-to-local-root; D2 = git direct push; D3 = all-at-once;
> D4 = shallow + blobless + sparse `docs/` git read fetch.
> **Numbering note:** this plan is the **remote transport** (a scope expansion the operator sequenced on
> 2026-06-18, ahead of `sync`). `architecture.md` § 10 still calls PLAN-007 "`sync`" — that is stale and
> is corrected by this plan; `sync` becomes **PLAN-008**.

---

## 1. Goal

Give the engine a **pluggable transport layer** so it can operate on a target repo wherever it lives —
a local folder (today's behavior), a forge remote reached over SSH (`git`), or a dev host reached over
SSH (`ssh`/rsync) — **without standing up any server and without permanently cloning every org repo**.

The engine stays **transport-agnostic** (D1, materialize-to-local-root): each target is *materialized* to
a local root, the engine performs its existing `root / "docs" / …` Path-based I/O against that root, and
on the write path the transport *flushes* the change back to the source. All four existing commands
(`status` / `drift` / `harvest` / `integrate`) become transport-aware in this one plan (D3).

## 2. Operator constraints & decisions settled

- **D1 — abstraction model:** *materialize-to-local-root.* A `Target` fetches the repo to a local root;
  the engine keeps its current Path-based reads/writes against that root; the transport flushes writes
  back. Chosen for minimal blast radius and because it scales to `sync`'s many-file writes (PLAN-008).
- **D2 — git write-back:** *direct push* to the target branch (needs only `git`, which is present).
  `glab`/`gh` are **not** installed; the merge-request variant is recorded as a documented future option
  (DD-6), not built here.
- **D3 — scope:** *all-at-once* — every command is transport-aware in this plan.
- **D4 — git read fetch:** *shallow + blobless + sparse `docs/`* (`--depth 1 --filter=blob:none` +
  `sparse-checkout set docs`). The write path materializes the full branch tip (depth 1) so a commit can
  be pushed.

### 2.1 New design decisions exposed by the audit — for Phase-2 confirmation (per § 10 / Rule 13.5)

- **DD-1 — Registry schema = per-target `transport` key**, defaulting to `local` (full back-compat: an
  entry with just `name` + `path` keeps working). Shape:
  ```toml
  [[project]]                       # local (default; transport key optional)
  name = "alpha"
  path = "/Users/me/Documents/alpha"

  [[project]]
  name = "beta"
  transport = "git"
  git_url = "git@gitlab.com:org/beta.git"
  git_branch = "main"               # optional; empty → the remote's default branch

  [[project]]
  name = "gamma"
  transport = "ssh"
  ssh_host = "devbox"               # an ssh alias or user@host
  ssh_path = "/home/me/gamma"
  ```
- **DD-2 — The transport seam is `cli.py` only.** The read/write *functions* (`parse_log`,
  `parse_adopted_version`, `count_open_log_entries`, `apply_writeback`) stay **Path-based and unchanged**;
  `cli.py` materializes each target to a root and builds the `docs/…` paths under it. This is why
  `integrate.apply_writeback` keeps its signature and its 20 tests stay valid (audit-confirmed: every
  target read/write derives from `project.path` at cli.py:37-38, 62, 86-87 only).
- **DD-3 — Per-target transport failure is non-fatal for read commands.** `status` / `drift` show an
  unreachable target as `unknown` with the error note (matching report.py's "never raises on a bad
  target" contract); `harvest` / `integrate` (worksheet) emit a stderr warning and skip the target,
  preserving their always-exit-0 behavior. A transport failure on the **write** path is fatal for that
  run (a write must be loud), but because all targets are materialized + validated *before* any push,
  a fetch failure aborts before anything is written.
- **DD-4 — Write-back is per-target atomic, not cross-target atomic.** True atomicity across N independent
  remotes is impossible. `cli` materializes every named target and `apply_writeback` validates **every**
  disposition before **any** write (so a validation error writes nothing — unchanged guarantee). Pushes
  then happen per target; a mid-sequence push failure leaves earlier targets pushed and is reported
  loudly (no silent partial success).
- **DD-5 — git direct push is fast-forward only.** A shallow clone of the branch tip + one commit on top
  + `git push origin HEAD:<branch>` (no `--force`). A non-fast-forward (someone pushed meanwhile) fails
  loudly as a `TransportError`; nothing is silently lost. Commit identity is a fixed
  `Standard DocSet <standard-docset@localhost>` passed via `-c` (never mutates the target's git config).
  Credentials are the operator's existing SSH agent/keys — the tool never handles secrets.
- **DD-6 — Building the transport is read-only on the vault → NO Set-Version bump** (same as
  PLAN-003/004/006). It is engine code; it edits **no** `docs/standards/` file. It *does* edit the root
  `CLAUDE.md` § 1 (an adopter copy, PROJECT-OWNED) to retire "operates on local repository checkouts /
  no remote infrastructure" — a project-specific edit that does not touch the canonical suite.
- **DD-6b (future, NOT built) — git merge-request write-back** via `glab`/`gh` (your memory's
  "push-back = reviewable MR"). Deferred: needs the binary + auth. Recorded so a later plan can add a
  `git_writeback = "push" | "mr"` key without re-litigating.

## 3. Scope summary

**In scope:** a new `transport.py` (the `Target` ABC + `LocalTarget` / `GitTarget` / `SshTarget` drivers +
`make_target` + `TransportError`); `registry.py` (grow `Project` with `transport` + per-transport
connection fields; validate per transport); `cli.py` (materialize each target via `make_target` +
`session()`; `ExitStack` for the multi-target write path; graceful per-target failure per DD-3);
`report.py` (`location` display + an `unreachable_status` helper; table column `PATH` → `LOCATION`);
tests (`test_transport.py` new + registry/cli/report updates, git/ssh exercised via mocked subprocess);
`config/projects.toml` (git/ssh example comments); `CLAUDE.md` § 1 (retire "no remote infra");
`architecture.md` (§ 1/§ 8/§ 9/§ 10/§ 11); `validation_ownership.toml` (soft `[rules.transport]`);
manifest/folder_structure/CHANGELOG sync; promote PLAN-007 + tracker to 1.0/CLOSED in the Phase-3 commit.

**Out of scope:** `sync` (now PLAN-008 — section-aware propagation; benefits from this transport); the
merge-request write-back (DD-6b); fetching anything beyond `docs/` (the four current commands only touch
`docs/` — `sync` may widen the materialization later); any model call; any vault edit; **no Set-Version
bump** (DD-6).

## 4. Phase tracker (high-level — granular sub-tasks in `PLAN-007_tracker.md`)

| Phase | Status | Date |
|---|---|---|
| 0 — Audit | ✅ done | 2026-06-20 |
| 1 — Design (this plan + tracker) | ✅ done | 2026-06-20 |
| 1.x — Rule 13 senior-review pass (runs ruff + mypy --strict + pytest on the § 5 code, per L051) | ✅ done | 2026-06-20 |
| 2 — Operator approval | ⏸ pending | — |
| 3 — Implement (fresh session, ALLOWLIST-bounded) | ⏸ pending | — |
| 4 — Validate (QA A–N + governance) | ⏸ pending | — |
| 5 — Operator gate (push; no tag — Set Version unchanged) | ⏸ pending | — |

## 5. Verbatim module spec (Phase 3)

> Implement these byte-for-byte (Rule 7). Code below was materialized in `src/` and run through
> `ruff check` + `mypy --strict` + `pytest` during the Phase-1 Rule 13 pass (per L051) — see the CHANGE
> LOG for what that run found and fixed.

### 5A — `src/standard_document_updater/transport.py` (NEW)

```python
# ==============================================================
# VERSION: 0.1
# Pluggable target transports (local | git | ssh): materialize -> operate -> flush.
#
# CHANGE LOG
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

_DOCS = "docs"  # the only subtree the current commands touch (status/drift/harvest/integrate)
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
    def session(self, *, writable: bool = False) -> Iterator[Path]:
        """Yield a local repo root for the target; clean up any temp copy on exit."""
        root = self._materialize(writable=writable)
        try:
            yield root
        finally:
            self._dispose(root)

    @abstractmethod
    def _materialize(self, *, writable: bool) -> Path:
        """Fetch the repo to a local root (in place for local; a temp dir otherwise)."""

    def flush(self, root: Path, changed: list[Path], message: str) -> None:  # noqa: B027
        """Push changed files (repo-relative) back to the source. No-op default (local)."""

    def _dispose(self, root: Path) -> None:  # noqa: B027
        """Remove a temporary materialization. No-op default (in-place local root)."""


class LocalTarget(Target):
    """A repo that is a folder on this machine. Reads and writes happen in place."""

    def _materialize(self, *, writable: bool) -> Path:
        path = self.project.path
        if path is None or not path.exists():
            raise TransportError(f"local target {self.name!r}: path not found: {path}")
        return path


class GitTarget(Target):
    """A repo fetched from a forge remote over SSH. Write-back = direct push (D2/D5)."""

    def _materialize(self, *, writable: bool) -> Path:
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
        else:  # read path: shallow + blobless + sparse docs/ only (D4)
            _run([*base, "--filter=blob:none", "--no-checkout", url, str(dest)])
            _run(["git", "-C", str(dest), "sparse-checkout", "set", _DOCS])
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

    def _materialize(self, *, writable: bool) -> Path:
        host, base = self._endpoint()
        dest = Path(tempfile.mkdtemp(prefix="stddocset-ssh-"))
        (dest / _DOCS).mkdir(parents=True, exist_ok=True)
        _run(["rsync", "-az", f"{host}:{base}/{_DOCS}/", f"{dest / _DOCS}/"])
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
```

### 5B — `src/standard_document_updater/registry.py` (Project grows transport fields; 0.1 → 0.2)

Replace the `Project` dataclass and the per-entry build loop. Keep `load_registry`'s outer shape
(missing/malformed file handling) intact.

```python
# (header) bump VERSION 0.1 -> 0.2; add CHANGE LOG line:
# v0.2 — 2026-06-20 — Project grows a per-target transport (local | git | ssh) + connection fields;
#                     load_registry validates the fields required by each transport (PLAN-007).

_VALID_TRANSPORTS = ("local", "git", "ssh")


@dataclass(frozen=True)
class Project:
    """A managed project: name + transport + the connection fields for that transport."""

    name: str
    transport: str = "local"
    path: Path | None = None        # local
    git_url: str | None = None      # git
    git_branch: str = ""            # git (empty -> the remote's default branch)
    ssh_host: str | None = None     # ssh
    ssh_path: str | None = None     # ssh

    @property
    def location(self) -> str:
        """Human-readable location for the report table."""
        if self.transport == "git":
            branch = f"@{self.git_branch}" if self.git_branch else ""
            return f"git:{self.git_url}{branch}"
        if self.transport == "ssh":
            return f"ssh:{self.ssh_host}:{self.ssh_path}"
        return str(self.path) if self.path is not None else "(no path)"


def _require(entry: dict[str, object], key: str, name: str) -> str:
    value = entry.get(key)
    if not isinstance(value, str) or not value.strip():
        raise RegistryError(f"project '{name}': missing a non-empty '{key}'")
    return value


def _build_project(name: str, transport: str, entry: dict[str, object]) -> Project:
    if transport == "local":
        return Project(name=name, path=Path(_require(entry, "path", name)).expanduser())
    if transport == "git":
        branch = entry.get("git_branch", "")
        if not isinstance(branch, str):
            raise RegistryError(f"project '{name}': 'git_branch' must be a string")
        return Project(
            name=name, transport="git", git_url=_require(entry, "git_url", name), git_branch=branch
        )
    if transport == "ssh":
        return Project(
            name=name,
            transport="ssh",
            ssh_host=_require(entry, "ssh_host", name),
            ssh_path=_require(entry, "ssh_path", name),
        )
    raise RegistryError(
        f"project '{name}': unknown transport '{transport}' "
        f"(expected one of: {', '.join(_VALID_TRANSPORTS)})"
    )
```

And the loop body inside `load_registry` (replacing the current name/path extraction at lines 49-58):

```python
    projects: list[Project] = []
    for index, entry in enumerate(raw_projects, start=1):
        if not isinstance(entry, dict):
            raise RegistryError(f"project #{index} is not a table")
        name = entry.get("name")
        if not isinstance(name, str) or not name.strip():
            raise RegistryError(f"project #{index} is missing a non-empty 'name'")
        transport = entry.get("transport", "local")
        if not isinstance(transport, str):
            raise RegistryError(f"project '{name}': 'transport' must be a string")
        projects.append(_build_project(name, transport, entry))
    return projects
```

### 5C — `src/standard_document_updater/cli.py` (materialize via transport; 0.3 → 0.4)

Add imports:
```python
from contextlib import ExitStack
from standard_document_updater.transport import TransportError, make_target
```

`_build_statuses` — materialize each target, read inside the session, fail gracefully (DD-3):
```python
def _build_statuses(vault_root: Path) -> list[report.ProjectStatus]:
    index_path = vault_root / "docs" / "standards" / "STANDARDS_INDEX.md"
    registry_path = vault_root / "config" / "projects.toml"
    vault_version = setversion.parse_vault_version(index_path)
    statuses: list[report.ProjectStatus] = []
    for project in load_registry(registry_path):
        try:
            with make_target(project).session() as root:
                adopted_path = root / "docs" / "SET_VERSION_ADOPTED.md"
                log_path = root / "docs" / "STANDARDS_LOG.md"
                statuses.append(report.compute_status(project, vault_version, adopted_path, log_path))
        except TransportError as exc:
            statuses.append(report.unreachable_status(project, vault_version, str(exc)))
    return statuses
```

`_build_open_items` — materialize each target; skip-with-warning on transport failure (DD-3):
```python
def _build_open_items(vault_root: Path) -> list[harvest.OpenItem]:
    registry_path = vault_root / "config" / "projects.toml"
    items: list[harvest.OpenItem] = []
    for project in load_registry(registry_path):
        try:
            with make_target(project).session() as root:
                log_path = root / "docs" / "STANDARDS_LOG.md"
                for entry in logentry.parse_log(log_path):
                    if entry.is_open:
                        items.append(harvest.OpenItem(project.name, entry))
        except TransportError as exc:
            print(f"warning: skipping {project.name!r}: {exc}", file=sys.stderr)
    return items
```

`_cmd_integrate` write-back path — materialize every named target, validate-all then write, then flush
each (per-target atomic, DD-4). Replace lines 84-92:
```python
    # write-back path
    dispositions = integrate.parse_decisions(args.apply)
    named = {d.project for d in dispositions}
    registry_path = vault_root / "config" / "projects.toml"
    projects = [p for p in load_registry(registry_path) if p.name in named]
    with ExitStack() as stack:
        targets = {p.name: make_target(p) for p in projects}
        roots = {name: stack.enter_context(t.session(writable=True)) for name, t in targets.items()}
        log_path_for = {name: root / "docs" / "STANDARDS_LOG.md" for name, root in roots.items()}
        report_lines = integrate.apply_writeback(dispositions, log_path_for, write=args.write)
        if args.write:
            count = len(dispositions)
            message = f"Standard DocSet: integrate write-back ({count} status update(s))"
            for name in sorted(named & set(targets)):
                targets[name].flush(roots[name], [Path("docs/STANDARDS_LOG.md")], message)
    print("\n".join(report_lines))
    return 0
```
(`apply_writeback` still raises `IntegrateError` for a disposition whose project is absent from
`log_path_for` — i.e. named but not registered — exactly as today, before any write/flush.)

### 5D — `src/standard_document_updater/report.py` (location display + unreachable helper; 0.1 → 0.2)

```python
# (header) bump VERSION 0.1 -> 0.2; CHANGE LOG:
# v0.2 — 2026-06-20 — Table column PATH -> LOCATION (transport-aware); add unreachable_status() for
#                     targets a transport cannot reach (PLAN-007).

def unreachable_status(
    project: Project, vault: tuple[int, ...], note: str
) -> ProjectStatus:
    """A status row for a target the transport could not reach (read path, DD-3)."""
    return ProjectStatus(project, None, vault, State.UNKNOWN, 0, note)
```

In `render_table`, change the header and the location cell:
```python
    headers = ["PROJECT", "LOCATION", "ADOPTED", "VAULT", "STATE", "OPEN LOG"]
    rows = [
        [
            s.project.name,
            s.project.location,           # was: str(s.project.path)
            _fmt_version(s.adopted),
            _fmt_version(s.vault),
            s.state.value,
            str(s.open_entries),
        ]
        for s in statuses
    ]
```

### 5E — Tests (new `tests/test_transport.py` + updates)

- **`tests/test_transport.py` (NEW):** `make_target` returns the right driver per transport + raises
  `TransportError` on an unknown transport; `LocalTarget.session()` yields `project.path` **in place**
  (no temp dir created) and `flush`/`_dispose` are no-ops; `LocalTarget` on a missing path raises
  `TransportError`; `GitTarget._materialize` (read) issues `clone --depth 1 --filter=blob:none
  --no-checkout` + `sparse-checkout set docs` + `checkout` (assert via a `monkeypatch` of
  `transport._run` capturing the command list); `GitTarget.flush` issues `add` + `commit -c …` +
  `push origin HEAD:<branch>`; `SshTarget._materialize`/`flush` issue the expected `rsync` commands;
  `_run` raises `TransportError` on non-zero exit (use a trivial failing command like
  `["git", "rev-parse", "--bogus-flag"]` or monkeypatch `subprocess.run`).
- **`tests/test_registry.py`:** add cases — a `git` table parses into `Project(transport="git",
  git_url=…, git_branch=…)`; an `ssh` table parses host+path; a `local`/bare table still parses (default
  transport); each transport missing a required field raises `RegistryError`; unknown transport raises.
  Keep the existing local cases green (back-compat).
- **`tests/test_cli.py`:** `status` over a `git` target with `transport._run` monkeypatched to populate a
  fake materialization → row computed; an **unreachable** git target (monkeypatched `_run` raising) →
  the row shows `unknown` + does not abort the report; `integrate --apply --write` to a local fixture
  still writes (unchanged path); write-back dry-run still writes nothing.
- **`tests/test_report.py`:** assert the header now reads `LOCATION`; a git `Project`'s row shows the
  `git:…` descriptor; `unreachable_status` yields `State.UNKNOWN`.

## 6. Spec update map

| Spec / doc | Update | Trigger |
|---|---|---|
| `CLAUDE.md` § 1 | retire "operates on local repository checkouts / no remote infrastructure" → "local **or** remote (git/ssh) checkouts via a pluggable transport; still no server/deploy infra of its own" | Critical-File behavior change |
| `architecture.md` § 1 | same retirement (design-doc mirror) | § 4 drift rule |
| `architecture.md` § 8 | registry + commands are transport-aware (local/git/ssh) | engine behavior added |
| `architecture.md` § 9 | "read before write" = fetch-fresh materialization + per-target atomic write-back/push | engine behavior added |
| `architecture.md` § 10 | this slice = **PLAN-007 transport**; `sync` → **PLAN-008**; fix the stale numbering note | scope/numbering correction |
| `architecture.md` § 11 | record DD-1…DD-6 as decided | § 10 never-assume audit trail |
| `config/projects.toml` | add `git`/`ssh` example tables in the header comment | new schema (now a Critical File) |
| `validation_ownership.toml` | soft `[rules.transport]` | new src module |
| `documents_manifest.md` | register `transport.py` + `test_transport.py`; bump touched cells; plan promotion; header | Rule 8 |
| `folder_structure.md` | add `transport.py` + `test_transport.py` | new tracked files |
| `CHANGELOG.md` | top entry + QA sub-section | every behavior change (Rule 11) |

**No `docs/standards/` edit and NO Set-Version bump (DD-6).** The root `CLAUDE.md` + `architecture.md`
edits are project-specific (the canonical suite/template is untouched).

## 7. ALLOWLIST (Phase 3 — the bullet enumeration IS the count: 18 tracked)

1. `src/standard_document_updater/transport.py` (new) [5A]
2. `src/standard_document_updater/registry.py` (Project + validation; 0.1→0.2) [5B]
3. `src/standard_document_updater/cli.py` (materialize via transport; 0.3→0.4) [5C]
4. `src/standard_document_updater/report.py` (location + unreachable_status; 0.1→0.2) [5D]
5. `src/standard_document_updater/__init__.py` (0.3→0.4)
6. `tests/test_transport.py` (new) [5E]
7. `tests/test_registry.py` (transport parse cases) [5E]
8. `tests/test_cli.py` (transport-aware; mocked git/ssh) [5E]
9. `tests/test_report.py` (LOCATION header / location cell) [5E]
10. `scripts/validation_ownership.toml` (soft `[rules.transport]`)
11. `config/projects.toml` (git/ssh example comments)
12. `CLAUDE.md` (§ 1 deployment-shape tweak; version bump)
13. `docs/architecture.md` (§ 1/§ 8/§ 9/§ 10/§ 11 + header)
14. `docs/documents_manifest.md` (register + cells + plan promotion + header)
15. `docs/folder_structure.md` (tree + header)
16. `CHANGELOG.md` (top entry + QA sub-section)
17. `docs/Plans/PLAN-007_remote_transport.md` (this plan → 1.0/CLOSED)
18. `docs/Plans/PLAN-007_tracker.md` (→ 1.0/CLOSED)

(`errors.py` is **not** touched — `TransportError` lives in `transport.py` per § 5A. `OPEN_TASKS.md` is
gitignored — edited, not staged.) Anything else staged → STOP and report (Rule 7).

## 8. Validation gate (Phase 4 — QA scenarios per Rule 11)

| ID | Verify | How | Pass |
|---|---|---|---|
| A | ruff clean | `.venv/bin/ruff check src tests` | exit 0 |
| B | mypy --strict clean | `MYPYPATH=src .venv/bin/python -m mypy` | 0 issues |
| C | full test suite | `.venv/bin/python -m pytest -q` | all green (57 prior + new) |
| D | governance | both Rule-2 scripts | exit 0 |
| E | local back-compat | existing local project: `status` / `harvest` / `integrate` | output identical to pre-PLAN-007 except the column header `PATH`→`LOCATION` |
| F | registry parse — git | a `[[project]] transport="git"` table | `Project(transport="git", git_url=…, git_branch=…)`; `location` = `git:…` |
| G | registry parse — ssh | an `ssh` table | host+path parsed; `location` = `ssh:host:path` |
| H | registry validation | each transport missing a required field; unknown transport | `RegistryError` naming the field/transport |
| I | `make_target` dispatch | one Project per transport + a bogus transport | right driver; bogus → `TransportError` |
| J | local materialize in place | `LocalTarget.session()` | yields `project.path`; no temp dir; flush/dispose no-op |
| K | git read fetch | monkeypatch `transport._run`, capture cmds | `clone --depth 1 --filter=blob:none --no-checkout` + `sparse-checkout set docs` + `checkout` |
| L | git push write-back | monkeypatched `_run` | `add` + `commit -c user.name/email` + `push origin HEAD:<branch>` |
| M | ssh rsync | monkeypatched `_run` | down: `rsync -az host:base/docs/ <tmp>/docs/`; up (per changed file): `rsync -az <tmp>/<rel> host:base/<rel>` |
| N | unreachable target non-fatal | `status` with a git target whose `_run` raises | row shows `unknown` + note; command does **not** abort; other rows still render |

## 9. Operator approval decision point (Phase 2)

Approve as **D1.A** to implement as drafted, or specify deltas. Worth an explicit nod: **DD-1** (registry
`transport` key, `local` default = back-compat), **DD-4/DD-5** (per-target atomic; git direct push is
fast-forward-only, fixed commit identity, operator's own SSH creds), **DD-3** (unreachable target is
non-fatal for reads). No code is touched until approval lands; Phase 3 runs in a **fresh session**
prompted from this committed plan + `OPEN_TASKS.md` (per [[feedback_plan_handoff_via_open_tasks]]).

## 10. Rollback path

New module + additive registry fields (defaulted, back-compatible) + a `cli.py` seam + display tweak +
tests/docs. Rollback = `git revert` the Phase-3 commit; no vault content touched (DD-6); no target repo
is written unless `integrate --apply … --write` is run against a remote (a separate, later, operator-gated
action). A registry with only local entries behaves exactly as before the revert.

## 11. Known risks

| # | Risk | Mitigation | Status |
|---|---|---|---|
| R1 | One unreachable remote aborts a whole multi-project read | per-target `try/except TransportError`: `status`/`drift` → `unknown` row (QA N); `harvest`/`integrate` → stderr warning + skip (DD-3) | mitigated |
| R2 | git push clobbers remote work / force-push | shallow clone of the branch tip + one commit + `push HEAD:<branch>` **no `--force`**; non-ff fails loudly as `TransportError` (DD-5) | mitigated |
| R3 | Write-back not atomic across N remotes | validate **all** dispositions before **any** write (unchanged); per-target push; mid-sequence failure reported loudly, never silent (DD-4) | mitigated/documented |
| R4 | Temp materialization leaks on crash | `session()` disposes in a `finally`; multi-target write path uses `ExitStack` | mitigated |
| R5 | Credentials/secrets handling | tool never handles secrets — git/ssh/rsync use the operator's existing SSH agent/keys; commit identity is fixed via `-c`, never written to the target's config (DD-5) | mitigated |
| R6 | A target branch lacks `docs/` at tip | reads return empty/None exactly as a local missing file does today (`parse_log` → `[]`, version → `unknown`) | mitigated |
| R7 | `openrsync` (macOS default) flag differences | only `-a -z` + a plain `src dest` form are used (portable across rsync/openrsync); no exotic flags | mitigated |
| R8 | git/ssh integration is hard to unit-test (network) | drivers isolate I/O behind `transport._run`; tests monkeypatch it to assert exact argv; `LocalTarget` needs no subprocess. A live git/ssh smoke is an operator step, not CI | mitigated |

## 12. Acceptance criteria

- A registry entry with `transport = "git"` / `"ssh"` (or a bare local entry) parses; `make_target`
  builds the right driver; an unknown transport / missing field errors clearly.
- `status` / `drift` / `harvest` / `integrate` run against local **and** remote (git/ssh) targets; a local
  registry behaves exactly as before (back-compat), with the only display change being `PATH`→`LOCATION`.
- An unreachable remote is non-fatal for read commands (shown `unknown` / skipped with a warning).
- `integrate --apply … --write` to a remote validates all dispositions first, writes the matched `Status:`
  line in the materialization, and flushes via direct push (git) / rsync (ssh) — dry-run pushes nothing.
- QA A–N pass; governance exit 0. No `docs/standards/` edit; **no Set-Version bump**. `CLAUDE.md` § 1 +
  `architecture.md` § 1/§ 8/§ 9/§ 10/§ 11 updated; manifest/folder_structure synced; PLAN-007 + tracker →
  1.0/CLOSED.
