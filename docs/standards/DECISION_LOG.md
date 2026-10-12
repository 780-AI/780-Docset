<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v0.1 — 2026-10-12 — Initial (Standard Set Version v2.8): decision-log template — one entry per operator decision, with the operator's verbatim answer. Vault-only at v2.8; delivered to projects at a later Set Version.
-->

<!-- TEMPLATE-ONLY:BEGIN (template banner — deleted at instantiation; sync never propagates this block) -->
> **This file is a TEMPLATE.** A project copies it to `docs/DECISION_LOG.md`, deletes this
> TEMPLATE-ONLY block (markers included), resets the header to VERSION 1.0 with a one-line
> creation entry, and records its decisions below. The project-local copy is project-owned:
> no sync ever overwrites it.
<!-- TEMPLATE-ONLY:END -->

# DECISION_LOG.md — Operator decisions

**What this file is:** the single record of every decision the operator makes for this project —
scope, design options, approvals, intake-gate answers, waivers — written once, in plain words,
with the operator's exact reply. Plans, CHANGELOG entries and memory cite an entry by its id
(`DL-NNN`) instead of restating the decision.

## Rules

1. **One entry per decision**, added at the top (newest first). Ids are permanent and never reused.
2. **The question as it was asked** — in plain words, with the options and what each one does.
3. **The answer is the operator's verbatim reply**, in quotes, with its date — never paraphrased.
   A reply that answers several questions is quoted in each entry it answers.
4. **Applied in** names where the decision was carried out (plan section, commit, file); filled in
   when known, completed later by an appended line.
5. **Entries are never edited or deleted.** A changed decision is a NEW entry that says
   "Supersedes DL-NNN"; the old entry gets one appended line, "Superseded by DL-MMM".
6. **What counts:** any choice between options the operator was asked to make. Routine "go on
   commit?" / "push" confirmations are not entries — the commit and the push record them.
7. The file's VERSION bumps once per commit that adds entries.

## Entry format

```markdown
### DL-NNN — YYYY-MM-DD — <short title>

- **Question:** <plain words — what was asked>
- **Options:** A — <what it does> / B — <what it does> (recommended: <X>)
- **Answer:** "<the operator's verbatim reply>" — YYYY-MM-DD
- **Decision:** <one line: what was decided>
- **Applied in:** <plan § / commit / file>
```

---

## Decisions (newest first)

_(none yet)_
