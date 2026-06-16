<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-16 -->
<!-- Status: CLOSED (tracks PLAN-004) -->
<!--
CHANGE LOG
v1.0 — 2026-06-16 — Phase 3 (Implement) + Phase 4 (Validate) done same-commit as the slice ships.
QA A–H ✅ (ruff + mypy --strict + 35 pytest green; both governance scripts exit 0; live CLI A/B/C/D/G).
Plan-defect D1 (E501 reflow) resolved mechanically. Promoted to 1.0/CLOSED. Phase 5 push held for operator.
v0.1 — 2026-06-16 18:06 — Sibling tracker created same-commit as the PLAN-004 draft (per § 15.7;
triggered by first-of-kind module + multi-scenario QA list A–H + expected cross-session Phase 3).
Phases 0–1 done; 2–5 pending.
-->

# PLAN-004 tracker — Slice 3: `harvest`

Sibling tracker for `docs/Plans/PLAN-004_harvest.md` (per `CLAUDE.md` § 15.7). Single-agent project →
`Owner:` header omitted (§ 14.4). Status: ⏸ pending · 🔄 in-progress · ✅ done · ❌ blocked. Updated
**same-commit** as the work it tracks; promoted to v1.0 / CLOSED with the plan.

---

## Phase 0 — Audit ✅ 2026-06-16

- ✅ Integration points cited by `file:line`: `registry.py:31` `load_registry`; `setversion.py:53`
  `count_open_log_entries` (+ `_ENTRY_RE:30` / `_STATUS_RE:31`); `report.py:71` render pattern;
  `cli.py:29` `_build_statuses` + `cli.py:68` subparser block; `errors.py:20` `ParseError`.
- ✅ Log schema confirmed against `docs/standards/STANDARDS_LOG.md:38-48` + the E001 example (multi-line
  free-text fields; em-dash heading; controlled-vocab area/status/portability).
- ✅ External deps: none new (`re`, `dataclasses`, `collections.defaultdict` — all stdlib). `conftest.py`
  fixtures (`make_vault`/`make_project`/`write_registry`) suffice for the CLI tests.
- ✅ Confirmed `harvest` needs only the registry + each project's log (not the vault Set Version /
  STANDARDS_INDEX) → reuses `--vault` to locate `config/projects.toml`.

## Phase 1 — Design ✅ 2026-06-16

- ✅ Plan drafted (§§ 1–12) with full verbatim § 5 contents (2 new modules + cli/init diffs + 2 test files).
- ✅ Operator design decisions locked: **D1** stdout only · **D2** defer `--json` · **D3** cautious
  cross-project title-only dup flag · **D4** always exit 0.
- ✅ Sibling tracker created (this file).
- ✅ Rule 13 senior-review-and-optimize pass — 2026-06-16; 6 findings applied in place (unused
  `_CONTROLLED` removed, long line reflow vs E501, `LogEntry` field defaults for fixture-free tests,
  dup same-project exclusion + write-back scenarios C/E, import-order + two-commit manifest split,
  DD-1 surfaced). Recorded in plan CHANGE LOG + § 11 + the plan foot.

## Phase 2 — Operator approval ✅ 2026-06-16

- ✅ `APPROVE PLAN-004` — operator approved 2026-06-16 (recorded in OPEN_TASKS).

## Phase 3 — Implement (fresh session; one commit, ALLOWLIST-bounded) ✅ 2026-06-16

New source:
- ✅ `src/standard_document_updater/logentry.py` (§ 5A)
- ✅ `src/standard_document_updater/harvest.py` (§ 5B; D1: line-85 reflow vs E501)

Modified source:
- ✅ `src/standard_document_updater/cli.py` (§ 5C — C1 header, C2 import, C3 builder+handler, C4 subparser, C5 dispatch; 0.1→0.2)
- ✅ `src/standard_document_updater/__init__.py` (§ 5D — header 0.1→0.2, `__version__` 0.1.0→0.2.0)

Tests:
- ✅ `tests/test_logentry.py` (§ 5E)
- ✅ `tests/test_harvest.py` (§ 5F)
- ✅ `tests/test_cli.py` (§ 5C tests note — appended 2 harvest tests; 0.1→0.2)

Governance + doc sync:
- ✅ `scripts/validation_ownership.toml` (+ `[rules.logentry]` + `[rules.harvest]`, soft)
- ✅ `docs/folder_structure.md` (added 2 src + 2 test files; 0.6→0.7)
- ✅ `docs/architecture.md` (§ 8 harvest ✅ + behavior note; § 10 Slice 3 ✅; 0.4→0.5)
- ✅ `docs/documents_manifest.md` (appended 4 code rows as Engine 50–53 → quick-index Engine range
  38–49 → 38–53; bumped cli/__init__/test_cli cells 0.1→0.2; promoted PLAN-004 plan+tracker 0.1→1.0
  CLOSED; 1.7→1.8)
- ✅ `CHANGELOG.md` (top entry + QA sub-section A–H)
- ✅ Verified NO Set Version bump · NO `.gitlab-ci.yml` · NO `CLAUDE.md` (Rule 6 `git status` check)

## Phase 4 — Validate ✅ 2026-06-16 (QA scenarios A–H, Rule 11)

- ✅ A — `harvest` empty registry → "No open log entries…", exit 0 (live CLI against real empty registry)
- ✅ B — `harvest` one project, 2 open entries → both listed under area, exit 0 (live + `test_cli`)
- ✅ C — parser: status write-back → `is_open` False (only `open` harvested) (`test_logentry` + live)
- ✅ D — dup: same title, different projects → both flagged (`test_harvest` + live)
- ✅ E — dup: same title, same project → not flagged (`test_harvest`)
- ✅ F — dup: distinct titles → not flagged (`test_harvest`)
- ✅ G — grouping: ≥2 areas → one sorted `## area (n)` block each (`test_harvest` + live)
- ✅ H — ruff clean · mypy --strict clean (16 files; plan estimated 14) · 35 pytest green · both
  governance scripts exit 0

## Phase 5 — Operator gate ⏸

- ⏸ push (no tag — engine code, Set Version unchanged) — held for operator
- ✅ promoted PLAN-004 + this tracker to v1.0 / CLOSED (this commit)
- ⏸ OPEN_TASKS: mark Slice 3 done; add DD-1 (setversion DRY) follow-up (local-only register; updated post-commit)
