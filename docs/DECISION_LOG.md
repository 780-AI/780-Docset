<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Source: docs/standards/DECISION_LOG.md (template) v0.1. Project-local instance for Standard DocSet. -->
<!--
CHANGE LOG
v1.0 — 2026-10-12 — Created (PLAN-020, Standard Set Version v2.8): the vault's decision log; seeded with the decisions of 2026-10-12 (DL-001 … DL-009, verbatim) and the PLAN-020 Phase 2 answers (DL-010 … DL-014). Decisions before 2026-10-12 live in each plan's § 9.1.
-->

# DECISION_LOG.md — Operator decisions

**What this file is:** the single record of every decision the operator makes for this project —
scope, design options, approvals, intake-gate answers, waivers — written once, in plain words,
with the operator's exact reply. Plans, CHANGELOG entries and memory cite an entry by its id
(`DL-NNN`) instead of restating the decision. Binding per `CLAUDE.md` § 10 "Record every operator
decision".

## Rules

1. **One entry per decision**, added at the top (newest first). Ids are permanent and never reused.
2. **The question as it was asked** — in plain words, with the options and what each one does.
3. **The answer is the operator's verbatim reply**, in quotes, with its date — never paraphrased.
   A reply that answers several questions is quoted in each entry it answers.
4. **Applied in** names where the decision was carried out (plan section, commit, file); filled in
   when known, completed later by an appended line.
5. **Entries are never edited or deleted.** A changed decision is a NEW entry that says
   "Supersedes DL-NNN"; the old entry gets one appended line, "Superseded by DL-MMM".
6. **What counts:** any choice between options the operator was asked to make. Routine "go on
   commit?" / "push" confirmations are not entries — the commit and the push record them.
7. The file's VERSION bumps once per commit that adds entries.

## Entry format

```markdown
### DL-NNN — YYYY-MM-DD — <short title>

- **Question:** <plain words — what was asked>
- **Options:** A — <what it does> / B — <what it does> (recommended: <X>)
- **Answer:** "<the operator's verbatim reply>" — YYYY-MM-DD
- **Decision:** <one line: what was decided>
- **Applied in:** <plan § / commit / file>
```

---

## Decisions (newest first)

### DL-014 — 2026-10-12 — PLAN-020 D-4: deliver v2.8 to the projects in the same session

- **Question:** After the release commit, deliver v2.8 to the reachable projects in the same session —
  or release only and deliver later?
- **Options:** A — yes: for each reachable project the idle evidence is shown, the operator says "go",
  the write runs and is re-checked; 780-Automation catches up when its host answers / B — release
  only; deliver later (the plan stays open until then) (recommended: A)
- **Answer:** "go on commit; approve 020, all A" — 2026-10-12
- **Decision:** A — delivery in the Phase 3 session (QA-V6), each project after its idle evidence and a "go".
- **Applied in:** PLAN-020 § 9.1, Phase 3b.

### DL-013 — 2026-10-12 — PLAN-020 D-3: proving the skill change in a real run (Rule 15)

- **Question:** The new skill lines run only when someone bootstraps, adopts or self-tests a project.
  Waive the real-run proof until that next real use, or make it ship-gating now?
- **Options:** A — waive until the next real use (its report is the evidence); the mechanical check
  QA-V8 still runs / B — ship-gating: run the selftest launcher on this Mac before the plan closes
  (recommended: A)
- **Answer:** "go on commit; approve 020, all A" — 2026-10-12
- **Decision:** A — Rule 15 waiver for the skill change until its next real use; recorded in the tracker.
- **Applied in:** PLAN-020 § 9.1; `docs/Plans/PLAN-020_tracker.md` Phase 4 (QA-V8).

### DL-012 — 2026-10-12 — PLAN-020 D-2: fix the skill now so the curator-only note never reaches a new project

- **Question:** The § 12 note about the Project Instructions template becomes a hidden-from-projects
  note. Sync strips such notes, but the skill's bootstrap / adopt modes don't. Include two small skill
  edits in this plan, or leave them for the separate skill change?
- **Options:** A — include the two skill edits (5m, 5n) / B — leave it; a project set up in between shows
  the note until its first sync (harmless, self-healing) (recommended: A)
- **Answer:** "go on commit; approve 020, all A" — 2026-10-12
- **Decision:** A — the two skill lines ship in PLAN-020.
- **Applied in:** PLAN-020 § 5m, § 5n (`skill/modes/bootstrap.md` 0.4, `skill/modes/adopt.md` 0.5).

### DL-011 — 2026-10-12 — PLAN-020 D-1: where the vault's decision-log rule lives

- **Question:** The vault's sessions need a rule that says "record every decision in
  `docs/DECISION_LOG.md`". Where should it live?
- **Options:** A — a short sub-section in CLAUDE.md § 10 (no new rule number, nothing renumbers when
  projects get the same rule in PLAN-021) / B — a new standing Rule 17 in the vault only (more
  prominent; the vault's rule numbers drift further from the template's) (recommended: A)
- **Answer:** "go on commit; approve 020, all A" — 2026-10-12
- **Decision:** A — `CLAUDE.md` § 10 "Record every operator decision"; no rule number.
- **Applied in:** PLAN-020 § 5o (`CLAUDE.md` 1.10).

### DL-010 — 2026-10-12 — PLAN-020 approval

- **Question:** Approve PLAN-020 (Standard Set Version v2.8) as written, with its draft commit?
- **Options:** A — approve as written / B — revise first (recommended: A)
- **Answer:** "go on commit; approve 020, all A" — 2026-10-12
- **Decision:** D20.A approved.
- **Applied in:** `5e7a8b0` (approval); PLAN-020 Phase 3.

