<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Status: DRAFT (Phase 1 — awaiting Phase 2 operator approval "APPROVE PLAN-011") -->
<!--
CHANGE LOG
v0.1 — 2026-10-03 — Initial draft (Phase 0 audit + Phase 1 design). Scope set by the live fleet
state: Capital-Signal, 780-Automation and 780-VPN are already converged + registered (fleet v2.5);
EverOn.Equinex is the last known unconverged project. Phase 0 delta audit: Equinex holds ONE lesson
+ ONE rule the vault lacks (L062 / Rule 16 — feature intake) plus uncodified machine-migration
guidance; adoption complications catalogued (rule/lesson numbering collisions, zero PROJECT-OWNED
markers, header-less session files). Rule 13 pass RUN same-day (record at the foot): 6 findings
fixed in place — project-rules annex destination (pilot pattern), vault-clean-at-release gate,
intervening-release rule for QA-F6, write-back landing note, tracker decision range, this record;
plus the Rule 10 read-through fix: QA-F2's grep made unambiguous (no `-c`; pass = no output).
-->

# PLAN-011 — Fleet convergence: Equinex intake + adoption (EverOn line retirement)

## 1. Goal

Converge **EverOn.Equinex** — the last known project still running its own divergent copy of the
suite — onto the vault, and with it close the fleet-adoption program. Per the lifecycle principle
(*the skill converges a project once; the engine syncs it forever*), the per-project flow is:

1. **Intake first** — every Equinex lesson / rule / suite-level novelty the vault does not hold is
   listed, explained and recommended at a **Rule 16 gate**; confirmed items are genericized and
   integrated vault-side as one Standard Set Version release, synced to the three live targets.
2. **Converge** — a dedicated Equinex session runs the skill's **adopt mode** (dry-run gated,
   customization-preserving); the own-line suite artifacts retire; Equinex's pre-adoption lesson
   archive is preserved per D-2 together with a numbering crosswalk (nothing destroyed — the
   780-Automation discard class, L069).
3. **Register** — Equinex becomes a local `~/` sync target; the log-recording discipline is proven
   end-to-end with a real harvest → write-back on its `STANDARDS_LOG.md`.

After this plan the steady state holds fleet-wide: lessons flow in only via STANDARDS_LOG →
harvest → integrate; suite updates flow out only via `sync`; no project authors its own Set line.

**Origin:** OPEN_TASKS PLAN-011 block (operator-approved 2026-08-16; scope expanded to team
projects 2026-08-16; EverOn line retirement DECIDED 2026-08-16). The team-rollout half has
already happened outside a plan: 780-Automation (2026-08-19) and 780-VPN (2026-08-27) were
bootstrapped self-service and registered, and the pilot (Capital-Signal) closed under PLAN-009.

## 2. Operator constraints (binding — decided earlier, recorded here)

- **EverOn line RETIRES; the vault is its upstream** (decided 2026-08-16). At convergence Equinex
  stops authoring its own Set line: no own Set-Version bumps, no manual cross-backports.
- **Log-recording discipline (operator requirement 2026-08-16)** — binding requirements 1–3:
  (1) line retirement at convergence; (2) `docs/STANDARDS_LOG.md` instantiated, new lessons land
  ONLY as `E0NN` entries, verified by a harvest of a post-adoption entry; (3) integration closes
  the loop via the engine's Status write-back (`integrated → vault L0NN` / `rejected`).
- **Rule 16** — no intaken content enters the suite without the complete list, per-item
  plain-language explanation + recommendation, and the operator's explicit per-intake confirmation.
- **Intake before converge** (skill adopt.md § 2) — adoption must never overwrite novelties before
  they are captured.
- **Never assume paths** — Equinex's path below was probed live 2026-10-03; the operator confirms
  it at Phase 2.
- **Equinex is a live, high-stakes project** (trading EA, very active — tags v7.39 → v7.41 since
  2026-08-27): the adoption touches governance docs only; runtime trees are never modified.
- **One machine at a time** — Equinex is Dropbox-synced; no vault write into it while an Equinex
  session is mid-work, and Dropbox settles between machines.
- **Rule numbering never changes — only append** (CLAUDE.md § 3, both copies) — binds D-6.
- **Plan-first, two-session split** (§ 15.3) — Phase 3 runs in separate sessions from this design.

## 3. Scope summary

**In scope**

- **S1 — Equinex intake (vault session).** The Phase 0 candidate list below is re-verified against
  Equinex's tip at execution, gated (Rule 16), and the confirmed items are integrated (genericized)
  as **one Set release**, synced to the three registered targets.
- **S2 — vault-side fixes riding the S1 release (found by this audit):**
  - `skill/modes/adopt.md` § 3 is silent on where a converging project's own archive goes, while
    `archive/LESSONS.md` is a SYNC_MAP *replace* item — D-2 settles it; § 5C carries the fix.
  - **Rule 12 step-6 drift (L063 class):** both the template and the vault root CLAUDE.md still
    read "`/tmp/` cleanup" while both SESSION_CLOSERs were retitled "§ 1.6 `/tmp/` cleanup +
    locality confirm" at v1.5 — § 5D.0 carries the verbatim fix.
