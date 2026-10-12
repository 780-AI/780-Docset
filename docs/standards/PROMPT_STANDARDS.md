<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.1 — 2026-10-12 — Standard Set Version v2.8: NEW § 3.12 relayed prompts and step guides (sent as a file; one self-checking block per step; one results file; bench-tested; plain words — L082, L084, L088); § 6.12 no longer names the Project Instructions template file (never delivered to projects; L068 recurrence).
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

# PROMPT_STANDARDS.md — Drafting Prompts for AI Agents

**Scope:** This document is the working reference for drafting prompts to AI coding agents (Cursor, Claude Code, GitHub Copilot Chat, etc.) and to Claude.ai sessions. It is loaded when the work is "draft a prompt." The binding rules in `CLAUDE.md` always apply; this file is the dispatcher target for prompt-craft specifics.

**Why this file exists:** Every prompt-craft failure on this project produced a debugging session — silent corruption from heredoc-piped commit messages, false grep positives from loose anchors, prose-described changes hallucinating section headers, agents reporting "done" without actually editing files. Each failure now has a corresponding rule below. Prompt-craft is a discipline; treating it as ad hoc is how you get to "STOP — anchor mismatch" mid-execution.

---

## Table of Contents

1. [The 5 prompt types](#1-the-5-prompt-types)
2. [Universal preamble — what every prompt needs](#2-universal-preamble--what-every-prompt-needs)
3. [Type 1 — Cursor multi-file edit prompt (the deep one)](#3-type-1--cursor-multi-file-edit-prompt-the-deep-one)
4. [Anchor selection for FIND blocks](#4-anchor-selection-for-find-blocks)
5. [Verification grep patterns](#5-verification-grep-patterns)
6. [Anti-patterns to refuse](#6-anti-patterns-to-refuse)
7. [The verification ritual — auditing your own prompt before sending](#7-the-verification-ritual--auditing-your-own-prompt-before-sending)
8. [What to verify in the agent's response](#8-what-to-verify-in-the-agents-response)
9. [Recovery prompts when things go wrong](#9-recovery-prompts-when-things-go-wrong)
10. [Type 2 — Claude.ai session orchestration prompts](#10-type-2--claudeai-session-orchestration-prompts)
11. [Type 3 — Design / specification prompts](#11-type-3--design--specification-prompts)
12. [Type 4 — Verification / audit prompts](#12-type-4--verification--audit-prompts)
13. [Type 5 — Recovery / diagnostic prompts](#13-type-5--recovery--diagnostic-prompts)
14. [Reusable templates](#14-reusable-templates)
15. [When the full protocol doesn't fit](#15-when-the-full-protocol-doesnt-fit)

---

## 1. The 5 prompt types

Different prompts serve different purposes and follow different rules. Identify the type before drafting — applying Type 1's structure to a Type 2 conversation is over-engineering; applying Type 2's looseness to a Type 1 edit invites the bugs § 6 catalogues.

| Type | Purpose | Channel | When to use |
|---|---|---|---|
| 1. Multi-file edit | Make precise changes to ≥2 files in a repo | Cursor, Claude Code | Implementing a planned change |
| 2. Session orchestration | Frame a Claude.ai working session | Claude.ai | Starting a working session |
| 3. Design / specification | Get an agent to draft a plan, design, or spec | Claude.ai or Cursor | Beginning a Major change before implementation |
| 4. Verification / audit | Ask an agent to check work — yours, theirs, or third party's | Claude.ai or Cursor | Reviewing prompts, code, docs, plans |
| 5. Recovery / diagnostic | Restore correct state when an agent reports a mismatch or something went wrong | Cursor or Claude.ai | After STOP, after CI failure, after silent drift |

The rest of this document covers Type 1 in depth (§§ 3-9), then Types 2-5 lightly (§§ 10-13), with reusable templates in § 14, and escape hatches for cases that don't fit Type 1 in § 15.

### 1.1 When to apply the full Type 1 protocol

Apply the full Type 1 protocol (§ 3) when **any** of the following hold:

- The prompt modifies more than one file
- The prompt modifies any file with a `VERSION` header (`.py`, `.sh`, certain `.md`)
- The prompt touches CI/CD configuration (`.gitlab-ci.yml`, `scripts/`, `docker-compose*.yml`)
- The prompt creates or modifies a tracked governance document (`cicd_setup_tracker.md`, manifest, `LESSONS.md`, `CHANGELOG.md`)
- The prompt is intended to land as a single git commit

Skip the full protocol only when **all** of the following hold:

- A single-file edit to a non-tracked file, OR
- Exploratory work that won't be committed, OR
- Read-only investigations

When in doubt, apply the full protocol. Friction is cheap; rework is expensive.

For prompts that don't fit Type 1 cleanly (single-line edits, exploratory work, emergency fixes, repeatedly-failing prompts), see § 15.

---

## 2. Universal preamble — what every prompt needs

Regardless of type, every prompt opens with the same four pieces of context. Skip any of them and the agent improvises in the gap.

### 2.1 Role / context framing (one sentence)

> "You are working on `<project-name>`, a `<one-line description>`."

This is the most under-valued line in any prompt. Without it the agent applies a generic baseline (e.g., assumes web app, assumes JavaScript, assumes mocked tests are fine) that may directly contradict project conventions. One sentence prevents an entire class of misalignment.

### 2.2 Reference to binding rules

> "Binding rules: see `CLAUDE.md` (all 9 standing rules apply)."

Don't restate the rules. Don't summarize them. The agent reads `CLAUDE.md` independently. Restating creates drift between two copies of the same rules — exactly the failure mode CLAUDE.md Rule 8 (manifest completeness, no exclusion lists) prevents. **Reference, don't restate.**

When invoking a specific rule mid-prompt, cite by number: "per CLAUDE.md Rule 4" or "per CLAUDE.md Rule 6". Cite at the point of enforcement, not in the preamble — the citation is most useful where the agent is about to do the relevant action.

### 2.3 Classification

> "Classification: Major / Infrastructure" *(or Minor / Docs, etc.)*

States which workflow strictness applies. Without this, the agent guesses — and guesses too low (Minor) more often than too high (Major), exactly the wrong direction.

### 2.4 Scope discipline statement

> "Scope: implement ONLY what is in this prompt. <List adjacent items that are NOT in scope so the agent doesn't helpfully expand the work.>"

Naming what's *out* of scope is more important than naming what's in. Agents are trained to be helpful and will absorb adjacent improvements without asking. The list of "not in scope" items is the speed brake.

<!--
Example preamble (from a reference project Task 3.5):

You are working on a reference project, a Python-based trading signal platform.

Binding rules: see CLAUDE.md (all 9 standing rules apply).

Classification: Major / Infrastructure.

Scope: implement ONLY what is in this prompt. The known minor inaccuracy in
the current § 11 of docs/ci_cd.md ("logic, integration, and contracts" —
should have said "scheduled" tier) is being deleted entirely by Step 3D;
do NOT attempt to fix it elsewhere.
-->

---

## 3. Type 1 — Cursor multi-file edit prompt (the deep one)

This is the workhorse prompt for implementing a planned change across multiple files. It is also where prompt-craft discipline pays the most — every section below addresses a specific failure mode that occurred at least once on this project.

### 3.1 Structure

```
================================================================
<TASK NAME — short, descriptive, includes phase/task ID if applicable>
================================================================

Universal preamble (§ 2):
 - Role/context
 - Binding rules reference (CLAUDE.md)
 - Classification
 - Scope discipline statement

================================================================
ALLOWLIST — agent MAY modify ONLY these N files:

 1. path/to/file1
 2. path/to/file2
 ...

If at any point `git status --short` shows any other file modified,
STOP and report. Do not absorb mismatches.
================================================================


----------------------------------------------------------------
STEP 1 — Pre-flight: confirm clean working tree
----------------------------------------------------------------

[Specific commands the agent runs to verify state]


----------------------------------------------------------------
STEP 2 — Edit <file 1>: <one-line purpose>
----------------------------------------------------------------

FIND (N lines, exact):

```
<verbatim text currently in the file>
```

REPLACE WITH (N lines, exact):

```
<verbatim text the file should contain after>
```

Verify (optional but recommended for high-stakes edits):

```
grep -nE '<targeted regex>' <file>
```

Expected: <ZERO matches | exactly N matches | etc.>


----------------------------------------------------------------
STEP K — Pre-commit governance verification (MANDATORY VERBATIM OUTPUT)
----------------------------------------------------------------

[Per CLAUDE.md Rule 6: paste full output of each command verbatim.]

[Specific governance commands appropriate to files touched]


----------------------------------------------------------------
STEP K+1 — Commit (single commit, no amend)
----------------------------------------------------------------

[Commit message via -F /tmp/<file> per Rule 4]
[Pre-add and post-add git status verification per Rule 6]
[git commit -F /tmp/<file>]
[Final verification with git log -1 --stat]


----------------------------------------------------------------
STEP K+2 — Files-modified checklist (CLAUDE.md Rule 7)
----------------------------------------------------------------

[Checklist matching ALLOWLIST exactly]
```

### 3.2 ALLOWLIST block — non-negotiable structure

Every multi-file prompt has an ALLOWLIST. The structure:

- **Numbered list** of every file the agent may touch (not just edit — `git status` must not show any other file)
- **Explicit STOP instruction** if any file outside the ALLOWLIST appears in `git status`
- **No** "may also touch related files if needed" — that defeats the purpose
- **The bullet enumeration IS the count.** If a prose sentence ("Total: N files") appears alongside the bullets, treat the bullets as authoritative and ignore the prose if the two disagree. Per `archive/LESSONS.md` L038. Plan authors keep prose counts in sync when editing the bullets — or omit prose counts entirely, since the bullets are self-counting.

The ALLOWLIST is the single most effective bug-prevention mechanism in the entire prompt structure. It catches: agents helpfully editing config files you didn't intend, agents creating new files for "convenience", agents fixing unrelated bugs in passing, agents touching the manifest when you didn't intend a manifest update.

**Agent verification ritual (Rule 6):** before staging, run `git status --short` and compare LINE-BY-LINE against the ALLOWLIST bullets. If the counts agree, proceed. If they disagree (a bullet has no corresponding `git status` row, or a `git status` row has no corresponding bullet), STOP and report. Never trust a prose "N total" sentence over the bullet enumeration — prose drifts during plan revisions, bullets do not.

<!--
Example:
The plan included `**Total files in execution commit: 12.**` as a prose sentence
above a 10-entry bullet ALLOWLIST. The bullets were correct; the prose count had
drifted during plan revisions. Phase 3 execution staged 10 files matching the bullets;
the two-second "did I miss two?" pause was the agent re-counting the bullets to confirm.
-->


### 3.2.1 TODO checklist with checkbox-tick discipline

In addition to the numbered STEP structure (§ 3.1), every Type 1 prompt includes a TODO checklist near the top — placed AFTER the ALLOWLIST and BEFORE STEP 1. The checklist enumerates every sub-edit, verification, commit substep, and final-report element as `[ ]` checkboxes that the agent ticks as work progresses.

```
============================================================
TODO CHECKLIST — agent MUST update as work progresses
============================================================

EDIT 1 — <filename> (N sub-edits)
- [ ] 1a — <description>
- [ ] 1b — <description>

Pre-commit verification
- [ ] V1 — <check>
- [ ] V2 — <check>

Commit
- [ ] C1 — git status BEFORE git add captured
- [ ] C2 — files staged
- [ ] C3 — git status AFTER git add shows exactly N files
- [ ] C4 — heredoc commit message verified via cat
- [ ] C5 — commit succeeded

Final report
- [ ] F1 — git log -1 --stat | cat output pasted
- [ ] F2 — commit SHA reported
- [ ] F3 — Files modified this session checklist confirmed
- [ ] F4 — final summary written
```

Rules:
- The agent ticks each box as work progresses. **No pre-ticking. No batch-ticking.**
- The checklist is also a recovery tool: if the agent crashes or the session is interrupted mid-prompt, the unticked items show what remains.
- Boxes are formatted as `[ ]` (single space inside) — never `[]` or `- [ ]` with extra prefix mismatch.

The TODO checklist and the numbered STEP structure are **complementary, not redundant**: STEPs are the instructions to perform; the TODO is the progress tracker that proves performance.

### 3.3 Pre-flight HEAD/branch check

Step 1 always confirms baseline state before any edit. Catches the situation where the prompt was drafted against a stale view of the repo (e.g., the user pulled new commits between drafting the prompt and pasting it).

```bash
git status --short
git rev-parse --short HEAD
git rev-parse --abbrev-ref HEAD
```

State the **expected** values. Agent must STOP if any condition fails.

<!--
Example pre-flight assertion:

Required state:
 - `git status --short` returns ZERO lines.
 - `git rev-parse --short HEAD` returns `f2f3d3f` (Task 3.2 close-out tip).
 - `git rev-parse --abbrev-ref HEAD` returns `master`.

If any condition fails, STOP.
-->

### 3.4 FIND/REPLACE blocks — verbatim, not described

This is the core technique that prevents the prose-composition failure mode. Per CLAUDE.md Rule 7:

- ❌ Wrong: "Update the validate job description in section 3 to remove the legacy job reference."
- ✅ Right: Provide the exact 5 lines to FIND and the exact 1 line to REPLACE WITH.

Why: agents composing text from descriptions introduce stylistic drift, sometimes invent section headers that don't exist, occasionally hallucinate plausible-but-wrong content. Verbatim FIND/REPLACE eliminates all three failure modes — the agent is doing string substitution, not authorship.

**Each FIND block declares its line count** ("FIND (5 lines, exact)") so agent and user can both spot anchor mismatches by simple counting before the substitution runs.

**Every FIND block must be unique in the file.** See § 4 for anchor selection.

### 3.5 Verification grep after each substantive edit

For high-stakes edits (deletion, insertion, structural change), include a `grep` after the FIND/REPLACE that proves the change applied correctly:

```bash
grep -nE '<targeted regex matching the deleted/inserted pattern>' <file>
```

State the expected result: "Expected: ZERO matches" or "Expected: exactly 2 matches."

The grep pattern must be **targeted** (won't match unrelated content). See § 5 for grep patterns and false-positive avoidance.

### 3.6 Pre-commit governance verification

Mandatory step before every commit. Per CLAUDE.md Rule 6:

```bash
python scripts/check_doc_coverage.py
python scripts/check_test_coverage_drift.py --ci
git status --short
git diff --stat
```

For `.yml` CI changes, also include the YAML parse check:
```bash
python -c "import yaml; yaml.safe_load(open('.gitlab-ci.yml')); print('YAML valid')"
```

**The agent must paste full stdout/stderr verbatim.** Self-reported "exit 0" or "passed" without the actual output is unacceptable per Rule 6.

State explicit decision rules: "If `check_doc_coverage.py` exits non-zero, STOP and paste full output."

### 3.7 Commit step

Per CLAUDE.md Rule 4: write commit message to `/tmp/<file>.txt` with single-quoted heredoc, then `git commit -F`. Per Rule 6: `git status --short` BEFORE and AFTER `git add`.

```bash
cat > /tmp/commit_msg_<task>.txt <<'EOF'
<title>

<body>

<impact statement>
EOF

cat /tmp/commit_msg_<task>.txt # Verify message file content (catches heredoc surprises)

git status --short # Verify file set matches ALLOWLIST
git add -A
git status --short # Verify staged set matches

git commit -F /tmp/commit_msg_<task>.txt

git log -1 --stat # Final verification
git log -1 --name-only --format=
```

End with: **"DO NOT PUSH. <user> pushes from <their machine>."**

The no-push rule keeps the human as the final gate. The user reviews the agent's reported output, then pushes only after confirming everything is correct.

#### 3.7.1 Commit subject line conventions

- **Imperative mood** — "Add X" not "Added X" or "Adds X"
- **≤72 chars when possible**, but legibility matters more than length
- For multi-purpose commits, prefix with category: `Phase 3 close:`, `F-1 fix:`, `vd-1:`, `Task 3.4:`, etc.
- Avoid trailing punctuation; subject is a title, not a sentence

#### 3.7.2 Commit body structure

```
<subject line>

<one-paragraph summary of what changed and why>

<file>:
- <change 1>
- <change 2>

<file>:
- <change 1>

<additional context: cascading impacts, design decisions, related commits>

<explicit scope statements: "No trading logic impact. No backtest impact. No code (.py/.sh/.yml) changes." or whatever applies>
```

Notes:
- The per-file bullet list is the diff narrative — what materially changed in each file. Not exhaustive; just the meaningful changes.
- Explicit scope statements near the end are how the reviewer/operator confirms the blast radius without reading the diff. Always include even when negative ("No trading logic impact").
- Cross-references to related commits or deferred items (D-numbers) help future archaeology.

### 3.8 Files-modified checklist

Final block of every Type 1 prompt:

```
The output of `git log -1 --name-only` must list EXACTLY these N files:

 [ ] path/to/file1
 [ ] path/to/file2
 ...

In your final response, transcribe this checklist with each box marked
[x] confirmed against actual output, OR mark missing/extra files with
[!] and report.

If ANY file outside this list appears, OR any of the above is missing,
REPORT and STOP.
```

This checklist is self-auditing. The agent can't fake it — they have to look at the real `git log` output to fill in the boxes. Discrepancies are loud.

### 3.9 Final summary requirement

Every Type 1 prompt instructs the agent to end its response with a **structured final summary** covering exactly these 7 points, in this order:

1. **What was done** — plain-language list of file changes.
2. **What was verified** — which checks passed; raw output (not self-reported "exit 0") for governance scripts and key verifications.
3. **Anything unexpected** — FIND match counts, gather-command results, any surprise discovered during execution.
4. **Anything skipped or deviated** — explicit "No deviations" if applicable; otherwise enumerate what was changed and why.
5. **Files modified this session** — the checklist (§ 3.8) confirmed.
6. **Commit SHA + `git log -1 --stat | cat`** — the full output, pasted verbatim.
7. **DO NOT PUSH reminder** — explicit confirmation that `git push` was not run.

The structured format makes review fast: the operator scans 7 specific points in a known order rather than parsing free-form prose. Skipping any element is a protocol violation.

### 3.10 Delivery in chat — single 4-backtick fence

When delivering a Type 1 prompt to the user (so they can paste it into Cursor or another agent), wrap the **entire** prompt in **ONE outer 4-backtick code fence** (since inner blocks use 3 backticks).

```
````
<entire prompt content here, including ```bash blocks, FIND/REPLACE blocks,
TODO checklist, ALLOWLIST, etc. — all between the outer 4-backticks>
````
```

Rules:
- **No section dividers (`---`) outside the fence.** No top-level markdown headers outside the fence either. The whole prompt is one copy-paste-ready block.
- **No interleaved commentary** between the fence opening and closing. The user copies the entire block in one action and pastes into the agent without trimming.
- **Commentary goes AFTER the closing fence** — an audit summary table, expected execution time, or preconditions. These are notes from drafter to operator, not part of what gets pasted.

This rule prevents two failure modes: (a) accidentally splitting the prompt across multiple paste actions (some sections lost), and (b) bracketing 3-backtick code blocks with 3-backtick fence (the closing inner fence terminates the outer prematurely).

### 3.11 Codex handoff variant (multi-agent projects only)

When the multi-file edit is being handed off to a secondary AI agent (Codex, Devin, or similar) under the Codex handoff protocol from `CLAUDE.md` § 14, the Type 1 prompt's shape changes — see `archive/LESSONS.md` L020.

**Key differences from the standard Type 1 prompt:**

| Standard Type 1 (Claude as agent) | Codex handoff variant |
|---|---|
| Agent runs `git add` + `git commit -F` end-to-end (per L026) | Codex does NOT commit. Claude commits later on Codex's behalf. |
| Final block: commit step + DO NOT PUSH | Final block: structured 7-element session summary (no commit, no push) |
| Agent updates manifest / CHANGELOG / folder_structure | Codex does NOT touch central bookkeeping. Claude does it. |
| Agent bumps in-file VERSION + CHANGE LOG | Codex DOES bump in-file VERSION + CHANGE LOG on source files it touches |

**Codex prompt structure modifications:**

1. **ALLOWLIST narrower than for Claude:** explicitly excludes `CHANGELOG.md`, `docs/documents_manifest.md`, `docs/folder_structure.md`, `CLAUDE.md`, `scripts/validation_ownership.toml`, any tracker Codex doesn't own. Any of those appearing in `git status` is a STOP condition.

2. **Final block replaces "commit + DO NOT PUSH" with the 7-element summary:**

 ```
 ============================================================
 SESSION SUMMARY (mandatory; deliver to operator at end of session)
 ============================================================

 1. Files modified — full list, one-line description each:
 - <path>: <description>

 2. Files created — full list, one-line purpose each:
 - <path>: <purpose>

 3. Why — 1-2 sentence rationale.

 4. Verification ran — raw stdout of any tests / governance scripts
 executed locally (paste verbatim, not "exit 0"):
 <verbatim output>

 5. Tracker reference — which tracker this work belongs to:
 <tracker file + section> OR "no tracker — operator-driven one-off"

 6. Anything unexpected or deviated from the plan:
 <text> OR "none"

 7. Files left out / deferred — anything intentionally not touched + reason:
 <text> OR "none"
 ============================================================
 ```

3. **No commit step. No `git add`. No `git commit -F`. No DO NOT PUSH reminder** (those are Claude's responsibility after receiving the summary).

4. **Code review still applies — Codex performs its own self-review before declaring done.** The review pass per L027 is part of every commit-worthy work, regardless of which agent commits.

**Operator workflow after Codex returns the summary:**

1. Operator pastes the summary to Claude verbatim
2. Claude verifies via filesystem (`git status`, `git diff`)
3. Claude checks the work against the relevant tracker
4. Claude runs governance scripts locally before staging
5. Claude code-reviews (per L027 / `CLAUDE.md` § 8.5)
6. Claude updates central bookkeeping (`CHANGELOG.md`, manifest, `folder_structure.md`, `validation_ownership.toml`)
7. Claude commits (per `CLAUDE.md` § 11)
8. Operator authorizes push

If Codex deviated from the prompt's ALLOWLIST or scope, the recovery prompt to Codex follows the **PRIOR DEVIATION WARNING** pattern in § 9.5.

### 3.12 Relayed prompts and step guides (for another person or their agent)

When the operator relays a prompt or a step-by-step guide to someone else — a project owner, or
the agent in their project — through a chat app:

- **Send it as a file** (a `.txt` attachment), never as pasted text: chat apps render paired `*`
  and `_` as formatting and silently drop them — a pattern once lost its `*` this way, and only the
  prompt's own gate caught it.
- **One block per step, and every block prints its own verdict** — `>>> OK`, `>>> NOT YET` or
  `>>> STOP: <reason>`, computed by the block itself, not judged by the reader.
- **Every block appends to one results file** that the person sends back — the curator reads the
  evidence, not a summary of it.
- **A step that would do harm if run too early checks its own precondition first**, so a mistimed
  paste is harmless (L084).
- **Bench-test the guide** against the real tool in a mock of the recipient's layout, including
  negative controls (L082), and check every concrete claim — file names, counts, rows — against
  their live files before sending (L088).
- **Plain words** — for each step: what it does, what you should see, what to do if you don't.

---

## 4. Anchor selection for FIND blocks

Every FIND block needs an anchor that is **unique in the file**. Bad anchors caused multiple bugs on this project. The discipline:

### 4.1 Prefer 3+ line anchors

Single-line anchors collide. Three-line anchors almost never do. Rule of thumb: include enough surrounding context that the anchor would be unique even if the file's content shifted.

- ❌ Risky: `validate:` (matches the YAML key but also any other `validate:` in any file)
- ✅ Safe: 3 lines combining the preceding comment + the `validate:` line + the next blank line

### 4.2 Anchor against structural elements when content is shifty

For inserting between sections of a markdown doc:
- Anchor against last line of preceding section + blank line + first line of next section

For inserting at end of file:
- Anchor against last meaningful content + structural element (closing horizontal rule, final list bullet, etc.)

For inserting in a table:
- Anchor against the line above the insertion point + the line below — the `|...|` table syntax is structural

### 4.3 Verify uniqueness before drafting

Before committing to an anchor, run:

```bash
grep -c '<anchor first line>' <file>
```

If the count is >1, the anchor is not unique. Either extend it (more lines of context) or pick a different one.

### 4.4 Common anchor failures

These all happened on this project. Each cost at least a "STOP" intervention:

**Failure 1 — Substring match:** Anchor `validate` matched the past-tense verb `validated` elsewhere in the file. **Fix:** anchor against `\| test \| `validate` \|` (the table-cell context) or `^### `validate`` (the section-header context).

**Failure 2 — Stale anchor:** Prompt drafted against an older view of the file. The literal text the prompt expected to find no longer existed because earlier commits had rotated the content. **Fix:** read the file fresh from disk before drafting the FIND block. Don't draft against memory of what the file "probably" looks like.

**Failure 3 — Whitespace mismatch:** Anchor included trailing spaces that the file didn't have, or didn't include trailing spaces the file did have. The substitution silently failed because trailing whitespace is invisible in markdown rendering. **Fix:** copy the anchor text directly from the file; never retype it.

**Failure 4 — Line count mismatch in declared block:** Prompt said "FIND (4 lines, exact)" but the actual block was 5 lines or 3 lines. The agent counts and detects the discrepancy, but only if the count is declared. **Fix:** always declare line count; always count before declaring.

<!--
Real example (Task 3.5 prompt review):

Original anchor:
 ```
 - **Date**: 2026-04-24
 - **Change**: Task 3.0b-ii — manifest completeness sweep complete...
 ```

Actual file state (different commit had rotated the block):
 ```
 - **Date**: 2026-04-24
 - **Change**: Phase 3 Task 3.2 close-out — docs/cicd_setup_tracker.md...
 ```

Cursor correctly STOPPED with "literal block mismatch" because the anchor
didn't match. Resolution: read actual current file state, redraft the
prompt with the correct anchor, re-issue.

Lesson: anchor against current filesystem state, not against project
knowledge or memory of "what the file probably looks like."
-->

### 4.5 Edit pattern templates

These are recurring shapes that FIND/REPLACE blocks take. Recognize the pattern your edit fits and use the template.

#### 4.5.1 Single-line value change

For version bumps or value substitutions:

```
EDIT — <description>

FIND (exact 1 line):
<old line verbatim>

REPLACE (exact 1 line):
<new line verbatim>
```

Use only when the line is unique in the file. If not unique, switch to a multi-line anchor pattern.

#### 4.5.2 Insert content between two existing anchors

For inserting a new entry, paragraph, or section between existing content:

```
EDIT — <description>

FIND (exact 2 lines — top anchor + bottom anchor):
<top anchor line>
<bottom anchor line>

REPLACE (top anchor preserved + new content + bottom anchor preserved):
<top anchor line>
<new content lines>
<bottom anchor line>
```

The top and bottom anchors are preserved verbatim; the new content goes between.

#### 4.5.3 Append after an anchor

For adding a new entry at the end of a list, table, or section:

```
EDIT — <description>

FIND (exact 1 line — anchor, typically the last existing entry):
<anchor line>

REPLACE (anchor preserved + new content appended):
<anchor line>
<new content lines>
```

#### 4.5.4 Prepend before an anchor (newest-first convention)

For LESSONS.md, CHANGELOG.md, incident blocks (newest entries on top):

```
EDIT — <description>

FIND (exact N lines — existing top entry):
<existing top entry, several lines>

REPLACE (new entry inserted ABOVE existing entry, existing preserved verbatim):
<new entry lines>
<existing top entry, preserved verbatim>
```

#### 4.5.5 Multi-section update with shared anchor area

When several edits share the same anchor area (e.g., updating a row + its legend entry in the same table), do them as **separate FIND/REPLACE blocks** even though they're in the same file. Don't try to merge them into one mega-edit; each FIND should be the smallest unique-matching text.

#### 4.5.6 Just-in-time gather pattern

When the exact text to FIND depends on session state (e.g., "rotate the Last Updated block — show me the current state first"), specify a gather command in the prompt:

```
EDIT — <description>

GATHER COMMAND (agent: run before drafting this edit):
```bash
<command that prints the current state>
```

Then draft the FIND/REPLACE based on the gather output.
```

This is appropriate when the content is volatile across commits (e.g., manifest Last Updated block rotates every commit). The drafter writes the gather command and the rotation logic; the agent fills in the literal FIND/REPLACE based on the gather output.

> **Caution:** § 6.5 (anti-pattern: prose-described changes) still applies. The gather pattern is allowed because the agent applies a *deterministic mechanical transformation* to the gathered state — not because the prose description carries semantic content the agent must compose from. If the rotation logic is not deterministic and mechanical, do not use this pattern; compute the FIND/REPLACE yourself.

---

## 5. Verification grep patterns

Verification greps after FIND/REPLACE blocks confirm the change applied correctly. Bad greps produce false alarms (stopping the agent when nothing's wrong) or false silence (passing when something IS wrong).

### 5.1 Targeted regex over loose word match

- ❌ Wrong: `grep 'validate' <file>` — matches `validated`, `validation`, `validator`, etc.
- ✅ Right: `grep -nE '\| test \| `validate` \||^### `validate`' <file>` — matches only the patterns you actually deleted

The principle: write the grep so it can ONLY match the thing you're checking for. If the grep can match anything else, false positives are inevitable.

### 5.2 Always state expected count

After every grep, state the expected result:

- "Expected: ZERO matches"
- "Expected: exactly 1 match"
- "Expected: exactly N matches (the inserted rows)"

Without an explicit expectation, "1 match" might mean success or failure — the agent has to guess. Explicit expectations make the assertion crisp.

### 5.3 Use line numbers when investigating, not when asserting

`grep -n '<pattern>' <file>` gives line numbers — useful for debugging, but the line numbers shift after edits. Don't anchor expectations against specific line numbers; anchor against pattern presence/absence and count.

### 5.4 Counter-example: today's near-miss

A prompt's verification step said:

```bash
grep -n 'validate' docs/ci_cd.md # Expected: ZERO matches
```

After the deletions, the grep would have matched the past-tense `validated` (line 287, unrelated to the deleted job) and the agent would have falsely STOPPED. Caught in pre-send audit. **Fix applied:**

```bash
grep -nE '\| test \| `validate` \||^### `validate`' docs/ci_cd.md # Expected: ZERO matches
```

The regex now matches only the table-cell pattern and the section-header pattern that were deleted — won't match `validated` or any other unrelated word.

### 5.5 Common verification command snippets

Reusable command shapes for the most common verification needs.

**Confirm a string is present:**
```bash
grep -n '<expected string>' <file>
# Expected: at least 1 match. If 0 matches, the edit didn't apply.
```

**Confirm a string is absent:**
```bash
grep -n '<old string>' <file>
# Expected: 0 matches (grep exits 1). If matches, old content lingers.
```

**Confirm count of occurrences:**
```bash
grep -c '<pattern>' <file>
# Expected: <specific number>. If different, the edit applied incorrectly.
```

### 5.6 Diff against another commit

When verifying a revert or comparing post-edit state to a known-good baseline:

```bash
git diff <commit-sha> -- <file>
# Expected: zero output (file matches that commit). Useful for verifying reverts.
```

For comparing an edit against the immediate predecessor:

```bash
git diff HEAD~1 -- <file>
# Shows what THIS commit changed in <file>. Useful in agent's final report.
```

### 5.7 Bash and YAML syntax checks

For commits touching `.sh` files:

```bash
bash -n <script.sh>
# Exit 0 = syntactically valid. Doesn't run the script. Catches typos that bash refuses to parse.
```

For commits touching `.yml` or `.yaml` files:

```bash
.venv/bin/python -c "import yaml; yaml.safe_load(open('<file.yml>')); print('YAML valid')"
# Exit 0 = parseable. Does NOT validate GitLab-CI schema (needs:, stage:, rules:, dependencies:) — those need a real pipeline run per CLAUDE.md Rule 5.
```

Both checks are mandatory pre-commit verifications when their respective file types are touched.

---

## 6. Anti-patterns to refuse

Each entry below caused a real bug on this project. Refuse to write a prompt that contains any of these.

### 6.1 Self-referential SHA backfill via `--amend`

❌ Pattern:
```bash
git commit ... # Commit
NEW_SHA=$(git log -1 --format=%h)
sed -i "s/<COMMIT_SHA>/$NEW_SHA/g" tracker.md
git add tracker.md
git commit --amend --no-edit # Amend changes the SHA
```

The amend changes the commit SHA, so the tracker's row now points at a SHA that doesn't exist in `git log`. Orphan-SHA wart. **Fix:** drop the SHA placeholder entirely; tracker entries reference the commit by message via `git log --grep`. CHANGELOG.md is the canonical record of what landed when.

### 6.2 Heredoc piped to `git commit`

❌ Pattern:
```bash
git commit -m "$(cat <<EOF
Multi-paragraph message with `backticks` and — em-dashes
EOF
)"
```

Silent character corruption. The commit appears clean but Unicode and special characters are mangled. Discovered weeks later when `git log --grep '`backticks`'` returns nothing. **Fix:** write to `/tmp/<file>.txt` with single-quoted heredoc, then `git commit -F /tmp/<file>.txt`. Per CLAUDE.md Rule 4.

### 6.3 `git commit -m "..."` with backticks or em-dashes

❌ Pattern:
```bash
git commit -m "Fix: \`validate\` job removed"
```

Shell escaping is fragile. Single quotes inside double quotes, backticks, dollar signs all need escaping; missing one creates silent corruption. **Fix:** any commit message beyond a single short line uses `-F /tmp/<file>.txt`. Per CLAUDE.md Rule 4.

### 6.4 Force-push of a pushed commit

❌ Pattern:
```bash
git commit --amend
git push --force # ❌ NEVER for pushed commits
```

Erases history. The broken state and the lesson both disappear. **Fix:** create a new commit with letter suffix (e.g., `Task 2.5b`). Per CLAUDE.md Rule 3. **Local-only commits (not yet pushed) may be amended freely.**

### 6.5 Prose-described changes

❌ Pattern: "Update the section to reflect the new behavior" / "Modify the relevant docstring" / "Adjust the table accordingly"

Agents compose from descriptions and produce stylistic drift, hallucinate section headers that don't exist, or generate plausible-but-wrong content. **Fix:** verbatim FIND/REPLACE blocks. Per CLAUDE.md Rule 7.

### 6.6 Hedging language

❌ Patterns: "optionally", "if applicable", "where relevant", "as needed", "if you think it's a good idea"

Agents interpret hedges inconsistently. Some treat them as "do this", others as "skip this", others as "ask the user". **Fix:** explicit decision rules: "if X, do Y; otherwise skip and state so in your final output."

### 6.7 Single-line anchors in FIND blocks

❌ Pattern:
```
FIND: `validate:`
REPLACE WITH: (deleted)
```

Single-line anchors collide. The agent might apply the substitution to the wrong location. **Fix:** 3+ line anchors with surrounding context. Per § 4.1.

### 6.8 Loose verification greps

❌ Pattern: `grep 'validate' <file>` to verify deletion of a job named `validate`

Matches unrelated content (`validated`, `validation`, `validator`). False positives stop the agent on non-issues. **Fix:** targeted regex matching only the deleted pattern. Per § 5.1.

### 6.9 Missing pre-add `git status` check

❌ Pattern:
```bash
git add -A
git commit ...
```

Skips the verification that the staged set matches the ALLOWLIST. **Fix:** `git status --short` before AND after `git add`. Per CLAUDE.md Rule 6.

### 6.10 Implicit governance ("just run the checks")

❌ Pattern: "Run the governance scripts and proceed if they pass."

Agent self-reports "passed" without showing output. Per CLAUDE.md Rule 6, self-reported "exit 0" without verbatim output is unacceptable. **Fix:** "Paste the FULL stdout/stderr of each command verbatim. Self-reported 'passed' without output is unacceptable per CLAUDE.md Rule 6."

### 6.11 Scope expansion mid-execution

❌ Pattern: Once a Cursor prompt is in flight (drafted, presented to user for review, or being executed by the agent), expanding scope based on user follow-up questions or design ideas surfaced mid-execution.

**Example:** User asks during execution: "While we're here, should we also add X?" Tempting answer: "Yes, let me update the prompt to include that too." This is the trap.

**Why it's wrong:**
- Reversing direction mid-commit creates documentation churn — a freshly-filed deferred item or tracker entry would need amending immediately
- Breaks the focused-commit discipline that makes commit messages and tracker updates meaningful in retrospect
- Increases agent cognitive load and risk of mistakes (same fatigue dynamics as § 9 pause discipline)
- Creates fragmented commits that are harder to review, blame, or revert

**Right response:** "Good question — deferred to [Phase X / specific commit / a separate session]. Let's let this commit land first."

**Wrong response:** "Yes, let's also handle that in this commit." OR "Let me update the prompt to include that too."

**Edge case:** If the user's mid-execution question reveals that the IN-PROGRESS work is wrong (e.g., "wait, that approach won't work because..."), STOP and discuss. That's not scope expansion — that's bug discovery. Different protocol.

**Source:** the standards source Phase 3 2026-04-28 session — user asked "should we put validators in smoke?" during the X11/D12 commit's execution. Correctly deferred to Phase 4 design rather than reversing course. The deferred D12 row would have needed immediate amending if reversed.

### 6.12 Popup questions when inline options work (Claude Code-specific)

❌ Pattern: using the harness's question-popup UI (`AskUserQuestion` or equivalent) for routine clarification when an inline option list in the chat would work just as well.

Why bad: popup UIs break the conversational flow. The operator has to click through a modal instead of reading and replying inline. For session protocols that run "one task per message" (as set in the project's Claude.ai Project Instructions), popups add a context-switch that linear chat avoids.

This is specific to Claude Code (and other harnesses that ship a question-UI). For pure Claude.ai conversations, this doesn't apply.

✅ Fix: render options inline as a labelled list ("Option (a) ... Option (b) ... Option (c) ... Pick one.") in the chat. Operator replies inline ("a"). The conversation stays linear and auditable. Popups are appropriate for high-stakes branching choices that explicitly benefit from a structured form (e.g., the harness's session-end pickers); routine clarifications use inline.

---

## 7. The verification ritual — auditing your own prompt before sending

Before sending a Type 1 prompt to the agent, walk this checklist. Today's session demonstrated that even a careful first draft has 2-6 bugs that this audit catches.

### 7.1 Walk every FIND block

For each FIND block in the prompt:
- Does the literal text match the current file state? (Check: `grep -F '<first line of FIND>' <file>` — should return exactly 1 hit)
- Is the declared line count correct? (Count lines manually)
- Is the anchor unique in the file? (Check: `grep -c '<distinguishing line>' <file>` — should return 1)
- Is whitespace exact? (Copy from file, never retype)

### 7.2 Walk every REPLACE block

For each REPLACE block:
- Does the result produce the intended outcome? (Mentally apply the substitution; does the result read correctly?)
- Are line counts consistent? (If FIND was 5 lines and REPLACE is 1 line, the file shrinks by 4 lines — intended?)
- Are placeholders that need backfill (e.g., `<COMMIT_SHA>`) clearly flagged?

### 7.3 Walk every verification grep

For each grep:
- Could the regex match anything other than the intended pattern? (False positive risk)
- Is the expected count stated explicitly?
- Is the assertion strong enough? (Counter-example: "Previous change count = 1" is true both before AND after rotation — useless assertion)

### 7.4 Walk every governance step

- Is the YAML parse included if `.yml` files are touched?
- Are `check_doc_coverage.py` and `check_test_coverage_drift.py --ci` both present?
- Is "PASTE VERBATIM OUTPUT" stated explicitly per CLAUDE.md Rule 6?
- Are STOP conditions explicit for each governance script?

### 7.5 Walk the commit step

- Is `git commit -F /tmp/<file>` used (not `-m` with escapes)?
- Is the heredoc single-quoted (`<<'EOF'`)?
- Is `git status --short` called BOTH before AND after `git add` per Rule 6?
- Is "DO NOT PUSH" stated at the end?

### 7.6 Walk the ALLOWLIST + checklist

- Does the ALLOWLIST list every file the prompt edits?
- Does the files-modified checklist at the end match the ALLOWLIST exactly?
- Are the checklist boxes formatted as `[ ]` (not `[]` or `- [ ]`)?

### 7.7 Final readability pass

- Are step numbers consecutive? (No skipped numbers)
- Are STEP K and STEP K+1 etc. resolved to actual numbers in the final draft?
- Is every "STOP" condition followed by what to do (report, ask user, etc.)?

This ritual takes ~3 minutes per prompt. Catches bugs that would otherwise cost ~30 minutes of mid-execution interruption. Always worth it.

### 7.8 Pre-draft duplicate check

Before adding new content (rules, sections, tracker rows, manifest entries, CHANGELOG entries, lesson entries), grep the target file for duplicates of what you're about to add. If a duplicate already exists, **do not re-add** — note the existing location in the prompt's pre-draft audit findings and skip the addition.

```bash
grep -nE '<distinguishing phrase from the new content>' <target file>
# Expected: 0 matches. If a match exists, the content is already present — skip.
```

**Why this matters:** prompts drafted from session memory or a working document occasionally propose adding a rule that's already in the target file (added in a prior commit not visible to the drafter). The duplicate check is the audit step that catches this before the prompt is sent. Per `CLAUDE.md` Rule "Multi-file Cursor prompt construction" point 7 (auto self-audit before sending), duplicate findings must be surfaced in the prompt's pre-draft audit-findings section as: "checked X — already in <file> at line N — NOT being re-added."

---

## 8. What to verify in the agent's response

After the agent runs the prompt and reports back, walk this checklist before pushing.

### 8.1 Governance output present and verbatim

Per CLAUDE.md Rule 6: did the agent paste actual stdout/stderr from the governance scripts, or did it summarize ("all checks passed")? Summary is unacceptable. If absent, do not push — ask the agent to re-run and paste verbatim.

### 8.2 STOP discipline

Did the agent STOP appropriately on any mismatch (anchor failure, governance failure, ALLOWLIST violation)? An agent that "fixes" mismatches by improvising is dangerous; an agent that STOPS and reports is doing the right thing — even though it means more turns.

### 8.3 Files-modified checklist matches ALLOWLIST

Compare the agent's reported `git log -1 --name-only` output against the ALLOWLIST. They must match exactly. Extra files → STOP, do not push, investigate. Missing files → STOP, the edit didn't apply.

### 8.4 Commit message rendered correctly

The agent should `cat /tmp/<file>.txt` after writing it. Verify backticks, em-dashes, and special characters survived the heredoc. If the rendered text shows `\backslash-escaped\` versions or replaced characters, the commit message file is corrupt — do not commit.

### 8.5 Final verification — does the change actually do what was intended?

The agent ran the substitutions and the governance passes — but does the result actually achieve the prompt's goal? Quick sanity check: read the diff of the changed files (the agent's `git diff --stat` shows scope; `git diff HEAD~` would show content if not yet pushed). Spot-check 1-2 substitutions to confirm intent.

### 8.6 Push only after all checks pass

Per the prompt's "DO NOT PUSH" instruction: the user is the final gate. After verifying §§ 8.1-8.5, push from your local machine. Watch the pipeline. Confirm green.

---

## 9. Recovery prompts when things go wrong

When an agent reports STOP — anchor mismatch, governance failure, scope violation, etc. — the response is NOT to improvise. Per CLAUDE.md Rule 6 and the "Ask when ambiguous" principle.

### 9.1 The two-interpretations protocol

When an agent reports a mismatch and asks for direction:

1. **Apply the prompt's documented logic against actual current state.** The prose semantics are correct; only the literal block was stale.
2. **Update the prompt's literal block to match current state and re-issue.** Treat the original prompt as drafted against an outdated view.

Pick one explicitly. Do not let the agent guess.

<!--
Real example (Task 3.5 STEP 5B mismatch):

Cursor reported the manifest's Last Updated block didn't match the FIND
anchor. Two valid interpretations:

(1) Apply rotation logic to actual current state: new Date=2026-04-25,
 new Change=(Task 3.5 entry), new Previous change=(current "Phase 3
 Task 3.2 close-out" content), drop the prior Previous change.

(2) Update the prompt's literal block to match current state and
 re-issue.

User picked (1). Re-issued only STEP 5B with corrected literal block.
Resolution time: one turn. If agent had improvised: would have produced
silently-wrong content with no audit trail.
-->

### 9.2 Re-issue corrected prompts as complete blocks

When you have to re-issue a prompt or a single step:
- Don't send inline patches or "change the FIND block to: ..." instructions
- Send the complete corrected prompt (or the complete corrected step) in a single copy-paste-ready block
- Explicitly mark which steps are unchanged ("Resume from STEP 5A as written, then use this CORRECTED STEP 5B in place of the original")

This is the "give me prompt always" rule from this project's session protocol.

### 9.3 Surface the bug clearly before fixing

When you find a bug in your own prompt during the verification ritual (§ 7), surface it explicitly to the user before redrafting:

- State which step has the bug
- Explain what would happen if the prompt ran as-is
- Propose the fix
- Ask for confirmation if the fix involves a design choice (e.g., "drop SHA backfill entirely" vs "use placeholder pattern")

This prevents two failure modes: silently fixing in a redraft (user can't review), and arguing about whether the bug is real (everyone wastes time).

### 9.4 Recovery from CI failure

When a pushed commit fails CI:

1. Read the actual CI failure (don't guess from the job name)
2. Determine: is this a real defect, or a known-acceptable failure?
3. If real defect: fix-forward per CLAUDE.md Rule 3 — new commit with letter suffix
4. Draft the fix-forward prompt as a fresh Type 1 prompt with its own ALLOWLIST and governance steps
5. Reference the original failed commit in the new commit message

Never `git push --force` an amended version. The broken commit stays in history; the fix sits next to it.

### 9.5 Retry prompts need PRIOR DEVIATION WARNING

When re-prompting an agent that just deviated from a prompt's scope (touched a file outside ALLOWLIST, modified a tracker it doesn't own, skipped a verification step, etc.), the retry prompt must include an explicit PRIOR DEVIATION WARNING at the top. Per `archive/LESSONS.md` L033.

**Anti-pattern this prevents:** sending the original prompt verbatim a second time and expecting the agent to read it more carefully this turn. Verbatim re-prompts without the deviation callout fail more often than not — agents drift toward the same training-data priors the original prompt was supposed to suppress.

**Retry prompt structure:**

```
============================================================
PRIOR DEVIATION WARNING
============================================================

In the prior attempt, <specific file or scope> was modified outside ALLOWLIST.
This is a protocol violation — see `CLAUDE.md` § <relevant rule>.

NON-NEGOTIABLE outcomes for this retry:
- <outcome 1 — usually "do not touch <file>">
- <outcome 2 — usually "verify ALLOWLIST against git status before each step">
- <outcome 3 — usually a specific check the prior attempt skipped>

If any of these is unclear, STOP and ask before proceeding.
============================================================

<original prompt content here — including the ALLOWLIST, TODO checklist, STEPs, etc.>
```

**Placement:** the PRIOR DEVIATION WARNING goes ABOVE the original prompt's ALLOWLIST. The agent processes it first, then encounters the ALLOWLIST with the warning fresh in context.

**TODO checklist addition:** add a new explicit checkbox `[ ] PD1 — prior deviation NOT repeated` to the TODO checklist. The agent ticks it after the corresponding verification step.

**Operator's role:** when reading the agent's response, verify the deviation was NOT repeated. If it was, the agent is structurally not following constraints — escalate to manual intervention per § 15.4 ("escalate after 3+ failed iterations").

**Worked example (from Phase 6 Codex collaboration, a reference project):**

Codex modified `CHANGELOG.md` despite the ALLOWLIST excluding it (per Codex handoff protocol). Operator's retry prompt to Codex included this warning at top:

```
PRIOR DEVIATION WARNING

In the prior attempt, you modified CHANGELOG.md. CHANGELOG.md is Claude's
responsibility per Codex handoff protocol (CLAUDE.md § 14).

NON-NEGOTIABLE outcomes:
- Do NOT touch CHANGELOG.md (it stays at its previous content)
- Do NOT touch docs/_gpt_context_manifest.md
- Do NOT touch docs/folder_structure.md
- Run `git status --short` BEFORE staging any file
- End with the structured 7-element summary (no commit, no push)
```

Codex completed the retry without deviation. The warning + non-negotiable list was the key change.

---

## 10. Type 2 — Claude.ai session orchestration prompts

These frame a Claude.ai working session. They go in the first message of a conversation (or in the Project Instructions field for repeated session shapes).

### 10.1 Structure

```
Project context (one paragraph): what we're working on and current state.

Today's priorities (in order):
1. <Task 1>
2. <Task 2>
3. <Task 3>

Current state:
- <Branch tip SHA>
- <What's done>
- <What's next>
- <Any context the agent needs that isn't in project knowledge>

Session protocol:
- Apply session interaction protocol from message 1: brief overview,
 then ONE command/task/question per message, wait for output. Do not batch.

Time budget: <expected duration>

Start by giving me <a brief overview of Task 1>, then we begin.
```

### 10.2 Key elements

- **Priorities in order** — agent works through them sequentially, not in parallel
- **Current state** — explicit branch SHA, what's done, what's next; prevents agent from re-reading project knowledge or asking
- **Session protocol** — one task per message; this prevents the "lost in batch" failure mode
- **Time budget** — agent paces appropriately; flags scope creep
- **Explicit start instruction** — tells the agent what to do first, avoids ambiguity

### 10.3 Anti-patterns

- ❌ Open-ended ("let's see where we get to today")
- ❌ Multiple parallel goals without priority order
- ❌ No current state context (forces agent to re-derive from project knowledge)
- ❌ No session protocol (agent batches multiple things into single responses)

---

## 11. Type 3 — Design / specification prompts

For getting an agent to draft a plan, design, or spec before implementation. Used at the start of any Major change.

### 11.1 Structure

```
Context: <one paragraph on what we're trying to accomplish>

Classification: Major / <Category>

Constraints:
- <Hard constraint 1>
- <Hard constraint 2>
- <Architectural constraint>
- <Project rules that bind: e.g., "must follow CLAUDE.md Rule X">

Out of scope:
- <Adjacent thing that's NOT being designed here>

What I want from you:
1. Acceptance criteria
2. Files / modules to touch
3. Dependencies and data flow
4. Integration points
5. Risks and mitigations
6. Open questions

Do NOT implement. Draft the plan only.
```

### 11.2 Key elements

- **Constraints upfront** — agent designs within them rather than producing a design that has to be retrofit
- **Out of scope** — speed brake against over-design
- **Explicit deliverable list** — agent knows what sections the plan must contain
- **"Do NOT implement"** — per CLAUDE.md "propose before implementing" rule

### 11.3 What a good design response looks like

The response should be a self-contained plan document that could be saved to `docs/Plans/<feature>.md` with minor formatting. If the response reads like a conversation rather than a document, ask for it to be restructured.

---

## 12. Type 4 — Verification / audit prompts

For asking an agent to check work — yours, theirs, or someone else's. Today's session used this multiple times: "double check the prompt and make sure it is complete", "recheck the CLAUDE.md if everything is ok and in place".

### 12.1 Structure

```
I'm about to <send/commit/push> the following <prompt/code/doc>.

Audit it for:
- <Specific concern 1>
- <Specific concern 2>
- <Common failure mode for this artifact type>

Verify against:
- <Source of truth 1, e.g., actual file state>
- <Source of truth 2, e.g., CLAUDE.md rules>

Report findings as:
- 🔴 BUG (would cause failure): <description + fix>
- 🟡 IMPROVEMENT (works but suboptimal): <description + suggested fix>
- 🟢 NIT (cosmetic): <description, optional fix>

Do NOT silently fix issues. Surface them with severity, let me decide.

<the artifact to audit>
```

### 12.2 Key elements

- **Specific concerns** — directs the audit; otherwise agent does generic review
- **Verify against** — explicit sources of truth; prevents agent from auditing against assumptions
- **Severity legend** — distinguishes "must fix" from "nice to fix"
- **"Do NOT silently fix"** — agent surfaces, user decides

### 12.3 Why this matters

Audit prompts catch bugs that the original drafter misses because of cognitive load. The audit is not redundant work — it's the second pair of eyes that the methodology specifically requires for high-stakes artifacts.

---

## 13. Type 5 — Recovery / diagnostic prompts

For restoring correct state when something goes wrong: agent reported mismatch, CI failed, drift discovered.

### 13.1 Structure

```
Situation: <one paragraph describing what happened>

Current state:
- <What we know about the actual state of files/git/CI>
- <What we expected vs what we got>

Constraints:
- Per CLAUDE.md Rule 6: do not improvise; verify against filesystem
- Per CLAUDE.md Rule 3: if pushed, fix-forward (no force-push)

What I need from you:
1. Diagnose the gap (don't guess; verify)
2. Propose 2-3 resolution options with trade-offs
3. Wait for my decision before acting

Do NOT begin fixing until I confirm the approach.
```

### 13.2 Key elements

- **Current state** — explicit facts, not interpretation
- **Constraints with rule citations** — agent knows what NOT to do
- **Multiple resolution options** — prevents jumping to first viable fix
- **"Wait for my decision"** — recovery is high-stakes; user is the final authority

---

## 14. Reusable templates

The following templates are ready to copy-paste-modify for common prompt patterns. See companion file `docs/standards/PROMPT_TEMPLATES/` for the actual template files.

### 14.1 Templates available

| Template | Use case | File |
|---|---|---|
| Type 1 — Cursor multi-file edit | Standard implementation prompt | `PROMPT_TEMPLATES/01-cursor-multi-file-edit.md` |
| Type 1 — Single-file edit | Simpler one-file change | `PROMPT_TEMPLATES/01-cursor-single-file-edit.md` |
| Type 1 — Doc-only change | When only `.md` files are edited | `PROMPT_TEMPLATES/01-cursor-docs-only.md` |
| Type 1 — Codex handoff variant | Multi-file edit handed to Codex (OPTIONAL — multi-agent projects only) | `PROMPT_TEMPLATES/01-codex-handoff.md` |
| Type 2 — Session start | Daily/weekly Claude.ai session opener | `PROMPT_TEMPLATES/02-session-start.md` |
| Type 3 — Design draft | Pre-implementation design prompt | `PROMPT_TEMPLATES/03-design-draft.md` |
| Type 4 — Prompt audit | Audit your own prompt before sending | `PROMPT_TEMPLATES/04-prompt-audit.md` |
| Type 4 — Code review | Audit code changes before commit | `PROMPT_TEMPLATES/04-code-review.md` |
| Type 5 — CI failure recovery | Diagnose + fix-forward after CI red | `PROMPT_TEMPLATES/05-ci-failure.md` |
| Type 5 — Drift recovery | When agent reports state mismatch | `PROMPT_TEMPLATES/05-drift-recovery.md` |
| Type 5 — Retry with deviation warning | Re-prompt after an agent deviated from scope | `PROMPT_TEMPLATES/05-retry-with-deviation-warning.md` |

> **Status note:** The `PROMPT_TEMPLATES/` directory is planned but not yet populated. Until then, use the structures in §§ 3, 10, 11, 12, 13 above as your templates. The Codex handoff variant is described in § 3.11; the retry-with-deviation-warning template is in § 9.5.

---

## 15. When the full protocol doesn't fit

The Type 1 protocol (§§ 2-9) is calibrated for multi-file edits to tracked files where the cost of a defect is high. Some situations don't need the full overhead.

### 15.1 Single-line edit to a single file

For a 1-line value change (a version bump, a single string substitution), the full protocol is overkill. Use a minimal prompt with:

- Universal preamble (§ 2)
- ALLOWLIST with one file
- TODO checklist (§ 3.2.1) — minimal, perhaps 4-5 boxes
- One FIND/REPLACE block
- Pre-commit governance (§ 3.6)
- Commit ceremony (§ 3.7)
- DO NOT PUSH

Skip the gather commands, the multi-section structure, and the elaborate verification grep ladder. The minimal prompt still gives the agent enough structure to commit cleanly without inventing process.

### 15.2 Exploratory or read-only work

If you're inspecting state — reading files, running greps, checking git status, querying the database — no prompt structure is needed. Just give the agent the question and let it use its tools. The protocol exists to govern *commits*; reads don't need governing.

### 15.3 Emergency fix

If the system is on fire (production down, deploy stuck, incident in progress), the cost of protocol overhead can exceed the cost of a small protocol violation.

In that case:
1. Make the fix as quickly as discipline allows.
2. **Document the deviation in the commit message** — explicitly list which protocol elements were skipped and why.
3. **Capture the lesson afterward** — open a follow-up commit (or LESSONS entry) describing what was deferred and what should be retroactively done (e.g., manifest update, governance rerun) once the incident is over.

Speed has a cost; protocol violations also have a cost. Pick deliberately. Never let "this is an emergency" become a habit-forming excuse — it should feel uncomfortable to skip protocol.

### 15.4 When to escalate to manual intervention

If a Type 1 prompt has been re-issued **3+ times** due to FIND mismatches, structural issues, or repeated agent failures, **stop and investigate**. Either:

- The prompt is wrong (audit it again per § 7)
- The file state is unexpected (compare against `git log` and `cicd_setup_tracker.md`)
- There's a hidden constraint not reflected in the prompt (governance, dependency, side effect)

Don't keep iterating on the same approach hoping the agent figures it out. After 3 failed iterations, the operator's time is better spent diagnosing the gap than re-issuing the prompt.

When manual intervention is needed:
1. Stop the prompt cycle.
2. Diagnose by reading current file state, recent commits, and any related governance docs.
3. Decide: rewrite the prompt? Pause and ask the user? Hand-edit the file and document the deviation?
4. Resume only after the gap is understood.

---

## End of standards

Prompt-craft is the difference between an AI agent that amplifies your work and one that silently degrades it. The patterns above were learned the hard way — every rule has a debugging session behind it.

When a new pattern emerges from a debugging session, **add it here**. When a rule above stops paying its weight, surface it for review — but never delete a rule without an explicit reason captured in `archive/LESSONS.md`.

The discipline scales: a 3-minute audit ritual prevents 30-minute mid-execution interruptions. Slow down to draft well.
