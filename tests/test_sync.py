# ==============================================================
# VERSION: 0.1
# Unit tests for the section-aware sync engine (replace | merge | record).
#
# CHANGE LOG
# v0.1 — 2026-08-16 — Initial: header split/bump, TEMPLATE-ONLY strip, marker-block
#         pairing, merge_file (+ idempotence + mismatch), record_adoption,
#         plan_target / apply_actions / render_plan (PLAN-008).
# ==============================================================
"""Tests for standard_document_updater.sync."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest

from standard_document_updater import sync

_TODAY = "2026-08-16"
_SET = "v1.5"

_TEMPLATE = """<!-- VERSION: 2.0 -->
<!-- Last Updated: 2026-08-01 -->
<!--
CHANGE LOG
v2.0 — 2026-08-01 — suite text NEW.
-->

<!-- TEMPLATE-ONLY:BEGIN (stripped at instantiation; sync never propagates this block) -->
# FILE — (template)
> TEMPLATE banner.
<!-- TEMPLATE-ONLY:END -->
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# FILE — (fill me in)
<!-- PROJECT-OWNED:END -->

Suite paragraph NEW.

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
| placeholder row |
<!-- PROJECT-OWNED:END -->

Tail NEW.
"""

_TARGET = """<!-- VERSION: 1.3 -->
<!-- Last Updated: 2026-07-01 -->
<!--
CHANGE LOG
v1.3 — 2026-07-01 — a project edit.
-->

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# FILE — Acme (project-local)
<!-- PROJECT-OWNED:END -->

Suite paragraph OLD.

<!-- PROJECT-OWNED:BEGIN (custom note — kept verbatim) -->
| project row 1 |
| project row 2 |
<!-- PROJECT-OWNED:END -->

