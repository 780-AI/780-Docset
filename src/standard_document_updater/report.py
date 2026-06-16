# ==============================================================
# VERSION: 0.1
# Build + render the project Set-Version comparison report.
#
# CHANGE LOG
# v0.1 — 2026-06-16 13:01 — Initial: state computation, table render, drift filter.
# ==============================================================
"""Comparison report: each project's adopted version vs the vault version."""
from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

from standard_document_updater import setversion
from standard_document_updater.errors import ParseError
from standard_document_updater.registry import Project


class State(StrEnum):
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
