<!-- VERSION: 0.3 -->
<!-- Last Updated: 2026-10-08 -->
<!-- Status: EXECUTING — Phase 3 shipped 2026-10-08; push, then QA-S4…S6 (S6 on Windows) -->
<!--
CHANGE LOG
v0.3 — 2026-10-08 — Phase 3 shipped (fresh session): `<P3-DATE>` = 2026-10-08 (local clock within 1 s of
gitlab.com / github.com); reconcile pass 11 / 11 blocks clean, ZERO plan defects (pre-blobs matched,
`selftest.md` absent, every FIND once in order; positive control → exactly 1 FAIL); the six files written
byte-for-byte; QA-S1…S3 ✅ (evidence in the tracker). § 4 Phase 3 ✅. No § 5 change.
v0.2 — 2026-10-08 — Phase 2 operator approval recorded ("go on commit; plan 018 approved, all A"); § 9.1
decision record added: D18.A approved; D-1…D-4 = A (D-1 = A carries the operator's Rule 15 waiver for
adopt mode's feature-ON evidence until its next real use — tracker waiver register). No § 5 change — the
11 blocks re-extracted from this file stay byte-identical to the proven files.
v0.1 — 2026-10-08 — Initial draft. § 15.9 intake (operator request in chat, no document; operator
"c, a, a") → Phase 0 audit against the live source (`9b1c49e`) → Phase 1 design. Code proven FIRST:
the six changed files drafted in a scratch overlay of a fresh GitHub clone; § 5 GENERATED from it
(11 blocks, 4-backtick fences) and parsed back byte-identical; Step 0 matrix 5 / 5 against the
extracted Step 0 (the current one pulls the current folder's repo in 2 of its cases); a fresh agent
given only the self-test launcher ran the whole self-test on the draft (§ 3 P6). Rule 13 pass on the
complete plan + tracker (record at the foot).
-->

# PLAN-018 — One-prompt delivery: the skill from a plain clone, a self-test mode, and a handoff report

## 1. Goal

Anyone with read access to the vault repository uses the suite through **one short prompt in Claude
Code** — no installer, no Terminal steps, Windows included — and every delivery ends in a **plain-text
handoff report** the curator can check against the vault:

1. **Step 0 takes a named vault folder** (`skill/SKILL.md`): the operator's prompt names a plain clone
   of the vault; the installed skill link stays the fallback. Step 0 checks the folder IS a vault
   before any git command — closing the audit's wrong-source defect (today, with no link, Step 0 pulls
   the current folder's repo and reads the suite from it).
2. **selftest mode** (`skill/modes/selftest.md`, new): an unattended, throwaway run of bootstrap mode on
   a practice project in a temporary folder — every result checked, everything removed, the real
   `~/.claude` never touched.
3. **The handoff report** (new SKILL.md section): the last step of every mode — a fixed-layout text
   file on the Desktop (CHECK lines, REGISTRATION facts, answers, stops, raw output of failures).
4. **Two launchers in the README** — the repository's GitHub landing page, refreshed (it still says
   "engine not yet implemented"): (1) the self-test, (2) set up a project.
5. **Windows**: the plain-clone path needs no symlink; bootstrap / adopt say what to do when the
   locality script refuses inside the live session.

## 2. Operator constraints + intake record (binding)

- **Request (2026-10-08, chat):** "make this process much easier for everyone — one single prompt that
  Claude Code will execute and get everything done by itself, then prepare a handoff report for you to
  be investigated." Agent proposal (one paste → the instructions live in the vault → Claude does the
  work → a report file); operator **"c, a, a"**: (c) both self-test and project setup, one design,
  self-test first; (a) the report is a file on the Desktop that the user sends; (a) start the intake +
  plan now — the PLAN-017 closure (Saturday 2026-10-10) stays first.
- **§ 15.9 intake:** no feature document (chat request) — step 1's copy is skipped, never the
  discipline. Step 2 = § 3 (audit + pre-tests, numbers). Step 3 = this design, re-derived from the
  repo's conventions.
- **Adopt / deviate, per item of the request:**
  - "One prompt" — **adopted**: a 3-line launcher; the instructions live in the vault (`skill/`), so
    the paste stays short, never goes stale, and the relay channel cannot mangle it.
  - "Gets everything done by itself" — **adopted for the self-test** (the mode file carries the
    operator's answers: a standing authorization for that mode only); **deviated for project setup**:
    project facts (name, domain, language, CI) are ASKED, never assumed (CLAUDE.md § 10) — the setup
    is one prompt plus the mode's questions in one conversation, with no Terminal work.
  - "Hands-off report" — **adopted**: one file per run, fixed layout, written even when the run STOPs.
  - Repo conventions over the proposal: the clone URL lives only in the README (vault-own) — `skill/`
    stays URL-free and passes the domain-neutral gate; the report is evidence, not suite content —
    lessons in it reach the suite only through the project's `docs/STANDARDS_LOG.md` (Rule 16).
- **Overlap — absorbed / superseded / left alone (explicit):**
  - **Supersedes** the 2026-08-19 "hassle-free delivery" lesson candidate (`make_kit.sh` + a tracked
    kit README): the organization repository + the README launcher replace the portable kit.
  - **Left out, queued:** `docs/standards/STANDARDS_INDEX.md` § 4 self-service wording (a
    `docs/standards/` edit → Set bump → v2.8 queue); template "symlink (junction on Windows)" wording
    (already queued for v2.8); the curator's own clone-from-GitHub variant in `docs/NEW_MACHINE_SETUP.md`
    (deferred minor); PLAN-015's read-only `assess` step (the report's REGISTRATION line feeds it later
    — no engine change here); the git-transport ssh timeout (engine finding — its own change).
  - `scripts/bootstrap_skill.sh` is **unchanged** — still the macOS / Linux convenience for the
    `/standard-docset` command; on Windows the plain clone replaces it.
  - **Found by the self-test's own pre-test runs (P6, P6b), pre-existing, queued — not widened into this
    plan:** (1) bootstrap § 3 resets CLAUDE.md's header but says nothing about the opener's / closer's;
    (2) bootstrap § 3 "keep the schema/header" of `STANDARDS_LOG.md` keeps the template's `TEMPLATE —`
    comment line; (3) bootstrap § 4 "the manifest lists every tracked .md" vs the template's Rule 8,
    which excludes `archive/`; (4) the template CLAUDE.md § 1 placeholder and § 14 say a single-agent
    project DELETES § 14, while bootstrap § 3 says never delete the block (a `docs/standards/` edit →
    v2.8); (5) bootstrap § 5 gives no content for the two governance scaffolds, so every bootstrap
    writes its own — P6 and P6b produced different scripts (candidate: ship them as vault files, copied
    verbatim). The agents resolved each sensibly (an engine probe found both practice projects in sync);
    each becomes a fix candidate in OPEN_TASKS — the self-test already paying for itself.

## 3. Scope summary

Files changed (all vault-side; no engine source, no `docs/standards/`, no target writes → no Set
Version bump, no tag): `skill/SKILL.md` 0.2 → 0.3, `skill/modes/selftest.md` NEW 0.1,
`skill/modes/bootstrap.md` 0.2 → 0.3, `skill/modes/adopt.md` 0.3 → 0.4, `README.md` (no VERSION
header — manifest row 2 keeps `-`), `docs/folder_structure.md` 0.17 → 0.18; bookkeeping per § 6.

### Phase 0 audit findings (2026-10-08, live source at `9b1c49e` = both remotes)

Integration points:

- `skill/SKILL.md:24-36` — Step 0 resolves the vault ONLY through `~/.claude/skills/standard-docset`
  and runs `git -C "$VAULT" pull` (line 27) before any check that `$VAULT` is a vault.
