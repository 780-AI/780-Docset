<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-17 -->
<!-- Re-home checklist: bring this vault to full operation on a new machine. Project-local (not a suite file). -->

# New-machine setup — re-homing this vault

The repository folder is Dropbox-synced, so the **files** travel automatically (tracked + untracked,
including `.claude/memory/` and `.git`). What does **not** travel is everything machine-local: the Python
toolchain, the harness memory **symlink**, and SSH push credentials. Walk this once on a new machine (and
after any folder move) to restore full operation. Derived from the 2026-06-17 re-home (see
`archive/LESSONS.md` L050).

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

## 4. Memory symlink (per `CLAUDE.md` Rule 14)

```bash
bash scripts/bootstrap_memory.sh      # re-creates ~/.claude/projects/<key>/memory → ./.claude/memory
```

The memory **content** is already present (Dropbox carried `./.claude/memory/`); only the machine-local
symlink needs re-creating. If the store is unexpectedly empty, recover per L050 (a backup/sync of the
prior machine's `~/.claude`).

## 5. Pre-flight

Run the `docs/SESSION_OPENER.md` § 1 pre-flight — its § 1.5 now verifies the memory link and self-heals
it, so a healthy run confirms the re-home is complete.
