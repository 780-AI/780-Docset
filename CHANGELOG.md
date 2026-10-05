# CHANGELOG

Newest entries at the top.

## [2026-10-05] — Session opener + closer: two push remotes (GitLab + GitHub)

- **Type:** Governance docs (binding session procedures) + a mechanical anchor shift in an approved
  plan. No engine change, no Set Version change, no tool behavior change.
- **What:** completes the deferred half of the second-remote change (entry below), on the operator's
  direction ("fix the session opener/closer"):
  - `docs/SESSION_OPENER.md` 1.18 → 1.19 — § 1.1 probes unpushed commits per remote (`origin` =
    GitLab, `github` = GitHub `780-AI/780-Docset`), names both remotes, and reconciles a recorded
    push-state against BOTH real remotes (`git ls-remote` each — L055); a push counts as done only
    when both show the same tip. § 4 "unpushed commits" line reports both.
  - `docs/SESSION_CLOSER.md` 1.6 → 1.7 — § 1.1 probes both remotes and states the push rule (every
    push to both, `--tags` to both on a release; done = `ls-remote` on both shows HEAD); § 1.4
    push-state flip only after both; § 4 "Unpushed" line reports both.
- **PLAN-016 0.2 → 0.3 — mechanical anchor shift (no design change; PLAN-011 0.4 precedent):** this
  commit took SESSION_OPENER 1.19 + SESSION_CLOSER 1.7, the numbers PLAN-016 § 6f / § 6g had reserved,
  so their header + CHANGE LOG FINDs now anchor on 1.19 / 1.7 and write 1.20 / 1.8 (§ 6h version list
  follows). Verified mechanically: the eight § 6f / § 6g blocks, re-extracted from the plan file, each
  match the live files exactly once and apply cleanly in order (results keep this commit's wording).
  Status stays APPROVED.
- **QA scenarios:** exempt per Rule 11 (governance-doc edits + plan bookkeeping, no tool behavior).
- **Versions:** SESSION_OPENER 1.18 → 1.19, SESSION_CLOSER 1.6 → 1.7, PLAN-016 0.2 → 0.3, manifest
  2.54 → 2.55. Impact: no runtime impact; every session now probes, pushes and verifies both remotes.

## [2026-10-05] — Second push remote: the vault is also on GitHub (`780-AI/780-Docset`)

- **Type:** Governance doc (Rule 14 machine-migration catalog) + repository hosting. Doc-only — no
  engine change, no Set Version change, no Critical File content touched (manifest cell only).
- **Operator decisions (2026-10-04/05):** push this repo to GitLab (unchanged, the CI of record) AND
  GitHub, inside the 780-AI organization; the repo as-is (operator accepted that org members can read
  the EverOn project MENTIONS in the vault's files and history — the EverOn code itself stays on
  private GitLab only); org members view-only (780-AI base permission = Read, operator-confirmed),
  only the operator writes; every push goes to both remotes (no server-side mirror). Operator created
  the private, empty repo `780-AI/780-Docset`.
- **Setup on this Mac:** github.com's three host keys trusted only after matching GitHub's published
  fingerprints (`api.github.com/meta`); this Mac's push key added to the operator's GitHub account
  (`ssh -T git@github.com` → "Hi yaserkho!"); `github` remote added (`.git/config` — travels with the
  folder). Pre-publish scan of the tracked tree + full history: no passwords, tokens or private keys
  (only the `test_password` example in a CI template).
- **Fix:** `docs/NEW_MACHINE_SETUP.md` 1.3 → 1.4 — § 1 checks both remotes (+ how a fresh clone
  re-adds `github`); § 3 registers the push key on GitHub too and records github.com's trusted
  fingerprints as the new-machine trust anchor; catalog intro names it.
- **Deferred (same session decision):** `SESSION_OPENER` § 1.1 (push-state reconcile on both remotes)
  and `SESSION_CLOSER` (push to both) — both files are anchored verbatim by the approved PLAN-016
  § 6f / § 6g, so they change right after PLAN-016 ships; until then every push runs to both remotes
  and is verified with `ls-remote` on each.
- **Versions:** NEW_MACHINE_SETUP 1.3 → 1.4, manifest 2.53 → 2.54. Impact: no runtime impact.
  Rule 11 exempt (governance-doc edit, no tool behavior change).

## [2026-10-04] — QA bookkeeping: 780-VPN E001 write-back closes v2.6 QA-E4 = PLAN-012 QA-H6 = PLAN-013 QA-K5

- **Type:** Plan/QA bookkeeping (post-close annotations, the PLAN-010 QA-I precedent). No behavior
  change.
- **What:** the 780-VPN E001 write-back ran in the 2026-10-04 `integrate --apply --write` (Rule 16
  gate, operator "Q1. yes to all"; record in the PLAN-011 closure entry below). It is the named
  trigger of one scenario carried under three ids:
  - **v2.6 QA-E4** — Status written back: `integrated → vault L079 (PROJECT_STANDARDS § 5.6, Set
    Version v2.6)` (the log diff is exactly that line); `harvest` shows no open 780-VPN entry.
  - **PLAN-012 QA-H6** — feature-ON write-back half: the write-back left its record in the target's
    handoff (`### Write 3` — integrate write-back, Set v2.7, 2026-10-04, `docs/STANDARDS_LOG.md`).
  - **PLAN-013 QA-K5** — accumulation, write-back half: the path that ran was **append to an
    accumulating handoff** (Writes 1–2 from 2026-10-03 preserved; the diff is a pure addition), not
    the `### Write 2` path anticipated on 2026-10-03 — the v2.7 fleet write had taken Write 2
    first. QA-K6's K5 half re-run: `sync --project 780-VPN` dry-run up-to-date 11/11.
  The ⏸ lines in the v2.6, v2.5 (PLAN-012) and PLAN-013 entries below are flipped in place; the
  trackers carry the evidence.
- **QA scenarios:** exempt per Rule 11 (bookkeeping/record; this entry IS the QA record).
- **Versions:** PLAN-012 tracker 1.2 → 1.3, PLAN-013 tracker 1.1 → 1.2, manifest 2.52 → 2.53.
  Impact: none at runtime.

## [2026-10-04] — PLAN-011 CLOSED: EverOn.Equinex registered — fourth sync target; log round-trip proven

- **Type:** Registry change (Critical File `config/projects.toml`) + plan closure under § 15 plan
  PLAN-011 (Phase 3c, § 7.4 ALLOWLIST — 6 files). No engine change, no Set Version change.
- **What:** EverOn.Equinex (adopted onto Set v2.7 on 2026-10-03, Equinex `3f65388`; EverOn own line
  retired) joins the registry as a local `~/` target (§ 5A) with its SESSION_OPENER § 2 row (§ 5B,
  → 1.18). The same SESSION_OPENER version and the 780-VPN registry comment carry an
  operator-confirmed correction: 780-VPN's old ssh host was the operator's own second Mac (account
  `parsaazad`), not a team member's machine.
- **Rule 16 gate (2026-10-04):** fleet `harvest` gathered 3 open entries (780-Automation unreachable
  — ssh timeout; its E001–E012 were not gathered and await their own gate). Presented with source,
  plain-language explanation, effect and recommendation per item; operator: *"Q1. yes to all"*
  and *"no session is open"* (Equinex idle):
  - 780-VPN E001 → write back `integrated → vault L079 (PROJECT_STANDARDS § 5.6, Set Version v2.6)`
    (approved at the v2.6 gate; only the write-back had been held). Its QA flips (v2.6 QA-E4 =
    PLAN-012 QA-H6 = PLAN-013 QA-K5) ride a separate bookkeeping commit.
  - Capital-Signal E002 (locality script `link`/`adopt` abort on a harness-created `memory/`;
    `status` names the wrong verb) → genericize-then-integrate at **v2.8**; Status stays `open`
    until then. Vault-verified real (`scripts/claude_project_data.sh` :51, :62-72, :94-98); the
    script is not a SYNC_MAP item, so v2.8 must also decide how the fix reaches existing adopters.
  - EverOn.Equinex E001 (the § 5F seeded verification entry) → rejected.
- **Write-back:** clock 16:14:30 UTC = gitlab.com 16:14:31; `integrate --apply` dry-run showed
  exactly the two approved lines; `--write` changed one Status line in each log. 780-VPN's handoff
  gained `### Write 3` (accumulated on Writes 1–2); Equinex received its first handoff
  (`### Write 1`) — its next session lands it first.
- **QA scenarios (Rule 11 / Rule 15 — statuses live in `PLAN-011_tracker.md`):**
  - ✅ QA-F5 ⚑ — Equinex adoption (2026-10-03, Equinex session; evidence recorded in the tracker).
  - ✅ QA-F6 ⚑ — `status` v2.7 / v2.7 current; `sync --project EverOn.Equinex` dry-run up-to-date
    11/11 (re-run 2026-10-04 after the write-back: unchanged, plus the un-landed-handoff note).
  - ✅ QA-F7 ⚑ — harvest surfaced Equinex E001 → write-back read back verbatim
    (`- Status:      rejected — seeded verification entry (PLAN-011 QA-F7)`) → re-run `harvest`:
    1 open entry (Capital-Signal E002), none for Equinex.
  - ✅ QA-F8 — own line retired: the seven § 5E.4 files gone, SVA v2.7 / `0e03e10`, legacy freeze
    banner + crosswalk, CLAUDE.md rule headings == template (15), § 15.9 present.
- **Versions:** SESSION_OPENER 1.17 → 1.18, PLAN-011 plan + tracker 0.4 → 1.0/CLOSED, manifest
  2.51 → 2.52. Impact: every engine command now includes EverOn.Equinex (fleet = 4 targets);
  780-VPN and Equinex each hold an un-landed write-back handoff for their next sessions.

## [2026-10-04] — PLAN-016 Phase 2 APPROVED — "plan 016 is approved"

- **Type:** Plan approval record (§ 15 Phase 2). No behavior change.
- **Decisions (plan § 9.1):** D-1 / D-2 / D-4 / D-5 = A (status/drift regenerate the file; unknown
  registry keys are an error; ssh fails fast; a missing file blocks a local push). D-3: 780-VPN
  `owner` → `operator` (operator: the owner is Yaser Khosravi, the operator); Capital-Signal and
  Equinex confirmed as `EverOn`, not 780 projects; every other value as proposed. The § 6a.4
  registry block was updated and re-proven (85 blocks re-extracted from the plan file —
  byte-identical; ruff clean, mypy 0, pytest 140).
- **Next:** Phase 3 in a fresh session, after the PLAN-011 closure commit (both plans touch
  `config/projects.toml` + `docs/SESSION_OPENER.md`).
- **QA scenarios:** exempt per Rule 11 (approval record); QA-L1…L8 remain ⏸ in the tracker.
- **Versions:** PLAN-016 + tracker 0.1 → 0.2, manifest 2.50 → 2.51. Impact: none at runtime.

## [2026-10-04] — PLAN-016 DRAFT: fleet view — `docs/fleet.csv`, generated and always current

- **Type:** Plan design commit (§ 15.9 intake → Phase 0 + Phase 1; Rule 1). No behavior change.
- **What:** Drafts PLAN-016 + sibling tracker for the operator's request (2026-10-04): one CSV with
  all fleet information, always up to date. Operator decisions: the proposed columns (registry
  facts / live state / run metadata), NOT committed (gitignored), engine-generated, at
  `docs/fleet.csv`. Design: fixed facts become optional, validated fleet-information keys in
  `config/projects.toml` (unknown keys rejected); one shared probe feeds `status` / `drift` / a new
  `fleet` command, each regenerating the file, and every `sync --write` / integrate write-back
  re-probes and regenerates it; an unreachable target keeps its last-known values; a local pre-push
  gate in `check_doc_coverage.py` fails while the file is missing or disagrees with the registry
  (skipped in CI); session opener/closer steps. D-4 proposes ssh fail-fast (`ConnectTimeout=10`,
  `BatchMode=yes`). Code proven first in a scratch overlay (ruff clean; mypy --strict 0 errors;
  pytest 140 = 120 + 20 new) and previewed read-only on the real fleet (75 s → 10.1 s with D-4);
  Rule 13 pass re-extracted all 85 blocks from the plan file onto a fresh tree — byte-identical
  and green for both D-4 variants. Decisions D16.A + D-1…D-5 await the operator; Phase 3 runs after
  the PLAN-011 closure commit.
- **QA scenarios:** exempt per Rule 11 (design-only commit); QA-L1…L8 defined in plan § 8 and
  tracked in `PLAN-016_tracker.md` (⏸).
- **Versions:** PLAN-016 + tracker 0.1 (new), manifest 2.49→2.50. Impact: none at runtime.

## [2026-10-04] — Rule 14 catalog gap closed: ssh-target access in NEW_MACHINE_SETUP

- **Type:** Governance doc (Rule 14 machine-migration catalog). Minor — doc-only; no engine change,
  no Set Version change, no Critical File touched.
- **Gap:** since the first ssh registration (780-Automation, 2026-08-19) the engine has depended on
  two pieces of machine-local state the catalog never named — this machine's key authorized on the
  target (`ssh-copy-id`) and the target's host keys in `~/.ssh/known_hosts`. A new or re-homed
  machine would hit an unreachable target with no recorded recovery path, and had no trust anchor
  for the first host-key prompt. Rule 14 says out-of-folder state is cataloged "same-commit"; this
  closes the lapse (flagged at the 2026-10-04 wrap-up as Major-defect class).
- **Fix:** `docs/NEW_MACHINE_SETUP.md` 1.2 → 1.3 — new § 3.1 ssh-target access: keyscan → compare
  fingerprints → `ssh-copy-id` → BatchMode probe → `status`; answer `yes` to a host-key prompt only
  on a fingerprint match, otherwise stop. Records 780-Automation's trusted SHA256 fingerprints
  (read from this machine's `known_hosts`; ED25519 matched at all three DHCP addresses it has held).
  New ssh targets add their row same-commit. Catalog intro + opening paragraph name the entry.
- **Versions:** NEW_MACHINE_SETUP 1.2 → 1.3, manifest 2.48 → 2.49 (cell 58 + Last-updated rotation).
- **Impact:** no runtime impact. Rule 11 exempt (governance-doc edit, no behavior change).

## [2026-10-03] — Set v2.7 delivered fleet-wide (PLAN-011 QA-F4) + 780-Automation re-pointed to 172.16.10.245

- **Type:** Registry change (Critical File `config/projects.toml` — operator-supplied DHCP IP,
  identity verified before re-pointing, the 2026-08-27 precedent) + plan bookkeeping. No engine
  change, no Set Version change.
- **780-Automation re-point:** the operator supplied the new address 172.16.10.245 (unreachable at
  .11.60 since 2026-09-08). Before trusting it: its ED25519 / RSA / ECDSA host keys were compared
  with the keys already trusted for .10.61 / .11.60 — all three identical — then added to
  `known_hosts`; identity probe: same repo (`/Users/a780/Projects/780-Automation`, origin
  `780-AI/780-Automation`, bootstrap `cb62527` in history), clean tree, Set v2.5, **no handoff** —
  the v2.5 write had been landed and the handoff deleted target-side (a third QA-H5-pattern data
  point). Registry `ssh_host` + SESSION_OPENER § 2 row (→ 1.17) updated.
- **Delivery (`sync --write` of release `0e03e10`):** clock 14:46:51 UTC = gitlab.com 14:46:52;
  no session mid-work in 780-VPN (no file changed in 3 h) or Capital-Signal. Capital-Signal 4 files
  (handoff → `### Write 3`), 780-Automation 5 (catch-up v2.5 → v2.7: CLAUDE.md merge +
  PROJECT_STANDARDS replace + LESSONS replace + SVA record + a new handoff), 780-VPN 4 (its
  pre-accumulation handoff wrapped as Write 1 + `### Write 2`). 780-Automation's dry-run was
  checked first per the discard-class rule: CLAUDE.md hunks identical to the reviewed v2.7 delta,
  PROJECT_STANDARDS = the v2.6 § 5.6 addition, LESSONS additive (L079–L081).
- **Finding (not acted on — Rule 16):** 780-Automation's `docs/STANDARDS_LOG.md` holds **12 open
  entries (E001–E012)**, codified target-side 2026-09-05 (`c097780`) — the L069 log channel
  working as designed. They await a `harvest` + the Rule 16 list-and-confirm gate; nothing
  integrated.
- **QA scenarios (Rule 11 / Rule 15):**
  - ✅ QA-R1 (re-point) — host-key match + identity probe above; `status` resolves
    `ssh:a780@172.16.10.245:…` and reports v2.7 / v2.7 current; a real write + read-back landed
    over the new address.
  - ✅ QA-F4 ⚑ (PLAN-011) — written files + handoffs read back on all three (§ 15.9, the Rule 14
    bullet and L080–L081 present; § 5.6 + L079 on 780-Automation; PROJECT-OWNED 4/4 each);
    immediate re-run up-to-date ×3; `status` v2.7 / v2.7 current ×3 (open-log: CS 0,
    780-Automation 12, 780-VPN 1 = E001 awaiting its write-back).
- **Versions:** SESSION_OPENER 1.16→1.17, PLAN-011 plan + tracker 0.3→0.4 (Phase 3a closed; § 5B
  anchor shifted to 1.17→1.18), PLAN-013 tracker 1.0→1.1 (Phase 5 push recorded — `ls-remote`
  verified `b65037c`), manifest 2.47→2.48. Impact: every engine command now reaches 780-Automation
  at the new address; all three targets hold v2.7 as uncommitted engine writes + handoffs for
  their next sessions to land.

## [2026-10-03] — Standard Set Version v2.7: fleet-convergence intake from EverOn.Equinex — L080 feature intake + L081 cloud-synced folders (PLAN-011 Phase 3a)

- **Type:** Standards-suite release (Critical Files `docs/standards/` + root `CLAUDE.md` + the
  manifest, plus the delivery skill's `skill/modes/adopt.md` — doc-only, no engine change) under
  § 15 plan PLAN-011 (Phase 3a, § 7.2 ALLOWLIST — 12 files, unamended: every confirmed item landed
  in an ALLOWLIST file).
- **Rule 16 gate record (QA-F1):** delta re-verified at Equinex's tip first (still `cf25e70`;
  `git log cf25e70..HEAD` empty; only the known untracked brief) → the complete list was C1–C7,
  presented in chat 2026-10-03 with source, plain-language explanation, exact integration effect
  and recommendation per item. Operator: *"confirmed as recommended"* — C1–C4 integrated
  (genericized), C5–C7 kept local, and the out-of-plan scope question answered (a).
- **What:**
  - **C1 → L080 + template CLAUDE.md § 15.9 Feature intake (before Phase 0)** (D-6 = A): every new
    feature and every feature document enters through preserve (idea source, binds nothing,
    adopt / deviate per item) → investigate the live source → redesign from scratch → § 15 plan;
    pointer in the § 15.2 Phase 0 row. Source: Equinex `CLAUDE.md` Rule 16 (v3.12/v3.13) + their
    L062. Step 3's domain specifics genericized (restart-surviving state persisted; reachable
    release for every threshold pair; the deployment-variant check dropped).
  - **C2 + C3 + C4 → L081 + a Rule 14 cloud-synced-folder bullet:** one machine at a time
    (conflicted copy inside `.git/` = corruption), sync settled on both sides before switching,
    folder pinned offline, `link` per machine, push when a batch completes, gitignored ≠
    sync-ignored (accept or exclude), git identity before a fresh clone's first commit. Source:
    Equinex `docs/MACHINE_MIGRATION.md` v0.3 § 6.1 / § 4 / § 6.2.
  - **§ 5D.0 drift fix:** Rule 12 step 6 → "`/tmp/` cleanup + locality confirm" in template + root
    (had lagged SESSION_CLOSER § 1.6 since v1.5 — L063 class).
  - **§ 5C (S2):** `skill/modes/adopt.md` § 3 lessons-archive bullet made explicit — the suite's
    `archive/LESSONS.md` is a replace item, so a converging project's own archive is classified
    entry-by-entry and preserved verbatim as `archive/LESSONS_LEGACY.md` with a numbering
    crosswalk (D-2 = A).
  - **Own-instance reconcile:** root `CLAUDE.md` → 1.9 mirrors § 15.9, the Rule 14 bullet and the
    step-6 fix (rule count stays 16 — the vault's Rule 16 harvest gate keeps its number); vault
    `archive/LESSONS.md` gains the L080–L081 provenance entry (dual-voice, L068).
  - **Counts** 79 → 81 (INDEX § 1 / § 2 / § 3, README, SVA — recomputed: `grep -c '^### L0'` = 81).
- **Intake notes — kept local (operator-confirmed):** C5 delegated subsystem manifest tracking
  (their Rule 8 bullet), C6 committed canonical config as the single QA base (their § 4), C7
  optional orientation-graph aid (their SESSION_OPENER § 1.5) — Equinex customizations, carried
  into PROJECT-OWNED blocks / the project annex at its adoption (Phase 3b); C5/C6 portable kernels
  may return as Equinex `E0NN` entries. Non-log intake (Equinex has no STANDARDS_LOG yet) — no
  write-back applies.
- **Label note (R6):** vault Set **v2.7** ≠ Equinex's own-line "Set v2.7" (its STANDARDS_INDEX);
  their L062 = vault L080. The full crosswalk lands in their `archive/LESSONS_LEGACY.md` at
  adoption.
- **Out of scope (operator, scope (a)):** the vault-authored lesson candidates queued for "v2.7"
  (handoff accumulation; adopt-mode archive gap; the PLAN-013 D2 round-trip family) ship later as
  their own small release (v2.8), keeping this release's delta exactly the plan's.
- **QA scenarios (Rule 11 / Rule 15 — statuses live in `PLAN-011_tracker.md`):**
  - ✅ QA-F1 — Rule 16 gate record (above).
  - ✅ QA-F2 — plan grep over `docs/standards/` + `skill/` → no output (exit 1); intake-surfaced
    names (dropbox, survival, backoffice, cloudzy, mt5, ea, monitor, telemetry, preset, trading,
    tester) absent from every added line (exit 1).
  - ✅ QA-F3 ⚑ — engine-as-oracle dry-run (pre-commit): Capital-Signal AND 780-VPN each show
    EXACTLY `CLAUDE.md` merge + `archive/LESSONS.md` replace + `docs/SET_VERSION_ADOPTED.md`
    record (+ the un-landed-handoff note), nothing else; `--diff`: the CLAUDE.md hunks are exactly
    the step-6 fix, the Rule 14 bullet + see-line, the § 15.2 pointer and § 15.9 (plus the engine
    header stamp), identical on both targets; LESSONS +82 lines, additive only; no clock warning.
    780-Automation unreachable (ssh timeout) — catch-up when back.
  - ✅ QA-F4 ⚑ — 2026-10-03, post-commit (evidence in the fleet-delivery entry above): `sync
    --write` to Capital-Signal (`### Write 3`), 780-VPN (record 1 + `### Write 2`) AND 780-Automation
    (back at a new IP — catch-up v2.5 → v2.7); handoffs read back; re-run up-to-date ×3; `status`
    current ×3.
- **Versions:** template CLAUDE.md 1.6→1.7, root CLAUDE.md 1.8→1.9, STANDARDS_INDEX 2.6→2.7,
  standards README 1.4→1.5, SET_VERSION_ADOPTED 1.14→1.15, adopt.md 0.2→0.3, manifest 2.46→2.47,
  PLAN-011 plan + tracker 0.2→0.3 (EXECUTING); both LESSONS files +L080/L081 (headers unchanged per
  the no-per-lesson-bump practice). Impact: standards content release — no engine behavior change;
  adopters receive a 3-item delta (CLAUDE.md merge + LESSONS replace + SVA record) plus the handoff.

## [2026-10-03] — PLAN-013 Phase 3: engine write safety — clock floor + accumulating handoffs

- **Type:** Engine behavior change (Major per § 4 — Critical Files touched; § 15 plan Phase 3,
  single commit). Engine-only: no `docs/standards/` change → **no Set Version bump, no tag**.
- **What:** Both engine write paths (`sync --write` and the `integrate --write` write-back) now
  (1) **refuse when the local clock is behind the target's newest stamp** — `sync.newest_stamp`
  reads stamp positions only (`Last Updated` headers + `vX.Y — date — ` change-log lines across
  the SYNC_MAP files + `docs/STANDARDS_LOG.md`); `sync.check_clock` raises before any file is
  touched (integrate checks EVERY target before the first write; sync isolates the refused
  target, exit 1) — the engine half of 780-VPN E001 (L079); and (2) **append to an un-landed
  `docs/SYNC_HANDOFF.md`** instead of overwriting it — earlier records kept verbatim, the new
  write added as the next `### Write N` (a pre-accumulation handoff is wrapped as record 1; an
  unrecognized file is kept in a fence). The sync dry-run gains two informational lines (clock
  warning; un-landed-handoff note). Architecture § 7 + § 9 updated (§ 4 drift rule); PLAN-012
  § 11 clock-caveat risk annotated CLOSED (§ 15.4). Engine: sync.py 0.2→0.3, cli.py 0.6→0.7,
  test_sync.py 0.1→0.2 (+5 unit + 1 D2 regression), test_cli.py 0.6→0.7 (+3 end-to-end).
- **Fleet effect:** Capital-Signal's v2.6 hold LIFTED — delivered as QA-K4 (handoff now lists
  v2.5 + v2.6); fleet: CS v2.6 + 780-VPN v2.6 current, 780-Automation unreachable (v2.5 —
  catch-up when back). PLAN-011 § 9.1 pre-write hold lifted (accumulation shipped).
- **QA scenarios (Rule 11/15 — statuses live in `PLAN-013_tracker.md`):**
  - ✅ QA-K1 — ruff clean; mypy error set identical (42 full / 25 `src`); pytest 120 passed
    (119 planned + 1 D2 regression).
  - ✅ QA-K2 ⚑ — fleet dry-run vs the HEAD engine: only the two new handoff notes differ; no
    false clock warning; changed-item lists identical.
  - ✅ QA-K3 ⚑ — scratch copy of Capital-Signal with a stamp moved to tomorrow: dry-run warns,
    `--write` exits 1 "clock is behind", copy byte-unchanged (76 files); scratch removed.
  - ✅ QA-K4 ⚑ — Capital-Signal v2.6 `sync --write` (operator "go k4"): exactly 4 files changed
    (3 + handoff); handoff = `Write 1 — earlier engine write` (v2.5 verbatim) + `Write 2` (v2.6).
  - ✅ QA-K5 ⚑ — write-back half (2026-10-04, at the E001 write-back = v2.6 QA-E4 = PLAN-012
    QA-H6): appended `### Write 3` to 780-VPN's accumulating handoff (see the QA bookkeeping entry).
  - ✅ QA-K6 — dry-run re-run up-to-date on CS + 780-VPN with the handoff present (K5 half
    2026-10-04: 780-VPN up-to-date 11/11 after the write-back).
- **Plan defect D2 (found at the Rule 10 review, operator D2 = A):** the approved § 5b code
  located the handoff's § 2 anchor with `find`, so a later write truncated a fenced
  unrecognized handoff containing its own § 2 heading (content silently lost — reproduced).
  Fixed with `rfind` + a regression test that fails on the unfixed code; the one recorded
  deviation from the approved § 5.
- **Known cosmetic (plan § 11 R7):** a sync refusal prints the project name twice; message
  content correct; shipped as approved (operator D1 = A).
- **Versions:** sync 0.2→0.3, cli 0.6→0.7, test_sync 0.1→0.2, test_cli 0.6→0.7, architecture
  0.12→0.13, PLAN-012 1.0→1.1, PLAN-013 + tracker 0.2→1.0/CLOSED, manifest 2.45→2.46.
- **Impact:** YES — behavior changes: an engine write is refused (nothing written) when the
  local clock is behind the target's newest stamp; a write into a target holding an un-landed
  handoff appends to it instead of replacing it; the sync dry-run prints up to two new
  informational lines. Dry-run planning, the integrate worksheet and read-only commands are
  otherwise unchanged.

## [2026-10-03] — PLAN-013 APPROVED (Phase 2): "approve plan 013"

- **Type:** Plan approval record (no behavior change).
- **What:** Operator approval landed on the v0.1 draft; plan + tracker → 0.2 / APPROVED. Decision
  record in plan § 9.1: D-1…D-4 = A (offline floor guard, accumulate, strict, no override — the
  options the § 5 code implements); D-5 = A (Capital-Signal's v2.6 catch-up is QA-K4, its write
  gated on the operator naming the target at QA time). Phase 3 (single commit, 10-file ALLOWLIST,
  engine-only — no Set Version bump) follows in this fresh session per § 15.3; its reconcile pass
  already ran clean (17/17 FIND blocks match live source exactly once).
- **QA scenarios:** exempt per Rule 11 (approval record); QA-K1…K6 stay in `PLAN-013_tracker.md`.
- **Versions:** PLAN-013 + tracker 0.1→0.2, manifest 2.44→2.45. Impact: none at runtime.

## [2026-10-03] — PLAN-013 DRAFT: engine write safety — clock floor + accumulating handoffs

- **Type:** Plan design commit (§ 15 Phase 0 + Phase 1; Rule 1). No behavior change.
- **What:** Drafts PLAN-013 + sibling tracker for the two live engine write-path defects:
  (1) the engine stamps "today" from an unchecked wall clock (780-VPN E001's engine half, L079)
  → both write paths compute the target's newest stamp and refuse when the clock reads earlier;
  the sync dry-run warns; (2) every write OVERWRITES `docs/SYNC_HANDOFF.md`, hiding earlier
  un-landed writes (live: Capital-Signal 7 modified files vs a 3-file handoff) → un-landed
  records are kept and the new write appended as `### Write N` (pre-accumulation handoffs
  wrapped; unrecognized ones kept verbatim). Engine-only — no Set Version bump. Code proven
  first in a scratch overlay (ruff clean; mypy error set identical; pytest 119 = 111 + 8 new)
  and previewed read-only on real fleet data; Rule 13 pass re-extracted all 17 blocks from the
  plan file and re-proved them. Decisions D13.A + D-1…D-5 await the operator.
- **QA scenarios:** exempt per Rule 11 (design-only commit); QA-K1…K6 defined in plan § 8 and
  tracked in `PLAN-013_tracker.md` (⏸).
- **Versions:** PLAN-013 + tracker 0.1 (new), manifest 2.43→2.44. Impact: none at runtime.

## [2026-10-03] — PLAN-011 Phase 2 APPROVED ("plan 011 is appvoved")

- **Type:** Plan approval record (no behavior change).
- **What:** Operator approved PLAN-011 on the request naming D-1 = Equinex only and D-2 = A.
  Decisions recorded in plan § 9.1: D-3 fleet grows later one by one; D-4 start immediately
  (Equinex idle); D-5 E001 first — already shipped as v2.6, so this plan's release is v2.7 and
  C1's lesson L080 (the R6 label clash with Equinex's own-line "v2.7" now exact — to be stated
  explicitly at release + adoption); D-6 = A (§ 15.9). Execution delta from the 2026-10-03
  handoff-overwrite finding: Phase 3a holds any target with an un-landed `docs/SYNC_HANDOFF.md`
  unless PLAN-013 ships first. The operator's org-wide expansion (20+ non-AI-native GitHub-org
  repos of one super-application — AI-enabled, delivered as reviewed PRs; cross-repo governance
  leaning "each repo stands alone", decided after the scan) is routed to PLAN-013 → PLAN-014 →
  PLAN-015. Phase 3a runs in a NEW session per § 15.3.
