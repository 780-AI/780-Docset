<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-16 -->
<!-- Status: CLOSED -->
<!--
CHANGE LOG
v1.0 — 2026-06-16 13:01 — Phase 3 implemented + Phase 4 validated; promoted to CLOSED in the ship commit.
All 16 new files created verbatim from § 5; 5 docs/governance edits applied. QA scenarios A–I PASSED
(ruff clean on src+tests; mypy --strict clean; 21 pytest green; governance both exit 0; live status/drift
on the empty real registry exit 0). Set Version unchanged (v1.1 — no docs/standards/ file touched).
Three mechanical plan-defect fixes surfaced during Phase-4 validation (the Rule 13 pass never ran
ruff/mypy, so these slipped through) — all behavior-preserving, required to satisfy the plan's own
scenario H, applied + recorded (analogous to PLAN-002 D1–D4):
  • D1 (§ 5E) — `class State(str, Enum)` tripped ruff UP042 → changed to the idiomatic 3.11 `StrEnum`
    (`from enum import StrEnum`). Identical behavior (`.value` + `is` comparisons unchanged).
  • D2 (§ 5M) — `tests/test_report.py` `_status(...)` signature was 103 cols (ruff E501 > 100) → reflowed
    across 3 lines. No logic change.
  • D3 (§ 5N / R7 residual) — `from standard_document_updater import cli` + `cli.main` failed mypy --strict
    `attr-defined` from outside the package (cli is never imported attribute-style by a source dependency,
    unlike report/setversion) → switched the test to the always-resolvable dotted idiom
    `from standard_document_updater.cli import main` + `main(...)`. Production code (incl. § 5G __main__)
    kept byte-for-byte as drafted; deviation confined to the test.
Environment note: `pip install -e` produced a correct `__editable__*.pth` pointing at `src`, but this
machine's site processing did not add it to sys.path (likely the space in the repo path) — validated via
the plan-sanctioned `PYTHONPATH=src` / `MYPYPATH=src` (§ 8) instead. No pyproject defect.
v0.1 — 2026-06-16 — Initial draft of Slice 2 (registry + `status`/`drift` — first Python engine
code), per docs/architecture.md § 10. Operator decisions locked at design time: (1) registry stores
name + path only, adopted version read live (SSoT); (2) two subcommands `status` and `drift`;
(3) stay small — introduce pyproject + tests, DEFER CI test-stage wiring, `python -m` invocation only;
(4) report columns confirmed. Rule 13 senior-review pass run (foot of file): fixed 4 defects —
mypy-fragile render_table width calc, fragile tests.conftest import (→ write_registry fixture),
redundant cli.py __main__ block, mypy explicit_package_bases; corrected ALLOWLIST count 18→21; surfaced
the drift exit-code design decision (R5) for operator confirmation.
-->

# PLAN-003 — Slice 2: registry + `status` / `drift` (first Python engine code)

## 1. Goal

Land the **first Python engine code**: a vault-side registry of managed projects plus two read-only
commands that report each project's adopted Standard Set Version against the vault's canonical version
and its open experiences-log count.

- `python -m standard_document_updater status` — table of every registered project (adopted vs vault,
  open-log count). Always exits 0.
- `python -m standard_document_updater drift` — only projects **not** on the vault version; exits **1**
  if any exist (automation-friendly).

This implements the `status` / `drift` row of `docs/architecture.md` § 8 and resolves three of the § 11
open decisions. Read-only: no command in this slice writes to any target. See `architecture.md` §§ 7–10.

## 2. Operator constraints (decisions locked at design, 2026-06-16)

1. **Registry stores name + path only.** A project's adopted Set Version is read **live** from its
   `docs/SET_VERSION_ADOPTED.md` at report time — never cached in the registry. (SSoT + read-before-write,
   per `architecture.md` § 9 / `CLAUDE.md` § 2. Caching the version would be the duplication defect the
   standards forbid.)
2. **Two subcommands** `status` and `drift` (not one command with a flag).
3. **Stay small.** Introduce `pyproject.toml` + `tests/`; **DEFER** wiring the CI `test` stage
   (`.gitlab-ci.yml` is NOT touched this slice — avoids a Rule 5 pipeline round-trip). Invocation is
   `python -m standard_document_updater` only — no extra console-script alias this slice.
4. **Report columns:** `project · path · adopted · vault · state · open log`. The vault (this repo) is
   the comparison reference, **not** a row.

## 3. Scope summary

- **A — package skeleton** under `src/standard_document_updater/` (src layout): `__init__`, `__main__`,
  `errors`, `registry`, `setversion`, `report`, `cli` (7 modules; clean DAG per ENGINEERING § 1.1).
- **B — registry** `config/projects.toml` (name + path per project; ships empty with a commented example).
- **C — parsers** (`setversion.py`): vault canonical version, project adopted version, open-log count —
  all live reads, regex-pinned to the real file formats.
- **D — report** (`report.py`): state computation (current/behind/ahead/unknown) + plain-stdlib table +
  drift filter.
- **E — CLI** (`cli.py` + `__main__.py`): argparse, `--vault` override, `status` / `drift` dispatch,
  exit codes, error handling.
- **F — packaging** `pyproject.toml` (setuptools src-layout; ruff/mypy-strict/pytest config; stdlib-only
  runtime, dev extras pytest/mypy/ruff).
- **G — tests** under `tests/` (pytest): `conftest` synthetic-tree fixtures + unit tests for setversion,
  registry, report, and an end-to-end cli test.
