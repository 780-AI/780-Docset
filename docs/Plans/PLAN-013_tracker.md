<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Status: CLOSED (Phase 3 shipped 2026-10-03; QA-K1…K4 + K6 ✅; K5 open at its named trigger; pushed 2026-10-03) -->
<!--
CHANGE LOG
v1.1 — 2026-10-03 — Phase 5 push recorded (operator "push"; `ls-remote` verified remote master =
`b65037c`; no tag — engine-only). Also observed: the Set v2.7 fleet write (vault `0e03e10`)
appended `### Write 3` to Capital-Signal's handoff and wrapped 780-VPN's pre-accumulation handoff
as Write 1 + `### Write 2` — the accumulation and legacy-wrap paths, live on two more targets.
v1.0 — 2026-10-03 — Phase 3 + QA-K1…K4 + K6 recorded (fresh implementer session): reconcile pass
clean, § 5/§ 6 applied byte-for-byte; feature-ON evidence analyzed (guard refusal on a real-data
copy; first accumulating write into Capital-Signal). Rule 10 review found plan defect D2 (§ 2
anchor `find` → `rfind`; operator D2 = A — fixed + regression test). Promoted with the plan per § 15.5.
v0.2 — 2026-10-03 — Phase 2 approval recorded ("approve plan 013"; D-1…D-5 = A, plan § 9.1).
v0.1 — 2026-10-03 — Created with the plan draft (tracker required per § 15.7: Phase 4 is
multi-scenario, QA-K1…K6, and K4/K5 fire at later triggers).
-->

# PLAN-013 tracker — engine write safety (clock floor + accumulating handoffs)

## Phase 0 — Audit

- ✅ 2026-10-03 — write sites cited (`_cmd_integrate`, `_cmd_sync`: `date.today()` unchecked;
  handoff `write_text` overwrite at both); live evidence (CS 7 files vs handoff 3; 780-VPN v2.6
  handoff un-landed); baseline ruff clean / mypy 42+25 / pytest 111.

## Phase 1 — Design

- ✅ 2026-10-03 — § 5 code developed + proven in a scratch overlay (ruff clean; mypy error set
  identical; pytest 119); real-data preview (CS legacy handoff wrapped; floors CS 2026-09-05,
  780-VPN 2026-10-03).
- ✅ 2026-10-03 — plan drafted (§§ 1–12) + this tracker.
- ✅ 2026-10-03 — Rule 13 pass RUN + recorded at the plan's foot.

## Phase 2 — Operator approval

- ✅ 2026-10-03 — operator: **"approve plan 013"** — D13.A + D-1…D-5 at the recommended options
  (offline floor guard / accumulate / strict / no override / CS v2.6 catch-up as QA-K4); recorded
  at plan v0.2 § 9.1.

## Phase 3 — Implement (fresh session; single commit; ALLOWLIST-bounded)

- ✅ 2026-10-03 — reconcile pass clean: all 17 § 5/§ 6 FIND blocks (parsed from the plan file)
  matched live source exactly once at `959c3e2`; no plan defect.
- ✅ 2026-10-03 — clock verified externally (local UTC vs gitlab.com / apple.com / google.com
  `Date:` headers, ≤8 s); `<P3-DATE>` = 2026-10-03; § 5 + § 6 applied byte-for-byte (no token left).
- ✅ 2026-10-03 — Rule 10 review: plan defect **D2** — § 5b `_prior_records` found the § 2 anchor
  with `find`; a later write truncated a fenced unrecognized handoff containing its own § 2
  heading (content + the previous file list lost — reproduced). Operator D2 = A → `rfind` + test
  `test_render_handoff_keeps_a_wrapped_handoff_across_later_writes` (fails on the unfixed code,
  passes fixed). D1 (doubled project name in the sync refusal) = A — shipped as approved (R7).
- ✅ 2026-10-03 — manifest cells + CHANGELOG; plan + tracker → 1.0/CLOSED (after K2–K4 ✅).

