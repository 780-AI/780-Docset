<!-- VERSION: 1.6 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.6 — 2026-08-16 — Standard Set Version v1.6 (PLAN-008): instantiation wording — delete the TEMPLATE-ONLY block, fill the PROJECT-OWNED heading block; § 3.1 stays suite-owned (customizations → § 3.2); retargeted every live v1.5 reference to v1.6 (per L053 — delivery docs are a parity set).
v1.5 — 2026-08-16 — Standard Set Version v1.5 (PLAN-010): retargeted every live v1.4 reference to v1.5 (per L053 — delivery docs are a parity set); Step 6.5 rewritten durable memory → project-data locality (creates scripts/claude_project_data.sh, runs link, seeds docs/MACHINE_MIGRATION.md); every bootstrap_memory reference swept — Step 6.5 body + Step 8.5 not-touched list (per L060).
v1.4 — 2026-08-16 — Retargeted every live v1.3 reference to v1.4 same-commit with the Standard Set Version v1.4 release (per L053 — delivery docs are a parity set; the parity update now rides the release itself). Prompt content otherwise unchanged.
v1.3 — 2026-06-21 — Fixed a bootstrap gap surfaced by the first real adoption: Step 5 gitignored
`docs/Plans/OPEN_TASKS.md` but never CREATED it, so a fresh project lacked the local-only register. Added
a Step 5 seed step (standard header + "no open items yet" placeholder; gitignored, not manifest-tracked).
Installer-only — the v1.3 suite CONTENT is unchanged → no Set-Version bump.
v1.2 — 2026-06-20 — Caught the bootstrap up to Standard Set Version v1.3 (it had been left at v1.1 across
the v1.2/v1.3 releases): retargeted every v1.1 reference to v1.3 (intro, prompt header, Step 4 Source line,
Step 5 SET_VERSION_ADOPTED); registered MEMORY_DURABILITY_ROLLOUT_PROMPT.md in the Step 1 pre-flight check,
the Step 3 lay-down, and the Step 8.5 strip DELETE list — fixing the set-cover, which the v1.2 file had
silently left at 17 of 18; added Step 6.5 (Rule 14 durable-memory setup) + `.claude/` to the Step 5
.gitignore. No Set-Version change — the v1.3 suite CONTENT is unchanged; this is overdue installer
maintenance so a fresh bootstrap delivers v1.3 (incl. durable memory) turn-key and records v1.3 adopted.
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): added the experiences-log create step (docs/STANDARDS_LOG.md from
the template, minus the example) and the lay-down/confirm entries for STANDARDS_LOG.md; moved the
SET_VERSION_ADOPTED target from docs/standards/ to docs/ so it survives the strip; added Step 8.5 (strip
the setup machinery as a second commit, with a set-cover safety check); retargeted the suite references
to Standard Set Version v1.1. Set Version v1.1.
v1.0 — 2026-06-07 — Initial release. One-shot bootstrap prompt: paste the fenced block into a fresh
Claude Code session to set up a new project from scratch on the v1.0 baseline. Replaces the long
HOW_TO_USE walkthrough as the headline setup path (HOW_TO_USE remains the supporting-prompt reference).
-->

# SETUP.md — One-shot project bootstrap

**What this is:** a single paste-and-run prompt. Open a fresh Claude Code session **in (or pointing at)
the new project's directory**, paste the whole fenced block below, and the agent sets the project up
from scratch on **Standard Set Version v1.6** — governance scaffold, customized contract, session
routines, project-data locality (Rule 14), governance scripts, CI, and a first commit. No push (operator-gated).

**Before you paste:** know where your canonical standards source lives on this machine (the folder that
contains this file and its sibling suite). You'll give that path as `SOURCE` in the prompt.

---

## The prompt (copy everything between the lines)