- **H — ownership** `scripts/validation_ownership.toml`: add `src/standard_document_updater/` as a **soft**
  monitored path + one rule per testable module (per VALIDATION § 4.6 / § 10.9 — same-commit as the source).
- **I — doc sync** (same commit): `folder_structure.md` (Planned → real), `architecture.md` (§ 10 tick
  Slice 2 ✅ + § 11 resolve the 3 decisions), `documents_manifest.md` (register 12 `.py` + 2 plan docs),
  `CHANGELOG.md` (top entry).

**Explicitly NOT in scope (flagged for operator):**
- No Set Version bump. The Set Version tracks the **standards suite** (`docs/standards/`); this slice adds
  engine code and touches no suite file, so the suite is unchanged → stays **v1.1**. (See § 6 + § 11 R6.)
- No `.gitlab-ci.yml` change (decision 3).
- No registration of any real target project (registry ships empty; registering real projects is an
  operator follow-up — never assume a target path).
- No `CLAUDE.md` § 4 edit. The package `src/standard_document_updater/` is already listed there as a
  Critical File, so all new modules are already covered; the stale "(created when the engine lands)"
  wording cleanup + adding `config/projects.toml` as critical is deferred to the sync slice (§ 6).

## 4. Phase tracker

Big plan → granular sub-tasks live in the **sibling tracker** `docs/Plans/PLAN-003_tracker.md`
(per § 15.7; triggered by first-engine-code + multi-scenario QA). This § 4 stays a high-level summary:

- Phase 0 — Audit ......... ✅ 2026-06-16 (integration points cited by file:line below; tomllib stdlib confirmed)
- Phase 1 — Design ........ ✅ 2026-06-16 (this file + sibling tracker + Rule 13 pass below)
- Phase 2 — Approval ...... ✅ 2026-06-16 (`APPROVE PLAN-003`, recorded in OPEN_TASKS; drift exit-code R5 confirmed)
- Phase 3 — Implement ..... ✅ 2026-06-16 (fresh session; one ALLOWLIST-bounded commit; D1–D3 fixes per CHANGE LOG)
- Phase 4 — Validate ...... ✅ 2026-06-16 (ruff+mypy+pytest green; QA A–I PASSED; governance exit 0)
- Phase 5 — Operator gate . ⏸ push held for operator (no tag — engine code, no Set Version change)

## 5. Transformation rules (verbatim new-file contents, per Rule 7)

Every file in this slice is **new** (greenfield engine), so each rule below is the **complete file
content** to create. Phase 3 stamps the real `HH:MM` into each VERSION CHANGE LOG line.

### 5A — `src/standard_document_updater/__init__.py`

```python
# ==============================================================
# VERSION: 0.1
# Standard DocSet engine — package marker + released CLI version.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial package (Slice 2: registry + status/drift).
# ==============================================================
"""Standard DocSet — keep standards/governance suites in sync across projects."""
from __future__ import annotations

__version__ = "0.1.0"
```

### 5B — `src/standard_document_updater/errors.py`

```python
# ==============================================================
# VERSION: 0.1
# Exception hierarchy for the Standard DocSet engine.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: base error + RegistryError + ParseError.
# ==============================================================
"""Project-specific exceptions (per ENGINEERING_STANDARDS § 4.3)."""
from __future__ import annotations


class StandardDocSetError(Exception):
    """Base for all engine errors."""


class RegistryError(StandardDocSetError):
    """The projects registry is missing or malformed."""


class ParseError(StandardDocSetError):
    """A standards file could not be parsed for the expected value."""
```

### 5C — `src/standard_document_updater/registry.py`

```python
# ==============================================================
# VERSION: 0.1
# Managed-projects registry loader (config/projects.toml).
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: parse name + path tables into Project list.
# ==============================================================
"""Load the managed-projects registry.

Stores ONLY each project's name + path. A project's adopted Set Version is NOT
stored here — it is read live from <path>/docs/SET_VERSION_ADOPTED.md at report
time (single source of truth, per docs/architecture.md § 9).
"""
from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

from standard_document_updater.errors import RegistryError


@dataclass(frozen=True)
class Project:
    """A managed project: a display name and its repository root path."""

    name: str
    path: Path


def load_registry(registry_path: Path) -> list[Project]:
    """Parse config/projects.toml into a list of Project, in file order.

    Returns an empty list when the registry exists but declares no projects.
    Raises RegistryError when the file is missing, unreadable, or malformed.
    """
    if not registry_path.exists():
        raise RegistryError(f"registry not found: {registry_path}")
    try:
        data = tomllib.loads(registry_path.read_text(encoding="utf-8"))
    except (tomllib.TOMLDecodeError, OSError) as exc:
        raise RegistryError(f"could not read registry {registry_path}: {exc}") from exc

    raw_projects = data.get("project", [])
    if not isinstance(raw_projects, list):
        raise RegistryError("registry key 'project' must be an array of tables")

    projects: list[Project] = []
    for index, entry in enumerate(raw_projects, start=1):
        if not isinstance(entry, dict):
            raise RegistryError(f"project #{index} is not a table")
        name = entry.get("name")
        path = entry.get("path")
        if not isinstance(name, str) or not name.strip():
            raise RegistryError(f"project #{index} is missing a non-empty 'name'")
        if not isinstance(path, str) or not path.strip():
            raise RegistryError(f"project '{name}' is missing a non-empty 'path'")
        projects.append(Project(name=name, path=Path(path).expanduser()))
    return projects
```

