<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-18 -->
<!-- Status: CLOSED -->
<!--
CHANGE LOG
v1.0 — 2026-06-18 — Phase 3 (Implement) + Phase 4 (Validate) shipped in one commit. integrate.py + 20-test
test_integrate.py + 2 CLI tests landed; cli.py/__init__.py 0.2→0.3; validation_ownership soft rule;
architecture 0.6→0.7 (§ 8/§ 10 + § 11 OPEN resolved); manifest 2.1→2.2 (entries 61–62); folder_structure
0.8→0.9; CHANGELOG entry + QA A–K. **Plan-defect D1 (mechanical):** the verbatim § 5A code shipped 5 E501
over-length lines — `next_lesson_id`'s read-text comprehension, the 4 worksheet-footer literals, and the
integrated-Status f-string — that the v0.1a Rule 13 pass did not fully catch (it claimed an E501 in a
"§ 5A CHANGE-LOG header line", but the actual over-length lines were elsewhere; same recurring class as
PLAN-003 D2 / PLAN-004 D1). All 5 reflowed **output-preserving**: the worksheet footer verified
byte-identical by SHA-256 (len 345, unchanged), the Status f-string re-confirmed by its parse test.
**Plan gap (surfaced, not silently filled):** § 5D/§ 6 scoped architecture to § 8 + § 10, but § 11's own
text mandated resolving the OPEN genericization decision at this slice → marked DECIDED (A1) same-commit.
QA A–K all PASS (ruff/mypy --strict 18 files/57 pytest green; both governance scripts exit 0; live
worksheet + dry-run + write + safety confirmed against a throwaway fixture). No Set Version change. Plan +
tracker promoted to 1.0/CLOSED this commit. Push held for the Phase-5 operator gate.
v0.1a — 2026-06-18 — Rule 13 senior-review pass (last task of Phase 1). Per the elevated lesson, the
§ 5 module code was MATERIALIZED in src/ + a real test_integrate.py written, then ruff + mypy --strict +
pytest were actually RUN (not eyeballed), then the scratch files removed. Result: ruff caught 1 E501 (the
§ 5A CHANGE-LOG header line, 102 > 100 — the same defect class that recurred in PLAN-003/004) → fixed in
§ 5A; mypy --strict clean across 18 files (incl. the new module + tests); 46 tests pass (35 prior + 11
new). The pre-applied reflows (parse_decisions `status` line, worksheet footer) held. No new design
decision beyond DD-1…DD-5. Plan finalized → ready for Phase 2.
v0.1 — 2026-06-18 — Initial DRAFT. Phase 0 (Audit) + Phase 1 (Design) for Slice 4: the `integrate`
command. A/A/A decided by operator: (A1) Claude-session-assisted genericization — the tool is a
deterministic spine, Claude authors the lesson in-session; (A2) full flow this slice; (A3) vault-canonical
only (propagation is sync/PLAN-007). Sibling tracker: PLAN-006_tracker.md.
-->

# PLAN-006 — Slice 4: `integrate` (worksheet + status write-back)

> **Type:** Major / new engine module (`src/standard_document_updater/`, a Critical File per § 4) + a new
> CLI command, one of which **writes to target repos**. Runs under the § 15 plan workflow.
> **Sibling tracker:** [`PLAN-006_tracker.md`](PLAN-006_tracker.md).
> **Operator decisions settled:** A1 (session-assisted, tool = deterministic spine), A2 (full flow),
> A3 (vault-canonical only — propagation belongs to `sync`/PLAN-007).

---

## 1. Goal

Ship the `integrate` command — the deterministic half of the harvest → **integrate** → sync loop
(architecture § 6c). It turns the open experiences-log entries into (a) a **worksheet** Claude uses to
author each genericized `L0NN` lesson in-session, and (b) an operator-gated **write-back** that records
each entry's disposition (`integrated → vault L0NN …` / `rejected — …`) into its project's
`STANDARDS_LOG.md`.

