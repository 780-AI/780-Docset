<!-- VERSION: 1.5 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.5 — 2026-08-16 — Standard Set Version v1.5 (PLAN-010 upstream intake): eleven lessons L057–L067 + NEW Rule 15 (post-implementation verification of the NEW behavior) + Rule 14 upgraded to project-data locality (claude_project_data.sh replaces bootstrap_memory.sh; verified at session open AND close). § 1 counts → 67 lessons / 15 rules; § 2 rows 1 + 9; § 3 caption → v1.5 + cells (CLAUDE.md 1.4, SESSION_OPENER 1.5, SESSION_CLOSER 1.3, STANDARDS_INDEX 1.5, NEW_PROJECT_BOOTSTRAP 1.5, SETUP 1.5, MEMORY_DURABILITY_ROLLOUT_PROMPT 1.2) + total → 67 (LESSONS cell unchanged per the no-per-lesson-bump practice); § 4.1 count swept 13 → 15 (per L060); § 6 history entry added.
v1.4 — 2026-08-16 — Standard Set Version v1.4: five process-hardening lessons L052–L056 + L051 recurrence #4 (final-indentation clause). § 1 counts → 56 lessons; § 2 row 9 → 56; § 3 caption → v1.4 + cells (CLAUDE.md 1.3, SESSION_OPENER 1.4, SESSION_CLOSER 1.2, STANDARDS_INDEX 1.4, NEW_PROJECT_BOOTSTRAP 1.4, SETUP 1.4; MEMORY_DURABILITY_ROLLOUT_PROMPT cell caught up to its already-shipped 1.1) + total → 56 (LESSONS cell unchanged per the no-per-lesson-bump practice); § 6 history entry added. Anchors: SESSION_OPENER § 1.1 + § 3.1 row (L055 / L051), SESSION_CLOSER § 1.4 + § 2.1 row (L055), CLAUDE.md § 15.2 (L054) + § 15.3 (L056). No rule added or removed.
v1.3 — 2026-06-20 — Standard Set Version v1.3: lesson L051 (the Rule 13 senior-review pass must mechanically run the linter / type-checker / tests against the plan's embedded code, not eyeball it) + a SESSION_OPENER § 3.1 universal row. § 1 lesson count → 51; § 2 row 9 → 51; § 3 caption → v1.3, SESSION_OPENER cell → 1.3, STANDARDS_INDEX cell → 1.3, total → 51 (LESSONS cell unchanged per the no-per-lesson-bump practice); § 6 history entry added. No existing rule changed (Rule 13 expectations sharpened, not rewritten).
v1.2 — 2026-06-17 — Standard Set Version v1.2 (PLAN-005): added Rule 14 (durable memory) to CLAUDE.md; SESSION_OPENER § 1.5 + § 3.1 row; lesson L050; new meta file MEMORY_DURABILITY_ROLLOUT_PROMPT.md. § 1 counts → 50 lessons / 14 rules; § 3 → 18 files (11 binding + 7 meta); CLAUDE.md + SESSION_OPENER cells → 1.2; § 6 history entry added.
v1.1 — 2026-06-13 — Standard Set Version v1.1 (PLAN-002, Slice 1): registered the STANDARDS_LOG.md
experiences-log template (meta "+"); recorded the PROJECT-OWNED marker convention + setup-and-strip;
bumped § 3 per-file versions for the edited files; refreshed counts (17 files) and added the § 6 history entry.
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; prior version history reset. Established as Standard Set Version v1.0.
-->

# STANDARDS_INDEX.md — Versioned Set Manifest

**Purpose:** The canonical record of the Standard Set Version and the per-file versions inside it.
Adopters name the version they adopted, backport changes deliberately, and see the suite at a glance.

**Why this file exists:** Per-file `VERSION` headers track each file's evolution. The **Standard Set
Version** tracks the suite as a whole — files added, structure changed, patterns codified across files.

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
Standard Set Version: v1.5
Released:             2026-08-16
Baseline:             v1.0 clean domain-neutral baseline + the experiences-log template, PROJECT-OWNED markers, and setup-and-strip (PLAN-002 Slice 1) + durable-memory Rule 14 (PLAN-005) + Rule 13 linter-enforcement lesson L051 (v1.3) + process-hardening lessons L052–L056 and the L051 final-indentation recurrence (v1.4) + upstream-intake process-hardening batch — lessons L057–L067, Rule 15, Rule 14 project-data locality (v1.5).
Adopter contract:     11 binding files + 4 meta files (+ SETUP.md + STANDARDS_LOG.md + MEMORY_DURABILITY_ROLLOUT_PROMPT.md); 67 lessons (L001–L067); 15 standing rules in CLAUDE.md
```

When adopting this suite, record the Set Version in the new project's `CHANGELOG.md` or its own
`docs/SET_VERSION_ADOPTED.md` so future updates can be back-ported deliberately.

---

## 2. What's in this set

### Tier 1 — Binding files (the 11-file modular suite)

Adopters copy these into their project. Each is loaded by the dispatcher (`CLAUDE.md` § 12) when its
topic is in scope, except `SESSION_OPENER.md` (loaded every session per Rule 9) and `SESSION_CLOSER.md`
(invoked on the wrap-up command per Rule 12).

| # | File | Role |
|---|---|---|
| 1 | `CLAUDE.md` | Binding contract — 15 standing rules, classification, workflow, validation checklist, dispatcher, plan workflow (§ 15), optional Codex handoff (§ 14) |
| 2 | `PROJECT_STANDARDS.md` | Governance — manifest mechanics, CHANGELOG conventions, tracker structure, commit discipline, sync triggers |
| 3 | `PROMPT_STANDARDS.md` | Prompt-craft — multi-file edit prompts, ALLOWLIST + verbatim FIND/REPLACE, retry-with-deviation-warning, Codex handoff variant |
| 4 | `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Claude.ai Project Instructions — three-tier template (static frame, project-specific, per-session) |
| 5 | `MEMORY_PROTOCOL.md` | Memory hygiene — four categories, what to store / not store, verify-before-recommending |
| 6 | `ENGINEERING_STANDARDS.md` | Engineering substrate — architecture invariants, coding standards, secrets, container discipline, ops |
| 7 | `VALIDATION_STANDARDS.md` | Test framework — tiered model, ownership map, deliberate-failure protocol, soak, first-fire expectations |
| 8 | `CICD_STANDARDS.md` | Pipeline architecture — staged shape, registry-pull deploy, smoke gating, auto-rollback, soak gate, explicit PROD authorization |
| 9 | `LESSONS.md` | Incident-to-rule archive — 67 lessons (append-only), each with incident + cost + codification + cross-references |
| 10 | `SESSION_OPENER.md` | Session-start pre-flight (binding per Rule 9) — environment mapping + failure-mode catalog + first-response output template |
| 11 | `SESSION_CLOSER.md` | Session-end wrap-up (binding per Rule 12) — wrap-up routine + failure-mode catalog + output template |

### Tier 2 — Meta files (about the suite)

| # | File | Role |
|---|---|---|
| 1 | `README.md` | Entry point — overview, mental model, dispatcher reference, orientation |
| 2 | `STANDARDS_INDEX.md` | This file — versioned set manifest, per-file table, bump policy |
| 3 | `NEW_PROJECT_BOOTSTRAP.md` | Detailed Day-Zero walkthrough — copy + customize + first commit |
| 4 | `HOW_TO_USE.md` | Practical usage guide — pointer to `SETUP.md` + supporting prompts (Day-One, code review, audit) |
| + | `SETUP.md` | **The one-shot bootstrap prompt** — paste into a fresh agent session to set up a new project from scratch |
| + | `STANDARDS_LOG.md` | **Experiences-log template** — the per-project contribution channel; `SETUP.md` copies it to the project's `docs/STANDARDS_LOG.md` (an adopter artifact, not a binding rule) |
| + | `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` | **Memory-durability rollout prompt** — paste-in prompt that sets up Rule 14 durable memory in an adopting project (setup machinery; stripped after use) |

---

## 3. Per-file version table

Current state as of Set Version v1.5 (2026-08-16). Files unchanged since v1.0 keep their 2026-06-07 dates.

| File | Tier | Version | Last Updated |
|---|---|---|---|
| `CLAUDE.md` | Binding | 1.4 | 2026-08-16 |
| `PROJECT_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `PROMPT_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Binding | 1.0 | 2026-06-07 |
| `MEMORY_PROTOCOL.md` | Binding | 1.0 | 2026-06-07 |
| `ENGINEERING_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `VALIDATION_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `CICD_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `LESSONS.md` | Binding | 1.0 | 2026-06-07 |
| `SESSION_OPENER.md` | Binding | 1.5 | 2026-08-16 |
| `SESSION_CLOSER.md` | Binding | 1.3 | 2026-08-16 |
| `README.md` | Meta | 1.0 | 2026-06-07 |
| `STANDARDS_INDEX.md` | Meta | 1.5 | 2026-08-16 |
| `NEW_PROJECT_BOOTSTRAP.md` | Meta | 1.5 | 2026-08-16 |
| `HOW_TO_USE.md` | Meta | 1.0 | 2026-06-07 |
| `SETUP.md` | Meta | 1.5 | 2026-08-16 |
| `STANDARDS_LOG.md` | Meta | 1.0 | 2026-06-13 |
| `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` | Meta | 1.2 | 2026-08-16 |

**Total file count:** 18 (11 binding + 7 meta).
**Total lesson count in `LESSONS.md`:** 67 (L001–L067).

---

## 4. How to apply this set to a new project

The fastest path is **`SETUP.md`** — paste its prompt into a fresh Claude Code session in the new
project's directory and follow it. For the manual, step-by-step route, see `NEW_PROJECT_BOOTSTRAP.md`.

### 4.1 What you get

- Repo-root `CLAUDE.md` carrying the 15 standing rules + project-specific critical-files list
- `docs/standards/` containing the focused standards files
- `archive/LESSONS.md` carrying the incident-to-rule archive
- Project-local `docs/SESSION_OPENER.md` + `docs/SESSION_CLOSER.md`
- Optional Codex handoff protocol (`CLAUDE.md` § 14) if the project uses a second AI agent
- Governance scripts, CI scaffold, MR template, manifest, folder structure

### 4.2 Set-Version drift management

Once adopted, the local copy lives independently. Backports from the source set are **explicit**:

1. Read the new Set Version's history entry (§ 6).
2. Decide which changes are relevant.
3. Cherry-pick the per-file edits into the local copy; bump the affected per-file versions.
4. Record the new adopted version in `docs/SET_VERSION_ADOPTED.md`.

Major Set-Version bumps include explicit migration notes — read them before backporting.

---

## 5. How to bump the Set Version

The Set Version is the coarse-grained maturity of the suite, distinct from per-file versions.

- **Minor (v1.X → v1.X+1):** additive — new lessons, new sub-sections, new optional features,
  refinements. Adopters may backport or stay. No migration required.
- **Major (v1.X → v2.0):** structural — a new binding file, a file split/merge, a dispatcher
  reorganization, a critical-file rename, a removed rule. Adopters migrate; notes go in § 6.

### Bump procedure

1. Decide Minor or Major.
2. Add an entry at the top of § 6 with the date and a summary.
3. Bump this file's `VERSION` header.
4. Update the § 3 per-file table for any per-file bumps that landed alongside.
5. Commit the bump with the changes that warranted it.

Per-file bumps and Set-Version bumps are independent: a single-file typo fix is per-file only; a
coordinated multi-file pattern is a Set-Version Minor; a structural change is a Set-Version Major.

---

## 6. Standard Set Version history

Newest first. Append-only.

### v1.5 — 2026-08-16 — Upstream-intake batch (L057–L067 + Rule 15 + Rule 14 project-data locality)

Additive Minor. First upstream intake: an adopter lineage that evolved independently on its own Set
line (2026-06 → 2026-08) folded back into the vault. Eleven genericized lessons: **L057** — identical
code + different behavior ⇒ runtime cause, instrument first; **L058** — audit every caller before
fixing a shared utility at one site; **L059** — verify evidence provenance before recording a result;
**L060** — grep every name-form of a removed identifier across code AND docs; **L061** — a reused
helper imports its implicit gates, enumerate them per new context; **L062** — plan-embedded code must
satisfy the plan's own acceptance criteria across all sites, sanitize before pasting; **L063** —
version stamps drift from their own change logs, grep the actual stamp; **L064** — validate on a
version-matched runtime with real dependencies, fakes return real driver types; **L065** — reconstruct
system state from its own event stream; **L066** — a liveness signal comes from the monitored layer's
own traffic on the monitor's own clock; **L067** — ship-gating verification must exercise the NEW
behavior itself. One NEW binding rule: **Rule 15** — post-implementation verification of the NEW
behavior is mandatory (pairs with L067). One strengthened rule: **Rule 14** upgraded in place from
memory-only durability to full **project-data locality** — physical home `.claude/project-data/`
(memory + session transcripts), managed by `scripts/claude_project_data.sh`
(`status`/`adopt`/`link`; replaces `bootstrap_memory.sh`), verified at session open
(`SESSION_OPENER` § 1.5) AND close (`SESSION_CLOSER` § 1.6); L050 carries a generalization note.
Session files gain three § 3.1 catalog rows (project-data locality / Rule 15 feature-ON / L063
stamp-vs-log). The intake mapping (upstream ↔ vault numbering) is recorded permanently in the vault's
PLAN-010 § 3 and its CHANGELOG. Adopters may stay on v1.4; to migrate, run the updated
`MEMORY_DURABILITY_ROLLOUT_PROMPT.md` (its `adopt` verb absorbs the old memory-symlink layout).

### v1.4 — 2026-08-16 — Process-hardening batch (L052–L056 + L051 recurrence #4)

Additive Minor. Five lessons from live adoption + plan-workflow experience: **L052** — an installer must
create every file it references, not just account for it; **L053** — the bootstrap delivery docs are a
parity set updated in the same pass (catch-up to an already-released Set Version is installer-only, never
a Set-Version bump; inventory changes update the lay-down + strip set-cover same-commit); **L054** — the
Phase-3 ALLOWLIST enumerates the plan file + sibling tracker as same-commit promotion rows so the count
matches `git status`; **L055** — recorded push-state is reconciled against the *real* remote
(`git ls-remote`) at session open and flipped in the same wrap-up as the push; **L056** — the Phase-3
implementer's first act is a reconcile pass of the plan against the live source (the backstop to Rule 13).
Plus **L051 recurrence #4**: the Rule 13 tools must run against the embedded code at the exact final
indentation it ships at. Anchors: `SESSION_OPENER.md` § 1.1 + § 3.1 row; `SESSION_CLOSER.md` § 1.4 +
§ 2.1 row; `CLAUDE.md` § 15.2 + § 15.3. No binding file added or removed and no existing rule changed —
adopters may backport or stay on v1.3.

### v1.3 — 2026-06-20 — Rule 13 senior-review pass must mechanically run the tools (L051)

Additive Minor. Adds lesson **L051** — the Rule 13 senior-review-and-optimize pass MUST mechanically run
the linter + type-checker + tests against the EXACT code a plan commits in its § 5 transformation rules
(not eyeball it), the fix MUST land in § 5 itself (not only be narrated in the CHANGE LOG), and the
recorded result MUST name the specific lines / checks it fixed — codifying a defect class that recurred
across three consecutive plans. Adds a matching `SESSION_OPENER.md` § 3.1 universal catalog row. No binding
file added or removed and **no existing rule changed** — Rule 13's expectations are sharpened, not
rewritten; adopters may backport or stay on v1.2.

### v1.2 — 2026-06-17 — Durable project memory (Rule 14)

Additive Minor (PLAN-005). Adds binding **Rule 14** (the Claude memory store lives inside the repo at
`./.claude/memory/` with the harness dir symlinked to it, so memory survives a machine change and a folder
move; repaired idempotently by `scripts/bootstrap_memory.sh`); a self-healing `SESSION_OPENER.md` § 1.5
pre-flight (verify + auto-repair + halt-on-empty) + a § 3.1 catalog row; lesson **L050**; and the
`MEMORY_DURABILITY_ROLLOUT_PROMPT.md` meta file for adopters. No binding file removed and no existing rule
changed — adopters may backport or stay on v1.1.

### v1.1 — 2026-06-13 — Experiences log + PROJECT-OWNED markers + setup-and-strip

Additive Minor (PLAN-002, Slice 1). Adds the `STANDARDS_LOG.md` experiences-log template (the per-project
contribution channel fed by `SESSION_CLOSER.md` § 1.7); wraps the project-customizable blocks in
`CLAUDE.md` + the session files (template and adopter) in `PROJECT-OWNED` markers so a future `sync`
preserves them; reworks `SETUP.md` into setup-and-strip (install the operative standard, create the log,
write `SET_VERSION_ADOPTED.md` to `docs/`, then strip the setup machinery as a second commit). No binding
file added or removed and no rule changed — adopters may backport or stay on v1.0.

### v1.0 — 2026-06-07 — Clean domain-neutral baseline

Initial domain-neutral release. The suite carries the 13 standing rules (`CLAUDE.md` § 3), 49 lessons
(L001–L049), and the session start/end forcing functions (Rules 9 & 12). All project identity and
source-domain specifics from the originating projects were removed; examples are role-based and
generic. This is the canonical baseline that `SETUP.md` distributes to new projects.

---

## End of index

When a new Set Version is released, add an entry to § 6 and bump this file's `VERSION` header. Per-file
CHANGE LOG entries capture finer-grained evolution; both layers stay in sync.
