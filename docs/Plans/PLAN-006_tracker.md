<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-06-18 -->
<!-- Status: DRAFT -->
<!--
CHANGE LOG
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

## Phase 1 — Design 🔄 2026-06-18

- ✅ Plan drafted (§§ 1–12) with A/A/A baked in + DD-1…DD-5 + full § 5 module spec; sibling tracker.
- ✅ **Rule 13 senior-review pass** (2026-06-18) — materialized the § 5 code in src/ + a real test,
  RAN ruff + mypy --strict + pytest (not eyeballed), removed scratch. Caught 1 E501 (§ 5A header line)
  → fixed; mypy clean (18 files); 46 tests pass. Recorded in plan CHANGE LOG. **Ready for Phase 2.**

## Phase 2 — Operator approval ⏸

- ⏸ Operator response (expected "APPROVE D1.A" or deltas). Confirm DD-1 / DD-2 / DD-5.

## Phase 3 — Implement ⏸ (fresh session, ALLOWLIST = § 7)

- ⏸ 3.1 `integrate.py` (routing, next-L0NN, worksheet, decisions parse, write-back) [5A]
- ⏸ 3.2 `cli.py` wire `integrate` + `--apply`/`--write` (0.2→0.3) [5B]
- ⏸ 3.3 `__init__.py` 0.2→0.3
- ⏸ 3.4 `tests/test_integrate.py` (routing / next-L0NN / worksheet / decisions / write-back atomicity) [5C]
- ⏸ 3.5 `tests/test_cli.py` +2 integrate cases
- ⏸ 3.6 `validation_ownership.toml` soft `[rules.integrate]`
- ⏸ 3.7 `architecture.md` § 8 / § 10 + header (no Set-Version bump — DD-4)
- ⏸ 3.8 `documents_manifest.md` register + cells + plan promotion + header
- ⏸ 3.9 `folder_structure.md` tree + header
- ⏸ 3.10 `CHANGELOG.md` top entry + QA sub-section
- ⏸ 3.11 Promote PLAN-006 + this tracker → 1.0 / CLOSED (same commit)

## Phase 4 — Validate ⏸ (QA A–K, plan § 8)

- ⏸ A ruff · ⏸ B mypy --strict · ⏸ C pytest · ⏸ D governance
- ⏸ E worksheet empty-registry · ⏸ F worksheet content · ⏸ G Area routing · ⏸ H next-L0NN (=L051)
- ⏸ I write-back dry-run (no file changed) · ⏸ J write-back write (only Status line) · ⏸ K safety (atomic, errors)

## Phase 5 — Operator gate ⏸

- ⏸ 5.1 push (no tag — Set Version unchanged, DD-4)
