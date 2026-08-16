<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Status: APPROVED -->
<!--
CHANGE LOG
v0.1 — 2026-08-16 — Sibling tracker created same-commit as the PLAN-008 DRAFT (big plan per § 15.7:
multi-scenario Phase-4 verify A–J; 25-file ALLOWLIST; spans sessions — Phase 3 is a fresh session).
Same session: Phase 2 **APPROVE D8.A** recorded (operator, 2026-08-16).
-->

# PLAN-008 tracker — Slice 5: `sync` (Set v1.6)

Sibling of [`PLAN-008_sync.md`](PLAN-008_sync.md). Updated same-commit as the work it tracks.
Markers: ⏸ pending · 🔄 in-progress · ✅ done · ❌ blocked · ⏭ skipped.

---

## Phase 0 — Audit ✅ 2026-08-16

- ✅ architecture § 7 (ownership model) + § 8 (command surface) + § 9 (invariants) re-read; § 10/§ 11
  slice/decision state confirmed (sync = the one open slice).
- ✅ Engine read in full: transport.py (session/materialize/flush seams), cli.py (command dispatch +
  integrate's ExitStack write pattern), registry.py (Project fields), integrate.py (dry-run/--write
  gate precedent + validate-all-before-write), setversion.py (DD-1 target), logentry.py (parse_log
  semantics — absent file → []), report.py (count_open_log_entries caller).
- ✅ Marker inventory verified against live files: template CLAUDE.md 4 PROJECT-OWNED blocks = root
  instance 4 (ordinal-matchable); opener template 2 = instance 2; closer 1 = 1 (pre-v1.6). Template
  § 14 BEGIN comment says "delete this entire § 14 block" — a sync-breaking instruction (5G-5 fixes).
- ✅ Materialization gap confirmed (the OPEN_TASKS standing question): sync's footprint includes
  `archive/LESSONS.md` + root `CLAUDE.md`, outside the docs/-only ssh rsync + git sparse read set →
  DD-B (full sessions). Git cone-mode sparse already includes root files; writable clones are full.
- ✅ Toolchain: `.venv` python 3.11.15; ruff (E,F,I,UP,B; line 100), mypy strict=true, pytest — the
  Rule-2 + L051 tool set.

## Phase 1 — Design ✅ 2026-08-16

- ✅ Plan drafted (§§ 1–12): SYNC_MAP + DD-A…DD-I settled; D1/D2 surfaced as § 9 operator decisions;
  25-file ALLOWLIST (plan + tracker promotion rows included per L054); § 8 QA A–J.
- ✅ **§ 5 code developed and proven BEFORE embedding** (L051 + recurrence #4 — tools run at the exact
  final ship indentation, in a scratch overlay of src/ + tests/):
  `ruff check src tests` → clean; `MYPYPATH=src python -m mypy` → "no issues found in 22 source
  files"; `python -m pytest` → **110 passed** (88 existing + 22 new: 14 test_sync + 5 cli sync +
  2 transport full + 1 setversion DD-1). The plan's fenced blocks are byte-copies of the proven files.
- ✅ **Rule 13 senior-review pass** (2026-08-16, mechanical per L051 + recurrence #4 — run against
  the PLAN FILE's own text): 10/10 § 5 blocks re-extracted + byte-identical to the proven overlay;
  fresh tree from the EXTRACTED blocks → ruff clean, mypy --strict clean (22 files), pytest 110
  passed; 7/7 § 5G FIND blocks anchor exactly once in their live targets; cross-section counts
  reconciled (ALLOWLIST 25 = Phase-3 rows 25; § 3 map 11 = SYNC_MAP 11; QA A–J ↔ tracker); domain
  grep plan + tracker = 0 hits. Findings recorded in the plan CHANGE LOG v0.1a. **Ready for
  Phase 2.**

## Phase 2 — Operator approval ✅ 2026-08-16

- ✅ **APPROVE D8.A** (2026-08-16) — full § 5 as specified; D1 (v1.6 markers) + D2 (§ 3.1
  suite-owned) confirmed; QA-E ssh waiver confirmed.

## Phase 3 — Implement ⏸ (fresh session; single commit; ALLOWLIST = plan § 7)

- ⏸ 3.1 sync.py NEW [5A] · ⏸ 3.2 transport.py [5B] · ⏸ 3.3 cli.py [5C] ·
  ⏸ 3.4 setversion.py [5D] · ⏸ 3.5 __init__.py [5E]
- ⏸ 3.6 test_sync.py NEW [5F1] · ⏸ 3.7 conftest.py [5F2] · ⏸ 3.8 test_transport.py [5F3] ·
  ⏸ 3.9 test_cli.py [5F4] · ⏸ 3.10 test_setversion.py [5F5]
- ⏸ 3.11 template SESSION_OPENER [5G-1] · ⏸ 3.12 template SESSION_CLOSER [5G-2] ·
  ⏸ 3.13 project SESSION_OPENER [5G-3] · ⏸ 3.14 project SESSION_CLOSER [5G-4] ·
  ⏸ 3.15 template CLAUDE.md § 14 wording [5G-5] · ⏸ 3.16 SETUP [5G-6] · ⏸ 3.17 NPB [5G-7]
- ⏸ 3.18 STANDARDS_INDEX → v1.6 [5H-1] · ⏸ 3.19 SET_VERSION_ADOPTED → adopt v1.6 [5H-2] ·
  ⏸ 3.20 architecture.md [5H-3] · ⏸ 3.21 documents_manifest [5H-4] · ⏸ 3.22 folder_structure [5H-5] ·
  ⏸ 3.23 CHANGELOG [5H-6]
- ⏸ 3.24 PLAN-008 → 1.0/CLOSED · ⏸ 3.25 this tracker → 1.0/CLOSED [5H-7]

## Phase 4 — Validate ⏸ (QA A–J, plan § 8)

- ⏸ A tools at ship indentation (ruff / mypy --strict / pytest 110) ·
  ⏸ B test_sync 14 cases · ⏸ C CLI feature-ON local (5 cases + manual dry-run→write→idempotent) ·
  ⏸ D git feature-ON vs local bare remote (scripted) ·
  ⏭ E ssh live path — **operator-waived to the post-registration live smoke** (Rule 15 waiver;
  pairs with PLAN-007 QA K–N) ·
  ⏸ F v1.6 stamp/parity greps · ⏸ G marker integrity counts · ⏸ H governance ·
  ⏸ I domain-neutral zero-hit · ⏸ J manifest completeness

## Phase 5 — Operator gate ⏸

- ⏸ 5.1 push + annotated tag `set-v1.6`
