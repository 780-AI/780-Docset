<!-- VERSION: 1.6 -->
<!-- Last Updated: 2026-05-23 -->
<!-- Source: ~/everon-standards/HOW_TO_USE.md -->
<!--
CHANGE LOG
v1.6 — 2026-05-23 — Set Version v2.5 alignment. § 4.1 standards-loaded reference + § 10 "Where to go next" rule + lesson count refresh: "11 standing rules" → "12 standing rules" (now includes Rule 12 session-wrap-up); "47 lessons (L001–L047)" → "48 lessons (L001–L048)".
v1.5 — 2026-05-22 — Set Version v2.4 alignment. § 4.1 standards-loaded reference + § 10 "Where to go next" rule + lesson count refresh: "10 standing rules" → "11 standing rules" (now includes Rule 11 QA-scenario-coupling); "46 lessons (L001–L046)" → "47 lessons (L001–L047)".
v1.4 — 2026-05-22 — Set Version v2.3 alignment. § 4.1 standards-loaded reference + § 10 "Where to go next" lesson count "44 lessons (L001–L044)" → "46 lessons (L001–L046)" reflecting L045 + L046 added in v2.3.
v1.3 — 2026-05-22 — Set Version v2.2 alignment. § 4.1 Day-One feature-work prompt reference: "9 standing rules" → "10 standing rules" (now includes Rule 9 session-start pre-flight + NEW Rule 10 code-review-before-commit). § 10 "Where to go next" lesson count "43 lessons (L001–L043)" → "44 lessons (L001–L044)". No prompt body content changed. Cross-project backport from EverOn.Capital-Signal commit `717529a`.
v1.2 — 2026-05-22 — Set Version v2.1 fix-forward: bring stale body-text references current. § 10 "Where to go next" lesson-count line "35 lessons, append-only" → "43 lessons, append-only" — the v1.0 / v1.1 set bumps both left this stale; brought current here. No other text changes.
v1.1 — 2026-05-22 — Set Version v2.1 alignment (cross-project SESSION_OPENER merge). § 4.1 Day-One feature-work prompt leads with the SESSION_OPENER pre-flight as the FIRST action (per CLAUDE.md Rule 9 / L043) — overrides the prior "Read CLAUDE.md once to refresh" lead step. Standards-loaded sub-block references the 10-file binding suite + 43-lesson archive (was 9 / 35). No other prompts changed.
v1.0 — 2026-05-16 — Initial release. Practical usage guide for the standards suite. Includes the canonical bootstrap prompt (ready to paste into a fresh Claude session to start a new project from the v1.0 baseline), plus supporting prompts for Day-One feature work, code review, prompt audit, quarterly audit, and lesson backporting. Complements README.md (conceptual overview) and NEW_PROJECT_BOOTSTRAP.md (detailed Day-Zero procedure) with the operator-facing copy-paste workflow.
-->

# HOW_TO_USE.md — Practical Usage Guide

**Scope:** This file is the practical, action-oriented guide for using the standards suite day-to-day. It complements three companion files:

- **`README.md`** — the conceptual overview (mental model, architecture, design rationale)
- **`STANDARDS_INDEX.md`** — the versioned set manifest (per-file versions, Set-Version-bump policy)
- **`NEW_PROJECT_BOOTSTRAP.md`** — the dispositive 13-step Day-Zero walkthrough

This file's job: give you **ready-to-paste prompts** for the common workflows — bootstrapping a new project, doing feature work in an existing one, requesting code review, auditing a prompt, running quarterly hygiene.

**If you only read one prompt:** § 3.1 (the bootstrap prompt). That's the headline deliverable here.

---

## Table of Contents

