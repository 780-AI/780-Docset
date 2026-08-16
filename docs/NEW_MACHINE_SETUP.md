<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Re-home checklist: bring this vault to full operation on a new machine. Project-local (not a suite file). -->
<!--
CHANGE LOG
v1.1 — 2026-08-16 — Standard Set Version v1.5 (PLAN-010): this doc now doubles as the Rule 14 machine-migration catalog (§§ 2–3 ARE the out-of-folder state entries); § 4 retargeted memory symlink → project-data link (claude_project_data.sh status/adopt/link replaces bootstrap_memory.sh); § 1 intro mentions .claude/project-data/.
v1.0 — 2026-06-17 — Initial. Derived from the 2026-06-17 re-home (L050).
-->

# New-machine setup — re-homing this vault

The repository folder is Dropbox-synced, so the **files** travel automatically (tracked + untracked,
including `.claude/project-data/` — memory + session transcripts — and `.git`). What does **not** travel
is everything machine-local: the Python toolchain, the harness project-data **symlink**, and SSH push
credentials. Walk this once on a new machine (and after any folder move) to restore full operation.
Derived from the 2026-06-17 re-home (see `archive/LESSONS.md` L050).

> **This doc is also the Rule 14 machine-migration catalog** — the named register of project state that
> genuinely cannot live in the project folder. Its entries are the sections below: the Python toolchain
> (§ 2, rebuilt per machine), and SSH push credentials (§ 3, per-machine keys). Anything new that must
> live outside the folder is added here with its migration steps, same-commit (per `CLAUDE.md` Rule 14).

## 1. Repo

Sync/clone the repo. Confirm `git status` is clean and `git rev-parse HEAD` matches the remote
(`git ls-remote origin master`).

## 2. Python toolchain (engine needs ≥ 3.11 — `tomllib`, `StrEnum`)

A Dropbox-carried `.venv` is **not** reusable — virtual envs hardcode machine paths. Rebuild it:

```bash
# install uv if absent (one-time per machine):
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.11
rm -rf .venv && uv venv --python 3.11 .venv
uv pip install -e ".[dev]"
```

Verify: `.venv/bin/python -m standard_document_updater --version`, `.venv/bin/ruff check src tests`,
`MYPYPATH=src .venv/bin/python -m mypy`, `.venv/bin/python -m pytest -q`, and both governance scripts.
(Best practice: keep `.venv` out of the synced path, or just treat the synced copy as disposable.)

## 3. SSH push key

```bash
ssh-keygen -t ed25519 -C "<your-email>" -f ~/.ssh/id_ed25519
pbcopy < ~/.ssh/id_ed25519.pub        # then add it at GitLab → Settings → SSH Keys
ssh -T git@gitlab.com                 # expect: Welcome to GitLab, @<user>!
```

## 4. Project-data link (per `CLAUDE.md` Rule 14)

```bash
bash scripts/claude_project_data.sh link     # re-points ~/.claude/projects/<key> → ./.claude/project-data
bash scripts/claude_project_data.sh status   # expect: STATUS: OK
```

The **content** (memory + session transcripts) is already present (Dropbox carried
`./.claude/project-data/`); only the machine-local symlink needs re-creating — `link` also merges in any
stray harness dir a pre-link session created. If the store is unexpectedly empty, recover per L050 (a
backup/sync of the prior machine's `~/.claude`).

## 5. Pre-flight

Run the `docs/SESSION_OPENER.md` § 1 pre-flight — its § 1.5 runs `claude_project_data.sh status` and
names the fix verb on any non-OK state, so a healthy run confirms the re-home is complete.
