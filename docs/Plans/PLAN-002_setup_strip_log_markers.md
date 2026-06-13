<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-06-13 -->
<!-- Status: DRAFT (awaiting Phase 2 operator approval) -->
<!--
CHANGE LOG
v0.1 — 2026-06-13 — Initial draft of Slice 1 (setup-and-strip + experiences log + PROJECT-OWNED markers), per docs/architecture.md § 10. Rule 13 senior-review pass recorded at the foot of this file (anchors verified against the real templates: CLAUDE.md §1/§4/§13/§14 = lines 17/229/564/579; OPENER §2/§3.2; CLOSER §2/§2.2; root CLAUDE.md architecture refs = lines 240,576; SET_VERSION_ADOPTED currently in docs/standards/).
-->

# PLAN-002 — Slice 1: setup-and-strip + experiences log + PROJECT-OWNED markers

## 1. Goal

Make the architecture's **footprint** and **non-clobbering sync** real at the document layer, before any
engine code. Three things: (a) `SETUP.md` installs the operative standard then **strips** the setup
machinery; (b) the suite gains the **experiences-log** template (`STANDARDS_LOG.md`); (c) the
customizable blocks in `CLAUDE.md` + the session files are wrapped in **`PROJECT-OWNED` markers** so a
future `sync` can update everything *except* those blocks.

No engine code in this slice (it's docs/prompt/markers). See `docs/architecture.md` §§ 3, 4, 5, 7, 10.

## 2. Operator constraints

- Footprint = operative standard kept, setup machinery stripped (settled 2026-06-13).
- Markers are the agreed mechanism for non-clobbering sync (settled 2026-06-13).
- Single-agent: this project's *own* root `CLAUDE.md` keeps its single-agent § 14 stub; the **template**
  keeps the full optional § 14 (per D-A on PLAN-001).

## 3. Scope summary

- **A — `PROJECT-OWNED` markers** in the templates (`docs/standards/CLAUDE.md`, `SESSION_OPENER.md`,
  `SESSION_CLOSER.md`) AND this project's adopter instances (root `CLAUDE.md`, `docs/SESSION_OPENER.md`,
  `docs/SESSION_CLOSER.md`) — so the repo dogfoods them.
- **B — experiences-log template** `docs/standards/STANDARDS_LOG.md` (schema + legend + one example).
- **C — `SETUP.md` rework**: create `docs/STANDARDS_LOG.md` from the template; write
  `SET_VERSION_ADOPTED.md` to `docs/` (not `docs/standards/`); add the final **strip step** with the
  explicit kept/stripped manifest.
- **D — convention move**: relocate this repo's `docs/standards/SET_VERSION_ADOPTED.md` →
  `docs/SET_VERSION_ADOPTED.md` (consistency with the new SETUP target).
- **E — drift fix**: root `CLAUDE.md` lines 240 & 576 — `docs/architecture.md` now exists (drop
  "created when the engine lands").
- **F — sync artifacts**: `STANDARDS_INDEX.md` (add `STANDARDS_LOG` to the suite; bump counts),
  `documents_manifest.md`, `docs/folder_structure.md`, `CHANGELOG.md`, `docs/architecture.md` (tick
  Slice 1 done in § 10).

## 4. Phase tracker (small plan — in-file per § 15.7)

- Phase 0 — Audit ........... ✅ 2026-06-13 (anchors verified; see header + § 13 senior-review)
- Phase 1 — Design ......... ✅ 2026-06-13 (this file + Rule 13 pass below)
- Phase 2 — Approval ....... ⏸ awaiting `APPROVE PLAN-002`
- Phase 3 — Implement (one commit, ALLOWLIST-bounded):
  - ⏸ 3A markers in 3 templates · ⏸ 3A markers in 3 adopter instances
  - ⏸ 3B `STANDARDS_LOG.md` template created
  - ⏸ 3C `SETUP.md` reworked (log create + SVA→docs/ + strip step)
  - ⏸ 3D move `SET_VERSION_ADOPTED` → `docs/`
  - ⏸ 3E root `CLAUDE.md` drift fix (lines 240, 576)
  - ⏸ 3F sync artifacts (INDEX, manifest, folder_structure, CHANGELOG, architecture § 10)
- Phase 4 — Validate ....... ⏸ (QA S1–S3 below)
- Phase 5 — Operator gate .. ⏸ push pending (no remote)

## 5. Transformation rules

### 5A — `PROJECT-OWNED` marker convention

Wrap each customizable block exactly as:

```
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
…the customizable content…
<!-- PROJECT-OWNED:END -->
```

Insert markers around these sections (verified anchors). In **templates** they wrap placeholder content;
in **adopter instances** they wrap the project's real values — same section boundaries:

| File | Block to wrap |
|---|---|
| `CLAUDE.md` (template @17 / root) | § 1 Project context — the 4–5 `**…:**` lines |
| `CLAUDE.md` (template @229 / root) | § 4 — from after the `> Customize…` note through the "Future critical files" bullets, up to (not incl.) `**Identification rule…**` (which is suite-owned/generic) |
| `CLAUDE.md` (template @564 / root) | § 13 — only the `- **Domain behavior:** …` bullet |
| `CLAUDE.md` (template @579 / root) | § 14 — the whole section (single-agent adopters delete it); marker note: "single-agent adopters delete this entire block" |
| `SESSION_OPENER.md` (@57 / root) | § 2 — the environment/registry **table** (not the generic "Why this matters" tail) |
| `SESSION_OPENER.md` (@105 / root) | § 3.2 — the project-specific patterns table |
| `SESSION_CLOSER.md` (@131 / root) | § 2.2 — the project-specific patterns table |

Rule: markers go **inside** the section, hugging the customizable content, so the section heading itself
stays suite-owned (sync can re-title/reorder headings; it just won't touch marked bodies).

### 5B — `docs/standards/STANDARDS_LOG.md` (NEW, template)

Content: VERSION 1.0 header; a one-paragraph purpose; the status legend (`open` / `integrated` /
`rejected`); the entry schema; one worked `E001` example (status `open`). Header note: "TEMPLATE —
`SETUP.md` copies this to `docs/STANDARDS_LOG.md` and removes the example."

### 5C — `SETUP.md` edits (in the prompt body)

1. Step 5 (supporting files): add "create `docs/STANDARDS_LOG.md` from `docs/standards/STANDARDS_LOG.md`,
   removing the example entry."
2. Step 5: change `SET_VERSION_ADOPTED.md` target from `docs/standards/` to **`docs/`**.
3. Add **Step 8.5 — Strip**: after the commit-gate, list and delete the setup-machinery from
   `docs/standards/`:
   - DELETE: `SETUP.md`, `NEW_PROJECT_BOOTSTRAP.md`, `STANDARDS_INDEX.md`, `README.md` (meta),
     `HOW_TO_USE.md`, `PROJECT_INSTRUCTIONS_TEMPLATE.md`, `CLAUDE.md` (template), `LESSONS.md` (template),
     `SESSION_OPENER.md` (template), `SESSION_CLOSER.md` (template), `STANDARDS_LOG.md` (template),
     `SET_VERSION_ADOPTED.md` (template).
   - KEEP in `docs/standards/`: the topical library — `PROJECT_STANDARDS`, `PROMPT_STANDARDS`,
     `MEMORY_PROTOCOL`, `ENGINEERING_STANDARDS`, `VALIDATION_STANDARDS`, `CICD_STANDARDS`.
   - (Already outside `docs/standards/`: root `CLAUDE.md`, `archive/LESSONS.md`, `docs/SESSION_*`,
     `docs/SET_VERSION_ADOPTED.md`, `docs/STANDARDS_LOG.md`, governance, CI, manifest.)
   - Strip is a **second commit** in the target ("strip setup machinery") so the delivered-then-removed
     state is visible in history.

### 5D — move `SET_VERSION_ADOPTED` (this repo)

`git mv docs/standards/SET_VERSION_ADOPTED.md docs/SET_VERSION_ADOPTED.md`; update its references in
manifest + folder_structure + README + architecture wherever the path appears.

### 5E — root `CLAUDE.md` drift fix

- Line 240: `(\`docs/architecture.md\`, created when the engine lands)` → `(\`docs/architecture.md\`)`.
- Line 576: `\`docs/architecture.md\` (created when the engine lands) is the navigable reference` →
  `\`docs/architecture.md\` is the navigable reference`.
- Leave line 237 (the `src/…` "created when the engine lands" placeholder) — the engine genuinely isn't built.

### 5F — sync artifacts

`STANDARDS_INDEX.md` § 2 + § 3 add `STANDARDS_LOG.md` (binding? — it's an adopter artifact template;
list under meta/“+” like SETUP) and refresh counts; `documents_manifest.md` add `STANDARDS_LOG` template
+ fix `SET_VERSION_ADOPTED` path; `folder_structure.md` reflect the move + new file; `architecture.md`
§ 10 mark Slice 1 ✅; `CHANGELOG.md` top entry.

## 6. Spec / doc update map

architecture.md § 4/§ 5 already describe this behavior → tick § 10 Slice 1. No behavior contradicts the
doc. (If anything diverges during implementation, fix the doc same-commit per § 4 drift rule.)

## 7. ALLOWLIST

`docs/standards/CLAUDE.md`, `docs/standards/SESSION_OPENER.md`, `docs/standards/SESSION_CLOSER.md`,
`docs/standards/STANDARDS_LOG.md` (NEW), `docs/standards/SETUP.md`, `docs/standards/STANDARDS_INDEX.md`,
`docs/standards/SET_VERSION_ADOPTED.md` (→ moved), `CLAUDE.md` (root), `docs/SESSION_OPENER.md`,
`docs/SESSION_CLOSER.md`, `docs/SET_VERSION_ADOPTED.md` (NEW path), `docs/documents_manifest.md`,
`docs/folder_structure.md`, `docs/architecture.md`, `CHANGELOG.md`, and this plan file.

## 8. Validation gate + QA scenarios (Rule 11)

- **S1 — marker integrity:** `grep -c PROJECT-OWNED:BEGIN` == `grep -c PROJECT-OWNED:END` in every
  edited file; every BEGIN has a matching END; markers are valid HTML comments (invisible in render).
- **S2 — SETUP self-consistency (dry-run):** every file SETUP's strip step names exists in the suite;
  the KEEP set ∪ DELETE set == the current `docs/standards/` contents (no file unaccounted for).
- **S3 — no-names still green:** the PLAN-001 dispositive scrub grep still returns 0 hits.
- Governance scripts exit 0; manifest/folder/INDEX counts consistent.

## 9. Operator-approval decision point

Reply **`APPROVE PLAN-002`**. One open sub-decision (§ 11 D-A): is `STANDARDS_LOG.md` a **binding suite
file** (Tier 1) or an **adopter artifact template** listed under meta? (Affects STANDARDS_INDEX framing
only.)

## 10. Rollback

Local commits on `master`; no remote. Rollback = `git revert` the Phase-3 commit(s). The
`SET_VERSION_ADOPTED` move is a `git mv` — trivially reversible.

## 11. Risks + design decisions

- **D-A (needs your call):** `STANDARDS_LOG.md` classification — binding suite file vs adopter-artifact
  template. **Rec: adopter-artifact template** (it's per-project data, not a rule), listed in
  STANDARDS_INDEX under the “+ SETUP.md” meta line.
- **R1 — markers wrap the wrong span** (e.g., swallow a generic heading). Mitigation: § 5A hugs content,
  leaves headings outside; S1 verifies pairing; implementer diffs each insertion.
- **R2 — strip deletes a kept file** (e.g., a topical file mis-listed). Mitigation: S2's set-cover check
  (KEEP ∪ DELETE == folder contents) before any delete is encoded.
- **R3 — `git mv` of SET_VERSION_ADOPTED leaves stale path refs.** Mitigation: § 5F greps for the old
  path across the repo after the move = 0 hits.

## 12. Acceptance criteria

- `SETUP.md` installs the operative standard, creates the log, writes SVA to `docs/`, and strips the
  machinery (kept/stripped manifest explicit and set-complete).
- `STANDARDS_LOG.md` template exists with schema + legend + example.
- `PROJECT-OWNED` markers wrap exactly the customizable blocks in the 3 templates + 3 adopter instances;
  S1 pairing check passes.
- SVA moved to `docs/`; no stale path refs. Scrub grep still 0. Governance green. Sync artifacts updated.

---

## Senior-review-and-optimize pass (Rule 13) — 2026-06-13

Ran the canonical review prompt against this draft, verified against the real templates.

1. **Anchors verified against source** (not memory): template `CLAUDE.md` §1/§4/§13/§14 = lines
   17/229/564/579; OPENER §2=57, §3.2=105; CLOSER §2=116, §2.2=131; root `CLAUDE.md` architecture refs =
   240 & 576 (and 237 is the `src/` placeholder — correctly excluded from the drift fix). SVA confirmed
   only in `docs/standards/`.
2. **Edge case — set-cover for the strip (R2).** Added S2's explicit check that KEEP ∪ DELETE equals the
   actual `docs/standards/` contents, so a newly-added suite file can never be silently deleted or
   silently kept. This is the highest-risk part of the slice; the check makes it safe.
3. **Markers hug content, not headings** — refined § 5A so headings stay suite-owned (sync may
   re-title/reorder; it only preserves marked bodies). Prevents a whole section freezing.
4. **Strip as a second commit** — chose to make the target's strip a separate commit ("deliver" then
   "strip") so the delivered-then-removed transition is visible in the target's history, not hidden.
5. **Surfaced D-A** (STANDARDS_LOG classification) rather than deciding silently.
6. **Consistency** — ALLOWLIST (§7) reconciled against every file named in §§ 3 + 5; QA (§8) covers each
   change class (markers → S1, strip → S2, names → S3).

No contradictions remain. Plan is internally consistent and ready for Phase 2.
