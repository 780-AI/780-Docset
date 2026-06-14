# CHANGELOG

Newest entries at the top.

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
