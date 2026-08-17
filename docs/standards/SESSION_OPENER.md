<!-- VERSION: 1.7 -->
<!-- Last Updated: 2026-08-17 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.7 — 2026-08-17 — Standard Set Version v2.0 (PLAN-009): End-of-file bootstrap pointer retargeted — the delivery skill instantiates the project-local copy during bootstrap (was: walk the retired NEW_PROJECT_BOOTSTRAP.md Step <N>).
v1.6 — 2026-08-16 — Standard Set Version v1.6 (PLAN-008 sync-enablement): TEMPLATE-ONLY banner block + PROJECT-OWNED instance-heading block, so section-merge sync never propagates template banners and preserves the adopter's heading.
v1.5 — 2026-08-16 — Standard Set Version v1.5 (PLAN-010): § 1.5 rewritten memory-link → project-data locality (claude_project_data.sh status; fix verbs link/adopt); § 1.3 read-the-register-WHOLE note; § 4 output line Memory link → Project data; § 3.1 row 14 upgraded (all project data) + new rows 16 (Rule 15 feature-ON verification) + 17 (L063 stamp-vs-log).
v1.4 — 2026-08-16 — Standard Set Version v1.4: § 1.1 push-state reconcile-vs-real-remote note (L055); § 3.1 row 15 sharpened with the L051 recurrence-#4 final-indentation clause.
v1.3 — 2026-06-20 — Added § 3.1 universal row 15 (Rule 13 senior-review pass recorded as run but not actually executed against the plan's embedded code). Standard Set Version v1.3 (lesson L051).
v1.2 — 2026-06-17 — PLAN-005: added § 1.5 memory-link health check (verify + self-heal + halt-on-empty, per Rule 14), the § 4 "Memory link" output line, and § 3.1 row 14. Standard Set Version v1.2.
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): wrapped the project-customizable blocks (§ 2 environment mapping table, § 3.2 project-specific failure-mode table) in PROJECT-OWNED markers so a future sync preserves them. Standard Set Version v1.1.
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

<!-- TEMPLATE-ONLY:BEGIN (delivery-crate banner — deleted at instantiation; sync never propagates this block) -->
# SESSION_OPENER.md — Mandatory session-start pre-flight (template)

> **This file is a TEMPLATE.** Adopters copy it to their project's `docs/SESSION_OPENER.md`, customize the placeholder sections per project, and add the binding rule to their repo-root `CLAUDE.md` (per template `CLAUDE.md` Rule 9 / § 3). Once instantiated, the project-local copy is BINDING for every Claude session in that repository. At instantiation: delete this TEMPLATE-ONLY block (markers included) and fill in the PROJECT-OWNED heading block below.
<!-- TEMPLATE-ONLY:END -->
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# SESSION_OPENER.md — Mandatory session-start pre-flight (project-local)

> **This is the BINDING project-local instance** for `<project-name>`. Every Claude session in this repository MUST read this file and execute its § 1 pre-flight, then post the § 4 first-response output block BEFORE acting on the operator's first task (per `CLAUDE.md` Rule 9).
<!-- PROJECT-OWNED:END -->

**Why this file exists:** Repeat mistakes across sessions traced to a single root cause — skipping context-loading at session start and going straight to action. Knowledge encoded in memory (host→env mapping, "grep tests before param change", etc.) is recalled only when the agent thinks to recall it. Without a forcing function, that recall is unreliable. SESSION_OPENER.md IS the forcing function: the binding rule says "read this file and execute its § 1 pre-flight before any action," and the § 4 first-response output template is the proof-of-pre-flight visible to the operator. See `LESSONS.md` L043 for the incident that motivated this.

This is the front-door catalog of project failure modes. Every repeat-pattern observed in the project gets a row in § 3, paired with a memory file. Over time § 3 becomes the project's institutional muscle memory.

---

## 1. Pre-flight Claude MUST execute on message 1 of a new session

Run these in parallel (single tool-call message) and produce the **first-response output template** in § 4. This MUST happen BEFORE acting on the operator's first task — even if the task seems simple.

### 1.1 Repository state
```bash
git log --oneline -3 origin/<main-branch> # tip of remote
git log --oneline origin/<main-branch>..HEAD # unpushed local commits
git status --short # working-tree dirt
```

Replace `<main-branch>` with `main` / `master` per project convention.

