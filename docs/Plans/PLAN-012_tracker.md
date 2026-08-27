<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-09-05 -->
<!-- Status: DRAFT (tracks PLAN-012; promoted to 1.0/CLOSED with the plan) -->
<!--
CHANGE LOG
v0.1 — 2026-09-05 — Created with the plan draft (tracker required: Phase 4 is multi-scenario,
QA-H1..H5).
-->

# PLAN-012 tracker — sync handoff report

## Phase 0 — Audit

- ✅ 2026-09-05 — write path cited: `cli.py::_cmd_sync` (`apply_actions` at cli.py:162 →
  `target.flush`); transport flush implementations local/git/ssh confirmed to carry any
  repo-relative path list; `docs/` always materialized (ssh) so the handoff path exists on every
  transport.
- ✅ 2026-09-05 — incident evidence: 780-VPN session report (operator-pasted) — four
  engine-written uncommitted files required reverse-engineering; clock-skew direction corrected
  same day (vault machine ~9 days slow, verified vs gitlab.com + apple.com).

## Phase 1 — Design

- ✅ 2026-09-05 — overlay built (`src` + `tests` copy), edits applied, tools run: ruff clean /
  mypy delta zero (25↔25) / pytest 111 passed.
- ✅ 2026-09-05 — plan drafted (§§ 1–12) with overlay-proven § 5 blocks.
- ✅ 2026-09-05 — Rule 13 pass RUN + recorded in the plan CHANGE LOG (tools at ship
  indentation; anchors grep-verified; ALLOWLIST count 12 = 12).

## Phase 2 — Operator approval

- ⏸ awaiting **"APPROVE PLAN-012"**.

## Phase 3 — Implement (fresh session; single commit; ALLOWLIST-bounded)

- ⏸ reconcile pass (plan § 5 anchors vs live source; any mismatch = named plan defect D1…).
- ⏸ apply § 5a–5f byte-for-byte; § 6 spec map (architecture § 7 paragraph, INDEX v2.5, SVA,
  manifest, CHANGELOG); promote plan + tracker to 1.0/CLOSED.

## Phase 4 — Validate

- ⏸ QA-H1 — ruff / mypy-delta / pytest 111 (re-run at ship).
- ⏸ QA-H2 — pre-release fleet dry-run oracle: exactly the 3-item v2.5 delta per target.
- ⏸ QA-H3 — feature-ON: v2.5 `sync --write` delivers `docs/SYNC_HANDOFF.md` to all three
  targets (spot-grep each).
- ⏸ QA-H4 — idempotence: dry-run re-run up-to-date 11/11 everywhere.
- ⏸ QA-H5 — loop closure: a target session lands a sync per the handoff + deletes it
  (operator-observed; first observation closes).

## Phase 5 — Operator gate

- ⏸ push + tag `set-v2.5`; `ls-remote` verify; register flips.
