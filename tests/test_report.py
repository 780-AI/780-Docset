# ==============================================================
# VERSION: 0.2
# Unit tests for state computation + rendering + drift filter.
#
# CHANGE LOG
# v0.2 — 2026-06-20 — Add LOCATION header / git-location cell / unreachable_status cases (PLAN-007).
# v0.1 — 2026-06-16 13:01 — Initial: current/behind/ahead/unknown + render + filter.
# ==============================================================
"""Tests for standard_document_updater.report."""
from __future__ import annotations

from pathlib import Path

from standard_document_updater import report
from standard_document_updater.registry import Project


def _status(
    name: str, adopted: str | None, open_entries: int, proj_dir: Path
) -> report.ProjectStatus:
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


def test_render_table_header_is_location() -> None:
    p = Project(name="x", path=Path("/tmp/x"))
    s = report.ProjectStatus(p, (1, 1), (1, 1), report.State.CURRENT, 0)
    header = report.render_table([s]).splitlines()[0]
    assert "LOCATION" in header and "PATH" not in header


def test_render_table_shows_git_location() -> None:
    p = Project(name="b", transport="git", git_url="git@h:r.git", git_branch="main")
    s = report.ProjectStatus(p, (1, 1), (1, 1), report.State.CURRENT, 0)
    assert "git:git@h:r.git@main" in report.render_table([s])


def test_unreachable_status_is_unknown() -> None:
    p = Project(name="b", transport="git", git_url="u")
    s = report.unreachable_status(p, (1, 1), "clone failed")
    assert s.state is report.State.UNKNOWN
    assert s.adopted is None and s.note == "clone failed"
