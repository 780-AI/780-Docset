<!-- VERSION: 1.5 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.5 — 2026-10-03 — Standard Set Version v2.7: LESSONS row count 79 → 81 (L001–L081; L080 feature intake, L081 cloud-synced folders).
v1.4 — 2026-10-03 — Standard Set Version v2.6: LESSONS row count 78 → 79 (L001–L079; L079 clock trust).
v1.3 — 2026-08-27 — Standard Set Version v2.3: LESSONS row count 68 → 78 (L001–L078; first adopter-originated intake batch).
v1.2 — 2026-08-18 — Standard Set Version v2.1: stale LESSONS row count in the file table fixed 48 → 68 (L001–L068) — had drifted since Set v1.4 (L060-class count sweep).
v1.1 — 2026-08-17 — Standard Set Version v2.0 (PLAN-009): the four delivery pointers retargeted
from the retired NEW_PROJECT_BOOTSTRAP.md to the vault-side standard-docset delivery skill
(STANDARDS_INDEX § 4); the § 4 walkthrough retained as orientation for the manual pattern.
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

# standards-source — Project Standards Repository

**A modular, portable set of standards for any new project.** Nine focused files covering operating rules, prompt-craft, governance, engineering substrate, validation framework, CI/CD architecture, memory hygiene, lessons learned, and Claude.ai project setup.

Distilled from production governance lessons. Every rule below has at least one incident behind it.

---

## Use-case quick reference

| If you want to... | Read this first |
|---|---|
| **Adopt these standards in a new project** | the standard-docset delivery skill (vault-side; `STANDARDS_INDEX.md` § 4) |
| **Find a ready-to-paste prompt for common workflows** | `HOW_TO_USE.md` (bootstrap, Day-One feature work, code review, prompt audit, quarterly audit, lesson backport) |
| Understand the overall architecture | § 2 (The 10-file modular suite) |
| See why this repo exists at all | § 1 (Mental model) and § 7 (Why this design) |
| Find out which file covers a specific topic | § 3 (Dispatcher table) |
| Update the standards (add a lesson, refine a rule) | § 5 (Maintenance protocol) |
| Check what placeholders need filling when adopting | § 6 (Customization checklist) |
| Backport a lesson learned on Project B to Project A | § 5.5 (Cross-project lesson propagation) |

If you're new to this repo: read the entire README top to bottom (~15 minutes). If you're returning: jump to the section you need from the table above.

---

## Table of Contents