- **QA scenarios:** exempt per Rule 11 (approval record).
- **Versions:** PLAN-011 + tracker 0.1 → 0.2, manifest 2.42 → 2.43. Impact: none at runtime.

## [2026-10-03] — Standard Set Version v2.6: clock trust — 780-VPN E001 integrated as L079 (second harvested adopter entry)

- **Type:** Standards-suite release (Critical File `docs/standards/` — doc-only, no engine change;
  Major workflow without a § 15 plan per the § 15.6 doc-only carve-out — the v2.1 / v2.3
  precedent, operator-approved route).
- **Rule 16 gate record:** harvest listed exactly ONE open entry — 780-VPN `docs/STANDARDS_LOG.md`
  E001 "Stamp sync output from a trusted clock, not the curator machine's wall clock" (2026-09-05,
  governance, general) — presented in chat 2026-10-03 with explanation, exact integration effect
  and recommendation (genericize → integrate; merge the vault's own "verify skew direction
  externally" candidate; engine half to its own plan). Operator: *"first the E001 is approved and
  ship it first"*.
- **What:** Lesson **L079** (the machine clock is an untrusted input — verify against an external
  authority before stamping or recording skew) added genericized to the canonical LESSONS and
  project-specific to the vault archive (dual-voice, the L068 precedent). PROJECT_STANDARDS →
  1.1: new **§ 5.6** (a new change-log line must not be dated earlier than the line below it;
  external clock check on a new machine or before stamping into other repositories; skew direction
  measured, never inferred; wrong stamps corrected with an explicit annotation). Counts 78 → 79
  (INDEX § 1 / § 2 / § 3, README, SVA — L060 sweep, live sites grep-clean). E001's engine half (a
  trusted "today" / newest-stamp floor + refuse when behind) is behavior-affecting in a Critical
  File → routed to its own plan (PLAN-013 candidate).
