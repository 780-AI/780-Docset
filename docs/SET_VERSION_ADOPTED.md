<!-- VERSION: 1.8 -->
<!-- Last Updated: 2026-08-17 -->
<!--
CHANGE LOG
v1.8 — 2026-08-17 — Adopt Standard Set Version v2.0 (PLAN-009 skill delivery: SETUP/NEW_PROJECT_BOOTSTRAP/MEMORY_DURABILITY_ROLLOUT_PROMPT retired; delivery = the vault-side live-reference standard-docset skill). Machinery retirement only — no operative-footprint change; counts unchanged (15 rules / 67 lessons); suite-contents bullet → 11 binding + 3 meta (+ STANDARDS_LOG); added the v2.0 backport row.
v1.7 — 2026-08-16 — Adopt Standard Set Version v1.6 (PLAN-008 sync-enablement: TEMPLATE-ONLY markers + instance-heading PROJECT-OWNED blocks + § 14 stub-keep wording; the `sync` engine ships). Counts unchanged (15 rules / 67 lessons); added the v1.6 backport row.
v1.6 — 2026-08-16 — Adopt Standard Set Version v1.5 (PLAN-010 upstream intake: lessons L057–L067 + NEW Rule 15 + Rule 14 project-data locality upgrade). Updated the adopted-state counts (15 rules / 67 lessons) + added the v1.5 backport row.
v1.5 — 2026-08-16 — Adopt Standard Set Version v1.4 (process-hardening batch: lessons L052–L056 + L051 recurrence #4). Updated the adopted-state lesson count (56) + added the v1.4 backport row.
v1.4 — 2026-06-20 — Adopt Standard Set Version v1.3 (lesson L051 — Rule 13 senior-review pass must mechanically run the linter/type-checker/tests). Updated the adopted-state lesson count (51) + added the v1.3 backport row.
v1.3 — 2026-06-17 — PLAN-005: adopt Standard Set Version v1.2 (durable memory — Rule 14). Updated the adopted-state counts (14 rules / 50 lessons / + rollout-prompt meta file) + added the v1.2 backport row.
v1.2 — 2026-06-14 — Project display name → "Standard DocSet" (the authorship line). Engine package `standard_document_updater` unchanged.
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): relocated from docs/standards/ to docs/ (survives the setup strip); records adoption of Standard Set Version v1.1 (experiences-log template + PROJECT-OWNED markers + setup-and-strip).
v1.0 — 2026-06-07 — Records adoption of Standard Set Version v1.0 (this repo also authors that baseline).
-->
# Standard Set Version Adopted

This project adopts the standards suite at:

- **Standard Set Version:** v2.0 (skill delivery — the SETUP/NEW_PROJECT_BOOTSTRAP/
  MEMORY_DURABILITY_ROLLOUT_PROMPT setup machinery is retired from the set; delivery is the
  vault-side **live-reference standard-docset skill** (bootstrap + adopt modes; PLAN-009).
  Machinery retirement only — no operative-footprint change and `sync` is unaffected; atop the
  v1.x line: v1.6 sync-enablement markers, v1.5 upstream-intake batch L057–L067 + Rule 15 +
  Rule 14 project-data locality, v1.4 process-hardening L052–L056 + the L051 final-indentation
  recurrence, v1.3 Rule 13 linter-enforcement L051, v1.2 durable-memory Rule 14, and v1.1
  experiences-log template + `PROJECT-OWNED` markers)
- **Adopted on:** 2026-08-17 (v1.6 adopted 2026-08-16; v1.5 adopted 2026-08-16; v1.4 adopted 2026-08-16; v1.3 adopted 2026-06-20; v1.2 adopted 2026-06-17; v1.1 adopted 2026-06-13; v1.0 baseline 2026-06-07)
- **Source:** this repository's own `docs/standards/` — `Standard DocSet` both **authors** the
  canonical domain-neutral suite and **adopts** it to govern its own development.

The adopted state:

- **15 standing rules** in `CLAUDE.md` § 3 (Rules 1–15).
- **67 lessons** (L001–L067) in `archive/LESSONS.md`.
- The suite per `docs/standards/STANDARDS_INDEX.md` (11 binding files + 3 meta files + the
  `STANDARDS_LOG.md` template).

## Backport tracking

Because this repo authors the canonical suite, "backport" here means: when the canonical
`docs/standards/` suite is bumped to a new Set Version, reconcile this project's own adopter instances
(root `CLAUDE.md`, `archive/LESSONS.md`, `docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`) and record
the new adopted version below.