- **S3 — Equinex adoption (Equinex session).** Skill adopt mode with TARGET = Equinex, under the
  extra requirements of § 5E: mapping table with a disposition for every customization, numbering
  crosswalk, § 4 dry-run gate, apply, validate, single adopt commit (no push).
- **S4 — registration + discipline proof + closure (vault session).** Registry entry + SESSION_OPENER
  § 2 row; status / sync dry-run / harvest QA; the requirement-2/3 log round-trip (QA-F7).

**Out of scope (routed elsewhere — confirm at D-1)**

- **DD-6b** (git merge-request write-back): no registered or planned target uses git transport;
  Equinex is local. Re-opens when a git-transport target appears.
- **Delivery-kit codification** (`make_kit.sh` + tracked kit README — the 2026-08-19
  "hassle-free" concern): a new-project delivery concern, not convergence. Own Minor/plan.
- **780-VPN's E001** (trusted clock): its own Rule 16 gate (presented 2026-10-03) and, for the
  engine half, its own plan. If its release ships first, S1's release takes the next version (D-5).
- **Equinex's local lesson-candidate queue** (58 uncodified items in its gitignored OPEN_TASKS):
  not codified content, so not intaken here. After adoption its wrap-up routes confirmed
  candidates as `E0NN` entries (SESSION_CLOSER § 1.7 binding rule) — including "Address drift
  first", which Equinex had queued as its own `L063` (must NOT be appended locally).
- **Unknown fleet members** (D-3): if the operator names more projects, each is added by amendment
  before Phase 2, or after closure as its own small plan.
- **Capital-Signal's uncommitted engine writes** (v2.1 → v2.5 backlog): a CS-session task; R4
  covers the interaction with S1's sync.

### Phase 0 audit findings (2026-10-03, read-only; Equinex tip `cf25e70`, tag v7.41)

**Baseline.** PLAN-010 audited Equinex commits `c0940f6..b9c8fe6` (own Set v2.7, 15 rules, 61
lessons) and mapped its L050–L060 → vault L057–L067, its L061 → the vault Rule 14 upgrade + L050
note, its R14 ↔ vault R15 and R15 ↔ vault R14 (PLAN-010 § 3 mapping table). No newer own-line Set
version exists (its STANDARDS_INDEX still declares v2.7); later changes landed without a Set bump.

**Lesson delta (`archive/LESSONS.md` v1.18, 62 lessons, contiguous L001–L062):**
L001–L049 present in the vault under the same numbers (bodies identical modulo genericization);
L050–L061 present per the PLAN-010 map; **L062 ABSENT** — the only new lesson. No partial overlaps
of substance (two domain-flavored sub-points of their L058 were left out of vault L065 by design).

**Rule delta (`CLAUDE.md` v3.14, "16 standing rules"):** R1–R13 match; R14/R15 swapped vs the vault
(substance equivalent; the vault versions are stronger — HALT-on-empty + drift clauses); **R16
"Feature-intake workflow" ABSENT** from both vault copies — and its number collides with the vault
root's own Rule 16 (the harvest gate), under the only-append numbering rule (→ D-6). Equinex has
the R12 step-6 wording right where the vault drifted (→ S2).

**Intake candidates for the Phase 3a Rule 16 gate (preliminary recommendations):**

