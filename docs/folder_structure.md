<!-- VERSION: 0.14 -->
<!-- Last Updated: 2026-08-17 -->
<!--
CHANGE LOG
v0.14 — 2026-08-17 — PLAN-009 (skill delivery, Standard Set Version v2.0): added the skill/ top-level dir (SKILL.md + modes/bootstrap.md + modes/adopt.md) and scripts/bootstrap_skill.sh to the tree; removed the retired SETUP.md + NEW_PROJECT_BOOTSTRAP.md lines from docs/standards/ (MDRP was never listed — pre-existing gap recorded in the plan); suite caption v1.6 → v2.0; STANDARDS_LOG template caption retargeted SETUP → the delivery skill; rider — root CLAUDE.md caption "13 standing rules" → "15 standing rules".
v0.13 — 2026-08-16 — PLAN-008 (Slice 5: sync, Standard Set Version v1.6): added src/standard_document_updater/sync.py and tests/test_sync.py to the tree; noted the sync subcommand on cli.py and the engine-tree comment ("Slice 5: + sync"); suite caption v1.5 → v1.6.
v0.12 — 2026-08-16 — PLAN-010 (Standard Set Version v1.5): scripts listing swap bootstrap_memory.sh → claude_project_data.sh; .claude/ tree memory/ → project-data/ (memory + session transcripts); suite caption v1.4 → v1.5; both LESSONS captions → L001–L067.
v0.11 — 2026-08-16 — Added docs/STANDARDS_LOG.md (this project's own experiences-log instance, created retroactively) to the docs/ tree; caught up two stale tree labels — standards/ suite caption "Set Version v1.1" → v1.4 and template LESSONS caption "L001–L049" → L001–L056.
v0.10 — 2026-06-23 — PLAN-007 (remote-target transport): added src/standard_document_updater/transport.py and tests/test_transport.py to the tree; noted transport-aware on cli.py, the registry.py connection-fields comment, and the engine-tree comment ("PLAN-007: + transport").
v0.9 — 2026-06-18 — PLAN-006 (Slice 4): added src/standard_document_updater/integrate.py and tests/test_integrate.py to the tree; noted the integrate subcommand on cli.py and the engine-tree comment ("Slice 4: + integrate").
v0.8 — 2026-06-17 — PLAN-005 (durable memory): added the `.claude/` workspace (untracked memory store + README) and `scripts/bootstrap_memory.sh` to the tree; bumped the archive LESSONS comment to L001–L050.
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
├── CLAUDE.md                      # operating contract (binding; 15 standing rules)
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
│   ├── STANDARDS_LOG.md           # this project's experiences log (contribution channel; kept file)
│   ├── standards/                 # canonical domain-neutral suite (Set Version v2.0)
│   │   ├── CLAUDE.md             # operating-contract TEMPLATE (with placeholders)
│   │   ├── LESSONS.md            # lessons archive (canonical template, L001–L067)
│   │   ├── CICD_STANDARDS.md
│   │   ├── ENGINEERING_STANDARDS.md
│   │   ├── HOW_TO_USE.md
│   │   ├── MEMORY_PROTOCOL.md
│   │   ├── PROJECT_INSTRUCTIONS_TEMPLATE.md
│   │   ├── PROJECT_STANDARDS.md
│   │   ├── PROMPT_STANDARDS.md
│   │   ├── README.md
│   │   ├── SESSION_CLOSER.md
│   │   ├── SESSION_OPENER.md
│   │   ├── STANDARDS_INDEX.md
│   │   ├── STANDARDS_LOG.md       # experiences-log TEMPLATE (the delivery skill copies to docs/STANDARDS_LOG.md)
│   │   └── VALIDATION_STANDARDS.md
│   └── Plans/                     # committed planning docs (Rule 1); OPEN_TASKS.md is gitignored
│       └── .gitkeep
├── skill/                         # delivery skill (live-reference; PLAN-009) — symlinked to ~/.claude/skills/standard-docset by scripts/bootstrap_skill.sh
│   ├── SKILL.md                   # mode dispatch + step-0 vault resolve/self-pull
│   └── modes/
│       ├── bootstrap.md           # NEW-project delivery (successor to SETUP.md)
│       └── adopt.md               # EXISTING-project migration (dry-run gated)
├── pyproject.toml                 # packaging + tool config (setuptools / ruff / mypy / pytest)
├── config/
│   └── projects.toml              # registry of managed projects (name + path; per architecture.md § 8)
├── src/
│   └── standard_document_updater/  # the CLI engine (Slice 2: registry + status/drift; Slice 3: + harvest; Slice 4: + integrate; PLAN-007: + transport; Slice 5: + sync)
│       ├── __init__.py            # package marker + released CLI version
│       ├── __main__.py            # `python -m standard_document_updater` entry point
│       ├── errors.py              # exception hierarchy
│       ├── registry.py            # config/projects.toml loader (name + transport + connection fields)
│       ├── setversion.py          # live parsers: vault/adopted Set Version + open-log count
│       ├── logentry.py            # STANDARDS_LOG.md entry parser (LogEntry + parse_log)
│       ├── harvest.py             # consolidate open log entries → stdout report (group-by-area + dup flag)
│       ├── integrate.py           # integration worksheet (Area→topical + next-L0NN) + gated Status write-back
│       ├── transport.py           # pluggable target transports (local | git | ssh): materialize → operate → flush
│       ├── sync.py                # section-aware suite propagation (replace | merge | record per file)
│       ├── report.py              # state computation + table render + drift filter
│       └── cli.py                 # argparse; status / drift / harvest / integrate / sync subcommands (transport-aware)
├── tests/                         # pytest suite
│   ├── conftest.py                # synthetic vault/project fixtures
│   ├── test_setversion.py
│   ├── test_registry.py
│   ├── test_report.py
│   ├── test_logentry.py
│   ├── test_harvest.py
│   ├── test_integrate.py
│   ├── test_transport.py
│   ├── test_sync.py
│   └── test_cli.py
├── .claude/                      # Claude Code workspace (untracked; Dropbox-synced)
│   ├── project-data/             # Claude project data (memory + session transcripts) — harness symlinks here (Rule 14)
│   └── README_memory.md
├── scripts/
│   ├── bootstrap_skill.sh        # per-machine skill installer (idempotent symlink)
│   ├── claude_project_data.sh    # Rule 14 project-data locality tool (status / adopt / link)
│   ├── check_doc_coverage.py
│   ├── check_test_coverage_drift.py
│   ├── doc_coverage_allowlist.toml
│   └── validation_ownership.toml
└── archive/
    └── LESSONS.md                 # incident-to-rule archive (L001–L067)
```

(Code-folder entries are added as the project grows. See `docs/standards/PROJECT_STANDARDS.md` § 6 for
the standard layout template and `docs/standards/ENGINEERING_STANDARDS.md` for module/layer rules.)
