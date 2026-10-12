<!-- VERSION: 1.2 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.2 — 2026-10-12 — Standard Set Version v2.8: § 4.6 fix line no longer names the Project Instructions template file (never delivered to projects — the reference dangled in every copy; L068 recurrence).
v1.1 — 2026-08-19 — Standard Set Version v2.2 (domain-neutral scrub): 3 example paths still carried a real username (survived the v1.0 genericization — the identifier-token class) → `/Users/you/...`.
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

# MEMORY_PROTOCOL.md — Memory Hygiene for Claude.ai Sessions

**Scope:** This document governs what gets stored in Claude.ai's persistent memory system, what does NOT, and how to keep memory aligned with source-of-truth files in the repo. It is loaded when the work involves managing memory entries explicitly (adding, removing, auditing) or when a session shows memory-related drift symptoms.

**Why this file exists:** Memory entries accumulate silently. Over months of sessions, the memory window fills with a mix of useful facts, redundant rule restatements, and stale historical state — actively degrading the agent's performance instead of helping. a reference project accumulated ~22 entries across Phases 1-3, and a retrospective audit found roughly half were either redundant (duplicating CLAUDE.md content) or actively stale (referencing facts that had since changed). This protocol prevents that drift by making memory storage deliberate.

---

## Table of Contents

