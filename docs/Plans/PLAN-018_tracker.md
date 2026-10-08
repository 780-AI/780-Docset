<!-- VERSION: 0.3 -->
<!-- Last Updated: 2026-10-08 -->
<!-- Status: EXECUTING — Phase 3 shipped 2026-10-08; push, then QA-S4…S6 (S6 on Windows) -->
<!--
CHANGE LOG
v0.3 — 2026-10-08 — Phase 3 ✅ (3.0–3.3; reconcile 11 / 11, zero plan defects); QA-S1…S3 ✅ with evidence.
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

- ✅ 2026-10-08 3.0 Pre-checks: local `date -u` 14:14:06 vs `Date:` gitlab.com 14:14:07 / github.com 14:14:05
  → `<P3-DATE>` = 2026-10-08; vault tree clean; HEAD `977a1ca` == `ls-remote` origin == github; the six
  files unchanged since the audit commit (`git diff 9b1c49e HEAD` on them empty).
- ✅ 2026-10-08 3.1 Reconcile pass — a parser written fresh in this session: 11 blocks extracted (5a 5b
  5c.1–3 5d.1–3 5e 5f.1–2); pre-blobs `b8e3757…` (SKILL.md) + `56d37dc…` (README.md) matched;
  `selftest.md` absent; every FIND matched exactly once, in order; **zero plan defects**. Positive
  control (FIND 5c.2 corrupted) → exactly 1 FAIL. Applied to an export of `9b1c49e` → the same six blobs.
- ✅ 2026-10-08 3.2 Apply § 5 → the six files written byte-for-byte (blobs in QA-S3); QA-S1 ✅, QA-S2 ✅.
- ✅ 2026-10-08 3.3 § 6c bookkeeping (manifest 2.67: cells 6 / 76 / 77 / 78, rows 93–94 → 0.3, new row 95,
  Delivery quick-index; CHANGELOG with QA scenarios; plan + tracker 0.3) → QA-S3 ✅ → Rule 10 review table
  in chat → operator "go on commit?" → commit (§ 7.3, 10 files; no push) → OPEN_TASKS (§ 6f).

## Phase 4 — Validate

| # | Scenario | Phase | Status | Date | Evidence |
|---|---|---|---|---|---|
| QA-S1 | Domain-neutral gate over `skill/` | 3.2 | ✅ | 2026-10-08 | the § 8 grep over `skill/` → no output, exit 1; control (same pattern on `config/projects.toml`) → 29 lines, exit 0 |
| QA-S2 ⚑ | Step 0 matrix 5 / 5 (control red on 0.2) | 3.2 | ✅ | 2026-10-08 | § 8.1 script extracted verbatim from the plan (46 lines), vault = a local clone at `977a1ca`. 0.3 Step 0 (13 lines): decoy git calls 0 / 0 / 0 / 0 / 0; cases 1–2 exit 0 `Delivering Standard Set Version v2.7 from vault commit 977a1ca (vault: …)`; cases 3–4 exit 1 `STOP: no vault folder named and no skill link …`, case 5 exit 1 `STOP: '…' is not a Standard DocSet vault` — 0 git calls in 3–5. Control, 0.2 Step 0 (`git show HEAD:skill/SKILL.md`, 7 lines): decoy calls 3 / 0 / 3 / 2 / 3 (`rev-parse`, `pull --ff-only`, `rev-parse`; case 4 via `git -C ""`), cases 1 / 3 / 5 print `Set Version  from vault commit <decoy sha>` — identical to § 3 P4 |
| QA-S3 | Governance, cells == headers, fences, blobs | 3.3 | ✅ | 2026-10-08 | governance exit 0 / 0 (stdout in the Phase 3 chat); cells 2 / 5 / 6 / 76 / 77 / 78 / 93 / 94 / 95 == their headers (Python check — it read row 94 as a mismatch before this tracker's bump: the checker sees a stale cell); fence lines even in all 10 files; blobs after apply: SKILL.md `69541b8`, selftest.md `e00e308`, bootstrap.md `a6882e9`, adopt.md `5abf898`, README.md `4ca4623`, folder_structure.md `b8551f8` (== § 5 applied to `9b1c49e`) |
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