**What the tool does NOT do (A1):** it does not call a model, and it does not edit the vault
(`LESSONS.md` / topical files / `STANDARDS_INDEX.md`). Those are judgment + Critical-File edits performed
by Claude **in-session under the § 15 flow** when `integrate` is actually run on real entries. The tool is
pure-Python, deterministic, and testable.

## 2. Operator constraints & decisions settled

- **A1 — genericization engine:** Claude-session-assisted. Tool = deterministic spine (worksheet +
  write-back + proposed-`L0NN` + Area→topical routing); Claude authors the lesson + does the vault edits.
- **A2 — scope:** full flow this slice (worksheet **and** write-back).
- **A3 — lessons target:** vault-canonical only. `integrate` never touches `archive/LESSONS.md` or this
  repo's other operative copies; spreading a new Set Version is `sync` (PLAN-007).

### 2.1 New design decisions exposed by the audit — for Phase-2 confirmation (per § 10 / Rule 13.5)

- **DD-1 — Command surface = one subcommand with a write flag**, mirroring the existing pattern
  (`status`/`drift`/`harvest` are read-only; the writer is explicit):
  - `integrate` → **read-only worksheet** to stdout (default; always exit 0, like `harvest`).
  - `integrate --apply <decisions.toml>` → **operator-gated write-back**. Default is a **dry-run diff**;
    actually writing requires `--write` (or `--yes`). Re-reads each target log before writing (§ 9), and
    touches only the projects named in the decisions file.
- **DD-2 — Decisions handoff = a small TOML file** (consistent with `config/projects.toml`). Claude
  authors it in-session after writing the lessons. Shape:
  ```toml
  [[integrated]]
  project = "<registry name>"
  entry   = "E007"
  lesson  = "L051"
  topical = "ENGINEERING_STANDARDS § 1.11"
  set_version = "v1.3"

  [[rejected]]
  project = "<registry name>"
  entry   = "E009"
  reason  = "project-specific, not portable"
  ```
- **DD-3 — Area→topical routing** is a fixed map (audit-confirmed against the dispatcher, CLAUDE.md § 12):
  engineering→`ENGINEERING_STANDARDS.md`, cicd→`CICD_STANDARDS.md`, validation→`VALIDATION_STANDARDS.md`,
  project→`PROJECT_STANDARDS.md`, prompt→`PROMPT_STANDARDS.md`, memory→`MEMORY_PROTOCOL.md`,
  governance→`CLAUDE.md` (rules live in the contract). Unknown/empty Area → `PROJECT_STANDARDS.md`
  (the catch-all) **with a `⚠ unrouted` flag** in the worksheet so Claude routes it by hand.
- **DD-4 — Building the tool is read-only on the vault → NO Set-Version bump** and **no `docs/standards/`
  edit** (same as PLAN-003/004). The worksheet only *reads* `docs/standards/LESSONS.md` (for the next
  `L0NN`) and `STANDARDS_INDEX.md` (for the current Set Version). The Set-Version bump happens later, in a
  session, when a real lesson is integrated.
- **DD-5 — Write-back safety:** the write-back is the only target-repo write in the engine. It (a)
  defaults to dry-run, (b) re-reads each log immediately before writing, (c) edits **only** the matching
  `Status:` line of the named entry (leaves the rest byte-for-byte), (d) errors (no partial write) if an
  entry id named in the decisions file is absent or already non-open, (e) never creates files.

## 3. Scope summary

**In scope:** a new `integrate.py` module (worksheet model + render; Area routing; next-`L0NN`;
decisions-file parse; status write-back with dry-run); `cli.py` wiring (`integrate` subcommand + `--apply`
/ `--write` flags); `errors.py` (one new error if needed); tests; `architecture.md` § 8 mark integrate
implemented; `validation_ownership.toml` soft entry; manifest/CHANGELOG/folder_structure sync; promote
PLAN-006 + tracker to 1.0/CLOSED in the Phase-3 commit.