### 5D — `src/standard_document_updater/setversion.py`

```python
# ==============================================================
# VERSION: 0.1
# Parse Set Versions + open-log counts from standards files (live reads).
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: vault version, adopted version, open-log count.
# ==============================================================
"""Live parsers for the version/log state the report needs.

Every read re-reads the file (never cached) per docs/architecture.md § 9 /
CLAUDE.md § 2. Regexes are pinned to the real on-disk formats:

  vault canonical  — docs/standards/STANDARDS_INDEX.md § 1 fenced block:
                       Standard Set Version: v1.1
  project adopted  — docs/SET_VERSION_ADOPTED.md:
                       - **Standard Set Version:** v1.1 (...)
  log entry        — docs/STANDARDS_LOG.md:
                       ## E001 — <title>
                       - Status:      open
"""
from __future__ import annotations

import re
from pathlib import Path

from standard_document_updater.errors import ParseError

_VAULT_RE = re.compile(r"^Standard Set Version:\s*v(\d+(?:\.\d+)+)", re.MULTILINE)
_ADOPTED_RE = re.compile(r"\*\*Standard Set Version:\*\*\s*v(\d+(?:\.\d+)+)")
_ENTRY_RE = re.compile(r"^##\s+E\d+\b", re.MULTILINE)
_STATUS_RE = re.compile(r"^-\s*Status:\s*(\S+)", re.MULTILINE)


def parse_vault_version(standards_index_path: Path) -> tuple[int, ...]:
    """Return the vault's canonical Set Version as an int tuple, e.g. (1, 1)."""
    return _parse_version(standards_index_path, _VAULT_RE, "vault Set Version")


def parse_adopted_version(adopted_path: Path) -> tuple[int, ...]:
    """Return a project's adopted Set Version as an int tuple, e.g. (1, 1)."""
    return _parse_version(adopted_path, _ADOPTED_RE, "adopted Set Version")


def _parse_version(path: Path, pattern: re.Pattern[str], label: str) -> tuple[int, ...]:
    if not path.exists():
        raise ParseError(f"{label}: file not found: {path}")
    match = pattern.search(path.read_text(encoding="utf-8"))
    if match is None:
        raise ParseError(f"{label}: no version line in {path}")
    return tuple(int(part) for part in match.group(1).split("."))


def count_open_log_entries(log_path: Path) -> int:
    """Count STANDARDS_LOG.md entries whose Status begins with 'open'.

    Returns 0 when the log file is absent (a project may not have started one).
    """
    if not log_path.exists():
        return 0
    text = log_path.read_text(encoding="utf-8")
    headings = list(_ENTRY_RE.finditer(text))
    count = 0
    for i, heading in enumerate(headings):
        start = heading.start()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        status = _STATUS_RE.search(text[start:end])
        if status is not None and status.group(1).lower().startswith("open"):
            count += 1
    return count
```

### 5E — `src/standard_document_updater/report.py`

```python
# ==============================================================
# VERSION: 0.1
# Build + render the project Set-Version comparison report.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: state computation, table render, drift filter.
# ==============================================================
"""Comparison report: each project's adopted version vs the vault version."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from standard_document_updater import setversion
from standard_document_updater.errors import ParseError
from standard_document_updater.registry import Project


class State(str, Enum):
    """Where a project's adopted version sits relative to the vault."""

    CURRENT = "current"
    BEHIND = "behind"
    AHEAD = "ahead"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class ProjectStatus:
    """One row of the report."""

    project: Project
    adopted: tuple[int, ...] | None  # None when the adopted version is unreadable
    vault: tuple[int, ...]
    state: State
    open_entries: int
    note: str = ""  # parse-error detail when state is UNKNOWN


def compute_status(
    project: Project,
    vault: tuple[int, ...],
    adopted_path: Path,
    log_path: Path,
) -> ProjectStatus:
    """Compare one project against the vault version (never raises on a bad target)."""
    open_entries = setversion.count_open_log_entries(log_path)
    try:
        adopted = setversion.parse_adopted_version(adopted_path)
    except ParseError as exc:
        return ProjectStatus(project, None, vault, State.UNKNOWN, open_entries, str(exc))
    if adopted == vault:
        state = State.CURRENT
    elif adopted < vault:
        state = State.BEHIND
    else:
        state = State.AHEAD
    return ProjectStatus(project, adopted, vault, state, open_entries)


def filter_drift(statuses: list[ProjectStatus]) -> list[ProjectStatus]:
    """Projects not on the vault version (behind / ahead / unknown)."""
    return [s for s in statuses if s.state is not State.CURRENT]


def _fmt_version(version: tuple[int, ...] | None) -> str:
    return "v" + ".".join(str(n) for n in version) if version else "?"


def render_table(statuses: list[ProjectStatus]) -> str:
    """Render the report as a fixed-width text table."""
    if not statuses:
        return "No projects registered. Add entries to config/projects.toml."
    headers = ["PROJECT", "PATH", "ADOPTED", "VAULT", "STATE", "OPEN LOG"]
    rows = [
        [
            s.project.name,
            str(s.project.path),
            _fmt_version(s.adopted),
            _fmt_version(s.vault),
            s.state.value,
            str(s.open_entries),
        ]
        for s in statuses
    ]
    widths = [max(len(row[i]) for row in [headers, *rows]) for i in range(len(headers))]

    def line(cells: list[str]) -> str:
        return "  ".join(cell.ljust(widths[i]) for i, cell in enumerate(cells))

    out = [line(headers), line(["-" * w for w in widths])]
    out.extend(line(r) for r in rows)
    return "\n".join(out)
```