- `skill/SKILL.md:49-59` — mode selection, (a) bootstrap / (b) adopt.
- `skill/modes/bootstrap.md:91-92, 97, 111-116` — § 6 runs `claude_project_data.sh link` inside the
  live delivering session; line 97 "On Windows, adapt (directory junction)" is stale since tool 0.2
  makes the junction itself; § 9 finish.
- `skill/modes/adopt.md:89-92, 108-114` — § 5 locality; § 8 post-adopt.
- `scripts/claude_project_data.sh:221-227` — on Windows `link` / `adopt` refuse while a transcript in
  the harness folder changed in the last 2 minutes — so inside the delivering session they ABORT by
  design (the bootstrap / adopt modes never said so).
- `scripts/bootstrap_skill.sh:33` — `ln -s`; Git Bash copies by default, so on Windows no link exists.
- `README.md` (whole file) — stale ("engine not yet implemented", "13 standing rules", Set v1.1, 49
  lessons) and it is the GitHub landing page a team member opens first.

Pre-tests (numbers, not plausibility):

| # | Hypothesis | Result |
|---|---|---|
| P1 | A plain GitHub clone is a complete, clean vault | `git clone` 18 s, 3.5 MB (pack 1.00 MiB); HEAD `9b1c49e` == both remotes; `.claude/`, `docs/Plans/OPEN_TASKS.md`, `docs/fleet.csv`, `.venv/` absent (nothing private published) |
| P2 | Step 0 works from a named clone | `Delivering Standard Set Version v2.7 from vault commit 9b1c49e`; `pull --ff-only` → Already up to date |
| P3 | The installer can be exercised without touching the real machine | `HOME=<sandbox> bash scripts/bootstrap_skill.sh` → link inside the sandbox only; real `~/.claude/skills/standard-docset` unchanged |
| P4 | The draft Step 0 closes the wrong-source defect | matrix below — draft 5 / 5; current Step 0 pulls the current folder's repo in both no-link cases |
| P5 | § 5 is exact | 11 blocks parsed from the rendered text, applied to a fresh copy of `9b1c49e` → the 6 files byte-identical to the overlay; positive control (one FIND corrupted) → exactly 1 FAIL |
| P6 | A fresh Claude, given ONLY the self-test launcher, runs the self-test end-to-end and writes a verifiable report | a fresh agent, launcher 1 only (vault = a local bare repo holding the draft): **SUMMARY pass=17 fail=0 info=1** (clock); 8 min 03 s unattended (12:15:41–12:23:44 UTC) + clone + clone removal; ≈ 210 k tokens, 65 tool calls; its inner bootstrap report 6 / 6 PASS with a complete `REGISTRATION` line; `CLEANUP clone-removed`. Curator's independent check: a before / after snapshot of the vault (status, HEAD, local git config), the real skill link and the `~/.claude/projects` listing — **identical**; clone + sandbox gone; no bytecode in the vault. Its "unclear instructions" list: 12 items → § 2 + the Rule 13 record |
| P6b | The fixes hold on the final text | a second fresh agent on the final draft (vault = a local bare repo): **SUMMARY pass=17 fail=0 info=1** again; 7 min 52 s (12:27:00–12:34:52 UTC); ≈ 207 k tokens, 71 tool calls; every P6 fix followed (`locality` on the `STATUS:` line, commit message in the sandbox, the installer's link removed before `rm -rf`, the Python chosen by the version rule and named, the canonical `/private/var` sandbox path); curator snapshot identical (its only diff = this design commit's own manifest edit, made after the snapshot). Its 9 notes: 4 artifacts of the simulation (the off-limits folder held the first `python3`; a delegated agent's chat is not shown), 2 wording gaps fixed (the nested report's `started:` / `work_machine`), 3 pre-existing gaps queued (§ 2) |

