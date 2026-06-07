<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-05-22 -->
<!-- Source: ~/everon-standards/NEW_PROJECT_BOOTSTRAP.md -->
<!--
CHANGE LOG
v1.1 — 2026-05-22 — Set Version v2.1 fix-forward: bring stale body-text references current. Five non-history occurrences updated: § 4.1 layout tree comment "The 9 binding standards files (copied)" → "The 10 binding standards files (copied)" (SESSION_OPENER added in v2.1); § 4.1 supporting-text "the 9-file standards suite" → "the 10-file standards suite"; § 8 first-commit impact statement + § 8 commit message body + § 13 closing prose: three instances of "the 8 standing rules" → "the 9 standing rules" (Rule 9 appended in v2.1). Worked-example commit messages preserved otherwise.
v1.0 — 2026-05-16 — Initial release. Detailed Day-Zero walkthrough for adopting the standards suite into a new project. Step-by-step commands, customization checklist, supporting files, governance scripts, CI scaffold, first commit shape. Pulls the adoption procedure out of README § 4.1 to keep README focused on orientation.
-->

# NEW_PROJECT_BOOTSTRAP.md — Day-Zero Walkthrough

**Scope:** This file is the dispositive step-by-step procedure for bootstrapping a new project from this standards suite. It expands on `README.md` § 4.1 (which is the orientation) with concrete commands, expected outputs, and customization details.

**Time required:** 30–60 minutes total. Most of it is reading and customization; the actual copying takes 2 minutes.

**Prerequisites:**

