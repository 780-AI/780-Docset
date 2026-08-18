# CHANGELOG

Newest entries at the top.

## [2026-08-18] — Standard Set Version v2.1: E001 integrated via the first harvest → integrate cycle

- **Type:** Standards-suite Minor (Critical File `docs/standards/` — doc-only template fix, no
  engine change; operator-confirmed "Major workflow, no § 15 plan" per the § 15.6 doc-only
  carve-out).
- **What:** The pilot's E001 (logged during the Capital-Signal adoption; surfaced by `harvest`;
  worksheet by `integrate`) is integrated: the SESSION_CLOSER **template** § 1.2 read the Set
  Version from `docs/standards/STANDARDS_INDEX.md` — a vault-side file adopters don't carry —
  now retargeted to `docs/SET_VERSION_ADOPTED.md`, which exists on both sides (the vault
  self-adopts; its own CLOSER instance already read the adoption record since bootstrap). Lesson
  **L068** (template cross-references must resolve in the adopter — SYNC_MAP items +
  skill-created files only) added to the canonical LESSONS (genericized) and `archive/LESSONS.md`
  (project-specific), per the dual-voice practice. L060-class count sweep caught + fixed a stale
  standards README lesson count (48 → 68, drifted since v1.4). E001's suggested mechanized
  delivery-QA grep is **deferred** (documented discipline in L068 only; a new check script would
  be behavior-affecting and beyond this doc-only change) — recorded as an open candidate in
  OPEN_TASKS.
- **QA scenarios (Rule 11; target-side steps follow this commit):**
  - QA-V1 ✅ 2026-08-18 (pre-commit, engine-as-oracle): `sync` dry-run against the edited working
    tree shows for Capital-Signal EXACTLY the intended delta — SESSION_CLOSER merge-update +
    archive/LESSONS replace-update + SET_VERSION_ADOPTED record v2.0→v2.1 — and no other item
    changed. Output verbatim in the session chat.
  - QA-V2 ✅ 2026-08-18 — first real `sync --write`: 3 files written + flushed to Capital-Signal;
    immediate dry-run re-run = up-to-date 11/11 (idempotence). Observed vs chat-predicted delta:
    local-transport flush is a by-design no-op (transport.py Target.flush default) — writes land
    in the target's working tree; the target's own session commits them (matches the
    manifest-reconcile note). Not a defect.
  - QA-V3 ✅ 2026-08-18 — CS `docs/SESSION_CLOSER.md` § 1.2 now reads
    `docs/SET_VERSION_ADOPTED.md` (line 49; instance header engine-bumped 2.0→2.1); CS SVA
    records v2.1 (record row + bullet); genericized L068 present in CS `archive/LESSONS.md`.
  - QA-V4 ✅ 2026-08-18 — write-back applied: CS E001 `Status: integrated → vault L068
    (SESSION_CLOSER § 1.2, Set Version v2.1)` (read back verbatim); `harvest` = no open entries;
    `status` = ADOPTED v2.1 / VAULT v2.1 / current / open-log 0. The harvest → integrate → sync →
    write-back loop is proven end-to-end on a real entry.
  - This entry is the permanent record (Rule 11 lifecycle); OPEN_TASKS rows cleared on completion.
- **Versions:** Set Version v2.0 → **v2.1**; template SESSION_CLOSER 1.5→1.6; standards README
  1.1→1.2; STANDARDS_INDEX 2.0→2.1; SET_VERSION_ADOPTED 1.8→1.9; manifest 2.22→2.23; LESSONS
  files content +L068 (headers unchanged per the no-per-lesson-bump practice). Impact: no vault
  runtime change; adopter-facing template fix propagates at each target's next `sync`.

## [2026-08-18] — Capital-Signal moved to Dropbox: registry re-pointed to a ~-based path

- **Type:** Registration update (Critical File `config/projects.toml`; no engine change).
- **What:** Operator moved EverOn.Capital-Signal from `/Users/parsaazad/Documents/` (MacBook Air)
  into the synced Dropbox folder. Registry entry re-pointed to
  `~/Library/CloudStorage/Dropbox/Projects/EverOn.Capital-Signal` — the registry expands `~` at
  load (`registry.py` `_build_project`), so every machine syncing the folder resolves its own
  copy: the machine-affinity constraint dissolves for this target (registry NOTE updated with the
  `~/`-path exception + the one-machine-at-a-time / let-Dropbox-settle caution). Post-move
  integrity verified on the receiving machine: clean tree, both adoption commits at tip, `fsck`
  clean (dangling objects only). `ls-remote` reconcile (L055) showed CS master = `2caa53e` — the
  pilot's adoption commits are PUSHED (the register's "held local on the Air" note was stale;
  flipped). CS project-data re-linked on this machine (`link`, 57 memory files intact). Project
  SESSION_OPENER § 2 target row updated. Manifest Last-updated block normalized to the
  § 2.6 schema (one Change / one Previous change — three drifted "Prior change" rows dropped).
- **QA scenarios (Rule 11; Rule 15 feature-ON):** all three ✅ 2026-08-18, run from the
  NON-holding machine — the exact capability the change enables (impossible pre-move): `status` =
  CS resolves at the expanded path, ADOPTED v2.0 / VAULT v2.0 / current / open-log 1; `sync`
  dry-run = up-to-date across all 11 SYNC_MAP items (the no-op invariant holds post-move);
  `harvest` = surfaces E001. Outputs verbatim in the session chat.
- **Versions:** manifest 2.21→2.22, project SESSION_OPENER 1.8→1.9. Impact: registry data +
  bookkeeping only — no engine behavior change; sync/harvest/status against CS now run from any
  machine syncing the Dropbox folder (writes one machine at a time).

## [2026-08-17] — PLAN-009 CLOSED: adopt-mode pilot passed (QA-E) + first sync target live (QA-F)

- **Type:** Plan closure (D-5 stage 2; docs-only commit — plan + tracker promotion, manifest cells,
  this note).
- **QA-E verdict (adopt-mode ship gate):** PASSED. EverOn.Capital-Signal adopted to Standard Set
  v2.0 by the skill's adopt mode in its own session on the machine holding the target: intake-first
  walked (lessons delta vault 67 ⊇ CS 48, zero CS-only leftovers), clean tree, operator-approved
  dry-run list (decisions D-A delete / D-B project_rules.md / D-C drop / D-D rename-prep) ==
  applied set line-for-line (29 logical items, zero deviation; target commits `d0e0781` +
  `2caa53e`, held local). Marker/count integrity engine-verified (4/3/2, merge idempotence); the
  pilot logged **E001** — a real upstream template defect (CLOSER § 1.2 references
  STANDARDS_INDEX.md, which adopters don't carry) — into its STANDARDS_LOG instead of patching
  locally: the contribution channel working as designed on day one. E001 = Set v2.1 candidate.
- **QA-F verdict:** PASSED. Pilot registered (`e9576d2`); on the target's machine: `status` current
  (v2.0 = v2.0, open-log 1), `sync` dry-run up-to-date across all 11 SYNC_MAP items (a
  just-adopted target is a sync no-op — "converge once, sync forever" held end-to-end), `harvest`
  surfaces E001 (also satisfying the PLAN-011 harvest-verification requirement with a real entry).
- **Versions:** PLAN-009 0.3→1.0 (CLOSED, § 11 R1/R3/R5/R8 closed), tracker 0.2→1.0 (CLOSED),
  manifest 2.20→2.21. Impact: none at runtime — bookkeeping closure; Phase 5 (push + annotated tag
  `set-v2.0`) remains operator-gated.

## [2026-08-17] — First target registered: EverOn.Capital-Signal (PLAN-009 QA-F)

- **Type:** Registration (Critical File `config/projects.toml` — planned, operator-approved QA-F
  step; no engine change).
- **What:** EverOn.Capital-Signal — adopted to Standard Set v2.0 earlier today by the skill's adopt
  mode (its commits `d0e0781` + `2caa53e`, held local) — registered as the first `sync` target
  (local transport, `/Users/parsaazad/Documents/EverOn.Capital-Signal`, machine-affine note in the
  registry). Project SESSION_OPENER § 2 registry table filled (vault Dropbox path — clears the
  stale `~/Documents/` deferred minor; canonical source = this repo's `docs/standards/`; the
  target row).
- **QA scenarios (Rule 11):** QA-F ✅ 2026-08-17 — vault-side on the machine holding the target:
  `status` = ADOPTED v2.0 / VAULT v2.0 / current / open-log 1; `sync` dry-run = up-to-date across
  all 11 SYNC_MAP items (a just-adopted target is a sync no-op); `harvest` = surfaces the pilot's
  E001 (also satisfying the PLAN-011 harvest-verification requirement with a real entry). Outputs
  verbatim in PLAN-009_tracker Phase 4.
- **Versions:** `docs/SESSION_OPENER.md` 1.7→1.8; manifest 2.19→2.20. Impact: `status`/`drift`/
  `harvest`/`sync` now operate on one registered target; no behavior change to the engine itself.

## [2026-08-17] — Standard Set Version v2.0: skill-based delivery ships (PLAN-009 Phase 3, release commit)

- **Type:** Major (Critical Files: `docs/standards/`; § 15 plan workflow, APPROVED D9.A; release
  commit 1 of 2 per D-5 two-stage close — the plan stays EXECUTING until QA-E, the real adopt-mode
  pilot, passes in a separate session).
- **What:** the delivery machinery is retired and replaced by the vault-side **live-reference
  standard-docset skill**. NEW: `skill/SKILL.md` (mode dispatch + step-0 vault resolve/self-pull) +
  `skill/modes/bootstrap.md` + `skill/modes/adopt.md` (byte-extracted from the plan's § 5A–5C
  fences) + `scripts/bootstrap_skill.sh` (idempotent per-machine symlink installer). RETIRED
  (git rm; git history is the archive): `docs/standards/SETUP.md`, `NEW_PROJECT_BOOTSTRAP.md`,
  `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`. STANDARDS_INDEX → **v2.0** (15 files = 11 binding +
  4 meta; § 2 delivery note; § 6 entry with the no-adopter-action migration note). Live delivery
  pointers swept (HOW_TO_USE, standards README, STANDARDS_LOG template, both session templates);
  architecture §§ 3/4/8/10/11, folder_structure (+ 15-rules rider), SET_VERSION_ADOPTED (vault
  self-adopts v2.0), NEW_MACHINE_SETUP (§ 5 skill-symlink catalog row) synced same-commit.
  Three plan defects fixed in-flight with disclosure (tracker register): D1/D2 editorial; **D3
  real** — the mode files' SET_VERSION_ADOPTED spec lacked the sync-ready shape
  `sync.record_adoption` hard-requires (a fresh delivery would have failed its first sync);
  amended and proven by running the engine's `plan_target` against the QA-B bootstrap (11 files,
  no SyncError, all changed=False — a fresh delivery is a sync no-op).