Step 0 matrix (P4; § 8.1's script) — the Step 0 block extracted verbatim from the file and run from
inside a fresh decoy repository per case (the folder a session may be opened in); a `git` wrapper logs
every git call with the folder it acts on. Numbers = git calls acting on the decoy. (A first detector —
an `ls` of the decoy's `.git` — went blind after the first pull created `FETCH_HEAD`; the wrapper
replaced it, and the 0.2 control proves it sees the defect.)

| Case | Current Step 0 (0.2) | Draft Step 0 (0.3) |
|---|---|---|
| 1 vault folder named (a plain clone) | **3** (`rev-parse`, `pull --ff-only`, `rev-parse` on the decoy — 0.2 cannot take a named folder); prints `Set Version  from vault commit <decoy sha>` | **0** (2 calls, both in the vault); `Delivering … v2.7 … 9b1c49e` |
| 2 none named, skill link installed | 0 | **0**; same result |
| 3 none named, no link | **3**, incl. `pull` | **0** — `STOP: no vault folder named and no skill link`, no git call at all |
| 4 none named, a COPY in place of the link (Windows) | **2** via `git -C ""`, incl. `pull` | **0** — `STOP` as 3, no git call at all |
| 5 named folder is not a vault | **3**, incl. `pull` | **0** — `STOP: '…' is not a Standard DocSet vault`, no git call at all |

## 4. Phase tracker (high-level — granular sub-tasks in `PLAN-018_tracker.md`)

| Phase | What | Status |
|---|---|---|
| 0 | Audit + pre-tests (§ 3) | ✅ 2026-10-08 |
| 1 | Design + proven files + Rule 13 pass | ✅ 2026-10-08 |
| 2 | Operator approval (§ 9) | ✅ 2026-10-08 — "plan 018 approved, all A" |
| 3 | Implement — fresh session: 3.0 pre-checks → 3.1 reconcile → 3.2 apply § 5 + QA-S1 / S2 → 3.3 bookkeeping § 6c + QA-S3 → Rule 10 review → vault commit (§ 7.3; no push) | ✅ 2026-10-08 — reconcile 11 / 11, zero plan defects |
| 4 | Validate — QA-S1…S3 inside Phase 3; QA-S4 / S5 (operator, this Mac) and QA-S6 (Windows) after the push | 🔄 QA-S1…S3 ✅ 2026-10-08; QA-S4…S6 ⏸ (after the push) |
| 5 | Operator gate — push (§ 6d, before QA-S4…S6); closure commit (§ 7.4) | ⏸ |

## 5. Verbatim transformation rules (files proven in scratch; Phase 3 copies byte-for-byte)

**How to apply (Phase 3).** Each block carries a machine-readable marker (`<!-- block … -->`). Every
block's content sits in a **4-backtick** fence (` ````text ` … ` ```` `), because the carried files
contain their own 3-backtick fences; the content is exactly the lines between the two fence lines,
plus a final newline. The reconcile pass (§ 15.3) re-extracts every block from THIS file before the
first edit and checks it against the vault's working tree: each `whole` block's pre-image hashes as
stated (`git hash-object`), each `new` file is absent, each `replace` FIND matches exactly once —
checked in order per file, a later FIND against the text after the earlier REPLACEs. Any mismatch is a
named plan defect (D1, D2, …) — stop and surface it. Replace every `<P3-DATE>` with the Phase 3 date
checked against an external time authority (L079). All six files are vault files; there is no target
write in this plan.

<!-- §5-GENERATED:BEGIN -->

### 5a — `skill/SKILL.md` — 0.2 → 0.3: Step 0 named vault + vault check; selftest mode; the handoff report — WHOLE-FILE REPLACE
<!-- block id=5a path=skill/SKILL.md kind=whole pre_blob=b8e37576d9e056f0fd7aaa06fd701c3bd340138a -->
**5a** — the live file must hash to `b8e37576d9e056f0fd7aaa06fd701c3bd340138a` (`git hash-object`); replace its whole content with:

````text
---
name: standard-docset
description: Deliver the Standard DocSet governance suite to a project. Bootstrap mode sets up a NEW project from scratch; adopt mode migrates an EXISTING project onto the suite (dry-run gated, customization-preserving); selftest mode proves the skill works on this machine with a throwaway practice run. Every mode ends with a handoff report for the vault's curator. Use when asked to bootstrap, standardize, adopt, converge or self-test a project onto the standards suite.
---
<!-- VERSION: 0.3 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.3 — <P3-DATE> — PLAN-018 (one-prompt delivery): Step 0 takes the vault folder the operator's prompt
names (a plain clone works — no skill link needed, so Windows works too) and otherwise the installed
skill link, and checks it IS a vault before any git command (the old resolution fell back to the
current directory's repo when no link existed); a third mode, selftest; every mode ends with the
handoff report (new section).
v0.2 — 2026-10-05 — PLAN-017: the old-SETUP catch-up paragraph names the whole one-time prep
(heading wrap, sync-ready SET_VERSION_ADOPTED, locality script) and an engine dry-run before
registering — the gaps the first catch-up exposed.
v0.1 — 2026-08-16 — Initial (PLAN-009, Standard Set Version v2.0). Live-reference delivery skill:
two modes (bootstrap | adopt); replaces SETUP.md + NEW_PROJECT_BOOTSTRAP.md +
MEMORY_DURABILITY_ROLLOUT_PROMPT.md.
-->

# Standard DocSet — suite delivery skill

You are delivering a domain-neutral standards suite to a project. This skill carries **no copy** of
the suite — the vault it lives in is the single canonical source, and you read the suite LIVE from
it. You never edit the vault in a delivery session (read-only on `$VAULT`).

## Step 0 — resolve the vault + self-update (ALWAYS FIRST, before anything else)

The vault is the folder the operator's prompt names — usually a plain clone of the vault repo (the
way to use the skill without installing it, and the only way on Windows, where Git Bash copies
instead of linking). If the prompt names no folder, the vault is the target of the installed skill
link `~/.claude/skills/standard-docset`. Never guess it and never fall back to the current folder.

```bash
VAULT="<the vault folder named in the operator's prompt — leave empty if none was named>"
if [ -z "$VAULT" ]; then
  LINK="$HOME/.claude/skills/standard-docset"
  [ -L "$LINK" ] || { echo "STOP: no vault folder named and no skill link at $LINK"; exit 1; }
  VAULT="$(git -C "$(readlink -f "$LINK")" rev-parse --show-toplevel)"
fi
[ -f "$VAULT/skill/SKILL.md" ] && [ -f "$VAULT/docs/standards/STANDARDS_INDEX.md" ] \
  || { echo "STOP: '$VAULT' is not a Standard DocSet vault"; exit 1; }
git -C "$VAULT" pull --ff-only || echo "WARN: vault pull failed (offline / no remote / diverged) — proceeding with the local copy; surface this to the operator"
SUITE="$VAULT/docs/standards"
SET_VERSION="$(grep -m1 '^Standard Set Version:' "$SUITE/STANDARDS_INDEX.md" | awk '{print $NF}')"
VAULT_SHA="$(git -C "$VAULT" rev-parse --short HEAD)"
echo "Delivering Standard Set Version $SET_VERSION from vault commit $VAULT_SHA (vault: $VAULT)"
```

If it prints `STOP`, or `SET_VERSION` comes back empty, STOP and report — do not improvise a suite
location. Shell variables do not survive from one command to the next: carry the four values
(`VAULT`, `SUITE`, `SET_VERSION`, `VAULT_SHA`) forward and set them again in later commands.

## Binding session protocol (from message 1)

- ONE question / ONE step per message; WAIT for the operator's reply before the next step.
- Render choices INLINE as lettered options "(a) … (b) …" — never popup/modal questions.
- Verify via filesystem (`git status` / `ls` / `grep`) before acting; never assume what's there.
- Don't fill placeholders silently — if a value is unclear, ASK.
- No hedges ("maybe", "optionally", "if applicable") — state an explicit decision or ask.
- Commit messages via `git commit -F /tmp/<file>.txt` (never `-m` with escapes; never heredoc piped
  to `git commit`).
- Named, file-by-file code review BEFORE `git add`. **DO NOT PUSH** — push is operator-gated.
- Exception — selftest mode only: the operator answered every question in advance by launching it;
  `modes/selftest.md` says exactly what runs without waiting.

## Mode selection (one question)

If the operator's prompt already names the mode (for example "run the self-test"), use it. Otherwise
ask:

> Which delivery mode? (a) **bootstrap** — brand-new project (empty or nearly-empty repo);
> (b) **adopt** — existing project migrating onto the suite; (c) **selftest** — a throwaway practice
> run that proves the skill works on this machine and changes nothing.

Then read the matching file from this skill's directory and follow it exactly, in order:

- bootstrap → `modes/bootstrap.md`
- adopt → `modes/adopt.md`
- selftest → `modes/selftest.md`

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

## Handoff report (the last step of every mode)

Every mode ends by writing ONE plain-text report that the operator sends to the vault's curator, who
checks it against the vault. Write it also when the run STOPped early — say where and why.

- **Where:** the folder the operator's prompt names for reports; otherwise `$HOME/Desktop` if it
  exists, else `$HOME`. Name: `standard-docset-<mode>-report-<YYYYMMDD-HHMMSS>.txt` (UTC time).
- **What:** facts copied from command output, never from memory. No secrets (passwords, tokens,
  private keys); paths and git remote URLs are fine.
- **Layout** — these sections, in this order, one item per line:

```text
STANDARD DOCSET <MODE> REPORT
report-format: 1
started: <UTC> | finished: <UTC>
machine: os=<uname -s> arch=<uname -m> git=<git --version>
clock: local=<date -u> server=<Date header of an HTTPS reply — the vault's git host, or any well-known HTTPS host — or "unavailable">
vault: path=<VAULT> remote=<git -C VAULT remote get-url origin> head=<VAULT_SHA> set=<SET_VERSION>
target: path=<the project folder> remote=<its origin URL, or none> branch=<its branch>
CHECK <name> PASS|FAIL|SKIP|INFO <one-line evidence>
SUMMARY pass=<n> fail=<n> skip=<n> info=<n>
REGISTRATION name=<project> git_remote=<host/org/repo, or none> work_machine=<os + account> onboarding=<bootstrap|adopt> onboarded_on=<YYYY-MM-DD> onboarded_set=<SET_VERSION> commit=<delivery commit sha>
ANSWERS
<every question asked during the run, with the answer used — one per line>
STOPS
<every STOP or deviation from the mode file, with the reason — or "none">
NOTES
<anything the curator should look at — observations, not instructions>
RAW
<for every FAIL and STOP: the exact command and its full output>
```

- **CHECK lines** — bootstrap / adopt: one per result of the mode's Validate step (each governance
  script; `git status`; marker integrity), plus `locality` (the `STATUS:` line of
  `claude_project_data.sh status`) and `commit` (the delivery commit's sha, FAIL if none). selftest:
  the checks its mode file names. `REGISTRATION` only in bootstrap / adopt.
- Finally tell the operator the report's full path, and to send the FILE (not pasted text) to the
  curator. The curator treats the report as evidence; a lesson in it reaches the suite only through
  the project's `docs/STANDARDS_LOG.md` and the curator's review.
````

### 5b — `skill/modes/selftest.md` — NEW (0.1): the unattended throwaway self-test
<!-- block id=5b path=skill/modes/selftest.md kind=new -->
**5b** — the file must not exist yet; create it with:

````text
<!-- VERSION: 0.1 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.1 — <P3-DATE> — Initial (PLAN-018, one-prompt delivery): an unattended, throwaway end-to-end run of
the skill on a practice project in a temporary folder — checks every result, cleans up, and ends with
the handoff report; nothing else on the machine changes.
-->

# selftest mode — prove the skill works on this machine (unattended, throwaway)

Precondition: SKILL.md Step 0 ran (`$VAULT` / `$SUITE` / `$SET_VERSION` / `$VAULT_SHA` resolved).

**What this is.** The operator asked for a self-test: deliver the suite to a practice project that
lives only in a temporary folder, check every result, clean up, and write the handoff report
(SKILL.md § Handoff report, mode `selftest`). Nothing outside the temporary folder and the report file
changes.

**Standing authorization.** The operator who launched this answered every question in advance. Run
§§ 1–8 in order WITHOUT waiting for replies: the answers in § 3 ARE the operator's replies to every
question bootstrap mode asks, including "go on commit?" (= go). This replaces SKILL.md's
one-question-per-message rule for this mode only. Still post bootstrap's review table in chat — it is
the record.

**Where this run may write — nothing else:**

1. `$SANDBOX` (made in § 1) and everything under it.
2. The report file (SKILL.md § Handoff report).
3. `$VAULT` itself, ONLY through SKILL.md Step 0's `git pull --ff-only` (it updates the clone from its
   remote) and to delete it in § 7.4 when every condition there holds.