Tail OLD.
"""


# --- header split + bump ---------------------------------------------------------

def test_split_header_returns_header_and_body() -> None:
    header, body = sync.split_header(_TARGET, "t")
    assert header.endswith("-->\n")
    assert "CHANGE LOG" in header
    assert body.startswith("\n<!-- PROJECT-OWNED:BEGIN")


def test_split_header_missing_version_raises() -> None:
    with pytest.raises(sync.SyncError, match="no '<!-- VERSION"):
        sync.split_header("# no header\n", "t")


def test_bump_header_minor_bumps_and_logs() -> None:
    header, _ = sync.split_header(_TARGET, "t")
    out = sync.bump_header(header, _SET, _TODAY, "t")
    assert "<!-- VERSION: 1.4 -->" in out
    assert f"<!-- Last Updated: {_TODAY} -->" in out
    assert "v1.4 — 2026-08-16 — sync: Standard Set Version v1.5 applied" in out
    assert "v1.3 — 2026-07-01" in out  # prior log line kept


# --- merge -----------------------------------------------------------------------

def test_merge_preserves_owned_blocks_and_updates_suite_text() -> None:
    out = sync.merge_file(_TEMPLATE, _TARGET, _SET, _TODAY, "t")
    assert "# FILE — Acme (project-local)" in out          # owned block 1 kept
    assert "| project row 2 |" in out                      # owned block 2 kept
    assert "(custom note — kept verbatim)" in out          # target's own BEGIN comment kept
    assert "Suite paragraph NEW." in out                   # suite text updated
    assert "Tail NEW." in out
    assert "TEMPLATE banner." not in out                   # TEMPLATE-ONLY stripped
    assert "(fill me in)" not in out                       # template placeholder replaced
    assert "<!-- VERSION: 1.4 -->" in out                  # target's own header, bumped


def test_merge_is_idempotent() -> None:
    once = sync.merge_file(_TEMPLATE, _TARGET, _SET, _TODAY, "t")
    again = sync.merge_file(_TEMPLATE, once, _SET, _TODAY, "t")
    assert again == once  # body already matches -> returned unchanged, no re-bump


def test_merge_block_count_mismatch_raises() -> None:
    target = _TARGET.replace(
        "<!-- PROJECT-OWNED:BEGIN (custom note — kept verbatim) -->", ""
    ).replace("<!-- PROJECT-OWNED:END -->\n\nTail OLD.", "\nTail OLD.")
    with pytest.raises(sync.SyncError, match="count mismatch"):
        sync.merge_file(_TEMPLATE, target, _SET, _TODAY, "t")


def test_merge_unbalanced_markers_raise() -> None:
    broken = _TARGET.replace(
        "<!-- PROJECT-OWNED:END -->\n\nSuite paragraph OLD.", "\nSuite paragraph OLD."
    )
    with pytest.raises(sync.SyncError, match="BEGIN without END|END without BEGIN|nested"):
        sync.merge_file(_TEMPLATE, broken, _SET, _TODAY, "t")


# --- record ----------------------------------------------------------------------

def test_record_adoption_updates_bullets_row_and_header(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    _, target = make_suite_pair()
    text = (target / "docs" / "SET_VERSION_ADOPTED.md").read_text(encoding="utf-8")
    out = sync.record_adoption(text, _SET, _TODAY, "sva")
    assert "- **Standard Set Version:** v1.5 (synced from the vault by the engine" in out
    assert f"- **Adopted on:** {_TODAY} (synced)" in out
    assert "| v1.5 | 2026-08-16 | sync (engine):" in out
    assert "| v1.4 | 2026-07-01 | Initial bootstrap |" in out  # history kept below
    assert "<!-- VERSION: 1.1 -->" in out
    assert out.index("| v1.5 |") < out.index("| v1.4 |")       # newest row on top


def test_record_adoption_without_table_raises() -> None:
    text = (
        "<!-- VERSION: 1.0 -->\n<!--\nCHANGE LOG\nv1.0 — x.\n-->\n"
        "- **Standard Set Version:** v1.4\n"
    )
    with pytest.raises(sync.SyncError, match="backport-tracking table"):
        sync.record_adoption(text, _SET, _TODAY, "sva")


# --- plan / apply / render -------------------------------------------------------

def test_plan_target_covers_every_sync_map_file(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    vault, target = make_suite_pair()
    actions = sync.plan_target(vault, target, _SET, _TODAY)
    assert len(actions) == len(sync.SYNC_MAP)
    assert all(a.changed for a in actions)  # the fixture adopter is one Set Version behind
    modes = {a.target_rel: a.mode for a in actions}
    assert modes["CLAUDE.md"] == "merge"
    assert modes["archive/LESSONS.md"] == "replace"
    assert modes["docs/SET_VERSION_ADOPTED.md"] == "record"


def test_plan_target_missing_file_raises(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    vault, target = make_suite_pair()
    (target / "archive" / "LESSONS.md").unlink()
    with pytest.raises(sync.SyncError, match="target file missing: archive/LESSONS.md"):
        sync.plan_target(vault, target, _SET, _TODAY)


def test_apply_then_replan_is_all_up_to_date(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    vault, target = make_suite_pair()
    actions = sync.plan_target(vault, target, _SET, _TODAY)
    written = sync.apply_actions(target, actions)
    assert Path("CLAUDE.md") in written and Path("archive/LESSONS.md") in written
    replay = sync.plan_target(vault, target, _SET, _TODAY)
    assert not any(a.changed for a in replay)  # idempotence: second run writes nothing
    merged = (target / "CLAUDE.md").read_text(encoding="utf-8")
    assert "Acme CLI." in merged                      # owned block survived the real write
    assert "## 3. Rules NEW." in merged               # suite section updated
    replaced = (target / "docs" / "standards" / "PROJECT_STANDARDS.md").read_text(encoding="utf-8")
    assert replaced == (vault / "docs" / "standards" / "PROJECT_STANDARDS.md").read_text(
        encoding="utf-8"
    )


def test_apply_actions_skips_unchanged(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    vault, target = make_suite_pair()
    sync.apply_actions(target, sync.plan_target(vault, target, _SET, _TODAY))
    assert sync.apply_actions(target, sync.plan_target(vault, target, _SET, _TODAY)) == []


def test_render_plan_reports_and_diffs(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    vault, target = make_suite_pair()
    actions = sync.plan_target(vault, target, _SET, _TODAY)
    text = sync.render_plan("acme", actions, show_diff=True)
    assert "[acme]" in text and "need sync" in text
    assert "merge   CLAUDE.md" in text
    assert "--- a/CLAUDE.md" in text                  # unified diff present under --diff
    sync.apply_actions(target, actions)
    done = sync.render_plan("acme", sync.plan_target(vault, target, _SET, _TODAY), show_diff=False)
    assert "up-to-date" in done
