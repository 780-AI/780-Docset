<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-06-07 -->
<!--
CHANGE LOG
v0.1 — 2026-06-07 — Project bootstrap. Initial manifest scaffold listing the governance suite + supporting docs + scripts.
-->
# Document & Code Manifest

Lists every committed `.md` file and every tracked code file (`.py`/`.sh` with a VERSION header), per
`CLAUDE.md` Rule 8. Updated in the **same commit** that creates, renames, or deletes a tracked file.

## Module quick index

| Module / Section | Entry range |
|---|---|
| Operating contract + project docs | 1–6 |
| Standards suite (adopted, Set v2.6) | 7–21 |
| Governance scripts | 22–23 |
| Archive | 24 |

## Manifest table

| # | Title | Version | Category | Path |
|---|---|---|---|---|
| 1 | Operating Contract (binding) | 1.0 | Governance | `CLAUDE.md` |
| 2 | Project README | - | Docs | `README.md` |
| 3 | CHANGELOG | - | Docs | `CHANGELOG.md` |
| 4 | Docs Index | - | Docs | `docs/README.md` |
| 5 | Documents Manifest | 0.1 | Governance | `docs/documents_manifest.md` |
| 6 | Folder Structure | 0.1 | Governance | `docs/folder_structure.md` |
| 7 | Session Opener (project-local, binding) | 1.0 | Governance | `docs/SESSION_OPENER.md` |
| 8 | Session Closer (project-local, binding) | 1.0 | Governance | `docs/SESSION_CLOSER.md` |
| 9 | Set Version Adopted | 1.0 | Governance | `docs/standards/SET_VERSION_ADOPTED.md` |
| 10 | Project Standards | 1.4 | Standards | `docs/standards/PROJECT_STANDARDS.md` |
| 11 | Prompt Standards | 1.5 | Standards | `docs/standards/PROMPT_STANDARDS.md` |
| 12 | Project Instructions Template | 1.4 | Standards | `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` |
| 13 | Memory Protocol | 1.4 | Standards | `docs/standards/MEMORY_PROTOCOL.md` |
| 14 | Engineering Standards | 1.3 | Standards | `docs/standards/ENGINEERING_STANDARDS.md` |
| 15 | Validation Standards | 1.2 | Standards | `docs/standards/VALIDATION_STANDARDS.md` |
| 16 | CI/CD Standards | 1.2 | Standards | `docs/standards/CICD_STANDARDS.md` |
| 17 | Session Opener (template) | 1.4 | Standards | `docs/standards/SESSION_OPENER.md` |
| 18 | Session Closer (template) | 1.0 | Standards | `docs/standards/SESSION_CLOSER.md` |
| 19 | Standards README (meta) | 1.9 | Standards | `docs/standards/README.md` |
| 20 | Standards Index (meta) | 1.9 | Standards | `docs/standards/STANDARDS_INDEX.md` |
| 21 | New Project Bootstrap (meta) | 1.1 | Standards | `docs/standards/NEW_PROJECT_BOOTSTRAP.md` |
| 22 | How To Use (meta) | 1.6 | Standards | `docs/standards/HOW_TO_USE.md` |
| 23 | Doc Coverage Check | 0.1 | Governance script | `scripts/check_doc_coverage.py` |
| 24 | Test Coverage Drift Check | 0.1 | Governance script | `scripts/check_test_coverage_drift.py` |
| 25 | Lessons Archive | 1.12 | Governance | `archive/LESSONS.md` |

> `.toml` config files (`scripts/doc_coverage_allowlist.toml`, `scripts/validation_ownership.toml`) and
> non-versioned config (`.gitlab-ci.yml`, `.gitignore`, MR template) carry no VERSION header and are not
> manifest-tracked per Rule 8; they are documented in `docs/folder_structure.md`.

## Last updated

- **Date**: 2026-06-07
- **Change**: Project bootstrap — initial manifest scaffold (25 entries).
- **Previous change**: (none — this is the first entry)
- **Previous audit**: (none — first audit will be quarterly per `PROJECT_STANDARDS.md` § 2.9)