Everything else is read-only: `$VAULT` (apart from those two), `~/.claude/` (skills, projects, settings), any
other project, git config outside the practice project, every remote. Never push. Run git only in
`$VAULT` (read-only commands) and in the practice project. Every run of `claude_project_data.sh` and
`bootstrap_skill.sh` is prefixed with `HOME="$SANDBOX/home"` — the real `~/.claude` is never touched.

**This session's working folder is NOT the practice project** — it may be a real project. Write
every command with absolute paths: `git -C "$SANDBOX/practice" …` for every git command there
(including bootstrap's `git add` / `git commit`), `bash "$SANDBOX/practice/scripts/…"` for its
scripts. Never rely on a `cd` lasting into the next command.

**STOP rule.** When a command fails unexpectedly, or a check FAILs so that later steps would mean
nothing, stop running steps: go straight to § 7 (cleanup — always) and § 8 (report — always), and
record the STOP. A FAIL that does not block later steps is recorded and the run continues.

## 1. Start

- Record the UTC start time, `uname -s`, `uname -m`, `git --version`.
- Record the real skill link as it is now — `ls -ld "$HOME/.claude/skills/standard-docset" 2>&1` —
  word for word; § 7.3 compares it.
- Make the sandbox and record its path:

```bash
SANDBOX="$(cd "$(mktemp -d)" && pwd -P)"   # the real path — on macOS /var is /private/var
mkdir -p "$SANDBOX/home" "$SANDBOX/practice" "$SANDBOX/reports"
echo "$SANDBOX"
```

- CHECK `clock`: local `date -u` vs the `Date:` header of `curl -sI https://github.com` (any HTTPS
  host works). INFO with the difference in seconds; FAIL when it is over 300 seconds (dates written
  into the practice files would be wrong); INFO "unavailable" when curl fails.

## 2. Vault checks

- CHECK `vault-current`: `git -C "$VAULT" rev-parse HEAD` equals the first field of
  `git -C "$VAULT" ls-remote origin HEAD` (FAIL: the clone is stale or the remote unreachable —
  continue).
- CHECK `vault-clean`: `git -C "$VAULT" status --short` prints nothing.
- CHECK `suite-files`: every file bootstrap mode § 1 lists exists in `$SUITE` (name any missing one;
  a missing file is a STOP).
- CHECK `installer`: run `HOME="$SANDBOX/home" bash "$VAULT/scripts/bootstrap_skill.sh"`. PASS when
  `$SANDBOX/home/.claude/skills/standard-docset` is a symlink (`[ -L … ]`) whose `readlink` is
  `$VAULT/skill`; otherwise INFO "the installer made no link (Windows Git Bash copies instead of
  linking) — use a prompt that names the vault folder". Never a STOP.

## 3. Practice project + the operator's answers

```bash
git -C "$SANDBOX/practice" init -b main
git -C "$SANDBOX/practice" config user.name "Standard DocSet self-test"
git -C "$SANDBOX/practice" config user.email "selftest@example.invalid"
```

Answers for bootstrap mode — TARGET: `$SANDBOX/practice` (already a git repo); project name:
`docset-selftest`; domain: `throwaway self-test project`; language: Python 3.11+; deployment:
(a) local CLI; multi-agent: (a) no; CI: (c) none; "go on commit?": go. Any other question: take the
option the mode marks as recommended or default, and list it under ANSWERS in the report.

## 4. Run bootstrap mode

Read `$VAULT/skill/modes/bootstrap.md` and follow its §§ 1–9 with the § 3 answers, TARGET =
`$SANDBOX/practice`, with exactly these changes:

1. § 6 — run the locality script as
   `HOME="$SANDBOX/home" bash "$SANDBOX/practice/scripts/claude_project_data.sh" link`.
2. § 8 — write the commit message file inside `$SANDBOX` (for example `$SANDBOX/commit_msg.txt`), not
   in `/tmp`.
3. § 9 — skip its two follow-ups (the practice project is deleted at the end) and write bootstrap's
   handoff report into `$SANDBOX/reports/` (not the Desktop); § 5 checks it. In that report `started:`
   is the time § 4 began, and `work_machine` names this machine and account as usual (the sandbox HOME
   does not change it).

