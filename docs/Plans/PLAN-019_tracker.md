<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Status: CLOSED — 2026-10-12 (Phase 5 push pending) -->
<!--
CHANGE LOG
v1.0 — 2026-10-12 — CLOSED: Phase 3 (3.0–3.4) + Phase 4 (QA-T1…T5) ✅ with evidence, one commit.
v0.2 — 2026-10-12 — Phase 2 ✅: "D1. A , D2. A" + "go" (plan § 9.1); 3.0 pre-check no longer requires
HEAD == both remotes (the planning commits may still be unpushed).
v0.1 — 2026-10-12 — Created with the plan draft (tracker required per CLAUDE.md § 15.7: Phase 4 has a
multi-scenario list, QA-T1…T5).
-->

# PLAN-019 tracker — git transport fails fast (ssh timeouts + keepalives, a cap on every transport command)

## Phase 0 — Audit

- ✅ 2026-10-12 — § 15.9 intake: operator request in chat (no document) — "yes get it done as quickly as
  possible"; adopt / deviate vs the queued fix candidate recorded (plan § 2).
- ✅ 2026-10-12 — integration points cited `file:line` at `bf8669e` (plan § 3).
- ✅ 2026-10-12 — pre-tests with numbers: silent server / blackhole / mid-transfer stall hang with no
  options (≥ 40–75 s caps) and fail in 10.0 / 10.0 / 41.2 s with them; normal clone 3.0 s; the run cap
  returns on time; one orphaned ssh seen (→ R2).

## Phase 1 — Design

- ✅ 2026-10-12 — code drafted in a scratch export of HEAD: ruff clean, mypy --strict 0, pytest 172
  (163 + 9); positive control 8 failed / 20 passed on transport 0.3.
- ✅ 2026-10-12 — the engine's own `GitTarget`: GitHub 7.5 s OK; silent 10.1 s; stall 41.6 s with the
  operator's base command kept.
- ✅ 2026-10-12 — § 5 generated (16 blocks) + § 8 harness embedded; parsed back from the plan text →
  17 / 17 clean, byte-identical; control 1 corrupted FIND → exactly that block fails.
- ✅ 2026-10-12 — QA harness: draft 4 / 4 PASS; HEAD 1 PASS / 3 HANG (control).
- ✅ 2026-10-12 — Rule 13 senior-review pass (record at the foot of the plan; 5 fixes).

## Phase 2 — Operator approval

- ✅ 2026-10-12 — "D1. A , D2. A" + "go" — D19.A; D-1 = A, D-2 = A (plan § 9.1). Plan + tracker → 0.2.

## Phase 3 — Implement (fresh session, one commit)

- ✅ 2026-10-12 3.0 — local 07:57:35 UTC vs gitlab.com 07:57:37 / apple.com 07:57:38 GMT (Δ ≤ 3 s) →
  `<P3-DATE>` = 2026-10-12; tree clean; HEAD `63e6c1f` (contains the approval commit); both remotes
  `ls-remote` = `63e6c1f` (nothing unpushed).
- ✅ 2026-10-12 3.1 — reconcile: 17 blocks parsed from the plan (16 replace + harness 8a); every FIND
  exactly once, in order → CLEAN, **zero plan defects**. Checker positive control: corrupted 5c.3 →
  only 5c.3 FAIL (0x); corrupted 5a.6 → only 5a.6 FAIL. All `transport._run` fakes accounted for (4 in
  `test_cli.py` + `_capture`); rsync callers keep `env=None`.
- ✅ 2026-10-12 3.2 — § 5 applied (4 files: transport 0.4, test_transport 0.4, test_cli 0.9,
  architecture 0.15); no `<P3-DATE>` left → QA-T1.
- ✅ 2026-10-12 3.3 — QA-T2 … T4 (live) → QA-T5 governance (below).
- ✅ 2026-10-12 3.4 — § 6 bookkeeping (manifest 2.71, CHANGELOG, plan + tracker → 1.0 CLOSED) → Rule 10
  review → "go on commit?" → commit (§ 7, 8 files; no push).

## Phase 4 — Validate (QA scenarios, plan § 8)

- ✅ 2026-10-12 QA-T1 — `ruff check src tests` "All checks passed!"; `MYPYPATH=src mypy --strict
  --cache-dir <fresh>` "Success: no issues found in 25 source files"; `pytest` **172 passed**. Control
  (scratch tree, `transport.py` = `bf8669e`'s 0.3): `pytest tests/test_transport.py` → **8 failed, 20
  passed** — the 8 new-behavior tests; the rsync guard passes on both.
- ✅ 2026-10-12 QA-T2 ⚑ — real `status` (no `GIT_SSH*` env, `core.sshCommand` unset → `ssh` + the four
  options): 780-estimator `v2.7 v2.7 current`; Capital-Signal / 780-VPN / Equinex current; 780-Automation
  `unknown` (ssh rsync host down — as at session open). Step timing confirmed every git command carried
  `GIT_SSH_COMMAND=ssh -o ConnectTimeout=10 -o BatchMode=yes -o ServerAliveInterval=10 -o
  ServerAliveCountMax=3`.
- ✅ 2026-10-12 QA-T3 ⚑ — harness (8a, extracted from the plan): T3a silent server `transport-error in
  10.1s`; T3b CLI `status` exit 0 in 10.1 s, row `silent … ? v2.7 unknown 0`.
- ✅ 2026-10-12 QA-T4 ⚑ — harness T4: `transport-error in 32.0s` with `GIT_SSH_COMMAND="ssh -o
  HostKeyAlias=github.com"` as the base (kept — the relay's host-key check passed). Harness run
  08:16 UTC: `SUMMARY pass=4 fail=0` (T2 real GitHub read ok 15.4 s); `pgrep` → no ssh left. Control on
  `bf8669e` src: `SUMMARY pass=1 fail=3` (T3a / T3b HANG 30 s, T4 HANG 75 s); no ssh left.
  **Deviation (recorded, not a defect):** the first harness run (~08:01 UTC) gave `pass=3 fail=1` — T2
  HANG at its 60 s watchdog. Investigated: GitHub link slow at the time (24 KB/s download, ~316 ms
  RTT); direct read sessions took 64.2 / 79.5 / 176.4 s on the NEW code and 42.3 / 105.8 s on the OLD
  (the blobless `checkout` = 36–156 s of it) → environment, not the change. Re-run on the recovered link
  (unchanged harness) 4 / 4. Plan R4 annotated (cap margin on a bad link ~1.7×; kept at 300 s).
- ✅ 2026-10-12 QA-T5 — governance exit 0 / 0 (stdout in the session chat; summary in CHANGELOG).

## Phase 5 — Operator gate

- ⏸ 5.1 — push to both remotes (`git push origin master` + `git push github master`; `ls-remote` both
  == HEAD); no tag (no Set Version change).
