<!-- VERSION: 0.7 -->
<!-- Last Updated: 2026-06-16 -->
<!--
CHANGE LOG
v0.7 — 2026-06-16 — PLAN-004 (Slice 3): added src/standard_document_updater/logentry.py + harvest.py and tests/test_logentry.py + test_harvest.py to the tree; noted the harvest subcommand on cli.py and the engine-tree comment ("Slice 3: + harvest").
v0.6 — 2026-06-16 — PLAN-003 (Slice 2): engine landed. Moved src/standard_document_updater/ (7 modules), tests/ (conftest + 4 test files), config/projects.toml, and pyproject.toml from the Planned block into the live repository tree.
v0.5 — 2026-06-14 — Project display name → "Standard DocSet" (layout title + tree root). Engine package path `standard_document_updater` unchanged.
v0.4 — 2026-06-13 — PLAN-002 (Slice 1): moved SET_VERSION_ADOPTED.md from docs/standards/ to docs/ (survives the setup strip); added the STANDARDS_LOG.md experiences-log template to the docs/standards/ listing; bumped the suite label to Set Version v1.1.
v0.3 — 2026-06-13 — Added docs/architecture.md (system-design record) to the docs/ listing; removed it from the Planned section (now real).
v0.2 — 2026-06-07 — PLAN-001: added canonical suite templates (CLAUDE.md, LESSONS.md, SETUP.md) to the docs/standards/ listing.
v0.1 — 2026-06-07 — Project bootstrap. Initial authoritative layout (governance scaffold only; no engine code yet).
-->
# Folder Structure

**Authoritative layout for `Standard DocSet`.**

Any change that contradicts this file is Major (per `CLAUDE.md` § 5) and must update this file in the
same commit.

## Repository root

```
Standard DocSet/
├── CLAUDE.md                      # operating contract (binding; 13 standing rules)
├── README.md                      # project overview
├── CHANGELOG.md                   # cross-cutting history (newest first)
├── .gitignore
├── .gitlab-ci.yml                 # CI scaffold (governance stage)
├── .gitlab/
│   └── merge_request_templates/
│       └── Default.md
├── docs/
│   ├── README.md                  # docs index
│   ├── documents_manifest.md      # version index of all tracked docs + code
│   ├── folder_structure.md        # this file
│   ├── architecture.md            # system-design record (the design the engine implements)
│   ├── SESSION_OPENER.md          # binding session-start pre-flight (Rule 9)
│   ├── SESSION_CLOSER.md          # binding session-end wrap-up (Rule 12)
│   ├── SET_VERSION_ADOPTED.md     # adopted Standard Set Version (moved here so it survives the setup strip)
│   ├── standards/                 # canonical domain-neutral suite (Set Version v1.1)
│   │   ├── SETUP.md               # one-shot bootstrap prompt
│   │   ├── CLAUDE.md             # operating-contract TEMPLATE (with placeholders)
│   │   ├── LESSONS.md            # lessons archive (canonical template, L001–L049)
│   │   ├── CICD_STANDARDS.md
│   │   ├── ENGINEERING_STANDARDS.md
│   │   ├── HOW_TO_USE.md
│   │   ├── MEMORY_PROTOCOL.md
│   │   ├── NEW_PROJECT_BOOTSTRAP.md
│   │   ├── PROJECT_INSTRUCTIONS_TEMPLATE.md
│   │   ├── PROJECT_STANDARDS.md
│   │   ├── PROMPT_STANDARDS.md
│   │   ├── README.md
│   │   ├── SESSION_CLOSER.md
│   │   ├── SESSION_OPENER.md
│   │   ├── STANDARDS_INDEX.md
│   │   ├── STANDARDS_LOG.md       # experiences-log TEMPLATE (SETUP copies to docs/STANDARDS_LOG.md)
│   │   └── VALIDATION_STANDARDS.md
│   └── Plans/                     # committed planning docs (Rule 1); OPEN_TASKS.md is gitignored
│       └── .gitkeep
├── pyproject.toml                 # packaging + tool config (setuptools / ruff / mypy / pytest)
├── config/
│   └── projects.toml              # registry of managed projects (name + path; per architecture.md § 8)
├── src/
│   └── standard_document_updater/  # the CLI engine (Slice 2: registry + status/drift; Slice 3: + harvest)
│       ├── __init__.py            # package marker + released CLI version
│       ├── __main__.py            # `python -m standard_document_updater` entry point
│       ├── errors.py              # exception hierarchy
│       ├── registry.py            # config/projects.toml loader (name + path)
│       ├── setversion.py          # live parsers: vault/adopted Set Version + open-log count
│       ├── logentry.py            # STANDARDS_LOG.md entry parser (LogEntry + parse_log)
│       ├── harvest.py             # consolidate open log entries → stdout report (group-by-area + dup flag)
│       ├── report.py              # state computation + table render + drift filter
│       └── cli.py                 # argparse; status / drift / harvest subcommands
├── tests/                         # pytest suite
│   ├── conftest.py                # synthetic vault/project fixtures
│   ├── test_setversion.py
│   ├── test_registry.py
│   ├── test_report.py
│   ├── test_logentry.py
│   ├── test_harvest.py
│   └── test_cli.py
├── scripts/
│   ├── check_doc_coverage.py
│   ├── check_test_coverage_drift.py
│   ├── doc_coverage_allowlist.toml
│   └── validation_ownership.toml
└── archive/
    └── LESSONS.md                 # incident-to-rule archive (L001–L049)
```

(Code-folder entries are added as the project grows. See `docs/standards/PROJECT_STANDARDS.md` § 6 for
the standard layout template and `docs/standards/ENGINEERING_STANDARDS.md` for module/layer rules.)
