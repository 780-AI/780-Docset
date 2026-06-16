<!-- VERSION: 1.7 -->
<!-- Last Updated: 2026-06-16 -->
<!--
CHANGE LOG
v1.7 — 2026-06-16 — Registered PLAN-004 (Slice 3: harvest) DRAFT + its sibling tracker as entries
36–37 (v0.1). Quick-index Plans range 31–35 → 31–37; Engine range 36–47 → 38–49 (shifted by the two
inserted plan rows). Design session only; engine code lands in the Phase-3 commit (→ 1.8).
v1.6 — 2026-06-16 — PLAN-003 (Slice 2) implemented: registered the first engine code as entries 36–47
(7 src modules + 5 test modules, all v0.1) under a new Engine quick-index range; promoted PLAN-003 +
its tracker (rows 34–35) from 0.1/DRAFT → 1.0/CLOSED in the same commit the slice ships. `config/projects.toml`
+ `pyproject.toml` carry no VERSION header → not manifest-tracked (documented in folder_structure.md).
v1.5 — 2026-06-16 — Registered PLAN-003 (Slice 2: registry + status/drift) DRAFT + its sibling tracker
as entries 34–35 (v0.1). Quick-index Plans range 31–33 → 31–35. Design session only; no engine code yet.
v1.4 — 2026-06-14 — Project rename: display name → "Standard DocSet" across root CLAUDE.md (1.2), session files (1.2), SET_VERSION_ADOPTED (1.2), architecture (0.3), folder_structure (0.5); version cells updated. Engine package `standard_document_updater` unchanged (Option B). GitLab project/remote → slug `standard-docset`.
v1.3 — 2026-06-13 — PLAN-002 (Slice 1): added docs/standards/STANDARDS_LOG.md (experiences-log template);
moved SET_VERSION_ADOPTED.md docs/standards/ → docs/ (path + category updated); bumped the marker/SETUP
edits to v1.1 (root CLAUDE.md, docs SESSION_OPENER/CLOSER + their templates, SETUP, NEW_PROJECT_BOOTSTRAP,
STANDARDS_INDEX, SET_VERSION_ADOPTED) and architecture.md to 0.2 / folder_structure.md to 0.4; promoted
PLAN-002 to 1.0 (CLOSED). Renumbered the table and corrected the module quick-index ranges + the manifest
self-version cell (was stale at 1.0). Standard Set Version v1.1.
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
| Operating contract + project docs | 1–10 |
| Canonical standards suite (Set v1.1) | 11–27 |
| Governance scripts | 28–29 |
| Archive | 30 |
| Plans | 31–37 |
| Engine (src + tests) | 38–49 |

## Manifest table

