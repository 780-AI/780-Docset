<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-06-20 -->
<!-- Source: standards-source/ (canonical). Added under Standard Set Version v1.2. -->
<!--
CHANGE LOG
v1.1 — 2026-06-20 — Reconciled step 5 with the settled Rule 14 practice: the memory store is now
GITIGNORED (`.claude/` in .gitignore) so it stays untracked + sync-carried AND a stray `git add -A` can
never accidentally commit it — superseding the original "NOT gitignored" wording; added `.gitignore` to
the ALLOWLIST. No Set-Version change (the Rule 14 capability is unchanged; this is a wording fix).
v1.0 — 2026-06-17 — Initial (Standard Set Version v1.2): paste-in prompt to set up Rule 14 durable memory.
-->

# Memory-durability rollout prompt (paste into a Claude Code session)

**Purpose:** make a project's Claude memory survive a machine change and a folder rename/move, per the
standards suite's `CLAUDE.md` Rule 14. Paste the block below into a fresh Claude Code session opened in
the project's root directory.

> **Platform note:** the mechanism uses a POSIX symlink and is targeted at macOS / Linux. On Windows,
> adapt step 1 (e.g. a directory junction) or keep memory in a synced path by another means.

---

> Set up durable Claude memory for THIS repository, per the standards suite's Rule 14.
>
> ALLOWLIST — you may touch ONLY these paths; if anything else appears in `git status`, STOP and report:
> - `scripts/bootstrap_memory.sh` (create)
> - `CLAUDE.md` (add Rule 14)
> - `docs/SESSION_OPENER.md` (add § 1.5 + the § 3.1 row)
> - `.gitignore` (add `.claude/`)
> - `.claude/memory/` (create dir — leave untracked)
> - `.claude/README_memory.md` (create — untracked)
> - your manifest / CHANGELOG per this project's governance
>
> Steps:
> 1. Create `scripts/bootstrap_memory.sh` with the body the suite ships (idempotent: derive the harness
>    key from the repo's absolute path — `'/'`→`'-'`, `' '`→`'-'` — and (re)create the symlink
>    `~/.claude/projects/<key>/memory → <repo>/.claude/memory`, preserving any pre-existing files).
> 2. `mkdir -p .claude/memory` and run `bash scripts/bootstrap_memory.sh`; paste its output.
> 3. Add Rule 14 to the repo-root `CLAUDE.md` (copy the text from the suite's `docs/standards/CLAUDE.md`
>    Rule 14, adjusting the sync-tool name in parentheses to this project's reality).
> 4. Add `§ 1.5 Memory-link health` to `docs/SESSION_OPENER.md` (copy from the suite) + the § 3.1 row.
> 5. Add `.claude/` to `.gitignore` — the memory store stays untracked and rides the project's sync
>    (gitignore does not stop the sync), and a stray `git add -A` can never accidentally commit it. (Do
>    NOT git-track the memory content unless this project deliberately opts in.)
> 6. Run this project's governance + code review, then commit per its rules.
>
> Files modified this session — enumerate them and reconcile against `git status`; raise any mismatch.

---

**Recovery note:** if memory was already lost before this rollout, the only lossless source is the prior
machine's `~/.claude/projects/<old-key>/memory/` (or a backup/sync of it). Copy those `.md` files into
`./.claude/memory/` (they go live immediately through the symlink). Otherwise reconstruct from whatever
the project committed/synced.
