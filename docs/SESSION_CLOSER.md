<!-- VERSION: 1.3 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Source: docs/standards/SESSION_CLOSER.md (template) v1.2. Project-local instance for Standard DocSet. -->
<!--
CHANGE LOG
v1.3 — 2026-08-16 — Standard Set Version v1.4: § 1.4 push-state flip step + § 2.1 row 5 (L055); header Source ref → template v1.2.
v1.2 — 2026-06-14 — Project display name → "Standard DocSet" (header Source ref + binding-instance line). Engine package `standard_document_updater` unchanged.
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): wrapped the project-owned block (§ 2.2 project-specific wrap-up failure-mode table) in PROJECT-OWNED markers so a future sync preserves it.
v1.0 — 2026-06-07 — Project bootstrap. Instantiated from the v1.0 template (docs/standards/SESSION_CLOSER.md v1.0). Customized § 1.2 versions (tool engine version + adopted Set Version; no EA / deploy artifact) and § 4 output block. BINDING per CLAUDE.md Rule 12.
-->

# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (project-local)

> **This is the BINDING project-local instance** for `Standard DocSet`. When the operator triggers a wrap-up, Claude MUST read this file and execute its § 1 routine, then post the § 4 output block BEFORE any farewell (per `CLAUDE.md` Rule 12).

**Why this file exists:** Across long sessions, new patterns / rules / lessons / scope changes emerge and are easy to forget by farewell time. This file is the forcing function; the § 4 output block is the proof-of-wrap-up. Symmetric counterpart to `docs/SESSION_OPENER.md` (Rule 9). See `archive/LESSONS.md` L048.

---

## 1. Wrap-up routine Claude MUST execute on the trigger command

**Trigger keywords** (any activates Rule 12 + this routine): `"wrap up"` / `"wrap"` / `"end session"` / `"close out"` / `"end of session"` / `"finish up"`.

Run steps in order; each step's output goes into the § 4 block.

### 1.1 Repo state
```bash
git status --short                              # working-tree state
git log --oneline origin/master..HEAD 2>/dev/null  # unpushed commits (if remote exists)
git log --oneline -<N>                          # session commits (N ≈ count made this session)
```

### 1.2 Tool + standards versions
- Engine version — `src/standard_document_updater/` `# VERSION:` headers (once the engine lands).
- Adopted **Standards Set Version** — `docs/SET_VERSION_ADOPTED.md`.
- Any pending tag operations on this repo.

### 1.3 Pending operator decisions
- DRAFT plans in `docs/Plans/*.md` (status DRAFT, awaiting `APPROVE D?.?`).
- Blocked tasks (Phase 4 verify pending, push not yet authorized, tag not yet created).
- Awaiting-approval QA scenarios.

### 1.4 Outstanding `docs/Plans/OPEN_TASKS.md` (if present, gitignored)
Surface active items, drafting/future items, operator-driven items, maintenance items, and the **Lesson candidates** section.

**Push-state flip (per `archive/LESSONS.md` L055):** if a `git push` happened this session, flip the matching OPEN_TASKS push-state line(s) ("unpushed" / "push held" → pushed + date) in this same wrap-up. Committed trackers stay frozen at their commit; only the live register is flipped.

### 1.5 Memory updates landed this session
List new/modified memory files under `~/.claude/projects/<sanitized-cwd>/memory/` + any `MEMORY.md` index changes.

### 1.6 `/tmp/` cleanup
```bash
rm -f /tmp/commit_msg.txt /tmp/recent_transcripts.txt
```
Remove any other session scratch artifacts.

### 1.7 Lessons-learned scan (the detail-capture step)
Review the session transcript for candidate codifications across these categories: new standing rule, new lesson (L0NN), new memory entry, new `SESSION_OPENER` § 3.2 row, scope expansion, spec/domain drift (`docs/architecture.md`), new convention. For each candidate decide: **codify now** / **add to OPEN_TASKS "Lesson candidates"** / **discard**. Surface all candidates with a recommendation each.

### 1.8 Next-up suggestion
Recommend the natural next action for the next session based on OPEN_TASKS + DRAFT-plan state + blockers.

### 1.9 Confirm done
End with explicit "Session wrap-up complete. Safe to close." Wait for any operator follow-up.

---

## 2. Wrap-up failure-mode catalog

### 2.1 Universal patterns (seed from the standards suite)

| # | Pattern | Trigger | Memory / lesson |
|---|---|---|---|
| 1 | Wrapping up without executing the routine — straight to farewell | every wrap-up trigger | `CLAUDE.md` Rule 12 |
| 2 | Lessons-learned scan skipped — insights lost between sessions | every wrap-up | `LESSONS.md` L048 |
| 3 | `/tmp/` artifacts left behind | every wrap-up | this file § 1.6 |
| 4 | `OPEN_TASKS.md` not updated with session-end state | every wrap-up | this file § 1.4 + `LESSONS.md` L046 |
| 5 | Push-state line not flipped after a mid-session push — register reads "unpushed" for pushed work | any session that ran `git push` | this file § 1.4 + `LESSONS.md` L055 |

### 2.2 Project-specific patterns

> Add rows as wrap-up failure patterns surface; pair each with a memory in the same commit per `LESSONS.md` L008.

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
| # | Pattern | Trigger | Memory / lesson |
|---|---|---|---|
| _(empty — append as needed)_ | | | |
<!-- PROJECT-OWNED:END -->

---

## 3. When the wrap-up may be abbreviated

Operator may explicitly say "skip wrap-up". Operator-only authorization — never self-skip. Even abbreviated, steps 1.1–1.3 remain in force; 1.4–1.9 may be omitted. The § 4 block is posted in shorter form.

---

## 4. First-response output template (what Claude posts when wrap-up triggered)

```
**Session wrap-up — executed per docs/SESSION_CLOSER.md**

**Repo state**
- Working tree: <clean | M file1, ...>
- Commits this session: <count> (newest first):
  - <SHA1> <subject>
- Unpushed: <N> ahead of origin/master (or "no remote")

**Tool + standards versions**
- Engine version: <version or "not yet implemented">
- Standards Set Version: <vX.Y>

**Pending operator decisions**
- <DRAFT plan + APPROVE string awaited / Phase 4 verify pending / push authorization> (or "none")

**Outstanding OPEN_TASKS** (from docs/Plans/OPEN_TASKS.md if present)
- Active: <count>; Drafting/future: <count>; Operator-driven: <count>; Maintenance: <count>; Lesson candidates: <count>

**Memory updates this session**
- NEW: <file> / UPDATED: <file> / MEMORY.md changes: <Y/N> (or "none")

**/tmp/ cleanup**
- Removed: <list> (or "nothing to remove")

**Lessons-learned scan**
- <Category>: <candidate> → <codify | queue | discard>
- (none, if nothing surfaced)

**Next-up suggestion**
- <one or two sentences>

**Session wrap-up complete. Safe to close.**
```

This block is the proof-of-wrap-up.

---

## 5. Maintenance

When a new wrap-up failure pattern is observed: create the matching memory; add a row in § 2; add to `MEMORY.md`; same-commit per `LESSONS.md` L008. Do not let this file go stale.
