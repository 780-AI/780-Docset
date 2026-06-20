# CHANGELOG

Newest entries at the top.

## [2026-06-20] — MEMORY_DURABILITY_ROLLOUT_PROMPT.md step-5 reconciled with Rule 14 (gitignore .claude/)

- **Type:** Major (edits `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md`, a Critical File) — wording
  fix only. **No Set-Version bump** (the Rule 14 capability is unchanged); `STANDARDS_INDEX` untouched.
- **What:** the rollout prompt's step 5 said "Confirm `.claude/` is NOT gitignored." That predated the
  settled practice (this session's quick win + `SETUP.md` Step 6.5 + `NEW_PROJECT_BOOTSTRAP.md` Step 8):
  **`.claude/` IS gitignored** so the store stays untracked + sync-carried *and* a stray `git add -A`
  can never accidentally commit it. Rewrote step 5 accordingly and added `.gitignore` to the prompt's
  ALLOWLIST. Added a CHANGE LOG block to the file (it previously had none).
- **Versions:** `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` 1.0→1.1; `documents_manifest.md` entry 57 1.0→1.1,
  header 2.7→2.8.
- **Impact:** none at runtime; the three delivery docs (SETUP, NEW_PROJECT_BOOTSTRAP, this rollout prompt)
  are now mutually consistent on the gitignore stance. **QA scenarios:** Rule 11 exempt (governance doc).

## [2026-06-20] — NEW_PROJECT_BOOTSTRAP.md caught up to Set Version v1.3 (closes the SETUP parity gap)

- **Type:** Major (edits `docs/standards/NEW_PROJECT_BOOTSTRAP.md`, a Critical File) — walkthrough/doc
  only. **No Set-Version bump** (the v1.3 suite content is unchanged; the long-form walkthrough was just
  behind). `STANDARDS_INDEX` untouched per its rule; the manifest carries the live version.
- **What:** rewrote the Day-Zero walkthrough to full **v1.3 step-parity with `SETUP.md`** (it is the
  long-form companion to that one-shot prompt — now stated explicitly, with a "keep the two in
  step-parity" note). Closed the long-standing parity gap:
  - added the project-local **SESSION_OPENER/CLOSER instantiation** (Step 2), the **experiences-log**
    (`docs/STANDARDS_LOG.md`) create step (Step 4), **Step 8 durable memory (Rule 14)**, and
    **Step 10.5 strip-the-machinery** (with the 6-KEEP / 12-DELETE set-cover matching SETUP.md);
  - retargeted every `v1.1` → `v1.3`; corrected stale counts ("9 standing rules" → **14**,
    "10 binding files" → **11**); added `.claude/` + `docs/Plans/OPEN_TASKS.md` to the `.gitignore`;
    updated the end-state tree, the TOC, and the bootstrap commit message.
- **Versions:** `docs/standards/NEW_PROJECT_BOOTSTRAP.md` 1.1→1.2; `documents_manifest.md` entry 24
  1.1→1.2, header 2.6→2.7.
- **Impact:** no runtime/engine impact; affects only the by-hand bootstrap walkthrough. **QA scenarios:**
  Rule 11 exempt (walkthrough doc). The dispositive check is a live bootstrap (the "SETUP.md end-to-end"
  pending-verification item — now covers both SETUP.md and this walkthrough).
- **Remaining (flagged):** `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` step-5 wording ("not gitignored") is
  still superseded by the Step-8 gitignore stance — a one-line reconcile logged for a future docs pass.

## [2026-06-20] — SETUP.md installer caught up to Set Version v1.3 (durable-memory turn-key)

- **Type:** Major (edits `docs/standards/SETUP.md`, a Critical File) — installer/doc only. **No
  Set-Version bump:** the v1.3 suite *content* is unchanged; only the bootstrap installer was stale
  (left at v1.1 across the v1.2/v1.3 releases). `STANDARDS_INDEX` untouched per its own rule (it bumps
  only at Set-Version releases; the manifest carries the live SETUP.md version).
- **What:** brought `SETUP.md` current so a fresh bootstrap delivers v1.3 turn-key:
  - retargeted every `v1.1` reference to `v1.3` (intro, prompt header, Step 4 CLAUDE.md Source line,
    Step 5 `SET_VERSION_ADOPTED.md`) — a new project now records **v1.3 adopted**, not v1.1;
  - added **Step 6.5 — durable memory (Rule 14)**: create `scripts/bootstrap_memory.sh` + `.claude/memory/`
    + the harness symlink (per `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`), and `.claude/` added to the Step 5
    `.gitignore`;
  - registered `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` in the Step 1 pre-flight check, the Step 3 lay-down,
    and the Step 8.5 strip DELETE list — **fixing the strip set-cover**, which the v1.2 file had silently
    left at 17 of 18 (KEEP 6 + DELETE 12 = 18 ✓).
- **Versions:** `docs/standards/SETUP.md` 1.1→1.2; `documents_manifest.md` entry 26 1.1→1.2, header 2.5→2.6.
- **Impact:** no runtime/engine impact; affects only how a *new* project is bootstrapped. **QA scenarios:**
  Rule 11 exempt (governance/installer doc, no observable CLI/engine behavior change). Live verification is
  the next real bootstrap (the long-standing "SETUP.md end-to-end" pending-verification item).
- **Remaining gap (flagged, not closed here):** `NEW_PROJECT_BOOTSTRAP.md` (the click-through walkthrough)
  still lacks the strip + log + durable-memory steps and the v1.3 retarget; and
  `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` step-5 wording ("not gitignored") is now superseded by Step 6.5.

## [2026-06-20] — Standard Set Version v1.3: lesson L051 (Rule 13 must run the tools)

- **Type:** Major (edits the canonical `docs/standards/` suite, a Critical File) — doc/governance only,
  **Set Version bump v1.2 → v1.3**. Additive Minor at the suite level: no existing rule changed (Rule 13's
  expectations are sharpened, not rewritten); adopters may backport or stay on v1.2.
- **What:** Codified **L051** — the Rule 13 senior-review-and-optimize pass MUST mechanically run the
  linter + type-checker + tests against the EXACT code a plan commits in its § 5 transformation rules
  (not eyeball it); the fix MUST be reflected in § 5 itself (not only narrated in the CHANGE LOG); and the
  recorded result MUST name the specific lines / checks fixed. Motivated by the same defect class (ruff
  `E501`/`UP042`, `mypy --strict`) recurring across **three consecutive plans** (PLAN-003/004/006), each
  time "claimed caught" by the Rule 13 pass but actually shipped to Phase 3.
  - Lesson written into both copies: `docs/standards/LESSONS.md` (genericized, domain-neutral) +
    `archive/LESSONS.md` (project-specific, citing the three recurrences).
  - New `SESSION_OPENER.md` § 3.1 universal catalog row in both the project copy (`docs/SESSION_OPENER.md`,
    row 14) and the template (`docs/standards/SESSION_OPENER.md`, row 15).
- **Versions:** project `SESSION_OPENER.md` 1.3→1.4; template `SESSION_OPENER.md` 1.2→1.3;
  `STANDARDS_INDEX.md` 1.2→1.3 (Set Version + counts + § 6 history; also corrected the stale "as of v1.1"
  § 3 caption and the self-row to current); `SET_VERSION_ADOPTED.md` 1.3→1.4 (adopt v1.3 + backport row);
  manifest 2.3→2.4. **LESSONS file headers unchanged** (no-per-lesson-bump practice; the count is tracked
  in STANDARDS_INDEX/SET_VERSION_ADOPTED). Lesson count 50 → 51 (L001–L051).
- **Impact:** No runtime/behavior impact — governance/process documentation only. **QA scenarios:** Rule 11
  exempt (lessons-archive addition + governance-doc edit, no observable CLI/engine behavior change).

## [2026-06-20] — CLAUDE.md § 4 Critical-files cleanup

- **Type:** Major (edits `CLAUDE.md`, a Critical File) but **doc-only** — no behavior change, no Set
  Version bump. Project-specific (root operating-contract copy only; the template's generic § 4 is
  untouched).
- **What:**
  - Dropped the stale "(created when the engine lands)" note on the `src/standard_document_updater/`
    Critical-File entry — the engine package has existed since PLAN-003.
  - **Promoted `config/projects.toml` to a Critical File.** It is the target-suite registry — it defines
    which repos the tool reads/writes; a silent edit could redirect a write to the wrong repo (the
    highest-cost mistake per `docs/SESSION_OPENER.md` § 2). Editing it is now always Major.
  - Reworked the "Future critical files" list accordingly (config/schema bullet folded into the now-active
    `config/projects.toml` entry).
- **Versions:** root `CLAUDE.md` 1.3→1.4 (header + CHANGE LOG); `docs/documents_manifest.md` entry 1
  1.3→1.4, manifest header 2.2→2.3. `config/projects.toml` is not manifest-tracked (Rule 8 covers `.md`
  + VERSION-headed `.py`/`.sh`; a `.toml` config file is neither) and carries no VERSION header.
- **Impact:** No runtime/behavior impact. **QA scenarios:** Rule 11 exempt (governance-doc edit, no
  observable CLI/engine behavior change).

## [2026-06-18] — PLAN-006 (Slice 4): `integrate` (worksheet + status write-back)

- **Type:** Major / New module — executed under the § 15 plan workflow (PLAN-006, Phase 3). New engine
  code under `src/standard_document_updater/` (a Critical File per `CLAUDE.md` § 4), one mode of which
  **writes to target repos**.
- **What:** Landed the `integrate` command — the deterministic half of the harvest → **integrate** → sync
  loop (architecture § 6c). **A1 division of labor:** the tool is the deterministic spine; the
  genericization, the `L0NN` lesson prose, and the vault edits (LESSONS / topical / Set Version) are
  authored by Claude **in-session** under the § 15 flow — the tool never calls a model and never edits the
  vault.
  - `python -m standard_document_updater integrate` — prints a **read-only worksheet**: every open
    experiences-log entry enriched with its Area→topical routing (unknown/empty Area → `PROJECT_STANDARDS.md`
    + a visible `⚠ unrouted` flag), a proposed **sequential `L0NN`** (vault `max + 1`), and the current Set
    Version. Always exit **0** (informational, like `harvest`/`status`).
  - `integrate --apply <decisions.toml>` — operator-gated **Status write-back**. Default is a **dry-run**
    diff; `--write` actually writes. Validates every disposition first (no partial writes), re-reads each
    target log immediately before writing (architecture § 9), and rewrites **only** the matched `Status:`
    line of the named entry, leaving the rest byte-identical. Errors (exit 2, nothing written) on an unknown
    project or an unresolvable entry.
  - New src module `integrate.py` (Area routing, next-`L0NN`, worksheet render, decisions-TOML parse,
    atomic write-back) with its own `IntegrateError`. New test module `test_integrate.py` (20 unit tests:
    routing / next-`L0NN` / worksheet / decisions parse / write-back atomicity) + 2 `integrate` CLI tests in
    `test_cli.py`. `cli.py`/`__init__.py` 0.2→0.3; soft `[rules.integrate]` ownership-map entry.
- **Impact:** Building the tool is **read-only on the vault** — **no Set Version change** (no `docs/standards/`
  file touched → suite stays **v1.2**). The only target-repo write is the explicit, operator-gated
  `integrate --apply … --write`, a separate later action (not part of building the tool). **CI unchanged**
  (`.gitlab-ci.yml` not touched). `architecture.md` § 8/§ 10 mark integrate implemented and § 11 resolves
  the last OPEN decision (genericization hands off to a Claude session — A1).
- **QA scenarios (Rule 11):** scenarios A–K tracked in `docs/Plans/PLAN-006_tracker.md` Phase 4 —
  A (ruff clean), B (mypy --strict, 18 files), C (full pytest, 57 green), D (both governance scripts exit 0),
  E (worksheet, empty registry → "No open entries…", exit 0), F (worksheet content — project/entry/area→topical,
  proposed `L0NN`, Set Version), G (Area routing — each Area → file; unknown → `PROJECT_STANDARDS.md` +
  `⚠ unrouted`), H (next-`L0NN` against the real `LESSONS.md` → `L051`), I (write-back dry-run — no file
  modified), J (write-back `--write` — only the named `Status:` line changes, rest byte-identical),
  K (write-back safety — unknown project / missing entry → `IntegrateError`, exit 2, no file written).
  E–K exercised both by the pytest suite and live via the CLI against a throwaway fixture (operator-run);
  A–D operator-run.
- **Plan-defect resolution (mechanical, during Phase 3):** D1 — the verbatim § 5A code shipped 5 `E501`
  over-length lines (`next_lesson_id` read-text comprehension, the worksheet footer's 4 adjacent literals,
  and the integrated-Status f-string) that the Rule 13 pass's claimed reflow did not fully catch (the same
  recurring `E501` class as PLAN-003 D2 / PLAN-004 D1). Reflowed all five **output-preserving** — the
  worksheet footer verified byte-identical via SHA-256 before/after (len 345, unchanged); the Status
  f-string re-confirmed by `test_parse_decisions_integrated_and_rejected`. Recorded in the PLAN-006 CHANGE
  LOG + § 11. Additionally, `architecture.md` § 11 (an OPEN decision the plan's § 5D under-specified but
  whose own text mandated resolution at this slice) was marked DECIDED same-commit.

## [2026-06-17] — PLAN-005: durable project memory (Rule 14 + Standard Set Version v1.2)

- **Type:** Major / governance — multiple Critical Files (`CLAUDE.md` ×2, `LESSONS.md` ×2,
  `SESSION_OPENER.md` ×2) + a Set-Version bump. Executed under the § 15 plan workflow (PLAN-005).
- **What:**
  - **Rule 14** added to the operating contract (operative + canonical `CLAUDE.md`): the Claude memory
    store lives inside the repo at `./.claude/memory/` with the harness memory dir symlinked to it, so
    memory survives a machine change and a folder rename/move; repaired idempotently by
    `scripts/bootstrap_memory.sh`.
  - **`SESSION_OPENER.md` § 1.5** (operative + template): a session-start memory-link health check that
    verifies the link, auto-repairs a stale/missing one, and HALTS-on-empty (forcing function) + a § 3.1
    catalog row.
  - **L050** added to both `LESSONS.md` copies — the 2026-06-17 memory-loss incident (harness memory was
    machine-local + path-keyed, so a machine change + folder move wiped it; recovered losslessly from a
    Dropbox backup of the prior machine's `~/.claude`).
  - New tracked tooling `scripts/bootstrap_memory.sh`; new adopter `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`;
    new project-local `docs/NEW_MACHINE_SETUP.md` (re-home checklist).
  - **Standard Set Version v1.1 → v1.2** (additive Minor) — STANDARDS_INDEX § 1/§ 2/§ 3/§ 6 + counts
    (18 files / 50 lessons / 14 rules); SET_VERSION_ADOPTED records adoption; manifest + folder_structure
    synced; engine slices renumbered (integrate → PLAN-006, sync → PLAN-007).
- **Impact:** Governance + tooling only — **no engine behavior change**. The durable store + symlink were
  established interactively the same day; this commit codifies + hardens + propagates them. The memory
  **content** stays untracked (Dropbox-carried); only the bootstrap tooling is committed.
- **QA scenarios (Rule 11):** A–G in `docs/Plans/PLAN-005_tracker.md` Phase 4 — A (bootstrap idempotent),
  B (self-heal after symlink removal), C (write-through), D (empty-store halt wording), E (governance
  exit 0), F (Set-Version consistency v1.2 / 18 / 50 / 14), G (fresh-machine toolchain smoke — verified
  2026-06-17: engine 0.2.0, ruff + mypy --strict + 35 tests + governance green, SSH push reachable).

## [2026-06-16] — PLAN-004 (Slice 3): `harvest` (consolidate open experiences-log entries)

- **Type:** Major / New module — executed under the § 15 plan workflow (PLAN-004, Phase 3). New engine
  code under `src/standard_document_updater/` (a Critical File per `CLAUDE.md` § 4).
- **What:** Landed the read-only `harvest` command:
  - `python -m standard_document_updater harvest` — reads **every registered project's**
    `docs/STANDARDS_LOG.md`, collects the entries whose `Status` is `open`, and prints a **consolidated
    report grouped by area** to stdout; always exit **0** (informational, like `status` — not a gate).
  - Conservatively flags likely cross-project duplicates (D3): two open entries are flagged only when
    their *normalized titles match* AND they come from *different* projects (`⚠ possible duplicate of
    <project>/<E0NN>`). Same-project repeats and distinct titles are not flagged.
  - 2 new src modules — `logentry.py` (parse a `STANDARDS_LOG.md` into `LogEntry` records; controlled-vocab
    fields reduce a status write-back like `integrated → vault L050` to `integrated` so it is correctly
    not-open) and `harvest.py` (pure render: collect → group-by-area → cautious dup flag, no filesystem).
  - 2 new test modules (`test_logentry.py`, `test_harvest.py`) + 2 harvest CLI tests in `test_cli.py`;
    `cli.py`/`__init__.py` 0.1→0.2; soft ownership-map entries for `logentry`/`harvest`.
- **Impact:** **Read-only** — writes nothing (not to any target, not to disk; the source logs are the
  durable record per D1). **No Set Version change** (no `docs/standards/` file touched → suite stays
  **v1.1** — the engine reads the log, it does not alter the suite). **CI unchanged** (`.gitlab-ci.yml`
  not touched — "stay small"). `--json` deferred (D2); `setversion.count_open_log_entries` DRY-delegation
  to `logentry.parse_log` deferred (plan § 11 DD-1, logged to OPEN_TASKS).
- **QA scenarios (Rule 11):** scenarios A–H tracked in `docs/Plans/PLAN-004_tracker.md` Phase 4 —
  A (empty registry → "No open log entries…", exit 0), B (one project, 2 open entries listed, exit 0),
  C (status write-back excluded — `is_open` False), D (cross-project same-title flagged both ways),
  E (same-project same-title not flagged), F (distinct titles not flagged), G (grouping across ≥2 areas,
  sorted), H (ruff + mypy --strict + full pytest green; both governance scripts exit 0). B–G are covered
  by the pytest suite; A, B, C, D, G also exercised live via the CLI; H operator-run.
- **Plan-defect resolution (mechanical, during Phase 3):** D1 — the verbatim § 5B report-append line was
  103 cols (ruff `E501`); reflowed to a wrapped `lines.append(...)` call. Production output is
  byte-identical; recorded in the PLAN-004 CHANGE LOG.
- **Version bumps:** new files `logentry.py`/`harvest.py`/`test_logentry.py`/`test_harvest.py` at v0.1;
  `cli.py` 0.1→0.2, `__init__.py` 0.1→0.2 (CLI version 0.1.0→0.2.0), `test_cli.py` 0.1→0.2;
  `architecture.md` 0.4→0.5, `folder_structure.md` 0.6→0.7, `documents_manifest.md` 1.7→1.8 (entries
  50–53); PLAN-004 + tracker promoted 0.1→1.0/CLOSED.
- **Author:** Yaser Khosravi

## [2026-06-16] — PLAN-003 (Slice 2): registry + `status` / `drift` (first engine code)

- **Type:** Major / New module — executed under the § 15 plan workflow (PLAN-003, Phase 3). First Python
  engine code under `src/standard_document_updater/` (a Critical File per `CLAUDE.md` § 4).
- **What:** Landed the vault-side managed-projects registry plus two read-only commands:
  - `python -m standard_document_updater status` — table of every registered project (adopted vs vault
    Set Version, state, open-log count); always exit 0.
  - `python -m standard_document_updater drift` — only projects **not** on the vault Set Version; exits
    **1** if any exist (`behind`, `ahead`, **and** `unknown` all count as drift).
  - Registry `config/projects.toml` stores **name + path only**; a project's adopted Set Version is read
    **live** from its `docs/SET_VERSION_ADOPTED.md` at report time (single source of truth, never cached).
  - 7 src modules (`__init__`, `__main__`, `errors`, `registry`, `setversion`, `report`, `cli`) +
    `pyproject.toml` (setuptools src-layout; ruff / mypy-strict / pytest config) + a pytest suite
    (`conftest` + 4 test modules) + a soft ownership-map entry in `scripts/validation_ownership.toml`.
- **Impact:** **Read-only** — no command in this slice writes to any target repo. **No Set Version
  change** (no `docs/standards/` file touched → suite stays **v1.1**). **CI unchanged** (`.gitlab-ci.yml`
  not touched — the `test` stage is deferred to a later slice per the plan's "stay small" constraint).
- **QA scenarios (Rule 11):** scenarios A–I tracked in `docs/Plans/PLAN-003_tracker.md` Phase 4 —
  A (empty registry → "No projects registered", exit 0), B–C (status current/behind), D–E (drift exit
  0/1), F (unknown counts as drift), G (open-log count), H (pytest + mypy --strict + ruff green),
  I (governance scripts exit 0). B–G are covered by the pytest suite; A, H, I are operator-run smokes.
- **Version bumps:** new engine files at v0.1; `folder_structure.md` 0.5→0.6, `architecture.md` 0.3→0.4,
  `documents_manifest.md` 1.5→1.6 (registered entries 36–47); PLAN-003 + tracker promoted 0.1→1.0/CLOSED.
- **Author:** Yaser Khosravi

## [2026-06-14] — Project renamed to "Standard DocSet"

- **Type:** Major / Identity (Critical-file edit: `CLAUDE.md` § 1)
- **What:** Renamed the project's display name `standard-document-updater` → **"Standard DocSet"** (Option B —
  display/identity only). Updated root `CLAUDE.md` § 1, `README`, `docs/README`, the project-local
  `SESSION_OPENER`/`SESSION_CLOSER`, `SET_VERSION_ADOPTED`, `architecture`, `folder_structure`, and the
  `.gitlab-ci.yml` header comment. The Python engine package identifier `standard_document_updater`
  (`src/standard_document_updater/`) is **deliberately unchanged** — it can be renamed when the engine lands.
- **Remote:** the GitLab project was renamed (name "Standard DocSet", path slug `standard-docset`); local
  `origin` re-pointed to `git@gitlab.com:yaser.khosravi/standard-docset.git`.
- **Not changed:** the historical `PLAN-001` record keeps the old name (it documents the state at that time).
  The local folder rename (`~/Documents/Standard document updater` → `Standard DocSet`) is handled separately.
- **Impact:** No runtime impact (identity/display only).
- **Version bumps:** CLAUDE.md 1.1→1.2, SESSION_OPENER 1.1→1.2, SESSION_CLOSER 1.1→1.2,
  SET_VERSION_ADOPTED 1.1→1.2, architecture 0.2→0.3, folder_structure 0.4→0.5, documents_manifest 1.3→1.4.
- **Author:** Yaser Khosravi

## [2026-06-13] — PLAN-002 (Slice 1): setup-and-strip + experiences log + PROJECT-OWNED markers (Set Version v1.1)

- **Type:** Major / Governance / Critical-file edit (`docs/standards/`, `CLAUDE.md`) — executed under the
  § 15 plan workflow (PLAN-002, Phase 3).
- **What:** Made the architecture's footprint + non-clobbering-sync model real at the document layer:
  (a) added the **experiences-log template** `docs/standards/STANDARDS_LOG.md` (the per-project
  contribution channel fed by `SESSION_CLOSER` § 1.7); (b) wrapped the project-customizable blocks of
  `CLAUDE.md` (§ 1/§ 4/§ 13/§ 14), `SESSION_OPENER` (§ 2/§ 3.2), and `SESSION_CLOSER` (§ 2.2) — in **both**
  the templates and this repo's adopter instances — in **`PROJECT-OWNED` markers** so a future `sync`
  preserves them; (c) reworked `SETUP.md` into **setup-and-strip** (create the log, write
  `SET_VERSION_ADOPTED` to `docs/`, then strip the setup machinery as a second commit, with a set-cover
  safety check); (d) **moved** `SET_VERSION_ADOPTED.md` from `docs/standards/` → `docs/` so it survives the
  strip; (e) fixed the stale "created when the engine lands" drift on the two `docs/architecture.md`
  references in root `CLAUDE.md`.
- **Set Version:** bumped the canonical suite **v1.0 → v1.1** (additive Minor) per `architecture.md` § 9
  ("every change to the suite bumps per-file VERSION + the Set Version"); this repo adopts v1.1 same-commit.
- **Plan-defect resolutions (operator-approved during Phase 3):** D1 — corrected the strip DELETE list to
  11 files (dropped `SET_VERSION_ADOPTED`, which the move removes from the crate) so the set-cover is
  complete (11 DELETE + 6 KEEP = 17). D2 — the Set-Version bump above. D3 — added `STANDARDS_LOG.md` to
  SETUP's confirm/lay-down lists. D4 — expanded the ALLOWLIST by `README.md` + `NEW_PROJECT_BOOTSTRAP.md`
  so all old-path references could be fixed (risk R3 → 0 stale hits, excluding the historical PLAN-001 record).
- **Impact:** No runtime impact (docs/prompt/markers only — no engine code). Changes the `SETUP.md`
  bootstrap *procedure* (now strips + creates the log + writes SVA to `docs/`) and adds the marker
  convention every future adopter inherits.
- **QA scenarios (Rule 11):** S1 marker pairing, S2 SETUP strip set-cover, S3 no-names scrub — defined in
  `docs/Plans/PLAN-002` § 8 and tracked in its § 4 Phase 4.
- **Sync:** `STANDARDS_INDEX` (Set v1.1 + STANDARDS_LOG + counts), `documents_manifest` (v1.3, renumbered to
  33 entries), `folder_structure` (v0.4), `architecture` (v0.2, § 10 Slice 1 ✅), `SET_VERSION_ADOPTED`
  (v1.1, moved), `README`. PLAN-002 promoted to v1.0 / CLOSED.
- **Author:** Yaser Khosravi

## [2026-06-13] — System design captured: docs/architecture.md

- **Type:** Major / Design record (docs-only)
- **What:** Committed `docs/architecture.md` — the system-design record converged with the operator in
  the 2026-06-13 design session. Captures: the **vault model** (this repo is the single canonical home),
  the **project footprint** (operative standard kept / setup-machinery stripped), **setup-and-strip**
  delivery, the **experiences log** (`docs/STANDARDS_LOG.md`) contribution channel fed by
  `SESSION_CLOSER` § 1.7, the **harvest → integrate → sync** loop, and the **`PROJECT-OWNED` marker**
  ownership model for non-clobbering sync. Includes the implementation roadmap (Slices 1–5 → plans).
- **Impact:** No runtime impact (design doc). Defines what the engine will implement; the engine source
  becomes the dispositive truth and this doc is kept in sync per `CLAUDE.md` § 4.
- **Sync:** manifest (entry 31, v1.1), `docs/folder_structure.md` (v0.3), `docs/README.md` updated.
- **Author:** Yaser Khosravi

## [2026-06-07] — PLAN-001: domain-neutral canonical suite (Standard Set Version v1.0)

- **Type:** Major / Governance / Critical-file edit (`docs/standards/`)
- **What:** Scrubbed all project identity (names, source-domain examples) from the standards suite and
  reset it to a clean **Standard Set Version v1.0** baseline; added the canonical `docs/standards/CLAUDE.md`
  and `docs/standards/LESSONS.md` templates (optional Codex § 14 kept in the template); added
  `docs/standards/SETUP.md` (one-shot bootstrap prompt) and slimmed `HOW_TO_USE.md` to a pointer;
  reconciled this project's own adopter files (manifest, root `CLAUDE.md`, session routines,
  `SET_VERSION_ADOPTED`) to v1.0.
- **Impact:** No runtime impact (docs/governance only). The suite is now domain-neutral and distributable.
- **Verification:** dispositive scrub grep over the suite + adopter governance files = **0 hits**; every
  `docs/standards/*.md` at VERSION 1.0; governance scripts exit 0.
- **Plan:** PLAN-001 (CLOSED) — Rule 13 senior-review pass recorded; Phase 3 landed as one commit.
- **QA scenarios:** S1 scrub-grep zero-hit ✅; S2 SETUP source-path dry-run ✅.
- **Author:** Yaser Khosravi

## [2026-06-07] — Project bootstrap: governance scaffold

- **Type:** Major / Infrastructure / Bootstrap
- **Files:** `CLAUDE.md` (repo root), `docs/standards/*.md` (13 standards files + `SET_VERSION_ADOPTED.md`),
  `docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`, `archive/LESSONS.md`, `README.md`, `docs/README.md`,
  `docs/documents_manifest.md`, `docs/folder_structure.md`, `docs/Plans/.gitkeep`,
  `scripts/check_doc_coverage.py`, `scripts/check_test_coverage_drift.py`,
  `scripts/doc_coverage_allowlist.toml`, `scripts/validation_ownership.toml`,
  `.gitlab-ci.yml`, `.gitlab/merge_request_templates/Default.md`, `.gitignore`
- **Impact:** No runtime impact. Establishes the operating contract (13 standing rules), the adopted
  standards suite, session start/end routines, document manifest, governance scripts, CI scaffold, and
  MR template before any feature work begins.
- **Standards:** Bootstrapped from the standards suite at **Standard Set Version v1.0** on
  2026-06-07 — independent versions from this point forward. Backports from the standards source are
  explicit (see `docs/standards/STANDARDS_INDEX.md` § 4.3).
- **Customizations:** single-agent project (Codex handoff § 14 omitted); domain-neutral local-CLI
  context in `CLAUDE.md` § 1 / § 4 / § 13; project-local `SESSION_OPENER`/`SESSION_CLOSER` tailored to a
  no-remote-infra, source→target propagation workflow.
- **QA scenarios:** none (no runtime code in this commit).
- **Author:** Yaser Khosravi
