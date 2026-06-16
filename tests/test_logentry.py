# ==============================================================
# VERSION: 0.1
# Unit tests for the STANDARDS_LOG.md entry parser.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: id/title/fields, write-back, ordering, defaults.
# ==============================================================
"""Tests for standard_document_updater.logentry."""
from __future__ import annotations

from pathlib import Path

from standard_document_updater.logentry import LogEntry, parse_log


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_missing_file_returns_empty(tmp_path: Path) -> None:
    assert parse_log(tmp_path / "docs" / "STANDARDS_LOG.md") == []


def test_parses_id_title_and_fields(tmp_path: Path) -> None:
    log = tmp_path / "STANDARDS_LOG.md"
    _write(
        log,
        "## E001 — Surface plan defects before implementing\n"
        "- Date:        2026-06-13\n"
        "- Area:        governance\n"
        "- Status:      open\n"
        "- Context:     One line\n"
        "               continued line\n"
        "- Learned:     A takeaway\n"
        "- Portability: general\n",
    )
    (entry,) = parse_log(log)
    assert entry.entry_id == "E001"
    assert entry.title == "Surface plan defects before implementing"
    assert entry.area == "governance"
    assert entry.is_open
    assert entry.context == "One line continued line"
    assert entry.portability == "general"


def test_status_writeback_is_not_open(tmp_path: Path) -> None:
    log = tmp_path / "STANDARDS_LOG.md"
    _write(
        log,
        "## E002 — Already integrated\n"
        "- Status:      integrated → vault L050 (ENGINEERING § 1.1, Set v1.1)\n",
    )
    (entry,) = parse_log(log)
    assert entry.status == "integrated"
    assert not entry.is_open


def test_multiple_entries_in_order(tmp_path: Path) -> None:
    log = tmp_path / "STANDARDS_LOG.md"
    _write(
        log,
        "## E001 — First\n- Status:      open\n\n"
        "## E002 — Second\n- Status:      rejected — not portable\n\n"
        "## E003 — Third\n- Status:      open\n",
    )
    entries = parse_log(log)
    assert [e.entry_id for e in entries] == ["E001", "E002", "E003"]
    assert [e.is_open for e in entries] == [True, False, True]


def test_missing_fields_default_empty(tmp_path: Path) -> None:
    log = tmp_path / "STANDARDS_LOG.md"
    _write(log, "## E001 — Title only\n")
    (entry,) = parse_log(log)
    assert entry.area == "" and entry.status == "" and entry.learned == ""
    assert not entry.is_open


def test_logentry_defaults_construct_directly() -> None:
    entry = LogEntry(entry_id="E009", title="t", area="prompt", status="open")
    assert entry.is_open and entry.area == "prompt"