| # | Candidate | Source | Preliminary recommendation |
|---|---|---|---|
| C1 | Feature-intake workflow — brief preserved byte-faithful as an idea source only (binds nothing; operator directives override it; per-item adopt/deviate), investigate before designing (live audit by `file:line`, existing-machinery inventory, overlap with open plans, pre-test the hypothesis), redesign from scratch per repo conventions, formalize as a § 15 plan | `CLAUDE.md` R16 (:294) + 3.13 sharpening (:7, :300); `archive/LESSONS.md` L062 (:158) | **Genericize → integrate** as a canonical lesson + the § 15.9 landing chosen at D-6 (step-3 EA specifics — restart-surviving state latches, threshold-pair exits, Monitor check — reduced to generic form) |
| C2 | Synced-folder operation rules — one machine at a time (cloud-drive conflicted copies inside `.git/` are corruption, not a merge conflict), sync-green before switching, keep the folder pinned offline, per-machine `link`, push promptly (unpushed commits exist only in the synced `.git/`) | `docs/MACHINE_MIGRATION.md` § 6.1 (:139–155) | **Genericize → integrate** (canonical lesson + the machine-migration guidance — landing proposed at the gate) |
| C3 | Fresh-clone git identity check — a new machine silently commits under a bogus author until `user.name/email` are set | `docs/MACHINE_MIGRATION.md` § 4 (:101) | **Genericize → integrate** with C2 |
| C4 | Secrets-in-cloud trade-off — gitignored secrets in a cloud-synced folder still travel; accept explicitly | `docs/MACHINE_MIGRATION.md` § 6.2 (:157) | **Integrate as a caution inside C2** (the project's own acceptance stays project-local) |
| C5 | Delegated subsystem manifest tracking (not exclusion) | `CLAUDE.md` R8 bullet (:149) | **Keep as Equinex customization**; portable kernel → its first post-adoption `E0NN` |
| C6 | Committed canonical config as the single QA base | `CLAUDE.md` § 4 (3.14) | **Keep as Equinex customization**; portable kernel → `E0NN` |
| C7 | Optional orientation-graph aid (advisory) | `docs/SESSION_OPENER.md` § 1.5 (:56) | **Keep as Equinex customization** (tool-specific) |

**Adoption complications (drive § 5E):** (1) `docs/SESSION_OPENER.md` / `SESSION_CLOSER.md` have
no VERSION header (`#` title first; change log as a trailing section — the opener's log also skips
v1.15) → instantiate from the templates. (2) **Zero PROJECT-OWNED markers** anywhere (the
templates carry CLAUDE 4 / OPENER 3 / CLOSER 2) → wrap per adopt § 3. (3) Customizations inside
suite-owned regions that a merge would revert — CLAUDE R8 bullet, R9/R11/R14 EA wording, R12 step
6; OPENER § 1.2 live-state probes, § 1.5 orientation aid, MQL5-flavored § 3.1 rows, § 4 block;
CLOSER § 1.2. (4) **Numbering collisions in live text**: "Rule 14" 100 hits / 18 `.md` files,
"Rule 15" 45 / 14, "Rule 16" 43 / 9 (+ 11 memory files); own-line L050–L062 cited in CLAUDE.md 11×,
SESSION_OPENER 35×, SESSION_CLOSER 1×, plans 221×, memory 15× — immutable history included.
(5) No SVA, no STANDARDS_LOG. (6) `scripts/claude_project_data.sh` is v0.1 on both sides but
differs (the vault copy is a separate lineage with the memory-symlink adopt branch) — equal
stamps must not suppress the replace. (7) Seven vault-only meta/template files in its
`docs/standards/` that the engine never touches (retire, as the pilot did). (8) Clean-tree gate
fails today: untracked `docs/Plans/margin-hike-guard-brief.md` (since 2026-08-20). (9) § 14
Multi-agent = Yes (Codex) → the template's § 14 PROJECT-OWNED block. Already present and kept:
governance scripts + TOMLs, `docs/MACHINE_MIGRATION.md` (v0.3), Rule 14 project-data (55 memory
files), `.claude/` + OPEN_TASKS gitignored.

## 4. Phase tracker (high-level — granular sub-tasks in `PLAN-011_tracker.md`)

- Phase 0 — Audit: ✅ 2026-10-03
- Phase 1 — Design + Rule 13 pass: ✅ 2026-10-03
- Phase 2 — Operator approval (D11.A + D-1…D-6): ⏸
- Phase 3a — Intake + release (vault session; commit § 7.2): ⏸
- Phase 3b — Equinex adoption (Equinex session; target commit § 7.3): ⏸
- Phase 3c — Registration + discipline proof (vault session; commit § 7.4, closes the plan): ⏸
- Phase 4 — Validate (QA-F1…F8, each recorded at its phase): ⏸
- Phase 5 — Operator gate (vault push + release tag; Equinex push is the operator's own call): ⏸

## 5. Transformation rules (verbatim per Rule 7; gate-dependent steps as mechanical rules)

### 5A — `config/projects.toml`: append the Equinex entry (Phase 3c)

Append after the last `[[project]]` table (780-VPN), separated by one blank line. Proven
2026-10-03 against a scratch copy: `load_registry` loads it as `LocalTarget` at the expanded path
and `session()` materializes the live repo.

```toml
[[project]]                        # PLAN-011 convergence (EverOn line retired); adopted via the skill (adopt mode)
name = "EverOn.Equinex"
path = "~/Library/CloudStorage/Dropbox/Projects/EverOn.Equinex"   # Dropbox-synced; ~ resolves per machine
# NOTE: high-stakes live project — every engine write lands in its working tree (local flush =
# write-in-place); its next session lands per docs/SYNC_HANDOFF.md BEFORE any other work.
# Write only between Equinex work sessions, one machine at a time.
```

### 5B — `docs/SESSION_OPENER.md` (project instance; Phase 3c)

Header: `<!-- VERSION: 1.16 -->` → `<!-- VERSION: 1.17 -->`; `Last Updated` → the Phase 3c date;
CHANGE LOG line prepended above `v1.16`:

```text
v1.17 — <Phase 3c date> — Fourth target registered: EverOn.Equinex (§ 2 registry row — local `~/` transport, Dropbox-synced; adopted <Phase 3b date> via the skill's adopt mode, EverOn own line retired — PLAN-011).
```

§ 2 table — insert this row immediately AFTER the `780-VPN` row (inside the PROJECT-OWNED block):

```text
| | `EverOn.Equinex` — `~/Library/CloudStorage/Dropbox/Projects/EverOn.Equinex` (Dropbox-synced) | Registered <Phase 3c date> (local transport, `~` path — resolves per machine; ONE machine at a time, let Dropbox settle). Adopted Set <vX.Y> <Phase 3b date> via the skill's adopt mode (PLAN-011); EverOn own line retired — pre-adoption archive + numbering crosswalk in `archive/LESSONS_LEGACY.md`. High-stakes live project: engine writes only between its work sessions. |
```

### 5C — `skill/modes/adopt.md` § 3 lessons-archive bullet (rides the Phase 3a release; D-2 = A)

Header `0.2` → `0.3`, `Last Updated` → release date, CHANGE LOG line prepended above `v0.2`:

```text
v0.3 — <release date> — PLAN-011 (S2): § 3 lessons-archive bullet made explicit — archive/LESSONS.md is a SYNC_MAP replace item, so a converging project's own archive is preserved verbatim as archive/LESSONS_LEGACY.md (frozen, carrying the numbering crosswalk) and every entry is classified; nothing dropped silently.
```

FIND (exact, unique — `skill/modes/adopt.md` lines 44–46 at v0.2):

```text
- Any existing lessons archive: entries stay in the project; portable candidates become
  `STANDARDS_LOG.md` `E0NN` entries (`Status: open`) for `harvest` — they are NOT merged into the
  suite's `LESSONS.md` (that file arrives suite-owned from the vault).
```

REPLACE:

```text
- Any existing lessons archive (`archive/LESSONS.md` or wherever the project keeps it): the suite's
  `archive/LESSONS.md` is a SYNC_MAP **replace** item — it arrives suite-owned from the vault and
  every later sync overwrites it — so the project's own archive can never survive in place.
  (1) Classify EVERY entry in this table: already in the vault canonical LESSONS (cite the vault
  L-number) | portable and not yet in the vault | project-specific. (2) Portable entries not yet
  in the vault are intake items (§ 2) — they reach the vault BEFORE adoption, never by being
  merged into the suite's `LESSONS.md` locally. (3) The archive itself is preserved verbatim:
  `git mv` it to `archive/LESSONS_LEGACY.md` (history follows the file), then prepend a freeze
  banner — frozen on the adoption date, read-only, NOT a SYNC_MAP item, new lessons go to
  `docs/STANDARDS_LOG.md` as `E0NN` entries — plus a **numbering crosswalk** (own lesson and rule
  numbers → suite numbers) whenever the project's numbering diverged; own-line numbers cited in
  documents dated before adoption resolve through it. Register it in the project manifest.
  Nothing is dropped silently.
```

### 5D — Release content (Phase 3a)

**5D.0 — Rule 12 step-6 drift fix (known now; verbatim).** In BOTH `docs/standards/CLAUDE.md`
(line 208 at v1.6) and the vault root `CLAUDE.md` (line 203 at v1.8), FIND (exact, unique in each):

```text
6. **`/tmp/` cleanup** — commit-msg files, transcript files, scratch artifacts
```

REPLACE:

```text
6. **`/tmp/` cleanup + locality confirm** — commit-msg files, transcript files, scratch artifacts; project-data locality intact (Rule 14), no new out-of-folder project state
```

Headers: template `1.6` → `1.7`, root `1.8` → `1.9`, each with a CHANGE LOG line naming the
release + "Rule 12 step 6 retitled to match SESSION_CLOSER § 1.6 (L063-class drift since v1.5)"
plus any gate-confirmed CLAUDE.md change (5D.5).

**5D.1–5D.8 — intake integration (content set by the Rule 16 gate — mechanical rules):**

1. **Re-verify the delta** at Equinex's tip at execution time (`git -C <Equinex> log --oneline
   cf25e70..HEAD -- CLAUDE.md archive/LESSONS.md docs/`): anything added since `cf25e70` joins the
   list. Post the COMPLETE list (Rule 16 item 1) — C1–C7 plus any additions.
2. **Per item** post: what it says, source (file + entry/section + date), exactly what
   integrating changes (new vault L-number / which template section), and a recommendation
   (integrate | genericize-then-integrate | reject/keep-local) with reasons. Wait for explicit
   confirmation.
3. **Genericize** confirmed content per the domain-neutral rule (no project / product / host /
   username / tool names; examples rewritten generically) — the v2.3 L070–L078 precedent.
4. **Number** new lessons from the next free canonical L-number at integration time (newest at
   the top of `docs/standards/LESSONS.md`); the vault `archive/LESSONS.md` gains a
   provenance-table entry (vault L#, Equinex own-line #, origin) — the v2.3 dual-voice precedent.
5. **Template text:** C1 lands per D-6 (A = new `### 15.9 Feature intake (before Phase 0)` appended
   to `docs/standards/CLAUDE.md` § 15, with a one-line pointer in § 15.2's Phase 0 row, mirrored in
   the vault root `CLAUDE.md` as its own-instance reconcile). Any other confirmed item that changes
   a template file `F` adds `F` to the § 7.2 ALLOWLIST; the amended ALLOWLIST is re-posted in chat
   BEFORE any edit to `F`.
6. **Counts sweep (L060 / L063):** lessons count in `STANDARDS_INDEX.md` (§ 2 row 9 and the § 6
   entry), `docs/standards/README.md`, and `docs/SET_VERSION_ADOPTED.md` — recompute from source
   (`grep -c '^### L0' docs/standards/LESSONS.md`) and grep every stamp site after editing. Rule
   count stays 15 under D-6 = A.
7. **Release:** `STANDARDS_INDEX.md` § 1 block + § 3 cells + § 6 history entry for the new Set
   Version; SVA backport row; then the engine-as-oracle dry-run (QA-F3) BEFORE the commit.
8. **Kept-local / rejected items** are recorded in the § 7.2 CHANGELOG entry's intake notes
   (Equinex has no STANDARDS_LOG yet — a non-log intake per Rule 16, so no write-back applies).

### 5E — Equinex adoption (Phase 3b; target edits come from the skill, not this plan)

The skill's adopt mode is the procedure; its § 4 approved dry-run list IS the target ALLOWLIST
(§ 7.3). This plan adds these binding requirements to the Equinex session:

1. **Pre-flight:** clean tree (the untracked `docs/Plans/margin-hike-guard-brief.md` is committed or
   moved by the operator first); state = (c) divergent line; intake-first answered "done — S1
   release vX.Y" with the release commit sha; the VAULT working tree is clean at that commit (the
   skill copies live from it — Step 0 reports the sha; it must equal the release sha).
