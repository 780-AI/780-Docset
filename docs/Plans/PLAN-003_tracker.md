<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-16 -->
<!-- Status: CLOSED (tracks PLAN-003) -->
<!--
CHANGE LOG
v1.0 — 2026-06-16 13:01 — Phases 2–4 marked done in the ship commit; promoted to CLOSED with the plan.
Phase 3 landed all 16 new files + 5 edits (ALLOWLIST-bounded). Phase 4 QA A–I PASSED (D1–D3 plan-defect
fixes per the plan CHANGE LOG). Phase 5 push held for the operator gate.
v0.1 — 2026-06-16 — Sibling tracker created same-commit as the PLAN-003 draft (per § 15.7; triggered
by first-engine-code + multi-scenario QA list A–I). Phases 0–1 done; 2–5 pending.
-->

# PLAN-003 tracker — Slice 2: registry + `status` / `drift`

Sibling tracker for `docs/Plans/PLAN-003_registry_status_drift.md` (per `CLAUDE.md` § 15.7).
Single-agent project → `Owner:` header omitted (§ 14.4). Status markers: ⏸ pending · 🔄 in-progress ·
✅ done · ❌ blocked. Updated **same-commit** as the work it tracks; promoted to v1.0 / CLOSED with the plan.

---

## Phase 0 — Audit ✅ 2026-06-16

- ✅ Integration points cited by `file:line`: vault version `docs/standards/STANDARDS_INDEX.md:37`;
  adopted version `docs/SET_VERSION_ADOPTED.md` (`- **Standard Set Version:** v1.1`); open-log schema
  `docs/standards/STANDARDS_LOG.md:38-48`.
- ✅ External deps verified: `tomllib` is stdlib ≥3.11 (no runtime dep); no `src/`/`tests/`/`pyproject`
  exist yet (greenfield); governance scripts are permissive scaffolds (won't block new files); CI `test`
  stage is commented-out (left untouched this slice).
- ✅ Target asymmetry confirmed: adopters carry `SET_VERSION_ADOPTED.md` + `STANDARDS_LOG.md` but NOT
  `STANDARDS_INDEX.md` (stripped) — only the vault carries the canonical version.

## Phase 1 — Design ✅ 2026-06-16

- ✅ Plan drafted (§§ 1–12) with full verbatim file contents in § 5.
- ✅ Sibling tracker created (this file).
- ✅ Operator decisions locked at design: registry name+path/live-read · two subcommands · stay small
  (defer CI) · columns confirmed.
- ✅ Rule 13 senior-review-and-optimize pass — 2026-06-16; 4 defects fixed in place (render_table width
  calc, tests.conftest import → fixture, redundant cli __main__ block, mypy explicit_package_bases);
  ALLOWLIST 18→21; drift exit-code decision surfaced. Recorded in plan CHANGE LOG + foot.

## Phase 2 — Operator approval ✅ 2026-06-16

- ✅ `APPROVE PLAN-003` (recorded in OPEN_TASKS) + drift exit-code semantics confirmed (R5: unknown/ahead count as drift).

## Phase 3 — Implement (fresh session; one commit, ALLOWLIST-bounded) ✅ 2026-06-16

Source package:
- ✅ `src/standard_document_updater/__init__.py` (§ 5A)
- ✅ `src/standard_document_updater/errors.py` (§ 5B)
- ✅ `src/standard_document_updater/registry.py` (§ 5C)
- ✅ `src/standard_document_updater/setversion.py` (§ 5D)
- ✅ `src/standard_document_updater/report.py` (§ 5E — D1: `StrEnum` per ruff UP042)
- ✅ `src/standard_document_updater/cli.py` (§ 5F)
- ✅ `src/standard_document_updater/__main__.py` (§ 5G — kept verbatim)

Config + packaging:
- ✅ `config/projects.toml` (§ 5H — empty, commented example)
- ✅ `pyproject.toml` (§ 5I)

Tests:
- ✅ `tests/conftest.py` (§ 5J)
- ✅ `tests/test_setversion.py` (§ 5K)
- ✅ `tests/test_registry.py` (§ 5L)
- ✅ `tests/test_report.py` (§ 5M — D2: signature reflow per ruff E501)
- ✅ `tests/test_cli.py` (§ 5N — D3: dotted import idiom per mypy --strict)

Governance + doc sync:
- ✅ `scripts/validation_ownership.toml` (§ 5O — soft monitor + 4 rules)
- ✅ `docs/folder_structure.md` (§ 5P — Planned → live; bump 0.5→0.6)
- ✅ `docs/architecture.md` (§ 5Q — § 8/§ 10 tick Slice 2, § 11 resolve 3 decisions; bump 0.3→0.4)
- ✅ `docs/documents_manifest.md` (§ 5R — +12 code rows; promoted plan rows 34–35; bump 1.5→1.6)
- ✅ `CHANGELOG.md` (§ 5S — top entry + QA sub-section)
- ✅ NO Set Version bump · NO `.gitlab-ci.yml` · NO `CLAUDE.md` (verified absent from `git status`, R6)

## Phase 4 — Validate ✅ 2026-06-16 (QA scenarios A–I, Rule 11)

- ✅ A — `python -m standard_document_updater status`, empty registry → "No projects registered", exit 0
- ✅ B — status, project current (v1.1) → `current`, exit 0 (test_cli / test_report)
- ✅ C — status, project behind (v1.0) → `behind`, exit 0 (test_cli `test_status_lists_project_exit_zero`)
- ✅ D — drift, all current → "No drift", exit 0 (test_cli `test_drift_all_current_exits_zero`)
- ✅ E — drift, one behind → lists it, exit 1 (test_cli `test_drift_behind_exits_one`)
- ✅ F — unknown target (no `SET_VERSION_ADOPTED.md`) → status `unknown`/exit 0; drift exit 1 (test_report + test_cli)
- ✅ G — open-log count (open/integrated/rejected mix) → only `open` counted (test_setversion)
- ✅ H — `ruff check src tests` clean · `mypy --strict` clean (12 files) · 21 pytest green
- ✅ I — governance: `check_doc_coverage.py` + `check_test_coverage_drift.py --ci` both exit 0

> Env: validated via `PYTHONPATH=src` / `MYPYPATH=src` (§ 8 alternative) — the `pip install -e` `.pth`
> wasn't honored by site processing on this machine (space in repo path); no pyproject defect.

## Phase 5 — Operator gate ⏸ (push held)

- ⏸ push (no tag — engine code, Set Version unchanged) — **held for operator**
- ✅ promoted PLAN-003 + this tracker to v1.0 / CLOSED (same commit as Phase 3 ships, per § 15.5/§15.7)
- ⏸ OPEN_TASKS: mark Slice 2 done; add follow-ups (register real targets; CLAUDE.md § 4 cleanup) — post-commit
