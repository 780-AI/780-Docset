<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Status: APPROVED (Phase 2 — operator approved PLAN-001 + D-A on 2026-06-07; executing in-session) -->
<!--
CHANGE LOG
v0.1 — 2026-06-07 — Initial draft. Plan to (A) scrub all project identity from the canonical standards suite → clean domain-neutral v1.0 baseline; (B) add the missing canonical templates (CLAUDE.md, LESSONS.md); (C) add a one-shot SETUP.md bootstrap prompt and slim HOW_TO_USE to a pointer. Senior-review-and-optimize pass (Rule 13) recorded below as the final Phase-1 task.
-->

# PLAN-001 — Domain-neutral canonical standards suite + one-shot SETUP prompt

## 1. Goal

Turn `docs/standards/` into a **pristine, domain-neutral canonical standards suite** — no project
name (`EverOn`, `Equinex`, `Capital-Signal`) and no source-domain specifics (trading EA, MQL5, MT5,
Hetzner) anywhere — reset to a clean **Set Version v1.0** baseline, made **complete and
distributable**, and fronted by a **single SETUP.md** whose body is a paste-and-run prompt that
bootstraps any new project from scratch.

This is the foundation the tool will later propagate. It also corrects the bootstrap flaw: the suite
currently carries the source project's identity.

## 2. Operator constraints (from the 2026-06-07 Q&A)

- **D1 = (a)** History/CHANGE-LOG blocks **reset to a clean v1.0**; lesson *content* stays, lesson
  *provenance* removed. Per-file VERSION → `1.0`; Set Version → `v1.0`.
- **D2 = (a)** Domain-specific examples **replaced with neutral generic examples** (keep teaching value).
- **D3 = (a)** New `SETUP.md` (one-shot prompt); **HOW_TO_USE slimmed to a pointer** (not deleted).
- **D4 = yes** Scrub the canonical suite (`docs/standards/`) + `archive/LESSONS.md`. This project's own
  adopter files that name `standard-document-updater` (root `CLAUDE.md`, `docs/SESSION_OPENER.md`,
  `docs/SESSION_CLOSER.md`, manifest) are left as adopter instances — but any *EverOn* names inside them
  are also removed (see § 5.E).

## 3. Scope summary

- **A — Scrub** 13 existing `docs/standards/*.md` files to domain-neutral v1.0.
- **B — Complete the suite:** add `docs/standards/CLAUDE.md` (clean template) and
  `docs/standards/LESSONS.md` (clean template) so the suite is self-contained and distributable.
- **C — One-shot setup:** add `docs/standards/SETUP.md` (paste-and-run prompt); slim
  `docs/standards/HOW_TO_USE.md` to a short pointer at SETUP.md.
- **D — Reconcile** this project's own adopter files to the v1.0 baseline (version cells, Set-Version
  references, manifest, SET_VERSION_ADOPTED) and scrub residual EverOn names from `archive/LESSONS.md`.

## 4. Phase tracker

Big plan (Phase 3 lands as >1 commit; multi-file). Sibling tracker:
**`docs/Plans/PLAN-001_tracker.md`** (granular sub-tasks live there per § 15.7).

- Phase 0 — Audit .......... ✅ 2026-06-07 (ref grep complete: ~340 refs, contexts sampled)
- Phase 1 — Design ......... ✅ 2026-06-07 (this file + tracker + Rule 13 senior pass below)
- Phase 2 — Approval ....... ✅ 2026-06-07 — operator approved PLAN-001; D-A = keep § 14 in template
- Phase 3 — Implement ...... ⏸ (see tracker — grouped commits)
- Phase 4 — Validate ....... ⏸
- Phase 5 — Operator gate .. ⏸

## 5. Transformation rules

The scrub is **rule-based**, not 340 literal blocks (the bullet enumeration below IS the rule set).
Each rule is mechanical and verifiable by a follow-up `grep`.

### 5.A — Name removal (applies to every file in scope)