- **Delivery held by design (new finding):** the PLAN-012 handoff is OVERWRITTEN by each engine
  write — un-landed writes do not accumulate, so a second write hides the first's file list.
  Observed live: Capital-Signal holds 7 engine-modified files (v2.1 → v2.5) while its handoff lists
  only v2.5's 3. Therefore: (1) **Capital-Signal held** at v2.5 until a CS session lands its
  backlog (another write would bury one more version); (2) the **E001 write-back is deferred**
  until 780-VPN lands this v2.6 handoff (a write-back now would overwrite it) — PLAN-012 QA-H6
  moves with it. The overwrite gap is an engine follow-up (pairs with E001's engine half).
  780-Automation unreachable (ssh refused since 2026-09-08).
- **QA scenarios (Rule 11 / Rule 15):**
  - QA-E1 ✅ 2026-10-03 — domain-neutral gate: `grep -rniE` for every fleet identifier over
    `docs/standards/` + `skill/` → no output (exit 1).
  - QA-E2 ✅ 2026-10-03 — engine-as-oracle dry-run (pre-commit): 780-VPN AND Capital-Signal each
    show EXACTLY `docs/standards/PROJECT_STANDARDS.md` replace + `archive/LESSONS.md` replace +
    `docs/SET_VERSION_ADOPTED.md` record, nothing else.
  - QA-E3 ✅ 2026-10-03 — feature-ON: clock verified (gitlab.com `Date:` = `date -u`, 1s);
    `sync --project 780-VPN --write` wrote + flushed 4 files incl. the handoff (v2.6, run date
    2026-10-03, the 3-file list — read back); spot-greps: L079 present, § 5.6 present, SVA reads
    v2.6; immediate re-run up-to-date 11/11; `status` 780-VPN v2.6/v2.6 current (open-log 1 =
    E001 awaiting the deferred write-back), CS behind (held), 780-Automation unknown.
  - QA-E4 ✅ 2026-10-04 — write-back: `integrate --apply --write` E001 →
    `integrated → vault L079 (PROJECT_STANDARDS § 5.6, Set Version v2.6)` + handoff spot-read
    (= PLAN-012 QA-H6); `harvest` = 0 open 780-VPN entries (see the 2026-10-04 QA bookkeeping
    entry; ran once PLAN-013 accumulation lifted the overwrite hold — no landing needed first).
- **Versions:** PROJECT_STANDARDS 1.0→1.1, STANDARDS_INDEX 2.5→2.6, standards README 1.3→1.4,
  SET_VERSION_ADOPTED 1.13→1.14, manifest 2.41→2.42; both LESSONS files +L079 (headers unchanged
  per the no-per-lesson-bump practice). Impact: standards content release — no engine behavior
  change; 780-VPN received the 3-file delta + handoff.

## [2026-10-03] — PLAN-011 DRAFT: fleet convergence — Equinex intake + adoption (EverOn line retirement)

- **Type:** Plan design commit (§ 15 Phase 0 + Phase 1; Rule 1). No behavior change.
- **What:** Drafts PLAN-011 + sibling tracker. The live fleet already has Capital-Signal,
  780-Automation and 780-VPN converged + registered (v2.5), so the plan converges the last known
  project, EverOn.Equinex: intake first (Rule 16 gate) → one Set release synced to the fleet →
  adopt in a dedicated Equinex session (dry-run gated) → register + prove the STANDARDS_LOG
  round-trip. Phase 0 (read-only, Equinex tip `cf25e70`): Equinex holds ONE lesson + ONE rule the
  vault lacks (its L062 / Rule 16 — feature-intake workflow) plus uncodified machine-migration
  guidance (synced-folder rules, git-identity check); everything else maps per PLAN-010.
  Adoption complications catalogued (rule R14↔R15 swap + Rule 16 collision, own L050–L062 ≠ vault
  numbering with 221 plan citations, zero PROJECT-OWNED markers, header-less session files,
  equal-stamp divergent locality script, clean-tree gate failing on one untracked brief). Two
  vault-side defects found and scheduled into the release: the adopt-mode spec gap (adopt.md § 3
  vs the `archive/LESSONS.md` replace item) and Rule 12 step-6 drift (template + root CLAUDE.md
  vs SESSION_CLOSER § 1.6 since v1.5, L063 class). Rule 13 pass RUN (code blocks extracted and
  executed through the engine; anchors byte-verified; 6 findings fixed in place). Decisions
  D11.A + D-1…D-6 await the operator (new: D-2 archive home, D-6 feature-intake landing under the
  only-append rule-numbering principle).
- **QA scenarios:** exempt per Rule 11 (design-only commit); QA-F1…F8 are defined in the plan § 8
  and tracked in `PLAN-011_tracker.md` (⏸).
- **Versions:** PLAN-011 + tracker 0.1 (new), manifest 2.40→2.41. Impact: none at runtime.

## [2026-10-03] — Bookkeeping: PLAN-012 QA-H5 ✅ — the handoff loop closed in a real target

- **Type:** Bookkeeping (post-close QA annotation; no vault behavior change).
- **What:** QA-H5 (loop closure — a target session reads the handoff, lands the changes per its
  § 2, and deletes it; first observation closes) is observed in 780-VPN commit `de1de37`
  (2026-09-05): the three engine-written v2.5 files + the adopter bookkeeping (manifest cells,
  docs/README, CHANGELOG) landed in one commit BEFORE the session's feature work, and
  `docs/SYNC_HANDOFF.md` was deleted in the same landing (untracked engine-transient — no git
  trace; evidence = commit body + file absent on disk + clean tree). Found by the 2026-09-08
  read-only probe; flip operator-authorized 2026-10-03. Contrast: Capital-Signal still holds its
  engine writes + handoff uncommitted (v2.1→v2.5) — the open uncommitted-fragility lesson
  candidate, not a QA-H5 concern. QA-H5 flipped in the v2.5 release entry below; tracker
  annotated. QA-H6 remains open at its named trigger (the 780-VPN E001 intake).
- **QA scenarios:** exempt per Rule 11 (bookkeeping/record; this entry IS the QA-H5 record).
- **Versions:** PLAN-012 tracker 1.1→1.2, manifest 2.39→2.40. Impact: none at runtime.

## [2026-10-03] — 780-VPN re-pointed ssh → local `~/` (shared Dropbox folder)

- **Type:** Registration update (Critical File `config/projects.toml`; no engine change).
- **What:** Operator decision ("switch the 780-vpn to local folder"). Both team-Mac ssh hosts have
  been unreachable on port 22 since 2026-09-08 (both refused then; 2026-10-03: 172.16.11.17
  times out, 172.16.11.60 refuses), leaving 780-VPN `unknown` and its open E001 unharvestable. The repo lives in a Dropbox folder SHARED with the
  team member's account, which also syncs to the curator machine at
  `~/Library/CloudStorage/Dropbox/Projects/780-VPN` — the registry entry now uses that `~/` path
  (local transport; the registry expands `~` per machine, the Capital-Signal pattern). Identity
  verified BEFORE re-pointing: same origin `git@github.com:780-AI/780-VPN.git`, bootstrap
  `be4d6d3` + both sync landings (`630f508`, `de1de37`) in history, SVA on Set v2.5, clean tree
  at `e739ff9` = `origin/main`. Drops the DHCP-IP dependency; the one-machine-at-a-time caution
  now spans BOTH Dropbox accounts (registry NOTE + § 2 row). Git transport (GitHub 780-AI)
  stays a candidate once DD-6b settles. Project SESSION_OPENER § 2 row updated. Manifest
  Last-updated block rotated (lapsed since 2026-08-19, v2.27–v2.38 — disclosed).
- **QA scenarios (Rule 11; Rule 15 feature-ON):** all three ✅ 2026-10-03, run against the
  re-pointed registry before commit:
  - QA-VL1 `status` — 780-VPN resolves at the expanded path: ADOPTED v2.5 / VAULT v2.5 /
    current / open-log 1 (was `?` / `unknown` / 0 over ssh).
  - QA-VL2 `sync --project 780-VPN` dry-run — up-to-date, 11/11 SYNC_MAP items `ok` (the
    transport swap perturbs nothing).
  - QA-VL3 `harvest` — surfaces 780-VPN E001 ("Stamp sync output from a trusted clock…",
    governance, general) — previously unreachable. Listing only; integration stays behind the
    Rule 16 gate. Target tree verified untouched after the runs (clean, `e739ff9`).
- **Versions:** manifest 2.38→2.39, project SESSION_OPENER 1.15→1.16. Impact: registry data +
  bookkeeping only — no engine behavior change; reads/writes against 780-VPN now run locally
  from any curator machine syncing the shared folder (writes one machine at a time).

## [2026-09-05] — Bookkeeping: v2.5 catch-up write to 780-Automation — QA-H3 complete on ALL THREE targets; discarded-writes finding recorded

- **Type:** Bookkeeping + fleet-state record (no vault behavior change).
- **What:** 780-Automation came back online (same IP 172.16.11.60, operator-confirmed). The
  pre-write dry-run found a **5-item delta, not 3** — investigation (dry-run `--diff` + ssh
  spot-reads) showed the target's tree carries NONE of the v2.3/v2.4 engine writes: its
  CLAUDE.md still had the pre-v2.4 runner localizations with no engine sync line, and its
  archive was back on its own line with the nine locally-appended lessons (their L069–L077).
  Tree clean → the engine's uncommitted v2.3+v2.4 writes were evidently **discarded
  target-side** after the 2026-08-27-stamped write session — most plausibly a session
  resetting "unexplained modified files": the EXACT incident class PLAN-012 exists to fix,
  now observed a second time. Safety verified BEFORE writing: all nine own-line lessons
  already rescued (vault L070–L078); STANDARDS_LOG empty of real entries (the one `## E0`
  hit is the template's format example); PROJECT-OWNED blocks (their § 4/§ 13 critical-file
  registrations) preserved by merge. Catch-up `sync --write` then landed 6 files (5 changed
  + the handoff — which now explains the write, the mitigation for the very failure that
  caused the discard); idempotence re-run up-to-date 11/11; handoff content spot-read and
  verified. **Fleet now v2.5/v2.5 current on ALL THREE targets** (status probe pasted in
  session). QA-H3's third-target half closes; tracker annotated (1.0→1.1).
- **QA scenarios:** exempt per Rule 11 (bookkeeping/record; the behavior QA is PLAN-012's
  QA-H3, which this completes). Lesson candidate logged in the register: targets can discard
  uncommitted engine writes — surfaced at wrap-up for codification decision.
- **Versions:** PLAN-012 tracker 1.0→1.1 (post-close QA annotation, the PLAN-010 QA-I
  precedent), manifest 2.37→2.38. Impact: none at vault runtime; target 780-Automation
  converged to v2.5.

## [2026-09-05] — Standard Set Version v2.5 RELEASED: sync handoff — every engine write explains itself (PLAN-012 Phase 3)

- **Type:** Engine behavior change + Set Version release (Major per § 4 — Critical Files
  touched; § 15 plan Phase 3, single commit).
- **What:** Every engine write into a target now leaves **`docs/SYNC_HANDOFF.md`** in that
  target and flushes it with the changed files — BOTH write paths: `sync --write` (per written
  target, listing the changed `(file, mode)` set) and the `integrate --write` write-back (per
  flushed target). The handoff states project, operation, vault Set Version, run date (with a
  clock-trust caveat pending E001's trusted-clock intake), and the six residual-bookkeeping
  steps (review diffs → manifest cells → CHANGELOG entry → one landing commit that also deletes
  the handoff; never manifest-listed — engine-transient, Rule 8 exempt by design; new lessons
  still land only as STANDARDS_LOG E0NN entries). NOT a SYNC_MAP item — converged targets still
  report up-to-date with a handoff present. Template side (Set v2.5): SESSION_OPENER → 1.8
  (§ 1.1 engine-handoff check — read the handoff FIRST, land per its § 2, before any other
  work); riding the release: LESSONS → 1.2 (L069–L078 date lines corrected — the vault clock
  ran ~9d slow at intake; no content change). Architecture § 7 gains the handoff paragraph
  (0.11→0.12, § 4 drift rule). En passant: STANDARDS_INDEX § 3 caption unstuck from v2.2 (L063
  drift). Engine: sync.py 0.1→0.2 (`HANDOFF_REL` + `render_handoff`), cli.py 0.5→0.6 (both
  hooks + write-notes), test_cli.py 0.5→0.6 (+1 end-to-end sync-handoff test, +2 write-back
  assertions).
- **QA scenarios (Rule 11/15 — statuses live in PLAN-012_tracker.md):**
  - QA-H1 ✅ 2026-09-05 — ruff clean; mypy delta zero (src 25↔25; full config 42↔42 vs HEAD);
    pytest 111 passed at ship indentation.
  - QA-H2 ✅ 2026-09-05 — dry-run oracle exact on both reachable targets (CS + 780-VPN: the
    3-item delta and nothing else); 780-Automation host DOWN (warn+skip as designed).
  - QA-H3 ✅ 2026-09-05 — feature-ON sync half (Rule 15): handoff delivered to CS + 780-VPN,
    content read back and verified against design; 780-Automation catch-up completed same day
    when the host returned (see the bookkeeping entry above) — ALL THREE targets verified.
  - QA-H4 ✅ 2026-09-05 — idempotence: dry-run re-run up-to-date 11/11 on both written targets.
  - QA-H5 ✅ 2026-10-03 — loop closure observed in 780-VPN `de1de37` (landed per the handoff +
    deleted it, before feature work; see the 2026-10-03 bookkeeping entry above).
  - QA-H6 ✅ 2026-10-04 — feature-ON write-back half: the 780-VPN E001 write-back left its
    record in the target's handoff (see the 2026-10-04 QA bookkeeping entry above).
- **Versions:** sync 0.1→0.2, cli 0.5→0.6, test_cli 0.5→0.6, template SESSION_OPENER 1.7→1.8,
  template LESSONS 1.1→1.2, STANDARDS_INDEX 2.4→2.5, SET_VERSION_ADOPTED 1.12→1.13,
  architecture 0.11→0.12, manifest 2.36→2.37, PLAN-012 + tracker 0.3→1.0/CLOSED.
- **Impact:** yes — every engine write now also writes one extra file (the handoff) into the
  target and includes it in the flush. Dry-run, worksheet, and read-only commands unchanged.

## [2026-09-05] — PLAN-012 APPROVED (Phase 2): "approve plan 012"

- **Type:** Plan bookkeeping (approval record; no behavior change).
- **What:** Operator approval landed on the v0.2 draft; plan + tracker → 0.3 / APPROVED. Phase 3
  (implement, single commit, 12-file ALLOWLIST, ships Set v2.5) runs in a FRESH session per
  § 15.3 — handoff via the committed plan + the local register.
- **Versions:** PLAN-012 + tracker 0.2→0.3, manifest 2.35→2.36. Impact: none at runtime.

## [2026-09-05] — PLAN-012 hardened to v0.2: the handoff now covers BOTH engine write paths

- **Type:** Plan revision (design only; no behavior change).
- **What:** Operator-directed re-review ("double check the plan… consistency check with the
  whole code base"). The full write-path sweep found the gap the v0.1 draft had deferred with
  thin justification: `integrate --write`'s write-back ALSO writes into targets (STANDARDS_LOG
  status flips) and would have reproduced the unknown-changes incident in miniature. Design
  generalized — `render_handoff` gains an operation line and a `(rel, mode)` files interface;
  the integrate flush hook writes the handoff per flushed target; handoff § 2 gains the
  manifest-exemption step (protects git-transport targets' Rule 8/doc-coverage gates from the
  engine-committed handoff); QA-H6 added with a NAMED feature-ON trigger (the pending E001
  intake from 780-VPN's log). E001's trusted-clock engine suggestion explicitly routed to its
  own gated intake (plan § 3). Overlay re-proven: ruff clean, mypy delta zero, pytest 111
  (sync + integrate handoff coverage); Rule 13 re-run; 12/12 mechanical extraction checks.
  Clock fixed on this machine before this commit (stamps now real-dated).
- **QA scenarios:** plan § 8 QA-H1..H6; statuses in PLAN-012_tracker.md.
- **Versions:** PLAN-012 + tracker 0.1→0.2, manifest 2.34→2.35. Impact: none at runtime.

## [2026-09-05] — PLAN-012 drafted: sync handoff report (every engine write leaves an explanation in the target)

- **Type:** § 15 plan draft (design commit only; no behavior change yet).
- **What:** Operator directive after a 780-VPN session opened to four engine-written uncommitted
  files it did not make: *"after any change there should be a hands-off report so claude code in
  other projects will not face unknown changes to the files."* PLAN-012 designs the fix at the
  L044 granularity — every `sync --write` will leave `docs/SYNC_HANDOFF.md` in the written
  target (what was written, at which Set Version, plus the five residual steps: review diffs,
  manifest cells, CHANGELOG entry, landing commit, delete-the-handoff), flushed by every
  transport in the same pass; the SESSION_OPENER template gains a § 1.1 engine-handoff check
  (rides as Set v2.5, together with the canonical LESSONS date-line corrections from the
  clock-skew finding). Code developed + tool-proven in a scratch overlay FIRST (proven-code-first
  pattern): ruff clean, mypy delta zero, pytest 111 passed (+1 new end-to-end test). Rule 13 pass
  RUN and recorded in the plan (extraction byte-verified against the overlay; all FIND anchors
  grep-verified unique in live source). Awaiting Phase 2 **"APPROVE PLAN-012"**; Phase 3 runs in
  a fresh session per § 15.3.
- **QA scenarios:** defined in the plan § 8 (QA-H1..H5, incl. the Rule 15 feature-ON v2.5
  rollout and the target-side loop-closure observation); statuses live in PLAN-012_tracker.md.
- **Versions:** manifest 2.33→2.34 (new rows 80–81). Impact: none at runtime (design only).

## [2026-09-05] — Record correction: the clock skew was OURS — the vault machine ran ~9 days slow

- **Type:** Record correction (no content release, no engine change).
- **What:** A 780-VPN session (GitHub setup work) found GitHub's server time matching that Mac to
  the second — and independent verification from this machine confirms it: gitlab.com and
  apple.com both report **2026-09-05** while this vault machine reads 2026-08-27. Every earlier
  conclusion pointing the other way ("both team Macs run fast clocks") was wrong — the team
  Macs were accurate; the VAULT machine is ~9 days slow. Corrected in: `config/projects.toml`
  (780-VPN comment), SESSION_OPENER § 2 row (1.14→1.15), the vault archive L070–L078 provenance
  entry, the local register, and the dynamic-IPs memory. **Consequences:** all vault stamps
  dated 2026-08-27 (the v2.3 + v2.4 releases, Rule 16, the registrations) were really written
  2026-09-05 — in adopters this produces change logs where a sync line predates the bootstrap
  line (observed at 780-VPN). Per the idempotent-engine reality, published stamps stay as
  delivered; the canonical LESSONS date-line corrections ride the next Set bump (v2.5, planned).
  **Operator action:** fix this machine's clock (System Settings → General → Date & Time → set
  automatically). Discovered by the adopter's session — the outbox/handoff loop working as
  intended even before it's formalized (PLAN-012, drafted next).
- **QA scenarios:** exempt per Rule 11 (record correction). Verification evidence (server Date
  headers) verbatim in the session chat.
- **Versions:** project SESSION_OPENER 1.14→1.15, manifest 2.32→2.33. Impact: none at runtime.

## [2026-08-27] — Bookkeeping: v2.4 QA-P4 verified + stale instance Source refs cleared

- **Type:** Bookkeeping + deferred-minor sweep (bundled as one commit — single coherent
  session-close deliverable, deviation recorded per the § 10 practice).
- **What:** (1) QA-P4 flipped ✅ in the v2.4 entry — full-fleet write ran with the
  780-Automation hold lifted; fleet v2.4/v2.4 current on all three targets, idempotent, 780
  spot-greps verified. (2) The long-deferred stale header Source refs fixed: project
  SESSION_OPENER (1.13→1.14, template ref v1.4→v1.7) + project SESSION_CLOSER (1.5→1.6, template
  ref v1.3→v1.7) — register row cleared. QA: exempt per Rule 11 (bookkeeping/doc cleanup).
- **Versions:** project SESSION_OPENER 1.13→1.14, project SESSION_CLOSER 1.5→1.6, manifest
  2.31→2.32. Impact: none at runtime.

## [2026-08-27] — Standard Set Version v2.4: environment portability (the Runner note) — 780-Automation hold lifts

- **Type:** Standards-suite release (Critical File `docs/standards/` — doc-only, no engine
  change; Major workflow without a § 15 plan per the § 15.6 doc-only carve-out; executed under
  the operator's batch authorization "get everything done as recommended").
- **What:** The second half of the 780-Automation divergence (the v2.3 entry rescued the first):
  the template contract hard-coded one environment's invocations (`python`, `.gitlab-ci.yml`) in
  suite-owned text, so an adopter on `python3`/`uv`/GitHub Actions had its adaptations reverted
  by every sync. Design chosen: **neutralize, not PROJECT-OWNED-wrap** (no fleet-wide hand-wrap;
  solves the class). Template CLAUDE.md → 1.6: Rule 2 gains the binding **Runner note** (command
  examples are generic — substitute the project's Python runner / CI flavor at run time; NEVER
  edit suite-owned text to localize; tooling facts belong in the § 1 PROJECT-OWNED block); the
  Rule 5 sentence and § 8.6 YAML one-liner are now CI-flavor-neutral. Counts unchanged; no rule
  added.
- **QA scenarios (Rule 11 — pre-commit, outputs verbatim in the session chat):**
  - QA-P1 ✅ 2026-08-27 — grep gate: exactly one `python3|uv run` hit in the template — line 65,
    the Runner note naming the variants (the mechanism); zero localized commands remain.
  - QA-P2 ✅ 2026-08-27 — engine-as-oracle merge of the new template against 780-Automation's
    LIVE CLAUDE.md: every remaining delta is the neutralization itself (their env-specific lines
    converge to the generic text + Runner note); PROJECT-OWNED customizations (§ 4/§ 13 Critical
    File registration) untouched. After this one-time convergence, sync stops fighting their
    environment — the hold's remaining reason is resolved.
  - QA-P3 ✅ 2026-08-27 — fleet dry-run: CS + 780-VPN show exactly the predicted 2-item delta
    (CLAUDE.md merge + SVA record); 780-Automation shows the predicted 4-item catch-up
    (CLAUDE.md + LESSONS + SESSION_CLOSER + SVA — v2.3 + v2.4 together).
  - QA-P4 ✅ 2026-08-27 (post-commit, same session) — full-fleet `sync --write` with the
    780-Automation **hold lifted** (both reasons resolved: lessons rescued at v2.3, portability
    fixed here): 2+4+2 files written + flushed; idempotence re-run = up-to-date 11/11 on all
    THREE targets; 780-side spot-greps verified (Runner note in their CLAUDE.md, L078 + ownership
    banner in their archive, closer binding rule, SVA v2.4); fleet `status` = v2.4/v2.4 current
    across the board — the first fully-current three-target fleet.
- **Versions:** template CLAUDE.md 1.5→1.6, STANDARDS_INDEX 2.3→2.4, SET_VERSION_ADOPTED
  1.11→1.12, manifest 2.30→2.31. Impact: standards content release — no engine behavior change;
  root CLAUDE.md untouched (its env-specific wording is a legitimate instance state under the
  note).

## [2026-08-27] — Standard Set Version v2.3: first adopter-originated lesson intake (L069–L078), under the Rule 16 gate

- **Type:** Standards-suite release (Critical File `docs/standards/` — doc-only, no engine
  change; Major workflow without a § 15 plan per the § 15.6 doc-only carve-out, operator-directed
  — the E001/v2.1 precedent).
- **What:** The nine lessons found in 780-Automation's engine-owned `archive/LESSONS.md` (the
  L069 incident) are rescued: genericized (project/file/spec names dropped per the domain-neutral
  rule) and integrated into the canonical LESSONS as **L070–L078** — uniqueness-key intent vs
  attempt, unexercised config overrides, fan-out payload guarantees, reserved logging attributes,
  side-effect transaction isolation, gitignore swallowing shipped files, scope-gaps-as-options,
  per-child pool installation, date-relative fixture bounds. **L069** (the incident + three-layer
  fix) added dual-voice (canonical genericized + vault archive project-specific, committed
  earlier today at `8938bee`); the vault archive gains the L070–L078 provenance-table entry
  (vault #, their #, origin — full texts live canonical-side). Prevention fixes ride the bump:
  the LESSONS **ownership banner** (engine-owned in adopters; contribute via STANDARDS_LOG E0NN)
  and the SESSION_CLOSER § 1.7 **binding where-codification-lands rule**. Counts 68 → 78
  everywhere (INDEX § 1/§ 2/§ 3, README, SVA — L060-class sweep). Template rules stay 15
  (Rule 16 is the vault's curator rule). **This intake ran under the first live Rule 16 gate:**
  all nine listed + explained in chat (twice — once in plain words at operator request), operator
  confirmed "all nine" 2026-08-27.
- **QA scenarios (Rule 11 — pre-commit, outputs verbatim in the session chat):**
  - QA-G1 ✅ 2026-08-27 — domain-neutral gate: `grep -rnic` for all fleet project identifiers
    across `docs/standards/` = zero hits (the nine genericized entries leak no source names).
  - QA-G2 ✅ 2026-08-27 — engine-as-oracle `sync` dry-run against the edited vault: BOTH
    reachable targets show EXACTLY the intended 3-item delta — `archive/LESSONS.md` replace +
    `docs/SESSION_CLOSER.md` merge + `docs/SET_VERSION_ADOPTED.md` record v2.2→v2.3 — and no
    other item changed. (780-Automation unreachable at run time — host asleep; it is write-HELD
    regardless pending the CLAUDE.md portability decision, and `sync --project` scoping keeps it
    excluded from the write.)
  - QA-G3 ✅ 2026-08-27 (post-commit, same session) — scoped `sync --write` delivered 3 files to
    each unheld target (write + flush confirmed); idempotence re-run = up-to-date 11/11 both;
    spot-greps verified on both targets (L078 present in each archive TOC + body, ownership
    banner present, SVA reads v2.3); fleet `status` = Capital-Signal v2.3/v2.3 current + 780-VPN
    v2.3/v2.3 current (780-Automation asleep at run time — held regardless).
- **Held:** 780-Automation write stays blocked until the template environment-portability gap is
  settled (planned v2.4) — its rescued originals are safe in its git history meanwhile.
- **Versions:** LESSONS template 1.0→1.1, SESSION_CLOSER template 1.6→1.7, STANDARDS_INDEX
  2.2→2.3, standards README 1.2→1.3, SET_VERSION_ADOPTED 1.10→1.11, manifest 2.29→2.30. Impact:
  standards content release — no engine behavior change; adopters receive it as a normal 3-file
  sync.

## [2026-08-27] — NEW Rule 16: operator confirmation gate on harvested content (the nine-orphaned-lessons incident)

- **Type:** Operating-contract rule addition (Critical File root `CLAUDE.md`; operator-decreed,
  firm; project-specific — curator workflow only, template untouched, no Set bump).
- **What:** After every `harvest` — and any other intake of externally-authored content,
  including manual rescues — the gathered candidate lessons/rules MUST be presented to the
  operator as a complete list with per-item plain-language explanations and recommendations, and
  NO integration edit lands until the operator explicitly confirms (per-intake; no standing
  authorization; rejected items marked in the source log, never silently dropped). No permitted
  abbreviation; drift is a Major defect. Motivated by today's discovery of nine adopter-authored
  lessons in 780-Automation's replace-mode `archive/LESSONS.md` (their log empty, harvest blind,
  content one `--write` from destruction) — the intake boundary had no operator gate at the
  granularity the risk fires. Incident codified as vault L069 (with the three-cause diagnosis:
  the contract teaches lesson-appending; ownership invisible at point of use; discipline had no
  forcing function). SESSION_OPENER § 3.2 row 1 added; matching memory files written same-commit
  (Rule 9 maintenance).
- **QA scenarios:** exempt per Rule 11 (governance-doc edit, no engine/runtime behavior change).
  The rule's first live exercise is the imminent L069–L077 intake — its list-and-confirm
  exchange in the session chat serves as the feature-ON evidence.
- **Versions:** root CLAUDE.md 1.7→1.8, project SESSION_OPENER 1.12→1.13, manifest 2.28→2.29.
  Impact: process rule only — no engine behavior change.

## [2026-08-27] — 780-Automation DHCP IP change: registry re-pointed 172.16.10.61 → 172.16.11.60

- **Type:** Registration data update (Critical File `config/projects.toml`; no engine change).
- **What:** The documented DHCP caveat fired — 780-Automation's team Mac came up on a new LAN IP.
  Before re-pointing, identity verified over ssh at the new address: same account (`a780`),
  passwordless key auth intact (survives IP changes by design), bootstrap commit `cb62527` in
  history, clean tree, SVA v0.2 / Set v2.2. Bonus finding: the team member completed the entire
  780-side follow-up from 2026-08-19 — the engine-written v2.2 sync files are committed AND the
  manifest cells reconciled (SVA v0.2, MEMORY_PROTOCOL v1.1) — cleared from the local register.
  Registry `ssh_host` + SESSION_OPENER § 2 row (1.11→1.12) re-pointed.
- **QA scenarios (Rule 11 — run pre-commit against the edited registry, outputs verbatim in the
  session chat):**
  - QA-IP1 ✅ 2026-08-27 — `status` resolves 780-Automation at the new IP: ADOPTED v2.2 / VAULT
    v2.2 / current / open-log 0 (full three-target fleet current — first time all three resolve
    in one run).
  - QA-IP2 ✅ 2026-08-27 — `sync` dry-run over ssh at the new IP resolves and plans correctly
    (transport path proven — the scenario's purpose). Substantive finding: NOT up-to-date — 2 of
    11 changed on the target since 2026-08-19. (1) `archive/LESSONS.md` (replace-mode): the team
    member appended NINE project-originated lessons L069–L077 directly — content that belongs in
    STANDARDS_LOG E0NN entries (their log is empty; harvest sees nothing) and that a future
    `sync --write` would DESTROY. (2) `CLAUDE.md` (merge-mode): engine-as-oracle merge shows a
    write would revert their environment adaptations in suite-owned text (`python3`/`uv run`
    invocations, GitHub-Actions refs vs the template's `python`/GitLab wording); their § 4/§ 13
    Critical-File registration sits in PROJECT-OWNED blocks and survives. **`sync --write` for
    780-Automation is HELD pending operator decision** (lessons intake path + template
    environment-portability gap — recorded in OPEN_TASKS).
  - QA-IP3 ✅ 2026-08-27 — `harvest`: no open entries across the full fleet (which is exactly the
    problem — the nine lessons bypassed the log).
- **Versions:** manifest 2.27→2.28, project SESSION_OPENER 1.11→1.12. Impact: registry data +
  bookkeeping only — no engine behavior change.

## [2026-08-27] — Third target registered: 780-VPN (ssh transport) — QA-D1b closed on the live bootstrap SVA

- **Type:** Registration (Critical File `config/projects.toml`; no engine change).
- **What:** 780-VPN — bootstrapped on a second team Mac to Standard Set v2.2 (vault `3f5590a`;
  single bootstrap commit `be4d6d3`, clean tree) — registered as the third sync target:
  `ssh_host = parsaazad@172.16.11.17` (LAN IP, DHCP — noted in the registry), `ssh_path =
  /Users/parsaazad/Library/CloudStorage/Dropbox/Projects/780-VPN`. Key auth installed same day
  (curator machine's ed25519; first `ssh-copy-id` ran from the wrong account — the team member's —
  and was redone from the curator account). Pre-registration cross-checks over ssh: repo root
  resolves, single bootstrap commit, clean tree, SVA v0.1 present WITH the CHANGE LOG block (the
  W-D1 spec repair proven in a live bootstrap), rsync available. Registry entry carries two new
  caveats: the remote path is Dropbox-synced on the team member's side (one-machine-at-a-time
  applies there too), and that Mac's clock ran +9 days fast at bootstrap (target stamps read
  2026-09-02; real date ~2026-08-24 — clock fix flagged). Project SESSION_OPENER § 2 registry row
  added (1.10→1.11).
- **QA scenarios (Rule 11 / Rule 15 feature-ON — all run pre-commit against the edited registry,
  outputs verbatim in the session chat):**
  - QA-S1 ✅ 2026-08-27 — `status` resolves 780-VPN over ssh: ADOPTED v2.2 / VAULT v2.2 /
    current / open-log 0 (fleet table now three targets; 780-Automation `unknown` — host down at
    run time, non-fatal warn+skip as designed).
  - QA-S2 ✅ 2026-08-27 — `sync` dry-run over ssh: up-to-date across all 11 SYNC_MAP items over
    rsync (a fresh v2.2 bootstrap is a sync no-op — "converge once, sync forever" holds).
  - QA-S3 ✅ 2026-08-27 — `harvest` covers the reachable fleet: no open entries (780-Automation
    skipped loudly: "Host is down").
  - QA-D1b ✅ 2026-08-27 — **the pending W-D1 follow-up scenario closes**: the live bootstrap's
    SVA fetched over ssh and run through the engine's `record_adoption` with a version-DELTA
    fixture (v9.9): parses (no SyncError at `split_header` — the W-D1 failure point), header
    bumps 0.1→0.2, sync log line prepends, adopted bullet updates, backport row inserts. The
    next real Set bump will apply cleanly to this target.
- **Versions:** manifest 2.26→2.27, project SESSION_OPENER 1.10→1.11. Impact: registry data +
  bookkeeping only — no engine behavior change; the vault now maintains three registered targets
  (two ssh). Machine-health follow-ups recorded in OPEN_TASKS: remote clock +9d skew; broken
  Intel CLT on that arm64 Mac (working git at `/usr/local/bin/git`).

## [2026-08-19] — W-D1 fix-forward: sync-ready SVA shape in both skill mode specs gains the CHANGE LOG block

- **Type:** Delivery-skill spec fix (fix-forward per Rule 3; vault machinery — not part of the
  adopter-facing Set, so no Set bump).
- **What:** The "sync-ready SVA shape" restated in `skill/modes/bootstrap.md` § 4 and
  `skill/modes/adopt.md` (both 0.1→0.2) omitted the CHANGE LOG comment block that the engine's
  record-update hard-requires (`sync.py` `_split_header` splits the target SVA at that block's
  closing `-->`). Consequence: the first live bootstrap (780-Automation, 2026-08-19) faithfully
  shipped an SVA that raises SyncError on its first version delta — found same day by the v2.2
  oracle dry-run (defect **W-D1**, recorded in the v2.2 entry below). The pilot adoption (CS) was
  unaffected only because its session wrote the block unprompted. Both specs now spell out the
  block verbatim with the reason attached.
- **QA scenarios (Rule 11):**
  - QA-D1a ✅ 2026-08-19 — one-time repair applied to 780-Automation's SVA over ssh (CHANGE LOG
    block inserted, provenance note in its v0.1 line); the v2.2 sync dry-run then planned its
    record-update cleanly (2-item delta, identical to CS) and the subsequent `--write` executed
    it — the repaired shape IS the fixed spec's shape, so this doubles as the spec's
    shape-validation.
  - QA-D1b ⏸ — the NEXT skill delivery (bootstrap or adopt) produces an SVA whose record-update
    parses on first delta (engine-as-oracle at that delivery — this time against a
    version-DELTA fixture, the path the D3-era same-version oracle never exercised).
- **Versions:** bootstrap mode 0.1→0.2, adopt mode 0.1→0.2, manifest 2.25→2.26. Impact: spec text
  only — future deliveries write a complete SVA; no engine change, no adopter-content change.

## [2026-08-19] — Standard Set Version v2.2: domain-neutral scrub — payload for the first ssh sync --write

- **Type:** Standards-suite Minor (Critical File `docs/standards/`; doc-only scrub, no engine
  change; § 15.6 carve-out — no plan file).
- **What:** Four example paths carrying a real username (`/Users/parsaazad/...`, survived the v1.0
  genericization — the identifier-token scrub class; found by the v2.1 release-gate grep, held in
  the register) scrubbed to `/Users/you/...` (the registry-example convention): MEMORY_PROTOCOL.md
  3 sites + PROJECT_INSTRUCTIONS_TEMPLATE.md 1 site, both 1.0→1.1. Counts unchanged (68 lessons /
  15 rules); no rule or lesson content change. This Minor doubles as the first real sync payload
  for the ssh transport: MEMORY_PROTOCOL is replace-class in the SYNC_MAP, so both registered
  targets show a genuine delta.
- **QA scenarios (Rule 11 / Rule 15 — the ssh WRITE-path smoke):**
  - QA-W1 2026-08-19 (pre-commit, engine-as-oracle dry-run against the edited tree, vault v2.2):
    **split verdict.** Capital-Signal ✅ — exactly 2 changed items (MEMORY_PROTOCOL replace + SVA
    record v2.1→v2.2), nothing else. 780-Automation ❌ — SyncError `docs/SET_VERSION_ADOPTED.md:
    no CHANGE LOG comment in header` → **defect W-D1**: BOTH skill mode files' "sync-ready SVA
    shape" spec omits the CHANGE LOG comment block that the engine's record-update hard-requires
    (`sync.py` `_split_header`). 780's bootstrap followed the spec literally; CS is unaffected
    only because its adopt session wrote a CHANGE LOG anyway. Root cause of the QA gap: the D3
    engine-as-oracle run used a SAME-version fixture, so the record-update parser (the only
    consumer of that block) never executed — first exercised by today's genuine delta.
    Fix-forward: mode-spec fix commit (same session) + one-time SVA repair on 780 (prepared;
    pending the team Mac's reachability — it left the network mid-repair).
  - QA-W2 ✅ 2026-08-19 — after the W-D1 SVA repair landed on 780 (dry-run then planned the
    identical 2-item delta on both targets), the fleet `sync --write` ran: **first live ssh
    `flush`** — 2 files rsync'd back to 780-Automation + 2 written locally to CS; immediate
    dry-run re-run = up-to-date 11/11 on BOTH targets. The ssh WRITE half of the transport smoke
    is proven.
  - QA-W3 ✅ 2026-08-19 — remote evidence over ssh: 780's MEMORY_PROTOCOL has zero username hits;
    its SVA carries the engine-written v0.2 sync log line and records v2.2. Same greps pass on CS.
    Fleet `status`: both targets ADOPTED v2.2 / VAULT v2.2 / current. (780's tree also holds the
    team member's own WIP — their session commits the synced files alongside it, per the
    write-in-place model.)
  - This entry is the permanent record.
- **Versions:** Set v2.1 → **v2.2**; PROJECT_INSTRUCTIONS_TEMPLATE 1.0→1.1; MEMORY_PROTOCOL
  1.0→1.1; STANDARDS_INDEX 2.1→2.2; SET_VERSION_ADOPTED 1.9→1.10; manifest 2.24→2.25. Impact: no
  vault runtime change; adopter-facing content fix propagates at each target's next `sync`.

## [2026-08-19] — Second target registered: 780-Automation (ssh transport) — ssh read path smoke-proven

- **Type:** Registration (Critical File `config/projects.toml`; no engine change).
- **What:** 780-Automation — bootstrapped earlier today to Standard Set v2.1 on the team member's
  Mac (self-service via the portable kit at `/Volumes/780-Data/Standard-Docset`; target commit
  `cb62527`) — registered as the second sync target and the FIRST ssh-transport target:
  `ssh_host = a780@172.16.10.61` (LAN IP, DHCP — noted in the registry), `ssh_path =
  /Users/a780/Projects/780-Automation`. Key auth installed same day (curator machine's ed25519).
  Pre-registration cross-checks over ssh: repo root resolves, single bootstrap commit, clean tree,
  SVA v0.1 present, rsync available. Registry entry carries the planned migration note: → git
  transport once the project lands on the organization GitHub (re-opens DD-6b write-back etiquette
  before any git `--write`). Project SESSION_OPENER § 2 registry row added (1.9→1.10).
- **QA scenarios (Rule 11 / Rule 15 feature-ON — all run pre-commit against the edited registry,
  outputs verbatim in the session chat):**
  - QA-S1 ✅ 2026-08-19 — `status` resolves 780-Automation over ssh: ADOPTED v2.1 / VAULT v2.1 /
    current / open-log 0 (fleet table now two targets).
  - QA-S2 ✅ 2026-08-19 — `sync` dry-run over ssh: up-to-date across all 11 SYNC_MAP items (a
    fresh kit-bootstrap is a sync no-op — "converge once, sync forever" holds over ssh; the full
    materialization rsyncs docs/ + archive/ + root CLAUDE.md). **This is the first live exercise
    of the ssh transport** (PLAN-007 QA K–N class; PLAN-008 ssh-sync read half) — the READ path is
    proven; the WRITE path (`flush` rsync-back) stays pending until the first real sync delta.
  - QA-S3 ✅ 2026-08-19 — `harvest` covers the two-project fleet: no open entries.
- **Versions:** manifest 2.23→2.24, project SESSION_OPENER 1.9→1.10. Impact: registry data +
  bookkeeping only — no engine behavior change; the vault now maintains two registered targets.

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
