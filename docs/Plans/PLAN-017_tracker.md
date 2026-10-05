<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-10-05 -->
<!-- Status: DRAFT (Phase 1 complete; awaiting Phase 2 approval) -->
<!--
CHANGE LOG
v0.1 — 2026-10-05 — Created with the plan draft (tracker required per CLAUDE.md § 15.7: Phase 3 lands
as several commits across two repos; Phase 4 has a multi-scenario list, QA-M1…M10; the Windows half
spans sessions).
-->

# PLAN-017 tracker — 780-estimator catch-up + Windows-capable locality tool

## Phase 0 — Audit

- ✅ 2026-10-05 — § 15.9 intake: operator request (no document); inputs recorded (plan § 2).
- ✅ 2026-10-05 — read-only scratch clone of `780-AI/780-estimator` `main` = `45d7c75`: 60 commits,
  Set v1.3 bootstrap `66ac85c`, governance layer changed after bootstrap only in `8b7f1fe`; Windows
  evidence in `scripts/bootstrap_memory.sh`; access: `ls-remote` ✓, no-op `push --dry-run` accepted.
- ✅ 2026-10-05 — engine as oracle on the untouched repo: adopted `?`; dry-run stops at the opener's
  PROJECT-OWNED count (2 vs 3); integration points cited `file:line` (plan § 3).
- ✅ 2026-10-05 — Rule 16 gate: 12 candidates listed + explained + recommended; operator "yes to all
  recommended" (dispositions in plan § 2).

## Phase 1 — Design

- ✅ 2026-10-05 — tool 0.2 + 11 tests proven in a scratch overlay: ruff clean / mypy 0 (25 files,
  `MYPYPATH=src`) / pytest 151; positive control vs 0.1 → exactly the 6 new-behavior tests fail.
- ✅ 2026-10-05 — the whole catch-up proven over the git transport against a local bare remote: prep
  commit → `status` behind → dry-run 7/11 → `--write` 8 files in one engine commit (parent = prep) →
  re-run up-to-date 11/11 → `status` current; post-sync integrity (markers 4/3/2, 15 rules, script
  present); removed-lines set recorded (plan § 8.1).
- ✅ 2026-10-05 — E002 decisions dry-run against the real Capital-Signal log (no write).
- ✅ 2026-10-05 — § 5 generated from the proven blocks (33 blocks; parse round-trip identical).
- ✅ 2026-10-05 — Rule 13 senior-review pass (record at the foot of the plan).

## Phase 2 — Operator approval

- ⏸ D17.A + D-1…D-5 (plan § 9).

## Phase 3 — Implement (fresh session)

- ⏸ 3.0 Pre-checks: vault tree clean at the approval commit; clock vs an external authority →
  `<P3-DATE>`; vault Set Version still v2.7 (else R9); estimator `ls-remote` main (`45d7c75` or
  reconcile); operator confirms Bahereh was told and is not mid-session.
- ⏸ 3.1 Reconcile pass: re-extract all 33 blocks from the plan; every FIND / pre-image / absence check
  passes on the live trees (vault working tree + a fresh writable estimator clone in the scratchpad).
- ⏸ 3.2 Vault § 5a, 5b, 5c, 5f, 5g applied → QA-M1, QA-M2, QA-M3, QA-M10.
- ⏸ 3.3 Estimator § 5h–5n applied on the clone → QA-M4 → Rule 10 review table → commit (§ 5o,
  `-F`) → operator "go" → push to `main` → `ls-remote`.
- ⏸ 3.4 Vault § 5d + 5e applied (registry entry + opener row) → `status` → dry-run → `--diff` ==
  § 8.1 → `sync --project 780-estimator --write` → QA-M5, QA-M6.
- ⏸ 3.5 CS E002 write-back (§ 5p) → QA-M7.
- ⏸ 3.6 § 6c / 6d / 6e bookkeeping → governance (stdout pasted) → Rule 10 review table → vault commit
  (§ 7.5; no push) → OPEN_TASKS (§ 6g). Operator relays the § 5n steps to Bahereh.

## Phase 4 — Validate

| # | Scenario | Phase | Status | Date | Evidence |
|---|---|---|---|---|---|
| QA-M1 | Tools (ruff / mypy / pytest 151) | 3.2 | ⏸ | | |
| QA-M2 | Tests go red on tool 0.1 (6 of 11) | 3.2 | ⏸ | | |
| QA-M3 ⚑ | Vault's own locality `status` OK | 3.2 | ⏸ | | |
| QA-M4 ⚑ | Prep proof (governance + engine oracle) | 3.3 | ⏸ | | |
| QA-M5 ⚑ | First live git write | 3.4 | ⏸ | | |
| QA-M6 ⚑ | Post-sync integrity | 3.4 | ⏸ | | |
| QA-M7 ⚑ | CS E002 write-back | 3.5 | ⏸ | | |
| QA-M8 ⚑ | Windows `adopt` on the owner's PC | post-3 | ⏸ | | |
| QA-M9 ⚑ | Handoff landing observed | post-3 | ⏸ | | |
| QA-M10 | Domain-neutral grep | 3.2 | ⏸ | | |

**Waiver register (Rule 15):** _(none)_

## Phase 5 — Operator gate

- ⏸ Push the vault commits to BOTH remotes (`origin` GitLab + `github` 780-AI/780-Docset) +
  `ls-remote` both (no tag — no Set Version change).
- ⏸ Closure commit (§ 7.6) after QA-M8 + QA-M9 (or the D-3 = B waiver).