```
You are bootstrapping a NEW project from my domain-neutral standards suite (Standard Set Version v1.6).

PATHS
- SOURCE (canonical suite, read-only): <fill: e.g. ~/standards-source/docs/standards/ — the folder containing CLAUDE.md, LESSONS.md, the focused standards, SESSION_OPENER/CLOSER templates>
- TARGET (this new project's working dir): <fill: e.g. ~/projects/<name>/  — or "here" if you opened the session in it>

BINDING SESSION PROTOCOL (from message 1)
- ONE question / ONE step per message; WAIT for my reply before the next step.
- Render choices INLINE as lettered options "(a) … (b) …" — never popup/modal questions.
- Verify via filesystem (git status / ls / grep) before acting; never assume what's there.
- Don't fill placeholders silently — if a value is unclear, ASK.
- No hedges ("maybe", "optionally", "if applicable") — state an explicit decision or ask.
- Commit messages via `git commit -F /tmp/<file>.txt` (never -m with escapes; never heredoc piped to git commit).
- Code review (named, file-by-file) BEFORE `git add`. DO NOT PUSH — push is operator-gated.

DO THIS, IN ORDER

1. PRE-FLIGHT
   - Run `git -C <TARGET> rev-parse --show-toplevel`. If it resolves to a PARENT of TARGET (e.g. $HOME),
     STOP and warn me: the project has no repo of its own. With my OK, run `git init -b main` inside TARGET
     so it has its own repo (this shadows any parent .git). Confirm the new repo root.
   - Confirm SOURCE exists and contains: CLAUDE.md, LESSONS.md, the 7 focused standards
     (PROJECT_STANDARDS, PROMPT_STANDARDS, PROJECT_INSTRUCTIONS_TEMPLATE, MEMORY_PROTOCOL,
     ENGINEERING_STANDARDS, VALIDATION_STANDARDS, CICD_STANDARDS), SESSION_OPENER.md, SESSION_CLOSER.md,
     STANDARDS_INDEX.md, README.md, NEW_PROJECT_BOOTSTRAP.md, HOW_TO_USE.md, SETUP.md, STANDARDS_LOG.md,
     MEMORY_DURABILITY_ROLLOUT_PROMPT.md. Report any missing.

2. ASK ME THE PROJECT CONTEXT (one message, lettered options; propose a sensible default first):
   - Project name
   - Domain (one line)
   - Primary language(s)  [recommend Python 3.11+ unless I say otherwise]
   - Deployment shape  [(a) local CLI (b) Dockerized + CI → VPS (c) other]
   - Multi-agent?  [(a) no — single-agent, trim Codex § 14  (b) yes — keep § 14]
   - CI provider  [(a) GitHub Actions (b) GitLab CI (c) none]
   Then WAIT for my answers.

3. LAY DOWN THE SUITE (copy from SOURCE; do not modify SOURCE)
   - `CLAUDE.md`         → TARGET/CLAUDE.md
   - `LESSONS.md`        → TARGET/archive/LESSONS.md
   - 7 focused standards + STANDARDS_INDEX.md + README.md + NEW_PROJECT_BOOTSTRAP.md + HOW_TO_USE.md
     + SETUP.md + STANDARDS_LOG.md + MEMORY_DURABILITY_ROLLOUT_PROMPT.md + SESSION_OPENER.md
     + SESSION_CLOSER.md  → TARGET/docs/standards/
   - Instantiate project-local TARGET/docs/SESSION_OPENER.md and TARGET/docs/SESSION_CLOSER.md from the
     templates: delete the TEMPLATE-ONLY block (markers included); fill the PROJECT-OWNED heading block
     with this project's name; customize the PROJECT-OWNED blocks (§ 2 environment/registry mapping,
     § 3.2 project rows — branch name, no remote rows if there's no remote infra). § 3.1 (the universal
     catalog) stays suite-owned VERBATIM — project-specific patterns + N/A annotations go in § 3.2, so
     a future `sync` can update § 3.1. Keep every PROJECT-OWNED marker.

4. CUSTOMIZE CLAUDE.md (TARGET root)
   - § 1 project context — fill from my answers.
   - § 4 critical files — replace the <placeholders> with this project's real always-Major paths
     (always include docs/documents_manifest.md and CLAUDE.md itself).
   - § 13 — set the domain-behavior source-of-truth bullet to this project's reality.
   - § 14 — if single-agent, replace with a short "NOT IN USE (single-agent project)" stub and set
     § 1 Multi-agent = no; if multi-agent, keep § 14 and name the second agent.
   - Reset the header to this project's own VERSION 1.0 with a one-line "Project bootstrap" CHANGE LOG;
     Source line = "docs/standards/ (this repo). Bootstrapped from Standard Set v1.6 on <today>."
     (The v1.6 template CLAUDE.md already carries Rules 14–15; keep them — § 6.5 wires up the Rule 14 mechanism.)

5. BUILD SUPPORTING FILES
   - TARGET/README.md (short), TARGET/CHANGELOG.md (bootstrap entry), TARGET/.gitignore
     (OS/IDE/language + `docs/Plans/OPEN_TASKS.md` + `.claude/` — the project-data store stays
     untracked / sync-carried per Rule 14, never accidentally committed).
   - TARGET/docs/README.md, TARGET/docs/documents_manifest.md (list every tracked .md + VERSION-bearing
     code file), TARGET/docs/folder_structure.md, TARGET/docs/Plans/.gitkeep.
   - TARGET/docs/Plans/OPEN_TASKS.md — SEED the local-only open-tasks register (the single "what's open
     now" index, per L046). Gitignored above, so it is NOT committed / NOT manifest-tracked — but create
     it now so the register exists from day one with a standard header. Seed content:
     a `# OPEN_TASKS — local-only register` H1, a one-line "gitignored by design (L046); done = deleted"
     note, and a `_(no open items yet)_` placeholder.
   - TARGET/docs/STANDARDS_LOG.md — create from TARGET/docs/standards/STANDARDS_LOG.md, removing the
     example entry (the project's own experiences log; a kept file that survives the strip).
   - TARGET/docs/SET_VERSION_ADOPTED.md (Set Version v1.6, adopted <today>).

6. GOVERNANCE + CI
   - TARGET/scripts/check_doc_coverage.py + check_test_coverage_drift.py (permissive scaffolds, exit 0,
     VERSION 0.1) + doc_coverage_allowlist.toml + validation_ownership.toml (starters).
   - CI per my choice: GitHub → .github/workflows/governance.yml; GitLab → .gitlab-ci.yml + MR template;
     none → skip. Governance stage runs the two scripts on the default branch + PR/MR.

6.5 PROJECT-DATA LOCALITY (Rule 14, Standard Set Version v1.6+)
   Make this project's Claude data (memory + session transcripts) live INSIDE the project folder, so it
   survives a machine change / folder move. The contract text is already present (the v1.6 template
   CLAUDE.md Rule 14 + SESSION_OPENER § 1.5 you laid down in steps 3–4); this step wires up the
   mechanism, following TARGET/docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md:
   - Create TARGET/scripts/claude_project_data.sh per that prompt (verbs status / adopt / link; physical
     home `<repo>/.claude/project-data/`; symlink left at `~/.claude/projects/<path-key>/`, where
     <path-key> = the repo's absolute path with every non-alphanumeric character replaced by `-`).
   - Run `bash scripts/claude_project_data.sh link` (fresh project: creates the home + symlink); paste
     its output. If this machine already has harness data for this path, run `adopt` instead (one-time
     move-in; it also absorbs the pre-v1.6 memory-symlink layout).
   - Seed TARGET/docs/MACHINE_MIGRATION.md — the catalog of project state that cannot live in the folder
     (Rule 14 names it): a `# MACHINE_MIGRATION — out-of-folder state catalog` H1, a one-line
     "everything project-local lives in the folder (Rule 14); list here ONLY what cannot, with migration
     steps" note, and an empty two-column table (What | How to migrate). Register it in the manifest.
   - `.claude/` is gitignored (Step 5) so the store rides the project's sync but is never accidentally
     committed.
   - POSIX symlink — macOS/Linux. On Windows, adapt (directory junction) or keep the data synced by other means.

7. VALIDATE
   - `python scripts/check_doc_coverage.py` and `python scripts/check_test_coverage_drift.py --ci` → both
     exit 0; paste their stdout verbatim.
   - `git status --short` shows ONLY the intended files.

8. CODE REVIEW (Rule 10) — post a named review table (one verdict per file), then ASK "go on commit?".
   On my go: `git add -A`, re-check `git status --short`, then `git commit -F /tmp/bootstrap_commit_msg.txt`.
   DO NOT PUSH.

8.5 STRIP THE SETUP MACHINERY (a SEPARATE second commit in the target)
   The suite under TARGET/docs/standards/ was a transient delivery crate. Now that the operative
   standard is installed and committed (step 8), delete the setup/maintenance machinery so the project
   keeps only the operative standard. Make this its own commit ("strip setup machinery") so the
   delivered-then-removed transition is visible in the target's history.
   - SAFETY CHECK FIRST (set-cover): the KEEP set ∪ the DELETE set below MUST equal the current
     TARGET/docs/standards/ contents — no file unaccounted for. `ls TARGET/docs/standards/` and confirm
     every file is in exactly one list. If a file is in NEITHER, STOP and ask me — a new suite file may
     have been added since this prompt was written; never blind-delete.
   - KEEP in TARGET/docs/standards/ (the topical library, loaded by the dispatcher during normal work):
     PROJECT_STANDARDS.md, PROMPT_STANDARDS.md, MEMORY_PROTOCOL.md, ENGINEERING_STANDARDS.md,
     VALIDATION_STANDARDS.md, CICD_STANDARDS.md  (6 files)
   - DELETE from TARGET/docs/standards/ (machinery — only used to deliver/maintain the suite):
     CLAUDE.md (template), LESSONS.md (template), SESSION_OPENER.md (template),
     SESSION_CLOSER.md (template), STANDARDS_LOG.md (template), SETUP.md, NEW_PROJECT_BOOTSTRAP.md,
     STANDARDS_INDEX.md, README.md (meta), HOW_TO_USE.md, PROJECT_INSTRUCTIONS_TEMPLATE.md,
     MEMORY_DURABILITY_ROLLOUT_PROMPT.md (used once in § 6.5, then stripped)  (12 files)
   - NOT touched here (already living outside docs/standards/ as operative/kept files): TARGET/CLAUDE.md,
     TARGET/archive/LESSONS.md, TARGET/docs/SESSION_OPENER.md, TARGET/docs/SESSION_CLOSER.md,
     TARGET/docs/SET_VERSION_ADOPTED.md, TARGET/docs/STANDARDS_LOG.md, TARGET/docs/MACHINE_MIGRATION.md,
     TARGET/scripts/claude_project_data.sh, TARGET/.claude/project-data/ (kept, untracked), governance
     scripts, CI, manifest.
   - In the SAME strip commit, update TARGET/docs/documents_manifest.md + TARGET/docs/folder_structure.md
     to drop the stripped files (manifest completeness, Rule 8). Then code-review, `git add -A`, re-check
     `git status --short`, and `git commit -F /tmp/strip_commit_msg.txt`. DO NOT PUSH.

9. FINISH — summarize what shipped (files + commit SHA), and tell me the next step is feature work
   (CLAUDE.md is binding; for the first feature session see docs/standards/HOW_TO_USE.md § 4).

Start now with step 1 (pre-flight) and the one-question-at-a-time protocol.
```

---

## Notes

- **The compact version:** if you've done this before, you can trim the prompt — but keep the PATHS, the
  session protocol, "no push", and "start with pre-flight". The protocol is what prevents drift.
- **Retrofitting an existing repo?** Same prompt; in step 1 the repo already exists (init is a no-op),
  and in steps 3–6 the agent skips any file that already exists and bundles the rest into a single
  "adopt-standards" commit.
- **Why a prompt and not a script:** setup needs judgment (critical-file selection, single- vs
  multi-agent, CI choice, placeholder fills). The prompt encodes the procedure while keeping the
  operator in the loop at each decision and at the commit gate.
- For the detailed, click-through walkthrough behind this prompt, see `NEW_PROJECT_BOOTSTRAP.md`.
