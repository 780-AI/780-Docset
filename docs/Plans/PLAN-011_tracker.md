<!-- VERSION: 0.2 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Status: APPROVED (tracks PLAN-011 — Phase 3a next, in a NEW session) -->
<!--
CHANGE LOG
v0.2 — 2026-10-03 — Phase 2 approval recorded ("plan 011 is appvoved"); decisions + execution
deltas in plan § 9.1; Phase 3a gains the un-landed-handoff pre-write hold.
v0.1 — 2026-10-03 — Created with the plan draft (tracker required per § 15.7: Phase 3 spans three
commits across three sessions — vault / Equinex / vault — and Phase 4 is multi-scenario,
QA-F1…F8).
-->

# PLAN-011 tracker — fleet convergence (Equinex intake + adoption)

## Phase 0 — Audit

- ✅ 2026-10-03 — live fleet state: CS / 780-Automation / 780-VPN converged + registered at v2.5
  (780-VPN re-pointed to local `~/`, vault `fd41686`); Equinex the last unconverged project.
- ✅ 2026-10-03 — Equinex probed read-only: tip `cf25e70` (tag v7.41) = origin; one untracked
  brief; CLAUDE.md 3.14; own-line INDEX 1.11; lessons in `archive/LESSONS.md` 1.18; no SVA, no
  STANDARDS_LOG; governance scripts + Rule 14 project-data + gitignore already present.
- ✅ 2026-10-03 — lesson / rule / suite-novelty delta vs vault (plan § 3 Phase 0 findings).
- ✅ 2026-10-03 — adopt-mode spec gap found (adopt.md § 3 vs the `archive/LESSONS.md` replace
  item) → S2 / D-2.
- ✅ 2026-10-03 — § 5A registry entry proven via `load_registry` + `make_target` on a scratch copy.

## Phase 1 — Design

- ✅ 2026-10-03 — plan drafted (§§ 1–12) + this tracker.
- ✅ 2026-10-03 — Rule 13 pass RUN + recorded at the plan's foot (6 findings fixed in place).

## Phase 2 — Operator approval

- ✅ 2026-10-03 — operator: **"plan 011 is appvoved"** — D-1 Equinex only; D-2 = A; D-3 fleet grows
  later one by one; D-4 start immediately; D-5 E001 first (✅ v2.6 shipped `18b4b61` → this release
  = v2.7, C1 = L080); D-6 = A (§ 15.9). Record: plan § 9.1.

## Phase 3a — Intake + release (vault session; commit § 7.2)

- ⏸ Clock check vs external authority (R8) recorded.
- ⏸ Pre-write hold check: list targets holding an un-landed `docs/SYNC_HANDOFF.md` (plan § 9.1) —
  held unless PLAN-013's accumulation fix has shipped.
- ⏸ Delta re-verified at Equinex tip (§ 5D.1).
- ⏸ Rule 16 gate posted; operator confirmation quoted here (QA-F1).
- ⏸ Integration per § 5D.0 (Rule 12 drift) + § 5D.2–5D.7 + § 5C adopt.md fix.
- ⏸ QA-F2 grep gate; QA-F3 oracle dry-run (pre-commit).
- ⏸ Review table → commit → `sync --write` → QA-F4.

## Phase 3b — Equinex adoption (Equinex session; target commit § 7.3)

- ⏸ Pre-flight gates (§ 5E.1) incl. untracked brief resolved.
- ⏸ Mapping table posted (§ 5E.2) incl. per-entry archive classification.
- ⏸ § 4 dry-run list approved by the operator (quote here).
- ⏸ Apply + validate (QA-F5) → review table → adopt commit (no push).

## Phase 3c — Registration + discipline proof (vault session; commit § 7.4)

- ⏸ § 5A + § 5B applied; clock check (R8).
- ⏸ QA-F6 status / sync dry-run.
- ⏸ QA-F7 harvest → integrate write-back → harvest clean.
- ⏸ QA-F8 line-retirement checks.
- ⏸ Review table → closure commit (plan + tracker → 1.0/CLOSED).

## Phase 4 — Validate (scenario ledger)

| # | Scenario | Phase | Status | Date | Evidence |
|---|---|---|---|---|---|
| QA-F1 | Rule 16 gate record | 3a | ⏸ | | |
| QA-F2 | Domain-neutral zero-hit grep | 3a | ⏸ | | |
| QA-F3 ⚑ | Engine-as-oracle release dry-run | 3a | ⏸ | | |
| QA-F4 ⚑ | Release delivered + idempotent | 3a | ⏸ | | |
| QA-F5 ⚑ | Equinex adoption (diff == approved list, legacy byte-identical, runtime untouched) | 3b | ⏸ | | |
| QA-F6 ⚑ | Registration: status current, sync no-op | 3c | ⏸ | | |
| QA-F7 ⚑ | Log round-trip (harvest → write-back → clean) | 3c | ⏸ | | |
| QA-F8 | Own line retired | 3c | ⏸ | | |

Waiver register (Rule 15): _(empty — ⚑ scenarios may not be deferred without an explicit
operator waiver recorded here)_

## Phase 5 — Operator gate

- ⏸ Vault push + release tag (operator). Equinex push is the operator's own call.