2. **Disposition table** (adopt § 3) covers every customization in a suite-owned region — at minimum
   the Phase 0 complication-(3) list — each → a PROJECT-OWNED block, a § 3.2 row, the binding
   project annex `docs/project_rules.md` referenced from the § 1 / § 13 PROJECT-OWNED blocks (the
   Capital-Signal pattern for domain-binding rules), or dropped with the operator's explicit
   approval (the Capital-Signal 20-section audit precedent). Nothing is reverted silently by the
   template merge.
3. **Numbering crosswalk** (in the `LESSONS_LEGACY.md` freeze banner, per § 5C): own Rule 14 → suite
   Rule 15; own Rule 15 → suite Rule 14; own Rule 16 → suite § 15.9 (D-6 = A); own L001–L049 →
   same numbers; own L050–L060 → vault L057–L067; own L061 → vault L050 note + Rule 14; own L062 →
   the vault L-number assigned in S1. **Live** text carried into the adopted files (PROJECT-OWNED
   blocks, § 3.2 rows, § 4 rules) is re-pointed to suite numbering in the adopt commit; immutable
   history (plans, CHANGELOG, the legacy archive) stays as written and resolves via the crosswalk.
   Memory files (gitignored) are re-pointed by the same session, outside the commit.
4. **Retire** from `docs/standards/` the vault-only files the pilot also removed:
   `HOW_TO_USE.md`, `NEW_PROJECT_BOOTSTRAP.md`, `PROJECT_INSTRUCTIONS_TEMPLATE.md`, `README.md`,
   `SESSION_CLOSER.md`, `SESSION_OPENER.md`, `STANDARDS_INDEX.md` (adopters carry only the six
   topical files there) — and drop their manifest rows.
