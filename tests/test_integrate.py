# ==============================================================
# VERSION: 0.1
# Unit tests for the integrate worksheet + status write-back.
#
# CHANGE LOG
# v0.1 — 2026-06-18 — Initial: routing, next-L0NN, worksheet, decisions parse, write-back atomicity.
# ==============================================================
"""Tests for standard_document_updater.integrate."""
from __future__ import annotations

from pathlib import Path

import pytest

from standard_document_updater.harvest import OpenItem
from standard_document_updater.integrate import (
    Disposition,
    IntegrateError,
    apply_writeback,
    build_rows,
    next_lesson_id,
    parse_decisions,
    render_worksheet,
    route_area,
)
from standard_document_updater.logentry import LogEntry


def _item(
    project: str = "alpha",
    entry_id: str = "E001",
    title: str = "A title",
    area: str = "engineering",
    context: str = "ctx",
    learned: str = "lrn",
    suggested: str = "sug",
) -> OpenItem:
    return OpenItem(
        project_name=project,
        entry=LogEntry(
            entry_id=entry_id,
            title=title,
            area=area,
            status="open",
            context=context,
            learned=learned,
            suggested=suggested,
        ),
    )


# --- route_area (QA G) -------------------------------------------------------


def test_route_area_each_known_area() -> None:
    assert route_area("engineering") == ("ENGINEERING_STANDARDS.md", True)
    assert route_area("cicd") == ("CICD_STANDARDS.md", True)
    assert route_area("validation") == ("VALIDATION_STANDARDS.md", True)
    assert route_area("project") == ("PROJECT_STANDARDS.md", True)
    assert route_area("prompt") == ("PROMPT_STANDARDS.md", True)
    assert route_area("memory") == ("MEMORY_PROTOCOL.md", True)
    assert route_area("governance") == ("CLAUDE.md", True)


def test_route_area_case_and_space_insensitive() -> None:
    assert route_area("  Engineering ") == ("ENGINEERING_STANDARDS.md", True)


def test_route_area_unknown_falls_back_unrouted() -> None:
    assert route_area("frobnicate") == ("PROJECT_STANDARDS.md", False)
    assert route_area("") == ("PROJECT_STANDARDS.md", False)


# --- next_lesson_id (QA H) ---------------------------------------------------


def test_next_lesson_id_max_plus_one(tmp_path: Path) -> None:
    p = tmp_path / "LESSONS.md"
    p.write_text("### L048 — a\n\n### L050 — b\n\n### L049 — c\n", encoding="utf-8")
    assert next_lesson_id(p) == "L051"


def test_next_lesson_id_absent_file(tmp_path: Path) -> None:
    assert next_lesson_id(tmp_path / "nope.md") == "L001"


def test_next_lesson_id_no_headings(tmp_path: Path) -> None:
    p = tmp_path / "LESSONS.md"
    p.write_text("# Lessons\n\nno entries yet\n", encoding="utf-8")
    assert next_lesson_id(p) == "L001"


# --- build_rows / render_worksheet -------------------------------------------


def test_build_rows_routes_and_preserves_order() -> None:
    rows = build_rows([_item(entry_id="E001", area="cicd"), _item(entry_id="E002", area="zzz")])
    assert [r.entry_id for r in rows] == ["E001", "E002"]
    assert rows[0].topical == "CICD_STANDARDS.md" and rows[0].routed is True
    assert rows[1].topical == "PROJECT_STANDARDS.md" and rows[1].routed is False
    assert rows[1].area == "zzz"


def test_build_rows_empty_area_label() -> None:
    rows = build_rows([_item(area="")])
    assert rows[0].area == "(unspecified)" and rows[0].routed is False


def test_render_worksheet_empty() -> None:
    assert render_worksheet([], "L051", "v1.2").startswith("No open entries to integrate.")


def test_render_worksheet_sequential_ids_and_flag() -> None:
    rows = build_rows(
        [
            _item(entry_id="E001", area="engineering", title="First"),
            _item(entry_id="E002", area="weird", title="Second"),
        ]
    )
    out = render_worksheet(rows, "L051", "v1.2")
    assert "vault next lesson L051" in out and "current Set Version v1.2" in out
    assert "2 open entries" in out
    assert "proposed: L051" in out and "proposed: L052" in out
    assert "ENGINEERING_STANDARDS.md" in out
    assert "⚠ unrouted" in out  # the second row (Area 'weird')


