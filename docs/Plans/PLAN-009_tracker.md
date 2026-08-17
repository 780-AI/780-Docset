<!-- VERSION: 1.0 -->
<!-- Status: CLOSED -->
<!-- Last Updated: 2026-08-17 -->
<!--
CHANGE LOG
v1.0 — 2026-08-17 — CLOSED with the plan (D-5 stage 2): QA-A completed (live invocation), QA-E
passed (Capital-Signal adopt commits `d0e0781`+`2caa53e`, evidence below), QA-F passed
(registration `e9576d2` + status/sync/harvest on the target's machine). Commit-2 checklist ticked.
Phase 5 (push + tag) remains operator-gated.
v0.2 — 2026-08-17 — Phase 3 release-commit session: commit-1 checklist ticked; reconcile-pass
record + plan-defect register (D1/D2/D3) added; Phase 4 QA table updated with evidence
(QA-B/C/D/G ✅; QA-A partial — fresh-session listing = operator confirm; QA-E/F pending).
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

## Phase 3 — Implement ✅ (commit 1 `66d45d5` 2026-08-17; commit 2 = the closure commit 2026-08-17)

### Commit 1 — the release commit (§ 7.2, 21 files) — ✅ 2026-08-17

- ✅ 2026-08-17 — Reconcile pass: 11/11 § 5G–5K anchors `grep -F`-verified byte-exact at the
  audited lines (17/18/104, 22/153/195/199, 4/70, 252, 279); § 5F/5L–5Q structural claims + § 7.2
  preconditions all verified; ZERO blocking defects. Three named defects surfaced + fixed with
  disclosure — see the plan-defect register below.
- ✅ 2026-08-17 — § 5A `skill/SKILL.md` (byte-extracted from the plan fence: 61 lines, 3184 bytes)
- ✅ 2026-08-17 — § 5B `skill/modes/bootstrap.md` (byte-extracted; + D3 sync-ready SVA amendment)
- ✅ 2026-08-17 — § 5C `skill/modes/adopt.md` (byte-extracted; + D3 sync-ready SVA amendment)
- ✅ 2026-08-17 — § 5D `scripts/bootstrap_skill.sh` (byte-extracted; `bash -n` PASS at ship state)
- ✅ 2026-08-17 — § 5E retirements (3 × git rm: SETUP / NPB / MDRP)
- ✅ 2026-08-17 — § 5F STANDARDS_INDEX → v2.0 (§ 1 block, § 2 pruned + delivery note, § 3 15-file
  table, § 4 skill path, § 6 v2.0 entry + verbatim migration note)
- ✅ 2026-08-17 — § 5G HOW_TO_USE 1.1 / § 5H README(std) 1.1 / § 5I STANDARDS_LOG 1.1 /
  § 5J OPENER template 1.7 / § 5K CLOSER template 1.5
- ✅ 2026-08-17 — § 5L architecture 0.11 (incl. D1) / § 5M folder_structure 0.14 (incl. 15-rules
  rider + D2) / § 5N SVA 1.8 / § 5O NEW_MACHINE_SETUP 1.2 (Pre-flight renumbered § 5 → § 6)
- ✅ 2026-08-17 — § 5P manifest 2.19 (rows 76–79 added; 24/26/57 deleted; cells bumped;
  stamp-vs-log grep-checked per L063) / § 5Q CHANGELOG release entry
- ✅ 2026-08-17 — QA-A(partial)/B/C/D + QA-G run pre-commit; evidence in the Phase 4 table below
- ✅ 2026-08-17 — Governance 0/0 (stdout in chat) → Rule 10 named review table posted →
  operator gate → `git add -A` (status checked before AND after) → `commit -F`

### Plan-defect register (reconcile pass + QA, 2026-08-17 — per § 15.3 / L056)

- **D1 (minor, editorial):** architecture § 3 trailing sentence "Deleting the machinery
  satisfies…" was not enumerated in § 5L and would have contradicted the new "Never enters" row —
  rewritten alongside the § 5L row edit.
- **D2 (minor, editorial):** folder_structure STANDARDS_LOG tree caption still said "(SETUP copies
  to…)" — retargeted to the delivery skill alongside § 5M.
- **D3 (REAL — the Rule 15 feature-ON class):** § 5B/§ 5C's SET_VERSION_ADOPTED bullets specified
  no shape, but `sync.record_adoption` (sync.py) hard-requires a VERSION comment header, the exact
  `- **Standard Set Version:**` bullet, and the `| Set Version | Adopted on | Notes |` backport
  table — SyncError otherwise. A skill-delivered project would have FAILED its first sync
  (contradicting DD-E + "converge once, sync forever"). Both mode files amended with the
  sync-ready shape; verified by running the engine's own `plan_target` against the QA-B bootstrap:
  11 files validated, NO SyncError, all changed=False. Found by executing the feature, not by
  reading the plan — L067 vindicated.

### Commit 2 — the closure commit (§ 7.3, after QA-E/QA-F) — ✅ 2026-08-17

- ✅ 2026-08-17 — Plan + tracker promoted 1.0 / CLOSED; manifest promotion cells (→ 2.21);
  CHANGELOG closure note; plan § 11 R1/R3/R5/R8 annotated CLOSED. (The QA-F registration landed
  separately as `e9576d2` — config/projects.toml + SESSION_OPENER § 2 registry — keeping this
  commit on the § 7.3 four-file ALLOWLIST.)

## Phase 4 — Validate (QA evidence; ⚑ = Rule 15 feature-ON gate)