- **QA scenarios (Rule 11 / Rule 15):** QA-B ✅ (feature-ON: full scratch bootstrap — zero
  machinery, markers 4/3/2, SVA stamped v2.0 + vault sha, locality OK, governance 0, single
  commit, engine sync no-op), QA-C ✅ (installer idempotence + re-point), QA-D ✅ (self-pull
  fast-forward + offline WARN), QA-G ✅ (domain-neutral 0 hits; retired-name hits all
  history/retirement-annotation), QA-A 🔄 partial (Step-0/live-reference half ✅ with evidence;
  fresh-session listing half = operator confirm at the commit gate), QA-E ⏸ (real Capital-Signal
  adopt pilot — adopt-mode + closure gate, separate session), QA-F ⏸ (post-adopt sync no-op on the
  pilot). Evidence verbatim in `docs/Plans/PLAN-009_tracker.md` Phase 4.
- **Versions:** NEW skill/SKILL.md 0.1, skill/modes/bootstrap.md 0.1, skill/modes/adopt.md 0.1,
  scripts/bootstrap_skill.sh 0.1; STANDARDS_INDEX 1.6→2.0; HOW_TO_USE 1.0→1.1; standards README
  1.0→1.1; STANDARDS_LOG template 1.0→1.1; template SESSION_OPENER 1.6→1.7; template
  SESSION_CLOSER 1.4→1.5; architecture 0.10→0.11; folder_structure 0.13→0.14; SET_VERSION_ADOPTED
  1.7→1.8; NEW_MACHINE_SETUP 1.1→1.2; manifest 2.18→2.19; PLAN-009 0.2→0.3 (EXECUTING); tracker
  0.1→0.2. **Impact:** delivery behavior changes (the skill replaces the paste prompts); no engine
  (`src/`) change; adopter on-disk footprint unchanged; `sync` unaffected.

## [2026-08-16] — PLAN-009 approved (D9.A): skill-based delivery — design + tracker

- **Type:** Design session (§ 15 Phases 0–2; docs-only — no behavior change, no engine change).
- **What:** PLAN-009 drafted, Rule 13-hardened, and operator-approved (APPROVE D9.A; D-1
  live-reference, D-2 `skill/` top-level home, D-3 retire NEW_PROJECT_BOOTSTRAP.md, D-4 retire
  MEMORY_DURABILITY_ROLLOUT_PROMPT.md, D-5 two-stage close gated on the real adopt-mode pilot). The
  plan replaces the SETUP.md paste-prompt delivery with a **live-reference Claude Code skill**
  (bootstrap + adopt modes; concierge default + self-service vault clone; step-0 self-pull), retiring
  SETUP/NPB/MDRP from the suite → **Standard Set Version v2.0** at the Phase-3 implement commit. The
  skill carries no copy of the suite (no export step, no parity surface — the L053 fork class removed
  structurally). Spike evidence recorded in the plan: symlinked skill dirs documented as supported;
  four FS probes passed (read into CloudStorage, two-link chain, physical `..`, pathlib). Rule 13
  pass ran the tools against the plan's own fenced bodies (`bash -n` on § 5A/§ 5D; 11/11 FIND anchors
  `grep -F`-verified) and fixed the escaped-backtick anchor defect it found.
- **QA scenarios:** defined in plan § 8 / tracker Phase 4 (QA-A…QA-G, all ⏸) — they gate the Phase-3
  commits per Rule 11; QA-A/B/E are Rule 15 feature-ON gates (QA-E = the real Capital-Signal
  adoption, D-5 closure gate).
- **Versions:** NEW `docs/Plans/PLAN-009_skill_delivery.md` 0.2 (APPROVED) + `docs/Plans/PLAN-009_tracker.md`
  0.1; `docs/documents_manifest.md` 2.17→2.18. No runtime impact.

## [2026-08-16] — Standard Set Version v1.6 + engine Slice 5: `sync` (PLAN-008)

- **Type:** Major (Critical Files: `src/standard_document_updater/` + `docs/standards/`; § 15 plan
  workflow, APPROVED D8.A, single Phase-3 commit, 25-file ALLOWLIST).
- **What:** the last engine slice — **`sync`** propagates the vault suite to every registered adopter
  without clobbering its customizations (architecture § 7): suite-owned files **replaced whole**; the
  three mixed files (`CLAUDE.md`, both session files) **section-merged** — every PROJECT-OWNED block
  preserved verbatim (ordinal matching, STRICT count check, per-file `SyncError` on mismatch — nothing
  written to a structurally surprising target), TEMPLATE-ONLY blocks stripped, the target keeps its own
  header minor-bumped; `docs/SET_VERSION_ADOPTED.md` mechanically updated (bullets + newest-first
  backport row). Dry-run by default; `--write` applies + flushes per target over the PLAN-007 transport
  layer; `--project` filters; `--diff` prints unified diffs; per-target failure isolation (exit 1 +
  FAILED summary); idempotent (second run = all up-to-date); the target's `documents_manifest` is
  deliberately NOT edited (post-write operator note instead, DD-F). Transport grows full-footprint
  sessions (DD-B: `full=True` materializes `docs/` + `archive/` + root `CLAUDE.md`; existing commands
  unchanged). DD-1 folded (deferred since PLAN-004): `setversion.count_open_log_entries` delegates to
  `logentry.parse_log` — exact `open` match, pinned by a regression test. **Standard Set Version
  v1.6** (sync-enablement, marker/wording only — counts stay 15 rules / 67 lessons): TEMPLATE-ONLY
  banner blocks + PROJECT-OWNED instance-heading blocks in the two session templates; this vault's own
  instances wrapped to match (opener 3/3, closer 2/2 owned blocks); template `CLAUDE.md` § 14 marker
  comment → stub-keep wording; SETUP/NPB instantiation wording + L053 v1.5→v1.6 parity retarget.
  The harvest → integrate → sync loop is complete. Registry stays EMPTY — no real target repo read or
  written by this plan; QA ran against tmp fixtures + a scratch local bare git remote.
