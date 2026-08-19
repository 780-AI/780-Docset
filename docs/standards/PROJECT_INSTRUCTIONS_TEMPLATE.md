<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-08-19 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.1 — 2026-08-19 — Standard Set Version v2.2 (domain-neutral scrub): 1 example path still carried a real username (survived the v1.0 genericization — the identifier-token class) → `/Users/you/...`.
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

# PROJECT_INSTRUCTIONS_TEMPLATE.md — Claude.ai Project Setup

**Scope:** This document is the template for the **Project Instructions** field of any new Claude.ai Project. The text in § 4 is what you actually paste into the field; the rest of this file is meta-guidance explaining what each section does, when to update it, and what anti-patterns to avoid.

**Why this file exists:** Project Instructions shape every conversation in a Claude.ai Project. Done well, they enforce binding rules, frame priorities, and establish session protocol from message 1 — saving 10-15 minutes of context-setting per session. Done badly, they restate content from `CLAUDE.md` (creating drift), batch too many goals (causing the agent to lose track), or omit current state (forcing the agent to re-derive context every session).

This template captures the patterns that worked across a reference project Phases 2 and 3.

---

## Table of Contents

1. [How Project Instructions fit in the standards architecture](#1-how-project-instructions-fit-in-the-standards-architecture)
2. [The three-tier structure](#2-the-three-tier-structure)
3. [How to use this template](#3-how-to-use-this-template)
4. [The template (copy this into Claude.ai)](#4-the-template-copy-this-into-claudeai)
5. [Section-by-section meta-guidance](#5-section-by-section-meta-guidance)
6. [When to update each tier](#6-when-to-update-each-tier)
7. [Anti-patterns to refuse](#7-anti-patterns-to-refuse)
8. [Worked example — a reference project](#8-worked-example--a-reference-project)

---

## 1. How Project Instructions fit in the standards architecture

Project Instructions are one of five distinct artifact categories. Each has different scope, lifecycle, and audience:

| Artifact | Scope | Lifecycle | Audience | Where it lives |
|---|---|---|---|---|
| `CLAUDE.md` | Repo (per-project) | Stable; rules added when something breaks | Coding agents reading the repo | Repo root |
| `docs/standards/*.md` | Repo (per-project) | Stable; updated when patterns evolve | Humans + agents on demand | Repo `docs/` |
| **Project Instructions** | **Claude.ai Project (per-project)** | **Mixed: static frame + per-session priorities** | **Claude.ai chat sessions** | **Claude.ai project setting** |
| User memory | User-wide (cross-project) | Persistent; pruned periodically | Every Claude.ai conversation | Claude.ai memory store |
| `archive/LESSONS.md` | Standards repo | Append-only history | Humans researching past decisions | Standards repo |

Project Instructions sit at the intersection of project-scoped (unlike user memory, which is wide) and conversation-level (unlike CLAUDE.md, which is repo-wide). They are the **first thing every chat session sees**, before any user message.

### What Project Instructions are FOR

- Enforce binding rules without re-explaining them every session ("Strictly follow CLAUDE.md")
- Frame current priorities so the agent works in order, not in parallel
- Establish session protocol (one task per message, brief overview first)
- Provide pointers to source-of-truth docs in the repo
- Set tone and expectations that span multiple sessions in this Project

### What Project Instructions are NOT for

- ❌ Re-stating CLAUDE.md content (creates drift; reference instead)
- ❌ Storing facts that change every session (those go in the first user message)
- ❌ Storing user-wide preferences (those go in Claude.ai memory)
- ❌ Storing project knowledge (that's the Project Knowledge feature)
- ❌ Lengthy domain explanation (that's what `README.md` and `docs/` are for; reference them)

---

## 2. The three-tier structure

Project Instructions have content with three different lifecycles. Mixing them without separation makes maintenance painful: every session-specific update accidentally touches the static frame.

### Tier A — Static frame (changes rarely; once per project)

The binding contract that frames every session. Set once at project creation, revisit only when standards evolve.

Contents:
- Project identity (name, domain, primary languages, deployment shape)
- Reference to `CLAUDE.md` and binding rules
- Session interaction protocol (one task per message, brief overview)
- Project knowledge precedence rule
- Standards file pointers
- Default response shape (per CLAUDE.md § 6)

### Tier B — Project-specific facts (changes when the project's environment changes)

Stable across most sessions but may rotate when infrastructure changes. Update when a new environment piece comes online, a critical file moves, or a key paths/credential rotates.

Contents:
- Critical files list (always-Major paths)
- Standard commands (test runner, lint, deploy, governance scripts)
- Environment specifics (key paths, languages versions, venv conventions)
- Domain-specific quirks worth flagging once

### Tier C — Per-session bits (changes every working session)

The conversation-level framing. Updated at the start of every working session.

Contents:
- Today's priorities in order
- Current state recap (branch tip SHA, what's done, what's next)
- Time budget for the session
- Anything unusual about this session (handoff context, reviewing yesterday's bug, etc.)
- Explicit start instruction

The Claude.ai Project Instructions field holds Tiers A + B. Tier C goes in the **first user message of each session** — never in the Project Instructions field, because Project Instructions persist across sessions and stale priorities are worse than no priorities.

---

## 3. How to use this template

### First-time setup (Day Zero of a new project)

1. Copy the template in § 4 below
2. Open the Claude.ai Project's Settings → Project Instructions field
3. Paste the template
4. Fill in every `<placeholder>` (Tiers A + B sections)
5. Delete the meta-comment markers at the top (`<!-- TIER A -->` etc.) — they're for reference only
6. Save

The Tier C section is **not** in the field — it's the structure for your first message in each session.

### Per-session use (start of every working session)

Open a new conversation in the Project. First message follows the Tier C template (§ 4 below). Send it. The agent now has:
- The static frame from Project Instructions (Tiers A + B, auto-loaded)
- Today's specific priorities and state from your first message (Tier C)

Skip Tier C in your first message → agent works without priority order, batches multiple goals, loses track.

### When the project changes

Edit Project Instructions (Tier B updates) when:
- A new critical file is added
- A key environment piece rotates (e.g., new VPS, new domain, new CI provider)
- Standard commands change
- Domain quirks evolve

Don't edit Project Instructions for per-session changes — that's Tier C territory.

---

## 4. The template (copy this into Claude.ai)

The block below is what you paste into the Project Instructions field. The Tier C section at the bottom is shown for reference but goes in your first user message of each session, not in the field.

````
<!-- ================================================================ -->
<!-- TIER A — STATIC FRAME (set once per project, revisit when standards evolve) -->
<!-- ================================================================ -->

You are working on <PROJECT NAME>, a <one-line domain description>.

## Binding rules

Strictly follow `CLAUDE.md` in the repo. It is binding, not advisory. When `CLAUDE.md` and a request conflict, refuse or propose a compliant alternative — do not silently override.

For any change:
- Classify per `CLAUDE.md` § Change Classification (Minor vs Major) before implementing.
- Major changes follow the full workflow: Analyze → Design → Implement → Sync → Validate.
- For Major changes: propose the plan before implementing. If I asked only for a plan, do not implement until I confirm.
- Use the response shape from `CLAUDE.md` § 6 when reporting completed work: Analysis → Plan/Design → Implementation → Doc/config updates → Version bumps → Changelog/impact statement.

For multi-file edits:
- Follow `docs/standards/PROMPT_STANDARDS.md` — ALLOWLIST + verbatim FIND/REPLACE + governance verification + files-modified checklist.
- Per `CLAUDE.md` Rule 6: verify via `git status --short` BEFORE every `git add`. Paste governance script outputs verbatim — never self-report "passed" without showing stdout/stderr.
- Per `CLAUDE.md` Rule 4: commit messages with backticks, em-dashes, or any special characters use `git commit -F /tmp/<file>.txt`. Never `-m` with escapes. Never heredoc piped to `git commit`.

## Session interaction protocol

- Brief full-picture overview first — what we're doing and why.
- Then strictly step-by-step: ONE terminal command, ONE task, or ONE question per message. WAIT for output/answer before the next step.
- Keep responses brief. Multiple commands or questions per message causes me to lose track.
- This is binding throughout the entire session, including under fatigue or complex multi-stage work.

## Project knowledge precedence

When repo information is needed (file contents, current versions, doc text, config values), search project knowledge FIRST. If not found, ask me or read from disk. Never assume, guess, or compose from memory. Project knowledge is the authoritative source for repo state.

## When I question an answer

When I question one of your answers ("how can X be Y?" / "but isn't Y supposed to be Z?"), treat that as a signal to investigate the underlying source — query the DB, read the file, run the probe. Defending the original answer with more elaboration is the anti-pattern. See `archive/LESSONS.md` L032.

- My clarifying question IS the uncertainty signal. Defend past it and we drift.
- Right move: query underlying state. Wrong move: re-explain with more confidence.
- If the data confirms the original answer, paste the data verbatim. If the data contradicts, update the answer and note the correction.

## Standards file pointers (load these when their topic is in scope)

| When working on... | Load |
|---|---|
| Anything code | `docs/standards/ENGINEERING_STANDARDS.md` |
| CI/CD, deploy scripts | `docs/standards/CICD_STANDARDS.md` |
| Tests / validators | `docs/standards/VALIDATION_STANDARDS.md` |
| Documentation, manifest, CHANGELOG | `docs/standards/PROJECT_STANDARDS.md` |
| Drafting a multi-file AI prompt | `docs/standards/PROMPT_STANDARDS.md` |
| Memory hygiene | `docs/standards/MEMORY_PROTOCOL.md` |

## Cursor prompt delivery format

Deliver multi-file Cursor prompts as ONE continuous plain-text block, wrapped in a single outer 4-backtick code fence (so inner triple-backtick blocks render correctly). No section headers or `---` dividers outside the fence. I copy the entire block in one action and paste into Cursor.

<!-- ================================================================ -->
<!-- TIER B — PROJECT-SPECIFIC FACTS (revisit when project environment changes) -->
<!-- ================================================================ -->

## Critical files (always Major; full workflow + extra care)

```
<critical_file_1>
<critical_file_2>
<critical_file_3>
<critical_doc_1>
docs/documents_manifest.md
```

## Standard commands

- Test orchestrator: `<command>`
- Lint: `<command>`
- Pre-push governance: `python scripts/check_doc_coverage.py && python scripts/check_test_coverage_drift.py --ci`
- Local YAML check (for `.gitlab-ci.yml`): `.venv/bin/python -c "import yaml; yaml.safe_load(open('.gitlab-ci.yml')); print('YAML valid')"`
- Deploy: `<command or "via CI only — manual click in GitLab UI">`

## Environment specifics

- Repo path on this machine: `<absolute path>`
- Language version: `<e.g., Python 3.11.15>`
- Virtual env activation: `<e.g., source .venv/bin/activate, or invoke .venv/bin/python directly>`
- Key infrastructure: `<e.g., "Staging VPS at <IP>, Production VPS at <IP>; SSH keys at ~/.ssh/<key-name>">`

## Domain-specific quirks (worth flagging once)

- `<quirk 1: e.g., "Configs are deep-copied via get_config; never mutate the returned dict">`
- `<quirk 2: e.g., "GitLab CI_COMMIT_SHORT_SHA is 8 characters, not 7">`
- `<quirk 3: e.g., "All registry image tags use 8-char SHA">`

## Multi-agent coordination (OPTIONAL — only if this project uses a second AI agent)

Include this sub-block ONLY if your project uses Codex / Devin / another AI agent alongside Claude. Single-agent projects: delete this entire block before saving.

- This project uses a secondary AI agent (`<agent name>`) for `<domain — e.g., "charting and frontend work">`.
- The Codex handoff protocol from `CLAUDE.md` § 14 applies. Each agent operates in its declared domain; Claude does all central bookkeeping on the secondary agent's behalf.
- When the operator pastes a Codex session summary: verify it via filesystem (`git status`, `git diff`), check it against the relevant tracker, run governance scripts, code-review (per `CLAUDE.md` § 8.5), commit (per `CLAUDE.md` § 11).
- Tracker ownership is declared per-tracker via `Owner:` header — see `PROJECT_STANDARDS.md` § 7.7.

<!-- ================================================================ -->
<!-- TIER C — PER-SESSION BITS (NOT in Project Instructions field; -->
<!-- these go in the FIRST USER MESSAGE of each session) -->
<!-- ================================================================ -->

<!--
First-message template for each session:

<PROJECT NAME> — <day> session.

Today's priorities (in order):
1. <Task 1>
2. <Task 2>
3. <Task 3>

Total expected: <duration estimate>. Saving <deferred items> for later.

Current state:
- origin/master tip: <SHA>
- <Phase or sprint status>
- <Anything special: pipelines green/red, environment differences, recent changes>

Apply session interaction protocol from message 1: brief overview, then ONE
command/task/question per message, wait for output. Do not batch.

Start by giving me <a brief overview of Task 1>, then we begin.
-->
````

---

## 5. Section-by-section meta-guidance

### 5.1 Project identity (Tier A, line 1)

One sentence. The agent uses this to apply correct defaults — assuming wrong (e.g., assuming a web app when it's a CLI tool) corrupts every subsequent suggestion. Specifically include:

- Project name
- Primary domain (one or two words)
- Primary language(s) and runtime versions
- Deployment shape (one phrase)

Don't write a marketing sentence. Write a technical inventory.

### 5.2 Binding rules block (Tier A)

This is the most-cited section in every session. Three sub-blocks:

- **Reference to CLAUDE.md** — never restate the rules
- **Change classification + workflow + response shape** — these are binding for every Major change
- **Multi-file edit + governance + commit discipline** — Rules 4, 6, 7 are most often violated by agents acting on autopilot; reminder here is worth its weight

### 5.3 Session interaction protocol (Tier A)

The single most underrated discipline in this entire system. Without it, agents batch multiple things into single responses and you lose track within ~5 turns. Codifying the protocol in Project Instructions means it's enforced from message 1, not from "wait, slow down" three turns in.

Three components, all binding:
- Brief overview first
- One command/task/question per message
- Wait for output/answer before next step

### 5.4 Project knowledge precedence (Tier A)

Stops the agent from guessing when an authoritative source exists. Every project hits this within the first session — the agent confidently states a config value or file location that turns out to be wrong. The rule prevents it.

### 5.5 Standards file pointers (Tier A)

The dispatcher table. Tells the agent which focused doc to load when. This mirrors the dispatcher in `CLAUDE.md` § 12 — and the duplication is intentional (and isolated). Project Instructions need to be self-contained because they fire before the agent has read CLAUDE.md.

When standards files are added or renamed in the standards repo, this table updates in lockstep.

### 5.6 Cursor prompt delivery format (Tier A)

A specific operational preference: how Claude.ai should deliver Cursor-bound prompts. Without this, every session re-discovers the formatting (4-backtick wrapper for inner triple-backticks) through trial and error.

### 5.7 Critical files list (Tier B)

Per `CLAUDE.md` § 4 — files where any edit is always Major. Domain-specific. Update when new core files are added or when the project's architecture shifts.

### 5.8 Standard commands (Tier B)

Reference for the agent and a lookup for you when memory blanks. Update when commands change (new test runner, deprecated lint, etc.).

### 5.9 Environment specifics (Tier B)

Path facts that don't live in the repo (Mac path, SSH key paths, infrastructure IPs). These could go in user memory but tend to be project-scoped — putting them here keeps memory cleaner.

### 5.10 Domain-specific quirks (Tier B)

Each entry should be a single-sentence rule that has bitten you at least once. Not "best practices in general" — specific gotchas for this project. Examples from a reference project: the 8-char SHA gotcha, the deep-copy config invariant, the manifest tracking exclusions.

### 5.10a Multi-agent coordination (Tier B; OPTIONAL)

Include this sub-block only if your project uses a second AI coding agent (Codex / Devin / other) alongside Claude. Single-agent projects delete it entirely before saving the Project Instructions field.

The block names which agent handles which domain and references the canonical handoff protocol in `CLAUDE.md` § 14 — it doesn't restate the protocol. Tier B is for project-specific facts; the protocol itself is binding in CLAUDE.md.

When to update this block:
- A new agent joins the project (rare; significant change — Major workflow applies)
- The agents' domain boundaries shift (e.g., Codex takes over a new area)
- A new tracker is added that needs ownership declared

### 5.11 Per-session first-message template (Tier C)

Goes in the first user message of each session, NOT in Project Instructions. Two reasons:
- Priorities change every session; storing them in Project Instructions creates stale data
- Current state (branch SHA, phase status) changes constantly; same problem

The template lives in the file as reference for what each session's first message should look like.

---

## 6. When to update each tier

| Tier | Update frequency | Trigger |
|---|---|---|
| A — Static frame | Quarterly or rarely | Standards evolved (new file in `docs/standards/`, new standing rule in `CLAUDE.md`, new dispatcher target) |
| B — Project-specific facts | Monthly or as needed | New critical file; environment moved (new VPS, new key, new CI provider); standard command changed; new domain quirk |
| C — Per-session bits | **Every session** | Always — Tier C is the per-session opener |

### Update protocol

When updating Tiers A or B:
1. Edit the Project Instructions field directly in Claude.ai
2. Save
3. Update this template file (`PROJECT_INSTRUCTIONS_TEMPLATE.md`) if the change is portable to other projects
4. If the change reflects a new standing rule or pattern, also update `CLAUDE.md` and propagate to the relevant `docs/standards/*.md` file

When updating Tier C:
1. Just type the new first message — no Project Instructions edit needed

---

## 7. Anti-patterns to refuse

Each pattern below was observed at some point on a reference project. Each costs context, drift, or lost time.

### 7.1 Restating CLAUDE.md rules in Project Instructions

❌ Pattern: copying the 9 standing rules into Project Instructions verbatim "for emphasis."

Why bad: creates two copies of the same rules. When CLAUDE.md evolves (and it does — yours grew from 0 → 8 rules over Phase 2-3), one copy drifts behind the other. Eventually they contradict, and the agent has no canonical source.

✅ Fix: reference CLAUDE.md, never restate. "Strictly follow CLAUDE.md" + cite specific rules at point of use ("per Rule 6") is the entire pattern.

### 7.2 Storing per-session state in Project Instructions

❌ Pattern: putting "current branch tip: f2f3d3f" or "today's priorities: 1. Task 3.5..." into Project Instructions.

Why bad: Project Instructions persist across sessions. Per-session data goes stale immediately and the agent reads outdated context. Worse than no context.

✅ Fix: Tier C goes in the first user message of each session, never in Project Instructions.

### 7.3 Lengthy domain explanation in Project Instructions

❌ Pattern: 5-paragraph description of what the project is, including history, architecture, and trade-offs.

Why bad: bloats every session's context window. Agent skims long preambles and misses what matters.

✅ Fix: one-line domain description in Tier A. Anything longer goes in `README.md` or `docs/`. Reference, don't restate.

### 7.4 Batching multiple session protocols

❌ Pattern: "Apply the session protocol unless we're doing exploration, in which case batching is fine, except for code edits where..."

Why bad: agents interpret conditional protocols inconsistently. Some treat them as "do X", others as "do Y", others as "ask the user."

✅ Fix: one binding protocol, no conditionals. If exploration sessions need different rules, set up a separate Project for them with its own Instructions.

### 7.5 Forgetting to update Tier B when environment changes

❌ Pattern: VPS migration happens; Tier B still references the old IP and key path. Agents follow the wrong instructions for weeks until somebody notices.

Why bad: silent drift between docs and reality is the failure mode CLAUDE.md Rule 6 ("verify via filesystem") exists to prevent. Tier B IS the docs in this case.

✅ Fix: when an environment piece changes, the same commit/PR that changes the infrastructure includes a Tier B update. Treat Project Instructions as a tracked artifact.

### 7.6 Hedge language in protocol sections

❌ Pattern: "Try to follow the session protocol when possible" / "Generally apply the response shape from CLAUDE.md § 6"

Why bad: agents interpret hedges inconsistently — same problem as `PROMPT_STANDARDS.md` § 6.6. "Try to" reads as "optional" to many models.

✅ Fix: binding language. "Strictly follow." "Apply." "Use." "Wait for output before next step." No softening.

### 7.7 Missing project knowledge precedence rule

❌ Pattern: Tier A omits the precedence rule. Agent confidently states a config value or file path from training-data priors.

Why bad: project knowledge IS the source of truth for repo state. Without an explicit "search project knowledge first" rule, the agent reverts to its trained defaults.

✅ Fix: explicit precedence rule in Tier A. The agent searches project knowledge before guessing or asking.

---

## 8. Worked example — a reference project

This is what the actual Project Instructions field looks like for a reference project as of 2026-04-25. Use as reference when adapting the template for new projects.

<!--
================================================================
TIER A — STATIC FRAME
================================================================

You are working on a reference project, a Python-based automated trading
signal platform that detects 8-point pivot patterns and delivers signals
to Expert Advisors via API.

## Binding rules

Strictly follow `CLAUDE.md` in the repo. It is binding, not advisory. When
`CLAUDE.md` and a request conflict, refuse or propose a compliant alternative
— do not silently override.

For any change:
- Classify per `CLAUDE.md` § Change Classification (Minor vs Major) before implementing.
- Any edit to `core/pattern_engine.py`, `config/instrument_config.py`,
 `config/condition_strategy_config.py`, `strategies/strategy_*.py`,
 `strategies/engine/*.py`, `validation/validate_*.py`, `market_bias/market_bias.py`
 or `market_bias/utils.py`, `config/live_feed_config.py`,
 `docs/<domain-spec>_combined.md`, or `docs/documents_manifest.md`
 is always Major. If unsure, classify as Major.
- Major changes follow the full workflow: Analyze → Design → Implement → Sync → Validate.
- For Major changes: propose the plan before implementing. If I asked only for a plan,
 do not implement until I confirm.
- Use the response shape from `CLAUDE.md` § 6 when reporting completed work.

For multi-file edits:
- Follow `docs/standards/PROMPT_STANDARDS.md` (ALLOWLIST + verbatim FIND/REPLACE +
 governance verification + files-modified checklist).
- Per `CLAUDE.md` Rule 6: verify via `git status --short` BEFORE every `git add`.
 Paste governance script outputs verbatim.
- Per `CLAUDE.md` Rule 4: commit messages with backticks, em-dashes, or any special
 characters use `git commit -F /tmp/<file>.txt`.

## Session interaction protocol

- Brief full-picture overview first.
- Then strictly step-by-step: ONE terminal command, ONE task, or ONE question per message.
 WAIT for output/answer before the next step.
- Keep responses brief.

## Project knowledge precedence

Search project knowledge FIRST for any repo info. Never assume or compose from memory.
Project knowledge is the authoritative source for repo state.

## Cursor prompt delivery

Deliver multi-file Cursor prompts as ONE continuous plain-text block in a single outer
4-backtick fence. No section headers or `---` dividers outside the fence.

================================================================
TIER B — PROJECT-SPECIFIC FACTS
================================================================

## Critical files (always Major)

```
core/pattern_engine.py
config/instrument_config.py
config/condition_strategy_config.py
config/live_feed_config.py
strategies/strategy_*.py
strategies/engine/*.py
validation/validate_*.py
market_bias/market_bias.py
market_bias/utils.py
docs/<domain-spec>_combined.md
docs/documents_manifest.md
```

## Standard commands

- Test orchestrator: `python -m validation.run_all`
- Pre-push governance: `.venv/bin/python scripts/check_doc_coverage.py && .venv/bin/python scripts/check_test_coverage_drift.py --ci`
- Local YAML check: `.venv/bin/python -c "import yaml; yaml.safe_load(open('.gitlab-ci.yml')); print('YAML valid')"`
- Deploy: via CI only — staging auto-deploys on master push; prod is manual-click in GitLab UI

## Environment specifics

- Repo path on Mac: `/Users/you/Documents/a reference project`
- Python: 3.11.15 via Homebrew at `/usr/local/bin/python3.11`
- Venv: `source .venv/bin/activate` OR invoke `.venv/bin/python` directly
- Staging VPS 1: `91.98.91.129`, SSH `ssh -i ~/.ssh/app_staging deploy@91.98.91.129`
- Production VPS 2: `188.245.172.198` (manual deploy gate)

## Domain-specific quirks

- GitLab `$CI_COMMIT_SHORT_SHA` is 8 characters, not the 7-character git default. All
 registry image tags use 8 chars. Always use 8 chars when probing the GitLab Container
 Registry for image existence.
- `pyyaml` is intentionally NOT in `requirements.txt` (would bloat prod Docker images).
 Local-only helper; install in `.venv` for governance YAML checks.
- `deploy.sh` v3.0 overwrites operator docker auth on every CI run. Manual `rollback.sh`
 use after a CI deploy requires re-login first.
- Manual `rollback.sh` invocations on VPS 1 must source `.env` for Telegram alerts to
 fire. Use the documented SSH wrapper.
- Production VPS 2 untouched since Phase 1 — first prod deploy of `deploy.sh` v3.0 +
 `healthcheck.sh` v1.2 planned for after Phase 3 closes.
-->

---

## End of template

Project Instructions are the first thing every session sees and the most-cited piece of context across an entire project's lifetime. Treat the field as a tracked artifact: update it deliberately, version-control changes via this template file, and never let it drift from the standards it references.

When a new pattern emerges from a working session that should generalize across projects, **update this template** — and only this template. Each project's actual Project Instructions field is a customization of the template, not a fork.
