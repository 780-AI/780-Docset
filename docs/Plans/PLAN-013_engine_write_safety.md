<!-- VERSION: 0.2 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Status: APPROVED (Phase 2 landed 2026-10-03 — operator: "approve plan 013"; Phase 3 runs in this fresh session) -->
<!--
CHANGE LOG
v0.2 — 2026-10-03 — Phase 2 operator approval recorded ("approve plan 013"); § 9.1 decision record
added (D-1…D-5 at the recommended options). Status DRAFT → APPROVED. No design change.
v0.1 — 2026-10-03 — Initial draft (Phase 0 audit + Phase 1 design). Code developed + tool-proven in a
scratch overlay FIRST (proven-code-first): ruff clean; mypy error SET identical to baseline (42 full
/ 25 src, line numbers stripped); pytest 119 passed (111 + 8 new). Feature behavior previewed
read-only on real fleet data (both live targets flagged as holding un-landed handoffs;
Capital-Signal's real pre-accumulation handoff wrapped as Write 1 + v2.6 appended). Rule 13 pass
recorded at the foot of this file same-day (code blocks re-extracted from this file and re-proven;
1 finding fixed — QA-K3 cleanup step; 1 optimization considered and declined — log entry dates in
the floor).
-->

# PLAN-013 — Engine write safety: clock floor + accumulating handoffs

## 1. Goal

Make every engine write into a target safe against the two failure modes found in live operation:

1. **A drifted clock stamping wrong dates (780-VPN E001, lesson L079).** The engine takes "today"
   from the curator machine's wall clock; when that clock ran ~9 days slow, syncs wrote stamps
   dated before the target's own history, and a re-sync cannot repair them. Fix: before any write,
   both write paths compute the target's **newest stamp** and **refuse** when the local clock reads
   earlier; the sync dry-run warns instead.
2. **Handoffs overwritten by later writes (found 2026-10-03).** `render_handoff` rewrites
   `docs/SYNC_HANDOFF.md` on every write, so a second write before the target lands the first
   erases the first write's explanation (live: Capital-Signal holds 7 engine-modified files while
   its handoff lists 3). Fix: an un-landed handoff's write records are **kept** and the new write is
   **appended** as the next `### Write N` record.

Engine-only: no suite content changes → **no Standard Set Version bump**. Shipping this lifts the
PLAN-011 § 9.1 pre-write hold and the Capital-Signal v2.6 hold (D-5).

## 2. Operator constraints

- Every engine write path (sync `--write` AND the integrate write-back) — the PLAN-012 principle.
- Dry-run / worksheet behavior unchanged except the two informational lines (warning, note).
- Handoffs already in the field (PLAN-012 single-write format) must be preserved, never dropped.
- Nothing is written to a target when the guard refuses (checked before the first write).
- The SESSION_OPENER § 1.1 handoff check needs no change (still "read first, land per § 2, delete").

## 3. Scope summary

- **Engine (`sync.py`):** `_prior_records` + accumulating `render_handoff(…, existing=None)`;
  `newest_stamp(target_root)` (stamp positions only: `Last Updated` headers + `vX.Y — date — `
  change-log lines across the SYNC_MAP files + `docs/STANDARDS_LOG.md`); `check_clock(project,
  today, floor)` raising `SyncError` when behind.
- **Engine (`cli.py`):** `_cmd_integrate` computes `today` up front and checks EVERY target before
  `apply_writeback`; both write sites read an existing handoff and pass it in; `_cmd_sync` warns in
  dry-run (clock behind / un-landed handoff) and checks before `apply_actions`.
- **Tests:** 5 unit (`test_sync.py`) + 3 end-to-end (`test_cli.py`).
- **Docs:** architecture § 7 paragraph + § 9 invariant (§ 4 drift rule); PLAN-012 § 11 closed-risk
  annotation (§ 15.4).
- **Out of scope:** an HTTP-Date external-authority check (D-1 option B); GitHub PR delivery
  (PLAN-014, where the handoff may move into the PR body); retroactive listing of Capital-Signal's
  v2.1–v2.4 writes (the new § 2 step-1 sentence covers unlisted suite files).

### Phase 0 audit findings (2026-10-03, live source at `03fa0dd`)

- **Clock sources:** `cli.py` `_cmd_integrate` (`today = date.today()`, inside `if args.write`,
  AFTER `apply_writeback` already wrote the logs) and `_cmd_sync` (`today = date.today()` at the top).
  Neither compares the date with anything.
- **Handoff writes:** both sites call `(root / sync.HANDOFF_REL).write_text(render_handoff(…))` —
  an unconditional overwrite.
- **Live evidence:** Capital-Signal handoff lists v2.5's 3 files while `git status` shows 7
  engine-modified files + the handoff (v2.1 → v2.5); 780-VPN holds the un-landed v2.6 handoff.
- **Live floors (overlay preview):** Capital-Signal `2026-09-05`, 780-VPN `2026-10-03` (= today —
  equal is allowed, so no false refusal today).
- **Test fixtures** stamp `2026-07-01` / `2026-08-01` — all past, so existing tests are unaffected
  (confirmed: the 111 baseline tests pass unmodified in the overlay).
- **Baseline:** ruff clean; mypy 42 errors full config / 25 `src` (pre-existing); pytest 111.

## 4. Phase tracker (high-level — granular sub-tasks in `PLAN-013_tracker.md`)

