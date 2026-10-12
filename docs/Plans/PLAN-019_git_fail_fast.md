<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Status: CLOSED — 2026-10-12 -->
<!--
CHANGE LOG
v1.0 — 2026-10-12 — CLOSED. Phase 3 + 4 in a fresh session, one commit: reconcile 16 / 16 blocks clean, zero
plan defects (checker control: one corrupted FIND → exactly that block fails); § 5 applied with
<P3-DATE> = 2026-10-12 (clock vs gitlab.com / apple.com, Δ ≤ 3 s); QA-T1…T5 ✅ (evidence in the
tracker). R4 annotated: on a slow link (24 KB/s) a normal read took up to 176 s — under the cap, kept
at 300 s (approved D-2); the first harness run's T2 HANG at its 60 s watchdog was that link (old code
equally slow), the re-run on a recovered link 4 / 4 PASS. Phase 5 (push) stays pending.
v0.2 — 2026-10-12 — Phase 2 operator approval recorded ("D1. A , D2. A" + "go"); § 9.1 decision record added: D19.A
approved; D-1 = A, D-2 = A. No § 5 change — the 16 blocks + harness re-extracted from this file stay
byte-identical to the proven files.
v0.1 — 2026-10-12 — Initial draft. § 15.9 feature intake (operator request in chat: "what is the ssh
timeout plan?" → "yes get it done as quickly as possible"; no document) → Phase 0 audit against the live
source (`bf8669e`) + pre-tests with numbers (§ 3) → Phase 1 design. Code proven FIRST in a scratch export
of HEAD (ruff clean, mypy --strict 0, pytest 172 = 163 + 9 new; positive control: 8 of the 9 new tests
fail on transport 0.3, the 9th is the rsync-unchanged guard); § 5 GENERATED from it (16 blocks) and
parsed back byte-identical; the § 8 QA harness run on the draft (4 / 4 PASS) and on HEAD (1 PASS / 3 HANG
= the control). Rule 13 pass on the complete plan + tracker (record at the foot).
-->

# PLAN-019 — Git transport fails fast: ssh timeouts + keepalives, and a cap on every transport command

## 1. Goal

A git-transport target that does not answer can never hang the engine again. Today every **git** command
the engine runs (`clone` / `sparse-checkout` / `checkout` / `add` / `commit` / `push`) has no time limit
at all — measured (§ 3): a silent server or a transfer that stalls mid-way hangs `status` / `fleet` /
`sync` with no end, and the session opener runs `status` on every session. After this plan:

1. **Every git command runs ssh fail-fast** — `-o ConnectTimeout=10 -o BatchMode=yes -o
   ServerAliveInterval=10 -o ServerAliveCountMax=3`, appended to the operator's own ssh command when one
   is set (D-1). Unreachable or silent host → error in ~10 s; a transfer that goes silent → dropped after
   ~30–40 s; never waits on a prompt.
2. **Every transport command (git and rsync) is capped at 300 s** (D-2) — the backstop for a
   slow-but-alive transfer the ssh options cannot see. A timeout is a `TransportError` like any other:
   non-fatal for reads (`status` shows the target `unknown`), fatal for that run on the write path.

Engine-only: no `docs/standards/` change → no Set Version bump, no tag, no target write.

## 2. Operator constraints + intake record (binding)

- **Intake (§ 15.9):** feature arrived as an operator request in chat, no document (step 1 copy skipped,
  never the discipline). Origin: the 2026-10-05 finding queued in `OPEN_TASKS.md` (PLAN-017 carry-over
  block) — "the git transport sets NO ssh timeout … Critical File → plan (small) or fold into PLAN-014."
  **Decided here: a standalone plan** — PLAN-014 (PR delivery) is not drafted and blocked on `gh`; this
  fix has no dependency on it and protects every session open now.
- **Operator directive:** "get it done as quickly as possible" → one Phase 3 commit that also CLOSES the
  plan (every QA scenario runs locally in the implementing session; nothing needs a push or another
  machine first).
- **Adopt / deviate vs the queued fix candidate** (`GIT_SSH_COMMAND="ssh -o ConnectTimeout=10 -o
  BatchMode=yes -o ServerAliveInterval=10 -o ServerAliveCountMax=3"` in the git `_run` env):
  - Adopt the four ssh options exactly (the PLAN-016 D-4 pattern + keepalives) — pre-tested § 3.
  - **Deviate — keep the operator's own ssh command as the base (D-1):** a blind `GIT_SSH_COMMAND=ssh …`
    would override an operator's `GIT_SSH_COMMAND` or `core.sshCommand` — the exact setting the Windows
    finding W2 (PLAN-018 QA-S6) needs to reach a key in the Windows ssh-agent. Appending keeps it; ssh
    keeps the FIRST value of each option (verified: `ssh -G -o ConnectTimeout=3 -o ConnectTimeout=10`
    → `connecttimeout 3`), so an option the operator already set wins.
  - **Add — a 300 s cap on every transport command (D-2):** the queued candidate does not cover a
    slow-but-alive transfer; the intake question raised to the operator in chat (2026-10-12).
  - **Not done:** rsync gets no keepalives (out of scope; the cap covers a stalled rsync); no
    process-group kill (§ 11 R2).

## 3. Scope summary

### Phase 0 audit findings (2026-10-12, live source at `bf8669e`)

- `src/standard_document_updater/transport.py:44` — `_RSYNC` carries `ssh -o ConnectTimeout=10 -o
  BatchMode=yes` (PLAN-016 D-4, transport 0.3). `:51-59` — `_run(cmd)` calls `subprocess.run(cmd,
  capture_output=True, text=True, check=False)`: **no timeout, no env**. `:111-131` — `GitTarget`
  runs six git commands through `_run`, none with ssh options; the read path's `checkout` of a
  `--filter=blob:none` clone fetches blobs over ssh too, so it needs the same env as `clone`.
- Callers: `cli.py:80` (`status` / `fleet` probes → `unreachable_status`), `cli.py:142` (`harvest` →
  warn + skip), `cli.py:277` (`sync` / `integrate` write paths → per-target isolation). All catch
  `TransportError` — a timeout raised AS `TransportError` needs no caller change.
- Tests that replace `transport._run` with a one-argument fake: `tests/test_transport.py:34-40`
  (`_capture`) and `tests/test_cli.py:180`, `:201`, `:366`, `:399` — each must accept the new optional
  `env` argument (the first full-tree run without it: 3 FAILED in `test_cli.py`, TypeError).
- Environment: OpenSSH 10.2p1, git 2.50.1, Python 3.11.15 (`.venv`); `core.sshCommand` unset, no
  `GIT_SSH*` env on this Mac. git's ssh precedence (git `connect.c`): `GIT_SSH_COMMAND` > `core.sshCommand`
  > `GIT_SSH` > `ssh`.
- Overlap: PLAN-014 (PR delivery, not drafted) — independent, nothing absorbed; PLAN-016 D-4 — this plan
  extends the same fail-fast pattern to git; `docs/architecture.md:255-258` documents D-4 → extended
  same-commit (§ 4 drift rule).

### Pre-tests (2026-10-12; `git clone --depth 1 --filter=blob:none` of 780-estimator; scratch harness)

| Case | No options (today) | With the options |
|---|---|---|
| Normal clone from GitHub | — | exit 0 in 3.0 s (options harmless) |
| Silent server (accepts, never speaks) | still hanging at the 45 s cap | fails in 10.0 s |
| Blackhole address `10.255.255.1` | still hanging at the 40 s cap | fails in 10.0 s |
| Relay to GitHub that freezes 1.5 s in | still hanging at the 75 s cap | dropped at 41.2 s |

- A `subprocess.run(timeout=)` cap **returned on time** in every hanging case (POSIX `run()` kills the
  child and does not wait on the pipes) — but the killed git's **ssh child lived on** (one orphan seen,
  blocked in TCP connect). With the options in place an orphan ends on its own within ~10–40 s → § 11 R2.
