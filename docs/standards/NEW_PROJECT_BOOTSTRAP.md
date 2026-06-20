<!-- VERSION: 1.2 -->
<!-- Last Updated: 2026-06-20 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.2 — 2026-06-20 — Brought to full Standard Set Version v1.3 parity with SETUP.md (the headline one-shot
path; this file is its long-form companion, kept in step-parity). Added the project-local SESSION_OPENER/
CLOSER instantiation, the experiences-log (docs/STANDARDS_LOG.md) create step, Step 8 durable memory
(Rule 14), and Step 10.5 strip-the-machinery. Retargeted every v1.1 reference to v1.3; corrected the stale
counts ("9 standing rules" → 14; "10 binding files" → 11); added `.claude/` + `docs/Plans/OPEN_TASKS.md`
to .gitignore. Installer/walkthrough only — the v1.3 suite CONTENT is unchanged → no Set-Version bump.
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): retargeted the SET_VERSION_ADOPTED write to docs/ and updated the current-suite references to Standard Set Version v1.1. (Strip + experiences-log steps deferred — now done in v1.2.) Set Version v1.1.
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

# NEW_PROJECT_BOOTSTRAP.md — Day-Zero Walkthrough

> **The one-shot path is [`SETUP.md`](SETUP.md)** — a single paste-and-run prompt. **This file is the
> long-form companion behind it**: the same procedure expanded into click-through commands, expected
> outputs, and customization detail. The two are kept in **step-parity** — if you change the bootstrap
> procedure, change both. Use `SETUP.md` to actually run a bootstrap; use this file to understand what
> each step does (or to bootstrap by hand).

**Scope:** the dispositive step-by-step procedure for bootstrapping a new project from this standards
suite at **Standard Set Version v1.3** — governance scaffold, customized contract, session routines,
durable memory (Rule 14), the experiences log, governance scripts, CI, a first commit, then a strip of
the delivery machinery.

**Time required:** 30–60 minutes — mostly reading and customization; the copying takes 2 minutes.

**Prerequisites:**