**Out of scope:** any vault edit (LESSONS/topical/Set-Version) — that is the in-session run-time activity
the worksheet feeds, governed separately; propagation to adopters (`sync`/PLAN-007); a model call (A1);
`integrate` of the in-process kind (rejected).

## 4. Phase tracker (high-level — granular sub-tasks in `PLAN-006_tracker.md`)

| Phase | Status | Date |
|---|---|---|
| 0 — Audit | ✅ done | 2026-06-18 |
| 1 — Design (this plan + tracker) | ✅ done | 2026-06-18 |
| 1.x — Rule 13 senior-review pass (runs ruff + mypy --strict + pytest on the § 5 code) | ✅ done | 2026-06-18 |
| 2 — Operator approval | ✅ APPROVE D1.A | 2026-06-18 |
| 3 — Implement (fresh session, ALLOWLIST-bounded) | ✅ done | 2026-06-18 |
| 4 — Validate (QA A–K + governance) | ✅ done | 2026-06-18 |
| 5 — Operator gate (push; no tag — Set Version unchanged) | ⏸ pending | — |

## 5. Verbatim module spec (Phase 3)

> Verified against live source 2026-06-18 (reuses `harvest.OpenItem`, `logentry`/`registry` loaders, the
> `cli.py` `_build_open_items` pattern, `errors`). The Rule 13 pass runs ruff + mypy --strict + the tests
> against this code (per the elevated lesson — do not eyeball it).

### 5A — new file `src/standard_document_updater/integrate.py`