- The engine's own `GitTarget` from the proven scratch copy: real GitHub read OK (7.5 s, SVA present);
  silent server `TransportError` in 10.1 s; mid-transfer stall `TransportError` in 41.6 s **with the
  operator's base command kept** (`ssh -o HostKeyAlias=github.com` — without it the host-key check
  behind the relay fails at once, so 41.6 s proves the base survived).
- The § 8 QA harness (the final text, extracted from this plan): draft code 4 / 4 PASS; HEAD code
  1 PASS (T2 — the normal path) / 3 FAIL as HANG — the harness sees the defect.

### Files (Phase 3 — one commit, § 7)

`transport.py` 0.3 → 0.4 · `tests/test_transport.py` 0.3 → 0.4 · `tests/test_cli.py` 0.8 → 0.9 ·
`docs/architecture.md` 0.14 → 0.15 · `CHANGELOG.md` · `docs/documents_manifest.md` · this plan + its
tracker → 1.0 CLOSED.

## 4. Phase tracker (high-level — granular sub-tasks in `PLAN-019_tracker.md`)

| Phase | Status | Date |
|---|---|---|
| 0 — Audit (+ § 15.9 intake, pre-tests) | ✅ | 2026-10-12 |
| 1 — Design (+ Rule 13 pass) | ✅ | 2026-10-12 |
| 2 — Operator approval | ✅ "D1. A , D2. A" + "go" | 2026-10-12 |
| 3 — Implement (fresh session, one commit) | ✅ | 2026-10-12 |
| 4 — Validate (QA-T1…T5, same session as Phase 3) | ✅ | 2026-10-12 |
| 5 — Operator gate (push both remotes; no tag) | ⏸ pending | — |

## 5. Verbatim transformation rules (code proven in scratch; Phase 3 copies byte-for-byte)

**How to apply (Phase 3).** Each block carries a machine-readable marker (`<!-- block … -->`); every
block is `kind=replace`. Each FIND / REPLACE body is exactly the lines between its two 4-backtick fence
lines, plus a final newline. The reconcile pass (§ 15.3) re-extracts every block from THIS file before
the first edit and checks it against the live tree: each FIND matches exactly once — in order per file,
a later FIND against the text after the earlier REPLACEs. Any mismatch is a named plan defect (D1, D2, …)
— stop and surface it. Replace every `<P3-DATE>` with the Phase 3 date checked against an external time
authority (L079). Then the § 6 mechanical rules.

<!-- §5-GENERATED:BEGIN -->

### 5a — `src/standard_document_updater/transport.py` — 0.3 → 0.4: git fail-fast ssh + run cap

<!-- block id=5a.1 path=src/standard_document_updater/transport.py kind=replace -->

**5a.1** — header 0.3 → 0.4. FIND:

````text
# VERSION: 0.3
# Pluggable target transports (local | git | ssh): materialize -> operate -> flush.
#
# CHANGE LOG
````

REPLACE WITH:

````text
# VERSION: 0.4
# Pluggable target transports (local | git | ssh): materialize -> operate -> flush.
#
# CHANGE LOG
# v0.4 — <P3-DATE> — PLAN-019: git fails fast too — every git command runs ssh with
#         ConnectTimeout=10 + BatchMode=yes + ServerAliveInterval=10 x ServerAliveCountMax=3
#         (a stalled transfer drops in ~30–40 s), appended to the operator's own ssh command
#         (GIT_SSH_COMMAND / core.sshCommand) when one is set (D-1); every transport command is
#         capped at 300 s (D-2).
````

<!-- block id=5a.2 path=src/standard_document_updater/transport.py kind=replace -->

