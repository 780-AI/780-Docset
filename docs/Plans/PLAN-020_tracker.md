<!-- VERSION: 0.3 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Status: EXECUTING — Phase 3a committed; Phase 3b (delivery) next -->
<!--
CHANGE LOG
v0.3 — 2026-10-12 — Phase 3a ✅ (3a.0–3a.4) with evidence; QA-V1…V5, V7, V8 ✅.
v0.2 — 2026-10-12 — Phase 2 ✅: "go on commit; approve 020, all A" (plan § 9.1); D-3 = A waiver recorded under Phase 4.
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

- ✅ 2026-10-12 — "go on commit; approve 020, all A" — D20.A; D-1 = A, D-2 = A, D-3 = A, D-4 = A (plan § 9.1). Plan + tracker → 0.2.

## Phase 3a — Release commit (fresh session)

- ✅ 2026-10-12 3a.0 — clock 10:18:59 UTC vs gitlab.com `date:` 10:19:03 GMT → `<P3-DATE>` = 2026-10-12; tree
  clean; HEAD = `5e7a8b0` (the approval commit); `ls-remote` origin master = github master = `5e7a8b0`.
- ✅ 2026-10-12 3a.1 — reconcile with a parser written fresh this session: 70 markers → 70 blocks (65 replace,
  2 create, 3 harnesses); on a `git archive HEAD` export every FIND once in order, both creates new → CLEAN,
  21 files; corrupted-FIND control (5f.2) → exactly that block FAILs, nothing written. Zero plan defects.
- ✅ 2026-10-12 3a.2 — applied to the live tree: 21 files, `cmp` byte-identical to the export (21 / 0 differ),
  no `<P3-DATE>` left → QA-V2, QA-V3, QA-V4 ⚑ (below).
- ✅ 2026-10-12 3a.3 — § 6 rules 1–4: manifest 2.74 (19 cells by path, rows 98–99 → 0.3 EXECUTING, new rows
  100–101, quick-index); DECISION_LOG DL-010 … DL-014 (its creation change line names them too); CHANGELOG
  entry; plan + tracker 0.3 → QA-V5, QA-V7, QA-V8 (below).
- ✅ 2026-10-12 3a.4 — Rule 10 review table posted → "go on commit?" → commit 1 (§ 7.1, 25 files; no push) —
  this commit.

## Phase 3b — Delivery (same session, D-4)

- ⏸ 3b.1 — EverOn.Capital-Signal: idle evidence → "go" → `sync --project … --write` → re-run up-to-date.
- ⏸ 3b.2 — 780-VPN: same.
- ⏸ 3b.3 — EverOn.Equinex: same (high-stakes — only between its work sessions).
- ⏸ 3b.4 — 780-estimator (git): write = one engine commit pushed to their `main` → re-run up-to-date.
- ⏸ 3b.5 — 780-Automation: probe; unreachable → recorded, catch-up later.
- ⏸ 3b.6 — `status` → QA-V6; § 6 rule 5 → Rule 10 review → "go on commit?" → commit 2 (§ 7.2, 4 files).

## Phase 4 — Validate (QA scenarios, plan § 8)

- ✅ 2026-10-12 QA-V1 — 67 edit blocks CLEAN; corrupted-FIND control → 1 FAIL (5f.2); no `<P3-DATE>` left.
- ✅ 2026-10-12 QA-V2 — domain-neutral gate: no output (grep exit 1); planted-name control → exactly 1 hit.
- ✅ 2026-10-12 QA-V3 — harness 8b `SUMMARY CLEAN` (89 + 73 TOC links, fences in 21 files, 16 INDEX rows,
  89 lessons); control (broken anchor + stale INDEX cell + unclosed fence) → `3 FAILURE(S)`.
- ✅ 2026-10-12 QA-V4 ⚑ — harness 8c on copies of the 3 local projects + a fresh `--depth 1` clone of the git
  project (`515ea96`, 138 s): draft `pass=13 fail=0` (each 10-item delta; merged CLAUDE.md PO 4 / 4, TO 0,
  checklist 1; idempotent); baseline (HEAD export, `uptodate`) `pass=5 fail=0`; control (HEAD export, `delta`)
  `pass=5 fail=8` (2 per project — the Rule 13 record's "2 FAILs" was a smaller run; § 8 asks only "FAILs").
  Real projects untouched (CLAUDE.md times unchanged, no handoff).
- ✅ 2026-10-12 QA-V5 — governance exit 0 / 0 (stdout in the session chat); harness 8d `SUMMARY CLEAN` (98
  rows); its control — the § 5-applied tree before § 6 rule 1 → exactly 21 failures (19 cells + 2 unlisted).
- ⏸ QA-V6 ⚑ — live delivery: four projects `v2.8 v2.8 current`, each idempotent; 780-Automation recorded.
- ✅ 2026-10-12 QA-V7 — `docs/DECISION_LOG.md`: DL-001 … DL-014, each with a dated verbatim answer; § 9.1
  cites DL-010 … DL-014; harness 8b fence check passes on it.
- ✅ 2026-10-12 QA-V8 — the engine's `strip_template_only` on the template CLAUDE.md: body TEMPLATE-ONLY 0,
  template-file references 0, § 12 table 11 rows contiguous (control: raw template 1 reference);
  `bootstrap.md:45` / `adopt.md:75` name the deletion. **Rule 15 waiver (D-3 = A, operator 2026-10-12):** the
  real-run evidence is the next bootstrap / adopt / selftest report — record it here as a post-close note.

## Phase 5 — Operator gate

- ⏸ 5.1 — push both remotes + annotated tag `set-v2.8` on commit 1; `ls-remote` both: master == HEAD,
  tag == commit 1.