5. **Archive** per § 5C (D-2 = A): `git mv archive/LESSONS.md archive/LESSONS_LEGACY.md` + freeze
   banner with the crosswalk, then the canonical `archive/LESSONS.md` is created from the vault.
6. **Runtime trees untouched:** the § 4 list may not include any path under `MQL5/`, `backoffice/`,
   `graphify-out/`, or any non-governance file under `scripts/`.
7. **`scripts/claude_project_data.sh`** is replaced by the vault copy verbatim even though both
   carry `VERSION: 0.1` (different lineages — equal stamps must not suppress the replace).
8. **STANDARDS_LOG:** instantiated (example dropped). If the operator routes a real portable
   candidate (C5/C6) to the log during adoption it becomes `E001`; otherwise seed § 5F verbatim.
9. **SVA** written sync-ready per adopt.md § 5 (W-D1 shape) with the vault Set Version + vault sha.
10. **Commit** with the review table → "go on commit?" → single `adopt-standards` commit (a
    separate prep commit only if the dry-run gate approves one). No push.

### 5F — Seeded verification entry (used only if 5E.8 has no real entry)

```text
## E001 — Prove the harvest path end-to-end after adoption
- Date:        <Phase 3b date>
- Area:        governance
- Status:      open
- Context:     Seeded by the adoption session (PLAN-011 QA-F7) so the vault's first harvest of this
               project has a known entry to find, disposition and write back.
- Learned:     A log entry written here reaches the vault only through harvest; the Status write-back
               is the proof the loop is closed.
- Suggested:   Curator: reject with reason "seeded verification entry (PLAN-011 QA-F7)".
- Portability: project-specific
```

Decisions file for the write-back (Phase 3c; `integrate --apply <file> --write`):

```toml
[[rejected]]
project = "EverOn.Equinex"
entry = "E001"
reason = "seeded verification entry (PLAN-011 QA-F7)"
```

(If E001 is a real entry instead, its disposition follows its own Rule 16 gate.)

## 6. Spec update map (per commit)

- **§ 7.1 design commit:** this plan + tracker (new manifest rows 82–83), manifest, CHANGELOG.
- **§ 7.2 release commit:** canonical + vault LESSONS, template + root CLAUDE.md (§ 5D.0 + D-6
  landing), STANDARDS_INDEX (§ 1/§ 2/§ 3/§ 6), standards README count, SVA (backport row + counts
  + own-instance reconcile note), `skill/modes/adopt.md` (§ 5C), any template file added under
  § 5D.5, manifest cells, CHANGELOG release entry, plan status → EXECUTING, tracker.