```python
# ==============================================================
# VERSION: 0.1
# Integration worksheet + status write-back (the deterministic half of `integrate`).
#
# CHANGE LOG
# v0.1 — 2026-06-18 — Initial: Area routing, next-L0NN, worksheet, decisions parse, write-back.
# ==============================================================
"""The deterministic spine of `integrate` (architecture § 6c).

A1 division of labor: this module does only the mechanical parts — collect open
entries, propose the next canonical L0NN, route each entry's Area to a topical
file, and (operator-gated) write the Status line back into each project's log.
The genericization, the L0NN lesson prose, and the vault edits (LESSONS, topical
file, Set Version) are authored by Claude in-session under the § 15 flow; this
module never calls a model and never edits the vault.

Read-only by default. The write-back re-reads each target log immediately before
writing (docs/architecture.md § 9) and rewrites only the matching Status line.
"""
from __future__ import annotations

import re
import tomllib
from dataclasses import dataclass
from pathlib import Path

from standard_document_updater.errors import StandardDocSetError
from standard_document_updater.harvest import OpenItem

# Area (controlled vocab from STANDARDS_LOG) -> destination doc under docs/standards/.
_AREA_TO_TOPICAL: dict[str, str] = {
    "engineering": "ENGINEERING_STANDARDS.md",
    "cicd": "CICD_STANDARDS.md",
    "validation": "VALIDATION_STANDARDS.md",
    "project": "PROJECT_STANDARDS.md",
    "prompt": "PROMPT_STANDARDS.md",
    "memory": "MEMORY_PROTOCOL.md",
    "governance": "CLAUDE.md",
}
_DEFAULT_TOPICAL = "PROJECT_STANDARDS.md"

_LESSON_ID_RE = re.compile(r"^###\s+L(\d+)\b", re.MULTILINE)
# A Status field line in a STANDARDS_LOG.md entry (leading "-", any spacing).
_STATUS_LINE_RE = re.compile(r"^(?P<prefix>-\s*Status:\s*).*$", re.MULTILINE)
_HEADING_RE = re.compile(r"^##[ \t]+(E\d+)\b", re.MULTILINE)


class IntegrateError(StandardDocSetError):
    """A decisions file is malformed, or a write-back target entry cannot be resolved."""


@dataclass(frozen=True)
class WorksheetRow:
    """One open entry, enriched with the deterministic integration proposals."""

    project_name: str
    entry_id: str
    area: str
    topical: str          # routed destination doc
    routed: bool          # False when Area was unknown/empty (catch-all used)
    title: str
    context: str
    learned: str
    suggested: str


def route_area(area: str) -> tuple[str, bool]:
    """Map an entry Area to (destination doc, routed?). Unknown/empty -> catch-all."""
    key = area.lower().strip()
    if key in _AREA_TO_TOPICAL:
        return _AREA_TO_TOPICAL[key], True
    return _DEFAULT_TOPICAL, False


def next_lesson_id(lessons_path: Path) -> str:
    """Next canonical lesson id (max existing L#### + 1), e.g. 'L051'. 'L001' if none/absent."""
    if not lessons_path.exists():
        return "L001"
    nums = [int(m.group(1)) for m in _LESSON_ID_RE.finditer(lessons_path.read_text(encoding="utf-8"))]
    return f"L{(max(nums) + 1) if nums else 1:03d}"


def build_rows(items: list[OpenItem]) -> list[WorksheetRow]:
    """Enrich open items with Area routing (pure; deterministic order preserved)."""
    rows: list[WorksheetRow] = []
    for item in items:
        topical, routed = route_area(item.entry.area)
        rows.append(
            WorksheetRow(
                project_name=item.project_name,
                entry_id=item.entry.entry_id,
                area=item.entry.area or "(unspecified)",
                topical=topical,
                routed=routed,
                title=item.entry.title,
                context=item.entry.context,
                learned=item.entry.learned,
                suggested=item.entry.suggested,
            )
        )
    return rows


def render_worksheet(rows: list[WorksheetRow], proposed_lesson: str, set_version: str) -> str:
    """Render the integration worksheet (deterministic). Read-only; Claude authors from it."""
    if not rows:
        return "No open entries to integrate. (Run `harvest` to review, or check the registry.)"
    next_n = int(proposed_lesson[1:])
    lines = [
        f"Integrate — {len(rows)} open entr{'y' if len(rows) == 1 else 'ies'}; "
        f"vault next lesson {proposed_lesson}; current Set Version {set_version}.",
        "",
        "For each entry you (Claude) decide integrate/reject, then IN-SESSION (under § 15): genericize "
        "(no project names), write the lesson to docs/standards/LESSONS.md, update the routed topical "
        "file, bump per-file VERSION + the Set Version. Then record dispositions in a decisions TOML and "
        "run `integrate --apply <file>` to write the Status lines back.",
    ]
    for i, row in enumerate(rows):
        lesson = f"L{next_n + i:03d}"
        flag = "" if row.routed else "   ⚠ unrouted (Area unknown → default; route by hand)"
        lines += [
            "",
            f"[{row.project_name}] {row.entry_id} — {row.title}",
            f"    area:     {row.area} -> {row.topical}{flag}",
            f"    proposed: {lesson}  (sequential; final id is assigned when you write the lesson)",
            f"    context:  {row.context}",
            f"    learned:  {row.learned}",
            f"    suggested:{row.suggested}",
        ]
    return "\n".join(lines)


@dataclass(frozen=True)
class Disposition:
    """One write-back instruction parsed from the decisions TOML."""

    project: str
    entry: str
    status_line: str   # the full replacement text for the Status: value


def parse_decisions(decisions_path: Path) -> list[Disposition]:
    """Parse the decisions TOML into Status-line write-back instructions.

    Raises IntegrateError on a missing file, bad TOML, or a row missing required keys.
    """
    if not decisions_path.exists():
        raise IntegrateError(f"decisions file not found: {decisions_path}")
    try:
        data = tomllib.loads(decisions_path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise IntegrateError(f"could not parse decisions file {decisions_path}: {exc}") from exc

    out: list[Disposition] = []
    for row in data.get("integrated", []):
        for key in ("project", "entry", "lesson", "topical", "set_version"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise IntegrateError(f"integrated row missing '{key}': {row}")
        status = f"integrated → vault {row['lesson']} ({row['topical']}, Set Version {row['set_version']})"
        out.append(Disposition(row["project"], row["entry"], status))
    for row in data.get("rejected", []):
        for key in ("project", "entry", "reason"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise IntegrateError(f"rejected row missing '{key}': {row}")
        out.append(Disposition(row["project"], row["entry"], f"rejected — {row['reason']}"))
    if not out:
        raise IntegrateError("decisions file has no [[integrated]] or [[rejected]] rows")
    return out


def _rewrite_status(text: str, entry_id: str, new_status: str) -> str:
    """Return `text` with the Status line of `entry_id` replaced. Raises if not found."""
    headings = list(_HEADING_RE.finditer(text))
    for i, h in enumerate(headings):
        if h.group(1) != entry_id:
            continue
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        block = text[h.start() : end]
        new_block, n = _STATUS_LINE_RE.subn(
            lambda m: f"{m.group('prefix')}{new_status}", block, count=1
        )
        if n == 0:
            raise IntegrateError(f"entry {entry_id}: no Status line found")
        return text[: h.start()] + new_block + text[end:]
    raise IntegrateError(f"entry {entry_id} not found in log")


def apply_writeback(
    dispositions: list[Disposition], log_path_for: dict[str, Path], *, write: bool
) -> list[str]:
    """Apply (or dry-run) the Status write-backs. Re-reads each log immediately (§ 9).

    Returns a human-readable report. Raises IntegrateError (before any write) if a
    target project is unknown or an entry/Status line cannot be resolved.
    """
    # Resolve + validate everything first — no partial writes.
    planned: list[tuple[Path, str, str, str]] = []  # (path, entry, new_status, project)
    for d in dispositions:
        log_path = log_path_for.get(d.project)
        if log_path is None:
            raise IntegrateError(f"project not in registry: {d.project}")
        if not log_path.exists():
            raise IntegrateError(f"log not found for {d.project}: {log_path}")
        text = log_path.read_text(encoding="utf-8")
        _rewrite_status(text, d.entry, d.status_line)  # validate (raises if unresolvable)
        planned.append((log_path, d.entry, d.status_line, d.project))

    report: list[str] = []
    for log_path, entry, new_status, project in planned:
        if write:
            text = log_path.read_text(encoding="utf-8")  # re-read immediately before write (§ 9)
            log_path.write_text(_rewrite_status(text, entry, new_status), encoding="utf-8")
            report.append(f"wrote  [{project}] {entry}: Status -> {new_status}")
        else:
            report.append(f"DRY-RUN [{project}] {entry}: Status -> {new_status}")
    if not write:
        report.append("\n(dry-run — re-run with --write to apply)")
    return report
```

