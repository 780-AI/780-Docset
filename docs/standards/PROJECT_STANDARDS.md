<!-- VERSION: 1.4 -->
<!-- Last Updated: 2026-05-22 -->
<!-- Source: ~/everon-standards/PROJECT_STANDARDS.md (template). Domain-neutral. EverOn examples in HTML comments. -->
<!--
CHANGE LOG
v1.4 — 2026-05-22 — Set Version v2.1 fix-forward: bring stale body-text references current. Two non-history occurrences updated: § 6 standard-folder-layout ASCII tree comment "The 8 standing rules + project specifics" → "The 9 standing rules + project specifics" (Rule 9 added in v2.1); § 9 sources-of-truth table row "The 8 standing rules" → "The 9 standing rules". No structural changes.
v1.3 — 2026-05-22 — EverOn.Equinex PLAN-001 § 11 fix-forward codification (L036). § 4 artifact sync trigger table: new row for "Phase 3 commit ships a mitigation for a risk documented in an earlier plan's § 11" → "annotate the earlier plan's risk row CLOSED in the SAME commit (status + closing commit hash + one-line reason)." NEW § 4.3 Closed-risk annotation discipline — full sub-section with annotation format, anti-pattern, fix-forward recovery shape, EverOn.Equinex PLAN-001 § 11 example in HTML comment.
v1.2 — 2026-05-16 — Phase 4–7 + EA-test-soak refresh. § 1 Step 5 Validate: code-review item added (L027). § 7 Tracker files: NEW § 7.7 Tracker ownership for multi-agent projects (OPTIONAL — cross-references CLAUDE.md § 14; L020 codification). § 8 Commit discipline: § 8.4 split-commit refined with L029 (distribute doc sync across commits, don't concentrate at "final sync"). New § 8.7 Code review before staging (L027), § 8.8 Agent runs commits end-to-end (L026), § 8.9 Push cadence — batch local commits (L028). § 10 Anti-patterns: added § 10.9 push-after-every-commit, § 10.10 concentrating doc-sync in final commit, § 10.11 skipping code review.
v1.1 — 2026-04-25 — Standards repo restructured to flat layout — Source path updated. The standards repo itself now lives flat (10 files at root); adopting projects still nest under `docs/standards/`.
v1.0 — 2026-04-25 — Initial release. Governance bible covering 5-step workflow, document manifest mechanics, CHANGELOG conventions, artifact sync triggers, tracker file structure, and document conventions. Distilled from EverOn.Capital-Signal Phases 1-3 governance evolution.
-->

# PROJECT_STANDARDS.md — Governance Reference

**Scope:** This document is the working reference for project governance — how changes flow through the system, how documents stay aligned with code, how the manifest and CHANGELOG are maintained, and how trackers organize multi-phase work. It is loaded when the work involves documentation, manifest updates, CHANGELOG entries, or tracker bookkeeping.

The binding rules in `CLAUDE.md` always apply; this file is the dispatcher target for governance specifics — the *how* behind the *what* that CLAUDE.md establishes.

**Why this file exists:** Governance is the mechanical discipline that keeps code, docs, and config aligned. Without it, drift accumulates silently — manifest entries go stale, CHANGELOG gaps appear, source-of-truth docs lag behind the code they describe. After ~3 months, the project has high apparent organization but low actual coherence. Every rule in this file exists because that drift was observed at least once on EverOn.Capital-Signal Phases 1-3.

---

## Table of Contents

1. [The 5-step change workflow (full detail)](#1-the-5-step-change-workflow-full-detail)
2. [Document manifest — structure and mechanics](#2-document-manifest--structure-and-mechanics)
3. [CHANGELOG conventions](#3-changelog-conventions)
4. [Artifact sync — full trigger table](#4-artifact-sync--full-trigger-table)
5. [Document version headers](#5-document-version-headers)
6. [Standard folder layout](#6-standard-folder-layout)
7. [Tracker files — phase and task management](#7-tracker-files--phase-and-task-management)
8. [Commit discipline (full detail)](#8-commit-discipline-full-detail)
9. [Sources of truth — single canonical authority per topic](#9-sources-of-truth--single-canonical-authority-per-topic)
10. [Anti-patterns to refuse](#10-anti-patterns-to-refuse)

---

## 1. The 5-step change workflow (full detail)

`CLAUDE.md` § 6 names the five steps; this section provides the full procedural detail for each.

### Step 1 — Analyze (mandatory always)

Before writing any code or doc edit:

- **Read `docs/folder_structure.md`** for placement and naming conventions. New files go where the structure says they go, not where convenience suggests.
- **Read the source-of-truth doc** for the domain or layer being touched (e.g., `docs/business_logic.md` for trading behavior changes; `docs/api_reference.md` for interface changes).
- **Search for existing implementations** — `grep`, `git log -S`, code search. Prefer reuse over new code. The pattern you're about to add probably exists somewhere already.
- **If the change conflicts with documented architecture**, do not silently implement. Propose an update to the architecture doc first; implement only after the proposal is reviewed.

Output of this step: a clear understanding of context, constraints, and existing patterns. For Minor changes, this is mostly mental. For Major changes, write it down — that document becomes the input to Step 2.

### Step 2 — Design (Major mandatory; Minor optional)

For Major changes, define explicitly before any implementation:

- **Purpose** — what problem does this solve? In one sentence.
- **Acceptance criteria** — how do we know it worked? Bullet list of specific, testable conditions.
- **Files / modules to touch** — full list. No surprises later. If you discover a new file needs to be touched mid-implementation, that's a signal to revisit the design.
- **Dependencies** — what does this depend on (libraries, other modules, infrastructure)? What depends on this?
- **Data flow** — for changes touching how data moves through the system, sketch it.
- **Integration points** — what other modules call this code? What does this code call?
- **Risk** — what could go wrong? What's the failure mode?
- **Rollback** — if this lands and breaks something, how do we revert? (For pushed commits: per Rule 3, we fix-forward, not roll back. But the design should still consider what "fix-forward" looks like for this change.)

For complex Major changes, write the design as a markdown doc in `docs/Plans/` first, get it reviewed, **then** implement. Per CLAUDE.md Rule 1: plans are committed.

For simple Major changes (one focused file change with clear acceptance), the design can be a paragraph in the prompt or in a comment. The form is less important than the discipline of explicitly stating purpose + acceptance + files + risk before coding.

### Step 3 — Implement (mandatory)

- Follow the architecture documented in `docs/system_architecture.md` and the layer boundaries in `docs/folder_structure.md`.
- Follow coding standards from `docs/standards/ENGINEERING_STANDARDS.md` (when that file exists).
- **No temporary hacks in production paths.** If a hack is genuinely needed for time pressure, file it as a Deferred Item in the tracker (§ 7.3) with severity. Don't leave silent technical debt.
- Bump VERSION headers and add CHANGE LOG lines as you touch files (§ 5 and `CLAUDE.md` § 7).

### Step 4 — Sync (mandatory; scope varies)

Walk the artifact sync trigger table (§ 4 of this file) and update everything in scope. Sync happens **in the same commit** as the implementation, not later. Drift between code and docs is a defect, not a future cleanup task.

For Major changes, the sync set is typically 4-7 files (code file + manifest + CHANGELOG + at least one source-of-truth doc + the tracker if applicable). For Minor changes, often 2-3 (code file + manifest + CHANGELOG).

### Step 5 — Validate (mandatory)

Walk the validation checklist in `CLAUDE.md` § 8. The full checklist is reproduced there because validation is too important to defer to a separate file. Key gates:

- All `.py`/`.sh` touched files have VERSION bump + CHANGE LOG line
- Manifest updated for any version change or new file
- CHANGELOG entry added with explicit impact statement
- **Code review pass on all modified/new files BEFORE `git add`** (per `archive/LESSONS.md` L027 — separate quality gate from governance scripts; see § 8.7 below for procedural detail)
- Pre-push governance scripts both exit 0
- For new alerting/check code: deliberate-failure test was run (`archive/LESSONS.md` L009)

### Response shape (when reporting completed work)

Per `CLAUDE.md` § 6, every "I'm done" report uses these labelled sections in this order:

1. **Analysis** — what was the situation
2. **Plan / Design** (if Major) — what was decided
3. **Implementation** — what was actually changed
4. **Documentation / config updates** — which docs got touched
5. **Version bumps** — every `.py`/`.sh` and tracked-doc version that moved
6. **Changelog / impact statement** — explicit "no runtime impact" or "yes, behavior X changes"

---

## 2. Document manifest — structure and mechanics

The manifest (`docs/documents_manifest.md`) is the **first place** any AI agent or contributor looks to find the current state of the repo. It is the version index for every committed `.md` file and every VERSION-bearing code file.

### 2.1 File structure

```markdown
<!-- VERSION: <doc-version> -->
# Document & Code Manifest

## Module Quick Index

| Module / Section | Entry range |
|---|---|
| Core engine | 1-12 |
| Configuration | 13-25 |
| ... | ... |
| Governance (rules + registries) | 165-171 |

## Manifest Table

| # | Title | Version | Category | Path |
|---|---|---|---|---|
| 1 | <Title> | <version> | <Category> | `<path>` |
| 2 | <Title> | <version> | <Category> | `<path>` |
| ... | ... | ... | ... | ... |

## Last Updated

- **Date**: YYYY-MM-DD
- **Change**: <one-paragraph summary of the most recent change to the manifest>
- **Previous change**: <one-paragraph summary of the prior change>
- **Previous audit**: <one-paragraph summary of the most recent full audit>
```

### 2.2 Module Quick Index

The Quick Index sits at the top of the manifest and groups entries into modules. Update only when entry ranges shift (e.g., after a manifest sweep adds entries that push a category's range forward).

### 2.3 Manifest Table — entry rules

Each row has 5 cells:

- **#** — entry number, monotonically increasing. **Never reused after deletion.** When a tracked file is deleted, the row is removed but the number is not re-issued to a new entry.
- **Title** — human-readable title (e.g., "Pattern Engine", "CI/CD Reference")
- **Version** — current VERSION header value for code files (e.g., `v3.4`); `-` for `.md` docs that don't carry a VERSION
- **Category** — broad classification (Core, Config, Charting, Infrastructure, Docs, Trackers, Plans, Governance, etc.)
- **Path** — exact path from repo root, in backticks

### 2.4 What gets tracked

Per CLAUDE.md Rule 8:
- **Every** committed `.md` file
- **Every** tracked code file with a VERSION header (`.py` or `.sh`)

### 2.5 What does NOT get tracked

- `.cursor/rules/*.md` (tooling configuration, not repo documentation)
- `.venv/`, `node_modules/`, anything gitignored
- `archive/` (historical materials)

No exclusion lists are maintained. Unused files must be **removed**, not allowlisted.

### 2.6 Last Updated block — rotation rules

The Last Updated block has 4 fields. On each rotation:

1. Current `Change` content moves to `Previous change`.
2. Prior `Previous change` drops off entirely.
3. `Previous audit` is **independent** — it only changes when a full manifest audit (sweep) happens, not on per-edit rotations.
4. New `Date` and `Change` reflect the current commit.

Always exactly **one** Date, **one** Change, **one** Previous change, **one** Previous audit. Never two of any.

<!--
Example rotation (EverOn Task 3.5 commit, 2026-04-25):

BEFORE rotation:
- **Date**: 2026-04-24
- **Change**: Phase 3 Task 3.2 close-out — tracker updated...
- **Previous change**: 2026-04-24 — Phase 3 Task 3.2b — entry #172 bumped...
- **Previous audit**: 2026-04-21 — Full manifest audit — added 51 untracked...

AFTER rotation:
- **Date**: 2026-04-25
- **Change**: Phase 3 Task 3.5 — entry #116 bumped v0.1 → v0.2...
- **Previous change**: 2026-04-24 — Phase 3 Task 3.2 close-out — tracker updated...
- **Previous audit**: 2026-04-21 — Full manifest audit — added 51 untracked...

The "Phase 3 Task 3.2b" Previous-change entry dropped off. Previous audit untouched.
-->

### 2.7 When to update the manifest

| Trigger | Manifest action |
|---|---|
| Tracked file's VERSION header bumped | Update version cell in the file's row + rotate Last Updated block |
| New `.md` file or new VERSION-bearing code file added | Add a new row + rotate Last Updated block |
| Tracked file deleted | Remove the row + rotate Last Updated block |
| Module Quick Index range shifts | Update Quick Index + rotate Last Updated block |

All of these happen **in the same commit** as the underlying change. Per CLAUDE.md Rule 8.

### 2.8 What the manifest is NOT

- **Not a diff log** — that's `CHANGELOG.md`
- **Not a roadmap** — that's a tracker file
- **Not an ownership map** — that's `scripts/validation_ownership.toml` (when applicable)

The manifest is **only** the version index. Stay narrow.

### 2.9 Manifest audit (full sweep)

Quarterly (or after detecting drift):

1. Walk the filesystem: every `.md` file under `docs/`, `archive/`, root; every `.py`/`.sh` file with a VERSION header (use `grep -r '^# VERSION:' .`)
2. Compare against the manifest entries
3. For each filesystem file not in manifest: add a row
4. For each manifest entry pointing at a non-existent file: remove the row
5. For each manifest entry whose VERSION cell doesn't match the file's actual VERSION: update the cell
6. Update the Module Quick Index ranges
7. Update Last Updated → "Previous audit" gets the current date and a summary

This is a Major change. Goes through the full workflow. Lands as one commit (or a split commit per § 8).

---

## 3. CHANGELOG conventions

`CHANGELOG.md` lives at the repo root. **Newest entries at the top.** Append after every meaningful commit.

### 3.1 Entry format

```markdown
## [YYYY-MM-DD] — <Title — phase/task or what shipped>
- **Type:** <Major | Minor> / <Category> [/ <Sub-category>]
- **Files:** `<path/to/file1>` (what changed in plain language), `<path/to/file2>`, ...
- **Impact:** <Explicit statement of runtime/behavior/test impact. Always state "No runtime impact" if true. If runtime IS affected, describe what changes and how to verify.>
- **Author:** <Person> [/ <AI co-author if any>]
```

### 3.2 Categories

Use one or more, slash-separated:

- Domain Logic / Trading Logic / Business Logic
- Database / Schema
- Config / Parameters
- Architecture
- API / Interface
- Infrastructure / CI/CD
- Docs / Governance
- Testing / Validation

### 3.3 The mandatory impact statement

Every entry **must** state runtime/behavior impact explicitly. Phrasing options:

- "No runtime impact. No backtest impact. Documentation-only."
- "No trading logic impact; affects deployment workflow only."
- "Behavior change: X now does Y instead of Z. Backtest results affected — re-run validation suite."
- "Schema change: new column `foo` on table `bar`. Existing rows backfilled with default. Migration `007` included."

Never omit. Future contributors searching git history for "did this change break anything" rely on this field.

### 3.4 What goes IN

- New features, refactors, doc rewrites
- Schema changes, config changes
- CI/CD pipeline changes
- Bug fixes that change behavior
- Governance / standing rule additions
- Tracker bookkeeping (judgment call — only if the bookkeeping change matters across sessions)

### 3.5 What stays OUT

- Pure typo fixes
- Whitespace-only commits
- Auto-generated lockfile bumps (unless they bump major versions of dependencies)
- "WIP" or rollback commits within a single session

### 3.6 Order — newest at top

Latest entry sits immediately under the file's preamble. Prior entries flow down chronologically. Don't reorder past entries — chronological position is part of the historical record.

### 3.7 Files field — list what matters

The Files field doesn't have to list every file touched in the commit (`git show` can do that). It lists the **significant** files — the source-of-truth files, the entry points, the docs that downstream readers will care about. Brief description after each in parentheses.

<!--
Example entry (EverOn Phase 3 Task 3.5, 2026-04-25):

## [2026-04-25] — Phase 3 Task 3.5: remove redundant `validate` job from `.gitlab-ci.yml`
- **Type:** Major / Infrastructure
- **Files:** `.gitlab-ci.yml` (deleted `validate:` job + preceding comment), `docs/ci_cd.md` (v0.1 → v0.2; Status date rotated; 3 references to removed job deleted in § 2, § 3, § 11), `docs/cicd_setup_tracker.md` (Phase 3 Status block rotated; Task 3.5 row marked Complete; close-out incident block appended), `docs/documents_manifest.md` (entry #116 v0.1 → v0.2; Last Updated block rotated), `CHANGELOG.md`
- **Impact:** No trading logic impact. No backtest impact. No live-system impact (the deleted job ran tests in CI only and was `allow_failure: true` — its absence affects neither staging nor production runtime). Removes the legacy `validate:` job from the master-push pipeline. The job ran `validation.validate_eurusd` and `validation.validate_us30` with `allow_failure: true` and no seeded DB, so both validators failed every run silently — zero coverage value. The same two validators are exercised by the nightly job's `scheduled` tier with proper DB seeding. Closes Phase 3 Task 3.5; only Task 3.4 remains.
- **Author:** Yaser / Claude
-->

---

## 4. Artifact sync — full trigger table

After implementing any change, walk this table top to bottom. For each trigger that applies, update everything in the right column **in the same commit**.

| Trigger | Document(s) to update |
|---|---|
| Any `.py` or `.sh` file edited | The file's VERSION header + CHANGE LOG line |
| Any tracked file's VERSION header bumped | `docs/documents_manifest.md` (version cell + Last Updated rotation) |
| New file created (any kind) | `docs/folder_structure.md` |
| New `.md` doc under `docs/` | `docs/README.md` index + manifest row |
| New planning doc | Created under `docs/Plans/` (NOT elsewhere); index entry in `docs/README.md` § Internal Reference |
| Public function/class signature changed | `docs/api_reference.md` |
| New env var or config key | `docs/config_reference.md` |
| DB table created / altered / renamed | `docs/database_schema.md` |
| Operational procedure changed (deploy, rollback, etc.) | `docs/runbook.md` and/or `docs/docker.md` |
| Architecture changed (new module, new tier, data flow change) | `docs/system_diagram.md` + `docs/system_architecture.md` |
| Domain logic / business rules changed | The domain doc (e.g., `docs/business_logic.md`) — IN THE SAME COMMIT |
| CI/CD pipeline changed | `docs/ci_cd.md` + same-commit verification by real pipeline run |
| Any meaningful change | `CHANGELOG.md` (newest at top) |
| Phase or task completed | The relevant tracker doc |
| New standing rule added | `CLAUDE.md` + `archive/LESSONS.md` (the incident behind the rule) |
| Phase 3 commit ships a mitigation for a risk documented in an earlier plan's § 11 | The earlier plan's risk row — annotated as CLOSED in the SAME commit (status, closing commit hash, one-line reason). See § 4.3 below + `archive/LESSONS.md` L036. |

### 4.1 Strict same-session sync — non-negotiable pairs

These code-doc pairs **must** update in the same edit session. Drift between them is a defect, not a future cleanup item.

| Code change | Doc that MUST update |
|---|---|
| Domain behavior (detection, entry, exit, simulation, etc.) | The authoritative domain doc |
| Public API surface (signatures, return types, env vars, CLI) | `docs/api_reference.md` |
| DB schema | `docs/database_schema.md` |
| Folder layout | `docs/folder_structure.md` |

Violating a strict-sync pair is a Major defect — surface it for fix-forward (Rule 3), do not silently absorb.

### 4.2 When strict same-session sync is NOT required

Minor-only edits may skip the strict-sync sources **only if ALL hold**:

- No change to outcomes (signal definitions, simulation semantics, API behavior, schema content)
- No change to user-facing parameters or config keys
- Comments / refactors / docs that do not assert new behavior

When in doubt, sync. Skipping a sync that turned out to be needed costs more than redundant sync.

### 4.3 Closed-risk annotation discipline

When a Phase 3 commit ships a mitigation for a risk documented in an earlier plan's § 11 risks section, the earlier plan's risk row MUST be annotated as CLOSED in the **same commit** that ships the mitigation. Per `archive/LESSONS.md` L036.

The annotation includes:

1. **Status change.** `OPEN` → `CLOSED` (or `PARTIAL` if the mitigation is incomplete).
2. **Closing commit hash.** The short SHA of the commit that ships the mitigation.
3. **One-line reason.** Which plan / mechanism closed the risk (e.g., "PLAN-003 / v7.07 force-true rule").

**The audit trail is the source of truth for open risks.** A risk is open if and only if the plan that documented it says it's open. Plan documents are mutable in this respect — the risk section is not a frozen historical snapshot; it's a living status board that the project's commits keep current.

**Anti-pattern:** shipping the mitigation in commit `A` and annotating the earlier plan's risk in a follow-up commit `B`. Between `A` and `B`, anyone reading the earlier plan in isolation forms a wrong mental model of open risks. Always bundle the annotation with the mitigation.

If a follow-up Phase 3 commit accidentally ships the mitigation without the annotation, the fix-forward (per CLAUDE.md Rule 3) takes the form of a small "bookkeeping fix-forward" commit annotating the earlier plan. Acceptable as recovery; not acceptable as the planned shape.

<!--
Example (EverOn.Equinex PLAN-001 § 11 fix-forward, commit d769b29):
PLAN-001 documented 7 design risks. Across PLAN-002, v7.06, and PLAN-003,
risks #1, #2, #3 were systematically closed but PLAN-001's § 11 was never
updated. Caught by operator status check on 2026-05-21; fix-forward landed
as d769b29 annotating all three risks with their closing commit hashes.
The L036 codification ensures future Phase 3 commits bundle the annotation
in the same commit as the mitigation.
-->

---

## 5. Document version headers

Every tracked `.md` doc carries a hidden HTML-comment header at the top, paralleling the VERSION headers on `.py`/`.sh` files (per CLAUDE.md § 7).

### 5.1 Header template

```markdown
<!-- VERSION: X.Y -->
<!-- Last Updated: YYYY-MM-DD -->
<!-- Source: <where the canonical version lives> -->
<!--
CHANGE LOG
vX.Y — YYYY-MM-DD — <one-line summary of this change>
vX.Y-1 — YYYY-MM-DD — <previous summary>
-->

# <Document Title>

**Status:** <one line — e.g., "Current-state documentation as of YYYY-MM-DD" or "Living tracker" or "Design draft">
```

### 5.2 Why HTML comments

HTML comments don't render in GitHub/GitLab markdown previews — they're invisible to readers viewing the rendered doc. But they're parseable by governance scripts and visible to anyone editing the source. Best of both worlds: clean reading experience, machine-readable metadata.

### 5.3 Bump rules (parallel to code files)

- **Minor bump** (1.2 → 1.3): typo fixes, clarifications, example additions, formatting tweaks
- **Major bump** (1.9 → 2.0): structural rewrites, new sections, removed sections, reorganization
- **First version on a new doc:** start at `0.1`. Promote to `1.0` when the structure stabilizes.

### 5.4 Status line

Below the title, a one-line Status field describes the doc's stability:

- "Current-state documentation as of YYYY-MM-DD" — for reference docs that describe how things are
- "Living tracker — updated continuously" — for tracker files
- "Design draft" — for plan docs in active design
- "Locked design — implementation in progress" — for plan docs handed off to implementation
- "Append-only history" — for archive files like LESSONS.md

### 5.5 Living trackers — date-stamped, not version-bumped

Some docs are updated continuously and don't carry meaningful versioning. Trackers are the canonical example: they get updated every time a task ships, and a VERSION bump per update would be noise. For these:

- Header still has VERSION (often `1.0` permanently)
- "Last Updated" is the active marker — bumped on every meaningful edit
- CHANGE LOG block can be omitted or used sparingly for structural changes only

---

## 6. Standard folder layout

```
<repo-root>/
├── CLAUDE.md                          # The 9 standing rules + project specifics
├── README.md                          # User-facing intro + Quick Start
├── CHANGELOG.md                       # Cross-cutting history
├── .gitignore
├── .gitlab-ci.yml                     # (or .github/workflows/)
├── .gitlab/
│   └── merge_request_templates/
│       └── Default.md                 # Required source-of-truth checklist
├── docs/
│   ├── README.md                      # Index of all docs/
│   ├── documents_manifest.md          # Version manifest
│   ├── folder_structure.md            # Authoritative layout
│   ├── system_architecture.md         # High-level system design
│   ├── system_diagram.md              # Architecture diagrams
│   ├── api_reference.md               # Public interfaces
│   ├── database_schema.md             # All tables, columns, keys
│   ├── config_reference.md            # All config keys + env vars
│   ├── runbook.md                     # Operations + deploy procedures
│   ├── docker.md                      # Container reference
│   ├── ci_cd.md                       # Pipeline reference
│   ├── staging_environment.md         # Staging host details
│   ├── testing.md                     # Test framework reference
│   ├── troubleshooting.md             # Known issues + fixes
│   ├── <project>_setup_tracker.md     # Living phase/task tracker
│   ├── <domain-specific>.md           # e.g., business_logic.md
│   ├── standards/                     # Standards files copied from this repo
│   │   ├── PROJECT_STANDARDS.md       # This file
│   │   ├── PROMPT_STANDARDS.md
│   │   ├── ENGINEERING_STANDARDS.md
│   │   ├── CICD_STANDARDS.md
│   │   ├── VALIDATION_STANDARDS.md
│   │   └── MEMORY_PROTOCOL.md
│   └── Plans/                         # All planning docs (committed)
│       ├── <feature-name>-plan.md
│       └── ...
├── scripts/
│   ├── check_doc_coverage.py          # Local governance: surfaces drift across env vars, DB tables, API routes, manifest, folder structure, config docs, CHANGELOG freshness, import boundaries
│   ├── check_test_coverage_drift.py   # Code↔test↔doc drift detector with ownership map
│   ├── doc_coverage_allowlist.toml    # Justified exceptions to coverage check
│   ├── validation_ownership.toml      # File-to-test-to-doc ownership rules
│   └── pre-commit                     # Optional: git pre-commit hook script
├── archive/
│   ├── LESSONS.md                     # Incident-to-rule history
│   └── postmortems/                   # Detailed postmortems for major incidents
└── <code folders>/
```

### 6.1 Layout rules

- **Standards folder is `docs/standards/`**, not `docs/STANDARDS/` or `standards/`. Lowercase, plural, under docs.
- **Plans folder is `docs/Plans/`** with capital P (historical convention). The capital-P matters — lowercase `plans/` may match a `.gitignore` rule on case-insensitive filesystems (LESSONS L012).
- **No new top-level directories** without explicit approval — adding one is an architecture change requiring full Major workflow.

### 6.2 docs/README.md — the docs index

Every `.md` file under `docs/` (excluding `Plans/` and `standards/` which have their own listing patterns) appears in `docs/README.md`'s main table. This is a parallel-but-different artifact from the manifest:

- **Manifest** = version index (every tracked `.md` and code file)
- **docs/README.md** = navigational index for the `docs/` folder

When new docs are added under `docs/`, both update in the same commit.

---

## 7. Tracker files — phase and task management

Living trackers organize multi-phase work. Each project gets ONE tracker (e.g., `docs/<project>_setup_tracker.md`). Sub-projects or feature-specific work that warrants tracking gets a separate tracker file.

### 7.1 Tracker file structure

```markdown
<!-- VERSION: 1.0 -->
<!-- Last Updated: YYYY-MM-DD -->
# <Project> Setup Tracker

**Status:** <one line — e.g., "Phase 3 in progress; 7/8 tasks complete">
**Origin/master tip:** <SHA>
**Active phase:** <Phase N — Description>

---

## Phase Tracking

### Phase 1 — <Phase title>

**Status:** <Complete | In progress | Blocked>
**Scope:** <one-paragraph description>
**Exit criteria:** <bullet list of conditions that mark this phase complete>

| # | Task | Status | Touches Repo | Notes/Commit |
|---|---|---|---|---|
| 1.1 | <Task description> | Complete (commit `abc1234`, YYYY-MM-DD — one-line outcome) | Yes | <notes> |
| 1.2 | <Task description> | In progress | Yes | — |
| 1.3 | <Task description> | Not started | No | — |

### Phase 2 — <Phase title>
... (same structure)

---

## Phase N Deferred Items

Items uncovered during Phase N work that are out of scope but must not be forgotten.

| # | Item | Source | Severity | Current state | Suggested resolution |
|---|---|---|---|---|---|
| D1 | <Item> | Task 2.5c verification | Hygiene | Open | <plan> |
| D2 | <Item> | Task 3.2 testing | Correctness | CLOSED — addressed by Task 3.3 | — |

**Resolution legend:**
- D1 → <where it goes>
- D2 → CLOSED — <closing context>

---

## Incidents

### YYYY-MM-DD — <Incident title>
**Trigger:** <what happened>
**What changed:** <facts>
**Why now:** <rationale>
**Validation:** <how it was verified>
**Lessons:** <what gets codified into a standing rule, or which existing rule was reinforced>

(append-only; never delete past incidents)
```

### 7.2 Update protocol

When a task completes:

1. Update the task row's Status cell with `Complete (commit hash, date — one-line outcome)`
2. Rotate the Phase Status block if the phase tally changed (e.g., "5/8 → 6/8 complete")
3. Append an incident block at the end of the Incidents section if the task was substantive
4. If a Deferred Item closes, mark it `CLOSED — addressed by <task>` (do not delete)

When a task partially completes (revealing follow-up work):

1. Mark the original task `Complete (with follow-ups)` referencing the original commit
2. Add new sub-task rows with letter suffixes (e.g., `2.5b`, `2.5c`)
3. Per CLAUDE.md Rule 3 / LESSONS L003 — letter-suffix sub-tasks preserve the failure history

### 7.3 Deferred Items — surfacing technical debt

When work uncovers something out of scope but worth tracking:

- Add a row to the Phase N Deferred Items table
- Severity: `Hygiene`, `Cosmetic`, `Correctness`, `Operational`, `Security`, `Telemetry`
- Current state: `Open`, `In progress`, `CLOSED — addressed by <task>`
- Suggested resolution: concrete next step or design option

Deferred Items are first-class — they get the same tracker discipline as primary tasks. The point is to make technical debt **visible** rather than silent.

### 7.4 Sub-task numbering conventions

- Tasks: `1.1, 1.2, 1.3` etc. — primary phase work
- Fix-forward sub-tasks: `1.5b, 1.5c` — letter suffix per Rule 3 / LESSONS L003
- Out-of-band tasks (alphabet): `Task A, Task M, Task C` — work that doesn't fit the numbered phase sequence (e.g., emergency docs, infrastructure that crosses phase boundaries)

### 7.5 Tracker is NOT

- Not the manifest (manifest tracks file versions, tracker tracks work)
- Not the changelog (changelog is project-wide, tracker is phase-scoped)
- Not throwaway — committed, reviewed, referenced months after work completes

### 7.6 Incidents — append-only, never delete

The Incidents section is append-only. Past incident blocks describe what was learned during specific tasks; deleting them erases the lesson. New incidents add at the end of the section, not the top.

If an incident's lessons get elevated into a standing rule (CLAUDE.md or one of the standards docs), the incident block stays in the tracker AND the lesson moves to `archive/LESSONS.md` with a cross-reference back to the tracker incident.

### 7.7 Tracker ownership (multi-agent projects)

**OPTIONAL — only relevant if your project uses a second AI coding agent.** See `CLAUDE.md` § 14 Codex handoff protocol and `archive/LESSONS.md` L020.

Each tracker declares its primary owner in a top-of-file `Owner:` header:

```markdown
<!-- VERSION: 1.0 -->
Owner: Claude
```

or

```markdown
<!-- VERSION: 1.0 -->
Owner: Codex
```

Other agents do NOT edit a tracker they don't own. If an agent has an observation that belongs in another tracker, it gets recorded in the agent's own tracker (with a cross-reference like "see incident I-15 in `ea_test_tracker.md`") rather than direct edit across the boundary.

When creating a new tracker, declare ownership in its header at creation time.

Single-agent projects: skip this subsection entirely; tracker ownership is implicit (the only agent owns all trackers).

---

## 8. Commit discipline (full detail)

`CLAUDE.md` § 11 covers the binding rules; this section provides the procedural detail.

### 8.1 When to commit

- After a **coherent task is complete** — not after every individual file edit.
- Multiple files changed for one logical task → **one commit**.
- **Never** commit half-finished work, broken states, or changes that haven't passed validation.

### 8.2 Commit message structure

```
<Type/Scope>: <Title — present tense, imperative>

<Body paragraph 1 — what changed and why>

<Body paragraph 2 — context, design choice, alternatives considered>

<Optional: explicit impact statement — "No domain logic impact." etc.>

<Optional: ties to tracker — "Closes Phase X Task Y.Z">
```

### 8.3 Multi-paragraph messages — `-F /tmp/<file>` (Rule 4)

Per CLAUDE.md Rule 4 / LESSONS L004 — multi-paragraph commit messages with backticks, em-dashes, or any special characters use `git commit -F`:

```bash
cat > /tmp/commit_msg_<task>.txt <<'EOF'
<title>

<body paragraph>

<impact statement>
EOF

# Verify the file content survived the heredoc:
cat /tmp/commit_msg_<task>.txt

# Verify staged set BEFORE git add (Rule 6):
git status --short

git add -A

# Verify staged set AFTER git add (Rule 6):
git status --short

git commit -F /tmp/commit_msg_<task>.txt
```

The `cat /tmp/commit_msg_<task>.txt` step exists specifically to catch heredoc surprises before they corrupt the commit. If the rendered output shows backslash-escaped versions or replaced characters, the commit message file is corrupt — fix the heredoc, do not commit.

### 8.4 Split-commit pattern for substantive doc additions

Per LESSONS L010 — substantive doc additions split into two commits:

- **Commit 1:** the risky content (doc additions, sections, examples). Local-only at this point — amendable freely if review surfaces issues.
- **Commit 2:** the mechanical wiring (manifest entries, CHANGELOG, cross-references in other docs). Built on Commit 1's stable state.

Used successfully for Tasks A (Parts 1+2) and C (Parts 1+2a+2b) on EverOn.Capital-Signal.

#### Distribute doc sync across split commits — don't concentrate at "final sync"

Per LESSONS L029 (a refinement of L010) — every commit in a multi-commit plan must satisfy governance independently. Don't concentrate manifest / CHANGELOG / cross-reference updates in a single "final-sync" wiring commit while leaving earlier commits with stale governance state. Each commit, if pushed in isolation, must pass governance on its own.

Redistribute the wiring backward into the content commits:

- Commit A includes manifest entries for files A touches
- Commit B does the same for B
- No deferred bundle at the end that backfills A's governance

This makes `git bisect` reliable across the range and lets each commit ship independently if CI verification of an intermediate commit is needed.

### 8.5 Fix-forward (Rule 3 / LESSONS L003)

When a pushed commit fails CI:

- ❌ Do NOT `git push --force` an amended version
- ✅ DO create a new commit with letter suffix (e.g., `Task 2.5b: fix-forward for Task 2.5 CI failure`)
- Local-only commits (not yet pushed) may be amended freely

### 8.6 The "DO NOT PUSH" handoff

In any AI-agent prompt that ends with a commit (per `PROMPT_STANDARDS.md` § 3.7): explicitly state **"DO NOT PUSH. <user> pushes from <their machine>."**

This keeps the human as the final gate. The user reviews the agent's reported output, then pushes only after confirming everything is correct.

### 8.7 Code review before staging (L027)

Per `archive/LESSONS.md` L027 — explicit named review pass on all modified/new files BEFORE `git add`. This is a separate quality gate from governance scripts (which validate alignment, not correctness).

Procedure:

1. After all edits land but BEFORE `git add`, walk each modified/new file
2. For each file, ask:
   - Does it read correctly?
   - Are edge cases the task implied actually handled?
   - Is there a subtle bug a future reader would catch?
   - Are there orphan changes (unintentional edits caught in the diff)?
3. If concerns surface: fix and re-review BEFORE staging. Don't add-then-fix — the staging set should match the reviewed set.

Code review is short and incremental. The cost (~2 min per commit) is low compared to the cost of shipping a bug that governance scripts can't catch.

### 8.8 Agent runs commits end-to-end (L026)

Per `archive/LESSONS.md` L026 — if an AI agent prepares the commit, the agent also runs the `git add` + `git commit -F` ceremony end-to-end. Operator gating happens at **push**, not at commit.

Procedure:

```bash
# After code review (§ 8.7) passes:
cat > /tmp/commit_msg_<task>.txt <<'EOF'
<title>

<body>

<impact statement>
EOF

cat /tmp/commit_msg_<task>.txt    # Verify message file content (Rule 4 / L004)

git status --short                 # Pre-add verify (Rule 6 / L006)
git add -A
git status --short                 # Post-add verify (Rule 6 / L006)

git commit -F /tmp/commit_msg_<task>.txt

git log -1 --stat | cat            # Pager-safe verification (L011)
```

Operator does NOT context-switch to terminal mid-flow to run `git add` manually. That handoff pattern caused multiple Rule 4 (`-m` with escapes) violations before being deprecated.

Sandbox-failure recovery: if the agent's environment denies git operations, operator authorizes specific path patterns for the commit-related operations (e.g., `git add docs/standards/*.md`) rather than blanket bypass. Scoped authorization preserves the safety boundary; blanket bypass invites scope expansion.

### 8.9 Push cadence — batch local commits (L028)

Per `archive/LESSONS.md` L028 — default to local commit + hold. Push only when a specific trigger demands it. Push-after-every-commit produces pipeline noise and dilutes signal value.

Push triggers (push only on one of these):

1. **CI-verify needed** — the commit changes CI behavior worth observing live
2. **Staging-verify needed** — the commit modifies deploy behavior; staging will run it on next push
3. **Deliberate-failure cycle in flight** — push-fail-push-revert sequence
4. **`.gitlab-ci.yml` change** — real-pipeline run is dispositive (per CLAUDE.md Rule 5 / L005)
5. **End-of-session trigger** — close the day with a clean published state

Otherwise: commit locally, batch with other commits, push once when a trigger is hit.

Effect: pipeline run count drops ~5-10× during multi-commit sessions. Pipeline UI stays meaningful. Each pipeline run has a purpose.

---

## 9. Sources of truth — single canonical authority per topic

If you find content in multiple places, that is a **defect**. Resolve it: keep the canonical one, replace the others with pointers.

| Topic | Canonical source |
|---|---|
| Version header format & bump rules | `CLAUDE.md` § 7 |
| Minor vs Major workflow | `CLAUDE.md` §§ 5-6 |
| The 9 standing rules | `CLAUDE.md` § 3 |
| Critical files list | `CLAUDE.md` § 4 |
| Document version index | `docs/documents_manifest.md` |
| Cross-cutting project history | `CHANGELOG.md` (root) |
| Folder layout authoritative reference | `docs/folder_structure.md` |
| Standard folder layout (template) | This file (§ 6) |
| Domain behavior | `<your domain doc>` (e.g., `docs/business_logic.md`) |
| Phase/task progress | `docs/<project>_setup_tracker.md` |
| Memory hygiene rules | `docs/standards/MEMORY_PROTOCOL.md` |
| Multi-file AI prompt construction | `docs/standards/PROMPT_STANDARDS.md` |
| Engineering substrate (coding, architecture, deploy, ops) | `docs/standards/ENGINEERING_STANDARDS.md` |
| Test framework + tiers | `docs/standards/VALIDATION_STANDARDS.md` |
| CI/CD pipeline architecture | `docs/standards/CICD_STANDARDS.md` |
| Lesson archive (incident → rule) | `archive/LESSONS.md` |

### 9.1 Resolving duplication

When a duplication is detected:

1. Identify which location is canonical (usually the most-frequently-cited one)
2. Verify the canonical version is correct and complete
3. Replace the duplicate locations with pointers to the canonical version
4. Add a note in the canonical version's CHANGE LOG about consolidation
5. If the duplicate had unique content not in the canonical, MERGE the unique content into canonical first

This is a Major change — goes through full workflow.

---

## 10. Anti-patterns to refuse

Each pattern below was observed at some point on EverOn.Capital-Signal. Each costs drift, broken trust in the manifest, or wasted debugging time.

### 10.1 Updating the manifest "later"

❌ Pattern: bumping a `.py` file's VERSION header but deferring the manifest update to "the next commit" or "the end of the sprint."

Why bad: by the next commit, the deferred update is forgotten. The manifest's version cell now disagrees with the file's actual VERSION. Drift starts; trust in the manifest as a version index erodes.

✅ Fix: per CLAUDE.md Rule 8, manifest updates land **in the same commit** as the version bump. No exceptions.

### 10.2 CHANGELOG entry without explicit impact statement

❌ Pattern: "Refactored `pattern_engine.py` for clarity. Author: Yaser." — no Impact field.

Why bad: future contributors searching git history for "did this break anything" rely on the Impact field. Omitting it forces them to read the diff and guess.

✅ Fix: every entry has explicit Impact statement, even if the impact is "No runtime impact."

### 10.3 Skipping the tracker after task completion

❌ Pattern: task completes, commits ship, but the tracker row stays "In progress" for days.

Why bad: tracker is the canonical phase-progress source. Stale tracker → wrong context for the next session → repeated work clarifying status.

✅ Fix: tracker update lands in the same commit as the task's final commit.

### 10.4 Deferred items go to "TODO comments" instead of the tracker

❌ Pattern: noticing technical debt mid-implementation and adding `# TODO: clean this up` to the code.

Why bad: TODO comments are silent. They don't surface in any review, audit, or tracker. They accumulate; nobody addresses them.

✅ Fix: add a row to the tracker's Phase N Deferred Items table with severity. Make the debt visible.

### 10.5 Manifest exclusion lists / allowlists

❌ Pattern: maintaining an "intentionally untracked" list or exception list to keep the manifest "tidy."

Why bad: per CLAUDE.md Rule 8, exclusion lists drift. Nobody remembers why each entry is on the list. Eventually the exclusion list becomes a defensive accumulation.

✅ Fix: no exclusion lists. Unused files get **removed**, not allowlisted. The only exclusion is the categorical one (`.cursor/rules/*.md`, `.venv/`, `node_modules/`, `archive/`, gitignored content).

### 10.6 Reordering past CHANGELOG entries

❌ Pattern: noticing a typo or ordering issue in an old CHANGELOG entry and "fixing" it.

Why bad: CHANGELOG is historical record. Past entries reflect what was understood at the time. Editing them retroactively is rewriting history.

✅ Fix: only correct factual errors in past entries (and only when the correction matters). Add a new entry referencing the correction. Never reorder.

### 10.7 Manifest "Last Updated" with two `Previous change` entries

❌ Pattern: appending instead of rotating — manifest now has Previous change A and Previous change B both listed.

Why bad: the manifest is supposed to show one current change + one prior change + one prior audit. Appending without rotating breaks the format and confuses future readers about what's actually current.

✅ Fix: per § 2.6, on each rotation: current Change → Previous change; prior Previous change drops off entirely; Previous audit untouched.

### 10.8 Tracker row marked Complete without commit hash

❌ Pattern: "Task 3.5: Complete." in the tracker, no commit hash, no date.

Why bad: tracker rows are useful as references precisely BECAUSE they tie a task to a specific commit. Without that link, the row is just a checkbox — drift target.

✅ Fix: tracker rows for completed tasks include `Complete (commit <sha>, <date> — one-line outcome)`. The commit hash is the audit trail.

### 10.9 Push-after-every-commit

❌ Pattern: pushing every commit immediately, regardless of whether CI verification is meaningful for that specific commit.

Why bad: per L028, multi-commit sessions trigger ~5-10× the necessary pipeline runs. Pipeline UI fills with intermediate states where the next commit immediately supersedes the deploy state. Operators learn to skim pipeline notifications because most of them are noise. Real signal value drops.

✅ Fix: per § 8.9 — push only on the five named triggers (CI-verify, staging-verify, deliberate-failure cycle, `.gitlab-ci.yml` change, end-of-session). Otherwise commit locally and batch.

### 10.10 Concentrating doc-sync in a "final-sync" commit

❌ Pattern: split a feature across 2-3 commits with content in early commits and ALL manifest / CHANGELOG / cross-reference wiring deferred to a final "sync" commit.

Why bad: per L029, the early commits fail governance if pushed in isolation (which sometimes happens for CI-verification reasons). `git bisect` becomes unreliable across the range because some commits in the middle are "officially broken." The split-commit pattern (L010 / § 8.4) is correct but concentration of wiring breaks its premise.

✅ Fix: per § 8.4 — distribute wiring backward into the content commits. Each commit, if pushed in isolation, must pass governance on its own.

### 10.11 Skipping code review (relying on governance only)

❌ Pattern: governance scripts pass + tests pass → ship.

Why bad: per L027, governance validates alignment (drift, manifest, coverage), not correctness. Logic errors, missed edge cases, and readability problems all pass governance silently. Tests catch known-test-shaped failure modes; code review catches subtle ones.

✅ Fix: per § 8.7 — explicit named code review pass on all modified/new files BEFORE `git add`. This is a 2-minute discipline that catches bugs that would otherwise ship.

---

## End of standards

Governance is the mechanical discipline that keeps a project coherent over months and years. The patterns above feel like overhead until the day they prevent the failure that would have cost a weekend.

When a new governance pattern emerges from a debugging session, **add it here** with a cross-reference to the lesson in `archive/LESSONS.md`. When a rule above stops paying its weight, surface it for review — but never delete a rule without an explicit reason captured in `archive/LESSONS.md` and a corresponding CHANGELOG entry explaining the removal.

The discipline scales: a 5-minute manifest update prevents a 2-hour audit when the drift is finally noticed. Slow down to maintain well.
