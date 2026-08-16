<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Status: CLOSED -->
<!--
CHANGE LOG
v1.0 — 2026-08-16 — Phase 3 implemented in a fresh session (single commit, 21-file ALLOWLIST; 3.22
adopt run as the final implementation step) + Phase 4 QA A–H + J flipped ✅ with evidence (I ⏸ at the
next session open). Tracker CLOSED with the plan.
v0.1 — 2026-08-16 — Sibling tracker created same-commit as the PLAN-010 DRAFT (big plan per § 15.7:
multi-scenario Phase-4 verify A–J; 21-file ALLOWLIST; spans sessions — Phase 3 is a fresh session).
-->

# PLAN-010 tracker — Upstream intake: EverOn v2.x → vault (Set v1.5)

Sibling of [`PLAN-010_everon_upstream_intake.md`](PLAN-010_everon_upstream_intake.md). Updated
same-commit as the work it tracks. Markers: ⏸ pending · 🔄 in-progress · ✅ done · ❌ blocked · ⏭ skipped.

---

## Phase 0 — Audit ✅ 2026-08-16

- ✅ EverOn.Equinex recon (read-only): origin lineage confirmed (own Set line v2.7, 15 rules /
  61 lessons; no SVA/STANDARDS_LOG → not a harvest job); all 12 lessons L050–L061 read in full;
  their Rule 14 + Rule 15 read in full; ripple commits `c0940f6 f688e79 ffd4145 f066fde ad0230a
  b9c8fe6` inspected; `d838097` = project-local (out of scope).
- ✅ Their `scripts/claude_project_data.sh` v0.1 read in full (124 lines) — port basis.
- ✅ Vault anchors verified; native L063-class find: § 3 heading "The 13 standing rules" stale in
  BOTH CLAUDE.md copies (+ § 13 bullets).
- ✅ Operator decisions settled: D1 = A1 (Rule 14 in-place upgrade + mechanism port + session-routine
  wiring); D2 = Equinex only (Capital-Signal → PLAN-011).

## Phase 1 — Design ✅ 2026-08-16

- ✅ Plan drafted (§§ 1–12): § 3 mapping table (their L050–L061/R14/R15 → vault L057–L067/R15/R14);
  § 5A eleven genericized lessons verbatim; § 5B L050 note; § 5C Rule-14 rewrite; § 5D Rule 15;
  § 5E full ported script (+ pre-v1.5 memory-symlink adopt branch); § 5F/§ 5G session-file edits;
  § 5H Set v1.5 cascade; § 7 21-file ALLOWLIST (plan + tracker rows included per L054); § 8 QA A–J.