1. [Mental model — what this repo solves](#1-mental-model--what-this-repo-solves)
2. [The 10-file modular suite](#2-the-10-file-modular-suite)
3. [Dispatcher pattern — which file when](#3-dispatcher-pattern--which-file-when)
4. [Adoption walkthrough](#4-adoption-walkthrough)
5. [Maintenance protocol — keeping the standards alive](#5-maintenance-protocol--keeping-the-standards-alive)
6. [Customization checklist — placeholders by file](#6-customization-checklist--placeholders-by-file)
7. [Why this design (architectural rationale)](#7-why-this-design-architectural-rationale)
8. [What this repo is NOT](#8-what-this-repo-is-not)
9. [Versioning and release discipline for the standards repo itself](#9-versioning-and-release-discipline-for-the-standards-repo-itself)
10. [Quick-start commands](#10-quick-start-commands)

---

## 1. Mental model — what this repo solves

Three problems compound silently in any project that doesn't address them deliberately:

### Problem 1 — Drift

Code, docs, and config diverge over months. Manifest entries go stale. CHANGELOG gaps appear. The source-of-truth doc lags behind the code it describes. After ~3 months, the project has high apparent organization but low actual coherence. New contributors learn the lies along with the truths because both look authoritative.

**This repo's answer:** governance discipline (mandatory same-commit sync, manifest completeness, pre-push verification scripts), codified across `PROJECT_STANDARDS.md` and enforced via the 9 standing rules in `CLAUDE.md`.

### Problem 2 — Re-litigation

Every project re-discovers the same engineering decisions: when to add a layer, how to handle secrets, what to log, how to fail safely, when to write tests. Without a captured set of defaults, each project's first month is spent re-litigating decisions that prior projects already paid for.

**This repo's answer:** captured defaults across `ENGINEERING_STANDARDS.md`, `VALIDATION_STANDARDS.md`, and `CICD_STANDARDS.md`, with the rationale preserved as lessons in `LESSONS.md`.

### Problem 3 — Lost recall on long documents

A single 1,500-line "bible" sounds comprehensive but performs badly. AI agents reading long documents have high recall on the first ~10% and last ~5%, and noticeably lower recall on the middle 70%. Rules buried at line 600 get inconsistently enforced. Human readers skim long preambles and miss what matters.

**This repo's answer:** modular files, each <1,000 lines, each topically coherent, loaded by a dispatcher (`CLAUDE.md` § 12) only when the work is in their topic. High recall preserved per file because each one is focused and short enough to be read attentively.

### Why every rule exists

This repo is a **distillation of pain**. Every rule below cost something — debugging time, lost commits, silent corruption — to learn. The full incident history lives in `archive/LESSONS.md`. When a future contributor proposes removing or relaxing a rule, the relevant lesson there is the evidence that has to be addressed, not just dismissed.

---

## 2. The 10-file modular suite

The standards repo itself lives **flat** (all 11 files at the repo root). Adopting projects nest these files under `docs/standards/` and `archive/` as part of their own folder discipline.

### Standards repo layout (this repo)

```
~/standards-source/
├── README.md ← this file
├── CLAUDE.md ← repo-root operating contract; the 9 standing rules + dispatcher
├── PROJECT_STANDARDS.md ← governance: workflow, manifest, CHANGELOG, sync, tracker
├── PROMPT_STANDARDS.md ← drafting prompts for AI agents (Cursor, Claude Code)
├── PROJECT_INSTRUCTIONS_TEMPLATE.md ← Claude.ai Project Instructions field template
├── MEMORY_PROTOCOL.md ← memory hygiene rules (what to memorize, what NOT to)
├── ENGINEERING_STANDARDS.md ← coding standards, architecture, secrets, ops
├── VALIDATION_STANDARDS.md ← test framework, tier model, ownership, deliberate-failure
├── CICD_STANDARDS.md ← pipeline architecture, deploy patterns, rollback
└── LESSONS.md ← incident-to-rule history (16 lessons, append-only)
```

Flat at 10 files because the overhead of subdirectories isn't worth it at this scale. Files are visible at a glance; `ls` shows the entire repo; copy operations are one-liners.

### Adopting project layout (when these files are copied into a project)

When you copy these files into a real project, they slot into the project's existing `docs/` discipline:

```
<your-project>/
├── CLAUDE.md ← from standards repo, customized
├── README.md ← your project's README (NOT the standards README)
├── CHANGELOG.md
├── docs/
│ ├── README.md
│ ├── documents_manifest.md
│ ├── folder_structure.md
│ ├── standards/ ← standards files copied here
│ │ ├── PROJECT_STANDARDS.md
│ │ ├── PROMPT_STANDARDS.md
│ │ ├── PROJECT_INSTRUCTIONS_TEMPLATE.md
│ │ ├── MEMORY_PROTOCOL.md
│ │ ├── ENGINEERING_STANDARDS.md
│ │ ├── VALIDATION_STANDARDS.md
│ │ └── CICD_STANDARDS.md
│ └── Plans/
└── archive/
 └── LESSONS.md ← from standards repo, copied here
```

The dispatcher table in `CLAUDE.md` § 12 references `docs/standards/` paths because it's pointing at the **adopting project's** structure, not the standards repo's. Two different places; same files.

### File summary

The suite is organized as **10 binding files** (core operating contract + 7 focused standards + lessons archive + session-start pre-flight) plus **4 meta files** (the README, set manifest, bootstrap walkthrough, and how-to-use guide).

**Binding files (the 10-file modular suite):**

| File | Audience | Purpose |
|---|---|---|
| `CLAUDE.md` | AI agents + humans | Binding contract: 12 rules incl. Rules 9 + 10 + 11 + 12 (session-start pre-flight + code-review-before-commit + QA-scenario-coupling + session-wrap-up), classification, workflow, validation checklist, dispatcher, plan workflow (§ 15), optional Codex handoff |
| `PROJECT_STANDARDS.md` | AI agents + humans | Governance specifics: manifest mechanics, CHANGELOG conventions, tracker structure, commit discipline |
| `PROMPT_STANDARDS.md` | AI agents + humans drafting prompts | Prompt-craft for Cursor / Claude Code: ALLOWLIST + verbatim FIND/REPLACE + verification + Codex handoff variant + retry-with-deviation-warning |
| `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Humans setting up Claude.ai | Three-tier template (static frame, project-specific, per-session) with optional Codex-aware sub-block |
| `MEMORY_PROTOCOL.md` | Humans + AI managing memory | What to memorize (Categories A & B), what NOT to (C & D), verify-before-recommending |
| `ENGINEERING_STANDARDS.md` | AI agents + humans writing code | Architecture invariants (incl. live-data settlement windows + time-window parsing pitfalls + refactor blast-radius), coding standards, secrets, container discipline, healthchecks, operator-machine ops |
| `VALIDATION_STANDARDS.md` | AI agents + humans writing tests | 7-tier test model, ownership map, deliberate-failure protocol, 24h soak, first-fire iteration expectations |
| `CICD_STANDARDS.md` | AI agents + humans touching pipelines | 6-stage pipeline shape, registry-pull deploy, smoke gating, auto-rollback, 24h soak gate, staging-mirrors-prod, explicit PROD authorization, REST-API status probing |
| `LESSONS.md` | Humans researching "why" | 81 lessons (L001–L081, append-only), each with incident + cost + codification |
| `SESSION_OPENER.md` | AI agents (loaded automatically per CLAUDE.md Rule 9) | Session-start pre-flight forcing function: canonical environment mapping + project failure-mode catalog + first-response output template (L043) |

**Meta files (about the suite, not part of the binding core):**

| File | Audience | Purpose |
|---|---|---|
| `README.md` | Humans (new adopters, contributors) | Entry point — overview, orientation, dispatcher |
| `STANDARDS_INDEX.md` | Humans + AI | Versioned set manifest: Standard Set Version + per-file version table + Set-Version-bump policy |
| `HOW_TO_USE.md` | Humans using the suite day-to-day | Practical usage guide: copy-paste bootstrap prompt + supporting prompts (Day-One feature work, code review, prompt audit, quarterly audit, lesson backport) + troubleshooting |

**Total: ~8,100+ lines across 14 files (10 binding + 4 meta).** No single file over ~1,400 lines, each topically coherent, each loaded by dispatcher pattern when its topic is in scope (except `SESSION_OPENER.md` which is loaded automatically at session start per `CLAUDE.md` Rule 9).

---

## 3. Dispatcher pattern — which file when

`CLAUDE.md` § 12 contains the canonical dispatcher table. Reproduced here for first-time orientation:

| When working on... | Load this file |
|---|---|
| Anything code (any `.py`/`.ts`/`.sh`) | `docs/standards/ENGINEERING_STANDARDS.md` |
| Architecture (modules, imports, layer boundaries) | `docs/standards/ENGINEERING_STANDARDS.md` |
| CI/CD (`.gitlab-ci.yml`, deploy scripts, release pipelines) | `docs/standards/CICD_STANDARDS.md` |
| Tests / validators / coverage / drift detection | `docs/standards/VALIDATION_STANDARDS.md` |
| Documentation (any `.md`, manifest, CHANGELOG, version headers) | `docs/standards/PROJECT_STANDARDS.md` |
| Drafting a multi-file AI agent prompt | `docs/standards/PROMPT_STANDARDS.md` |
| Memory hygiene (what to memorize, what NOT to) | `docs/standards/MEMORY_PROTOCOL.md` |
| Setting up Claude.ai Project Instructions for a new project | `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` |
| Researching a past decision or incident ("why does X exist?") | `archive/LESSONS.md` |

### How agents use the dispatcher

1. Agent reads `CLAUDE.md` (auto-loaded by Claude Code; referenced in Project Instructions for Claude.ai)
2. Agent identifies the work category from the first user message
3. Agent loads the relevant focused file via the dispatcher
4. Agent follows the rules in `CLAUDE.md` PLUS the rules in the loaded focused file

Result: high recall on every rule because the agent is reading <1,000 focused lines, not 6,000 mixed lines.

### How humans use the dispatcher

Same way. When making a change, identify the category and read the focused file's relevant section before implementing. The dispatcher is just navigation aid for a multi-file knowledge base.

---

## 4. Adoption walkthrough

This is the operational guide for adopting these standards in a new project. Four milestones: Day Zero, Day One, Week One, Month One.

> **Delivery note (Set v2.0):** bootstrap/adopt is performed by the vault-side standard-docset skill (`STANDARDS_INDEX.md` § 4). The walkthrough below is retained as orientation for the manual pattern.

### 4.1 Day Zero — bootstrap a new project

Before any feature work, set up the governance scaffold. Order matters. **The operational path is the delivery skill (bootstrap mode)** — the steps below are the orientation.

#### Step 1 — Create the repo and clone it locally

```bash
# Create on GitHub/GitLab, then:
git clone <repo-url>
cd <project-name>
```

#### Step 2 — Copy the standards files into the new repo

Two patterns:

**Pattern A — Copy (independent versions per project)**

The standards repo is flat; the adopting project nests. Two copy operations:

```bash
# 1. CLAUDE.md goes to repo root in the adopting project
cp ~/standards-source/CLAUDE.md ./CLAUDE.md

# 2. The 7 docs/standards/ files go under docs/standards/
mkdir -p docs/standards archive
cp ~/standards-source/PROJECT_STANDARDS.md \
 ~/standards-source/PROMPT_STANDARDS.md \
 ~/standards-source/PROJECT_INSTRUCTIONS_TEMPLATE.md \
 ~/standards-source/MEMORY_PROTOCOL.md \
 ~/standards-source/ENGINEERING_STANDARDS.md \
 ~/standards-source/VALIDATION_STANDARDS.md \
 ~/standards-source/CICD_STANDARDS.md \
 docs/standards/

# 3. LESSONS.md goes under archive/
cp ~/standards-source/LESSONS.md archive/LESSONS.md

# Note: README.md from the standards repo does NOT get copied — your project
# has its own README.md describing your project.
```

After this, the new project has its own copy in the standard nested layout. Updates to the standards repo do NOT auto-propagate; you decide when to backport. This is the recommended pattern — explicit propagation is safer than implicit drift.

**Pattern B — Symlink or submodule (shared versions across projects)**

Either git submodule or symlinks (`ln -s ~/standards-source/docs/standards docs/standards`). Gives you instant updates across all projects but couples them; a standards revision affects every project at once. Only use if you genuinely want lockstep evolution.

I recommend Pattern A for solo work, Pattern B only for organizations enforcing identical standards across many projects.

#### Step 3 — Customize the placeholders

Walk § 6 (Customization checklist) and replace every `<placeholder>` with project-specific values. Most are in CLAUDE.md (§ 1 project context, § 4 critical files) and PROJECT_INSTRUCTIONS_TEMPLATE.md (Tier B project-specific facts).

#### Step 4 — Create the supporting files

```bash
# At repo root
touch README.md CHANGELOG.md .gitignore

# Under docs/
mkdir -p docs/Plans
touch docs/README.md
touch docs/documents_manifest.md
touch docs/folder_structure.md
```

Initialize each with minimal scaffolding (use the templates and structures defined in PROJECT_STANDARDS.md §§ 2, 3, 5, 6).

#### Step 5 — Add the governance scripts

Copy or recreate:
- `scripts/check_doc_coverage.py` — surfaces drift across env vars, DB tables, API routes, manifest, folder structure
- `scripts/check_test_coverage_drift.py` — code↔test↔doc drift detector
- `scripts/doc_coverage_allowlist.toml` — empty starter
- `scripts/validation_ownership.toml` — starter with the project's known critical paths

These scripts come from a reference project. For a new project, port and adapt them.

#### Step 6 — Add the CI scaffold

Create `.gitlab-ci.yml` (or `.github/workflows/`) with at minimum a `governance` stage running both check scripts. Per `VALIDATION_STANDARDS.md` § 5 and `CICD_STANDARDS.md` § 2, the standard 6-stage shape is:

```
test → build → deploy → verify → deploy-prod → verify-prod
```

Build out as the project grows; start with `test → build` and add stages as the deploy story matures.

#### Step 7 — Add the MR/PR template

`.gitlab/merge_request_templates/Default.md` (or `.github/pull_request_template.md`) — required source-of-truth checklist. Forces every MR to account for which docs were updated.

#### Step 8 — First commit

```bash
git add -A
git status --short # Verify expected files (per CLAUDE.md Rule 6)
git commit -F /tmp/bootstrap_msg.txt
```

Commit message:

```
Project bootstrap: governance scaffold

Establishes the 9 standing rules (CLAUDE.md), document manifest scaffold,
CHANGELOG, governance scripts, CI placeholder, and standards files
(docs/standards/) before any feature work begins. No runtime code.

Standards files copied from ~/standards-source/ at <date> — independent
versions from this point forward. Backport explicitly when standards
repo evolves.
```

#### Step 9 — Set up the Claude.ai Project (if using Claude.ai)

1. Create a new Project in Claude.ai
2. Open Project Instructions field
3. Copy the template from `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` § 4 (the block inside the 4-backtick fence)
4. Fill in Tier A and Tier B; remove the Tier C HTML comment
5. Save

Done. Day Zero takes ~30-60 minutes including all customization.

### 4.2 Day One — first feature work using the standards

The first real change goes through the full workflow:

1. **Classify the change** per CLAUDE.md § 5 (Minor vs Major; Critical Files always Major)
2. **For Major changes:** propose the design first per CLAUDE.md § 6 step 2
3. **Implement** per the engineering substrate (`ENGINEERING_STANDARDS.md`)
4. **If it's a multi-file change:** draft the prompt per `PROMPT_STANDARDS.md` (ALLOWLIST + verbatim FIND/REPLACE + governance verification + checklist)
5. **Sync** all affected docs in the same commit per `PROJECT_STANDARDS.md` § 4 trigger table
6. **Validate** per CLAUDE.md § 8 checklist
7. **Add a CHANGELOG entry** with explicit impact statement
8. **Commit** via `git commit -F /tmp/<file>` per Rule 4

The first time through, this feels heavy. By the third change, it's reflex.

### 4.3 Week One — accumulating lessons

After the first ~5-10 commits, observed friction surfaces real lessons specific to the new project:

- A docker-compose substitution gotcha specific to the deployment shape
- A naming convention that doesn't fit the domain
- A specific environment variable that should have been documented sooner

These are project-specific lessons, not standards-repo lessons. Capture them in:

- `docs/<project>_setup_tracker.md` Incidents section (the local tracker)
- A new entry in the project's own CLAUDE.md if the lesson reaches "binding rule" significance

If the lesson is genuinely portable to other projects (not just this one), backport per § 5.5.

### 4.4 Month One — first audits

Quarterly audits should start at month one even if there's not much to audit yet — establish the rhythm.

#### Month-1 audit checklist

1. **Manifest sweep** — walk the filesystem, verify every committed `.md` and every VERSION-bearing code file appears in `docs/documents_manifest.md`. Per `PROJECT_STANDARDS.md` § 2.9.
2. **Lessons review** — open `archive/LESSONS.md` (or the project's own lessons file). For each lesson, check: is the rule still in force? Is the rationale still accurate? Have we accumulated new project-specific lessons that should be added?
3. **Memory hygiene** — open the Claude.ai memory store, walk the four-category test from `MEMORY_PROTOCOL.md` § 1. Delete Category C and Category D entries; move project-specific Category A entries to Project Instructions Tier B.
4. **CHANGELOG continuity check** — walk `git log` for the period; verify every meaningful commit has a CHANGELOG entry per `PROJECT_STANDARDS.md` § 3.
5. **Tracker review** — verify the tracker reflects current state (no rows stuck at "In progress" for >2 weeks; deferred items have current state and severity).

Fix anything broken. Celebrate that the discipline is paying off.

---

## 5. Maintenance protocol — keeping the standards alive

The standards repo itself follows the rules it codifies. Don't let it drift.

### 5.1 When to update which file

| Trigger | Update |
|---|---|
| New standing rule added (e.g., a 9th rule) | `CLAUDE.md` § 3 + `LESSONS.md` (the incident behind it) |
| Workflow procedure refined | `PROJECT_STANDARDS.md` § 1 |
| Manifest mechanics change | `PROJECT_STANDARDS.md` § 2 |
| New CHANGELOG convention | `PROJECT_STANDARDS.md` § 3 |
| New artifact-sync trigger | `PROJECT_STANDARDS.md` § 4 |
| New prompt-craft pattern | `PROMPT_STANDARDS.md` |
| Memory category redefined | `MEMORY_PROTOCOL.md` |
| New coding standard / architecture invariant | `ENGINEERING_STANDARDS.md` |
| New test tier / validation pattern | `VALIDATION_STANDARDS.md` |
| New pipeline pattern / deploy gotcha | `CICD_STANDARDS.md` |
| New incident codified into a rule | `LESSONS.md` (always) + the standards file the rule lives in |
| Project Instructions template evolution | `PROJECT_INSTRUCTIONS_TEMPLATE.md` |

### 5.2 Standards-repo's own VERSION discipline

Each standards file carries the same 4-block HTML header as project files (per `PROJECT_STANDARDS.md` § 5):

```markdown
<!-- VERSION: X.Y -->
<!-- Last Updated: YYYY-MM-DD -->
<!-- Source: ~/standards-source/<path> -->
<!--
CHANGE LOG
vX.Y — YYYY-MM-DD — <one-line summary>
-->
```

Bump rules:
- **Minor (X.Y → X.Y+1):** clarifications, typo fixes, example additions, anti-pattern additions, new lessons appended to LESSONS.md
- **Major (X.Y → X+1.0):** structural rewrites, new sections, removed sections, file split, file consolidation

### 5.3 Standards-repo's own CHANGELOG

`CHANGELOG.md` at the standards repo root tracks meaningful evolution of the standards themselves:

```markdown
## [2026-04-25] — Standards repo v1.0 release: initial 9-file modular suite
- **Type:** Major / Governance
- **Files:** All 9 standards files + README + LESSONS
- **Impact:** No project-runtime impact. Standards published for adoption in future projects.
- **Author:** Yaser / Claude
```

Per `PROJECT_STANDARDS.md` § 3 — newest entries at top, every entry has explicit impact statement.

### 5.4 Standards-repo's own manifest

The standards repo can have its own `docs/documents_manifest.md` listing the 10 files (9 standards + README). At only 10 files this may feel like overhead, but the discipline matters: if you don't track the standards repo, you'll forget when a file was added or its current version. The pattern scales — at 30+ files (when you add templates, examples, scripts), the manifest becomes essential.

### 5.5 Cross-project lesson propagation

Sometimes a lesson learned on Project B should backport to the standards repo (and from there, optionally to Project A's adopted copy of the standards).

#### Backport procedure

1. **Identify the lesson** in Project B — what specifically failed, what did the project change to prevent recurrence
2. **Determine portability** — is this specific to Project B's domain (don't backport) or genuinely cross-project (backport)
3. **Add the lesson to standards-repo `LESSONS.md`** with a new L-number (next available)
4. **Update the relevant standards file** with the new rule or anti-pattern
5. **Bump that file's VERSION** and add CHANGE LOG entry
6. **Add CHANGELOG entry** at standards-repo root
7. **Decide propagation to existing adopters:**
 - If urgent: notify each project to backport into their adopted copy
 - If non-urgent: each project picks up on next manual sync

The key insight: standards evolve. Lessons accumulate. The standards repo is the canonical source; per-project copies are snapshots that backport explicitly when the project owner decides.

### 5.6 Adding new files vs extending existing ones

Per `ENGINEERING_STANDARDS.md` § 1.3 — extend before adding. The 9-file architecture is the current shape; adding a 10th file is a Major change requiring explicit rationale. Most new patterns belong inside an existing file (a new section in `ENGINEERING_STANDARDS.md`, a new anti-pattern in `PROMPT_STANDARDS.md`, etc.), not a new file.

---

## 6. Customization checklist — placeholders by file

When adopting these standards in a new project, every `<placeholder>` and HTML-comment example must be reviewed and replaced. This checklist enumerates them by file.

### CLAUDE.md

- [ ] § 1 Project context — replace project name, domain, primary languages, deployment shape
- [ ] § 4 Critical files — list this project's actual always-Major paths; delete the example HTML comment or replace with project-specific list
- [ ] § 12 Dispatcher status note — once all 9 standards files exist in this repo, delete the status note OR mark all as ✅
- [ ] § 13 Sources of truth — update the "Domain behavior" row with the project's actual domain doc filename

### PROJECT_INSTRUCTIONS_TEMPLATE.md

- [ ] § 4 Tier A — replace `<PROJECT NAME>` and `<one-line domain description>` in the role line
- [ ] § 4 Tier B — fill in critical files, standard commands, environment specifics, domain-specific quirks
- [ ] § 4 Tier C — leave as comment (this section goes in first user message of each session, not in the field)
- [ ] § 8 Worked example — review and decide: keep as a reference, or replace with this project's actual filled-in example

### PROJECT_STANDARDS.md

- [ ] § 6 Standard folder layout — adjust if this project deviates from the canonical layout (most don't)
- [ ] § 9 Sources of truth table — update "Domain behavior" row with the project's actual domain doc

### PROMPT_STANDARDS.md

- [ ] § 14 Templates available — if you create the `PROMPT_TEMPLATES/` directory referenced here, populate or remove the references

### MEMORY_PROTOCOL.md

- [ ] § 8 Worked example — review the memory audit example; keep as reference or adapt

### ENGINEERING_STANDARDS.md

- [ ] § 1.1 Dependency direction — adjust the example layer diagram to match this project's actual layers
- [ ] § 1.6 Backtest vs live isolation — applies to trading/simulation projects; delete or replace if not relevant
- [ ] § 3.4 Configuration access pattern — adapt the the standards source-specific notes if needed
- [ ] § 7.4 Image source verification — adjust expected registry pattern to this project's registry
- [ ] § 9.3 Operator vs CI credentials — adapt the the standards source D8 example or delete if not yet relevant

### VALIDATION_STANDARDS.md

- [ ] § 2.5 Tier 5 smoke — adapt the example sections to this project's actual smoke checks
- [ ] § 4.1 Ownership file structure — fill in actual rules for this project's source files
- [ ] § 7.4 Examples — replace the standards source examples with this project's deliberate-failure tests as they accumulate

### CICD_STANDARDS.md

- [ ] § 2 Standard 6-stage shape — keep as-is or adapt if this project's pipeline diverges (most won't)
- [ ] § 4.2 Standard variable taxonomy — fill in this project's actual CI variable names
- [ ] § 4.4 Export-across-SSH gotcha — keep example as cautionary; replace with this project's actual deploy.sh excerpt if useful
- [ ] § 6.4 Authentication on the deploy host — adapt the standards source D8 example if applicable
- [ ] § 8.8 Telegram alert dependency — adapt or remove based on this project's alerting

### LESSONS.md

- [ ] All 16 lessons — keep as historical record (these are the standards source-specific incidents but the patterns are portable)
- [ ] As new lessons accumulate from THIS project: add at top with new L-number, follow the format in § 2

### Universal customization

- [ ] All file headers — `Source:` line points to the standards-repo location; if you copied into project repo, decide whether to update the Source line to reflect the local copy (recommended) or keep pointing back to standards-repo origin

---

## 7. Why this design (architectural rationale)

For each major design decision, the alternative considered and the reason this design won.

### Why 9 files instead of 1 bible?

**Considered:** single 1,500-line `PROJECT_STANDARDS.md` covering everything.

**Rejected because:** lost-in-the-middle problem. Rules buried at line ~600 are inconsistently enforced by AI agents. A single bible looks comprehensive but performs badly.

**This design:** 9 focused files, each <1,000 lines, dispatcher pattern routes agents to relevant files only. Per-file recall is high because each file is short and topically coherent.

### Why a dispatcher in CLAUDE.md instead of agents reading every file?

**Considered:** agents auto-load all 9 files on every interaction.

**Rejected because:** wastes context window; degrades attention; the rules in irrelevant files crowd out the rules that actually apply.

**This design:** CLAUDE.md is read every session (small, focused). The dispatcher table tells the agent which OTHER file to load based on the work in scope. Agent reads at most 2 files (CLAUDE.md + one focused file) for most interactions.

### Why HTML-comment examples instead of separate example files?

**Considered:** worked examples in `examples/` directory.

**Rejected because:** breaks the "everything you need is in one place" experience. Forcing a context switch to a separate file for an example reduces actual usage of examples.

**This design:** the standards source examples live in HTML comments inside the file's relevant section. Invisible in rendered preview (don't bloat the prose), visible to anyone editing the source (concrete reference where it's needed).

### Why append-only LESSONS.md instead of a wiki?

**Considered:** lessons in a wiki or docs site that can be edited freely.

**Rejected because:** the rationale behind a rule is part of the rule's defensibility. If the lesson can be casually rewritten, future contributors lose the ability to challenge a removal proposal with the original incident context.

**This design:** LESSONS.md is append-only. Lessons get permanent L-numbers. Even if a rule is later relaxed or removed, the original lesson stays as evidence. New lessons add at top (newest first) but old ones never get removed.

### Why HTML headers (VERSION, Last Updated, CHANGE LOG) on `.md` files?

**Considered:** YAML frontmatter, separate `__metadata__` files, or no metadata at all.

**Rejected because:** YAML frontmatter renders as visible noise in some markdown previewers. Separate files violate "everything in one place." No metadata loses the version trail entirely.

**This design:** HTML comments are invisible in rendered preview but parseable by governance scripts and visible to source editors. Best of all worlds.

### Why two separate places for "rules" (CLAUDE.md) and "details" (focused files)?

**Considered:** all rules in CLAUDE.md.

**Rejected because:** CLAUDE.md would balloon past the lost-in-the-middle threshold. Binding rules deserve high-visibility placement; topical details belong with their topic.

**This design:** CLAUDE.md holds the binding contract (8 rules, classification, workflow, validation checklist). Focused files hold the procedural detail. The rule "use deliberate-failure testing for new alert code" is in CLAUDE.md § 8.4 (one line); the full deliberate-failure protocol is in `VALIDATION_STANDARDS.md` § 7 (a section).

### Why is the standards repo separate from individual projects?

**Considered:** every project maintains its own `CLAUDE.md` with no shared source.

**Rejected because:** lessons learned on Project B can't propagate to Project A. Every project re-discovers the same patterns from scratch. The lost-in-the-middle problem and the re-litigation problem (both from § 1) re-occur per project.

**This design:** standards repo is the canonical source. Projects copy or symlink standards files into their own repos. Cross-project lesson propagation per § 5.5 keeps the canonical source evolving while project copies remain stable until explicitly synced.

---

## 8. What this repo is NOT

A few clarifications about scope:

### Not a project skeleton

This repo provides **standards**, not application code, framework boilerplate, or starter templates. It tells you how to organize, govern, and validate a project; it doesn't tell you how to build a web app, a CLI tool, or a data pipeline.

### Not a code style guide

`ENGINEERING_STANDARDS.md` § 2 covers naming, type hints, function size, imports — but at the level of "use snake_case for files," not "indent with 4 spaces." For language-specific style, use language-native tools (Black, Prettier, Rustfmt, etc.).

### Not a replacement for documentation

The standards repo doesn't document YOUR project. It documents how to document any project (`PROJECT_STANDARDS.md` § 5-6) and what the document conventions are. You still write `README.md`, API references, runbooks, etc. for your specific project.

### Not opinionated about tech stack

The patterns in this repo work for Python, TypeScript, Rust, Go, Bash. The CI examples use GitLab CI but the patterns translate to GitHub Actions. The Docker discipline applies whether you deploy to Kubernetes, Docker Swarm, ECS, or a single VPS. The principles are tech-agnostic.

### Not a one-time read

These files are reference material, loaded on demand. Read the README once for orientation. Read CLAUDE.md once to internalize the 8 rules. Read each focused file the first time you do work in its category. Re-reference as needed.

---

## 9. Versioning and release discipline for the standards repo itself

The standards repo is a project too. It follows its own rules.

### 9.1 Versioning

**Two layers of versioning** govern the standards suite:

1. **Per-file versions** — each standards file carries its own VERSION header (in HTML comment at top) and bumps independently when its content changes. Bump rules: Minor for clarifications / additions; Major for structural rewrites or breaking changes. See `PROJECT_STANDARDS.md` § 5 for the version-header template.

2. **Standard Set Version** — the suite as a whole carries a coarser-grained version representing the baseline maturity of the entire set. The canonical location is `STANDARDS_INDEX.md`. The first Set Version is **v1.0** (initial 9-file suite, released 2026-04-25; refreshed with Phase 4–7 lessons 2026-05-16, still within v1.0 because the structural shape didn't change).

**When to bump the Set Version:**

- **Minor (v1.0 → v1.1):** new lessons codified, new sub-sections added, anti-patterns expanded — anything additive that doesn't change the file count or break adopters
- **Major (v1.0 → v2.0):** structural changes — new binding file added, an existing binding file split or merged, dispatcher table reorganized, breaking renames in critical files

Adopters track the Set Version they adopted at; backporting Minor updates is optional and explicit; Major updates require a documented migration in the set's CHANGELOG.

### 9.2 Release notes

When tagging a new release, write release notes summarizing:
- Which standards files changed (and from which version to which)
- What lessons were added
- Any new anti-patterns codified
- Any breaking changes to existing rules (rare; handle as Major bumps)

Release notes go in the standards-repo CHANGELOG.md and the git tag annotation.

### 9.3 Deprecation policy

If a rule is removed:
- Document the removal in CHANGELOG.md with explicit rationale
- Move the rule's text to LESSONS.md as an addendum to the original incident lesson — "Rule was relaxed/removed on YYYY-MM-DD because <reason>"
- Bump the affected standards file Major version (X.Y → X+1.0)

Never silently delete a rule. The history must remain reconstructible.

### 9.4 Breaking changes

A breaking change is one that adopting projects need to actively respond to (e.g., renaming `_gpt_context_manifest.md` → `documents_manifest.md`).

Procedure:
1. Document the breaking change clearly in CHANGELOG.md
2. Bump affected files to a new Major version
3. Provide a migration note in CHANGELOG.md ("To adopt this version: rename X to Y in your project")
4. Tag the repo with a new minor or major release that bundles the change

---

## 10. Quick-start commands

### First-time read of this repo

```bash
# Read the README (you are here)
less README.md

# Read CLAUDE.md (the binding contract)
less CLAUDE.md

# Skim the 7 focused standards files in any order
for f in PROJECT_STANDARDS.md PROMPT_STANDARDS.md PROJECT_INSTRUCTIONS_TEMPLATE.md \
 MEMORY_PROTOCOL.md ENGINEERING_STANDARDS.md VALIDATION_STANDARDS.md \
 CICD_STANDARDS.md; do
 echo "=== $f ==="
 less "$f"
done

# Read the lessons archive
less LESSONS.md
```

### Adopt for a new project

```bash
NEW_PROJECT=~/projects/my-new-project
mkdir -p "$NEW_PROJECT"
cd "$NEW_PROJECT"
git init

# Copy CLAUDE.md to repo root
cp ~/standards-source/CLAUDE.md ./

# Create the docs/standards/ folder and copy the 7 standards files
mkdir -p docs/standards docs/Plans archive
cp ~/standards-source/PROJECT_STANDARDS.md \
 ~/standards-source/PROMPT_STANDARDS.md \
 ~/standards-source/PROJECT_INSTRUCTIONS_TEMPLATE.md \
 ~/standards-source/MEMORY_PROTOCOL.md \
 ~/standards-source/ENGINEERING_STANDARDS.md \
 ~/standards-source/VALIDATION_STANDARDS.md \
 ~/standards-source/CICD_STANDARDS.md \
 docs/standards/

# Copy LESSONS.md to archive/
cp ~/standards-source/LESSONS.md archive/

# Create supporting files (these are project-specific, not from standards repo)
touch README.md CHANGELOG.md .gitignore
touch docs/README.md docs/documents_manifest.md docs/folder_structure.md
touch docs/Plans/.gitkeep

# Walk § 6 customization checklist; replace placeholders
# Then first commit per § 4.1 step 8
```

### Maintain the standards repo

```bash
cd ~/standards-source

# Add a new lesson (e.g., learned on Project B)
# 1. Open archive/LESSONS.md, add new lesson at top of § 3 with next L-number
# 2. Update relevant standards file with the new rule or anti-pattern
# 3. Bump that file's VERSION header + CHANGE LOG entry
# 4. Bump archive/LESSONS.md VERSION header + CHANGE LOG entry
# 5. Update CHANGELOG.md at root
# 6. Commit per CLAUDE.md Rule 4 (-F /tmp/<file>)

# Verify state before pushing
git status --short # Per CLAUDE.md Rule 6
git diff --stat
```

---

## End of README

This repo is a starting point, not a destination. Every project adopting these standards will discover patterns specific to its domain. Capture those patterns in the project's own tracker and lessons file. Backport portable ones to this repo per § 5.5 so the next project starts from a richer baseline.

The standards exist to slow down the right things and speed up the rest. Spend the 30 minutes reading. Spend the 60 minutes setting up. The payback is the next 6 months of friction you don't have.