- Phase 0 — Audit: ✅ 2026-10-03
- Phase 1 — Design + Rule 13 pass: ✅ 2026-10-03
- Phase 2 — Operator approval (D13.A + D-1…D-5): ✅ 2026-10-03 — "approve plan 013" (§ 9.1)
- Phase 3 — Implement (fresh session, single commit): ⏸
- Phase 4 — Validate (QA-K1…K6): ⏸
- Phase 5 — Operator gate (push): ⏸

## 5. Verbatim transformation rules (code proven in overlay; Phase 3 copies byte-for-byte)

**Mechanical rule:** every `<P3-DATE>` token is replaced with the Phase 3 date, verified against an
external clock first (L079 / PROJECT_STANDARDS § 5.6) — the overlay was proven with a 10-character
ISO date in its place (line widths measured at ship form). Apply in label order; each FIND matches
exactly once in live source at `03fa0dd`.

### 5a — `src/standard_document_updater/sync.py` — header 0.2 → 0.3

FIND (exact; matches once):

`````text
# VERSION: 0.2
# Section-aware suite propagation (`sync`): replace | merge | record per file.
#
# CHANGE LOG
`````

REPLACE:

`````text
# VERSION: 0.3
# Section-aware suite propagation (`sync`): replace | merge | record per file.
#
# CHANGE LOG
# v0.3 — <P3-DATE> — PLAN-013: handoffs ACCUMULATE (an un-landed handoff's write records are
#         kept and the new write appended as the next record) + newest_stamp / check_clock —
#         the floor guard that refuses an engine write when the local clock is behind the
#         target's newest stamp (L079).
`````

### 5b — `src/standard_document_updater/sync.py` — accumulating `render_handoff` (+ `_prior_records`)

FIND (exact; matches once):

`````text
HANDOFF_REL = Path("docs/SYNC_HANDOFF.md")


def render_handoff(
    project_name: str, operation: str, set_version: str, today: str, files: list[tuple[str, str]]
) -> str:
    """The handoff report every engine write leaves in the target (PLAN-012).

    Written on every write — `sync --write` and the integrate write-back — so
    the target's NEXT session finds engine-landed changes explained: what was
    written, by which operation and vault release, and the residual bookkeeping
    the engine deliberately leaves to the target (manifest cells, CHANGELOG
    entry, the landing commit). The target session deletes the file in the
    commit that lands the changes; the next engine write recreates it.
    """
    lines = [
        "# SYNC HANDOFF — engine-written changes landed in this repository",
        "",
        "> **READ ME FIRST.** The Standard DocSet engine wrote the files below directly",
        "> into this working tree. They are NOT unexplained local edits. Land them per § 2,",
        "> then DELETE this file in that same commit.",
        "",
        "## 1. What the engine did",
        "",
        f"- **Project:** {project_name}",
        f"- **Operation:** {operation}",
        f"- **Vault Standard Set Version:** {set_version}",
        f"- **Run date:** {today} (stamped by the curator machine's clock — if stamp ordering",
        "  looks wrong against local history, trust an external time authority)",
        "- **Files written (suite-owned sections updated; PROJECT-OWNED blocks preserved):**",
    ]
    for rel, mode in files:
        lines.append(f"  - `{rel}` ({mode})")
    lines += [
        "",
        "## 2. What this project's next session must do (the engine does NOT do these)",
        "",
        "1. Review the diffs (`git diff`) against the file list above.",
`````

REPLACE:

`````text
HANDOFF_REL = Path("docs/SYNC_HANDOFF.md")

_HANDOFF_S1 = "## 1. What the engine did\n"
_HANDOFF_S2 = "## 2. What this project's next session must do"
_WRITE_HEADING_RE = re.compile(r"^### Write \d+", re.MULTILINE)
_PROJECT_LINE_RE = re.compile(r"^- \*\*Project:\*\*[^\n]*\n", re.MULTILINE)


def _prior_records(existing: str) -> tuple[str, int]:
    """Write records kept verbatim from an un-landed handoff, plus how many there are.

    PLAN-013: a second engine write before the target lands the first must not
    erase the first write's explanation. Three shapes: the accumulating format
    (`### Write N` records), the single-write PLAN-012 format (wrapped as one
    record), and anything else (kept verbatim in a fence — nothing is lost).
    """
    start = existing.find(_HANDOFF_S1)
    end = existing.find(_HANDOFF_S2)
    if start == -1 or end < start:
        fenced = f"````text\n{existing.rstrip()}\n````"
        return f"### Write 1 — earlier handoff (unrecognized format, kept verbatim)\n\n{fenced}", 1
    body = _PROJECT_LINE_RE.sub("", existing[start + len(_HANDOFF_S1) : end], count=1).strip()
    if not body:
        return "", 0
    count = len(_WRITE_HEADING_RE.findall(body))
    if count:
        return body, count
    return f"### Write 1 — earlier engine write\n\n{body}", 1


def render_handoff(
    project_name: str,
    operation: str,
    set_version: str,
    today: str,
    files: list[tuple[str, str]],
    existing: str | None = None,
) -> str:
    """The handoff report every engine write leaves in the target (PLAN-012).

    Written on every write — `sync --write` and the integrate write-back — so
    the target's NEXT session finds engine-landed changes explained: what was
    written, by which operation and vault release, and the residual bookkeeping
    the engine deliberately leaves to the target (manifest cells, CHANGELOG
    entry, the landing commit). The target session deletes the file in the
    commit that lands the changes. PLAN-013: when the target still holds an
    un-landed handoff (`existing`), its write records are kept and this write is
    appended as the next record — every write since the last landing stays listed.
    """
    prior, count = _prior_records(existing) if existing is not None else ("", 0)
    lines = [
        "# SYNC HANDOFF — engine-written changes landed in this repository",
        "",
        "> **READ ME FIRST.** The Standard DocSet engine wrote the files below directly",
        "> into this working tree. They are NOT unexplained local edits. Land them per § 2,",
        "> then DELETE this file in that same commit. If several writes are listed, land them",
        "> ALL in that one commit.",
        "",
        "## 1. What the engine did",
        "",
        f"- **Project:** {project_name}",
        "",
    ]
    if prior:
        lines += [prior, ""]
    lines += [
        f"### Write {count + 1}",
        "",
        f"- **Operation:** {operation}",
        f"- **Vault Standard Set Version:** {set_version}",
        f"- **Run date:** {today} (stamped by the curator machine's clock — the engine refuses",
        "  to stamp behind this repository's newest stamp; if ordering still looks wrong",
        "  against local history, trust an external time authority)",
        "- **Files written (suite-owned sections updated; PROJECT-OWNED blocks preserved):**",
    ]
    for rel, mode in files:
        lines.append(f"  - `{rel}` ({mode})")
    lines += [
        "",
        "## 2. What this project's next session must do (the engine does NOT do these)",
        "",
        "1. Review the diffs (`git diff`) against EVERY file list above. Suite files modified but",
        "   listed in no record come from engine writes made before handoffs accumulated —",
        "   review them against the vault and land them in the same commit.",
`````

### 5c — `src/standard_document_updater/sync.py` — handoff footer + clock floor (`newest_stamp`, `check_clock`) appended at end of file

FIND (exact; matches once):

`````text
        "*Engine-generated on every engine write; the next write rewrites it.*",
        "",
    ]
    return "\n".join(lines)
`````

REPLACE:

`````text
        "*Engine-generated on every engine write; a later write before landing appends to it.*",
        "",
    ]
    return "\n".join(lines)


_STAMP_RES = (
    re.compile(r"<!-- Last Updated: (\d{4}-\d{2}-\d{2}) -->"),
    re.compile(r"^v\d+\.\d+ — (\d{4}-\d{2}-\d{2}) — ", re.MULTILINE),
)
_STAMPED_RELS = (*(item.target_rel for item in SYNC_MAP), "docs/STANDARDS_LOG.md")


def newest_stamp(target_root: Path) -> str | None:
    """Newest header / CHANGE LOG date (ISO text) in the target's engine-touched files, or None.

    PLAN-013 (L079): the floor the local clock must not be behind before any
    engine write stamps dates into this target. Only stamp positions count
    (`Last Updated` headers + `vX.Y — YYYY-MM-DD — ` change-log lines), never
    dates quoted in prose.
    """
    newest: str | None = None
    for rel in _STAMPED_RELS:
        path = target_root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in _STAMP_RES:
            for match in pattern.finditer(text):
                if newest is None or match.group(1) > newest:
                    newest = match.group(1)
    return newest


def check_clock(project_name: str, today: str, floor: str | None) -> None:
    """Refuse an engine write when the local clock is behind the target's newest stamp (L079)."""
    if floor is not None and today < floor:
        raise SyncError(
            f"{project_name}: refusing to write — the local clock reads {today} but this target "
            f"already carries a stamp dated {floor} (the clock is behind, L079). Verify the "
            "clock against an external time authority and fix it; if the target's stamp is the "
            "wrong one, correct it there (PROJECT_STANDARDS § 5.6) and re-run."
        )
`````

### 5d — `src/standard_document_updater/cli.py` — header 0.6 → 0.7

FIND (exact; matches once):

`````text
# VERSION: 0.6
# Command-line interface: `python -m standard_document_updater <command>`.
#
# CHANGE LOG
`````

REPLACE:

`````text
# VERSION: 0.7
# Command-line interface: `python -m standard_document_updater <command>`.
#
# CHANGE LOG
# v0.7 — <P3-DATE> — PLAN-013: both engine write paths (sync --write + integrate write-back)
#                     refuse when the local clock is behind the target's newest stamp, and
#                     append to an un-landed handoff instead of overwriting it; the sync
#                     dry-run warns about a behind clock and notes an un-landed handoff.
`````

### 5e — `src/standard_document_updater/cli.py` — integrate write path (guard before ANY write; append to an un-landed handoff)

FIND (exact; matches once):

`````text
        log_path_for = {name: root / "docs" / "STANDARDS_LOG.md" for name, root in roots.items()}
        report_lines = integrate.apply_writeback(dispositions, log_path_for, write=args.write)
        if args.write:
            set_version = "v" + ".".join(str(n) for n in setversion.parse_vault_version(index))
            today = date.today().isoformat()
            count = len(dispositions)
            message = f"Standard DocSet: integrate write-back ({count} status update(s))"
            for name in sorted(named & set(targets)):
                (roots[name] / sync.HANDOFF_REL).write_text(
                    sync.render_handoff(
                        name,
                        "integrate write-back",
                        set_version,
                        today,
                        [("docs/STANDARDS_LOG.md", "write-back")],
                    ),
                    encoding="utf-8",
                )