**5a.2** — import os. FIND:

````text
import shutil
import subprocess
````

REPLACE WITH:

````text
import os
import shutil
import subprocess
````

<!-- block id=5a.3 path=src/standard_document_updater/transport.py kind=replace -->

**5a.3** — constants `_GIT_SSH_OPTS` + `_RUN_TIMEOUT`. FIND:

````text
_RSYNC = ("rsync", "-az", "-e", "ssh -o ConnectTimeout=10 -o BatchMode=yes")
````

REPLACE WITH:

````text
_RSYNC = ("rsync", "-az", "-e", "ssh -o ConnectTimeout=10 -o BatchMode=yes")
# git fails fast too (PLAN-019 D-1): the same two options plus keepalives — a connection that goes
# silent mid-transfer is dropped after ~30–40 s (three missed 10 s probes).
_GIT_SSH_OPTS = (
    "-o ConnectTimeout=10 -o BatchMode=yes -o ServerAliveInterval=10 -o ServerAliveCountMax=3"
)
# Last-resort cap on any one transport command (PLAN-019 D-2): catches a slow-but-alive transfer
# the ssh options cannot see.
_RUN_TIMEOUT = 300
````

<!-- block id=5a.4 path=src/standard_document_updater/transport.py kind=replace -->

**5a.4** — `_run` gains `env` + the 300 s cap. FIND:

````text
def _run(cmd: list[str]) -> None:
    """Run a subprocess; raise TransportError with captured output on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except OSError as exc:  # the binary is missing / not executable
````

REPLACE WITH:

````text
def _run(cmd: list[str], env: dict[str, str] | None = None) -> None:
    """Run a subprocess (capped at _RUN_TIMEOUT s); raise TransportError on failure."""
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, check=False, env=env, timeout=_RUN_TIMEOUT
        )
    except subprocess.TimeoutExpired as exc:
        raise TransportError(f"{' '.join(cmd)} timed out after {_RUN_TIMEOUT} s") from exc
    except OSError as exc:  # the binary is missing / not executable
````

<!-- block id=5a.5 path=src/standard_document_updater/transport.py kind=replace -->

**5a.5** — new `_configured_ssh_command` + `_git_env` after `_run`. FIND:

````text
        raise TransportError(f"{' '.join(cmd)} failed (exit {proc.returncode}): {detail}")
````

REPLACE WITH:

````text
        raise TransportError(f"{' '.join(cmd)} failed (exit {proc.returncode}): {detail}")


def _configured_ssh_command() -> str | None:
    """The operator's `core.sshCommand` git setting, or None when unset."""
    try:
        proc = subprocess.run(
            ["git", "config", "--get", "core.sshCommand"],
            capture_output=True, text=True, check=False, timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    value = proc.stdout.strip()
    return value if proc.returncode == 0 and value else None


def _git_env() -> dict[str, str] | None:
    """The environment for every git command: the operator's ssh command + _GIT_SSH_OPTS.

    git picks its ssh as GIT_SSH_COMMAND, else core.sshCommand, else GIT_SSH, else `ssh`. The
    options are appended to the first two — ssh keeps the first value it sees, so an option the
    operator already set wins. Legacy GIT_SSH names a program that may not take options, so it is
    left alone (None = inherit the environment); the _RUN_TIMEOUT cap still applies.
    """
    env = dict(os.environ)
    base = env.get("GIT_SSH_COMMAND") or _configured_ssh_command()
    if base is None and env.get("GIT_SSH"):
        return None
    env["GIT_SSH_COMMAND"] = f"{base or 'ssh'} {_GIT_SSH_OPTS}"
    return env
````

<!-- block id=5a.6 path=src/standard_document_updater/transport.py kind=replace -->

**5a.6** — `GitTarget` passes the env to every git command. FIND:

````text
        branch = self.project.git_branch
        dest = Path(tempfile.mkdtemp(prefix="stddocset-git-"))
        base = ["git", "clone", "--depth", "1"]
        if branch:
            base += ["--branch", branch]
        if writable:  # full branch tip so a commit can be pushed
            _run([*base, url, str(dest)])
        else:  # read path: shallow + blobless + sparse (D4); cone mode keeps root files
            _run([*base, "--filter=blob:none", "--no-checkout", url, str(dest)])
            sparse = [_DOCS, _ARCHIVE] if full else [_DOCS]
            _run(["git", "-C", str(dest), "sparse-checkout", "set", *sparse])
            _run(["git", "-C", str(dest), "checkout"])
        return dest

    def flush(self, root: Path, changed: list[Path], message: str) -> None:
        rels = [p.as_posix() for p in changed]
        _run(["git", "-C", str(root), "add", *rels])
        _run([
            "git", "-C", str(root),
            "-c", f"user.name={_COMMIT_NAME}", "-c", f"user.email={_COMMIT_EMAIL}",
            "commit", "-m", message,
        ])
        branch = self.project.git_branch
        refspec = f"HEAD:{branch}" if branch else "HEAD"
        _run(["git", "-C", str(root), "push", "origin", refspec])
````

REPLACE WITH:

````text
        branch = self.project.git_branch
        dest = Path(tempfile.mkdtemp(prefix="stddocset-git-"))
        env = _git_env()  # every command: the blobless checkout fetches over ssh too
        base = ["git", "clone", "--depth", "1"]
        if branch:
            base += ["--branch", branch]
        if writable:  # full branch tip so a commit can be pushed
            _run([*base, url, str(dest)], env)
        else:  # read path: shallow + blobless + sparse (D4); cone mode keeps root files
            _run([*base, "--filter=blob:none", "--no-checkout", url, str(dest)], env)
            sparse = [_DOCS, _ARCHIVE] if full else [_DOCS]
            _run(["git", "-C", str(dest), "sparse-checkout", "set", *sparse], env)
            _run(["git", "-C", str(dest), "checkout"], env)
        return dest

    def flush(self, root: Path, changed: list[Path], message: str) -> None:
        rels = [p.as_posix() for p in changed]
        env = _git_env()
        _run(["git", "-C", str(root), "add", *rels], env)
        _run([
            "git", "-C", str(root),
            "-c", f"user.name={_COMMIT_NAME}", "-c", f"user.email={_COMMIT_EMAIL}",
            "commit", "-m", message,
        ], env)
        branch = self.project.git_branch
        refspec = f"HEAD:{branch}" if branch else "HEAD"
        _run(["git", "-C", str(root), "push", "origin", refspec], env)
````

### 5b — `tests/test_transport.py` — 0.3 → 0.4: env capture + nine new tests

<!-- block id=5b.1 path=tests/test_transport.py kind=replace -->

**5b.1** — header 0.3 → 0.4. FIND:

````text
# VERSION: 0.3
# Unit tests for the pluggable target transports (local | git | ssh).
#
# CHANGE LOG
````

REPLACE WITH:

````text
# VERSION: 0.4
# Unit tests for the pluggable target transports (local | git | ssh).
#
# CHANGE LOG
# v0.4 — <P3-DATE> — PLAN-019: _capture also records the env each command ran with; new tests —
#         git fail-fast ssh (every git command; the operator's GIT_SSH_COMMAND / core.sshCommand
#         kept as the base; legacy GIT_SSH left alone), rsync unchanged, the 300 s run cap.
````

<!-- block id=5b.2 path=tests/test_transport.py kind=replace -->

**5b.2** — `_capture` records the env. FIND:

````text
def _capture(cmds: list[list[str]]) -> Callable[[list[str]], None]:
    """A drop-in for transport._run that records the argv it was called with."""

    def _fake(cmd: list[str]) -> None:
        cmds.append(cmd)

    return _fake
````

REPLACE WITH:

````text
def _capture(
    cmds: list[list[str]], envs: list[dict[str, str] | None] | None = None
) -> Callable[..., None]:
    """A drop-in for transport._run that records the argv (and env) it was called with."""

    def _fake(cmd: list[str], env: dict[str, str] | None = None) -> None:
        cmds.append(cmd)
        if envs is not None:
            envs.append(env)

    return _fake
````

<!-- block id=5b.3 path=tests/test_transport.py kind=replace -->

**5b.3** — nine new tests appended at the end of the file. FIND:

````text
    with pytest.raises(transport.TransportError, match="could not run"):
        transport._run(["nonexistent-binary-xyz"])
````

REPLACE WITH:

````text
    with pytest.raises(transport.TransportError, match="could not run"):
        transport._run(["nonexistent-binary-xyz"])


# --- git fail-fast ssh + run cap (PLAN-019) ----------------------------------------

_FAIL_FAST = (
    "-o ConnectTimeout=10 -o BatchMode=yes -o ServerAliveInterval=10 -o ServerAliveCountMax=3"
)


def _git_session_envs(
    monkeypatch: pytest.MonkeyPatch, configured: str | None
) -> list[dict[str, str] | None]:
    """Run a git read session + a flush; return the env of every git command (6 commands)."""
    cmds: list[list[str]] = []
    envs: list[dict[str, str] | None] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds, envs))
    monkeypatch.setattr(transport, "_configured_ssh_command", lambda: configured)
    t = transport.make_target(Project(name="b", transport="git", git_url="u", git_branch="main"))
    with t.session():
        pass
    t.flush(Path("/root"), [Path("docs/x.md")], "msg")
    assert len(envs) == 6  # clone, sparse-checkout, checkout, add, commit, push
    return envs