- **Versions:** engine `__init__` 0.4→0.5 (CLI 0.5.0); `cli.py` 0.4→0.5; `transport.py` 0.1→0.2;
  `setversion.py` 0.1→0.2; NEW `sync.py` 0.1 + `tests/test_sync.py` 0.1; `conftest.py` 0.1→0.2;
  `test_transport.py` 0.1→0.2; `test_cli.py` 0.4→0.5; `test_setversion.py` 0.1→0.2; template
  `SESSION_OPENER.md` 1.5→1.6; template `SESSION_CLOSER.md` 1.3→1.4; `docs/SESSION_OPENER.md` 1.6→1.7;
  `docs/SESSION_CLOSER.md` 1.4→1.5; template `CLAUDE.md` 1.4→1.5; `STANDARDS_INDEX.md` 1.5→1.6;
  `SET_VERSION_ADOPTED.md` 1.6→1.7; `SETUP.md` 1.5→1.6; `NEW_PROJECT_BOOTSTRAP.md` 1.5→1.6;
  `architecture.md` 0.9→0.10; `documents_manifest.md` 2.16→2.17; `folder_structure.md` 0.12→0.13;
  PLAN-008 + tracker 0.1→1.0 (CLOSED).
- **Impact:** new engine behavior — the `sync` subcommand ships (dry-run default; writes only with
  `--write`, and only to registry targets, of which there are none yet). Existing commands' behavior
  unchanged except DD-1: the status/drift open-log count now requires Status exactly `open`
  (case-insensitive) instead of `startswith("open")` — it can no longer disagree with harvest.
  **QA scenarios (Rule 11; per PLAN-008 § 8, tracker Phase 4):** A tools at ship indentation
  (ruff/mypy --strict/pytest 110) ✅; B test_sync 14 cases ✅; C CLI feature-ON local
  (5 CLI cases + manual dry-run → write → idempotent re-run) ✅; D git transport feature-ON vs local
  bare remote ✅; E ssh live path ⏭ operator-waived to the post-registration live smoke (Rule 15
  waiver in tracker; pairs with PLAN-007 QA K–N); F v1.6 stamp/parity greps ✅; G marker integrity
  ✅; H governance ✅; I domain-neutral zero-hit ✅; J manifest completeness ✅.

## [2026-08-16] — Standard Set Version v1.5 — upstream intake: EverOn v2.x → vault (PLAN-010)

- **Type:** Major (Critical Files: both CLAUDE.md copies, docs/standards/, the session routines; § 15
  plan workflow, APPROVED D10.A, single Phase-3 commit).
- **What:** first upstream intake — EverOn.Equinex's post-split standards evolution (its own line
  v2.7, commits `c0940f6..b9c8fe6`, 2026-06-08 → 2026-08-16) folded into the vault as **Set v1.5**:
  eleven genericized lessons (vault L057–L067 in BOTH LESSONS files + an L050 generalization note),
  one NEW binding rule (**Rule 15** — post-implementation verification of the NEW behavior), one
  strengthened rule (**Rule 14** upgraded in place from memory-only durability to full
  **project-data locality**: physical home `.claude/project-data/` for memory + session transcripts,
  managed by `scripts/claude_project_data.sh` `status`/`adopt`/`link`, replacing
  `bootstrap_memory.sh` — deleted; verified at session open `SESSION_OPENER` § 1.5 AND close
  `SESSION_CLOSER` § 1.6). Both CLAUDE.md § 3/§ 13 counts corrected 13 → 15 (stale two
  rule-additions — the L063 class). Release cascade: STANDARDS_INDEX v1.5, SVA adopts v1.5,
  SETUP/NPB retargeted (Step 6.5 / Step 8 → project-data locality + `docs/MACHINE_MIGRATION.md`
  seed), rollout prompt retargeted, NEW_MACHINE_SETUP doubles as the Rule 14 migration catalog,
  manifest + folder_structure synced. Read-only toward EverOn; no engine (`src/`) change; no
  `config/projects.toml` change. This repo's own store migrated via the one-time `adopt` run.
- **Numbering map (EverOn → vault; the § 3 table of PLAN-010, reproduced as the permanent record):**

  | EverOn | Vault | Title (genericized) |
  |---|---|---|
  | L050 | L057 | Identical code + different behavior ⇒ runtime cause; instrument first |
  | L051 | L058 | Audit every caller before fixing a shared utility at one site |
  | L052 | L059 | Verify evidence provenance before recording a result |
  | L053 | L060 | Grep every name-form of a removed identifier across code AND docs |
  | L054 | L061 | A reused helper imports its implicit gates; enumerate them per new context |
  | L055 | L062 | Plan-embedded code must satisfy the plan's own acceptance criteria; sanitize before pasting |
  | L056 | L063 | Version stamps drift from their own change logs; grep the actual stamp |
  | L057 | L064 | Validate on a version-matched runtime; fakes must return real driver types |
  | L058 | L065 | Reconstruct system state from its own event stream |
  | L059 | L066 | A liveness signal comes from the monitored layer's own traffic, on the monitor's own clock |
  | L060 | L067 | Ship-gating verification must exercise the NEW behavior itself |
  | L061 | — | Merged into the Rule 14 upgrade + the L050 generalization note |
  | R14 (theirs) | Rule 15 | Post-implementation verification is MANDATORY |
  | R15 (theirs) | Rule 14 (upgraded) | Project data lives in the project folder |

- **Versions:** root `CLAUDE.md` 1.6→1.7; `docs/standards/CLAUDE.md` 1.3→1.4; both LESSONS headers
  unchanged (1.0, no-per-lesson-bump practice); `docs/SESSION_OPENER.md` 1.5→1.6; template
  1.4→1.5; `docs/SESSION_CLOSER.md` 1.3→1.4; template 1.2→1.3; `STANDARDS_INDEX.md` 1.4→1.5;
  `SET_VERSION_ADOPTED.md` 1.5→1.6; `SETUP.md` 1.4→1.5; `NEW_PROJECT_BOOTSTRAP.md` 1.4→1.5;
  `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` 1.1→1.2; `NEW_MACHINE_SETUP.md` 1.0→1.1;
  `documents_manifest.md` 2.14→2.15; `folder_structure.md` 0.11→0.12;
  `scripts/claude_project_data.sh` NEW 0.1; `scripts/bootstrap_memory.sh` DELETED;
  PLAN-010 + tracker 0.1→1.0 (CLOSED).
- **Impact:** doc/governance impact only — no engine runtime change. Session-routine behavior
  changes: every session open/close now probes project-data locality via the new script; the memory
  store's physical home moved `.claude/memory/` → `.claude/project-data/memory/` (one-time `adopt`
  migration on this repo, run as the final Phase-3 step). **QA scenarios:** doc side Rule 11 exempt
  (standards-suite refresh); script/mechanism side per PLAN-010 § 8 (tracker Phase 4): A `bash -n` ✅,
  B fixture behaviors (adopt/link/pre-v1.5 absorb) ✅, C this-repo `adopt` feature-ON ✅, D
  domain-neutral zero-hit grep ✅, E stamp/count greps ✅, F LESSONS ToC↔heading parity ✅, G
  governance ✅, H delivery-doc parity ✅, I opener § 1.5 live at next session open ⏸, J manifest
  completeness ✅.

## [2026-08-16] — docs/STANDARDS_LOG.md instantiated (closes the self-adoption gap)

- **Type:** Minor (new project doc from the suite's own template; no behavior change).
- **What:** created this repo's own `docs/STANDARDS_LOG.md` from the v1.0 template — the experiences-log
  instance every adopter gets at bootstrap. The suite's self-adoption (PLAN-002 era) skipped the
  instantiation step; the gap sat in OPEN_TASKS since 2026-06-20 ("fix when convenient"). Example entry
  removed per the template's instantiation note; a self-adoption note added (this repo is also the vault,
  so portable lessons codify directly into the LESSONS files — the log exists so the project exercises
  the same contribution channel as any adopter, and so `harvest` has a real in-repo target to read).
- **Versions:** `docs/STANDARDS_LOG.md` new (1.0, manifest entry 67); `folder_structure.md` 0.10→0.11
  (tree + two stale labels caught up: standards/ caption v1.1→v1.4, template LESSONS caption
  L001–L049→L056); `documents_manifest.md` 2.12→2.13 (entry 67 appended; quick-index range; entry 6
  cell 0.9→0.11 staleness caught up).