**Python for the governance scripts:** use the first of `python3`, `python3.13`, `python3.12`,
`python3.11` whose `--version` is 3.11 or newer (a `python3` from some project's virtual environment
may be older — check, don't assume); record which one under NOTES. If none is, bootstrap's Validate step
and the § 5 `governance` check are SKIP (with the versions seen), and the run continues.

## 5. Check the result — one CHECK line each, in this order

| CHECK | PASS when |
|---|---|
| `commit` | `git -C "$SANDBOX/practice" log --oneline` shows exactly 1 commit, and `git -C "$SANDBOX/practice" remote` prints nothing |
| `tree-clean` | `git -C "$SANDBOX/practice" status --short` prints nothing |
| `files` | all exist in the practice project: `CLAUDE.md`, `archive/LESSONS.md`, the 6 topical standards in `docs/standards/`, `docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`, `docs/STANDARDS_LOG.md`, `docs/SET_VERSION_ADOPTED.md`, `docs/documents_manifest.md`, `docs/folder_structure.md`, `docs/MACHINE_MIGRATION.md`, `scripts/claude_project_data.sh`, `scripts/check_doc_coverage.py`, `scripts/check_test_coverage_drift.py` (name any missing one) |
| `verbatim` | `cmp` finds no difference between each of the 6 topical standards and its `$SUITE` original, `archive/LESSONS.md` and `$SUITE/LESSONS.md`, `scripts/claude_project_data.sh` and `$VAULT/scripts/claude_project_data.sh` |
| `provenance` | `CLAUDE.md` contains both `$SET_VERSION` and `$VAULT_SHA`; `docs/SET_VERSION_ADOPTED.md` contains `- **Standard Set Version:** $SET_VERSION`, a `CHANGE LOG` line and the line `\| Set Version \| Adopted on \| Notes \|` |
| `markers` | for `CLAUDE.md`, `docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`: the count of `PROJECT-OWNED:BEGIN` equals the count of `PROJECT-OWNED:END`, and both equal the count in the matching `$SUITE` template |
| `governance` | both scripts exit 0, each run with the practice project as its working folder and the § 4 Python (`(cd "$SANDBOX/practice" && <python> scripts/check_doc_coverage.py)`, likewise `check_test_coverage_drift.py --ci`; SKIP as § 4 says) |
| `locality` | `HOME="$SANDBOX/home" bash "$SANDBOX/practice/scripts/claude_project_data.sh" status` prints a line starting `STATUS: OK` (on a new project it is followed by a `WARNING: no memory files` line — expected) |
| `handoff-report` | exactly one file in `$SANDBOX/reports/`, holding the lines `report-format: 1`, at least one `CHECK `, `SUMMARY ` and `REGISTRATION ` |
| `vault-untouched` | `git -C "$VAULT" status --short` prints nothing and `git -C "$VAULT" rev-parse HEAD` is unchanged since § 2 |

## 6. Read the bootstrap report into this one

Under NOTES, add the bootstrap report's `SUMMARY` line and its `STOPS` section, so the curator sees
both runs in one file.

## 7. Cleanup — ALWAYS, also after a STOP

1. Remove the practice project's harness link — never what it points to. Get its path from
   `HOME="$SANDBOX/home" bash "$SANDBOX/practice/scripts/claude_project_data.sh" status` (the
   `harness path:` line). macOS / Linux: `rm "<that path>"`. Windows (Git Bash):
   `cmd //c rmdir "$(cygpath -w "<that path>")"`. Then CHECK `unlink`: PASS when the harness path is
   gone AND `$SANDBOX/practice/.claude/project-data` still exists (proof nothing behind the link was
   deleted). If the link cannot be removed, STOP the cleanup here, leave `$SANDBOX` in place and say so
   in the report — never delete a folder that still holds a link.
2. Remove every other link the run left in the sandbox (the installer's skill link, anything the run
   made): `find "$SANDBOX" -type l -exec rm {} +`. Then `rm -rf "$SANDBOX"`; CHECK `sandbox-removed`:
   the path no longer exists.
3. CHECK `real-skill-link`: `ls -ld "$HOME/.claude/skills/standard-docset" 2>&1` prints exactly
   what § 1 recorded.
4. The clone — ONLY when all of these hold: the operator's prompt says the vault folder was cloned for
   this self-test; the folder's name is `docset-selftest`; `git -C "$VAULT" status --short` prints
   nothing. Then, AFTER § 8 has written the report: `rm -rf "$VAULT"`, and append the line
   `CLEANUP clone-removed <path>` to the report. Otherwise leave it and say why under NOTES.

## 8. Report

Write the handoff report (SKILL.md § Handoff report, mode `selftest`; no `REGISTRATION` line) with
the CHECK lines in run order, `target:` = the practice project, and under ANSWERS the § 3 answers
plus any default taken. Then tell the operator, in plain words: how many checks passed and failed,
and the report's full path — "send this file to the curator". Run § 7.4 last.
````

### 5c — `skill/modes/bootstrap.md` — 0.2 → 0.3: § 6 Windows note; § 9 handoff report
<!-- block id=5c.1 path=skill/modes/bootstrap.md kind=replace -->
**5c.1** FIND:

````text
<!-- VERSION: 0.2 -->
<!-- Last Updated: 2026-08-19 -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 0.3 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.3 — <P3-DATE> — PLAN-018: § 6 — the locality script makes the Windows junction itself (since tool 0.2) and, on Windows, refuses while this session is live — the operator links from Git Bash afterwards; § 9 ends with the handoff report (SKILL.md).
````

<!-- block id=5c.2 path=skill/modes/bootstrap.md kind=replace -->
**5c.2** FIND:

````text
- POSIX symlink — macOS/Linux. On Windows, adapt (directory junction) and say so.
````

REPLACE WITH:

````text
- The script makes a symlink on macOS / Linux and a directory junction on Windows (Git Bash) by
  itself. On Windows it refuses while this very session is live (`ABORT: … looks active` — its
  transcript sits in the harness folder): that is expected, not a failure. Finish the bootstrap, then
  tell the operator to close Claude Code and run `bash scripts/claude_project_data.sh link` from a
  Git Bash window; list it as a follow-up in the handoff report.
````

<!-- block id=5c.3 path=skill/modes/bootstrap.md kind=replace -->
**5c.3** FIND:

````text
(SESSION_OPENER pre-flight).
````

REPLACE WITH:

````text
(SESSION_OPENER pre-flight).

Then write the handoff report (SKILL.md § Handoff report, mode `bootstrap`).
````

### 5d — `skill/modes/adopt.md` — 0.3 → 0.4: § 5 Windows note; § 8 handoff report
<!-- block id=5d.1 path=skill/modes/adopt.md kind=replace -->
**5d.1** FIND:

````text
<!-- VERSION: 0.3 -->
<!-- Last Updated: 2026-10-03 -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 0.4 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.4 — <P3-DATE> — PLAN-018: § 5 notes the Windows locality refusal while this session is live (the operator links from Git Bash afterwards); § 8 ends with the handoff report (SKILL.md).
````

<!-- block id=5d.2 path=skill/modes/adopt.md kind=replace -->
**5d.2** FIND:

````text
  `adopt` (machine already has harness data for this path) or `link`; paste output; seed
````

REPLACE WITH:

````text
  `adopt` (machine already has harness data for this path) or `link`; paste output (on Windows
  the script refuses while this session is live — expected: the operator runs it from Git Bash with
  Claude Code closed, listed as a follow-up in the handoff report); seed
````

<!-- block id=5d.3 path=skill/modes/adopt.md kind=replace -->
**5d.3** FIND:

````text
own suite files.
````

REPLACE WITH:

````text
own suite files.

Then write the handoff report (SKILL.md § Handoff report, mode `adopt`) — it carries the facts the
curator needs for (1).
````

### 5e — `README.md` — refresh + the two launchers — WHOLE-FILE REPLACE
<!-- block id=5e path=README.md kind=whole pre_blob=56d37dc2e15cdfab6f9a77f9ebeff31ed5230977 -->
**5e** — the live file must hash to `56d37dc2e15cdfab6f9a77f9ebeff31ed5230977` (`git hash-object`); replace its whole content with:

````text
# Standard DocSet

A domain-neutral standards vault and CLI tool that keeps **standards / governance documentation
suites** up to date across the projects that adopt them.

It holds the canonical suite (`docs/standards/`), the delivery skill that sets a project up on it
(`skill/`), and the engine that keeps every registered project current afterwards
(`src/standard_document_updater/`). It is not tied to any single project's domain — the projects it
operates on are inputs, supplied at runtime.

## Use the standards — one prompt in Claude Code

You need: read access to this repository with an SSH key registered at its host, `git`, and Claude
Code (on Windows, Claude Code runs its commands in Git Bash). Nothing from this repository is
installed and nothing in it changes — Claude reads it from a clone in your home folder. Claude Code
asks before it runs a command; approve them.

**1. Test it first — changes nothing on your computer.** Open Claude Code in your home folder (not
inside a project) and send:

```text
Run the Standard DocSet self-test on this computer.

1. Clone git@github.com:780-AI/780-Docset.git into the new folder docset-selftest in my home folder (it is cloned for this self-test). If that folder already exists, stop and tell me.
2. Read skill/SKILL.md in that folder and follow it in selftest mode. The vault folder is that docset-selftest folder.
```

Claude works on its own (about 10 minutes), deletes everything it made, and leaves
`standard-docset-selftest-report-<time>.txt` on your Desktop. Send that file to the curator.

**2. Set up a project.** Open Claude Code in the project's folder and send:

```text
Set up the Standard DocSet standards for the project in this folder.

1. If the folder Standard-DocSet exists in my home folder, update it with git pull --ff-only; otherwise clone git@github.com:780-AI/780-Docset.git into that folder.
2. Read skill/SKILL.md in that folder and follow it. The vault folder is that Standard-DocSet folder; the project is the folder this session was opened in.
```

Claude asks a few questions about the project, one at a time, sets it up in one commit (it never
pushes), and leaves a handoff report on your Desktop. Send that file to the curator, who registers
the project — from then on, suite updates reach it without running this again.

A project that already carries the suite needs neither prompt: its updates come from the curator.

## For the curator

- `CLAUDE.md` — the binding operating contract; read it first.
- Engine: `python -m standard_document_updater {status,drift,fleet,harvest,integrate,sync}` —
  behavior in `docs/architecture.md`; the registry of projects is `config/projects.toml`.
- The current Standard Set Version and its history: `docs/standards/STANDARDS_INDEX.md`.
- `docs/SESSION_OPENER.md` / `docs/SESSION_CLOSER.md` — binding session start / end routines.
- `docs/documents_manifest.md` — the version index; `docs/folder_structure.md` — the layout.
- `docs/Plans/` — committed plans; `archive/LESSONS.md` — the incident-to-rule archive.
- A new machine: `docs/NEW_MACHINE_SETUP.md`.
````

### 5f — `docs/folder_structure.md` — 0.17 → 0.18: header + the skill/ tree
<!-- block id=5f.1 path=docs/folder_structure.md kind=replace -->
**5f.1** FIND:

````text
<!-- VERSION: 0.17 -->
<!-- Last Updated: 2026-10-07 -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 0.18 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.18 — <P3-DATE> — PLAN-018: added skill/modes/selftest.md to the tree; the skill/ line says a plain clone works too; SKILL.md's line names the handoff report.
````

<!-- block id=5f.2 path=docs/folder_structure.md kind=replace -->
**5f.2** FIND:

````text
├── skill/                         # delivery skill (live-reference; PLAN-009) — symlinked to ~/.claude/skills/standard-docset by scripts/bootstrap_skill.sh
│   ├── SKILL.md                   # mode dispatch + step-0 vault resolve/self-pull
│   └── modes/
│       ├── bootstrap.md           # NEW-project delivery (successor to SETUP.md)
│       └── adopt.md               # EXISTING-project migration (dry-run gated)
````

REPLACE WITH:

````text
├── skill/                         # delivery skill (live-reference; PLAN-009) — symlinked to ~/.claude/skills/standard-docset by scripts/bootstrap_skill.sh, or read from a plain clone (PLAN-018)
│   ├── SKILL.md                   # mode dispatch + step-0 vault resolve/self-pull + the handoff report
│   └── modes/
│       ├── bootstrap.md           # NEW-project delivery (successor to SETUP.md)
│       ├── adopt.md               # EXISTING-project migration (dry-run gated)
│       └── selftest.md            # unattended throwaway self-test on a practice project (PLAN-018)
````

<!-- §5-GENERATED:END -->

## 6. Spec update map (mechanical rules; same commit as the work)

- **6a — design commit (§ 7.1):** vault manifest — new rows **93** (PLAN-018 plan, 0.1 DRAFT, Plan) and
  **94** (tracker, 0.1, Plan); quick-index *Plans* `… 90–91` → `… 90–91, 93–94`; self-row 5; header +
  CHANGE LOG + Last-updated rotation. CHANGELOG top entry (plan drafted; no runtime impact).
- **6b — Phase 2 approval commit (§ 7.2):** plan + tracker 0.1 → 0.2 APPROVED with the § 9.1 decision
  record; manifest cells 93 / 94; CHANGELOG line.
- **6c — Phase 3 commit (§ 7.3):** manifest — cells **76** (`skill/SKILL.md`) → 0.3, **77**
  (`skill/modes/bootstrap.md`) → 0.3, **78** (`skill/modes/adopt.md`) → 0.4, **6**
  (`docs/folder_structure.md`) → 0.18; new row **95** `| 95 | Delivery skill — selftest mode | 0.1 |
  Delivery | \`skill/modes/selftest.md\` |` + quick-index *Delivery skill (vault-side)* `76–79` →
  `76–79, 95`; **93 / 94** → the plan / tracker headers; row 2 (`README.md`) keeps `-` (no VERSION
  header); self-row; grep-verify every touched cell == its file header (L063). CHANGELOG top entry: what
  shipped, the impact statement ("the delivery skill gains a named-vault Step 0, a selftest mode and the
  handoff report; the README is refreshed; no engine change, no `docs/standards/` change, no Set
  Version bump"), and a **QA scenarios** sub-section listing QA-S1…S6 with status. Plan + tracker →
  0.3 EXECUTING.
- **6d — push (Phase 5a), BEFORE QA-S4…S6:** the launchers clone from the organization repository, so
  the feature-ON scenarios run only after the Phase 3 commit is on both remotes (operator "push";
  governance; `ls-remote` both = HEAD; no tag).
- **6e — closure commit (§ 7.4):** plan + tracker → 1.0 CLOSED (QA evidence + waivers in the tracker);
  manifest cells 93 / 94 + rotation; CHANGELOG (QA-S4…S6 evidence).
- **6f — `docs/Plans/OPEN_TASKS.md`** (local, never committed): next actions; the 2026-08-19
  "hassle-free delivery" candidate marked SUPERSEDED by this plan; v2.8 queue + `STANDARDS_INDEX.md`
  § 4 self-service wording; deferred minor + `NEW_MACHINE_SETUP.md` clone-from-GitHub variant (the
  curator's own; `--origin github` + set the git identity).
- No engine source changes → `docs/architecture.md` untouched (§ 4 drift rule not triggered); no new
  top-level directory.

## 7. ALLOWLIST (the bullet enumeration IS the count — L038; plan + tracker included per L054)

### 7.1 Design commit (vault; 4 files)

- `docs/Plans/PLAN-018_one_prompt_delivery.md` (new)
- `docs/Plans/PLAN-018_tracker.md` (new)
- `docs/documents_manifest.md`
- `CHANGELOG.md`

### 7.2 Phase 2 approval commit (vault; 4 files)

- `docs/Plans/PLAN-018_one_prompt_delivery.md`
- `docs/Plans/PLAN-018_tracker.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`

### 7.3 Phase 3 commit (vault; 10 files)

- `skill/SKILL.md`
- `skill/modes/selftest.md` (new)
- `skill/modes/bootstrap.md`
- `skill/modes/adopt.md`
- `README.md`
- `docs/folder_structure.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-018_one_prompt_delivery.md`
- `docs/Plans/PLAN-018_tracker.md`

### 7.4 Closure commit (vault; 4 files)

- `docs/Plans/PLAN-018_one_prompt_delivery.md`
- `docs/Plans/PLAN-018_tracker.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`

## 8. Validation gate (Rule 11 scenarios; Rule 15 feature-ON marked ⚑; status in the tracker)

- **QA-S1 — domain-neutral gate (3.2).** `grep -rniE "780|estimator|everon|equinex|capital-signal|bahereh|parsaazad|a780" skill/`
  prints nothing (exit 1); control: the same pattern on `config/projects.toml` → hits.
- **QA-S2 ⚑ — Step 0 matrix (3.2).** § 8.1's script on the applied `skill/SKILL.md` and a clone of the
  vault: cases 1–2 print `Delivering Standard Set Version <current> from vault commit <sha>`; cases 3–5
  print `STOP`, exit 1 and make no git call at all; **0 git calls act on the decoy in all five**.
  Control (the detector can see the defect): the same script on the 0.2 Step 0
  (`git show HEAD:skill/SKILL.md` before the commit) → git calls on the decoy in cases 1, 3, 4, 5
  (§ 3 P4: 3 / 3 / 2 / 3).
- **QA-S3 — mechanics (3.3).** The two governance scripts exit 0 (stdout pasted); every touched manifest
  cell == its header (L063); each changed Markdown file has an even number of fence lines; the six files
  == § 5 applied to `9b1c49e` (the reconcile pass already proves it — record the blob of each).
- **QA-S4 ⚑ — the real self-test (operator, this Mac, after the push — § 6d).** Before: snapshot the
  vault's status / HEAD / local git config, the real skill link and the `~/.claude/projects` listing. A
  NEW Claude Code session opened in the home folder; the operator pastes launcher 1 copied from the
  repository's web page and approves the commands it asks for. Expected: the report on the Desktop —
  every CHECK PASS (`installer` PASS on macOS), `SUMMARY … fail=0`, `CLEANUP clone-removed`; after: the
  snapshot identical, `~/docset-selftest` and the sandbox gone, no new entry in `~/.claude/projects`
  other than the session's own (the session opened in the home folder writes its transcript there —
  expected, named in the report's NOTES or derived from the session folder name). Record the run time.
- **QA-S5 ⚑ — project setup (operator, this Mac, after the push).** A throwaway folder
  (`~/docset-setup-test`, `git init -b main`, a repo-local identity); a NEW Claude Code session opened
  in it; launcher 2 pasted; the operator answers the questions. Expected: one delivery commit; the
  files of QA-S4's `files` check; `claude_project_data.sh status` OK; a handoff report on the Desktop
  whose `REGISTRATION` line carries name / git_remote (none) / work_machine / onboarding=bootstrap /
  onboarded_on / onboarded_set (current) / commit (== the real sha), and whose ANSWERS list every
  question asked; `~/Standard-DocSet` created (or pulled). Cleanup (curator-guided): remove the practice
  harness link with `rm` (a symlink — never `rm -r`), delete the folder; keep or delete
  `~/Standard-DocSet` (operator).
- **QA-S6 ⚑ — Windows self-test (D-2).** A Windows user pastes launcher 1. Expected: every CHECK PASS
  except `installer`, which may be INFO (Git Bash copies instead of linking — the expected Windows
  result) or PASS (Developer Mode symlinks); `unlink` PASS via `cmd //c rmdir`; the report in Desktop or
  the home folder (a redirected Desktop is a fallback, not a failure).

### 8.1 Step 0 matrix script (QA-S2; verbatim — run as `bash step0_matrix.sh <SKILL.md> <vault clone> <workdir>`)

````bash
#!/usr/bin/env bash
# PLAN-018 QA-S2: run SKILL.md's Step 0 block (extracted verbatim) in five situations, from inside a
# decoy repository standing for "the folder the session was opened in". A git wrapper logs every git
# call with the folder it acts on; a call that acts on the decoy is the wrong-source defect.
# usage: step0_matrix.sh <SKILL.md> <vault clone> <workdir>
set -uo pipefail
SKILL="$1"; VCLONE="$2"; W="$3"
rm -rf "$W"; mkdir -p "$W/bin"
REAL_GIT="$(command -v git)"
awk '/^## Step 0/{s=1} s&&/^```bash$/{f=1;next} f&&/^```$/{exit} f' "$SKILL" > "$W/step0.sh"
echo "extracted $(wc -l < "$W/step0.sh" | tr -d ' ') lines from Step 0 of $SKILL"
cat > "$W/bin/git" <<EOF
#!/usr/bin/env bash
dir="\$PWD"
if [ "\${1:-}" = "-C" ]; then dir="\${2:-}"; [ -z "\$dir" ] && dir="\$PWD"; fi
( cd "\$dir" 2>/dev/null && printf '%s\t%s\n' "\$(pwd -P)" "\$*" >> "\$GIT_CALL_LOG" ) || printf '%s\t%s\n' "\$dir" "\$*" >> "\$GIT_CALL_LOG"
exec "$REAL_GIT" "\$@"
EOF
chmod +x "$W/bin/git"
mkdir -p "$W/home-none" "$W/home-link/.claude/skills" "$W/home-copy/.claude/skills" "$W/not-a-vault"
ln -s "$VCLONE/skill" "$W/home-link/.claude/skills/standard-docset"
cp -R "$VCLONE/skill" "$W/home-copy/.claude/skills/standard-docset"

run_case() {  # $1 label, $2 VAULT value to inject ("" = none named), $3 HOME dir
  local label="$1" named="$2" home="$3" n decoy
  decoy="$W/decoy-${label%% *}"
  "$REAL_GIT" init -q "$decoy"
  "$REAL_GIT" -C "$decoy" -c user.name=t -c user.email=t@x commit -q --allow-empty -m decoy
  "$REAL_GIT" -C "$decoy" remote add origin "$W/does-not-exist.git"
  decoy="$(cd "$decoy" && pwd -P)"
  sed "s#^VAULT=\"<the vault folder named in the operator's prompt — leave empty if none was named>\"#VAULT=\"$named\"#" \
    "$W/step0.sh" > "$W/case.sh"
  : > "$W/calls.log"
  out="$(cd "$decoy" && PATH="$W/bin:$PATH" GIT_CALL_LOG="$W/calls.log" HOME="$home" bash "$W/case.sh" 2>&1)"; rc=$?
  n="$(awk -F'\t' -v d="$decoy" '$1==d' "$W/calls.log" | wc -l | tr -d ' ')"
  echo "=== $label (exit $rc) ==="
  printf '%s\n' "$out" | sed 's/^/    /'
  echo "    git calls: $(wc -l < "$W/calls.log" | tr -d ' ') total, $n acting on the decoy (the session's folder)"
  awk -F'\t' -v d="$decoy" '$1==d {print "      decoy <- git " $2}' "$W/calls.log"
}

run_case "1 named vault clone"                 "$VCLONE"          "$W/home-none"
run_case "2 none named, skill link installed"  ""                 "$W/home-link"
run_case "3 none named, no link"               ""                 "$W/home-none"
run_case "4 none named, a COPY (Windows-like)" ""                 "$W/home-copy"
run_case "5 named folder is not a vault"       "$W/not-a-vault"   "$W/home-none"
````

## 9. Operator decision points (Phase 2 — answer with the approval)

- **D18.A — approve the plan** ("plan 018 is approved", or "APPROVE PLAN-018" with any D-deltas).
- **D-1 — what the self-test covers.** RECOMMEND **A**: bootstrap mode only — adopt mode's change is its
  last lines (the Windows note + the report), exercised at its next real use; that half of its
  feature-ON evidence is waived by the operator and recorded in the tracker's waiver register. B: the
  self-test also adopts a second practice project ("an existing project") — about twice the run time,
  a fixture to design, P6 re-run before approval.
- **D-2 — Windows.** RECOMMEND **A**: ship-gating — the plan closes only with a Windows self-test report
  (QA-S6); the Windows path is half the point. B: close on macOS evidence with an explicit waiver; the
  README then says "Windows: not yet verified" until a run (a § 5e edit in the approval commit).
- **D-3 — README.** RECOMMEND **A**: refresh the whole file (§ 5e) — it is the landing page and states
  nothing true about today's vault. B: add the launcher section only, the stale lines stay (§ 5e becomes
  an insertion block).
- **D-4 — the self-test deletes its own clone.** RECOMMEND **A**: yes, guarded (the prompt says the
  folder was cloned for this self-test, its name is `docset-selftest`, its tree is clean) — the run is
  fully hands-off. B: keep it; the closing message tells the user to delete the folder (§ 5b § 7.4
  becomes that sentence).

### 9.1 Decision record (Phase 2, 2026-10-08)

- **D18.A — APPROVED:** operator *"go on commit; plan 018 approved, all A"* (2026-10-08).
- **D-1 = A** — the self-test covers bootstrap mode only. Adopt mode's two changes (§ 5d: the Windows note
  in § 5 and the handoff report in § 8) are code-reviewed in Phase 3; their feature-ON evidence is
  **waived by the operator until adopt mode's next real use** (recorded in the tracker's waiver register,
  Rule 15) — that run's handoff report is the evidence.
