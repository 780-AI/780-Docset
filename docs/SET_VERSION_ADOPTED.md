<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-06-13 -->
<!--
CHANGE LOG
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): relocated from docs/standards/ to docs/ (survives the setup strip); records adoption of Standard Set Version v1.1 (experiences-log template + PROJECT-OWNED markers + setup-and-strip).
v1.0 — 2026-06-07 — Records adoption of Standard Set Version v1.0 (this repo also authors that baseline).
-->
# Standard Set Version Adopted

This project adopts the standards suite at:

- **Standard Set Version:** v1.1 (adds the `STANDARDS_LOG.md` experiences-log template, `PROJECT-OWNED`
  markers, and setup-and-strip — atop the v1.0 clean domain-neutral baseline)
- **Adopted on:** 2026-06-13 (v1.0 baseline adopted 2026-06-07)
- **Source:** this repository's own `docs/standards/` — `standard-document-updater` both **authors** the
  canonical domain-neutral suite and **adopts** it to govern its own development.

The adopted state:

- **13 standing rules** in `CLAUDE.md` § 3 (Rules 1–13).
- **49 lessons** (L001–L049) in `archive/LESSONS.md`.
- The suite per `docs/standards/STANDARDS_INDEX.md` (11 binding files + meta files + `SETUP.md` +
  `STANDARDS_LOG.md`).

## Backport tracking

Because this repo authors the canonical suite, "backport" here means: when the canonical
`docs/standards/` suite is bumped to a new Set Version, reconcile this project's own adopter instances
(root `CLAUDE.md`, `archive/LESSONS.md`, `docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`) and record
the new adopted version below.

| Set Version | Adopted on | Notes |
|---|---|---|
| v1.1 | 2026-06-13 | PLAN-002 (Slice 1): added the `STANDARDS_LOG.md` experiences-log template; wrapped project-owned blocks in `PROJECT-OWNED` markers (root `CLAUDE.md` + `docs/SESSION_OPENER/CLOSER.md` and their templates); reworked `SETUP.md` (setup-and-strip + log create + SVA→docs/); moved this file from `docs/standards/` to `docs/`. |
| v1.0 | 2026-06-07 | Clean domain-neutral baseline established (PLAN-001). Single-agent adopter (Codex § 14 omitted from this project's own root `CLAUDE.md`; retained in the template). |