### 5F — `src/standard_document_updater/cli.py`

```python
# ==============================================================
# VERSION: 0.1
# Command-line interface: `python -m standard_document_updater <command>`.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: status + drift subcommands, --vault override.
# ==============================================================
"""CLI entry point and command dispatch."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from standard_document_updater import __version__, report, setversion
from standard_document_updater.errors import StandardDocSetError
from standard_document_updater.registry import load_registry


def default_vault_root() -> Path:
    """Repo root inferred from this package's location (src layout).

    .../src/standard_document_updater/cli.py -> parents[2] == repo root.
    Override with --vault when the engine is installed outside the repo.
    """
    return Path(__file__).resolve().parents[2]


def _build_statuses(vault_root: Path) -> list[report.ProjectStatus]:
    index_path = vault_root / "docs" / "standards" / "STANDARDS_INDEX.md"
    registry_path = vault_root / "config" / "projects.toml"
    vault_version = setversion.parse_vault_version(index_path)
    statuses: list[report.ProjectStatus] = []
    for project in load_registry(registry_path):
        adopted_path = project.path / "docs" / "SET_VERSION_ADOPTED.md"
        log_path = project.path / "docs" / "STANDARDS_LOG.md"
        statuses.append(report.compute_status(project, vault_version, adopted_path, log_path))
    return statuses


def _cmd_status(args: argparse.Namespace) -> int:
    print(report.render_table(_build_statuses(args.vault)))
    return 0


def _cmd_drift(args: argparse.Namespace) -> int:
    drifted = report.filter_drift(_build_statuses(args.vault))
    if not drifted:
        print("No drift: all registered projects are on the vault Set Version.")
        return 0
    print(report.render_table(drifted))
    print(f"\n{len(drifted)} project(s) not on the vault Set Version.")
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="standard_document_updater",
        description="Keep adopting projects in sync with the canonical standards suite.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "--vault",
        type=Path,
        default=default_vault_root(),
        help="path to the vault repo root (default: inferred from install location)",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="show every registered project's adopted vs vault Set Version")
    sub.add_parser("drift", help="show only projects not on the vault Set Version (exit 1 if any)")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse argv and run the chosen command. Returns the process exit code."""
    args = build_parser().parse_args(argv)
    handlers = {"status": _cmd_status, "drift": _cmd_drift}
    try:
        return handlers[args.command](args)
    except StandardDocSetError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
```

> `cli.py` has no `if __name__ == "__main__"` block — the single entry point is `__main__.py` (5G), which
> keeps the package's absolute imports valid (running `cli.py` as a loose script would break them).

### 5G — `src/standard_document_updater/__main__.py`

```python
# ==============================================================
# VERSION: 0.1
# Module entry point for `python -m standard_document_updater`.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: delegate to cli.main().
# ==============================================================
"""Enable `python -m standard_document_updater`."""
from __future__ import annotations

from standard_document_updater.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
```

### 5H — `config/projects.toml` (NEW; no VERSION header — config, not manifest-tracked)

```toml
# ==============================================================
# Registry of projects managed by Standard DocSet.
#
# Stores ONLY name + path per project. A project's adopted Set Version is read
# LIVE from <path>/docs/SET_VERSION_ADOPTED.md at report time — never cached
# here (single source of truth, per docs/architecture.md § 9).
#
# Add one [[project]] table per managed repository:
#
# [[project]]
# name = "example-adopter"
# path = "/Users/you/Documents/example-adopter"
# ==============================================================

# (empty — no projects registered yet)
```

### 5I — `pyproject.toml` (NEW; no VERSION header — config)

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "standard-docset"
version = "0.1.0"
description = "Keep standards/governance documentation suites in sync across projects."
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
dev = ["pytest>=8", "mypy>=1.8", "ruff>=0.4"]

[tool.setuptools.packages.find]
where = ["src"]

[tool.ruff]
line-length = 100
src = ["src", "tests"]

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]

[tool.mypy]
python_version = "3.11"
strict = true
files = ["src", "tests"]
explicit_package_bases = true

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### 5J — `tests/conftest.py`

```python
# ==============================================================
# VERSION: 0.1
# Shared pytest fixtures — synthetic vault + adopter-project trees.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: make_vault + make_project factories.
# ==============================================================
"""Fixtures that build minimal on-disk vault/project trees under tmp_path.

All three fixtures return factory callables. Tests annotate the injected
parameter as ``Callable[..., Path]`` so mypy --strict is satisfied without
importing anything from this module (no cross-test imports, no type: ignore).
"""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def make_vault(tmp_path: Path) -> Callable[..., Path]:
    """Factory: build a vault root with STANDARDS_INDEX.md at the given Set Version."""

    def _make(version: str = "1.1") -> Path:
        root = tmp_path / "vault"
        _write(
            root / "docs" / "standards" / "STANDARDS_INDEX.md",
            f"## 1. Standard Set Version (current)\n\n```\nStandard Set Version: v{version}\n```\n",
        )
        (root / "config").mkdir(parents=True, exist_ok=True)
        return root

    return _make


@pytest.fixture
def make_project(tmp_path: Path) -> Callable[..., Path]:
    """Factory: build an adopter tree; adopted=None omits SET_VERSION_ADOPTED.md."""

    def _make(name: str, adopted: str | None = "1.1", open_entries: int = 0) -> Path:
        proj = tmp_path / name
        if adopted is not None:
            _write(
                proj / "docs" / "SET_VERSION_ADOPTED.md",
                f"- **Standard Set Version:** v{adopted} (notes)\n",
            )
        if open_entries:
            body = "".join(
                f"## E{i + 1:03d} — title\n- Status:      open\n\n" for i in range(open_entries)
            )
            _write(proj / "docs" / "STANDARDS_LOG.md", body)
        return proj

    return _make


@pytest.fixture
def write_registry() -> Callable[..., Path]:
    """Factory: write config/projects.toml from (name, path) pairs; return its path."""

    def _write_registry(vault_root: Path, projects: list[tuple[str, Path]]) -> Path:
        body = "".join(
            f'[[project]]\nname = "{name}"\npath = "{path}"\n\n' for name, path in projects
        )
        registry = vault_root / "config" / "projects.toml"
        _write(registry, body)
        return registry

    return _write_registry
```