- **D-2 = A** — Windows is ship-gating: the plan closes only with a Windows self-test report (QA-S6).
- **D-3 = A** — the README is refreshed as a whole (§ 5e as written).
- **D-4 = A** — the self-test deletes its own clone, guarded (§ 5b § 7.4 as written).
- **No § 5 change:** the blocks re-extracted from this file stay byte-identical to the proven files
  (re-verified in the approval commit).

## 10. Rollback path

- `git revert` the Phase 3 commit and push both remotes: `skill/` back to 0.2 / 0.3, the README back.
  A launcher started before the revert keeps its own clone — nothing on the user's machine depends on
  the vault afterwards (the self-test leaves nothing; a set-up project holds plain files + one commit).
- No target is written by the curator in this plan, no engine change, no data migration.

## 11. Known risks + mitigation

| # | Risk | Mitigation |
|---|---|---|
| R1 | The unattended session drifts from the mode file (skips a check, invents a step) | fixed report layout with named CHECKs; the curator verifies every line against expectations; P6 measured the drift on the draft (§ 3) |
| R2 | The self-test touches the real machine — a relative command lands in the folder the session was opened in, or removing the practice link follows it | absolute paths + `git -C` everywhere (rule in § 5b); `HOME="$SANDBOX/home"` for both scripts; unlink → verify the store still exists → only then `rm -rf`; the write ALLOWLIST; QA-S4's before / after snapshot |
| R3 | The clone deletion removes a real vault | three guards (§ 5b § 7.4); launcher 2 uses a different folder name (`Standard-DocSet`); D-4 = B removes the step |
| R4 | Permission prompts or the auto-mode safety classifier block a step | the STOP rule — report what was blocked, never work around it (the 2026-10-07 transcript-write precedent); the README says to approve the commands |
| R5 | Windows specifics (temp folder, `cmd //c rmdir`, a OneDrive-redirected Desktop) | report falls back to the home folder; unlink failure leaves the sandbox and says so; QA-S6 (D-2) |
| R6 | Launcher 2 run on a project already on the suite | SKILL.md forbids a delivery over an existing adopter (unchanged); the README says such projects need neither prompt |
| R7 | A secret ends up in a report | the "no secrets" rule; facts from command output only; the curator reads the report before forwarding anything |
| R8 | The launcher is mangled in transit (a chat app strips paired `*` / `_`) | the launchers contain neither; they are copied from the repository page, or relayed as a `.txt` file |
| R9 | Run time / cost on a team machine | measured in P6 and stated in the README |
| R10 | No Python 3.11+ on the machine | governance becomes SKIP, not FAIL — the report is still useful |
| R11 | Step 0's new STOP surprises an operator who relied on the old current-folder fallback | that fallback only ever "worked" inside the vault itself — a vault session never runs the skill; the STOP message names both ways to fix it |

