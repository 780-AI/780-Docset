# ==============================================================
# VERSION: 0.1
# Unit tests for the harvest report (pure render + dup logic, no disk).
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: grouping, cross-project dup flag, exclusions.
# ==============================================================
"""Tests for standard_document_updater.harvest."""
from __future__ import annotations

from standard_document_updater.harvest import OpenItem, render_report
from standard_document_updater.logentry import LogEntry


def _item(
    project: str,
    entry_id: str,
    title: str,
    area: str = "engineering",
    portability: str = "",
) -> OpenItem:
    return OpenItem(
        project_name=project,
        entry=LogEntry(
            entry_id=entry_id, title=title, area=area, status="open", portability=portability
        ),
    )


def test_empty_items_message() -> None:
    assert render_report([]) == "No open log entries across registered projects."


def test_groups_by_area_and_counts() -> None:
    out = render_report(
        [
            _item("alpha", "E001", "Aaa", area="engineering"),
            _item("alpha", "E002", "Bbb", area="cicd"),
        ]
    )
    assert "## cicd (1)" in out
    assert "## engineering (1)" in out
    assert "across 1 project(s), 2 area(s)" in out


def test_flags_cross_project_duplicate() -> None:
    out = render_report(
        [
            _item("alpha", "E001", "Pin every read site"),
            _item("beta", "E007", "Pin every read site!"),
        ]
    )
    assert "possible duplicate of beta/E007" in out
    assert "possible duplicate of alpha/E001" in out


def test_same_project_same_title_not_flagged() -> None:
    out = render_report(
        [
            _item("alpha", "E001", "Repeated"),
            _item("alpha", "E002", "Repeated"),
        ]
    )
    assert "possible duplicate" not in out


def test_distinct_titles_not_flagged() -> None:
    out = render_report(
        [
            _item("alpha", "E001", "One thing"),
            _item("beta", "E002", "Another thing"),
        ]
    )
    assert "possible duplicate" not in out


def test_portability_shown_when_present() -> None:
    out = render_report([_item("alpha", "E001", "T", portability="general")])
    assert "(general)" in out
