<!-- VERSION: 1.4 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.4 — 2026-08-16 — Standard Set Version v1.6 (PLAN-008 sync-enablement): TEMPLATE-ONLY banner block + PROJECT-OWNED instance-heading block, so section-merge sync never propagates template banners and preserves the adopter's heading.
v1.3 — 2026-08-16 — Standard Set Version v1.5 (PLAN-010): § 1.6 retitled "/tmp cleanup + locality confirm" — adds the Rule 14 close-side confirm (claude_project_data.sh status → STATUS: OK; new out-of-folder state moved in or cataloged same-commit).
v1.2 — 2026-08-16 — Standard Set Version v1.4: § 1.4 push-state flip step + § 2.1 row 5 (L055).
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): wrapped the project-customizable block (§ 2.2 project-specific wrap-up failure-mode table) in PROJECT-OWNED markers so a future sync preserves it. Standard Set Version v1.1.
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

<!-- TEMPLATE-ONLY:BEGIN (delivery-crate banner — deleted at instantiation; sync never propagates this block) -->
# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (template)

> **This file is a TEMPLATE.** Adopters copy it to their project's `docs/SESSION_CLOSER.md`, customize the placeholder sections per project (output-block specifics, project-specific failure-mode rows in § 2), and add the binding rule to their repo-root `CLAUDE.md` (per template `CLAUDE.md` Rule 12 / § 3). Once instantiated, the project-local copy is BINDING for every Claude session in that repository. At instantiation: delete this TEMPLATE-ONLY block (markers included) and fill in the PROJECT-OWNED heading block below.
<!-- TEMPLATE-ONLY:END -->
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (project-local)

> **This is the BINDING project-local instance** for `<project-name>`. When the operator triggers a wrap-up, Claude MUST read this file and execute its § 1 routine, then post the § 4 output block BEFORE any farewell (per `CLAUDE.md` Rule 12).
<!-- PROJECT-OWNED:END -->

**Why this file exists:** Across long sessions, new patterns / new rules / new lessons / scope expansions / memory updates emerge organically and are easy to forget by farewell time. Without a forcing function at session-end, codification slips and the next session can't pick up cleanly. SESSION_CLOSER.md IS the forcing function: the binding rule (Rule 12) says "read this file and execute its routine before any farewell," and the § 4 output template is the proof-of-wrap-up visible to the operator. See `LESSONS.md` L048 for the originating pattern.

This file is the symmetric counterpart to `SESSION_OPENER.md` (Rule 9, pre-flight at session start). Together they bracket every session — pre-flight at start, wrap-up at end.

---

## 1. Wrap-up routine Claude MUST execute on the trigger command

**Trigger keywords** (any of these activates Rule 12 + this routine):
- `"wrap up"`
- `"wrap"`
- `"end session"`
- `"close out"` (context-disambiguated — if discussing project-specific closeout logic, NOT a session-end trigger)
- `"end of session"`
- `"finish up"`

Run steps in order. Each step's output goes into the § 4 first-response output block.

### 1.1 Repo state
```bash
git status --short # working-tree state
git log --oneline origin/<main-branch>..HEAD # unpushed commits
git log --oneline -<N> # session commits (N = approx count made this session)
```

Replace `<main-branch>` with `main` / `master` per project convention.

### 1.2 Project + standards versions

Project-specific. Customize per project to surface:
- Live deployable artifact's version (EA `// VERSION:` / Docker image tag / commit SHA / etc.)
- Recent snapshots / tags
- **Standards Set Version** (from `docs/standards/STANDARDS_INDEX.md` § 1)

### 1.3 Pending operator decisions

Surface any of:
- DRAFT plans in `docs/Plans/*.md` (status DRAFT, awaiting `APPROVE D?.?`)
- Blocked tasks (Phase 4 verify pending, push not yet authorized, tag not yet created)
- Approval scenarios awaiting operator response
- Cross-project propagation prompts saved to `~/Desktop/` awaiting operator action

### 1.4 Outstanding `OPEN_TASKS.md`

If `docs/Plans/OPEN_TASKS.md` exists (gitignored local-only register per L046), surface:
- Active plans — open items
- Plans in drafting / future
- Operator-driven (no plan) items
- Maintenance / housekeeping items
- **Lesson candidates** section (if populated by step 1.7 below)

**Push-state flip (per `LESSONS.md` L055):** if a `git push` happened this session, flip the matching `OPEN_TASKS.md` push-state line(s) ("unpushed" / "push held" → pushed + date) in this same wrap-up. Committed trackers stay frozen at their commit; only the live register is flipped.

### 1.5 Memory updates landed this session

