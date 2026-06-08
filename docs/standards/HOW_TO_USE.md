<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Slimmed: the long bootstrap walkthrough is replaced
by a pointer to SETUP.md (the one-shot prompt). Retains the supporting prompts (Day-One feature work,
code review, prompt audit, quarterly audit, lesson backport), scrubbed and trimmed. Established as
Standard Set Version v1.0.
-->

# HOW_TO_USE.md — Practical usage guide

This file holds the **supporting prompts** for working day-to-day with the suite. The headline workflow
— bootstrapping a new project — has its own dedicated file.

- **Bootstrap a new project →** use **`SETUP.md`** (a single paste-and-run prompt).
- **Detailed click-through walkthrough →** `NEW_PROJECT_BOOTSTRAP.md`.
- **Conceptual overview →** `README.md`. **Versioned set manifest →** `STANDARDS_INDEX.md`.

The prompts below establish the binding session protocol from message 1 so you don't re-explain it each
session. Each is copy-paste ready; fill the `[bracketed]` placeholders.

---

## 1. Day-One feature-work prompt (first session after bootstrap)

```
I'm working on [project-name], a [one-line domain]. Bootstrapped from Standard Set Version v1.0.

Approach (per CLAUDE.md):
1. FIRST action — session-start pre-flight per Rule 9: read docs/SESSION_OPENER.md, run its § 1
   pre-flight, and post the § 4 first-response block BEFORE acting on the task.
2. Re-anchor on CLAUDE.md (quick re-read of any section the task touches).
3. Classify the change (Minor vs Major per § 5). Critical-file edits are always Major.
4. If Major: propose the design BEFORE implementing (§ 6 step 2) — wait for my confirmation.
   If vital (Critical File / central logic): use the § 15 plan workflow.
5. Implement per the focused standards (load via the § 12 dispatcher).
6. Sync all required docs in the same commit (PROJECT_STANDARDS § 4 trigger table).
7. Code-review pass on each modified file BEFORE git add (Rule 10).
8. Pair any behavior-affecting change with a QA scenario (Rule 11).
9. Validate (§ 8); governance scripts must exit 0. Commit via git commit -F (Rule 4). Don't push.

Session protocol: ONE task per message; WAIT for my reply; inline options (no popups); verify via
filesystem before acting; investigate-when-questioned (L032).

Today's task: [one sentence]. Start with the pre-flight, then give me a 3-bullet approach
(classification, files touched, risk) and wait for my confirm.
```

## 2. Code-review request prompt (before staging)

```
I have unstaged changes in [project]. Before I git add, do a code-review pass per CLAUDE.md Rule 10 / § 8.5.
Files: [paths, or "all unstaged per git status --short"].
For each file: read it; walk it in plain English (what changed, intent); check — reads correctly?
edge cases handled? subtle bug a future reader would catch? orphan/unintended edits?
Report each finding as 🔴 BUG (fix before staging) / 🟡 IMPROVEMENT / 🟢 NIT, with a suggested fix.
Do NOT silently fix — surface findings; I decide. End with: "Stage as-is" / "Fix N first" / "Reconsider".
```

## 3. Prompt-audit prompt (audit a multi-file edit prompt before sending)

```
Audit this multi-file edit prompt per PROMPT_STANDARDS § 7 before I send it.
Check: FIND blocks anchored against current file state (grep -F to confirm) and unique; line counts
correct; verification greps can't false-positive; STOP conditions explicit; commit uses git commit -F;
git status --short BOTH before AND after git add (Rule 6); ALLOWLIST matches the real file set; the
files-modified checklist matches the ALLOWLIST; no hedges; pre-draft duplicate check done.
Report 🔴/🟡/🟢 with fixes. Do NOT silently fix — surface; I redraft.
[paste prompt below]
```

## 4. Quarterly audit prompt (manifest + lessons + memory hygiene)

```
Quarterly audit for [project] (README § 4.4 + MEMORY_PROTOCOL § 5). Audit only — do NOT fix anything;
I authorize each fix separately. Walk, pasting raw command output then a summary:
1. Manifest sweep — every committed .md + VERSION-bearing code file vs docs/documents_manifest.md;
   report filesystem-not-in-manifest, manifest-pointing-at-missing, version-cell mismatches.
2. Lessons review — for each L00N, is its rule still in force? any silently relaxed?
3. Memory hygiene — list memory entries; categorize (store/delete) per the four-category test.
4. CHANGELOG continuity — each meaningful commit since last audit has a CHANGELOG entry?
5. Tracker review — rows stuck "in progress" > 2 weeks; stale deferred items.
End with counts per audit + top-3 priorities + recommended next session.
```

## 5. Lesson-backport prompt (propagate a lesson into the suite)

```
Backport a lesson into the standards source at [path].
Lesson: trigger/incident [..]; cost [..]; codification (rule + file) [..]; portability rationale [..].
Procedure: find the next L-number at the top of LESSONS.md; draft the entry (incident + cost +
codification + cross-refs); pick the topical standards file to host the rule body and update it; bump
per-file VERSION + CHANGE LOG on every modified file; if it's a coordinated multi-file change, add a
Set-Version history entry in STANDARDS_INDEX § 6 and bump the Set Version; update CHANGELOG; commit.
ONE step at a time: show me the draft lesson first; wait for approval before editing the topical file.
```

---

## Where to go next

- **Bootstrapping now?** → `SETUP.md`.
- **Starting your first feature?** → § 1 above.
- **Sending a multi-file edit prompt?** → audit it with § 3 first.
- **Why is the suite shaped this way?** → `README.md` (design rationale).
- **The Set-Version concept / how to bump?** → `STANDARDS_INDEX.md` § 5.
- **Every lesson (incident → rule)?** → `LESSONS.md` (L001–L049).