- **Impact:** none at runtime. A live `harvest` against this repo now finds an (empty) log instead of a
  missing file. **QA scenarios:** Rule 11 exempt (doc creation, no behavior change).

## [2026-08-16] — Standard Set Version v1.4 — process-hardening batch (L052–L056 + L051 recurrence #4)

- **Type:** Major (edits `docs/standards/` + root `CLAUDE.md` — Critical Files). Doc-only; § 15 plan
  workflow not required per § 15.6 (doc edits follow the sync triggers directly). Operator-approved batch
  ("get all 1, 2 and 3 done" — elevate the queued lesson candidates and release v1.4).
- **What:** codified the six queued lesson candidates from OPEN_TASKS into the suite (template
  `docs/standards/LESSONS.md` genericized + `archive/LESSONS.md` project-specific, both append-only,
  headers unchanged per the no-per-lesson-bump practice):
  - **L052** — an installer must CREATE every file it references (the OPEN_TASKS bootstrap-seed gap,
    fixed in `8c990bf`).
  - **L053** — the bootstrap delivery docs (`SETUP.md` / `NEW_PROJECT_BOOTSTRAP.md` / rollout prompt) are
    a **parity set** updated in the same pass; catch-up to a released Set Version is installer-only (no
    Set-Version bump); suite-inventory changes update lay-down + strip set-cover same-commit.
  - **L054** — the § 7 Phase-3 ALLOWLIST must include the plan + sibling-tracker promotion rows
    (PLAN-003/004 undercounted by 2; PLAN-007 proved the fix). Anchored in `CLAUDE.md` § 15.2.
  - **L055** — recorded push-state reconciles against the *real* remote (`git ls-remote`) at session open
    and is flipped in the same wrap-up as the push. Anchored in `SESSION_OPENER` § 1.1 +
    `SESSION_CLOSER` § 1.4 / § 2.1 row 5 (template + project instances).
  - **L056** — the Phase-3 implementer's first act is a reconcile pass of the plan against the live
    source (PLAN-002 D1–D4; recurred through PLAN-007). Anchored in `CLAUDE.md` § 15.3.
  - **L051 recurrence #4** — the Rule 13 tools must run against the § 5 code *at the final indentation it
    ships at* (PLAN-007 D1); appended to L051 in both LESSONS files + sharpened `SESSION_OPENER` § 3.1
    row (project 14 / template 15).
- **Honoring L053 in the same commit:** SETUP.md + NEW_PROJECT_BOOTSTRAP.md retargeted every live v1.3
  reference to v1.4 alongside the release (the parity update rides the release itself, ending the
  catch-up-later pattern). STANDARDS_INDEX § 3 cells for SETUP/NPB/rollout-prompt caught up to their
  already-shipped versions.
- **Versions:** template suite — `LESSONS.md` (content only, header 1.0), `CLAUDE.md` 1.2→1.3,
  `SESSION_OPENER.md` 1.3→1.4, `SESSION_CLOSER.md` 1.1→1.2, `STANDARDS_INDEX.md` 1.3→1.4 (Set v1.4
  release entry), `SETUP.md` 1.3→1.4, `NEW_PROJECT_BOOTSTRAP.md` 1.3→1.4. Adopter instances —
  root `CLAUDE.md` 1.5→1.6, `archive/LESSONS.md` (content only, header 1.0), `docs/SESSION_OPENER.md`
  1.4→1.5, `docs/SESSION_CLOSER.md` 1.2→1.3, `docs/SET_VERSION_ADOPTED.md` 1.4→1.5 (v1.4 backport row).
  Sync — `documents_manifest.md` 2.11→2.12 (incl. stale self-row 2.10→2.12 + quick-index caption
  Set v1.2→v1.4 caught up).
- **Impact:** no runtime/engine impact — governance and suite content only. No standing rule added or
  removed; Rule 13 / § 15 expectations sharpened. Next § 15 plan (PLAN-008) drafts under the sharpened
  L051/L054/L056 discipline.
- **QA scenarios:** Rule 11 exempt (lessons-archive additions + standards-suite refresh + governance-doc
  edits with no behavior impact).

## [2026-06-23] — PLAN-007: remote-target transport (local | git | ssh)

- **Type:** Major (new engine module + a registry-schema change + a `CLAUDE.md` § 1 edit — Critical Files).
  Ran under the § 15 plan workflow (Phase 3 implement). **No Set-Version bump** — engine-only, read-only on
  the vault (no `docs/standards/` file touched), per plan DD-6.
- **What:** gave the engine a **pluggable transport layer** so it operates on a target repo wherever it
  lives — a local folder (unchanged default), a forge remote over SSH (`git`), or a dev host over SSH
  (`ssh`/rsync) — without standing up any server or permanently cloning every org repo. New
  [transport.py](src/standard_document_updater/transport.py): a `Target` ABC + `LocalTarget`/`GitTarget`/
  `SshTarget` drivers + `make_target` + `TransportError`. Each target is *materialized* to a local root
  (`git` = shallow + blobless + sparse-`docs/` clone; `ssh` = rsync of `docs/`), the engine does its
  existing Path-based I/O against that root, and the write path *flushes* back (`git` = commit +
  fast-forward `push origin HEAD:<branch>` with a fixed `Standard DocSet` identity, no `--force`; `ssh` =
  rsync the changed files up). All four commands (`status`/`drift`/`harvest`/`integrate`) became
  transport-aware in one plan; the seam is `cli.py` only (read/write functions keep their Path-based
  signatures, so `integrate.apply_writeback` and its tests are unchanged).
- **Behavior:** a registry entry with `transport = "git"`/`"ssh"` (or a bare local entry — full
  back-compat) parses; the report table column `PATH` → `LOCATION` (transport-aware descriptor). A
  per-target transport failure is **non-fatal for reads** (`status`/`drift` show `unknown`;
  `harvest`/`integrate` warn on stderr + skip); write-back validates **all** dispositions before **any**
  write (per-target atomic). No secrets handled — git/ssh/rsync use the operator's existing SSH agent/keys.
- **Versions:** `transport.py` new (0.1), `test_transport.py` new (0.1); `registry.py` 0.1→0.2, `report.py`
  0.1→0.2, `cli.py` 0.3→0.4, `__init__.py` 0.3→0.4 (CLI 0.3.0→0.4.0); `test_registry.py` 0.1→0.2,
  `test_report.py` 0.1→0.2, `test_cli.py` 0.3→0.4. Docs: `CLAUDE.md` 1.4→1.5 (§ 1 deployment shape),
  `architecture.md` 0.8→0.9 (§ 1/§ 8/§ 9/§ 10/§ 11), `documents_manifest.md` 2.10→2.11 (entries 65–66
  registered, cells bumped, PLAN-007 63–64 → 1.0/CLOSED), `folder_structure.md` 0.9→0.10. Soft
  `[rules.transport]` added to `validation_ownership.toml`; `config/projects.toml` gained git/ssh example
  comments. PLAN-007 + tracker promoted 1.0/CLOSED.
- **Plan-defect (mechanical, recorded):** the verbatim § 5C `statuses.append(report.compute_status(...))`
  line, now indented one level deeper inside the `with` block, was 102 cols — an E501 the Rule 13 pass did
  not catch (the L051 recurrence class). Reflowed output-preserving; no behavior change. Also resolved the
  `no_implicit_reexport` issue in the new test by importing `subprocess` directly (mypy --strict).
- **Impact:** local registries behave exactly as before (only display change: `PATH`→`LOCATION`). A write
  to a remote happens **only** when `integrate --apply … --write` is run against a git/ssh target — a
  separate, operator-gated action.
- **QA scenarios (Rule 11 — all PASS, Phase 4):**
  - ✅ **A** ruff clean (`ruff check src tests`); **B** mypy --strict 0 issues (20 files,
    `MYPYPATH=src python -m mypy`); **C** pytest 88 pass (57 prior + 31 new); **D** governance both exit 0.
  - ✅ **E** local back-compat — existing local `status`/`drift`/`harvest`/`integrate` tests green; only the
    column header changed (`PATH`→`LOCATION`). **F/G** git + ssh registry tables parse (`location` shows
    `git:…@branch` / `ssh:host:path`). **H** each transport missing a required field / unknown transport →
    `RegistryError`. **I** `make_target` dispatch (right driver; bogus → `TransportError`). **J** local
    `session()` yields `project.path` in place (no temp dir; flush/dispose no-op).
  - ✅ **K** git read fetch = `clone --depth 1 --branch … --filter=blob:none --no-checkout` +
    `sparse-checkout set docs` + `checkout` (asserted via monkeypatched `_run`). **L** git push write-back =
    `add` + `commit -c user.name/email` + `push origin HEAD:<branch>`. **M** ssh rsync down/up commands.
    **N** an unreachable git target → `status` row shows `unknown` + the report does not abort (exit 0).

