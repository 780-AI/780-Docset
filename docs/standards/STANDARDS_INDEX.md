<!-- VERSION: 1.9 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Source: ~/everon-standards/STANDARDS_INDEX.md -->
<!--
CHANGE LOG
v1.8 — 2026-05-23 — **Standard Set Version bumped v2.4 → v2.5 (Major — new binding file `SESSION_CLOSER.md` adopted; adopter migration required).** NEW binding file `docs/standards/SESSION_CLOSER.md` v1.0 (template) + project-local `docs/SESSION_CLOSER.md` v1.0 introduced same commit. NEW Rule 12 "Session wrap-up routine on operator command is MANDATORY" added to CLAUDE.md § 3 (Rules 1–11 unchanged); same-commit drift fix § 3 heading "11 standing rules" → "12 standing rules" + § 13 sources-of-truth bullet. NEW L048 in LESSONS.md ("Session wrap-up routine as forcing function against detail loss across session boundaries") above L047. Symmetric counterpart to v2.0/v2.1 SESSION_OPENER / Rule 9 / L043. Per-file bumps: CLAUDE.md 3.4 → 3.5; LESSONS.md 1.10 → 1.11; README.md 1.8 → 1.9; HOW_TO_USE.md 1.5 → 1.6; STANDARDS_INDEX.md (this file) 1.7 → 1.8. NEW entries for SESSION_CLOSER template (v1.0) + project-local (v1.0). § 1 adopter contract: 47 lessons → 48 lessons; 11 standing rules → 12 standing rules; 10 binding files → 11 binding files. § 2 binding-files table extends to 11 rows. § 3 per-file table refreshed. § 6 history: new v2.5 entry at top with adopter-migration steps.
v1.7 — 2026-05-22 — **Standard Set Version bumped v2.3 → v2.4** (Minor — additive, no adopter migration required structurally). NEW Rule 11 "QA / smoke-test scenario for every change" in CLAUDE.md § 3 (Rules 1–10 unchanged); same-commit drift fix § 3 heading "10 standing rules" → "11 standing rules" + § 13 sources-of-truth bullet. NEW L047 in LESSONS.md ("QA scenarios must be coupled to changes at change-time, not validation-time") above L046. SESSION_OPENER.md template § 3.1 gains NEW row 13 (behavior-affecting change without paired scenario). Per-file bumps: CLAUDE.md 3.3 → 3.4; LESSONS.md 1.9 → 1.10; SESSION_OPENER template 1.3 → 1.4; README.md 1.7 → 1.8; HOW_TO_USE.md 1.4 → 1.5. § 1 adopter contract: 46 lessons → 47 lessons; 10 standing rules → 11 standing rules. § 3 per-file table refreshed. § 6 history: new v2.4 entry at top.
v1.6 — 2026-05-22 — **Standard Set Version bumped v2.2 → v2.3** (Minor — additive, no adopter migration required). Cross-project backport from EverOn.Capital-Signal commit `5ee36ed`: 2 new lessons (L045 + L046) from EverOn.Equinex 2026-05-22 PLAN-004 close-out session. CLAUDE.md § 15.7 (Tracker requirement for plans) — already in Equinex's repo-root CLAUDE.md from earlier same-day commits `1bfd62d` + `6ec4469`, so this set bump promotes the existing rule into canonical standards form without further CLAUDE.md text change. SESSION_OPENER.md template § 1.3 extended with priority-ordered tracker-source list; § 3.1 NEW rows 11 + 12. MEMORY_PROTOCOL.md § 1 Category B gains permission-policy example + memory↔settings.json mirror paragraph. Per-file bumps: LESSONS.md 1.8 → 1.9 (L045 + L046 added); SESSION_OPENER template 1.2 → 1.3; MEMORY_PROTOCOL 1.3 → 1.4; README 1.6 → 1.7; HOW_TO_USE 1.3 → 1.4; STANDARDS_INDEX (this file) 1.5 → 1.6. § 1 adopter contract: 44 → 46 lessons. § 3 per-file table refreshed. § 6 history: new v2.3 entry at top.
v1.5 — 2026-05-22 — **Standard Set Version bumped v2.1 → v2.2** (Minor — additive, no adopter migration required). Cross-project backport from EverOn.Capital-Signal commit `717529a`: NEW Rule 10 "Code review before commit is MANDATORY" added to CLAUDE.md § 3 (Rules 1–9 unchanged); same-commit drift fix § 3 heading "9 standing rules" → "10 standing rules"; § 13 sources-of-truth bullet update. NEW L044 in LESSONS.md ("Session-scoped checklists don't enforce per-commit discipline; embed the rule in the procedure") above L043. Per-file bumps: CLAUDE.md 3.2 → 3.3; LESSONS.md 1.7 → 1.8; SESSION_OPENER template 1.1 → 1.2 (§ 3.1 row 3 update to cite Rule 10 + L044); README.md 1.5 → 1.6; HOW_TO_USE.md 1.2 → 1.3. § 1 adopter contract: 43 lessons → 44 lessons; 9 standing rules → 10 standing rules. § 3 per-file table refreshed. § 6 history: new v2.2 entry at top.
v1.4 — 2026-05-22 — Set Version v2.1 fix-forward: bring stale body-text references current across the standards suite. Standard Set Version unchanged at v2.1 (no Set-Version bump — clarification-only edits per § 5.1; no new lessons, no new files, no structural changes). § 3 per-file table refreshed to reflect the fix-forward bumps: PROJECT_STANDARDS.md 1.3 → 1.4; PROMPT_STANDARDS.md 1.4 → 1.5; PROJECT_INSTRUCTIONS_TEMPLATE.md 1.3 → 1.4; MEMORY_PROTOCOL.md 1.2 → 1.3; README.md 1.4 → 1.5; STANDARDS_INDEX.md (this file) 1.3 → 1.4; NEW_PROJECT_BOOTSTRAP.md 1.0 → 1.1; HOW_TO_USE.md 1.1 → 1.2. § 4 "What you get" body-prose "the 8 standing rules" → "the 9 standing rules". § 6 history NOT modified — append-only.
v1.3 — 2026-05-22 — **Standard Set Version bumped v1.1 → v2.1** (Major — new binding file `SESSION_OPENER.md` adopted; adopter migration: instantiate `docs/SESSION_OPENER.md` from the template + append Rule 9 to repo-root `CLAUDE.md`). Cross-project merge backporting EverOn.Capital-Signal's v2.0 (SESSION_OPENER + CLAUDE.md Rule 9) + v2.1 (L036–L042 lessons EverOn already had from Equinex). Net effect for Equinex: receives SESSION_OPENER.md + Rule 9 + L043 from EverOn's v2.1; Equinex's existing L036–L042 + topical-file additions stay intact. Per-file changes: NEW `SESSION_OPENER.md` v1.1 (template) + project-local `docs/SESSION_OPENER.md` v1.0 (Equinex-customized). `CLAUDE.md` 2.0 → 3.0 (Rule 9 appended; Rules 1–8 unchanged). `LESSONS.md` 1.6 → 1.7 (L043 added; project-of-origin reads "EverOn.Capital-Signal"). `README.md` + `HOW_TO_USE.md` bumped to reflect 10 binding + 4 meta and SESSION_OPENER pre-flight as the FIRST Day-One action. § 2 binding-files table extends from 9 to 10 rows. § 3 per-file table refreshed with new SESSION_OPENER row + bumped CLAUDE.md / LESSONS.md / README.md / HOW_TO_USE.md cells. § 6 history extended with v2.1 entry at top.
v1.2 — 2026-05-22 — **Standard Set Version bumped v1.0 → v1.1** (Minor — additive, no adopter migration required). 7 new lessons (L036–L042) added to LESSONS.md from EverOn.Equinex PLAN-001..PLAN-004 multi-plan sequence 2026-05-19..05-22. CLAUDE.md template: new § 15 plan workflow for vital changes (codifies L042; Phases 0–5; Phase 2 operator-approval gate; Phase 3 in a fresh agent session). ENGINEERING_STANDARDS.md template: new § 1.8 time-window parsing pitfalls (L037); new § 1.9 refactor blast-radius (L039); new § 4.6 fail-safe defaults for external-data sources that may be unavailable (L040); new § 4.7 safety tripwire for pattern-match drift (L041). PROMPT_STANDARDS.md template: § 3.2 ALLOWLIST block refined with bullet-vs-prose count discipline (L038). PROJECT_STANDARDS.md template: § 4 artifact sync trigger table extended with closed-risk annotation row; new § 4.3 closed-risk annotation discipline (L036). § 6 history block updated with v1.1 entry.
v1.1 — 2026-05-16 — Register new meta file HOW_TO_USE.md v1.0 in § 2 Tier 2 Meta files table and § 3 per-file version table. § 1 Adopter contract line updated ("3 meta files" → "4 meta files"). § 3 total file count updated (12 → 13; "9 binding + 3 meta" → "9 binding + 4 meta"). Set Version stays at v1.0 — additive Minor change to the meta tier per § 5.1; no binding-file count change; no adopter migration required.
v1.0 — 2026-05-16 — Initial release. Versioned manifest of the standards set. Captures Standard Set Version v1.0 baseline (the suite refreshed with EverOn.Capital-Signal Phase 4–7 + EA-test-soak lessons). Per-file version table; Set-Version-bump policy; how-to-apply guide; Set-Version history block.
-->

