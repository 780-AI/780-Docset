<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-06-13 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
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
Standard Set Version: v1.1
Released:             2026-06-13
Baseline:             v1.0 clean domain-neutral baseline + the experiences-log template, PROJECT-OWNED markers, and setup-and-strip (PLAN-002 Slice 1).
Adopter contract:     11 binding files + 4 meta files (+ SETUP.md + STANDARDS_LOG.md); 49 lessons (L001–L049); 13 standing rules in CLAUDE.md
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
| 1 | `CLAUDE.md` | Binding contract — 13 standing rules, classification, workflow, validation checklist, dispatcher, plan workflow (§ 15), optional Codex handoff (§ 14) |
| 2 | `PROJECT_STANDARDS.md` | Governance — manifest mechanics, CHANGELOG conventions, tracker structure, commit discipline, sync triggers |
| 3 | `PROMPT_STANDARDS.md` | Prompt-craft — multi-file edit prompts, ALLOWLIST + verbatim FIND/REPLACE, retry-with-deviation-warning, Codex handoff variant |
| 4 | `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Claude.ai Project Instructions — three-tier template (static frame, project-specific, per-session) |
| 5 | `MEMORY_PROTOCOL.md` | Memory hygiene — four categories, what to store / not store, verify-before-recommending |
| 6 | `ENGINEERING_STANDARDS.md` | Engineering substrate — architecture invariants, coding standards, secrets, container discipline, ops |
| 7 | `VALIDATION_STANDARDS.md` | Test framework — tiered model, ownership map, deliberate-failure protocol, soak, first-fire expectations |
| 8 | `CICD_STANDARDS.md` | Pipeline architecture — staged shape, registry-pull deploy, smoke gating, auto-rollback, soak gate, explicit PROD authorization |
| 9 | `LESSONS.md` | Incident-to-rule archive — 49 lessons (append-only), each with incident + cost + codification + cross-references |
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

---

## 3. Per-file version table

Current state as of Set Version v1.1 (2026-06-13). Files unchanged since v1.0 keep their 2026-06-07 dates.

| File | Tier | Version | Last Updated |
|---|---|---|---|
| `CLAUDE.md` | Binding | 1.1 | 2026-06-13 |
| `PROJECT_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `PROMPT_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Binding | 1.0 | 2026-06-07 |
| `MEMORY_PROTOCOL.md` | Binding | 1.0 | 2026-06-07 |
| `ENGINEERING_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `VALIDATION_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `CICD_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `LESSONS.md` | Binding | 1.0 | 2026-06-07 |
| `SESSION_OPENER.md` | Binding | 1.1 | 2026-06-13 |
| `SESSION_CLOSER.md` | Binding | 1.1 | 2026-06-13 |
| `README.md` | Meta | 1.0 | 2026-06-07 |
| `STANDARDS_INDEX.md` | Meta | 1.1 | 2026-06-13 |
| `NEW_PROJECT_BOOTSTRAP.md` | Meta | 1.1 | 2026-06-13 |
| `HOW_TO_USE.md` | Meta | 1.0 | 2026-06-07 |
| `SETUP.md` | Meta | 1.1 | 2026-06-13 |
| `STANDARDS_LOG.md` | Meta | 1.0 | 2026-06-13 |

**Total file count:** 17 (11 binding + 6 meta).
**Total lesson count in `LESSONS.md`:** 49 (L001–L049).

---

## 4. How to apply this set to a new project

The fastest path is **`SETUP.md`** — paste its prompt into a fresh Claude Code session in the new
project's directory and follow it. For the manual, step-by-step route, see `NEW_PROJECT_BOOTSTRAP.md`.

### 4.1 What you get

- Repo-root `CLAUDE.md` carrying the 13 standing rules + project-specific critical-files list
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
