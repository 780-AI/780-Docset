<!-- VERSION: 1.21 -->
<!-- Last Updated: 2026-10-05 -->
<!-- Source: docs/standards/SESSION_OPENER.md (template) v1.7. Project-local instance for Standard DocSet. -->
<!--
CHANGE LOG
v1.21 — 2026-10-05 — Fifth target registered: 780-estimator (§ 2 registry row — git transport, the first git target; team project on a Windows PC; Set v1.3 old-SETUP adopter caught up to v2.7 after a one-time prep commit — PLAN-017).
v1.20 — 2026-10-05 — PLAN-016: § 1.2 fleet-view bullet (run `status` — prints every target's state and regenerates `docs/fleet.csv`; call out unreachable / not-current / handoff-pending targets); § 4 "Registered target suites" line reads from that run.
v1.19 — 2026-10-05 — Two push remotes (operator 2026-10-05): § 1.1 probes unpushed commits per remote (`origin` = GitLab, `github` = GitHub 780-AI/780-Docset) and reconciles a recorded push-state against BOTH real remotes (`git ls-remote` each) — a push counts as done only when both show the same tip; § 4 "unpushed commits" line reports both.
v1.18 — 2026-10-03 — Fourth target registered: EverOn.Equinex (§ 2 registry row — local `~/` transport, Dropbox-synced; adopted 2026-10-03 via the skill's adopt mode, EverOn own line retired — PLAN-011). Also (operator-confirmed fact, PLAN-011 Phase 3c execution delta): the 780-VPN row's "team member's account / Mac" wording corrected — the old ssh host was the operator's own second Mac (account `parsaazad`).
v1.17 — 2026-10-03 — 780-Automation DHCP IP change (§ 2 registry row: 172.16.11.60 → 172.16.10.245, operator-supplied; the host's ED25519/RSA/ECDSA keys verified identical to the ones trusted at .10.61/.11.60 before trusting the new address; same repo — origin 780-AI/780-Automation, bootstrap `cb62527` in history — clean tree, Set v2.5, no un-landed handoff).
v1.16 — 2026-10-03 — 780-VPN re-pointed ssh → local `~/` (§ 2 target row): the repo lives in a SHARED Dropbox folder that also syncs to the curator machine; its ssh host had been unreachable since 2026-09-08. Drops the DHCP-IP dependency; one-machine-at-a-time caution now spans both Dropbox accounts.
v1.15 — 2026-09-05 — Clock-skew record CORRECTED (§ 2 780-VPN row): the vault machine was ~9 days slow (verified vs gitlab.com + apple.com server time); the team Macs' stamps were accurate. Earlier entries dated 2026-08-27 were written under the slow clock (real date 2026-09-05). Also: 780-VPN folder is SHARED Dropbox (also local at ~/).
v1.14 — 2026-08-27 — Deferred-minor sweep: stale header Source ref template v1.4 → v1.7 (the template moved at Set v2.0; surgical omission since — cleared from the register).
v1.13 — 2026-08-27 — § 3.2 row 1 added (Rule 16: no integration of externally-authored content without the operator list-and-confirm gate — the nine-orphaned-lessons incident, L069).
v1.12 — 2026-08-27 — 780-Automation DHCP IP change (§ 2 registry row: 172.16.10.61 → 172.16.11.60; the documented DHCP caveat fired — verified same repo + clean tree + v2.2 before re-pointing).
v1.11 — 2026-08-27 — Third target registered: 780-VPN (§ 2 registry row — ssh transport to a second team Mac, LAN IP + key auth; bootstrapped Set v2.2 self-service; remote path Dropbox-synced on their side; remote clock +9d skew noted).
v1.10 — 2026-08-19 — Second target registered: 780-Automation (§ 2 registry row — ssh transport to the team Mac, LAN IP + key auth; bootstrapped Set v2.1 via the portable kit; git-transport migration planned at the org-GitHub settle).
v1.9 — 2026-08-18 — Capital-Signal moved into the Dropbox folder: § 2 target row re-pointed to the ~-based path (the registry expands ~ per machine — machine-affinity resolved for this target; writes still one machine at a time, let Dropbox settle).
v1.8 — 2026-08-17 — First target registration (PLAN-009 QA-F): § 2 registry table filled — vault path corrected to the Dropbox location (stale ~/Documents/ deferred-minor cleared), canonical source = this repo's docs/standards/, first registered target EverOn.Capital-Signal (local transport, machine-affine note).
v1.7 — 2026-08-16 — Standard Set Version v1.6 (PLAN-008): heading block wrapped in PROJECT-OWNED — reconciles with the v1.6 template structure; owned-block count now 3 = template's 3.
v1.6 — 2026-08-16 — Standard Set Version v1.5 (PLAN-010): § 1.5 rewritten memory-link → project-data locality (claude_project_data.sh status; fix verbs link/adopt); § 1.3 read-the-register-WHOLE note; § 4 output line Memory link → Project data; § 3.1 row 13 upgraded (all project data) + new rows 15 (Rule 15 feature-ON verification) + 16 (L063 stamp-vs-log).
v1.5 — 2026-08-16 — Standard Set Version v1.4: § 1.1 push-state reconcile-vs-real-remote note (L055); § 3.1 row 14 sharpened with the L051 recurrence-#4 final-indentation clause.
v1.4 — 2026-06-20 — Added § 3.1 universal row 14 (Rule 13 senior-review pass recorded as run but not actually executed against the § 5 code). Standard Set Version v1.3 (lesson L051).
v1.3 — 2026-06-17 — PLAN-005: added § 1.5 memory-link health check (verify + self-heal + halt-on-empty, per Rule 14), the § 4 "Memory link" output line, and § 3.1 row 13. Standard Set Version v1.2.
v1.2 — 2026-06-14 — Project display name → "Standard DocSet" (header Source ref + § 2 registry folder path). Engine package `standard_document_updater` unchanged.
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): wrapped the project-owned blocks (§ 2 source/target registry table, § 3.2 project-specific patterns table) in PROJECT-OWNED markers so a future sync preserves them.
v1.0 — 2026-06-07 — Project bootstrap. Instantiated from the v1.0 template (docs/standards/SESSION_OPENER.md v1.0). Customized for a single-agent, local-CLI, domain-neutral project: § 1.2 live-system probes replaced with "registered target suites" (no remote infra); § 2 environment mapping rewritten as the source-suite + target-repo registry (no staging/prod hosts); § 3.1 universal failure-mode catalog kept (remote rows annotated N/A for this project); § 4 output template trimmed of the live-system block. BINDING per CLAUDE.md Rule 9.
-->

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# SESSION_OPENER.md — Mandatory session-start pre-flight (project-local)

> **This is the BINDING project-local instance** for `Standard DocSet`. Every Claude session in this repository MUST read this file and execute its § 1 pre-flight, then post the § 4 first-response output block BEFORE acting on the operator's first task (per `CLAUDE.md` Rule 9).
<!-- PROJECT-OWNED:END -->

**Why this file exists:** Repeat mistakes across sessions trace to one root cause — skipping context-loading at session start and going straight to action. This file is the forcing function; the § 4 output block is the proof-of-pre-flight visible to the operator. See `archive/LESSONS.md` L043.

---

## 1. Pre-flight Claude MUST execute on message 1 of a new session

Run these (single tool-call message where possible) and produce the § 4 output block. This happens BEFORE acting on the operator's first task — even if the task seems simple.

### 1.1 Repository state
```bash
git log --oneline -3                          # recent local commits (tip of master)
git log --oneline origin/master..HEAD 2>/dev/null  # unpushed to GitLab (origin)
git log --oneline github/master..HEAD 2>/dev/null  # unpushed to GitHub (github)
git status --short                            # working-tree dirt
```

This project's default branch is `master`. It has **two remotes, and every push goes to both**: `origin` = GitLab `yaser.khosravi/standard-docset` (private; the CI of record) and `github` = GitHub `780-AI/780-Docset` (private; 780-AI members read-only, only the operator writes). Either probe is skipped gracefully if that remote is not configured (a fresh clone re-adds `github` per `docs/NEW_MACHINE_SETUP.md` § 1).

When `OPEN_TASKS.md` or a tracker records a push-state ("unpushed" / "push held"), reconcile it against **both real remotes** (`git ls-remote origin master` and `git ls-remote github master`) — not the local `origin/master` / `github/master` caches — before trusting it (per `archive/LESSONS.md` L055). A push counts as done only when both remotes show the same tip. Committed trackers stay frozen at their commit; only the live register is reconciled.

### 1.2 Operating context (read-only)

This is a **local CLI tool** — there is no staging/production infrastructure to probe. Instead, surface the context the tool operates on:

- **The tool's own state** — current version of the engine (`src/standard_document_updater/` `# VERSION:` headers once it lands) and the adopted Standards Set Version (`docs/SET_VERSION_ADOPTED.md`).
- **Registered target suites** (once the registry exists) — which source suite + adopting repos the tool is configured to operate on (§ 2 below). Read-only: confirm the configured paths exist before any run that writes to them.
- **Fleet view (PLAN-016)** — run `.venv/bin/python -m standard_document_updater status`: it prints every target's state and regenerates `docs/fleet.csv`. Call out any target that is unreachable, not `current`, or holds an un-landed handoff (`handoff_pending` > 0 in the file).

If the operator's task is purely internal (editing this repo, no run against a target suite), § 1.2's registry portion may be light — but always confirm the tool/Set-Version state.

### 1.3 Tracker tip

Read the top of the most relevant tracker for the stated task. **Sources in priority order:**

- **Local-only register** — `docs/Plans/OPEN_TASKS.md` (gitignored by design, per `archive/LESSONS.md` L046). Read top IF PRESENT (`head -50 docs/Plans/OPEN_TASKS.md`); skip gracefully if absent.
- **Per-plan tracker** — `docs/Plans/PLAN-NNN_tracker.md` (created per `CLAUDE.md` § 15.7 for big plans).
- **In-file § 4 phase block** of the active small plan.
- **Latest CHANGELOG entry** — `head -30 CHANGELOG.md`.

Read the register WHOLE — top to bottom, every time; never a partial slice. Approved or live
items can sit low in the file.

### 1.4 Memory recall

Surface 3–5 memories most relevant to the stated task (per `MEMORY_PROTOCOL.md` § 5 verify-before-recommending). Cite each as `[[memory-slug]]`. Recall from the project failure-mode catalog (§ 3 below).

### 1.5 Project-data locality (durability check — per `CLAUDE.md` Rule 14)

Confirm the in-repo project-data store is live BEFORE relying on recall (§ 1.4):

```bash
bash scripts/claude_project_data.sh status
ls -1 .claude/project-data/memory/*.md 2>/dev/null | wc -l
```

- `STATUS: OK` → proceed. Any other status names its fix verb — run it (`link` after a
  move/new machine; `adopt` on a machine with un-adopted harness data) and note the repair in
  the § 4 block.
- Store **unexpectedly empty** when prior sessions are known to have written memory → **STOP**
  and warn the operator in the § 4 block (Rule 14 + `archive/LESSONS.md` L050); do not proceed
  as if there is genuinely no history.

---

## 2. Canonical environment mapping (the source/target registry)

> This project has **no remote environments**. The "environments" that matter are the **source standards suite** and the **target repositories** the tool reads from / writes to. Cite this section (or the memory that mirrors it) before any command that writes to a target repo.

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
| Role | Path | Notes |
|---|---|---|
| **This repo (the tool + vault)** | `~/Library/CloudStorage/Dropbox/Projects/Standard DocSet/` | Dropbox-synced across machines (`$HOME` differs per machine); the CLI tool itself. |
| **Canonical source suite** | `docs/standards/` (this repo) | The vault IS the source — the authoritative set the tool propagates FROM (also its own adopted suite). |
| **Target repo(s)** | `EverOn.Capital-Signal` — `~/Library/CloudStorage/Dropbox/Projects/EverOn.Capital-Signal` (Dropbox-synced; moved 2026-08-18) | Registered in `config/projects.toml` (local transport, `~` path — resolves per machine, so any machine syncing the folder can run reads/writes; ONE machine at a time, let Dropbox settle). Set v2.0 adopter, 2026-08-17 (PLAN-009 pilot). |
| | `780-Automation` — `ssh:a780@172.16.10.245:/Users/a780/Projects/780-Automation` (team Mac, LAN) | Registered 2026-08-19 (ssh transport; key auth; LAN IP is DHCP — changed 10.61→11.60 2026-08-27, →10.245 2026-10-03 (host keys verified identical)). Bootstrapped Set v2.1 same day via the portable kit (self-service). Migration to git transport planned when the project lands on the organization GitHub (re-opens DD-6b before any git write-back). |
| | `780-VPN` — `~/Library/CloudStorage/Dropbox/Projects/780-VPN` (Dropbox-synced; worked on from the operator's second Mac, account `parsaazad`) | Registered 2026-08-27 over ssh; **re-pointed to local `~/` 2026-10-03** (ssh host unreachable since 2026-09-08; identity verified pre-re-point — same GitHub origin `780-AI/780-VPN`, bootstrap `be4d6d3` + both sync landings in history, Set v2.5, clean tree). The old ssh host was the operator's own second Mac (corrected 2026-10-03 — earlier wording called it a team member's machine): one machine at a time across the operator's two Macs — let Dropbox settle; never write while a session there is mid-work. Bootstrapped Set v2.2 on that Mac (vault `3f5590a`). Git transport (GitHub) remains a candidate at DD-6b. |
| | `EverOn.Equinex` — `~/Library/CloudStorage/Dropbox/Projects/EverOn.Equinex` (Dropbox-synced) | Registered 2026-10-03 (local transport, `~` path — resolves per machine; ONE machine at a time, let Dropbox settle). Adopted Set v2.7 2026-10-03 via the skill's adopt mode (PLAN-011); EverOn own line retired — pre-adoption archive + numbering crosswalk in `archive/LESSONS_LEGACY.md`. High-stakes live project: engine writes only between its work sessions. |
| | `780-estimator` — `git@github.com:780-AI/780-estimator.git` (branch `main`) | Registered 2026-10-05 — git transport, the FIRST git target: every engine write is a commit pushed straight to their `main` (Delivery A; fast-forward only — a concurrent push makes the write fail, never overwrite). Team project, owner Bahereh Hassanpour, worked on from a Windows PC (Git Bash; Rule 14 via directory junctions — `claude_project_data.sh` v0.2). Bootstrapped Set v1.3 2026-06-21 (old SETUP flow); caught up to v2.7 2026-10-05 by `sync` after a one-time prep commit (v1.6 heading wrap + sync-ready SVA + locality tool) — PLAN-017. |
<!-- PROJECT-OWNED:END -->

**Cross-checks before writing to any target:**
- Confirm the target path exists and is a git repo (`git -C <path> rev-parse --show-toplevel`).
- Confirm the target's current Set Version (`docs/SET_VERSION_ADOPTED.md` or `STANDARDS_INDEX.md`) before computing a backport.
- Never write to a target the operator has not named in the current task.

**Why this matters:** the highest-cost mistake for this tool is writing to the wrong repository or overwriting a target's customized files with source-template content. Read-only diffs are cheap; writes are not. Always state which repo a write targets before running it.

---

## 3. Project failure-mode catalog (mistake-avoidance checklist)

Each row links to the memory/lesson that codifies it. Recall the linked memory when its trigger is in play.

### 3.1 Universal patterns (seed from the standards suite)

| # | Pattern | Trigger | Memory / lesson |
|---|---|---|---|
| 1 | Writing to the wrong repo / overwriting a target's customizations | any command that writes to a target suite | project-specific (see § 2) |
| 2 | Acting on a cached/remembered version of a target instead of re-reading | any diff / merge / version-bump against a target | `CLAUDE.md` § 2 + `archive/LESSONS.md` L016 |
| 3 | Code review skipped before `git add` | every commit | `CLAUDE.md` **Rule 10 (binding)** + `LESSONS.md` L027 + L044 |
| 4 | Manifest / CHANGELOG missed | every commit | `LESSONS.md` L008 |
| 5 | Push without proper cadence | every `git push` | `LESSONS.md` L028 |
| 6 | Defending wrong answers when operator questions | "are you sure?" / "but how can…" | `LESSONS.md` L032 |
| 7 | Local governance not validating CI schema | any `.gitlab-ci.yml` edit | `LESSONS.md` L005 |
| 8 | Heredoc-piped commit messages corrupt special chars | multi-paragraph commit messages | `LESSONS.md` L004 |
| 9 | Force-push amend after broken-on-push | any pushed commit that fails CI | `LESSONS.md` L003 |
| 10 | Behavior-affecting change without a paired QA scenario | every behavior-affecting commit | `CLAUDE.md` **Rule 11 (binding)** + `LESSONS.md` L047 |
| 11 | Starting a § 15 plan without granular sub-task tracking | any new `docs/Plans/PLAN-NNN_*.md` | `LESSONS.md` L045 + `CLAUDE.md` § 15.7 |
| 12 | Local-only OPEN_TASKS.md register stale | every session start | `LESSONS.md` L046 + `CLAUDE.md` § 15.7 |
| 13 | Project data written or left outside the project folder — locality symlink absent/broken after a machine change or folder move, silently orphaning memory + transcripts | § 1.5 probe on every session-open; any tool creating project state outside the repo | `CLAUDE.md` Rule 14 + `LESSONS.md` L050 (+ v1.5 generalization) |
| 14 | Rule 13 senior-review pass not actually executed against the § 5 code — or run on an unindented draft snippet instead of the final indentation it ships at (`ruff` / `mypy --strict` / tests) | finalizing any § 15 plan (the Rule 13 pass) | `CLAUDE.md` Rule 13 + `LESSONS.md` L051 (recurrence #4) |
| 15 | Implementation closed on rollback-guarantee QA alone — the NEW behavior never exercised; broken feature ships with an unbounded defect window | every behavior-affecting implementation, at completion | `CLAUDE.md` **Rule 15 (binding)** + `LESSONS.md` L067 |
| 16 | Version stamp edited in the change log but not in the stamp field itself (headers, § 3 heading counts, manifest cells, count tables) | every stamp-touching edit + the Rule 10 review | `LESSONS.md` L063 |
| — | Remote/host rows (staging↔prod, SSH, cloud web-console) from the template | N/A — this project has no remote infra | `LESSONS.md` L035, L043 (retained for reference) |

### 3.2 Project-specific patterns

> Add rows here as repeat-patterns surface. Pair each new row with a `feedback_<slug>.md` memory in the same commit per `LESSONS.md` L008.

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
| # | Pattern | Trigger | Memory / lesson |
|---|---|---|---|
| 1 | Externally-authored content (harvested entries, rescued lessons, target-project rules) integrated into the suite without the operator list-and-confirm gate | every `integrate` run + any intake, incl. manual rescues | `CLAUDE.md` **Rule 16 (binding)** + `archive/LESSONS.md` L069 |
<!-- PROJECT-OWNED:END -->

---

## 4. First-response output template (what Claude posts at message 1)

```
**Session pre-flight — completed per docs/SESSION_OPENER.md**

**Repo state**
- master tip: <sha> <subject>
- unpushed commits: GitLab <N> / GitHub <N> (or "none — both remotes at HEAD")
- working tree: <clean | M file1, file2, ...>

**Tool + suite state**
- Engine version: <version or "engine not yet implemented">
- Adopted Standards Set Version: <vX.Y>
- Registered target suites: <N from `status` (docs/fleet.csv refreshed); call out unreachable / not-current / handoff-pending>
- Project data: <OK: N memory files | repaired (link/adopt run) | EMPTY — operator warned>

**Tracker tip**
<2-3 line summary of current phase / open task, or "no active tracker">

**Relevant memories for today's task**
- [[memory-slug]] — one-line why-relevant
- ... (3-5 total)

**Mistake-avoidance flags for this task**
<reference § 3 rows that apply, one line each>

**Operator's task (as understood)**
<one-sentence restatement>

**Proposed approach**
<bullet list, 2-5 items max>

**Awaiting your go on the approach, or any correction to my read.**
```

This block is the proof-of-pre-flight. No edits, no writes to any target, no commits before it is posted.

---

## 5. When the pre-flight may be abbreviated

Operator may explicitly say "skip pre-flight" for trivial follow-up sessions. Operator-only authorization — never self-skip. Even when abbreviated: still recall relevant memories (§ 1.4), still cite the source/target registry before any write (§ 2), still walk § 3 mentally. The § 4 block may be skipped; the discipline cannot.

---

## 6. Maintenance

When a new repeat-pattern is observed: (1) create the `feedback_<slug>.md` memory; (2) add a row in § 3.2; (3) add it to the memory index; (4) same-commit per `LESSONS.md` L008. Do not let § 3 go stale.
