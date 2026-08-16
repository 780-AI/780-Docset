<!-- VERSION: 1.5 -->
<!-- Last Updated: 2026-08-16 -->
<!--
CHANGE LOG
v1.5 — 2026-08-16 — Adopt Standard Set Version v1.4 (process-hardening batch: lessons L052–L056 + L051 recurrence #4). Updated the adopted-state lesson count (56) + added the v1.4 backport row.
v1.4 — 2026-06-20 — Adopt Standard Set Version v1.3 (lesson L051 — Rule 13 senior-review pass must mechanically run the linter/type-checker/tests). Updated the adopted-state lesson count (51) + added the v1.3 backport row.
v1.3 — 2026-06-17 — PLAN-005: adopt Standard Set Version v1.2 (durable memory — Rule 14). Updated the adopted-state counts (14 rules / 50 lessons / + rollout-prompt meta file) + added the v1.2 backport row.
v1.2 — 2026-06-14 — Project display name → "Standard DocSet" (the authorship line). Engine package `standard_document_updater` unchanged.
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): relocated from docs/standards/ to docs/ (survives the setup strip); records adoption of Standard Set Version v1.1 (experiences-log template + PROJECT-OWNED markers + setup-and-strip).
v1.0 — 2026-06-07 — Records adoption of Standard Set Version v1.0 (this repo also authors that baseline).
-->
# Standard Set Version Adopted

This project adopts the standards suite at:

- **Standard Set Version:** v1.4 (adds process-hardening lessons L052–L056 — installer-creates-what-it-
  references, delivery-doc parity set, ALLOWLIST promotion rows, push-state reconcile/flip, Phase-3
  reconcile-first — plus the L051 final-indentation recurrence; atop v1.3's Rule 13 linter-enforcement
  lesson L051, v1.2's durable-memory Rule 14, and v1.1's `STANDARDS_LOG.md` experiences-log template,
  `PROJECT-OWNED` markers, and setup-and-strip)
- **Adopted on:** 2026-08-16 (v1.3 adopted 2026-06-20; v1.2 adopted 2026-06-17; v1.1 adopted 2026-06-13; v1.0 baseline 2026-06-07)
- **Source:** this repository's own `docs/standards/` — `Standard DocSet` both **authors** the
  canonical domain-neutral suite and **adopts** it to govern its own development.

The adopted state:

- **14 standing rules** in `CLAUDE.md` § 3 (Rules 1–14).
- **56 lessons** (L001–L056) in `archive/LESSONS.md`.
- The suite per `docs/standards/STANDARDS_INDEX.md` (11 binding files + meta files + `SETUP.md` +
  `STANDARDS_LOG.md` + `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`).

## Backport tracking

Because this repo authors the canonical suite, "backport" here means: when the canonical
`docs/standards/` suite is bumped to a new Set Version, reconcile this project's own adopter instances
(root `CLAUDE.md`, `archive/LESSONS.md`, `docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`) and record
the new adopted version below.

| Set Version | Adopted on | Notes |
|---|---|---|
| v1.4 | 2026-08-16 | Process-hardening batch: lessons **L052–L056** (installer creates every referenced file; delivery-doc parity set; ALLOWLIST plan+tracker promotion rows; push-state reconcile-at-open / flip-at-close; Phase-3 reconcile-first) + **L051 recurrence #4** (Rule 13 tools run at the final indentation the § 5 code ships at). No rule added or removed. Reconciled this repo's own adopter instances same-commit (root `CLAUDE.md` → 1.6, `archive/LESSONS.md` L052–L056, `docs/SESSION_OPENER.md` → 1.5, `docs/SESSION_CLOSER.md` → 1.3). LESSONS file headers unchanged per the no-per-lesson-bump practice. |
| v1.3 | 2026-06-20 | Lesson **L051** (the Rule 13 senior-review pass must mechanically run the linter / type-checker / tests against a plan's embedded § 5 code, not eyeball it) + a `SESSION_OPENER` § 3.1 universal catalog row. No existing rule changed. Reconciled this repo's own adopter instances (`archive/LESSONS.md` L051, `docs/SESSION_OPENER.md` → 1.4). LESSONS file headers unchanged per the no-per-lesson-bump practice. |
| v1.2 | 2026-06-17 | PLAN-005: added binding **Rule 14** (durable memory); `SESSION_OPENER` § 1.5 self-heal + § 3.1 row; lesson **L050**; new meta file `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`; tracked `scripts/bootstrap_memory.sh`. Reconciled this repo's own adopter instances (root `CLAUDE.md` → 1.3, `archive/LESSONS.md` L050, `docs/SESSION_OPENER.md` → 1.3). |
| v1.1 | 2026-06-13 | PLAN-002 (Slice 1): added the `STANDARDS_LOG.md` experiences-log template; wrapped project-owned blocks in `PROJECT-OWNED` markers (root `CLAUDE.md` + `docs/SESSION_OPENER/CLOSER.md` and their templates); reworked `SETUP.md` (setup-and-strip + log create + SVA→docs/); moved this file from `docs/standards/` to `docs/`. |
| v1.0 | 2026-06-07 | Clean domain-neutral baseline established (PLAN-001). Single-agent adopter (Codex § 14 omitted from this project's own root `CLAUDE.md`; retained in the template). |