1. [The four memory categories](#1-the-four-memory-categories)
2. [The memory-vs-repo decision rule](#2-the-memory-vs-repo-decision-rule)
3. [Memory entry shape standard](#3-memory-entry-shape-standard)
4. [Anti-patterns to refuse](#4-anti-patterns-to-refuse)
5. [Memory hygiene rituals](#5-memory-hygiene-rituals)
6. [Per-project reset procedure](#6-per-project-reset-procedure)
7. [Memory vs Project Instructions vs CLAUDE.md — disambiguation](#7-memory-vs-project-instructions-vs-claudemd--disambiguation)
8. [Worked example — auditing memory at end of project](#8-worked-example--auditing-memory-at-end-of-project)

---

## 1. The four memory categories

Every memory entry falls into one of four categories. Each has a different lifecycle and different storage rules. Mixing them without separation is what made the original memory accumulation problematic — there was no way to prune one category without auditing the entire memory store.

### Category A — Project-specific facts (store: yes)

**Definition:** Facts about a specific project that don't live in any repo file but are needed every session.

**Lifecycle:** Lives as long as the project does. Updated when the underlying fact changes (new IP, new path, new key).

**Examples:**
- Repo path on the local machine
- VPS IP addresses, SSH key paths, deploy token IDs
- Operational quirks not documented in the repo (e.g., "always cd to repo root before git operations")
- Production vs staging environment differences not yet doc'd

**Why store:** Saves repeated lookup; can't be in repo (paths are user-specific, IPs are infrastructure-specific).

### Category B — Operational protocols (store: yes)

**Definition:** Workflow conventions and personal preferences that span all projects, not just one.

**Lifecycle:** Long-lived. Updated when the protocol itself evolves (rare).

**Examples:**
- Session interaction protocol (one task per message, brief overview first)
- Cursor prompt delivery format (4-backtick fence wrapper)
- Project knowledge precedence rule
- Git workflow preferences (always check `git status` before `git add`)
- **Permission policy** — which action classes the operator wants always-prompted (e.g., `git push`, edits to critical source files) vs auto-allowed (e.g., governance doc edits, read-only Bash, governance scripts). Memory holds the policy semantics; `.claude/settings.json` allowlist holds the harness-level implementation that mirrors it.

**Why store:** These are user-wide conventions that apply across every project; storing them in memory means every session — in any project — applies them automatically.

**Note on the permission-policy / settings.json mirror.** Permission policy is a special case of Category B: it lives in *two* places (memory + `.claude/settings.json`). The memory file is the source of truth for the *semantics* — "always ask for git push because operator wants the push trigger gated per CLAUDE.md § 11" — and the settings.json allowlist is the harness-level enforcement. If they ever drift, memory wins and settings.json is updated to match. The split exists because the harness only consumes settings.json (memory is invisible to it), and humans only easily consume memory (settings.json is terse pattern syntax). Keeping both in sync — and the memory file declaring itself as the authoritative semantics — is the discipline.

### Category C — CLAUDE.md / standards-doc rule restatements (store: NO)

**Definition:** Content that's already in `CLAUDE.md`, `PROMPT_STANDARDS.md`, or another standards file in the repo.

**Lifecycle:** N/A — should never be in memory.

**Examples (all anti-patterns):**
- The 9 standing rules verbatim
- The multi-file Cursor prompt construction rules
- The change classification table
- The validation checklist

**Why NOT store:** The agent reads these files every session. Memorizing the same content creates two copies — when the standards docs evolve (and they do), one drifts behind the other. Eventually they contradict, and the agent has no canonical source.

### Category D — Historical state / current status (store: NO)

**Definition:** Facts about the current state of the project that change frequently — commit SHAs, current phase status, in-flight task numbers, "what's next" lists.

**Lifecycle:** N/A — should never be in memory. Decays into noise within days.

**Examples (all anti-patterns):**
- "Phase 3 complete through Task 3.2"
- "Origin/master tip: 9e44b4e"
- "Current task: Task 3.4 — auto-rollback CI job"
- "Last deploy: 2026-04-24 v3.0"

**Why NOT store:** This information goes stale instantly. The repo's tracker (`docs/<project>_setup_tracker.md`), the `git log`, and the project's CHANGELOG are the canonical sources for current state. Querying them is more reliable than querying memory.

---

## 2. The memory-vs-repo decision rule

The single decision rule for whether to memorize anything:

> **If the information lives in a file the agent reads on every session (`CLAUDE.md`, `docs/documents_manifest.md`, the tracker, etc.), don't memorize it.**
>
> **If it's needed every session but isn't in any repo file (Mac path, SSH credentials, personal preferences), memorize it.**
>
> **Memory is for the gap between "needed every session" and "in the repo."**

### Decision flowchart

```
Is the information needed every session?
├── No → Don't store. Reference on demand.
└── Yes → Is it in a repo file the agent reads on every session?
 ├── Yes → Don't store. Avoid duplication.
 └── No → Is it a current-state fact that changes frequently?
 ├── Yes → Don't store. Will go stale. Query source instead.
 └── No → STORE. This is what memory is for.
```

### Apply the rule before adding any entry

When tempted to add a memory entry, walk the flowchart. Most candidates fail at one of the gates. The remaining candidates — the genuine Category A and Category B entries — are what memory should hold.

---

## 3. Memory entry shape standard

Memory entries that follow the shape standard below are easier to audit, easier to update, and less prone to drift.

### 3.1 One atomic fact per entry

Memory entries should be **single declarative sentences**, not multi-clause paragraphs. Why: when an underlying fact changes, you need to update one entry, not parse a paragraph for the relevant clause.

- ❌ Wrong: "User is working on a reference project which uses Python 3.11 at /usr/local/bin/python3.11 with venv at .venv (rebuilt 2026-04-24) and the repo is at /Users/you/Documents/a reference project."
- ✅ Right (4 separate entries):
 - "a reference project repo path on Mac: /Users/you/Documents/a reference project."
 - "Python 3.11.15 installed via Homebrew at /usr/local/bin/python3.11."
 - "Repo .venv rebuilt on 3.11 (2026-04-24)."
 - "Activate venv: source .venv/bin/activate OR invoke .venv/bin/python directly."

### 3.2 Avoid embedding rules

Don't put rule content in memory. Reference the source file instead.

- ❌ Wrong: "Rule: always run check_doc_coverage.py and check_test_coverage_drift.py before push, both must exit 0."
- ✅ Right: don't store at all. CLAUDE.md Rule 2 covers this. The agent reads CLAUDE.md every session.

### 3.3 Date-stamp historical entries

If an entry references a fact that COULD become stale (e.g., "rebuilt 2026-04-24"), include the date in the entry. Makes staleness visible during audit.

### 3.4 Use the explicit memory tool, not implicit memorization

Use the `memory_user_edits` tool to add/remove entries explicitly. Implicit memorization (the agent deciding to remember based on conversation) is opaque and uneditable.

**Note on memory implementation shapes:** The rules in this file apply regardless of where memory is physically stored. Different agent runtimes use different storage:

- **Claude.ai memory store:** centralized, single-sentence entries indexed numerically
- **Claude Code's auto-memory:** file-based shape — one Markdown file per memory entry under the project's memory directory, plus a `MEMORY.md` index file listing all entries with one-line hooks
- **Other tools:** vary

The four memory categories (§ 1), the memory-vs-repo decision rule (§ 2), the anti-patterns (§ 4), and the hygiene rituals (§ 5) apply across all shapes. The shape only affects the mechanics of adding / removing / inspecting entries.

### 3.5 Anti-pattern lengths to avoid

If an entry runs longer than ~200 characters, it's probably:
- A multi-fact entry that should be split
- Rule content that belongs in a standards file
- Historical narrative that belongs in `archive/postmortems/`

Split, move, or delete.

---

## 4. Anti-patterns to refuse

Each pattern below was observed during the a reference project memory accumulation. Each cost real performance — either through drift, staleness, or memory-window bloat.

### 4.1 Memorizing the 9 standing rules from CLAUDE.md

❌ Pattern: adding entries like "CLAUDE.md Rule 4: commit messages with backticks must use git commit -F /tmp/<file>.txt" to memory.

Why bad: CLAUDE.md is read every session. The rule is already in context. Memorizing it creates two copies that can drift. When you update CLAUDE.md (and you will), the memory copy is now wrong. The agent has no way to know which is canonical.

✅ Fix: don't memorize rule content. The agent reads CLAUDE.md fresh every session.

### 4.2 Memorizing current Phase status

❌ Pattern: "Phase 3 complete through Task 3.2 as of 2026-04-24."

Why bad: stale within hours of the next commit. By the next session, Phase 3 might be through Task 3.5. The memory entry now contradicts reality, and the agent has to decide which to trust.

✅ Fix: query `docs/<project>_setup_tracker.md` for current state. Tracker is updated in the same commit as the work — always accurate.

### 4.3 Memorizing commit SHAs

❌ Pattern: "Origin/master tip: 9e44b4e (rollback.sh v0.3)."

Why bad: stale on the next commit. Tomorrow's tip is a different SHA. The agent loses confidence in memory accuracy ("the SHA in memory might be stale, let me check") — at which point the memory entry stops saving any time.

✅ Fix: `git log -1 --oneline` is faster and always correct.

### 4.4 Multi-paragraph memory entries

❌ Pattern: a 500-character entry covering history, current state, what's next, and three operational quirks.

Why bad: the agent reads memory entries shallowly when there are many of them. Long entries get skimmed; specific facts buried in them get missed. Also: hard to update — when one of the three quirks changes, you have to surgically edit the entry without disturbing the other content.

✅ Fix: split into atomic single-sentence entries.

### 4.5 Memorizing rule rationale ("why we do X")

❌ Pattern: "We use fix-forward instead of git push --force because force-push erases history and the lessons that history captures."

Why bad: the rationale belongs in `archive/LESSONS.md` (incident → rule → why). Memory should hold what to do, not why. The why is reference material, loaded on demand.

✅ Fix: rationale lives in `archive/LESSONS.md`. Memory holds the rule reference if anything: "Per CLAUDE.md Rule 3, fix-forward not amend." (And even this is questionable — see § 4.1.)

### 4.6 Cross-project entries that should be project-specific

❌ Pattern: "Project's repo path is /Users/you/Documents/a reference project" stored in user-wide memory while working on a different project.

Why bad: the entry now applies (incorrectly) to every project. The agent uses the wrong path on a different project's session.

✅ Fix: Project-specific facts go in the **Project Instructions** field of that project (Tier B — the curator keeps the Project Instructions template), not in user-wide memory. Memory is for facts that span all projects.

### 4.7 "We discussed this before" memorization

❌ Pattern: "User prefers <X>" memorized after the user mentioned it once in passing.

Why bad: a single mention isn't a preference. It might have been situational. Memorizing it without confirmation creates an apparent preference that the user didn't actually establish.

✅ Fix: only memorize a preference when the user explicitly says "remember that I prefer X" or after the same preference comes up in 3+ sessions.

### 4.8 Memorizing what an existing standards file already covers

❌ Pattern: "Multi-file Cursor prompts must include ALLOWLIST + verbatim FIND/REPLACE + checklist."

Why bad: that's PROMPT_STANDARDS.md content. The agent loads PROMPT_STANDARDS.md when drafting prompts — memorizing the content duplicates and risks drift.

✅ Fix: don't memorize what a standards file covers. Trust the dispatcher pattern — the agent loads the right file when it's relevant.

### 4.9 Trusting recalled memory without verification

❌ Pattern: agent recalls a memory entry that names a file path / function / config key / version, then recommends action based on the recalled fact without verifying it's still accurate.

Why bad: memory captures state at a point in time. By the next session (or the one after), files may have been renamed, functions extracted, config keys renamed, versions bumped. A memory that says "X exists" is a claim that X existed when the memory was written — not that X exists now.

Per `archive/LESSONS.md` L032 — when the operator questions an answer (including a memory-backed answer), the right move is to investigate the underlying source, not to defend the memory with more elaboration.

✅ Fix:

- If memory names a file path: check the file exists (`ls`, `find`) before recommending action
- If memory names a function / flag / config key: `grep` for it
- If the user is about to act on a memory-backed recommendation: verify first
- If recalled memory contradicts what the filesystem shows: trust the filesystem, update or remove the stale memory

Memory is for **continuity across sessions**, not for **dispositive facts about current state**. Verify before recommending.

---

## 5. Memory hygiene rituals

Memory hygiene is not automatic. Without periodic audits, the four categories blur and the memory store accumulates entries that should have been deleted.

### 5.1 Quarterly audit (every ~3 months)

Open the memory tool, view all entries, and walk each one against the four-category test:

1. **Is this Category A or B?** (Project-specific fact or operational protocol — store)
2. **Is this Category C?** (Rule restatement — DELETE; reference standards file instead)
3. **Is this Category D?** (Historical state — DELETE; query source instead)
4. **Is this still accurate?** (Date-stamped facts — verify; if stale, update or delete)

Document the audit in `archive/postmortems/YYYY-MM-DD-memory-audit.md` if substantial changes happened. Brief audits don't need a postmortem.

### 5.2 Per-project reset

When starting a new project, prune project-specific entries from the previous project. See § 6 for the procedure.

### 5.3 Post-major-change update

When a significant fact changes (new VPS, new repo path, key rotation, version bump on a referenced tool), update the matching memory entry **in the same session** as the change. Don't defer.

Examples:
- VPS migrated → update the entry referencing the old IP
- `deploy.sh` bumped from v3.0 → v3.1 → update the entry referencing it (if any)
- `.venv` rebuilt with new Python version → update the version entry

### 5.4 Detection signals — when to do an unscheduled audit

Run an audit immediately if:
- The agent confidently states a fact that turns out to be wrong (likely a stale memory entry)
- A session loads with confusing or contradictory context (likely Category D bloat)
- You realize you've been adding entries faster than removing them for ~1 month (drift accumulating)
- You start a new project and the previous project's facts keep "leaking" into context (prune trigger)

### 5.5 Verify recalled memory before recommending action

Per `archive/LESSONS.md` L032 — a memory entry that names a specific file path / function / flag / config key is a claim that it existed **when the memory was written**. By the time the entry fires, it may have been renamed, removed, or never merged. Before recommending action based on memory:

- If the memory names a file path: check the file exists
- If the memory names a function or flag: `grep` for it
- If the user is about to act on the recommendation (not just asking about history): verify first

**"The memory says X exists" is not the same as "X exists now."**

A memory that summarizes repo state (activity logs, architecture snapshots) is frozen in time. If the user asks about *recent* or *current* state, prefer `git log` or reading the code over recalling the snapshot.

When a recalled memory conflicts with current information observed via filesystem / grep / DB query: **trust what you observe now**, and update or remove the stale memory rather than acting on it.

---

## 6. Per-project reset procedure

When starting a new project, the previous project's memory state needs to be cleaned up. Procedure:

### 6.1 List all current memory entries

Use the memory tool's `view` command. Get the complete numbered list.

### 6.2 Categorize each entry

For each numbered entry, mark it:
- **K** — Keep (Category A or B that still applies; or A/B that applies cross-project)
- **M** — Move (Category A that's project-specific; should go in the new project's Project Instructions Tier B instead)
- **D** — Delete (Category C, Category D, or stale Category A from the previous project)

### 6.3 Execute the cleanup

- For **D** entries: use the memory tool's `remove` command, working from highest line number down (so renumbering doesn't break in-flight removals).
- For **M** entries: copy the content to the new project's Project Instructions Tier B section, then `remove` from memory.
- For **K** entries: leave alone.

### 6.4 Verify post-cleanup state

`view` the memory store again. Confirm only Category A (cross-project facts) and Category B (operational protocols) remain. Total entry count should typically drop by 30-60% after a per-project reset.

### 6.5 Document the reset

Add a one-line entry to `archive/lessons.md` or wherever you track standards-repo evolution: "YYYY-MM-DD — Memory reset for new project <name>. Removed N stale/project-specific entries. Kept M cross-project entries."

---

## 7. Memory vs Project Instructions vs CLAUDE.md — disambiguation

Three different artifact categories have overlapping use cases. Knowing which is which prevents the duplication that drift problems start from.

| Artifact | Scope | Lifecycle | What it holds |
|---|---|---|---|
| **CLAUDE.md** | Per-project (in repo) | Stable; rules added when something breaks | Binding rules, critical files, workflow, response shape |
| **Project Instructions Tier A** | Per-project (Claude.ai field) | Stable | Reference to CLAUDE.md, session protocol, dispatcher pointers |
| **Project Instructions Tier B** | Per-project (Claude.ai field) | Stable; updated on env change | Project-specific facts: paths, commands, environment, domain quirks |
| **User-wide memory** | Cross-project | Stable; pruned periodically | Cross-project operational protocols (Category B); rare cross-project Category A facts |

### Decision rules

- **Is it a binding rule?** → CLAUDE.md (per-project; cited from elsewhere by reference)
- **Is it a project-specific fact?** → Project Instructions Tier B (per-project; never user-wide memory)
- **Is it a cross-project workflow preference?** → User-wide memory (Category B)
- **Is it a one-off conversation-level preference?** → Don't store. Just say it in the prompt.

### Common mistake: storing project-specific facts in user memory

This is the most common pattern and the most damaging. Project-specific facts in user memory cause "context bleed" — the next project's session inherits the previous project's IP addresses, paths, and quirks. Always Project Instructions Tier B for project-specific facts.

---

## 8. Worked example — auditing memory at end of project

Below is a worked example showing how a memory audit at the end of a project phase looks. Use as reference for your own audits.

<!--
a reference project end-of-Phase-3 audit (hypothetical, post-project-close):

Pre-audit state: 22 memory entries.

Audit walk:

| # | Entry summary | Category | Action |
|---|---|---|---|
| 1 | User uses Claude Opus for coding via Cursor extension | B (cross-project tool preference) | KEEP |
| 2 | Multi-file Cursor prompts protocol | C (covered by PROMPT_STANDARDS.md § 3) | DELETE |
| 3 | Phase 3 complete through Task 3.2 as of 2026-04-24 | D (historical state) | DELETE |
| 4 | Staging VPS 1 IP, SSH key path, layout | A (project-specific) | MOVE to Project Instructions Tier B |
| 5 | Production VPS 2 IP, status | A (project-specific) | MOVE to Project Instructions Tier B |
| 6 | CI/CD pipeline 6-stage layout | C (covered by CICD_STANDARDS.md) | DELETE |
| 7 | The 8 CLAUDE.md standing rules part 1 | C (covered by CLAUDE.md) | DELETE |
| 8 | The 8 CLAUDE.md standing rules part 2 | C (covered by CLAUDE.md) | DELETE |
| 9 | The 8 CLAUDE.md standing rules part 3 | C (covered by CLAUDE.md) | DELETE |
| 10 | Phase 3 Deferred Items D1-D9 list | D (historical state; lives in tracker) | DELETE |
| 11 | Workflow protocols reinforced across Phase 2 | C (covered by various standards files) | DELETE |
| 12 | Project knowledge precedence rule | B (operational protocol — cross-project) | KEEP |
| 13 | Session interaction protocol | B (operational protocol — cross-project) | KEEP |
| 14 | Cursor prompt delivery format | B (operational protocol — cross-project) | KEEP |
| 15 | Cursor prompt construction additional rules | C (covered by PROMPT_STANDARDS.md) | DELETE |
| 16 | Local Mac dev environment Python 3.11.15 | A (project-specific paths) | MOVE to Project Instructions Tier B |
| 17 | Phase 3 task order reversed reasoning | D (historical state) | DELETE |
| 18 | deploy.sh v3.0 docker auth overwrite | A (project-specific quirk) | MOVE to Project Instructions Tier B (D8) |
| 19 | Manual rollback.sh .env sourcing | A (project-specific quirk) | MOVE to Project Instructions Tier B (D9) |
| 20 | GitLab CI_COMMIT_SHORT_SHA 8 chars | A (project-specific quirk) | MOVE to Project Instructions Tier B |
| 21 | pyyaml local-only governance helper | A (project-specific quirk) | MOVE to Project Instructions Tier B |
| 22 | the standards source repo path on Mac | A (project-specific path) | MOVE to Project Instructions Tier B |

Post-audit state: 4 entries remaining (#1, #12, #13, #14 — all Category B cross-project).
8 entries moved to Project Instructions Tier B.
10 entries deleted (Categories C and D).

Memory store reduced 22 → 4 entries. All remaining entries are cross-project,
none are stale, none duplicate standards file content.
-->

---

## End of protocol

Memory is a tool, not an archive. Treat memory entries the way you treat tracker rows — they earn their place by being currently useful, and they get pruned the moment they stop. Drift is silent; vigilance is the price of memory paying off.

When a new memorization-vs-don't pattern emerges, **add it as an anti-pattern in § 4** with the incident that motivated it. When the four categories stop covering a real case, surface it for protocol revision — but never invent a fifth category casually.
