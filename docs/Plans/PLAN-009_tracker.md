<!-- VERSION: 0.1 -->
<!-- Status: APPROVED (D9.A, 2026-08-16) -->
<!-- Last Updated: 2026-08-16 -->
<!--
CHANGE LOG
v0.1 — 2026-08-16 23:15 — Initial (same commit as the PLAN-009 draft). Big-plan sibling tracker:
Phase 3 spans 2 commits (release + closure), Phase 4 is multi-scenario (QA-A…QA-G), and the
Capital-Signal pilot is cross-session.
-->

# PLAN-009 tracker — skill-based suite delivery (Set v2.0)

Plan: `docs/Plans/PLAN-009_skill_delivery.md`. Status markers: ⏸ pending / 🔄 in-progress /
✅ done / ❌ blocked / ⏭ superseded (annotated). Every transition gets a date stamp.

---

## Phase 0 — Audit ✅ 2026-08-16

- ✅ Delivery machinery read end-to-end: `SETUP.md` v1.6 (steps 1–9 + 8.5 strip set-cover),
  `NEW_PROJECT_BOOTSTRAP.md` v1.6 (structure), `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` v1.2
  (self-declares PLAN-009 absorption).
- ✅ Integration points cited: `STANDARDS_INDEX.md` §§ 1–6 (v1.6 state, 18 files / 11+7);
  `architecture.md` §§ 3/4/8/10/11 (v0.10); `folder_structure.md` v0.13;
  `claude_project_data.sh` v0.1 (path-independent — copyable verbatim to targets);
  `NEW_MACHINE_SETUP.md` v1.1 (Rule 14 catalog); `config/projects.toml` (empty registry);
  governance scripts (permissive scaffolds — no changes needed for `skill/`).
- ✅ Reference sweep (L060, live sites only): HOW_TO_USE 17/18/104; README(std) 22/153/195/199;
  STANDARDS_LOG template 4/70; SESSION_OPENER template 252; SESSION_CLOSER template 279. Root
  `CLAUDE.md` = no edit (grep hit was a `NEW_MACHINE_SETUP.md` false positive). Frozen history
  (CHANGELOG, LESSONS 618/642, SVA rows, docs/Plans/) deliberately NOT retargeted.
- ✅ Skill-symlink spike: docs confirm symlinked skill dirs are followed (code.claude.com/docs
  skills — "can be a symlink to a directory elsewhere on disk"); supporting-file reads docs-silent
  → FS probes run 2026-08-16: (1) read through symlink INTO the CloudStorage vault ✅; (2) two-link
  chain ✅; (3) physical `..` resolution ✅; (4) Python pathlib resolve+read ✅.
  `~/.claude/skills/` does not exist yet on this machine (installer creates it).
- ✅ Desktop-export check: no live doc mandates `~/Desktop/Standard-DocSet-Suite/` (only generic
  propagation-prompt wording in the CLOSER template) — nothing to edit; retirement is operator-side
  folder deletion.

## Phase 1 — Design ✅ 2026-08-16

- ✅ §§ 1–12 drafted (this commit).
- ✅ Sibling tracker created same-commit (§ 15.7 triggers 1+2+3 all true).
- ✅ Rule 13 senior-review-and-optimize pass run on the complete plan + tracker (see plan CHANGE
  LOG; tools run against the § 5 fenced bodies at final ship indentation — record below).
  - Rule 13 tooling record: `bash -n` on extracted § 5D ✅; `grep -F` anchor verification on every
    § 5G–5K FIND block ✅; shellcheck unavailable on this machine (noted; manual walk done);
    ruff/mypy N/A (no Python ships in this plan).

## Phase 2 — Operator approval ✅ 2026-08-16

- ✅ 2026-08-16 — operator: "approved" (recorded as APPROVE D9.A; D-1 live-reference, D-2 `skill/`,
  D-3 NPB retire, D-4 MDRP retire, D-5 two-stage close — all per the plan's § 9 recommendations).
- ✅ 2026-08-16 — design commit landed per § 7.1 (plan + tracker + manifest rows + CHANGELOG).

## Phase 3 — Implement ⏸ (fresh session; reconcile pass first per § 15.3)

### Commit 1 — the release commit (§ 7.2, 21 files)

- ⏸ Reconcile pass: § 5 anchors + § 7.2 ALLOWLIST vs live source; mismatches surfaced as D1, D2, …
- ⏸ § 5A `skill/SKILL.md` (byte-for-byte from the plan fence)
- ⏸ § 5B `skill/modes/bootstrap.md`
- ⏸ § 5C `skill/modes/adopt.md`
- ⏸ § 5D `scripts/bootstrap_skill.sh` (+ `bash -n` at ship state)
- ⏸ § 5E retirements (3 × git rm)
- ⏸ § 5F STANDARDS_INDEX → v2.0
- ⏸ § 5G HOW_TO_USE / § 5H README(std) / § 5I STANDARDS_LOG / § 5J OPENER / § 5K CLOSER
- ⏸ § 5L architecture / § 5M folder_structure (incl. 15-rules rider) / § 5N SVA / § 5O
  NEW_MACHINE_SETUP
- ⏸ § 5P manifest (rows + cells + L063 stamp-vs-log grep) / § 5Q CHANGELOG
- ⏸ QA-A…QA-D run + evidence recorded below (gate: before the commit ships)
- ⏸ Governance scripts (stdout verbatim) → Rule 10 named review table → "go on commit?" →
  `git add -A` (status check before AND after) → `commit -F`

### Commit 2 — the closure commit (§ 7.3, after QA-E/QA-F)

- ⏸ Plan + tracker promoted 1.0 / CLOSED; manifest promotion cells; CHANGELOG closure note.

## Phase 4 — Validate (QA evidence; ⚑ = Rule 15 feature-ON gate)

| ID | Scenario (plan § 8) | Status | Date | Evidence |
|---|---|---|---|---|
| QA-A ⚑ | Fresh-session skill discovery + Step 0 report line | ⏸ | — | — |
| QA-B ⚑ | Bootstrap end-to-end on a scratch target (zero machinery; SVA stamped; governance 0) | ⏸ | — | — |
| QA-C | Installer idempotence + re-point | ⏸ | — | — |
| QA-D | Step-0 self-pull + offline WARN | ⏸ | — | — |
| QA-E ⚑ | REAL adopt pilot: Capital-Signal (dry-run list == applied diff; markers intact) — adopt-mode + closure gate; separate session | ⏸ | — | — |
| QA-F | Pilot registered + `sync` dry-run reports current | ⏸ | — | — |
| QA-G | Zero-hit greps (domain-neutral incl. skill/; no live retired-file refs) | ⏸ | — | — |

Waiver register (Rule 15): _(empty — QA-E may not be deferred without an explicit operator waiver
recorded here)_

## Phase 5 — Operator gate ⏸

- ⏸ Push authorization (release commit + closure commit)
- ⏸ Annotated tag `set-v2.0`
- ⏸ OPEN_TASKS reconcile: mark the standing "SETUP.md end-to-end live test" item ⏭ superseded by
  QA-B; flip push-state lines in the same wrap-up as the push (L055)