- **Type:** Major (edits `docs/standards/`, a Critical File) — installer-only. **No Set-Version bump**
  (the v1.3 suite CONTENT is unchanged; `STANDARDS_INDEX` untouched).
- **What:** the first real project bootstrap surfaced a gap — SETUP.md (and its long-form companion
  NEW_PROJECT_BOOTSTRAP.md) **gitignored** `docs/Plans/OPEN_TASKS.md` but had **no step to create it**, so
  a fresh project came up without the local-only open-tasks register. Added a seed step to both
  (standard header + "no open items yet" placeholder). `OPEN_TASKS.md` stays gitignored/local-only and is
  **not** manifest-tracked (per Rule 8) — the fix is "create it", not "track it".
- **Versions:** `SETUP.md` 1.2→1.3; `NEW_PROJECT_BOOTSTRAP.md` 1.2→1.3; `documents_manifest.md` header
  2.9→2.10 (entries 24 + 26 → 1.3, self-row entry 5 → 2.10).
- **Also:** the desktop SOURCE export (`~/Desktop/Standard-DocSet-Suite/`) re-synced for the two changed
  files so the next bootstrap is fixed.
- **Impact:** future bootstraps create one additional (gitignored) file. No change to any committed/tracked
  artifact of an adopting project. **Follow-ups (not in this commit):** retrofit the already-bootstrapped
  first project (seed its `OPEN_TASKS.md`); operator decision on a portable lesson L052 (would it cut
  Set v1.4?).
- **QA scenarios:**
  - ✅ **QA-1** (PASSED 2026-08-16 — operator-verified at a real bootstrap of a new project) — *What:*
    SETUP.md bootstrap seeds `docs/Plans/OPEN_TASKS.md`. *How:* run the SETUP.md
    prompt against a fresh TARGET dir. *Pass:* after Step 5, `docs/Plans/OPEN_TASKS.md` exists with the
    standard header, is matched by `git check-ignore`, and does NOT appear in `git status` / the manifest.

## [2026-06-21] — Drift fix: architecture.md §10 roadmap numbering + stale manifest version cells

- **Type:** Minor (doc-only; no engine behavior change). **No Set-Version bump.**
- **What:** (1) [architecture.md](docs/architecture.md) §10 roadmap corrected the stale slice→plan
  numbering — `sync` is **PLAN-008** (was PLAN-007); **PLAN-007** is the remote-target transport
  infrastructure expansion inserted before `sync`. Now matches the live planning state. (2) While syncing
  the manifest, found three version-column cells lagging their files (the column is not governance-validated
  — `check_doc_coverage.py` checks header *presence* + coverage, not cell values): entry 7 architecture.md
  0.6, entry 6 folder_structure.md 0.8, entry 5 manifest self-row 2.1. The v2.2 manifest CHANGE LOG already
  claimed "architecture 0.6→0.7, folder_structure 0.8→0.9 synced" but never edited the cells — so this
  completes that recorded-but-incomplete sync. All values filesystem-verified (Rule 2).
- **Versions:** `architecture.md` 0.7→0.8; `documents_manifest.md` header 2.8→2.9, entry 7 0.6→0.8,
  entry 6 0.8→0.9, entry 5 2.1→2.9.
- **Impact:** none at runtime. **QA scenarios:** Rule 11 exempt (pure doc cleanup, no behavior).

## [2026-06-20] — MEMORY_DURABILITY_ROLLOUT_PROMPT.md step-5 reconciled with Rule 14 (gitignore .claude/)

- **Type:** Major (edits `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md`, a Critical File) — wording
  fix only. **No Set-Version bump** (the Rule 14 capability is unchanged); `STANDARDS_INDEX` untouched.
