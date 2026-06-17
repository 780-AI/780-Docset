<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-17 -->
<!-- Source: standards-source/ (canonical). Added under Standard Set Version v1.2. -->

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
> 5. Confirm `.claude/` is NOT gitignored (so the memory content rides the project's sync) but that you
>    are NOT committing the memory content unless this project opts into git-tracking it.
> 6. Run this project's governance + code review, then commit per its rules.
>
> Files modified this session — enumerate them and reconcile against `git status`; raise any mismatch.

---

**Recovery note:** if memory was already lost before this rollout, the only lossless source is the prior
machine's `~/.claude/projects/<old-key>/memory/` (or a backup/sync of it). Copy those `.md` files into
`./.claude/memory/` (they go live immediately through the symlink). Otherwise reconstruct from whatever
the project committed/synced.