- A new empty git repository (created on GitHub/GitLab or initialized locally)
- A local checkout of this standards repo (the source you're copying FROM)
- Decided: are you using a single AI agent (Claude only) or multiple (Claude + Codex / Devin / other)?
- Decided: which CI provider (GitLab CI / GitHub Actions / other)?
- Decided: which deploy shape (registry-pull to VPS / Kubernetes / serverless / other)?

If any of these are still undecided, decide before starting. The customization step (§ 4) depends on these decisions.

---

## Table of Contents

1. [Overview — what you'll have when done](#1-overview--what-youll-have-when-done)
2. [Step 1 — Create the project repository](#2-step-1--create-the-project-repository)
3. [Step 2 — Copy the standards files](#3-step-2--copy-the-standards-files)
4. [Step 3 — Customize placeholders](#4-step-3--customize-placeholders)
5. [Step 4 — Create supporting files](#5-step-4--create-supporting-files)
6. [Step 5 — Add governance scripts](#6-step-5--add-governance-scripts)
7. [Step 6 — Add CI scaffold](#7-step-6--add-ci-scaffold)
8. [Step 7 — Add merge-request template](#8-step-7--add-merge-request-template)
9. [Step 8 — First commit](#9-step-8--first-commit)
10. [Step 9 — Set up Claude.ai Project (if using Claude.ai)](#10-step-9--set-up-claudeai-project-if-using-claudeai)
11. [Step 10 — Record Set Version adopted](#11-step-10--record-set-version-adopted)
12. [Post-bootstrap — what to do next](#12-post-bootstrap--what-to-do-next)
13. [Troubleshooting](#13-troubleshooting)

---

## 1. Overview — what you'll have when done

After completing this walkthrough, your new project will have:

```
<your-project>/
├── CLAUDE.md                                # Repo-root operating contract (customized)
├── README.md                                # Your project's README (placeholder for now)
├── CHANGELOG.md                             # Cross-cutting history (with bootstrap entry)
├── .gitignore                               # Standard ignores
├── .gitlab-ci.yml (or .github/workflows/)   # CI scaffold (governance + test stages)
├── .gitlab/merge_request_templates/Default.md  # MR template
├── docs/
│   ├── README.md                            # Index of docs/
│   ├── documents_manifest.md                # Version manifest
│   ├── folder_structure.md                  # Authoritative layout
│   ├── standards/                           # The 10 binding standards files (copied)
│   │   ├── CLAUDE.md                        # (Note: also at repo root — this is the template version)
│   │   ├── PROJECT_STANDARDS.md
│   │   ├── PROMPT_STANDARDS.md
│   │   ├── PROJECT_INSTRUCTIONS_TEMPLATE.md
│   │   ├── MEMORY_PROTOCOL.md
│   │   ├── ENGINEERING_STANDARDS.md
│   │   ├── VALIDATION_STANDARDS.md
│   │   └── CICD_STANDARDS.md
│   └── Plans/                               # Empty for now; planning docs land here
├── scripts/
│   ├── check_doc_coverage.py                # Governance: drift detection across env vars, DB tables, manifest
│   ├── check_test_coverage_drift.py         # Governance: code↔test↔doc drift
│   ├── doc_coverage_allowlist.toml          # Justified exceptions (empty initially)
│   └── validation_ownership.toml            # File-to-test-to-doc ownership rules (project-specific)
└── archive/
    └── LESSONS.md                           # Incident-to-rule archive (initial copy from source)
```

After the first commit (Step 8), you have a working governance scaffold and can start feature work in your next session.

---

## 2. Step 1 — Create the project repository

```bash
# Option A: Create on GitLab/GitHub, then clone
git clone <repo-url>
cd <project-name>

# Option B: Initialize locally
mkdir <project-name>
cd <project-name>
git init
```

Either path is fine. The bootstrap procedure operates on a working tree; the remote doesn't matter for steps 2–8.

**Verify:** `pwd` shows the project directory; `git status` shows a clean tree (or one untracked .DS_Store-style file from the empty directory).

---

## 3. Step 2 — Copy the standards files

Two patterns:

### Pattern A — Copy (independent versions per project) — RECOMMENDED

The standards repo is flat; your project nests these files under `docs/standards/` and `archive/`. Three copy operations:

```bash
# Assume you're in your new project's root directory.
# Replace ~/everon-standards/ with the actual path to your standards source.
STANDARDS_SRC=~/everon-standards

# 1. CLAUDE.md goes to repo root (it's the binding contract)
cp "$STANDARDS_SRC/CLAUDE.md" ./CLAUDE.md

# 2. The 7 focused standards files go under docs/standards/
mkdir -p docs/standards archive
cp "$STANDARDS_SRC/PROJECT_STANDARDS.md" \
   "$STANDARDS_SRC/PROMPT_STANDARDS.md" \
   "$STANDARDS_SRC/PROJECT_INSTRUCTIONS_TEMPLATE.md" \
   "$STANDARDS_SRC/MEMORY_PROTOCOL.md" \
   "$STANDARDS_SRC/ENGINEERING_STANDARDS.md" \
   "$STANDARDS_SRC/VALIDATION_STANDARDS.md" \
   "$STANDARDS_SRC/CICD_STANDARDS.md" \
   docs/standards/

# 3. LESSONS.md goes under archive/
cp "$STANDARDS_SRC/LESSONS.md" archive/LESSONS.md

# Verify:
ls -la CLAUDE.md docs/standards/ archive/
```

Expected output: 8 files (CLAUDE.md at root, 7 files in `docs/standards/`, 1 file in `archive/`).

**Note:** `README.md`, `STANDARDS_INDEX.md`, `NEW_PROJECT_BOOTSTRAP.md` from the standards repo are **not** copied into your project. Those are meta files about the standards repo itself; your project has its own `README.md` (Step 5) and refers to the standards-repo's STANDARDS_INDEX + BOOTSTRAP as external references.

### Pattern B — Symlink / submodule (shared versions across projects)

Either git submodule or symlinks. Gives instant updates across all projects but couples them. Only use for organizations enforcing identical standards across many projects.

```bash
# Submodule example:
git submodule add <standards-repo-url> docs/standards-source
ln -s docs/standards-source/CLAUDE.md ./CLAUDE.md
# ... etc
```

Pattern A is recommended for solo work; Pattern B for orgs.

---

## 4. Step 3 — Customize placeholders

Walk `README.md` § 6 (Customization checklist) and replace every `<placeholder>` with project-specific values.

### Mandatory customizations (won't work without these):

**`CLAUDE.md` — § 1 Project context:**

Find:

```
**Project:** `<project-name>`
**Domain:** `<one-line description — e.g., "Python-based trading signal platform" / ...>`
**Primary languages:** `<e.g., Python 3.11, TypeScript, Bash>`
**Deployment shape:** `<e.g., "Dockerized, GitLab CI → Hetzner VPS via registry-pull">`
```

Replace with your actual values. Example for a SaaS API:

```
**Project:** acme-api
**Domain:** Node.js SaaS API for inventory management; serves customer-facing REST endpoints
**Primary languages:** TypeScript (Node 20.x), Bash
**Deployment shape:** Dockerized, GitHub Actions CI → AWS ECS via registry-pull
```

**`CLAUDE.md` — § 4 Critical files:**

Replace the `<critical_file_1>` placeholder block with your project's actual always-Major files. Delete the EverOn HTML-comment example or replace it with your project-specific list.

### Optional customizations:

**`docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` — Tier B (for Claude.ai users):**

If you'll be using Claude.ai sessions, fill in Tier B with this project's paths, commands, environment specifics, and quirks. Tier A and Tier C are usually fine as-is.

**`CLAUDE.md` — § 14 Codex handoff (multi-agent projects only):**

If your project uses a second AI agent (Codex / Devin / other), keep § 14 and customize the agent name + domain. If you're single-agent, you can either leave § 14 in place (it's marked OPTIONAL) or delete it for clarity.

### Run the customization checklist:

Open `README.md` § 6 and walk every `- [ ]` checkbox. Replace placeholders or confirm defaults.

---

## 5. Step 4 — Create supporting files

```bash
# Repo root
touch README.md CHANGELOG.md .gitignore

# docs/
mkdir -p docs/Plans
touch docs/README.md
touch docs/documents_manifest.md
touch docs/folder_structure.md

# docs/Plans needs a placeholder to be committed
touch docs/Plans/.gitkeep
```

### Initialize each with minimal content:

**`README.md`** (project README — short, will grow):

```markdown
# <project-name>

<One-paragraph project description.>

## Quick Start

<Setup commands.>

## Standards

This project follows the standards in `docs/standards/`. Binding contract: `CLAUDE.md` at repo root.
```

**`CHANGELOG.md`** (initialize with the bootstrap entry):

```markdown
# CHANGELOG

Newest entries at the top.

## [YYYY-MM-DD] — Project bootstrap: governance scaffold

- **Type:** Major / Infrastructure / Bootstrap
- **Files:** `CLAUDE.md` (repo root), `docs/standards/*.md` (7 binding files), `archive/LESSONS.md`, `docs/README.md`, `docs/documents_manifest.md`, `docs/folder_structure.md`, `scripts/check_doc_coverage.py`, `scripts/check_test_coverage_drift.py`, `.gitlab-ci.yml` (or equivalent), `.gitlab/merge_request_templates/Default.md`
- **Impact:** No runtime impact. Establishes the 9 standing rules, document manifest scaffold, CHANGELOG, governance scripts, CI placeholder, and standards files before any feature work begins. Standards files copied from `~/everon-standards/` at Standard Set Version v1.0 — independent versions from this point forward. Backport explicitly when standards repo evolves.
- **Author:** <your-name>
```

**`.gitignore`**:

```
# OS
.DS_Store

# IDE
.vscode/
.idea/

# Language-specific (add as needed)
# Python:
__pycache__/
*.pyc
.venv/
# Node:
node_modules/

# Secrets
.env
.env.local
*.pem
*.key

# Misc
*.log
```

**`docs/README.md`** (docs index):

```markdown
# docs/

Documentation for <project-name>.

## Internal Reference

- `documents_manifest.md` — version index of all tracked docs and code files
- `folder_structure.md` — authoritative layout
- `standards/` — the 10-file standards suite (copied from ~/everon-standards/)
- `Plans/` — planning documents (all committed; never throwaway)
```

**`docs/documents_manifest.md`** (manifest scaffold — fill in as files land):

```markdown
<!-- VERSION: 0.1 -->
# Document & Code Manifest

## Module Quick Index

| Module / Section | Entry range |
|---|---|
| Bootstrap | 1-10 |

## Manifest Table

| # | Title | Version | Category | Path |
|---|---|---|---|---|
| 1 | Operating Contract (binding) | - | Governance | `CLAUDE.md` |
| 2 | Project Standards | 1.2 | Governance | `docs/standards/PROJECT_STANDARDS.md` |
| 3 | Prompt Standards | 1.3 | Governance | `docs/standards/PROMPT_STANDARDS.md` |
| 4 | Project Instructions Template | 1.3 | Governance | `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` |
| 5 | Memory Protocol | 1.2 | Governance | `docs/standards/MEMORY_PROTOCOL.md` |
| 6 | Engineering Standards | 1.2 | Governance | `docs/standards/ENGINEERING_STANDARDS.md` |
| 7 | Validation Standards | 1.2 | Governance | `docs/standards/VALIDATION_STANDARDS.md` |
| 8 | CI/CD Standards | 1.2 | Governance | `docs/standards/CICD_STANDARDS.md` |
| 9 | Lessons Archive | 1.5 | Governance | `archive/LESSONS.md` |
| 10 | Docs Manifest | 0.1 | Governance | `docs/documents_manifest.md` |

## Last Updated

- **Date**: YYYY-MM-DD
- **Change**: Project bootstrap — initial manifest scaffold with 10 entries.
- **Previous change**: (none — this is the first entry)
- **Previous audit**: (none — first audit will be quarterly per `PROJECT_STANDARDS.md` § 2.9)
```

**`docs/folder_structure.md`** (authoritative layout scaffold):

```markdown
<!-- VERSION: 0.1 -->
# Folder Structure

**Authoritative layout for <project-name>.**

## Repository root

```
<project-name>/
├── CLAUDE.md
├── README.md
├── CHANGELOG.md
├── .gitignore
├── .gitlab-ci.yml (or .github/workflows/)
├── docs/
│   ├── README.md
│   ├── documents_manifest.md
│   ├── folder_structure.md
│   ├── standards/
│   └── Plans/
├── scripts/
└── archive/
    └── LESSONS.md
```

(Add code-folder entries as the project grows. See `docs/standards/PROJECT_STANDARDS.md` § 6 for the standard layout template.)
```

---

## 6. Step 5 — Add governance scripts

Copy or recreate the two governance scripts. These come from your standards source (or from a reference project that has them):

```bash
mkdir -p scripts
cp "$STANDARDS_SRC/../<reference-project>/scripts/check_doc_coverage.py" scripts/
cp "$STANDARDS_SRC/../<reference-project>/scripts/check_test_coverage_drift.py" scripts/
cp "$STANDARDS_SRC/../<reference-project>/scripts/doc_coverage_allowlist.toml" scripts/  # may be empty
cp "$STANDARDS_SRC/../<reference-project>/scripts/validation_ownership.toml" scripts/    # starter

# Make scripts executable
chmod +x scripts/check_doc_coverage.py scripts/check_test_coverage_drift.py
```

If you don't have a reference project to copy from, write minimal versions:

**`scripts/check_doc_coverage.py`** (minimal scaffold — extend over time):

```python
#!/usr/bin/env python3
# VERSION: 0.1
# Doc coverage governance — surface drift between code, docs, manifest.
# Initial scaffold; extend with project-specific checks.

import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
manifest = repo_root / "docs" / "documents_manifest.md"

if not manifest.exists():
    print("ERROR: docs/documents_manifest.md missing")
    sys.exit(1)

# TODO: actual coverage checks — env vars, DB tables, API routes, etc.
print("doc coverage: OK (scaffold — extend with project-specific checks)")
sys.exit(0)
```

**`scripts/check_test_coverage_drift.py`** (similar scaffold):

```python
#!/usr/bin/env python3
# VERSION: 0.1
# Test coverage drift governance — code↔test↔doc ownership map.

import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
ownership = repo_root / "scripts" / "validation_ownership.toml"

if not ownership.exists():
    print("ERROR: scripts/validation_ownership.toml missing")
    sys.exit(1)

# TODO: actual ownership-map checks per VALIDATION_STANDARDS § 4
print("test coverage drift: OK (scaffold — extend with project-specific rules)")
sys.exit(0)
```

The scaffolds exit 0 so initial setup doesn't block. Extend them as the project grows and the ownership-map rules accumulate.

**`scripts/validation_ownership.toml`** (starter):

```toml
# Per VALIDATION_STANDARDS § 4 — ownership map for source files → tests + docs.
# Add rules as your project's monitored paths grow.

# Example starter rule (adapt for your project):
# [rules.example]
# source_paths = ["src/example.py"]
# test_paths = ["tests/test_example.py"]
# doc_paths = ["docs/api_reference.md"]
# strictness = "strict"
# require_docs = true
# reason = "Example rule — replace with project-specific rules."

[monitored_paths]
strict = []  # populate as the project grows
soft = []
```

**`scripts/doc_coverage_allowlist.toml`** (starter — empty):

```toml
# Per VALIDATION_STANDARDS § 4.5 — justified exceptions to doc coverage checks.
# Add entries only when genuinely needed; each entry needs author + date + reason.
```

---

## 7. Step 6 — Add CI scaffold

The minimum CI shape is a `governance` stage that runs the two governance scripts. Build out additional stages as the project grows.

**For GitLab CI** (`.gitlab-ci.yml`):

```yaml
stages:
  - governance
  - test
  - build
  - deploy
  - verify
  - deploy-prod
  - verify-prod

governance:
  stage: governance
  image: python:3.11-slim
  script:
    - python scripts/check_doc_coverage.py
    - python scripts/check_test_coverage_drift.py --ci
  rules:
    - if: $CI_COMMIT_BRANCH == "master" || $CI_PIPELINE_SOURCE == "merge_request_event"
```

**For GitHub Actions** (`.github/workflows/governance.yml`):

```yaml
name: governance
on: [push, pull_request]
jobs:
  governance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: python scripts/check_doc_coverage.py
      - run: python scripts/check_test_coverage_drift.py --ci
```

Extend with `test`, `build`, `deploy`, `verify`, `deploy-prod`, `verify-prod` stages per `CICD_STANDARDS.md` § 2 as your deploy story matures.

---

## 8. Step 7 — Add merge-request template

`.gitlab/merge_request_templates/Default.md` (or `.github/pull_request_template.md`):

```markdown
## Summary

<one-line description>

## Change classification

- [ ] Minor — bug fix / refactor / docs / lint
- [ ] Major — domain logic / new module / public API / DB schema / CI structure / critical file

## Sync checklist (per `docs/standards/PROJECT_STANDARDS.md` § 4)

- [ ] VERSION header bumped on every touched `.py`/`.sh` (per `CLAUDE.md` § 7)
- [ ] CHANGE LOG line added in each touched file's header
- [ ] `docs/documents_manifest.md` updated (version cells + Last Updated rotation)
- [ ] `CHANGELOG.md` entry added at top with explicit impact statement
- [ ] Source-of-truth doc updated if behavior changed (e.g., `docs/business_logic.md`)
- [ ] Tracker file updated if Phase/Task work
- [ ] Code review pass on all touched files BEFORE staging (per `CLAUDE.md` § 8.5)

## Pre-push governance

- [ ] `python scripts/check_doc_coverage.py` exits 0 — paste output below
- [ ] `python scripts/check_test_coverage_drift.py --ci` exits 0 — paste output below

```
<paste verbatim output here>
```

## Test plan

<Bulleted checklist of how to verify this change.>

## Impact statement

- [ ] No runtime impact
- [ ] Behavior change — describe what changes and how to verify
- [ ] Schema change — migration included
- [ ] CI/CD change — first pipeline run will be the dispositive validation
```

---

## 9. Step 8 — First commit

```bash
cat > /tmp/bootstrap_commit_msg.txt <<'EOF'
Bootstrap: governance scaffold

Establishes the 9 standing rules (CLAUDE.md at repo root + 7 focused standards
under docs/standards/), document manifest scaffold, CHANGELOG, folder
structure, governance scripts, CI scaffold, MR template, and LESSONS archive
before any feature work begins. No runtime code in this commit.

Standards files copied from ~/everon-standards/ at Standard Set Version v1.0
on YYYY-MM-DD. Independent versions from this point forward. Backports from
the standards source are explicit (see docs/standards/STANDARDS_INDEX.md at
the source for set-version evolution).

Scope:
- CLAUDE.md at repo root (template; customized per project)
- 7 focused standards in docs/standards/ (PROJECT_STANDARDS, PROMPT_STANDARDS,
  PROJECT_INSTRUCTIONS_TEMPLATE, MEMORY_PROTOCOL, ENGINEERING_STANDARDS,
  VALIDATION_STANDARDS, CICD_STANDARDS)
- LESSONS.md under archive/
- README.md (project README, placeholder)
- docs/{README,documents_manifest,folder_structure}.md
- scripts/{check_doc_coverage,check_test_coverage_drift}.py (scaffolds)
- scripts/{doc_coverage_allowlist,validation_ownership}.toml (starters)
- .gitlab-ci.yml (or .github/workflows/governance.yml)
- .gitlab/merge_request_templates/Default.md (or .github/pull_request_template.md)
- docs/Plans/.gitkeep

Customizations applied:
- CLAUDE.md § 1 project context filled
- CLAUDE.md § 4 critical files filled (or stub for now)
- (Codex handoff § 14: kept / removed per project)

No runtime impact. No tests required (no runtime code). First feature work
follows in subsequent commits using the established workflow.
EOF

# Pre-add verify (per CLAUDE.md Rule 6)
git status --short

# Stage all bootstrap files
git add CLAUDE.md README.md CHANGELOG.md .gitignore
git add docs/
git add archive/LESSONS.md
git add scripts/
git add .gitlab-ci.yml || git add .github/workflows/  # whichever you used
git add .gitlab/ || git add .github/

# Post-add verify (per CLAUDE.md Rule 6)
git status --short

# Commit
git commit -F /tmp/bootstrap_commit_msg.txt

# Final verification
git log -1 --stat | cat
```

**Verify the commit looks correct:**

- Commit message preserved special characters (em-dashes, backticks if any)
- File set matches expectations
- All listed files appear in `git log -1 --name-only`

If anything is off, **do not push yet**. Fix-forward (if pushed) or amend (if local-only) before continuing.

---

## 10. Step 9 — Set up Claude.ai Project (if using Claude.ai)

If you'll be using Claude.ai sessions in this project:

1. Create a new Project in Claude.ai (https://claude.ai/projects)
2. Open Project Instructions field
3. Copy the template from `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` § 4 (the block inside the 4-backtick fence)
4. Fill in Tier A (project context) and Tier B (critical files, commands, environment, quirks)
5. **Delete the Tier C HTML-comment block** — Tier C goes in the FIRST USER MESSAGE of each session, never in the Project Instructions field
6. **Decide on multi-agent block:** include the optional "Multi-agent coordination" sub-block ONLY if your project uses Codex / Devin / other. Otherwise delete it.
7. Save

Verify by starting a new conversation in the Project — the agent should reference CLAUDE.md and apply the session interaction protocol from message 1.

---

## 11. Step 10 — Record Set Version adopted

Record the Standard Set Version you adopted today. This makes future backports explicit.

**Option A — In CHANGELOG.md:**

Already present in the bootstrap entry from Step 5. Verify it says "Standard Set Version v1.0 on YYYY-MM-DD" (or whatever the current Set Version is when you bootstrap).

**Option B — Dedicated file:**

```bash
cat > docs/standards/SET_VERSION_ADOPTED.md <<'EOF'
<!-- VERSION: 1.0 -->
# Standard Set Version Adopted

This project was bootstrapped from the standards suite at:

- **Standard Set Version:** v1.0
- **Adopted on:** YYYY-MM-DD
- **Source:** ~/everon-standards/ (or wherever your source lives)

## Backport tracking

Backports from the source set are explicit. Newer Set Versions become available; track them here when adopting.

| Set Version | Adopted on | Backport notes |
|---|---|---|
| v1.0 | YYYY-MM-DD | Initial bootstrap |
EOF
```

Either approach is fine. The point is that a future-you can answer "what set version did we bootstrap from?" in 10 seconds.

---

## 12. Post-bootstrap — what to do next

Day Zero is complete. The next milestones:

### Day One — first feature work

Per `README.md` § 4.2 — the first real change goes through the full workflow:

1. Classify the change (Minor vs Major) per `CLAUDE.md` § 5
2. For Major: propose the design first per `CLAUDE.md` § 6 step 2
3. Implement per `ENGINEERING_STANDARDS.md`
4. If multi-file edit: draft the prompt per `PROMPT_STANDARDS.md`
5. Sync all affected docs in the same commit per `PROJECT_STANDARDS.md` § 4
6. Code review pass per `CLAUDE.md` § 8.5
7. Validate per `CLAUDE.md` § 8 checklist
8. CHANGELOG entry with explicit impact
9. Commit via `git commit -F /tmp/<file>` per Rule 4

### Week One — accumulating lessons

After ~5–10 commits, observed friction surfaces project-specific lessons. Capture them in:

- `docs/<project>_setup_tracker.md` Incidents section (the local tracker — create when first needed)
- A new entry in CLAUDE.md if the lesson reaches binding-rule significance

If a lesson is genuinely portable to other projects (not just this one), eventually backport it to the standards source per `README.md` § 5.5.

### Month One — first audits

Per `README.md` § 4.4 — quarterly audits should start at month one even if there's little to audit yet. Establish the rhythm:

1. Manifest sweep — every committed `.md` and VERSION-bearing code file in `docs/documents_manifest.md`
2. Lessons review — open `archive/LESSONS.md`; check rules still in force
3. Memory hygiene — walk the four-category test from `MEMORY_PROTOCOL.md` § 1
4. CHANGELOG continuity check — every meaningful commit has a CHANGELOG entry
5. Tracker review — no rows stuck "In progress" for >2 weeks

---

## 13. Troubleshooting

### "`git commit -F` is failing — invalid message"

Check that `/tmp/bootstrap_commit_msg.txt` actually exists and is non-empty: `cat /tmp/bootstrap_commit_msg.txt`. The heredoc must terminate correctly with `EOF` on its own line.

### "Pre-push governance scripts exit non-zero on first push"

The scaffolds in Step 6 are intentionally permissive (exit 0). If you replaced them with full implementations and they fail:

1. Read the actual error from the script's output
2. Either fix the gap (add the missing manifest entry, doc reference, etc.)
3. Or add a justified entry to `scripts/doc_coverage_allowlist.toml` (with author + date + reason + expiry)

Don't push with failing governance.

### "CI fails on the first push to master"

Per `CLAUDE.md` Rule 5 — local YAML parse validates syntax, not CI semantics. The first real-pipeline run may surface defects in `needs:`, `stage:`, `rules:`, etc. Fix-forward per Rule 3 (new commit with letter suffix, e.g., "Bootstrap-fix-b"). Do not force-push.

### "Standards file references docs/business_logic.md but my project doesn't have that"

Several standards files mention domain-specific docs (e.g., `docs/business_logic.md`) as a per-project source-of-truth doc. Either:

- Create the doc for your project (the standards files reference it but don't require any specific name)
- Adjust the reference in CLAUDE.md § 13 ("Single sources of truth") and any other files that mention it, to point at your project's actual domain doc

### "I'm using Codex / Devin / a second agent — what changes?"

Keep `CLAUDE.md` § 14 (Codex handoff) in your repo. Customize the agent name + domain. Read `archive/LESSONS.md` L020 for the codification incident. Read `docs/standards/PROMPT_STANDARDS.md` § 3.11 for the Codex variant of multi-file edit prompts. Single-agent projects can delete § 14.

---

## End of bootstrap

After Step 10, you have a working governance scaffold. Start feature work in your next session. The 9 standing rules now bind every commit, every prompt, every push.

Re-read `README.md` § 7 (Why this design) if you find yourself wanting to skip a rule — that section captures the reasoning. The discipline scales: 30 minutes of setup prevents months of friction.
