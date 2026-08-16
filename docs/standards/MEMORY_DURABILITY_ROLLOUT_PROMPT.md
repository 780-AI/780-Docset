<!-- VERSION: 1.2 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Source: standards-source/ (canonical). Added under Standard Set Version v1.2. -->
<!--
CHANGE LOG
v1.2 — 2026-08-16 — Standard Set Version v1.5 (PLAN-010): retargeted from the memory-symlink pattern to
Rule 14 project-data locality — the prompt now creates scripts/claude_project_data.sh (status/adopt/link;
physical home .claude/project-data/ for memory + session transcripts), runs adopt for existing harness
data (absorbing the pre-v1.5 memory-symlink layout), wires the SESSION_CLOSER § 1.6 close-side confirm,
and seeds docs/MACHINE_MIGRATION.md. PLAN-009 will absorb this prompt into the setup skill's retrofit
mode.
v1.1 — 2026-06-20 — Reconciled step 5 with the settled Rule 14 practice: the memory store is now
GITIGNORED (`.claude/` in .gitignore) so it stays untracked + sync-carried AND a stray `git add -A` can
never accidentally commit it — superseding the original "NOT gitignored" wording; added `.gitignore` to
the ALLOWLIST. No Set-Version change (the Rule 14 capability is unchanged; this is a wording fix).
v1.0 — 2026-06-17 — Initial (Standard Set Version v1.2): paste-in prompt to set up Rule 14 durable memory.
-->

# Project-data locality rollout prompt (paste into a Claude Code session)

**Purpose:** make a project's Claude data — persistent memory AND session transcripts — live inside the
project folder and survive a machine change / folder rename/move, per the standards suite's `CLAUDE.md`
Rule 14 (project-data locality, Standard Set Version v1.5+). Paste the block below into a fresh Claude
Code session opened in the project's root directory. Works for both a fresh setup and a retrofit of the
pre-v1.5 memory-symlink layout (`adopt` absorbs it).

> **Platform note:** the mechanism uses a POSIX symlink and is targeted at macOS / Linux. On Windows,
> adapt step 1 (e.g. a directory junction) or keep the data in a synced path by another means.

---

> Set up Rule 14 project-data locality for THIS repository, per the standards suite.
>
> ALLOWLIST — you may touch ONLY these paths; if anything else appears in `git status`, STOP and report:
> - `scripts/claude_project_data.sh` (create; replaces `scripts/bootstrap_memory.sh`, which is deleted
>   if present)
> - `CLAUDE.md` (upgrade/add Rule 14)
> - `docs/SESSION_OPENER.md` (replace/add § 1.5 + the § 3.1 row)
> - `docs/SESSION_CLOSER.md` (add the § 1.6 locality confirm)
> - `docs/MACHINE_MIGRATION.md` (create — the out-of-folder state catalog)
> - `.gitignore` (ensure `.claude/`)
> - `.claude/project-data/` (created by the script — leave untracked)
> - your manifest / CHANGELOG per this project's governance
>
> Steps:
> 1. Create `scripts/claude_project_data.sh` with the body the suite ships (verbs `status` / `adopt` /
>    `link`; physical home `<repo>/.claude/project-data/`; symlink left at the harness path
>    `~/.claude/projects/<path-key>/`, where <path-key> = the repo's absolute path with every
>    non-alphanumeric character replaced by `-`; `adopt` merges without clobbering and absorbs the
>    pre-v1.5 layout where `memory/` inside the harness dir symlinks to `<repo>/.claude/memory`).
> 2. Run `bash scripts/claude_project_data.sh adopt` if this machine already has harness data for this
>    path (the usual retrofit case); otherwise `... link`. Then run `... status` and paste its output —
>    expect `STATUS: OK`.
> 3. Upgrade the repo-root `CLAUDE.md` Rule 14 to the project-data-locality text (copy from the suite's
>    `docs/standards/CLAUDE.md` Rule 14, adjusting the sync-tool parenthetical and the machine-migration
>    doc name to this project's reality).
> 4. Replace/add `§ 1.5 Project-data locality` in `docs/SESSION_OPENER.md` (copy from the suite) + the
>    § 3.1 row; add the `§ 1.6` locality confirm to `docs/SESSION_CLOSER.md` (copy from the suite).
> 5. Create `docs/MACHINE_MIGRATION.md` — the catalog of project state that genuinely cannot live in
>    the folder: H1 + a one-line "everything project-local lives in the folder (Rule 14); list here
>    ONLY what cannot, with migration steps" note + an empty two-column table (What | How to migrate).
>    Register it in the manifest.
> 6. Ensure `.claude/` is in `.gitignore` — the store stays untracked and rides the project's sync
>    (gitignore does not stop the sync), and a stray `git add -A` can never accidentally commit it. (Do
>    NOT git-track the project-data content unless this project deliberately opts in.)
> 7. Run this project's governance + code review, then commit per its rules.
>
> Files modified this session — enumerate them and reconcile against `git status`; raise any mismatch.

---

**Recovery note:** if data was already lost before this rollout, the only lossless source is the prior
machine's `~/.claude/projects/<old-key>/` (or a backup/sync of it). Copy its contents into
`./.claude/project-data/` (they go live immediately through the symlink). Otherwise reconstruct from
whatever the project committed/synced.

**Roadmap note:** PLAN-009 (the setup skill) absorbs this prompt into its retrofit/adopt mode; the
prompt remains the manual path until then.
