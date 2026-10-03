<!-- VERSION: 0.2 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Status: APPROVED (tracks PLAN-013; promoted to 1.0/CLOSED with the plan) -->
<!--
CHANGE LOG
v0.2 — 2026-10-03 — Phase 2 approval recorded ("approve plan 013"; D-1…D-5 = A, plan § 9.1).
v0.1 — 2026-10-03 — Created with the plan draft (tracker required per § 15.7: Phase 4 is
multi-scenario, QA-K1…K6, and K4/K5 fire at later triggers).
-->

# PLAN-013 tracker — engine write safety (clock floor + accumulating handoffs)

## Phase 0 — Audit

- ✅ 2026-10-03 — write sites cited (`_cmd_integrate`, `_cmd_sync`: `date.today()` unchecked;
  handoff `write_text` overwrite at both); live evidence (CS 7 files vs handoff 3; 780-VPN v2.6
  handoff un-landed); baseline ruff clean / mypy 42+25 / pytest 111.

## Phase 1 — Design

- ✅ 2026-10-03 — § 5 code developed + proven in a scratch overlay (ruff clean; mypy error set
  identical; pytest 119); real-data preview (CS legacy handoff wrapped; floors CS 2026-09-05,
  780-VPN 2026-10-03).
- ✅ 2026-10-03 — plan drafted (§§ 1–12) + this tracker.
- ✅ 2026-10-03 — Rule 13 pass RUN + recorded at the plan's foot.

## Phase 2 — Operator approval

- ✅ 2026-10-03 — operator: **"approve plan 013"** — D13.A + D-1…D-5 at the recommended options
  (offline floor guard / accumulate / strict / no override / CS v2.6 catch-up as QA-K4); recorded
  at plan v0.2 § 9.1.

## Phase 3 — Implement (fresh session; single commit; ALLOWLIST-bounded)

- ⏸ Reconcile pass: every § 5/§ 6 FIND byte-matches live source (else: named plan defect).
- ⏸ Clock verified externally; `<P3-DATE>` substituted; § 5 + § 6 applied byte-for-byte.
- ⏸ Manifest cells + CHANGELOG; plan + tracker → 1.0/CLOSED (after K2–K4 per Rule 15).

## Phase 4 — Validate (scenario ledger)

| # | Scenario | Status | Date | Evidence |
|---|---|---|---|---|
| QA-K1 | ruff / mypy error set / pytest 119 | ⏸ | | |
| QA-K2 ⚑ | live dry-run: notes, no false warning, plans unchanged | ⏸ | | |
| QA-K3 ⚑ | clock guard on a real-data scratch copy | ⏸ | | |
| QA-K4 ⚑ | accumulation — sync half (CS v2.6 catch-up, D-5) | ⏸ | | |
| QA-K5 ⚑ | accumulation — write-back half (E001 write-back) | ⏸ | | |
| QA-K6 | idempotence after K4/K5 | ⏸ | | |

Waiver register (Rule 15): _(empty)_

## Phase 5 — Operator gate

- ⏸ Push (operator). No tag — engine-only, no Set Version change.
