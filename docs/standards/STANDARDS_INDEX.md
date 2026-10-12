<!-- VERSION: 2.8 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v2.8 — 2026-10-12 — Standard Set Version v2.8 (lessons batch + senior-review checklist + template fixes + decision-log template): lessons L082–L089 (L082–L088 the curator's own, consolidated; L089 adopter-originated, confirmed at the intake gate) + an L080 data point; CLAUDE.md 1.8 (§ 15.8 checklist, Rule 14 junction + never-by-hand, TEMPLATE-ONLY dispatcher note, Rule 12 alias, § 1/§ 14 stub wording); PROMPT_STANDARDS 1.1 (§ 3.12), ENGINEERING_STANDARDS 1.1 (§ 2.7), PROJECT_STANDARDS 1.2 (§ 8.10), MEMORY_PROTOCOL 1.2 + CICD_STANDARDS 1.1 (dangling reference), SESSION_OPENER 1.9, SESSION_CLOSER 1.8, LESSONS 1.3, README 1.6; NEW meta template DECISION_LOG.md 0.1. § 1 block → v2.8; § 2 rows; § 3 caption + cells + totals (16 files = 11 binding + 5 meta; 89 lessons); § 4 self-service wording; § 6 v2.8 entry.
v2.7 — 2026-10-03 — Standard Set Version v2.7 (fleet-convergence intake — an operator adopter's own-line suite, under the intake gate): lessons L080 (feature intake — preserve, investigate, redesign, plan) + L081 (cloud-synced folder operating rules; gitignored ≠ sync-ignored) added; CLAUDE.md → 1.7 (NEW § 15.9 Feature intake + § 15.2 Phase 0 pointer; Rule 14 cloud-synced-folder bullet; Rule 12 step 6 retitled to match SESSION_CLOSER § 1.6). § 1 block → v2.7 (counts → 81 lessons); § 2 row 9 → 81; § 3 caption → v2.7 + cells (CLAUDE 1.7, README 1.5, STANDARDS_INDEX 2.7) + lesson total → 81; § 6 history entry. No rule change (15).
v2.6 — 2026-10-03 — Standard Set Version v2.6 (clock trust — the second harvested adopter entry, under the Rule 16 gate): lesson L079 added (the machine clock is an untrusted input — verify against an external authority before stamping or recording skew); PROJECT_STANDARDS → 1.1 (§ 5.6 stamp-date check). § 1 block → v2.6 (counts → 79 lessons); § 2 row 9 → 79; § 3 caption → v2.6 + cells (PROJECT_STANDARDS 1.1, README 1.4, STANDARDS_INDEX 2.6) + lesson total → 79; § 6 history entry. No rule change (15).
v2.5 — 2026-09-05 — Standard Set Version v2.5 (PLAN-012 sync handoff): every engine write into a target (sync --write AND integrate write-back) now leaves the engine-transient docs/SYNC_HANDOFF.md explaining what landed + what remains; SESSION_OPENER → 1.8 (§ 1.1 engine-handoff check); LESSONS → 1.2 (L069–L078 date-line corrections — the vault clock ran ~9d slow at intake). § 1 block → v2.5; § 3 caption → v2.5 (caption had drifted, stuck at v2.2 — L063 class) + cells (SESSION_OPENER 1.8, LESSONS 1.2, STANDARDS_INDEX 2.5); § 6 history entry. Counts unchanged (78 lessons / 15 rules).
v2.4 — 2026-08-27 — Standard Set Version v2.4 (environment portability): template CLAUDE.md → 1.6 (Rule 2 Runner note — command examples are generic, substitute runner/CI flavor at run time, never localize suite-owned text; Rule 5 + § 8.6 neutralized). § 1 block → v2.4; § 3 cells (CLAUDE 1.6, STANDARDS_INDEX 2.4); § 6 history entry. Counts unchanged (78 lessons / 15 rules).
v2.3 — 2026-08-27 — Standard Set Version v2.3 (first adopter-originated lesson intake, under the new operator gate): lessons L069–L078 added to LESSONS.md (L069 the intake-gate incident; L070–L078 the nine rescued adopter lessons, genericized) + LESSONS ownership banner + SESSION_CLOSER § 1.7 binding where-codification-lands rule. § 1 block → v2.3 (counts → 78 lessons); § 2 row 9 → 78; § 3 caption → v2.3 + cells (LESSONS 1.1, SESSION_CLOSER 1.7, README 1.3, STANDARDS_INDEX 2.3) + lesson total → 78; § 6 history entry added. No rule change (the intake gate is a vault-side curator rule — Rule 16 in the vault's own contract; template rules stay 15).
v2.2 — 2026-08-19 — Standard Set Version v2.2 (domain-neutral scrub): 4 example paths carrying a real username (survived the v1.0 genericization; found by the v2.1 gate grep) scrubbed to `/Users/you/...` — MEMORY_PROTOCOL (3) + PROJECT_INSTRUCTIONS_TEMPLATE (1), both → 1.1. § 1 block → v2.2 (counts unchanged — 68 lessons / 15 rules); § 3 caption → v2.2 + cells (MEMORY_PROTOCOL 1.1, PROJECT_INSTRUCTIONS_TEMPLATE 1.1, STANDARDS_INDEX 2.2); § 6 history entry added. No rule or lesson content change.
v2.1 — 2026-08-18 — Standard Set Version v2.1 (first harvest → integrate cycle — adopter entry E001): SESSION_CLOSER § 1.2 Set-Version reference retargeted to docs/SET_VERSION_ADOPTED.md (adopters don't carry the INDEX) + lesson L068 (template cross-references must resolve in the adopter) + README stale LESSONS count fixed 48 → 68 (drifted since v1.4; L060-class sweep). § 1 block → v2.1 (lesson count → 68; files unchanged); § 2 row 9 → 68; § 3 caption → v2.1 + cells (SESSION_CLOSER 1.6, README 1.2, STANDARDS_INDEX 2.1; LESSONS cell unchanged per the no-per-lesson-bump practice) + lesson total → 68; § 6 history entry added. No rule change.
v2.0 — 2026-08-17 — Standard Set Version v2.0 (PLAN-009 skill delivery): SETUP.md + NEW_PROJECT_BOOTSTRAP.md + MEMORY_DURABILITY_ROLLOUT_PROMPT.md retired in favor of the vault-side live-reference delivery skill (skill/SKILL.md + skill/modes/ + scripts/bootstrap_skill.sh — vault machinery, never copied to adopters). § 1 block → v2.0 (counts unchanged — 15 rules / 67 lessons; total → 15 files = 11 binding + 4 meta); § 2 Tier 2 table pruned to README / STANDARDS_INDEX / HOW_TO_USE (+ STANDARDS_LOG) + delivery note added; § 3 caption → v2.0 + cells (README 1.1, HOW_TO_USE 1.1, STANDARDS_LOG 1.1, SESSION_OPENER 1.7, SESSION_CLOSER 1.5, STANDARDS_INDEX 2.0); § 4 delivery path rewritten (skill, concierge/self-service); § 5 unchanged (live-reference — no release-procedure step added); § 6 v2.0 history entry with the adopter-migration note.
v1.6 — 2026-08-16 — Standard Set Version v1.6 (PLAN-008 sync-enablement): TEMPLATE-ONLY marker convention + PROJECT-OWNED instance-heading blocks in the two session templates + § 14 stub-keep wording; the `sync` engine ships (Slice 5). § 1 block → v1.6 (counts unchanged — 15 rules / 67 lessons); § 3 caption → v1.6 + cells (CLAUDE.md 1.5, SESSION_OPENER 1.6, SESSION_CLOSER 1.4, SETUP 1.6, NEW_PROJECT_BOOTSTRAP 1.6, STANDARDS_INDEX 1.6); § 6 history entry added. No rule or lesson content change.
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
Standard Set Version: v2.8
Released:             2026-10-12
Baseline:             v2.7 (fleet-convergence intake — L080 feature intake, L081 cloud-synced folders) + lessons batch: L082–L088 (proof must be able to fail; prove first, generate and re-extract plan blocks; gates as their own step; engine as oracle; writes into another repository; shared folders; check before acting or telling) + L089 (a connection that opens is not a service that answers); CLAUDE.md § 15.8 senior-review checklist; template fixes (dangling Project Instructions references, Rule 12 alias, § 14 stub wording, Windows junction); PROMPT § 3.12 relayed guides; ENGINEERING § 2.7 shell safety; PROJECT § 8.10 publishing; the DECISION_LOG.md template.
Adopter contract:     11 binding files + 3 meta files (+ STANDARDS_LOG.md); 89 lessons (L001–L089); 15 standing rules in CLAUDE.md. Vault-only for now: the DECISION_LOG.md template (delivered to projects at a later Set Version).
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
| 9 | `LESSONS.md` | Incident-to-rule archive — 89 lessons (append-only), each with incident + cost + codification + cross-references |
| 10 | `SESSION_OPENER.md` | Session-start pre-flight (binding per Rule 9) — environment mapping + failure-mode catalog + first-response output template |
| 11 | `SESSION_CLOSER.md` | Session-end wrap-up (binding per Rule 12) — wrap-up routine + failure-mode catalog + output template |

### Tier 2 — Meta files (about the suite)

| # | File | Role |
|---|---|---|
| 1 | `README.md` | Entry point — overview, mental model, dispatcher reference, orientation |
| 2 | `STANDARDS_INDEX.md` | This file — versioned set manifest, per-file table, bump policy |
| 3 | `HOW_TO_USE.md` | Practical usage guide — supporting prompts (Day-One, code review, audit); delivery is the vault-side skill |
| + | `STANDARDS_LOG.md` | **Experiences-log template** — the per-project contribution channel; the delivery skill copies it to the project's `docs/STANDARDS_LOG.md` (an adopter artifact, not a binding rule) |
| + | `DECISION_LOG.md` | **Decision-log template** — one entry per operator decision, with the operator's verbatim answer; the vault keeps its own `docs/DECISION_LOG.md` from v2.8; delivery to projects comes with a later Set Version |

> **Delivery (not part of the set):** the suite is delivered by the vault-side skill
> (`skill/SKILL.md` + `skill/modes/` + `scripts/bootstrap_skill.sh`) — live-reference vault
> machinery, versioned in the vault's own manifest, never copied to adopters.

---

## 3. Per-file version table

Current state as of Set Version v2.8 (2026-10-12). Files unchanged since v1.0 keep their 2026-06-07 dates.

| File | Tier | Version | Last Updated |
|---|---|---|---|
| `CLAUDE.md` | Binding | 1.8 | 2026-10-12 |
| `PROJECT_STANDARDS.md` | Binding | 1.2 | 2026-10-12 |
| `PROMPT_STANDARDS.md` | Binding | 1.1 | 2026-10-12 |
| `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Binding | 1.1 | 2026-08-19 |
| `MEMORY_PROTOCOL.md` | Binding | 1.2 | 2026-10-12 |
| `ENGINEERING_STANDARDS.md` | Binding | 1.1 | 2026-10-12 |
| `VALIDATION_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `CICD_STANDARDS.md` | Binding | 1.1 | 2026-10-12 |
| `LESSONS.md` | Binding | 1.3 | 2026-10-12 |
| `SESSION_OPENER.md` | Binding | 1.9 | 2026-10-12 |
| `SESSION_CLOSER.md` | Binding | 1.8 | 2026-10-12 |
| `README.md` | Meta | 1.6 | 2026-10-12 |
| `STANDARDS_INDEX.md` | Meta | 2.8 | 2026-10-12 |
| `HOW_TO_USE.md` | Meta | 1.1 | 2026-08-17 |
| `STANDARDS_LOG.md` | Meta | 1.1 | 2026-08-17 |
| `DECISION_LOG.md` | Meta | 0.1 | 2026-10-12 |

**Total file count:** 16 (11 binding + 5 meta).
**Total lesson count in `LESSONS.md`:** 89 (L001–L089).

---

## 4. How to apply this set to a new project

The delivery path is the **standard-docset skill** (vault-side). **Concierge:** the curator runs
it against the target. **Self-service:** paste one of the launcher prompts from the vault's
README into a Claude Code session — Claude clones the vault into a named folder, checks that it
is a vault, and reads the skill from that clone; nothing is installed
(`bash scripts/bootstrap_skill.sh` remains an optional macOS / Linux convenience). Modes:
**bootstrap** (new projects), **adopt** (existing ones, dry-run gated) and **selftest** (a
throwaway practice run that proves the skill works on the machine). Every mode ends with a
handoff report for the curator.

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

### v2.8 — 2026-10-12 — Lessons batch, senior-review checklist, template fixes, decision-log template

Additive Minor, mostly authored by the curator. Lessons **L082–L088** consolidate about 25
recorded data points into seven lessons: a proof must be able to fail (positive controls); prove
the change first, then generate the plan's blocks and re-extract them; a gate is its own step and
checks content, not a commit id; engine as oracle; writes into another repository (explanations
accumulate, a landing is proven by the branch); a folder shared by several machines; check before
acting or telling. **L089** (adopter-originated, confirmed at the intake gate): a connection that
opens is not a service that answers. L080 gains an adopter data point (verify an environmental
premise before designing). **CLAUDE.md → 1.8:** § 15.8 gains the senior-review checklist; Rule 14
names the Windows form of the harness link (a directory junction) and forbids handling it by hand;
the dispatcher row for the Project Instructions template becomes a TEMPLATE-ONLY note — projects
never receive that file (an L068 recurrence; MEMORY_PROTOCOL → 1.2, PROMPT_STANDARDS and
CICD_STANDARDS → 1.1 reword the same reference); the Rule 12 alias text loses a leftover domain
identifier; § 1 and § 14 tell single-agent projects to keep a "NOT IN USE" stub, matching the
delivery skill. **PROMPT_STANDARDS** § 3.12 relayed prompts and step guides; **ENGINEERING_STANDARDS
→ 1.1** § 2.7 shell safety; **PROJECT_STANDARDS → 1.2** § 8.10 publishing a repository to a wider
audience; **SESSION_OPENER → 1.9** (§ 1.5 leftover-`memory/` line — adopter-originated, confirmed
at the intake gate; § 3.1 row 14 junction wording); **SESSION_CLOSER → 1.8** (junction wording).
New meta template **DECISION_LOG.md** (0.1): one entry per operator decision with the operator's
verbatim answer — the vault keeps its own log from this release; delivery to projects comes with a
later Set Version. § 4 self-service wording updated (launcher prompts, selftest mode, handoff
report). LESSONS → 1.3, which also covers L079–L081 (added at v2.6–v2.7 without a header bump).
Lesson count → 89; no rule change (15). Sync note: adopters receive a 10-item delta — CLAUDE.md,
SESSION_OPENER and SESSION_CLOSER merges; LESSONS, MEMORY_PROTOCOL, PROMPT_STANDARDS,
CICD_STANDARDS, ENGINEERING_STANDARDS and PROJECT_STANDARDS replaces; the SET_VERSION_ADOPTED
record — plus the handoff.

### v2.7 — 2026-10-03 — Fleet-convergence intake (feature intake + cloud-synced folders)

Additive Minor — intake from an operator adopter that had been running its own divergent copy of
the suite, gathered before that project converges onto the vault (intake-first: adoption replaces
its lessons archive, so novelties must reach the vault before it). Seven candidates were presented
at the intake gate; the operator confirmed four for integration and kept three as that project's
customizations. Lesson **L080** + CLAUDE.md **§ 15.9 Feature intake (before Phase 0)**: every new
feature and every feature document enters through four steps before any plan is drafted —
preserve the document unchanged as an idea source that binds nothing (adopt / deviate per item),
investigate the live source before designing, redesign from scratch per the repo's conventions,
then formalize as a § 15 plan; the § 15.2 Phase 0 row points to it. Landed in § 15 rather than as
a new standing rule so no rule number moves. Lesson **L081** + a **Rule 14** bullet for
cloud-synced folders: one machine at a time (a conflicted copy inside `.git/` is corruption), sync
settled on both sides before switching, folder pinned offline, `link` per machine, push when a
batch completes, gitignored is not sync-ignored, git identity set before a fresh clone's first
commit. Rule 12 step 6 retitled to match SESSION_CLOSER § 1.6 (drift since v1.5). CLAUDE.md → 1.7,
README → 1.5 (count). Lesson count → 81; no rule change (15). Sync note: adopters receive a
3-item delta (CLAUDE.md merge + LESSONS replace + SET_VERSION_ADOPTED record) plus the handoff.

### v2.6 — 2026-10-03 — Clock trust (the second harvested adopter entry)

Additive Minor — the second Set bump produced by the experiences-log loop, and the first from a
team adopter's log. The curator machine's clock had drifted ~9 days slow; the engine stamped
"today" from it, so a newly registered adopter's change logs read out of order, and the vault had
recorded the skew direction backwards. The adopter logged an `E0NN` entry; harvest surfaced it;
the operator confirmed it at the Rule 16 gate. Lesson **L079** (the machine clock is an untrusted
input — verify against an external authority before stamping or recording skew; merged with the
vault's own skew-record correction) + PROJECT_STANDARDS → 1.1 (**§ 5.6** — a new change-log line
must not be dated earlier than the line below it; verify the clock externally before stamping into
other repositories). README → 1.4 (count). Lesson count → 79; no rule change. The entry's engine
half (a trusted "today" / newest-stamp floor) is behavior-affecting and routed to its own plan.
Sync note: adopters receive a 3-item delta (PROJECT_STANDARDS replace + LESSONS replace +
SET_VERSION_ADOPTED record) plus the handoff.

### v2.5 — 2026-09-05 — Sync handoff (every engine write explains itself)

Additive Minor (PLAN-012). A target session opened to four engine-written uncommitted files it
did not make and had to reverse-engineer their provenance. Fix at the engine-write boundary
(L044's forcing-function-at-failure-granularity applied): **every engine write into a target** —
`sync --write` AND the `integrate --write` write-back — now also writes the engine-owned
transient **`docs/SYNC_HANDOFF.md`** into that target and flushes it with the changed files. The
handoff states project, operation, vault Set Version, run date (with a clock-trust caveat), the
`(file, mode)` list, and the six residual-bookkeeping steps (review diffs → manifest cells →
CHANGELOG entry → one landing commit that also deletes the handoff; never manifest-listed —
engine-transient, Rule 8 exempt by design; new lessons still land only as STANDARDS_LOG E0NN
entries). It is NOT a SYNC_MAP item — a converged target still reports up-to-date with a handoff
present. The reader side: SESSION_OPENER → 1.8 (§ 1.1 engine-handoff check — read the handoff
FIRST, land per its § 2, before any other work). Riding the release: LESSONS → 1.2 (L069–L078
date lines corrected — the vault machine's clock ran ~9 days slow at intake; real date
2026-09-05, stamped 2026-08-27; no lesson content change). Counts unchanged (78 lessons / 15
rules). Sync note: adopters receive a 3-item delta (SESSION_OPENER merge + LESSONS replace +
SET_VERSION_ADOPTED record) — plus `docs/SYNC_HANDOFF.md` itself appears with the write: land it
per its own § 2 and delete it in the landing commit.

### v2.4 — 2026-08-27 — Environment portability (the Runner note)

Additive Minor. A live team adopter — whose stack runs `python3`/`uv` and GitHub Actions —
adapted the contract's command examples in suite-owned text; every sync would have reverted the
adaptations (found by the same dry-run that surfaced the v2.3 intake). Root cause: the template
hard-coded one environment's invocations (`python`, `.gitlab-ci.yml`) in text adopters may not
edit. Fix: the contract's command examples are now declared **generic** — Rule 2 carries the
binding Runner note (substitute the project's Python runner / CI flavor at run time; NEVER
localize suite-owned text — project tooling facts belong in the § 1 PROJECT-OWNED context
block); the Rule 5 sentence and § 8.6 YAML one-liner are CI-flavor-neutral. Template CLAUDE.md →
1.6. No rule added or removed; counts unchanged (78 lessons / 15 standing rules). Sync note:
adopters receive a 2-item delta (CLAUDE.md merge + SET_VERSION_ADOPTED record); any existing
runner localizations in suite-owned text converge to the neutral wording — re-apply nothing,
just run commands with your own runner from now on.

### v2.3 — 2026-08-27 — First adopter-originated lesson intake (under the operator gate)

Additive Minor. A routine sync dry-run found nine well-formed, project-originated lessons
appended directly to an adopter's engine-owned `archive/LESSONS.md` (its STANDARDS_LOG empty —
the contribution channel bypassed silently; one `sync --write` from destruction). Rescued via
manual intake under the vault's new operator confirmation gate (each lesson listed, explained,
and individually confirmed before integration): **L070–L078** — uniqueness-key intent vs
attempt, unexercised config overrides, fan-out payload guarantees, reserved logging attributes,
side-effect transaction isolation, gitignore swallowing shipped files, scope-gaps-as-options,
per-child pool installation, date-relative fixture bounds. **L069** codifies the incident itself
plus its three-layer fix: the LESSONS ownership banner (visible at the point of temptation), the
SESSION_CLOSER § 1.7 binding where-codification-lands rule (E0NN entries ONLY), and the
vault-side intake gate. Counts → 78 lessons; template rules stay 15 (the gate is a curator rule
in the vault's own contract). Sync note: adopters receive LESSONS (replace), SESSION_CLOSER
(merge), and the SET_VERSION_ADOPTED record update — three files, no action required; the
banner + closer wording change future contribution behavior, not existing content.

### v2.2 — 2026-08-19 — Domain-neutral scrub (identifier-token class)

Additive Minor. Four example paths in the suite still carried a real username
that survived the v1.0 genericization — the identifier-token scrub gap
(usernames, SSH users, image names) the scrub-sweep discipline warns about. Found by the v2.1
release-gate grep; scrubbed to `/Users/you/...` (the registry-example convention):
MEMORY_PROTOCOL.md (3 sites) + PROJECT_INSTRUCTIONS_TEMPLATE.md (1 site), both → 1.1. Counts
unchanged (68 lessons / 15 rules); no rule or lesson content change. Sync note: MEMORY_PROTOCOL
is replace-class in the SYNC_MAP — adopters receive the fix at their next `sync`;
PROJECT_INSTRUCTIONS_TEMPLATE is vault-side only (not in the SYNC_MAP).

### v2.1 — 2026-08-18 — Adopter-reference fix (first harvest → integrate cycle)

Additive Minor — the first Set bump produced by the experiences-log loop end-to-end. The adopt-mode
pilot logged E001 (its instantiated SESSION_CLOSER § 1.2 pointed at the vault-side
`STANDARDS_INDEX.md`, which adopters don't carry), `harvest` surfaced it, `integrate` mapped it to
lesson **L068** (template cross-references must resolve in the adopter — SYNC_MAP items +
skill-created files only), and the template fix retargets § 1.2 to `docs/SET_VERSION_ADOPTED.md`
(present on both sides — the vault self-adopts). SESSION_CLOSER → 1.6; README → 1.2 (stale LESSONS
count swept 48 → 68, drifted since v1.4); lesson count → 68; no rule
change. The engine's Status write-back closes the adopter's entry
(`integrated → vault L068`). E001's suggested mechanized delivery-QA grep (template refs vs
SYNC_MAP + skill-created files) is deferred — recorded as an open candidate, not shipped here.

### v2.0 — 2026-08-17 — Skill delivery (machinery retired)

Structural Major (PLAN-009). The delivery machinery — `SETUP.md` (the one-shot bootstrap prompt),
`NEW_PROJECT_BOOTSTRAP.md` (the Day-Zero walkthrough), and `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`
(the Rule 14 retrofit prompt) — is retired from the set. Delivery is now the vault-side
**standard-docset skill** (`skill/SKILL.md` + `skill/modes/bootstrap.md` + `skill/modes/adopt.md`
+ the per-machine installer `scripts/bootstrap_skill.sh`): **live-reference** — the skill carries
no copy of the suite; it resolves the vault through its own symlink, self-pulls at step 0, and
reads `docs/standards/` directly at delivery time, so there is no bundle, no export script, and no
re-export release step (the L053 delivery-parity class is removed structurally, not managed).
Distribution is a plugin-free dual route: **concierge** (the curator runs the skill against the
target — team machines need nothing installed) and **self-service** (clone the vault repo, run the
installer once). Bootstrap mode covers new projects; adopt mode migrates existing ones (dry-run
gated, customization-preserving, performs the one-time v1.6 heading-wrap) and ships gated on a
real pilot adoption. No release-procedure step is added to § 5 — live-reference means the skill
needs no per-release refresh.

**No adopter action required** — the retired files were setup machinery that never survived in
adopters (the strip removed them), so no adopter footprint changes and `sync` is unaffected. New
deliveries use the skill; old-SETUP adopters just register + heading-wrap + sync.

### v1.6 — 2026-08-16 — Sync-enablement markers (PLAN-008: the `sync` engine ships)

Additive Minor. Marker/wording enablement only — no rule or lesson content change (counts stay
15 rules / 67 lessons). The two session templates gain a `TEMPLATE-ONLY` banner block (deleted at
instantiation; never propagated by sync) and a `PROJECT-OWNED` instance-heading block (so
section-merge sync preserves each adopter's own heading); the template `CLAUDE.md` § 14 marker
comment switches to stub-keep wording (single-agent adopters replace the § 14 body with a
"NOT IN USE" stub INSIDE the block — deleting the block would break sync's ordinal block matching);
`SETUP.md` + `NEW_PROJECT_BOOTSTRAP.md` instantiation wording updated to match (delete the
TEMPLATE-ONLY block, fill the heading block, keep every marker; § 3.1 stays suite-owned VERBATIM —
customizations go to § 3.2). The engine's `sync` command ships alongside (dry-run by default;
suite-owned files replaced whole, mixed files section-merged with PROJECT-OWNED blocks preserved,
`SET_VERSION_ADOPTED.md` mechanically updated). Adopters may stay on v1.5 — pre-v1.6 instances lack
the heading wrap and will count-mismatch on their FIRST sync, by design (loud, per-file, nothing
written): wrap once by hand or via adopt-mode, then sync forever.

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