# STANDARDS_INDEX.md — Versioned Set Manifest

**Purpose:** This file is the canonical record of the Standard Set Version and the per-file versions inside it. It exists so adopters can name what version of the suite they adopted, backport changes deliberately, and see the suite's evolution at a glance.

**Why this file exists:** Per-file VERSION headers (in each file's HTML comment) track individual file evolution. But the suite as a whole also evolves — new files get added, the shape of the modular suite changes, new patterns get codified across multiple files in a single release. The Standard Set Version captures that coarser-grained evolution.

---

## Table of Contents

1. [Standard Set Version (current)](#1-standard-set-version-current)
2. [What's in this set](#2-whats-in-this-set)
3. [Per-file version table](#3-per-file-version-table)
4. [How to apply this set to a new project](#4-how-to-apply-this-set-to-a-new-project)
5. [How to bump the Set Version](#5-how-to-bump-the-set-version)
6. [Standard Set Version history](#6-standard-set-version-history)

---

## 1. Standard Set Version (current)

```
Standard Set Version: v2.6
Released:             2026-05-23
Baseline:             EverOn.Capital-Signal Phases 1–7 + EA-test-soak + EverOn.Equinex PLAN-001..PLAN-004 + cross-project SESSION_OPENER merge + 2026-05-22 code-review-before-commit elevation (L044) + 2026-05-22 Equinex plan-tracker-discipline + OPEN_TASKS register (L045 + L046) + 2026-05-22 QA-scenario-coupling rule (L047) + 2026-05-23 session-wrap-up routine (L048)
Adopter contract:     11 binding files + 4 meta files; 49 lessons (L001–L049); 13 standing rules in CLAUDE.md
```

When adopting this suite in a new project, record the Set Version in the new project's CHANGELOG.md or in its own `docs/standards/SET_VERSION_ADOPTED.md` so future updates can be back-ported deliberately.

---

## 2. What's in this set

The suite has two tiers:

### Tier 1 — Binding files (the 10-file modular suite)

These are the files an adopter copies into their project. Each one is loaded by the dispatcher pattern (`CLAUDE.md` § 12) when its topic is in scope, except for `SESSION_OPENER.md` which is loaded automatically at the start of every session per `CLAUDE.md` Rule 9.

| # | File | Role |
|---|---|---|
| 1 | `CLAUDE.md` | Binding contract — 13 standing rules, classification, workflow, validation checklist, dispatcher, plan-workflow (§ 15), optional Codex handoff (§ 14) |
| 2 | `PROJECT_STANDARDS.md` | Governance — manifest mechanics, CHANGELOG conventions, tracker structure, commit discipline, sync triggers |
| 3 | `PROMPT_STANDARDS.md` | Prompt-craft — multi-file edit prompts, ALLOWLIST + verbatim FIND/REPLACE, retry-with-deviation-warning, Codex handoff variant |
| 4 | `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Claude.ai Project Instructions field — three-tier template (static frame, project-specific, per-session) |
| 5 | `MEMORY_PROTOCOL.md` | Memory hygiene — four categories, what to store / not store, verify-before-recommending |
| 6 | `ENGINEERING_STANDARDS.md` | Engineering substrate — architecture invariants (incl. live-data settlement + time-window parsing pitfalls + refactor blast-radius), coding standards, secrets, container discipline, operator-machine ops |
| 7 | `VALIDATION_STANDARDS.md` | Test framework — 7-tier model, ownership map, deliberate-failure protocol, 24h soak, first-fire iteration expectations |
| 8 | `CICD_STANDARDS.md` | Pipeline architecture — 6-stage shape, registry-pull deploy, smoke gating, auto-rollback, 24h soak gate, staging-mirrors-prod, explicit PROD authorization |
| 9 | `LESSONS.md` | Incident-to-rule archive — 43 lessons (append-only), each with incident + cost + codification + cross-references |
| 10 | `SESSION_OPENER.md` | Session-start pre-flight (binding per `CLAUDE.md` Rule 9) — canonical environment mapping + project failure-mode catalog + first-response output template |

### Tier 2 — Meta files (about the suite)

These describe and orient the suite itself. They go alongside the binding files in the source repo but are typically not copied verbatim into adopters (adopters maintain their own README; STANDARDS_INDEX is canonical at the source; BOOTSTRAP is read once during adoption).

| # | File | Role |
|---|---|---|
| 10 | `README.md` | Entry point — overview, mental model, dispatcher reference, quick orientation |
| 11 | `STANDARDS_INDEX.md` | This file — versioned set manifest, per-file version table, Set-Version-bump policy |
| 12 | `NEW_PROJECT_BOOTSTRAP.md` | Detailed Day-Zero walkthrough — how to copy this suite into a new project (commands, customization, first commit, CI scaffold) |
| 13 | `HOW_TO_USE.md` | Practical usage guide — copy-paste bootstrap prompt + supporting prompts (Day-One feature work, code review, prompt audit, quarterly audit, lesson backport) + troubleshooting |

---

## 3. Per-file version table

Current state as of Set Version v2.5 (2026-05-23):

| File | Tier | Current Version | Last Updated | Change-driver |
|---|---|---|---|---|
| `CLAUDE.md` | Binding | 3.6 | 2026-06-07 | NEW Rule 13 "Senior-review-and-optimize pass before a plan goes to approval is MANDATORY" + § 15.8 canonical review prompt + § 15.2 Phase-1 note; § 3 heading "12" → "13 standing rules"; § 13 sources-of-truth bullet "12" → "13" (L049) |
| `PROJECT_STANDARDS.md` | Binding | 1.4 | 2026-05-22 | (unchanged in v2.4) |
| `PROMPT_STANDARDS.md` | Binding | 1.5 | 2026-05-22 | (unchanged in v2.4) |
| `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Binding | 1.4 | 2026-05-22 | (unchanged in v2.4) |
| `MEMORY_PROTOCOL.md` | Binding | 1.4 | 2026-05-22 | (unchanged in v2.4) |
| `ENGINEERING_STANDARDS.md` | Binding | 1.3 | 2026-05-22 | (unchanged in v2.4) |
| `VALIDATION_STANDARDS.md` | Binding | 1.2 | 2026-05-16 | (unchanged in v2.4) |
| `CICD_STANDARDS.md` | Binding | 1.2 | 2026-05-16 | (unchanged in v2.4) |
| `LESSONS.md` | Binding | 1.12 | 2026-06-07 | L049 added (A plan draft is a hypothesis — senior-review-and-optimize pass before approval) above L048 |
| `SESSION_OPENER.md` | Binding | 1.4 (template) / 1.6 (project) | 2026-06-07 | project-local § 3.1 NEW row 12 (plan without senior-review-and-optimize pass — Rule 13 / L049) |
| `SESSION_CLOSER.md` | Binding | 1.0 (template) / 1.0 (project) | 2026-05-23 | NEW binding file — session wrap-up routine forcing function (L048). Symmetric counterpart to SESSION_OPENER.md |
| `README.md` | Meta | 1.9 | 2026-05-23 | LESSONS.md row "47 lessons" → "48 lessons (L001–L048)"; CLAUDE.md row "11 rules" → "12 rules incl. Rule 12 session-wrap-up"; binding-files count 10 → 11; new SESSION_CLOSER row added |
| `STANDARDS_INDEX.md` | Meta | 1.9 | 2026-06-07 | Set Version v2.5 → v2.6; § 1 adopter contract refreshed (48 → 49 lessons; 12 → 13 standing rules); § 2 CLAUDE.md row "9" → "13 standing rules" (pre-existing-drift fix); § 6 history v2.6 entry |
| `NEW_PROJECT_BOOTSTRAP.md` | Meta | 1.1 | 2026-05-22 | (unchanged in v2.5) |
| `HOW_TO_USE.md` | Meta | 1.6 | 2026-05-23 | § 4.1 + § 10 lesson + rule count refresh (47 → 48 lessons; 11 → 12 standing rules) |

**Total file count:** 15 (11 binding + 4 meta).
**Total lesson count in LESSONS.md:** 49 (L001–L049).

---

## 4. How to apply this set to a new project

The dispositive walkthrough is in `NEW_PROJECT_BOOTSTRAP.md`. The summary:

### 4.1 Quick start

1. **Read** this file (STANDARDS_INDEX.md) + `README.md` for orientation (~15 min)
2. **Choose** a copy strategy: independent copy (Pattern A, recommended) or shared via symlink/submodule (Pattern B, for organizations enforcing identical standards)
3. **Run** the bootstrap procedure from `NEW_PROJECT_BOOTSTRAP.md` (Day Zero — ~30–60 min total)
4. **Record** the Set Version adopted (this is v1.0 if adopting today) in the new project's CHANGELOG or `docs/standards/SET_VERSION_ADOPTED.md`
5. **Customize** placeholders walking `README.md` § 6 customization checklist
6. **First commit** lands the governance scaffold (per `NEW_PROJECT_BOOTSTRAP.md`)

### 4.2 What you get

After adoption:

- Repo-root `CLAUDE.md` carrying the 13 standing rules + project-specific critical-files list
- `docs/standards/` containing the 7 focused standards files
- `archive/LESSONS.md` carrying the incident-to-rule archive (initially shared from the source set; lessons specific to your project accumulate in your local copy)
- Optional Codex handoff protocol (`CLAUDE.md` § 14) if your project uses a second AI agent
- Governance scripts (`scripts/check_doc_coverage.py`, `scripts/check_test_coverage_drift.py`) — these come with the bootstrap, not the standards files themselves
- CI scaffold (governance stage at minimum) — see `NEW_PROJECT_BOOTSTRAP.md` § 7

### 4.3 Set-Version drift management

Once adopted, the local copy of the standards lives independently. Backports from the source set are explicit — you decide what to take.

When the source set bumps Set Version (e.g., v1.0 → v1.1):

1. Read the new Set Version's CHANGE LOG entry (see § 6 below)
2. Decide which changes are relevant to your project
3. Cherry-pick the relevant per-file updates into your local copy
4. Record the new "Set Version adopted" reference

Major Set Version bumps (e.g., v1.0 → v2.0) require an explicit migration — read the migration notes in the new Set Version's CHANGE LOG before backporting.

---

## 5. How to bump the Set Version

The Set Version represents the coarse-grained maturity of the suite. It's distinct from per-file versions.

### 5.1 When to bump (Minor: v1.X → v1.X+1)

Additive changes that don't break adopters:

- New lessons added to LESSONS.md (e.g., L036, L037, ...)
- New sub-sections added to existing standards files
- New anti-patterns codified
- New optional features (e.g., a new optional Codex handoff variant)
- Refinements to existing patterns (e.g., L029 refining L010)

Adopters can choose to backport or stay at their current Set Version. No migration required.

### 5.2 When to bump (Major: v1.X → v2.0)

Structural changes that affect the suite's shape:

- New binding file added (the modular suite grows from 9 to 10+ files)
- An existing binding file split into multiple files
- Two binding files consolidated into one
- Dispatcher table reorganized
- Critical file renamed (e.g., `docs/documents_manifest.md` → `docs/manifest.md`)
- Any rule removed (rare — and documented in LESSONS as deprecation)

Adopters need to migrate. Migration notes go in the Set Version's CHANGE LOG.

### 5.3 The bump procedure

1. **Decide** the new Set Version (Minor or Major)
2. **Add an entry to § 6 Standard Set Version history below** at the top (newest first), with the date and a summary of what changed
3. **Bump this file's VERSION header** (HTML comment at top) — Minor for set Minor bumps, Major for set Major bumps
4. **Update the per-file version table** in § 3 to reflect any per-file bumps that landed alongside
5. **Commit** the Set Version bump in the same commit (or split-commit chain) as the changes that warranted it
6. **Tag** the source repo with the new Set Version (`v1.1`, `v2.0`, etc.) for adopter reference

### 5.4 Per-file bumps vs Set Version bumps

These are independent. A per-file Minor bump (e.g., PROMPT_STANDARDS 1.2 → 1.3) doesn't automatically trigger a Set Version bump. A Set Version bump usually coincides with multiple per-file bumps (a coordinated refresh across files).

Rule of thumb:

- A single-file edit (typo fix, anti-pattern add) → per-file bump only
- A coordinated multi-file refresh (e.g., adding a new pattern that touches 4 files) → consider a Set Version Minor bump
- A structural change (new file, split, consolidation) → Set Version Major bump

---

## 6. Standard Set Version history

Newest first. Append-only — past entries describe what changed at the time and stay as historical record.

### v2.6 — 2026-06-07 — Senior-review-and-optimize pass before plan approval (Rule 13 + § 15.8 + L049) — Minor bump (additive rule, no new file)

**Minor bump.** Additive — no adopter migration beyond appending Rule 13 + § 15.8 to repo-root `CLAUDE.md`. Codifies 1 new lesson (L049) from the EverOn.Equinex 2026-06-07 session: the senior-review pass on PLAN-012 (run against the real EA source) caught a non-functional `SYMBOL_TRADE_MODE` market-open check, a backwards panel state, and redundant per-tick recomputation — all shipped by the drafting pass despite the plan looking complete. NEW Rule 13 "Senior-review-and-optimize pass before a plan goes to approval is MANDATORY" + NEW § 15.8 (canonical review prompt; the pass is the last task of plan development, applies fixes in place, records them in the plan CHANGE LOG, surfaces new decisions). Plan-level analogue of Rule 10 (per-commit code review). Per-file bumps: CLAUDE.md 3.5 → 3.6; LESSONS.md 1.11 → 1.12; SESSION_OPENER project 1.5 → 1.6; STANDARDS_INDEX (this file) 1.8 → 1.9. § 1 adopter contract: 48 → 49 lessons; 12 → 13 standing rules. Same-commit pre-existing-drift fix: § 2 + § 4 "9 standing rules" → "13 standing rules" (stale since the Rule 10 addition).

### v2.5 — 2026-05-23 — Session wrap-up routine (Rule 12 + SESSION_CLOSER.md + L048) — Major bump (new binding file)

**Major bump.** Adopter migration required: instantiate `docs/SESSION_CLOSER.md` from the template + append Rule 12 to repo-root `CLAUDE.md`. Codifies 1 new lesson (L048) from EverOn.Equinex 2026-05-22/23 multi-day session — operator observed that without a session-end forcing function, new patterns/rules/lessons/scope-expansions emerged during long sessions are easy to forget by farewell time; OPEN_TASKS goes stale; `/tmp/` artifacts accumulate. Symmetric to v2.0/v2.1 introduction of SESSION_OPENER.md (Rule 9, L043) — same shape applied to the session-end boundary.

**What v2.5 carries that v2.4 did not:**

- **NEW binding file `SESSION_CLOSER.md`** — template at `docs/standards/SESSION_CLOSER.md` v1.0 + project-local at `docs/SESSION_CLOSER.md` v1.0. Binding suite grows from 10 files to 11.
  - § 1 wrap-up routine has 9 mandatory steps including step 1.7 **lessons-learned scan** that surfaces candidate codifications (new rules / lessons / memory entries / SESSION_OPENER rows / scope expansions / conventions) with codify / queue / discard recommendations per candidate.
  - § 2 wrap-up failure-mode catalog (symmetric to SESSION_OPENER § 3).
  - § 4 first-response output template (proof-of-wrap-up visible to operator).
- **CLAUDE.md template § 3 NEW Rule 12:** "Session wrap-up routine on operator command is MANDATORY." Trigger keywords: `"wrap up"` / `"wrap"` / `"end session"` / `"close out"` (context-disambiguated) / `"end of session"` / `"finish up"`. Same-commit drift fix: § 3 heading "11 standing rules" → "12 standing rules"; § 13 sources-of-truth "11" → "12."
- **LESSONS.md NEW L048:** "Session wrap-up routine as forcing function against detail loss across session boundaries." Full incident block from the 2026-05-22/23 multi-day Equinex session. Pattern-recognition rule: every session boundary needs a forcing function — Rule 9/L043 covers start, Rule 12/L048 covers end; the shape generalizes to any high-stakes transition.
- **README.md + HOW_TO_USE.md:** count refresh — "11 standing rules" → "12 standing rules"; "47 lessons (L001–L047)" → "48 lessons (L001–L048)"; binding files count 10 → 11; new SESSION_CLOSER row in README binding-files table.

**Adopter migration steps (cherry-pick):**

1. Copy `docs/standards/SESSION_CLOSER.md` template into adopter's project at `docs/SESSION_CLOSER.md`. Customize §§ 2 (failure-mode catalog seeded with universal rows + project-specific rows) + 4 (output-block content per project's deployable artifact + tag conventions).
2. Append Rule 12 from CLAUDE.md template § 3 into adopter's repo-root CLAUDE.md after Rule 11 (verbatim — rule body is domain-neutral). Reconcile § 3 heading + § 13 sources-of-truth bullet from "11" → "12."
3. Append L048 to adopter's LESSONS.md (top of § 3, above L047) — text is domain-neutral.
4. Refresh adopter's README.md + HOW_TO_USE.md rule / lesson / binding-files counts.
5. Bump per-file VERSION headers + CHANGE LOG entries.
6. Optional: create `feedback_session_closer_routine.md` memory file declaring the rule semantics; add MEMORY.md index hook.

### v2.4 — 2026-05-22 — QA / smoke-test scenario coupling rule (L047)

**Minor bump.** Additive, no adopter migration required structurally (adopters cherry-pick Rule 11 into their repo-root CLAUDE.md + add L047 + add SESSION_OPENER row 13 + refresh counts in README/HOW_TO_USE). Codifies 1 new lesson (L047) from the EverOn.Equinex 2026-05-22 session — operator-driven rule addition after observing that PLAN-001..PLAN-004's scenarios were plan-design-time only, leaving mid-flight changes and Minor changes outside plans without a change-time forcing function for verification.

**What v2.4 carries that v2.3 did not:**

- **CLAUDE.md § 3 NEW Rule 11:** "QA / smoke-test scenario for every change." Per-change coupling — every behavior-affecting change adds a written QA / smoke-test scenario (what to verify / how to verify / expected pass criteria) to the plan's tracker (sibling for big plans per § 15.7, in-file § 4 for small plans) OR `docs/Plans/OPEN_TASKS.md` "Pending verification" section + CHANGELOG `QA scenarios` sub-section (for Minor changes outside a § 15 plan). Same-commit coupling. Exempt: pure doc / governance / lessons / manifest / standards-suite changes (no observable runtime behavior). Status markers ⏸ / ✅ / ❌ / ⏭ mirror § 15.7.
- **CLAUDE.md § 3 heading drift fix:** "The 10 standing rules" → "The 11 standing rules."
- **CLAUDE.md § 13:** sources-of-truth bullet "The 10 standing rules" → "The 11 standing rules."
- **LESSONS.md NEW L047:** "QA / smoke-test scenarios must be coupled to changes at change-time, not validation-time." Codifies the pattern. Diagnosis frames the meta-lesson as a specific application of L044's "forcing-function cadence must match failure cadence." Plan-design-time scenarios fire once per plan-draft; per-change failures need per-change forcing functions.
- **SESSION_OPENER.md template § 3.1 NEW row 13:** "Behavior-affecting change shipped without a paired QA / smoke-test scenario" — Memory/lesson column cites Rule 11 + L047.
- **README.md + HOW_TO_USE.md:** count refresh — "10 standing rules" → "11 standing rules"; "46 lessons (L001–L046)" → "47 lessons (L001–L047)."

**Adopter migration steps (cherry-pick):**

1. Append Rule 11 from CLAUDE.md § 3 into adopter's repo-root CLAUDE.md after Rule 10 (verbatim — rule body is domain-neutral).
2. Reconcile § 3 heading + § 13 sources-of-truth bullet from "10" → "11."
3. Append L047 to adopter's LESSONS.md (top of § 3, above L046).
4. Add row 13 to adopter's SESSION_OPENER.md (template + project-local) § 3.1.
5. Refresh adopter's README.md + HOW_TO_USE.md rule/lesson counts.
6. Bump per-file VERSION headers + CHANGE LOG entries.
7. Optional: create `feedback_qa_scenario_coupling.md` memory file declaring the rule + 3-element scenario template; add MEMORY.md index hook.

### v2.3 — 2026-05-22 — Plan tracker discipline + local OPEN_TASKS register (L045 + L046) — cross-project backport from EverOn.Equinex

**Minor bump.** Additive, no adopter migration required. Codifies 2 new lessons (L045 + L046) from EverOn.Equinex 2026-05-22 PLAN-004 close-out session. Cross-project backport mirroring EverOn.Capital-Signal commit `5ee36ed` (which was Capital-Signal's own v2.3 — Equinex made parallel v2.2 content for the same lessons that Capital-Signal had to renumber).

**What v2.3 carries that v2.2 did not:**

- **CLAUDE.md § 15.7 promoted to canonical standards form:** the "Tracker requirement for plans" sub-section was already in the Equinex repo-root CLAUDE.md from earlier same-day commits `1bfd62d` (big-plan sibling tracker) and `6ec4469` (small-plan in-file tracker symmetric companion). v2.3 doesn't re-edit the text; it formally counts § 15.7 as standards-suite content backed by L045.
- **SESSION_OPENER.md template § 1.3:** "Tracker tip" extended with a priority-ordered tracker-source list: (a) local-only `docs/Plans/OPEN_TASKS.md` register if the project uses one (read if present, skip if absent — per L046); (b) per-plan tracker `docs/Plans/PLAN-NNN_tracker.md` for multi-task / multi-scenario plans per L045; (c) in-file § 4 phase block for small plans per L045; (d) latest CHANGELOG entry; (e) project-specific rolling tracker (fallback).
- **SESSION_OPENER.md template § 3.1 NEW rows 11 + 12:** row 11 "starting a § 15 plan without granular sub-task tracking" (L045); row 12 "local-only OPEN_TASKS.md register stale or unmaintained" (L046).
- **MEMORY_PROTOCOL.md § 1 Category B:** NEW example bullet — permission policy (which action classes the operator wants always-prompted vs auto-allowed). Sub-paragraph explaining the memory + `.claude/settings.json` allowlist mirror pattern (memory holds the semantics; settings.json is the harness-level implementation; if they drift, memory wins).
- **LESSONS.md:** L045 (Plan tracker discipline — big sibling vs small in-file) + L046 (Local-only OPEN_TASKS.md register) added at top of § 3 above L044.

**Adopter migration:** None required for Minor bump. To backport into an adopting project:

1. Append § 15.7 (if not already in the adopter's repo-root CLAUDE.md) — verbatim from the template, after § 15.6, before End-of-contract.
2. Apply the § 1.3 + § 3.1 updates to the adopter's `docs/SESSION_OPENER.md` (project-local) and/or `docs/standards/SESSION_OPENER.md` (template).
3. Apply the Category B + mirror-paragraph update to the adopter's `docs/standards/MEMORY_PROTOCOL.md`.
4. Append L045 + L046 to the adopter's `archive/LESSONS.md` (verbatim — they're domain-neutral).
5. If the adopter wants the local OPEN_TASKS.md register: add `docs/Plans/OPEN_TASKS.md` to its `.gitignore` and seed the file locally.
6. If the adopter wants the permission-policy memory pattern: create a `feedback_permission_policy.md` memory file declaring which actions stay gated, and mirror the auto-allow side into `.claude/settings.json` allowlist.

### v2.2 — 2026-05-22 — Code-review-before-commit elevated to Rule 10 (L044)

**Minor bump.** Additive, no adopter migration required (existing adopters cherry-pick Rule 10 into their repo-root CLAUDE.md + add L044 + refresh SESSION_OPENER row 3 + bump counts in README/HOW_TO_USE). Codifies 1 new lesson (L044) from EverOn.Capital-Signal's 2026-05-22 session-start incident — same session that codified Rule 9 honored code-review on the first commit but silently dropped it on the second; operator caught it post-commit. Diagnosis: prior forcing functions (memory + SESSION_OPENER § 3 row 3) are session-scoped, but code-review-skip is a per-commit failure mode. Forcing-function cadence must match failure cadence.

**What v2.2 carries that v2.1 did not:**

- **CLAUDE.md template § 3 NEW Rule 10:** "Code review before commit is MANDATORY." Procedural framing: `edits → governance → named review table → "go on commit?" → commit`. Review IS step 3 — skipping it breaks the pattern. Cites L044 for the incident. § 8 step 5 + § 11 "Code review before staging" retained as detailed checklists, now cross-referenced from Rule 10 as the binding anchor.
- **CLAUDE.md template § 3 heading drift fix:** "The 9 standing rules" → "The 10 standing rules" (prior v2.1 cross-project merge added Rule 9 without updating the heading count; now reconciled).
- **CLAUDE.md template § 13:** sources-of-truth bullet "The 9 standing rules" → "The 10 standing rules."
- **LESSONS.md NEW L044:** "Session-scoped checklists don't enforce per-commit discipline; embed the rule in the procedure." Full incident block from the 2026-05-22 EverOn session.
- **SESSION_OPENER.md template § 3.1 row 3** (code-review-skipped) Memory/lesson column updated to cite CLAUDE.md Rule 10 (binding) + L027 + L044 (was only L027).
- **README.md + HOW_TO_USE.md:** count refresh — "9 standing rules" → "10 standing rules"; "43 lessons (L001–L043)" → "44 lessons (L001–L044)".

**Adopter migration steps (cherry-pick):**

1. Append Rule 10 from CLAUDE.md template § 3 into adopter's repo-root CLAUDE.md after Rule 9 (verbatim block — the rule body is domain-neutral).
2. Reconcile § 3 heading + § 13 sources-of-truth bullet from "9" → "10" if not already done.
3. Append L044 to adopter's LESSONS.md (top of § 3, above L043) — text is domain-neutral.
4. Update adopter's SESSION_OPENER.md (template + project-local) row 3 (code-review-skipped) to cite Rule 10.
5. Refresh adopter's README.md + HOW_TO_USE.md rule/lesson counts.
6. Bump per-file VERSION headers + CHANGE LOG entries.

### v2.1 — 2026-05-22 — Cross-project SESSION_OPENER merge (Equinex v1.1 → v2.1)

**Major bump.** Adopter migration required: instantiate `docs/SESSION_OPENER.md` from the template + append Rule 9 to repo-root `CLAUDE.md`. Codifies 1 lesson (L043) from EverOn.Capital-Signal's 2026-05-22 session-start incident.

**What v2.1 carries that v1.1 did not:**

- **NEW binding file `SESSION_OPENER.md`** — template at `docs/standards/SESSION_OPENER.md` v1.1 + project-local instance at `docs/SESSION_OPENER.md` v1.0 (Equinex-customized — no remote envs, replaced with EA version + snapshot mapping; § 3 failure-mode catalog seeded with Equinex-specific rows derived from L036–L042 + project memory). Binding suite grows from 9 files to 10.
- **NEW `CLAUDE.md` Rule 9 "Session start pre-flight is MANDATORY"** — every new agent session reads SESSION_OPENER.md and posts its § 4 first-response output block BEFORE any action. Operator-only abbreviation via explicit "skip pre-flight." Rules 1–8 numbering unchanged.
- **NEW lesson L043** — "Session-start pre-flight as forcing function." Project-of-origin reads "EverOn.Capital-Signal" per the L-archive convention of preserving the originating project.

**Files refreshed (4 binding + 2 meta):**

- `CLAUDE.md` (2.0 → 3.0) — Rule 9 appended to § 3; § 13 "8 standing rules" → "9 standing rules" cross-ref updated; CHANGE LOG entry. Rules 1–8 byte-identical.
- `LESSONS.md` (1.6 → 1.7) — L043 entry added at top of § 3; TOC extended.
- `SESSION_OPENER.md` (NEW — template 1.1 / project 1.0) — see above.
- `README.md` (1.3 → 1.4) — binding-file count "9 binding + 4 meta" → "10 binding + 4 meta"; SESSION_OPENER row added to binding-files table; lesson count refreshed to 43.
- `HOW_TO_USE.md` (1.0 → 1.1) — § 4.1 Day-One feature-work prompt leads with the SESSION_OPENER pre-flight as the FIRST action (overrides the prior "Read CLAUDE.md once" lead step).
- `STANDARDS_INDEX.md` (1.2 → 1.3) — this file. Set Version bump + § 1 adopter contract + § 2 binding-files table (9 → 10 rows) + § 3 per-file table + § 6 history extended.

**Equinex-specific provenance note:** v2.1 in Equinex is a CROSS-PROJECT merge with EverOn.Capital-Signal's v2.1. EverOn's v2.0 introduced SESSION_OPENER + Rule 9; EverOn's v2.1 backported Equinex's L036–L042 (which Equinex already had from its v1.1). Equinex's v2.1 lands the SESSION_OPENER + Rule 9 + L043 components from EverOn's v2.1. Net effect: both projects now sit at Set Version v2.1 with identical lesson sets (L001–L043) and identical binding-file shape (10 binding + 4 meta).

**Adopter impact (other projects bootstrapped from this standards repo):** Migration required for adopters who instantiated v1.X or earlier. Steps:
1. Copy `docs/standards/SESSION_OPENER.md` from the source into your project's `docs/standards/`
2. Customize the project-local copy as `docs/SESSION_OPENER.md` (replace §§ 2 + 3 with your project's environment mapping + failure-mode catalog)
3. Append Rule 9 to your repo-root `CLAUDE.md` (per the template's Rule 9 text); bump CLAUDE.md to a new Major version
4. Add L043 to `archive/LESSONS.md` (keep project-of-origin as "EverOn.Capital-Signal")
5. Update your manifest + CHANGELOG in the same commit

### v1.1 — 2026-05-22 — EverOn.Equinex PLAN-001..PLAN-004 refresh

**Minor bump.** Additive, no adopter migration required. Codifies 7 lessons (L036–L042) from the EverOn.Equinex multi-plan sequence 2026-05-19..05-22.

**Files refreshed (6 binding):**

- `CLAUDE.md` (1.9 → 2.0) — NEW § 15 plan workflow for vital changes (Phases 0–5; Phase 2 operator-approval gate; Phase 3 in a fresh agent session prompted from the committed plan file). § 12 dispatcher row added. The Major bump reflects the new top-level section, not a structural change to the existing 8 standing rules.
- `PROJECT_STANDARDS.md` (1.2 → 1.3) — NEW § 4.3 closed-risk annotation discipline. § 4 sync trigger table extended with the "Phase 3 ships a mitigation for an earlier plan's risk → annotate the earlier plan's risk row CLOSED in the same commit" trigger.
- `PROMPT_STANDARDS.md` (1.3 → 1.4) — § 3.2 ALLOWLIST refined with bullet-vs-prose count discipline (the bullet enumeration IS the count; prose totals can drift during plan revisions).
- `ENGINEERING_STANDARDS.md` (1.2 → 1.3) — Four new sub-sections:
  - § 1.8 Time-window parsing pitfalls — HH:MM with `end="00:00"` creates wrap-window matches at start-of-day; recommend `23:59` for end-of-day intent.
  - § 1.9 Refactor blast-radius — grep all reads before splitting a globally-read state variable into typed concerns.
  - § 4.6 Fail-safe defaults for external-data sources that may be unavailable — silent skip + log, not warn/error, when prod-only data is absent.
  - § 4.7 Safety tripwire for pattern-match drift — log uncategorized "interesting" items when matching against external string catalogs.
- `LESSONS.md` (1.5 → 1.6) — 7 new lessons (L036–L042); § 3 TOC extended.
- `STANDARDS_INDEX.md` (1.1 → 1.2) — this file. Set Version bump + per-file table refresh + § 6 history extended.

**Lesson coverage:**

| Lesson | Domain | Primary enforcement |
|---|---|---|
| L036 — Closed-risk annotation discipline | Plan governance | PROJECT_STANDARDS § 4.3 |
| L037 — Time-window wrap-fire at minute 0 | Time-parsing engineering | ENGINEERING_STANDARDS § 1.8 |
| L038 — ALLOWLIST count = bullet enumeration | Prompt craft | PROMPT_STANDARDS § 3.2 |
| L039 — Grep all reads before splitting a state variable | Refactor engineering | ENGINEERING_STANDARDS § 1.9 |
| L040 — Fail-safe defaults for external data | Error handling | ENGINEERING_STANDARDS § 4.6 |
| L041 — Pattern-match safety tripwire | Error handling | ENGINEERING_STANDARDS § 4.7 |
| L042 — Plan-first workflow for vital changes | Workflow | CLAUDE.md § 15 |

**Adopter impact:** No breaking changes. Existing adopters backport selectively:

- Projects with central domain logic that's edited frequently → adopt CLAUDE.md § 15 + PROJECT_STANDARDS § 4.3.
- Projects that parse time-of-day windows → adopt ENGINEERING_STANDARDS § 1.8.
- Projects that integrate with optional / degradable external data sources → adopt ENGINEERING_STANDARDS § 4.6 + § 4.7.
- Projects that draft multi-file agent prompts → adopt PROMPT_STANDARDS § 3.2 refinement.
- Projects that refactor inherited state-management code → adopt ENGINEERING_STANDARDS § 1.9.

### v1.0 — 2026-05-16 — Baseline released

**Set Version baseline.** The suite refreshed with EverOn.Capital-Signal Phase 4–7 + EA-test-soak lessons. 16 new lessons (L020–L035) added to LESSONS.md. All 9 binding files refreshed to incorporate the new lessons via topical cross-references.

**Major changes from initial draft (pre-v1.0) to v1.0:**

- 16 new lessons (L020–L035) covering: Codex handoff protocol, live data settlement-window mutability, 24h staging soak, staging-mirrors-prod, never raw `docker compose up`, CI-injected `.env` wipes, run-commits-yourself, code-review-before-commit, push cadence, distribute-doc-sync-across-split-commits, explicit PROD-action authorization, never-bounce-to-UI, investigate-when-questioned, retry-with-deviation-warning, macOS disk-full recovery, Hetzner web-console avoidance
- CLAUDE.md template: new § 14 Codex handoff (OPTIONAL); new § 8.5 code review (separate gate); new § 10 investigate-when-questioned; new § 11 sub-sections for push cadence + run-commits-yourself + code review
- CICD_STANDARDS.md: new § 4.7 CI-injected file wipes; new § 9.7/9.8/9.9 (24h soak, staging mirrors prod, explicit PROD); new § 11.4 REST API status probing; new anti-patterns 13.11–13.14
- ENGINEERING_STANDARDS.md: new § 1.7 live data invariants; new § 3.6 verify config source-of-truth; new § 7.8 never raw compose-up; new § 9.6/9.7 (Hetzner avoidance, macOS recovery); new anti-patterns 10.11–10.12
- VALIDATION_STANDARDS.md: new § 5.6 first-fire iteration expectations; new § 7.5 24-hour soak; new anti-patterns 10.11–10.12
- PROMPT_STANDARDS.md: new § 3.11 Codex handoff variant; new § 9.5 retry-with-deviation-warning; new § 6.12 popup-questions anti-pattern (Claude Code-specific)
- PROJECT_STANDARDS.md: new § 7.7 tracker ownership; new § 8.7/8.8/8.9 (code review, run-commits-yourself, push cadence); § 8.4 refined with L029; new anti-patterns 10.9–10.11
- Two new meta files: STANDARDS_INDEX.md (this file), NEW_PROJECT_BOOTSTRAP.md
- README.md: updated file summary to "9 binding + 3 meta" framing; adoption walkthrough refactored to delegate detail to BOOTSTRAP file

**Adopter impact:** No breaking changes. Existing adopters can backport selectively. Single-agent projects skip the Codex sections entirely. Projects without live time-series data can skip the live-data invariants and 24h soak rules (but the patterns are reusable for any system with similar slow-burn regression characteristics).

### Pre-v1.0 — 2026-04-25 — Initial draft (the 9-file suite as released)

Initial release of the 9-file modular suite based on EverOn.Capital-Signal Phases 1–3. Captured in `README.md` v1.0 / v1.1 history. The Standard Set Version concept didn't exist yet at this point — adopters of the pre-v1.0 draft tracked per-file versions only.

---

## End of index

This file is the canonical record of the suite's coarse-grained evolution. When a new Set Version is released, add an entry to § 6 and bump this file's VERSION header. Adopters refer to this file to decide when to backport.

Per-file CHANGE LOG entries in each file's HTML-comment header capture per-file evolution at finer granularity. Both layers stay in sync — every Set Version release coincides with per-file bumps that the § 3 table reflects.
