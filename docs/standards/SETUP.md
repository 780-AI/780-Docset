<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.0 — 2026-06-07 — Initial release. One-shot bootstrap prompt: paste the fenced block into a fresh
Claude Code session to set up a new project from scratch on the v1.0 baseline. Replaces the long
HOW_TO_USE walkthrough as the headline setup path (HOW_TO_USE remains the supporting-prompt reference).
-->

# SETUP.md — One-shot project bootstrap

**What this is:** a single paste-and-run prompt. Open a fresh Claude Code session **in (or pointing at)
the new project's directory**, paste the whole fenced block below, and the agent sets the project up
from scratch on **Standard Set Version v1.0** — governance scaffold, customized contract, session
routines, governance scripts, CI, and a first commit. No push (operator-gated).

**Before you paste:** know where your canonical standards source lives on this machine (the folder that
contains this file and its sibling suite). You'll give that path as `SOURCE` in the prompt.

---

## The prompt (copy everything between the lines)

```
You are bootstrapping a NEW project from my domain-neutral standards suite (Standard Set Version v1.0).

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
     STANDARDS_INDEX.md, README.md, NEW_PROJECT_BOOTSTRAP.md, HOW_TO_USE.md, SETUP.md. Report any missing.

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
     + SETUP.md + SESSION_OPENER.md + SESSION_CLOSER.md  → TARGET/docs/standards/
   - Instantiate project-local TARGET/docs/SESSION_OPENER.md and TARGET/docs/SESSION_CLOSER.md from the
     templates (drop the "TEMPLATE" banner; customize §§ 2–3 for this project: branch name, the
     environment/registry mapping, failure-mode rows; no remote rows if there's no remote infra).

4. CUSTOMIZE CLAUDE.md (TARGET root)
   - § 1 project context — fill from my answers.
   - § 4 critical files — replace the <placeholders> with this project's real always-Major paths
     (always include docs/documents_manifest.md and CLAUDE.md itself).
   - § 13 — set the domain-behavior source-of-truth bullet to this project's reality.
   - § 14 — if single-agent, replace with a short "NOT IN USE (single-agent project)" stub and set
     § 1 Multi-agent = no; if multi-agent, keep § 14 and name the second agent.
   - Reset the header to this project's own VERSION 1.0 with a one-line "Project bootstrap" CHANGE LOG;
     Source line = "docs/standards/ (this repo). Bootstrapped from Standard Set v1.0 on <today>."

5. BUILD SUPPORTING FILES
   - TARGET/README.md (short), TARGET/CHANGELOG.md (bootstrap entry), TARGET/.gitignore
     (OS/IDE/language + `docs/Plans/OPEN_TASKS.md`).
   - TARGET/docs/README.md, TARGET/docs/documents_manifest.md (list every tracked .md + VERSION-bearing
     code file), TARGET/docs/folder_structure.md, TARGET/docs/Plans/.gitkeep.
   - TARGET/docs/standards/SET_VERSION_ADOPTED.md (Set Version v1.0, adopted <today>).

6. GOVERNANCE + CI
   - TARGET/scripts/check_doc_coverage.py + check_test_coverage_drift.py (permissive scaffolds, exit 0,
     VERSION 0.1) + doc_coverage_allowlist.toml + validation_ownership.toml (starters).
   - CI per my choice: GitHub → .github/workflows/governance.yml; GitLab → .gitlab-ci.yml + MR template;
     none → skip. Governance stage runs the two scripts on the default branch + PR/MR.

7. VALIDATE
   - `python scripts/check_doc_coverage.py` and `python scripts/check_test_coverage_drift.py --ci` → both
     exit 0; paste their stdout verbatim.
   - `git status --short` shows ONLY the intended files.

8. CODE REVIEW (Rule 10) — post a named review table (one verdict per file), then ASK "go on commit?".
   On my go: `git add -A`, re-check `git status --short`, then `git commit -F /tmp/bootstrap_commit_msg.txt`.
   DO NOT PUSH.

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