def test_git_commands_run_fail_fast_ssh(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GIT_SSH_COMMAND", raising=False)
    monkeypatch.delenv("GIT_SSH", raising=False)
    for env in _git_session_envs(monkeypatch, None):
        assert env is not None
        assert env["GIT_SSH_COMMAND"] == f"ssh {_FAIL_FAST}"


def test_git_ssh_keeps_operator_env_command(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GIT_SSH_COMMAND", "/opt/ssh -i key")
    for env in _git_session_envs(monkeypatch, "ignored-config"):  # env beats config, as in git
        assert env is not None
        assert env["GIT_SSH_COMMAND"] == f"/opt/ssh -i key {_FAIL_FAST}"


def test_git_ssh_keeps_operator_core_sshcommand(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GIT_SSH_COMMAND", raising=False)
    monkeypatch.setenv("GIT_SSH", "/opt/legacy")  # core.sshCommand beats GIT_SSH, as in git
    for env in _git_session_envs(monkeypatch, "C:/Windows/System32/OpenSSH/ssh.exe"):
        assert env is not None
        assert env["GIT_SSH_COMMAND"] == f"C:/Windows/System32/OpenSSH/ssh.exe {_FAIL_FAST}"


def test_git_legacy_git_ssh_left_alone(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GIT_SSH_COMMAND", raising=False)
    monkeypatch.setenv("GIT_SSH", "/opt/legacy")
    assert _git_session_envs(monkeypatch, None) == [None] * 6  # inherit; the run cap still applies


def test_configured_ssh_command_reads_git_config(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: list[list[str]] = []

    def fake(cmd: list[str], **kwargs: object) -> _FakeProc:
        seen.append(cmd)
        return _FakeProc(0, stdout="/opt/ssh -F cfg\n")

    monkeypatch.setattr(subprocess, "run", fake)
    assert transport._configured_ssh_command() == "/opt/ssh -F cfg"
    assert seen == [["git", "config", "--get", "core.sshCommand"]]


def test_configured_ssh_command_unset_is_none(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake(*args: object, **kwargs: object) -> _FakeProc:
        return _FakeProc(1)  # git config --get: exit 1 when the key is unset

    monkeypatch.setattr(subprocess, "run", fake)
    assert transport._configured_ssh_command() is None


def test_rsync_commands_keep_inherited_env(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    envs: list[dict[str, str] | None] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds, envs))
    t = transport.make_target(Project(name="c", transport="ssh", ssh_host="h", ssh_path="/p"))
    with t.session():
        pass
    assert envs == [None]  # rsync carries its own `-e ssh ...`; no git env


def test_run_passes_cap_and_env(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: dict[str, object] = {}

    def fake(cmd: list[str], **kwargs: object) -> _FakeProc:
        seen.update(kwargs)
        return _FakeProc(0)

    monkeypatch.setattr(subprocess, "run", fake)
    transport._run(["true"], {"K": "V"})
    assert seen["timeout"] == 300 and seen["env"] == {"K": "V"}


def test_run_raises_on_timeout(monkeypatch: pytest.MonkeyPatch) -> None:
    def slow(cmd: list[str], **kwargs: object) -> _FakeProc:
        raise subprocess.TimeoutExpired(cmd, 300)

    monkeypatch.setattr(subprocess, "run", slow)
    with pytest.raises(transport.TransportError, match="timed out after 300 s"):
        transport._run(["git", "clone", "u", "d"])
````

### 5c — `tests/test_cli.py` — 0.8 → 0.9: the `_run` fakes accept `env`

<!-- block id=5c.1 path=tests/test_cli.py kind=replace -->

**5c.1** — header 0.8 → 0.9. FIND:

````text
# VERSION: 0.8
# End-to-end tests for the CLI (status / drift / fleet / harvest / integrate / sync).
#
# CHANGE LOG
````

REPLACE WITH:

````text
# VERSION: 0.9
# End-to-end tests for the CLI (status / drift / fleet / harvest / integrate / sync).
#
# CHANGE LOG
# v0.9 — <P3-DATE> — PLAN-019: the transport._run fakes accept the new optional `env` argument
#         (git commands now run with the fail-fast ssh environment).
````

<!-- block id=5c.2 path=tests/test_cli.py kind=replace -->

**5c.2** — `fake_run` accepts `env`. FIND:

````text
    def fake_run(cmd: list[str]) -> None:
````

REPLACE WITH:

````text
    def fake_run(cmd: list[str], env: dict[str, str] | None = None) -> None:
````

<!-- block id=5c.3 path=tests/test_cli.py kind=replace -->

**5c.3** — `boom` (status test) accepts `env`. FIND:

````text
    def boom(cmd: list[str]) -> None:
        raise transport.TransportError("host unreachable")

    monkeypatch.setattr(transport, "_run", boom)
    assert main(["--vault", str(root), "status"]) == 0  # non-fatal for a read command
````

REPLACE WITH:

````text
    def boom(cmd: list[str], env: dict[str, str] | None = None) -> None:
        raise transport.TransportError("host unreachable")

    monkeypatch.setattr(transport, "_run", boom)
    assert main(["--vault", str(root), "status"]) == 0  # non-fatal for a read command
````

<!-- block id=5c.4 path=tests/test_cli.py kind=replace -->

**5c.4** — `_git_clone_with_sva` accepts `env`. FIND:

````text
def _git_clone_with_sva(cmd: list[str]) -> None:
````

REPLACE WITH:

````text
def _git_clone_with_sva(cmd: list[str], env: dict[str, str] | None = None) -> None:
````

<!-- block id=5c.5 path=tests/test_cli.py kind=replace -->

**5c.5** — `boom` (fleet test) accepts `env`. FIND:

````text
    def boom(cmd: list[str]) -> None:
        raise transport.TransportError("host unreachable")

    monkeypatch.setattr(transport, "_run", boom)
    assert main(["--vault", str(root), "fleet"]) == 0
````

REPLACE WITH:

````text
    def boom(cmd: list[str], env: dict[str, str] | None = None) -> None:
        raise transport.TransportError("host unreachable")

    monkeypatch.setattr(transport, "_run", boom)
    assert main(["--vault", str(root), "fleet"]) == 0
````

### 5d — `docs/architecture.md` — 0.14 → 0.15: § 8 transport paragraph

<!-- block id=5d.1 path=docs/architecture.md kind=replace -->

**5d.1** — header 0.14 → 0.15 + CHANGE LOG line. FIND:

````text
<!-- VERSION: 0.14 -->
<!-- Last Updated: 2026-10-05 -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 0.15 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.15 — <P3-DATE> — PLAN-019 (git fail-fast) landed. § 8 transport paragraph: every git command runs ssh with ConnectTimeout / BatchMode / ServerAlive options appended to the operator's own ssh command (D-1); every transport command is capped at 300 s (D-2). Engine-only — no Set Version change.
````

<!-- block id=5d.2 path=docs/architecture.md kind=replace -->

**5d.2** — § 8 transport paragraph — the git fail-fast + run-cap sentences. FIND:

````text
host key per `docs/NEW_MACHINE_SETUP.md` § 3.1 first).
````

REPLACE WITH:

````text
host key per `docs/NEW_MACHINE_SETUP.md` § 3.1 first). Every **git** command fails fast too
(PLAN-019, D-1): it runs with `GIT_SSH_COMMAND` = the operator's own ssh command (`GIT_SSH_COMMAND`,
else `core.sshCommand`, else `ssh`) + `-o ConnectTimeout=10 -o BatchMode=yes -o
ServerAliveInterval=10 -o ServerAliveCountMax=3` — an unreachable or silent host fails in ~10 s and a
transfer that stalls mid-way is dropped after ~30–40 s of silence; an option the operator's command
already sets wins (ssh keeps the first value it sees); a legacy `GIT_SSH` program is left untouched.
Every transport command (git and rsync) is also capped at 300 s (D-2) — a timeout is a
`TransportError` like any other: non-fatal for reads, fatal for that run on the write path.
````

<!-- §5-GENERATED:END -->

## 6. Spec update map (mechanical rules; same commit as Phase 3)

1. **`docs/documents_manifest.md`:** cells 7 (architecture 0.14 → 0.15), 51 (test_cli 0.8 → 0.9), 65
   (transport 0.3 → 0.4), 66 (test_transport 0.3 → 0.4); rows 96 (this plan) + 97 (tracker) → `1.0`,
   titles `(DRAFT)` → `(CLOSED)`; self-row 5 + header → next version; new top CHANGE LOG line; the
   `## Last updated` block rotated. Every touched cell checked against its file's header (L063) — by a
   script that FAILS on an empty value (session-8 zsh `path` lesson), not a shell loop.
2. **`CHANGELOG.md`:** a new top entry `## [<P3-DATE>] — PLAN-019: the git transport fails fast (ssh
   timeouts + keepalives, a 300 s cap on every transport command)` — Type, What changed, Pre-tests,
   Versions, Impact ("yes: an unreachable / silent / stalled git target now fails in ~10–40 s instead of
   hanging; reads show it `unknown`; nothing else changes"), and a `### QA scenarios` sub-section listing
   QA-T1…T5 with their results (Rule 11).
3. **This plan:** header → 1.0, Status `CLOSED — <P3-DATE>`, CHANGE LOG line; § 4 Phases 2–4 ✅ (Phase 5
   stays ⏸ until the push). **Tracker:** → 1.0 with the evidence.
4. **`docs/Plans/OPEN_TASKS.md`** (gitignored — not in the commit): delete the "Engine finding … git
   transport sets NO ssh timeout" bullet; the queue line starts at v2.8.

## 7. ALLOWLIST (the bullet enumeration IS the count — L038; plan + tracker included per L054)

Phase 3 commit — **8 files**:

- `src/standard_document_updater/transport.py`
- `tests/test_transport.py`
- `tests/test_cli.py`
- `docs/architecture.md`
- `CHANGELOG.md`
- `docs/documents_manifest.md`
- `docs/Plans/PLAN-019_git_fail_fast.md`
- `docs/Plans/PLAN-019_tracker.md`

Anything else in `git status --short` → STOP and report (Rule 6). `docs/fleet.csv` is gitignored (QA-T2
regenerates it) and never appears.

## 8. Validation gate (Rule 11 scenarios; Rule 15 feature-ON marked ⚑; status in the tracker)

All five run in the Phase 3 session, before the commit. Python = the vault's `.venv/bin/python`.

- **QA-T1 — unit tests + type / lint.** `ruff check src tests` → "All checks passed!";
  `MYPYPATH=src mypy --cache-dir <fresh dir> src tests` → "no issues found in 25 source files"; `pytest`
  → **172 passed** (163 + 9). Positive control: in a scratch copy of the tree with `transport.py`
  swapped for `git show bf8669e:src/standard_document_updater/transport.py`, `pytest
  tests/test_transport.py` → **8 failed, 20 passed** — the 8 new-behavior tests (the rsync guard passes
  on both).
- **QA-T2 ⚑ — the real fleet still reads.** `python -m standard_document_updater status` → 780-estimator
  `v2.7 v2.7 current` (the git target through the new env); the other rows as at session open.
- **QA-T3 ⚑ — a silent git server fails fast** (harness below, T3a + T3b): `GitTarget` → `TransportError`
  in < 15 s; `status` through the CLI on a scratch vault whose only target points at the silent server →
  exit 0, the row reads `unknown`, < 20 s.
- **QA-T4 ⚑ — a transfer that stalls mid-way is dropped** (harness T4): `TransportError` in 15–60 s with
  the operator's base command (`ssh -o HostKeyAlias=github.com`) kept.
- **QA-T5 — governance.** `python scripts/check_doc_coverage.py` and `python
  scripts/check_test_coverage_drift.py --ci` → exit 0, stdout pasted verbatim (Rule 6).

**Harness (QA-T2's GitHub read + T3 + T4)** — write the block to the session scratchpad as
`qa_harness.py`; run `.venv/bin/python -I -u qa_harness.py <vault>/src <vault>` → expect `SUMMARY pass=4
fail=0`. Control (proves it sees the defect): run it once against an export of `bf8669e`'s `src/` →
`SUMMARY pass=1 fail=3` (T3a / T3b / T4 = HANG). Needs network to github.com:22; ~2 min new, ~2.5 min
control. Afterwards `pgrep -fl "ssh .*127.0.0.1"` → nothing left running.

<!-- block id=8a path=qa_harness.py kind=harness -->
````python
"""PLAN-019 QA harness (QA-T2…T4). Usage: python -I qa_harness.py <engine-src-dir> <vault-root>

Runs the engine's own GitTarget / CLI against real GitHub, a silent server (accepts, never speaks)
and a relay that freezes mid-transfer. Every probe runs under a watchdog, so the OLD code shows up
as HANG = FAIL (positive control) instead of hanging the harness. Prints one PASS/FAIL line each.
"""
from __future__ import annotations

import contextlib
import os
import socket
import subprocess
import sys
import tempfile
import threading
import time
from collections.abc import Callable
from pathlib import Path

sys.path.insert(0, sys.argv[1])
from standard_document_updater import transport  # noqa: E402
from standard_document_updater.registry import Project  # noqa: E402

REPO = "780-AI/780-estimator.git"
RESULTS: list[bool] = []


def _listener() -> socket.socket:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    s.listen(5)
    return s


def silent_server() -> int:
    s, held = _listener(), []

    def loop() -> None:
        while True:
            held.append(s.accept()[0])  # accept, never speak

    threading.Thread(target=loop, daemon=True).start()
    return int(s.getsockname()[1])


def stall_proxy(after: float) -> int:
    """Relay to github.com:22; `after` s into a connection, relay nothing more (never close)."""
    s = _listener()

    def pump(a: socket.socket, b: socket.socket, start: float) -> None:
        with contextlib.suppress(OSError):
            while data := a.recv(65536):
                while time.monotonic() - start > after:
                    time.sleep(3600)
                b.sendall(data)

    def loop() -> None:
        while True:
            c = s.accept()[0]
            u = socket.create_connection(("github.com", 22))
            t0 = time.monotonic()
            threading.Thread(target=pump, args=(c, u, t0), daemon=True).start()
            threading.Thread(target=pump, args=(u, c, t0), daemon=True).start()

    threading.Thread(target=loop, daemon=True).start()
    return int(s.getsockname()[1])


def watchdog(fn: Callable[[], str], limit: float) -> tuple[str, float]:
    box: list[str] = []
    t0 = time.monotonic()
    th = threading.Thread(target=lambda: box.append(fn()), daemon=True)
    th.start()
    th.join(limit)
    return (box[0] if box else "HANG"), time.monotonic() - t0


def git_read(url: str) -> Callable[[], str]:
    def run() -> str:
        project = Project(name="x", transport="git", git_url=url, git_branch="main")
        t = transport.make_target(project)
        try:
            with t.session() as root:
                return "ok" if (root / "docs" / "SET_VERSION_ADOPTED.md").is_file() else "no-sva"
        except transport.TransportError:
            return "transport-error"

    return run


def check(name: str, ok: bool, detail: str) -> None:
    RESULTS.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}")


def main() -> None:
    vault = Path(sys.argv[2])
    print("engine:", transport.__file__)
    os.environ.pop("GIT_SSH_COMMAND", None)

    # QA-T2 — the normal path still works (real GitHub, 780-estimator read session)
    got, dt = watchdog(git_read(f"git@github.com:{REPO}"), 60)
    check("T2 real GitHub read", got == "ok", f"{got} in {dt:.1f}s")

    # QA-T3a — a silent server fails in ~10 s
    port = silent_server()
    got, dt = watchdog(git_read(f"ssh://git@127.0.0.1:{port}/{REPO}"), 30)
    check("T3a silent server", got == "transport-error" and dt < 15, f"{got} in {dt:.1f}s")

    # QA-T3b — `status` through the CLI: the target shows unknown, exit 0, fast
    scratch = Path(tempfile.mkdtemp(prefix="pl19-vault-"))
    arch = subprocess.run(["git", "-C", str(vault), "archive", "HEAD"], capture_output=True,
                          check=True).stdout
    subprocess.run(["tar", "-x", "-C", str(scratch)], input=arch, check=True)
    (scratch / "config" / "projects.toml").write_text(
        f'[[project]]\nname = "silent"\ntransport = "git"\n'
        f'git_url = "ssh://git@127.0.0.1:{port}/{REPO}"\ngit_branch = "main"\n',
        encoding="utf-8",
    )
    code = (f"import sys; sys.path.insert(0, {sys.argv[1]!r}); "
            "from standard_document_updater.cli import main; "
            f"sys.exit(main(['--vault', {str(scratch)!r}, 'status']))")
    out: list[str] = []

    def status() -> str:
        try:
            p = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True,
                               timeout=30, check=False)
        except subprocess.TimeoutExpired:
            return "HANG"
        out.append(p.stdout)
        return str(p.returncode)

    got, dt = watchdog(status, 35)
    line = next((ln for ln in "".join(out).splitlines() if ln.startswith("silent")), "")
    check("T3b CLI status", got == "0" and " unknown " in line and dt < 20,
          f"exit {got} in {dt:.1f}s; row: {' '.join(line.split())}")

    # QA-T4 — a transfer that stalls 1.5 s in is dropped after ~30 s of silence; the operator's own
    # ssh command (HostKeyAlias — verifies GitHub's key behind the relay) is kept as the base
    os.environ["GIT_SSH_COMMAND"] = "ssh -o HostKeyAlias=github.com"
    got, dt = watchdog(git_read(f"ssh://git@127.0.0.1:{stall_proxy(1.5)}/{REPO}"), 75)
    check("T4 mid-transfer stall", got == "transport-error" and 15 < dt < 60, f"{got} in {dt:.1f}s")

    print(f"SUMMARY pass={RESULTS.count(True)} fail={RESULTS.count(False)}")
    sys.stdout.flush()
    os._exit(0 if all(RESULTS) else 1)  # daemon threads may still hold a hung probe (control run)


if __name__ == "__main__":
    main()
````

## 9. Operator decision points (Phase 2 — answer with the approval)

| # | Decision | A (recommended — § 5 implements A) | B |
|---|---|---|---|
| D19 | Approve PLAN-019 | **APPROVE D19.A** | revise |
| D-1 | Whose ssh command git runs | **Keep the operator's own** (`GIT_SSH_COMMAND`, else `core.sshCommand`) and append the options; a legacy `GIT_SSH` program is left alone (the cap still applies) | Always `ssh` + the options — simpler, but silently overrides an operator's ssh setting (W2-class machines lose their key) |
| D-2 | A cap on every transport command | **300 s** on every git / rsync command — catches the slow-but-alive transfer; a normal read takes 3–11 s | No cap — the ssh options only (a trickling transfer stays unbounded) |

Reply e.g. **"plan 019 approved, all A"**. Choosing B on D-1 or D-2 → a plan revision (re-generated § 5)
before Phase 3.

### 9.1 Decision record (Phase 2, 2026-10-12)

- **D19.A — APPROVED:** operator *"D1. A , D2. A"* then *"go"* (2026-10-12) — "go" answered the
  explicit ask to confirm both the plan approval and the two commits.
- **D-1 = A** — keep the operator's own ssh command (`GIT_SSH_COMMAND`, else `core.sshCommand`) and append
  the options; a legacy `GIT_SSH` program is left alone.
- **D-2 = A** — a 300 s cap on every git / rsync command.
- **No § 5 change:** the blocks re-extracted from this file stay byte-identical to the proven files
  (re-verified in the approval commit).

## 10. Rollback path

`git revert <Phase 3 sha>` restores transport 0.3 + the tests + docs in one step; no target, registry or
Set Version state changes, so nothing else to undo.

## 11. Known risks + mitigation

- **R1 — an operator's ssh command that is not ssh-compatible** (a wrapper that rejects `-o`): git
  commands fail with an ssh error → the target reads `unknown`, nothing written. Mitigation: visible, not
  silent; the operator drops the wrapper or unsets it. None configured on the curator Mac (§ 3).
- **R2 — orphaned ssh after the 300 s cap fires:** `subprocess.run` kills git, not its ssh child. With
  the D-1 options the orphan ends within ~10–40 s of going silent; a slow-but-alive orphan ends when its
  pipe to the dead git breaks (next write). No process-group kill (would need `Popen` + `killpg`; POSIX
  only) — revisit only if seen.
- **R3 — a push cut by the cap may still have landed** server-side (the ref update is atomic). The run
  reports failure; the next `sync` re-materializes fresh and reports up-to-date. Mitigation: the existing
  per-target isolation + fetch-fresh rule (architecture § 9).
- **R4 — 300 s too short for a legitimately huge clone:** reads are shallow + blobless + sparse (3–11 s
  measured); a write clones one branch tip at depth 1. Revisit the constant if a target ever trips it.
  **Phase 3 observation (2026-10-12):** on a slow link (GitHub 24 KB/s, ~316 ms RTT) normal 780-estimator
  reads took 42–176 s on BOTH the old and the new code — the blobless `checkout` (lazy blob fetch) was
  36–156 s of it. All succeeded under the cap; the margin on a bad link is ~1.7×, not ~30×. Kept at
  300 s (D-2 as approved); a read that trips it shows the target `unknown` (non-fatal).
- **R5 — keepalive timing varies:** a stall is dropped 30–41 s after it starts, depending on where the
  10 s probe cycle is (both seen). QA-T4 accepts 15–60 s.

## 12. Acceptance criteria

1. Every `GitTarget` git command runs with `GIT_SSH_COMMAND` = (operator base or `ssh`) + the four
   options; legacy `GIT_SSH` alone → environment inherited (QA-T1).
2. Every transport command is capped at 300 s; a timeout raises `TransportError` (QA-T1).
3. rsync commands unchanged (QA-T1 guard).
4. Real fleet `status` unchanged (QA-T2 ⚑); a silent git server fails in < 15 s and reads `unknown`
   through the CLI (QA-T3 ⚑); a mid-transfer stall is dropped with the operator's base kept (QA-T4 ⚑).
5. 172 tests green, ruff + mypy --strict clean, governance exit 0 / 0 (QA-T1, QA-T5).
6. `docs/architecture.md` § 8 transport paragraph matches the code (§ 4 drift rule).

## Rule 13 senior-review pass (2026-10-12)

Run once on the complete plan + tracker with the § 15.8 prompt, the tools run against the EXTRACTED
text (L051): § 5 + the § 8 harness parsed back from this file onto a fresh export of `bf8669e` → 17 / 17
blocks clean, the three code files byte-identical to the proven copy; positive control (one FIND
corrupted) → exactly that block + its file FAIL. On the extracted tree: `ruff check` clean, `mypy
--strict` 0 issues (25 files, fresh cache), `pytest` 172 passed; the extracted harness 4 / 4 PASS (T2
7.0 s, T3a 10.1 s, T3b 10.1 s, T4 41.1 s); no ssh left running.

Found + fixed in the pass:

1. **The stall drop time was understated** — code comment, transport header and architecture text said
   "~30 s"; measured drops are 30.9–41.6 s (one keepalive cycle of slack). → "~30–40 s" in all three
   (§ 5 regenerated + re-proven); R5 + QA-T4's 15–60 s window record the spread.
2. **The QA harness hid its own failures** on the old code: T3b ran the CLI under `redirect_stdout` in
   a thread that hung, so every later line (FAIL lines + SUMMARY) went into the buffer. → T3b runs the
   CLI as a subprocess with its own 30 s limit; the control now prints `pass=1 fail=3` (9th data point for
   "a green proof must prove it ran").
3. **QA-T4's first window (30–60 s) was too tight** — one run dropped at 30.9 s. → 15–60 s: the lower
   bound only has to prove the relay worked (a lost base command fails in < 5 s).
4. **Four CLI-test fakes of `_run` take one argument** — found by the full-tree run (3 FAILED,
   TypeError), not by the transport tests. → § 5c + `tests/test_cli.py` in the ALLOWLIST (8 files).
5. **QA-T1's control was ambiguous** ("the 9 new tests … 8 FAIL") → names the exact command and the
   expected `8 failed, 20 passed`.

Checked, no change: every `TransportError` caller (`cli.py:80`, `:142`, `:277`) handles a timeout with no
edit; `_configured_ssh_command` has its own 10 s cap (never inherits the 300 s one); an empty
`GIT_SSH_COMMAND` falls through to `core.sshCommand` / `ssh` (git alone would try to run an empty
command and fail — the engine now works there; no regression); § 1 ↔ § 5 ↔ § 7 ↔ § 8 ↔ § 12 consistent (8 files; QA-T1…T5);
no hedge words (Rule 7). **No new design decision surfaced** beyond D-1 / D-2, both already raised in
chat before drafting.