If a local register (`OPEN_TASKS.md`) or a tracker records a push-state ("unpushed" / "push held"), reconcile it against the **real** remote (`git ls-remote origin <main-branch>`) — not the local remote-tracking cache — before trusting it (per `LESSONS.md` L055). Committed trackers stay frozen at their commit; only the live register is reconciled.

### 1.2 Live system state (read-only — skip if task is purely local)
- **Staging deploy SHA**: `ssh <staging-user>@<staging-host> "cat <staging-deploy-marker> 2>/dev/null"`
- **Production deploy SHA**: `ssh <prod-user>@<prod-host> "cat <prod-deploy-marker> 2>/dev/null"`
- **Live runtime state probe** (project-specific — e.g., active feature flag, active config row, current job runner state)
- **Latest CI pipeline on main**: probe via CI provider API (GitLab REST, GitHub Actions API, etc.). Per `CICD_STANDARDS.md` § 11 / L031, never bounce the operator to the UI.

If the operator's task is purely local (no deploy, no SSH, no live system touch), § 1.2 may be skipped. When in doubt, run it — read-only probes are cheap.

### 1.3 Tracker tip
Read the top ~80 lines of the tracker most relevant to the stated task. Surface the current phase, the open task, and any cross-references to memories or open incidents.

**Tracker sources to check in priority order** (per project tracker-ownership rules — see `PROJECT_STANDARDS.md` § 7.7):

- **Local-only open-tasks register** (if the project uses one) — typically `docs/Plans/OPEN_TASKS.md`, gitignored by design. Per `LESSONS.md` L046 + `CLAUDE.md` § 15.7. Read top of file IF PRESENT (e.g., `head -50 docs/Plans/OPEN_TASKS.md`); skip gracefully if absent (fresh clones / other machines will not have it). When present, it is the single "what's open right now" index across all plans + non-plan items + future-plan placeholders.
- **Per-plan tracker** — `docs/Plans/PLAN-NNN_tracker.md`, created per `CLAUDE.md` § 15.7 when a plan is "big" (Phase 3 lands as >1 commit, OR Phase 4 has multi-scenario verification, OR plan spans >1 agent session, OR operator-declared). Read this if work continues a multi-task / multi-scenario plan.
- **In-file § 4 phase block of the active plan** — for "small" plans (those that do NOT trigger the sibling-tracker conditions), the granular sub-task checklist lives inside the plan file's own § 4 (per `CLAUDE.md` § 15.7). Read top of plan file in those cases.
- **Latest CHANGELOG entry** — `head -30 CHANGELOG.md` shows the most recent commit's intent + impact.
- **Project-specific rolling tracker** — some projects maintain a single rolling task tracker (e.g., `docs/<project>_setup_tracker.md`); if so, read it as a fallback.

Read the register WHOLE — top to bottom, every time; never a partial slice. Approved or live
items can sit low in the file.

### 1.4 Memory recall
Surface 3–5 memories most relevant to the stated task (per `MEMORY_PROTOCOL.md` § 5 verify-before-recommending). Cite each as `[[memory-slug]]`. Recall from the project failure-mode catalog (§ 3 below) — every row there is a memory that may be relevant.

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
  and warn the operator in the § 4 block (Rule 14 + `LESSONS.md` L050); do not proceed
  as if there is genuinely no history.

---

## 2. Canonical environment mapping

> **Customize this section per project.** This is the master record of which credentials, hostnames, paths, and container prefixes belong to which environment. Cite this section (or the project memory that mirrors it) every time you SSH, `scp`, or run any remote command.