### 5B — `cli.py` wiring

Add the `integrate` builders + handler, mirroring `_build_open_items`/`_cmd_harvest`:

```python
# add to imports:
from standard_document_updater import integrate  # alongside harvest, logentry, report, setversion

def _cmd_integrate(args: argparse.Namespace) -> int:
    vault_root: Path = args.vault
    lessons = vault_root / "docs" / "standards" / "LESSONS.md"
    index = vault_root / "docs" / "standards" / "STANDARDS_INDEX.md"
    if args.apply is None:
        rows = integrate.build_rows(_build_open_items(vault_root))
        proposed = integrate.next_lesson_id(lessons)
        set_version = "v" + ".".join(str(n) for n in setversion.parse_vault_version(index))
        print(integrate.render_worksheet(rows, proposed, set_version))
        return 0
    # write-back path
    log_path_for = {
        p.name: p.path / "docs" / "STANDARDS_LOG.md"
        for p in load_registry(vault_root / "config" / "projects.toml")
    }
    dispositions = integrate.parse_decisions(args.apply)
    report = integrate.apply_writeback(dispositions, log_path_for, write=args.write)
    print("\n".join(report))
    return 0
```

Parser (in `build_parser`), plus the handler registration:

```python
p_int = sub.add_parser(
    "integrate",
    help="worksheet of open entries to integrate; --apply <file> writes Status back",
)
p_int.add_argument("--apply", type=Path, default=None,
                   help="decisions TOML; write integrated/rejected Status lines back to project logs")
p_int.add_argument("--write", action="store_true",
                   help="actually write (default is a dry-run diff); only valid with --apply")
# ... handlers = {"status": ..., "drift": ..., "harvest": ..., "integrate": _cmd_integrate}
```

