<!-- VERSION: 0.2 -->
<!-- Last Updated: 2026-10-08 -->
<!-- Status: APPROVED — Phase 3 next, in a fresh session -->
<!--
CHANGE LOG
v0.2 — 2026-10-08 — Phase 2 ✅: "go on commit; plan 018 approved, all A" (plan § 9.1); waiver register:
D-1 = A (adopt mode's feature-ON evidence until its next real use).
v0.1 — 2026-10-08 — Created with the plan draft (tracker required per CLAUDE.md § 15.7: Phase 4 has a
multi-scenario list, QA-S1…S6, and the feature-ON half runs after the push and on a Windows machine —
the plan spans sessions).
-->

# PLAN-018 tracker — one-prompt delivery (named-vault Step 0, selftest mode, handoff report)

## Phase 0 — Audit

- ✅ 2026-10-08 — § 15.9 intake: operator request in chat (no document); "c, a, a"; adopt / deviate per
  item recorded (plan § 2).
- ✅ 2026-10-08 — integration points cited `file:line` at `9b1c49e` (plan § 3).
- ✅ 2026-10-08 — P1 GitHub clone (18 s, 3.5 MB, HEAD == both remotes, nothing private published); P2
  named-vault Step 0; P3 installer in a sandbox HOME.
- ✅ 2026-10-08 — P4 Step 0 matrix: draft 5 / 5; the current Step 0 pulls the current folder's repo in
  both no-link cases (control).

## Phase 1 — Design

- ✅ 2026-10-08 — the six files drafted in a scratch overlay of the GitHub clone; domain-neutral grep over
  `skill/` clean; fences balanced.
- ✅ 2026-10-08 — P5: § 5 generated from the overlay (11 blocks), parsed back from the plan text, applied
  to a fresh copy of `9b1c49e` → 6 / 6 files byte-identical; control 1 FAIL.
- ✅ 2026-10-08 — P6: a fresh agent given only launcher 1 ran the self-test on the draft — 17 / 0 / 1, the
  machine identical before and after (curator snapshot); 12 notes → fixes + queued gaps (plan § 2, Rule 13).
- ✅ 2026-10-08 — P6b: a second fresh agent on the final draft — 17 / 0 / 1 again, every fix followed.
- ✅ 2026-10-08 — Rule 13 senior-review pass (record at the foot of the plan).

## Phase 2 — Operator approval

- ✅ 2026-10-08 — "go on commit; plan 018 approved, all A" — D18.A; D-1…D-4 = A (plan § 9.1). Plan +
  tracker → 0.2.

## Phase 3 — Implement (fresh session; one vault commit)

- ⏸ 3.0 Pre-checks: clock vs an external authority → `<P3-DATE>`; vault tree clean; HEAD == both remotes.
- ⏸ 3.1 Reconcile pass: § 5 re-extracted (11 blocks); pre-blobs `b8e3757…` (SKILL.md) + `56d37dc…`
  (README.md); `selftest.md` absent; every FIND matched once, in order; checker positive control.
- ⏸ 3.2 Apply § 5 → QA-S1, QA-S2.
- ⏸ 3.3 § 6c bookkeeping → QA-S3 → Rule 10 review table → operator "go on commit?" → commit (§ 7.3; no
  push) → OPEN_TASKS (§ 6f).

## Phase 4 — Validate

| # | Scenario | Phase | Status | Date | Evidence |
|---|---|---|---|---|---|
| QA-S1 | Domain-neutral gate over `skill/` | 3.2 | ⏸ | | |
| QA-S2 ⚑ | Step 0 matrix 5 / 5 (control red on 0.2) | 3.2 | ⏸ | | |
| QA-S3 | Governance, cells == headers, fences, blobs | 3.3 | ⏸ | | |
| QA-S4 ⚑ | Real self-test from the GitHub page (operator, this Mac) | post-push | ⏸ | | |
| QA-S5 ⚑ | Project setup with launcher 2 (operator, this Mac) | post-push | ⏸ | | |
| QA-S6 ⚑ | Windows self-test (D-2) | post-push | ⏸ | | |

**Waiver register (Rule 15):**

| Date | Scope | Waiver | By |
|---|---|---|---|
| 2026-10-08 | adopt mode's § 5 Windows note + § 8 handoff report (plan § 5d) | feature-ON evidence deferred to adopt mode's next real use — its handoff report is the evidence (D-1 = A) | operator ("plan 018 approved, all A") |

## Phase 5 — Operator gate

- ⏸ Push the Phase 3 commit to BOTH remotes + `ls-remote` both (no tag) — BEFORE QA-S4…S6 (§ 6d).
- ⏸ Closure commit (§ 7.4) after QA-S4…S6 (or the recorded waivers).
