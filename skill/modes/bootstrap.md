<!-- VERSION: 0.3 -->
<!-- Last Updated: 2026-10-08 -->
<!--
CHANGE LOG
v0.3 — 2026-10-08 — PLAN-018: § 6 — the locality script makes the Windows junction itself (since tool 0.2) and, on Windows, refuses while this session is live — the operator links from Git Bash afterwards; § 9 ends with the handoff report (SKILL.md).
v0.2 — 2026-08-19 — W-D1 fix: § 4 sync-ready SVA shape gains the required CHANGE LOG comment block — the engine's record-update (sync.py _split_header) hard-requires it; the spec omitted it, so the first live bootstrap shipped an SVA that failed on its first version delta.
v0.1 — 2026-08-16 — Initial (PLAN-009, Set v2.0). Successor to SETUP.md's one-shot prompt: same
procedure, but the lay-down COPIES the live vault suite (no generation) and no machinery ever
enters the target (no strip commit).
-->

# bootstrap mode — set up a NEW project

Precondition: SKILL.md Step 0 ran (`$VAULT` / `$SUITE` / `$SET_VERSION` / `$VAULT_SHA` resolved).

## 1. Target + pre-flight

- Ask for TARGET (the new project's working dir; "here" allowed). ONE question.
- `git -C <TARGET> rev-parse --show-toplevel`: if it resolves to a PARENT of TARGET (e.g. `$HOME`),
  STOP and warn — the project has no repo of its own. With the operator's OK, `git init -b main`
  inside TARGET. Confirm the new repo root.
- Confirm `$SUITE` contains: `CLAUDE.md`, `LESSONS.md`, the 6 topical standards
  (`PROJECT_STANDARDS`, `PROMPT_STANDARDS`, `MEMORY_PROTOCOL`, `ENGINEERING_STANDARDS`,
  `VALIDATION_STANDARDS`, `CICD_STANDARDS`), `PROJECT_INSTRUCTIONS_TEMPLATE.md`,
  `SESSION_OPENER.md`, `SESSION_CLOSER.md`, `STANDARDS_INDEX.md`, `STANDARDS_LOG.md`. Report any
  missing and STOP.

## 2. Project context (one message, lettered options, sensible defaults first)

Project name; domain (one line); primary language(s) [recommend Python 3.11+]; deployment shape
[(a) local CLI (b) Dockerized + CI → VPS (c) other]; multi-agent? [(a) no — single-agent, § 14
stub (b) yes — keep § 14]; CI provider [(a) GitHub Actions (b) GitLab CI (c) none]. WAIT.

## 3. Lay down the suite (COPY from `$SUITE` — read-only on the vault)

Nothing below is generated from memory — every suite file is copied from the live vault, then
instantiated where the templates say so. **No machinery file enters the target** (no SETUP/INDEX/
templates/meta — there is nothing to strip afterwards).

- `$SUITE/CLAUDE.md` → TARGET/`CLAUDE.md`, then instantiate: § 1 context from the answers; § 4
  critical files (always include `docs/documents_manifest.md` + `CLAUDE.md` itself); § 13
  domain-behavior bullet; § 14 — single-agent: replace the body with the "NOT IN USE" stub INSIDE
  the PROJECT-OWNED markers (never delete the block — sync's ordinal matching needs it);
  multi-agent: keep § 14 and name the second agent. Reset the header to VERSION 1.0 with a one-line
  "Project bootstrap" CHANGE LOG; Source line = "docs/standards/ (this repo). Bootstrapped from
  Standard Set $SET_VERSION (vault commit $VAULT_SHA) on <today>."
- `$SUITE/LESSONS.md` → TARGET/`archive/LESSONS.md` (verbatim).
- The 6 topical standards → TARGET/`docs/standards/` (verbatim).
- `$SUITE/PROJECT_INSTRUCTIONS_TEMPLATE.md` → NOT copied (vault-side reference; the dispatcher row
  in the instantiated CLAUDE.md § 12 still names it — the project loads it from the vault when that
  topic is in scope, via the curator).
- `$SUITE/SESSION_OPENER.md` + `SESSION_CLOSER.md` → instantiate to TARGET/`docs/SESSION_OPENER.md`
  + `docs/SESSION_CLOSER.md`: delete the TEMPLATE-ONLY block (markers included); fill the
  PROJECT-OWNED heading block with the project's name; customize the PROJECT-OWNED blocks (§ 2
  environment/registry mapping, § 3.2 project rows). § 3.1 (universal catalog) stays suite-owned
  VERBATIM. Keep every PROJECT-OWNED marker.
- `$SUITE/STANDARDS_LOG.md` → TARGET/`docs/STANDARDS_LOG.md`, removing the example entry (keep the
  schema/header).

## 4. Supporting files

- TARGET/`README.md` (short), `CHANGELOG.md` (bootstrap entry), `.gitignore` (OS/IDE/language +
  `docs/Plans/OPEN_TASKS.md` + `.claude/`).
- TARGET/`docs/README.md`, `docs/documents_manifest.md` (every tracked .md + VERSION-bearing code
  file), `docs/folder_structure.md`, `docs/Plans/.gitkeep`.
- TARGET/`docs/Plans/OPEN_TASKS.md` — seed the local-only register (gitignored; H1 + "gitignored by
  design (L046); done = deleted" note + `_(no open items yet)_`).
- TARGET/`docs/SET_VERSION_ADOPTED.md` — records: Standard Set Version `$SET_VERSION`, vault commit
  `$VAULT_SHA`, adopted <today>, delivered by the standard-docset skill (bootstrap mode). Write it
  **sync-ready** — the engine's mechanical record-update hard-requires this shape (SyncError
  otherwise): `<!-- VERSION: 0.1 -->` + `<!-- Last Updated: <today> -->` comment lines; a CHANGE
  LOG comment block — `<!--`, then `CHANGE LOG`, then the line `v0.1 — <today> — Adoption record
  created by the standard-docset skill (bootstrap mode): Standard Set Version $SET_VERSION, vault
  commit $VAULT_SHA.`, then `-->` — the record-update splits the header at this block's closing
  `-->` and prepends its own log line into it; omitting the block breaks every future
  record-update (W-D1); the two
  exact bullets `- **Standard Set Version:** $SET_VERSION (…)` and `- **Adopted on:** <today> (…)`;
  and a seeded backport table (header `| Set Version | Adopted on | Notes |`, separator
  `|---|---|---|`, one initial row for this adoption).

## 5. Governance + CI

- TARGET/`scripts/check_doc_coverage.py` + `check_test_coverage_drift.py` (permissive scaffolds,
  exit 0, VERSION 0.1) + `doc_coverage_allowlist.toml` + `validation_ownership.toml` (starters).
- CI per the answer: GitHub → `.github/workflows/governance.yml`; GitLab → `.gitlab-ci.yml` + MR
  template; none → skip. Governance stage runs the two scripts on the default branch + PR/MR.

## 6. Project-data locality (Rule 14)

- COPY `$VAULT/scripts/claude_project_data.sh` → TARGET/`scripts/claude_project_data.sh` VERBATIM
  (the script is path-independent — it resolves its repo from its own location).
- Run `bash scripts/claude_project_data.sh link` (fresh project). If this machine already has
  harness data for this path, run `adopt` instead. Paste the output — expect `STATUS: OK`.
- Seed TARGET/`docs/MACHINE_MIGRATION.md`: H1 `# MACHINE_MIGRATION — out-of-folder state catalog`,
  a one-line "everything project-local lives in the folder (Rule 14); list here ONLY what cannot,
  with migration steps" note, and an empty two-column table (What | How to migrate). Register it in
  the manifest.
- The script makes a symlink on macOS / Linux and a directory junction on Windows (Git Bash) by
  itself. On Windows it refuses while this very session is live (`ABORT: … looks active` — its
  transcript sits in the harness folder): that is expected, not a failure. Finish the bootstrap, then
  tell the operator to close Claude Code and run `bash scripts/claude_project_data.sh link` from a
  Git Bash window; list it as a follow-up in the handoff report.

## 7. Validate

- `python scripts/check_doc_coverage.py` and `python scripts/check_test_coverage_drift.py --ci` →
  both exit 0; paste stdout VERBATIM.
- `git status --short` shows ONLY the intended files.

## 8. Review + commit (single commit — there is no strip commit)

Post a named review table (one verdict per file), then ASK "go on commit?". On go:
`git add -A`, re-check `git status --short`, `git commit -F /tmp/bootstrap_commit_msg.txt`.
**DO NOT PUSH.**

## 9. Finish

Summarize what shipped (files + commit SHA). Tell the operator the two follow-ups:
(1) curator-side — register the project in the vault's `config/projects.toml` so `sync` maintains
it from now on; (2) project-side — first feature session opens per the new CLAUDE.md Rule 9
(SESSION_OPENER pre-flight).

Then write the handoff report (SKILL.md § Handoff report, mode `bootstrap`).