`load_registry` is already imported in `cli.py`; `setversion` is already imported. `integrate` import is new.

### 5C — tests `tests/test_integrate.py`

Cover: `route_area` (each Area + unknown→default+unrouted); `next_lesson_id` (max+1; absent→L001;
none→L001); `build_rows`/`render_worksheet` (empty → message; rows grouped, ⚠ on unrouted; proposed ids
sequential); `parse_decisions` (integrated + rejected rows → Status text; missing key → IntegrateError;
no rows → IntegrateError; bad TOML → IntegrateError); `apply_writeback` (dry-run changes nothing on disk;
`write=True` rewrites only the target Status line and leaves the rest byte-identical; unknown project →
IntegrateError with NO file written; missing entry id → IntegrateError with NO partial write). 2 CLI tests
in `test_cli.py`: `integrate` (worksheet, exit 0) and `integrate --apply <tmp>` dry-run (exit 0, no write).

### 5D — bookkeeping (same commit)

- `validation_ownership.toml`: add a soft `[rules.integrate]` entry (source `integrate.py`, test
  `test_integrate.py`, doc `architecture.md`) — mirrors the existing `harvest` entry.
- `architecture.md` § 8: mark `integrate` implemented (worksheet + gated write-back; A1 division of
  labor); § 10 tick Slice 4 ✅. Header bump. (Read-only on the vault → no Set Version change, DD-4.)
- `cli.py` + `__init__.py`: 0.2 → 0.3 (new subcommand).
- `documents_manifest.md`: register `integrate.py` + `test_integrate.py`; bump touched code cells; promote
  PLAN-006 + tracker → 1.0/CLOSED; header bump.
- `CHANGELOG.md`: top entry + QA sub-section (A–K).
- `folder_structure.md`: add `integrate.py` + `test_integrate.py` to the tree; header bump.

## 6. Spec update map

| Spec / doc | Update | Trigger |
|---|---|---|
| `architecture.md` § 8 / § 10 | integrate implemented; Slice 4 ✅ | engine behavior added (§ 4 drift rule) |
| `validation_ownership.toml` | soft `[rules.integrate]` | new src module |
| `documents_manifest.md` | new module + test rows; cells; plan promotion | Rule 8 |
| `folder_structure.md` | integrate.py + test_integrate.py | new tracked files |
| `CHANGELOG.md` | top entry + QA sub-section | every behavior change (Rule 11) |

No `docs/standards/` edit and **no Set-Version bump** (DD-4).

## 7. ALLOWLIST (Phase 3 — the bullet enumeration IS the count: 9 tracked)

1. `src/standard_document_updater/integrate.py` (new)
2. `src/standard_document_updater/cli.py` (wire subcommand; 0.2→0.3)
3. `src/standard_document_updater/__init__.py` (0.2→0.3)
4. `tests/test_integrate.py` (new)
5. `tests/test_cli.py` (+2 integrate cases)
6. `scripts/validation_ownership.toml` (soft rule)
7. `docs/architecture.md` (§ 8 / § 10 + header)
8. `docs/documents_manifest.md` (register + cells + plan promotion + header)
9. `docs/folder_structure.md` (tree + header)
10. `CHANGELOG.md`
11. `docs/Plans/PLAN-006_integrate.md` (this plan → 1.0/CLOSED)
12. `docs/Plans/PLAN-006_tracker.md` (→ 1.0/CLOSED)