| Find (regex, case-sensitive) | Replace with |
|---|---|
| `EverOn\.Capital-Signal` / `Capital-Signal` | (drop the clause, or `an adopting project`) |
| `EverOn\.Equinex` / `Equinex` | (drop the clause, or `an adopting project`) |
| `EverOn` (standalone) | (drop, or `the standards source`) |
| `~/everon-standards/` | `~/standards-source/` |

Concrete patterns:
- `Example (EverOn.Capital-Signal):` / `Example (EverOn.Equinex …):` → `Example:`
- `Distilled from … EverOn.Capital-Signal Phases 1-3.` → `Distilled from production governance lessons.`
- `cross-project backport from EverOn.Capital-Signal commit \`abc\`` → removed (history reset, § 5.B).
- Lesson provenance (`Project of origin: …`, `(origin: EverOn… )`, `from the EverOn.Equinex … session`)
  → removed; lessons keep the abstract incident + cost + codification only.

### 5.B — History reset (D1) — applies to every file's top HTML comment

Replace each file's multi-entry `CHANGE LOG` block with a single entry:

```
CHANGE LOG
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
```

- Every per-file `<!-- VERSION: X.Y -->` → `<!-- VERSION: 1.0 -->`.
- `STANDARDS_INDEX.md`: § 1 current Set Version → `v1.0`; § 3 per-file table → all `1.0`; § 6 history →
  a single `v1.0 — 2026-06-07 — Clean domain-neutral baseline` entry (prior v1.0–v2.6 history removed).
- `LESSONS.md` count language preserved (49 lessons, L001–L049) — lessons are not renumbered; only their
  provenance is stripped.

### 5.C — Neutral-example mapping (D2)

Prefer **role-based neutral language**; use a concrete neutral example only where one aids understanding.

| Source-domain specific | Neutral replacement |
|---|---|
| "MQL5 Expert Advisor", "the EA", `.mq5`/`.ex5`, "MetaTrader 5"/"MT5" | "the deployable artifact" / "the service" / "the application" |
| "compile in MetaEditor, attach to a chart" | "build and deploy the artifact" |
| "Hetzner VPS" / "Hetzner web console" | "a VPS" / "a cloud provider's web console" |
| "the cent-account `/100` divisor", "wrap-window `end=00:00`" (lesson examples) | keep the abstract lesson (off-by-one / boundary parsing); replace the trading specific with a neutral analogue ("a unit-conversion factor", "an end-of-day time boundary") |
| "docs/business_logic/" | "docs/<domain-spec>/" (generic domain-spec placeholder) |
| live-candle OHLC / settlement-window examples | "a live data feed whose latest record mutates until finalized" |
| DB-specific phrasing where it implies a domain | keep DB as a generic runtime store (DBs are domain-neutral) |

**Rule:** never swap one concrete domain for another concrete domain. Default to role-based wording;
concrete neutral examples only when abstraction would lose clarity.

### 5.D — New canonical files

1. **`docs/standards/CLAUDE.md`** — clean template (placeholders `<project-name>`, `<domain>`,
   `<primary-languages>`, `<deployment-shape>`, `<multi-agent y/n>`; § 4 critical-files placeholder list;
   all 13 rules + § 15 verbatim, domain-neutral; § 14 kept as the OPTIONAL Codex section since the
   *template* must support multi-agent adopters even though *this* project is single-agent).
2. **`docs/standards/LESSONS.md`** — clean template = the scrubbed L001–L049 (canonical copy that the
   suite distributes).
3. **`docs/standards/SETUP.md`** — see § 5.F.

### 5.E — Reconcile this project's adopter files (D4)

- `archive/LESSONS.md` → replace with the scrubbed canonical `LESSONS.md` content (removes its 66 EverOn refs).
- Root `CLAUDE.md` → change the one `Source:` line + CHANGE LOG mention of "Standard Set v2.6" → "v1.0";
  fix the § 14 stub wording that references restoring from a multi-agent project (keep generic).
