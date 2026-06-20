<!-- VERSION: 1.4 -->
<!-- Last Updated: 2026-06-20 -->
<!-- Source: docs/standards/SESSION_OPENER.md (template) v1.4. Project-local instance for Standard DocSet. -->
<!--
CHANGE LOG
v1.4 — 2026-06-20 — Added § 3.1 universal row 14 (Rule 13 senior-review pass recorded as run but not actually executed against the § 5 code). Standard Set Version v1.3 (lesson L051).
v1.3 — 2026-06-17 — PLAN-005: added § 1.5 memory-link health check (verify + self-heal + halt-on-empty, per Rule 14), the § 4 "Memory link" output line, and § 3.1 row 13. Standard Set Version v1.2.
v1.2 — 2026-06-14 — Project display name → "Standard DocSet" (header Source ref + § 2 registry folder path). Engine package `standard_document_updater` unchanged.
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): wrapped the project-owned blocks (§ 2 source/target registry table, § 3.2 project-specific patterns table) in PROJECT-OWNED markers so a future sync preserves them.
v1.0 — 2026-06-07 — Project bootstrap. Instantiated from the v1.0 template (docs/standards/SESSION_OPENER.md v1.0). Customized for a single-agent, local-CLI, domain-neutral project: § 1.2 live-system probes replaced with "registered target suites" (no remote infra); § 2 environment mapping rewritten as the source-suite + target-repo registry (no staging/prod hosts); § 3.1 universal failure-mode catalog kept (remote rows annotated N/A for this project); § 4 output template trimmed of the live-system block. BINDING per CLAUDE.md Rule 9.
-->

# SESSION_OPENER.md — Mandatory session-start pre-flight (project-local)

> **This is the BINDING project-local instance** for `Standard DocSet`. Every Claude session in this repository MUST read this file and execute its § 1 pre-flight, then post the § 4 first-response output block BEFORE acting on the operator's first task (per `CLAUDE.md` Rule 9).

**Why this file exists:** Repeat mistakes across sessions trace to one root cause — skipping context-loading at session start and going straight to action. This file is the forcing function; the § 4 output block is the proof-of-pre-flight visible to the operator. See `archive/LESSONS.md` L043.

---

## 1. Pre-flight Claude MUST execute on message 1 of a new session

Run these (single tool-call message where possible) and produce the § 4 output block. This happens BEFORE acting on the operator's first task — even if the task seems simple.

### 1.1 Repository state
```bash
git log --oneline -3                          # recent local commits (tip of master)
git log --oneline origin/master..HEAD 2>/dev/null  # unpushed local commits (if a remote exists)
git status --short                            # working-tree dirt
```

This project's default branch is `master`. A remote may not be configured yet (local-only CLI tool) — the `origin/master..HEAD` probe is skipped gracefully if there is no `origin`.

### 1.2 Operating context (read-only)

This is a **local CLI tool** — there is no staging/production infrastructure to probe. Instead, surface the context the tool operates on:

- **The tool's own state** — current version of the engine (`src/standard_document_updater/` `# VERSION:` headers once it lands) and the adopted Standards Set Version (`docs/SET_VERSION_ADOPTED.md`).
- **Registered target suites** (once the registry exists) — which source suite + adopting repos the tool is configured to operate on (§ 2 below). Read-only: confirm the configured paths exist before any run that writes to them.

If the operator's task is purely internal (editing this repo, no run against a target suite), § 1.2's registry portion may be light — but always confirm the tool/Set-Version state.

### 1.3 Tracker tip

Read the top of the most relevant tracker for the stated task. **Sources in priority order:**

- **Local-only register** — `docs/Plans/OPEN_TASKS.md` (gitignored by design, per `archive/LESSONS.md` L046). Read top IF PRESENT (`head -50 docs/Plans/OPEN_TASKS.md`); skip gracefully if absent.
- **Per-plan tracker** — `docs/Plans/PLAN-NNN_tracker.md` (created per `CLAUDE.md` § 15.7 for big plans).
- **In-file § 4 phase block** of the active small plan.
- **Latest CHANGELOG entry** — `head -30 CHANGELOG.md`.

### 1.4 Memory recall

Surface 3–5 memories most relevant to the stated task (per `MEMORY_PROTOCOL.md` § 5 verify-before-recommending). Cite each as `[[memory-slug]]`. Recall from the project failure-mode catalog (§ 3 below).

### 1.5 Memory-link health (durability check — per `CLAUDE.md` Rule 14)

Confirm the in-repo memory store is live BEFORE relying on recall (§ 1.4):

```bash
bash scripts/bootstrap_memory.sh                 # idempotent: (re)creates ~/.claude → ./.claude/memory symlink
ls -1 .claude/memory/*.md 2>/dev/null | wc -l    # count stored memories (expect > 0 once memory exists)
```

- If bootstrap reports it **re-created** a stale/missing link → note it in the § 4 block (expected on a new machine or after a folder move).
- If the store is **empty when prior sessions are known to have written memory** → **STOP** and warn the operator in the § 4 block. Memory may have been lost (see Rule 14 + `archive/LESSONS.md` L050); do not proceed as if there is genuinely no history.

---

## 2. Canonical environment mapping (the source/target registry)

> This project has **no remote environments**. The "environments" that matter are the **source standards suite** and the **target repositories** the tool reads from / writes to. Cite this section (or the memory that mirrors it) before any command that writes to a target repo.

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
| Role | Path | Notes |
|---|---|---|
| **This repo (the tool)** | `~/Documents/Standard DocSet/` | The CLI tool itself; its own `docs/standards/` is its adopted suite. |
| **Canonical source suite** | `<to be registered>` | The authoritative standards set the tool propagates FROM (the most current adopter suite on this machine). |
| **Target repo(s)** | `<to be registered>` | Adopting project repos the tool updates TO. Supplied at runtime; never assumed. |
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
| 13 | Project memory lost on machine change / folder move | session start; any repo move or new machine | `CLAUDE.md` Rule 14 + `LESSONS.md` L050 |
| 14 | Rule 13 senior-review pass recorded as run but not actually executed against the § 5 code (`ruff` / `mypy --strict` / tests) | finalizing any § 15 plan (the Rule 13 pass) | `CLAUDE.md` Rule 13 + `LESSONS.md` L051 |
| — | Remote/host rows (staging↔prod, SSH, cloud web-console) from the template | N/A — this project has no remote infra | `LESSONS.md` L035, L043 (retained for reference) |

### 3.2 Project-specific patterns

> Add rows here as repeat-patterns surface. Pair each new row with a `feedback_<slug>.md` memory in the same commit per `LESSONS.md` L008.

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
| # | Pattern | Trigger | Memory / lesson |
|---|---|---|---|
| _(empty — append as needed)_ | | | |
<!-- PROJECT-OWNED:END -->

---

## 4. First-response output template (what Claude posts at message 1)

```
**Session pre-flight — completed per docs/SESSION_OPENER.md**

**Repo state**
- master tip: <sha> <subject>
- unpushed commits: <N> (or "none" / "no remote configured")
- working tree: <clean | M file1, file2, ...>

**Tool + suite state**
- Engine version: <version or "engine not yet implemented">
- Adopted Standards Set Version: <vX.Y>
- Registered target suites: <list or "none registered yet">
- Memory link: <healthy: N files | repaired (new machine / post-move) | EMPTY — operator warned>

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
