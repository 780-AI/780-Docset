<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-17 -->
<!-- Status: CLOSED -->
<!--
CHANGE LOG
v1.0 — 2026-06-17 — Phase 3 implemented in a single ALLOWLIST-bounded commit (17 tracked files) + promoted to CLOSED. Shipped Rule 14 (both CLAUDE.md), L050 (both LESSONS), SESSION_OPENER § 1.5 + § 3.1 (both copies), scripts/bootstrap_memory.sh, MEMORY_DURABILITY_ROLLOUT_PROMPT.md, docs/NEW_MACHINE_SETUP.md, Set Version v1.1→v1.2, + manifest/CHANGELOG/folder_structure/SET_VERSION/architecture sync. QA A–G green.
v0.1 — 2026-06-17 — Initial DRAFT + Rule 13 senior-review pass (same session, last task of Phase 1).
DRAFT scope: new binding Rule 14, lesson L050, SESSION_OPENER § 1.5 self-healing pre-flight, a tracked
bootstrap script, an adopter rollout prompt, Set Version v1.1 → v1.2. Sibling tracker: PLAN-005_tracker.md.
Rule 13 pass found + fixed three defects verified against live source: (1) the Set-Version adopter-contract
count was mis-stated as "13 binding files" — live § 1 reads "11 binding files" and the new file is meta, not
binding (fixed 5I to keep binding=11, meta 6→7, total 17→18); (2) Rule 14's drift clause was too strong —
a genuinely new project with no memory yet would have read as a violation (scoped to "unexpectedly empty,
prior sessions known to have written"); (3) the § 7 ALLOWLIST "untracked" note conflated the git-mv pair
and the gitignored OPEN_TASKS edit with the staged set (clarified: 16 staged, git-mv = one item). No new
design decision surfaced beyond DD-1…DD-5 already in § 2.1.
v0.1a — 2026-06-17 — Material revision after the Rule 13 pass (per § 15.8 re-trigger): folded in
deliverable (c) — a project-local re-home checklist `docs/NEW_MACHINE_SETUP.md` (5K) — and recorded the
two environment prerequisites completed this session (§ 2.0: Python 3.11 via uv + SSH key, both verified).
ALLOWLIST 16→17; added QA scenario G (fresh-machine smoke, already green). Focused re-check of the
touched sections (§ 2.0/§ 3/§ 5K/§ 7/§ 8) — consistent; no new design decision; Set-Version file counts
unchanged (the new doc is project-local, not a suite file).
-->

# PLAN-005 — Durable project memory (Rule 14 + L050 + Set Version v1.2)

> **Type:** Major / governance — multiple Critical Files (`CLAUDE.md` ×2, `LESSONS.md` ×2,
> `SESSION_OPENER.md` ×2) + a Set-Version bump. Runs under the § 15 plan workflow.
> **Sibling tracker:** [`PLAN-005_tracker.md`](PLAN-005_tracker.md) (big plan per § 15.7 — multi-file,
> multi-scenario Phase-4 verify, Critical-File edits).
> **Numbering note:** this governance plan takes **PLAN-005**; the engine slices shift —
> `integrate` → PLAN-006 (Slice 4), `sync` → PLAN-007 (Slice 5). `architecture.md` § 10 + `OPEN_TASKS.md`
> are updated in the Phase-3 commit.

---

## 1. Goal

Make the project's Claude memory **survive a machine change and a folder rename/move**, codify the fix
as a binding rule the whole standards suite inherits, and give other adopting projects a paste-in prompt
to set the same thing up.

The durable store + symlink were already established interactively on 2026-06-17 (the immediate fix);
this plan **hardens** it (a forcing-function pre-flight self-heal), **codifies** it (Rule 14 + L050 in
both the operative and canonical copies), **tools** it (a tracked, adopter-deliverable bootstrap
script), and **propagates** it (Set Version v1.2 + a rollout prompt).

---

## 2. Operator constraints & decisions already settled

Settled via operator Q&A this session:

- **D-A — Durability model:** the real memory files live **once**, inside the repo at `./.claude/memory/`
  (Dropbox-synced because the repo is); the harness dir `~/.claude/projects/<key>/memory/` is a
  **symlink** to them. "Memory in both the machine and the project folder" is satisfied by this single
  store (on local disk via the repo, in the repo, in Dropbox) — **no second physical copy**. The repo
  copy is sufficient for the two failure modes that occurred.
- **D-B — No git-tracking of memory content:** `./.claude/memory/` stays **untracked** (Dropbox carries
  it). Git-committing the content is an explicit non-goal here (a one-line opt-in for later if a
  Dropbox-level loss ever needs guarding — out of scope).
- **D-C — Forcing function:** session-start pre-flight (`SESSION_OPENER` § 1) **auto-verifies + self-heals
  + halts-on-empty** (the most aggressive option).
- **D-D — Plan numbering:** this = PLAN-005; engine slices shift to PLAN-006 / PLAN-007.

### 2.0 Environment prerequisites completed this session (2026-06-17 — not plan deliverables)

The audit found two machine-local gaps that blocked full operation on the new machine; both were fixed
interactively (one-time setup, already done) and are **documented** by deliverable (c) so a re-home is
repeatable:

- **Python 3.11+ toolchain** — the machine had only system Python 3.9.6 and a broken Dropbox-carried
  `.venv` (its interpreter was absent). Installed `uv`, then `uv python install 3.11` + a fresh
  `.venv` + `uv pip install -e ".[dev]"`. Verified: engine runs (`standard_document_updater 0.2.0`),
  ruff clean, `mypy --strict` clean (16 files), **35 tests pass**, both governance scripts exit 0.
- **SSH push key** — no `~/.ssh` existed; the SSH remote was unusable. Generated an `ed25519` key,
  operator added the public half to GitLab; `ssh -T git@gitlab.com` → `Welcome … @yaser.khosravi`,
  `git ls-remote origin` confirms repo access (remote tip `9457ac4` = local HEAD).

### 2.1 New design decisions exposed by the audit — surfaced for Phase-2 confirmation (per § 10 / Rule 13.5)

These were decided by the plan author with a stated rationale; the operator confirms or overrides at
Phase 2:

- **DD-1 — Bootstrap script location = `scripts/bootstrap_memory.sh` (tracked), NOT `.claude/`.**
  Rationale: the *content* stays untracked (D-B), but the *tool* must be versioned and delivered to
  adopters (SETUP delivers `scripts/`). The script created interactively at `.claude/bootstrap_memory.sh`
  is **relocated** to `scripts/`; the untracked `.claude/README_memory.md` is updated to point at it.
- **DD-2 — Lesson L050 lands in BOTH lessons files**, each at its own next number (both currently sit at
  L049 → both get L050). `archive/LESSONS.md` gets the real incident; `docs/standards/LESSONS.md` gets the
  genericized mirror. Matches the existing lockstep state of the two files. **No LESSONS.md header bump**
  — both files have carried L043–L049 without per-lesson header bumps (lesson count is tracked via the Set
  Version / STANDARDS_INDEX instead); this plan matches that established practice.
- **DD-3 — The memory-durability failure mode is a UNIVERSAL pattern** → it goes in `SESSION_OPENER` § 3.1
  (universal table) of both copies, not § 3.2 (project-specific), because it is now a suite-wide Rule 14.
- **DD-4 — Rollout prompt = a new canonical-suite file** `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md`
  (Tier-2 meta), manifest-tracked, part of Set v1.2. Rationale: a reusable, versioned artifact other
  projects' operators paste into a Claude Code session.
- **DD-5 — Set Version bump is Minor (v1.1 → v1.2).** Adding a rule + lesson + a meta file is additive
  (§ 5 of STANDARDS_INDEX: "new lessons, new sub-sections, new optional features" = Minor). No binding
  file removed, no structural reorg.

---

## 3. Scope summary

**In scope:** Rule 14 (operative + canonical CLAUDE.md); L050 (archive + canonical LESSONS); SESSION_OPENER
§ 1.5 self-heal + § 4 output line + § 3.1 row (operative + canonical); relocate + version the bootstrap
script; the rollout-prompt file; the project-local re-home checklist `docs/NEW_MACHINE_SETUP.md`
(deliverable (c)); Set Version v1.1 → v1.2 in STANDARDS_INDEX; manifest / CHANGELOG /
SET_VERSION_ADOPTED / folder_structure sync; architecture.md § 10/§ 11 + OPEN_TASKS renumber note; promote
PLAN-005 + tracker to 1.0/CLOSED in the Phase-3 commit.

**Out of scope:** committing memory content to git (D-B); a second physical mirror (D-A); any
SESSION_CLOSER change; reconciling the pre-existing dual-LESSONS / stale-header drift beyond adding L050;
the `integrate`/`sync` engine slices (now PLAN-006/007).

---

## 4. Phase tracker (high-level — granular sub-tasks live in `PLAN-005_tracker.md`)

| Phase | Status | Date |
|---|---|---|
| 0 — Audit | ✅ done | 2026-06-17 |
| 1 — Design (this plan + tracker) | 🔄 in-progress | 2026-06-17 |
| 1.x — Rule 13 senior-review pass | ⏸ pending | — |
| 2 — Operator approval | ⏸ pending | — |
| 3 — Implement (single commit, ALLOWLIST-bounded) | ⏸ pending | — |
| 4 — Validate (scenarios A–F + governance) | ⏸ pending | — |
| 5 — Operator gate (push + Set Version tag `set-v1.2`) | ⏸ pending | — |

---

## 5. Verbatim transformation rules (Phase 3)

> Anchors verified against live source 2026-06-17. The implementer reads each file fresh and applies the
> change at the cited anchor. Where an exact FIND/REPLACE is given, use it verbatim. Mechanical
> bookkeeping (manifest rows, version cells) is described as read-then-edit because line positions shift.

### 5A — `CLAUDE.md` (operative root) — add Rule 14

**Anchor:** line ~229, the last line of Rule 13: `See \`archive/LESSONS.md\` L049 for the incident that
motivated this rule.` followed by a `---` then `## 4. Critical files`. **INSERT the Rule 14 block between
Rule 13's closing line and the `---` that precedes § 4** (i.e., Rule 14 becomes the last rule in § 3).

INSERT:

```markdown

### Rule 14 — Project memory must be durable across machines and folder moves

The Claude memory store MUST live **inside the repository** at `./.claude/memory/` — the single physical copy — with the harness's per-project memory directory (`~/.claude/projects/<sanitized-abs-path>/memory/`) pointed at it via a **symlink**. Because the repository folder is the unit that is version-controlled and/or cloud-synced (Dropbox here), keeping the real memory files inside it means memory travels with the project: it survives a **machine change** (the synced repo carries the content) and a **folder rename/move** (the repo-relative path is stable).

The harness memory path is machine-local and keyed by the folder's absolute path — so it is the one thing that breaks on a move or a new machine. Repair is mechanical and idempotent: `scripts/bootstrap_memory.sh` re-derives the key from the current repo path and (re)creates the symlink. Run it once per machine and after any folder move.

This rule is enforced by a forcing function: `SESSION_OPENER.md` § 1.5 verifies the link resolves and the store is non-empty at every session start, **auto-repairs** a stale/missing link, and **HALTS with a warning** if the store is unexpectedly empty (the signal that memory was lost).

**Only permitted abbreviation:** none — the pre-flight check is cheap and silent when healthy.

**Drift on this rule is a Major defect** — a session that proceeds past an *unexpectedly* empty memory store (one where prior sessions are known to have written memory) without surfacing it to the operator is a rule violation. A genuinely new project with no memory yet is not a violation.

See `archive/LESSONS.md` L050 for the incident that motivated this rule.
```

Then bump the root `CLAUDE.md` header `VERSION: 1.2 → 1.3` and add a CHANGE LOG line:
`v1.3 — 2026-06-17 — Add Rule 14 (durable project memory across machines/folder moves). PLAN-005.`

### 5B — `docs/standards/CLAUDE.md` (canonical template) — add Rule 14 (genericized)

Same anchor (Rule 13 closing line `See \`archive/LESSONS.md\` L049 ...` → `---` → `## 4. Critical files`).
INSERT the **same Rule 14 block as 5A** with two genericizations:

- Replace `(Dropbox here)` with `(e.g. Dropbox / iCloud / a git remote)`.
- Keep the `See \`archive/LESSONS.md\` L050` reference (the template already references `archive/LESSONS.md`
  for Rules 9–13 — match that convention exactly).

Bump `docs/standards/CLAUDE.md` header `VERSION: 1.1 → 1.2` + CHANGE LOG line:
`v1.2 — 2026-06-17 — Add Rule 14 (durable project memory). Standard Set Version v1.2 (PLAN-005).`

### 5C — `archive/LESSONS.md` — add L050 (real incident) + TOC entry

1. **TOC:** under `## Table of Contents` → `## 3. The lessons (newest first)`, add as the FIRST sub-bullet
   (newest first), above the L049 line:
   `- [L050 — Project memory must live inside the synced repo, not the machine-local harness dir](#l050--project-memory-must-live-inside-the-synced-repo-not-the-machine-local-harness-dir)`
2. **Body:** at `## 3. The lessons (newest first)`, INSERT above `### L049` (newest-first):

```markdown
### L050 — Project memory must live inside the synced repo, not the machine-local harness dir

**Date:** 2026-06-17
**Project:** Standard DocSet
**Phase / Task:** Operator-driven binding rule addition (Rule 14)

#### Incident

A new session's pre-flight found the project's entire Claude memory empty — no `MEMORY.md`, no `feedback_*` files — though prior sessions had written several (`feedback_never_change_workflow`, `feedback_plan_handoff_via_open_tasks`, `feedback_pushstate_register_sync`). Investigation: Claude memory lives at `~/.claude/projects/<sanitized-absolute-path>/memory/`, which is (a) **machine-local** — under `~/.claude`, not inside the project folder, so the Dropbox sync that carries the repo never carried it; and (b) **keyed by the folder's absolute path** — so the folder having been renamed/moved (package-name path → `~/Documents/Standard DocSet` → a Dropbox path) minted new keys and orphaned the old memory dir. The development machine had also been replaced, so the old `~/.claude` was gone. Both failure modes hit at once; nothing survived locally — the local session transcripts only *referenced* the slugs (from reading `OPEN_TASKS.md`), with no `Write` calls from which to recover content.

#### Diagnosis

Durable knowledge was kept in a location that was neither version-controlled nor cloud-synced, and whose path was unstable under renames. The project's own governance philosophy — "if it's worth keeping, commit/sync it" (Rule 1) — had a gap: harness memory sat *outside* the synced unit, so it was invisible to both Dropbox and git.

#### Codification

Rule 14: the memory store lives inside the repo at `./.claude/memory/` (rides the same sync as the repo; stable under rename), with the harness dir symlinked to it; `scripts/bootstrap_memory.sh` re-establishes the symlink per machine / after a move; `SESSION_OPENER.md` § 1.5 verifies + self-heals + halts-on-empty as the forcing function. Recovery of the lost content is from the prior machine's `~/.claude` (the only lossless source) or by reconstruction from `OPEN_TASKS.md`.

#### Cross-references

- `CLAUDE.md` § 3 Rule 14 (the binding rule)
- `docs/SESSION_OPENER.md` § 1.5 (the forcing function) + § 3.1 (catalog row)
- `scripts/bootstrap_memory.sh` (the idempotent repair tool)

---
```

(No header bump — see DD-2.)

### 5D — `docs/standards/LESSONS.md` — add L050 (genericized mirror) + TOC entry

Same structure as 5C (TOC bullet + body above `### L049`), genericized:

- `**Project:** a reference project`
- Drop the literal slug names and the literal folder paths; phrase as "the project folder had been
  renamed/moved more than once and the development machine had been replaced."
- Keep the Diagnosis + Codification + Cross-references sections (cross-refs identical: Rule 14,
  SESSION_OPENER § 1.5/§ 3.1, `scripts/bootstrap_memory.sh`).

(No header bump — DD-2.)

### 5E — `docs/SESSION_OPENER.md` (operative) — add § 1.5, § 4 line, § 3.1 row

1. **§ 1.5 (new):** after § 1.4 Memory recall (ends ~line 52) and before the `---` that closes § 1,
   INSERT:

```markdown
### 1.5 Memory-link health (durability check — per CLAUDE.md Rule 14)

Confirm the in-repo memory store is live BEFORE relying on recall (§ 1.4):

```bash
bash scripts/bootstrap_memory.sh                 # idempotent: (re)creates ~/.claude → ./.claude/memory symlink
ls -1 .claude/memory/*.md 2>/dev/null | wc -l    # count stored memories (expect > 0 once memory exists)
```

- If bootstrap reports it **re-created** a stale/missing link → note it in the § 4 block (expected on a new machine or after a folder move).
- If the store is **empty when prior sessions are known to have written memory** → **STOP** and warn the operator in the § 4 block. Memory may have been lost (see Rule 14 + `archive/LESSONS.md` L050); do not proceed as if there is genuinely no history.
```

2. **§ 4 output template:** in the `**Tool + suite state**` block, add a line:
   `- Memory link: <healthy: N files | repaired (new machine / post-move) | EMPTY — operator warned>`
3. **§ 3.1 universal table:** append a row after the current last row (`| 12 | Local-only OPEN_TASKS...`):
   `| 13 | Project memory lost on machine change / folder move | session start; any repo move or new machine | \`CLAUDE.md\` Rule 14 + \`LESSONS.md\` L050 |`

Bump `docs/SESSION_OPENER.md` header `VERSION: 1.2 → 1.3` + CHANGE LOG line.

### 5F — `docs/standards/SESSION_OPENER.md` (canonical) — add § 1.5, § 4 line, § 3.1 row (genericized)

Same three edits as 5E, genericized for the template:

- § 1.5 identical (the commands are repo-relative, so portable as-is).
- § 4: the template's output block (lines ~130–162) has no "Tool + suite state" block; add the
  `- Memory link: ...` line under `**Repo state**`.
- § 3.1: append after the current last row (`| 13 | Behavior-affecting change ... |`):
  `| 14 | Project memory lost on machine change / folder move | session start; any repo move or new machine | \`CLAUDE.md\` Rule 14 + \`LESSONS.md\` L050 |`

Bump `docs/standards/SESSION_OPENER.md` header `VERSION: 1.1 → 1.2` + CHANGE LOG line.

### 5G — `scripts/bootstrap_memory.sh` (relocate + version)

`git mv .claude/bootstrap_memory.sh scripts/bootstrap_memory.sh` (or create at the new path and remove the
old). Content is the script already written this session (idempotent symlink (re)creation, derives the key
from the repo path). Confirm its VERSION header reads `0.1` and the description matches. Update the
untracked `.claude/README_memory.md` to reference `scripts/bootstrap_memory.sh`.

> The script is **tracked** (DD-1) and registered in the manifest (5I). The memory **content** under
> `.claude/memory/` remains untracked (D-B).

### 5H — `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md` (new canonical file)

Create the adopter rollout prompt — a paste-in prompt for another project's Claude Code session that sets
up the same durable memory. Follows `PROMPT_STANDARDS` (explicit ALLOWLIST, verbatim steps, a "files
modified" checklist, no hedges). It instructs the adopter's agent to: create `./.claude/memory/`; add
`scripts/bootstrap_memory.sh` (script body inlined); run it; add Rule 14 to the repo-root `CLAUDE.md`; add
§ 1.5 to `docs/SESSION_OPENER.md`; commit per that project's governance. Full prompt body drafted in
§ 5.1 below.

### 5I — `docs/standards/STANDARDS_INDEX.md` — Set Version v1.1 → v1.2

- **§ 1 block (current text reads `11 binding files + 4 meta files (+ SETUP.md + STANDARDS_LOG.md); 49
  lessons (L001–L049); 13 standing rules`):** `Standard Set Version: v1.1 → v1.2`;
  `Released: 2026-06-13 → 2026-06-17`; binding-file count **unchanged at 11** (the new file is meta, not
  binding); append `+ MEMORY_DURABILITY_ROLLOUT_PROMPT.md` inside the meta parenthetical;
  `49 lessons (L001–L049)` → `50 lessons (L001–L050)`; `13 standing rules` → `14 standing rules`.
- **§ 2:** register `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` as a Tier-2 meta file.
- **§ 3 per-file table:** `CLAUDE.md 1.1 → 1.2`; `SESSION_OPENER.md 1.1 → 1.2`; add row
  `MEMORY_DURABILITY_ROLLOUT_PROMPT.md | Meta | 1.0 | 2026-06-17`; **Total file count line
  `17 (11 binding + 6 meta)` → `18 (11 binding + 7 meta)`**; **Total lesson count 49 → 50**.
  (LESSONS.md row stays 1.0 per DD-2.)
- **§ 6 history:** add a `### v1.2 — 2026-06-17 — Durable project memory (Rule 14)` entry (additive Minor).
- Bump `STANDARDS_INDEX.md` header `VERSION: 1.1 → 1.2` + CHANGE LOG line.

### 5J — bookkeeping (same commit)

- `docs/documents_manifest.md`: add rows for `scripts/bootstrap_memory.sh`,
  `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`, and `docs/NEW_MACHINE_SETUP.md`; bump version cells for root
  `CLAUDE.md` (1.3), canonical
  `CLAUDE.md` (1.2), both `SESSION_OPENER.md` (1.3 / 1.2), `STANDARDS_INDEX.md` (1.2); promote PLAN-005 +
  tracker rows 0.1/DRAFT → 1.0/CLOSED; bump the manifest's own header + quick-index ranges.
- `CHANGELOG.md`: new top entry (Major / governance; Set v1.2; explicit "QA scenarios" sub-section per
  Rule 11 listing A–F).
- `docs/SET_VERSION_ADOPTED.md`: record adoption of **v1.2**; bump header.
- `docs/folder_structure.md`: add `.claude/memory/` (untracked store) + `scripts/bootstrap_memory.sh`;
  bump header.
- `docs/architecture.md` § 10 + § 11 and `docs/Plans/OPEN_TASKS.md`: renumber engine slices
  (`integrate` → PLAN-006, `sync` → PLAN-007); architecture bump.
- Promote this plan + tracker to `1.0` / `CLOSED` (header Status + manifest rows) in the same commit.

### 5K — `docs/NEW_MACHINE_SETUP.md` (new, project-local) — the re-home checklist (deliverable (c))

Create a project-local operational doc (NOT a canonical-suite file → does not change the Set Version file
count) capturing the exact steps to re-home this vault on a new machine, derived from what was done
2026-06-17 (§ 2.0):

1. Sync/clone the repo (Dropbox carries it, incl. `.claude/memory/` + `.git`).
2. **Python:** install `uv` (`curl -LsSf https://astral.sh/uv/install.sh | sh`); `uv python install 3.11`;
   `rm -rf .venv && uv venv --python 3.11 .venv`; `uv pip install -e ".[dev]"`. (Do **not** trust a
   Dropbox-carried `.venv` — venvs are machine-specific; rebuild it. Ideally keep `.venv` out of the
   synced path.)
3. **SSH:** `ssh-keygen -t ed25519 -C "<email>" -f ~/.ssh/id_ed25519`; add `~/.ssh/id_ed25519.pub` to
   GitLab → Settings → SSH Keys; verify `ssh -T git@gitlab.com`.
4. **Memory:** `bash scripts/bootstrap_memory.sh` (re-creates the harness → `./.claude/memory` symlink).
5. Run the `docs/SESSION_OPENER.md` § 1 pre-flight (which now includes § 1.5 memory-link health).

Header: `<!-- VERSION: 1.0 -->` + the standard one-line description. Cross-reference Rule 14 +
`scripts/bootstrap_memory.sh`.

### 5.1 — Full body of `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`

```markdown
<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-17 -->
<!-- Source: standards-source/ (canonical). Added under Standard Set Version v1.2. -->

# Memory-durability rollout prompt (paste into a Claude Code session)

**Purpose:** make this project's Claude memory survive a machine change and a folder rename/move, per the
standards suite's `CLAUDE.md` Rule 14. Paste the block below into a fresh Claude Code session opened in
the project's root directory.

---

> Set up durable Claude memory for THIS repository, per Standard DocSet Rule 14.
>
> ALLOWLIST — you may touch ONLY these paths; if anything else appears in `git status`, STOP and report:
> - `scripts/bootstrap_memory.sh` (create)
> - `CLAUDE.md` (add Rule 14)
> - `docs/SESSION_OPENER.md` (add § 1.5 + § 3.1 row)
> - `.claude/memory/` (create dir — leave untracked)
> - `.claude/README_memory.md` (create — untracked)
> - your manifest / CHANGELOG per this project's governance
>
> Steps:
> 1. Create `scripts/bootstrap_memory.sh` with the body the suite ships (idempotent: derive the harness
>    key from the repo's absolute path — `'/'`→`'-'`, `' '`→`'-'` — and (re)create the symlink
>    `~/.claude/projects/<key>/memory → <repo>/.claude/memory`, preserving any pre-existing files).
> 2. `mkdir -p .claude/memory` and run `bash scripts/bootstrap_memory.sh`; paste its output.
> 3. Add Rule 14 to the repo-root `CLAUDE.md` (copy the text from the suite's `docs/standards/CLAUDE.md`
>    Rule 14, adjusting the sync-tool name in parentheses to this project's reality).
> 4. Add `§ 1.5 Memory-link health` to `docs/SESSION_OPENER.md` (copy from the suite) + the § 3.1 row.
> 5. Confirm `.claude/` is NOT gitignored (so the memory content rides the project's sync) but that you
>    are NOT committing the memory content unless this project opts into git-tracking it.
> 6. Run this project's governance + code review, then commit per its rules.
>
> Files modified this session — enumerate them and reconcile against `git status`; raise any mismatch.

---

**Recovery note:** if memory was already lost before this rollout, the only lossless source is the prior
machine's `~/.claude/projects/<old-key>/memory/`. Copy those `.md` files into `./.claude/memory/` (they go
live immediately through the symlink). Otherwise reconstruct from whatever the project committed/synced.
```

---

## 6. Spec update map

| Spec / doc | Update | Trigger |
|---|---|---|
| `CLAUDE.md` (×2) | Rule 14 added | new binding rule |
| `LESSONS.md` (×2) | L050 added | new incident-to-rule |
| `SESSION_OPENER.md` (×2) | § 1.5 + § 4 line + § 3.1 row | new pre-flight step + catalog row |
| `STANDARDS_INDEX.md` | Set v1.2; per-file + counts; § 6 history | Set-Version bump (§ 5 of the index) |
| `SET_VERSION_ADOPTED.md` | adopts v1.2 | this repo adopts its own bump |
| `documents_manifest.md` | new files + version cells + plan promotion | Rule 8 |
| `folder_structure.md` | `.claude/memory/` + `scripts/bootstrap_memory.sh` | new tracked + untracked paths |
| `NEW_MACHINE_SETUP.md` (new, project-local) | re-home checklist | deliverable (c) |
| `architecture.md` / `OPEN_TASKS.md` | engine-slice renumber | DD-4 / D-D |
| `CHANGELOG.md` | top entry + QA sub-section | every commit (Rule 11) |

---

## 7. ALLOWLIST (Phase 3 — the bullet enumeration IS the count: 17 tracked + 2 untracked)

Tracked (in the git commit):
1. `CLAUDE.md`
2. `docs/standards/CLAUDE.md`
3. `archive/LESSONS.md`
4. `docs/standards/LESSONS.md`
5. `docs/SESSION_OPENER.md`
6. `docs/standards/SESSION_OPENER.md`
7. `scripts/bootstrap_memory.sh` (relocated from `.claude/`)
8. `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md` (new)
9. `docs/standards/STANDARDS_INDEX.md`
10. `docs/documents_manifest.md`
11. `CHANGELOG.md`
12. `docs/SET_VERSION_ADOPTED.md`
13. `docs/folder_structure.md`
14. `docs/architecture.md`
15. `docs/NEW_MACHINE_SETUP.md` (new — deliverable (c))
16. `docs/Plans/PLAN-005_durable_memory.md` (this plan → 1.0/CLOSED)
17. `docs/Plans/PLAN-005_tracker.md` (→ 1.0/CLOSED)

The 17 numbered files are the complete staged set. Touched but NOT staged (so they will NOT appear in
`git status` as staged, and that is expected): `.claude/memory/` and `.claude/README_memory.md`
(untracked, Dropbox-only — the README updated to point at `scripts/bootstrap_memory.sh`), and
`docs/Plans/OPEN_TASKS.md` (gitignored — edited for the slice renumber).

Any **tracked** path outside the 17 appearing staged in `git status` → STOP and report (Rule 7). The
`git mv` of the bootstrap script shows as one delete (`.claude/bootstrap_memory.sh`) + one add
(`scripts/bootstrap_memory.sh`) — that pair is item 7, not an extra file.

---

## 8. Validation gate (Phase 4 — QA scenarios per Rule 11)

| ID | What to verify | How | Pass criteria |
|---|---|---|---|
| A | Bootstrap is idempotent | run `bash scripts/bootstrap_memory.sh` twice | both exit 0; second run reports the link already correct; no error |
| B | Self-heal after a "move" | `rm` the symlink, run bootstrap | link re-created; `ls -ld` shows it → `./.claude/memory`; store files intact |
| C | Write-through | `touch` a file via the harness path | appears in `./.claude/memory/` |
| D | Empty-store halt wording | dry-read § 1.5 logic against an empty store | the documented STOP/warn path is unambiguous (no hedge) |
| E | Governance | `python scripts/check_doc_coverage.py` + `python scripts/check_test_coverage_drift.py --ci` | both exit 0 (paste stdout) |
| F | Set-Version consistency | grep Set Version across STANDARDS_INDEX § 1/§ 3/§ 6 + SET_VERSION_ADOPTED | all read v1.2; counts 18 files / 50 lessons / 14 rules |
| G | Toolchain on this machine (re-home) | rebuilt env per `NEW_MACHINE_SETUP.md` | ✅ already verified 2026-06-17: engine `0.2.0`, ruff clean, mypy --strict clean (16 files), 35 tests pass, governance exit 0, SSH push reachable |

(No new Python tests — the bootstrap is a shell tool exercised by A–C; `validation_ownership.toml` covers
only `src/`, matching the existing governance scripts which carry no ownership entry. Scenario G is the
fresh-machine smoke and is already green — it documents the § 2.0 setup outcome.)

---

## 9. Operator approval decision point (Phase 2)

Approve as **D5.A** to implement as drafted, or specify deltas. Items most worth an explicit nod:
**DD-1** (script → `scripts/`, tracked), **DD-4** (rollout prompt as a new canonical file), **DD-5**
(Minor bump v1.2). No code is touched until approval lands.

---

## 10. Rollback path

All edits are additive text + one `git mv`. Rollback = `git revert` the single Phase-3 commit; the
durable store + symlink (already live, untracked) are unaffected by a revert. The Set Version returns to
v1.1; no adopter has consumed v1.2 yet.

---

## 11. Known risks

| # | Risk | Mitigation | Status |
|---|---|---|---|
| R1 | `git mv` of the bootstrap script leaves a dangling `.claude/README_memory.md` reference | 5G updates the README same-step | open |
| R2 | A future `sync` (PLAN-007) overwrites a project's Rule 14 / § 1.5 customizations | Rule 14 + § 1.5 are suite-owned (whole-file/section-merge) — not in PROJECT-OWNED blocks; document in PLAN-007 | open (PLAN-007) |
| R3 | Symlink semantics differ on Windows/WSL adopters | script + rule are macOS/Linux-targeted (project is darwin); note the limitation in the rollout prompt | open |
| R4 | The pre-flight auto-run of bootstrap surprises an operator who moved the folder deliberately | bootstrap is silent/idempotent when healthy; only acts on a stale link; § 1.5 notes the repair in § 4 | mitigated |

---

## 12. Acceptance criteria

- Rule 14 present in both `CLAUDE.md` copies; L050 in both `LESSONS.md` copies; § 1.5 + § 3.1 row +
  § 4 line in both `SESSION_OPENER.md` copies.
- `scripts/bootstrap_memory.sh` tracked + manifest-registered; `.claude/memory/` untracked.
- `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` present + registered; Set Version reads **v1.2** consistently
  (18 files / 50 lessons / 14 rules) across STANDARDS_INDEX + SET_VERSION_ADOPTED.
- QA A–F pass; both governance scripts exit 0.
- Engine slices renumbered (integrate → PLAN-006, sync → PLAN-007) in architecture.md + OPEN_TASKS.
- PLAN-005 + tracker promoted to 1.0/CLOSED in the Phase-3 commit; manifest rows match.
