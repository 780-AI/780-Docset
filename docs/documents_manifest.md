<!-- VERSION: 1.2 -->
<!-- Last Updated: 2026-06-13 -->
<!--
CHANGE LOG
v1.2 — 2026-06-13 — Registered PLAN-002 (Slice 1) as entry 32.
v1.1 — 2026-06-13 — Registered docs/architecture.md (system-design record) as entry 31.
v1.0 — 2026-06-07 — PLAN-001: domain-neutral v1.0 baseline. All standards-suite version cells reset to
1.0; added canonical templates docs/standards/CLAUDE.md + LESSONS.md + SETUP.md. Bumped from v0.1.
v0.1 — 2026-06-07 — Project bootstrap. Initial manifest scaffold.
-->
# Document & Code Manifest

Lists every committed `.md` file and every tracked code file (`.py`/`.sh` with a VERSION header), per
`CLAUDE.md` Rule 8. Updated in the **same commit** that creates, renames, or deletes a tracked file.

## Module quick index

| Module / Section | Entry range |
|---|---|
| Operating contract + project docs | 1–8 |
| Canonical standards suite (Set v1.0) | 9–24 |
| Governance scripts | 25–26 |
| Archive | 27 |
| Plans | 29–30, 32 |
| Project design | 31 |

## Manifest table

| # | Title | Version | Category | Path |
|---|---|---|---|---|
| 1 | Operating Contract (binding) | 1.0 | Governance | `CLAUDE.md` |
| 2 | Project README | - | Docs | `README.md` |
| 3 | CHANGELOG | - | Docs | `CHANGELOG.md` |
| 4 | Docs Index | - | Docs | `docs/README.md` |
| 5 | Documents Manifest | 1.0 | Governance | `docs/documents_manifest.md` |
| 6 | Folder Structure | 0.1 | Governance | `docs/folder_structure.md` |
| 7 | Session Opener (project-local, binding) | 1.0 | Governance | `docs/SESSION_OPENER.md` |
| 8 | Session Closer (project-local, binding) | 1.0 | Governance | `docs/SESSION_CLOSER.md` |
| 9 | Set Version Adopted | 1.0 | Standards | `docs/standards/SET_VERSION_ADOPTED.md` |
| 10 | CLAUDE.md (template) | 1.0 | Standards | `docs/standards/CLAUDE.md` |
| 11 | Lessons Archive (template) | 1.0 | Standards | `docs/standards/LESSONS.md` |
| 12 | Project Standards | 1.0 | Standards | `docs/standards/PROJECT_STANDARDS.md` |
| 13 | Prompt Standards | 1.0 | Standards | `docs/standards/PROMPT_STANDARDS.md` |
| 14 | Project Instructions Template | 1.0 | Standards | `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` |
| 15 | Memory Protocol | 1.0 | Standards | `docs/standards/MEMORY_PROTOCOL.md` |
| 16 | Engineering Standards | 1.0 | Standards | `docs/standards/ENGINEERING_STANDARDS.md` |
| 17 | Validation Standards | 1.0 | Standards | `docs/standards/VALIDATION_STANDARDS.md` |
| 18 | CI/CD Standards | 1.0 | Standards | `docs/standards/CICD_STANDARDS.md` |
| 19 | Session Opener (template) | 1.0 | Standards | `docs/standards/SESSION_OPENER.md` |
| 20 | Session Closer (template) | 1.0 | Standards | `docs/standards/SESSION_CLOSER.md` |
| 21 | Standards README (meta) | 1.0 | Standards | `docs/standards/README.md` |
| 22 | Standards Index (meta) | 1.0 | Standards | `docs/standards/STANDARDS_INDEX.md` |
| 23 | New Project Bootstrap (meta) | 1.0 | Standards | `docs/standards/NEW_PROJECT_BOOTSTRAP.md` |
| 24 | How To Use (meta) | 1.0 | Standards | `docs/standards/HOW_TO_USE.md` |
| 25 | Setup — one-shot prompt (meta) | 1.0 | Standards | `docs/standards/SETUP.md` |
| 26 | Doc Coverage Check | 0.1 | Governance script | `scripts/check_doc_coverage.py` |
| 27 | Test Coverage Drift Check | 0.1 | Governance script | `scripts/check_test_coverage_drift.py` |
| 28 | Lessons Archive (adopter copy) | 1.0 | Governance | `archive/LESSONS.md` |
| 29 | PLAN-001 — domain-neutral suite (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-001_domain_neutral_suite.md` |
| 30 | PLAN-001 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-001_tracker.md` |
| 31 | Architecture (system-design record) | 0.1 | Docs | `docs/architecture.md` |
| 32 | PLAN-002 — Slice 1 (setup-strip + log + markers) | 0.1 | Plan | `docs/Plans/PLAN-002_setup_strip_log_markers.md` |

> `.toml` config (`scripts/doc_coverage_allowlist.toml`, `scripts/validation_ownership.toml`) and
> non-versioned config (`.gitlab-ci.yml`, `.gitignore`, MR template) carry no VERSION header and are not
> manifest-tracked per Rule 8; they are documented in `docs/folder_structure.md`.

## Last updated

- **Date**: 2026-06-13
- **Change**: Registered `docs/architecture.md` (system-design record) — 31 entries.
- **Previous change**: PLAN-001 — domain-neutral v1.0 baseline; suite version cells reset to 1.0; added
  `docs/standards/{CLAUDE.md, LESSONS.md, SETUP.md}` + PLAN-001 rows (30 entries).
- **Previous audit**: (none — first audit will be quarterly per `PROJECT_STANDARDS.md` § 2.9)
