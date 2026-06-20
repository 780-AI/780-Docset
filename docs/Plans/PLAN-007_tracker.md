<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-06-20 -->
<!-- Status: DRAFT -->
<!--
CHANGE LOG
v0.1 — 2026-06-20 — Sibling tracker created same-commit as the PLAN-007 DRAFT (big plan per § 15.7:
new module + registry-schema change + a target-repo write over a network transport; 18-file ALLOWLIST;
multi-scenario Phase-4 verify (A–N); will span sessions — Phase 3 is a fresh session).
-->

# PLAN-007 tracker — Remote-target transport (local | git | ssh)

Sibling of [`PLAN-007_remote_transport.md`](PLAN-007_remote_transport.md). Updated same-commit as the
work it tracks. Markers: ⏸ pending · 🔄 in-progress · ✅ done · ❌ blocked · ⏭ skipped.

---

## Phase 0 — Audit ✅ 2026-06-20

- ✅ Every target-repo I/O site enumerated (per E007/L039): all derive from `project.path` and are built
  at `cli.py:37-38, 62, 86-87`; the actual reads/writes live in `setversion.py:47/60`, `logentry.py:67`,
  `integrate.py:209/216/217` (write). Vault I/O (registry / STANDARDS_INDEX / LESSONS / decisions file)
  never goes through a target → not wrapped by transport.
- ✅ External deps verified: `git` ✓ (2.50.1), `rsync` ✓ (openrsync), `ssh` ✓; `glab`/`gh` **absent**
  → git write-back is direct push (D2), MR variant deferred (DD-6b).
- ✅ Numbering conflict found: `architecture.md` § 10 still maps PLAN-007 = `sync`; corrected by this plan
  (transport = PLAN-007, sync = PLAN-008).
- ✅ Confirmed `integrate.apply_writeback` can stay Path-based + unchanged (transport seam is cli-only,
  DD-2) → its 20 tests remain valid.

## Phase 1 — Design ✅ 2026-06-20

- ✅ Plan drafted (§§ 1–12) with D1–D4 baked in + DD-1…DD-6 + full § 5 spec (transport.py + registry/cli/
  report diffs + test plan); sibling tracker created.
- ✅ **Rule 13 senior-review pass** (2026-06-20) — materialized the § 5 code in `src/` + a real
  `test_transport.py`, RAN `ruff` + `mypy --strict` (MYPYPATH=src) + `pytest` (per L051 — not eyeballed),
  removed scratch. Found + fixed in § 5: ruff E501 ×2 (§ 5C), B027 ×2 (§ 5A no-op hooks), I001 (§ 5B),
  E501 ×2 + reexport in the test; rewrote the `_run`-failure test. Caught my own mypy mis-invocation
  (needs `MYPYPATH=src` — QA B fixed) + a stale mypy cache. Final: ruff clean, mypy 0/20, 71 tests pass.
  Recorded in the plan CHANGE LOG (v0.1a). **Ready for Phase 2.**

## Phase 2 — Operator approval ⏸

- ⏸ Awaiting "APPROVE D1.A" (or deltas). Confirm DD-1 (registry `transport` key), DD-4/DD-5 (per-target
  atomic; git direct fast-forward push, fixed identity, operator SSH creds), DD-3 (unreachable = non-fatal).

## Phase 3 — Implement ⏸ (fresh session, ALLOWLIST = § 7)

- ⏸ 3.1 `transport.py` — Target ABC + Local/Git/Ssh + make_target + TransportError [5A]
- ⏸ 3.2 `registry.py` — Project transport fields + per-transport validation (0.1→0.2) [5B]
- ⏸ 3.3 `cli.py` — materialize via `make_target`/`session`; ExitStack write path; graceful failure (0.3→0.4) [5C]
- ⏸ 3.4 `report.py` — `location` cell + `unreachable_status`; header PATH→LOCATION (0.1→0.2) [5D]
- ⏸ 3.5 `__init__.py` 0.3→0.4
- ⏸ 3.6 `tests/test_transport.py` (new) + 3.7 test_registry / 3.8 test_cli / 3.9 test_report updates [5E]
- ⏸ 3.10 `validation_ownership.toml` soft `[rules.transport]`
- ⏸ 3.11 `config/projects.toml` git/ssh example comments
- ⏸ 3.12 `CLAUDE.md` § 1 (retire "no remote infra") + version bump
- ⏸ 3.13 `architecture.md` § 1/§ 8/§ 9/§ 10/§ 11 + header bump (no Set-Version bump — DD-6)
- ⏸ 3.14 `documents_manifest.md` register transport.py + test_transport.py + cells + plan promotion + header
- ⏸ 3.15 `folder_structure.md` tree + header
- ⏸ 3.16 `CHANGELOG.md` top entry + QA A–N sub-section
- ⏸ 3.17 Promote PLAN-007 + this tracker → 1.0 / CLOSED (same commit)

## Phase 4 — Validate ⏸ (QA A–N, plan § 8)

- ⏸ A ruff · B mypy --strict · C pytest · D governance
- ⏸ E local back-compat · F/G/H registry parse+validation · I make_target dispatch · J local-in-place
- ⏸ K git read fetch · L git push · M ssh rsync · N unreachable non-fatal

## Phase 5 — Operator gate ⏸

- ⏸ 5.1 push (no tag — Set Version unchanged, DD-6)
