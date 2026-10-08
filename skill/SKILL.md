---
name: standard-docset
description: Deliver the Standard DocSet governance suite to a project. Bootstrap mode sets up a NEW project from scratch; adopt mode migrates an EXISTING project onto the suite (dry-run gated, customization-preserving); selftest mode proves the skill works on this machine with a throwaway practice run. Every mode ends with a handoff report for the vault's curator. Use when asked to bootstrap, standardize, adopt, converge or self-test a project onto the standards suite.
---
<!-- VERSION: 0.3 -->
<!-- Last Updated: 2026-10-08 -->
<!--
CHANGE LOG
v0.3 — 2026-10-08 — PLAN-018 (one-prompt delivery): Step 0 takes the vault folder the operator's prompt
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