| # | Title | Version | Category | Path |
|---|---|---|---|---|
| 1 | Operating Contract (binding) | 1.2 | Governance | `CLAUDE.md` |
| 2 | Project README | - | Docs | `README.md` |
| 3 | CHANGELOG | - | Docs | `CHANGELOG.md` |
| 4 | Docs Index | - | Docs | `docs/README.md` |
| 5 | Documents Manifest | 1.7 | Governance | `docs/documents_manifest.md` |
| 6 | Folder Structure | 0.6 | Governance | `docs/folder_structure.md` |
| 7 | Architecture (system-design record) | 0.4 | Docs | `docs/architecture.md` |
| 8 | Session Opener (project-local, binding) | 1.2 | Governance | `docs/SESSION_OPENER.md` |
| 9 | Session Closer (project-local, binding) | 1.2 | Governance | `docs/SESSION_CLOSER.md` |
| 10 | Set Version Adopted | 1.2 | Governance | `docs/SET_VERSION_ADOPTED.md` |
| 11 | CLAUDE.md (template) | 1.1 | Standards | `docs/standards/CLAUDE.md` |
| 12 | Lessons Archive (template) | 1.0 | Standards | `docs/standards/LESSONS.md` |
| 13 | Project Standards | 1.0 | Standards | `docs/standards/PROJECT_STANDARDS.md` |
| 14 | Prompt Standards | 1.0 | Standards | `docs/standards/PROMPT_STANDARDS.md` |
| 15 | Project Instructions Template | 1.0 | Standards | `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` |
| 16 | Memory Protocol | 1.0 | Standards | `docs/standards/MEMORY_PROTOCOL.md` |
| 17 | Engineering Standards | 1.0 | Standards | `docs/standards/ENGINEERING_STANDARDS.md` |
| 18 | Validation Standards | 1.0 | Standards | `docs/standards/VALIDATION_STANDARDS.md` |
| 19 | CI/CD Standards | 1.0 | Standards | `docs/standards/CICD_STANDARDS.md` |
| 20 | Session Opener (template) | 1.1 | Standards | `docs/standards/SESSION_OPENER.md` |
| 21 | Session Closer (template) | 1.1 | Standards | `docs/standards/SESSION_CLOSER.md` |
| 22 | Standards README (meta) | 1.0 | Standards | `docs/standards/README.md` |
| 23 | Standards Index (meta) | 1.1 | Standards | `docs/standards/STANDARDS_INDEX.md` |
| 24 | New Project Bootstrap (meta) | 1.1 | Standards | `docs/standards/NEW_PROJECT_BOOTSTRAP.md` |
| 25 | How To Use (meta) | 1.0 | Standards | `docs/standards/HOW_TO_USE.md` |
| 26 | Setup — one-shot prompt (meta) | 1.1 | Standards | `docs/standards/SETUP.md` |
| 27 | Standards Log — experiences-log template (meta) | 1.0 | Standards | `docs/standards/STANDARDS_LOG.md` |
| 28 | Doc Coverage Check | 0.1 | Governance script | `scripts/check_doc_coverage.py` |
| 29 | Test Coverage Drift Check | 0.1 | Governance script | `scripts/check_test_coverage_drift.py` |
| 30 | Lessons Archive (adopter copy) | 1.0 | Governance | `archive/LESSONS.md` |
| 31 | PLAN-001 — domain-neutral suite (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-001_domain_neutral_suite.md` |
| 32 | PLAN-001 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-001_tracker.md` |
| 33 | PLAN-002 — Slice 1 (setup-strip + log + markers) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-002_setup_strip_log_markers.md` |
| 34 | PLAN-003 — Slice 2 (registry + status/drift) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-003_registry_status_drift.md` |
| 35 | PLAN-003 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-003_tracker.md` |
| 36 | PLAN-004 — Slice 3 (harvest) (DRAFT) | 0.1 | Plan | `docs/Plans/PLAN-004_harvest.md` |
| 37 | PLAN-004 tracker (DRAFT) | 0.1 | Plan | `docs/Plans/PLAN-004_tracker.md` |
| 38 | Engine — package marker + CLI version | 0.1 | Engine | `src/standard_document_updater/__init__.py` |
| 39 | Engine — module entry point | 0.1 | Engine | `src/standard_document_updater/__main__.py` |
| 40 | Engine — exception hierarchy | 0.1 | Engine | `src/standard_document_updater/errors.py` |
| 41 | Engine — registry loader | 0.1 | Engine | `src/standard_document_updater/registry.py` |
| 42 | Engine — Set-Version / open-log parsers | 0.1 | Engine | `src/standard_document_updater/setversion.py` |
| 43 | Engine — comparison report | 0.1 | Engine | `src/standard_document_updater/report.py` |
| 44 | Engine — CLI (status / drift) | 0.1 | Engine | `src/standard_document_updater/cli.py` |
| 45 | Engine test — shared fixtures | 0.1 | Engine test | `tests/conftest.py` |
| 46 | Engine test — setversion | 0.1 | Engine test | `tests/test_setversion.py` |
| 47 | Engine test — registry | 0.1 | Engine test | `tests/test_registry.py` |
| 48 | Engine test — report | 0.1 | Engine test | `tests/test_report.py` |
| 49 | Engine test — cli | 0.1 | Engine test | `tests/test_cli.py` |

> `.toml` config (`scripts/doc_coverage_allowlist.toml`, `scripts/validation_ownership.toml`) and
> non-versioned config (`.gitlab-ci.yml`, `.gitignore`, MR template) carry no VERSION header and are not
> manifest-tracked per Rule 8; they are documented in `docs/folder_structure.md`.

## Last updated

- **Date**: 2026-06-16
- **Change**: PLAN-003 (Slice 2) implemented — registered the first engine code (entries 36–47: 7 src +
  5 test modules, v0.1) under a new Engine quick-index range; promoted PLAN-003 + tracker (34–35) to
  1.0/CLOSED. folder_structure 0.5→0.6, architecture 0.3→0.4 synced same-commit.
- **Previous change**: Registered PLAN-003 DRAFT + sibling tracker as entries 34–35 (design session).
- **Previous audit**: (none — first audit will be quarterly per `PROJECT_STANDARDS.md` § 2.9)
