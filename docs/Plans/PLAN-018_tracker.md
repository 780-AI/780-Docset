<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-10-11 -->
<!-- Status: CLOSED — 2026-10-11: QA-S1…S6 ✅ (S6 on Windows); acceptance § 12 items 1–7 met; two waivers recorded -->
<!--
CHANGE LOG
v1.0 — 2026-10-11 — CLOSED: QA-S4 (2026-10-10, the operator's second Mac), QA-S5 (2026-10-10, this Mac) and
QA-S6 (2026-10-11, the owner's Windows PC) ✅ with evidence; second waiver (bootstrap § 6 Windows note);
Phase 5 ✅ (push 2026-10-08 + this closure commit); new Closure section — acceptance § 12 items 1–7 and the
Windows findings queued as a follow-up.
v0.3 — 2026-10-08 — Phase 3 ✅ (3.0–3.3; reconcile 11 / 11, zero plan defects); QA-S1…S3 ✅ with evidence.
v0.2 — 2026-10-08 — Phase 2 ✅: "go on commit; plan 018 approved, all A" (plan § 9.1); waiver register:
D-1 = A (adopt mode's feature-ON evidence until its next real use).
v0.1 — 2026-10-08 — Created with the plan draft (tracker required per CLAUDE.md § 15.7: Phase 4 has a
multi-scenario list, QA-S1…S6, and the feature-ON half runs after the push and on a Windows machine —
the plan spans sessions).
-->

# PLAN-018 tracker — one-prompt delivery (named-vault Step 0, selftest mode, handoff report)

## Phase 0 — Audit

- ✅ 2026-10-08 — § 15.9 intake: operator request in chat (no document); "c, a, a"; adopt / deviate per
  item recorded (plan § 2).
- ✅ 2026-10-08 — integration points cited `file:line` at `9b1c49e` (plan § 3).
- ✅ 2026-10-08 — P1 GitHub clone (18 s, 3.5 MB, HEAD == both remotes, nothing private published); P2
  named-vault Step 0; P3 installer in a sandbox HOME.
- ✅ 2026-10-08 — P4 Step 0 matrix: draft 5 / 5; the current Step 0 pulls the current folder's repo in
  both no-link cases (control).

## Phase 1 — Design

- ✅ 2026-10-08 — the six files drafted in a scratch overlay of the GitHub clone; domain-neutral grep over
  `skill/` clean; fences balanced.
- ✅ 2026-10-08 — P5: § 5 generated from the overlay (11 blocks), parsed back from the plan text, applied
  to a fresh copy of `9b1c49e` → 6 / 6 files byte-identical; control 1 FAIL.
- ✅ 2026-10-08 — P6: a fresh agent given only launcher 1 ran the self-test on the draft — 17 / 0 / 1, the
  machine identical before and after (curator snapshot); 12 notes → fixes + queued gaps (plan § 2, Rule 13).
- ✅ 2026-10-08 — P6b: a second fresh agent on the final draft — 17 / 0 / 1 again, every fix followed.
- ✅ 2026-10-08 — Rule 13 senior-review pass (record at the foot of the plan).

## Phase 2 — Operator approval

- ✅ 2026-10-08 — "go on commit; plan 018 approved, all A" — D18.A; D-1…D-4 = A (plan § 9.1). Plan +
  tracker → 0.2.

## Phase 3 — Implement (fresh session; one vault commit)

- ✅ 2026-10-08 3.0 Pre-checks: local `date -u` 14:14:06 vs `Date:` gitlab.com 14:14:07 / github.com 14:14:05
  → `<P3-DATE>` = 2026-10-08; vault tree clean; HEAD `977a1ca` == `ls-remote` origin == github; the six
  files unchanged since the audit commit (`git diff 9b1c49e HEAD` on them empty).
- ✅ 2026-10-08 3.1 Reconcile pass — a parser written fresh in this session: 11 blocks extracted (5a 5b
  5c.1–3 5d.1–3 5e 5f.1–2); pre-blobs `b8e3757…` (SKILL.md) + `56d37dc…` (README.md) matched;
  `selftest.md` absent; every FIND matched exactly once, in order; **zero plan defects**. Positive
  control (FIND 5c.2 corrupted) → exactly 1 FAIL. Applied to an export of `9b1c49e` → the same six blobs.
- ✅ 2026-10-08 3.2 Apply § 5 → the six files written byte-for-byte (blobs in QA-S3); QA-S1 ✅, QA-S2 ✅.
- ✅ 2026-10-08 3.3 § 6c bookkeeping (manifest 2.67: cells 6 / 76 / 77 / 78, rows 93–94 → 0.3, new row 95,
  Delivery quick-index; CHANGELOG with QA scenarios; plan + tracker 0.3) → QA-S3 ✅ → Rule 10 review table
  in chat → operator "go on commit?" → commit (§ 7.3, 10 files; no push) → OPEN_TASKS (§ 6f).

## Phase 4 — Validate

| # | Scenario | Phase | Status | Date | Evidence |
|---|---|---|---|---|---|
| QA-S1 | Domain-neutral gate over `skill/` | 3.2 | ✅ | 2026-10-08 | the § 8 grep over `skill/` → no output, exit 1; control (same pattern on `config/projects.toml`) → 29 lines, exit 0 |
| QA-S2 ⚑ | Step 0 matrix 5 / 5 (control red on 0.2) | 3.2 | ✅ | 2026-10-08 | § 8.1 script extracted verbatim from the plan (46 lines), vault = a local clone at `977a1ca`. 0.3 Step 0 (13 lines): decoy git calls 0 / 0 / 0 / 0 / 0; cases 1–2 exit 0 `Delivering Standard Set Version v2.7 from vault commit 977a1ca (vault: …)`; cases 3–4 exit 1 `STOP: no vault folder named and no skill link …`, case 5 exit 1 `STOP: '…' is not a Standard DocSet vault` — 0 git calls in 3–5. Control, 0.2 Step 0 (`git show HEAD:skill/SKILL.md`, 7 lines): decoy calls 3 / 0 / 3 / 2 / 3 (`rev-parse`, `pull --ff-only`, `rev-parse`; case 4 via `git -C ""`), cases 1 / 3 / 5 print `Set Version  from vault commit <decoy sha>` — identical to § 3 P4 |
| QA-S3 | Governance, cells == headers, fences, blobs | 3.3 | ✅ | 2026-10-08 | governance exit 0 / 0 (stdout in the Phase 3 chat); cells 2 / 5 / 6 / 76 / 77 / 78 / 93 / 94 / 95 == their headers (Python check — it read row 94 as a mismatch before this tracker's bump: the checker sees a stale cell); fence lines even in all 10 files; blobs after apply: SKILL.md `69541b8`, selftest.md `e00e308`, bootstrap.md `a6882e9`, adopt.md `5abf898`, README.md `4ca4623`, folder_structure.md `b8551f8` (== § 5 applied to `9b1c49e`) |
| QA-S4 ⚑ | Real self-test from the GitHub page (operator, this Mac) | post-push | ✅ | 2026-10-10 | Run on the operator's SECOND Mac (account `parsaazad`, arm64), launcher 1 copied from the GitHub page; report `…-20261010-113651.txt`: clone of GitHub `780-AI/780-Docset` at `d57c56b`, v2.7; SUMMARY pass=17 fail=0 skip=0 info=1 (clock 17 s); `installer` PASS; nested bootstrap 6/0/0/0; STOPS none; `CLEANUP clone-removed`; §§ 1–8 4 min 21 s. **Deviations (operator-accepted, option (a)):** (1) no "before" snapshot on that Mac — the vault half checked from this Mac (same Dropbox folder: clean, `d57c56b` on both remotes, local git config identical to the 2026-10-08 snapshot) and the machine half by a read-only after-check run there (control-tested first): clone + sandbox gone; skill link byte-for-byte the report's § 1 line (unchanged since Aug 17); no new skill link; of 217 entries under `~/.claude`, the only ones created during the run are the session's own start-up files; (2) the session was opened in a fresh EMPTY folder (`…/Dropbox/Projects/780-docset`, created a minute before), not the home folder — still empty afterwards. Report notes: `files` "all 19" where the list has 18 (agent arithmetic, R1); the CLAUDE.md § 14 delete-vs-stub conflict again (queued gap 4) |
| QA-S5 ⚑ | Project setup with launcher 2 (operator, this Mac) | post-push | ✅ | 2026-10-10 | Fixture `~/docset-setup-test` (`git init -b main`, test identity) + before snapshot; launcher 2 from the GitHub page in a new session; report `…bootstrap-report-20261010-131204.txt`: SUMMARY 11/0/0/0, STOPS none; REGISTRATION `name=docset-setup-test git_remote=none work_machine=Darwin (macOS 26.5.2) + yaserkhosravi onboarding=bootstrap onboarded_on=2026-10-10 onboarded_set=v2.7 commit=c60571a`; ANSWERS list all 8 asks. Curator check: `c60571a` the only commit (== the report), no remote, clean, 25 files; the 18 `files` present; 8 verbatim copies `cmp`-identical; markers 4/4, 3/3, 2/2; locality `STATUS: OK`; `~/Standard-DocSet` cloned at `d57c56b`. Engine as oracle (`sync.plan_target` from the vault's `.venv` — the machine's system python3 is 3.9.6): `up-to-date`, 11 / 11 ok. Benign deviations: commit message in the agent's scratchpad, `adopt` not `link` (§ 6 says so when the harness dir exists), review + commit in one turn (operator pre-answered "go"). Cleanup after the session was verified closed: harness symlink `rm`'d (store survived), both folders deleted (`~/Standard-DocSet` after an identity check); `~/.claude/projects` == the before snapshot |
| QA-S6 ⚑ | Windows self-test (D-2) | post-push | ✅ | 2026-10-11 | The owner's Windows PC (MINGW64_NT-10.0-26300, git 2.39.2.windows.1), guided by a self-checking `.txt` (pre-check control-tested OK + STOP); report `…-20261011-064042.txt`: clone of GitHub `780-AI/780-Docset` at `d57c56b`, v2.7; SUMMARY pass=16 fail=0 skip=0 info=2 — clock +4 s, `installer` INFO "Windows Git Bash copies instead of linking" (the expected result); `unlink` PASS via `cmd rmdir` (junction removed, store survived); sandbox under `AppData\Local\Temp` removed; real-skill-link "No such file" before = after; nested bootstrap 6/0/0/0; governance PASS; `CLEANUP clone-removed`; §§ 1–8 2 min 38 s. Self-reported deviations → Closure findings W1–W3 |

**Waiver register (Rule 15):**

| Date | Scope | Waiver | By |
|---|---|---|---|
| 2026-10-08 | adopt mode's § 5 Windows note + § 8 handoff report (plan § 5d) | feature-ON evidence deferred to adopt mode's next real use — its handoff report is the evidence (D-1 = A) | operator ("plan 018 approved, all A") |
| 2026-10-11 | bootstrap mode's § 6 Windows live-session note (plan § 5c.2) — not reachable in the self-test (sandbox HOME: the session is never live there) | feature-ON evidence deferred to the first real Windows bootstrap — its handoff report is the evidence | operator ("do as suggested") |

## Phase 5 — Operator gate

- ✅ 2026-10-08 Push of `d57c56b` to BOTH remotes (operator "push"; governance exit 0 / 0; `ls-remote` origin
  master = github master = `d57c56b` = HEAD; no tag) — before QA-S4…S6 (§ 6d).
- ✅ 2026-10-11 Closure commit (§ 7.4) after QA-S4…S6 + the two recorded waivers (this commit).

## Closure — acceptance (plan § 12), checked 2026-10-11

1. ✅ QA-S1…S3 (2026-10-08, Phase 3 session), QA-S4 + S5 (2026-10-10, after the push), QA-S6 (2026-10-11,
   Windows) with evidence above; adopt-report waiver (D-1 = A) + bootstrap § 6 Windows-note waiver recorded.
2. ✅ Step 0 runs no git command outside a verified vault — QA-S2 cases 3–5: 0 git calls; control red on 0.2.
3. ✅ A NEW session given only launcher 1 finished unattended with `fail=0` on macOS (QA-S4) — and on Windows
   (QA-S6) — and left the machine as it found it (QA-S4 after-check; QA-S6 cleanup checks).
4. ✅ Launcher 2 ended in a delivery commit (`c60571a`) and a report whose `REGISTRATION` line holds every
   registry fact, each matching the real repo (QA-S5).
5. ✅ `skill/` passes the domain-neutral gate (QA-S1) and carries no clone URL; `README.md` is the only
   user-facing file with it (other `git grep` hits are curator records: opener / closer remote notes,
   `NEW_MACHINE_SETUP.md`, plans, CHANGELOG, manifest).
6. ✅ Every manifest cell touched == its file header (L063); governance exit 0 / 0 at the closure commit.
7. ✅ Plan + tracker 1.0 / CLOSED; OPEN_TASKS: the "hassle-free delivery" candidate deleted as superseded;
   its v2.8 queue holds the `STANDARDS_INDEX.md` § 4 self-service wording.

**Findings queued as a follow-up change (operator "do as suggested", 2026-10-11 — none failed a check):**

- **W1 — selftest § 4 Python list has no Windows names.** `python3` on Windows is the Store alias stub, so the
  spec said SKIP; the QA-S6 agent used `python` (3.12.10) instead. Fix candidate: add `python` and `py -3`.
- **W2 — Git Bash's bundled ssh cannot use a key held by the Windows ssh-agent** (the owner's key has a
  passphrase); the QA-S6 agent set `GIT_SSH_COMMAND=C:/Windows/System32/OpenSSH/ssh.exe` for its git calls
  (environment only). Without that, the launchers' clone fails on such a machine. Fix candidate: a Windows
  line in the README (or Step 0) — point git at Windows' ssh.
- **W3 — write-list drift (R1):** the QA-S6 agent copied the nested report to `/tmp` outside the sandbox
  during cleanup, then deleted it. Recorded; candidate: selftest § 7 says "read it from `$SANDBOX/reports/`
  before removing the sandbox".
- Cosmetic: an em dash in the governance scaffold output showed as a replacement character in the Windows
  console; CRLF checkouts (`core.autocrlf`) — verbatim `cmp` still matched.