### DL-009 — 2026-10-12 — v2.8: the remaining recommendations (lessons, notes, template fixes)

- **Question:** Are the recommendations for the seven new lessons (B), the notes (C — C5 deferred,
  C6 rejected) and the template fixes (D) fine as listed?
- **Options:** yes / name the items to change (recommended: yes)
- **Answer:** "Q5 A, Q6 yes" — 2026-10-12
- **Decision:** B1–B7 → L082–L088; C1–C4 integrated, C5 deferred, C6 rejected; D1–D5 fixed.
- **Applied in:** PLAN-020 (Standard Set Version v2.8).

### DL-008 — 2026-10-12 — The decision log: how far it goes

- **Question:** A decision log — one file recording every decision once, with the operator's exact
  words. A brand-new file cannot reach existing projects without an engine change. How far should
  it go?
- **Options:** A — two steps: the vault starts its own log in v2.8 and the projects' template is
  written; PLAN-021 delivers it to every project with the rule that tells their sessions to use it /
  B — vault only, never in projects / C — everything in v2.8, pulling an engine change in
  (recommended: A)
- **Answer:** "Q5 A, Q6 yes" — 2026-10-12
- **Decision:** A — vault log + template in v2.8; delivery to projects in PLAN-021.
- **Applied in:** PLAN-020 (this file, `docs/standards/DECISION_LOG.md`, `CLAUDE.md` § 10); PLAN-021 (queued).

### DL-007 — 2026-10-12 — Plain-language decisions + a decision log

- **Question:** The "explain decisions in plain language with a small table and a one-line reply
  format" pattern has 12 data points. Save it as a feedback memory now?
- **Options:** yes / no (recommended: yes)
- **Answer:** "Q4. yes this is very important we should have descision log" — 2026-10-12
- **Decision:** feedback memory saved (marked very important); a decision log requested (→ DL-008).
- **Applied in:** memory `feedback_plain_language_decisions.md`; DL-008.

### DL-006 — 2026-10-12 — v2.8: the four dangling Project Instructions references

- **Question:** Four places in the standards point at `PROJECT_INSTRUCTIONS_TEMPLATE.md`, a file
  projects never receive. Take the pointers out of the projects' copies, or point them at the
  vault's copy?
- **Options:** A — remove them from the projects' copies (the vault keeps a curator-only note) /
  B — point all four at the vault's location (recommended: A)
- **Answer:** "Q3. eplain in simple words" (first reply), then "Q3 A" — 2026-10-12
- **Decision:** A.
- **Applied in:** PLAN-020 § 5b.6, 5e, 5f.3, 5g (Standard Set Version v2.8).

### DL-005 — 2026-10-12 — v2.8 Rule 16 intake gate

- **Question:** Confirm for integration: A1 (780-estimator #4 → an L080 data point), A2 (#5 → a new
  lesson), A3 (#8 → a Rule 13 checklist line), A5 (Capital-Signal E002's remainder → an opener
  § 1.5 line + a lesson); A4 (#6, ALLOWLIST-count automation) deferred to vault tooling?
- **Options:** yes / no / name the items to change (recommended: yes)
- **Answer:** "Q2. yes" — 2026-10-12
- **Decision:** A1, A2, A3, A5 integrated; A4 deferred; nothing rejected.
- **Applied in:** PLAN-020 (L080 data point, L089, § 15.8 checklist, SESSION_OPENER § 1.5, L087).

### DL-004 — 2026-10-12 — v2.8 scope

- **Question:** Should v2.8 be documents only (lessons, notes, template fixes), with the locality-tool
  delivery and the skill / Windows fixes as their own changes — or one bigger release including
  the engine change?
- **Options:** A — documents only; the rest separately / B — everything in one v2.8 (recommended: A)
- **Answer:** "Q1 A, but record the rest for planning and getting them done right away" — 2026-10-12
- **Decision:** A; the rest queued to start right after v2.8 (PLAN-021, the skill Minor, vault tooling).
- **Applied in:** PLAN-020; OPEN_TASKS "Right after v2.8".

### DL-003 — 2026-10-12 — PLAN-019 approval

- **Question:** Approve PLAN-019 (the git transport fails fast) with the two design answers, and its
  draft + approval commits?
- **Options:** approve (D19.A) / revise (recommended: approve)
- **Answer:** "D1. A , D2. A", then "go" — 2026-10-12
- **Decision:** D19.A approved.
- **Applied in:** `63e6c1f` (approval); `9366b7a` (Phase 3, plan CLOSED).

### DL-002 — 2026-10-12 — PLAN-019 D-2: a cap on every transport command

- **Question:** Should every git / rsync command stop after a time limit, to catch a slow-but-alive
  transfer the ssh options cannot see?
- **Options:** A — 300 s on every command / B — no cap, ssh options only (recommended: A)
- **Answer:** "D1. A , D2. A" — 2026-10-12
- **Decision:** A — 300 s.
- **Applied in:** `src/standard_document_updater/transport.py` 0.4 (`9366b7a`).

### DL-001 — 2026-10-12 — PLAN-019 D-1: whose ssh command git runs

- **Question:** When the engine adds its fail-fast ssh options, should it keep the operator's own ssh
  command (`GIT_SSH_COMMAND`, else `core.sshCommand`) and append to it — or always use plain `ssh`?
- **Options:** A — keep the operator's own and append; a legacy `GIT_SSH` program left alone / B —
  always `ssh` + the options (overrides an operator setting a Windows machine needs) (recommended: A)
- **Answer:** "D1. A , D2. A" — 2026-10-12
- **Decision:** A.
- **Applied in:** `src/standard_document_updater/transport.py` 0.4 (`9366b7a`).