`````

REPLACE:

`````text
        log_path_for = {name: root / "docs" / "STANDARDS_LOG.md" for name, root in roots.items()}
        today = date.today().isoformat()
        if args.write:  # clock floor (L079) checked for EVERY target before ANY write
            for name, root in roots.items():
                sync.check_clock(name, today, sync.newest_stamp(root))
        report_lines = integrate.apply_writeback(dispositions, log_path_for, write=args.write)
        if args.write:
            set_version = "v" + ".".join(str(n) for n in setversion.parse_vault_version(index))
            count = len(dispositions)
            message = f"Standard DocSet: integrate write-back ({count} status update(s))"
            for name in sorted(named & set(targets)):
                handoff = roots[name] / sync.HANDOFF_REL
                existing = handoff.read_text(encoding="utf-8") if handoff.is_file() else None
                handoff.write_text(
                    sync.render_handoff(
                        name,
                        "integrate write-back",
                        set_version,
                        today,
                        [("docs/STANDARDS_LOG.md", "write-back")],
                        existing,
                    ),
                    encoding="utf-8",
                )
`````

### 5f — `src/standard_document_updater/cli.py` — sync path (dry-run warning + note; guard before `apply_actions`; append)

FIND (exact; matches once):

`````text
                print(sync.render_plan(project.name, actions, show_diff=args.diff))
                changed = [a for a in actions if a.changed]
                if args.write and changed:
                    written = sync.apply_actions(root, changed)
                    (root / sync.HANDOFF_REL).write_text(
                        sync.render_handoff(
                            project.name,
                            "sync --write",
                            set_version,
                            today,
                            [(a.target_rel, a.mode) for a in changed],
                        ),
                        encoding="utf-8",
                    )
                    written.append(sync.HANDOFF_REL)
                    message = f"Standard DocSet: sync to Standard Set Version {set_version}"
                    target.flush(root, written, message)
                    print(f"  -> wrote + flushed {len(written)} file(s) (incl. the handoff)")
`````

REPLACE:

`````text
                print(sync.render_plan(project.name, actions, show_diff=args.diff))
                floor = sync.newest_stamp(root)
                handoff = root / sync.HANDOFF_REL
                existing = handoff.read_text(encoding="utf-8") if handoff.is_file() else None
                if not args.write:
                    if floor is not None and today < floor:
                        print(
                            f"  warning: the local clock ({today}) is behind this target's "
                            f"newest stamp ({floor}) — a --write would refuse (L079)"
                        )
                    if existing is not None:
                        print(
                            "  note: this target holds an un-landed docs/SYNC_HANDOFF.md — "
                            "a --write appends to it"
                        )
                changed = [a for a in actions if a.changed]
                if args.write and changed:
                    sync.check_clock(project.name, today, floor)
                    written = sync.apply_actions(root, changed)
                    handoff.write_text(
                        sync.render_handoff(
                            project.name,
                            "sync --write",
                            set_version,
                            today,
                            [(a.target_rel, a.mode) for a in changed],
                            existing,
                        ),
                        encoding="utf-8",
                    )
                    written.append(sync.HANDOFF_REL)
                    message = f"Standard DocSet: sync to Standard Set Version {set_version}"
                    target.flush(root, written, message)
                    print(f"  -> wrote + flushed {len(written)} file(s) (incl. the handoff)")
                    if existing is not None:
                        print(
                            "  note: appended to an un-landed handoff — earlier engine writes "
                            "stay listed"
                        )
`````

### 5g-header — `tests/test_sync.py` — header 0.1 → 0.2

FIND (exact; matches once):

`````text
# VERSION: 0.1
# Unit tests for the section-aware sync engine (replace | merge | record).
#
# CHANGE LOG
`````

REPLACE:

`````text
# VERSION: 0.2
# Unit tests for the section-aware sync engine (replace | merge | record).
#
# CHANGE LOG
# v0.2 — <P3-DATE> — PLAN-013: newest_stamp (stamp positions only), check_clock (refuses only
#         when behind), render_handoff accumulation (first write, append, pre-accumulation
#         format wrapped, unrecognized format kept verbatim).
`````

### 5g-tests — `tests/test_sync.py` — five new tests appended at end of file

FIND (exact; matches once):

`````text
    sync.apply_actions(target, actions)
    done = sync.render_plan("acme", sync.plan_target(vault, target, _SET, _TODAY), show_diff=False)
    assert "up-to-date" in done
`````

REPLACE:

`````text
    sync.apply_actions(target, actions)
    done = sync.render_plan("acme", sync.plan_target(vault, target, _SET, _TODAY), show_diff=False)
    assert "up-to-date" in done


def test_newest_stamp_reads_stamp_positions_only(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "SESSION_OPENER.md").write_text(
        "<!-- VERSION: 1.1 -->\n<!-- Last Updated: 2026-09-02 -->\n<!--\nCHANGE LOG\n"
        "v1.1 — 2026-09-02 — x.\nv1.0 — 2026-08-01 — y.\n-->\n",
        encoding="utf-8",
    )
    (docs / "STANDARDS_LOG.md").write_text(
        "<!-- Last Updated: 2026-09-05 -->\nProse mentions 2027-01-01, not a stamp.\n",
        encoding="utf-8",
    )
    assert sync.newest_stamp(tmp_path) == "2026-09-05"
    assert sync.newest_stamp(tmp_path / "missing") is None


def test_check_clock_refuses_only_when_behind() -> None:
    sync.check_clock("acme", "2026-09-05", None)
    sync.check_clock("acme", "2026-09-05", "2026-09-05")
    sync.check_clock("acme", "2026-09-06", "2026-09-05")
    with pytest.raises(sync.SyncError, match="clock is behind"):
        sync.check_clock("acme", "2026-08-27", "2026-09-02")


