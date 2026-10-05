<!-- VERSION: 1.4 -->
<!-- Last Updated: 2026-10-05 -->
<!-- Re-home checklist: bring this vault to full operation on a new machine. Project-local (not a suite file). -->
<!--
CHANGE LOG
v1.4 — 2026-10-05 — Second push remote: the vault is also pushed to GitHub `780-AI/780-Docset` (private; org members read-only, operator-only write) alongside GitLab. § 1 checks both remotes (the `github` remote lives in `.git/config` and travels with the folder; a fresh clone re-adds it); § 3 registers the push key on GitHub too and trusts github.com only on a fingerprint match with GitHub's published keys (recorded); catalog intro names it.
v1.3 — 2026-10-04 — Rule 14 catalog gap closed: added § 3.1 ssh-target access (the § 3 key authorized on each `transport = "ssh"` target + its trusted host keys in `~/.ssh/known_hosts` — machine-local state uncataloged since the first ssh registration 2026-08-19); trusted host-key fingerprints recorded as the new-machine trust anchor; catalog intro + opening paragraph name it.
v1.2 — 2026-08-17 — PLAN-009 (Set v2.0): added § 5 delivery-skill symlink (machine-local ~/.claude/skills/standard-docset; restore via bash scripts/bootstrap_skill.sh, idempotent) + its entry in the Rule 14 catalog intro; Pre-flight renumbered § 5 → § 6.
v1.1 — 2026-08-16 — Standard Set Version v1.5 (PLAN-010): this doc now doubles as the Rule 14 machine-migration catalog (§§ 2–3 ARE the out-of-folder state entries); § 4 retargeted memory symlink → project-data link (claude_project_data.sh status/adopt/link replaces bootstrap_memory.sh); § 1 intro mentions .claude/project-data/.
v1.0 — 2026-06-17 — Initial. Derived from the 2026-06-17 re-home (L050).
-->

# New-machine setup — re-homing this vault

The repository folder is Dropbox-synced, so the **files** travel automatically (tracked + untracked,
including `.claude/project-data/` — memory + session transcripts — and `.git`). What does **not** travel
is everything machine-local: the Python toolchain, the harness project-data **symlink**, and SSH
credentials (the push key + ssh-target access). Walk this once on a new machine (and after any folder
move) to restore full operation.
Derived from the 2026-06-17 re-home (see `archive/LESSONS.md` L050).

> **This doc is also the Rule 14 machine-migration catalog** — the named register of project state that
> genuinely cannot live in the project folder. Its entries are the sections below: the Python toolchain
> (§ 2, rebuilt per machine), SSH credentials (§ 3, per-machine keys — the push key, registered on GitLab
> **and** GitHub, plus github.com's trusted host keys; § 3.1
> ssh-target access: the key authorized on each ssh target and its trusted host keys), and the
> delivery-skill symlink (§ 5, re-created by `bash scripts/bootstrap_skill.sh`). Anything new that must
> live outside the folder is added here with its migration steps, same-commit (per `CLAUDE.md` Rule 14).

## 1. Repo

Sync/clone the repo. Confirm `git status` is clean and `git rev-parse HEAD` matches **both** remotes:
`git ls-remote origin master` (GitLab) and `git ls-remote github master` (GitHub `780-AI/780-Docset`,
private — org members read-only, only the operator writes). The `github` remote lives in `.git/config`,
so it travels with the folder; a fresh clone re-adds it:
`git remote add github git@github.com:780-AI/780-Docset.git`.

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
pbcopy < ~/.ssh/id_ed25519.pub        # also add at GitHub → Settings → SSH and GPG keys (+ Configure SSO → 780-AI, if shown)
ssh-keyscan -t ed25519,ecdsa,rsa github.com 2>/dev/null | ssh-keygen -lf -   # must match the table below
ssh -T git@github.com                 # expect: Hi <user>! You've successfully authenticated…
```

Trust github.com (answer `yes` to the first host-key prompt, or append the keyscan output to
`~/.ssh/known_hosts`) only when its fingerprints match GitHub's published ones
(`https://api.github.com/meta` → `ssh_key_fingerprints`) and the table below:

| Host | Host keys trusted since | Fingerprints (SHA256) |
|---|---|---|
| github.com | 2026-10-05 (matched `api.github.com/meta`) | ED25519 `+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU` · ECDSA `p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM` · RSA `uNiVztksCsDhcc0u9e8BujQXVUpKZIDTMczCvj3tD2s` |

### 3.1 ssh-target access (each `transport = "ssh"` target in `config/projects.toml`)

The engine reaches an ssh target with plain `rsync <ssh_host>:…` (no `~/.ssh/config`), so it uses
this machine's default key (the § 3 `~/.ssh/id_ed25519`) and this machine's `~/.ssh/known_hosts`.
Neither travels with the folder. Per machine, for every ssh target:

```bash
ssh-keyscan <ip> 2>/dev/null | ssh-keygen -lf -   # 1. fingerprints offered at the address
ssh-copy-id <ssh_host>                            # 2. authorize THIS machine's key (target password once)
ssh -o BatchMode=yes <ssh_host> true && echo ok   # 3. expect: ok — key auth, no prompt
.venv/bin/python -m standard_document_updater status   # 4. its row is not "unknown" (= reachable)
```

Answer `yes` to a host-key prompt — first contact on a machine, or a new DHCP address — only after
step 1's fingerprints match the trusted ones below. A mismatch means a different machine at that
address: stop and ask the operator. Run step 2 from the curator account (the one that runs the
engine), not the target's.

| Target | Host keys trusted since | Fingerprints (SHA256) |
|---|---|---|
| 780-Automation | 2026-08-19 (ED25519 matched at .10.61, .11.60 and .10.245; RSA + ECDSA at .10.61 and .10.245) | ED25519 `FUsmmMsjipLZuka+DDPE6sGHK+rv09f1FUQmT7H0FvA` · ECDSA `8bRJ2WOCGCusS2BjjPXgKxVSfvtFODNvl+2pU75pOjg` · RSA `oKO2gmPjltVWMEvO7lh9F2mtbipYm7MdeMFwa0bU+L0` |

Registering a new ssh target adds its row here, same-commit (Rule 14).

## 4. Project-data link (per `CLAUDE.md` Rule 14)

```bash
bash scripts/claude_project_data.sh link     # re-points ~/.claude/projects/<key> → ./.claude/project-data
bash scripts/claude_project_data.sh status   # expect: STATUS: OK
```

The **content** (memory + session transcripts) is already present (Dropbox carried
`./.claude/project-data/`); only the machine-local symlink needs re-creating — `link` also merges in any
stray harness dir a pre-link session created. If the store is unexpectedly empty, recover per L050 (a
backup/sync of the prior machine's `~/.claude`).

## 5. Delivery-skill symlink (per `CLAUDE.md` Rule 14)

The standard-docset delivery skill is machine-local state: `~/.claude/skills/standard-docset` is a
symlink into this vault's `skill/` dir. Restore it with:

```bash
bash scripts/bootstrap_skill.sh     # idempotent; re-points a stale link, errors on a non-link
```

New Claude Code sessions on the machine then list the `standard-docset` skill (delivery per
`docs/standards/STANDARDS_INDEX.md` § 4).

## 6. Pre-flight

Run the `docs/SESSION_OPENER.md` § 1 pre-flight — its § 1.5 runs `claude_project_data.sh status` and
names the fix verb on any non-OK state, so a healthy run confirms the re-home is complete.