(12 enumerated — `errors.py` is touched ONLY IF a new error class is added; `IntegrateError` lives in
`integrate.py` per § 5A, so `errors.py` is **not** in the ALLOWLIST. `OPEN_TASKS.md` is gitignored —
edited, not staged.) Anything else staged → STOP and report (Rule 7).

## 8. Validation gate (Phase 4 — QA scenarios per Rule 11)

| ID | Verify | How | Pass |
|---|---|---|---|
| A | ruff clean | `.venv/bin/ruff check src tests` | exit 0 |
| B | mypy --strict clean | `MYPYPATH=src .venv/bin/python -m mypy` | 0 issues |
| C | full test suite | `.venv/bin/python -m pytest -q` | all green (35 prior + new) |
| D | governance | both Rule-2 scripts | exit 0 |
| E | worksheet, empty registry | `integrate` with empty `config/projects.toml` | "No open entries…", exit 0 |
| F | worksheet content | fixture project, 1 open entry | row shows project/entry/area→topical, proposed L0NN, Set Version; exit 0 |
| G | Area routing | unit: each Area → file; unknown → PROJECT_STANDARDS + `routed=False` | matches DD-3 |
| H | next-`L0NN` | unit: against the real `docs/standards/LESSONS.md` | returns `L051` (current max L050 + 1) |
| I | write-back dry-run | `integrate --apply <decisions.toml>` (no `--write`) | prints planned changes; **no file modified** |
| J | write-back write | `--apply … --write` on a fixture log | only the named `Status:` line changes; rest byte-identical |
| K | write-back safety | decisions referencing an unknown project / missing entry | `IntegrateError`; **no file written** (atomic) |

## 9. Operator approval decision point (Phase 2)

Approve as **D1.A** to implement as drafted, or specify deltas. Worth an explicit nod: **DD-1** (one
subcommand + `--apply`/`--write`), **DD-2** (TOML decisions handoff), **DD-5** (write-back is dry-run by
default, validate-all-before-write). No code is touched until approval lands; Phase 3 runs in a **fresh
session** prompted from this committed plan + `OPEN_TASKS.md` (per [[feedback_plan_handoff_via_open_tasks]]).

## 10. Rollback path

New module + additive CLI wiring + additive tests/docs. Rollback = `git revert` the Phase-3 commit; no
vault content was touched (DD-4), no target log is modified unless `integrate --apply … --write` was run
(a separate, later, operator-gated action, not part of building the tool).

## 11. Known risks

| # | Risk | Mitigation | Status |
|---|---|---|---|
| R1 | Write-back corrupts/clobbers a target log | dry-run default; validate-all-before-write (no partials); rewrite only the matched `Status:` line; re-read immediately before write (§ 9); leave the rest byte-identical (QA J) | mitigated |
| R2 | Write-back to the wrong/unintended project | only projects named in the decisions file AND present in the registry are touched; unknown project → hard error (QA K) | mitigated |
| R3 | `Area` vocab drifts from the topical-file set | unknown Area → catch-all + visible `⚠ unrouted`, never a silent mis-route | mitigated |
| R4 | Worksheet's proposed `L0NN` races a concurrent vault edit | the proposed id is advisory; the **final** id is assigned when Claude writes the lesson, and the decisions file records the actual id used | mitigated |
| R5 | `governance` Area has no single topical file | routed to `CLAUDE.md`; worksheet footer reminds Claude a governance lesson may be a rule + a LESSONS entry rather than a topical sub-section | open (handled in-session) |

## 12. Acceptance criteria

- `integrate` prints a deterministic worksheet (open entries + Area→topical + proposed `L0NN` + Set
  Version); exit 0; empty registry handled.
- `integrate --apply <decisions.toml>` dry-runs by default and only writes with `--write`; writes only
  the named `Status:` lines; validates all before writing (atomic); errors on unknown project/entry.
- QA A–K pass; governance exit 0. No `docs/standards/` edit; **no Set-Version bump**.
- `architecture.md` § 8/§ 10 updated; manifest/folder_structure synced; PLAN-006 + tracker → 1.0/CLOSED.