def test_render_handoff_appends_records_to_an_unlanded_handoff() -> None:
    first = sync.render_handoff("acme", "sync --write", "v1.5", _TODAY, [("CLAUDE.md", "merge")])
    assert "### Write 1" in first and "### Write 2" not in first
    second = sync.render_handoff(
        "acme",
        "integrate write-back",
        "v1.5",
        _TODAY,
        [("docs/STANDARDS_LOG.md", "write-back")],
        first,
    )
    assert second.count("- **Project:** acme") == 1
    assert second.index("### Write 1") < second.index("### Write 2")
    assert "`CLAUDE.md` (merge)" in second and "`docs/STANDARDS_LOG.md` (write-back)" in second
    third = sync.render_handoff(
        "acme", "sync --write", "v1.6", _TODAY, [("a.md", "replace")], second
    )
    assert third.count("### Write ") == 3 and "### Write 3" in third


_LEGACY_HANDOFF = """# SYNC HANDOFF — engine-written changes landed in this repository

> **READ ME FIRST.** The Standard DocSet engine wrote the files below directly
> into this working tree. They are NOT unexplained local edits. Land them per § 2,
> then DELETE this file in that same commit.

## 1. What the engine did

- **Project:** acme
- **Operation:** sync --write
- **Vault Standard Set Version:** v1.4
- **Run date:** 2026-08-01 (stamped by the curator machine's clock — if stamp ordering
  looks wrong against local history, trust an external time authority)
- **Files written (suite-owned sections updated; PROJECT-OWNED blocks preserved):**
  - `archive/LESSONS.md` (replace)

## 2. What this project's next session must do (the engine does NOT do these)

1. Review the diffs (`git diff`) against the file list above.
"""


def test_render_handoff_wraps_a_pre_accumulation_handoff() -> None:
    text = sync.render_handoff(
        "acme", "sync --write", _SET, _TODAY, [("a.md", "replace")], _LEGACY_HANDOFF
    )
    assert "### Write 1 — earlier engine write" in text
    assert "- **Vault Standard Set Version:** v1.4" in text
    assert "`archive/LESSONS.md` (replace)" in text
    assert "### Write 2" in text and text.count("- **Project:**") == 1


def test_render_handoff_keeps_an_unrecognized_handoff_verbatim() -> None:
    text = sync.render_handoff(
        "acme", "sync --write", _SET, _TODAY, [("a.md", "replace")], "hand-edited notes\n"
    )
    assert "unrecognized format, kept verbatim" in text and "hand-edited notes" in text
    assert "### Write 2" in text
`````

### 5h-header — `tests/test_cli.py` — header 0.6 → 0.7

FIND (exact; matches once):

`````text
# VERSION: 0.6
# End-to-end tests for the CLI (status / drift / harvest / integrate / sync).
#
# CHANGE LOG
`````

REPLACE:

`````text
# VERSION: 0.7
# End-to-end tests for the CLI (status / drift / harvest / integrate / sync).
#
# CHANGE LOG
# v0.7 — <P3-DATE> — PLAN-013: a second sync --write appends to the un-landed handoff (dry-run
#         notes it); a behind clock makes the sync dry-run warn and --write refuse (exit 1,
#         nothing written) and the integrate write-back refuse (exit 2, log untouched).
`````

### 5h-imports — `tests/test_cli.py` — imports (`date`, `cli`)

FIND (exact; matches once):

`````text
from collections.abc import Callable
from pathlib import Path

import pytest

from standard_document_updater import transport
from standard_document_updater.cli import main
`````

REPLACE:

`````text
from collections.abc import Callable
from datetime import date
from pathlib import Path

import pytest

from standard_document_updater import cli, transport
from standard_document_updater.cli import main
`````

### 5h-tests — `tests/test_cli.py` — `_BehindDate` + three new tests inserted immediately BEFORE `def test_sync_unknown_project_filter_errors(`

FIND (exact; matches once):

`````text
def test_sync_unknown_project_filter_errors(`````

REPLACE:

`````text
class _BehindDate(date):
    """A local clock reading 2026-07-01 — behind the fixtures' 2026-08-01 stamps."""

    @classmethod
    def today(cls) -> _BehindDate:
        return cls(2026, 7, 1)


def test_sync_second_write_appends_to_unlanded_handoff(
    make_suite_pair: MakePair, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("acme", target)])
    assert main(["--vault", str(vault), "sync", "--write"]) == 0
    std = vault / "docs" / "standards" / "PROJECT_STANDARDS.md"
    std.write_text(std.read_text(encoding="utf-8") + "\nSuite text NEWER.\n", encoding="utf-8")
    capsys.readouterr()
    assert main(["--vault", str(vault), "sync"]) == 0
    assert "holds an un-landed docs/SYNC_HANDOFF.md" in capsys.readouterr().out
    assert main(["--vault", str(vault), "sync", "--write"]) == 0
    assert "appended to an un-landed handoff" in capsys.readouterr().out
    handoff = (target / "docs" / "SYNC_HANDOFF.md").read_text(encoding="utf-8")
    assert "`CLAUDE.md` (merge)" in handoff  # the first write's list survives
    second = handoff[handoff.index("### Write 2") : handoff.index("## 2.")]
    assert "`docs/standards/PROJECT_STANDARDS.md` (replace)" in second
    assert "CLAUDE.md" not in second


def test_sync_refuses_when_clock_is_behind_target_stamp(
    make_suite_pair: MakePair,
    write_registry: Make,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("acme", target)])
    monkeypatch.setattr(cli, "date", _BehindDate)
    before = (target / "CLAUDE.md").read_text(encoding="utf-8")
    assert main(["--vault", str(vault), "sync"]) == 0
    assert "a --write would refuse (L079)" in capsys.readouterr().out
    assert main(["--vault", str(vault), "sync", "--write"]) == 1
    assert "clock is behind" in capsys.readouterr().err
    assert (target / "CLAUDE.md").read_text(encoding="utf-8") == before
    assert not (target / "docs" / "SYNC_HANDOFF.md").exists()


