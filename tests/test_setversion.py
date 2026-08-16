# ==============================================================
# VERSION: 0.2
# Unit tests for setversion parsers.
#
# CHANGE LOG
# v0.2 — 2026-08-16 — DD-1: pin the delegated semantics — Status must equal 'open'
#         (case-insensitive), not merely start with it.
# v0.1 — 2026-06-16 13:01 — Initial: version parsing + open-log counting.
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


def test_count_open_log_entries_requires_exact_open(tmp_path: Path) -> None:
    log = tmp_path / "STANDARDS_LOG.md"
    log.write_text(
        "## E001 — a\n- Status:      open\n\n"
        "## E002 — b\n- Status:      opened by mistake\n\n"
        "## E003 — c\n- Status:      Open\n\n",
        encoding="utf-8",
    )
    # DD-1: delegated to logentry.is_open — exact 'open' (case-insensitive), not startswith
    assert setversion.count_open_log_entries(log) == 2