### 5K — `tests/test_setversion.py`

```python
# ==============================================================
# VERSION: 0.1
# Unit tests for setversion parsers.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: version parsing + open-log counting.
# ==============================================================
"""Tests for standard_document_updater.setversion."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest

from standard_document_updater import setversion
from standard_document_updater.errors import ParseError


def test_parse_vault_version_reads_index(make_vault: Callable[..., Path]) -> None:
    root = make_vault("1.1")
    index = root / "docs" / "standards" / "STANDARDS_INDEX.md"
    assert setversion.parse_vault_version(index) == (1, 1)


def test_parse_adopted_version_reads_bold_line(make_project: Callable[..., Path]) -> None:
    proj = make_project("p", adopted="1.0")
    adopted = proj / "docs" / "SET_VERSION_ADOPTED.md"
    assert setversion.parse_adopted_version(adopted) == (1, 0)


def test_parse_version_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(ParseError):
        setversion.parse_vault_version(tmp_path / "nope.md")


def test_parse_version_no_line_raises(tmp_path: Path) -> None:
    bad = tmp_path / "x.md"
    bad.write_text("nothing here\n", encoding="utf-8")
    with pytest.raises(ParseError):
        setversion.parse_adopted_version(bad)


def test_count_open_log_entries_counts_only_open(tmp_path: Path) -> None:
    log = tmp_path / "STANDARDS_LOG.md"
    log.write_text(
        "## E001 — a\n- Status:      open\n\n"
        "## E002 — b\n- Status:      integrated → vault L050\n\n"
        "## E003 — c\n- Status:      open\n\n"
        "## E004 — d\n- Status:      rejected — not portable\n\n",
        encoding="utf-8",
    )
    assert setversion.count_open_log_entries(log) == 2


def test_count_open_log_entries_absent_file_is_zero(tmp_path: Path) -> None:
    assert setversion.count_open_log_entries(tmp_path / "missing.md") == 0
```

### 5L — `tests/test_registry.py`

```python
# ==============================================================
# VERSION: 0.1
# Unit tests for the registry loader.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: load / empty / missing / malformed.
# ==============================================================
"""Tests for standard_document_updater.registry."""
from __future__ import annotations

from pathlib import Path

import pytest

from standard_document_updater.errors import RegistryError
from standard_document_updater.registry import load_registry


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_load_registry_parses_projects_in_order(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(
        reg,
        '[[project]]\nname = "alpha"\npath = "/tmp/alpha"\n\n'
        '[[project]]\nname = "beta"\npath = "/tmp/beta"\n',
    )
    projects = load_registry(reg)
    assert [p.name for p in projects] == ["alpha", "beta"]
    assert projects[0].path == Path("/tmp/alpha")


def test_load_registry_empty_is_empty_list(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, "# no projects\n")
    assert load_registry(reg) == []


def test_load_registry_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(RegistryError):
        load_registry(tmp_path / "absent.toml")


def test_load_registry_missing_name_raises(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, '[[project]]\npath = "/tmp/x"\n')
    with pytest.raises(RegistryError):
        load_registry(reg)
```

### 5M — `tests/test_report.py`

```python
# ==============================================================
# VERSION: 0.1
# Unit tests for state computation + rendering + drift filter.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: current/behind/ahead/unknown + render + filter.
# ==============================================================
"""Tests for standard_document_updater.report."""
from __future__ import annotations

from pathlib import Path

from standard_document_updater import report
from standard_document_updater.registry import Project


def _status(name: str, adopted: str | None, open_entries: int, proj_dir: Path) -> report.ProjectStatus:
    if adopted is not None:
        (proj_dir / "docs").mkdir(parents=True, exist_ok=True)
        (proj_dir / "docs" / "SET_VERSION_ADOPTED.md").write_text(
            f"- **Standard Set Version:** v{adopted}\n", encoding="utf-8"
        )
    return report.compute_status(
        Project(name=name, path=proj_dir),
        vault=(1, 1),
        adopted_path=proj_dir / "docs" / "SET_VERSION_ADOPTED.md",
        log_path=proj_dir / "docs" / "STANDARDS_LOG.md",
    )


def test_state_current(tmp_path: Path) -> None:
    assert _status("p", "1.1", 0, tmp_path).state is report.State.CURRENT


def test_state_behind(tmp_path: Path) -> None:
    assert _status("p", "1.0", 0, tmp_path).state is report.State.BEHIND


def test_state_ahead(tmp_path: Path) -> None:
    assert _status("p", "1.2", 0, tmp_path).state is report.State.AHEAD


def test_state_unknown_when_adopted_missing(tmp_path: Path) -> None:
    s = _status("p", None, 0, tmp_path)
    assert s.state is report.State.UNKNOWN
    assert s.adopted is None


def test_render_table_empty_message() -> None:
    assert "No projects registered" in report.render_table([])


def test_filter_drift_excludes_current(tmp_path: Path) -> None:
    current = _status("cur", "1.1", 0, tmp_path / "a")
    behind = _status("old", "1.0", 0, tmp_path / "b")
    drifted = report.filter_drift([current, behind])
    assert [s.project.name for s in drifted] == ["old"]
```

