<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Status: DRAFT — awaiting operator approval (plan § 9) -->
<!--
CHANGE LOG
v0.1 — 2026-10-12 — Created with the plan draft (tracker required per CLAUDE.md § 15.7: Phase 4 has a
multi-scenario list, QA-T1…T5).
-->

# PLAN-019 tracker — git transport fails fast (ssh timeouts + keepalives, a cap on every transport command)

## Phase 0 — Audit

- ✅ 2026-10-12 — § 15.9 intake: operator request in chat (no document) — "yes get it done as quickly as
  possible"; adopt / deviate vs the queued fix candidate recorded (plan § 2).
- ✅ 2026-10-12 — integration points cited `file:line` at `bf8669e` (plan § 3).
- ✅ 2026-10-12 — pre-tests with numbers: silent server / blackhole / mid-transfer stall hang with no
  options (≥ 40–75 s caps) and fail in 10.0 / 10.0 / 41.2 s with them; normal clone 3.0 s; the run cap
  returns on time; one orphaned ssh seen (→ R2).

## Phase 1 — Design

- ✅ 2026-10-12 — code drafted in a scratch export of HEAD: ruff clean, mypy --strict 0, pytest 172
  (163 + 9); positive control 8 failed / 20 passed on transport 0.3.
- ✅ 2026-10-12 — the engine's own `GitTarget`: GitHub 7.5 s OK; silent 10.1 s; stall 41.6 s with the
  operator's base command kept.
- ✅ 2026-10-12 — § 5 generated (16 blocks) + § 8 harness embedded; parsed back from the plan text →
  17 / 17 clean, byte-identical; control 1 corrupted FIND → exactly that block fails.
- ✅ 2026-10-12 — QA harness: draft 4 / 4 PASS; HEAD 1 PASS / 3 HANG (control).
- ✅ 2026-10-12 — Rule 13 senior-review pass (record at the foot of the plan; 5 fixes).

## Phase 2 — Operator approval

- ⏸ D19.A + D-1 / D-2 (plan § 9).

## Phase 3 — Implement (fresh session, one commit)

- ⏸ 3.0 — clock vs an external authority → `<P3-DATE>`; tree clean; HEAD == both remotes.
- ⏸ 3.1 — reconcile: re-extract the 16 § 5 blocks from the plan; every FIND once, in order; checker
  positive control.
- ⏸ 3.2 — apply § 5 (4 files) → QA-T1.
- ⏸ 3.3 — QA-T2 … T4 (live) → QA-T5 governance.
- ⏸ 3.4 — § 6 bookkeeping (manifest, CHANGELOG, plan + tracker → 1.0 CLOSED) → Rule 10 review →
  "go on commit?" → commit (§ 7, 8 files; no push).

## Phase 4 — Validate (QA scenarios, plan § 8)

- ⏸ QA-T1 — ruff / mypy / pytest 172; control 8 failed / 20 passed.
- ⏸ QA-T2 ⚑ — real fleet `status`: 780-estimator current over the new env.
- ⏸ QA-T3 ⚑ — silent git server: `TransportError` < 15 s; CLI `status` row `unknown`, exit 0, < 20 s.
- ⏸ QA-T4 ⚑ — mid-transfer stall dropped in 15–60 s with the operator's base kept.
- ⏸ QA-T5 — governance exit 0 / 0 (stdout pasted).

## Phase 5 — Operator gate

- ⏸ 5.1 — push to both remotes (`git push origin master` + `git push github master`; `ls-remote` both
  == HEAD); no tag (no Set Version change).
