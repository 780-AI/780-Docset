<!-- VERSION: 0.4 -->
<!-- Last Updated: 2026-10-07 -->
<!-- Status: EXECUTING — Phase 3b revision DRAFT (QA-M9 ✅; QA-M8 re-runs with tool 0.3) -->
<!--
CHANGE LOG
v0.4 — 2026-10-07 — QA-M9 ✅ (evidence); QA-M8 partial evidence + the 2026-10-06 incident record; Phase
1b ✅ (tool 0.3 proven, replay, Rule 13), Phase 2b / 3b sub-tasks ⏸; QA-M11…M16 rows; Phase 5 push ✅.
v0.3 — 2026-10-05 — Phase 3 executed in a fresh session (3.0–3.6 ✅); QA-M1…M7 + M10 ✅ with evidence;
plan defect D1 (§ 8.1 wording; operator D1 = A); QA-M7 idle-gate process note. QA-M8 / M9 ⏸ (owner's PC).
v0.2 — 2026-10-05 — Phase 2 approval recorded ("Plan-017 is approved"; decisions in plan § 9.1).
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

- ✅ 2026-10-05 — "Plan-017 is approved" — D17.A; D-1…D-5 = A (plan § 9.1). Plan + tracker → 0.2.

## Phase 3 — Implement (fresh session)

- ✅ 2026-10-05 — 3.0 Pre-checks: vault tree clean at `b2f6aa3` (after the approval commit only PLAN-016
  bookkeeping moved — CHANGELOG, manifest, PLAN-016 tracker; no block anchor among them); local clock ==
  `gitlab.com` / `apple.com` `Date:` within 2 s → `<P3-DATE>` = 2026-10-05; vault Set Version v2.7 (R9
  not triggered); estimator `ls-remote` main = `45d7c75` (R8 not triggered); operator: "Bahereh told +
  idle".
- ✅ 2026-10-05 — 3.1 Reconcile pass: all 33 blocks re-extracted from the plan by a parser and checked
  sequentially per file on the live trees (vault working tree + a fresh writable estimator clone in the
  session scratchpad) — every FIND matched once, both pre-image blobs matched (`c746047…`, `6ee9fc2…`),
  both NEW files absent, the § 5k copy source present. **Zero block defects.** Checker positive control:
  one FIND corrupted → exactly 1 FAIL.
- ✅ 2026-10-05 — 3.2 Vault § 5a, 5b, 5c, 5f, 5g applied (`<P3-DATE>` substituted; script mode 100755
  kept) → QA-M1, QA-M2, QA-M3, QA-M10 ✅.
- ✅ 2026-10-05 — 3.3 Estimator § 5h–5n applied on the clone (7 files == § 7.2; § 5k `cmp` identical,
  mode 755) → QA-M4 ✅ → Rule 10 review table posted → commit `b4cae64` (§ 5o message via `-F`, author
  Yaser Khosravi, parent `45d7c75`) → operator "go D1 = A" → pushed `45d7c75..b4cae64` → `ls-remote` main
  = `b4cae64`. Clones deleted after use.
- ✅ 2026-10-05 — 3.4 Vault § 5d + 5e applied (after the prep was on their `main`) → `status` behind →
  dry-run 7/11 → `--diff` identical to the QA-M4 oracle diff → operator "go" → `sync --project
  780-estimator --write` → QA-M5, QA-M6 ✅.
- ✅ 2026-10-05 — 3.5 Capital-Signal E002 write-back (§ 5p TOML extracted verbatim) → QA-M7 ✅ (process
  note below).
- ✅ 2026-10-05 — 3.6 § 6c / 6d / 6e bookkeeping → governance (stdout pasted in chat) → Rule 10 review
  table → vault commit (§ 7.5; no push) → OPEN_TASKS (§ 6g).

> **Plan defect D1 (wording; operator D1 = A, 2026-10-05).** § 8.1 listed removed lines for the merge /
> record files only; the dry-run also removes 3 non-header lines from the replace-mode
> `docs/standards/MEMORY_PROTOCOL.md`. Investigated before any write: the estimator's three changed
> replace-mode files (PROJECT_STANDARDS, MEMORY_PROTOCOL, LESSONS) are byte-identical to the vault's
> `set-v1.3` blobs (`cfbaff0`, `ac947df`, `b30f618`) — no local text; the 3 lines are the vault's v2.2
> identifier scrub (`64a5752`). § 8.1 gains one sentence (plan v0.3).
>
> **Process note (QA-M7 idle gate).** The idle re-check ran in the same command as `integrate --write`, so
> it printed instead of gating: it listed one Capital-Signal transcript changed in the last 10 minutes.
> Investigation (plain reads, no git in that repo): a session on the operator's other Mac had posted its
> completed wrap-up block at 21:26:42 local, ~7 minutes before the write (clean tree; its one commit
> `08b638d` touched neither written file); `STANDARDS_LOG.md` held E001 + E002 only, header unchanged; no
> conflicted copies; no handoff existed before. No collision — but a check that cannot stop the action is
> not a gate; gating checks run as separate steps from here on (lesson candidate in OPEN_TASKS).

## Phase 1b — Phase 3b design (revision, 2026-10-07)

- ✅ 2026-10-06 — Incident investigated (read-only: vault side + the owner's Claude): tool 0.2 has no path
  that empties the store; root cause a manual Explorer move of the junction (plan § 2); the store
  recovered from the Recycle Bin (14 memories byte-identical; two transcripts re-assembled before `link`).
- ✅ 2026-10-07 — Operator: "A" (fix inside this plan before closing).
- ✅ 2026-10-07 — tool 0.3 + tests 0.2 proven in a scratch overlay: ruff clean / mypy 0 (25 files,
  `MYPYPATH=src`) / `bash -n` clean / pytest 163; positive control vs 0.2 → 13 failed / 10 passed.
- ✅ 2026-10-07 — replay of the owner's post-incident state, both orders (plan § 8.2 QA-M14 outputs).
- ✅ 2026-10-07 — § 5q–5w generated from the proven files; Rule 13 pass (record at the foot of the plan).

## Phase 2b — Operator approval of the revision

- ⏸ D17.B + D-6…D-9 (plan § 9.2).

## Phase 3b — Implement (fresh session)

- ⏸ 3b.0 Pre-checks: clock vs an external authority → `<P3B-DATE>`; vault tree clean; estimator
  `ls-remote` main (`1ddbbf9` expected — otherwise plan § 6i); the operator has told the owner (R15).
- ⏸ 3b.1 Reconcile pass: § 5q–5v + § 5w re-extracted from the plan; pre-blobs `4e3d1f0…` (vault tool and
  their copy) + `f66fc29…` (tests); every FIND matched once.
- ⏸ 3b.2 Vault § 5q, 5r, 5s → QA-M11…M15.
- ⏸ 3b.3 Estimator § 5t–5v on a fresh clone → their governance 0 / 0 → Rule 10 review → operator "go" →
  commit (§ 5w via `-F`) → push → QA-M16.
- ⏸ 3b.4 § 6h bookkeeping → governance → Rule 10 review → vault commit (§ 7.9; no push) → OPEN_TASKS.

## Phase 4 — Validate

| # | Scenario | Phase | Status | Date | Evidence |
|---|---|---|---|---|---|
| QA-M1 | Tools (ruff / mypy / pytest 151) | 3.2 | ✅ | 2026-10-05 | `ruff check src tests` → All checks passed; `MYPYPATH=src mypy --cache-dir <fresh> src tests` (strict) → no issues in 25 source files; pytest → 151 passed |
| QA-M2 | Tests go red on tool 0.1 (6 of 11) | 3.2 | ✅ | 2026-10-05 | the 11 tests vs a scratch copy of 0.1 → 6 failed (2 POSIX E002 + 4 Windows), 5 passed (the baseline cases) |
| QA-M3 ⚑ | Vault's own locality `status` OK | 3.2 | ✅ | 2026-10-05 | before: `STATUS: OK (18 memory files)`; with 0.2: `symlink: -> …/.claude/project-data`, `STATUS: OK (18 memory files)`, exit 0 |
| QA-M4 ⚑ | Prep proof (governance + engine oracle) | 3.3 | ✅ | 2026-10-05 | their `check_doc_coverage.py` / `check_test_coverage_drift.py --ci` exit 0 / 0; scratch vault (`git archive HEAD`, registry → the clone, local transport): `status` v1.3 / v2.7 behind; dry-run 7 of 11 (the § 3 seven); removed lines CLAUDE 28 / opener 19 / closer 6 / SVA 3 == § 8.1, line set matches its description; replace-mode removals explained (D1) |
| QA-M5 ⚑ | First live git write | 3.4 | ✅ | 2026-10-05 | `status` (git read path) 780-estimator v1.3 / v2.7 behind; dry-run 7/11; live `--diff` identical to the QA-M4 oracle diff; `--write` → "wrote + flushed 8 file(s) (incl. the handoff)"; `ls-remote` main `b4cae64` → `fdb87b9`; `fdb87b9` parent = `b4cae64`, author `Standard DocSet <standard-docset@localhost>`; `git show --stat` = the 8 files of § 7.3; re-run up-to-date 11/11 (notes the un-landed handoff); `status` v2.7 / v2.7 current; `docs/fleet.csv` row: registry columns == § 5d (registered_on 2026-10-05), `reachable` yes, `handoff_pending` 1 |
| QA-M6 ⚑ | Post-sync integrity | 3.4 | ✅ | 2026-10-05 | fresh clone of `main`: PROJECT-OWNED BEGIN/END CLAUDE 4/4, opener 3/3, closer 2/2; 15 `### Rule` headings; Rule 14 names `scripts/claude_project_data.sh` (4×), file present + executable; opener heading (l.14) + § 2 "Current state" note (l.92) + § 3.2 popup row intact; closer heading (l.13); SVA bullets v2.7 / 2026-10-05, rows v2.7 + v1.3 |
| QA-M7 ⚑ | CS E002 write-back | 3.5 | ✅ | 2026-10-05 | operator "go" (no CS session); dry-run → `--write` → Status read back == § 5p's rendering verbatim; CS `docs/SYNC_HANDOFF.md` new, `### Write 1` = integrate write-back of `docs/STANDARDS_LOG.md`; `harvest` → "No open log entries across registered projects" (780-Automation skipped, unreachable). Idle-gate process note above |
| QA-M8 ⚑ | Windows `adopt` on the owner's PC — re-run with 0.3 (plan § 8.2) | post-3b | ⏸ | 2026-10-06 (partial) | before: 14 (stated beforehand); Git Bash `adopt` → "Adopted." + `STATUS: OK (14 memory files)`; `link` → "Already linked." — then the store was emptied by a manual Explorer move (incident below); remaining sub-checks in plan § 8.2 |
| QA-M9 ⚑ | Handoff landing observed | post-3 | ✅ | 2026-10-06 | `ls-remote` main `fdb87b9` → `1ddbbf9`; fresh clone: `7e466f8` = CHANGELOG + manifest 1.57 (cells == headers) + `docs/SYNC_HANDOFF.md` deleted; `1ddbbf9` = `bootstrap_memory.sh` + its manifest row + tree line removed (manifest 1.58, CHANGELOG 1.41, folder_structure 1.18); linear, governance paths only; their tool blob `4e3d1f0` == the vault's; vault `status` 780-estimator v2.7 current, fleet `handoff_pending` 0 |
| QA-M10 | Domain-neutral grep | 3.2 | ✅ | 2026-10-05 | `grep -rniE "780\|estimator\|everon\|equinex\|capital-signal\|bahereh\|parsaazad\|a780" skill/ docs/standards/ scripts/claude_project_data.sh tests/test_claude_project_data.py` → no output, exit 1; control: same pattern on `config/projects.toml` → 23 hits |
| QA-M11 | Tools (ruff / mypy / pytest 163) | 3b | ⏸ | | |
| QA-M12 | Tests go red on tool 0.2 (13 of 23) | 3b | ⏸ | | |
| QA-M13 ⚑ | Vault's own locality `status` + `cleanup` | 3b | ⏸ | | |
| QA-M14 ⚑ | Replay of the owner's state, both orders | 3b | ⏸ | | |
| QA-M15 | Domain-neutral grep | 3b | ⏸ | | |
| QA-M16 ⚑ | Delivery commit on their `main` | 3b | ⏸ | | |

**Waiver register (Rule 15):** _(none)_

> **Incident 2026-10-06 (QA-M8, the owner's PC).** At 09:35 `adopt` ran correctly. At 09:45 the junction
> and the tool's backup beside it were cut into a new Desktop folder in Explorer; moving the junction moved
> the real files (E: → C:) and emptied `.claude/project-data/`; the leftover junction was recycled at
> 09:45:55 and the Desktop folder at 09:52:53; Claude Code then wrote into a fresh plain harness dir. The
> owner's opener § 1.5 halt-on-empty caught it at her next session (17:04). Evidence: Recycle Bin items +
> deletion times, folder timestamps, no shell-history hits (her Claude, read-only). Recovered from the
> Recycle Bin by her Claude: 14 memories byte-identical; the two transcripts' re-assembly sent with the
> `link` steps. Tool 0.2 has no path that empties the store; the design gaps F1 / F2 are Phase 3b.

## Phase 5 — Operator gate

- ✅ 2026-10-06 — Vault push (`fb8960c`) to BOTH remotes (`origin` GitLab + `github` 780-AI/780-Docset):
  governance exit 0 / 0; `ls-remote` origin master = github master = `fb8960c` = HEAD; no tag.
- ⏸ Push the Phase 3b vault commits to BOTH remotes + `ls-remote` both (no tag).
- ⏸ Closure commit (§ 7.6) after QA-M8 (re-run with 0.3) — QA-M9 ✅.