- **§ 7.4 registration + closure commit:** registry (§ 5A), SESSION_OPENER § 2 (§ 5B), manifest,
  CHANGELOG, plan + tracker → 1.0/CLOSED.
- No engine code changes → `docs/architecture.md` untouched (§ 4 drift rule not triggered).
  No new top-level directory → `docs/folder_structure.md` untouched.

## 7. ALLOWLIST (the bullet enumeration IS the count — L038; plan + tracker included per L054)

### 7.1 Design commit (this draft; 4 files)

- `docs/Plans/PLAN-011_fleet_convergence.md` (new)
- `docs/Plans/PLAN-011_tracker.md` (new)
- `docs/documents_manifest.md`
- `CHANGELOG.md`

### 7.2 Phase 3a release commit (vault; 12 files + any § 5D.5 additions, re-posted before edit)

- `docs/standards/LESSONS.md`
- `archive/LESSONS.md`
- `docs/standards/CLAUDE.md`
- `CLAUDE.md`
- `docs/standards/STANDARDS_INDEX.md`
- `docs/standards/README.md`
- `docs/SET_VERSION_ADOPTED.md`
- `skill/modes/adopt.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-011_fleet_convergence.md` (status → EXECUTING)
- `docs/Plans/PLAN-011_tracker.md`

### 7.3 Phase 3b adopt commit (Equinex repo)

The skill's § 4 operator-approved dry-run list — exactly, per adopt.md § 6 (`git status --short`
must match it; any extra or missing path is a STOP).

### 7.4 Phase 3c registration + closure commit (vault; 6 files)

- `config/projects.toml`
- `docs/SESSION_OPENER.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-011_fleet_convergence.md` (promotion to 1.0/CLOSED)
- `docs/Plans/PLAN-011_tracker.md` (promotion to 1.0/CLOSED)

## 8. Validation gate (Rule 11 scenarios; Rule 15 feature-ON marked ⚑; status in the tracker)

- **QA-F1 — Rule 16 gate record (3a).** The complete re-verified candidate list is posted with a
  per-item explanation + recommendation; the operator's confirmation text is quoted in the
  tracker; kept-local / rejected items appear in the release CHANGELOG intake notes.
- **QA-F2 — domain-neutral gate (3a, pre-commit).** `grep -rniE "everon|equinex|capital-signal|780-automation|780-vpn|parsaazad|a780|mql5|hetzner|metatrader|graphify" docs/standards/ skill/`
  (plus any product/tool names the intake surfaces) prints nothing (exit 1). Baseline 2026-10-03:
  no hits.
- **QA-F3 ⚑ — engine-as-oracle (3a, pre-commit).** Fleet `sync` dry-run against the edited vault:
  every reachable registered target shows EXACTLY the intended delta — `CLAUDE.md` merge (§ 5D.0
  + the D-6 landing) + `archive/LESSONS.md` replace + `docs/SET_VERSION_ADOPTED.md` record, plus
  one item per template file added under § 5D.5 — and nothing else; any wider delta ⇒ investigate
  with `--diff` before writing (the 2026-09-05 discard finding).
- **QA-F4 ⚑ — release delivered (3a, post-commit).** `sync --write`; each written target holds
  `docs/SYNC_HANDOFF.md` naming the release; immediate dry-run re-run = up-to-date 11/11;
  fleet `status` = current on every reachable target.