- **What:** the rollout prompt's step 5 said "Confirm `.claude/` is NOT gitignored." That predated the
  settled practice (this session's quick win + `SETUP.md` Step 6.5 + `NEW_PROJECT_BOOTSTRAP.md` Step 8):
  **`.claude/` IS gitignored** so the store stays untracked + sync-carried *and* a stray `git add -A`
  can never accidentally commit it. Rewrote step 5 accordingly and added `.gitignore` to the prompt's
  ALLOWLIST. Added a CHANGE LOG block to the file (it previously had none).
- **Versions:** `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` 1.0→1.1; `documents_manifest.md` entry 57 1.0→1.1,
  header 2.7→2.8.
- **Impact:** none at runtime; the three delivery docs (SETUP, NEW_PROJECT_BOOTSTRAP, this rollout prompt)
  are now mutually consistent on the gitignore stance. **QA scenarios:** Rule 11 exempt (governance doc).

## [2026-06-20] — NEW_PROJECT_BOOTSTRAP.md caught up to Set Version v1.3 (closes the SETUP parity gap)

- **Type:** Major (edits `docs/standards/NEW_PROJECT_BOOTSTRAP.md`, a Critical File) — walkthrough/doc
  only. **No Set-Version bump** (the v1.3 suite content is unchanged; the long-form walkthrough was just
  behind). `STANDARDS_INDEX` untouched per its rule; the manifest carries the live version.
- **What:** rewrote the Day-Zero walkthrough to full **v1.3 step-parity with `SETUP.md`** (it is the
  long-form companion to that one-shot prompt — now stated explicitly, with a "keep the two in
  step-parity" note). Closed the long-standing parity gap:
  - added the project-local **SESSION_OPENER/CLOSER instantiation** (Step 2), the **experiences-log**
    (`docs/STANDARDS_LOG.md`) create step (Step 4), **Step 8 durable memory (Rule 14)**, and
    **Step 10.5 strip-the-machinery** (with the 6-KEEP / 12-DELETE set-cover matching SETUP.md);
  - retargeted every `v1.1` → `v1.3`; corrected stale counts ("9 standing rules" → **14**,
    "10 binding files" → **11**); added `.claude/` + `docs/Plans/OPEN_TASKS.md` to the `.gitignore`;
    updated the end-state tree, the TOC, and the bootstrap commit message.
- **Versions:** `docs/standards/NEW_PROJECT_BOOTSTRAP.md` 1.1→1.2; `documents_manifest.md` entry 24
  1.1→1.2, header 2.6→2.7.
- **Impact:** no runtime/engine impact; affects only the by-hand bootstrap walkthrough. **QA scenarios:**
  Rule 11 exempt (walkthrough doc). The dispositive check is a live bootstrap (the "SETUP.md end-to-end"
  pending-verification item — now covers both SETUP.md and this walkthrough).
- **Remaining (flagged):** `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` step-5 wording ("not gitignored") is
  still superseded by the Step-8 gitignore stance — a one-line reconcile logged for a future docs pass.

## [2026-06-20] — SETUP.md installer caught up to Set Version v1.3 (durable-memory turn-key)

- **Type:** Major (edits `docs/standards/SETUP.md`, a Critical File) — installer/doc only. **No
  Set-Version bump:** the v1.3 suite *content* is unchanged; only the bootstrap installer was stale
  (left at v1.1 across the v1.2/v1.3 releases). `STANDARDS_INDEX` untouched per its own rule (it bumps
  only at Set-Version releases; the manifest carries the live SETUP.md version).
- **What:** brought `SETUP.md` current so a fresh bootstrap delivers v1.3 turn-key:
  - retargeted every `v1.1` reference to `v1.3` (intro, prompt header, Step 4 CLAUDE.md Source line,
    Step 5 `SET_VERSION_ADOPTED.md`) — a new project now records **v1.3 adopted**, not v1.1;
  - added **Step 6.5 — durable memory (Rule 14)**: create `scripts/bootstrap_memory.sh` + `.claude/memory/`
    + the harness symlink (per `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`), and `.claude/` added to the Step 5
    `.gitignore`;
  - registered `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` in the Step 1 pre-flight check, the Step 3 lay-down,
    and the Step 8.5 strip DELETE list — **fixing the strip set-cover**, which the v1.2 file had silently
    left at 17 of 18 (KEEP 6 + DELETE 12 = 18 ✓).
- **Versions:** `docs/standards/SETUP.md` 1.1→1.2; `documents_manifest.md` entry 26 1.1→1.2, header 2.5→2.6.
- **Impact:** no runtime/engine impact; affects only how a *new* project is bootstrapped. **QA scenarios:**
  Rule 11 exempt (governance/installer doc, no observable CLI/engine behavior change). Live verification is
  the next real bootstrap (the long-standing "SETUP.md end-to-end" pending-verification item).
- **Remaining gap (flagged, not closed here):** `NEW_PROJECT_BOOTSTRAP.md` (the click-through walkthrough)
  still lacks the strip + log + durable-memory steps and the v1.3 retarget; and
  `MEMORY_DURABILITY_ROLLOUT_PROMPT.md` step-5 wording ("not gitignored") is now superseded by Step 6.5.

## [2026-06-20] — Standard Set Version v1.3: lesson L051 (Rule 13 must run the tools)

- **Type:** Major (edits the canonical `docs/standards/` suite, a Critical File) — doc/governance only,
  **Set Version bump v1.2 → v1.3**. Additive Minor at the suite level: no existing rule changed (Rule 13's
  expectations are sharpened, not rewritten); adopters may backport or stay on v1.2.
- **What:** Codified **L051** — the Rule 13 senior-review-and-optimize pass MUST mechanically run the
  linter + type-checker + tests against the EXACT code a plan commits in its § 5 transformation rules
  (not eyeball it); the fix MUST be reflected in § 5 itself (not only narrated in the CHANGE LOG); and the
  recorded result MUST name the specific lines / checks fixed. Motivated by the same defect class (ruff
  `E501`/`UP042`, `mypy --strict`) recurring across **three consecutive plans** (PLAN-003/004/006), each
  time "claimed caught" by the Rule 13 pass but actually shipped to Phase 3.
  - Lesson written into both copies: `docs/standards/LESSONS.md` (genericized, domain-neutral) +
    `archive/LESSONS.md` (project-specific, citing the three recurrences).
  - New `SESSION_OPENER.md` § 3.1 universal catalog row in both the project copy (`docs/SESSION_OPENER.md`,
    row 14) and the template (`docs/standards/SESSION_OPENER.md`, row 15).
- **Versions:** project `SESSION_OPENER.md` 1.3→1.4; template `SESSION_OPENER.md` 1.2→1.3;
  `STANDARDS_INDEX.md` 1.2→1.3 (Set Version + counts + § 6 history; also corrected the stale "as of v1.1"
  § 3 caption and the self-row to current); `SET_VERSION_ADOPTED.md` 1.3→1.4 (adopt v1.3 + backport row);
  manifest 2.3→2.4. **LESSONS file headers unchanged** (no-per-lesson-bump practice; the count is tracked
  in STANDARDS_INDEX/SET_VERSION_ADOPTED). Lesson count 50 → 51 (L001–L051).
- **Impact:** No runtime/behavior impact — governance/process documentation only. **QA scenarios:** Rule 11
  exempt (lessons-archive addition + governance-doc edit, no observable CLI/engine behavior change).

## [2026-06-20] — CLAUDE.md § 4 Critical-files cleanup

- **Type:** Major (edits `CLAUDE.md`, a Critical File) but **doc-only** — no behavior change, no Set
  Version bump. Project-specific (root operating-contract copy only; the template's generic § 4 is
  untouched).
- **What:**
  - Dropped the stale "(created when the engine lands)" note on the `src/standard_document_updater/`
    Critical-File entry — the engine package has existed since PLAN-003.
  - **Promoted `config/projects.toml` to a Critical File.** It is the target-suite registry — it defines
    which repos the tool reads/writes; a silent edit could redirect a write to the wrong repo (the
    highest-cost mistake per `docs/SESSION_OPENER.md` § 2). Editing it is now always Major.
  - Reworked the "Future critical files" list accordingly (config/schema bullet folded into the now-active
    `config/projects.toml` entry).
- **Versions:** root `CLAUDE.md` 1.3→1.4 (header + CHANGE LOG); `docs/documents_manifest.md` entry 1
  1.3→1.4, manifest header 2.2→2.3. `config/projects.toml` is not manifest-tracked (Rule 8 covers `.md`
  + VERSION-headed `.py`/`.sh`; a `.toml` config file is neither) and carries no VERSION header.
- **Impact:** No runtime/behavior impact. **QA scenarios:** Rule 11 exempt (governance-doc edit, no
  observable CLI/engine behavior change).

## [2026-06-18] — PLAN-006 (Slice 4): `integrate` (worksheet + status write-back)

- **Type:** Major / New module — executed under the § 15 plan workflow (PLAN-006, Phase 3). New engine
  code under `src/standard_document_updater/` (a Critical File per `CLAUDE.md` § 4), one mode of which
  **writes to target repos**.
- **What:** Landed the `integrate` command — the deterministic half of the harvest → **integrate** → sync
  loop (architecture § 6c). **A1 division of labor:** the tool is the deterministic spine; the
  genericization, the `L0NN` lesson prose, and the vault edits (LESSONS / topical / Set Version) are
  authored by Claude **in-session** under the § 15 flow — the tool never calls a model and never edits the
  vault.
  - `python -m standard_document_updater integrate` — prints a **read-only worksheet**: every open
    experiences-log entry enriched with its Area→topical routing (unknown/empty Area → `PROJECT_STANDARDS.md`
    + a visible `⚠ unrouted` flag), a proposed **sequential `L0NN`** (vault `max + 1`), and the current Set
    Version. Always exit **0** (informational, like `harvest`/`status`).
  - `integrate --apply <decisions.toml>` — operator-gated **Status write-back**. Default is a **dry-run**
    diff; `--write` actually writes. Validates every disposition first (no partial writes), re-reads each
    target log immediately before writing (architecture § 9), and rewrites **only** the matched `Status:`
    line of the named entry, leaving the rest byte-identical. Errors (exit 2, nothing written) on an unknown
    project or an unresolvable entry.
  - New src module `integrate.py` (Area routing, next-`L0NN`, worksheet render, decisions-TOML parse,
    atomic write-back) with its own `IntegrateError`. New test module `test_integrate.py` (20 unit tests:
    routing / next-`L0NN` / worksheet / decisions parse / write-back atomicity) + 2 `integrate` CLI tests in
    `test_cli.py`. `cli.py`/`__init__.py` 0.2→0.3; soft `[rules.integrate]` ownership-map entry.
- **Impact:** Building the tool is **read-only on the vault** — **no Set Version change** (no `docs/standards/`
  file touched → suite stays **v1.2**). The only target-repo write is the explicit, operator-gated
  `integrate --apply … --write`, a separate later action (not part of building the tool). **CI unchanged**
  (`.gitlab-ci.yml` not touched). `architecture.md` § 8/§ 10 mark integrate implemented and § 11 resolves
  the last OPEN decision (genericization hands off to a Claude session — A1).
- **QA scenarios (Rule 11):** scenarios A–K tracked in `docs/Plans/PLAN-006_tracker.md` Phase 4 —
  A (ruff clean), B (mypy --strict, 18 files), C (full pytest, 57 green), D (both governance scripts exit 0),
  E (worksheet, empty registry → "No open entries…", exit 0), F (worksheet content — project/entry/area→topical,
  proposed `L0NN`, Set Version), G (Area routing — each Area → file; unknown → `PROJECT_STANDARDS.md` +
  `⚠ unrouted`), H (next-`L0NN` against the real `LESSONS.md` → `L051`), I (write-back dry-run — no file
  modified), J (write-back `--write` — only the named `Status:` line changes, rest byte-identical),
  K (write-back safety — unknown project / missing entry → `IntegrateError`, exit 2, no file written).
  E–K exercised both by the pytest suite and live via the CLI against a throwaway fixture (operator-run);
  A–D operator-run.
- **Plan-defect resolution (mechanical, during Phase 3):** D1 — the verbatim § 5A code shipped 5 `E501`
  over-length lines (`next_lesson_id` read-text comprehension, the worksheet footer's 4 adjacent literals,
  and the integrated-Status f-string) that the Rule 13 pass's claimed reflow did not fully catch (the same
  recurring `E501` class as PLAN-003 D2 / PLAN-004 D1). Reflowed all five **output-preserving** — the
  worksheet footer verified byte-identical via SHA-256 before/after (len 345, unchanged); the Status
  f-string re-confirmed by `test_parse_decisions_integrated_and_rejected`. Recorded in the PLAN-006 CHANGE
  LOG + § 11. Additionally, `architecture.md` § 11 (an OPEN decision the plan's § 5D under-specified but
  whose own text mandated resolution at this slice) was marked DECIDED same-commit.

## [2026-06-17] — PLAN-005: durable project memory (Rule 14 + Standard Set Version v1.2)

- **Type:** Major / governance — multiple Critical Files (`CLAUDE.md` ×2, `LESSONS.md` ×2,
  `SESSION_OPENER.md` ×2) + a Set-Version bump. Executed under the § 15 plan workflow (PLAN-005).
- **What:**
  - **Rule 14** added to the operating contract (operative + canonical `CLAUDE.md`): the Claude memory
    store lives inside the repo at `./.claude/memory/` with the harness memory dir symlinked to it, so
    memory survives a machine change and a folder rename/move; repaired idempotently by
    `scripts/bootstrap_memory.sh`.
  - **`SESSION_OPENER.md` § 1.5** (operative + template): a session-start memory-link health check that
    verifies the link, auto-repairs a stale/missing one, and HALTS-on-empty (forcing function) + a § 3.1
    catalog row.
  - **L050** added to both `LESSONS.md` copies — the 2026-06-17 memory-loss incident (harness memory was
    machine-local + path-keyed, so a machine change + folder move wiped it; recovered losslessly from a
    Dropbox backup of the prior machine's `~/.claude`).
  - New tracked tooling `scripts/bootstrap_memory.sh`; new adopter `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`;
    new project-local `docs/NEW_MACHINE_SETUP.md` (re-home checklist).
  - **Standard Set Version v1.1 → v1.2** (additive Minor) — STANDARDS_INDEX § 1/§ 2/§ 3/§ 6 + counts
    (18 files / 50 lessons / 14 rules); SET_VERSION_ADOPTED records adoption; manifest + folder_structure
    synced; engine slices renumbered (integrate → PLAN-006, sync → PLAN-007).
- **Impact:** Governance + tooling only — **no engine behavior change**. The durable store + symlink were
  established interactively the same day; this commit codifies + hardens + propagates them. The memory
  **content** stays untracked (Dropbox-carried); only the bootstrap tooling is committed.
- **QA scenarios (Rule 11):** A–G in `docs/Plans/PLAN-005_tracker.md` Phase 4 — A (bootstrap idempotent),
  B (self-heal after symlink removal), C (write-through), D (empty-store halt wording), E (governance
  exit 0), F (Set-Version consistency v1.2 / 18 / 50 / 14), G (fresh-machine toolchain smoke — verified
  2026-06-17: engine 0.2.0, ruff + mypy --strict + 35 tests + governance green, SSH push reachable).

## [2026-06-16] — PLAN-004 (Slice 3): `harvest` (consolidate open experiences-log entries)

- **Type:** Major / New module — executed under the § 15 plan workflow (PLAN-004, Phase 3). New engine
  code under `src/standard_document_updater/` (a Critical File per `CLAUDE.md` § 4).
- **What:** Landed the read-only `harvest` command:
  - `python -m standard_document_updater harvest` — reads **every registered project's**
    `docs/STANDARDS_LOG.md`, collects the entries whose `Status` is `open`, and prints a **consolidated
    report grouped by area** to stdout; always exit **0** (informational, like `status` — not a gate).
  - Conservatively flags likely cross-project duplicates (D3): two open entries are flagged only when
    their *normalized titles match* AND they come from *different* projects (`⚠ possible duplicate of
    <project>/<E0NN>`). Same-project repeats and distinct titles are not flagged.
  - 2 new src modules — `logentry.py` (parse a `STANDARDS_LOG.md` into `LogEntry` records; controlled-vocab
    fields reduce a status write-back like `integrated → vault L050` to `integrated` so it is correctly
    not-open) and `harvest.py` (pure render: collect → group-by-area → cautious dup flag, no filesystem).
  - 2 new test modules (`test_logentry.py`, `test_harvest.py`) + 2 harvest CLI tests in `test_cli.py`;
    `cli.py`/`__init__.py` 0.1→0.2; soft ownership-map entries for `logentry`/`harvest`.
- **Impact:** **Read-only** — writes nothing (not to any target, not to disk; the source logs are the
  durable record per D1). **No Set Version change** (no `docs/standards/` file touched → suite stays
  **v1.1** — the engine reads the log, it does not alter the suite). **CI unchanged** (`.gitlab-ci.yml`
  not touched — "stay small"). `--json` deferred (D2); `setversion.count_open_log_entries` DRY-delegation
  to `logentry.parse_log` deferred (plan § 11 DD-1, logged to OPEN_TASKS).
- **QA scenarios (Rule 11):** scenarios A–H tracked in `docs/Plans/PLAN-004_tracker.md` Phase 4 —
  A (empty registry → "No open log entries…", exit 0), B (one project, 2 open entries listed, exit 0),
  C (status write-back excluded — `is_open` False), D (cross-project same-title flagged both ways),
  E (same-project same-title not flagged), F (distinct titles not flagged), G (grouping across ≥2 areas,
  sorted), H (ruff + mypy --strict + full pytest green; both governance scripts exit 0). B–G are covered
  by the pytest suite; A, B, C, D, G also exercised live via the CLI; H operator-run.
- **Plan-defect resolution (mechanical, during Phase 3):** D1 — the verbatim § 5B report-append line was
  103 cols (ruff `E501`); reflowed to a wrapped `lines.append(...)` call. Production output is
  byte-identical; recorded in the PLAN-004 CHANGE LOG.
- **Version bumps:** new files `logentry.py`/`harvest.py`/`test_logentry.py`/`test_harvest.py` at v0.1;
  `cli.py` 0.1→0.2, `__init__.py` 0.1→0.2 (CLI version 0.1.0→0.2.0), `test_cli.py` 0.1→0.2;
  `architecture.md` 0.4→0.5, `folder_structure.md` 0.6→0.7, `documents_manifest.md` 1.7→1.8 (entries
  50–53); PLAN-004 + tracker promoted 0.1→1.0/CLOSED.
- **Author:** Yaser Khosravi

## [2026-06-16] — PLAN-003 (Slice 2): registry + `status` / `drift` (first engine code)

- **Type:** Major / New module — executed under the § 15 plan workflow (PLAN-003, Phase 3). First Python
  engine code under `src/standard_document_updater/` (a Critical File per `CLAUDE.md` § 4).
- **What:** Landed the vault-side managed-projects registry plus two read-only commands:
  - `python -m standard_document_updater status` — table of every registered project (adopted vs vault
    Set Version, state, open-log count); always exit 0.
  - `python -m standard_document_updater drift` — only projects **not** on the vault Set Version; exits
    **1** if any exist (`behind`, `ahead`, **and** `unknown` all count as drift).
  - Registry `config/projects.toml` stores **name + path only**; a project's adopted Set Version is read
    **live** from its `docs/SET_VERSION_ADOPTED.md` at report time (single source of truth, never cached).
  - 7 src modules (`__init__`, `__main__`, `errors`, `registry`, `setversion`, `report`, `cli`) +
    `pyproject.toml` (setuptools src-layout; ruff / mypy-strict / pytest config) + a pytest suite
    (`conftest` + 4 test modules) + a soft ownership-map entry in `scripts/validation_ownership.toml`.
- **Impact:** **Read-only** — no command in this slice writes to any target repo. **No Set Version
  change** (no `docs/standards/` file touched → suite stays **v1.1**). **CI unchanged** (`.gitlab-ci.yml`
  not touched — the `test` stage is deferred to a later slice per the plan's "stay small" constraint).
- **QA scenarios (Rule 11):** scenarios A–I tracked in `docs/Plans/PLAN-003_tracker.md` Phase 4 —
  A (empty registry → "No projects registered", exit 0), B–C (status current/behind), D–E (drift exit
  0/1), F (unknown counts as drift), G (open-log count), H (pytest + mypy --strict + ruff green),
  I (governance scripts exit 0). B–G are covered by the pytest suite; A, H, I are operator-run smokes.
- **Version bumps:** new engine files at v0.1; `folder_structure.md` 0.5→0.6, `architecture.md` 0.3→0.4,
  `documents_manifest.md` 1.5→1.6 (registered entries 36–47); PLAN-003 + tracker promoted 0.1→1.0/CLOSED.
- **Author:** Yaser Khosravi

## [2026-06-14] — Project renamed to "Standard DocSet"

- **Type:** Major / Identity (Critical-file edit: `CLAUDE.md` § 1)
- **What:** Renamed the project's display name `standard-document-updater` → **"Standard DocSet"** (Option B —
  display/identity only). Updated root `CLAUDE.md` § 1, `README`, `docs/README`, the project-local
  `SESSION_OPENER`/`SESSION_CLOSER`, `SET_VERSION_ADOPTED`, `architecture`, `folder_structure`, and the
  `.gitlab-ci.yml` header comment. The Python engine package identifier `standard_document_updater`
  (`src/standard_document_updater/`) is **deliberately unchanged** — it can be renamed when the engine lands.
- **Remote:** the GitLab project was renamed (name "Standard DocSet", path slug `standard-docset`); local
  `origin` re-pointed to `git@gitlab.com:yaser.khosravi/standard-docset.git`.
- **Not changed:** the historical `PLAN-001` record keeps the old name (it documents the state at that time).
  The local folder rename (`~/Documents/Standard document updater` → `Standard DocSet`) is handled separately.
- **Impact:** No runtime impact (identity/display only).
- **Version bumps:** CLAUDE.md 1.1→1.2, SESSION_OPENER 1.1→1.2, SESSION_CLOSER 1.1→1.2,
  SET_VERSION_ADOPTED 1.1→1.2, architecture 0.2→0.3, folder_structure 0.4→0.5, documents_manifest 1.3→1.4.
- **Author:** Yaser Khosravi

## [2026-06-13] — PLAN-002 (Slice 1): setup-and-strip + experiences log + PROJECT-OWNED markers (Set Version v1.1)

- **Type:** Major / Governance / Critical-file edit (`docs/standards/`, `CLAUDE.md`) — executed under the
  § 15 plan workflow (PLAN-002, Phase 3).
- **What:** Made the architecture's footprint + non-clobbering-sync model real at the document layer:
  (a) added the **experiences-log template** `docs/standards/STANDARDS_LOG.md` (the per-project
  contribution channel fed by `SESSION_CLOSER` § 1.7); (b) wrapped the project-customizable blocks of
  `CLAUDE.md` (§ 1/§ 4/§ 13/§ 14), `SESSION_OPENER` (§ 2/§ 3.2), and `SESSION_CLOSER` (§ 2.2) — in **both**
  the templates and this repo's adopter instances — in **`PROJECT-OWNED` markers** so a future `sync`
  preserves them; (c) reworked `SETUP.md` into **setup-and-strip** (create the log, write
  `SET_VERSION_ADOPTED` to `docs/`, then strip the setup machinery as a second commit, with a set-cover
  safety check); (d) **moved** `SET_VERSION_ADOPTED.md` from `docs/standards/` → `docs/` so it survives the
  strip; (e) fixed the stale "created when the engine lands" drift on the two `docs/architecture.md`
  references in root `CLAUDE.md`.
- **Set Version:** bumped the canonical suite **v1.0 → v1.1** (additive Minor) per `architecture.md` § 9
  ("every change to the suite bumps per-file VERSION + the Set Version"); this repo adopts v1.1 same-commit.
- **Plan-defect resolutions (operator-approved during Phase 3):** D1 — corrected the strip DELETE list to
  11 files (dropped `SET_VERSION_ADOPTED`, which the move removes from the crate) so the set-cover is
  complete (11 DELETE + 6 KEEP = 17). D2 — the Set-Version bump above. D3 — added `STANDARDS_LOG.md` to
  SETUP's confirm/lay-down lists. D4 — expanded the ALLOWLIST by `README.md` + `NEW_PROJECT_BOOTSTRAP.md`
  so all old-path references could be fixed (risk R3 → 0 stale hits, excluding the historical PLAN-001 record).
- **Impact:** No runtime impact (docs/prompt/markers only — no engine code). Changes the `SETUP.md`
  bootstrap *procedure* (now strips + creates the log + writes SVA to `docs/`) and adds the marker
  convention every future adopter inherits.
- **QA scenarios (Rule 11):** S1 marker pairing, S2 SETUP strip set-cover, S3 no-names scrub — defined in
  `docs/Plans/PLAN-002` § 8 and tracked in its § 4 Phase 4.
- **Sync:** `STANDARDS_INDEX` (Set v1.1 + STANDARDS_LOG + counts), `documents_manifest` (v1.3, renumbered to
  33 entries), `folder_structure` (v0.4), `architecture` (v0.2, § 10 Slice 1 ✅), `SET_VERSION_ADOPTED`
  (v1.1, moved), `README`. PLAN-002 promoted to v1.0 / CLOSED.
- **Author:** Yaser Khosravi

## [2026-06-13] — System design captured: docs/architecture.md

- **Type:** Major / Design record (docs-only)
- **What:** Committed `docs/architecture.md` — the system-design record converged with the operator in
  the 2026-06-13 design session. Captures: the **vault model** (this repo is the single canonical home),
  the **project footprint** (operative standard kept / setup-machinery stripped), **setup-and-strip**
  delivery, the **experiences log** (`docs/STANDARDS_LOG.md`) contribution channel fed by
  `SESSION_CLOSER` § 1.7, the **harvest → integrate → sync** loop, and the **`PROJECT-OWNED` marker**
  ownership model for non-clobbering sync. Includes the implementation roadmap (Slices 1–5 → plans).
- **Impact:** No runtime impact (design doc). Defines what the engine will implement; the engine source
  becomes the dispositive truth and this doc is kept in sync per `CLAUDE.md` § 4.
- **Sync:** manifest (entry 31, v1.1), `docs/folder_structure.md` (v0.3), `docs/README.md` updated.
- **Author:** Yaser Khosravi

## [2026-06-07] — PLAN-001: domain-neutral canonical suite (Standard Set Version v1.0)

- **Type:** Major / Governance / Critical-file edit (`docs/standards/`)
- **What:** Scrubbed all project identity (names, source-domain examples) from the standards suite and
  reset it to a clean **Standard Set Version v1.0** baseline; added the canonical `docs/standards/CLAUDE.md`
  and `docs/standards/LESSONS.md` templates (optional Codex § 14 kept in the template); added
  `docs/standards/SETUP.md` (one-shot bootstrap prompt) and slimmed `HOW_TO_USE.md` to a pointer;
  reconciled this project's own adopter files (manifest, root `CLAUDE.md`, session routines,
  `SET_VERSION_ADOPTED`) to v1.0.
- **Impact:** No runtime impact (docs/governance only). The suite is now domain-neutral and distributable.
- **Verification:** dispositive scrub grep over the suite + adopter governance files = **0 hits**; every
  `docs/standards/*.md` at VERSION 1.0; governance scripts exit 0.
- **Plan:** PLAN-001 (CLOSED) — Rule 13 senior-review pass recorded; Phase 3 landed as one commit.
- **QA scenarios:** S1 scrub-grep zero-hit ✅; S2 SETUP source-path dry-run ✅.
- **Author:** Yaser Khosravi

## [2026-06-07] — Project bootstrap: governance scaffold

- **Type:** Major / Infrastructure / Bootstrap
- **Files:** `CLAUDE.md` (repo root), `docs/standards/*.md` (13 standards files + `SET_VERSION_ADOPTED.md`),
  `docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`, `archive/LESSONS.md`, `README.md`, `docs/README.md`,
  `docs/documents_manifest.md`, `docs/folder_structure.md`, `docs/Plans/.gitkeep`,
  `scripts/check_doc_coverage.py`, `scripts/check_test_coverage_drift.py`,
  `scripts/doc_coverage_allowlist.toml`, `scripts/validation_ownership.toml`,
  `.gitlab-ci.yml`, `.gitlab/merge_request_templates/Default.md`, `.gitignore`
- **Impact:** No runtime impact. Establishes the operating contract (13 standing rules), the adopted
  standards suite, session start/end routines, document manifest, governance scripts, CI scaffold, and
  MR template before any feature work begins.
- **Standards:** Bootstrapped from the standards suite at **Standard Set Version v1.0** on
  2026-06-07 — independent versions from this point forward. Backports from the standards source are
  explicit (see `docs/standards/STANDARDS_INDEX.md` § 4.3).
- **Customizations:** single-agent project (Codex handoff § 14 omitted); domain-neutral local-CLI
  context in `CLAUDE.md` § 1 / § 4 / § 13; project-local `SESSION_OPENER`/`SESSION_CLOSER` tailored to a
  no-remote-infra, source→target propagation workflow.
- **QA scenarios:** none (no runtime code in this commit).
- **Author:** Yaser Khosravi