def test_integrate_write_refuses_when_clock_is_behind(
    make_vault: Make,
    make_project: Make,
    write_registry: Make,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", open_entries=1)
    log = proj / "docs" / "STANDARDS_LOG.md"
    stamped = "<!-- Last Updated: 2026-08-01 -->\n" + log.read_text(encoding="utf-8")
    log.write_text(stamped, encoding="utf-8")
    write_registry(root, [("alpha", proj)])
    before = log.read_text(encoding="utf-8")
    decisions = tmp_path / "decisions.toml"
    decisions.write_text(
        '[[rejected]]\nproject = "alpha"\nentry = "E001"\nreason = "n/a"\n',
        encoding="utf-8",
    )
    monkeypatch.setattr(cli, "date", _BehindDate)
    assert main(["--vault", str(root), "integrate", "--apply", str(decisions), "--write"]) == 2
    assert "clock is behind" in capsys.readouterr().err
    assert log.read_text(encoding="utf-8") == before
    assert not (proj / "docs" / "SYNC_HANDOFF.md").exists()


def test_sync_unknown_project_filter_errors(`````

## 6. Spec update map (same commit as Phase 3) — verbatim

### 6a — `docs/architecture.md` — header 0.12 → 0.13 + CHANGE LOG line

FIND (exact; matches once):

`````text
<!-- VERSION: 0.12 -->
<!-- Last Updated: 2026-09-05 -->
<!--
CHANGE LOG
`````

REPLACE:

`````text
<!-- VERSION: 0.13 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.13 — <P3-DATE> — PLAN-013 (engine write safety) landed. § 7 handoff paragraph: handoffs ACCUMULATE (an un-landed handoff's `### Write N` records are kept and the new write appended; a pre-accumulation handoff is wrapped as record 1; an unrecognized one is kept verbatim) + the clock floor (newest_stamp / check_clock refuse a write whose date precedes the target's newest stamp; the sync dry-run warns). § 9 gains the never-stamp-behind invariant. Engine-only — no Set Version change.
`````

### 6b — `docs/architecture.md` § 7 — accumulation + clock-floor paragraph after the handoff paragraph

FIND (exact; matches once):

`````text
SESSION_OPENER template's § 1.1 engine-handoff check.
`````

REPLACE:

`````text
SESSION_OPENER template's § 1.1 engine-handoff check.
**Accumulation + clock floor (PLAN-013).** When the target still holds an un-landed handoff, the
engine keeps its write records verbatim and appends the new write as the next `### Write N`
record (a pre-accumulation single-write handoff is wrapped as record 1; an unrecognized file is
kept verbatim in a fence), so the target's next session sees every engine write since its last
landing; the sync dry-run notes an un-landed handoff. Before stamping, both write paths take the
target's newest stamp (`sync.newest_stamp` — `Last Updated` headers + `vX.Y — date — ` change-log
lines across the SYNC_MAP files + `docs/STANDARDS_LOG.md`) and refuse (`sync.check_clock`) when
the local clock reads earlier (L079); the sync dry-run warns instead of refusing.
`````

### 6c — `docs/architecture.md` § 9 — never-stamp-behind invariant

FIND (exact; matches once):

`````text
- **Sync never clobbers** a `PROJECT-OWNED` block.
`````

REPLACE:

`````text
- **Sync never clobbers** a `PROJECT-OWNED` block.
- **The engine never stamps behind a target** (PLAN-013, L079): a write whose date precedes the
  target's newest stamp is refused before any file is touched.
`````

### 6d — `docs/Plans/PLAN-012_sync_handoff.md` — header 1.0 → 1.1

FIND (exact; matches once):

`````text
<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-09-05 -->
`````

REPLACE:

`````text
<!-- VERSION: 1.1 -->
<!-- Last Updated: <P3-DATE> -->
`````

### 6e — `docs/Plans/PLAN-012_sync_handoff.md` — CHANGE LOG line

FIND (exact; matches once):

`````text
CHANGE LOG
v1.0 — 2026-09-05 —`````

REPLACE:

`````text
CHANGE LOG
v1.1 — <P3-DATE> — Closed-risk annotation (§ 15.4, PLAN-013 Phase 3): § 11 clock-caveat risk CLOSED (newest-stamp floor shipped); stale-handoff row notes the next write now appends.
v1.0 — 2026-09-05 —`````

### 6f — `docs/Plans/PLAN-012_sync_handoff.md` § 11 — closed-risk annotation (§ 15.4)

FIND (exact; matches once):

`````text
  reader is forced at session start) and by the next engine write rewriting it.
- **Clock caveat**: the run-date line carries the trust note; the real fix (trusted time source /
  newest-stamp floor) is E001's suggestion and arrives via its own gated intake.
`````

REPLACE:

`````text
  reader is forced at session start) and by the next engine write rewriting it. *(PLAN-013,
  <P3-DATE>: the next write now APPENDS to an un-landed handoff; the sync dry-run surfaces it.)*
