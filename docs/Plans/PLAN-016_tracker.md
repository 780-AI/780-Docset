<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-10-05 -->
<!-- Status: CLOSED (Phase 3 shipped 2026-10-05; QA-L1…L8 ✅ — L7 / L8 post-ship; pushed 2026-10-05 to both remotes) -->
<!--
CHANGE LOG
v1.1 — 2026-10-05 — Post-close annotations (PLAN-013 v1.1 / v1.2 precedent): Phase 5 push recorded (both
remotes = `8b914db`, `ls-remote` verified; no tag); QA-L7 ✅ (operator opened the CSV: "QA-L7 is passed");
QA-L8 ✅ (the next session's open `status` + close `fleet` both reported the fleet line). All eight ✅.
v1.0 — 2026-10-05 — Phase 3 + QA-L1…L6 recorded (fresh implementer session): reconcile pass clean
(85/85 FIND blocks matched the live tree once; zero plan defects); D1 (Equinex `registered_on`) = A →
2026-10-04; applied byte-for-byte; ship-gating QA ✅ with evidence below. Promoted with the plan.
v0.2 — 2026-10-04 — Phase 2 approval recorded ("plan 016 is approved"; decisions in plan § 9.1).
v0.1 — 2026-10-04 — Created with the plan draft (tracker required per CLAUDE.md § 15.7: Phase 4 is
multi-scenario, QA-L1…L8).
-->

# PLAN-016 tracker — fleet view (`docs/fleet.csv`)

## Phase 0 — Audit

- ✅ 2026-10-04 — § 15.9 intake: operator request (no document); decisions 1–4 recorded (plan § 2).
- ✅ 2026-10-04 — integration points cited by `file:line` (plan § 3): the shared probe
  (`cli.py:58-73`), handoff record counting (`sync.py:320-339`), the registry's unknown-key gap
  (`registry.py:59-110`), the private version formatter (`report.py:76`), the ssh transport
  (`transport.py:150-160`), the governance script + CI job (`.gitlab-ci.yml:20-22`).
- ✅ 2026-10-04 — baseline on a scratch overlay of `23d2ef2`: ruff clean, mypy --strict 0 errors,
  pytest 120 passed.

## Phase 1 — Design

- ✅ 2026-10-04 — code developed + tool-proven in the overlay (ruff clean / mypy 0 / pytest 140).
- ✅ 2026-10-04 — read-only real-fleet preview (scratch vault copy, 4 targets): rows correct; 75 s →
  10.1 s with D-4; gate failure paths F1–F6 fired as designed.
- ✅ 2026-10-04 — § 5 / § 6 blocks generated from the overlay (no hand-copying).
- ✅ 2026-10-04 — Rule 13 senior-review pass (record at the foot of the plan).

## Phase 2 — Operator approval

- ✅ 2026-10-04 — "plan 016 is approved" — D-1 / D-2 / D-4 / D-5 = A; D-3: 780-VPN owner →
  operator (§ 6a.4 updated + re-proven), the rest as proposed (plan § 9.1). Plan + tracker → 0.2.

## Phase 3 — Implement (fresh session; single commit; AFTER the PLAN-011 closure commit)

- ✅ 2026-10-05 — Pre-checks: PLAN-011 closure `1477e33` landed; clock verified externally (local ==
  gitlab.com / apple.com `Date:` within 2 s) → `<P3-DATE>` = 2026-10-05; `<P3C-DATE>` = `git log -1
  --format=%cs 1477e33` = 2026-10-04 — operator **D1 = A** (vs 2026-10-03, SESSION_OPENER § 2's
  "Registered" prose; that prose stays as written).
- ✅ 2026-10-05 — Reconcile pass: a parser re-extracted all 85 blocks (20 files) from the plan; every
  FIND matched the live tree exactly once; both new files absent. Zero plan defects.
- ✅ 2026-10-05 — Applied § 5a–5m + § 6a–6g (D-4 = A, no skips): sequentially on a scratch copy first
  (every FIND matched once at its turn; ruff clean / mypy 0 / pytest 140 with the scratch `src`
  imported), then on the real tree — byte-identical to the scratch result, 20/20 files.
- ✅ 2026-10-05 — § 6h manifest (2.55 → 2.56: rows 88–89 new, 15 cells + self-row, row 46 retitled,
  86–87 → 1.0 CLOSED, Engine quick-index + 88–89) + § 6i CHANGELOG + § 6j promotion.
- ✅ 2026-10-05 — QA-L1…L6 ✅ (below) → Rule 10 review table → single commit (no push).
- ✅ 2026-10-05 — Hand-kept fleet table deleted from `docs/Plans/OPEN_TASKS.md` (local).

## Phase 4 — Validate

| # | Scenario | Phase | Status | Date | Evidence |
|---|---|---|---|---|---|
| QA-L1 | Tools (ruff / mypy / pytest 140) | 3 | ✅ | 2026-10-05 | `ruff check src tests` all checks passed; `mypy` (strict, fresh `--cache-dir`) no issues in 24 source files; pytest **140 passed** (baseline 120); imported from the repo `src` (CLI 0.6.0). The in-repo `.mypy_cache` showed 2 phantom `attr-defined` errors on the UNCHANGED baseline (stale cache) — 0 with a fresh cache, before and after |
| QA-L2 ⚑ | Real fleet run | 3 | ✅ | 2026-10-05 | `fleet`: "4 project(s), 3 reachable" in **10.1 s** with 780-Automation down (D-4); file starts with the UTF-8 BOM; 24 columns × 4 rows in registry order; registry columns == § 6a values; live columns == the `status` table (CS / 780-VPN / Equinex v2.7 / v2.7 current, open-log 1 / 0 / 0); 780-VPN `handoff_pending=3` == its handoff's 3 `### Write` records; CS + Equinex 0 (no handoff file — Equinex landed its E001 write-back handoff in a session earlier the same day) |
| QA-L3 ⚑ | Unreachable carry-over (scratch vault) | 3 | ✅ | 2026-10-05 | run 1: 780-VPN yes / current / v2.7 / open 0 / pending 3 / last_seen 08:56:08Z; path → `/nonexistent/780-VPN`, run 2: `reachable=no`, `state=unknown`, `adopted_set` v2.7 / `open_log` 0 / `handoff_pending` 3 / `last_seen` 08:56:08Z carried, `as_of` 08:56:19Z, `location` = the new path (registry fresh) |
| QA-L4 ⚑ | Freshness gate a–e (scratch copy) | 3 | ✅ | 2026-10-05 | (a) "fleet view: OK" exit 0; (b) 780-Automation owner edited → "780-Automation: stale column(s): owner" + fix line, exit 1; (c) `ownr` → "unknown key(s): ownr", exit 1; (d) CSV deleted → "docs/fleet.csv missing" + fix line, exit 1; (e) `CI=true`, no CSV → "skipped in CI", exit 0 |
| QA-L5 ⚑ | Write-path refresh (scratch target copy) | 3 | ✅ | 2026-10-05 | scratch vault + a copy of Capital-Signal's `docs/` + `archive/` + `CLAUDE.md` (its `archive/LESSONS.md` made stale): `sync --write` → "wrote + flushed 2 file(s)" + "docs/fleet.csv refreshed"; `as_of` 08:56:54Z → 08:56:55Z; `handoff_pending` 0 → 1 (copy's handoff: 1 `### Write` record); real CS `archive/LESSONS.md` md5 unchanged, no handoff created |
| QA-L6 ⚑ | Machine neutrality (`HOME` elsewhere) | 3 | ✅ | 2026-10-05 | after a real `fleet` run: `HOME=<scratch>/otherhome python scripts/check_doc_coverage.py` → "fleet view: OK", exit 0 (`Path.home()` confirmed = the other dir) |
| QA-L7 | Operator opens the CSV | post-ship | ✅ | 2026-10-05 | operator opened `docs/fleet.csv` after the push and confirmed: "QA-L7 is passed" |
| QA-L8 | Session open / close fleet lines | post-ship | ✅ | 2026-10-05 | next session (the 780-estimator intake): open — SESSION_OPENER § 1.2 `status` 10.1 s, "docs/fleet.csv refreshed — 4 project(s), 3 reachable", the § 4 block carried the fleet line (780-Automation unreachable; 780-VPN `handoff_pending` 3; Capital-Signal open-log 1); close — SESSION_CLOSER § 1.2 `fleet` 10.1 s, same 4 rows / 3 reachable, reported in the wrap-up § 4 block |

## Phase 5 — Operator gate

- ✅ 2026-10-05 — Pushed to BOTH remotes (operator "push"): `git ls-remote origin master` = `git ls-remote
  github master` = `8b914db` = HEAD; no tag (engine-only, no Set Version change).