| Set Version | Adopted on | Notes |
|---|---|---|
| v2.0 | 2026-08-17 | Skill delivery (PLAN-009): `SETUP.md` + `NEW_PROJECT_BOOTSTRAP.md` + `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` retired from the set; delivery is now the vault-side **live-reference standard-docset skill** (`skill/` + `scripts/bootstrap_skill.sh`; bootstrap + adopt modes; concierge default / self-service clone; step-0 self-pull). Machinery retirement — no adopter footprint change, `sync` unaffected; counts stay 15 rules / 67 lessons. Vault self-adoption same-commit per DD-H: delivery pointers swept in HOW_TO_USE (1.1) / README (1.1) / STANDARDS_LOG (1.1) / session templates (1.7 / 1.5); this repo's own adopter instances carry no operative change. |
| v1.6 | 2026-08-16 | Sync-enablement batch (PLAN-008): the two session templates gain **TEMPLATE-ONLY** banner blocks + **PROJECT-OWNED** instance-heading blocks; template `CLAUDE.md` § 14 marker comment → stub-keep wording; SETUP/NEW_PROJECT_BOOTSTRAP instantiation wording matched (L053 parity). No rule or lesson content change (counts stay 15/67). Reconciled this repo's own adopter instances same-commit per DD-H (`docs/SESSION_OPENER.md` → 1.7, `docs/SESSION_CLOSER.md` → 1.5 — heading blocks wrapped in PROJECT-OWNED; owned-block counts now match the templates 3/3 + 2/2). The engine's `sync` command ships in the same commit (Slice 5 — the harvest → integrate → sync loop is complete). |
| v1.5 | 2026-08-16 | Upstream-intake batch (PLAN-010): lessons **L057–L067** (genericized from an adopter lineage's own line, mapping recorded in PLAN-010 § 3 + CHANGELOG); NEW binding **Rule 15** (post-implementation verification of the NEW behavior); **Rule 14** upgraded in place to project-data locality (`.claude/project-data/` + `scripts/claude_project_data.sh` `status`/`adopt`/`link`, replacing `bootstrap_memory.sh`; open- AND close-side forcing functions). Reconciled this repo's own adopter instances same-commit (root `CLAUDE.md` → 1.7, `archive/LESSONS.md` L057–L067 + L050 note, `docs/SESSION_OPENER.md` → 1.6, `docs/SESSION_CLOSER.md` → 1.4); this repo's store migrated via the one-time `adopt` run. LESSONS file headers unchanged per the no-per-lesson-bump practice. |
| v1.4 | 2026-08-16 | Process-hardening batch: lessons **L052–L056** (installer creates every referenced file; delivery-doc parity set; ALLOWLIST plan+tracker promotion rows; push-state reconcile-at-open / flip-at-close; Phase-3 reconcile-first) + **L051 recurrence #4** (Rule 13 tools run at the final indentation the § 5 code ships at). No rule added or removed. Reconciled this repo's own adopter instances same-commit (root `CLAUDE.md` → 1.6, `archive/LESSONS.md` L052–L056, `docs/SESSION_OPENER.md` → 1.5, `docs/SESSION_CLOSER.md` → 1.3). LESSONS file headers unchanged per the no-per-lesson-bump practice. |
| v1.3 | 2026-06-20 | Lesson **L051** (the Rule 13 senior-review pass must mechanically run the linter / type-checker / tests against a plan's embedded § 5 code, not eyeball it) + a `SESSION_OPENER` § 3.1 universal catalog row. No existing rule changed. Reconciled this repo's own adopter instances (`archive/LESSONS.md` L051, `docs/SESSION_OPENER.md` → 1.4). LESSONS file headers unchanged per the no-per-lesson-bump practice. |
| v1.2 | 2026-06-17 | PLAN-005: added binding **Rule 14** (durable memory); `SESSION_OPENER` § 1.5 self-heal + § 3.1 row; lesson **L050**; new meta file `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`; tracked `scripts/bootstrap_memory.sh`. Reconciled this repo's own adopter instances (root `CLAUDE.md` → 1.3, `archive/LESSONS.md` L050, `docs/SESSION_OPENER.md` → 1.3). |
| v1.1 | 2026-06-13 | PLAN-002 (Slice 1): added the `STANDARDS_LOG.md` experiences-log template; wrapped project-owned blocks in `PROJECT-OWNED` markers (root `CLAUDE.md` + `docs/SESSION_OPENER/CLOSER.md` and their templates); reworked `SETUP.md` (setup-and-strip + log create + SVA→docs/); moved this file from `docs/standards/` to `docs/`. |
| v1.0 | 2026-06-07 | Clean domain-neutral baseline established (PLAN-001). Single-agent adopter (Codex § 14 omitted from this project's own root `CLAUDE.md`; retained in the template). |