### 5N — `tests/test_cli.py`

```python
# ==============================================================
# VERSION: 0.1
# End-to-end tests for the CLI (status / drift).
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: status table, drift exit codes, empty registry.
# ==============================================================
"""Tests for standard_document_updater.cli."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest

from standard_document_updater import cli

Make = Callable[..., Path]


def test_status_empty_registry_exit_zero(
    make_vault: Make, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    root = make_vault("1.1")
    write_registry(root, [])
    assert cli.main(["--vault", str(root), "status"]) == 0
    assert "No projects registered" in capsys.readouterr().out


def test_status_lists_project_exit_zero(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted="1.0", open_entries=2)
    write_registry(root, [("alpha", proj)])
    assert cli.main(["--vault", str(root), "status"]) == 0
    out = capsys.readouterr().out
    assert "alpha" in out and "behind" in out and "v1.0" in out


def test_drift_behind_exits_one(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted="1.0")
    write_registry(root, [("alpha", proj)])
    assert cli.main(["--vault", str(root), "drift"]) == 1


def test_drift_all_current_exits_zero(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted="1.1")
    write_registry(root, [("alpha", proj)])
    assert cli.main(["--vault", str(root), "drift"]) == 0
    assert "No drift" in capsys.readouterr().out


def test_drift_unknown_counts_as_drift(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted=None)
    write_registry(root, [("alpha", proj)])
    assert cli.main(["--vault", str(root), "drift"]) == 1
```

### 5O — `scripts/validation_ownership.toml` (MODIFIED — add soft monitoring + rules)

Replace the two trailing lines

```toml
[monitored_paths]
strict = []   # populate as the project grows
soft   = []
```

with

```toml
[rules.registry]
source_paths = ["src/standard_document_updater/registry.py"]
test_paths   = ["tests/test_registry.py"]
doc_paths    = ["docs/architecture.md"]
strictness   = "soft"
require_docs = false
reason       = "Registry loader — defines which projects the engine reads."

[rules.setversion]
source_paths = ["src/standard_document_updater/setversion.py"]
test_paths   = ["tests/test_setversion.py"]
doc_paths    = ["docs/architecture.md"]
strictness   = "soft"
require_docs = false
reason       = "Set-Version + open-log parsers — the data the report depends on."

[rules.report]
source_paths = ["src/standard_document_updater/report.py"]
test_paths   = ["tests/test_report.py"]
doc_paths    = ["docs/architecture.md"]
strictness   = "soft"
require_docs = false
reason       = "State computation + rendering — operator-visible output."

[rules.cli]
source_paths = ["src/standard_document_updater/cli.py"]
test_paths   = ["tests/test_cli.py"]
doc_paths    = ["docs/architecture.md"]
strictness   = "soft"
require_docs = false
reason       = "Command surface — status/drift behavior + exit codes."

[monitored_paths]
strict = []                               # populate as coverage matures
soft   = ["src/standard_document_updater/"]
```

> Soft (warn-only), per VALIDATION § 4.3 — promote to strict in a later slice once the drift checker
> actually parses this map. `errors.py` / `__init__.py` / `__main__.py` are thin (re-exports / entry
> points) and need no rule per § 4.5.

### 5P–5S — doc sync (mechanical; full edits given in the sibling tracker Phase 3 checklist)

- **`docs/folder_structure.md`** — move `src/standard_document_updater/` (list the 7 modules), `tests/`
  (list conftest + 4 test files), `config/projects.toml`, and `pyproject.toml` from the **Planned**
  block into the live tree; bump header `0.5 → 0.6` + CHANGE LOG line.
- **`docs/architecture.md`** (Critical File) — § 10: tick Slice 2 ✅ (with a one-line "shipped registry +
  status/drift" note). § 11: strike the three now-decided items (registry format = name+path live-read;
  CLI = `python -m standard_document_updater`; status/drift = two commands) and leave the remaining open
  decisions (STANDARDS_LOG home is already decided; `integrate` model-in-process question stays open).
  § 8: note `status`/`drift` are implemented. Bump `0.3 → 0.4` + CHANGE LOG line.
- **`docs/documents_manifest.md`** (Critical File) — add 12 rows (7 src + 5 test `.py`, all with VERSION
  headers) under a new **Engine** module-index range + 2 Plan rows (PLAN-003 + PLAN-003_tracker); bump
  `1.4 → 1.5`; rotate the Last Updated block. (`config/projects.toml` + `pyproject.toml` carry no VERSION
  header → not manifest-tracked, per the manifest's own note; they're covered by folder_structure.)
