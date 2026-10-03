<!-- VERSION: 1.15 -->
<!-- Last Updated: 2026-10-03 -->
<!--
CHANGE LOG
v1.15 — 2026-10-03 — Adopt Standard Set Version v2.7 (PLAN-011 fleet-convergence intake from EverOn.Equinex, operator-confirmed at the Rule 16 gate: L080 + template CLAUDE.md § 15.9 feature intake; L081 + the Rule 14 cloud-synced-folder bullet; Rule 12 step 6 drift fix). Counts → 81 lessons / 16-own rules. Own-instance reconcile same-commit: root CLAUDE.md → 1.9 mirrors all three CLAUDE.md changes; `archive/LESSONS.md` gains the L080–L081 provenance entry; added the v2.7 backport row.
v1.14 — 2026-10-03 — Adopt Standard Set Version v2.6 (clock trust: lesson L079 + PROJECT_STANDARDS § 5.6 stamp-date check — 780-VPN's E001 via harvest under the Rule 16 gate). Counts → 79 lessons / 16-own rules. Own-instance reconcile: the vault reads PROJECT_STANDARDS from docs/standards/ directly (no instance); `archive/LESSONS.md` gains the project-specific L079 same-commit; added the v2.6 backport row.
v1.13 — 2026-09-05 — Adopt Standard Set Version v2.5 (PLAN-012 sync handoff: every engine write into a target leaves docs/SYNC_HANDOFF.md; SESSION_OPENER template → 1.8 with the § 1.1 engine-handoff check; LESSONS → 1.2 date-line corrections). Counts unchanged (78/16-own). Own-instance reconcile: no operative change (the engine never writes into the vault — the § 1.1 check is target-side; own instance wording deferred-minor); added the v2.5 backport row.
v1.12 — 2026-08-27 — Adopt Standard Set Version v2.4 (environment portability: the Rule 2 Runner note — command examples generic, substitute runner/CI flavor at run time). Counts unchanged (78/16-own). Own root CLAUDE.md keeps its env-specific wording (a legitimate instance state under the new note — vault runs plain `python` + GitLab); added the v2.4 backport row.
v1.11 — 2026-08-27 — Adopt Standard Set Version v2.3 (first adopter-originated lesson intake under the Rule 16 operator gate: L069–L078 + LESSONS ownership banner + SESSION_CLOSER binding E0NN rule). Counts → 78 lessons; own-instance state now 16 rules (project Rule 16 atop the Set's 15); added the v2.3 backport row.
v1.10 — 2026-08-19 — Adopt Standard Set Version v2.2 (domain-neutral scrub: residual real-username example paths in MEMORY_PROTOCOL + PROJECT_INSTRUCTIONS_TEMPLATE → /Users/you/...). Counts unchanged (68 lessons / 15 rules); added the v2.2 backport row. Own adopter instances carry no operative change (neither scrubbed file is instantiated per-project).
v1.9 — 2026-08-18 — Adopt Standard Set Version v2.1 (first harvest → integrate cycle, adopter entry E001: SESSION_CLOSER template § 1.2 → SET_VERSION_ADOPTED reference + lesson L068). Counts → 68 lessons; added the v2.1 backport row. Own-instance reconcile: `docs/SESSION_CLOSER.md` § 1.2 already reads the adoption record (customized at bootstrap) — no operative change; `archive/LESSONS.md` gains the project-specific L068 same-commit.
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

- **Standard Set Version:** v2.7 (fleet-convergence intake: lesson L080 + CLAUDE.md § 15.9 Feature
  intake — every new feature and feature document goes preserve → investigate → redesign → plan;
  lesson L081 + the Rule 14 cloud-synced-folder bullet; Rule 12 step 6 aligned with SESSION_CLOSER
  § 1.6 — from an operator adopter's own-line suite, gathered before its convergence.
  Atop v2.6: clock trust — lesson L079, the machine clock is an untrusted
  input, verify against an external authority before stamping or recording skew — plus the
  PROJECT_STANDARDS § 5.6 stamp-date check; from a team adopter's E001 via harvest.
  Atop v2.5: sync handoff — every engine write into a target — `sync
  --write` AND the integrate write-back — leaves the engine-transient `docs/SYNC_HANDOFF.md`
  explaining what landed and what bookkeeping remains; SESSION_OPENER § 1.1 engine-handoff
  check; LESSONS L069–L078 date lines corrected for the vault clock skew.
  Atop v2.4: environment portability — the contract's command examples are
  generic per the Rule 2 Runner note; adopters substitute their Python runner / CI flavor at
  run time instead of editing suite-owned text.
  Atop v2.3: first adopter-originated lesson intake, under the operator
  gate: lessons L069–L078 — the intake-gate incident + nine rescued adopter lessons — plus the
  LESSONS ownership banner and the SESSION_CLOSER § 1.7 binding E0NN codification rule.
  Atop v2.2: domain-neutral scrub — residual real-username example paths
  genericized in MEMORY_PROTOCOL + PROJECT_INSTRUCTIONS_TEMPLATE, the identifier-token class.
  Atop v2.1: adopter-reference fix — SESSION_CLOSER § 1.2 reads the Set
  Version from the adoption record `docs/SET_VERSION_ADOPTED.md`; + lesson L068. The first Set
  bump produced by the experiences-log harvest → integrate cycle (adopter entry E001). Atop
  v2.0 skill delivery — the SETUP/NEW_PROJECT_BOOTSTRAP/MEMORY_DURABILITY_ROLLOUT_PROMPT setup
  machinery retired; delivery is the vault-side **live-reference standard-docset skill**
  (bootstrap + adopt modes; PLAN-009) — and the v1.x line: v1.6 sync-enablement markers, v1.5
  upstream-intake batch L057–L067 + Rule 15 + Rule 14 project-data locality, v1.4
  process-hardening L052–L056 + the L051 final-indentation recurrence, v1.3 Rule 13
  linter-enforcement L051, v1.2 durable-memory Rule 14, and v1.1 experiences-log template +
  `PROJECT-OWNED` markers)
- **Adopted on:** 2026-10-03 (v2.6 adopted 2026-10-03; v2.5 adopted 2026-09-05; v2.4 adopted 2026-08-27; v2.3 adopted 2026-08-27; v2.2 adopted 2026-08-19; v2.1 adopted 2026-08-18; v2.0 adopted 2026-08-17; v1.6 adopted 2026-08-16; v1.5 adopted 2026-08-16; v1.4 adopted 2026-08-16; v1.3 adopted 2026-06-20; v1.2 adopted 2026-06-17; v1.1 adopted 2026-06-13; v1.0 baseline 2026-06-07)
- **Source:** this repository's own `docs/standards/` — `Standard DocSet` both **authors** the
  canonical domain-neutral suite and **adopts** it to govern its own development.

The adopted state:

- **16 standing rules** in `CLAUDE.md` § 3 (Rules 1–15 from the Set + project-specific Rule 16,
  the operator intake gate — vault-only; the template stays at 15).
- **81 lessons** (L001–L081) in `archive/LESSONS.md` (L070–L078 and L080–L081 recorded there as
  provenance-table intake entries; full genericized texts in the canonical file).
- The suite per `docs/standards/STANDARDS_INDEX.md` (11 binding files + 3 meta files + the
  `STANDARDS_LOG.md` template).

## Backport tracking

Because this repo authors the canonical suite, "backport" here means: when the canonical
`docs/standards/` suite is bumped to a new Set Version, reconcile this project's own adopter instances
(root `CLAUDE.md`, `archive/LESSONS.md`, `docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`) and record
the new adopted version below.

| Set Version | Adopted on | Notes |
|---|---|---|
| v2.7 | 2026-10-03 | Fleet-convergence intake (PLAN-011 Phase 3a — EverOn.Equinex's own-line suite, gathered before its convergence; Rule 16 gate C1–C7, operator "confirmed as recommended" 2026-10-03: C1–C4 integrated, C5–C7 kept as Equinex customizations): lesson L080 + template CLAUDE.md → 1.7 (§ 15.9 Feature intake + § 15.2 Phase 0 pointer — landed in § 15 so no rule renumbers, D-6 = A), lesson L081 + Rule 14 cloud-synced-folder bullet, Rule 12 step 6 drift fix; README → 1.5 (count). Own-instance reconcile: root `CLAUDE.md` → 1.9 mirrors all three; `archive/LESSONS.md` gains the L080–L081 provenance entry. Vault Set v2.7 ≠ Equinex's own-line "v2.7" (R6). Counts → 81 lessons / 16-own rules. |
| v2.6 | 2026-10-03 | Clock trust (the second harvested adopter entry — 780-VPN E001, operator-confirmed at the Rule 16 gate 2026-10-03): lesson L079 (machine clock = untrusted input; verify against an external authority before stamping or recording skew — merged with the vault's own skew-record correction) + PROJECT_STANDARDS → 1.1 (§ 5.6 stamp-date check) + README → 1.4 (count). Own-instance reconcile: PROJECT_STANDARDS has no vault instance (read directly from `docs/standards/`); `archive/LESSONS.md` gains the project-specific L079 same-commit. E001's engine half routed to its own plan. Counts → 79 lessons / 16-own rules. |
| v2.5 | 2026-09-05 | Sync handoff (PLAN-012 — a target session opened to unexplained engine-written files): every engine write (`sync --write` + integrate write-back) now also writes + flushes `docs/SYNC_HANDOFF.md` (engine-transient, never manifest-listed, deleted by the target's landing commit); SESSION_OPENER → 1.8 (§ 1.1 engine-handoff check); LESSONS → 1.2 (L069–L078 date-line corrections — vault clock ran ~9d slow at intake). Own-instance reconcile: no operative change — the engine writes INTO targets, never into the vault, so the § 1.1 engine-handoff check has nothing to fire on here; own `docs/SESSION_OPENER.md` picks the wording up at its next instance reconcile (deferred-minor). Counts unchanged (78/16-own). |
| v2.4 | 2026-08-27 | Environment portability (the Runner note — found via a live team adopter whose runner/CI adaptations in suite-owned contract text were reverted by sync): template CLAUDE.md → 1.6 (Rule 2 binding Runner note; Rule 5 + § 8.6 CI-flavor-neutral). Own-instance reconcile: root `CLAUDE.md` untouched — its env-specific wording (plain `python`, GitLab) is a legitimate instance state under the new note; no operative change. Counts unchanged. |
| v2.3 | 2026-08-27 | First adopter-originated lesson intake (nine lessons rescued from a team adopter's engine-owned archive — the L069 incident — genericized and integrated as L070–L078 under the new Rule 16 operator gate, all nine operator-confirmed) + L069 itself + LESSONS ownership banner (→ 1.1) + SESSION_CLOSER § 1.7 binding E0NN rule (→ 1.7). Own-instance reconcile same-commit: `archive/LESSONS.md` gains L070–L078 as the provenance-table entry (dual-voice); root `CLAUDE.md` already carries Rule 16 (added 2026-08-27, pre-release); own SESSION_CLOSER instance § 1.7 wording — vault codifies directly by design, no operative change. Counts → 78 lessons. |
| v2.2 | 2026-08-19 | Domain-neutral scrub (identifier-token class, found by the v2.1 release-gate grep): 4 example paths `/Users/parsaazad/...` → `/Users/you/...` — MEMORY_PROTOCOL (3 sites, → 1.1) + PROJECT_INSTRUCTIONS_TEMPLATE (1 site, → 1.1). Counts unchanged (68/15). Own adopter instances: no operative change (neither file is instantiated per-project; MEMORY_PROTOCOL is replace-class in the SYNC_MAP — registered targets receive it at their next `sync`). |
| v2.1 | 2026-08-18 | Adopter-reference fix (first harvest → integrate cycle, adopter entry E001): SESSION_CLOSER template § 1.2 retargeted `docs/standards/STANDARDS_INDEX.md` → `docs/SET_VERSION_ADOPTED.md` (adopters don't carry the INDEX; the adoption record exists on both sides) + lesson L068 (template cross-references must resolve in the adopter). Own-instance reconcile: `docs/SESSION_CLOSER.md` § 1.2 already reads the adoption record (customized at bootstrap v1.0) — no operative change; `archive/LESSONS.md` gains the project-specific L068 same-commit. Counts → 68 lessons. Also swept: stale standards README lesson count 48 → 68 (drifted since v1.4, L060-class). |
| v2.0 | 2026-08-17 | Skill delivery (PLAN-009): `SETUP.md` + `NEW_PROJECT_BOOTSTRAP.md` + `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` retired from the set; delivery is now the vault-side **live-reference standard-docset skill** (`skill/` + `scripts/bootstrap_skill.sh`; bootstrap + adopt modes; concierge default / self-service clone; step-0 self-pull). Machinery retirement — no adopter footprint change, `sync` unaffected; counts stay 15 rules / 67 lessons. Vault self-adoption same-commit per DD-H: delivery pointers swept in HOW_TO_USE (1.1) / README (1.1) / STANDARDS_LOG (1.1) / session templates (1.7 / 1.5); this repo's own adopter instances carry no operative change. |
| v1.6 | 2026-08-16 | Sync-enablement batch (PLAN-008): the two session templates gain **TEMPLATE-ONLY** banner blocks + **PROJECT-OWNED** instance-heading blocks; template `CLAUDE.md` § 14 marker comment → stub-keep wording; SETUP/NEW_PROJECT_BOOTSTRAP instantiation wording matched (L053 parity). No rule or lesson content change (counts stay 15/67). Reconciled this repo's own adopter instances same-commit per DD-H (`docs/SESSION_OPENER.md` → 1.7, `docs/SESSION_CLOSER.md` → 1.5 — heading blocks wrapped in PROJECT-OWNED; owned-block counts now match the templates 3/3 + 2/2). The engine's `sync` command ships in the same commit (Slice 5 — the harvest → integrate → sync loop is complete). |
| v1.5 | 2026-08-16 | Upstream-intake batch (PLAN-010): lessons **L057–L067** (genericized from an adopter lineage's own line, mapping recorded in PLAN-010 § 3 + CHANGELOG); NEW binding **Rule 15** (post-implementation verification of the NEW behavior); **Rule 14** upgraded in place to project-data locality (`.claude/project-data/` + `scripts/claude_project_data.sh` `status`/`adopt`/`link`, replacing `bootstrap_memory.sh`; open- AND close-side forcing functions). Reconciled this repo's own adopter instances same-commit (root `CLAUDE.md` → 1.7, `archive/LESSONS.md` L057–L067 + L050 note, `docs/SESSION_OPENER.md` → 1.6, `docs/SESSION_CLOSER.md` → 1.4); this repo's store migrated via the one-time `adopt` run. LESSONS file headers unchanged per the no-per-lesson-bump practice. |
| v1.4 | 2026-08-16 | Process-hardening batch: lessons **L052–L056** (installer creates every referenced file; delivery-doc parity set; ALLOWLIST plan+tracker promotion rows; push-state reconcile-at-open / flip-at-close; Phase-3 reconcile-first) + **L051 recurrence #4** (Rule 13 tools run at the final indentation the § 5 code ships at). No rule added or removed. Reconciled this repo's own adopter instances same-commit (root `CLAUDE.md` → 1.6, `archive/LESSONS.md` L052–L056, `docs/SESSION_OPENER.md` → 1.5, `docs/SESSION_CLOSER.md` → 1.3). LESSONS file headers unchanged per the no-per-lesson-bump practice. |
| v1.3 | 2026-06-20 | Lesson **L051** (the Rule 13 senior-review pass must mechanically run the linter / type-checker / tests against a plan's embedded § 5 code, not eyeball it) + a `SESSION_OPENER` § 3.1 universal catalog row. No existing rule changed. Reconciled this repo's own adopter instances (`archive/LESSONS.md` L051, `docs/SESSION_OPENER.md` → 1.4). LESSONS file headers unchanged per the no-per-lesson-bump practice. |
| v1.2 | 2026-06-17 | PLAN-005: added binding **Rule 14** (durable memory); `SESSION_OPENER` § 1.5 self-heal + § 3.1 row; lesson **L050**; new meta file `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`; tracked `scripts/bootstrap_memory.sh`. Reconciled this repo's own adopter instances (root `CLAUDE.md` → 1.3, `archive/LESSONS.md` L050, `docs/SESSION_OPENER.md` → 1.3). |
| v1.1 | 2026-06-13 | PLAN-002 (Slice 1): added the `STANDARDS_LOG.md` experiences-log template; wrapped project-owned blocks in `PROJECT-OWNED` markers (root `CLAUDE.md` + `docs/SESSION_OPENER/CLOSER.md` and their templates); reworked `SETUP.md` (setup-and-strip + log create + SVA→docs/); moved this file from `docs/standards/` to `docs/`. |
| v1.0 | 2026-06-07 | Clean domain-neutral baseline established (PLAN-001). Single-agent adopter (Codex § 14 omitted from this project's own root `CLAUDE.md`; retained in the template). |
