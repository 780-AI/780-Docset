<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-06-17 -->
<!-- Status: DRAFT -->
<!--
CHANGE LOG
v0.1 — 2026-06-17 — Sibling tracker created same-commit as the PLAN-005 DRAFT (big plan per § 15.7:
multi-file, Critical-File edits, multi-scenario Phase-4 verify). Granular sub-task list.
-->

# PLAN-005 tracker — Durable project memory (Rule 14 + Set v1.2)

Sibling of [`PLAN-005_durable_memory.md`](PLAN-005_durable_memory.md). Updated same-commit as the work it
tracks. Markers: ⏸ pending · 🔄 in-progress · ✅ done · ❌ blocked · ⏭ skipped.

---

## Phase 0 — Audit ✅ 2026-06-17

- ✅ Cited every insertion anchor against live source (CLAUDE.md ×2, LESSONS ×2, SESSION_OPENER ×2,
  STANDARDS_INDEX, manifest, folder_structure, scripts/, validation_ownership.toml).
- ✅ Confirmed both LESSONS files sit at L049 in lockstep; governance scripts are permissive scaffolds.
- ✅ Confirmed the durable store + symlink are already live (interactive fix 2026-06-17).

## Phase 0.5 — Environment prerequisites ✅ 2026-06-17 (not plan deliverables; documented by 5K)

- ✅ Memory recovered losslessly from the old machine's Dropbox-synced `~/.claude` backup (6 files).
- ✅ Python 3.11 toolchain rebuilt via `uv` (engine `0.2.0`, ruff clean, mypy --strict clean 16 files,
  35 tests pass, governance exit 0).
- ✅ SSH key generated + added to GitLab; `ssh -T` + `git ls-remote` confirm push access.

## Phase 1 — Design 🔄 2026-06-17

- ✅ Plan drafted (§§ 1–12) + sibling tracker created.
- ✅ **Rule 13 senior-review-and-optimize pass** (2026-06-17) — found + fixed 3 defects (binding-file
  count, Rule 14 drift clause over-reach, ALLOWLIST untracked note); recorded in the plan CHANGE LOG.
  No new design decision beyond DD-1…DD-5. **Plan finalized → ready for Phase 2.**

## Phase 2 — Operator approval ⏸

- ⏸ Operator response (expected "APPROVE D5.A" or deltas). Confirm DD-1 / DD-4 / DD-5.

## Phase 3 — Implement ⏸ (single commit, ALLOWLIST = § 7)

- ⏸ 3.1 Rule 14 → root `CLAUDE.md` (+ header 1.2→1.3) [5A]
- ⏸ 3.2 Rule 14 → `docs/standards/CLAUDE.md` (+ header 1.1→1.2) [5B]
- ⏸ 3.3 L050 → `archive/LESSONS.md` + TOC [5C]
- ⏸ 3.4 L050 → `docs/standards/LESSONS.md` + TOC (genericized) [5D]
- ⏸ 3.5 `docs/SESSION_OPENER.md` § 1.5 + § 4 line + § 3.1 row (+ header 1.2→1.3) [5E]
- ⏸ 3.6 `docs/standards/SESSION_OPENER.md` § 1.5 + § 4 line + § 3.1 row (+ header 1.1→1.2) [5F]
- ⏸ 3.7 `git mv .claude/bootstrap_memory.sh → scripts/`; update `.claude/README_memory.md` ref [5G]
- ⏸ 3.8 Create `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md` [5H / § 5.1]
- ⏸ 3.8b Create `docs/NEW_MACHINE_SETUP.md` (re-home checklist) [5K]
- ⏸ 3.9 `STANDARDS_INDEX.md` Set v1.1→v1.2 (§ 1 / § 2 / § 3 / § 6 + header) [5I]
- ⏸ 3.10 Bookkeeping: manifest, CHANGELOG, SET_VERSION_ADOPTED, folder_structure, architecture §10/§11,
  OPEN_TASKS renumber [5J]
- ⏸ 3.11 Promote PLAN-005 + this tracker → 1.0 / CLOSED (same commit)

## Phase 4 — Validate ⏸ (QA scenarios A–F, plan § 8)

- ⏸ A — bootstrap idempotent (run twice, exit 0)
- ⏸ B — self-heal after symlink removal
- ⏸ C — write-through (harness path → repo store)
- ⏸ D — empty-store halt wording unambiguous
- ⏸ E — governance scripts exit 0 (paste stdout)
- ⏸ F — Set-Version consistency (v1.2 / 18 files / 50 lessons / 14 rules)
- ✅ G — fresh-machine toolchain smoke (engine/ruff/mypy/35 tests/governance/SSH) — verified 2026-06-17

## Phase 5 — Operator gate ⏸

- ⏸ 5.1 push
- ⏸ 5.2 tag `set-v1.2`