def test_render_worksheet_singular_entry() -> None:
    out = render_worksheet(build_rows([_item()]), "L051", "v1.2")
    assert "1 open entry;" in out


# --- parse_decisions ---------------------------------------------------------


def _decisions(tmp_path: Path, body: str) -> Path:
    p = tmp_path / "decisions.toml"
    p.write_text(body, encoding="utf-8")
    return p


def test_parse_decisions_integrated_and_rejected(tmp_path: Path) -> None:
    p = _decisions(
        tmp_path,
        """
[[integrated]]
project = "alpha"
entry = "E001"
lesson = "L051"
topical = "ENGINEERING_STANDARDS § 1.11"
set_version = "v1.3"

[[rejected]]
project = "beta"
entry = "E009"
reason = "project-specific, not portable"
""",
    )
    out = parse_decisions(p)
    assert out[0] == Disposition(
        "alpha",
        "E001",
        "integrated → vault L051 (ENGINEERING_STANDARDS § 1.11, Set Version v1.3)",
    )
    assert out[1] == Disposition("beta", "E009", "rejected — project-specific, not portable")


def test_parse_decisions_missing_file(tmp_path: Path) -> None:
    with pytest.raises(IntegrateError):
        parse_decisions(tmp_path / "nope.toml")


def test_parse_decisions_missing_key(tmp_path: Path) -> None:
    p = _decisions(tmp_path, '[[integrated]]\nproject = "alpha"\nentry = "E001"\n')
    with pytest.raises(IntegrateError):
        parse_decisions(p)


def test_parse_decisions_no_rows(tmp_path: Path) -> None:
    p = _decisions(tmp_path, "# nothing here\n")
    with pytest.raises(IntegrateError):
        parse_decisions(p)


def test_parse_decisions_bad_toml(tmp_path: Path) -> None:
    p = _decisions(tmp_path, "this is = = not valid toml [[[")
    with pytest.raises(IntegrateError):
        parse_decisions(p)


# --- apply_writeback (QA I / J / K) ------------------------------------------

_LOG = (
    "## E001 — first\n"
    "- Status:      open\n"
    "- Learned:     something\n"
    "\n"
    "## E002 — second\n"
    "- Status:      open\n"
)


def _log(tmp_path: Path) -> Path:
    p = tmp_path / "alpha" / "docs" / "STANDARDS_LOG.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(_LOG, encoding="utf-8")
    return p


def test_apply_writeback_dry_run_changes_nothing(tmp_path: Path) -> None:
    log = _log(tmp_path)
    before = log.read_text(encoding="utf-8")
    disp = [Disposition("alpha", "E001", "integrated → vault L051 (...)")]
    report = apply_writeback(disp, {"alpha": log}, write=False)
    assert log.read_text(encoding="utf-8") == before
    assert any("DRY-RUN" in line for line in report)


def test_apply_writeback_write_only_target_line(tmp_path: Path) -> None:
    log = _log(tmp_path)
    before = log.read_text(encoding="utf-8")
    new = "integrated → vault L051 (ENG § 1, Set Version v1.3)"
    disp = [Disposition("alpha", "E001", new)]
    apply_writeback(disp, {"alpha": log}, write=True)
    expected = before.replace(
        "## E001 — first\n- Status:      open\n",
        f"## E001 — first\n- Status:      {new}\n",
    )
    # Only E001's Status line changed; everything else is byte-identical.
    assert log.read_text(encoding="utf-8") == expected


def test_apply_writeback_unknown_project_no_write(tmp_path: Path) -> None:
    log = _log(tmp_path)
    before = log.read_text(encoding="utf-8")
    disp = [Disposition("ghost", "E001", "rejected — x")]
    with pytest.raises(IntegrateError):
        apply_writeback(disp, {"alpha": log}, write=True)
    assert log.read_text(encoding="utf-8") == before


def test_apply_writeback_missing_entry_is_atomic(tmp_path: Path) -> None:
    log = _log(tmp_path)
    before = log.read_text(encoding="utf-8")
    # First disposition is valid; the second names a missing entry — nothing must be written.
    disp = [
        Disposition("alpha", "E001", "rejected — a"),
        Disposition("alpha", "E999", "rejected — b"),
    ]
    with pytest.raises(IntegrateError):
        apply_writeback(disp, {"alpha": log}, write=True)
    assert log.read_text(encoding="utf-8") == before