- `docs/standards/SET_VERSION_ADOPTED.md` → adopted Set Version `v2.6` → `v1.0 (clean domain-neutral
  baseline)`; drop the EverOn source reference.
- `docs/documents_manifest.md` → version cells updated to `1.0` across the suite; add rows for new
  `CLAUDE.md` template, `LESSONS.md` template, `SETUP.md`.
- `docs/SESSION_OPENER.md` / `docs/SESSION_CLOSER.md` (project-local) → the `Set Version v2.6` /
  template-version references updated to v1.0; remove the "Equinex" reference in OPENER § 2 example.
- `README.md` (root) / `CHANGELOG.md` → "Standard Set Version v2.6" → "v1.0"; remove EverOn mention.

### 5.F — SETUP.md (the one-shot prompt)

A short `.md` whose body is a fenced, paste-ready prompt. When pasted into a fresh Claude Code session
opened in (or pointing at) a new empty project dir, the prompt instructs the agent to:

1. Confirm/`git init` the target repo (own repo; warn if the resolved git root is a parent like `$HOME`).
2. Ask **only** the project-specific questions inline (name, domain, languages, deployment shape,
   multi-agent y/n, CI provider) — one block, lettered options, no popups.
3. Copy the canonical suite from a given `--source` path into `docs/standards/` + `CLAUDE.md` (root) +
   `archive/LESSONS.md`; instantiate `docs/SESSION_OPENER.md` + `docs/SESSION_CLOSER.md` from templates.
4. Customize `CLAUDE.md` §1/§4/§13 and (if single-agent) trim §14; build the supporting files,
   governance scripts, CI scaffold, MR template, `SET_VERSION_ADOPTED.md`, manifest, folder structure.
5. Run governance (exit 0), code-review (Rule 10), commit via `-F` (Rule 4), **no push**.

HOW_TO_USE.md is slimmed to: a 1-paragraph intro + "To bootstrap a new project, use `SETUP.md`." + the
supporting prompts (Day-One, code review, audit) kept but scrubbed.

## 6. Spec / doc update map

- `docs/folder_structure.md` → add `docs/standards/{CLAUDE.md,LESSONS.md,SETUP.md}` rows.
- `docs/documents_manifest.md` → § 5.E.
- `CHANGELOG.md` → one entry summarizing the v1.0 clean baseline.

## 7. ALLOWLIST (files this plan may touch)

Existing (scrub): `docs/standards/CICD_STANDARDS.md`, `ENGINEERING_STANDARDS.md`, `HOW_TO_USE.md`,
`MEMORY_PROTOCOL.md`, `NEW_PROJECT_BOOTSTRAP.md`, `PROJECT_INSTRUCTIONS_TEMPLATE.md`,
`PROJECT_STANDARDS.md`, `PROMPT_STANDARDS.md`, `README.md`, `SESSION_CLOSER.md`, `SESSION_OPENER.md`,
`STANDARDS_INDEX.md`, `VALIDATION_STANDARDS.md`, `SET_VERSION_ADOPTED.md`; `archive/LESSONS.md`;
root `CLAUDE.md`; `docs/SESSION_OPENER.md`; `docs/SESSION_CLOSER.md`; `docs/documents_manifest.md`;
`docs/folder_structure.md`; `README.md`; `CHANGELOG.md`.
New: `docs/standards/CLAUDE.md`, `docs/standards/LESSONS.md`, `docs/standards/SETUP.md`;
`docs/Plans/PLAN-001_domain_neutral_suite.md` (this file) + `docs/Plans/PLAN-001_tracker.md`.

## 8. Validation gate (Phase 4)