- **Clock caveat**: the run-date line carries the trust note; the real fix (trusted time source /
  newest-stamp floor) is E001's suggestion and arrives via its own gated intake. **CLOSED
  <P3-DATE> by PLAN-013** — the engine refuses to stamp behind a target's newest stamp
  (`sync.newest_stamp` / `check_clock`); E001's lesson half shipped as Set v2.6 (L079).
`````

Plus (mechanical, L063 stamp-grep after editing): `docs/documents_manifest.md` cells 7
(architecture 0.12→0.13), 46 (cli 0.6→0.7), 51 (test_cli 0.6→0.7), 72 (sync 0.2→0.3), 73
(test_sync 0.1→0.2), 80 (PLAN-012 1.0→1.1), 84–85 (this plan + tracker → 1.0/CLOSED), self-row, and
the Last-updated block; `CHANGELOG.md` release entry with the QA scenarios. No `docs/standards/`
file changes → no Set Version bump, no SVA row.

## 7. ALLOWLIST (the bullet enumeration IS the count — 10 files)

- `src/standard_document_updater/sync.py`
- `src/standard_document_updater/cli.py`
- `tests/test_sync.py`
- `tests/test_cli.py`
- `docs/architecture.md`
- `docs/Plans/PLAN-012_sync_handoff.md` (closed-risk annotation)
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-013_engine_write_safety.md` (promotion to 1.0/CLOSED)
- `docs/Plans/PLAN-013_tracker.md` (promotion to 1.0/CLOSED)

## 8. Validation gate (Rule 11 scenarios; Rule 15 feature-ON marked ⚑; status in the tracker)

- **QA-K1 — suite.** `ruff check src tests` clean; mypy error SET identical to the pre-change
  baseline (line numbers stripped; 42 full / 25 `src` at `03fa0dd`); `pytest` 119 passed. Proven in
  the overlay 2026-10-03; re-run at Phase 3.
- **QA-K2 ⚑ — live dry-run (pre-commit).** Fleet `sync` dry-run with the new engine: every target
  holding a handoff shows the "un-landed docs/SYNC_HANDOFF.md" note; no clock warning with a
  verified clock; per-target changed-item lists identical to the old engine's.
- **QA-K3 ⚑ — clock guard on real data.** A scratch vault worktree whose registry points at a
  scratch COPY of a real target with one `Last Updated` stamp moved to tomorrow: dry-run prints the
  "a --write would refuse (L079)" warning; `sync --write` exits 1 with "clock is behind"; the copy's
  tree is byte-unchanged and holds no handoff. Cleanup: `git worktree remove` the scratch
  worktree and delete the scratch copy (no vault or target state may persist).
