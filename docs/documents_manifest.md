<!-- VERSION: 2.15 -->
<!-- Last Updated: 2026-08-16 -->
<!--
CHANGE LOG
v2.15 — 2026-08-16 — PLAN-010 (Standard Set Version v1.5) implemented: entry 56 swapped
bootstrap_memory.sh → claude_project_data.sh (0.1; Rule 8 delete + register, slot reused to avoid a
renumber); bumped touched cells (1 root CLAUDE.md → 1.7, 6 folder_structure → 0.12, 8 SESSION_OPENER
→ 1.6, 9 SESSION_CLOSER → 1.4, 10 SVA → 1.6, 11 template CLAUDE.md → 1.4, 20 template OPENER → 1.5,
21 template CLOSER → 1.3, 23 STANDARDS_INDEX → 1.5, 24 NPB → 1.5, 26 SETUP → 1.5, 57 rollout prompt
→ 1.2, 58 NEW_MACHINE_SETUP → 1.1); LESSONS cells (12, 30) unchanged per the no-per-lesson-bump
practice; promoted PLAN-010 + tracker (68–69) to 1.0/CLOSED; quick-index caption Set v1.4 → v1.5;
self-row caught up 2.13 → 2.15 (v2.14's log claimed the bump but the cell never moved — the L063
class, fixed here).
v2.14 — 2026-08-16 — Registered PLAN-010 (upstream intake: EverOn v2.x → vault, Set v1.5) DRAFT +
its sibling tracker as entries 68–69 (v0.1; appended, not inserted); quick-index Plans range →
31–39, 59–60, 63–64, 68–69; self-row 2.13→2.14. **Fix-forward for v2.13 (`2c7833d`, pushed):** the
entry-67 table row (`docs/STANDARDS_LOG.md`) was never actually added — v2.13's CHANGE LOG and
quick-index referenced it but the row was missing (the L063 stamp-vs-log class, caught during the
PLAN-010 Rule 13 pass); row registered now. Design session only; the Phase-3 implement commit lands
the 21-file § 7 ALLOWLIST.
v2.13 — 2026-08-16 — Registered docs/STANDARDS_LOG.md (this project's own experiences-log instance,
created retroactively — the self-adoption had skipped the instantiation step) as entry 67 (v1.0;
appended, not inserted, to avoid a renumber); quick-index "Operating contract + project docs" range →
1–10, 58, 67; bumped entry 6 (folder_structure.md) cell 0.9→0.11 (cell was stale — the v2.11 commit
bumped the file to 0.10 but not this cell; filesystem-verified) and self-row 2.12→2.13. Doc-only.
v2.12 — 2026-08-16 — Standard Set Version v1.4 (process-hardening batch: lessons L052–L056 + L051
recurrence #4): bumped touched cells — entry 1 (root CLAUDE.md) 1.5→1.6, entry 8 (project SESSION_OPENER)
1.4→1.5, entry 9 (project SESSION_CLOSER) 1.2→1.3, entry 10 (SET_VERSION_ADOPTED) 1.4→1.5, entry 11
(template CLAUDE.md) 1.2→1.3, entry 20 (template SESSION_OPENER) 1.3→1.4, entry 21 (template
SESSION_CLOSER) 1.1→1.2, entry 23 (STANDARDS_INDEX) 1.3→1.4, entry 24 (NEW_PROJECT_BOOTSTRAP) 1.3→1.4,
entry 26 (SETUP) 1.3→1.4. LESSONS rows (12 template, 30 adopter) left at 1.0 per the established
no-per-lesson-bump practice. Also caught up two stale cells: self-row (entry 5) 2.10→2.12 (was never
bumped at v2.11) and the quick-index caption "Set v1.2" → "Set v1.4". Doc-only; no engine change.
v2.11 — 2026-06-23 — PLAN-007 (remote-target transport) implemented: registered transport.py + test_transport.py as entries 65–66 (v0.1; Engine quick-index range → 40–55, 61–62, 65–66); bumped touched cells — entry 1 (root CLAUDE.md) 1.4→1.5, entry 7 (architecture.md) 0.8→0.9, entry 40 (__init__) 0.3→0.4, entry 43 (registry) 0.1→0.2, entry 45 (report) 0.1→0.2, entry 46 (cli) 0.3→0.4, entry 49 (test_registry) 0.1→0.2, entry 50 (test_report) 0.1→0.2, entry 51 (test_cli) 0.3→0.4; promoted PLAN-007 + tracker (63–64) 0.1/DRAFT → 1.0/CLOSED. Engine behavior added; read-only on the vault → no Set Version change.
v2.10 — 2026-06-21 — Installer fix (bootstrap gap from first real adoption): bumped entry 26 (SETUP.md)
1.2→1.3 and entry 24 (NEW_PROJECT_BOOTSTRAP.md) 1.2→1.3 — both now SEED `docs/Plans/OPEN_TASKS.md` at
bootstrap (it was gitignored but never created). Installer-only; OPEN_TASKS is gitignored/local so it is
not itself a tracked entry. No Set-Version bump (v1.3 suite CONTENT unchanged).
v2.9 — 2026-06-21 — Drift fix: bumped entry 7 (architecture.md) 0.6→0.8 (roadmap slice→plan numbering
corrected: sync = PLAN-008, PLAN-007 = remote transport). Also corrected two pre-existing stale version
cells the v2.2 CHANGE LOG already claimed but never edited in the table: entry 5 (this manifest, self-row)
2.1→2.9 and entry 6 (folder_structure.md) 0.8→0.9. Filesystem-verified (Rule 2). Doc-only; the version
column is not governance-validated, which is how the cells drifted. No Set-Version bump.
v2.8 — 2026-06-20 — Bumped entry 57 (MEMORY_DURABILITY_ROLLOUT_PROMPT.md) 1.0→1.1 — reconciled its step-5
wording with the settled Rule 14 practice (gitignore `.claude/`) + added `.gitignore` to its ALLOWLIST.
Wording fix only; no Set-Version bump, STANDARDS_INDEX untouched.
v2.7 — 2026-06-20 — Bumped entry 24 (NEW_PROJECT_BOOTSTRAP.md) 1.1→1.2 — the long-form walkthrough caught
up to full Standard Set Version v1.3 parity with SETUP.md (added session-file instantiation + experiences
log + Step 8 durable memory + Step 10.5 strip; v1.1→v1.3; counts 9→14 rules / 10→11 binding). Installer/
walkthrough only; v1.3 suite content unchanged → no Set-Version bump, STANDARDS_INDEX untouched.
v2.6 — 2026-06-20 — Bumped entry 26 (SETUP.md) 1.1→1.2 — the bootstrap installer caught up to Standard
Set Version v1.3 (v1.3 refs + Step 6.5 durable memory + rollout-prompt registered in lay-down/strip,
fixing the strip set-cover). Installer-only; the v1.3 suite content is unchanged → no Set-Version bump,
STANDARDS_INDEX untouched (it bumps only at Set-Version releases).
v2.5 — 2026-06-20 — Registered PLAN-007 (remote transport) DRAFT + its sibling tracker as entries 63–64
(v0.1); quick-index Plans range → "31–39, 59–60, 63–64" (appended, not inserted, to avoid an Engine
renumber). Design session only; the Phase-3 implement commit lands transport.py + tests (→ 2.6).
v2.4 — 2026-06-20 — Standard Set Version v1.3 (lesson L051 — Rule 13 senior-review pass must mechanically
run the linter/type-checker/tests): bumped touched cells — entry 8 (project SESSION_OPENER) 1.3→1.4,
entry 10 (SET_VERSION_ADOPTED) 1.3→1.4, entry 20 (template SESSION_OPENER) 1.2→1.3, entry 23
(STANDARDS_INDEX) 1.2→1.3. LESSONS rows (12 template, 30 adopter) left at 1.0 per the established
no-per-lesson-bump practice. No new tracked files.
v2.3 — 2026-06-20 — Root CLAUDE.md § 4 cleanup: bumped entry 1 (Operating Contract) 1.3→1.4 (dropped the
stale "created when the engine lands" note; promoted config/projects.toml to a Critical File). Doc-only,
project-specific — no new tracked files, no Set Version change.
v2.2 — 2026-06-18 — PLAN-006 (Slice 4: integrate) implemented: registered integrate.py + test_integrate.py
as entries 61–62 (v0.1; Engine range 38–55 → +61, Engine-test +62); bumped touched cells (__init__ 40, cli 46,
test_cli 51) 0.2→0.3 and the cli description (+ integrate); promoted PLAN-006 + its tracker (59–60) 0.1/DRAFT
→ 1.0/CLOSED. architecture 0.6→0.7, folder_structure 0.8→0.9 synced same-commit. No Set Version change.
v2.1 — 2026-06-18 — Registered PLAN-006 (Slice 4: integrate) DRAFT + its sibling tracker as entries 59–60
(v0.1); quick-index Plans range → "31–39, 59–60" (appended, not inserted, to avoid an Engine renumber).
Design session only; the Phase-3 implement commit lands integrate.py + tests (→ 2.2).
v2.0 — 2026-06-17 — PLAN-005 implemented (Standard Set Version v1.2 — durable memory): promoted PLAN-005 +
tracker (38–39) 0.1/DRAFT → 1.0/CLOSED; bumped touched cells — root CLAUDE.md 1.2→1.3, template CLAUDE.md
1.1→1.2, project SESSION_OPENER 1.2→1.3, template SESSION_OPENER 1.1→1.2, STANDARDS_INDEX 1.1→1.2;
registered the three new tracked files (`scripts/bootstrap_memory.sh`, `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`,
`docs/NEW_MACHINE_SETUP.md`) as entries 56–58 — appended rather than inserted-in-category to avoid a
full-table renumber (quick-index ranges extended: 1–10,58 / 11–27,57 / 28–29,56). archive/LESSONS.md +
L050 (archive excluded from manifest per Rule 8; LESSONS header unchanged per the established no-per-lesson-bump practice).
v1.9 — 2026-06-17 — Registered PLAN-005 (durable memory — Rule 14 + Set v1.2) DRAFT + its sibling tracker
as entries 38–39 (v0.1). Quick-index Plans range 31–37 → 31–39; Engine range 38–53 → 40–55 (shifted by the
two inserted plan rows). Design session only; the Phase-3 implement commit lands the suite edits (→ 2.0).
v1.8 — 2026-06-16 — PLAN-004 (Slice 3: harvest) implemented: registered the two new engine modules +
two test modules as entries 50–53 (v0.1) — Engine quick-index range 38–49 → 38–53; bumped the touched
code cells (__init__ row 38, cli row 44, test_cli row 49) 0.1→0.2; promoted PLAN-004 + its tracker
(rows 36–37) 0.1/DRAFT → 1.0/CLOSED in the same commit the slice ships. architecture 0.4→0.5,
folder_structure 0.6→0.7 synced same-commit. No Set Version change (no docs/standards/ file touched).
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
| Operating contract + project docs | 1–10, 58, 67 |
| Canonical standards suite (Set v1.5) | 11–27, 57 |
| Governance scripts | 28–29, 56 |
| Archive | 30 |
| Plans | 31–39, 59–60, 63–64, 68–69 |
| Engine (src + tests) | 40–55, 61–62, 65–66 |

## Manifest table

| # | Title | Version | Category | Path |
|---|---|---|---|---|
| 1 | Operating Contract (binding) | 1.7 | Governance | `CLAUDE.md` |
| 2 | Project README | - | Docs | `README.md` |
| 3 | CHANGELOG | - | Docs | `CHANGELOG.md` |
| 4 | Docs Index | - | Docs | `docs/README.md` |
| 5 | Documents Manifest | 2.15 | Governance | `docs/documents_manifest.md` |
| 6 | Folder Structure | 0.12 | Governance | `docs/folder_structure.md` |
| 7 | Architecture (system-design record) | 0.9 | Docs | `docs/architecture.md` |
| 8 | Session Opener (project-local, binding) | 1.6 | Governance | `docs/SESSION_OPENER.md` |
| 9 | Session Closer (project-local, binding) | 1.4 | Governance | `docs/SESSION_CLOSER.md` |
| 10 | Set Version Adopted | 1.6 | Governance | `docs/SET_VERSION_ADOPTED.md` |
| 11 | CLAUDE.md (template) | 1.4 | Standards | `docs/standards/CLAUDE.md` |
| 12 | Lessons Archive (template) | 1.0 | Standards | `docs/standards/LESSONS.md` |
| 13 | Project Standards | 1.0 | Standards | `docs/standards/PROJECT_STANDARDS.md` |
| 14 | Prompt Standards | 1.0 | Standards | `docs/standards/PROMPT_STANDARDS.md` |
| 15 | Project Instructions Template | 1.0 | Standards | `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` |
| 16 | Memory Protocol | 1.0 | Standards | `docs/standards/MEMORY_PROTOCOL.md` |
| 17 | Engineering Standards | 1.0 | Standards | `docs/standards/ENGINEERING_STANDARDS.md` |
| 18 | Validation Standards | 1.0 | Standards | `docs/standards/VALIDATION_STANDARDS.md` |
| 19 | CI/CD Standards | 1.0 | Standards | `docs/standards/CICD_STANDARDS.md` |
| 20 | Session Opener (template) | 1.5 | Standards | `docs/standards/SESSION_OPENER.md` |
| 21 | Session Closer (template) | 1.3 | Standards | `docs/standards/SESSION_CLOSER.md` |
| 22 | Standards README (meta) | 1.0 | Standards | `docs/standards/README.md` |
| 23 | Standards Index (meta) | 1.5 | Standards | `docs/standards/STANDARDS_INDEX.md` |
| 24 | New Project Bootstrap (meta) | 1.5 | Standards | `docs/standards/NEW_PROJECT_BOOTSTRAP.md` |
| 25 | How To Use (meta) | 1.0 | Standards | `docs/standards/HOW_TO_USE.md` |
| 26 | Setup — one-shot prompt (meta) | 1.5 | Standards | `docs/standards/SETUP.md` |
| 27 | Standards Log — experiences-log template (meta) | 1.0 | Standards | `docs/standards/STANDARDS_LOG.md` |
| 28 | Doc Coverage Check | 0.1 | Governance script | `scripts/check_doc_coverage.py` |
| 29 | Test Coverage Drift Check | 0.1 | Governance script | `scripts/check_test_coverage_drift.py` |
| 30 | Lessons Archive (adopter copy) | 1.0 | Governance | `archive/LESSONS.md` |
| 31 | PLAN-001 — domain-neutral suite (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-001_domain_neutral_suite.md` |
| 32 | PLAN-001 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-001_tracker.md` |
| 33 | PLAN-002 — Slice 1 (setup-strip + log + markers) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-002_setup_strip_log_markers.md` |
| 34 | PLAN-003 — Slice 2 (registry + status/drift) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-003_registry_status_drift.md` |
| 35 | PLAN-003 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-003_tracker.md` |
| 36 | PLAN-004 — Slice 3 (harvest) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-004_harvest.md` |
| 37 | PLAN-004 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-004_tracker.md` |
| 38 | PLAN-005 — durable memory (Rule 14 + Set v1.2) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-005_durable_memory.md` |
| 39 | PLAN-005 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-005_tracker.md` |
| 40 | Engine — package marker + CLI version | 0.4 | Engine | `src/standard_document_updater/__init__.py` |
| 41 | Engine — module entry point | 0.1 | Engine | `src/standard_document_updater/__main__.py` |
| 42 | Engine — exception hierarchy | 0.1 | Engine | `src/standard_document_updater/errors.py` |
| 43 | Engine — registry loader | 0.2 | Engine | `src/standard_document_updater/registry.py` |
| 44 | Engine — Set-Version / open-log parsers | 0.1 | Engine | `src/standard_document_updater/setversion.py` |
| 45 | Engine — comparison report | 0.2 | Engine | `src/standard_document_updater/report.py` |
| 46 | Engine — CLI (status / drift / harvest / integrate) | 0.4 | Engine | `src/standard_document_updater/cli.py` |
| 47 | Engine test — shared fixtures | 0.1 | Engine test | `tests/conftest.py` |
| 48 | Engine test — setversion | 0.1 | Engine test | `tests/test_setversion.py` |
| 49 | Engine test — registry | 0.2 | Engine test | `tests/test_registry.py` |
| 50 | Engine test — report | 0.2 | Engine test | `tests/test_report.py` |
| 51 | Engine test — cli | 0.4 | Engine test | `tests/test_cli.py` |
| 52 | Engine — experiences-log entry parser | 0.1 | Engine | `src/standard_document_updater/logentry.py` |
| 53 | Engine — harvest report (open-entry consolidation) | 0.1 | Engine | `src/standard_document_updater/harvest.py` |
| 54 | Engine test — logentry | 0.1 | Engine test | `tests/test_logentry.py` |
| 55 | Engine test — harvest | 0.1 | Engine test | `tests/test_harvest.py` |
| 56 | Project-data locality script | 0.1 | Governance script | `scripts/claude_project_data.sh` |
| 57 | Memory Durability Rollout Prompt (meta) | 1.2 | Standards | `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md` |
| 58 | New-Machine Setup (re-home checklist + Rule 14 migration catalog) | 1.1 | Docs | `docs/NEW_MACHINE_SETUP.md` |
| 59 | PLAN-006 — Slice 4 (integrate) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-006_integrate.md` |
| 60 | PLAN-006 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-006_tracker.md` |
| 61 | Engine — integration worksheet + status write-back | 0.1 | Engine | `src/standard_document_updater/integrate.py` |
| 62 | Engine test — integrate | 0.1 | Engine test | `tests/test_integrate.py` |
| 63 | PLAN-007 — remote transport (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-007_remote_transport.md` |
| 64 | PLAN-007 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-007_tracker.md` |
| 65 | Engine — pluggable target transports (local \| git \| ssh) | 0.1 | Engine | `src/standard_document_updater/transport.py` |
| 66 | Engine test — transport | 0.1 | Engine test | `tests/test_transport.py` |
| 67 | Standards Log — project experiences log | 1.0 | Governance | `docs/STANDARDS_LOG.md` |
| 68 | PLAN-010 — upstream intake: EverOn v2.x → vault (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-010_everon_upstream_intake.md` |
| 69 | PLAN-010 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-010_tracker.md` |

> `.toml` config (`scripts/doc_coverage_allowlist.toml`, `scripts/validation_ownership.toml`) and
> non-versioned config (`.gitlab-ci.yml`, `.gitignore`, MR template) carry no VERSION header and are not
> manifest-tracked per Rule 8; they are documented in `docs/folder_structure.md`.

## Last updated

- **Date**: 2026-08-16
- **Change**: PLAN-010 (upstream intake → Standard Set Version v1.5) implemented — 19 tracked files
  touched + the script swap (entry 56: bootstrap_memory.sh deleted, claude_project_data.sh registered
  in the reused slot); 13 doc cells bumped; PLAN-010 + tracker (68–69) promoted to 1.0/CLOSED;
  quick-index suite caption → Set v1.5; self-row caught up 2.13 → 2.15 (L063 class). Doc + governance-
  script change only; no engine change.
- **Previous change**: PLAN-007 (remote-target transport) implemented — registered transport.py +
  test_transport.py as entries 65–66 (v0.1; Engine range → 40–55, 61–62, 65–66); bumped touched cells;
  promoted PLAN-007 + tracker (63–64) to 1.0/CLOSED. Engine behavior added; no Set Version change.
- **Previous audit**: (none — first audit will be quarterly per `PROJECT_STANDARDS.md` § 2.9)