## 12. Acceptance criteria

1. QA-S1…S3 ✅ in the Phase 3 session; QA-S4 + S5 ✅ after the push; QA-S6 ✅ (or the D-2 = B waiver);
   the adopt-report waiver recorded if D-1 = A.
2. Step 0 runs no git command outside a verified vault (QA-S2 cases 3–5, control red on 0.2).
3. A NEW session given only launcher 1 finishes unattended with `fail=0` on macOS and leaves the machine
   as it found it (QA-S4 snapshot).
4. Launcher 2 ends in a delivery commit and a report whose `REGISTRATION` line holds every fact the
   registry needs (QA-S5).
5. `skill/` passes the domain-neutral gate; `README.md` is the only file carrying the clone URL.
6. Every manifest cell touched == its file header; governance exit 0 in the vault (stdout pasted).
7. Plan + tracker 1.0 / CLOSED; OPEN_TASKS: the "hassle-free delivery" candidate superseded, the v2.8
   queue holds the `STANDARDS_INDEX.md` § 4 wording.

## Rule 13 senior-review pass (2026-10-08)

Run on the complete plan + tracker, after drafting, with the canonical § 15.8 prompt.

**Mechanical (L051 — the files exactly as they ship):** § 5 generated from the scratch overlay and parsed
back from THIS file's text (4-backtick fences): the 11 blocks applied to a fresh copy of `9b1c49e` → the
6 files byte-identical to the overlay; positive control (one FIND corrupted) → exactly 1 FAIL. `skill/`
domain-neutral grep → exit 1. Every changed Markdown file has an even number of fence lines. § 8.1's
script on the final Step 0 → 0 git calls on the decoy in 5 / 5; on 0.2 → 3 / 0 / 3 / 2 / 3 (the control).
P6b — a second fresh agent on the final text: 17 PASS / 0 FAIL / 1 INFO, every fix followed, the machine identical before and after. No Python source in this plan: ruff / mypy /
pytest are not affected (no `src/`, `tests/` or script change); the vault governance scripts run on the
design commit.

