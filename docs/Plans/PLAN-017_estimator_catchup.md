<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-10-08 -->
<!-- Status: CLOSED — 2026-10-08: QA-M8 ✅ on the owner's Windows PC with tool 0.3 (all § 8.2 sub-checks, (b) captured live); 780-estimator lifecycle active -->
<!--
CHANGE LOG
v1.0 — 2026-10-08 — CLOSED (§ 7.6 closure commit). QA-M8 ✅ on the owner's Windows PC with tool 0.3, run
from a self-checking step guide relayed as a .txt (each block printed its own verdict and appended to one
results file): pull `1ddbbf9..515ea96`; sub-check (b) captured LIVE before the link (`ABORT … looks
active`, D-9 = A — no waiver); transcripts repaired (d65a220e 188 lines, 335dbc56 identical); `link` with
0.3 → backup in `~/.claude/locality-backups/`, `STATUS: OK (14)`, `<JUNCTION>`; a fresh session named a
known memory before reading any file; `cleanup` → KEPT, exactly the two repaired transcripts listed (the
expectation was written down before the output), only the junction left for the key. The owner confirmed
the 2026-10-06 Explorer move ("YES, I DID"). Acceptance § 12 items 1–10 checked one by one (tracker).
Registry `lifecycle` → `active`. Clock checked against gitlab.com.
v0.6 — 2026-10-07 — Phase 3b executed in a fresh session. Reconcile pass: the 11 Phase 3b blocks + the § 5w
message re-extracted from this file by a parser written fresh in that session — vault 4 / 4 and estimator
7 / 7 matched (pre-blobs, single FINDs); zero block defects; checker positive control 1 FAIL as expected.
§ 5q–5s applied to the vault and § 5t–5v to a fresh estimator clone with `<P3B-DATE>` = 2026-10-07
(clock checked against gitlab.com); their `main` was still `1ddbbf9` (§ 6i not triggered). Delivery
commit `515ea96` pushed fast-forward. QA-M11…M16 ✅ (evidence in the tracker). Process note: the fresh
clone had no git identity on this machine — set repo-locally to the vault's before the commit (Rule 14
fresh-clone clause). Status stays EXECUTING — QA-M8 (owner's PC, with 0.3) gates the closure.
v0.5 — 2026-10-07 — Phase 3b approval recorded (operator: "commit; Phase 3b approved, all A"); § 9.3
decision record added: D17.B approved; D-6…D-9 = A. No § 5 change — the 11 Phase 3b blocks re-extracted
from this file stay byte-identical to the proven files.
v0.4 — 2026-10-07 — Phase 3b revision (operator "A": fix inside this plan before it closes). Incident
record (§ 2): after a correct `adopt` the owner's store was emptied by a manual Explorer move of the
junction (recovered from the Recycle Bin); tool 0.2 had no path that empties the store, but F1 (`status`
recommended `link` for an EMPTY store) and F2 (the backup sat beside the junction; "delete it once…") are
fixed here: tool 0.3 + tests 0.2 (§ 5q–5s), delivered to the estimator in one curator commit (§ 5t–5w);
QA-M11…M16 + the QA-M8 re-run (§ 8.2); D-6…D-9 (§ 9.2); § 6h / 6i; § 7.7–7.10; R12–R15; acceptance 8–10.
Code proven FIRST in a scratch overlay (ruff clean, mypy --strict 0 in 25 files, pytest 163 = 151 + 12;
positive control vs tool 0.2 → 13 failed / 10 passed; replay of the owner's state in both orders). Rule
13 pass on the revised plan + tracker (record at the foot): the 11 blocks re-extracted and applied to
fresh trees of both repos, all green; 3 gaps fixed, 3 options declined. Status stays EXECUTING (revision
DRAFT).
v0.3 — 2026-10-05 — Phase 3 executed in a fresh session. Reconcile pass: all 33 blocks re-extracted from
this file, every FIND / pre-image / absence check passed on the live trees — zero block defects. § 5
applied byte-for-byte with `<P3-DATE>` = 2026-10-05 (clock checked against gitlab.com / apple.com).
Estimator: prep `b4cae64` + the engine's sync `fdb87b9` on their `main` (the fleet's first live git
write); vault: tool 0.2 + tests, registry entry, opener row, skill, folder tree; Capital-Signal E002
written back. QA-M1…M7 + M10 ✅ (evidence in the tracker). Plan defect D1 (wording; operator D1 = A):
§ 8.1 listed the merge / record files only — the dry-run also removes 3 non-header lines from the
replace-mode MEMORY_PROTOCOL, explained before the write (the target's replace-mode copies are
byte-identical to `set-v1.3`; the lines are the v2.2 identifier scrub) — § 8.1 gains one sentence.
Process note: QA-M7's idle re-check printed instead of gating (tracker). Status APPROVED → EXECUTING.
v0.2 — 2026-10-05 — Phase 2 operator approval recorded ("Plan-017 is approved"); § 9.1 decision record
added: D17.A approved; D-1…D-5 = A (the recommended options the § 5 code and the § 5n entry implement).
No § 5 change — the 33 blocks re-extracted from this file stay byte-identical to the proven blocks.
Status DRAFT → APPROVED.
v0.1 — 2026-10-05 — Initial draft. § 15.9 intake (operator request, no document) → Rule 16 gate
(12 candidates; operator: "yes to all recommended") → Phase 0 audit (read-only: a scratch clone of
780-estimator `45d7c75`) → Phase 1 design. Code proven FIRST in scratch overlays: the locality tool
v0.2 + 11 tests (ruff clean, mypy --strict 0 in 25 files, pytest 151 = 140 + 11; positive control —
the same tests against v0.1 fail exactly the 6 new-behavior cases); the whole catch-up run end-to-end
over the git transport against a local bare remote standing in for GitHub (status behind → dry-run
7/11 → write 8 files in one engine commit → re-run up-to-date 11/11 → status current). § 5 is
GENERATED from the proven blocks (no hand-copying). Rule 13 pass run the same day on the complete
plan + tracker (record at the foot): blocks RE-EXTRACTED from this file onto fresh copies of both
repos — QA-M1 / M2 / M10 green, the catch-up reproduced over the git transport with § 8.1's counts
exact; 1 defect (domain-neutrality of the delivered tool) + 1 ordering defect (§ 5d/5e before the
prep push) + 3 cross-section gaps fixed; 2 optimizations applied, 2 declined.
-->

# PLAN-017 — 780-estimator catch-up (Set v1.3 → v2.7, the first git target) + a Windows-capable locality tool

## 1. Goal

Bring **780-estimator** — a team project (owner Bahereh Hassanpour, GitHub `780-AI/780-estimator`)
that bootstrapped the suite at **Set v1.3** on 2026-06-21 and has run under the contract since — onto
the vault's current Set and under `sync` for good, **without breaking its owner's Claude memory on
Windows**:

1. **Make the project-data locality tool Windows-capable** (`scripts/claude_project_data.sh` 0.1 →
   0.2): the synced Rule 14 makes every estimator session call it, and v0.1 only works on macOS /
   Linux. Absorbs the two Rule 16 intake items confirmed for this plan (§ 2): the estimator's own
   Windows junction logic and Capital-Signal's E002.
2. **One-time prep commit in the estimator** (the old-SETUP catch-up path, SKILL.md): v1.6 heading
   wrap of the session opener + closer, `docs/SET_VERSION_ADOPTED.md` in the engine's sync-ready shape,
   the locality tool copied in, and the two pieces of local text the sync would otherwise drop moved
   into PROJECT-OWNED blocks (or accepted at the gate).
3. **Register and catch up**: a `git`-transport registry entry (the fleet's first) with the full fleet
   keys, then `sync --write` — the engine's first live git write, Delivery A (direct to `main`).
4. **Verify on the owner's Windows PC** (Rule 15): the `adopt` migration and the handoff landing.
5. **Phase 3b — fix-forward (added 2026-10-07, operator "A"):** locality tool 0.3 — `status` never
   recommends `link` for an empty store (F1); Windows backups leave the link's folder, `adopt` / `link`
   warn never to handle the link in a file manager, and a `cleanup` verb removes a backup only when the
   store fully covers it (F2) — delivered to the estimator in one curator commit; QA-M8 re-runs with 0.3.

After this plan the fleet has five targets on all three transports, and the old-SETUP catch-up path
is documented completely in the skill.

## 2. Operator constraints + intake record (binding)

- **Operator inputs (2026-10-05):** name `780-estimator`; repo `https://github.com/780-AI/780-estimator`;
  owner Bahereh Hassanpour; **Delivery A** (direct + handoff); Bahereh works on a **Windows PC**
  (confirmed); **transport = git** (operator chose it over ssh after the comparison: a Windows PC has no
  rsync and is often unreachable; git commits cannot be silently discarded); **Option A** — the locality
  tool is fixed inside this plan; the operator **will tell Bahereh** before the first push.
- **§ 15.9 intake:** no feature document (operator request only) — step 1's copy is skipped, never the
  discipline; the investigation (step 2) is the § 3 Phase 0 audit; the design's core hypothesis was
  pre-tested end-to-end before approval (§ 3, "numbers").
- **Rule 16 gate — record (2026-10-05).** Complete list presented in chat (all 60 commits, governance
  files, CHANGELOG, 44 plan files, scripts scanned; Bahereh's machine-local Claude memory not reachable
  and not scanned). Operator: **"yes to all recommended"**. Dispositions:

  | # | Candidate (source) | Disposition |
  |---|---|---|
  | 1 | Windows junction support (estimator `scripts/bootstrap_memory.sh`, bootstrap `66ac85c`) | **integrate (genericized)** — § 5a |
  | 2 | CS E002 — locality tool aborts after a folder move (Capital-Signal `STANDARDS_LOG.md` E002) | **integrate** — § 5a; Status write-back § 5p; delivery to existing adopters → v2.8 (D-2) |
  | 3 | "Ask in plain chat, never via popup" (estimator `CLAUDE.md` § 10 + opener § 3.2 row 1, `8b7f1fe`) | **kept project-local** — the § 3.2 row survives the sync; the § 10 line is dropped by it (accepted) |
  | 4 | Verify an environmental premise before designing (estimator PLAN-013 § 14.4) | **v2.8** — a data-point paragraph in L080 |
  | 5 | A TLS handshake is not reachability (estimator CHANGELOG, PLAN-014) | **v2.8** — genericized new lesson |
  | 6 | ALLOWLIST-count governance check (estimator CHANGELOG, PLAN-011) | covered by L038; automation idea → the queued mechanize-checks candidate |
  | 7 | Header vs own change log (estimator CHANGELOG, PLAN-012) | covered by L063 |
  | 8 | Rule 13 tested one input size (estimator PLAN-004 v0.3) | **v2.8** — data point for the queued Rule 13 checklist candidate |
  | 9 | Re-base version bumps before Phase 3 (estimator PLAN-002b § 4) | covered by L056 |
  | 10 | Stale push markers (estimator PLAN-006c) | covered by L055 |
  | 11 | `PLAN-NNN_rules_n_assumptions.md` companion files (estimator `docs/Plans/`) | **kept project-local** |
  | 12 | The estimator's two governance scripts | nothing to take (a project scaffold) |

  None of the 12 is an `E0NN` log entry except #2, so nothing else is marked `rejected` anywhere;
  the v2.8 items are queued in `docs/Plans/OPEN_TASKS.md`.
- **The owner's repo is theirs.** Only governance files + the one new script are touched; no runtime,
  domain, test or data path under `src/`, `tests/`, `scripts/run_daily.sh`, `requirements*`, `.env*`.
- **Never assume paths / hosts** — every value in § 5d came from the operator or the live repo.
- **Rule 4 in both repos** — every curator-made commit uses `git commit -F <file>`.
- **Plan-first, two-session split** (§ 15.3) — Phase 3 runs in a fresh session from this file.
- **Clock trust (L079)** — the Phase 3 date is checked against an external time authority; the
  engine refuses to stamp behind the target's newest stamp.
- **Incident + operator decision (2026-10-06 / 07) — Phase 3b.** After a correct `adopt` (09:35,
  `STATUS: OK (14 memory files)`), the owner's store was emptied at 09:45 by a manual Explorer move: both
  entries for this key in `C:\Users\<owner>\.claude\projects` — the junction and the tool's
  `.pre-locality-…` backup beside it — were cut into a new Desktop folder; moving the junction moved the
  real files behind it (E: → C:); the leftover junction was recycled at 09:45:55 and the Desktop folder at
  09:52:53. Evidence (the owner's Claude, read-only): Recycle Bin items with deletion times, folder
  timestamps, no shell-history hits, session `d65a220e` resumed at 09:46:56 into a fresh plain harness
  dir. Her opener § 1.5 halt-on-empty caught it at her next session open (Rule 14 worked). Recovered from
  the Recycle Bin: 14 memories byte-identical into `.claude/project-data/`; the resumed session's two
  transcript halves re-assembled and a title stub replaced before `link`. Vault review: tool 0.2 has no
  code path that empties the store, but two weaknesses — **F1** `status` said "in-repo data exists" for
  an EMPTY store and recommended `link` (that would have joined Claude Code to the empty store and hidden
  the loss); **F2** the backup sat beside the junction with the same name prefix and `adopt` / `link`
  said "delete it once…" with no safe way — it sent the owner into the one folder where a file-manager
  action destroys data (§ 11 had no row for it). Operator: **"A"** — fix inside this plan before closing
  (tool 0.3 + delivery + QA-M8 re-run), not deferred to v2.8. The owner confirmed the Explorer action on
  2026-10-08 ("YES, I DID"); it does not change the design.

## 3. Scope summary

**In scope**

- **S1 — locality tool 0.2 (vault):** Windows (Git Bash) branch — drive-form path-key, directory
  junction via `mklink /J`, junctions removed only with `rmdir` (never `rm` — `rm -r` on a junction can
  follow into the target), rename-to-backup + no-overwrite copy in place of `mv` (Windows cannot move a
  directory a live session holds; the harness dir and the repo often sit on different drives),
  refusal while a transcript changed in the last 2 minutes; E002 — the merge recurses into same-name
  dirs and drops the empty ones Claude Code creates, `status` names `link` when in-repo data exists,
  `link` absorbs the pre-v1.5 layout too. POSIX behavior otherwise unchanged (the four Mac/Linux
  targets and the vault itself). New test module (11 cases incl. a Windows branch through stand-in
  `uname` / `cygpath` / `cmd`).
- **S2 — skill fix (vault):** SKILL.md's old-SETUP paragraph names the whole prep (it named only the
  heading wrap; this audit hit the other two gaps).
- **S3 — estimator prep commit** (§ 5h–5n; message § 5o), pushed to their `main`.
- **S4 — registration + catch-up:** registry entry (§ 5d) + SESSION_OPENER § 2 row (§ 5e); `sync
  --project 780-estimator --write` over git (one engine commit, author "Standard DocSet").
- **S5 — CS E002 write-back** (§ 5p) via `integrate --apply`.
- **S6 — Windows verification** (QA-M8) + landing observation (QA-M9), then closure.
- **S7 — locality tool 0.3 + tests 0.2 (vault, Phase 3b):** F1 + F2 (§ 1 item 5; § 5q–5s); the vault
  tree line names `cleanup`.
- **S8 — delivery to the estimator (Phase 3b):** one curator commit on their `main` — the tool copy, its
  manifest row and a CHANGELOG entry with the owner's next steps (§ 5t–5w).

**Out of scope (routed)**

- Delivering tool 0.2 to the four existing adopters (none is on Windows; E002's delivery half) →
  v2.8, where the script-delivery path is designed (D-2). Sync cannot carry it today: `scripts/` is not
  a SYNC_MAP item and the ssh transport materializes only `docs/` + `archive/` + `CLAUDE.md`.
- Handoff wording for committed (git) writes → PLAN-014 (PLAN-013 R6); explained to the owner in the
  prep CHANGELOG entry meanwhile (D-4).
- Rule 16 items 4, 5, 8 → the v2.8 release.
- The estimator's CI: its repo is on GitHub but carries only `.gitlab-ci.yml`, so its Rule 2 CI half
  never runs — reported to the owner (§ 5n entry is silent on it; the operator relays), not fixed here.
- PR delivery / DD-6b (PLAN-014) — Delivery A makes it unnecessary for this repo.
- Template wording: Rule 14 (`docs/standards/CLAUDE.md:250-254`) and the opener / closer say
  "symlink"; on Windows it is a junction — a `docs/standards/` edit (Set bump), queued for v2.8.
- Listing `cleanup` beside `status` / `adopt` / `link` in template Rule 14 (`docs/standards/CLAUDE.md`)
  and the vault's own CLAUDE.md → v2.8 with the junction wording above (a Set bump); the tool's usage
  header documents the verb meanwhile.
- Tool 0.3 for the four existing adopters → v2.8's script-delivery fix (D-2 stands; none is on Windows).

### Phase 0 audit findings (2026-10-05, read-only; estimator `main` = `45d7c75`, vault `8b914db`)

- **The repo:** 60 commits, one author (bahereh), first `66ac85c` 2026-06-21 "Bootstrap: install
  Standard Set v1.3"; after bootstrap the governance layer changed only in `8b7f1fe` (ask inline) and
  in its § 4 Critical Files (PROJECT-OWNED). `archive/LESSONS.md` = exactly L001–L051 (the v1.3
  canon); `docs/STANDARDS_LOG.md` has no entries; `.claude/` is gitignored (`.gitignore:70-72`).
  Platform: `scripts/bootstrap_memory.sh` carries a MINGW/MSYS branch (`cygpath -m`, lowercased drive,
  `cmd //c mklink //J`, example path `E:/Bahereh_780/...`).
- **Why the engine refuses it today:** `setversion.py:33` reads `**Standard Set Version:**` (the
  estimator writes `**Set Version:**` → adopted `?`); `sync.py:212-233` `record_adoption` needs that
  bullet + `**Adopted on:**` + the backport table, and `sync.py:145` the CHANGE LOG header; `sync.py`
  `plan_target` stops at the first PROJECT-OWNED count mismatch — opener 2 vs 3, closer 1 vs 2
  (CLAUDE.md 4 = 4). Measured: `sync` dry-run → `SESSION_OPENER.md: PROJECT-OWNED block count mismatch
  (template 3 vs target 2)`.
- **After the prep (scratch proof):** `status` v1.3 / v2.7 behind; dry-run **7 of 11** need sync
  (CLAUDE.md, PROJECT_STANDARDS, MEMORY_PROTOCOL, LESSONS, opener, closer, SVA; PROMPT / ENGINEERING /
  VALIDATION / CICD byte-identical). Removed-lines review in § 8.1.
- **Git transport** (`transport.py:112-146`): a writable `--depth 1` clone of the branch; `flush` =
  `git add` + `commit -m` as `Standard DocSet <standard-docset@localhost>` (`transport.py:41-42`) +
  `push origin HEAD:main` — no force, so a concurrent push makes the write fail, never overwrite. The
  handoff rides the same commit (`cli.py:249-266`). Proven locally against a bare remote: one engine
  commit, 8 files, parent = the prep commit; re-run up-to-date 11/11; `status` current.
- **Access:** the operator's GitHub key reads the repo (`ls-remote`) and a no-op `push --dry-run` was
  accepted (GitHub refuses the receive-pack connection to keys without write access); the first real
  push is the proof.
- **Locality tool 0.1** (`scripts/claude_project_data.sh`): key from the POSIX path (`:31`), `ln -s`
  (`:103`, `:124`), the merge skips same-name entries (`:62-72`) so a harness-created `memory/` makes
  `link` / `adopt` abort (`:95-98`, `:117-120`) — E002; no Windows branch. The synced suite calls it
  from template Rule 14 (`docs/standards/CLAUDE.md:251-256`), opener § 1.5
  (`docs/standards/SESSION_OPENER.md:82`) and closer § 1.6 (`docs/standards/SESSION_CLOSER.md:99`).
- **Skill:** `skill/SKILL.md:58-61` lists only the heading wrap for an old-SETUP catch-up.
- **E002 write-back format** (`integrate.py:157-165`): dry-run against the real Capital-Signal log
  parses and resolves the entry (§ 5p).
- **Tool baseline:** ruff clean; `MYPYPATH=src mypy --cache-dir <fresh>` → 0 issues in 24 files
  (without `MYPYPATH` the editable install yields 49 `import-untyped` errors — an environment effect,
  not code); pytest 140.

## 4. Phase tracker (high-level — granular sub-tasks in `PLAN-017_tracker.md`)

| Phase | What | Status |
|---|---|---|
| 0 | Audit (read-only) | ✅ 2026-10-05 |
| 1 | Design + proven code + Rule 13 pass | ✅ 2026-10-05 |
| 2 | Operator approval | ✅ 2026-10-05 |
| 3 | Implement — fresh session: 3.0 pre-checks → 3.1 reconcile → 3.2 vault tool + skill blocks → 3.3 estimator prep commit + push → 3.4 registry + catch-up write → 3.5 CS E002 write-back → 3.6 vault commit | ✅ 2026-10-05 |
| 4 | Validate — QA-M1…M7 inside Phase 3; QA-M8 / M9 on the owner's PC | ✅ M1…M7 + M10 2026-10-05; M9 2026-10-06; M8 (re-run with 0.3) 2026-10-08 |
| 1b | Phase 3b design — incident record, tool 0.3 proven, Rule 13 pass | ✅ 2026-10-07 |
| 2b | Operator approval of the revision | ✅ 2026-10-07 |
| 3b | Implement — fresh session: 3b.0 pre-checks → 3b.1 reconcile → 3b.2 vault § 5q–5s + QA-M11…M15 → 3b.3 estimator delivery commit + push (QA-M16) → 3b.4 vault bookkeeping + commit | ✅ 2026-10-07 (estimator `515ea96`) |
| 4b | Validate — QA-M11…M16 inside Phase 3b; QA-M8 re-run on the owner's PC with 0.3 | ✅ M11…M16 2026-10-07; M8 2026-10-08 |
| 5 | Operator gate — vault push ✅ 2026-10-06 (`fb8960c`, both remotes); Phase 3b vault push ✅ 2026-10-07 (`9b1c49e`, both remotes); closure commit after QA-M8 ✅ 2026-10-08 | ✅ |

## 5. Verbatim transformation rules (code proven in scratch; Phase 3 copies byte-for-byte)

**How to apply (Phase 3).** Each block carries a machine-readable marker (`<!-- block … -->`). The
reconcile pass (§ 15.3) re-extracts every block from THIS file before the first edit and checks it
against the live trees — vault: the working tree; estimator: a fresh writable clone of `main` in the
session scratchpad (never inside the vault folder; deleted after the push): every FIND matches exactly
once, every whole-file pre-image hashes as stated, every NEW file is absent. Any mismatch is a named
plan defect (D1, D2, …) — stop and surface it. Replace every `<P3-DATE>` with the Phase 3 date checked
against an external time authority (L079). **Order:** step 3.2 applies § 5a, 5b, 5c, 5f, 5g to the vault;
step 3.3 applies § 5h–5n to the estimator clone (§ 5k copies the vault file that § 5a produced); step
3.4 applies § 5d + 5e (registry entry + opener row) only AFTER the prep commit is on their `main` — a
`status` / `fleet` / governance run before that would probe a repo the engine cannot read yet. If the
estimator's `main` moved past `45d7c75`, the reconcile pass decides: blocks that still match apply; any
that does not is a plan defect.

<!-- §5-GENERATED:BEGIN -->

### 5a — `scripts/claude_project_data.sh` (vault) — 0.1 → 0.2: Windows junction support + the E002 fix — WHOLE-FILE REPLACE
<!-- block id=5a repo=vault path=scripts/claude_project_data.sh kind=whole pre_blob=c746047406e427dce4319bed5ec05bd447fbf6c6 -->
**5a** — the live file must hash to `c746047406e427dce4319bed5ec05bd447fbf6c6` (`git hash-object`); replace its whole content with:

```text
#!/usr/bin/env bash
# ==============================================================
# VERSION: 0.2
# Claude project-data locality tool (CLAUDE.md Rule 14) — keeps the Claude Code
# per-project data (memory + session transcripts) physically INSIDE the project
# folder at <repo>/.claude/project-data/, with a link left at the harness path
# ~/.claude/projects/<path-key>/ so Claude Code keeps working unchanged — a
# symlink on macOS / Linux, a directory junction on Windows (Git Bash).
#
# Usage:
#   bash scripts/claude_project_data.sh status   # report physical home + link health
#   bash scripts/claude_project_data.sh adopt    # one-time on a machine that already has
#                                                # data under ~/.claude: move it in + link
#   bash scripts/claude_project_data.sh link     # new machine, or after a folder move/rename:
#                                                # (re)point the harness path at the in-repo data,
#                                                # merging any stray harness-created dir first
#
# The <path-key> is the repo's absolute path with every non-alphanumeric
# character replaced by "-" (Claude Code's own convention), so it changes
# whenever the folder moves — run `link` after any move/rename. On Windows the
# key is built from the drive form of the path (e:/dir/repo, drive lowercased).
#
# Windows (Git Bash): run `adopt` / `link` from a Git Bash window with Claude Code
# CLOSED for this project (a live session holds files in the harness dir; the tool
# refuses while a transcript changed in the last 2 minutes). There the harness dir is
# renamed to a backup (<key>.pre-locality-<stamp>), its files are copied into the
# in-repo home without overwriting, and a junction is created; the backup stays until
# you delete it. Junctions are removed with rmdir, never rm.
#
# CHANGE LOG
# v0.2 — <P3-DATE> — PLAN-017: Windows (Git Bash) support — drive-form path-key, directory
#         junction (mklink /J) in place of the symlink, junctions removed with rmdir (never
#         rm), rename-to-backup + no-overwrite copy in place of mv, refusal while a session
#         is live. An adopter's E002: the merge recurses into same-name dirs and drops the
#         empty ones Claude Code creates (link/adopt no longer abort on its empty memory/);
#         status names `link`, not `adopt`, when in-repo data already exists; link absorbs
#         the pre-v1.5 memory layout too.
# v0.1 — 2026-08-16 — Initial for this suite (PLAN-010 upstream intake): ported from an
#         upstream project's locality tool; added the pre-v1.5 memory-symlink layout
#         branch in adopt() (absorbs a harness dir whose memory/ entry symlinks to
#         <repo>/.claude/memory — the old Rule 14 mechanism). Replaces bootstrap_memory.sh.
# ==============================================================
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$REPO/.claude/project-data"

case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) WINDOWS=1; LINKWORD="junction" ;;
  *) WINDOWS=0; LINKWORD="symlink" ;;
esac

if [ "$WINDOWS" = 1 ]; then
  WINPATH="$(cygpath -m "$REPO")"
  DRIVE="$(printf '%s' "$WINPATH" | cut -c1 | tr '[:upper:]' '[:lower:]')"
  KEY="$(printf '%s%s' "$DRIVE" "$(printf '%s' "$WINPATH" | cut -c2-)" | sed 's#[^A-Za-z0-9]#-#g')"
else
  KEY="$(printf '%s' "$REPO" | sed 's#[^A-Za-z0-9]#-#g')"
fi
HARNESS_DIR="$HOME/.claude/projects/$KEY"

say() { printf '%s\n' "$*"; }

is_link() {  # $1 is a symlink, or (Windows) a junction Git Bash may not report as one
  [ -L "$1" ] && return 0
  if [ "$WINDOWS" = 1 ] && [ -e "$1" ]; then
    [ "$(readlink -f "$1")" != "$(readlink -f "$(dirname "$1")")/$(basename "$1")" ]
    return
  fi
  return 1
}

link_target() {
  if [ "$WINDOWS" = 1 ]; then readlink -f "$1"; else readlink "$1"; fi
}

points_home() {  # the link at $1 resolves to this repo's project-data
  if [ "$WINDOWS" = 1 ]; then
    [ -d "$DATA" ] && [ "$(readlink -f "$1")" = "$(readlink -f "$DATA")" ]
  else
    [ "$(readlink "$1")" = "$DATA" ] && [ -d "$DATA" ]
  fi
}

make_link() {  # harness path -> $DATA
  mkdir -p "$(dirname "$HARNESS_DIR")"
  if [ "$WINDOWS" = 1 ]; then
    cmd //c mklink //J "$(cygpath -w "$HARNESS_DIR")" "$(cygpath -w "$DATA")" >/dev/null
  else
    ln -s "$DATA" "$HARNESS_DIR"
  fi
}

drop_link() {  # remove the link at $1 — never what it points to
  if [ "$WINDOWS" = 1 ]; then
    cmd //c rmdir "$(cygpath -w "$1")" >/dev/null
  else
    rm "$1"
  fi
}

status() {
  say "repo:          $REPO"
  say "path-key:      $KEY"
  say "harness path:  $HARNESS_DIR"
  say "physical home: $DATA"
  if is_link "$HARNESS_DIR"; then
    say "$LINKWORD:       -> $(link_target "$HARNESS_DIR")"
    if points_home "$HARNESS_DIR"; then
      say "STATUS: OK — data lives in the project folder ($(ls -1 "$DATA/memory" 2>/dev/null | wc -l | tr -d ' ') memory files)"
    else
      say "STATUS: BROKEN — $LINKWORD does not resolve to this repo's project-data. Run: link"
      return 1
    fi
  elif [ -d "$HARNESS_DIR" ]; then
    if [ -d "$DATA" ]; then
      say "STATUS: NOT LINKED — Claude Code created a real directory at the harness path, and in-repo data exists. Run: link"
    else
      say "STATUS: NOT ADOPTED — real directory at the harness path (data outside the project folder). Run: adopt"
    fi
    return 1
  elif [ -d "$DATA" ]; then
    say "STATUS: NOT LINKED — in-repo data exists but the harness path is absent (fresh machine / folder moved). Run: link"
    return 1
  else
    say "STATUS: EMPTY — no data on either side (brand-new project on this machine). Run: link (creates the home + $LINKWORD)"
    return 1
  fi
}

merge_dir_into() {  # move the contents of real dir $1 into dir $2 without clobbering;
                    # same-name dirs merge recursively and are dropped once empty (E002)
  find "$1" -mindepth 1 -maxdepth 1 -print0 | while IFS= read -r -d '' item; do
    base="$(basename "$item")"
    dest="$2/$base"
    if [ ! -e "$dest" ] && [ ! -L "$dest" ]; then
      mv "$item" "$2/" && say "  moved: $base"
    elif [ -d "$item" ] && [ ! -L "$item" ] && [ -d "$dest" ] && [ ! -L "$dest" ]; then
      merge_dir_into "$item" "$dest"
      if rmdir "$item" 2>/dev/null; then say "  merged: $base/"; fi
    else
      say "  skip (exists at destination): $base"
    fi
  done
}

copy_missing() {  # copy every file under $1 that is absent under $2 — never overwrite
  ( cd "$1" && find . -type f -print0 ) | while IFS= read -r -d '' rel; do
    rel="${rel#./}"
    if [ -e "$2/$rel" ]; then
      say "  skip (exists at destination): $rel"
    else
      mkdir -p "$2/$(dirname "$rel")"
      cp -p "$1/$rel" "$2/$rel" || { say "  FAILED to copy: $rel"; exit 1; }
    fi
  done
}

absorb_old_memory() {  # pre-v1.5 layout (old Rule 14): $1/memory links to <repo>/.claude/memory
  if is_link "$1/memory"; then
    drop_link "$1/memory"
    if [ -d "$REPO/.claude/memory" ] && [ ! -e "$DATA/memory" ]; then
      mkdir -p "$DATA"
      mv "$REPO/.claude/memory" "$DATA/memory"
      say "  absorbed old in-repo memory store -> project-data/memory"
    elif [ -d "$REPO/.claude/memory" ]; then
      say "  note: project-data/memory already exists — the old store stays at .claude/memory; merge it by hand"
    fi
  fi
}

absorb_harness_dir() {  # bring the real dir at the harness path into $DATA; frees the path
  if [ "$WINDOWS" = 1 ]; then
    recent="$(find "$HARNESS_DIR" -maxdepth 1 -name '*.jsonl' -mmin -2 2>/dev/null | head -n 1 || true)"
    if [ -n "$recent" ]; then
      say "ABORT: a Claude Code session for this project looks active (a transcript changed in the last 2 minutes)."
      say "       Close Claude Code, then run this again from a Git Bash window."
      return 1
    fi
    backup="$HARNESS_DIR.pre-locality-$(date +%Y%m%d-%H%M%S)"
    if ! mv "$HARNESS_DIR" "$backup"; then
      say "ABORT: could not move the harness dir aside (in use?) — close Claude Code and retry."
      return 1
    fi
    say "Harness dir moved aside to $backup — copying its data in (nothing is overwritten)."
    say "  (if anything below fails, restore with: mv \"$backup\" \"$HARNESS_DIR\")"
    absorb_old_memory "$backup"
    mkdir -p "$DATA"
    if ! copy_missing "$backup" "$DATA"; then
      say "ABORT: copy failed — nothing was deleted; the original is still at $backup"
      return 1
    fi
    say "  original kept at $backup — delete it once Claude Code shows your memories"
    return 0
  fi
  absorb_old_memory "$HARNESS_DIR"
  if [ -d "$DATA" ]; then
    say "$1"
    merge_dir_into "$HARNESS_DIR" "$DATA"
    leftover="$(find "$HARNESS_DIR" -mindepth 1 | head -n 1 || true)"
    if [ -n "$leftover" ]; then
      say "ABORT: harness dir not empty after merge (name collisions above) — resolve manually."; return 1
    fi
    rmdir "$HARNESS_DIR"
  else
    mv "$HARNESS_DIR" "$DATA"
  fi
}

adopt() {
  if is_link "$HARNESS_DIR"; then
    say "Already adopted — harness path is a $LINKWORD."; status; return 0
  fi
  if [ ! -d "$HARNESS_DIR" ]; then
    say "Nothing to adopt at $HARNESS_DIR — use: link"; return 1
  fi
  mkdir -p "$REPO/.claude"
  absorb_harness_dir "In-repo home exists — merging harness dir into it:"
  make_link
  say "Adopted."; status
}

link() {
  mkdir -p "$DATA"
  if is_link "$HARNESS_DIR"; then
    if points_home "$HARNESS_DIR"; then say "Already linked."; status; return 0; fi
    say "Re-pointing stale $LINKWORD (was -> $(link_target "$HARNESS_DIR"))"
    drop_link "$HARNESS_DIR"
  elif [ -d "$HARNESS_DIR" ]; then
    absorb_harness_dir "Harness-created dir found (session started before link) — merging it in:"
  fi
  make_link
  say "Linked."; status
}

case "${1:-status}" in
  status) status ;;
  adopt)  adopt ;;
  link)   link ;;
  *) say "Usage: $0 [status|adopt|link]"; exit 2 ;;
esac
```

### 5b — `tests/test_claude_project_data.py` (vault) — NEW FILE (0.1)
<!-- block id=5b repo=vault path=tests/test_claude_project_data.py kind=new -->
**5b** — the file must not exist; write:

```text
# ==============================================================
# VERSION: 0.1
# Behavior tests for scripts/claude_project_data.sh (CLAUDE.md Rule 14 locality tool).
#
# CHANGE LOG
# v0.1 — <P3-DATE> — Initial (PLAN-017): the script runs for real against throwaway repo +
#         HOME trees — POSIX status / link / adopt, the pre-v1.5 memory layout, the E002
#         folder-move merge — and its Windows branch through stand-in uname / cygpath / cmd
#         commands (a junction is simulated by a symlink; cmd calls are logged).
# ==============================================================
"""Tests for scripts/claude_project_data.sh — run the real script in temp trees."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "claude_project_data.sh"
OLD = time.time() - 3600  # an mtime well outside the live-session window

pytestmark = pytest.mark.skipif(shutil.which("bash") is None, reason="bash not available")


@dataclass
class Tree:
    repo: Path
    home: Path
    env: dict[str, str]
    log: Path | None = None

    @property
    def data(self) -> Path:
        return self.repo / ".claude" / "project-data"

    def run(self, verb: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["bash", str(self.repo / "scripts" / "claude_project_data.sh"), verb],
            env=self.env, capture_output=True, text=True, check=False,
        )

    def harness(self) -> Path:
        out = self.run("status").stdout
        match = re.search(r"^harness path:\s+(.+)$", out, re.MULTILINE)
        assert match, out
        return Path(match.group(1))


def _write(path: Path, text: str = "x", mtime: float | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if mtime is not None:
        os.utime(path, (mtime, mtime))


def _make_repo(repo: Path) -> None:
    (repo / "scripts").mkdir(parents=True)
    shutil.copy2(SCRIPT, repo / "scripts" / "claude_project_data.sh")


@pytest.fixture
def posix(tmp_path: Path) -> Tree:
    repo = tmp_path / "work" / "my repo"
    home = tmp_path / "home"
    home.mkdir()
    _make_repo(repo)
    env = {**os.environ, "HOME": str(home)}
    return Tree(repo=repo, home=home, env=env)


_SHIMS = {
    "uname": '#!/bin/bash\necho "MINGW64_NT-10.0-19045"\n',
    "cygpath": (
        "#!/bin/bash\n"
        'p="$2"; rest="${p#"$FAKE_WINROOT"/}"\n'
        '[ "$rest" != "$p" ] || exit 1\n'
        'drive="$(printf \'%s\' "${rest:0:1}" | tr \'[:lower:]\' \'[:upper:]\')"\n'
        'out="$drive:${rest:1}"\n'
        '[ "$1" = "-w" ] && out="${out//\\//\\\\}"\n'
        "printf '%s\\n' \"$out\"\n"
    ),
    "cmd": (
        "#!/bin/bash\n"
        'echo "cmd $*" >> "$SHIM_LOG"\n'
        "topath() {\n"
        '  p="${1//\\\\//}"\n'
        '  d="$(printf \'%s\' "${p:0:1}" | tr \'[:upper:]\' \'[:lower:]\')"\n'
        "  printf '%s/%s%s' \"$FAKE_WINROOT\" \"$d\" \"${p:2}\"\n"
        "}\n"
        'case "$2" in\n'
        '  mklink) ln -s "$(topath "$5")" "$(topath "$4")" ;;\n'
        '  rmdir) t="$(topath "$3")"; if [ -L "$t" ]; then rm "$t"; else rmdir "$t"; fi ;;\n'
        "  *) exit 1 ;;\n"
        "esac\n"
    ),
}


@pytest.fixture
def windows(tmp_path: Path) -> Tree:
    root = tmp_path / "win"
    repo = root / "e" / "Work_Area" / "demo-repo"
    home = root / "c" / "Users" / "someone"
    home.mkdir(parents=True)
    _make_repo(repo)
    shims = tmp_path / "shims"
    shims.mkdir()
    for name, body in _SHIMS.items():
        (shims / name).write_text(body, encoding="utf-8")
        (shims / name).chmod(0o755)
    log = tmp_path / "cmd.log"
    log.touch()
    env = {
        **os.environ, "HOME": str(home), "PATH": f"{shims}{os.pathsep}{os.environ['PATH']}",
        "FAKE_WINROOT": str(root), "SHIM_LOG": str(log),
    }
    return Tree(repo=repo, home=home, env=env, log=log)


# ---- POSIX (macOS / Linux) -------------------------------------------------


def test_posix_empty_then_link_is_idempotent(posix: Tree) -> None:
    first = posix.run("status")
    assert first.returncode == 1 and "STATUS: EMPTY" in first.stdout
    linked = posix.run("link")
    assert linked.returncode == 0 and "STATUS: OK" in linked.stdout
    harness = posix.harness()
    assert harness.is_symlink() and os.readlink(harness) == str(posix.data)
    again = posix.run("link")
    assert again.returncode == 0 and "Already linked." in again.stdout


def test_posix_adopt_moves_harness_data_in(posix: Tree) -> None:
    harness = posix.harness()
    _write(harness / "memory" / "a.md")
    _write(harness / "s1.jsonl")
    assert "Run: adopt" in posix.run("status").stdout
    out = posix.run("adopt")
    assert out.returncode == 0 and "STATUS: OK" in out.stdout
    assert (posix.data / "memory" / "a.md").is_file() and (posix.data / "s1.jsonl").is_file()
    assert harness.is_symlink()


def test_posix_adopt_absorbs_pre_v15_memory_layout(posix: Tree) -> None:
    old_store = posix.repo / ".claude" / "memory"
    _write(old_store / "a.md")
    _write(old_store / "b.md")
    harness = posix.harness()
    harness.mkdir(parents=True)
    (harness / "memory").symlink_to(old_store)
    _write(harness / "s1.jsonl")
    out = posix.run("adopt")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "absorbed old in-repo memory store" in out.stdout
    assert "(2 memory files)" in out.stdout
    assert not old_store.exists() and (posix.data / "s1.jsonl").is_file()


def test_posix_e002_folder_move_merges_harness_created_dir(posix: Tree) -> None:
    for name in ("a.md", "b.md", "c.md"):
        _write(posix.data / "memory" / name)
    harness = posix.harness()
    (harness / "memory").mkdir(parents=True)  # what Claude Code creates on session start
    _write(harness / "new.jsonl")
    status = posix.run("status")
    assert status.returncode == 1 and "Run: link" in status.stdout and "adopt" not in status.stdout
    out = posix.run("link")
    assert out.returncode == 0 and "(3 memory files)" in out.stdout, out.stdout
    assert (posix.data / "new.jsonl").is_file() and harness.is_symlink()


def test_posix_merge_recurses_into_same_name_dirs(posix: Tree) -> None:
    _write(posix.data / "memory" / "a.md")
    harness = posix.harness()
    _write(harness / "memory" / "c.md")
    out = posix.run("link")
    assert out.returncode == 0, out.stdout
    assert sorted(p.name for p in (posix.data / "memory").iterdir()) == ["a.md", "c.md"]


def test_posix_file_collision_still_aborts_without_loss(posix: Tree) -> None:
    _write(posix.data / "f.txt", "in-repo")
    harness = posix.harness()
    _write(harness / "f.txt", "harness")
    out = posix.run("link")
    assert out.returncode == 1 and "ABORT" in out.stdout
    assert (posix.data / "f.txt").read_text(encoding="utf-8") == "in-repo"
    assert (harness / "f.txt").read_text(encoding="utf-8") == "harness"


def test_posix_stale_symlink_is_repointed(posix: Tree, tmp_path: Path) -> None:
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    posix.data.mkdir(parents=True)
    harness = posix.harness()
    harness.parent.mkdir(parents=True)
    harness.symlink_to(elsewhere)
    assert "STATUS: BROKEN" in posix.run("status").stdout
    out = posix.run("link")
    assert out.returncode == 0 and "Re-pointing stale symlink" in out.stdout
    assert os.readlink(harness) == str(posix.data)


# ---- Windows (Git Bash) through stand-in uname / cygpath / cmd ---------------


def test_windows_path_key_uses_the_lowercased_drive_form(windows: Tree) -> None:
    out = windows.run("status").stdout
    assert re.search(r"^path-key:\s+e--Work-Area-demo-repo$", out, re.MULTILINE), out
    expected = windows.home / ".claude" / "projects" / "e--Work-Area-demo-repo"
    assert windows.harness() == expected


def test_windows_adopt_migrates_the_old_junction_layout(windows: Tree) -> None:
    old_store = windows.repo / ".claude" / "memory"
    _write(old_store / "m1.md", mtime=OLD)
    _write(old_store / "m2.md", mtime=OLD)
    harness = windows.harness()
    harness.mkdir(parents=True)
    (harness / "memory").symlink_to(old_store)  # bootstrap_memory.sh's junction
    _write(harness / "old.jsonl", "transcript", mtime=OLD)
    out = windows.run("adopt")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "STATUS: OK" in out.stdout and "(2 memory files)" in out.stdout
    assert harness.is_symlink() and harness.resolve() == windows.data.resolve()
    assert (windows.data / "old.jsonl").read_text(encoding="utf-8") == "transcript"
    backups = list(harness.parent.glob(f"{harness.name}.pre-locality-*"))
    assert len(backups) == 1 and (backups[0] / "old.jsonl").is_file()
    assert windows.log is not None
    calls = windows.log.read_text(encoding="utf-8")
    assert "cmd //c rmdir " in calls and "\\memory" in calls  # junction dropped via rmdir
    assert "cmd //c mklink //J " in calls


def test_windows_refuses_while_a_session_is_live(windows: Tree) -> None:
    harness = windows.harness()
    _write(harness / "live.jsonl")  # mtime = now
    out = windows.run("adopt")
    assert out.returncode == 1 and "looks active" in out.stdout
    assert harness.is_dir() and not harness.is_symlink()
    assert not list(harness.parent.glob(f"{harness.name}.pre-locality-*"))


def test_windows_e002_link_after_move_keeps_memories(windows: Tree) -> None:
    for name in ("a.md", "b.md"):
        _write(windows.data / "memory" / name)
    harness = windows.harness()
    (harness / "memory").mkdir(parents=True)
    _write(harness / "s.jsonl", mtime=OLD)
    assert "Run: link" in windows.run("status").stdout
    out = windows.run("link")
    assert out.returncode == 0 and "(2 memory files)" in out.stdout, out.stdout + out.stderr
    assert (windows.data / "s.jsonl").is_file()
    again = windows.run("link")
    assert again.returncode == 0 and "Already linked." in again.stdout
    assert "junction:" in again.stdout
```

### 5c — `scripts/validation_ownership.toml` (vault) — `[rules.locality]`
<!-- block id=5c.1 repo=vault path=scripts/validation_ownership.toml kind=replace -->
**5c.1** FIND:

```text
reason       = "Fleet view — docs/fleet.csv rows + the pre-push freshness check (PLAN-016)."

[monitored_paths]
```

REPLACE WITH:

```text
reason       = "Fleet view — docs/fleet.csv rows + the pre-push freshness check (PLAN-016)."

[rules.locality]
source_paths = ["scripts/claude_project_data.sh"]
test_paths   = ["tests/test_claude_project_data.py"]
doc_paths    = ["docs/folder_structure.md"]
strictness   = "soft"
require_docs = false
reason       = "Rule 14 locality tool — symlink / Windows junction; adopt + link merges (PLAN-017)."

[monitored_paths]
```

### 5d — `config/projects.toml` (vault) — the 780-estimator entry
<!-- block id=5d.1 repo=vault path=config/projects.toml kind=replace -->
**5d.1** FIND:

```text
# NOTE: high-stakes live project — every engine write lands in its working tree (local flush =
# write-in-place); its next session lands per docs/SYNC_HANDOFF.md BEFORE any other work.
# Write only between Equinex work sessions, one machine at a time.
```

REPLACE WITH:

```text
# NOTE: high-stakes live project — every engine write lands in its working tree (local flush =
# write-in-place); its next session lands per docs/SYNC_HANDOFF.md BEFORE any other work.
# Write only between Equinex work sessions, one machine at a time.

[[project]]                        # team project; Set v1.3 old-SETUP adopter (2026-06-21), caught up via sync (PLAN-017)
name = "780-estimator"
transport = "git"
git_url = "git@github.com:780-AI/780-estimator.git"
git_branch = "main"
owner = "team"
git_remote = "github.com/780-AI/780-estimator"
part_of = "780-AI"
work_machine = "Bahereh Hassanpour's PC (Windows)"
delivery = "direct+handoff"
onboarding = "catch-up"
onboarded_on = "2026-06-21"
onboarded_set = "v1.3"
registered_on = "<P3-DATE>"
plan = "PLAN-017"
lifecycle = "onboarding"
caveats = "first git-transport target: engine writes are commits pushed to main; Windows PC (Git Bash, Rule 14 via junctions)"
# NOTE: owner Bahereh Hassanpour. Delivery A (operator, 2026-10-05): the engine commits as
# "Standard DocSet" and pushes straight to `main` — fast-forward only, so a concurrent push makes
# the write fail, never overwrite; the owner's next session pulls and lands docs/SYNC_HANDOFF.md.
```

### 5e — `docs/SESSION_OPENER.md` (vault) — 1.20 → 1.21 + § 2 registry row
<!-- block id=5e.1 repo=vault path=docs/SESSION_OPENER.md kind=replace -->
**5e.1** FIND:

```text
<!-- VERSION: 1.20 -->
<!-- Last Updated: 2026-10-05 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.21 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5e.2 repo=vault path=docs/SESSION_OPENER.md kind=replace -->
**5e.2** FIND:

```text
CHANGE LOG
v1.20 — 2026-10-05 — PLAN-016: § 1.2 fleet-view bullet (run `status` — prints every target's state and regenerates `docs/fleet.csv`; call out unreachable / not-current / handoff-pending targets); § 4 "Registered target suites" line reads from that run.
```

REPLACE WITH:

```text
CHANGE LOG
v1.21 — <P3-DATE> — Fifth target registered: 780-estimator (§ 2 registry row — git transport, the first git target; team project on a Windows PC; Set v1.3 old-SETUP adopter caught up to v2.7 after a one-time prep commit — PLAN-017).
v1.20 — 2026-10-05 — PLAN-016: § 1.2 fleet-view bullet (run `status` — prints every target's state and regenerates `docs/fleet.csv`; call out unreachable / not-current / handoff-pending targets); § 4 "Registered target suites" line reads from that run.
```

<!-- block id=5e.3 repo=vault path=docs/SESSION_OPENER.md kind=replace -->
**5e.3** FIND:

```text
| | `EverOn.Equinex` — `~/Library/CloudStorage/Dropbox/Projects/EverOn.Equinex` (Dropbox-synced) | Registered 2026-10-03 (local transport, `~` path — resolves per machine; ONE machine at a time, let Dropbox settle). Adopted Set v2.7 2026-10-03 via the skill's adopt mode (PLAN-011); EverOn own line retired — pre-adoption archive + numbering crosswalk in `archive/LESSONS_LEGACY.md`. High-stakes live project: engine writes only between its work sessions. |
<!-- PROJECT-OWNED:END -->
```

REPLACE WITH:

```text
| | `EverOn.Equinex` — `~/Library/CloudStorage/Dropbox/Projects/EverOn.Equinex` (Dropbox-synced) | Registered 2026-10-03 (local transport, `~` path — resolves per machine; ONE machine at a time, let Dropbox settle). Adopted Set v2.7 2026-10-03 via the skill's adopt mode (PLAN-011); EverOn own line retired — pre-adoption archive + numbering crosswalk in `archive/LESSONS_LEGACY.md`. High-stakes live project: engine writes only between its work sessions. |
| | `780-estimator` — `git@github.com:780-AI/780-estimator.git` (branch `main`) | Registered <P3-DATE> — git transport, the FIRST git target: every engine write is a commit pushed straight to their `main` (Delivery A; fast-forward only — a concurrent push makes the write fail, never overwrite). Team project, owner Bahereh Hassanpour, worked on from a Windows PC (Git Bash; Rule 14 via directory junctions — `claude_project_data.sh` v0.2). Bootstrapped Set v1.3 2026-06-21 (old SETUP flow); caught up to v2.7 <P3-DATE> by `sync` after a one-time prep commit (v1.6 heading wrap + sync-ready SVA + locality tool) — PLAN-017. |
<!-- PROJECT-OWNED:END -->
```

### 5f — `skill/SKILL.md` (vault) — 0.1 → 0.2: the old-SETUP catch-up paragraph
<!-- block id=5f.1 repo=vault path=skill/SKILL.md kind=replace -->
**5f.1** FIND:

```text
<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-08-16 -->
<!--
CHANGE LOG
```

REPLACE WITH:

```text
<!-- VERSION: 0.2 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.2 — <P3-DATE> — PLAN-017: the old-SETUP catch-up paragraph names the whole one-time prep
(heading wrap, sync-ready SET_VERSION_ADOPTED, locality script) and an engine dry-run before
registering — the gaps the first catch-up exposed.
```

<!-- block id=5f.2 repo=vault path=skill/SKILL.md kind=replace -->
**5f.2** FIND:

```text
If the operator says the project is an **old-SETUP adopter** (already carries the suite, just a
stale Set Version), neither mode applies — tell them the path is: register the project in the
vault's `config/projects.toml`, hand-apply the one-time v1.6 heading-wrap if it predates v1.6, and
let `sync` catch it up. Do not run a delivery mode over an existing adopter.
```

REPLACE WITH:

```text
If the operator says the project is an **old-SETUP adopter** (already carries the suite, just a
stale Set Version), neither mode applies — tell them the path is a one-time prep commit in the
project, then registration, then `sync`. The prep commit supplies what the engine needs and an
old-SETUP copy lacks: the v1.6 PROJECT-OWNED heading-wrap of the session opener + closer if it
predates v1.6; `docs/SET_VERSION_ADOPTED.md` rewritten in the sync-ready shape `modes/adopt.md`
§ 5 specifies, still recording the version the project really has (the engine refuses any other
shape); and `scripts/claude_project_data.sh` copied verbatim from the vault if absent (sync never
delivers scripts, yet the synced Rule 14 calls it). Before registering, prove it with an engine
dry-run against the prepared copy: it must list only suite files. Then register the project in
the vault's `config/projects.toml` and let `sync` catch it up. Do not run a delivery mode over an
existing adopter.
```

### 5g — `docs/folder_structure.md` (vault) — 0.15 → 0.16 + tree
<!-- block id=5g.1 repo=vault path=docs/folder_structure.md kind=replace -->
**5g.1** FIND:

```text
<!-- VERSION: 0.15 -->
<!-- Last Updated: 2026-10-05 -->
<!--
CHANGE LOG
```

REPLACE WITH:

```text
<!-- VERSION: 0.16 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.16 — <P3-DATE> — PLAN-017: added tests/test_claude_project_data.py to the tree; the claude_project_data.sh comment notes the Windows junction.
```

<!-- block id=5g.2 repo=vault path=docs/folder_structure.md kind=replace -->
**5g.2** FIND:

```text
│   ├── test_fleet.py
│   └── test_cli.py
```

REPLACE WITH:

```text
│   ├── test_fleet.py
│   ├── test_claude_project_data.py
│   └── test_cli.py
```

<!-- block id=5g.3 repo=vault path=docs/folder_structure.md kind=replace -->
**5g.3** FIND:

```text
│   ├── claude_project_data.sh    # Rule 14 project-data locality tool (status / adopt / link)
```

REPLACE WITH:

```text
│   ├── claude_project_data.sh    # Rule 14 project-data locality tool (status / adopt / link; symlink, or a junction on Windows)
```

### 5h — `docs/SESSION_OPENER.md` (estimator) — 1.2 → 1.3: heading wrap + § 2 note into its block
<!-- block id=5h.1 repo=estimator path=docs/SESSION_OPENER.md kind=replace -->
**5h.1** FIND:

```text
<!-- VERSION: 1.2 -->
<!-- Last Updated: 2026-06-21 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.3 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5h.2 repo=estimator path=docs/SESSION_OPENER.md kind=replace -->
**5h.2** FIND:

```text
CHANGE LOG
v1.2 — 2026-06-21 — Added § 3.2 project-specific row 1: never use the AskUserQuestion popup; ask inline in chat (pairs with feedback_ask_in_chat_not_popup memory + CLAUDE.md § 10).
```

REPLACE WITH:

```text
CHANGE LOG
v1.3 — <P3-DATE> — Standard Set catch-up prep (Standard DocSet PLAN-017): instance heading + BINDING note wrapped in a PROJECT-OWNED block (the v1.6 heading wrap the vault's sync engine needs); the § 2 "Current state" note moved inside the § 2 PROJECT-OWNED block so the sync keeps it.
v1.2 — 2026-06-21 — Added § 3.2 project-specific row 1: never use the AskUserQuestion popup; ask inline in chat (pairs with feedback_ask_in_chat_not_popup memory + CLAUDE.md § 10).
```

<!-- block id=5h.3 repo=estimator path=docs/SESSION_OPENER.md kind=replace -->
**5h.3** FIND:

```text
# SESSION_OPENER.md — Mandatory session-start pre-flight (780-estimator)

> **BINDING for every Claude session in this repository.** Read this file and execute its § 1 pre-flight before acting on the operator's first task, then post the § 4 first-response block. (Mandated by repo-root `CLAUDE.md` Rule 9.)
```

REPLACE WITH:

```text
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# SESSION_OPENER.md — Mandatory session-start pre-flight (780-estimator)

> **BINDING for every Claude session in this repository.** Read this file and execute its § 1 pre-flight before acting on the operator's first task, then post the § 4 first-response block. (Mandated by repo-root `CLAUDE.md` Rule 9.)
<!-- PROJECT-OWNED:END -->
```

<!-- block id=5h.4 repo=estimator path=docs/SESSION_OPENER.md kind=replace -->
**5h.4** FIND:

```text
**Current state (2026-06-21): no remote infrastructure provisioned yet.** The target deployment shape is Dockerized + GitLab CI → VPS (registry-pull). Until the VPS and GitLab project exist, all work is local and § 1.2 live-system probes are N/A. Fill the rows below the moment each environment is provisioned — never invent a host.

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
```

REPLACE WITH:

```text
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
**Current state (2026-06-21): no remote infrastructure provisioned yet.** The target deployment shape is Dockerized + GitLab CI → VPS (registry-pull). Until the VPS and GitLab project exist, all work is local and § 1.2 live-system probes are N/A. Fill the rows below the moment each environment is provisioned — never invent a host.

```

### 5i — `docs/SESSION_CLOSER.md` (estimator) — 1.1 → 1.2: heading wrap
<!-- block id=5i.1 repo=estimator path=docs/SESSION_CLOSER.md kind=replace -->
**5i.1** FIND:

```text
<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-06-21 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.2 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5i.2 repo=estimator path=docs/SESSION_CLOSER.md kind=replace -->
**5i.2** FIND:

```text
CHANGE LOG
v1.1 — 2026-06-21 — Strip-consistency: point § 1.2 Set-Version lookup at docs/SET_VERSION_ADOPTED.md (STANDARDS_INDEX.md was stripped); corrected the Source provenance line.
```

REPLACE WITH:

```text
CHANGE LOG
v1.2 — <P3-DATE> — Standard Set catch-up prep (Standard DocSet PLAN-017): instance heading + BINDING note wrapped in a PROJECT-OWNED block (the v1.6 heading wrap the vault's sync engine needs).
v1.1 — 2026-06-21 — Strip-consistency: point § 1.2 Set-Version lookup at docs/SET_VERSION_ADOPTED.md (STANDARDS_INDEX.md was stripped); corrected the Source provenance line.
```

<!-- block id=5i.3 repo=estimator path=docs/SESSION_CLOSER.md kind=replace -->
**5i.3** FIND:

```text
# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (780-estimator)

> **BINDING for every Claude session in this repository.** On a wrap-up trigger keyword, read this file and execute its § 1 routine before any farewell, then post the § 4 block. (Mandated by repo-root `CLAUDE.md` Rule 12.)
```

REPLACE WITH:

```text
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (780-estimator)

> **BINDING for every Claude session in this repository.** On a wrap-up trigger keyword, read this file and execute its § 1 routine before any farewell, then post the § 4 block. (Mandated by repo-root `CLAUDE.md` Rule 12.)
<!-- PROJECT-OWNED:END -->
```

### 5j — `docs/SET_VERSION_ADOPTED.md` (estimator) — 1.0 → 1.1: sync-ready shape — WHOLE-FILE REPLACE
<!-- block id=5j repo=estimator path=docs/SET_VERSION_ADOPTED.md kind=whole pre_blob=6ee9fc20aecd103bbbfed8ac0bdc91435c526285 -->
**5j** — the live file must hash to `6ee9fc20aecd103bbbfed8ac0bdc91435c526285` (`git hash-object`); replace its whole content with:

```text
<!-- VERSION: 1.1 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v1.1 — <P3-DATE> — Rewritten in the shape the Standard DocSet sync engine updates mechanically (Standard DocSet PLAN-017 catch-up prep): the `Standard Set Version` + `Adopted on` bullets and the backport table. Still records v1.3 — the engine's sync commit records the new version.
v1.0 — 2026-06-21 — Adoption record created at bootstrap (Standard Set v1.3).
-->

# Standard Set Version adopted

- **Standard Set Version:** v1.3 (bootstrapped 2026-06-21 from the canonical suite, old SETUP flow)
- **Adopted on:** 2026-06-21 (bootstrap)
- **Scope:** the operating contract (`CLAUDE.md`), the topical standards library (`docs/standards/`),
  the session pre-flight / wrap-up forcing functions (`docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`),
  the lessons archive (`archive/LESSONS.md`), and durable project data (Rule 14).

## How this file is updated

The suite's curator keeps this repo current with the Standard DocSet `sync` engine. Each sync rewrites
the two bullets above and adds a row to the table below; in `CLAUDE.md`, `docs/SESSION_OPENER.md` and
`docs/SESSION_CLOSER.md` it keeps every PROJECT-OWNED block and replaces the rest; the six
`docs/standards/` files and `archive/LESSONS.md` are replaced whole. Every engine write also leaves
`docs/SYNC_HANDOFF.md`, which tells the next session here what landed and what bookkeeping remains.
Project lessons go to `docs/STANDARDS_LOG.md` as `E0NN` entries — never into the suite files.

## Backport tracking

| Set Version | Adopted on | Notes |
|---|---|---|
| v1.3 | 2026-06-21 | bootstrap (old SETUP flow) |
```

### 5k — `scripts/claude_project_data.sh` (estimator) — NEW: byte-identical copy of the vault file after § 5a
<!-- block id=5k repo=estimator path=scripts/claude_project_data.sh kind=copy source=scripts/claude_project_data.sh -->
**5k** — copy `scripts/claude_project_data.sh` from the vault (after § 5a, dates substituted) byte-for-byte, mode 100755; `cmp` must exit 0.

### 5l — `docs/documents_manifest.md` (estimator) — 1.55 → 1.56: cells + the new script row
<!-- block id=5l.1 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.1** FIND:

```text
<!-- VERSION: 1.55 -->
<!-- Last Updated: 2026-09-14 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.56 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5l.2 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.2** FIND:

```text
| `CHANGELOG.md` | 1.38 | Cross-cutting history. |
```

REPLACE WITH:

```text
| `CHANGELOG.md` | 1.39 | Cross-cutting history. |
```

<!-- block id=5l.3 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.3** FIND:

```text
| `docs/documents_manifest.md` | 1.55 | This version index (critical). |
```

REPLACE WITH:

```text
| `docs/documents_manifest.md` | 1.56 | This version index (critical). |
```

<!-- block id=5l.4 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.4** FIND:

```text
| `docs/folder_structure.md` | 1.16 | Authoritative layout reference. |
```

REPLACE WITH:

```text
| `docs/folder_structure.md` | 1.17 | Authoritative layout reference. |
```

<!-- block id=5l.5 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.5** FIND:

```text
| `docs/SESSION_OPENER.md` | 1.2 | Session-start pre-flight (Rule 9). |
```

REPLACE WITH:

```text
| `docs/SESSION_OPENER.md` | 1.3 | Session-start pre-flight (Rule 9). |
```

<!-- block id=5l.6 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.6** FIND:

```text
| `docs/SESSION_CLOSER.md` | 1.1 | Session wrap-up (Rule 12). |
```

REPLACE WITH:

```text
| `docs/SESSION_CLOSER.md` | 1.2 | Session wrap-up (Rule 12). |
```

<!-- block id=5l.7 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.7** FIND:

```text
| `docs/SET_VERSION_ADOPTED.md` | 1.0 | Adopted Standard Set Version. |
```

REPLACE WITH:

```text
| `docs/SET_VERSION_ADOPTED.md` | 1.1 | Adopted Standard Set Version. |
```

<!-- block id=5l.8 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.8** FIND:

```text
| `scripts/bootstrap_memory.sh` | 0.1 | Durable-memory link bootstrap (Rule 14). |
```

REPLACE WITH:

```text
| `scripts/bootstrap_memory.sh` | 0.1 | Durable-memory link bootstrap (Rule 14). |
| `scripts/claude_project_data.sh` | 0.2 | Project-data locality tool (Rule 14, Standard Set v1.5+): memory + session transcripts live in `.claude/project-data/`, linked from Claude Code's harness path — a symlink on macOS / Linux, a directory junction on Windows (Git Bash). Copied verbatim from the Standard DocSet vault (Standard DocSet PLAN-017); replaces `bootstrap_memory.sh` once `adopt` has run. |
```

### 5m — `docs/folder_structure.md` (estimator) — 1.16 → 1.17: tree line
<!-- block id=5m.1 repo=estimator path=docs/folder_structure.md kind=replace -->
**5m.1** FIND:

```text
<!-- VERSION: 1.16 -->
<!-- Last Updated: 2026-09-13 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.17 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5m.2 repo=estimator path=docs/folder_structure.md kind=replace -->
**5m.2** FIND:

```text
│   ├── run_daily.sh              # daily-flow wrapper for cron/notebook/manual + dependency gate (landed — PLAN-010)
│   └── bootstrap_memory.sh        # durable-memory link (Rule 14)
```

REPLACE WITH:

```text
│   ├── run_daily.sh              # daily-flow wrapper for cron/notebook/manual + dependency gate (landed — PLAN-010)
│   ├── claude_project_data.sh     # project-data locality tool (Rule 14, Set v1.5+; symlink / Windows junction) — replaces bootstrap_memory.sh after `adopt`
│   └── bootstrap_memory.sh        # durable-memory link (Rule 14)
```

### 5n — `CHANGELOG.md` (estimator) — 1.38 → 1.39: header + the catch-up entry
<!-- block id=5n.1 repo=estimator path=CHANGELOG.md kind=replace -->
**5n.1** FIND:

```text
<!-- VERSION: 1.38 -->
<!-- Last Updated: 2026-09-14 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.39 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5n.2 repo=estimator path=CHANGELOG.md kind=replace -->
**5n.2** FIND:

```text
All notable changes to `780-estimator`. Newest at the top. Each entry states an explicit impact.

```

REPLACE WITH:

```text
All notable changes to `780-estimator`. Newest at the top. Each entry states an explicit impact.

## <P3-DATE> — Standard Set catch-up, step 1 of 2: the one-time prep (v1.3 → v2.7)

**Impact: governance documents and one new script only — no forecasting, evaluation, publication,
test or runtime behavior changes.** This repo was bootstrapped on Standard Set v1.3 (2026-06-21). The
suite's curator now keeps adopting projects current with the Standard DocSet `sync` engine; this
commit makes the repo readable by it (Standard DocSet PLAN-017). The next commit is the engine's own
(`Standard DocSet: sync to Standard Set Version v2.7`, author "Standard DocSet"): it updates the suite
files and leaves `docs/SYNC_HANDOFF.md`.

**What this commit changes:**
- `docs/SESSION_OPENER.md` 1.3 / `docs/SESSION_CLOSER.md` 1.2 — the instance heading and its BINDING
  note are wrapped in a PROJECT-OWNED block (the engine keeps PROJECT-OWNED blocks and replaces the
  rest); the opener's § 2 "Current state" note moved inside the § 2 block so it survives.
- `docs/SET_VERSION_ADOPTED.md` 1.1 — rewritten in the shape the engine updates mechanically; it
  still records v1.3 until the sync commit records v2.7.
- `scripts/claude_project_data.sh` 0.2 (new) — the suite's Rule 14 tool since Set v1.5: memory AND
  session transcripts live in `.claude/project-data/`, linked from Claude Code's folder — a directory
  junction on Windows. It replaces `scripts/bootstrap_memory.sh`, which stays until the migration
  below has run.
- `docs/documents_manifest.md` 1.56, `docs/folder_structure.md` 1.17 — registered.

**What the sync commit will change:** `CLAUDE.md` (15 standing rules: Rule 14 upgraded to project-data
locality, new Rule 15, § 15.9 feature intake, …), `archive/LESSONS.md` (L001–L051 → L001–L081),
`docs/standards/PROJECT_STANDARDS.md` + `MEMORY_PROTOCOL.md`, everything outside the PROJECT-OWNED
blocks of the session opener and closer, and the adoption record. Two local texts do not survive it,
by design: the `CLAUDE.md` § 10 line "ask in plain chat, never via a popup" (the rule lives on in
opener § 3.2 row 1) and the "Branch convention: `main`" lines (the template now writes
`origin/<main-branch>`).

**Next session on the Windows PC, in order:**
1. `git pull` before any other work.
2. The updated opener § 1.1 finds `docs/SYNC_HANDOFF.md` — land it first. Over git the engine's files
   arrive ALREADY COMMITTED (its commit, author "Standard DocSet"), so the handoff's "review the
   diffs" step means `git show` of that commit. Then reconcile the manifest cells for the files it
   lists, add a CHANGELOG entry, and delete the handoff — one commit.
3. The updated opener § 1.5 runs `bash scripts/claude_project_data.sh status` and reports
   `NOT ADOPTED`. Note the memory count first (`ls .claude/memory | wc -l`). Close Claude Code, open
   Git Bash in the repo, run `bash scripts/claude_project_data.sh adopt`, reopen Claude Code, and
   confirm `status` says `STATUS: OK` with that same count. Keep the `*.pre-locality-*` backup it
   reports until your memories show up, then delete it.
4. Once `status` says `STATUS: OK`: delete `scripts/bootstrap_memory.sh` with its manifest row and
   its `docs/folder_structure.md` line (one commit).
5. Send the `status` / `adopt` output to the curator — it is the Windows verification of the new
   tool (Standard DocSet PLAN-017 QA-M8).

**QA scenarios** (Rule 11): step 3 above is this change's scenario — ⏸ until it runs on the Windows
PC. The curator's side (engine dry-run, sync write, idempotent re-run) is recorded in Standard
DocSet PLAN-017.

```

<!-- §5-GENERATED:END -->

### 5o — estimator prep commit message (verbatim; `git commit -F <file>`)

```text
Docs/Governance: Standard Set catch-up prep, step 1 of 2 (v1.3 -> v2.7)

One-time preparation so the Standard DocSet sync engine can bring this repo
from Standard Set v1.3 to v2.7 (Standard DocSet PLAN-017). Governance docs
and one new script only; no runtime, domain or test change.

- docs/SESSION_OPENER.md 1.3, docs/SESSION_CLOSER.md 1.2: instance heading
  wrapped in a PROJECT-OWNED block; the opener's section 2 "Current state"
  note moved inside its block.
- docs/SET_VERSION_ADOPTED.md 1.1: the engine's sync-ready shape (still v1.3).
- scripts/claude_project_data.sh 0.2 (new): Rule 14 project-data locality
  tool with Windows junction support; replaces bootstrap_memory.sh after
  `adopt` (steps in CHANGELOG.md).
- docs/documents_manifest.md 1.56, docs/folder_structure.md 1.17,
  CHANGELOG.md 1.39: registered.

Step 2 is the engine's own commit (author "Standard DocSet").

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
```

### 5p — E002 write-back decisions (verbatim TOML; `integrate --apply <file>`, then `--write`)

```toml
[[integrated]]
project = "EverOn.Capital-Signal"
entry = "E002"
lesson = "scripts/claude_project_data.sh v0.2"
topical = "PLAN-017 locality-tool fix — same-name dirs merge, status names link; adopter copies refresh at the script-delivery fix"
set_version = "v2.7"
```

Rendered Status (dry-run 2026-10-05): `integrated → vault scripts/claude_project_data.sh v0.2 (PLAN-017
locality-tool fix — same-name dirs merge, status names link; adopter copies refresh at the
script-delivery fix, Set Version v2.7)`. If the vault Set Version moved before Phase 3, `set_version`
takes the current value.

### Phase 3b blocks (revision 2026-10-07)

**How to apply (Phase 3b).** Same mechanics as Phase 3 (markers, reconcile, byte-for-byte): the
reconcile pass re-extracts § 5q–5v and the § 5w message from THIS file before the first edit — vault
blocks against the working tree, estimator blocks against a fresh writable clone of `main` in the
session scratchpad (deleted after the push). Replace every `<P3B-DATE>` with the Phase 3b date checked
against an external time authority (L079). **Order:** step 3b.2 applies § 5q, 5r, 5s to the vault;
step 3b.3 applies § 5t–5v to the estimator clone (§ 5t copies the vault file § 5q produced) and commits
with § 5w. The estimator blocks are pinned to their `main` at `1ddbbf9` (2026-10-06). **If their `main`
moved past it** (the owner's own work lands meanwhile), the reconcile pass applies rule § 6i to § 5u.1,
5u.2, 5u.3 and 5v.1 only — version numbers and date — and records each substitution as a named reconcile
delta shown to the operator with the commit gate; any other mismatch (§ 5u.4, § 5v.2, the § 5t
pre-image) is a plan defect.

<!-- §5b-GENERATED:BEGIN -->
### 5q — `scripts/claude_project_data.sh` (vault) — 0.2 → 0.3: F1 + F2 + the `cleanup` verb — WHOLE-FILE REPLACE
<!-- block id=5q repo=vault path=scripts/claude_project_data.sh kind=whole pre_blob=4e3d1f020d730277012cac3c0e7324945564d56f -->
**5q** — the live file must hash to `4e3d1f020d730277012cac3c0e7324945564d56f` (`git hash-object`); replace its whole content with:

```text
#!/usr/bin/env bash
# ==============================================================
# VERSION: 0.3
# Claude project-data locality tool (CLAUDE.md Rule 14) — keeps the Claude Code
# per-project data (memory + session transcripts) physically INSIDE the project
# folder at <repo>/.claude/project-data/, with a link left at the harness path
# ~/.claude/projects/<path-key>/ so Claude Code keeps working unchanged — a
# symlink on macOS / Linux, a directory junction on Windows (Git Bash).
#
# Usage:
#   bash scripts/claude_project_data.sh status   # report physical home + link health
#   bash scripts/claude_project_data.sh adopt    # one-time on a machine that already has
#                                                # data under ~/.claude: move it in + link
#   bash scripts/claude_project_data.sh link     # new machine, or after a folder move/rename:
#                                                # (re)point the harness path at the in-repo data,
#                                                # merging any stray harness-created dir first
#   bash scripts/claude_project_data.sh cleanup  # remove this project's backups — each only when
#                                                # every file in it is also in the project folder
#
# The <path-key> is the repo's absolute path with every non-alphanumeric
# character replaced by "-" (Claude Code's own convention), so it changes
# whenever the folder moves — run `link` after any move/rename. On Windows the
# key is built from the drive form of the path (e:/dir/repo, drive lowercased).
#
# Never move, rename or delete the harness path in a file manager: it is a link, and
# Windows Explorer moves or deletes the real files behind a junction. Use this script.
#
# Windows (Git Bash): run `adopt` / `link` from a Git Bash window with Claude Code
# CLOSED for this project (a live session holds files in the harness dir; the tool
# refuses while a transcript changed in the last 2 minutes). There the harness dir is
# renamed to a backup in ~/.claude/locality-backups/ (<key>.pre-locality-<stamp>) —
# away from the link, on the same drive — its files are copied into the in-repo home
# without overwriting, and a junction is created. `cleanup` removes a backup once every
# file in it is in the project folder (same bytes, or grown); it never deletes through
# a link and never uses rm -r. Junctions are removed with rmdir, never rm.
#
# CHANGE LOG
# v0.3 — <P3B-DATE> — PLAN-017 Phase 3b (a Windows adopter's lost-store incident): status
#         reports an EMPTY in-repo store as empty and says STOP instead of recommending
#         link, warns on an OK link with no memory files, and lists kept backups; Windows
#         backups go to ~/.claude/locality-backups/ instead of beside the link; adopt/link
#         warn never to handle the link in a file manager; new `cleanup` verb removes a
#         backup only when every file in it is in the store (verified file by file, never
#         rm -r, never through a link) and moves a kept old-location backup away from the link.
# v0.2 — 2026-10-05 — PLAN-017: Windows (Git Bash) support — drive-form path-key, directory
#         junction (mklink /J) in place of the symlink, junctions removed with rmdir (never
#         rm), rename-to-backup + no-overwrite copy in place of mv, refusal while a session
#         is live. An adopter's E002: the merge recurses into same-name dirs and drops the
#         empty ones Claude Code creates (link/adopt no longer abort on its empty memory/);
#         status names `link`, not `adopt`, when in-repo data already exists; link absorbs
#         the pre-v1.5 memory layout too.
# v0.1 — 2026-08-16 — Initial for this suite (PLAN-010 upstream intake): ported from an
#         upstream project's locality tool; added the pre-v1.5 memory-symlink layout
#         branch in adopt() (absorbs a harness dir whose memory/ entry symlinks to
#         <repo>/.claude/memory — the old Rule 14 mechanism). Replaces bootstrap_memory.sh.
# ==============================================================
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$REPO/.claude/project-data"

case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) WINDOWS=1; LINKWORD="junction" ;;
  *) WINDOWS=0; LINKWORD="symlink" ;;
esac

if [ "$WINDOWS" = 1 ]; then
  WINPATH="$(cygpath -m "$REPO")"
  DRIVE="$(printf '%s' "$WINPATH" | cut -c1 | tr '[:upper:]' '[:lower:]')"
  KEY="$(printf '%s%s' "$DRIVE" "$(printf '%s' "$WINPATH" | cut -c2-)" | sed 's#[^A-Za-z0-9]#-#g')"
else
  KEY="$(printf '%s' "$REPO" | sed 's#[^A-Za-z0-9]#-#g')"
fi
HARNESS_DIR="$HOME/.claude/projects/$KEY"
BACKUP_ROOT="$HOME/.claude/locality-backups"

say() { printf '%s\n' "$*"; }

is_link() {  # $1 is a symlink, or (Windows) a junction Git Bash may not report as one
  [ -L "$1" ] && return 0
  if [ "$WINDOWS" = 1 ] && [ -e "$1" ]; then
    [ "$(readlink -f "$1")" != "$(readlink -f "$(dirname "$1")")/$(basename "$1")" ]
    return
  fi
  return 1
}

link_target() {
  if [ "$WINDOWS" = 1 ]; then readlink -f "$1"; else readlink "$1"; fi
}

points_home() {  # the link at $1 resolves to this repo's project-data
  if [ "$WINDOWS" = 1 ]; then
    [ -d "$DATA" ] && [ "$(readlink -f "$1")" = "$(readlink -f "$DATA")" ]
  else
    [ "$(readlink "$1")" = "$DATA" ] && [ -d "$DATA" ]
  fi
}

has_files() {  # dir $1 exists and holds at least one file
  [ -d "$1" ] && [ -n "$(find "$1" -type f 2>/dev/null | head -n 1 || true)" ]
}

mem_count() {  # number of entries in $1/memory (0 when absent)
  { ls -1 "$1/memory" 2>/dev/null || true; } | wc -l | tr -d ' '
}

backups() {  # this project's locality backups: the backup root, then the old spot beside the link
  for b in "$BACKUP_ROOT/$KEY".pre-locality-* "$HOME/.claude/projects/$KEY".pre-locality-*; do
    if [ -e "$b" ] || [ -L "$b" ]; then printf '%s\n' "$b"; fi
  done
}

make_link() {  # harness path -> $DATA
  mkdir -p "$(dirname "$HARNESS_DIR")"
  if [ "$WINDOWS" = 1 ]; then
    cmd //c mklink //J "$(cygpath -w "$HARNESS_DIR")" "$(cygpath -w "$DATA")" >/dev/null
  else
    ln -s "$DATA" "$HARNESS_DIR"
  fi
}

drop_link() {  # remove the link at $1 — never what it points to
  if [ "$WINDOWS" = 1 ]; then
    cmd //c rmdir "$(cygpath -w "$1")" >/dev/null
  else
    rm "$1"
  fi
}

warn_link() {  # after a link is made: the one action that destroys data
  say "Note: never move, rename or delete $HARNESS_DIR in a file manager —"
  say "      it is a $LINKWORD to the project folder, and a file manager can move or delete the real files behind it."
}

status() {
  say "repo:          $REPO"
  say "path-key:      $KEY"
  say "harness path:  $HARNESS_DIR"
  say "physical home: $DATA"
  backups | while IFS= read -r b; do
    say "backup kept:   $b (once a new session shows your memories: bash scripts/claude_project_data.sh cleanup)"
  done
  if is_link "$HARNESS_DIR"; then
    say "$LINKWORD:       -> $(link_target "$HARNESS_DIR")"
    if points_home "$HARNESS_DIR"; then
      n="$(mem_count "$DATA")"
      say "STATUS: OK — data lives in the project folder ($n memory files)"
      if [ "$n" = 0 ]; then
        say "WARNING: no memory files — normal for a new project; if this project had memories before, STOP: they are not in the project folder."
      fi
    else
      say "STATUS: BROKEN — $LINKWORD does not resolve to this repo's project-data. Run: link"
      return 1
    fi
  elif [ -d "$HARNESS_DIR" ]; then
    if has_files "$DATA"; then
      say "STATUS: NOT LINKED — Claude Code created a real directory at the harness path, and in-repo data exists. Run: link"
    elif [ -d "$DATA" ]; then
      say "STATUS: NOT LINKED — the in-repo store is EMPTY (no files in .claude/project-data/); the harness directory holds $(mem_count "$HARNESS_DIR") memory files."
      say "        If this project had memories that are in neither place, STOP and recover them before running link (link would join Claude Code to an empty store). Otherwise run: link"
    else
      say "STATUS: NOT ADOPTED — real directory at the harness path (data outside the project folder). Run: adopt"
    fi
    return 1
  elif has_files "$DATA"; then
    say "STATUS: NOT LINKED — in-repo data exists but the harness path is absent (fresh machine / folder moved). Run: link"
    return 1
  elif [ -d "$DATA" ]; then
    say "STATUS: EMPTY — the in-repo store exists but holds no files, and the harness path is absent."
    say "        New project: run link. If this project had memories before, STOP and recover them first."
    return 1
  else
    say "STATUS: EMPTY — no data on either side (brand-new project on this machine). Run: link (creates the home + $LINKWORD)"
    return 1
  fi
}

merge_dir_into() {  # move the contents of real dir $1 into dir $2 without clobbering;
                    # same-name dirs merge recursively and are dropped once empty (E002)
  find "$1" -mindepth 1 -maxdepth 1 -print0 | while IFS= read -r -d '' item; do
    base="$(basename "$item")"
    dest="$2/$base"
    if [ ! -e "$dest" ] && [ ! -L "$dest" ]; then
      mv "$item" "$2/" && say "  moved: $base"
    elif [ -d "$item" ] && [ ! -L "$item" ] && [ -d "$dest" ] && [ ! -L "$dest" ]; then
      merge_dir_into "$item" "$dest"
      if rmdir "$item" 2>/dev/null; then say "  merged: $base/"; fi
    else
      say "  skip (exists at destination): $base"
    fi
  done
}

copy_missing() {  # copy every file under $1 that is absent under $2 — never overwrite
  ( cd "$1" && find . -type f -print0 ) | while IFS= read -r -d '' rel; do
    rel="${rel#./}"
    if [ -e "$2/$rel" ]; then
      say "  skip (exists at destination): $rel"
    else
      mkdir -p "$2/$(dirname "$rel")"
      cp -p "$1/$rel" "$2/$rel" || { say "  FAILED to copy: $rel"; exit 1; }
    fi
  done
}

absorb_old_memory() {  # pre-v1.5 layout (old Rule 14): $1/memory links to <repo>/.claude/memory
  if is_link "$1/memory"; then
    drop_link "$1/memory"
    if [ -d "$REPO/.claude/memory" ] && [ ! -e "$DATA/memory" ]; then
      mkdir -p "$DATA"
      mv "$REPO/.claude/memory" "$DATA/memory"
      say "  absorbed old in-repo memory store -> project-data/memory"
    elif [ -d "$REPO/.claude/memory" ]; then
      say "  note: project-data/memory already exists — the old store stays at .claude/memory; merge it by hand"
    fi
  fi
}

absorb_harness_dir() {  # bring the real dir at the harness path into $DATA; frees the path
  if [ "$WINDOWS" = 1 ]; then
    recent="$(find "$HARNESS_DIR" -maxdepth 1 -name '*.jsonl' -mmin -2 2>/dev/null | head -n 1 || true)"
    if [ -n "$recent" ]; then
      say "ABORT: a Claude Code session for this project looks active (a transcript changed in the last 2 minutes)."
      say "       Close Claude Code, then run this again from a Git Bash window."
      return 1
    fi
    mkdir -p "$BACKUP_ROOT"
    backup="$BACKUP_ROOT/$KEY.pre-locality-$(date +%Y%m%d-%H%M%S)"
    if ! mv "$HARNESS_DIR" "$backup"; then
      say "ABORT: could not move the harness dir aside (in use?) — close Claude Code and retry."
      return 1
    fi
    say "Harness dir moved aside to $backup — copying its data in (nothing is overwritten)."
    say "  (if anything below fails, restore with: mv \"$backup\" \"$HARNESS_DIR\")"
    absorb_old_memory "$backup"
    mkdir -p "$DATA"
    if ! copy_missing "$backup" "$DATA"; then
      say "ABORT: copy failed — nothing was deleted; the original is still at $backup"
      return 1
    fi
    say "  backup kept at $backup — once a NEW Claude Code session shows your memories, run: bash scripts/claude_project_data.sh cleanup"
    return 0
  fi
  absorb_old_memory "$HARNESS_DIR"
  if [ -d "$DATA" ]; then
    say "$1"
    merge_dir_into "$HARNESS_DIR" "$DATA"
    leftover="$(find "$HARNESS_DIR" -mindepth 1 | head -n 1 || true)"
    if [ -n "$leftover" ]; then
      say "ABORT: harness dir not empty after merge (name collisions above) — resolve manually."; return 1
    fi
    rmdir "$HARNESS_DIR"
  else
    mv "$HARNESS_DIR" "$DATA"
  fi
}

adopt() {
  if is_link "$HARNESS_DIR"; then
    say "Already adopted — harness path is a $LINKWORD."; status; return 0
  fi
  if [ ! -d "$HARNESS_DIR" ]; then
    say "Nothing to adopt at $HARNESS_DIR — use: link"; return 1
  fi
  mkdir -p "$REPO/.claude"
  absorb_harness_dir "In-repo home exists — merging harness dir into it:"
  make_link
  say "Adopted."; warn_link; status
}

link() {
  mkdir -p "$DATA"
  if is_link "$HARNESS_DIR"; then
    if points_home "$HARNESS_DIR"; then say "Already linked."; status; return 0; fi
    say "Re-pointing stale $LINKWORD (was -> $(link_target "$HARNESS_DIR"))"
    drop_link "$HARNESS_DIR"
  elif [ -d "$HARNESS_DIR" ]; then
    absorb_harness_dir "Harness-created dir found (session started before link) — merging it in:"
  fi
  make_link
  say "Linked."; warn_link; status
}

backup_problems() {  # print every file of backup $1 the store does not hold with the same
                     # leading bytes, and every link in it; prints nothing when all is covered
  rb="$(readlink -f "$1")"
  ( cd "$1" && find . \( -type f -o -type l \) -print0 ) | while IFS= read -r -d '' rel; do
    rel="${rel#./}"
    f="$1/$rel"
    if [ -L "$f" ]; then say "link (never followed): $rel"; continue; fi
    case "$(readlink -f "$f")" in
      "$rb"/*) ;;
      *) say "reached through a link (never followed): $rel"; continue ;;
    esac
    if [ ! -f "$DATA/$rel" ]; then say "missing from the project folder: $rel"; continue; fi
    size="$(wc -c < "$f" | tr -d ' ')"
    if ! head -c "$size" "$DATA/$rel" | cmp -s - "$f"; then
      say "differs from the project folder copy: $rel"
    fi
  done
}

remove_backup() {  # delete the files of verified backup $1, then its emptied dirs — never rm -r
  ( cd "$1" && find . -type f -print0 ) | while IFS= read -r -d '' rel; do
    rm -f -- "$1/${rel#./}"
  done
  find "$1" -depth -type d -exec rmdir {} \; 2>/dev/null || true
  if [ -e "$1" ]; then say "  partly kept (not empty after removing verified files): $1"; else say "  removed: $1"; fi
}

cleanup() {  # remove this project's locality backups, each only when fully covered by the store
  if ! status >/dev/null; then
    say "cleanup refused — status is not OK. Run: bash scripts/claude_project_data.sh status"
    return 1
  fi
  list="$(backups)"
  if [ -z "$list" ]; then say "No backups to clean up for this project."; return 0; fi
  say "Checking backups (each is removed only when every file in it is also in the project folder):"
  printf '%s\n' "$list" | while IFS= read -r b; do
    if [ -L "$b" ] || is_link "$b"; then
      say "KEPT (a link, not a backup folder — remove it by hand only after checking): $b"
      continue
    fi
    problems="$(backup_problems "$b" || true)"
    if [ -z "$problems" ]; then remove_backup "$b"; continue; fi
    say "KEPT $b — not everything in it is in the project folder:"
    printf '%s\n' "$problems" | sed 's/^/    /'
    case "$b" in
      "$HOME/.claude/projects/"*)
        mkdir -p "$BACKUP_ROOT"
        if mv "$b" "$BACKUP_ROOT/"; then
          b="$BACKUP_ROOT/$(basename "$b")"
          say "    moved away from the link to: $b"
        fi
        ;;
    esac
    say "    Copy anything you need into $DATA; this backup is a plain folder (not the link) — delete it yourself once checked."
  done
}

case "${1:-status}" in
  status)  status ;;
  adopt)   adopt ;;
  link)    link ;;
  cleanup) cleanup ;;
  *) say "Usage: $0 [status|adopt|link|cleanup]"; exit 2 ;;
esac
```

### 5r — `tests/test_claude_project_data.py` (vault) — 0.1 → 0.2: 12 new cases, 2 updated — WHOLE-FILE REPLACE
<!-- block id=5r repo=vault path=tests/test_claude_project_data.py kind=whole pre_blob=f66fc29d96bb178fe9f5585ee6c4a9ac949ff069 -->
**5r** — the live file must hash to `f66fc29d96bb178fe9f5585ee6c4a9ac949ff069` (`git hash-object`); replace its whole content with:

```text
# ==============================================================
# VERSION: 0.2
# Behavior tests for scripts/claude_project_data.sh (CLAUDE.md Rule 14 locality tool).
#
# CHANGE LOG
# v0.2 — <P3B-DATE> — PLAN-017 Phase 3b: an empty store is reported, never recommended for
#         link; Windows backups live in ~/.claude/locality-backups/ (not beside the link);
#         the new cleanup verb removes only fully covered backups, never follows a link, and
#         moves a kept old-location backup away from the link.
# v0.1 — 2026-10-05 — Initial (PLAN-017): the script runs for real against throwaway repo +
#         HOME trees — POSIX status / link / adopt, the pre-v1.5 memory layout, the E002
#         folder-move merge — and its Windows branch through stand-in uname / cygpath / cmd
#         commands (a junction is simulated by a symlink; cmd calls are logged).
# ==============================================================
"""Tests for scripts/claude_project_data.sh — run the real script in temp trees."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "claude_project_data.sh"
OLD = time.time() - 3600  # an mtime well outside the live-session window

pytestmark = pytest.mark.skipif(shutil.which("bash") is None, reason="bash not available")


@dataclass
class Tree:
    repo: Path
    home: Path
    env: dict[str, str]
    log: Path | None = None

    @property
    def data(self) -> Path:
        return self.repo / ".claude" / "project-data"

    def run(self, verb: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["bash", str(self.repo / "scripts" / "claude_project_data.sh"), verb],
            env=self.env, capture_output=True, text=True, check=False,
        )

    def harness(self) -> Path:
        out = self.run("status").stdout
        match = re.search(r"^harness path:\s+(.+)$", out, re.MULTILINE)
        assert match, out
        return Path(match.group(1))


def _write(path: Path, text: str = "x", mtime: float | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if mtime is not None:
        os.utime(path, (mtime, mtime))


def _backups(tree: Tree) -> list[Path]:
    return sorted((tree.home / ".claude" / "locality-backups").glob("*.pre-locality-*"))


def _make_repo(repo: Path) -> None:
    (repo / "scripts").mkdir(parents=True)
    shutil.copy2(SCRIPT, repo / "scripts" / "claude_project_data.sh")


@pytest.fixture
def posix(tmp_path: Path) -> Tree:
    repo = tmp_path / "work" / "my repo"
    home = tmp_path / "home"
    home.mkdir()
    _make_repo(repo)
    env = {**os.environ, "HOME": str(home)}
    return Tree(repo=repo, home=home, env=env)


_SHIMS = {
    "uname": '#!/bin/bash\necho "MINGW64_NT-10.0-19045"\n',
    "cygpath": (
        "#!/bin/bash\n"
        'p="$2"; rest="${p#"$FAKE_WINROOT"/}"\n'
        '[ "$rest" != "$p" ] || exit 1\n'
        'drive="$(printf \'%s\' "${rest:0:1}" | tr \'[:lower:]\' \'[:upper:]\')"\n'
        'out="$drive:${rest:1}"\n'
        '[ "$1" = "-w" ] && out="${out//\\//\\\\}"\n'
        "printf '%s\\n' \"$out\"\n"
    ),
    "cmd": (
        "#!/bin/bash\n"
        'echo "cmd $*" >> "$SHIM_LOG"\n'
        "topath() {\n"
        '  p="${1//\\\\//}"\n'
        '  d="$(printf \'%s\' "${p:0:1}" | tr \'[:upper:]\' \'[:lower:]\')"\n'
        "  printf '%s/%s%s' \"$FAKE_WINROOT\" \"$d\" \"${p:2}\"\n"
        "}\n"
        'case "$2" in\n'
        '  mklink) ln -s "$(topath "$5")" "$(topath "$4")" ;;\n'
        '  rmdir) t="$(topath "$3")"; if [ -L "$t" ]; then rm "$t"; else rmdir "$t"; fi ;;\n'
        "  *) exit 1 ;;\n"
        "esac\n"
    ),
}


@pytest.fixture
def windows(tmp_path: Path) -> Tree:
    root = tmp_path / "win"
    repo = root / "e" / "Work_Area" / "demo-repo"
    home = root / "c" / "Users" / "someone"
    home.mkdir(parents=True)
    _make_repo(repo)
    shims = tmp_path / "shims"
    shims.mkdir()
    for name, body in _SHIMS.items():
        (shims / name).write_text(body, encoding="utf-8")
        (shims / name).chmod(0o755)
    log = tmp_path / "cmd.log"
    log.touch()
    env = {
        **os.environ, "HOME": str(home), "PATH": f"{shims}{os.pathsep}{os.environ['PATH']}",
        "FAKE_WINROOT": str(root), "SHIM_LOG": str(log),
    }
    return Tree(repo=repo, home=home, env=env, log=log)


# ---- POSIX (macOS / Linux) -------------------------------------------------


def test_posix_empty_then_link_is_idempotent(posix: Tree) -> None:
    first = posix.run("status")
    assert first.returncode == 1 and "STATUS: EMPTY" in first.stdout
    linked = posix.run("link")
    assert linked.returncode == 0 and "STATUS: OK" in linked.stdout
    harness = posix.harness()
    assert harness.is_symlink() and os.readlink(harness) == str(posix.data)
    again = posix.run("link")
    assert again.returncode == 0 and "Already linked." in again.stdout


def test_posix_adopt_moves_harness_data_in(posix: Tree) -> None:
    harness = posix.harness()
    _write(harness / "memory" / "a.md")
    _write(harness / "s1.jsonl")
    assert "Run: adopt" in posix.run("status").stdout
    out = posix.run("adopt")
    assert out.returncode == 0 and "STATUS: OK" in out.stdout
    assert (posix.data / "memory" / "a.md").is_file() and (posix.data / "s1.jsonl").is_file()
    assert harness.is_symlink()


def test_posix_adopt_absorbs_pre_v15_memory_layout(posix: Tree) -> None:
    old_store = posix.repo / ".claude" / "memory"
    _write(old_store / "a.md")
    _write(old_store / "b.md")
    harness = posix.harness()
    harness.mkdir(parents=True)
    (harness / "memory").symlink_to(old_store)
    _write(harness / "s1.jsonl")
    out = posix.run("adopt")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "absorbed old in-repo memory store" in out.stdout
    assert "(2 memory files)" in out.stdout
    assert not old_store.exists() and (posix.data / "s1.jsonl").is_file()


def test_posix_e002_folder_move_merges_harness_created_dir(posix: Tree) -> None:
    for name in ("a.md", "b.md", "c.md"):
        _write(posix.data / "memory" / name)
    harness = posix.harness()
    (harness / "memory").mkdir(parents=True)  # what Claude Code creates on session start
    _write(harness / "new.jsonl")
    status = posix.run("status")
    assert status.returncode == 1 and "Run: link" in status.stdout and "adopt" not in status.stdout
    out = posix.run("link")
    assert out.returncode == 0 and "(3 memory files)" in out.stdout, out.stdout
    assert (posix.data / "new.jsonl").is_file() and harness.is_symlink()


def test_posix_merge_recurses_into_same_name_dirs(posix: Tree) -> None:
    _write(posix.data / "memory" / "a.md")
    harness = posix.harness()
    _write(harness / "memory" / "c.md")
    out = posix.run("link")
    assert out.returncode == 0, out.stdout
    assert sorted(p.name for p in (posix.data / "memory").iterdir()) == ["a.md", "c.md"]


def test_posix_file_collision_still_aborts_without_loss(posix: Tree) -> None:
    _write(posix.data / "f.txt", "in-repo")
    harness = posix.harness()
    _write(harness / "f.txt", "harness")
    out = posix.run("link")
    assert out.returncode == 1 and "ABORT" in out.stdout
    assert (posix.data / "f.txt").read_text(encoding="utf-8") == "in-repo"
    assert (harness / "f.txt").read_text(encoding="utf-8") == "harness"


def test_posix_stale_symlink_is_repointed(posix: Tree, tmp_path: Path) -> None:
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    posix.data.mkdir(parents=True)
    harness = posix.harness()
    harness.parent.mkdir(parents=True)
    harness.symlink_to(elsewhere)
    assert "STATUS: BROKEN" in posix.run("status").stdout
    out = posix.run("link")
    assert out.returncode == 0 and "Re-pointing stale symlink" in out.stdout
    assert os.readlink(harness) == str(posix.data)


def test_posix_empty_store_is_reported_not_recommended(posix: Tree) -> None:
    posix.data.mkdir(parents=True)  # the store exists but its files are gone
    harness = posix.harness()
    (harness / "memory").mkdir(parents=True)  # what Claude Code creates on session start
    out = posix.run("status")
    assert out.returncode == 1, out.stdout
    assert "in-repo store is EMPTY" in out.stdout and "STOP" in out.stdout
    assert "holds 0 memory files" in out.stdout
    assert "in-repo data exists" not in out.stdout


def test_posix_empty_store_without_harness_says_stop(posix: Tree) -> None:
    posix.data.mkdir(parents=True)
    out = posix.run("status")
    assert out.returncode == 1
    assert "STATUS: EMPTY — the in-repo store exists but holds no files" in out.stdout
    assert "STOP" in out.stdout and "in-repo data exists" not in out.stdout


def test_posix_ok_with_no_memory_files_warns(posix: Tree) -> None:
    linked = posix.run("link")
    assert linked.returncode == 0 and "never move, rename or delete" in linked.stdout
    out = posix.run("status")
    assert out.returncode == 0 and "(0 memory files)" in out.stdout
    assert "WARNING: no memory files" in out.stdout
    _write(posix.data / "memory" / "a.md")
    again = posix.run("status")
    assert "(1 memory files)" in again.stdout and "WARNING" not in again.stdout


def test_posix_cleanup_with_no_backups_is_a_no_op(posix: Tree) -> None:
    assert posix.run("link").returncode == 0
    out = posix.run("cleanup")
    assert out.returncode == 0 and "No backups to clean up" in out.stdout


def test_cleanup_refused_unless_status_is_ok(posix: Tree) -> None:
    harness = posix.harness()
    _write(harness / "s.jsonl")  # data still outside the project folder: not adopted
    backup = posix.home / ".claude" / "locality-backups" / f"{harness.name}.pre-locality-1"
    _write(backup / "s.jsonl")
    assert f"backup kept:   {backup}" in posix.run("status").stdout
    out = posix.run("cleanup")
    assert out.returncode == 1 and "cleanup refused" in out.stdout
    assert (backup / "s.jsonl").is_file()


# ---- Windows (Git Bash) through stand-in uname / cygpath / cmd ---------------


def test_windows_path_key_uses_the_lowercased_drive_form(windows: Tree) -> None:
    out = windows.run("status").stdout
    assert re.search(r"^path-key:\s+e--Work-Area-demo-repo$", out, re.MULTILINE), out
    expected = windows.home / ".claude" / "projects" / "e--Work-Area-demo-repo"
    assert windows.harness() == expected


def test_windows_adopt_migrates_the_old_junction_layout(windows: Tree) -> None:
    old_store = windows.repo / ".claude" / "memory"
    _write(old_store / "m1.md", mtime=OLD)
    _write(old_store / "m2.md", mtime=OLD)
    harness = windows.harness()
    harness.mkdir(parents=True)
    (harness / "memory").symlink_to(old_store)  # bootstrap_memory.sh's junction
    _write(harness / "old.jsonl", "transcript", mtime=OLD)
    out = windows.run("adopt")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "STATUS: OK" in out.stdout and "(2 memory files)" in out.stdout
    assert harness.is_symlink() and harness.resolve() == windows.data.resolve()
    assert (windows.data / "old.jsonl").read_text(encoding="utf-8") == "transcript"
    assert not list(harness.parent.glob(f"{harness.name}.pre-locality-*"))  # not beside the link
    backups = _backups(windows)
    assert len(backups) == 1 and (backups[0] / "old.jsonl").is_file()
    assert windows.log is not None
    calls = windows.log.read_text(encoding="utf-8")
    assert "cmd //c rmdir " in calls and "\\memory" in calls  # junction dropped via rmdir
    assert "cmd //c mklink //J " in calls


def test_windows_refuses_while_a_session_is_live(windows: Tree) -> None:
    harness = windows.harness()
    _write(harness / "live.jsonl")  # mtime = now
    out = windows.run("adopt")
    assert out.returncode == 1 and "looks active" in out.stdout
    assert harness.is_dir() and not harness.is_symlink()
    assert not list(harness.parent.glob(f"{harness.name}.pre-locality-*"))
    assert _backups(windows) == []


def test_windows_e002_link_after_move_keeps_memories(windows: Tree) -> None:
    for name in ("a.md", "b.md"):
        _write(windows.data / "memory" / name)
    harness = windows.harness()
    (harness / "memory").mkdir(parents=True)
    _write(harness / "s.jsonl", mtime=OLD)
    assert "Run: link" in windows.run("status").stdout
    out = windows.run("link")
    assert out.returncode == 0 and "(2 memory files)" in out.stdout, out.stdout + out.stderr
    assert (windows.data / "s.jsonl").is_file()
    again = windows.run("link")
    assert again.returncode == 0 and "Already linked." in again.stdout
    assert "junction:" in again.stdout


def _adopt_with_session(windows: Tree) -> Path:
    harness = windows.harness()
    _write(harness / "memory" / "m1.md", "memory one", mtime=OLD)
    _write(harness / "s1.jsonl", "line1\n", mtime=OLD)
    out = windows.run("adopt")
    assert out.returncode == 0, out.stdout + out.stderr
    return harness


def test_windows_backup_goes_to_the_backup_root_not_beside_the_link(windows: Tree) -> None:
    harness = _adopt_with_session(windows)
    assert harness.is_symlink()
    assert not list(harness.parent.glob(f"{harness.name}.pre-locality-*"))
    backups = _backups(windows)
    assert len(backups) == 1 and (backups[0] / "s1.jsonl").is_file()
    assert f"backup kept:   {backups[0]}" in windows.run("status").stdout


def test_windows_adopt_output_points_to_cleanup_not_to_deleting(windows: Tree) -> None:
    harness = windows.harness()
    _write(harness / "s1.jsonl", mtime=OLD)
    out = windows.run("adopt").stdout
    assert "bash scripts/claude_project_data.sh cleanup" in out
    assert "delete it once" not in out
    assert "never move, rename or delete" in out


def test_windows_cleanup_removes_a_fully_covered_backup(windows: Tree) -> None:
    harness = _adopt_with_session(windows)
    with (windows.data / "s1.jsonl").open("a", encoding="utf-8") as fh:
        fh.write("line2\n")  # the resumed session grew its transcript
    out = windows.run("cleanup")
    assert out.returncode == 0 and "removed:" in out.stdout, out.stdout + out.stderr
    assert _backups(windows) == []
    assert (windows.data / "memory" / "m1.md").read_text(encoding="utf-8") == "memory one"
    assert (windows.data / "s1.jsonl").read_text(encoding="utf-8") == "line1\nline2\n"
    assert harness.is_symlink()


def test_windows_cleanup_keeps_a_backup_the_store_does_not_cover(windows: Tree) -> None:
    _adopt_with_session(windows)
    (windows.data / "memory" / "m1.md").unlink()  # the store lost a file the backup still has
    _write(windows.data / "s1.jsonl", "rewritten\n")  # and holds other bytes for another
    out = windows.run("cleanup")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "KEPT" in out.stdout
    assert "missing from the project folder: memory/m1.md" in out.stdout
    assert "differs from the project folder copy: s1.jsonl" in out.stdout
    backups = _backups(windows)
    assert len(backups) == 1 and (backups[0] / "memory" / "m1.md").is_file()


def test_cleanup_never_follows_a_link_inside_a_backup(windows: Tree) -> None:
    harness = _adopt_with_session(windows)
    trap = harness.parent / f"{harness.name}.pre-locality-20261006-093516"  # the v0.2 spot
    trap.mkdir()
    (trap / "memory").symlink_to(windows.data / "memory")  # a junction into the real store
    out = windows.run("cleanup")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "link (never followed): memory" in out.stdout
    assert (windows.data / "memory" / "m1.md").read_text(encoding="utf-8") == "memory one"
    assert not (windows.data / "memory").is_symlink()
    moved = windows.home / ".claude" / "locality-backups" / trap.name
    assert not trap.exists() and (moved / "memory").is_symlink()


def test_cleanup_keeps_a_backup_entry_that_is_itself_a_link(windows: Tree) -> None:
    harness = _adopt_with_session(windows)
    fake = harness.parent / f"{harness.name}.pre-locality-20261006-000000"
    fake.symlink_to(windows.data)  # what renaming a mis-detected junction would leave
    out = windows.run("cleanup")
    assert out.returncode == 0 and "KEPT (a link" in out.stdout, out.stdout + out.stderr
    assert fake.is_symlink() and (windows.data / "memory" / "m1.md").is_file()


def test_cleanup_handles_backups_left_beside_the_link_by_v02(windows: Tree) -> None:
    harness = _adopt_with_session(windows)
    covered = harness.parent / f"{harness.name}.pre-locality-20261006-093516"
    _write(covered / "s1.jsonl", "line1\n")
    unique = harness.parent / f"{harness.name}.pre-locality-20261006-101010"
    _write(unique / "only-here.jsonl", "unique")
    out = windows.run("cleanup")
    assert out.returncode == 0, out.stdout + out.stderr
    assert not covered.exists() and not unique.exists()
    assert "moved away from the link" in out.stdout
    moved = windows.home / ".claude" / "locality-backups" / unique.name
    assert (moved / "only-here.jsonl").read_text(encoding="utf-8") == "unique"
    assert [b.name for b in _backups(windows)] == [unique.name]
```

### 5s — `docs/folder_structure.md` (vault) — 0.16 → 0.17: the tool line names `cleanup`
<!-- block id=5s.1 repo=vault path=docs/folder_structure.md kind=replace -->
**5s.1** FIND:

```text
<!-- VERSION: 0.16 -->
<!-- Last Updated: 2026-10-05 -->
<!--
CHANGE LOG
```

REPLACE WITH:

```text
<!-- VERSION: 0.17 -->
<!-- Last Updated: <P3B-DATE> -->
<!--
CHANGE LOG
v0.17 — <P3B-DATE> — PLAN-017 Phase 3b: the claude_project_data.sh line names the new `cleanup` verb.
```

<!-- block id=5s.2 repo=vault path=docs/folder_structure.md kind=replace -->
**5s.2** FIND:

```text
│   ├── claude_project_data.sh    # Rule 14 project-data locality tool (status / adopt / link; symlink, or a junction on Windows)
```

REPLACE WITH:

```text
│   ├── claude_project_data.sh    # Rule 14 project-data locality tool (status / adopt / link / cleanup; symlink, or a junction on Windows)
```

### 5t — `scripts/claude_project_data.sh` (estimator) — 0.2 → 0.3: byte-identical copy of the vault file after § 5q
<!-- block id=5t repo=estimator path=scripts/claude_project_data.sh kind=copy source=scripts/claude_project_data.sh pre_blob=4e3d1f020d730277012cac3c0e7324945564d56f -->
**5t** — their live file must hash to `4e3d1f020d730277012cac3c0e7324945564d56f` (the 0.2 copy § 5k delivered — never edited there); copy `scripts/claude_project_data.sh` from the vault (after § 5q, date substituted) byte-for-byte, mode 100755; `cmp` must exit 0.

### 5u — `docs/documents_manifest.md` (estimator) — 1.58 → 1.59: cells + the script row
<!-- block id=5u.1 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5u.1** FIND:

```text
<!-- VERSION: 1.58 -->
<!-- Last Updated: 2026-10-06 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.59 -->
<!-- Last Updated: <P3B-DATE> -->
```

<!-- block id=5u.2 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5u.2** FIND:

```text
| `CHANGELOG.md` | 1.41 | Cross-cutting history. |
```

REPLACE WITH:

```text
| `CHANGELOG.md` | 1.42 | Cross-cutting history. |
```

<!-- block id=5u.3 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5u.3** FIND:

```text
| `docs/documents_manifest.md` | 1.58 | This version index (critical). |
```

REPLACE WITH:

```text
| `docs/documents_manifest.md` | 1.59 | This version index (critical). |
```

<!-- block id=5u.4 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5u.4** FIND:

```text
| `scripts/claude_project_data.sh` | 0.2 | Project-data locality tool (Rule 14, Standard Set v1.5+): memory + session transcripts live in `.claude/project-data/`, linked from Claude Code's harness path — a symlink on macOS / Linux, a directory junction on Windows (Git Bash). Copied verbatim from the Standard DocSet vault (Standard DocSet PLAN-017); replaces `bootstrap_memory.sh` once `adopt` has run. |
```

REPLACE WITH:

```text
| `scripts/claude_project_data.sh` | 0.3 | Project-data locality tool (Rule 14, Standard Set v1.5+): memory + session transcripts live in `.claude/project-data/`, linked from Claude Code's harness path — a symlink on macOS / Linux, a directory junction on Windows (Git Bash). Copied verbatim from the Standard DocSet vault (Standard DocSet PLAN-017); `cleanup` removes its backups safely. Never move or delete the harness link by hand. |
```

### 5v — `CHANGELOG.md` (estimator) — 1.41 → 1.42: header + the delivery entry
<!-- block id=5v.1 repo=estimator path=CHANGELOG.md kind=replace -->
**5v.1** FIND:

```text
<!-- VERSION: 1.41 -->
<!-- Last Updated: 2026-10-06 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.42 -->
<!-- Last Updated: <P3B-DATE> -->
```

<!-- block id=5v.2 repo=estimator path=CHANGELOG.md kind=replace -->
**5v.2** FIND:

```text
All notable changes to `780-estimator`. Newest at the top. Each entry states an explicit impact.

```

REPLACE WITH:

```text
All notable changes to `780-estimator`. Newest at the top. Each entry states an explicit impact.

## <P3B-DATE> — Locality tool 0.3 from the Standard DocSet vault: safer backups + `cleanup`

**Impact: one governance script only — no forecasting, evaluation, publication, test or runtime
behavior changes.** `scripts/claude_project_data.sh` 0.2 → 0.3, copied verbatim from the Standard
DocSet vault (Standard DocSet PLAN-017 Phase 3b). Do not edit it here; report problems as an entry in
`docs/STANDARDS_LOG.md`.

Why: on 2026-10-06 the project-data store was emptied when the harness link
(`C:\Users\<you>\.claude\projects\e--…-780-estimator`) was moved in Explorer — Explorer moves the
real files behind a junction. The files were recovered from the Recycle Bin. Version 0.3:

- `status` reports an EMPTY store as empty and says STOP instead of recommending `link`; an OK link
  with no memory files prints a warning; kept backups are listed (`backup kept:`).
- Backups made by `adopt` / `link` on Windows go to `~/.claude/locality-backups/` — no longer next to
  the link — and `adopt` / `link` end with a warning never to move, rename or delete the link in a
  file manager.
- New `bash scripts/claude_project_data.sh cleanup`: removes a backup only when every file in it is
  also in `.claude/project-data/` (same bytes, or grown); otherwise it keeps the backup, lists what
  differs, and moves a backup that sits next to the link away from it. It never deletes through a
  link.

Also: `docs/documents_manifest.md` 1.59 — the script's row (0.3) and the CHANGELOG cell.

**Next session (owner, Windows PC):**
1. `git pull`.
2. `bash scripts/claude_project_data.sh status` — expect `STATUS: OK` with 14 or more memory files
   (new sessions may add some) and, while a backup exists, a `backup kept:` line.
3. Once a new Claude Code session has shown your memories: `bash scripts/claude_project_data.sh
   cleanup`. Expected after the 2026-10-06 recovery: the backup is KEPT, listing the two transcripts
   the recovery rebuilt (the project folder holds the better copies), and it is moved to
   `~/.claude/locality-backups/` if it sat next to the link. Deleting that kept folder in Explorer is
   safe — it is a plain folder, not the link. Never touch the link itself.
4. Send the output to the curator (Standard DocSet PLAN-017 QA-M8).

**QA scenarios** (Rule 11): steps 2–3 above are this change's scenario — ⏸ until they run on the
Windows PC. The curator's side (tests, a replay of this machine's state) is recorded in Standard
DocSet PLAN-017.

```

<!-- §5b-GENERATED:END -->

### 5w — estimator delivery commit message (verbatim; `git commit -F <file>`)

```text
Ops/Governance: locality tool 0.3 from the Standard DocSet vault

scripts/claude_project_data.sh 0.2 -> 0.3, copied verbatim from the
Standard DocSet vault (Standard DocSet PLAN-017 Phase 3b) after the
2026-10-06 store loss (the harness junction was moved in Explorer; the
files were recovered from the Recycle Bin):

- status reports an empty store as empty and says STOP instead of
  recommending link; it lists kept backups.
- Windows backups go to ~/.claude/locality-backups/, not next to the
  link; adopt/link warn never to handle the link in a file manager.
- new cleanup verb: removes a backup only when the store fully covers
  it; never deletes through a link.

docs/documents_manifest.md 1.59 (script row 0.3), CHANGELOG.md 1.42
(entry with the owner's next-session steps). No runtime, domain or test
change.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
```

## 6. Spec update map (mechanical rules; same commit as the work)

- **6a — design commit (§ 7.1):** vault manifest — new rows **90** (PLAN-017 plan, 0.1 DRAFT, Plan) and
  **91** (tracker, 0.1, Plan); self-row 5; quick-index *Plans* `31–39, 59–60, 63–64, 68–71, 74–75` →
  `31–39, 59–60, 63–64, 68–71, 74–75, 80–87, 90–91` (90–91 new; 80–87 = the OPEN_TASKS deferred minor on
  the same line, ridden along and recorded); header + CHANGE LOG + Last-updated rotation. CHANGELOG top
  entry (plan drafted; no runtime impact).
- **6b — Phase 2 approval commit:** plan + tracker 0.1 → 0.2 APPROVED with the § 9.1 decision record;
  manifest cells 90–91; CHANGELOG line (the PLAN-016 approval-commit precedent).
- **6c — Phase 3 vault commit (§ 7.5):** manifest — row **56** 0.1 → 0.2; new row **92**
  `tests/test_claude_project_data.py` (0.1, "Project-data locality script test", category
  `Governance script test`) + quick-index *Governance scripts* `28–29, 56` → `28–29, 56, 92`; cells **6** → 0.16, **8** → 1.21,
  **76** → 0.2, **64** → 1.1 (6d), **90 / 91** → the plan / tracker headers; self-row; files without a
  VERSION header (`config/projects.toml`, `scripts/validation_ownership.toml`) have no row — say so in
  the CHANGE LOG line; grep-verify every touched cell == its file header (L063). CHANGELOG top entry:
  what shipped, the estimator commits (shas), the impact statement ("the vault's own locality tool
  changes; no engine change; one target written by git, one by integrate"), and a **QA scenarios**
  sub-section listing QA-M1…M10 with status.
- **6d — PLAN-007 tracker post-close annotation (v1.1):** the git-transport half of QA K–N is closed
  by the first live git read + write (QA-M5 evidence) — the PLAN-013 v1.1 post-close precedent.
- **6e — plan + tracker:** → 0.3 EXECUTING in the Phase 3 commit (Phase 4 Windows QA open); Phase 3b:
  0.4 revision DRAFT → 0.5 APPROVED (§ 7.8) → 0.6 EXECUTING (§ 7.9); → 1.0 / CLOSED in the closure commit.
- **6f — closure commit (§ 7.6):** registry `lifecycle` → `active` (FIND `plan = "PLAN-017"` +
  `lifecycle = "onboarding"` → `lifecycle = "active"`), then `fleet`; manifest cells; CHANGELOG
  (QA-M8 / M9 evidence); plan + tracker 1.0.
- **6g — `docs/Plans/OPEN_TASKS.md`** (local, never committed): next actions + the v2.8 queue items
  from the § 2 gate.
- **6h — Phase 3b vault bookkeeping (the § 7.9 commit):** manifest — header + Last-updated block +
  change log line; cells **56** (tool) → 0.3, **92** (tests) → 0.2, **6** (folder_structure) → 0.17,
  **90 / 91** → the plan / tracker headers; self-row; grep-verify every touched cell == its file header
  (L063). CHANGELOG top entry: tool 0.3 (F1 / F2), the estimator delivery commit sha, the impact
  statement ("the vault's own locality tool gains a `cleanup` verb and safer messages; no engine change;
  one target written by a curator commit"), and a **QA scenarios** sub-section listing QA-M11…M16 + the
  QA-M8 re-run with status. Plan + tracker → 0.6 EXECUTING (Phase 3b done; QA-M8 open).
- **6i — the estimator moved past `1ddbbf9` (reconcile rule for § 5u.1–5u.3 / § 5v.1):** read the live
  `<!-- VERSION: X.YY -->` of their `docs/documents_manifest.md` and `CHANGELOG.md`; the new values are the
  next minor bump of each (X.YY + 0.01); § 5u.2's CHANGELOG cell and § 5u.3's self-row take the same two
  values; the dates take `<P3B-DATE>`. The rendered blocks go to the operator with the commit gate, and
  the owner is told the two numbers the delivery took (their in-flight work re-bases past them — R15).
- No engine source changes → `docs/architecture.md` untouched (§ 4 drift rule not triggered); no new
  top-level directory.

## 7. ALLOWLIST (the bullet enumeration IS the count — L038; plan + tracker included per L054)

### 7.1 Design commit (vault; 4 files)

- `docs/Plans/PLAN-017_estimator_catchup.md` (new)
- `docs/Plans/PLAN-017_tracker.md` (new)
- `docs/documents_manifest.md`
- `CHANGELOG.md`

### 7.2 Estimator prep commit (curator; 7 files)

- `docs/SESSION_OPENER.md`
- `docs/SESSION_CLOSER.md`
- `docs/SET_VERSION_ADOPTED.md`
- `scripts/claude_project_data.sh` (new)
- `docs/documents_manifest.md`
- `docs/folder_structure.md`
- `CHANGELOG.md`

### 7.3 Estimator sync commit (engine-made; 8 files — verify with `git show --stat`)

- `CLAUDE.md`
- `docs/standards/PROJECT_STANDARDS.md`
- `docs/standards/MEMORY_PROTOCOL.md`
- `archive/LESSONS.md`
- `docs/SESSION_OPENER.md`
- `docs/SESSION_CLOSER.md`
- `docs/SET_VERSION_ADOPTED.md`
- `docs/SYNC_HANDOFF.md` (new)

### 7.4 Capital-Signal write-back (engine-made, uncommitted in CS; 2 files)

- `docs/STANDARDS_LOG.md`
- `docs/SYNC_HANDOFF.md`

### 7.5 Phase 3 vault commit (12 files)

- `scripts/claude_project_data.sh`
- `tests/test_claude_project_data.py` (new)
- `scripts/validation_ownership.toml`
- `config/projects.toml`
- `docs/SESSION_OPENER.md`
- `skill/SKILL.md`
- `docs/folder_structure.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-007_tracker.md`
- `docs/Plans/PLAN-017_estimator_catchup.md`
- `docs/Plans/PLAN-017_tracker.md`

### 7.6 Closure commit (vault; 5 files)

- `config/projects.toml`
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-017_estimator_catchup.md`
- `docs/Plans/PLAN-017_tracker.md`

### 7.7 Phase 3b revision commit (vault; 4 files)

- `docs/Plans/PLAN-017_estimator_catchup.md`
- `docs/Plans/PLAN-017_tracker.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`

### 7.8 Phase 3b approval commit (vault; 4 files)

- `docs/Plans/PLAN-017_estimator_catchup.md`
- `docs/Plans/PLAN-017_tracker.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`

### 7.9 Phase 3b vault commit (7 files)

- `scripts/claude_project_data.sh`
- `tests/test_claude_project_data.py`
- `docs/folder_structure.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-017_estimator_catchup.md`
- `docs/Plans/PLAN-017_tracker.md`

### 7.10 Estimator delivery commit (curator; 3 files)

- `scripts/claude_project_data.sh`
- `docs/documents_manifest.md`
- `CHANGELOG.md`

## 8. Validation gate (Rule 11 scenarios; Rule 15 feature-ON marked ⚑; status in the tracker)

- **QA-M1 — tools (3.2).** `ruff check src tests` clean; `MYPYPATH=src mypy --cache-dir <fresh>` 0
  issues in 25 files; pytest **151** passed (140 + 11).
- **QA-M2 — the tests exercise the new code (3.2).** The 11 new tests run against tool 0.1 (copied
  into a scratch copy) fail exactly the 6 new-behavior cases (2 E002, 4 Windows) and pass the 5
  baseline cases — a green run proves nothing unless it can go red.
- **QA-M3 ⚑ — the vault's own locality (3.2).** With 0.2 in place: `bash
  scripts/claude_project_data.sh status` → `STATUS: OK` with the pre-change memory count (macOS
  regression on the live store).
- **QA-M4 ⚑ — prep proof (3.3, before the commit).** On the prepared estimator clone: its own
  governance scripts exit 0 (output pasted); engine-as-oracle through a scratch vault whose registry
  points at the clone (local transport): `status` v1.3 / v2.7 behind; dry-run 7 of 11; the
  removed-lines set == § 8.1.
- **QA-M5 ⚑ — the first live git write (3.4).** Live GitHub: `status` → 780-estimator v1.3 / v2.7
  behind (git read path); dry-run 7 / 11 + `--diff` removed lines == § 8.1; `sync --project
  780-estimator --write` → "wrote + flushed 8 file(s)"; `git ls-remote` main = the engine commit and
  its parent = the prep commit; `git show --stat` == § 7.3; re-run → up-to-date 11/11; `status` → v2.7
  current; `docs/fleet.csv` row: registry columns == § 5d (date substituted), `reachable` yes,
  `handoff_pending` 1.
- **QA-M6 ⚑ — post-sync integrity (3.4).** In a fresh clone of `main`: PROJECT-OWNED counts CLAUDE 4 /
  opener 3 / closer 2 (BEGIN == END); 15 `### Rule` headings; Rule 14 names
  `scripts/claude_project_data.sh` and the file exists; the opener heading + § 2 "Current state" note
  intact; SVA bullets read v2.7 with rows v2.7 + v1.3.
- **QA-M7 ⚑ — E002 write-back (3.5).** Capital-Signal idle (no transcript in its project-data changed
  in the last 10 minutes; operator confirms no session there); `integrate --apply` dry-run → `--write`;
  the Status line read back verbatim == § 5p's rendering; Capital-Signal's `docs/SYNC_HANDOFF.md`
  ends with a `### Write` record for this write-back (a new handoff if it held none); `harvest` → no
  open Capital-Signal entries.
- **QA-M8 ⚑ — Windows verification (owner's PC; operator-relayed evidence).** Before: the
  `.claude/memory` file count N. In a session: `status` → `NOT ADOPTED`; `adopt` there → refused
  ("looks active"). Claude Code closed, Git Bash: `adopt` → "Adopted." + `STATUS: OK (N memory
  files)`; `cmd //c dir "%USERPROFILE%\.claude\projects"` lists the key as `<JUNCTION>`; Claude Code
  reopened → a fresh session's `status` OK and it recalls a known memory; `link` → "Already linked.".
  Ship-gating (Rule 15) — waivable only by the operator, recorded in the tracker.
- **QA-M9 ⚑ — landing observed.** On their `main`: a commit deleting `docs/SYNC_HANDOFF.md` with the
  manifest cells + a CHANGELOG entry; `scripts/bootstrap_memory.sh` removed with its manifest row +
  tree line (D-1 = A); vault `status` / `fleet` → current, `handoff_pending` 0.
- **QA-M10 — domain-neutral gate (3.2).** `grep -rniE "780|estimator|everon|equinex|capital-signal|bahereh|parsaazad|a780" skill/ docs/standards/ scripts/claude_project_data.sh tests/test_claude_project_data.py`
  prints nothing (exit 1) — the tool is copied verbatim into every adopter, so it is held to the
  suite's rule.

### 8.1 Expected removed lines (catch-up dry-run `--diff`, after the prep; header lines aside)

- `CLAUDE.md` (28 lines): the "13 standing rules" heading + § 13 bullet; the Rule 5 local-checks
  wording and the § 8.6 YAML example (template v2.4 runner note); Rule 12 step 6 title; the whole old
  Rule 14 (`.claude/memory` + `bootstrap_memory.sh`); **the § 10 "Ask in plain chat — never via a
  popup" bullet** (accepted, § 2 #3); the § 15.2 Phase 0 / Phase 1 rows and the § 15.3 ambiguity
  sentence (template v2.7 / L056 wording).
- `docs/SESSION_OPENER.md` (19 lines incl. its VERSION line): the two `origin/main` § 1.1 commands +
  "Branch convention for this project: `main`."; the old § 1.5 memory-link block; § 3.1 rows 14 / 15
  (renumbered upstream); three § 4 template lines; the freshly-bootstrapped trailer.
- `docs/SESSION_CLOSER.md` (6 lines incl. its VERSION line): the `origin/main` command + branch line;
  the Set-Version bullet; the § 1.6 title; the trailer.
- `docs/SET_VERSION_ADOPTED.md` (3 lines): its VERSION line and the two bullets (rewritten to v2.7).

If the engine's run date differs from `<P3-DATE>` (a session crossing midnight), each of the opener,
closer and SVA also loses its `Last Updated` line (+1 each) — nothing else may differ. Anything else in
the removed set ⇒ STOP and investigate before writing (the 2026-09-05 discard finding: a delta wider
than the oracle is a defect until explained).

Replace-mode files (the six `docs/standards/` files and `archive/LESSONS.md`) sit outside this list: their
removed lines are header lines plus canonical evolution PROVIDED each target copy is byte-identical to the
vault's tag for the version it adopted — check that blob match (D1, Phase 3: the estimator's three changed
replace-mode files matched `set-v1.3`; MEMORY_PROTOCOL's 3 non-header lines are the v2.2 identifier scrub).

### 8.2 Phase 3b scenarios (revision 2026-10-07)

- **QA-M11 — tools (3b.2).** `ruff check src tests` clean; `MYPYPATH=src mypy --cache-dir <fresh> src
  tests` 0 issues in 25 files; `bash -n scripts/claude_project_data.sh` clean; pytest **163** (151 + 12).
- **QA-M12 — the new tests exercise the new code (3b.2).** Tests 0.2 against tool 0.2 (a scratch copy of
  the § 5q pre-image) → **13 failed / 10 passed**: the 12 new tests and the updated adopt test fail, the
  10 unchanged tests pass.
- **QA-M13 ⚑ — the vault's own locality (3b.2, macOS live).** `status` → `STATUS: OK … (N memory files)`
  with N the pre-change count, no `WARNING`, no `backup kept:` line; `cleanup` → "No backups to clean up
  for this project." exit 0; the count unchanged.
- **QA-M14 ⚑ — replay of the owner's post-incident state (3b.2, scratch, Windows stand-ins).** The store
  holds two memories, a re-assembled transcript (both halves) and a recovered transcript; the harness is a
  plain dir holding the second half, a title stub and a later session. Order 1 — `link` with 0.3: the
  backup lands under `~/.claude/locality-backups/`, `status` OK + `backup kept:`, `cleanup` → **KEPT**,
  listing exactly the second half and the stub as "differs from the project folder copy"; nothing
  deleted. Order 2 — `link` with 0.2, then 0.3: `status` lists the old-location backup; `cleanup` →
  **KEPT** + "moved away from the link"; only the link remains for the key in `.claude/projects`.
- **QA-M15 — domain-neutral gate (3b.2).** QA-M10's grep over the tool + tests → no output (exit 1);
  control on `config/projects.toml` → hits.
- **QA-M16 ⚑ — delivery (3b.3).** Before the commit their two governance scripts exit 0; after the push
  `ls-remote` main = the delivery commit, parent = their previous tip; `git show --stat` == § 7.10; their
  tool blob == the vault's 0.3 blob, mode 100755; their touched manifest cells == the file headers; vault
  `status` → 780-estimator still v2.7 current (scripts are outside SYNC_MAP).
- **QA-M8 ⚑ — Windows verification, re-run with 0.3 (owner's PC; operator-relayed).** Already evidenced
  2026-10-06: N = 14 before; Git Bash `adopt` → "Adopted." + `STATUS: OK (14 memory files)`; `link` →
  "Already linked.". Still required: (b) the in-session refusal (D-9); after the recovery `link`:
  `status` OK with ≥ 14 memory files (new sessions may add some) and `cmd //c dir
  "C:\Users\<owner>\.claude\projects"` lists the key as `<JUNCTION>`; a fresh session names a known
  memory before reading any file; after `git pull` of the § 7.10 commit: `status` OK (≥ 14), no
  `WARNING`; `cleanup` → the QA-M14 result for the order she linked in, after which only the junction
  remains for the key. The expected `cleanup` list assumes her Claude's recovery report shows both
  transcript steps ran (the halves joined, the stub replaced); if either stopped, derive the expected
  list from that report BEFORE judging the `cleanup` output. Ship-gating (Rule 15).

## 9. Operator decision points (Phase 2 — answer with the approval)

- **D17.A — approve the plan** ("plan 017 is approved", or "APPROVE PLAN-017" with any D-deltas).
- **D-1 — the old `scripts/bootstrap_memory.sh`.** RECOMMEND **A**: the owner's session deletes it
  (+ manifest row + tree line) once `status` says OK — step 4 of the § 5n entry; it is their repo and
  their Rule 8, and until then it is the fallback. B: the curator removes it in a third direct commit
  at closure — the approval commit then drops step 4 from the § 5n entry and adds the commit to
  § 7 (re-run the § 5 round-trip).
- **D-2 — the four existing adopters' copies of the tool (0.1).** RECOMMEND **A**: defer to v2.8's
  script-delivery fix (none is on Windows; E002 hits them only after a folder move, with the
  documented workaround). B: hand-copy 0.2 into Capital-Signal now (outside the engine's handoff
  discipline).
- **D-3 — closure gate.** RECOMMEND **A**: the plan closes only with QA-M8 + QA-M9 evidence (Rule 15).
  B: an explicit operator waiver for QA-M8 recorded in the tracker, then close after Phase 3.
- **D-4 — the handoff's wording for a committed (git) write.** RECOMMEND **A**: explain it in the
  § 5n entry (step 2: "review" = `git show` of the engine commit) and leave the engine fix to PLAN-014
  (PLAN-013 R6). B: fix `render_handoff` here (Critical engine change; widens this plan — a plan
  revision with new § 5 blocks + a fresh Rule 13 pass before approval).
- **D-5 — registry lifecycle.** RECOMMEND **A**: `onboarding` from Phase 3, `active` at closure
  (§ 6f). B: `active` from Phase 3 — § 5d's value changes in the approval commit and § 6f's FIND drops
  out of the closure commit (config/projects.toml leaves § 7.6).

### 9.1 Decision record (Phase 2, 2026-10-05)

- **D17.A — APPROVED:** operator *"Plan-017 is approved"* (2026-10-05).
- **D-1 … D-5 = A** — not answered item by item; the agent's read (approving the drafted plan = its
  recommended options, which the § 5 blocks and the § 5n entry implement) was stated in chat and
  confirmed at the approval-commit gate:
  - **D-1 = A** — the owner's session deletes `scripts/bootstrap_memory.sh` (+ manifest row + tree line)
    once `status` says OK (§ 5n step 4).
  - **D-2 = A** — tool 0.2 reaches the four existing adopters at v2.8's script-delivery fix.
  - **D-3 = A** — the plan closes only with QA-M8 + QA-M9 evidence (Rule 15; no waiver).
  - **D-4 = A** — the handoff's wording for a committed (git) write is explained in the § 5n entry
    (step 2); the engine fix stays with PLAN-014.
  - **D-5 = A** — `lifecycle = "onboarding"` from Phase 3, `"active"` at closure (§ 6f).
- **No § 5 change:** the blocks re-extracted from this file are byte-identical to the proven blocks
  (re-verified in the approval commit).

### 9.2 Phase 3b decision points (answer with the revision approval)

- **D17.B — approve the Phase 3b revision** ("Phase 3b approved", or with any D-deltas).
- **D-6 — where Windows backups go.** RECOMMEND **A**: `~/.claude/locality-backups/` — the same drive as
  the harness path, so moving the harness dir aside stays one atomic rename that fails clean while a
  session holds it, and the backup no longer sits beside the link. B: inside the repo
  (`.claude/locality-backups/`) — on the owner's PC another drive, so the move becomes a non-atomic copy +
  delete. C: no backup (delete after a verified copy) — removes the safety net the 2026-10-06 recovery
  depended on.
- **D-7 — how backups are removed.** RECOMMEND **A**: the `cleanup` verb (§ 5q) — removes a backup only
  when every file in it is in the store with the same leading bytes, file by file, never `rm -r`, never
  through a link; a kept backup beside the link is moved away from it. B: no verb — print a safe manual
  command instead (still a hand action next to the link).
- **D-8 — how 0.3 reaches the estimator.** RECOMMEND **A**: one curator commit pushed to their `main`
  (§ 5t–5w; Delivery A, like the prep). B: the owner's session copies the file from the vault's GitHub
  mirror — needs her org read access and leaves the version-cell edits to her.
- **D-9 — QA-M8 sub-check (b), the in-session refusal.** RECOMMEND **A**: capture it live — before she
  links, her Claude runs `bash scripts/claude_project_data.sh link` inside the session; expected `ABORT: a
  Claude Code session for this project looks active` and nothing changed (the guard runs before any move).
  Possible only while her harness path is still a plain folder — once she has linked, A is impossible and
  B applies. B: accept the unit test `test_windows_refuses_while_a_session_is_live` for sub-check (b) —
  an operator waiver recorded in the tracker's waiver register (D-3 otherwise stands).

### 9.3 Phase 3b decision record (2026-10-07)

- **D17.B — APPROVED:** operator *"commit; Phase 3b approved, all A"* (2026-10-07).
- **D-6 = A** — Windows backups go to `~/.claude/locality-backups/` (§ 5q).
- **D-7 = A** — backups are removed by the `cleanup` verb (§ 5q).
- **D-8 = A** — one curator commit on their `main` delivers 0.3 (§ 5t–5w).
- **D-9 = A** — sub-check (b) is captured live before she links (the in-session line was handed to the
  operator 2026-10-07); if she has already linked when it arrives, A is impossible and B needs the
  operator's explicit waiver, recorded in the tracker's waiver register.
- **No § 5 change:** the blocks re-extracted from this file stay byte-identical to the proven files
  (re-verified in the approval commit).

## 10. Rollback path

- **Vault:** `git revert` the Phase 3 commit — tool 0.1 back (the vault's own link is a plain symlink,
  untouched by the change), registry entry gone (the estimator simply stops being synced).
- **Estimator:** `git revert` the engine commit, then the prep commit — new commits on `main`, never a
  force-push (their Rule 3). Their old memory link keeps working throughout: `bootstrap_memory.sh` and
  its junction stay until `adopt` succeeds (D-1 = A).
- **Owner's PC:** `adopt` keeps the original harness dir as `<key>.pre-locality-<stamp>`; to undo:
  remove the junction (`cmd //c rmdir`), rename the backup back, re-run `bash
  scripts/bootstrap_memory.sh`.
- **Capital-Signal:** the write-back only rewrites E002's Status line; its next session can revert it.
- **Phase 3b:** vault — `git revert` the § 7.9 commit (tool 0.2 + tests 0.1 back); estimator — `git
  revert` the § 7.10 commit (a new commit, never a force-push); owner's PC — 0.3 changes no data layout
  (the junction stays; backups in `~/.claude/locality-backups/` are plain folders).

## 11. Known risks + mitigation

| # | Risk | Mitigation |
|---|---|---|
| R1 | Claude Code's Windows path-key differs from the drive-form rule | No destructive step acts on a missing path: `adopt` with no dir at the computed key says "Nothing to adopt" and touches nothing; the old junction keeps the memory reachable; QA-M8's fresh-session recall proves the key; NTFS is case-insensitive, so the drive letter's case cannot split it |
| R2 | Git Bash does not report a junction as a symlink | `is_link` falls back to comparing the entry's resolved path with its parent's; QA-M8 checks `status` OK after `adopt` and `link` idempotence |
| R3 | A live session holds the harness dir | the 2-minute transcript guard refuses first; the rename is atomic (fails clean); the restore line prints before any copy; the backup is kept |
| R4 | The owner pushes while the engine writes | push is fast-forward only → the write fails, nothing overwritten; re-run the dry-run, then `--write` |
| R5 | The owner has unpushed local work touching the synced files | governance files only; their next `git pull` merges or reports conflicts in docs they own; the operator tells them first (§ 2) |
| R6 | The handoff's "review `git diff`" does not fit a committed write | D-4 = A: the § 5n entry says what to do; PLAN-014 owns the engine wording |
| R7 | Tool 0.2 regresses the Mac/Linux targets or the vault | POSIX branch = 0.1 semantics + the E002 fix; 7 POSIX tests; QA-M3 on the live vault store |
| R8 | The estimator moved past `45d7c75` before Phase 3 | the reconcile pass re-checks all 21 estimator FINDs on the live tip; a mismatch is a plan defect |
| R9 | The vault Set Version moves before Phase 3 (a v2.8 lands first) | the catch-up delivers whatever is current; § 5e / § 5n / § 5p name v2.7 → a reconcile defect, text updated in the approval or reconcile step |
| R10 | The owner's name sits in the vault, which the 780-AI GitHub mirror shows to org members | operator-supplied for the registry (§ 2); `config/projects.toml` + the opener § 2 row only — never in `docs/standards/` or `skill/` (QA-M10) |
| R11 | Capital-Signal busy when the write-back runs | QA-M7's idle check first; the engine write accumulates in its handoff either way |
| R12 | A file-manager action on the harness link moves or deletes the real store (the 2026-10-06 incident: an Explorer move of the junction emptied it) | 0.3: the backup no longer sits beside the link; `adopt` / `link` end with a warning; `cleanup` replaces "delete it once…"; the owner's rule (relayed); the Rule 14 halt-on-empty still catches a loss at the next session open |
| R13 | The owner's `main` moves before Phase 3b | § 6i re-renders only version numbers + date as named reconcile deltas; anything else is a plan defect |
| R14 | `cleanup` deletes data it should keep | removes only files the store holds with the same leading bytes; refuses unless `status` is OK; never `rm -r` (files one by one, then empty dirs with `rmdir`); never follows a link — a link inside a backup, or a path that resolves outside it, keeps the whole backup; 7 tests |
| R15 | The delivery takes the version numbers the owner's in-flight work planned to use | § 6i tells the owner the two numbers; her work re-bases past them (her session re-bases before running its edit script) |

## 12. Acceptance criteria

1. QA-M1…M7 + M10 ✅ in the Phase 3 session with evidence pasted in the tracker; QA-M8 + M9 ✅ (or an
   operator waiver for M8, D-3 = B) before closure.
2. The estimator's `main` carries exactly three commits from this plan — the prep (§ 7.2), the
   engine's sync (§ 7.3) and the tool delivery (§ 7.10) — and no force-push.
3. Vault `status` lists 780-estimator **v2.7 / v2.7 current** over git; the re-run dry-run is a no-op.
4. The owner's Claude memory count after `adopt` equals the count before (QA-M8).
5. Capital-Signal E002 reads `integrated → vault scripts/claude_project_data.sh v0.2 (…)`.
6. Every manifest cell touched equals its file header (grep, L063); governance scripts exit 0 in the
   vault (stdout pasted, Rule 6).
7. Plan + tracker 1.0 / CLOSED; OPEN_TASKS updated; the v2.8 queue holds Rule 16 items 4, 5, 8 and
   the D-2 delivery item.
8. QA-M11…M16 ✅ in the Phase 3b session with evidence in the tracker; QA-M8 ✅ with tool 0.3 on the
   owner's PC (sub-check (b) live, or the D-9 = B waiver).
9. The estimator's copy of the tool is byte-identical to the vault's 0.3.
10. No locality backup sits beside the owner's harness link after the QA-M8 `cleanup`.

## Rule 13 senior-review pass (2026-10-05)

Run on the complete plan + tracker, after drafting, with the canonical § 15.8 prompt.

**Mechanical (L051 — tools on the code exactly as it ships):** all 33 blocks re-extracted from THIS
file by a parser (round-trip identical to the proven blocks) and applied to brand-new copies of the
vault (`8b914db`) and the estimator (`45d7c75`, re-confirmed live by `ls-remote`) with `<P3-DATE>` =
2026-10-05: every FIND matched once, both pre-image blobs matched, both new files were absent, the
§ 5k copy was byte-identical. QA-M1: ruff clean, `MYPYPATH=src mypy` 0 issues in 25 files, pytest 151.
QA-M2: the 11 tests against tool 0.1 → 6 failed / 5 passed (exactly the new-behavior cases). QA-M10:
grep clean. Estimator: its two governance scripts exit 0 / 0; the prep committed with the § 5o message
extracted from this file; over the git transport (local bare remote): `status` v1.3 / v2.7 behind →
dry-run 7 of 11 → removed lines 28 / 19 / 6 / 3 == § 8.1 → `--write` 8 files in one engine commit whose
parent is the prep → re-run up-to-date → `status` v2.7 current.

**Findings fixed in place:**

1. **Defect — domain-neutrality of the delivered tool.** The tool is copied verbatim into every
   adopter, yet its 0.2 change log named a fleet project and the Windows test fixture used a path with
   the owner's name. Both genericized (§ 5a / § 5b re-rendered); QA-M10's grep now covers the tool and
   its test.
2. **Defect — ordering.** § 5d / 5e (registry + opener row) were scheduled with the other vault blocks
   in step 3.2, before the prep commit reaches their `main`: any `status` / `fleet` / governance run in
   between would probe a repo the engine cannot read. Moved to step 3.4 (§ 5 "Order", § 4, tracker).
3. **Gap — midnight.** § 8.1's exact counts assumed the prep and the engine stamp the same date; the
   rule for a session crossing midnight is now stated (+1 `Last Updated` line per stamped doc).
4. **Gap — D-item consequences.** Each option B now says what it changes in the plan (D-1, D-4, D-5);
   choosing one means an approval-commit edit and a fresh round-trip, not a silent divergence.
5. **Gap — Windows wording in the template.** Rule 14 and the session files say "symlink"; on Windows
   it is a junction. A `docs/standards/` edit → queued for v2.8 (§ 3), not widened into this plan.

**Optimizations applied:** whole-file replace with a pinned pre-image blob for the two rewritten files
(the reconcile pass proves the live file is exactly what the plan expects, instead of 20+ hunks); the
§ 5n entry carries the owner's whole next-session sequence (handoff landing, `adopt`, cleanup, evidence)
so the git-write handoff gap (D-4) needs no engine change here.

**Considered and declined:** (a) a `trap` restoring the backup on any Windows failure — the restore
line printed before the copy plus a kept backup is simpler and leaves the operator in control;
(b) making the POSIX branch copy-then-swap like Windows — it would change proven behavior on the four
Mac / Linux targets and the vault for no benefit there.

**Edge cases walked:** a live session (guard + atomic rename), cross-drive harness/repo (copy, not
move), a pre-existing in-repo `memory/` during the old-layout migration (left in place, reported), a
concurrent owner push (fast-forward only), the estimator moving before Phase 3 (reconcile), a Set
release before Phase 3 (R9), Capital-Signal busy (idle check), a key mismatch (no destructive step on
a missing path, R1), Git Bash not reporting a junction as a symlink (R2).

**No new design decision surfaced** beyond D-1…D-5 (§ 9).

## Rule 13 senior-review pass — Phase 3b revision (2026-10-07)

Run on the complete revised plan + tracker, after drafting, with the canonical § 15.8 prompt.

**Mechanical (L051 — tools on the code exactly as it ships):** the 11 Phase 3b blocks + the § 5w message
re-extracted from THIS file by a parser and applied to a brand-new copy of the vault (`fb8960c`) and a
fresh clone of the estimator (`main` = `1ddbbf9`, re-confirmed by `ls-remote`) with `<P3B-DATE>` =
2026-10-07: every pre-image blob matched (`4e3d1f0…` for the vault tool and their copy, `f66fc29…` for the
tests), every FIND matched once, the § 5t copy was byte-identical with mode 100755; the tool, the tests and
their copy are byte-identical to the proven files. Checker positive control: one FIND corrupted → exactly
1 FAIL. QA-M11: ruff clean, `MYPYPATH=src mypy` 0 issues in 25 files, `bash -n` clean, pytest 163.
QA-M12: tests 0.2 against tool 0.2 → 13 failed / 10 passed. QA-M15: grep clean (control: 16 hits).
Estimator: its two governance scripts exit 0 / 0 after § 5t–5v; every touched cell == its header
(CHANGELOG 1.42, manifest 1.59, tool 0.3); a local commit with the extracted § 5w message (never pushed)
stats exactly the 3 files of § 7.10. QA-M14 replay (both orders) matches § 8.2. Re-run after finding 1
below — all green again.

**Findings fixed in place:**

1. **Gap — the memory count is not frozen.** § 5v.2 and QA-M8 expected exactly 14 memory files after the
   recovery, but new sessions on the owner's PC may add memories before 0.3 arrives — both now read "14
   or more" (the 2026-10-06 adopt evidence stays at 14, as observed).
2. **Gap — QA-M8's expected `cleanup` list depends on the recovery.** It assumed her Claude's two
   transcript steps both ran; either may legitimately STOP on its own decision rule. The expected list is
   now derived from her recovery report before the output is judged (no fitting after the fact).
3. **Gap — a stray-backup probe must prove it ran.** QA-M13's prediction ("No backups to clean up")
   rests on this Mac holding no `pre-locality` dirs; the first probe aborted on a zsh unmatched glob and
   proved nothing — re-run with `find` and a positive control (3 entries seen, 0 backups, no backup root).
   No plan text change; a data point for the queued "a green proof must prove it ran" lesson.

**Considered and declined:** (a) a suffix rule in `cleanup` (treat a backup file as covered when the store
copy ENDS with it — the re-assembled transcript) — it would delete more on a heuristic; the prefix rule
keeps the backup and lists the file, the safe direction; (b) a guard against a same-named folder already
in `~/.claude/locality-backups/` when a kept old-location backup moves there — names carry a per-second
stamp and the old ones predate 0.3, so a clash is not reachable; (c) listing `cleanup` in template Rule 14
now — a `docs/standards/` edit (Set bump), routed to v2.8 (§ 3).

**Edge cases walked:** an empty store with and without a harness dir (F1 messages, exit 1); a linked store
with no memories (warning, exit 0); a live session during `link` (guard before any move); a backup that is
itself a link, holds a link, or resolves outside itself through a junction Git Bash does not report (kept
whole — the conservative direction, also if path-case differences make the `readlink -f` prefixes
disagree); a grown transcript (the prefix covers it); a store file deleted or rewritten (kept, listed);
`cleanup` while `status` is not OK (refused); backups of other projects (key-scoped glob); file names with
spaces (NUL-separated loops); the owner's `main` moving before Phase 3b (§ 6i); her in-flight version
numbers (R15); her uncommitted work touching none of the 3 delivered files (her pull stays clean).

**New design decisions surfaced:** D-6…D-9 (§ 9.2) — none decided silently.
