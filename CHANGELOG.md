# CHANGELOG

Newest entries at the top.

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