Example shape (replace with your project's actual mapping):

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
| Env | SSH | Container prefix | App path |
|---|---|---|---|
| **STAGING** | `<user>@<staging-ip-or-host>` | `<prefix>-*` | `<path>` |
| **PRODUCTION** | `<user>@<prod-ip-or-host>` | `<prefix>-*` | `<path>` |
| **<other-env>** | ... | ... | ... |
<!-- PROJECT-OWNED:END -->

**Cross-checks** (use any one to verify a host's identity independently of memory):
- `hostname` → distinct per-env hostnames
- `docker ps --format '{{.Names}}' | head -1` → container-name prefix per env
- App path presence (`ls <path>`)
- CI variable scope (e.g., `$STAGING_HOST` vs `$PRODUCTION_HOST` in `.gitlab-ci.yml`)

If memory and a live probe ever disagree, **trust the live probe** and update memory afterward.

**Why this matters:** Confusing staging and production hosts is one of the highest-cost mistakes a project can make. It is easy to make if SSH config has both hosts indexed by IP alone and the agent never explicitly states which env it is targeting. The mistake is invisible until a write lands — read-only queries against the wrong env merely produce wrong answers; writes against the wrong env produce incidents.

---

## 3. Project failure-mode catalog (mistake-avoidance checklist)

> **Customize this section per project.** Seed rows with the universal patterns below; append project-specific rows as new repeat-patterns surface.

Each row links to the memory that codifies it. Recall the linked memory when its trigger condition is in play during a session.

### 3.1 Universal patterns (seed from the standards suite)

| # | Pattern | Trigger | Memory / lesson |
|---|---|---|---|
| 1 | Wrong host (staging↔prod confusion) | any `ssh` / `scp` / remote command | `[[feedback_verify_host_env_before_ssh]]` / `LESSONS.md` L043 |
| 2 | Skipped test sync on a config/param change | any `config/*` edit affecting runtime behavior | `[[feedback_grep_tests_before_param_change]]` / project-specific |
| 3 | Code review skipped before `git add` | every commit | `CLAUDE.md` **Rule 10 (binding)** + `LESSONS.md` L027 + L044 |
| 4 | Manifest / CHANGELOG missed | every commit | `LESSONS.md` L008 |
| 5 | Push without proper cadence | every `git push` | `LESSONS.md` L028 |
| 6 | Defending wrong answers when operator questions | "are you sure?" / "but how can…" | `LESSONS.md` L032 |
| 7 | Local governance not validating CI schema | any `.gitlab-ci.yml` / workflow edit | `LESSONS.md` L005 |
| 8 | Heredoc-piped commit messages corrupt special chars | multi-paragraph commit messages | `LESSONS.md` L004 |
| 9 | Force-push amend after broken-on-push | any pushed commit that fails CI | `LESSONS.md` L003 |
| 10 | Web-console for sensitive files (a cloud VPS provider / similar) | any `.env` / key handling | `LESSONS.md` L035 |
| 11 | Starting a § 15 plan without granular sub-task tracking — either (a) big plan without sibling tracker, OR (b) small plan without expanded § 4 in-file checklist | any new `docs/Plans/PLAN-NNN_*.md` | `LESSONS.md` L045 + `CLAUDE.md` § 15.7 |
| 12 | Local-only OPEN_TASKS.md register stale or unmaintained (if the project uses the convention) | every session start | `LESSONS.md` L046 + `CLAUDE.md` § 15.7 |
| 13 | Behavior-affecting change shipped without a paired QA / smoke-test scenario in the plan's tracker or OPEN_TASKS | every behavior-affecting commit | `CLAUDE.md` **Rule 11 (binding)** + `LESSONS.md` L047 |
| 14 | Project data written or left outside the project folder — locality symlink absent/broken after a machine change or folder move, silently orphaning memory + transcripts | § 1.5 probe on every session-open; any tool creating project state outside the repo | `CLAUDE.md` Rule 14 + `LESSONS.md` L050 (+ v1.5 generalization) |
| 15 | Rule 13 senior-review pass not actually executed against the plan's embedded code — or run on an unindented draft snippet instead of the final indentation it ships at (linter / type-checker / tests) | finalizing any § 15 plan (the Rule 13 pass) | `CLAUDE.md` Rule 13 + `LESSONS.md` L051 (recurrence #4) |
| 16 | Implementation closed on rollback-guarantee QA alone — the NEW behavior never exercised; broken feature ships with an unbounded defect window | every behavior-affecting implementation, at completion | `CLAUDE.md` **Rule 15 (binding)** + `LESSONS.md` L067 |
| 17 | Version stamp edited in the change log but not in the stamp field itself (headers, § 3 heading counts, manifest cells, count tables) | every stamp-touching edit + the Rule 10 review | `LESSONS.md` L063 |

### 3.2 Project-specific patterns

> Add rows here as new repeat-patterns surface. Each new row should be paired with a `feedback_<slug>.md` memory in the same commit per `LESSONS.md` L008 (manifest completeness).

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
| # | Pattern | Trigger | Memory / lesson |
|---|---|---|---|
| _(empty — append as needed)_ | | | |
<!-- PROJECT-OWNED:END -->

Examples of patterns that may surface during a real project:
- Deploy-script-specific bypasses (e.g., "never raw `docker compose up` on staging/prod" — see `LESSONS.md` L024)
- Config-source-of-truth verification (e.g., "CI-injected `.env` files are wiped on every deploy" — see L025)
- Post-pattern soak (e.g., "24-hour staging soak before any prod deploy" — see L022)
- Staging-mirrors-prod (e.g., "every prod config change has a parallel staging change" — see L023)
- Explicit PROD action gating (e.g., "every prod-touching command is its own auth round" — see L030)
- Hot-edits paired with same-day repo commit (project-specific config-source-of-truth pattern)

---

## 4. First-response output template (what Claude posts at message 1)

```
**Session pre-flight — completed per docs/SESSION_OPENER.md**

**Repo state**
- origin/<main-branch> tip: <sha> <subject>
- unpushed commits: <N> (or "none")
- working tree: <clean | M file1, file2, ...>
- Project data: <OK: N memory files | repaired (link/adopt run) | EMPTY — operator warned>

**Live system** (skip if task is purely local)
- Staging deploy SHA: <sha> (deployed <ts>)
- Production deploy SHA: <sha> (deployed <ts>)
- Live runtime state: <project-specific probe result>
- Latest pipeline on <main-branch>: <id> <status>

**Tracker tip — <tracker-name>**
<2-3 line summary of current phase / open task>

**Relevant memories for today's task**
- [[memory-slug]] — one-line why-relevant
- [[memory-slug]] — one-line why-relevant
- ... (3-5 total)

**Mistake-avoidance flags for this task**
<reference checklist rows from § 3 that apply, with one-line how-they-apply>

**Operator's task (as understood)**
<one-sentence restatement>

**Proposed approach**
<bullet list, 2-5 items max>

**Awaiting your go on the approach, or any correction to my read.**
```

This block is the proof-of-pre-flight. No edits, no SSH commands, no remote queries, no commits should happen before this block is posted.

---

## 5. When the pre-flight may be abbreviated

Operator may explicitly say "skip pre-flight" for trivial follow-up sessions (e.g., re-opening within the same hour to continue a clearly-bounded task). Operator-only authorization — never self-skip.

Even when abbreviated:
- Still recall memories relevant to the task (§ 1.4)
- Still cite host → env mapping before any remote command (§ 2)
- Still walk the mistake-avoidance checklist mentally (§ 3)

The block in § 4 may be skipped; the underlying discipline cannot.

---

## 6. Maintenance

When a new repeat-pattern is observed (operator flags a recurring mistake, or an incident reveals a missing guardrail):

1. Create the matching `feedback_<slug>.md` memory file (per `MEMORY_PROTOCOL.md`)
2. Add a row in § 3.2 of this file
3. Add the memory to your memory-index file (per `MEMORY_PROTOCOL.md`)
4. Same-commit per `LESSONS.md` L008 (manifest completeness)

Do NOT let this file go stale. Its value depends on being the current, complete catalog of every failure mode the project has produced. A § 3 that hasn't been touched in 6 months is a signal that either nothing is being learned, or learnings aren't being captured — both are problems.

---

## 7. Relationship to the rest of the standards suite

This file is a **binding standards file** (Tier 1) in the suite. It is referenced by:

- `CLAUDE.md` Rule 9 (the binding rule that mandates the pre-flight)
- `MEMORY_PROTOCOL.md` (the failure-mode catalog rows pair 1:1 with feedback memories)
- `LESSONS.md` L043 (the lesson capturing why this file exists)
- `PROJECT_STANDARDS.md` § 8 commit policy (pre-flight is a separate phase from commit/governance/push)

This file does NOT replace:
- `CLAUDE.md` § 8 validation checklist (pre-commit, not pre-session)
- `PROMPT_STANDARDS.md` multi-file prompt construction (per-prompt, not per-session)
- `MEMORY_PROTOCOL.md` memory hygiene rules (always-in-force, not session-bounded)

The pre-flight runs ONCE at the front of a session, not at every turn. After it has been posted, subsequent turns proceed normally under the rules surfaced by it.

---

## End of file

If you are reading this in a freshly-bootstrapped project, the delivery skill instantiates the project-local copy and customizes §§ 2 + 3 during bootstrap. If you are reading this as a working contributor, you should have already produced the § 4 output block — if you haven't, do so now before continuing.
