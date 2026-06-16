<!-- VERSION: 1.0 -->
<!-- Status: CLOSED -->
<!-- Last Updated: 2026-06-16 -->
<!--
CHANGE LOG
v1.0 — 2026-06-16 — Phase 3 (Implement) shipped in one ALLOWLIST-bounded commit + Phase 4 validate
passed (QA A–H green: ruff + mypy --strict + 35 pytest; both governance scripts exit 0; live CLI
A/B/C/D/G confirmed). Plan-defect D1 resolved (mechanical): the § 5B report-append line was 103 cols
(ruff E501) — reflowed to a wrapped lines.append(...); production output byte-identical. Promoted to
1.0/CLOSED. Push held for the Phase-5 operator gate.
v0.1 — 2026-06-16 18:06 — Phase 0 (Audit) + Phase 1 (Design) drafted. Slice 3: the `harvest`
command — read every registered project's docs/STANDARDS_LOG.md, collect the `open` entries, render
a consolidated report grouped by area, cautiously flag cross-project duplicates. Read-only; always
exits 0. Operator design decisions D1–D4 locked (2026-06-16). Sibling tracker created same-commit.
Rule 13 senior-review-and-optimize pass recorded at the foot.
-->

# PLAN-004 — Slice 3: `harvest` (consolidate open experiences-log entries)

> § 15 plan (vital change — new engine module other slices depend on). Sibling tracker:
> `docs/Plans/PLAN-004_tracker.md`. Phase 3 runs in a fresh session, prompted from this file +
> `OPEN_TASKS.md` (per [[feedback_plan_handoff_via_open_tasks]]).

## 1. Goal

Implement the `harvest` command (architecture.md § 6a / § 8 / § 10 Slice 3):

```
python -m standard_document_updater harvest
```

Read **every registered project's** `docs/STANDARDS_LOG.md`, collect the entries whose `Status` is
`open`, and print a **consolidated report grouped by area**, conservatively flagging likely
cross-project duplicates. **Read-only** (writes nothing — not to any target, not to disk). Always
exits `0`. This is the read side of the harvest→integrate→sync loop; `integrate` (Slice 4 / PLAN-005)
consumes the same open entries later.

## 2. Operator constraints (design decisions locked 2026-06-16)