1. [Three ways to use this suite](#1-three-ways-to-use-this-suite)
2. [Prerequisites](#2-prerequisites)
3. [Bootstrap a new project — the canonical prompt](#3-bootstrap-a-new-project--the-canonical-prompt)
4. [Day-One feature-work prompt (post-bootstrap)](#4-day-one-feature-work-prompt-post-bootstrap)
5. [Code review request prompt](#5-code-review-request-prompt)
6. [Prompt audit prompt (audit your own draft before sending)](#6-prompt-audit-prompt-audit-your-own-draft-before-sending)
7. [Quarterly audit prompt (manifest + lessons + memory hygiene)](#7-quarterly-audit-prompt-manifest--lessons--memory-hygiene)
8. [Backport a lesson from another project](#8-backport-a-lesson-from-another-project)
9. [Common issues & troubleshooting](#9-common-issues--troubleshooting)
10. [Where to go next](#10-where-to-go-next)

---

## 1. Three ways to use this suite

| Scenario | What to do | See |
|---|---|---|
| Starting a brand-new project from scratch | Use the bootstrap prompt in § 3 | § 3 + `NEW_PROJECT_BOOTSTRAP.md` |
| Doing feature work in a project that already adopted the suite | Use the Day-One prompt in § 4 | § 4 |
| Retrofitting an existing project that doesn't yet have the suite | Run the bootstrap prompt against the existing repo (skip Step 1 of NEW_PROJECT_BOOTSTRAP.md; merge changes via a single "adopt-standards" commit) | § 3 + read `NEW_PROJECT_BOOTSTRAP.md` § 13 troubleshooting |
| Maintaining the standards source itself (adding new lessons, refining patterns) | Read `README.md` § 5 (Maintenance protocol) + the Set-Version-bump policy in `STANDARDS_INDEX.md` § 5 | `README.md` § 5 |

---

## 2. Prerequisites

Before running any prompt below, confirm:

1. **You have a local copy of the standards source.** Typical path: `~/everon-standards/` or wherever you cloned the source. The bootstrap prompt asks for this path.
2. **You have decided the project context.** For bootstrap: project name, one-line domain, primary languages, deployment shape, whether you'll use a second AI agent (Codex / Devin / other). For feature work: at minimum, a clear one-sentence task statement.
3. **You're running Claude Code (or equivalent agent with filesystem access)** for bootstrap. Claude.ai can be used for prompt-craft / planning sessions but doesn't have direct file-system access — for bootstrap, Claude needs to read `NEW_PROJECT_BOOTSTRAP.md` from disk, so a file-system-capable agent is required.
4. **You're ready to be the operator.** The prompts establish a step-by-step protocol; you'll authorize each step. Plan ~30-60 minutes for a full bootstrap.

---

## 3. Bootstrap a new project — the canonical prompt

This is the headline prompt. Paste it verbatim into a **fresh Claude (Code) session** in (or pointing at) your new project's working directory, after filling in the bracketed placeholders.

### 3.1 The prompt (copy this whole block)

```
I'm bootstrapping a new project from the EverOn standards suite at Standard Set Version v1.0.

Project context (I'll confirm / refine these during the walkthrough — fill in your best current values):
- Project name: [my-project-name]
- Domain: [one-line description, e.g., "Python-based trading signal platform"]
- Primary languages: [e.g., "Python 3.11, Bash"]
- Deployment shape: [e.g., "Dockerized, GitLab CI → Hetzner VPS via registry-pull"]
- Multi-agent? [yes — if I'll use Codex/Devin alongside Claude / no — single-agent]
- Standards source on this machine: [e.g., "~/everon-standards/"]
- New project repo path on this machine: [e.g., "~/projects/my-project-name/"]

What to do, in order:

1. Read `docs/standards/NEW_PROJECT_BOOTSTRAP.md` (from the standards source path) — this is the dispositive 13-step procedure.
2. Read `docs/standards/STANDARDS_INDEX.md` (same source path) to confirm the current Set Version baseline (v1.0).
3. Give me a brief overview (under 200 words) of what the bootstrap involves end-to-end and what state I'll have when it's complete.
4. Then begin Step 1 of NEW_PROJECT_BOOTSTRAP.md (create the repository). Ask me ONE question at a time about my project context — then WAIT for my reply before continuing to Step 2.

Session protocol — binding from message 1:
- Brief overview first; then ONE command / ONE task / ONE question per message; WAIT for my reply before the next step.
- Render options inline (e.g., "(a) ... (b) ... (c) ... — pick one by letter") — never popup / modal questions.
- Verify via filesystem (`git status`, `cat`, `grep`) before acting — never assume what's there.
- Customize placeholders deliberately — don't fill in defaults silently. If something is unclear, ask.
- Code review BEFORE `git add` — walk each modified / new file in plain English; surface concerns; fix before staging (not after).
- Commit messages via `git commit -F /tmp/<file>.txt` — never `-m` with escapes; never heredoc piped to git commit (silent corruption).
- Don't push. Pushes are operator-gated — I run `git push` after final review.
- If I question an answer ("how can X be Y?"), investigate the underlying source (query DB, read file, run probe) — don't defend the original with more elaboration.
- If you find yourself reaching for a hedge ("maybe", "optionally", "if applicable"), stop and ask me explicitly instead.

At the end of bootstrap (after Step 10 of NEW_PROJECT_BOOTSTRAP.md is complete):
- Summarize what we shipped (files created, manifest entries, governance scripts in place, CI scaffold, first commit SHA).
- Tell me what to do in my NEXT session (Day-One feature work) — point me at § 4 of `docs/standards/HOW_TO_USE.md` for the Day-One prompt.

Start now by reading `NEW_PROJECT_BOOTSTRAP.md` and giving me the overview.
```

### 3.2 How to use this prompt

1. **Open a fresh Claude Code session** in (or pointing at) your new project's intended directory. If the directory doesn't exist yet, that's fine — Step 1 of the walkthrough creates it.
2. **Copy the entire block above** between the triple-backticks (everything from "I'm bootstrapping..." to "Start now by reading...").
3. **Fill in the bracketed placeholders** in the "Project context" section. If you're unsure of any value, leave it as "TBD" — Claude will ask you during Step 1.
4. **Paste into the chat** and send.
5. **Respond to each step one at a time.** Don't batch answers. The protocol catches drift; let it work.

Expected runtime: ~30–60 minutes. Most of that is reading the walkthrough and customizing files. The actual file copying takes ~2 minutes.

### 3.3 Compact bootstrap prompt (for repeat operators)

If you've done this before and don't need the full protocol preamble, use the compact version:

```
Bootstrap a new project from the standards suite at `~/everon-standards/` (Standard Set Version v1.0). Read `docs/standards/NEW_PROJECT_BOOTSTRAP.md` and walk me through the 13 steps. Project: [name]. Domain: [domain]. Languages: [langs]. Deployment: [shape]. Multi-agent: [y/n]. Session protocol: ONE task per message. No push (operator-gated). Begin with the overview.
```

Use the full prompt (§ 3.1) for your first bootstrap and any high-stakes bootstrap. Compact (§ 3.3) is for muscle-memory repeats.

---

## 4. Day-One feature-work prompt (post-bootstrap)

Use this for the FIRST feature-work session after bootstrap is complete. It establishes the working relationship and the standards-driven workflow from message 1.

### 4.1 The prompt

```
I'm working on [project-name], a [one-line domain]. Bootstrapped from Standard Set Version v1.0 on [bootstrap-date].

Standards are loaded:
- `CLAUDE.md` at repo root — binding contract (12 standing rules + change classification + workflow + § 14 Codex handoff if applicable + § 15 plan workflow for vital changes)
- `docs/standards/` — 9 focused standards files (loaded via dispatcher in CLAUDE.md § 12) + `SESSION_OPENER.md` template
- `docs/SESSION_OPENER.md` at project root under docs/ — project-local session-start pre-flight (binding per CLAUDE.md Rule 9)
- `archive/LESSONS.md` (or `docs/standards/LESSONS.md` if it lives there in this project) — 48 lessons capturing why each rule exists

Today's task: [one-sentence description of what you want to accomplish — e.g., "implement user registration with email verification"]

Approach (per CLAUDE.md):
1. **FIRST action — session-start pre-flight per Rule 9.** Read `docs/SESSION_OPENER.md` and execute its § 1 pre-flight (repo state + live system state + tracker tip + memory recall). Post the § 4 first-response output block BEFORE acting on this task.
2. Then re-anchor on CLAUDE.md binding rules (auto-loaded; quick re-read of any section your task touches).
3. Classify the change (Minor vs Major per § 5). Critical-file edits are always Major.
4. If Major: propose the design BEFORE implementing (per § 6 Step 2) — wait for my confirmation.
5. Implement per the appropriate focused standards file (load via dispatcher in § 12).
6. Sync all required docs in the same commit (per `PROJECT_STANDARDS.md` § 4 trigger table).
7. Code review pass on each modified file BEFORE `git add` (per § 8.5).
8. Validate (per § 8 checklist) — governance scripts must exit 0.
9. Commit via `git commit -F /tmp/<file>.txt` (per Rule 4).
10. Don't push — pushes are operator-gated.

Session protocol — binding from message 1:
- Brief overview first; then ONE task per message; WAIT for my reply.
- Render options inline (no popups).
- Verify via filesystem before acting.
- Investigate-when-questioned (per L032) — don't defend; query the data.

Start by reading CLAUDE.md, then giving me a 3-bullet overview of how you'll approach today's task (classification, expected files touched, risk). Then ask me to confirm or adjust before implementing.
```

### 4.2 When to use a different opener

- **Audit / investigation session** (no code changes intended) — use § 7 quarterly audit prompt as a starting point
- **Multi-file edit you've already designed** — skip the design-proposal step and go directly to drafting a Type 1 prompt per `PROMPT_STANDARDS.md` § 3
- **CI/deploy work** — same opener, but explicitly mention the 24h soak rule (L022) if a prod deploy might be in the session's scope

---

## 5. Code review request prompt

Use this when you've drafted changes (yourself or via an agent) and want a quality-review pass BEFORE staging — per `archive/LESSONS.md` L027.

### 5.1 The prompt

```
I have unstaged changes in [project-name]. Before I run `git add`, please do a code review pass per `CLAUDE.md` § 8.5 / `archive/LESSONS.md` L027.

Files to review:
[list of file paths, or "all unstaged changes per `git status --short`"]

For each file:
1. Read it (or read the diff via `git diff <file>`)
2. Walk it in plain English: what changed, what's the intent
3. Check:
   - Does it read correctly?
   - Are edge cases the task implied handled?
   - Is there a subtle bug a future reader would catch?
   - Are there orphan changes (unintentional edits caught in the diff)?
4. Report findings as:
   - 🔴 BUG (must fix before staging) — describe + suggested fix
   - 🟡 IMPROVEMENT (works but suboptimal) — describe + suggested fix
   - 🟢 NIT (cosmetic) — describe, optional fix

Do NOT silently fix issues — surface them; I'll decide which to address before I stage.

After review, summarize: "Stage as-is" / "Fix N items first" / "Reconsider design".
```

### 5.2 When this is appropriate

- After any multi-file change before commit
- After any change to a Critical File (always Major per `CLAUDE.md` § 4)
- After any change to logic / detection / entry / exit / simulation code
- After any change that surfaced unexpected complexity mid-implementation

Skip code review only for trivial single-line fixes that you authored yourself and already mentally verified. When in doubt, ask for review.

---

## 6. Prompt audit prompt (audit your own draft before sending)

When you've drafted a multi-file Cursor / Claude Code prompt (Type 1 per `PROMPT_STANDARDS.md` § 3) and want to audit it before sending — per `PROMPT_STANDARDS.md` § 7 verification ritual.

### 6.1 The prompt

```
I've drafted the following multi-file edit prompt. Audit it per `docs/standards/PROMPT_STANDARDS.md` § 7 (verification ritual) before I send it to the agent.

Audit checklist:
- Are all FIND blocks anchored against current file state (not memory)? Verify by `grep -F` against the actual file.
- Is each FIND anchor unique in its target file?
- Are line counts in the FIND blocks correct (count manually)?
- Could any verification grep false-positive on unrelated content?
- Are STOP conditions explicit on each governance / verification step?
- Does the commit step use `git commit -F /tmp/<file>.txt` (not `-m` with escapes)?
- Is `git status --short` called BOTH before AND after `git add` per Rule 6?
- Is "DO NOT PUSH" stated at the end (if Claude is the agent — not Codex)?
- Does the ALLOWLIST match the actual file set the prompt edits?
- Does the files-modified checklist at the end match the ALLOWLIST exactly?
- Are there any hedges ("maybe", "optionally", "if applicable")? If yes, surface them.
- Pre-draft duplicate check (per § 7.8): grep for what's being added to confirm it doesn't already exist.

Report findings as:
- 🔴 BUG (would cause agent to fail or produce silently-wrong output) — describe + fix
- 🟡 IMPROVEMENT (works but fragile) — describe + suggested fix
- 🟢 NIT (cosmetic, no functional impact) — describe

Do NOT silently fix — surface findings; I'll redraft.

[paste your prompt below this line]
```

### 6.2 When this is appropriate

- Any Type 1 multi-file prompt before sending (per § 1.1 trigger criteria in `PROMPT_STANDARDS.md`)
- Any prompt that modifies a Critical File
- Any prompt going to a second agent (Codex / Devin) — use § 6.1 + the retry-with-deviation-warning shape from `PROMPT_STANDARDS.md` § 9.5 if this is a retry
- When you've been iterating on a prompt and want a fresh pair of eyes

Skipping the audit is gambling. The audit takes ~3 minutes and catches bugs that would otherwise cost ~30 minutes of mid-execution interruption.

---

## 7. Quarterly audit prompt (manifest + lessons + memory hygiene)

Run quarterly (or after detecting drift). Catches manifest drift, stale lessons, unused-but-tracked files, memory bloat.

### 7.1 The prompt

```
Quarterly audit for [project-name]. Per `docs/standards/README.md` § 4.4 (Month One audit checklist) and `MEMORY_PROTOCOL.md` § 5 (hygiene rituals).

Walk the following audits in order. For each, paste raw output (governance commands), then summarize findings.

1. **Manifest sweep** (per `PROJECT_STANDARDS.md` § 2.9):
   - Walk the filesystem: every committed `.md` file under `docs/`, `archive/`, root; every `.py`/`.sh` with VERSION header (`grep -rEn '^(# VERSION:|<!-- VERSION:)' .`)
   - Compare against `docs/_gpt_context_manifest.md` (or `docs/documents_manifest.md`) entries
   - Report: files in filesystem not in manifest; manifest entries pointing at non-existent files; manifest version cells that don't match actual file VERSION header.

2. **Lessons review** (per `archive/LESSONS.md`):
   - For each lesson L001 → LNNN, check: is the rule still in force in CLAUDE.md / the topical standards file? Is the rationale still accurate? Has any rule been silently relaxed without a corresponding lesson update?
   - Report: lessons whose rules have drifted; lessons that should be reinforced because a recent incident reinforces them.

3. **Memory hygiene** (per `MEMORY_PROTOCOL.md` § 5):
   - List all memory entries (Claude Code: read MEMORY.md + all `*.md` under the memory directory; Claude.ai: use the memory tool's view command).
   - Categorize each per the four-category test (A/B store; C/D delete).
   - Report: Category C entries that should be deleted (already in standards files); Category D entries that have gone stale (historical state); Category A entries that are project-specific and should move to Project Instructions Tier B.

4. **CHANGELOG continuity check**:
   - Walk `git log --since="3 months ago" --format='%h %s'` for the audit period
   - Cross-check: does each meaningful commit have a corresponding CHANGELOG.md entry?
   - Report: commits with no CHANGELOG; CHANGELOG entries with no commit reference.

5. **Tracker review** (if your project has a tracker, e.g., `docs/<project>_setup_tracker.md`):
   - Open the tracker; identify rows stuck "In progress" for >2 weeks (likely drift)
   - Identify Deferred Items with stale "Suggested resolution" text
   - Report.

Final summary:
- Total findings per audit (counts)
- Top 3 highest-priority items to address
- Recommended next session: which items to fix first

Do NOT silently fix anything during the audit. Audit only; I'll authorize each fix as a separate task.
```

### 7.2 When this is appropriate

- **Quarterly** as a regular rhythm (every ~3 months) — even if no drift is suspected
- **After a major project phase closes** (e.g., Phase 5 close on EverOn surfaced cleanup work)
- **When you notice the agent stating wrong facts** about repo state (likely stale memory or manifest drift)
- **Before a major refactor** to baseline state cleanly first

---

## 8. Backport a lesson from another project

When a lesson learned on Project B should propagate to the standards source (and from there, optionally to Project A's adopted copy) — per `README.md` § 5.5.

### 8.1 The prompt

```
Backport a lesson from [Project B] to the standards source at [path to standards repo].

The lesson:
- **Trigger / incident** (what specifically failed): [describe]
- **Cost** (time, broken commits, silent corruption, etc.): [describe]
- **Codification** (what rule was added to Project B's CLAUDE.md or standards file): [describe + cite the file]
- **Portability rationale** (why this generalizes beyond Project B): [describe]

Backport procedure (per `README.md` § 5.5):
1. Read the current top of `LESSONS.md` to find the next available L-number.
2. Draft a new lesson entry following the format in `LESSONS.md` § 2 — incident + cost + codification + cross-references.
3. Identify which topical standards file should host the rule body. Update that file with a new sub-section or anti-pattern.
4. Bump the per-file VERSION header + CHANGE LOG entry on every modified file.
5. Update `STANDARDS_INDEX.md` — add a row in the Set Version history if this warrants a Set Version Minor bump (multiple files touched; pattern likely to recur).
6. Update the standards source's `CHANGELOG.md` at the top with the new entry.
7. Commit per the standards source's commit policy.

Session protocol: ONE step at a time. Show me the draft lesson entry first; wait for my approval before modifying the topical standards file. After the topical-file edit, show the diff before I authorize the commit.
```

### 8.2 When this is appropriate

- A debugging session on Project B revealed a pattern that would have helped on Project A
- A new automation / governance pattern emerged that's worth codifying for future projects
- A near-miss caught at design time that could easily have been a real incident (codify the avoidance pattern before it bites)

---

## 9. Common issues & troubleshooting

### 9.1 "Claude doesn't seem to be following the rules"

Most common cause: Claude didn't read CLAUDE.md before starting. The session-opener prompt above includes "read CLAUDE.md first" as the first action. If you skipped that or the agent is somehow ignoring it:

- Explicitly cite the rule by number: "per CLAUDE.md Rule 4, use `git commit -F`"
- Re-state the session protocol in your message: "remember — ONE task per message; wait for my reply"
- If the agent persists in deviating, restart the session with the full opener prompt

If a specific lesson seems unenforced, cite the lesson number too: "per L027, code review BEFORE staging — please walk each file in plain English first".

### 9.2 "I want to update the standards from a newer Set Version"

Per `STANDARDS_INDEX.md` § 4.3 — backports from the source set are explicit. Procedure:

1. Read the source's `STANDARDS_INDEX.md` § 6 (Set Version history) for what changed since your adopted version.
2. For each change relevant to your project, cherry-pick the per-file edits into your local copy.
3. Bump the relevant per-file versions in your local manifest.
4. Record the new "Set Version adopted" in your project's CHANGELOG.md or `docs/standards/SET_VERSION_ADOPTED.md`.

Major Set Version bumps (v1.X → v2.0) include explicit migration notes — read those before backporting.

### 9.3 "I'm using only one agent — can I skip the Codex sections?"

Yes. The Codex handoff protocol (`CLAUDE.md` § 14) is explicitly marked OPTIONAL. Single-agent projects can:

- Delete `CLAUDE.md` § 14 entirely (or keep it for future use — it's small and doesn't fire unless triggered)
- Delete the "Multi-agent coordination" sub-block from `PROJECT_INSTRUCTIONS_TEMPLATE.md` Tier B
- Ignore § 3.11 (Codex handoff variant) of `PROMPT_STANDARDS.md`
- Ignore L020 and L033 in `LESSONS.md` — they remain in the archive as historical context

The bootstrap walkthrough (Step 4 customization) asks you "multi-agent? yes/no" — answering "no" skips the Codex-specific customizations.

### 9.4 "The bootstrap prompt is too long for my use case"

Use the compact bootstrap prompt (§ 3.3) — it's a one-paragraph variant for repeat bootstrappers. Or write your own minimal variant; just ensure it includes:

- Reference to `NEW_PROJECT_BOOTSTRAP.md` as the dispositive procedure
- Project context fields (name, domain, languages, deployment, multi-agent)
- Session protocol (one task per message)
- Explicit "start by reading NEW_PROJECT_BOOTSTRAP.md"

The full prompt's protocol section is binding from message 1; trimming it risks the agent improvising. Compact only if you're confident the agent will inherit your project's protocol from project-level memory / Project Instructions.

### 9.5 "I want to retrofit an existing project, not start fresh"

Run the bootstrap prompt against your existing repo. The walkthrough's Step 1 (create repo) is a no-op for you — your repo already exists. The remaining steps still apply:

- Step 2 copies the standards files into your `docs/standards/` (creating it if needed)
- Step 3 customizes the placeholders against your existing project
- Step 4 creates supporting files (skip any that already exist in your project)
- Step 5–8 add governance scripts, CI scaffold, MR template, first commit

The "first commit" in a retrofit becomes "adopt-standards commit" — bundles all the standards-related additions into one logical commit per the split-commit pattern (`LESSONS.md` L010 + L029). Subsequent feature work follows the Day-One opener (§ 4 above).

---

## 10. Where to go next

- **Bootstrapping right now?** → Copy § 3.1 (full prompt) or § 3.3 (compact); fill in placeholders; paste into a fresh Claude Code session.
- **Already bootstrapped, starting your first feature?** → Copy § 4.1 (Day-One prompt) and adapt.
- **About to send a multi-file Cursor prompt?** → Audit it first using § 6.1.
- **Need a deeper understanding of WHY the suite is structured this way?** → Read `README.md` § 7 (design rationale).
- **Curious about the Set Version concept?** → Read `STANDARDS_INDEX.md` § 5 (how to bump the Set Version).
- **Want to read every lesson?** → `archive/LESSONS.md` (or `docs/standards/LESSONS.md` if your project nests there) — 48 lessons (L001–L048), append-only, each with incident + cost + codification.

---

## End of guide

This file's purpose is to **shorten the gap between "I want to use these standards" and "I'm productively using them."** Every prompt above is calibrated to establish the binding rules from message 1 so you don't have to keep re-explaining the protocol.

When you find a workflow worth a new prompt (e.g., a recurring kind of task that benefits from a structured opener), **add it here** and bump this file's VERSION. New prompts are additive — they expand the operator-facing toolkit without changing the binding rules.

The discipline scales: 30 seconds to paste a calibrated prompt saves 10 minutes of context-setting per session. Slow down to set up well.