- **QA-K4 ⚑ — accumulation, sync half.** The first real `sync --write` into a target holding a
  pre-accumulation handoff (D-5: Capital-Signal's v2.6 catch-up): the handoff reads `### Write 1 —
  earlier engine write` (the v2.5 list, verbatim) + `### Write 2` (the v2.6 list); immediate
  dry-run re-run up-to-date 11/11.
- **QA-K5 ⚑ — accumulation, write-back half.** The deferred E001 write-back (v2.6 QA-E4 = PLAN-012
  QA-H6): if 780-VPN has not landed its v2.6 handoff, the write-back appends as `### Write 2`;
  if it has, a fresh `### Write 1` — record which path ran.
- **QA-K6 — idempotence.** After K4/K5, dry-run up-to-date on every written target; the handoff's
  presence does not perturb planning.

**Rule 15:** QA-K2/K3/K4 gate plan closure; K5 fires at its named trigger (scheduled work, not a
silent deferral; the write-back path is test-covered under K1).

## 9. Operator decision points (Phase 2 — answer with the approval)

- **D13.A — approve the plan** ("APPROVE PLAN-013").
- **D-1 — clock source.** (A) **offline floor guard** — the target's own newest stamp is the
  authority (RECOMMEND: deterministic, testable, no network dependency, catches the actual incident
  — a 9-day-slow clock is behind every recent stamp); (B) A + an HTTP `Date:` check against a
  well-known host on `--write` (catches a slow clock even against a target with only old stamps,
  at the cost of a network dependency and a new failure mode). The human-side check already ships
  in PROJECT_STANDARDS § 5.6 (v2.6).
- **D-2 — un-landed handoff policy.** (A) **accumulate** (RECOMMEND: the fleet stays syncable and
  every write stays explained); (B) refuse any write while an un-landed handoff exists (strongest
  against the discard class, but an idle target — e.g. Capital-Signal — then blocks every release
  indefinitely).
- **D-3 — strictness.** (A) **strict** — refuse whenever `today < floor` (RECOMMEND: a one-day
  inversion is still an inversion, § 5.6); (B) 1-day tolerance for cross-timezone midnight cases
  (avoids rare false refusals; re-running after midnight solves them under A anyway).
- **D-4 — override.** (A) **none** — fix the clock, or correct a wrong target stamp per § 5.6
  (RECOMMEND: fewer knobs; the refusal message names both paths); (B) a `--today YYYY-MM-DD` flag.
- **D-5 — first feature-ON write.** After ship, run Capital-Signal's v2.6 catch-up as QA-K4
  (RECOMMEND: it lifts the CS hold — the handoff will list v2.5 + v2.6, and the new § 2 step-1
  sentence covers its older unlisted v2.1–v2.4 files); alternative: keep CS held until a CS session
  lands its backlog, and use the next release for QA-K4.

### 9.1 Decision record (Phase 2, 2026-10-03)

- **D13.A — APPROVED:** operator *"approve plan 013"* (2026-10-03, opening the Phase 3 session:
  "start new session and approve plan 013 then start implementation").
- **D-1…D-4 = A** — offline floor guard; accumulate; strict; no override. These are the plan as
  drafted (the § 5 code implements exactly these options). Not answered item by item: the agent's
  read (approving the drafted plan = its recommended options) was stated in the session pre-flight
  and confirmed by the operator at the approval-commit gate.
- **D-5 = A** — Capital-Signal's v2.6 catch-up is QA-K4. The write itself still requires the
  operator to name the target at QA time (SESSION_OPENER § 2: never write to an unnamed target).

## 10. Rollback path

Single revert of the Phase 3 commit restores the overwrite behavior and removes the guard. Handoffs
written in the accumulating format remain human-readable; a later old-engine write would overwrite
them (the pre-PLAN-013 behavior). No persistent state, no schema.

## 11. Known risks + mitigation

| # | Risk | Mitigation |
|---|---|---|
| R1 | A target stamp dated in the future (target clock fast, or a typo) makes every write refuse | The refusal message names it; correct the stamp in the target per § 5.6 and re-run (D-4 = A) |
| R2 | Cross-timezone midnight: a target stamped "tomorrow" by local time → spurious refusal | D-3; re-run after midnight; the dry-run warning shows it before any write |
| R3 | A stale handoff (landed but not deleted) makes the next write list already-landed records as pending | § 1.1 opener check deletes on landing; landed records show no `git diff`; the sync dry-run note surfaces any handoff before the curator writes |
| R4 | An unrecognized handoff containing `### Write N` text inside its fence skews record numbering | Cosmetic only — content is preserved verbatim; the format only arises from manual edits |
| R5 | Stamps in non-SYNC_MAP target files are not scanned, so the floor can sit below the true newest stamp | The guard can only be weaker, never falsely refuse; it covers exactly the files the engine stamps |
| R6 | Git transport flushes commit the handoff, so `existing` may be a committed file | Accumulation still reads it correctly; PLAN-014 (PR delivery) revisits moving the handoff into the PR body |

## 12. Acceptance criteria

1. Both write paths refuse (nothing written) when the local clock is behind the target's newest
   stamp; the sync dry-run warns (QA-K3; tests).
2. A write into a target holding an un-landed handoff appends the next `### Write N` record and keeps
   every earlier record verbatim; a pre-accumulation handoff is wrapped as record 1; an unrecognized
   one is kept in a fence (QA-K4/K5; tests).
3. Dry-run planning unchanged (QA-K2/K6); `ruff` clean, mypy error set identical, 119 tests (QA-K1).
4. architecture § 7 + § 9 and the PLAN-012 § 11 annotation land in the same commit.

---

**Rule 13 senior-review-and-optimize pass — RUN 2026-10-03 (recorded per § 15.8):** the canonical
prompt was run against the complete plan + tracker, mechanically (L051):

- **Proven-code-first, then re-extracted:** the § 5 code was developed in a scratch overlay of `src`
  + `tests` at `03fa0dd` and proven there; then ALL 17 FIND/REPLACE blocks were re-extracted from
  THIS FILE by a parser, compared byte-for-byte with the proven edits (identical), and applied to a
  fresh overlay with a 10-character date in place of `<P3-DATE>` (ship form): `ruff check src tests`
  — clean; mypy — 42 errors full config / 25 `src`, the error SET identical to the baseline with
  line numbers stripped; `pytest` — 119 passed, imported from the overlay (verified via
  `__file__`).
- **Anchors:** every § 5 FIND matched exactly once in the live-source copy; every § 6 FIND matched
  exactly once in live `docs/architecture.md` / `docs/Plans/PLAN-012_sync_handoff.md`.
- **Real data (engine-as-oracle, read-only):** the overlay engine's fleet dry-run flagged both live
  targets' un-landed handoffs with unchanged changed-item lists; `render_handoff` over
  Capital-Signal's REAL pre-accumulation handoff produced `Write 1 — earlier engine write` (its v2.5
  list verbatim) + `Write 2`; live floors CS `2026-09-05`, 780-VPN `2026-10-03` (no false refusal).
- **Cross-section consistency:** § 1 goal ↔ § 3 scope ↔ § 5 (11 code blocks) ↔ § 6 (6 doc blocks +
  mechanical manifest/CHANGELOG) ↔ § 7 ALLOWLIST (10 bullets, counted) ↔ § 8 QA-K1…K6 ↔ tracker
  ledger (6 rows) ↔ § 9 D-1…D-5 + D13.A ↔ § 12 criteria.
- **Edge cases walked:** clock equal to the floor (allowed); no changed items (no guard, nothing
  stamped); guard failure inside the integrate ExitStack (sessions close without flush — nothing
  written; exit 2); ssh non-full sessions (only `docs/` materialized — floor from what exists);
  legacy / new / unrecognized handoff shapes; a stale landed-but-not-deleted handoff (R3); cross-
  timezone midnight (R2 → D-3).
- **Fixed in place (1):** QA-K3 gains its cleanup step (scratch worktree + copy removed).
- **Considered, not applied (1):** adding STANDARDS_LOG `- Date:` entry lines to the floor would
  strengthen the guard but turn a mistyped entry date into a false refusal; the floor stays on the
  stamp positions PROJECT_STANDARDS § 5.6 defines.
- **New design decisions surfaced, not decided silently:** D-1 (clock source), D-2 (accumulate vs
  refuse), D-3 (strictness), D-4 (override), D-5 (first feature-ON write).