- **`CHANGELOG.md`** — top entry: "Slice 2 — registry + status/drift (first engine code)", explicit
  impact statement ("read-only; no Set Version change; CI unchanged"), QA-scenarios sub-section
  referencing A–I.

## 6. Spec / doc update map

| Behavior introduced | Authoritative source (code) | Navigable doc kept in sync (same commit) |
|---|---|---|
| Registry = name + path, version read live | `registry.py` + `setversion.py` | `architecture.md` § 8 (registry) + § 11 decision struck |
| `status` / `drift` commands + exit codes | `cli.py` | `architecture.md` § 8 command table + § 10 Slice 2 ✅ |
| State model (current/behind/ahead/unknown) | `report.py` | `architecture.md` § 8 (implicit) |
| Engine package exists | `src/standard_document_updater/` | `folder_structure.md` Planned → live |

**No Set Version bump.** Per `architecture.md` § 9 the Set Version tracks the **standards suite**
(`docs/standards/`). This slice touches no file under `docs/standards/`, so the suite is unchanged and the
Set Version stays **v1.1**. (`SET_VERSION_ADOPTED.md` and `STANDARDS_INDEX.md` are NOT edited.) This is the
deliberate inverse of PLAN-002's D2, where suite content *did* change and a bump *was* required.

**Deferred (operator-flagged, → OPEN_TASKS follow-up):** `CLAUDE.md` § 4 wording cleanup (drop "(created
when the engine lands)" from the `src/...` entry; add `config/projects.toml` as a Critical File). Not
required for correctness this slice — the package entry already makes all new modules critical — and
deferring keeps the contract untouched (decision 3, stay small).

## 7. ALLOWLIST (the bullet enumeration IS the count — 21 paths: 16 new + 5 modified)

**NEW (16):**
1. `src/standard_document_updater/__init__.py`
2. `src/standard_document_updater/__main__.py`
3. `src/standard_document_updater/errors.py`
4. `src/standard_document_updater/registry.py`
5. `src/standard_document_updater/setversion.py`
6. `src/standard_document_updater/report.py`
7. `src/standard_document_updater/cli.py`
8. `tests/conftest.py`
9. `tests/test_setversion.py`
10. `tests/test_registry.py`
11. `tests/test_report.py`
12. `tests/test_cli.py`
13. `config/projects.toml`
14. `pyproject.toml`
15. `docs/Plans/PLAN-003_registry_status_drift.md` (this plan)
16. `docs/Plans/PLAN-003_tracker.md` (sibling tracker)

**MODIFIED (5):**
17. `scripts/validation_ownership.toml`
18. `docs/folder_structure.md`
19. `docs/architecture.md`
20. `docs/documents_manifest.md`
21. `CHANGELOG.md`

(16 new + 5 modified = 21 paths. NOT touched: `.gitlab-ci.yml`, `CLAUDE.md`, any `docs/standards/` file,
`SET_VERSION_ADOPTED.md`, `STANDARDS_INDEX.md`. If any of those appears in `git status`, STOP per Rule 6.)
No `tests/__init__.py` (tests stay top-level modules; mypy uses `explicit_package_bases`).

## 8. Validation gate + QA scenarios (Rule 11)

Run from the repo root (editable install: `pip install -e ".[dev]"`, or `PYTHONPATH=src`). Each scenario
is tracked in `PLAN-003_tracker.md` Phase 4.

- **A — module run, empty registry:** `python -m standard_document_updater status` against the real repo
  (empty `config/projects.toml`) → prints "No projects registered…", exit 0.
- **B — status, project current:** fixture target on v1.1 → row shows `current`, exit 0.
- **C — status, project behind:** fixture target on v1.0 → row shows `behind`, exit 0 (status never fails).
- **D — drift, all current:** → "No drift…", exit 0.
- **E — drift, one behind:** → lists it, exit **1**.
- **F — unknown target:** target missing `SET_VERSION_ADOPTED.md` → `status` shows `unknown` (exit 0);
  `drift` lists it, exit **1** (unknown counts as drift — see § 11 R5).
- **G — open-log count:** target log with open/integrated/rejected mix → `OPEN LOG` shows only the `open`
  count.
- **H — quality gates:** `pytest` green; `mypy --strict` clean on `src` + `tests`; `ruff check` clean.
- **I — governance unchanged:** `python scripts/check_doc_coverage.py` and
  `python scripts/check_test_coverage_drift.py --ci` both exit 0 (paste stdout per Rule 6).

B–G are covered by the pytest suite (§ 5K–5N); A, H, I are operator-run smokes confirmed in Phase 4.

## 9. Operator-approval decision point

Reply **`APPROVE PLAN-003`**. Decisions already locked (§ 2). One micro-decision surfaced for confirmation
(not silently chosen): **drift exit-code semantics** — `drift` treats a project as drift when its state is
**not** `current`, i.e. `behind`, `ahead`, **or** `unknown` all exit 1 (§ 11 R5). Say so if you'd rather
`unknown`/`ahead` be exit-0 warnings.

## 10. Rollback

Local commit on `master`. Rollback = `git revert` the single Phase-3 commit (or `git reset` if unpushed).
All new files are additive (no `git mv`, no deletions); reverting removes `src/`, `tests/`, `config/`,
`pyproject.toml` and restores the four synced docs + ownership toml. No state outside the repo is touched
(read-only engine).

## 11. Risks + design decisions

