<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-10-04 -->
<!-- Status: DRAFT (tracks PLAN-016 — Phases 0–1 done; awaiting Phase 2 approval) -->
<!--
CHANGE LOG
v0.1 — 2026-10-04 — Created with the plan draft (tracker required per CLAUDE.md § 15.7: Phase 4 is
multi-scenario, QA-L1…L8).
-->

# PLAN-016 tracker — fleet view (`docs/fleet.csv`)

## Phase 0 — Audit

- ✅ 2026-10-04 — § 15.9 intake: operator request (no document); decisions 1–4 recorded (plan § 2).
- ✅ 2026-10-04 — integration points cited by `file:line` (plan § 3): the shared probe
  (`cli.py:58-73`), handoff record counting (`sync.py:320-339`), the registry's unknown-key gap
  (`registry.py:59-110`), the private version formatter (`report.py:76`), the ssh transport
  (`transport.py:150-160`), the governance script + CI job (`.gitlab-ci.yml:20-22`).
- ✅ 2026-10-04 — baseline on a scratch overlay of `23d2ef2`: ruff clean, mypy --strict 0 errors,
  pytest 120 passed.

## Phase 1 — Design

- ✅ 2026-10-04 — code developed + tool-proven in the overlay (ruff clean / mypy 0 / pytest 140).
- ✅ 2026-10-04 — read-only real-fleet preview (scratch vault copy, 4 targets): rows correct; 75 s →
  10.1 s with D-4; gate failure paths F1–F6 fired as designed.
- ✅ 2026-10-04 — § 5 / § 6 blocks generated from the overlay (no hand-copying).
- ✅ 2026-10-04 — Rule 13 senior-review pass (record at the foot of the plan).

## Phase 2 — Operator approval

- ⏸ "APPROVE PLAN-016" + D-1…D-5 (D-3 = the per-project values). Approval commit: plan + tracker
  0.1 → 0.2 APPROVED (+ any D-3 correction applied to § 6a; any D-1/D-2/D-5 = B → plan revision +
  Rule 13 re-run in that commit).

## Phase 3 — Implement (fresh session; single commit; AFTER the PLAN-011 closure commit)

- ⏸ Pre-checks: PLAN-011 closure commit landed; clock verified externally (`<P3-DATE>`);
  `<P3C-DATE>` read from the closure commit.
- ⏸ Reconcile pass: every § 5 / § 6 FIND matches the live tree exactly once (else: named defect).
- ⏸ Apply § 5a–5m (skip 5d / 5k if D-4 = B) and § 6a–6g (skip 6d.4 if D-4 = B).
- ⏸ § 6h manifest + § 6i CHANGELOG + § 6j promotion.
- ⏸ QA-L1…L6 (below) → Rule 10 review table → single commit (no push).
- ⏸ Delete the hand-kept fleet table from `docs/Plans/OPEN_TASKS.md` (local).

## Phase 4 — Validate

| # | Scenario | Phase | Status | Date | Evidence |
|---|---|---|---|---|---|
| QA-L1 | Tools (ruff / mypy / pytest 140) | 3 | ⏸ | | |
| QA-L2 ⚑ | Real fleet run | 3 | ⏸ | | |
| QA-L3 ⚑ | Unreachable carry-over (scratch vault) | 3 | ⏸ | | |
| QA-L4 ⚑ | Freshness gate a–e (scratch copy) | 3 | ⏸ | | |
| QA-L5 ⚑ | Write-path refresh (scratch target copy) | 3 | ⏸ | | |
| QA-L6 ⚑ | Machine neutrality (`HOME` elsewhere) | 3 | ⏸ | | |
| QA-L7 | Operator opens the CSV | post-ship | ⏸ | | |
| QA-L8 | Session open / close fleet lines | post-ship | ⏸ | | |

## Phase 5 — Operator gate

- ⏸ Push (no tag — engine-only, no Set Version change).
