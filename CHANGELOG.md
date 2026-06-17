# CHANGELOG

Newest entries at the top.

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