1. `grep -rIE "EverOn|Equinex|Capital-Signal|Hetzner|MQL5|MetaTrader|MT5|\.mq5|\.ex5|business_logic" docs/standards/ archive/ CLAUDE.md README.md CHANGELOG.md docs/*.md` → **zero hits** (the dispositive scrub check).
2. `grep -rL "VERSION: 1.0" docs/standards/*.md` → only files that legitimately differ (none expected for the suite).
3. Both governance scripts exit 0.
4. `python3 -m py_compile scripts/*.py` clean.
5. **QA scenario (Rule 11):** dry-run SETUP.md mentally against an empty dir — every step references a
   file that exists in the canonical suite; the source-copy step names real paths. (Full live SETUP test
   is a follow-up once we have a throwaway target dir.)

## 9. Operator-approval decision point

Reply **`APPROVE PLAN-001`** to authorize Phase 3. One genuine design decision is surfaced (§ 11 D-A).

## 10. Rollback path

All work is local commits on `master` (no remote). Rollback = `git revert` the Phase-3 commits, or
`git reset` while local-only (per Rule 3, amend only pre-push).

## 11. Known risks + design decisions

- **D-A (RESOLVED 2026-06-07 — operator: keep § 14):** the **template** `docs/standards/CLAUDE.md`
  keeps the OPTIONAL Codex § 14 so multi-agent adopters get it; single-agent adopters trim it via
  SETUP.md. This project's *own* root `CLAUDE.md` stays single-agent (no § 14).
- **R1 — over-scrub of useful examples.** Mitigation: § 5.C prefers role-based wording and keeps
  abstract lessons; reviewed file-by-file in Phase 3, not blind sed.
- **R2 — version-cascade mistakes** (manifest cells vs actual headers drift). Mitigation: § 8 check 2.
- **R3 — SETUP.md drift from the real layout.** Mitigation: SETUP.md is generated from this very
  bootstrap's actual steps; § 8 check 5 dry-runs it.

## 12. Acceptance criteria

- Zero project-name / source-domain hits in the canonical suite (§ 8.1).
- Suite is complete (CLAUDE.md + LESSONS.md + SETUP.md present in `docs/standards/`) and self-describes
  as Set Version v1.0.
- `SETUP.md` is a single paste-and-run prompt that reproduces this bootstrap from scratch.
- Governance green; manifest + folder-structure + CHANGELOG synced.

---

## Senior-review-and-optimize pass (Rule 13) — 2026-06-07

Ran the canonical review prompt against this draft. Findings + fixes applied in place:

1. **Completeness gap fixed.** Initial draft scrubbed `docs/standards/` but the suite had **no
   CLAUDE.md / LESSONS.md template** there — SETUP.md would have nothing domain-neutral to copy as the
   root contract. Added § 5.D (create both templates) + § 3 B. Without this the plan was internally
   inconsistent (SETUP.md § 5.F step 3 references files that wouldn't exist).
2. **Cascade gap fixed.** Resetting the suite to v1.0 silently breaks this project's own version cells
   (manifest lists v2.6-era numbers; root CLAUDE.md/SET_VERSION_ADOPTED say v2.6). Added § 5.E to
   reconcile adopter files + § 8.2 drift check.
3. **Cross-section consistency.** ALLOWLIST (§7) reconciled against every file named in §5 (added the
   adopter files + the two templates + tracker). § 8.1 grep pattern made identical to the Phase-0 audit
   grep so "zero hits" is the exact inverse of the discovery query.
4. **Edge case — `business_logic` and DB.** Distinguished: `business_logic` path is genericized, but a
   DB as a generic runtime store is itself domain-neutral and kept (§ 5.C) — avoids over-scrub.
5. **Surfaced D-A** (template § 14 Codex) rather than silently deciding, per § 10 never-assume.
6. **Optimization:** changed the scrub from "340 literal FIND/REPLACE blocks" to a rule set (§ 5.A–C)
   because the history-reset (§ 5.B) wholesale-removes the majority of references in one transform per
   file — literal blocks would be redundant and fragile.

No new contradictions found after fixes. Plan is internally consistent and ready for Phase 2.
