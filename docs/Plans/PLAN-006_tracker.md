<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-18 -->
<!-- Status: CLOSED -->
<!--
CHANGE LOG
v1.0 — 2026-06-18 — Phase 3 + Phase 4 complete (one commit). All Phase-3 sub-tasks 3.1–3.11 ✅; QA A–K ✅
(ruff/mypy --strict 18 files/57 pytest; governance exit 0; live worksheet + dry-run + write + safety).
D1 E501 reflow (output-preserving, footer SHA-verified) recorded in the plan CHANGE LOG. Phase 5 (push)
held for the operator gate. Promoted to 1.0/CLOSED same-commit as the implementation.
v0.1 — 2026-06-18 — Sibling tracker created same-commit as the PLAN-006 DRAFT (big plan per § 15.7:
new module + a target-repo write, multi-scenario Phase-4 verify, likely spans sessions).
-->

# PLAN-006 tracker — Slice 4: `integrate` (worksheet + write-back)

Sibling of [`PLAN-006_integrate.md`](PLAN-006_integrate.md). Updated same-commit as the work it tracks.
Markers: ⏸ pending · 🔄 in-progress · ✅ done · ❌ blocked · ⏭ skipped.

---

## Phase 0 — Audit ✅ 2026-06-18

- ✅ `integrate` inputs/outputs grounded in source (reuse `harvest.OpenItem` + `_build_open_items`).
- ✅ Area→topical map confirmed against the dispatcher (CLAUDE.md § 12).
- ✅ `setversion.py` confirmed parse-only (no writer) → bump is in-session, not tool code (A1/DD-4).
- ✅ Topical files use numbered `## N` sections; LESSONS at L050 → next `L051`; Set Version v1.2.

## Phase 1 — Design ✅ 2026-06-18

- ✅ Plan drafted (§§ 1–12) with A/A/A baked in + DD-1…DD-5 + full § 5 module spec; sibling tracker.
- ✅ **Rule 13 senior-review pass** (2026-06-18) — materialized the § 5 code in src/ + a real test,
  RAN ruff + mypy --strict + pytest (not eyeballed), removed scratch. Caught 1 E501 (§ 5A header line)
  → fixed; mypy clean (18 files); 46 tests pass. Recorded in plan CHANGE LOG. **Ready for Phase 2.**

## Phase 2 — Operator approval ✅ 2026-06-18 (APPROVE D1.A)

- ✅ Operator approved D1.A (recorded in OPEN_TASKS 2026-06-18). DD-1 / DD-2 / DD-5 confirmed.

## Phase 3 — Implement ✅ 2026-06-18 (fresh session, ALLOWLIST = § 7)

- ✅ 3.1 `integrate.py` (routing, next-L0NN, worksheet, decisions parse, write-back) [5A]
- ✅ 3.2 `cli.py` wire `integrate` + `--apply`/`--write` (0.2→0.3) [5B]
- ✅ 3.3 `__init__.py` 0.2→0.3
- ✅ 3.4 `tests/test_integrate.py` (20 unit: routing / next-L0NN / worksheet / decisions / write-back atomicity) [5C]
- ✅ 3.5 `tests/test_cli.py` +2 integrate cases (0.2→0.3)
- ✅ 3.6 `validation_ownership.toml` soft `[rules.integrate]`
- ✅ 3.7 `architecture.md` § 8 / § 10 + § 11 OPEN resolved + header 0.6→0.7 (no Set-Version bump — DD-4)
- ✅ 3.8 `documents_manifest.md` register (61–62) + cells + plan promotion + header 2.1→2.2
- ✅ 3.9 `folder_structure.md` tree + header 0.8→0.9
- ✅ 3.10 `CHANGELOG.md` top entry + QA A–K sub-section
- ✅ 3.11 Promote PLAN-006 + this tracker → 1.0 / CLOSED (same commit)
- ⚠ D1 (mechanical): 5 E501 over-length lines in the verbatim § 5A code reflowed output-preserving
  (footer SHA-verified byte-identical, len 345); recorded in plan CHANGE LOG.

## Phase 4 — Validate ✅ 2026-06-18 (QA A–K, plan § 8)

- ✅ A ruff (exit 0) · ✅ B mypy --strict (18 files, 0 issues) · ✅ C pytest (57 passed) · ✅ D governance (both exit 0)
- ✅ E worksheet empty-registry ("No open entries…", exit 0) · ✅ F worksheet content (project/entry/area→topical, proposed L0NN, Set Version v1.2)
- ✅ G Area routing (engineering→ENGINEERING_STANDARDS.md; bizarre→PROJECT_STANDARDS.md ⚠ unrouted) · ✅ H next-L0NN (=L051, real LESSONS max L050 + 1)
- ✅ I write-back dry-run (file SHA unchanged) · ✅ J write-back write (only the 2 Status lines changed; rest byte-identical) · ✅ K safety (unknown project → error, exit 2, log unchanged)

## Phase 5 — Operator gate ⏸

- ⏸ 5.1 push (no tag — Set Version unchanged, DD-4)