## Phase 4 — Validate (scenario ledger)

| # | Scenario | Status | Date | Evidence |
|---|---|---|---|---|
| QA-K1 | ruff / mypy error set / pytest 119 | ✅ | 2026-10-03 | `ruff check src tests` clean; mypy error SET identical to the `959c3e2` baseline, line numbers stripped (42 full / 25 `src`); pytest **119 passed** (111 + 8 new), imported from repo `src`; re-run after the D2 fix: ruff clean, mypy set identical, **120 passed** (+1 D2 regression) |
| QA-K2 ⚑ | live dry-run: notes, no false warning, plans unchanged | ✅ | 2026-10-03 | Fleet `sync` dry-run, new engine vs HEAD engine (extracted to scratch): stdout differs ONLY by the un-landed-handoff note on CS + 780-VPN; no clock warning (clock verified); changed-item lists identical (CS 3 = the v2.6 delta; 780-VPN up-to-date). 780-Automation ssh refused (known; stderr differs only in temp-dir names) |
| QA-K3 ⚑ | clock guard on a real-data scratch copy | ✅ | 2026-10-03 | Detached scratch vault worktree + registry → scratch copy of Capital-Signal (CLAUDE.md + docs/ + archive/; CS chosen — 780-VPN has no changed item, so the guard would never be reached); copy's SESSION_OPENER stamp → 2026-10-04 (floor 2026-09-05 → 2026-10-04). Dry-run: "warning: the local clock (2026-10-03) is behind this target's newest stamp (2026-10-04) — a --write would refuse (L079)". `--write`: exit 1, "refusing to write … (the clock is behind, L079)"; copy byte-unchanged (76 files shasum-identical, incl. its pre-existing handoff — no handoff written or appended). Cleanup: worktree removed + pruned, copy deleted. Finding: refusal prints the project name twice (plan § 11 R7, D1 = A) |
| QA-K4 ⚑ | accumulation — sync half (CS v2.6 catch-up, D-5) | ✅ | 2026-10-03 | Operator "go k4". Pre-checks: git repo, SVA v2.5, fresh dry-run 3 changed + handoff note. `sync --project EverOn.Capital-Signal --write`: "wrote + flushed 4 file(s)" + "appended to an un-landed handoff"; shasum diff of the whole tree (1339 files, .venv/.git excluded) = exactly PROJECT_STANDARDS + LESSONS + SVA + SYNC_HANDOFF. Handoff read back: `### Write 1 — earlier engine write` (v2.5, 2026-09-05, its 3-file list verbatim) + `### Write 2` (v2.6, 2026-10-03, the 3 files); § 2 step 1 carries the unlisted-files sentence. Spot-greps: L079 in LESSONS, § 5.6 in PROJECT_STANDARDS, SVA v2.6 row. Verdict: matches design. CS hold LIFTED (status v2.6/v2.6 current) |
| QA-K5 ⚑ | accumulation — write-back half (E001 write-back) | ⏸ | | Fires at its named trigger (plan § 8 Rule 15 note): the E001 write-back after 780-VPN's next session (v2.6 QA-E4 = PLAN-012 QA-H6). 780-VPN still holds its un-landed v2.6 handoff (2026-10-03) → expect the `### Write 2` path; record which ran |
| QA-K6 | idempotence after K4/K5 | ✅ | 2026-10-03 | K4 half: immediate fleet dry-run — CS + 780-VPN "up-to-date — all suite files match the vault" with the handoff note (presence does not perturb planning); `status` CS v2.6/v2.6 current, 780-VPN v2.6/v2.6 current. K5 half re-runs at the K5 trigger |

Waiver register (Rule 15): _(empty)_

## Phase 5 — Operator gate

- ✅ 2026-10-03 — Push (operator "push"; `ls-remote` verified remote master = `b65037c`). No tag —
  engine-only, no Set Version change.
