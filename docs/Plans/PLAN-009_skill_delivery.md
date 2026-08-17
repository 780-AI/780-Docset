<!-- VERSION: 1.0 -->
<!-- Status: CLOSED -->
<!-- Last Updated: 2026-08-17 -->
<!--
CHANGE LOG
v1.0 — 2026-08-17 — CLOSED (D-5 stage 2, same day as the release commit). QA-E PASSED: real
Capital-Signal adoption via adopt mode (target commits `d0e0781` prep + `2caa53e` adopt; approved
dry-run list == applied set, 29 logical items, zero deviation; 20-section CLAUDE.md disposition
audit — nothing dropped silently; lessons delta vault 67 ⊇ CS 48 with zero leftovers; markers
4/3/2 engine-verified + live merge idempotence; E001 upstream defect — CLOSER template § 1.2
INDEX ref — logged to the pilot's STANDARDS_LOG, deliberately unpatched locally). QA-F PASSED:
pilot registered (vault commit `e9576d2`) + on the machine holding the target: status ADOPTED
v2.0 / VAULT v2.0 / current / open-log 1; sync dry-run up-to-date across all 11 SYNC_MAP items;
harvest surfaces E001 (also satisfies the PLAN-011 harvest-verification requirement). QA-A
COMPLETED (operator invoked the skill live; Step 0 reported v2.0 @ 66d45d5). § 11 R1/R3/R5/R8
annotated CLOSED. Phase 5 (push + annotated tag `set-v2.0`) remains operator-gated.
v0.3 — 2026-08-17 — Phase 3 release-commit session (fresh session per § 15.3). Reconcile pass:
11/11 § 5G–5K anchors byte-exact at the audited lines; all § 5F/5L–5Q structural claims verified;
zero blocking defects. Three named plan-defects fixed in-flight with disclosure (tracker has the
record): D1 architecture § 3 trailing strip-sentence (unenumerated, contradicted the new row);
D2 folder_structure STANDARDS_LOG caption "(SETUP copies…)"; D3 REAL (QA-B-found, Rule 15 class) —
§ 5B/§ 5C SVA bullets lacked the sync-ready shape `sync.record_adoption` hard-requires (VERSION
header + exact bullets + backport table → SyncError on a fresh delivery's first sync); both mode
files amended, then the engine's own `plan_target` run against the QA-B bootstrap: 11 files
validated, NO SyncError, all changed=False (sync no-op — converge once, sync forever proven).
Status → EXECUTING; § 4 Phase 3 commit-1 + Phase 4 QA ticks (QA-B/C/D/G ✅; QA-A partial —
fresh-session listing = operator confirm at the gate; QA-E/F pending, separate session per D-5).
v0.2 — 2026-08-16 23:40 — Rule 13 senior-review-and-optimize pass (recorded per § 15.8). Tools run
against the plan's own fenced bodies at final ship indentation: re-extracted § 5D + the § 5A Step 0
block → `bash -n` PASS on both; Step 0 SET_VERSION/VAULT_SHA pipeline exercised against the real
vault (prints v1.6 / c9898f0 — correct live values); all 11 § 5G–5K FIND anchors `grep -F`-verified
byte-exact (shellcheck unavailable on this machine — manual walk of § 5D branches done; ruff/mypy
N/A, no Python ships). FIXED: §§ 5G–5K FIND/REPLACE blocks rewritten from inline-code with
backslash-escaped backticks (would have made the implementer search for literal backslashes that
are not in the source — the L062 anchor-precision class) to fenced raw-text blocks; QA-D rewritten
from a vague sketch to a concrete scratch-clone procedure (behind-by-one pull + invalid-origin WARN
+ symlink restore). Consistency walk §§ 1–12 ↔ tracker: counts (§ 7.2 enumeration = 21), § 5 letter
references, QA ↔ acceptance mapping — no other contradictions found. Design decisions all surfaced
in § 9 (D-1…D-5), none silently resolved.
v0.1 — 2026-08-16 23:15 — Initial draft (Phase 0 audit + Phase 1 design, this session). Charter from
the operator-approved 2026-08-16 scope: skill-based delivery, TWO modes (bootstrap + adopt),
plugin-free dual route (concierge default + self-service vault clone), Set v2.0.
-->

# PLAN-009 — Skill-based suite delivery (bootstrap + adopt modes), Set Version v2.0

**Classification:** Vital (Critical Files: `docs/standards/` + `docs/architecture.md`) → full § 15
workflow. Big plan (Phase 3 spans 2 commits; Phase 4 is multi-scenario incl. a cross-session real
adoption) → sibling tracker `PLAN-009_tracker.md`.

---

## 1. Goal

Replace the paste-a-prompt delivery machinery (`SETUP.md` + `NEW_PROJECT_BOOTSTRAP.md` +
`MEMORY_DURABILITY_ROLLOUT_PROMPT.md`) with a **Claude Code skill** that delivers the suite to
projects in two modes:

- **bootstrap** — set up a NEW project from scratch (the SETUP.md procedure, skill-ified).
- **adopt** — migrate an EXISTING project onto the suite (dry-run gated; preserves the project's
  customizations; absorbs the MEMORY_DURABILITY_ROLLOUT_PROMPT retrofit).

The skill is **live-reference**: it carries NO copy of the suite. It resolves the vault through its
own symlink and reads `docs/standards/` directly, so there is no bundle, no export script, no
re-export step, and no new parity surface (the L053 fork class is removed structurally, not managed).

Retiring `SETUP.md` (+ NPB + MDRP) from the suite is structural per `STANDARDS_INDEX.md` § 5 →
**Standard Set Version v2.0** ("engine complete + skill delivery").

**Lifecycle principle (operator, 2026-08-16):** the skill converges a project once; the engine
`sync`s it forever.

## 2. Operator constraints (settled 2026-08-16 — binding for this plan)

1. **NO PLUGIN** — plugin-free dual route. Plugin packaging is explicitly DEFERRED (mechanical to
   add later if curator-bootstrap ever becomes a bottleneck).
2. **Concierge default:** team machines need NOTHING installed — the curator clones the team repo,
   runs the skill, delivers via push/MR, registers the target. Registration is already curator-side
   (`config/projects.toml` lives in the vault).
3. **Self-service option:** a team member with vault READ access clones the vault repo and runs
   `bootstrap_skill.sh` once (identical to the operator's Dropbox channel).
4. **Step 0 self-pull:** SKILL.md's first action is `git pull` on the vault repo the skill lives in
   — the skill self-updates at use time.
5. **Vault canonical:** the vault's `docs/standards/` stays the SINGLE canonical source. The skill
   never carries a hand-editable copy of suite content.
6. **Adopt-mode ship gate:** adopt mode ships only after a REAL adoption run against
   `EverOn.Capital-Signal` (Rule 15 feature-ON): intake-first, clean tree, dry-run would-change list
   reviewed → apply → post-diff verified against the list. Diff-based pass criteria (dormant
   project — nobody notices defects organically).
7. **Team contributions** flow ONLY via `STANDARDS_LOG.md` → `harvest`; vault write stays
   curator-only (no vault MRs/forks). The skill does not create any team write channel.
8. **Adopt mode's job includes the one-time v1.6 heading-wrap** (pre-v1.6 instances lack the
   PROJECT-OWNED heading block that `sync`'s ordinal matching needs — PLAN-008 § 11 R1/R6).

## 3. Scope summary

**In scope (Phase 3, commit 1 — the release commit):**

- New `skill/` top-level dir: `SKILL.md` + `modes/bootstrap.md` + `modes/adopt.md` (§ 5A–5C).
- New `scripts/bootstrap_skill.sh` — per-machine idempotent installer symlink (§ 5D).
- Retire from `docs/standards/`: `SETUP.md`, `NEW_PROJECT_BOOTSTRAP.md`,
  `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` (git rm; decisions D-3/D-4, § 9).
- Set Version **v2.0** release in `STANDARDS_INDEX.md` (§ 5F).
- Live-reference sweep of every live doc that points at the retired files (§ 5G–5K; enumerated in
  Phase 0 — frozen history is NOT retargeted: CHANGELOG entries, LESSONS bodies, SVA backport rows,
  committed plans, tracker history).
- Spec sync: `docs/architecture.md` §§ 3/4/8/10/11 + `docs/folder_structure.md` +
  `docs/documents_manifest.md` + `docs/SET_VERSION_ADOPTED.md` + `docs/NEW_MACHINE_SETUP.md` +
  `CHANGELOG.md` (§ 5L–5Q).
- Rider (per OPEN_TASKS deferred-minor convention "rides ANY next commit that touches the file"):
  `folder_structure.md` root-tree caption "13 standing rules" → "15 standing rules".

**In scope (Phase 3, commit 2 — the closure commit, after QA-E passes):**

- Plan + tracker promotion to v1.0/CLOSED + manifest promotion cells + CHANGELOG QA note.

**Out of scope:**

- PLAN-011 fleet rollout (per-project convergence order, intake runs, line retirement execution).
- DD-6b merge-request write-back (PLAN-011 prerequisite; needs `glab`/`gh`, not on this machine).
- Plugin packaging (deferred by constraint 1).
- Any engine (`src/`) change — adopters' on-disk footprint is unchanged; `sync` is unaffected.
- Rewriting `docs/standards/README.md` § 4's full manual walkthrough (Pattern A/B) — only the four
  delivery pointers are retargeted (§ 5H); a deeper README refresh is a separate Minor if wanted.
- Retro-editing append-only history (CHANGELOG, LESSONS L052/L053 bodies, SVA rows, docs/Plans/).

**Observed pre-existing gaps (not fixed here, recorded):** `folder_structure.md` standards/ tree
never listed `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` (nothing to remove); `HOW_TO_USE.md` line 109
still says "L001–L049" (stale since v1.0; untouched — outside the delivery sweep).

## 4. Phase tracker (high-level — sub-tasks live in `PLAN-009_tracker.md`)

| Phase | Status | Date |
|---|---|---|
| 0 — Audit | ✅ done | 2026-08-16 |
| 1 — Design (this file; Rule 13 pass at end) | ✅ done | 2026-08-16 |
| 2 — Operator approval (D9.A + D-1…D-5) | ✅ operator: "approved" = APPROVE D9.A; D-1…D-5 per recommendations | 2026-08-16 |
| 3 — Implement (commit 1: release; commit 2: closure after QA-E) | ✅ commit 1 `66d45d5`; commit 2 = this closure commit | 2026-08-17 |
| 4 — Validate (QA-A…QA-G; A/B/E are Rule 15 feature-ON gates) | ✅ all seven passed — QA-E pilot commits `d0e0781`+`2caa53e`; QA-F status/sync/harvest on the target's machine; evidence in the tracker | 2026-08-17 |
| 5 — Operator gate (push + tag `set-v2.0`) | ⏸ pending | — |

## 5. Transformation rules (verbatim, per Rule 7)

> Phase 3 extracts the fenced bodies below **byte-for-byte** (the PLAN-008 proven pattern). FIND
> blocks are anchored against the live source as of `c9898f0`; the implementer's reconcile pass
> (§ 15.3) re-verifies each anchor with `grep -F` before editing.

### 5A — NEW `skill/SKILL.md`

`````markdown
---
name: standard-docset
description: Deliver the Standard DocSet governance suite to a project. Bootstrap mode sets up a NEW project from scratch; adopt mode migrates an EXISTING project onto the suite (dry-run gated, customization-preserving). Use when asked to bootstrap, standardize, adopt, or converge a project onto the standards suite.
---
<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-08-16 -->
<!--
CHANGE LOG
v0.1 — 2026-08-16 — Initial (PLAN-009, Standard Set Version v2.0). Live-reference delivery skill:
two modes (bootstrap | adopt); replaces SETUP.md + NEW_PROJECT_BOOTSTRAP.md +
MEMORY_DURABILITY_ROLLOUT_PROMPT.md.
-->

# Standard DocSet — suite delivery skill

You are delivering a domain-neutral standards suite to a project. This skill carries **no copy** of
the suite — the vault it lives in is the single canonical source, and you read the suite LIVE from
it. You never edit the vault in a delivery session (read-only on `$VAULT`).

## Step 0 — self-update + resolve the vault (ALWAYS FIRST, before anything else)

```bash
SKILL_DIR="$(cd "$(readlink -f "$HOME/.claude/skills/standard-docset")" && pwd)"
VAULT="$(git -C "$SKILL_DIR" rev-parse --show-toplevel)"
git -C "$VAULT" pull --ff-only || echo "WARN: vault pull failed (offline / no remote / diverged) — proceeding with the local copy; surface this to the operator"
SUITE="$VAULT/docs/standards"
SET_VERSION="$(grep -m1 '^Standard Set Version:' "$SUITE/STANDARDS_INDEX.md" | awk '{print $NF}')"
VAULT_SHA="$(git -C "$VAULT" rev-parse --short HEAD)"
echo "Delivering Standard Set Version $SET_VERSION from vault commit $VAULT_SHA"
```

If `$SUITE` does not exist or `SET_VERSION` comes back empty, STOP and report — do not improvise a
suite location.

## Binding session protocol (from message 1)

- ONE question / ONE step per message; WAIT for the operator's reply before the next step.
- Render choices INLINE as lettered options "(a) … (b) …" — never popup/modal questions.
- Verify via filesystem (`git status` / `ls` / `grep`) before acting; never assume what's there.
- Don't fill placeholders silently — if a value is unclear, ASK.
- No hedges ("maybe", "optionally", "if applicable") — state an explicit decision or ask.
- Commit messages via `git commit -F /tmp/<file>.txt` (never `-m` with escapes; never heredoc piped
  to `git commit`).
- Named, file-by-file code review BEFORE `git add`. **DO NOT PUSH** — push is operator-gated.

## Mode selection (one question)

Ask the operator:

> Which delivery mode? (a) **bootstrap** — brand-new project (empty or nearly-empty repo);
> (b) **adopt** — existing project migrating onto the suite.

Then read the matching file from this skill's directory and follow it exactly, in order:

- bootstrap → `modes/bootstrap.md`
- adopt → `modes/adopt.md`

If the operator says the project is an **old-SETUP adopter** (already carries the suite, just a
stale Set Version), neither mode applies — tell them the path is: register the project in the
vault's `config/projects.toml`, hand-apply the one-time v1.6 heading-wrap if it predates v1.6, and
let `sync` catch it up. Do not run a delivery mode over an existing adopter.
`````

### 5B — NEW `skill/modes/bootstrap.md`

`````markdown
<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-08-16 -->
<!--
CHANGE LOG
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
  `$VAULT_SHA`, adopted <today>, delivered by the standard-docset skill (bootstrap mode).

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
- POSIX symlink — macOS/Linux. On Windows, adapt (directory junction) and say so.

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
`````

### 5C — NEW `skill/modes/adopt.md`

`````markdown
<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-08-16 -->
<!--
CHANGE LOG
v0.1 — 2026-08-16 — Initial (PLAN-009, Set v2.0). Migration mode for EXISTING projects: dry-run
gated, customization-preserving; absorbs the MEMORY_DURABILITY_ROLLOUT_PROMPT retrofit; performs
the one-time v1.6 heading-wrap sync needs.
-->

# adopt mode — migrate an EXISTING project onto the suite

Precondition: SKILL.md Step 0 ran (`$VAULT` / `$SUITE` / `$SET_VERSION` / `$VAULT_SHA` resolved).

**This is a migration, not a bootstrap.** The worst case is clobbering the project's own
customizations — therefore NOTHING is written before the operator approves the dry-run list (§ 4).

## 1. Target + pre-flight gates (all three are hard gates)

- Ask for TARGET. Confirm it is a git repo (`git -C <TARGET> rev-parse --show-toplevel`).
- **Clean tree required:** `git -C <TARGET> status --short` must be empty. Otherwise STOP — the
  operator commits or stashes first (the adoption diff must stand alone).
- Ask the operator which state the project is in: (a) never-standardized; (b) old-SETUP adopter
  (carries the suite at an older Set Version); (c) divergent line (evolved its own variant of the
  suite). If (b): STOP — no adoption needed; the path is register + one-time v1.6 heading-wrap +
  `sync` catch-up (see SKILL.md).

## 2. Intake-first check

Ask: does this project hold novelties the vault should learn from (its own lessons, rules,
conventions)? If yes and they have not been intaken, PAUSE adoption and tell the operator the
intake flow runs FIRST (grab → genericize → vault — the PLAN-010 pattern, curator-side). Adoption
NEVER copies target novelties into the vault silently, and it must not overwrite them locally
before they are captured.

## 3. Inventory + mapping table (posted in chat, before any dry-run)

Walk the target and post one table: existing artifact → suite slot → planned action
(`keep` | `wrap in PROJECT-OWNED` | `merge` | `replace` | `create`). Cover at minimum:

- Root `CLAUDE.md` (or equivalent contract): its project-specific content (§ 1 context, § 4
  critical files, § 13 domain bullet, § 14 agency) maps INTO the suite template's PROJECT-OWNED
  blocks; local rules map to the matching vault rule number, or to project-specific rows/sections.
- Any existing lessons archive: entries stay in the project; portable candidates become
  `STANDARDS_LOG.md` `E0NN` entries (`Status: open`) for `harvest` — they are NOT merged into the
  suite's `LESSONS.md` (that file arrives suite-owned from the vault).
- Session opener/closer files (any form) → instantiated suite templates with the project's § 2
  registry + § 3.2 rows carried over; **the PROJECT-OWNED instance-heading wrap is applied** (the
  v1.6 requirement sync's ordinal matching needs).
- Governance scripts / CI / manifest / folder-structure docs: keep what exists and works; create
  the missing scaffolds.

## 4. DRY-RUN GATE (hard)

Post the full would-change list — every file to be created, replaced, merged, or wrapped, with a
one-line "what changes" per file — and WAIT for the operator's written approval. Nothing is
written before that approval. If the run later deviates from the approved list, STOP and re-gate.

## 5. Apply (only after § 4 approval)

Per the approved list, copying suite content from `$SUITE` (read-only on the vault), preserving
every mapped customization inside PROJECT-OWNED markers. Also:

- TARGET/`docs/SET_VERSION_ADOPTED.md` — Standard Set Version `$SET_VERSION`, vault commit
  `$VAULT_SHA`, adopted <today>, delivered by the standard-docset skill (adopt mode).
- TARGET/`docs/STANDARDS_LOG.md` — instantiate from `$SUITE/STANDARDS_LOG.md` (drop the example)
  if absent; existing log kept as-is.
- Project-data locality (Rule 14): COPY `$VAULT/scripts/claude_project_data.sh` verbatim; run
  `adopt` (machine already has harness data for this path) or `link`; paste output; seed
  `docs/MACHINE_MIGRATION.md` if absent; ensure `.claude/` + `docs/Plans/OPEN_TASKS.md` are
  gitignored; seed `OPEN_TASKS.md` if absent.
- Governance scaffolds (the two check scripts + TOMLs) if absent — never overwrite existing ones.

## 6. Validate

- Governance scripts exit 0 (paste stdout verbatim).
- Marker integrity: every `PROJECT-OWNED:BEGIN` has its `END`; the three mixed files carry the
  instance-heading block; counts match the template (sync's strict count check will enforce this —
  verify it here first).
- `git status --short` matches the approved § 4 list EXACTLY — any extra/missing file is a STOP.

## 7. Review + commit

Named review table → "go on commit?" → `git add -A`, re-check `git status --short`,
`git commit -F /tmp/adopt_commit_msg.txt` (single "adopt-standards" commit). **DO NOT PUSH.**

## 8. Post-adopt (curator-side, outside this session)

(1) Register the project in the vault's `config/projects.toml` (transport per where it lives);
(2) run a vault-side `sync` dry-run — a freshly-adopted target should report current/no-op;
(3) the project's log-recording discipline is now binding: new experience lands ONLY as `E0NN`
entries in its `STANDARDS_LOG.md` (`Status: open`), harvested by the vault — never as edits to its
own suite files.
`````

### 5D — NEW `scripts/bootstrap_skill.sh`

```bash
#!/usr/bin/env bash
# ==============================================================
# VERSION: 0.1
# Per-machine installer for the standard-docset delivery skill: symlinks
# ~/.claude/skills/standard-docset -> <this repo>/skill so Claude Code loads
# the skill from the live vault (PLAN-009, Set v2.0). Idempotent; machine-local
# state cataloged in docs/NEW_MACHINE_SETUP.md per CLAUDE.md Rule 14.
#
# CHANGE LOG
# v0.1 — 2026-08-16 — Initial (PLAN-009).
# ==============================================================
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$REPO/skill"
LINK="$HOME/.claude/skills/standard-docset"

[ -f "$TARGET/SKILL.md" ] || { echo "ERROR: $TARGET/SKILL.md missing — run from a vault checkout."; exit 1; }

mkdir -p "$HOME/.claude/skills"
if [ -L "$LINK" ]; then
  current="$(readlink "$LINK")"
  if [ "$current" = "$TARGET" ]; then
    echo "Already installed: $LINK -> $TARGET"
    exit 0
  fi
  echo "Re-pointing (was -> $current)"
  rm "$LINK"
elif [ -e "$LINK" ]; then
  echo "ERROR: $LINK exists and is not a symlink — resolve manually."
  exit 1
fi
ln -s "$TARGET" "$LINK"
echo "Installed: $LINK -> $TARGET"
echo "New Claude Code sessions on this machine will list the 'standard-docset' skill."
```

### 5E — Retirements (git rm)

```bash
git rm docs/standards/SETUP.md
git rm docs/standards/NEW_PROJECT_BOOTSTRAP.md          # per D-3 (§ 9)
git rm docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md   # per D-4 (§ 9)
```

No archive copies: git history is the archive (`c9898f0` and earlier hold every retired file; the
v2.0 § 6 history entry names them). `archive/` stays lessons-only.

### 5F — `docs/standards/STANDARDS_INDEX.md` → v2.0 (header bump 1.6 → 2.0)

1. **§ 1 block** — replace the four lines inside the fence with:

   ```
   Standard Set Version: v2.0
   Released:             <implement-date>
   Baseline:             v1.x line (v1.0 baseline … sync-enablement markers v1.6) + skill delivery: the SETUP/NEW_PROJECT_BOOTSTRAP/MEMORY_DURABILITY_ROLLOUT_PROMPT machinery is retired in favor of the vault-side live-reference delivery skill (PLAN-009).
   Adopter contract:     11 binding files + 3 meta files (+ STANDARDS_LOG.md); 67 lessons (L001–L067); 15 standing rules in CLAUDE.md
   ```

2. **§ 2 Tier 2 table** — remove the `NEW_PROJECT_BOOTSTRAP.md` row (#3), the `SETUP.md` row (+),
   and the `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` row (+); renumber remaining meta rows 1–3
   (README, STANDARDS_INDEX, HOW_TO_USE) keeping the `STANDARDS_LOG.md` "+" row. Update the
   `HOW_TO_USE.md` row's Role cell to: `Practical usage guide — supporting prompts (Day-One, code
   review, audit); delivery is the vault-side skill`. Add below the table:

   > **Delivery (not part of the set):** the suite is delivered by the vault-side skill
   > (`skill/SKILL.md` + `skill/modes/` + `scripts/bootstrap_skill.sh`) — live-reference vault
   > machinery, versioned in the vault's own manifest, never copied to adopters.

3. **§ 3 per-file table** — remove the `NEW_PROJECT_BOOTSTRAP.md`, `SETUP.md`, and
   `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` rows; bump the cells for files edited in this release
   (README 1.1, HOW_TO_USE 1.1, STANDARDS_LOG 1.1, SESSION_OPENER 1.7, SESSION_CLOSER 1.5,
   STANDARDS_INDEX 2.0); totals line → `**Total file count:** 15 (11 binding + 4 meta).`

4. **§ 4** — replace the intro sentence pair with:

   > The delivery path is the **standard-docset skill** (vault-side): concierge — the curator runs
   > it against the target; or self-service — clone the vault repo and run
   > `bash scripts/bootstrap_skill.sh` once, then invoke the skill in a session opened at the
   > target. Bootstrap mode covers new projects; adopt mode migrates existing ones (dry-run gated).

   § 4.2 (drift management) is unchanged.

5. **§ 5** — unchanged (live-reference means NO release-procedure step is added; record that
   explicitly in the § 6 entry).

6. **§ 6** — add at top a `### v2.0 — <date> — Skill delivery (machinery retired)` entry:
   structural Major; names the three retired files; states the adopter-migration note verbatim:
   *"No adopter action required — the retired files were setup machinery that never survived in
   adopters (the strip removed them), so no adopter footprint changes and `sync` is unaffected.
   New deliveries use the skill; old-SETUP adopters just register + heading-wrap + sync."* Also
   records: live-reference design (no bundle, no re-export step — the L053 parity class removed
   structurally), the concierge/self-service dual route, and the adopt-mode Capital-Signal gate
   (named only as "a real pilot adoption" — the suite file stays domain-neutral).

> §§ 5G–5K FIND blocks are raw text (fenced), byte-exact against the live source and
> `grep -F`-verified 2026-08-16. Apply each as an exact single-line (or single-sentence)
> substitution; "delete" means remove the whole line/row.

### 5G — `docs/standards/HOW_TO_USE.md` (1.0 → 1.1)

G1 — FIND:
```text
- **Bootstrap a new project →** use **`SETUP.md`** (a single paste-and-run prompt).
```
G1 — REPLACE:
```text
- **Bootstrap or adopt a project →** the **standard-docset delivery skill** (vault-side; see `STANDARDS_INDEX.md` § 4).
```
G2 — FIND (delete the whole line):
```text
- **Detailed click-through walkthrough →** `NEW_PROJECT_BOOTSTRAP.md`.
```
G3 — FIND:
```text
- **Bootstrapping now?** → `SETUP.md`.
```
G3 — REPLACE:
```text
- **Bootstrapping now?** → the standard-docset delivery skill (`STANDARDS_INDEX.md` § 4).
```

### 5H — `docs/standards/README.md` (1.0 → 1.1)

H1 — FIND:
```text
| **Adopt these standards in a new project** | `NEW_PROJECT_BOOTSTRAP.md` (detailed walkthrough); `HOW_TO_USE.md` § 3 (copy-paste bootstrap prompt) |
```
H1 — REPLACE:
```text
| **Adopt these standards in a new project** | the standard-docset delivery skill (vault-side; `STANDARDS_INDEX.md` § 4) |
```
H2 — FIND (delete the whole table row):
```text
| `NEW_PROJECT_BOOTSTRAP.md` | Humans adopting the suite | Detailed Day-Zero walkthrough: how to start a new project from this template (copy commands, customization, first commit, supporting scripts, CI scaffold) |
```
H3 — FIND:
```text
> **Detailed Day-Zero walkthrough:** See `NEW_PROJECT_BOOTSTRAP.md` for the full step-by-step bootstrap procedure (copy commands, customization checklist tied to placeholders, governance script setup, CI scaffold, first commit). The summary below is the orientation; the bootstrap file is the dispositive walkthrough.
```
H3 — REPLACE:
```text
> **Delivery note (Set v2.0):** bootstrap/adopt is performed by the vault-side standard-docset skill (`STANDARDS_INDEX.md` § 4). The walkthrough below is retained as orientation for the manual pattern.
```
H4 — FIND:
```text
Before any feature work, set up the governance scaffold. Order matters. **The procedure summarized below is implemented in full detail in `NEW_PROJECT_BOOTSTRAP.md`** — read both, follow the bootstrap file's commands.
```
H4 — REPLACE:
```text
Before any feature work, set up the governance scaffold. Order matters. **The operational path is the delivery skill (bootstrap mode)** — the steps below are the orientation.
```

### 5I — `docs/standards/STANDARDS_LOG.md` (1.0 → 1.1)

I1 — FIND:
```text
<!-- TEMPLATE — SETUP.md copies this to docs/STANDARDS_LOG.md and removes the example entry. -->
```
I1 — REPLACE:
```text
<!-- TEMPLATE — the delivery skill copies this to docs/STANDARDS_LOG.md and removes the example entry. -->
```
I2 — FIND:
```text
> (SETUP.md does this automatically when it instantiates the project's copy).
```
I2 — REPLACE:
```text
> (the delivery skill does this automatically when it instantiates the project's copy).
```

### 5J — `docs/standards/SESSION_OPENER.md` template (1.6 → 1.7)

J1 — FIND (sentence within line 252; keep the rest of the line intact):
```text
If you are reading this in a freshly-bootstrapped project, your next step is to walk `NEW_PROJECT_BOOTSTRAP.md` Step <N> to instantiate the project-local copy and customize §§ 2 + 3.
```
J1 — REPLACE:
```text
If you are reading this in a freshly-bootstrapped project, the delivery skill instantiates the project-local copy and customizes §§ 2 + 3 during bootstrap.
```

### 5K — `docs/standards/SESSION_CLOSER.md` template (1.4 → 1.5)

K1 — FIND (sentence within line 279; keep the rest of the line intact):
```text
If you are reading this in a freshly-bootstrapped project, your next step is to walk `NEW_PROJECT_BOOTSTRAP.md` to instantiate the project-local copy and customize §§ 2 + 4 output-block specifics.
```
K1 — REPLACE:
```text
If you are reading this in a freshly-bootstrapped project, the delivery skill instantiates the project-local copy and customizes §§ 2 + 4 output-block specifics during bootstrap.
```

### 5L — `docs/architecture.md` (0.10 → 0.11)

1. § 3 table, machinery row — REPLACE the row's "In project?" rationale: machinery **never enters
   the project** (Set v2.0: delivery is the vault-side skill; the crate/strip mechanism is retired
   for new deliveries; the row's file list gains "(retired from the suite at v2.0: SETUP /
   NEW_PROJECT_BOOTSTRAP / MEMORY_DURABILITY_ROLLOUT_PROMPT)").
2. § 4 — retitle `## 4. Delivery (vault → project): the skill` and replace the numbered body:
   skill resolves the vault via its own symlink (step-0 self-pull), COPIES the operative files
   directly from the live `docs/standards/`, instantiates the mixed files, stamps
   `SET_VERSION_ADOPTED.md` with Set Version + vault commit; **no crate, no strip**; two modes
   (bootstrap | adopt — adopt is dry-run gated and performs the v1.6 heading-wrap); concierge
   default / self-service clone; the old SETUP.md path is retired (v2.0).
3. § 8 table — REPLACE the `setup` row with:
   `| \`skill\` (bootstrap \| adopt) | the live vault suite | the new/adopting project | operator-run Claude Code skill (\`skill/SKILL.md\`); adopt mode dry-run gated |`
4. § 10 — append: `6. ✅ **Delivery layer — the standard-docset skill** (done — PLAN-009, Set
   Version v2.0). Live-reference skill (bootstrap + adopt) + per-machine installer; SETUP/NPB/MDRP
   retired.`
5. § 11 — append a `✅ DECIDED (PLAN-009)` block recording D-1…D-5 (§ 9 of this plan).

### 5M — `docs/folder_structure.md` (0.13 → 0.14)

- Root tree: add after the `docs/` block's `Plans/` lines:
  ```
  ├── skill/                         # delivery skill (live-reference; PLAN-009) — symlinked to ~/.claude/skills/standard-docset by scripts/bootstrap_skill.sh
  │   ├── SKILL.md                   # mode dispatch + step-0 vault resolve/self-pull
  │   └── modes/
  │       ├── bootstrap.md           # NEW-project delivery (successor to SETUP.md)
  │       └── adopt.md               # EXISTING-project migration (dry-run gated)
  ```
- `scripts/` block: add `bootstrap_skill.sh` line (`# per-machine skill installer (idempotent symlink)`).
- `docs/standards/` block: remove the `SETUP.md` and `NEW_PROJECT_BOOTSTRAP.md` lines; suite
  caption `(Set Version v1.6)` → `(Set Version v2.0)`.
- Rider: root-tree CLAUDE.md caption `# operating contract (binding; 13 standing rules)` →
  `(binding; 15 standing rules)`.

### 5N — `docs/SET_VERSION_ADOPTED.md` (1.7 → 1.8)

Add the v2.0 backport row + header CHANGE LOG line: vault self-adopts v2.0 same-commit (machinery
retirement — no operative-footprint change; counts unchanged 15 rules / 67 lessons).

### 5O — `docs/NEW_MACHINE_SETUP.md` (1.1 → 1.2)

Add a section after the project-data link section: **Delivery-skill symlink** — machine-local state
(`~/.claude/skills/standard-docset`); restore with `bash scripts/bootstrap_skill.sh` (idempotent);
add the matching row to the Rule 14 catalog intro list.

### 5P — `docs/documents_manifest.md` (design commit → 2.18; implement commit → 2.19)

- **Design commit (with approval):** append PLAN-009 + tracker rows (0.1 / DRAFT→APPROVED); bump
  self-row 2.17 → 2.18; quick-index Plans range += the two new entries.
- **Implement commit:** append rows for `skill/SKILL.md`, `skill/modes/bootstrap.md`,
  `skill/modes/adopt.md`, `scripts/bootstrap_skill.sh` (all 0.1); DELETE the rows for the three
  retired files (row removal, no renumbering of surviving entries); bump every § 6-mapped cell;
  self-row → 2.19 (grep-verify stamp vs log per L063).
- **Closure commit:** promote PLAN-009 + tracker rows to 1.0 / CLOSED; self-row → 2.20.

### 5Q — `CHANGELOG.md`

- **Design commit:** `PLAN-009 (APPROVED D9.A): skill-based delivery — design + tracker` entry.
- **Implement commit:** release entry (Set v2.0; skill ships; three retirements; QA scenarios
  sub-section per Rule 11 naming QA-A…QA-G with initial statuses).
- **Closure commit:** QA-E/QA-F verdict note + plan closure.

## 6. Spec update map (same-commit sync triggers)

| Artifact | Update | Commit |
|---|---|---|
| `docs/architecture.md` | § 5L (drift rule: behavior toward delivery changes) | implement |
| `docs/folder_structure.md` | § 5M (new top-level dir) | implement |
| `docs/standards/STANDARDS_INDEX.md` | § 5F (v2.0 release) | implement |
| `docs/documents_manifest.md` | § 5P (rows + cells, Rule 8) | all three |
| `docs/SET_VERSION_ADOPTED.md` | § 5N (vault self-adoption) | implement |
| `docs/NEW_MACHINE_SETUP.md` | § 5O (Rule 14 catalog) | implement |
| `CHANGELOG.md` | § 5Q | all three |
| Memories (`project_skill_based_delivery`, `project_target_registration_deferred`, `feedback_domain_neutral_no_project_names`, `project_suite_dual_nature`) | post-ship at wrap-up (memory layer, not commit-bound) | after closure |
| Git tag | `set-v2.0` annotated tag at Phase 5 (operator push gate) | after implement |

## 7. ALLOWLIST (the bullet enumeration IS the count — L038; plan + tracker included per L054)

### 7.1 Design commit (rides D9.A approval; 4 files)

- `docs/Plans/PLAN-009_skill_delivery.md` (new)
- `docs/Plans/PLAN-009_tracker.md` (new)
- `docs/documents_manifest.md` (2 new rows + self-row)
- `CHANGELOG.md` (entry)

### 7.2 Phase 3 implement commit (21 files)

- `skill/SKILL.md` (new — § 5A)
- `skill/modes/bootstrap.md` (new — § 5B)
- `skill/modes/adopt.md` (new — § 5C)
- `scripts/bootstrap_skill.sh` (new — § 5D)
- `docs/standards/SETUP.md` (DELETE — § 5E)
- `docs/standards/NEW_PROJECT_BOOTSTRAP.md` (DELETE — § 5E, per D-3)
- `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md` (DELETE — § 5E, per D-4)
- `docs/standards/STANDARDS_INDEX.md` (§ 5F)
- `docs/standards/HOW_TO_USE.md` (§ 5G)
- `docs/standards/README.md` (§ 5H)
- `docs/standards/STANDARDS_LOG.md` (§ 5I)
- `docs/standards/SESSION_OPENER.md` (§ 5J)
- `docs/standards/SESSION_CLOSER.md` (§ 5K)
- `docs/architecture.md` (§ 5L)
- `docs/folder_structure.md` (§ 5M)
- `docs/SET_VERSION_ADOPTED.md` (§ 5N)
- `docs/NEW_MACHINE_SETUP.md` (§ 5O)
- `docs/documents_manifest.md` (§ 5P)
- `CHANGELOG.md` (§ 5Q)
- `docs/Plans/PLAN-009_skill_delivery.md` (status DRAFT→EXECUTING; § 4 ticks)
- `docs/Plans/PLAN-009_tracker.md` (Phase 3 ticks + QA-A…QA-D evidence)

### 7.3 Closure commit (after QA-E/QA-F; 4 files)

- `docs/Plans/PLAN-009_skill_delivery.md` (promote 1.0 / CLOSED)
- `docs/Plans/PLAN-009_tracker.md` (promote 1.0 / CLOSED; QA-E/F evidence)
- `docs/documents_manifest.md` (promotion cells + self-row)
- `CHANGELOG.md` (closure note)

`~/.claude/skills/standard-docset` (created by running § 5D) is machine-local, outside the repo,
and cataloged in § 5O — it never appears in `git status`.

## 8. Validation gate (Rule 11 scenarios; Rule 15 feature-ON marked ⚑)

Run in the implement session unless noted. Evidence pasted verbatim into the tracker.

- **QA-A ⚑ Skill discovery + invocation.** Run `bash scripts/bootstrap_skill.sh`; open a FRESH
  Claude Code session anywhere; the `standard-docset` skill is listed; invoking it executes Step 0
  and reports `Delivering Standard Set Version v2.0 from vault commit <sha>`. Pass = exact report
  line with the live values. (Verifies the loader-follows-symlink fact + live supporting-file
  reads end-to-end.)
- **QA-B ⚑ Bootstrap mode end-to-end.** Scratch target dir; run bootstrap mode through commit.
  Pass = operative footprint present (root CLAUDE.md instantiated, 6 topical files, archive
  LESSONS, session instances with markers, STANDARDS_LOG, SVA stamped `v2.0` + vault sha,
  locality `STATUS: OK`, OPEN_TASKS seeded); ZERO machinery files anywhere in the target;
  governance scripts exit 0 (stdout pasted); single commit; no push. Supersedes the standing
  OPEN_TASKS "SETUP.md end-to-end live test" item (mark ⏭ superseded there at ship).
- **QA-C Installer idempotence.** `bootstrap_skill.sh` twice → second run prints
  `Already installed:` and exits 0; re-point case: point the link elsewhere, run again → re-points.
- **QA-D Step-0 self-pull.** Without touching the real vault: `git clone` the vault to a scratch
  dir (its `origin` = the vault via `file://`); `git -C <scratch> reset --hard HEAD~1` so the clone
  is one commit behind; temporarily re-point `~/.claude/skills/standard-docset` → `<scratch>/skill`;
  run the Step 0 block → observe the fast-forward pull and the report line showing the vault-tip
  sha. Then set the scratch clone's origin URL to an invalid path and re-run → observe the WARN
  line + proceed-on-local-copy. Restore the symlink via `bootstrap_skill.sh` (the QA-C re-point
  path). Pass = both behaviors observed + symlink restored.
- **QA-E ⚑ Adopt mode — REAL pilot (ship gate for adopt mode; separate session, PLAN-011 pilot).**
  Target: `EverOn.Capital-Signal` (operator decision 2026-08-16). Intake-first walked; clean tree;
  § 4 dry-run list posted and operator-approved; apply; **post-diff verified line-for-line against
  the approved list** (diff-based pass criteria); marker/count integrity checks pass. Any
  expected≠observed = defect → fix-forward per Rule 3.
- **QA-F Post-adopt sync no-op.** After QA-E: register the pilot in `config/projects.toml`;
  vault-side `sync` dry-run reports the target current (no writes proposed beyond none).
- **QA-G Domain-neutral + reference sweep (greps, zero-hit gates).**
  `grep -rn "EverOn\|Capital-Signal\|Equinex" docs/standards/ skill/` → zero hits;
  `grep -rn "SETUP\.md\|NEW_PROJECT_BOOTSTRAP\|MEMORY_DURABILITY_ROLLOUT_PROMPT" docs/standards/ skill/ docs/architecture.md docs/folder_structure.md docs/NEW_MACHINE_SETUP.md` → hits ONLY in
  append-only history blocks (CHANGE LOG comments, INDEX § 6 history, L052/L053 lesson bodies);
  governance scripts exit 0.

**Rule 15 compliance:** QA-A/B gate the release commit (run before it ships). QA-E gates adopt
mode and plan closure — it cannot be waived silently; deferring it requires an explicit operator
waiver recorded in the tracker. QA-D exercises the self-update path.

## 9. Operator decision points (Phase 2 — answer with the approval)

- **D9.A — approve the plan** (required to commit the design + proceed to Phase 3).
- **D-1 — live-reference vs copy-bundle.** RECOMMEND live-reference (spike-backed: symlinked skill
  dirs documented as supported; FS probes — CloudStorage resolution, two-link chain, physical `..`,
  pathlib — all passed 2026-08-16; kills the export script, the re-export release step, and the
  parity surface). Copy-bundle remains the fallback if QA-A ever fails.
- **D-2 — new top-level dir `skill/`** (explicit approval required per § 8 checklist). Alternatives
  considered: `delivery/` (vaguer), `docs/skill/` (not documentation).
- **D-3 — NEW_PROJECT_BOOTSTRAP.md: retire (recommended) or keep.** RECOMMEND retire: the
  walkthrough duplicates what the skill does interactively; keeping it re-creates the L053 parity
  set the plan exists to kill. Git history preserves it.
- **D-4 — MEMORY_DURABILITY_ROLLOUT_PROMPT.md: retire (recommended) or keep.** Its own v1.2 header
  already says "PLAN-009 will absorb this prompt into the setup skill's retrofit mode" — adopt
  mode § 5 does. RECOMMEND retire.
- **D-5 — two-stage close.** Phase 3 release commit ships bootstrap mode fully verified (QA-A…D);
  the plan stays EXECUTING until QA-E (the real Capital-Signal adoption) passes, then a small
  closure commit promotes plan + tracker (deliberate deviation from § 15.2's same-commit
  promotion, forced by Rule 15: adopt-mode's feature-ON evidence cannot exist before a real
  adoption runs). RECOMMEND approve as designed.

## 10. Rollback path

- **Before push:** single `git revert` of the release commit restores SETUP/NPB/MDRP, removes
  `skill/` + installer, and reverts every doc edit (one commit = one revert). Remove the local
  symlink with `rm ~/.claude/skills/standard-docset`.
- **After push/tag:** fix-forward per Rule 3 (letter-suffix commits); the retired files are
  recoverable from history (`git show c9898f0:docs/standards/SETUP.md` etc.) if a fallback
  delivery path is ever needed.
- **Adopt-mode pilot failure (QA-E):** the pilot commit in the target is a single revert there;
  the vault plan stays EXECUTING and fix-forwards.

## 11. Known risks + mitigation

| # | Risk | Mitigation |
|---|---|---|
| R1 | Supporting-file reads at use time are docs-silent (only SKILL.md loading via symlink is documented) | FS probes passed (2026-08-16); QA-A/B exercise the full path before the release commit ships; D-1 fallback = copy-bundle — **CLOSED 2026-08-17** (QA-A/B passed; live delivery read every supporting file) |
| R2 | Skill invisible on a machine that never ran the installer | By design (concierge — team machines need nothing); NEW_MACHINE_SETUP § 5O row covers the curator's machines |
| R3 | Stale references to retired files linger | Phase 0 enumerated every live site (§ 5G–5K); QA-G zero-hit grep gates the commit — **CLOSED 2026-08-17** (QA-G passed, hits classified history-only) |
| R4 | v2.0 alarms existing adopters | § 5F migration note: machinery never survived in adopters — no footprint change, `sync` unaffected |
| R5 | Adopt mode meets an unmapped artifact shape at the pilot | § 4 dry-run gate = nothing written unapproved; defects fix-forward; dormant pilot = low blast radius — **CLOSED 2026-08-17** (QA-E pilot passed; every artifact mapped, incl. the manifest-rename prep + project_rules.md relocation via D-A…D-D) |
| R6 | Dropbox/CloudStorage symlink oddities | The only symlink is machine-local (`~/.claude`, outside Dropbox), recreated idempotently by § 5D; probe 1 verified reads INTO CloudStorage |
| R7 | `pull --ff-only` fails on a diverged vault clone | Step 0 WARNs + proceeds on the local copy + surfaces to operator (never blocks delivery on network) |
| R8 | Skill description exceeds the 1,536-char listing cap | § 5A description is ~340 chars; QA-A confirms listing — **CLOSED 2026-08-17** (skill listed + invoked live) |

## 12. Acceptance criteria

1. QA-A: fresh session lists + invokes the skill; Step 0 reports v2.0 + live vault sha. ⚑
2. QA-B: scratch bootstrap yields the full operative footprint, zero machinery, governance exit 0,
   SVA stamped with Set Version + vault commit. ⚑
3. QA-C/QA-D: installer idempotent; self-pull + offline WARN both observed.
4. QA-E: real Capital-Signal adoption — approved dry-run list == applied diff; marker integrity
   holds. ⚑ (adopt-mode + closure gate)
5. QA-F: pilot registered; `sync` dry-run reports it current.
6. QA-G: both grep gates zero-hit (domain-neutral incl. `skill/`; no live refs to retired files).
7. STANDARDS_INDEX v2.0 consistent (counts 15 files / 11+4, § 6 entry + migration note); manifest,
   folder_structure, architecture, SVA, NEW_MACHINE_SETUP all synced same-commit; governance
   scripts exit 0 at every commit.
8. Plan + tracker promoted 1.0/CLOSED only after criterion 4 (per D-5).
