<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-10-08 -->
<!--
CHANGE LOG
v0.1 — 2026-10-08 — Initial (PLAN-018, one-prompt delivery): an unattended, throwaway end-to-end run of
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