- **QA-F5 ⚑ — adoption (3b).** Intake-first confirmed by sha; clean tree; § 4 list approved;
  applied `git status --short` == approved list; marker integrity (every BEGIN has END; counts =
  template: CLAUDE 4 / OPENER 3 / CLOSER 2 PROJECT-OWNED); `archive/LESSONS_LEGACY.md` below its
  banner byte-identical to `git show HEAD~1:archive/LESSONS.md`; crosswalk present; every
  disposition-table row resolved; zero paths under the § 5E.6 runtime trees; governance exit 0
  (stdout pasted); SVA sync-ready; the engine's own `merge_file` runs clean on the adopted
  CLAUDE.md / OPENER / CLOSER (the pilot's engine-verified idempotence check).
- **QA-F6 ⚑ — registration (3c, pre-commit).** With § 5A applied: `status` = Equinex ADOPTED vX.Y
  / VAULT vX.Y / current; `sync --project EverOn.Equinex` dry-run = up-to-date 11/11 (a freshly
  adopted target is a no-op — the pilot's QA-F proof). If the vault Set Version moved between 3b
  and 3c (e.g. a D-5 release), the dry-run must instead show exactly that release's delta; run
  `sync --project EverOn.Equinex --write` (R8 clock check first), then re-run = up-to-date 11/11.
- **QA-F7 ⚑ — log-recording discipline round-trip (3c; requirements 2 + 3).** `harvest` surfaces
  Equinex `E001`; `integrate --apply <decisions> --write` writes the Status back (`rejected — …`
  for the seed, or the gated disposition for a real entry) and leaves the write-back handoff
  (PLAN-012 § 5d behavior); read back the Status line verbatim; `harvest` = no open Equinex
  entries. The Equinex session then lands the write-back per its handoff (the PLAN-012 QA-H5
  pattern) — observed after closure, not ship-gating.
- **QA-F8 — line retirement (3c).** In Equinex: none of the seven § 5E.4 files remain;
  `docs/SET_VERSION_ADOPTED.md` records the vault Set Version + vault sha; the legacy archive's
  freeze banner + crosswalk present; CLAUDE.md § 3 = the template's 15 rules in template order
  (project-only binding rules live in PROJECT-OWNED blocks or the `docs/project_rules.md` annex —
  the pilot pattern).

**Rule 15:** QA-F3/F4/F5/F6/F7 are ship-gating; none may be deferred without an explicit operator
waiver recorded in the tracker's waiver register.

## 9. Operator decision points (Phase 2 — answer with the approval)

- **D11.A — approve the plan** ("APPROVE PLAN-011"). Required before any Phase 3 work.
- **D-1 — scope boundary.** RECOMMEND as § 3: Equinex convergence + program closure only; DD-6b,
  the delivery kit, E001's engine half and Equinex's local candidate queue routed elsewhere.
- **D-2 — home for Equinex's pre-adoption lesson archive.** (A) **frozen legacy file**
  `archive/LESSONS_LEGACY.md` via `git mv` + freeze banner + numbering crosswalk (RECOMMEND — with
  221 plan citations to own-line numbers, the crosswalk keeps Equinex's history readable; zero
  knowledge loss; no new ongoing convention: new lessons still go only to STANDARDS_LOG);
  (B) git history only, crosswalk in the CHANGELOG (smallest footprint; history citations then
  resolve only via `git show`); (C) re-key project lessons as STANDARDS_LOG entries for the
  curator to reject (heavy; floods the first harvest; Phase 0 found no project-only lesson
  content that is not already in the vault or C1, so it buys nothing here).
- **D-3 — fleet completeness.** Is the fleet exactly the four known projects? If others exist
  (e.g. the "team old-SETUP adopters" mentioned 2026-08-16), name them — each needs register +
  one-time heading wrap + `sync` catch-up (no skill run), added by amendment.
- **D-4 — Equinex adoption window.** The adopt session needs a clean tree and a pause in Equinex
  feature work for one session. RECOMMEND: the operator picks the window; the untracked brief is
  committed or moved first.
- **D-5 — release ordering with E001.** If E001's Rule 16 gate is confirmed, RECOMMEND it ships
  first as its own small release (it is ready now); S1 then takes the next Set Version and the
  next free L-numbers.
- **D-6 — where the feature-intake workflow (C1) lands** (only-append rule numbering binds):
  (A) **template `§ 15.9 Feature intake (before Phase 0)`** — a binding stage of the already-binding
  § 15 plan workflow, plus the canonical lesson; template rule count stays 15, no renumbering
  anywhere (RECOMMEND — it IS a pre-plan workflow stage, so § 15 is its natural home);
  (B) **template Rule 16** — collides with the vault root's own Rule 16 (harvest gate); the vault
  would have to renumber it, which the only-append rule forbids; (C) **template Rule 17**, leaving
  16 unused in the template — avoids renumbering but leaves adopters a numbering hole, and the
  next template rule collides again with any project-specific Rule 16.

## 10. Rollback path

- **§ 7.2 release:** before push — single `git revert`; then a `sync --write` re-delivers the prior
  suite (the targets' working-tree writes are overwritten back; handoffs explain both). After push —
  fix-forward per Rule 3.
- **§ 7.3 adopt commit (Equinex, unpushed):** single revert in Equinex restores the own-line suite;
  `LESSONS_LEGACY.md` returns to `archive/LESSONS.md` by the same revert. Memory re-points (5E.3)
  are reverted by hand from the session record.
- **§ 7.4 registration:** single revert; an unregistered Equinex is simply outside the fleet again.

## 11. Known risks + mitigation

| # | Risk | Mitigation |
|---|---|---|
| R1 | Equinex's own-line lessons destroyed by the `archive/LESSONS.md` replace (the 780-Automation class, L069) | Intake-first (S1) + D-2 preservation + QA-F5 byte-identity check of the legacy file |
| R2 | Live-trading runtime disturbed by the adoption | Docs-only § 4 list; § 5E.6 forbids runtime trees; QA-F5 asserts zero such paths; no push by the skill |
| R3 | Equinex keeps evolving its own line between this audit and Phase 3 | § 5D.1 re-verifies from `cf25e70` to the tip; operator asked to make no own-line suite edits from approval to adoption |
| R4 | The S1 release sync deepens Capital-Signal's uncommitted backlog (v2.1 → v2.5 already, the discard class) | Handoff rides the write; RECOMMEND a CS landing session before Phase 3a; the QA-F3 oracle shows CS's exact delta first |
| R5 | Rule / lesson numbering collisions corrupt meaning in live text (Equinex R14↔R15 swap, R16, own L050–L062 ≠ vault L050–L062) | § 5E.3 crosswalk + live-text re-point in the adopt commit; history resolves via the crosswalk; D-6 = A avoids any new collision |
| R6 | Version-label confusion — Equinex's own line calls itself "Set v2.7" while the vault releases v2.6 / v2.7 | Own-line STANDARDS_INDEX retires at adoption; SVA records the vault sha; the adopt CHANGELOG entry states the mapping explicitly |
| R7 | Count / stamp drift on the release (L060 / L063) | § 5D.6 recompute-from-source + grep every stamp site; Rule 10 review re-greps |
| R8 | Wrong stamps from a drifting clock (780-VPN E001 — the engine still trusts the wall clock) | Before every engine write in this plan: `curl -sI https://gitlab.com \| grep -i date:` agrees with `date -u` (recorded in the tracker) |
| R9 | Dropbox concurrency on Equinex | Engine writes only between Equinex sessions; one machine at a time; § 5A registry NOTE |
| R10 | Customizations in suite-owned regions silently reverted on the first merge | § 5E.2 disposition table + dry-run gate; QA-F5 engine `merge_file` idempotence check before commit |
| R11 | Equal VERSION stamps hide a divergent script (`claude_project_data.sh`) | § 5E.7 replaces by content, not stamp |

## 12. Acceptance criteria

1. Rule 16 gate recorded (QA-F1); confirmed items integrated genericized (QA-F2 zero-hit) in one Set
   release, together with the § 5C adopt.md fix and the § 5D.0 Rule 12 drift fix.
2. Release delivered to every reachable registered target with handoffs; idempotent re-run
   up-to-date 11/11 (QA-F3/F4).
3. Equinex adopted in one approved, docs-only commit; pre-adoption archive preserved per D-2
   (byte-identical) with the crosswalk; markers intact; governance exit 0 (QA-F5).
4. Equinex registered; `status` current, `sync` no-op (QA-F6).
5. Log round-trip proven: harvest finds Equinex `E001`, write-back lands, harvest clean (QA-F7).
6. EverOn own line retired in Equinex (QA-F8) — requirements 1–3 satisfied.
7. Manifest, CHANGELOG, SESSION_OPENER § 2 and registry consistent at every commit; governance
   exit 0 at every commit; plan + tracker → 1.0/CLOSED in the § 7.4 commit.

---

**Rule 13 senior-review-and-optimize pass — RUN 2026-10-03 (recorded per § 15.8):** the canonical
prompt was run against the complete plan + tracker, with mechanical verification rather than a
re-read (L051 / memory: run the tools at ship form):

- **Extracted from this file and executed:** the § 5A TOML appended to a scratch copy of the live
  registry → `load_registry` + `make_target` load it as `LocalTarget` at the expanded Equinex path
  and `session()` materializes the live repo; the § 5F decisions TOML → `integrate.parse_decisions`
  returns the expected `rejected — seeded verification entry (PLAN-011 QA-F7)` disposition; a
  scratch STANDARDS_LOG holding the § 5F seeded entry → `integrate.apply_writeback` (dry-run) finds
  `E001` and plans the Status flip. No Python is embedded, so ruff / mypy / pytest have no target.
- **Anchors byte-verified against live source:** § 5C FIND = exactly 1 match in
  `skill/modes/adopt.md`, starting line 44 (3 lines); § 5D.0 FIND = exactly 1 match in each of
  `docs/standards/CLAUDE.md` (line 208) and `CLAUDE.md` (line 203); § 5B's 1.16 header and the
  `780-VPN` § 2 row exist; manifest's last row is 81 → plan rows 82–83.
- **Gates pre-run:** QA-F2's grep over `docs/standards/` + `skill/` = zero hits today (a gate that
  already failed would be a plan defect); § 5D.1's delta command from `cf25e70` = empty today;
  template PROJECT-OWNED counts 4 / 3 / 2 (QA-F5's expected values) confirmed by `grep -c`;
  count-sweep sites located (INDEX § 2 row 9 + § 6 entries, README line 149, SVA counts).
- **Audit provenance (L059):** the subagent's Equinex line references spot-checked live (R16 :294,
  L062 :158, MACHINE_MIGRATION :101 / :139 / :157, R8 :149, OPENER :56) and its live-reference
  counts recomputed (Rule 14 / 15 / 16 → 18 / 14 / 9 files).
- **Cross-section consistency:** § 3 scope ↔ § 5 rules ↔ § 6 map ↔ § 7 ALLOWLISTs (4 / 12 / approved
  list / 6 — bullets counted) ↔ § 8 QA-F1…F8 ↔ tracker ledger (8 rows) ↔ § 12 criteria ↔ § 9
  decisions D-1…D-6 (tracker Phase 2 line corrected from D-5 to D-6).
- **Findings fixed in place (6):** (1) project-specific binding rules: the pilot used the binding
  annex `docs/project_rules.md`, not PROJECT-OWNED blocks alone — § 5E.2 destinations and QA-F8
  corrected; (2) § 5E.1 gains the vault-clean-at-release-sha gate (the skill copies live from the
  vault tree); (3) QA-F6 gains the intervening-release rule (a D-5 release between 3b and 3c makes
  Equinex "behind", not "current"); (4) QA-F7 notes the write-back handoff landing (QA-H5
  pattern, non-gating); (5) tracker decision range; (6) this record.
- **New design decisions surfaced, not decided silently:** D-2 (archive home — the adopt-mode spec
  gap) and D-6 (feature-intake landing under the only-append numbering rule) are both genuinely
  new and left to the operator with a recommendation.