| ID | Scenario (plan § 8) | Status | Date | Evidence |
|---|---|---|---|---|
| QA-A ⚑ | Fresh-session skill discovery + Step 0 report line | ✅ | 2026-08-17 | Implement-session half: installer created `~/.claude/skills/standard-docset → <vault>/skill`; Step 0 block executed verbatim: pull "Already up to date.", report `Delivering Standard Set Version v2.0 from vault commit 1a061c6` — v2.0 read LIVE from the working tree (live-reference + supporting-file reads proven; R1 closed). COMPLETED post-release-commit: operator invoked `/standard-docset` in a live session — skill listed + loaded; Step 0 reported `Delivering Standard Set Version v2.0 from vault commit 66d45d5`. Bonus: fresh-install path verified on a second machine (MacBook Air installer run). |
| QA-B ⚑ | Bootstrap end-to-end on a scratch target (zero machinery; SVA stamped; governance 0) | ✅ | 2026-08-17 | Full bootstrap.md walk on a scratch target (answers: sample-cli-project / local CLI / single-agent / CI none): operative footprint complete; machinery scan 0 hits (docs/standards = exactly the 6 topical); marker counts 4/3/2, TEMPLATE-ONLY 0; placeholder scrub 0 on target-owned files; locality `STATUS: OK`; governance scaffolds exit 0 (stdout in chat); single commit, no remote. DECISIVE: engine `plan_target` on the fresh bootstrap → 11 files validated, NO SyncError, all changed=False (sync no-op). One QA-harness bug (duplicated header comments from the executor's header surgery) fixed + re-verified — not a skill defect. Supersedes the OPEN_TASKS "SETUP.md end-to-end live test" item (⏭ there). |
| QA-C | Installer idempotence + re-point | ✅ | 2026-08-17 | Second run → `Already installed:` exit 0; link pointed elsewhere → `Re-pointing (was -> …)` + reinstalled; verified both directions (also exercised in the QA-D restore). |
| QA-D | Step-0 self-pull + offline WARN | ✅ | 2026-08-17 | `file://` scratch clone reset to c9898f0 (behind-by-one), symlink re-pointed → Step 0 observed `Fast-forward` c9898f0..1a061c6 + report line with the tip sha; origin set invalid → WARN line + proceed-on-local-copy observed; symlink restored via the installer. (Report showed Set v1.6 — the clone's committed INDEX predates the release commit; the pull mechanism is what QA-D verifies.) |
| QA-E ⚑ | REAL adopt pilot: Capital-Signal (dry-run list == applied diff; markers intact) — adopt-mode + closure gate; separate session | ✅ | 2026-08-17 | Ran as designed in its own session on the machine holding the target (intake-first walked — vault 67 ⊇ CS 48, zero CS-only lessons; clean tree; § 4 dry-run list posted with D-A…D-D decisions, operator-approved with picks a/a/b/a). Applied as TWO target commits: `d0e0781` (manifest-rename prep, D-D a) + `2caa53e` (adopt, 28 files +3007/−5337 — 29 logical items, LESSONS delete+create recorded as one rename; zero deviation from the approved list). Evidence pack: 20-section CLAUDE.md disposition audit (nothing dropped silently); markers 4/3/2 engine-verified + live `merge_file` idempotence assertion; engine dry-run "up-to-date all 11 items" proven pre-commit from the target side; governance exit 0 verbatim; operational `adopt` → STATUS: OK (57 memory files). Found + logged E001 (upstream defect: CLOSER template § 1.2 references STANDARDS_INDEX.md, which adopters don't carry) — deliberately unpatched locally for merge idempotence, harvest-routed. Both target commits held local (no push). |
| QA-F | Pilot registered + `sync` dry-run reports current | ✅ | 2026-08-17 | Registered in `config/projects.toml` (vault commit `e9576d2`; local transport, machine-affinity note). On the target's machine (Python 3.11.15): `status` → ADOPTED v2.0 / VAULT v2.0 / current / open-log 1; `sync` → "DRY-RUN … [EverOn.Capital-Signal] up-to-date — all suite files match the vault" (11/11 ok); `harvest` → "1 open entry … [EverOn.Capital-Signal] E001 — Session-closer template points at a file adopters don't carry (STANDARDS_INDEX.md)". The harvest hit also satisfies the PLAN-011 requirement-2 verification (entry surfaces vault-side) with a real entry. On the non-holding machine the target reports non-fatally `unknown` (documented degradation, exit 0). |
| QA-G | Zero-hit greps (domain-neutral incl. skill/; no live retired-file refs) | ✅ | 2026-08-17 | Gate 1 (EverOn\|Capital-Signal\|Equinex over docs/standards/ + skill/): **0 hits**. Gate 2 (retired-file names over the sweep set): every hit classified in chat — CHANGE LOG comments, INDEX § 6 history + § 1 Baseline retirement statement, LESSONS L052/L053 bodies, or explicit retirement annotations (architecture § 3/§ 4/§ 10/§ 11, folder_structure "successor to" caption — the § 5L/§ 5M plan-mandated texts); zero live delivery pointers at retired files. Governance 0/0. |

Waiver register (Rule 15): _(empty — QA-E may not be deferred without an explicit operator waiver
recorded here)_

## Phase 5 — Operator gate ⏸

- ⏸ Push authorization — unpushed vault set: `1a061c6` (design) + `66d45d5` (release) + `e9576d2`
  (registration) + the closure commit. (The pilot's own two commits are held local target-side —
  that push is a Capital-Signal-session matter.)
- ⏸ Annotated tag `set-v2.0`
- ✅ 2026-08-17 — OPEN_TASKS reconcile: "SETUP.md end-to-end live test" marked ⏭ superseded by
  QA-B at ship. ⏸ push-state lines flip in the same wrap-up as the push (L055)
