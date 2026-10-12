<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Status: DRAFT — awaiting Phase 2 approval -->
<!--
CHANGE LOG
v0.1 — 2026-10-12 — Created with the plan draft (tracker required per CLAUDE.md § 15.7: Phase 3 lands as
two commits plus project writes; Phase 4 has a multi-scenario list, QA-V1…V8).
-->

# PLAN-020 tracker — Standard Set Version v2.8

## Phase 0 — Audit

- ✅ 2026-10-12 — § 15.9 intake: operator "start 2.8" (no document); the v2.8 inventory posted in chat —
  every recorded candidate with source + recommendation, the adopter items as the Rule 16 list.
- ✅ 2026-10-12 — operator answers, verbatim → `docs/DECISION_LOG.md` DL-004 … DL-009 (plan § 2).
- ✅ 2026-10-12 — integration points cited `file:line` at `9366b7a` (plan § 3); four audit findings beyond
  the inventory (stamp drift ×2, the skill's TEMPLATE-ONLY gap → D-2, the historical lesson references).

## Phase 1 — Design

- ✅ 2026-10-12 — § 5 drafted as plan blocks (67) and applied to a scratch export of HEAD: CLEAN, 21 files.
- ✅ 2026-10-12 — QA harnesses built and controlled: 8b structure (CLEAN; control 3 FAILs), 8c oracle
  (13 / 13; baseline 5 / 5; control FAILs), 8d manifest cells (HEAD 94 rows CLEAN; draft tree 21 FAILs =
  the § 6 work list).
- ✅ 2026-10-12 — Rule 13 senior-review pass on the extracted text (record at the foot of the plan; 3 fixes).

## Phase 2 — Operator approval

- ⏸ D20 + D-1 … D-4 (plan § 9) → § 9.1 decision record → plan + tracker 0.2.

## Phase 3a — Release commit (fresh session)

- ⏸ 3a.0 — clock vs an external authority → `<P3-DATE>`; tree clean; HEAD contains the approval commit;
  push state vs both remotes recorded.
- ⏸ 3a.1 — reconcile: re-extract the 67 § 5 blocks + harnesses 8b / 8c / 8d from the plan; every FIND once,
  in order; creates new; corrupted-FIND control → QA-V1.
- ⏸ 3a.2 — apply § 5 → QA-V2 (domain-neutral + control) → QA-V3 (harness 8b + control) → QA-V4 ⚑
  (harness 8c on fresh copies: baseline export `uptodate`, draft `delta`, control).
- ⏸ 3a.3 — § 6 rules 1–4 (manifest by path, DECISION_LOG Phase 2 entries, CHANGELOG, plan + tracker 0.3)
  → QA-V5 (governance pasted + harness 8d) → QA-V7 → QA-V8.
- ⏸ 3a.4 — Rule 10 review table → "go on commit?" → commit 1 (§ 7.1, 25 files; no push).

## Phase 3b — Delivery (same session, D-4)

- ⏸ 3b.1 — EverOn.Capital-Signal: idle evidence → "go" → `sync --project … --write` → re-run up-to-date.
- ⏸ 3b.2 — 780-VPN: same.
- ⏸ 3b.3 — EverOn.Equinex: same (high-stakes — only between its work sessions).
- ⏸ 3b.4 — 780-estimator (git): write = one engine commit pushed to their `main` → re-run up-to-date.
- ⏸ 3b.5 — 780-Automation: probe; unreachable → recorded, catch-up later.
- ⏸ 3b.6 — `status` → QA-V6; § 6 rule 5 → Rule 10 review → "go on commit?" → commit 2 (§ 7.2, 4 files).

## Phase 4 — Validate (QA scenarios, plan § 8)

- ⏸ QA-V1 — apply: 67 blocks CLEAN; corrupted-FIND control; no `<P3-DATE>` left.
- ⏸ QA-V2 — domain-neutral gate: no output; planted-name control → 1 hit.
- ⏸ QA-V3 — structure (8b): CLEAN; control → 3 FAILs.
- ⏸ QA-V4 ⚑ — oracle on copies (8c): `pass=13 fail=0`; baseline `pass=5 fail=0`; control FAILs.
- ⏸ QA-V5 — governance 0 / 0 (pasted) + manifest cells (8d) CLEAN.
- ⏸ QA-V6 ⚑ — live delivery: four projects `v2.8 v2.8 current`, each idempotent; 780-Automation recorded.
- ⏸ QA-V7 — decision log: DL-001 … DL-009 + the Phase 2 entries, verbatim, cited from § 9.1.
- ⏸ QA-V8 — skill change: mechanical strip check; real-run evidence per D-3.

## Phase 5 — Operator gate

- ⏸ 5.1 — push both remotes + annotated tag `set-v2.8` on commit 1; `ls-remote` both: master == HEAD,
  tag == commit 1.