**Findings fixed in place:**

1. **Defect — wrong source (P4).** Step 0 ran `git pull` before checking that `$VAULT` is a vault, and with
   no skill link it fell back to the current folder's repo. → the vault check runs first; no fallback.
2. **Defect — the self-test's write list contradicted the run (P6 #1, #2).** Step 0's `pull` and
   bootstrap's `/tmp` commit-message file were outside it. → the pull is named; the message file goes in
   the sandbox.
3. **Defect — `locality` could not pass as worded (P6 #3).** Tool 0.3 prints a `WARNING: no memory files`
   line after `STATUS: OK` on a new project. → judged on the `STATUS:` line (selftest § 5, SKILL.md).
4. **Gap — relative commands (found while drafting, before P6).** The session's folder may be a real
   project; a split `git config` or `bash scripts/…` would land there. → absolute paths + `git -C`.
5. **Gap — which Python (P6 #11).** The first `python3` on PATH was another project's virtual
   environment. → an explicit order with a version check; SKIP when none qualifies.
6. **Gap — links left before `rm -rf` (P6 #10).** → every link in the sandbox removed first.
7. **Gap — `/var` vs `/private/var` (P6 #12).** → the sandbox path is made canonical (`pwd -P`).
8. **Gap — bootstrap § 9's follow-ups in a throwaway run (P6 #9).** → skipped in selftest.
9. **Gap — the report's clock line assumed an HTTPS vault host (P6 #4).** → any well-known HTTPS host.
10. **Gap — Windows inside the delivering session** (`claude_project_data.sh:221-227`). The locality
    script refuses while that session is live. → bootstrap § 6 and adopt § 5 say it is expected and that
    the operator links from Git Bash afterwards (a handoff-report follow-up).
11. **Gap — the bootstrap report nested in a self-test (P6b #6, #7).** Its `started:` and `work_machine`
    were ambiguous. → selftest § 4 says what each means there.
12. **Defect in my own test harness.** The first Step 0 detector (an `ls` of the decoy's `.git`) went blind
    once the first pull had created `FETCH_HEAD`. → a git wrapper logging every call + a fresh decoy per
    case; the 0.2 control proves the detector sees the defect.

**Considered and declined:** (a) an engine-as-oracle CHECK in the self-test — P6's agent ran
`sync.plan_target` on its own and found the practice project in sync; built in, it would couple the
skill to engine internals and require the engine to be importable on every team machine. A registry-free
dry run in the engine CLI (for example `sync --path <dir>`) is the right tool → engine candidate in
OPEN_TASKS. (b) Pre-answering project setup (launcher 2) — project facts are asked (CLAUDE.md § 10).
(c) Fixing bootstrap's three pre-existing gaps here (§ 2) — they widen the scope; queued. (d) Making
`bootstrap_skill.sh` Windows-aware — superseded by the named-vault path.

**Edge cases walked:** a named clone / a link / no link / a copy / not a vault (P4); a stale clone
(`vault-current` FAIL, the run continues); no Python 3.11+ (SKIP); a OneDrive-redirected Desktop (the home
folder fallback); a STOP mid-run (cleanup + report always); the unlink failing (the sandbox is kept and the
report says so); clone deletion (three guards); the session opened inside a real project (absolute
paths); permission prompts and classifier blocks (the STOP rule); launcher 2 on a project already on the
suite (SKILL.md forbids it).

**New design decisions surfaced:** D-1…D-4 (§ 9) — none decided silently.