- **R1 — vault-root inference breaks if installed as a wheel outside the repo.** `default_vault_root()`
  uses `parents[2]`, correct only for the src-layout in-repo run (the supported Slice-2 mode). Mitigation:
  `--vault PATH` override; the help text states the default is inferred. Revisit when/if the CLI is
  packaged for install elsewhere.
- **R2 — regex drift against the real file formats.** If `STANDARDS_INDEX.md` § 1 or
  `SET_VERSION_ADOPTED.md` change shape, parsing fails with a clear `ParseError`. Mitigation: both formats
  are standards-governed; tests pin them; vault-version failure surfaces as a top-level `error:` (exit 2),
  adopted-version failure degrades that one project to `unknown` (not a crash).
- **R3 — version tuple comparison across unequal lengths.** Current scheme is 2-part (`vX.Y`); the regex
  is forward-compatible (`\d+(?:\.\d+)+`) and tuple compare is lexicographic. A future 3-part scheme would
  compare correctly (`(1,1) < (1,1,1)`); documented here so it isn't a surprise.
- **R4 — a registry path doesn't exist / isn't a repo.** `compute_status` catches `ParseError` →
  `unknown` with the error message in `note`; the run never crashes on a bad target (scenario F).
- **R5 — drift exit-code semantics (design decision, surfaced § 9).** `drift` = state ≠ `current`, so
  `unknown` and `ahead` also exit 1. Rationale: `unknown` (unreadable target) is a real problem operators
  should see fail; `ahead` is anomalous and worth surfacing. Operator may override at approval.
- **R6 — accidental Set Version bump.** The inverse of PLAN-002's defect: an implementer might reflexively
  bump the Set Version. § 6 makes the non-bump explicit and lists `SET_VERSION_ADOPTED.md` /
  `STANDARDS_INDEX.md` as NOT-touched in § 7 — appearance in `git status` is a STOP signal.
- **R7 — tests packaging under pytest + mypy --strict (resolved by design).** Originally `test_cli`
  imported `write_registry` from `tests.conftest`, which is fragile without a `tests/__init__.py`. The
  Rule 13 pass removed the cross-import entirely: `write_registry` is now a **fixture**, and tests
  annotate factory params as `Callable[..., Path]` (no conftest import, no `type: ignore`). Residual
  mypy namespace handling is covered by `explicit_package_bases = true`. Confirmed at Phase 4 (scenario H).

## 12. Acceptance criteria

- `status` lists every registered project with correct `state` (current/behind/ahead/unknown) and `open`
  count; empty registry prints the friendly message; always exit 0.
- `drift` filters to non-current projects, prints the table + count, exits 1 if any, else "No drift" exit 0.
- Engine is read-only — no file outside the repo is written; no target is read that isn't in the registry.
- `pytest` + `mypy --strict` + `ruff` all green; governance scripts exit 0; `.gitlab-ci.yml` unchanged.
- Set Version stays v1.1 (no suite file touched); docs synced same-commit (folder_structure, architecture,
  manifest, CHANGELOG); ownership map updated.

---

## Senior-review-and-optimize pass (Rule 13) — 2026-06-16

Ran the canonical review prompt over the complete plan + sibling tracker, verifying every § 5 code block
against the real current source (regex anchors checked against `STANDARDS_INDEX.md:37`,
`SET_VERSION_ADOPTED.md`, and the `STANDARDS_LOG.md` schema). Four genuine defects found and **fixed in
place**, plus consistency repairs:

1. **`render_table` width calc was mypy-fragile** (`max(len(h), *(gen))` — positional + unpack mixes
   poorly under `--strict`). Rewrote to `max(len(row[i]) for row in [headers, *rows])` — single-iterable
   form, mypy-clean, identical output. (§ 5E)
2. **`test_cli` imported `write_registry` from `tests.conftest`** — fragile without `tests/__init__.py`
   (would `ImportError` under pytest's default rootdir import). Converted `write_registry` to a **fixture**;
   all factory params now annotate as `Callable[..., Path]`. Eliminated every `# type: ignore[operator]`
   and the `object` placeholder annotations across `test_setversion` + `test_cli`. (§ 5J, 5K, 5N; R7 closed)
3. **`cli.py` carried a redundant `if __name__ == "__main__"` block** that implied it was runnable as a
   loose script (its absolute imports would break if so). Removed; `__main__.py` is the sole entry. (§ 5F)
4. **mypy namespace robustness** — added `explicit_package_bases = true` so `src` + `tests` type-check
   without `__init__.py` collisions. (§ 5I)

Consistency repairs: ALLOWLIST heading corrected 18 → **21** (16 new + 5 modified; enumeration governs per
L038) and the stray correction-note removed; `collections.abc.Callable` used throughout (ruff `UP`);
import groups ordered for ruff `I`.

**Verified correct against real source (no change needed):** `_VAULT_RE` matches `STANDARDS_INDEX.md:37`
exactly; `_ADOPTED_RE` matches the bold adopted line and does NOT collide with the vault line; open-log
counting handles the `open`/`integrated`/`rejected` schema; `default_vault_root()` `parents[2]` resolves
to repo root for `src/standard_document_updater/cli.py`; the empty shipped `config/projects.toml` parses
to `[]` → "No projects registered" (scenario A).

**New design decision surfaced** (not silently chosen) — **drift exit-code semantics** (R5/§ 9):
`unknown` and `ahead` both count as drift (exit 1). Flagged for operator confirmation at approval.

No contradictions remain across §§ 1–12 + tracker. Plan is internally consistent and ready for Phase 2.
