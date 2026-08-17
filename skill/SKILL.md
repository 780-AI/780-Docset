---
name: standard-docset
description: Deliver the Standard DocSet governance suite to a project. Bootstrap mode sets up a NEW project from scratch; adopt mode migrates an EXISTING project onto the suite (dry-run gated, customization-preserving). Use when asked to bootstrap, standardize, adopt, or converge a project onto the standards suite.
---
<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-08-16 -->
<!--
CHANGE LOG
v0.1 — 2026-08-16 — Initial (PLAN-009, Standard Set Version v2.0). Live-reference delivery skill:
two modes (bootstrap | adopt); replaces SETUP.md + NEW_PROJECT_BOOTSTRAP.md +
MEMORY_DURABILITY_ROLLOUT_PROMPT.md.
-->

# Standard DocSet — suite delivery skill

You are delivering a domain-neutral standards suite to a project. This skill carries **no copy** of
the suite — the vault it lives in is the single canonical source, and you read the suite LIVE from
it. You never edit the vault in a delivery session (read-only on `$VAULT`).

## Step 0 — self-update + resolve the vault (ALWAYS FIRST, before anything else)

```bash
SKILL_DIR="$(cd "$(readlink -f "$HOME/.claude/skills/standard-docset")" && pwd)"
VAULT="$(git -C "$SKILL_DIR" rev-parse --show-toplevel)"
git -C "$VAULT" pull --ff-only || echo "WARN: vault pull failed (offline / no remote / diverged) — proceeding with the local copy; surface this to the operator"
SUITE="$VAULT/docs/standards"
SET_VERSION="$(grep -m1 '^Standard Set Version:' "$SUITE/STANDARDS_INDEX.md" | awk '{print $NF}')"
VAULT_SHA="$(git -C "$VAULT" rev-parse --short HEAD)"
echo "Delivering Standard Set Version $SET_VERSION from vault commit $VAULT_SHA"
```

If `$SUITE` does not exist or `SET_VERSION` comes back empty, STOP and report — do not improvise a
suite location.

## Binding session protocol (from message 1)

- ONE question / ONE step per message; WAIT for the operator's reply before the next step.
- Render choices INLINE as lettered options "(a) … (b) …" — never popup/modal questions.
- Verify via filesystem (`git status` / `ls` / `grep`) before acting; never assume what's there.
- Don't fill placeholders silently — if a value is unclear, ASK.
- No hedges ("maybe", "optionally", "if applicable") — state an explicit decision or ask.
- Commit messages via `git commit -F /tmp/<file>.txt` (never `-m` with escapes; never heredoc piped
  to `git commit`).
- Named, file-by-file code review BEFORE `git add`. **DO NOT PUSH** — push is operator-gated.

## Mode selection (one question)

Ask the operator:

> Which delivery mode? (a) **bootstrap** — brand-new project (empty or nearly-empty repo);
> (b) **adopt** — existing project migrating onto the suite.

Then read the matching file from this skill's directory and follow it exactly, in order:

- bootstrap → `modes/bootstrap.md`
- adopt → `modes/adopt.md`

If the operator says the project is an **old-SETUP adopter** (already carries the suite, just a
stale Set Version), neither mode applies — tell them the path is: register the project in the
vault's `config/projects.toml`, hand-apply the one-time v1.6 heading-wrap if it predates v1.6, and
let `sync` catch it up. Do not run a delivery mode over an existing adopter.