- ✅ **Rule 13 senior-review pass** (2026-08-16, mechanical per L051 + recurrence #4): `bash -n`
  clean; fixture runs A/B/C ALL PASS (incl. the memory-symlink adopt branch + idempotency); QA-D
  grep run → 2 false-positives on bare `sweep` → pattern refined + re-run 0 hits; counts
  56+11=67 / 14+1=15 cross-checked; § 5F/§ 5G anchors reconciled against live files (all correct);
  `bootstrap_memory` blast-radius grep → ALLOWLIST complete, § 5H-3/4 strengthened to every-reference
  sweeps (3 + 5 sites). Findings recorded in the plan CHANGE LOG v0.1a. **Ready for Phase 2.**

## Phase 2 — Operator approval ✅ 2026-08-16

- ✅ **APPROVE D10.A** (2026-08-16) — full § 5 as specified; D1 = A1 + D2 = Equinex-only confirmed.

## Phase 3 — Implement ✅ 2026-08-16 (fresh session; single commit; ALLOWLIST = plan § 7)

Reconcile-first pass (§ 15.3 / L056) ran before any edit: all § 5 anchors, the 3+5 `bootstrap_memory`
site counts, and the § 3.1 row numbering verified against the live source — **no plan defects**.
Embedded blocks sanitized per L062 (straight quotes; § 5A prose mapped onto the live lesson format;
archive L050 note anchored on its project-instance tail, which differs from the template's).

- ✅ 3.1 LESSONS template — L057–L067 + L050 note + ToC [5A, 5B] — 2026-08-16
- ✅ 3.2 LESSONS archive — same [5A, 5B] — 2026-08-16
- ✅ 3.3 root CLAUDE.md — Rule 14 rewrite + Rule 15 + § 3/§ 13 counts + § 8.4 row [5C, 5D] — 2026-08-16
- ✅ 3.4 template CLAUDE.md — same (generic variances) [5C, 5D] — 2026-08-16
- ✅ 3.5 scripts/claude_project_data.sh NEW (extracted verbatim from § 5E) [5E] — 2026-08-16
- ✅ 3.6 scripts/bootstrap_memory.sh DELETED [5E] — 2026-08-16
- ✅ 3.7 project SESSION_OPENER — § 1.3/§ 1.5/§ 4 + rows 13/15/16 [5F] — 2026-08-16
- ✅ 3.8 template SESSION_OPENER — same, rows 14/16/17 [5F] — 2026-08-16
- ✅ 3.9 project SESSION_CLOSER — § 1.6 locality confirm [5G] — 2026-08-16
- ✅ 3.10 template SESSION_CLOSER — same [5G] — 2026-08-16
- ✅ 3.11 STANDARDS_INDEX → v1.5 (incl. § 4.1 "13 standing rules" → 15, swept per L060) [5H-1] — 2026-08-16
- ✅ 3.12 SET_VERSION_ADOPTED → adopt v1.5 [5H-2] — 2026-08-16
- ✅ 3.13 SETUP → v1.5 refs + Step 6.5 rewrite (3 bootstrap_memory sites swept) [5H-3] — 2026-08-16
- ✅ 3.14 NEW_PROJECT_BOOTSTRAP → v1.5 refs + Step 8 rewrite (5 sites swept; MACHINE_MIGRATION tree
  line added) [5H-4] — 2026-08-16
- ✅ 3.15 MEMORY_DURABILITY_ROLLOUT_PROMPT → project-data pattern [5H-5] — 2026-08-16
- ✅ 3.16 NEW_MACHINE_SETUP → catalog role + new verbs [5H-6] — 2026-08-16
- ✅ 3.17 documents_manifest — cells + script swap (slot 56 reused) + quick-index + self-row caught up
  2.13→2.15 (the v2.14 log claimed the bump but the cell never moved — L063 class) [5H-7] — 2026-08-16
- ✅ 3.18 folder_structure [5H-8] — 2026-08-16
- ✅ 3.19 CHANGELOG top entry (incl. mapping table) [5H-9] — 2026-08-16
- ✅ 3.20 PLAN-010 → 1.0/CLOSED · ✅ 3.21 this tracker → 1.0/CLOSED [5H-10] — 2026-08-16
- ✅ 3.22 operational: `claude_project_data.sh adopt` on this repo — run as the FINAL implementation
  step, immediately before the commit (§ 11 R1); .claude/README_memory.md updated same step — 2026-08-16

## Phase 4 — Validate ✅ 2026-08-16 (QA A–J, plan § 8; I pending at next open)

- ✅ A script syntax — `bash -n` exit 0 — 2026-08-16
- ✅ B fixture behaviors — scratchpad fixtures: un-adopted harness dir → `adopt` → OK; folder move →
  `link` → OK; pre-v1.5 memory-symlink layout → `adopt` absorbs both halves, idempotent re-adopt —
  2026-08-16
- ✅ C this-repo adopt (feature-ON, Rule-15 style) — `adopt` then `status` = OK; memory ≥ 11 files;
  transcripts present under `.claude/project-data/` — 2026-08-16
- ✅ D domain zero-hit — plan § 8 grep over the diff's added lines = 0 hits — 2026-08-16
- ✅ E stamp/count greps — § 3/§ 13 = 15 both CLAUDE.md; INDEX § 1/§ 2/§ 3 = 15/67; SVA counts;
  manifest header = self-row = 2.15 — 2026-08-16
- ✅ F LESSONS integrity — ToC ↔ `### L0NN` 1:1, 67 headings, newest-first, both files — 2026-08-16
- ✅ G governance — both Rule-2 scripts exit 0 — 2026-08-16
- ✅ H delivery-doc parity — no live v1.4 refs outside CHANGE LOGs in SETUP/NPB; rollout prompt
  retargeted — 2026-08-16
- ⏸ I opener § 1.5 live at next session open
- ✅ J manifest completeness — new script registered; bootstrap_memory row gone; folder_structure
  matches tree — 2026-08-16

## Phase 5 — Operator gate ⏸

- ⏸ 5.1 push + annotated tag `set-v1.5`