List new/modified memory files in the project's `~/.claude/projects/<sanitized-cwd>/memory/` dir:
- New `feedback_*.md` / `project_*.md` files
- Updated existing memory files (description/body changes)
- `MEMORY.md` index hook line additions/changes

### 1.6 `/tmp/` cleanup + locality confirm

Remove session-artifacts:
- `/tmp/commit_msg.txt` (Rule 4 commit-message files)
- `/tmp/recent_transcripts.txt` (skill artifacts)
- Any other `/tmp/` files created during the session that aren't expected to persist

```bash
rm -f /tmp/commit_msg.txt /tmp/recent_transcripts.txt
```

**Locality confirm (Rule 14):** `bash scripts/claude_project_data.sh status` → expect `STATUS: OK`.
If any new project state landed outside the folder this session, move it in (same symlink pattern)
or catalog it in the machine-migration doc — same-commit.

### 1.7 Lessons-learned scan (the detail-capture step)

Review the session transcript for candidate codifications. Output goes into both the § 4 output block AND `OPEN_TASKS.md` "Lesson candidates" section.

**Categories to scan for:**

| Category | What to look for |
|---|---|
| **New standing rule** | Did operator establish a "from now on" rule? Did multiple incidents in the session converge to a single new discipline? |
| **New lesson (L0NN)** | Was a non-obvious bug pattern surfaced and root-caused? Was a meta-rule discovered (forcing-function cadence, audit-before-fix, etc.)? |
| **New memory entry** | Was a workflow convention / operator preference established that should persist across sessions? |
| **New SESSION_OPENER § 3.x row** | Was a repeat-pattern observed that warrants a new failure-mode catalog row? |
| **Scope expansion** | Did any existing plan's scope change? Memory + OPEN_TASKS must reflect. |
| **Spec / domain drift** | Did project behavior change in a way that requires `docs/<domain-spec>/*.md` (or equivalent domain spec) updates? |
| **Convention** | Was a new file-organization / naming / commit-message convention established? |

**For each candidate**, decide:
- **Codify now** (same wrap-up commit) — if confidence is high and operator confirms
- **Add to `OPEN_TASKS.md` "Lesson candidates"** — if needs confirmation, more proof, or pattern hasn't been proven across multiple instances yet
- **Discard** — if not significant enough to codify (operator decides)

Surface all candidates in the § 4 output block with recommendation per candidate (codify / queue / discard).

### 1.8 Next-up suggestion

Based on OPEN_TASKS + DRAFT-plan state + any blocking dependencies, recommend the natural next action for the next session.

### 1.9 Confirm done

End the wrap-up with explicit "Session wrap-up complete. Safe to close." or equivalent. Wait for any operator follow-up before treating the session as ended.

---

## 2. Wrap-up failure-mode catalog (mistake-avoidance for next sessions)

> **Customize this section per project.** Seed rows with the universal patterns below; append project-specific rows as new wrap-up failure patterns surface.

Each row links to the memory or lesson that codifies it.

### 2.1 Universal patterns (seed from the standards suite)

| # | Pattern | Trigger | Memory / lesson |
|---|---|---|---|
| 1 | Wrapping up without executing the routine — going straight to farewell | every wrap-up trigger keyword | `CLAUDE.md` Rule 12 + project memory `feedback_session_closer_routine` |
| 2 | Lessons-learned scan skipped — new insights lost between sessions | every wrap-up | `LESSONS.md` L048 |
| 3 | `/tmp/` artifacts left behind (commit_msg.txt etc.) | every wrap-up | this file § 1.6 |
| 4 | `OPEN_TASKS.md` not updated with session-end state | every wrap-up | this file § 1.4 + `LESSONS.md` L046 |
| 5 | Push-state line not flipped after a mid-session push — register reads "unpushed" for pushed work | any session that ran `git push` | this file § 1.4 + `LESSONS.md` L055 |

### 2.2 Project-specific patterns

> Add rows here as new wrap-up failure patterns surface. Each new row should be paired with a memory in the same commit per `LESSONS.md` L008 (manifest completeness).

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
| # | Pattern | Trigger | Memory / lesson |
|---|---|---|---|
| _(empty — append as needed)_ | | | |
<!-- PROJECT-OWNED:END -->

---

## 3. When the wrap-up may be abbreviated

Operator may explicitly say **"skip wrap-up"** for trivial mid-session check-ins where operator doesn't want a full routine. Operator-only authorization — never self-skip.

Even when abbreviated:
- Steps 1.1-1.3 (repo state + versions + pending decisions) remain in force — they're the minimum safety net.
- Steps 1.4-1.9 may be omitted.