| ID | Decision | Locked choice |
|---|---|---|
| **D1** | Report destination | **Print to stdout only.** No persisted file. The source logs are the durable record; a saved report is a staleness risk (this session's OPEN_TASKS incident). A keepsake copy is `harvest > file.md`. |
| **D2** | Machine-readable output | **Defer `--json`.** Plain text now; add when `integrate` (Slice 4) defines the need (YAGNI / "stay small" as in PLAN-003). |
| **D3** | Duplicate detection | **Cautious + deterministic.** Flag two open entries only when their *normalized titles match* AND they are from *different projects*. Annotate `⚠ possible duplicate of <project>/<E0NN>`. |
| **D4** | Exit code | **Always `0`.** `harvest` is informational (like `status`), not a gate (unlike `drift`). |

Carried from PLAN-003: registry = `config/projects.toml` (name + path; adopted version read live);
CLI = `python -m standard_document_updater <command>`; "stay small" (no CI `test` stage this slice);
**no Set Version bump** (no `docs/standards/` suite file is touched).

## 3. Scope summary

**New modules (2):**
- `src/standard_document_updater/logentry.py` — parse a `STANDARDS_LOG.md` into `list[LogEntry]`
  (full entry: id, title, date, area, status, free-text fields; `is_open` property). Live re-read
  per architecture § 9.
- `src/standard_document_updater/harvest.py` — pure render: collect → group-by-area → cautious
  dup-flag → text report. No filesystem (the CLI does path-building, mirroring PLAN-003's
  report/cli split).

**Modified code (3):** `cli.py` (+`harvest` subcommand, `_build_open_items`, `_cmd_harvest`; bump
0.1→0.2), `__init__.py` (`__version__` 0.1.0→0.2.0; header 0.1→0.2), `tests/test_cli.py` (+2 harvest
tests; bump 0.1→0.2).

**New tests (2):** `tests/test_logentry.py` (parser), `tests/test_harvest.py` (pure render + dup
logic, no disk).

**Deliberately NOT touched:** `setversion.py` (`count_open_log_entries` keeps its own lightweight
heading-walk; DRY-delegation to `logentry.parse_log` is a noted follow-up — see § 11 DD-1, kept out
to avoid touching tested status/drift code this slice). `conftest.py` (existing fixtures suffice).
`registry.py`, `report.py`, `errors.py`, `__main__.py` (unchanged). No `docs/standards/` file → no
Set Version bump. No `.gitlab-ci.yml`, no `CLAUDE.md`.

## 4. Phase tracker (high-level; granular sub-tasks in the sibling tracker)

| Phase | Status |
|---|---|
| 0 — Audit | ✅ 2026-06-16 |
| 1 — Design (+ Rule 13 pass) | ✅ 2026-06-16 |
| 2 — Operator approval | ✅ 2026-06-16 (`APPROVE PLAN-004`) |
| 3 — Implement (fresh session, 1 commit) | ✅ 2026-06-16 |
| 4 — Validate (QA A–H) | ✅ 2026-06-16 |
| 5 — Operator gate (push; no tag) | ⏸ push held for operator |

## 5. Transformation rules (verbatim, per Rule 7)

### 5A — `src/standard_document_updater/logentry.py` (NEW)

```python
# ==============================================================
# VERSION: 0.1
# Parse a STANDARDS_LOG.md into structured experience entries.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: LogEntry dataclass + parse_log (full-entry parser).
# ==============================================================
"""Parse a project's experiences log (docs/STANDARDS_LOG.md) into entries.

Re-reads the file on every call (never cached) per docs/architecture.md § 9.
The entry schema is fixed by docs/standards/STANDARDS_LOG.md:

    ## E001 — <title>
    - Date:        YYYY-MM-DD
    - Area:        <engineering | cicd | validation | project | prompt | memory | governance>
    - Status:      open                 # open | integrated | rejected
    - Context:     <free text, may span multiple indented lines>
    - Learned:     <free text>
    - Suggested:   <free text>
    - Portability: <project-specific | general>

Controlled-vocabulary fields (area / status / portability) keep only their
first whitespace-delimited token, so a trailing "# comment" or a status
write-back such as "integrated -> vault L050 (...)" reduces to "integrated".
Free-text fields (context / learned / suggested) keep continuation lines,
joined with single spaces.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

_HEADING_RE = re.compile(r"^##[ \t]+(E\d+)\b[ \t]*(?:[—-][ \t]*(.*))?$", re.MULTILINE)
_FIELD_RE = re.compile(r"^-[ \t]*([A-Za-z]+):[ \t]*(.*)$")


@dataclass(frozen=True)
class LogEntry:
    """One experiences-log entry. Free-text fields may be empty."""

    entry_id: str
    title: str = ""
    date: str = ""
    area: str = ""
    status: str = ""
    context: str = ""
    learned: str = ""
    suggested: str = ""
    portability: str = ""

    @property
    def is_open(self) -> bool:
        """True when the entry has not yet been harvested/integrated."""
        return self.status.lower() == "open"


def parse_log(log_path: Path) -> list[LogEntry]:
    """Parse STANDARDS_LOG.md into entries, in file order.

    Returns an empty list when the file is absent (a project may not have
    started a log). Malformed or partial entries are tolerated: missing
    fields default to "".
    """
    if not log_path.exists():
        return []
    text = log_path.read_text(encoding="utf-8")
    headings = list(_HEADING_RE.finditer(text))
    entries: list[LogEntry] = []
    for i, heading in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        body = text[heading.end() : end]
        entries.append(_build_entry(heading.group(1), heading.group(2), body))
    return entries


def _build_entry(entry_id: str, title: str | None, body: str) -> LogEntry:
    fields = _parse_fields(body)
    return LogEntry(
        entry_id=entry_id,
        title=(title or "").strip(),
        date=fields.get("date", ""),
        area=_token(fields.get("area", "")),
        status=_token(fields.get("status", "")),
        context=fields.get("context", ""),
        learned=fields.get("learned", ""),
        suggested=fields.get("suggested", ""),
        portability=_token(fields.get("portability", "")),
    )


def _parse_fields(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: str | None = None
    for line in body.splitlines():
        match = _FIELD_RE.match(line)
        if match:
            current = match.group(1).lower()
            fields[current] = match.group(2).strip()
        elif current is not None and line.strip():
            fields[current] = f"{fields[current]} {line.strip()}".strip()
    return fields


def _token(value: str) -> str:
    """First whitespace-delimited token, lowercased ('' when value is empty)."""
    parts = value.split()
    return parts[0].lower() if parts else ""
```

### 5B — `src/standard_document_updater/harvest.py` (NEW)

```python
# ==============================================================
# VERSION: 0.1
# Consolidate open experiences-log entries across registered projects.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: collect/group-by-area, cautious dup flag, render.
# ==============================================================
"""Build the harvest report: every open log entry, grouped by area.

Read-only. Flags likely cross-project duplicates conservatively (PLAN-004 D3):
two open entries are flagged only when their normalized titles match AND they
come from different projects. Always informational; the CLI exits 0 (D4).
"""
from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass

from standard_document_updater.logentry import LogEntry

_NORM_RE = re.compile(r"[^a-z0-9]+")


@dataclass(frozen=True)
class OpenItem:
    """An open log entry paired with the project it came from."""

    project_name: str
    entry: LogEntry


def _normalize(title: str) -> str:
    """Lowercase, drop punctuation, collapse whitespace — for dup matching."""
    return _NORM_RE.sub(" ", title.lower()).strip()


def _duplicate_refs(items: list[OpenItem]) -> dict[int, list[str]]:
    """Map item index -> refs of same-title items from *other* projects."""
    by_title: dict[str, list[int]] = defaultdict(list)
    for index, item in enumerate(items):
        key = _normalize(item.entry.title)
        if key:
            by_title[key].append(index)
    refs: dict[int, list[str]] = {}
    for indices in by_title.values():
        if len({items[i].project_name for i in indices}) < 2:
            continue
        for i in indices:
            others = [
                f"{items[j].project_name}/{items[j].entry.entry_id}"
                for j in indices
                if items[j].project_name != items[i].project_name
            ]
            if others:
                refs[i] = others
    return refs


def render_report(items: list[OpenItem]) -> str:
    """Render the consolidated report grouped by area (stable, deterministic)."""
    if not items:
        return "No open log entries across registered projects."
    refs = _duplicate_refs(items)
    by_area: dict[str, list[int]] = defaultdict(list)
    for index, item in enumerate(items):
        by_area[item.entry.area or "(unspecified)"].append(index)

    project_count = len({item.project_name for item in items})
    plural = "y" if len(items) == 1 else "ies"
    lines = [
        f"Harvest — {len(items)} open entr{plural} "
        f"across {project_count} project(s), {len(by_area)} area(s)."
    ]
    for area in sorted(by_area):
        lines.append("")
        lines.append(f"## {area} ({len(by_area[area])})")
        ordered = sorted(
            by_area[area],
            key=lambda i: (items[i].project_name, items[i].entry.entry_id),
        )
        for i in ordered:
            item = items[i]
            suffix = f"  ({item.entry.portability})" if item.entry.portability else ""
            lines.append(f"  [{item.project_name}] {item.entry.entry_id} — {item.entry.title}{suffix}")
            if i in refs:
                lines.append(f"      ⚠ possible duplicate of {', '.join(refs[i])}")
    return "\n".join(lines)
```

### 5C — `src/standard_document_updater/cli.py` (MODIFIED)

**C1 — header bump.** Replace the VERSION block top matter:

```python
# ==============================================================
# VERSION: 0.2
# Command-line interface: `python -m standard_document_updater <command>`.
#
# CHANGE LOG
# v0.2 — 2026-06-16 — Add the `harvest` subcommand (open-log consolidation).
# v0.1 — 2026-06-16 13:01 — Initial: status + drift subcommands, --vault override.
# ==============================================================
```

**C2 — import line.** Replace:

```python
from standard_document_updater import __version__, report, setversion
```

with:

```python
from standard_document_updater import __version__, harvest, logentry, report, setversion
```

**C3 — new builder + handler.** Insert after `_cmd_drift` (after the `return 1` on the existing
drift handler, before `build_parser`):

```python
def _build_open_items(vault_root: Path) -> list[harvest.OpenItem]:
    registry_path = vault_root / "config" / "projects.toml"
    items: list[harvest.OpenItem] = []
    for project in load_registry(registry_path):
        log_path = project.path / "docs" / "STANDARDS_LOG.md"
        for entry in logentry.parse_log(log_path):
            if entry.is_open:
                items.append(harvest.OpenItem(project.name, entry))
    return items


def _cmd_harvest(args: argparse.Namespace) -> int:
    print(harvest.render_report(_build_open_items(args.vault)))
    return 0
```

**C4 — subparser.** After the existing `sub.add_parser("drift", ...)` line, insert:

```python
    sub.add_parser(
        "harvest",
        help="consolidate open experiences-log entries across all projects",
    )
```

**C5 — handler dispatch.** Replace:

```python
    handlers = {"status": _cmd_status, "drift": _cmd_drift}
```

with:

```python
    handlers = {"status": _cmd_status, "drift": _cmd_drift, "harvest": _cmd_harvest}
```

### 5D — `src/standard_document_updater/__init__.py` (MODIFIED)

**D-i — header bump:**

```python
# ==============================================================
# VERSION: 0.2
# Standard DocSet engine — package marker + released CLI version.
#
# CHANGE LOG
# v0.2 — 2026-06-16 — Slice 3 (harvest): CLI version 0.1.0 -> 0.2.0.
# v0.1 — 2026-06-16 13:01 — Initial package (Slice 2: registry + status/drift).
# ==============================================================
```

**D-ii — version constant.** Replace `__version__ = "0.1.0"` with `__version__ = "0.2.0"`.

### 5E — `tests/test_logentry.py` (NEW)

```python
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
```

### 5F — `tests/test_harvest.py` (NEW)

```python
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
```

### 5G — doc sync (mechanical; full edits enumerated in the sibling tracker Phase 3 checklist)

- **`docs/architecture.md`** (0.4→0.5): § 8 command table — change the `harvest` row marker to ✅ /
  "(Implemented Slice 3 — PLAN-004)"; § 10 roadmap — tick Slice 3 ✅ with a one-line summary; CHANGE LOG.
- **`docs/folder_structure.md`** (0.6→0.7): add `logentry.py` + `harvest.py` to the `src/…` tree and
  `test_logentry.py` + `test_harvest.py` to the `tests/` tree; update the engine-tree comment to
  "(Slice 3: + harvest)"; CHANGE LOG.
- **`docs/documents_manifest.md`** (1.6→1.7 at DRAFT for the plan rows; →1.8 at Phase 3 for the code
  rows): see § 7 for the exact two-commit split.
- **`scripts/validation_ownership.toml`**: add `[rules.logentry]` and `[rules.harvest]` (soft;
  `source_paths`/`test_paths`/`doc_paths=docs/architecture.md`).
- **`CHANGELOG.md`**: top entry + explicit `QA scenarios` sub-section (A–H).

## 6. Spec / doc update map

| Behavior introduced | Dispositive code | Navigable doc kept in sync (same commit) |
|---|---|---|
| `harvest` command exists, exit 0 | `cli.py` | `architecture.md` § 8 row; `folder_structure.md` |
| Parse a log into full entries | `logentry.py` | `architecture.md` § 5 schema (already matches) |
| Group by area + cautious cross-project dup flag | `harvest.py` | `architecture.md` § 6a ("grouped by area, flagging likely cross-project duplicates") |
| New tracked code files | all new `.py` | `documents_manifest.md` rows + `validation_ownership.toml` |

No `docs/standards/` suite file changes → **Set Version stays v1.1** (architecture § 9 invariant
preserved: the engine reads the log, it does not alter the suite).

## 7. ALLOWLIST

**This (DRAFT / Phase 1) commit — 3 paths (the bullet enumeration IS the count):**
- `docs/Plans/PLAN-004_harvest.md` (NEW, this file, v0.1 DRAFT)
- `docs/Plans/PLAN-004_tracker.md` (NEW, sibling tracker, v0.1)
- `docs/documents_manifest.md` (MODIFIED — register the two plan files; renumber; bump 1.6→1.7)

**Phase 3 (Implement) commit — 11 paths (4 new + 7 modified):**
- `src/standard_document_updater/logentry.py` (NEW)
- `src/standard_document_updater/harvest.py` (NEW)
- `tests/test_logentry.py` (NEW)
- `tests/test_harvest.py` (NEW)
- `src/standard_document_updater/cli.py` (MODIFIED — § 5C; 0.1→0.2)
- `src/standard_document_updater/__init__.py` (MODIFIED — § 5D; 0.1→0.2, ver 0.2.0)
- `tests/test_cli.py` (MODIFIED — +2 harvest tests; 0.1→0.2)
- `docs/architecture.md` (MODIFIED — § 5G; 0.4→0.5)
- `docs/folder_structure.md` (MODIFIED — § 5G; 0.6→0.7)
- `scripts/validation_ownership.toml` (MODIFIED — § 5G; +2 rules)
- `docs/documents_manifest.md` (MODIFIED — register 4 code rows; bump code-cell versions; promote
  PLAN-004 plan+tracker 0.1→1.0; bump 1.7→1.8)
- `CHANGELOG.md` (MODIFIED — top entry + QA sub-section)

> Count note: the Phase 3 bullet list enumerates 12 lines because `documents_manifest.md` and
> `CHANGELOG.md` are each listed once; "4 new + 7 modified" = 11 distinct files (manifest appears in
> both commits but is one file). If any file outside the active commit's ALLOWLIST appears in
> `git status`, STOP and report (Rule 7).

## 8. Validation gate + QA scenarios (Rule 11)

Run from repo root with `PYTHONPATH=src` / `MYPYPATH=src` (PLAN-003 env note — the editable-install
`.pth` is not honored on this machine; not a code defect).

| ID | Scenario | Expected |
|---|---|---|
| A | `harvest`, empty registry | "No open log entries across registered projects.", **exit 0** |
| B | `harvest`, one project with 2 open entries | both `E0NN` listed under their area, **exit 0** |
| C | parser: status write-back (`integrated → …`) | `is_open` False; only `open` entries harvested |
| D | dup: same normalized title, **different** projects | both flagged `⚠ possible duplicate of …` |
| E | dup: same title, **same** project | **not** flagged |
| F | dup: distinct titles | **not** flagged |
| G | grouping: entries across ≥2 areas | one `## <area> (n)` block each, areas sorted |
| H | `ruff check src tests` clean · `mypy --strict` clean (14 files) · full pytest green; governance `check_doc_coverage.py` + `check_test_coverage_drift.py --ci` both **exit 0** |

B–G covered by `test_logentry.py` / `test_harvest.py`; A, B, H also exercised live via the CLI.

## 9. Operator-approval decision point

Phase 2 gate: operator replies **`APPROVE PLAN-004`** (or requests changes). No code is written until
approval lands. Phase 3 runs in a fresh session prompted from this file + `OPEN_TASKS.md`.

## 10. Rollback

Single Phase-3 commit, unpushed until the Phase-5 gate. Rollback = `git reset --hard HEAD~1` (or drop
the new files + revert the 7 edits) before push. No persisted state, no target writes → nothing to
clean up externally. The DRAFT commit is independently revertable.

## 11. Risks + design decisions

| ID | Item | Disposition |
|---|---|---|
| R1 | Log entry with a non-em-dash heading (`## E001 - title`) | `_HEADING_RE` accepts `[—-]`; title still parsed. Low risk. |
| R2 | Free-text field containing a `- Word:` line | `_FIELD_RE` would misread it as a new field. Accepted — the schema indents continuations; real logs follow it. Noted, not mitigated this slice. |
| R3 | Manifest renumber error (insert plan rows shifts Engine block) | Mechanical; governance `check_doc_coverage.py` validates completeness; explicit table in tracker. |
| DD-1 | **DRY:** `setversion.count_open_log_entries` duplicates the heading-walk now in `logentry.parse_log` | **Deliberately deferred.** Refactoring it to delegate would touch tested status/drift code; out of scope for "stay small". Logged as a follow-up in OPEN_TASKS. Surfaced for operator awareness. |
| DD-2 | **Dup scope:** flag is title-only, cross-project only (D3) | Intended. Same-project repeats and fuzzy/keyword matches are explicitly out (avoids false positives). |
| D1 (Phase 3) | **E501:** verbatim § 5B report-append line was 103 cols | **Resolved (mechanical).** Reflowed to a wrapped `lines.append(...)` call; production output byte-identical. The Rule 13 pass (finding #2) had reflowed the *header* f-string but missed this per-item line; caught by ruff at Phase 4. |

## 12. Acceptance criteria

- `harvest` lists every `open` entry across registered projects, grouped by area, exit 0 (D1/D4).
- Only `open` entries appear (write-back / rejected excluded).
- Cross-project same-title entries flagged; same-project and distinct-title entries not (D3).
- `ruff` + `mypy --strict` + full pytest green; both governance scripts exit 0 (Rule 2).
- All touched code files VERSION-bumped + CHANGE LOG line (Rule 7); manifest + folder_structure +
  architecture + ownership synced same-commit; CHANGELOG entry with QA sub-section.
- **No Set Version bump; no target-repo write; no `.gitlab-ci.yml` / `CLAUDE.md` change.**

---

## Senior-review-and-optimize pass (Rule 13) — 2026-06-16 18:06

Ran the canonical § 15.8 prompt against the complete plan, verified every § 5 block against the real
current source (`logentry`/`harvest` designed fresh; `cli.py`/`__init__.py` diffs checked line-by-line
against the on-disk files; `test_cli.py` fixture names `make_vault`/`make_project`/`write_registry`
confirmed against `conftest.py`; ruff line-length=100 and `select=[E,F,I,UP,B]` checked against
`pyproject.toml`). Findings applied in place:

1. **Removed an unused `_CONTROLLED` frozenset** from the first `logentry.py` draft (would have tripped
   ruff `F401`/dead code) — `_token` is applied per-field instead.
2. **Reflowed the long report line** in `harvest.py` to a `line =` assignment pattern and split the
   header f-string across two literals to stay ≤100 cols (pre-empts the ruff `E501` that bit PLAN-003).
3. **Made `LogEntry` fields default to `""`** so `test_harvest.py` can construct entries directly
   without disk I/O — keeps `harvest.render_report` a pure, fixture-free unit (the report/cli split
   from PLAN-003).
4. **Confirmed dup logic excludes same-project repeats** (`len({project_name}) < 2` guard) and that
   `_token` reduces a status write-back (`integrated → vault L050`) to `integrated` so `is_open` is
   correctly False — added scenarios C/E to lock both.
5. **Pinned the import order** `__version__, harvest, logentry, report, setversion` (ruff `I`
   alphabetical) and the two-commit manifest split (DRAFT registers plan rows; Phase 3 registers code
   rows) to avoid a Rule-8 same-commit miss.
6. **Surfaced DD-1** (the `setversion` DRY deferral) to the operator rather than silently refactoring
   tested code — § 11.

No new product design decision beyond D1–D4 (already operator-locked). Plan finalized; ready for
Phase 2.