- A new git repository for the project (created on a forge or initialized locally — it must have its
  **own** repo, not inherit a parent's `.git`).
- A local checkout of the canonical standards suite (the `SOURCE` you copy FROM — the folder containing
  `CLAUDE.md`, `LESSONS.md`, the focused standards, the session templates, `SETUP.md`, etc.).
- Decided: single AI agent (Claude only) or multiple (Claude + a second agent)?
- Decided: CI provider (GitLab CI / GitHub Actions / none)?
- Decided: deploy shape (local CLI / Dockerized + CI → host / serverless / other)?

---

## Table of Contents

1. [Overview — what you'll have when done](#1-overview--what-youll-have-when-done)
2. [Step 1 — Create the project repository](#2-step-1--create-the-project-repository)
3. [Step 2 — Lay down the suite](#3-step-2--lay-down-the-suite)
4. [Step 3 — Customize CLAUDE.md](#4-step-3--customize-claudemd)
5. [Step 4 — Create supporting files](#5-step-4--create-supporting-files)
6. [Step 5 — Add governance scripts](#6-step-5--add-governance-scripts)
7. [Step 6 — Add CI scaffold](#7-step-6--add-ci-scaffold)
8. [Step 7 — Add merge-request template](#8-step-7--add-merge-request-template)
9. [Step 8 — Set up durable memory (Rule 14)](#9-step-8--set-up-durable-memory-rule-14)
10. [Step 9 — Validate](#10-step-9--validate)
11. [Step 10 — First commit (operative standard installed)](#11-step-10--first-commit-operative-standard-installed)
12. [Step 10.5 — Strip the setup machinery](#12-step-105--strip-the-setup-machinery)
13. [Step 11 — Set up Claude.ai Project (optional)](#13-step-11--set-up-claudeai-project-optional)
14. [Step 12 — Record the Set Version adopted](#14-step-12--record-the-set-version-adopted)
15. [Post-bootstrap — what to do next](#15-post-bootstrap--what-to-do-next)
16. [Troubleshooting](#16-troubleshooting)

---

## 1. Overview — what you'll have when done

The suite is delivered by **setup-and-strip**: you lay down the whole crate, install + customize the
operative standard, commit it, then **delete the delivery machinery** in a second commit. The end state
(after the strip) carries only the operative standard:

```
<your-project>/
├── CLAUDE.md                      # repo-root operating contract (customized; 14 standing rules)
├── README.md                      # project README (placeholder)
├── CHANGELOG.md                   # cross-cutting history (bootstrap entry)
├── .gitignore                     # OS/IDE/language + docs/Plans/OPEN_TASKS.md + .claude/
├── .gitlab-ci.yml (or .github/workflows/)   # CI scaffold (governance stage)
├── .claude/
│   └── memory/                    # durable Claude memory (Rule 14; untracked / sync-carried)
├── docs/
│   ├── README.md
│   ├── documents_manifest.md      # version index
│   ├── folder_structure.md
│   ├── SESSION_OPENER.md          # project-local session-start pre-flight (binding, Rule 9)
│   ├── SESSION_CLOSER.md          # project-local session wrap-up (binding, Rule 12)
│   ├── SET_VERSION_ADOPTED.md     # records Standard Set Version v1.3
│   ├── STANDARDS_LOG.md           # the project's experiences log (contribution channel)
│   ├── standards/                 # 6 topical files KEPT after the strip
│   │   ├── PROJECT_STANDARDS.md
│   │   ├── PROMPT_STANDARDS.md
│   │   ├── MEMORY_PROTOCOL.md
│   │   ├── ENGINEERING_STANDARDS.md
│   │   ├── VALIDATION_STANDARDS.md
│   │   └── CICD_STANDARDS.md
│   └── Plans/                     # planning docs land here (all committed)
├── scripts/
│   ├── check_doc_coverage.py      # governance scaffold
│   ├── check_test_coverage_drift.py
│   ├── doc_coverage_allowlist.toml
│   ├── validation_ownership.toml
│   └── bootstrap_memory.sh        # idempotent Rule 14 symlink repair
└── archive/
    └── LESSONS.md                 # incident-to-rule archive (operative copy)
```

The **11 binding files** of the suite are CLAUDE.md, the 7 focused standards (PROJECT_STANDARDS,
PROMPT_STANDARDS, PROJECT_INSTRUCTIONS_TEMPLATE, MEMORY_PROTOCOL, ENGINEERING_STANDARDS,
VALIDATION_STANDARDS, CICD_STANDARDS), LESSONS.md, SESSION_OPENER.md, and SESSION_CLOSER.md. During
bootstrap they are laid down in full, then the strip (Step 10.5) keeps only the operative copies and
deletes the templates/meta machinery.

---

## 2. Step 1 — Create the project repository

```bash
# Option A: create on a forge, then clone
git clone <repo-url> && cd <project-name>

# Option B: initialize locally
mkdir <project-name> && cd <project-name> && git init -b main
```

**Critical pre-flight:** run `git rev-parse --show-toplevel`. If it resolves to a **parent** of your
project (e.g. `$HOME`), the project has no repo of its own — STOP and `git init -b main` inside it (this
shadows the parent `.git`). Confirm the new repo root before continuing. (This is the L043 home-dir
gotcha.)

**Verify:** `pwd` is the project dir; `git status` is clean (or a stray `.DS_Store`).

---

## 3. Step 2 — Lay down the suite

Copy the whole crate from `SOURCE` (do not modify `SOURCE`). `CLAUDE.md` goes to the repo root;
`LESSONS.md` to `archive/`; everything else to `docs/standards/`.

```bash
# In your new project's root. SOURCE = your canonical suite folder.
SOURCE=~/path/to/standards-suite           # the folder containing CLAUDE.md, LESSONS.md, ...
mkdir -p docs/standards archive

cp "$SOURCE/CLAUDE.md"   ./CLAUDE.md        # binding contract → repo root
cp "$SOURCE/LESSONS.md"  archive/LESSONS.md # incident-to-rule archive → archive/

# the 7 focused standards + the meta/machinery files + the session + log + memory templates
cp "$SOURCE/PROJECT_STANDARDS.md" "$SOURCE/PROMPT_STANDARDS.md" \
   "$SOURCE/PROJECT_INSTRUCTIONS_TEMPLATE.md" "$SOURCE/MEMORY_PROTOCOL.md" \
   "$SOURCE/ENGINEERING_STANDARDS.md" "$SOURCE/VALIDATION_STANDARDS.md" \
   "$SOURCE/CICD_STANDARDS.md" "$SOURCE/STANDARDS_INDEX.md" "$SOURCE/README.md" \
   "$SOURCE/NEW_PROJECT_BOOTSTRAP.md" "$SOURCE/HOW_TO_USE.md" "$SOURCE/SETUP.md" \
   "$SOURCE/STANDARDS_LOG.md" "$SOURCE/MEMORY_DURABILITY_ROLLOUT_PROMPT.md" \
   "$SOURCE/SESSION_OPENER.md" "$SOURCE/SESSION_CLOSER.md" \
   docs/standards/

ls -la CLAUDE.md docs/standards/ archive/    # 1 + 16 + 1
```

This is a **transient delivery crate** — Step 10.5 strips the machinery back down to the 6 operative
topical files. Laying it all down first keeps the strip's set-cover check honest.

**Instantiate the project-local session files** from the templates (these are operative — they survive
the strip and live in `docs/`, not `docs/standards/`):

```bash
cp docs/standards/SESSION_OPENER.md docs/SESSION_OPENER.md
cp docs/standards/SESSION_CLOSER.md docs/SESSION_CLOSER.md
```

Then edit `docs/SESSION_OPENER.md` and `docs/SESSION_CLOSER.md`: drop the "(template)" banner, and
customize §§ 2–3 for this project — the branch name, the environment/registry mapping, the failure-mode
rows (drop the remote-host rows if there's no remote infra). Keep the `PROJECT-OWNED` markers so a future
`sync` preserves your customizations.

---

## 4. Step 3 — Customize CLAUDE.md

`CLAUDE.md` is the binding contract. Customize the project-owned sections (everything else is verbatim
from the suite, including all 14 standing rules):

- **§ 1 Project context** — fill Project / Domain / Primary languages / Deployment shape / Multi-agent
  from your decisions.
- **§ 4 Critical files** — replace the `<placeholders>` with this project's real always-Major paths.
  Always include `docs/documents_manifest.md` and `CLAUDE.md` itself.
- **§ 13** — set the domain-behavior source-of-truth bullet to this project's reality.
- **§ 14 Codex handoff** — single-agent: replace with a short "NOT IN USE (single-agent project)" stub
  and set § 1 Multi-agent = no. Multi-agent: keep § 14 and name the second agent.
- **Reset the header** to this project's own `VERSION 1.0` with a one-line "Project bootstrap" CHANGE
  LOG; Source line = `docs/standards/ (this repo). Bootstrapped from Standard Set v1.3 on <today>.`
  (The v1.3 template already carries **Rule 14** — keep it; Step 8 wires up the mechanism.)

Example § 1 fill (SaaS API):

```
**Project:** acme-api
**Domain:** Node.js SaaS API for inventory management; customer-facing REST endpoints
**Primary languages:** TypeScript (Node 20.x), Bash
**Deployment shape:** Dockerized, GitHub Actions CI → AWS ECS via registry-pull
**Multi-agent:** no — single-agent (Codex § 14 trimmed)
```

---

## 5. Step 4 — Create supporting files

```bash
touch README.md CHANGELOG.md .gitignore
mkdir -p docs/Plans
touch docs/README.md docs/documents_manifest.md docs/folder_structure.md docs/Plans/.gitkeep
```

**`.gitignore`** — OS/IDE/language ignores **plus** the two standards-specific entries:

```
# OS / IDE
.DS_Store
.vscode/
.idea/

# Language-specific (add as needed) — Python:
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

# Local-only open-tasks register (per archive/LESSONS.md L046)
docs/Plans/OPEN_TASKS.md

# Durable project-memory workspace — untracked / sync-carried by design (Rule 14 / L050)
.claude/

# Misc
*.log
```

**`docs/STANDARDS_LOG.md`** — the project's experiences log (the contribution channel feeding harvest →
integrate). Create it from the template, **removing the example entry**:

```bash
# Start from docs/standards/STANDARDS_LOG.md, delete the E001 example, keep the schema/header.
cp docs/standards/STANDARDS_LOG.md docs/STANDARDS_LOG.md
# then edit docs/STANDARDS_LOG.md to remove the example entry (leave the format reference).
```

**`docs/SET_VERSION_ADOPTED.md`** — record the adopted version (Standard Set Version **v1.3**, adopted
`<today>`); see Step 12 for the full content.

**`README.md`**, **`docs/README.md`**, **`docs/documents_manifest.md`**, **`docs/folder_structure.md`**
— initialize with minimal content. The manifest lists every committed `.md` + every VERSION-bearing code
file (per Rule 8); the bootstrap entry seeds it. `CHANGELOG.md` gets the bootstrap entry (Step 10).

> Tip: the manifest's per-file version cells should reflect the files you actually laid down — read each
> file's `<!-- VERSION: -->` header rather than guessing. After the strip (Step 10.5), drop the stripped
> files' rows in the same commit.

---

## 6. Step 5 — Add governance scripts

Create `scripts/check_doc_coverage.py` + `scripts/check_test_coverage_drift.py` as **permissive
scaffolds** (VERSION 0.1, exit 0 so initial setup doesn't block), plus `doc_coverage_allowlist.toml` and
`validation_ownership.toml` starters. Copy from a reference project if you have one; otherwise the
minimal scaffolds:

```python
#!/usr/bin/env python3
# VERSION: 0.1
# Doc coverage governance — extend with project-specific checks.
import sys
from pathlib import Path

manifest = Path(__file__).resolve().parent.parent / "docs" / "documents_manifest.md"
if not manifest.exists():
    print("ERROR: docs/documents_manifest.md missing"); sys.exit(1)
print("doc coverage: OK (scaffold)"); sys.exit(0)
```

```python
#!/usr/bin/env python3
# VERSION: 0.1
# Test coverage drift governance — code↔test↔doc ownership map.
import sys
from pathlib import Path

ownership = Path(__file__).resolve().parent.parent / "scripts" / "validation_ownership.toml"
if not ownership.exists():
    print("ERROR: scripts/validation_ownership.toml missing"); sys.exit(1)
print("test coverage drift: OK (scaffold)"); sys.exit(0)
```

`check_test_coverage_drift.py` must accept a `--ci` flag (governance + CI call it that way). Extend both
as the project's ownership-map rules accumulate (per `VALIDATION_STANDARDS.md` § 4).

---

## 7. Step 6 — Add CI scaffold

Minimum CI = a `governance` stage running the two scripts on the default branch + PR/MR.

**GitLab CI** (`.gitlab-ci.yml`):

```yaml
stages: [governance, test, build, deploy, verify]

governance:
  stage: governance
  image: python:3.11-slim
  script:
    - python scripts/check_doc_coverage.py
    - python scripts/check_test_coverage_drift.py --ci
  rules:
    - if: $CI_COMMIT_BRANCH == "main" || $CI_PIPELINE_SOURCE == "merge_request_event"
```

**GitHub Actions** (`.github/workflows/governance.yml`):

```yaml
name: governance
on: [push, pull_request]
jobs:
  governance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: python scripts/check_doc_coverage.py
      - run: python scripts/check_test_coverage_drift.py --ci
```

Extend with `test` / `build` / `deploy` / `verify` per `CICD_STANDARDS.md` § 2 as the deploy story
matures. (CI semantics are validated by a real pipeline run, not local YAML parse — per Rule 5.)

---

## 8. Step 7 — Add merge-request template

`.gitlab/merge_request_templates/Default.md` (or `.github/pull_request_template.md`):

```markdown
## Summary
<one-line description>

## Change classification
- [ ] Minor — bug fix / refactor / docs / lint
- [ ] Major — domain logic / new module / public API / DB schema / CI structure / critical file

## Sync checklist (per docs/standards/PROJECT_STANDARDS.md § 4)
- [ ] VERSION header bumped on every touched .py/.sh (CLAUDE.md § 7) + CHANGE LOG line
- [ ] docs/documents_manifest.md updated (version cells + Last Updated)
- [ ] CHANGELOG.md entry at top with explicit impact statement
- [ ] Source-of-truth doc updated if behavior changed
- [ ] Code review pass on all touched files BEFORE staging (Rule 10)

## Pre-push governance (paste output)
- [ ] python scripts/check_doc_coverage.py exits 0
- [ ] python scripts/check_test_coverage_drift.py --ci exits 0

## Impact statement
- [ ] No runtime impact
- [ ] Behavior change — describe + how to verify
- [ ] Schema change — migration included
- [ ] CI/CD change — first pipeline run is dispositive
```

---

## 9. Step 8 — Set up durable memory (Rule 14)

Make the project's Claude memory survive a machine change / folder move. The contract text is already
present (the v1.3 template `CLAUDE.md` Rule 14 + `SESSION_OPENER.md` § 1.5 you laid down); this step
wires up the mechanism, following `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md`:

```bash
# 1. Create scripts/bootstrap_memory.sh per the rollout prompt: idempotent — derive the harness key from
#    the repo's absolute path ('/'→'-', ' '→'-') and (re)create the symlink
#    ~/.claude/projects/<key>/memory → <repo>/.claude/memory, preserving any pre-existing files.
mkdir -p .claude/memory
bash scripts/bootstrap_memory.sh        # paste its output
```

- `.claude/` is gitignored (Step 4), so the memory store rides the project's sync but is never
  accidentally committed.
- POSIX symlink — macOS/Linux. On Windows, adapt (directory junction) or keep memory synced by other
  means.

---

## 10. Step 9 — Validate

```bash
python scripts/check_doc_coverage.py            # exit 0 — paste stdout
python scripts/check_test_coverage_drift.py --ci # exit 0 — paste stdout
git status --short                              # ONLY the intended files
```

---

## 11. Step 10 — First commit (operative standard installed)

Post a named code-review pass (one verdict per file, per Rule 10), then commit. **Do not push** — push
is operator-gated.

```bash
cat > /tmp/bootstrap_commit_msg.txt <<'EOF'
Bootstrap: governance scaffold (Standard Set Version v1.3)

Installs the operative standard: CLAUDE.md (14 standing rules) at repo root +
the focused standards under docs/standards/, the LESSONS archive, project-local
SESSION_OPENER/CLOSER, the experiences log, durable memory (Rule 14), governance
scripts, CI scaffold, MR template, and the document manifest — before any feature
work. No runtime code in this commit.

Bootstrapped from the standards suite at Standard Set Version v1.3 on <today>.
Independent versions from this point forward; backports are explicit.
EOF

git status --short              # pre-add verify (Rule 6)
git add -A
git status --short              # post-add verify (Rule 6)
git commit -F /tmp/bootstrap_commit_msg.txt
git log -1 --stat | cat
```

Verify the commit preserved special characters and the file set matches. If anything is off, **don't
push** — amend (local-only) or fix-forward (if pushed) per Rule 3.

---

## 12. Step 10.5 — Strip the setup machinery

The suite under `docs/standards/` was a transient delivery crate. Now that the operative standard is
installed and committed, delete the setup/maintenance machinery so the project keeps only the operative
standard. Make this a **separate second commit** ("strip setup machinery") so the delivered-then-removed
transition is visible in history.

**Safety check first (set-cover):** the KEEP set ∪ the DELETE set below MUST equal the current
`docs/standards/` contents — no file unaccounted for. `ls docs/standards/` and confirm each file is in
exactly one list. If a file is in NEITHER, STOP — a new suite file may have been added since this was
written; never blind-delete.

- **KEEP in `docs/standards/`** (the topical library, loaded by the dispatcher during normal work):
  `PROJECT_STANDARDS.md`, `PROMPT_STANDARDS.md`, `MEMORY_PROTOCOL.md`, `ENGINEERING_STANDARDS.md`,
  `VALIDATION_STANDARDS.md`, `CICD_STANDARDS.md`  (6 files)
- **DELETE from `docs/standards/`** (machinery — only used to deliver/maintain the suite):
  `CLAUDE.md` (template), `LESSONS.md` (template), `SESSION_OPENER.md` (template),
  `SESSION_CLOSER.md` (template), `STANDARDS_LOG.md` (template), `SETUP.md`, `NEW_PROJECT_BOOTSTRAP.md`,
  `STANDARDS_INDEX.md`, `README.md` (meta), `HOW_TO_USE.md`, `PROJECT_INSTRUCTIONS_TEMPLATE.md`,
  `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` (used once in Step 8, then stripped)  (12 files)
- **NOT touched** (operative/kept files already outside `docs/standards/`): `CLAUDE.md` (root),
  `archive/LESSONS.md`, `docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`, `docs/SET_VERSION_ADOPTED.md`,
  `docs/STANDARDS_LOG.md`, `scripts/bootstrap_memory.sh`, `.claude/memory/`, governance scripts, CI,
  manifest.

In the **same strip commit**, update `docs/documents_manifest.md` + `docs/folder_structure.md` to drop
the stripped files (Rule 8). Then code-review, `git add -A`, re-check `git status --short`, and
`git commit -F /tmp/strip_commit_msg.txt`. Do not push.

---

## 13. Step 11 — Set up Claude.ai Project (optional)

If you'll use Claude.ai sessions:

1. Create a Project at https://claude.ai/projects and open Project Instructions.
2. Copy the template from `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` § 4 (inside the 4-backtick
   fence). *(Do this before the strip, or from `SOURCE` after — the template is stripped from the repo.)*
3. Fill Tier A (project context) and Tier B (critical files, commands, environment, quirks).
4. **Delete the Tier C block** — Tier C goes in the FIRST USER MESSAGE of each session, never in the
   Project Instructions field.
5. Include the multi-agent sub-block ONLY if using a second agent; otherwise delete it. Save.

Verify by starting a conversation — the agent should reference `CLAUDE.md` and run the session pre-flight
from message 1.

---

## 14. Step 12 — Record the Set Version adopted

`docs/SET_VERSION_ADOPTED.md` makes future backports explicit:

```bash
cat > docs/SET_VERSION_ADOPTED.md <<'EOF'
<!-- VERSION: 1.0 -->
# Standard Set Version Adopted

This project adopts the standards suite at:

- **Standard Set Version:** v1.3
- **Adopted on:** <today>
- **Source:** <your canonical suite path>

## Backport tracking

Backports from the source set are explicit. When a newer Set Version is released, read its history entry
(the source `STANDARDS_INDEX.md` § 6), reconcile your operative copies, and record it below.

| Set Version | Adopted on | Notes |
|---|---|---|
| v1.3 | <today> | Initial bootstrap |
EOF
```

The adopted state at v1.3: **14 standing rules** in `CLAUDE.md` § 3; the suite's lessons in
`archive/LESSONS.md`; durable memory (Rule 14) wired up.

---

## 15. Post-bootstrap — what to do next

**Day One — first feature work.** The first real change runs the full workflow: classify Minor vs Major
(CLAUDE.md § 5) → for Major, propose first (§ 6) → implement → if multi-file, draft the prompt
(`PROMPT_STANDARDS.md`) → sync all docs same-commit (`PROJECT_STANDARDS.md` § 4) → code review (Rule 10)
→ validate (§ 8) → CHANGELOG entry → commit via `git commit -F` (Rule 4). See `HOW_TO_USE.md` § 1 for the
Day-One prompt.

**Week One — lessons.** As friction surfaces, capture it in `docs/STANDARDS_LOG.md` (the experiences
log) via the wrap-up routine; portable lessons later flow back to the suite via harvest → integrate.

**Month One — first audit.** Establish the rhythm: manifest sweep, lessons review, memory hygiene
(`MEMORY_PROTOCOL.md`), CHANGELOG continuity, tracker review.

---

## 16. Troubleshooting

**`git commit -F` fails — invalid message:** confirm `/tmp/bootstrap_commit_msg.txt` exists and is
non-empty; the heredoc must end with `EOF` on its own line.

**Governance scripts exit non-zero on first push:** the scaffolds (Step 5) are permissive (exit 0). If
you replaced them and they fail, read the error and fix the gap, or add a justified
`doc_coverage_allowlist.toml` entry (author + date + reason + expiry). Don't push with failing
governance.

**CI fails on the first push:** local YAML parse validates syntax, not CI semantics (Rule 5). The first
real-pipeline run may surface `needs:` / `stage:` / `rules:` defects. Fix-forward (new commit with a
letter suffix) — never force-push (Rule 3).

**Memory store empty after a machine change / folder move:** run `bash scripts/bootstrap_memory.sh` to
re-home the symlink (Rule 14). If the content itself was lost, recover from the prior machine's
`~/.claude/projects/<old-key>/memory/` (or a sync/backup of it).

**Using a second agent (Codex / Devin):** keep `CLAUDE.md` § 14, name the agent + domain, and see
`PROMPT_STANDARDS.md` for the second-agent multi-file-edit prompt variant. Single-agent projects delete
§ 14.

---

## End of bootstrap

After Step 12 you have a working governance scaffold on Standard Set Version v1.3. Start feature work in
your next session — the 14 standing rules now bind every commit, every prompt, every push. The one-shot
equivalent of this walkthrough is `SETUP.md`; keep the two in step-parity if you change the procedure.
