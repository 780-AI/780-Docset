<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-10-08 -->
<!-- Status: CLOSED — 2026-10-08: QA-M8 ✅ on the owner's Windows PC with tool 0.3; acceptance § 12 items 1–10 met -->
<!--
CHANGE LOG
v1.0 — 2026-10-08 — CLOSED: QA-M8 ✅ with evidence (all plan § 8.2 sub-checks; (b) captured live, no
waiver); incident record gains the owner's confirmation; Phase 5 ✅ (Phase 3b push 2026-10-07 + this
closure commit); new Closure section — acceptance § 12 items 1–10 checked one by one.
v0.6 — 2026-10-07 — Phase 3b executed in a fresh session (3b.0–3b.4 ✅): reconcile 11 / 11 clean; vault
tool 0.3 + tests 0.2 + folder_structure 0.17; estimator delivery commit `515ea96` pushed; QA-M11…M16 ✅
with evidence. QA-M8 stays ⏸ (owner's PC, with 0.3).
v0.5 — 2026-10-07 — Phase 2b ✅: "commit; Phase 3b approved, all A" (plan § 9.3).
v0.4 — 2026-10-07 — QA-M9 ✅ (evidence); QA-M8 partial evidence + the 2026-10-06 incident record; Phase
1b ✅ (tool 0.3 proven, replay, Rule 13), Phase 2b / 3b sub-tasks ⏸; QA-M11…M16 rows; Phase 5 push ✅.
v0.3 — 2026-10-05 — Phase 3 executed in a fresh session (3.0–3.6 ✅); QA-M1…M7 + M10 ✅ with evidence;
plan defect D1 (§ 8.1 wording; operator D1 = A); QA-M7 idle-gate process note. QA-M8 / M9 ⏸ (owner's PC).
v0.2 — 2026-10-05 — Phase 2 approval recorded ("Plan-017 is approved"; decisions in plan § 9.1).
v0.1 — 2026-10-05 — Created with the plan draft (tracker required per CLAUDE.md § 15.7: Phase 3 lands
as several commits across two repos; Phase 4 has a multi-scenario list, QA-M1…M10; the Windows half
spans sessions).
-->

# PLAN-017 tracker — 780-estimator catch-up + Windows-capable locality tool

## Phase 0 — Audit

- ✅ 2026-10-05 — § 15.9 intake: operator request (no document); inputs recorded (plan § 2).
- ✅ 2026-10-05 — read-only scratch clone of `780-AI/780-estimator` `main` = `45d7c75`: 60 commits,
  Set v1.3 bootstrap `66ac85c`, governance layer changed after bootstrap only in `8b7f1fe`; Windows
  evidence in `scripts/bootstrap_memory.sh`; access: `ls-remote` ✓, no-op `push --dry-run` accepted.
- ✅ 2026-10-05 — engine as oracle on the untouched repo: adopted `?`; dry-run stops at the opener's
  PROJECT-OWNED count (2 vs 3); integration points cited `file:line` (plan § 3).
- ✅ 2026-10-05 — Rule 16 gate: 12 candidates listed + explained + recommended; operator "yes to all
  recommended" (dispositions in plan § 2).

## Phase 1 — Design

- ✅ 2026-10-05 — tool 0.2 + 11 tests proven in a scratch overlay: ruff clean / mypy 0 (25 files,
  `MYPYPATH=src`) / pytest 151; positive control vs 0.1 → exactly the 6 new-behavior tests fail.
- ✅ 2026-10-05 — the whole catch-up proven over the git transport against a local bare remote: prep
  commit → `status` behind → dry-run 7/11 → `--write` 8 files in one engine commit (parent = prep) →
  re-run up-to-date 11/11 → `status` current; post-sync integrity (markers 4/3/2, 15 rules, script
  present); removed-lines set recorded (plan § 8.1).
- ✅ 2026-10-05 — E002 decisions dry-run against the real Capital-Signal log (no write).
- ✅ 2026-10-05 — § 5 generated from the proven blocks (33 blocks; parse round-trip identical).
- ✅ 2026-10-05 — Rule 13 senior-review pass (record at the foot of the plan).

## Phase 2 — Operator approval

- ✅ 2026-10-05 — "Plan-017 is approved" — D17.A; D-1…D-5 = A (plan § 9.1). Plan + tracker → 0.2.

## Phase 3 — Implement (fresh session)

- ✅ 2026-10-05 — 3.0 Pre-checks: vault tree clean at `b2f6aa3` (after the approval commit only PLAN-016
  bookkeeping moved — CHANGELOG, manifest, PLAN-016 tracker; no block anchor among them); local clock ==
  `gitlab.com` / `apple.com` `Date:` within 2 s → `<P3-DATE>` = 2026-10-05; vault Set Version v2.7 (R9
  not triggered); estimator `ls-remote` main = `45d7c75` (R8 not triggered); operator: "Bahereh told +
  idle".
- ✅ 2026-10-05 — 3.1 Reconcile pass: all 33 blocks re-extracted from the plan by a parser and checked
  sequentially per file on the live trees (vault working tree + a fresh writable estimator clone in the
  session scratchpad) — every FIND matched once, both pre-image blobs matched (`c746047…`, `6ee9fc2…`),
  both NEW files absent, the § 5k copy source present. **Zero block defects.** Checker positive control:
  one FIND corrupted → exactly 1 FAIL.
- ✅ 2026-10-05 — 3.2 Vault § 5a, 5b, 5c, 5f, 5g applied (`<P3-DATE>` substituted; script mode 100755
  kept) → QA-M1, QA-M2, QA-M3, QA-M10 ✅.
- ✅ 2026-10-05 — 3.3 Estimator § 5h–5n applied on the clone (7 files == § 7.2; § 5k `cmp` identical,
  mode 755) → QA-M4 ✅ → Rule 10 review table posted → commit `b4cae64` (§ 5o message via `-F`, author
  Yaser Khosravi, parent `45d7c75`) → operator "go D1 = A" → pushed `45d7c75..b4cae64` → `ls-remote` main
  = `b4cae64`. Clones deleted after use.
- ✅ 2026-10-05 — 3.4 Vault § 5d + 5e applied (after the prep was on their `main`) → `status` behind →
  dry-run 7/11 → `--diff` identical to the QA-M4 oracle diff → operator "go" → `sync --project
  780-estimator --write` → QA-M5, QA-M6 ✅.
- ✅ 2026-10-05 — 3.5 Capital-Signal E002 write-back (§ 5p TOML extracted verbatim) → QA-M7 ✅ (process
  note below).
- ✅ 2026-10-05 — 3.6 § 6c / 6d / 6e bookkeeping → governance (stdout pasted in chat) → Rule 10 review
  table → vault commit (§ 7.5; no push) → OPEN_TASKS (§ 6g).

> **Plan defect D1 (wording; operator D1 = A, 2026-10-05).** § 8.1 listed removed lines for the merge /
> record files only; the dry-run also removes 3 non-header lines from the replace-mode
> `docs/standards/MEMORY_PROTOCOL.md`. Investigated before any write: the estimator's three changed
> replace-mode files (PROJECT_STANDARDS, MEMORY_PROTOCOL, LESSONS) are byte-identical to the vault's
> `set-v1.3` blobs (`cfbaff0`, `ac947df`, `b30f618`) — no local text; the 3 lines are the vault's v2.2
> identifier scrub (`64a5752`). § 8.1 gains one sentence (plan v0.3).
>
> **Process note (QA-M7 idle gate).** The idle re-check ran in the same command as `integrate --write`, so
> it printed instead of gating: it listed one Capital-Signal transcript changed in the last 10 minutes.
> Investigation (plain reads, no git in that repo): a session on the operator's other Mac had posted its
> completed wrap-up block at 21:26:42 local, ~7 minutes before the write (clean tree; its one commit
> `08b638d` touched neither written file); `STANDARDS_LOG.md` held E001 + E002 only, header unchanged; no
> conflicted copies; no handoff existed before. No collision — but a check that cannot stop the action is
> not a gate; gating checks run as separate steps from here on (lesson candidate in OPEN_TASKS).

## Phase 1b — Phase 3b design (revision, 2026-10-07)

- ✅ 2026-10-06 — Incident investigated (read-only: vault side + the owner's Claude): tool 0.2 has no path
  that empties the store; root cause a manual Explorer move of the junction (plan § 2); the store
  recovered from the Recycle Bin (14 memories byte-identical; two transcripts re-assembled before `link`).
- ✅ 2026-10-07 — Operator: "A" (fix inside this plan before closing).
- ✅ 2026-10-07 — tool 0.3 + tests 0.2 proven in a scratch overlay: ruff clean / mypy 0 (25 files,
  `MYPYPATH=src`) / `bash -n` clean / pytest 163; positive control vs 0.2 → 13 failed / 10 passed.
- ✅ 2026-10-07 — replay of the owner's post-incident state, both orders (plan § 8.2 QA-M14 outputs).
- ✅ 2026-10-07 — § 5q–5w generated from the proven files; Rule 13 pass (record at the foot of the plan).

## Phase 2b — Operator approval of the revision

- ✅ 2026-10-07 — "commit; Phase 3b approved, all A" — D17.B; D-6…D-9 = A (plan § 9.3). Plan + tracker → 0.5.

## Phase 3b — Implement (fresh session)

- ✅ 2026-10-07 — 3b.0 Pre-checks: local clock 13:32:27 UTC vs `gitlab.com` `Date:` 13:32:33 GMT →
  `<P3B-DATE>` = 2026-10-07 (local 17:17 +0330); vault tree clean at `d4c6e2f`; estimator `ls-remote` main
  = `1ddbbf9` (§ 6i not triggered); operator: "bahere is informed go on" (R15).
- ✅ 2026-10-07 — 3b.1 Reconcile pass: all 11 blocks + the § 5w message re-extracted from the plan by a
  parser written fresh in this session (fence counts asserted per block kind) — vault 4 / 4 and estimator
  7 / 7 OK: pre-blobs `4e3d1f0…` (vault tool and their copy) + `f66fc29…` (tests) matched, every FIND
  matched once. **Zero block defects.** Checker positive control: one FIND corrupted → exactly 1 FAIL.
- ✅ 2026-10-07 — 3b.2 Vault § 5q, 5r, 5s applied (script mode 100755 kept; no `<P3B-DATE>` left); tool and
  tests byte-identical to the drafting session's proven files → QA-M11…M15 ✅.
- ✅ 2026-10-07 — 3b.3 Estimator § 5t–5v applied on a fresh clone (3 files == § 7.10; § 5t `cmp` identical,
  mode 755) → their governance exit 0 / 0 → Rule 10 review table posted → operator "go" → commit `515ea96`
  (§ 5w message via `-F`; author Yaser Khosravi — the fresh clone had NO identity on this machine, set
  repo-locally to the vault's before committing, matching `b4cae64`) → pushed `1ddbbf9..515ea96` →
  QA-M16 ✅. Clone deleted after use.
- ✅ 2026-10-07 — 3b.4 § 6h bookkeeping → governance → Rule 10 review → vault commit (§ 7.9; no push) →
  OPEN_TASKS.

## Phase 4 — Validate

| # | Scenario | Phase | Status | Date | Evidence |
|---|---|---|---|---|---|
| QA-M1 | Tools (ruff / mypy / pytest 151) | 3.2 | ✅ | 2026-10-05 | `ruff check src tests` → All checks passed; `MYPYPATH=src mypy --cache-dir <fresh> src tests` (strict) → no issues in 25 source files; pytest → 151 passed |
| QA-M2 | Tests go red on tool 0.1 (6 of 11) | 3.2 | ✅ | 2026-10-05 | the 11 tests vs a scratch copy of 0.1 → 6 failed (2 POSIX E002 + 4 Windows), 5 passed (the baseline cases) |
| QA-M3 ⚑ | Vault's own locality `status` OK | 3.2 | ✅ | 2026-10-05 | before: `STATUS: OK (18 memory files)`; with 0.2: `symlink: -> …/.claude/project-data`, `STATUS: OK (18 memory files)`, exit 0 |
| QA-M4 ⚑ | Prep proof (governance + engine oracle) | 3.3 | ✅ | 2026-10-05 | their `check_doc_coverage.py` / `check_test_coverage_drift.py --ci` exit 0 / 0; scratch vault (`git archive HEAD`, registry → the clone, local transport): `status` v1.3 / v2.7 behind; dry-run 7 of 11 (the § 3 seven); removed lines CLAUDE 28 / opener 19 / closer 6 / SVA 3 == § 8.1, line set matches its description; replace-mode removals explained (D1) |
| QA-M5 ⚑ | First live git write | 3.4 | ✅ | 2026-10-05 | `status` (git read path) 780-estimator v1.3 / v2.7 behind; dry-run 7/11; live `--diff` identical to the QA-M4 oracle diff; `--write` → "wrote + flushed 8 file(s) (incl. the handoff)"; `ls-remote` main `b4cae64` → `fdb87b9`; `fdb87b9` parent = `b4cae64`, author `Standard DocSet <standard-docset@localhost>`; `git show --stat` = the 8 files of § 7.3; re-run up-to-date 11/11 (notes the un-landed handoff); `status` v2.7 / v2.7 current; `docs/fleet.csv` row: registry columns == § 5d (registered_on 2026-10-05), `reachable` yes, `handoff_pending` 1 |
| QA-M6 ⚑ | Post-sync integrity | 3.4 | ✅ | 2026-10-05 | fresh clone of `main`: PROJECT-OWNED BEGIN/END CLAUDE 4/4, opener 3/3, closer 2/2; 15 `### Rule` headings; Rule 14 names `scripts/claude_project_data.sh` (4×), file present + executable; opener heading (l.14) + § 2 "Current state" note (l.92) + § 3.2 popup row intact; closer heading (l.13); SVA bullets v2.7 / 2026-10-05, rows v2.7 + v1.3 |
| QA-M7 ⚑ | CS E002 write-back | 3.5 | ✅ | 2026-10-05 | operator "go" (no CS session); dry-run → `--write` → Status read back == § 5p's rendering verbatim; CS `docs/SYNC_HANDOFF.md` new, `### Write 1` = integrate write-back of `docs/STANDARDS_LOG.md`; `harvest` → "No open log entries across registered projects" (780-Automation skipped, unreachable). Idle-gate process note above |
| QA-M8 ⚑ | Windows `adopt` on the owner's PC — re-run with 0.3 (plan § 8.2) | post-3b | ✅ | 2026-10-08 | 2026-10-06: before 14 (stated beforehand); Git Bash `adopt` → "Adopted." + `STATUS: OK (14 memory files)`; `link` → "Already linked." — then the Explorer move (incident below). **Re-run 2026-10-08 with 0.3** (owner, Git Bash, a self-checking step guide relayed as a .txt — every block printed its verdict and appended to one results file): `git pull --ff-only` `1ddbbf9..515ea96`, `# VERSION: 0.3`; `status` NOT LINKED (harness dir + in-repo data), repaired 0 of 2; **(b) live, before the link:** Claude Code open + a new message → `link` → `ABORT: a Claude Code session for this project looks active …` (17:00:58), nothing changed (D-9 = A); transcripts repaired from the Desktop backup: d65a220e 188 lines (63 + 125), 335dbc56 identical, git status unchanged, 14 memories; Claude Code closed → `link` (17:05): harness dir → `C:\Users\<owner>\.claude\locality-backups\<key>.pre-locality-20261008-170519`, `skip` exactly the two repaired transcripts, "Linked.", `backup kept:`, `STATUS: OK (14 memory files)`; `cmd //c dir` → the key `<JUNCTION>` → `E:\…\780-estimator\.claude\project-data`, nothing beside it; **new session** named the memory `project_plan_pipeline_status` (citing `45d7c75`, their `main` at our 2026-10-05 audit) before reading any file, `status` OK 14 exit 0, `backup kept:` line, no `WARNING`, d65a220e 188; **`cleanup`** (17:26) → `KEPT` + exactly `differs …: 335dbc56…` and `differs …: d65a220e…` (expectation written down before the output — matched; no "moved away" line, Order 1), `dir` → only the `<JUNCTION>` for the key. Memory count 14 before = 14 after (acceptance #4) |
| QA-M9 ⚑ | Handoff landing observed | post-3 | ✅ | 2026-10-06 | `ls-remote` main `fdb87b9` → `1ddbbf9`; fresh clone: `7e466f8` = CHANGELOG + manifest 1.57 (cells == headers) + `docs/SYNC_HANDOFF.md` deleted; `1ddbbf9` = `bootstrap_memory.sh` + its manifest row + tree line removed (manifest 1.58, CHANGELOG 1.41, folder_structure 1.18); linear, governance paths only; their tool blob `4e3d1f0` == the vault's; vault `status` 780-estimator v2.7 current, fleet `handoff_pending` 0 |
| QA-M10 | Domain-neutral grep | 3.2 | ✅ | 2026-10-05 | `grep -rniE "780\|estimator\|everon\|equinex\|capital-signal\|bahereh\|parsaazad\|a780" skill/ docs/standards/ scripts/claude_project_data.sh tests/test_claude_project_data.py` → no output, exit 1; control: same pattern on `config/projects.toml` → 23 hits |
| QA-M11 | Tools (ruff / mypy / pytest 163) | 3b | ✅ | 2026-10-07 | `ruff check src tests` → All checks passed; `MYPYPATH=src mypy --cache-dir <fresh> src tests` → no issues in 25 source files; `bash -n scripts/claude_project_data.sh` exit 0; pytest → 163 passed |
| QA-M12 | Tests go red on tool 0.2 (13 of 23) | 3b | ✅ | 2026-10-07 | tests 0.2 vs a scratch copy of the § 5q pre-image (tool 0.2) → 13 failed / 10 passed: the 12 new tests + `test_windows_adopt_migrates_the_old_junction_layout` fail; the 10 unchanged pass |
| QA-M13 ⚑ | Vault's own locality `status` + `cleanup` | 3b | ✅ | 2026-10-07 | pre-probe (`find`, positive control: the key seen): 0 `pre-locality` entries, no backup root; `status` → `symlink: -> …/.claude/project-data`, `STATUS: OK (18 memory files)`, no `WARNING`, no `backup kept:`, exit 0; then (own step) `cleanup` → "No backups to clean up for this project." exit 0; count 18 → 18; no backup root created |
| QA-M14 ⚑ | Replay of the owner's state, both orders | 3b | ✅ | 2026-10-07 | Windows stand-ins (the tests' shims): store = 2 memories + `d65a220e` (A+H) + `335dbc56` (159 lines); harness = H + a 4-line stub + a later session. Order 1 (`link` 0.3): backup under `~/.claude/locality-backups/`, link → store, nothing beside it, later session copied, store copies not overwritten; `status` OK + `backup kept:`; `cleanup` → `KEPT`, lists exactly `differs …: d65a220e.jsonl` + `differs …: 335dbc56.jsonl`, store + backup hashes unchanged. Order 2 (`link` 0.2, then 0.3): backup beside the link; `status` lists it; `cleanup` → `KEPT` + "moved away from the link to: …/locality-backups/…", backup intact there, only the link left for the key, store unchanged. 17 / 17 checks pass (11 + 6) |
| QA-M15 | Domain-neutral grep | 3b | ✅ | 2026-10-07 | QA-M10's pattern over the tool + tests → no output, exit 1 (also over `skill/` + `docs/standards/`: exit 1); control on `config/projects.toml` → 29 lines (23 at QA-M10, before § 5d added the estimator entry) |
| QA-M16 ⚑ | Delivery commit on their `main` | 3b | ✅ | 2026-10-07 | before the commit: their `check_doc_coverage.py` / `check_test_coverage_drift.py --ci` exit 0 / 0; after the push: `ls-remote` main = `515ea96`, parent `1ddbbf9`; `git show --name-only` = the 3 files of § 7.10; their tool `100755 blob 24f758b…` == vault 0.3 `git hash-object`; cells == headers at `515ea96` (CHANGELOG 1.42, manifest 1.59, tool 0.3); vault `status` → 780-estimator v2.7 / v2.7 current, fleet `handoff_pending` 0 |

**Waiver register (Rule 15):** _(none — QA-M8 sub-check (b) was captured live on 2026-10-08, D-9 = A)_

> **Incident 2026-10-06 (QA-M8, the owner's PC).** At 09:35 `adopt` ran correctly. At 09:45 the junction
> and the tool's backup beside it were cut into a new Desktop folder in Explorer; moving the junction moved
> the real files (E: → C:) and emptied `.claude/project-data/`; the leftover junction was recycled at
> 09:45:55 and the Desktop folder at 09:52:53; Claude Code then wrote into a fresh plain harness dir. The
> owner's opener § 1.5 halt-on-empty caught it at her next session (17:04). Evidence: Recycle Bin items +
> deletion times, folder timestamps, no shell-history hits (her Claude, read-only). Recovered from the
> Recycle Bin by her Claude: 14 memories byte-identical; the two transcripts' re-assembly sent with the
> `link` steps. Tool 0.2 has no path that empties the store; the design gaps F1 / F2 are Phase 3b.
> **Owner confirmation 2026-10-08:** "YES, I DID" — the cut-and-paste of both entries into
> `Desktop\calude_BAK` in Explorer at about 09:45 on 2026-10-06 (incident cause confirmed).

## Phase 5 — Operator gate

- ✅ 2026-10-06 — Vault push (`fb8960c`) to BOTH remotes (`origin` GitLab + `github` 780-AI/780-Docset):
  governance exit 0 / 0; `ls-remote` origin master = github master = `fb8960c` = HEAD; no tag.
- ✅ 2026-10-07 — Phase 3b vault commits (`b4ce2ce` `d4c6e2f` `9b1c49e`) pushed to BOTH remotes (operator
  "push"): governance exit 0 / 0; `ls-remote` origin master = github master = `9b1c49e` = HEAD; no tag.
- ✅ 2026-10-08 — Closure commit (§ 7.6, 5 files) after QA-M8 ✅ (QA-M9 ✅); its push to both remotes runs
  on the operator's "push" (recorded in OPEN_TASKS — this tracker is frozen at closure).

## Closure — acceptance (plan § 12), checked 2026-10-08

1. ✅ QA-M1…M7 + M10 (2026-10-05) and QA-M8 + M9 (2026-10-08 / 2026-10-06) with evidence above; no waiver.
2. ✅ The estimator's `main` (fresh clone, `ls-remote` = `515ea96`): `45d7c75..main` = `b4cae64` (prep,
   curator) → `fdb87b9` (engine sync, "Standard DocSet") → `7e466f8` + `1ddbbf9` (the owner's landing) →
   `515ea96` (delivery, curator); 0 merges; all three plan commits are ancestors of `main` — no force-push.
3. ✅ Vault `status`: 780-estimator v2.7 / v2.7 current over git; `sync --project 780-estimator` dry-run
   → every item `ok` (no-op).
4. ✅ Memory count 14 before `adopt` (2026-10-06) = 14 after the 0.3 `link` (2026-10-08).
5. ✅ Capital-Signal `docs/STANDARDS_LOG.md` E002: `Status: integrated → vault scripts/claude_project_data.sh
   v0.2 (PLAN-017 locality-tool fix — …)` (plain read).
6. ✅ Every manifest cell touched by the closure == its file header (grep, L063); governance exit 0 / 0 in
   the vault at the closure commit.
7. ✅ Plan + tracker 1.0 / CLOSED; OPEN_TASKS updated; its v2.8 queue holds Rule 16 items #4, #5, #8 and the
   D-2 tool-delivery item.
8. ✅ QA-M11…M16 (2026-10-07) + QA-M8 with tool 0.3 on the owner's PC, sub-check (b) live.
9. ✅ The estimator's tool blob `24f758b…` == the vault's 0.3 `git hash-object` (re-checked 2026-10-08).
10. ✅ After the QA-M8 `cleanup`, `dir C:\Users\<owner>\.claude\projects` shows only the `<JUNCTION>` for the
    key — the kept backup lives in `~/.claude/locality-backups/`.