The § 4 output block in abbreviated form is shorter but still posted.

---

## 4. First-response output template (what Claude posts when wrap-up triggered)

```
**Session wrap-up — executed per docs/SESSION_CLOSER.md**

**Repo state**
- Working tree: <clean | M file1, file2, ...>
- Commits this session: <count> (newest first):
 - <SHA1> <subject>
 - <SHA2> <subject>
 - ...
- Unpushed: <N> commits ahead of origin/<branch>

**Project + standards versions**
- <Project's live-artifact version: deployable name + version string>
- <Recent snapshots / tags as project convention requires>
- Standards Set Version: <vX.Y>

**Pending operator decisions**
- <DRAFT plan name + APPROVE D?.? string awaited>
- <Phase 4 verify scenario awaiting operator run>
- <Push authorization for SHA <X>>
- <Cross-project propagation prompt at ~/Desktop/<file> awaiting paste>
- (none, if nothing pending)

**Outstanding OPEN_TASKS** (from docs/Plans/OPEN_TASKS.md if present)
- Active plans — open items: <count>; brief list
- Plans in drafting / future: <count>; brief list
- Operator-driven: <count>; brief list
- Maintenance: <count>; brief list
- Lesson candidates: <count>; brief list

**Memory updates this session**
- NEW: <file1>
- UPDATED: <file2>
- MEMORY.md index changes: <Y/N>
- (none, if no memory touched)

**/tmp/ cleanup**
- Removed: <list> (or "nothing to remove")

**Lessons-learned scan**
- <Category>: <candidate text> → recommendation: <codify | queue | discard>
- <Category>: <candidate text> → recommendation: <codify | queue | discard>
- (none, if nothing surfaced)

**Next-up suggestion**
- <one or two sentences on what to start next session with>

**Session wrap-up complete. Safe to close.**
```

This block is the proof-of-wrap-up. Posted in full at the end of every "wrap up"-triggered session.

---

## 5. Maintenance

When a new wrap-up failure pattern is observed (operator flags a recurring miss or detail loss between sessions):

1. Create the matching `feedback_<slug>.md` or `project_<slug>.md` memory file (per `MEMORY_PROTOCOL.md`).
2. Add a row in § 2 of this file (universal if domain-neutral; project-specific if project-only).
3. Add the memory to `MEMORY.md` index.
4. Same-commit per `LESSONS.md` L008 (manifest completeness).

Do NOT let this file go stale. Its value depends on being the current, complete catalog of session-end failure modes.

---

## 6. Relationship to SESSION_OPENER.md

This file is the symmetric counterpart to `SESSION_OPENER.md` (Rule 9, pre-flight at session start). Together they bracket every session:

| Aspect | SESSION_OPENER (Rule 9) | SESSION_CLOSER (Rule 12) |
|---|---|---|
| Trigger | New session opens (message 1) | Operator says "wrap up" (or alias) |
| Mandatory? | Yes — every session | Yes — on the trigger keyword |
| Routine | § 1 pre-flight (4 steps) | § 1 wrap-up (9 steps) |
| Output | § 4 first-response block | § 4 output template |
| Catalog | § 3 failure-mode rows | § 2 failure-mode rows |
| Abbreviation | Operator-said "skip pre-flight" | Operator-said "skip wrap-up" |

Both files are BINDING (Tier 1 in the standards suite). Both are referenced by the standing rules in `CLAUDE.md` § 3.

---

## 7. Relationship to the rest of the standards suite

This file is a **binding standards file** (Tier 1) in the suite. It is referenced by:

- `CLAUDE.md` Rule 12 (the binding rule that mandates the wrap-up)
- `MEMORY_PROTOCOL.md` (the failure-mode catalog rows pair 1:1 with feedback memories)
- `LESSONS.md` L048 (the lesson capturing why this file exists)
- `PROJECT_STANDARDS.md` § 8 commit policy (wrap-up is a separate phase from commit/governance/push)

This file does NOT replace:
- `SESSION_OPENER.md` (session-start, not session-end)
- `CLAUDE.md` § 8 validation checklist (pre-commit, not session-end)
- `MEMORY_PROTOCOL.md` memory hygiene rules (always-in-force, not session-bounded)

The wrap-up runs ONCE at the back of a session, not at every turn. After it has been posted, the session can close.

---

## End of file

If you are reading this in a freshly-bootstrapped project, your next step is to walk `NEW_PROJECT_BOOTSTRAP.md` to instantiate the project-local copy and customize §§ 2 + 4 output-block specifics. If you are reading this as a working contributor responding to a "wrap up" command, you should already be producing the § 4 output block — if you haven't, do so now before any farewell message.
