<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Status: CLOSED -->
<!--
CHANGE LOG
v1.0 — 2026-08-16 — Phase 3 implemented in a fresh session (single commit, 25-file § 7 ALLOWLIST;
reconcile pass clean — all 10 § 5A–5F blocks re-extracted from this file and written byte-for-byte,
diffs vs live source matched the plan's described scope, 7/7 § 5G FIND anchors unique, all
from-versions verified; no plan defects). Phase 4: QA A–D + F–J PASSED (A: ruff/mypy --strict clean,
pytest 110 passed at ship indentation; C/D: Rule 15 feature-ON runs against the REAL vault content —
local dry-run→write→idempotent + git push to a local bare remote, all assertions green; E:
operator-waived to the post-registration live smoke, recorded in the tracker). Plan CLOSED; Phase 5
(push + tag `set-v1.6`) awaits the operator gate.
v0.1b — 2026-08-16 — Phase 2: **APPROVE D8.A** (operator, 2026-08-16). Status → APPROVED; Phase 3 to
run in a fresh session per § 15.3. D1 (TEMPLATE-ONLY markers + instance-heading PROJECT-OWNED blocks,
Set v1.6) and D2 (§ 3.1 stays suite-owned) confirmed; QA-E ssh live-path waiver confirmed (Rule 15,
per-change, recorded in the tracker).
v0.1a — 2026-08-16 — Rule 13 senior-review pass (last task of Phase 1; per L051 + recurrence #4 the
tools were ACTUALLY RUN — and against the PLAN FILE's own text, not the drafting copy). Mechanical
results: (1) all 10 § 5A–5F fenced blocks re-EXTRACTED from this file and byte-compared against the
proven overlay — identical; (2) a fresh tree materialized from the extracted blocks over live
src/tests → `ruff check` clean, `mypy --strict` "no issues found in 22 source files", pytest
**110 passed**; (3) every § 5G FIND block verified to occur EXACTLY ONCE in its live target doc
(7/7); (4) cross-section counts reconciled — § 7 ALLOWLIST 25 = tracker Phase-3 rows 25, § 3 map
11 rows = 5A SYNC_MAP 11 items, § 8 QA A–J = tracker letters (E waived); (5) domain-neutral grep
over plan + tracker = 0 hits. No new design decision beyond D1/D2 (already § 9). Plan finalized →
ready for Phase 2.
v0.1 — 2026-08-16 — Initial DRAFT. Phase 0 (engine + marker + toolchain audit) + Phase 1 (design).
The § 5 code was developed and PROVEN in a scratch overlay before being embedded: ruff clean,
mypy --strict clean (22 files), pytest 110 passed (88 existing + 22 new) — at the exact final ship
indentation (L051 rec #4). Design decisions D1/D2 settled with the operator via § 9; DD-A…DD-I
settled at design (§ 3).
-->

# PLAN-008 — Slice 5: `sync` — section-aware suite propagation (Set v1.6)

> **Type:** Major / vital — new engine module other code depends on; edits `src/standard_document_updater/`
> (Critical File) and `docs/standards/` (Critical File — the sync-enablement marker changes). Runs under
> the § 15 plan workflow. **Sibling tracker:** [`PLAN-008_tracker.md`](PLAN-008_tracker.md) (big plan:
> multi-scenario § 8 verify + spans sessions — Phase 3 is a fresh session).
> **No real target repo is written by this plan** — the registry stays empty; QA runs against fixtures
> and a scratch bare git repo.

---

## 1. Goal

Ship the last engine slice: **`sync`** — propagate the vault's suite to every registered adopter
without clobbering its customizations (architecture § 7). Suite-owned files are replaced whole; the
three mixed files (`CLAUDE.md`, both session files) are **section-merged** — every `PROJECT-OWNED`
block in the target is preserved verbatim, everything else comes from the vault template;
`docs/SET_VERSION_ADOPTED.md` gets a mechanical adoption-record update. Dry-run by default; `--write`
applies and flushes per target over the existing transport layer. Plus the enabling doc changes
(**Standard Set Version v1.6**): `TEMPLATE-ONLY` markers + a project-owned heading block in the two
session templates (so merge output never carries template banners), matching marker wraps in this
vault's own instances, and the § 14 stub-keep wording. Also folds the long-deferred **DD-1**
(`setversion.count_open_log_entries` delegates to `logentry.parse_log`). After this plan the engine's
harvest → integrate → sync loop is complete.

## 2. Operator constraints (settled at design)

- **Registry stays EMPTY through this plan** (operator decision 2026-06-21, reaffirmed in the queue):
  real targets are registered only after PLAN-008 ships; then the live git/ssh smoke runs.
- **Read-only toward every real project.** QA writes go only to tmp fixtures + a scratch bare repo.
- **No rule/lesson content change** — Set v1.6 is marker/wording enablement only; counts stay 15/67.
- **Rule 15 feature-ON:** local-transport end-to-end (QA-C) + git transport against a LOCAL bare
  remote (QA-D) are ship-gating. The ssh live path is operator-waived to the post-registration live
  smoke (recorded in the tracker; pairs with PLAN-007's deferred QA K–N).
- Domain-neutral gate: zero-hit grep on all new/changed template text (QA-I).

## 3. Scope summary

**The SYNC_MAP (dispositive — § 5A carries it in code):**

| Vault source | Target path | Mode |
|---|---|---|
| `docs/standards/CLAUDE.md` | `CLAUDE.md` | merge |
| `docs/standards/PROJECT_STANDARDS.md` | same path | replace |
| `docs/standards/PROMPT_STANDARDS.md` | same path | replace |
| `docs/standards/MEMORY_PROTOCOL.md` | same path | replace |
| `docs/standards/ENGINEERING_STANDARDS.md` | same path | replace |
| `docs/standards/VALIDATION_STANDARDS.md` | same path | replace |
| `docs/standards/CICD_STANDARDS.md` | same path | replace |
| `docs/standards/LESSONS.md` | `archive/LESSONS.md` | replace |
| `docs/standards/SESSION_OPENER.md` | `docs/SESSION_OPENER.md` | merge |
| `docs/standards/SESSION_CLOSER.md` | `docs/SESSION_CLOSER.md` | merge |
| — | `docs/SET_VERSION_ADOPTED.md` | record |

**Design decisions settled at design time (DD):**

- **DD-A — command shape:** dry-run report by default; `--write` applies + flushes; `--project NAME`
  (repeatable) filters; `--diff` prints unified diffs. Mirrors `integrate`'s gate pattern.
- **DD-B — full-footprint sessions** (answers the standing materialization question): `sync` needs
  `archive/` + root `CLAUDE.md`, which live outside `docs/`. `Target.session()` grows
  `full: bool = False`; full ssh sessions rsync `docs/` + `archive/` + `CLAUDE.md` (each required —
  hard-fail); full git READ sessions add `archive` to the sparse set (cone mode already includes root
  files); git WRITE sessions were already full clones. Existing commands are unchanged (full=False).
- **DD-C — ordinal marker matching:** PROJECT-OWNED blocks pair template↔target by position, with a
  STRICT count-equality check; any mismatch (or unbalanced/nested markers) is a per-file `SyncError` —
  the target fails loudly, nothing is written to it. The target's own BEGIN-comment text is preserved.
- **DD-D — headers:** merged files keep the TARGET's own header, minor-bumped, with a standard sync
  CHANGE-LOG line + Last-Updated refresh; replaced files carry the vault file verbatim (its header IS
  the version). Unchanged bodies are never re-bumped (idempotence: second run = all up-to-date).
- **DD-E — adoption record:** mechanical — Set-Version + Adopted-on bullets rewritten, a newest-first
  backport-table row inserted, header bumped. A target missing the SVA file or table errors (an
  unadopted project is adopt-mode's job, not sync's).
- **DD-F — the target's `documents_manifest` is NOT edited by sync** (formats vary per project; a
  silent mis-edit is worse than a stale cell). After a write, sync prints a note telling the operator
  to reconcile the target's manifest cells at that project's next session (its own governance catches
  the drift).
- **DD-G — DD-1 fold:** `count_open_log_entries` delegates to `logentry.parse_log` — one log parser,
  one truth. Semantics tighten from `startswith("open")` to `== "open"` (case-insensitive) — the
  harvest criterion; the drift count can no longer disagree with what harvest collects. Pinned by a
  new regression test.
- **DD-H — the vault is never a sync target.** Its own adopter instances are reconciled same-commit
  at each release (the SVA discipline); `sync` operates on the registry only.
- **DD-I — per-target isolation:** a failed target (transport or SyncError) is reported to stderr and
  the run continues; exit 1 at the end with a FAILED summary; healthy targets still sync. Within one
  target, plan_target validates every file before any write (no partial target writes).

**Operator decisions baked in per § 9 approval (D1, D2):** see § 9.

Out of scope: registering targets; the ssh live run; adopt-mode for divergent/legacy projects
(PLAN-011); retiring the desktop export (PLAN-009); any change to `harvest`/`integrate` behavior.

## 4. Phase tracker (high-level — granular sub-tasks in the sibling tracker)

- Phase 0 — Audit ✅ 2026-08-16 (architecture § 7/§ 8; all engine modules read; marker inventory —
  template CLAUDE 4 owned blocks = root instance 4, opener 2/2, closer 1/1 (pre-v1.6); toolchain
  verified: .venv python 3.11.15 + ruff/mypy/pytest, mypy strict=true)
- Phase 1 — Design ✅ 2026-08-16 (this file; § 5 code proven in overlay BEFORE embedding; Rule 13
  pass re-extracts from THIS file and re-runs the tools)
- Phase 2 — Operator approval ✅ 2026-08-16 — **APPROVE D8.A**
- Phase 3 — Implement ✅ 2026-08-16 (fresh session; single commit per § 7 ALLOWLIST; reconcile pass
  clean — no plan defects)
- Phase 4 — Validate ✅ 2026-08-16 (QA A–D + F–J passed; E operator-waived per Rule 15 — see tracker)
- Phase 5 — Operator gate ⏸ (push + tag `set-v1.6`)

## 5. Transformation rules (verbatim)

> **Code files (5A–5F): the fenced block IS the complete final file content** — the implementer
> writes each file exactly as embedded (byte-for-byte), then diffs against the live source to confirm
> the change scope matches this plan's description. This is the most mechanical Rule 7 form; it is
> what the Rule 13 pass ran the tools against, at ship indentation.

### 5A–5E — Engine code (full final file contents)

#### 5A — `src/standard_document_updater/sync.py` — NEW file

```python
# ==============================================================
# VERSION: 0.1
# Section-aware suite propagation (`sync`): replace | merge | record per file.
#
# CHANGE LOG
# v0.1 — 2026-08-16 — Initial: SYNC_MAP, marker-block parsing (PROJECT-OWNED /
#         TEMPLATE-ONLY), header split + minor-bump, merge_file, record_adoption,
#         plan_target / apply_actions / render_plan (PLAN-008).
# ==============================================================
"""Propagate the vault suite to an adopter without clobbering its customizations.

Architecture § 7: suite-owned files are replaced whole; mixed files are
section-merged — every PROJECT-OWNED block in the target is preserved verbatim,
everything else comes from the vault template (TEMPLATE-ONLY blocks stripped);
docs/SET_VERSION_ADOPTED.md gets a mechanical adoption-record update. All
functions here are pure text transforms over an already-materialized target
root (the transport layer does the fetching/flushing); nothing in this module
touches the vault.
"""
from __future__ import annotations

import difflib
import re
from dataclasses import dataclass
from pathlib import Path

from standard_document_updater import setversion
from standard_document_updater.errors import StandardDocSetError

_PO_BEGIN_RE = re.compile(r"^<!-- PROJECT-OWNED:BEGIN[^\n]*$", re.MULTILINE)
_PO_END_RE = re.compile(r"^<!-- PROJECT-OWNED:END -->[ \t]*$", re.MULTILINE)
_TO_BEGIN_RE = re.compile(r"^<!-- TEMPLATE-ONLY:BEGIN[^\n]*$", re.MULTILINE)
_TO_END_RE = re.compile(r"^<!-- TEMPLATE-ONLY:END -->[ \t]*$", re.MULTILINE)
_VERSION_RE = re.compile(r"<!-- VERSION: (\d+)\.(\d+) -->")
_LAST_UPDATED_RE = re.compile(r"<!-- Last Updated: \d{4}-\d{2}-\d{2} -->")
_ADOPTED_BULLET_RE = re.compile(r"^- \*\*Standard Set Version:\*\*[^\n]*$", re.MULTILINE)
_ADOPTED_ON_RE = re.compile(r"^- \*\*Adopted on:\*\*[^\n]*$", re.MULTILINE)
_BACKPORT_SEP_RE = re.compile(
    r"^\| Set Version \| Adopted on \| Notes \|\n\|[-| ]+\|$", re.MULTILINE
)


class SyncError(StandardDocSetError):
    """A target file cannot be safely synced (structure mismatch); nothing is written."""


@dataclass(frozen=True)
class SyncItem:
    """One suite file the engine propagates: vault source -> target path + mode."""

    vault_rel: str
    target_rel: str
    mode: str  # "replace" | "merge" | "record"


# Architecture § 7 ownership table. Order = report order.
SYNC_MAP: tuple[SyncItem, ...] = (
    SyncItem("docs/standards/CLAUDE.md", "CLAUDE.md", "merge"),
    SyncItem(
        "docs/standards/PROJECT_STANDARDS.md", "docs/standards/PROJECT_STANDARDS.md", "replace"
    ),
    SyncItem("docs/standards/PROMPT_STANDARDS.md", "docs/standards/PROMPT_STANDARDS.md", "replace"),
    SyncItem("docs/standards/MEMORY_PROTOCOL.md", "docs/standards/MEMORY_PROTOCOL.md", "replace"),
    SyncItem(
        "docs/standards/ENGINEERING_STANDARDS.md",
        "docs/standards/ENGINEERING_STANDARDS.md",
        "replace",
    ),
    SyncItem(
        "docs/standards/VALIDATION_STANDARDS.md",
        "docs/standards/VALIDATION_STANDARDS.md",
        "replace",
    ),
    SyncItem("docs/standards/CICD_STANDARDS.md", "docs/standards/CICD_STANDARDS.md", "replace"),
    SyncItem("docs/standards/LESSONS.md", "archive/LESSONS.md", "replace"),
    SyncItem("docs/standards/SESSION_OPENER.md", "docs/SESSION_OPENER.md", "merge"),
    SyncItem("docs/standards/SESSION_CLOSER.md", "docs/SESSION_CLOSER.md", "merge"),
    SyncItem("", "docs/SET_VERSION_ADOPTED.md", "record"),
)


@dataclass(frozen=True)
class FileAction:
    """The planned outcome for one target file (computed before any write)."""

    target_rel: str
    mode: str
    changed: bool
    old_text: str
    new_text: str  # == old_text when changed is False


def _block_spans(
    text: str, begin_re: re.Pattern[str], end_re: re.Pattern[str], label: str
) -> list[tuple[int, int]]:
    """Character spans of marker blocks (BEGIN line start .. END line end).

    Raises SyncError on unbalanced or nested markers — a malformed file must
    never be guessed at.
    """
    events = sorted(
        [(m.start(), m.end(), "begin") for m in begin_re.finditer(text)]
        + [(m.start(), m.end(), "end") for m in end_re.finditer(text)]
    )
    spans: list[tuple[int, int]] = []
    open_start: int | None = None
    for start, end, kind in events:
        if kind == "begin":
            if open_start is not None:
                raise SyncError(f"{label}: nested marker BEGIN without END")
            open_start = start
        else:
            if open_start is None:
                raise SyncError(f"{label}: marker END without BEGIN")
            spans.append((open_start, end))
            open_start = None
    if open_start is not None:
        raise SyncError(f"{label}: marker BEGIN without END")
    return spans


def strip_template_only(text: str, label: str) -> str:
    """Remove TEMPLATE-ONLY blocks (plus one following blank line each)."""
    out = text
    for start, end in reversed(_block_spans(out, _TO_BEGIN_RE, _TO_END_RE, label)):
        cut = end
        if out[cut : cut + 1] == "\n":
            cut += 1
        if out[cut : cut + 1] == "\n":  # swallow one following blank line
            cut += 1
        out = out[:start] + out[cut:]
    return out


def split_header(text: str, label: str) -> tuple[str, str]:
    """Split off the leading comment header (through the CHANGE LOG comment's `-->`).

    Raises SyncError when the file lacks the standard VERSION + CHANGE LOG header.
    """
    if _VERSION_RE.search(text) is None:
        raise SyncError(f"{label}: no '<!-- VERSION: X.Y -->' header line")
    log_at = text.find("CHANGE LOG")
    if log_at == -1:
        raise SyncError(f"{label}: no CHANGE LOG comment in header")
    close_at = text.find("-->", log_at)
    if close_at == -1:
        raise SyncError(f"{label}: unterminated CHANGE LOG comment")
    split = close_at + len("-->")
    if text[split : split + 1] == "\n":
        split += 1
    return text[:split], text[split:]


def bump_header(header: str, set_version: str, today: str, label: str) -> str:
    """Minor-bump the target's own header + prepend the standard sync log line."""
    match = _VERSION_RE.search(header)
    if match is None:  # split_header already guarantees this; defensive
        raise SyncError(f"{label}: no VERSION line in header")
    major, minor = int(match.group(1)), int(match.group(2))
    new_version = f"{major}.{minor + 1}"
    out = header.replace(match.group(0), f"<!-- VERSION: {new_version} -->", 1)
    out = _LAST_UPDATED_RE.sub(f"<!-- Last Updated: {today} -->", out, count=1)
    log_at = out.find("CHANGE LOG\n")
    if log_at == -1:
        raise SyncError(f"{label}: no CHANGE LOG line in header")
    insert_at = log_at + len("CHANGE LOG\n")
    line = (
        f"v{new_version} — {today} — sync: Standard Set Version {set_version} applied by the "
        "engine (suite-owned sections updated; PROJECT-OWNED blocks preserved).\n"
    )
    return out[:insert_at] + line + out[insert_at:]


def merge_file(
    template_text: str, target_text: str, set_version: str, today: str, label: str
) -> str:
    """Section-merge a mixed-ownership file (architecture § 7).

    Output = template body (TEMPLATE-ONLY stripped) with each PROJECT-OWNED
    block replaced, in order, by the target's corresponding block — under the
    target's own header, minor-bumped. Returns target_text unchanged when the
    merged body already equals the target body (idempotence: no bump, no write).
    """
    _, template_body = split_header(template_text, f"{label} (template)")
    target_header, target_body = split_header(target_text, label)
    body = strip_template_only(template_body, f"{label} (template)")
    tpl_spans = _block_spans(body, _PO_BEGIN_RE, _PO_END_RE, f"{label} (template)")
    tgt_spans = _block_spans(target_body, _PO_BEGIN_RE, _PO_END_RE, label)
    if len(tpl_spans) != len(tgt_spans):
        raise SyncError(
            f"{label}: PROJECT-OWNED block count mismatch (template {len(tpl_spans)} vs "
            f"target {len(tgt_spans)}) — reconcile the target by hand before syncing"
        )
    pairs = zip(reversed(tpl_spans), reversed(tgt_spans), strict=True)
    for (t_start, t_end), (g_start, g_end) in pairs:
        body = body[:t_start] + target_body[g_start:g_end] + body[t_end:]
    if body == target_body:
        return target_text
    return bump_header(target_header, set_version, today, label) + body


def record_adoption(target_text: str, set_version: str, today: str, label: str) -> str:
    """Mechanically update docs/SET_VERSION_ADOPTED.md to the vault Set Version."""
    header, body = split_header(target_text, label)
    if _ADOPTED_BULLET_RE.search(body) is None:
        raise SyncError(f"{label}: no '- **Standard Set Version:**' bullet")
    body = _ADOPTED_BULLET_RE.sub(
        f"- **Standard Set Version:** {set_version} (synced from the vault by the engine; "
        "release history: the vault's STANDARDS_INDEX.md § 6)",
        body,
        count=1,
    )
    body = _ADOPTED_ON_RE.sub(f"- **Adopted on:** {today} (synced)", body, count=1)
    sep = _BACKPORT_SEP_RE.search(body)
    if sep is None:
        raise SyncError(f"{label}: no backport-tracking table header")
    row = (
        f"| {set_version} | {today} | sync (engine): suite-owned files replaced; "
        "PROJECT-OWNED blocks preserved; see the vault STANDARDS_INDEX § 6 |\n"
    )
    insert_at = sep.end() + 1  # just past the separator row's newline
    body = body[:insert_at] + row + body[insert_at:]
    return bump_header(header, set_version, today, label) + body


def plan_target(
    vault_root: Path, target_root: Path, set_version: str, today: str
) -> list[FileAction]:
    """Compute every file action for one target. Validates ALL files before any write.

    Raises SyncError on the first unsafe file (missing, malformed header, marker
    mismatch) so a structurally surprising target is never partially written.
    """
    actions: list[FileAction] = []
    for item in SYNC_MAP:
        target_path = target_root / item.target_rel
        if not target_path.exists():
            raise SyncError(
                f"target file missing: {item.target_rel} — not a converged adopter "
                "(bootstrap or adopt it first)"
            )
        old = target_path.read_text(encoding="utf-8")
        if item.mode == "record":
            adopted = setversion.parse_adopted_version(target_path)
            vault = tuple(int(p) for p in set_version.lstrip("v").split("."))
            if adopted == vault:
                new = old
            else:
                new = record_adoption(old, set_version, today, item.target_rel)
        else:
            vault_path = vault_root / item.vault_rel
            if not vault_path.exists():
                raise SyncError(f"vault file missing: {item.vault_rel}")
            vault_text = vault_path.read_text(encoding="utf-8")
            if item.mode == "replace":
                new = vault_text
            else:
                new = merge_file(vault_text, old, set_version, today, item.target_rel)
        actions.append(
            FileAction(
                target_rel=item.target_rel,
                mode=item.mode,
                changed=new != old,
                old_text=old,
                new_text=new,
            )
        )
    return actions


def apply_actions(target_root: Path, actions: list[FileAction]) -> list[Path]:
    """Write every changed action's new text. Returns the changed repo-relative paths."""
    written: list[Path] = []
    for action in actions:
        if not action.changed:
            continue
        (target_root / action.target_rel).write_text(action.new_text, encoding="utf-8")
        written.append(Path(action.target_rel))
    return written


def render_plan(project_name: str, actions: list[FileAction], *, show_diff: bool) -> str:
    """Human-readable per-target report (the dry-run output)."""
    changed = [a for a in actions if a.changed]
    lines = [f"[{project_name}] {len(changed)} of {len(actions)} suite file(s) need sync:"]
    if not changed:
        lines = [f"[{project_name}] up-to-date — all suite files match the vault."]
    for action in actions:
        marker = "changed " if action.changed else "ok      "
        lines.append(f"  {marker}{action.mode:8}{action.target_rel}")
    if show_diff:
        for action in changed:
            diff = difflib.unified_diff(
                action.old_text.splitlines(keepends=True),
                action.new_text.splitlines(keepends=True),
                fromfile=f"a/{action.target_rel}",
                tofile=f"b/{action.target_rel}",
            )
            lines.append("")
            lines.append("".join(diff).rstrip("\n"))
    return "\n".join(lines)
```

#### 5B — `src/standard_document_updater/transport.py` — full replacement (0.1 → 0.2)

```python
# ==============================================================
# VERSION: 0.2
# Pluggable target transports (local | git | ssh): materialize -> operate -> flush.
#
# CHANGE LOG
# v0.2 — 2026-08-16 — PLAN-008 (sync): sessions grow a `full` scope — full=True materializes the
#         whole sync footprint (docs/ + archive/ + root CLAUDE.md); git read path adds `archive`
#         to the sparse set (cone mode already includes root files); ssh adds two rsyncs.
# v0.1 — 2026-06-20 — Initial: Target ABC + Local/Git/Ssh drivers + make_target.
# ==============================================================
"""Reach a target repo wherever it lives, keeping the engine transport-agnostic.

D1 (materialize-to-local-root): each Target fetches the target repo to a local
root; the engine performs its existing Path-based I/O against that root; on the
write path the Target flushes the changes back to the source.

Transports (chosen per-target in config/projects.toml):
  local — a folder on this machine (default; reads/writes happen in place).
  git   — clone/fetch from a forge remote over SSH; write-back = commit + push (D2/D5).
  ssh   — rsync from a remote host; write-back = rsync the changed files back.
"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from abc import ABC, abstractmethod
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from standard_document_updater.errors import StandardDocSetError
from standard_document_updater.registry import Project

_DOCS = "docs"        # the subtree status/drift/harvest/integrate touch (full=False sessions)
_ARCHIVE = "archive"  # + root CLAUDE.md: the wider footprint `sync` needs (full=True sessions)
_ROOT_FILE = "CLAUDE.md"
_COMMIT_NAME = "Standard DocSet"
_COMMIT_EMAIL = "standard-docset@localhost"


class TransportError(StandardDocSetError):
    """A transport operation (clone / fetch / push / rsync) failed."""


def _run(cmd: list[str]) -> None:
    """Run a subprocess; raise TransportError with captured output on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except OSError as exc:  # the binary is missing / not executable
        raise TransportError(f"could not run {cmd[0]}: {exc}") from exc
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()
        raise TransportError(f"{' '.join(cmd)} failed (exit {proc.returncode}): {detail}")


class Target(ABC):
    """A managed repo reachable through some transport. Materialize -> operate -> flush."""

    def __init__(self, project: Project) -> None:
        self.project = project

    @property
    def name(self) -> str:
        return self.project.name

    @property
    def location(self) -> str:
        return self.project.location

    @contextmanager
    def session(self, *, writable: bool = False, full: bool = False) -> Iterator[Path]:
        """Yield a local repo root for the target; clean up any temp copy on exit.

        full=True materializes the whole sync footprint (docs/ + archive/ + root
        CLAUDE.md) instead of docs/ only — required by `sync`, whose targets
        include files outside docs/.
        """
        root = self._materialize(writable=writable, full=full)
        try:
            yield root
        finally:
            self._dispose(root)

    @abstractmethod
    def _materialize(self, *, writable: bool, full: bool) -> Path:
        """Fetch the repo to a local root (in place for local; a temp dir otherwise)."""

    def flush(self, root: Path, changed: list[Path], message: str) -> None:  # noqa: B027
        """Push changed files (repo-relative) back to the source. No-op default (local)."""

    def _dispose(self, root: Path) -> None:  # noqa: B027
        """Remove a temporary materialization. No-op default (in-place local root)."""


class LocalTarget(Target):
    """A repo that is a folder on this machine. Reads and writes happen in place."""

    def _materialize(self, *, writable: bool, full: bool) -> Path:
        path = self.project.path
        if path is None or not path.exists():
            raise TransportError(f"local target {self.name!r}: path not found: {path}")
        return path


class GitTarget(Target):
    """A repo fetched from a forge remote over SSH. Write-back = direct push (D2/D5)."""

    def _materialize(self, *, writable: bool, full: bool) -> Path:
        url = self.project.git_url
        if not url:
            raise TransportError(f"git target {self.name!r}: missing git_url")
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

    def _dispose(self, root: Path) -> None:
        shutil.rmtree(root, ignore_errors=True)


class SshTarget(Target):
    """A repo on a remote host reached via rsync over SSH. Only docs/ is materialized."""

    def _materialize(self, *, writable: bool, full: bool) -> Path:
        host, base = self._endpoint()
        dest = Path(tempfile.mkdtemp(prefix="stddocset-ssh-"))
        (dest / _DOCS).mkdir(parents=True, exist_ok=True)
        _run(["rsync", "-az", f"{host}:{base}/{_DOCS}/", f"{dest / _DOCS}/"])
        if full:  # the sync footprint reaches outside docs/ — hard-fail if absent
            (dest / _ARCHIVE).mkdir(parents=True, exist_ok=True)
            _run(["rsync", "-az", f"{host}:{base}/{_ARCHIVE}/", f"{dest / _ARCHIVE}/"])
            _run(["rsync", "-az", f"{host}:{base}/{_ROOT_FILE}", f"{dest / _ROOT_FILE}"])
        return dest

    def flush(self, root: Path, changed: list[Path], message: str) -> None:
        host, base = self._endpoint()
        for rel in changed:
            _run(["rsync", "-az", str(root / rel), f"{host}:{base}/{rel.as_posix()}"])

    def _endpoint(self) -> tuple[str, str]:
        host = self.project.ssh_host
        path = self.project.ssh_path
        if not host or not path:
            raise TransportError(f"ssh target {self.name!r}: missing ssh_host or ssh_path")
        return host, path.rstrip("/")

    def _dispose(self, root: Path) -> None:
        shutil.rmtree(root, ignore_errors=True)


_DRIVERS: dict[str, type[Target]] = {
    "local": LocalTarget,
    "git": GitTarget,
    "ssh": SshTarget,
}


def make_target(project: Project) -> Target:
    """Build the Target driver for a project's declared transport."""
    driver = _DRIVERS.get(project.transport)
    if driver is None:
        raise TransportError(
            f"project {project.name!r}: unknown transport {project.transport!r} "
            f"(expected one of: {', '.join(sorted(_DRIVERS))})"
        )
    return driver(project)
```

#### 5C — `src/standard_document_updater/cli.py` — full replacement (0.4 → 0.5)

```python
# ==============================================================
# VERSION: 0.5
# Command-line interface: `python -m standard_document_updater <command>`.
#
# CHANGE LOG
# v0.5 — 2026-08-16 — PLAN-008 (Slice 5): add the `sync` subcommand (dry-run report by default;
#                     --write applies + flushes per target; --project filter; --diff). Per-target
#                     failure is isolated (continue others, exit 1 at the end).
# v0.4 — 2026-06-20 — Materialize each target via the transport layer (local | git | ssh): reads
#                     run inside a Target.session(); the integrate write-back uses an ExitStack +
#                     per-target flush; per-target failure is non-fatal for reads (PLAN-007).
# v0.3 — 2026-06-18 — Add the `integrate` subcommand (worksheet + --apply/--write write-back).
# v0.2 — 2026-06-16 — Add the `harvest` subcommand (open-log consolidation).
# v0.1 — 2026-06-16 13:01 — Initial: status + drift subcommands, --vault override.
# ==============================================================
"""CLI entry point and command dispatch."""
from __future__ import annotations

import argparse
import sys
from contextlib import ExitStack
from datetime import date
from pathlib import Path

from standard_document_updater import (
    __version__,
    harvest,
    integrate,
    logentry,
    report,
    setversion,
    sync,
)
from standard_document_updater.errors import StandardDocSetError
from standard_document_updater.registry import Project, load_registry
from standard_document_updater.transport import TransportError, make_target


def default_vault_root() -> Path:
    """Repo root inferred from this package's location (src layout).

    .../src/standard_document_updater/cli.py -> parents[2] == repo root.
    Override with --vault when the engine is installed outside the repo.
    """
    return Path(__file__).resolve().parents[2]


def _build_statuses(vault_root: Path) -> list[report.ProjectStatus]:
    index_path = vault_root / "docs" / "standards" / "STANDARDS_INDEX.md"
    registry_path = vault_root / "config" / "projects.toml"
    vault_version = setversion.parse_vault_version(index_path)
    statuses: list[report.ProjectStatus] = []
    for project in load_registry(registry_path):
        try:
            with make_target(project).session() as root:
                adopted_path = root / "docs" / "SET_VERSION_ADOPTED.md"
                log_path = root / "docs" / "STANDARDS_LOG.md"
                statuses.append(
                    report.compute_status(project, vault_version, adopted_path, log_path)
                )
        except TransportError as exc:
            statuses.append(report.unreachable_status(project, vault_version, str(exc)))
    return statuses


def _cmd_status(args: argparse.Namespace) -> int:
    print(report.render_table(_build_statuses(args.vault)))
    return 0


def _cmd_drift(args: argparse.Namespace) -> int:
    drifted = report.filter_drift(_build_statuses(args.vault))
    if not drifted:
        print("No drift: all registered projects are on the vault Set Version.")
        return 0
    print(report.render_table(drifted))
    print(f"\n{len(drifted)} project(s) not on the vault Set Version.")
    return 1


def _build_open_items(vault_root: Path) -> list[harvest.OpenItem]:
    registry_path = vault_root / "config" / "projects.toml"
    items: list[harvest.OpenItem] = []
    for project in load_registry(registry_path):
        try:
            with make_target(project).session() as root:
                log_path = root / "docs" / "STANDARDS_LOG.md"
                for entry in logentry.parse_log(log_path):
                    if entry.is_open:
                        items.append(harvest.OpenItem(project.name, entry))
        except TransportError as exc:
            print(f"warning: skipping {project.name!r}: {exc}", file=sys.stderr)
    return items


def _cmd_harvest(args: argparse.Namespace) -> int:
    print(harvest.render_report(_build_open_items(args.vault)))
    return 0


def _cmd_integrate(args: argparse.Namespace) -> int:
    vault_root: Path = args.vault
    lessons = vault_root / "docs" / "standards" / "LESSONS.md"
    index = vault_root / "docs" / "standards" / "STANDARDS_INDEX.md"
    if args.apply is None:
        rows = integrate.build_rows(_build_open_items(vault_root))
        proposed = integrate.next_lesson_id(lessons)
        set_version = "v" + ".".join(str(n) for n in setversion.parse_vault_version(index))
        print(integrate.render_worksheet(rows, proposed, set_version))
        return 0
    # write-back path
    dispositions = integrate.parse_decisions(args.apply)
    named = {d.project for d in dispositions}
    registry_path = vault_root / "config" / "projects.toml"
    projects = [p for p in load_registry(registry_path) if p.name in named]
    with ExitStack() as stack:
        targets = {p.name: make_target(p) for p in projects}
        roots = {name: stack.enter_context(t.session(writable=True)) for name, t in targets.items()}
        log_path_for = {name: root / "docs" / "STANDARDS_LOG.md" for name, root in roots.items()}
        report_lines = integrate.apply_writeback(dispositions, log_path_for, write=args.write)
        if args.write:
            count = len(dispositions)
            message = f"Standard DocSet: integrate write-back ({count} status update(s))"
            for name in sorted(named & set(targets)):
                targets[name].flush(roots[name], [Path("docs/STANDARDS_LOG.md")], message)
    print("\n".join(report_lines))
    return 0


def _sync_projects(vault_root: Path, only: list[str] | None) -> list[Project]:
    """Registry rows to sync, honoring the --project filter (unknown names error)."""
    projects = load_registry(vault_root / "config" / "projects.toml")
    if only is None:
        return projects
    by_name = {p.name: p for p in projects}
    unknown = [name for name in only if name not in by_name]
    if unknown:
        raise StandardDocSetError(f"not in the registry: {', '.join(sorted(unknown))}")
    return [by_name[name] for name in only]


def _cmd_sync(args: argparse.Namespace) -> int:
    vault_root: Path = args.vault
    index = vault_root / "docs" / "standards" / "STANDARDS_INDEX.md"
    set_version = "v" + ".".join(str(n) for n in setversion.parse_vault_version(index))
    today = date.today().isoformat()
    projects = _sync_projects(vault_root, args.project)
    if not projects:
        print("No registered projects to sync. (Register targets in config/projects.toml.)")
        return 0
    if not args.write:
        print(f"DRY-RUN — vault Standard Set Version {set_version}; no target is written.\n")
    failed: list[str] = []
    for project in projects:
        try:
            target = make_target(project)
            with target.session(writable=args.write, full=True) as root:
                actions = sync.plan_target(vault_root, root, set_version, today)
                print(sync.render_plan(project.name, actions, show_diff=args.diff))
                changed = [a for a in actions if a.changed]
                if args.write and changed:
                    written = sync.apply_actions(root, changed)
                    message = f"Standard DocSet: sync to Standard Set Version {set_version}"
                    target.flush(root, written, message)
                    print(f"  -> wrote + flushed {len(written)} file(s)")
                    print(
                        "  note: sync does not edit the target's documents_manifest — "
                        "reconcile its cells at that project's next session"
                    )
        except StandardDocSetError as exc:  # incl. TransportError / SyncError: isolate the target
            print(f"error: {project.name}: {exc}", file=sys.stderr)
            failed.append(project.name)
    if failed:
        print(f"\n{len(failed)} target(s) FAILED: {', '.join(failed)}", file=sys.stderr)
        return 1
    if not args.write:
        print("\n(dry-run — re-run with --write to apply)")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="standard_document_updater",
        description="Keep adopting projects in sync with the canonical standards suite.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "--vault",
        type=Path,
        default=default_vault_root(),
        help="path to the vault repo root (default: inferred from install location)",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="show every registered project's adopted vs vault Set Version")
    sub.add_parser("drift", help="show only projects not on the vault Set Version (exit 1 if any)")
    sub.add_parser(
        "harvest",
        help="consolidate open experiences-log entries across all projects",
    )
    p_int = sub.add_parser(
        "integrate",
        help="worksheet of open entries to integrate; --apply <file> writes Status back",
    )
    p_int.add_argument(
        "--apply",
        type=Path,
        default=None,
        help="decisions TOML; write integrated/rejected Status lines back to project logs",
    )
    p_int.add_argument(
        "--write",
        action="store_true",
        help="actually write (default is a dry-run diff); only valid with --apply",
    )
    p_sync = sub.add_parser(
        "sync",
        help="propagate the vault suite to registered projects (dry-run unless --write)",
    )
    p_sync.add_argument(
        "--write",
        action="store_true",
        help="write the changes and flush them to each target (default: dry-run report)",
    )
    p_sync.add_argument(
        "--project",
        action="append",
        default=None,
        metavar="NAME",
        help="limit the run to the named registry project (repeatable)",
    )
    p_sync.add_argument(
        "--diff",
        action="store_true",
        help="show a unified diff for every file that would change",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse argv and run the chosen command. Returns the process exit code."""
    args = build_parser().parse_args(argv)
    handlers = {
        "status": _cmd_status,
        "drift": _cmd_drift,
        "harvest": _cmd_harvest,
        "integrate": _cmd_integrate,
        "sync": _cmd_sync,
    }
    try:
        return handlers[args.command](args)
    except StandardDocSetError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
```

#### 5D — `src/standard_document_updater/setversion.py` — full replacement (0.1 → 0.2; DD-1)

```python
# ==============================================================
# VERSION: 0.2
# Parse Set Versions + open-log counts from standards files (live reads).
#
# CHANGE LOG
# v0.2 — 2026-08-16 — DD-1 (deferred since PLAN-004): count_open_log_entries delegates to
#                     logentry.parse_log — one log parser, one truth. Status match tightens
#                     from startswith("open") to == "open" (the harvest criterion).
# v0.1 — 2026-06-16 13:01 — Initial: vault version, adopted version, open-log count.
# ==============================================================
"""Live parsers for the version/log state the report needs.

Every read re-reads the file (never cached) per docs/architecture.md § 9 /
CLAUDE.md § 2. Regexes are pinned to the real on-disk formats:

  vault canonical  — docs/standards/STANDARDS_INDEX.md § 1 fenced block:
                       Standard Set Version: v1.1
  project adopted  — docs/SET_VERSION_ADOPTED.md:
                       - **Standard Set Version:** v1.1 (...)
  log entry        — docs/STANDARDS_LOG.md:
                       ## E001 — <title>
                       - Status:      open
"""
from __future__ import annotations

import re
from pathlib import Path

from standard_document_updater.errors import ParseError
from standard_document_updater.logentry import parse_log

_VAULT_RE = re.compile(r"^Standard Set Version:\s*v(\d+(?:\.\d+)+)", re.MULTILINE)
_ADOPTED_RE = re.compile(r"\*\*Standard Set Version:\*\*\s*v(\d+(?:\.\d+)+)")


def parse_vault_version(standards_index_path: Path) -> tuple[int, ...]:
    """Return the vault's canonical Set Version as an int tuple, e.g. (1, 1)."""
    return _parse_version(standards_index_path, _VAULT_RE, "vault Set Version")


def parse_adopted_version(adopted_path: Path) -> tuple[int, ...]:
    """Return a project's adopted Set Version as an int tuple, e.g. (1, 1)."""
    return _parse_version(adopted_path, _ADOPTED_RE, "adopted Set Version")


def _parse_version(path: Path, pattern: re.Pattern[str], label: str) -> tuple[int, ...]:
    if not path.exists():
        raise ParseError(f"{label}: file not found: {path}")
    match = pattern.search(path.read_text(encoding="utf-8"))
    if match is None:
        raise ParseError(f"{label}: no version line in {path}")
    return tuple(int(part) for part in match.group(1).split("."))


def count_open_log_entries(log_path: Path) -> int:
    """Count STANDARDS_LOG.md entries whose Status is 'open' (the harvest criterion).

    Returns 0 when the log file is absent (a project may not have started one).
    Delegates to logentry.parse_log (DD-1) — one log parser, one truth: the
    status/drift open-count can never disagree with what harvest collects.
    """
    return sum(1 for entry in parse_log(log_path) if entry.is_open)
```

#### 5E — `src/standard_document_updater/__init__.py` — full replacement (0.4 → 0.5)

```python
# ==============================================================
# VERSION: 0.5
# Standard DocSet engine — package marker + released CLI version.
#
# CHANGE LOG
# v0.5 — 2026-08-16 — PLAN-008 (Slice 5: sync): CLI version 0.4.0 -> 0.5.0.
# v0.4 — 2026-06-20 — PLAN-007 (remote-target transport): CLI version 0.3.0 -> 0.4.0.
# v0.3 — 2026-06-18 — Slice 4 (integrate): CLI version 0.2.0 -> 0.3.0.
# v0.2 — 2026-06-16 — Slice 3 (harvest): CLI version 0.1.0 -> 0.2.0.
# v0.1 — 2026-06-16 13:01 — Initial package (Slice 2: registry + status/drift).
# ==============================================================
"""Standard DocSet — keep standards/governance suites in sync across projects."""
from __future__ import annotations

__version__ = "0.5.0"
```

### 5F — Tests (5F1–5F5, full final file contents)

#### 5F1 — `tests/test_sync.py` — NEW file

```python
# ==============================================================
# VERSION: 0.1
# Unit tests for the section-aware sync engine (replace | merge | record).
#
# CHANGE LOG
# v0.1 — 2026-08-16 — Initial: header split/bump, TEMPLATE-ONLY strip, marker-block
#         pairing, merge_file (+ idempotence + mismatch), record_adoption,
#         plan_target / apply_actions / render_plan (PLAN-008).
# ==============================================================
"""Tests for standard_document_updater.sync."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest

from standard_document_updater import sync

_TODAY = "2026-08-16"
_SET = "v1.5"

_TEMPLATE = """<!-- VERSION: 2.0 -->
<!-- Last Updated: 2026-08-01 -->
<!--
CHANGE LOG
v2.0 — 2026-08-01 — suite text NEW.
-->

<!-- TEMPLATE-ONLY:BEGIN (stripped at instantiation; sync never propagates this block) -->
# FILE — (template)
> TEMPLATE banner.
<!-- TEMPLATE-ONLY:END -->
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# FILE — (fill me in)
<!-- PROJECT-OWNED:END -->

Suite paragraph NEW.

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
| placeholder row |
<!-- PROJECT-OWNED:END -->

Tail NEW.
"""

_TARGET = """<!-- VERSION: 1.3 -->
<!-- Last Updated: 2026-07-01 -->
<!--
CHANGE LOG
v1.3 — 2026-07-01 — a project edit.
-->

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# FILE — Acme (project-local)
<!-- PROJECT-OWNED:END -->

Suite paragraph OLD.

<!-- PROJECT-OWNED:BEGIN (custom note — kept verbatim) -->
| project row 1 |
| project row 2 |
<!-- PROJECT-OWNED:END -->

Tail OLD.
"""


# --- header split + bump ---------------------------------------------------------

def test_split_header_returns_header_and_body() -> None:
    header, body = sync.split_header(_TARGET, "t")
    assert header.endswith("-->\n")
    assert "CHANGE LOG" in header
    assert body.startswith("\n<!-- PROJECT-OWNED:BEGIN")


def test_split_header_missing_version_raises() -> None:
    with pytest.raises(sync.SyncError, match="no '<!-- VERSION"):
        sync.split_header("# no header\n", "t")


def test_bump_header_minor_bumps_and_logs() -> None:
    header, _ = sync.split_header(_TARGET, "t")
    out = sync.bump_header(header, _SET, _TODAY, "t")
    assert "<!-- VERSION: 1.4 -->" in out
    assert f"<!-- Last Updated: {_TODAY} -->" in out
    assert "v1.4 — 2026-08-16 — sync: Standard Set Version v1.5 applied" in out
    assert "v1.3 — 2026-07-01" in out  # prior log line kept


# --- merge -----------------------------------------------------------------------

def test_merge_preserves_owned_blocks_and_updates_suite_text() -> None:
    out = sync.merge_file(_TEMPLATE, _TARGET, _SET, _TODAY, "t")
    assert "# FILE — Acme (project-local)" in out          # owned block 1 kept
    assert "| project row 2 |" in out                      # owned block 2 kept
    assert "(custom note — kept verbatim)" in out          # target's own BEGIN comment kept
    assert "Suite paragraph NEW." in out                   # suite text updated
    assert "Tail NEW." in out
    assert "TEMPLATE banner." not in out                   # TEMPLATE-ONLY stripped
    assert "(fill me in)" not in out                       # template placeholder replaced
    assert "<!-- VERSION: 1.4 -->" in out                  # target's own header, bumped


def test_merge_is_idempotent() -> None:
    once = sync.merge_file(_TEMPLATE, _TARGET, _SET, _TODAY, "t")
    again = sync.merge_file(_TEMPLATE, once, _SET, _TODAY, "t")
    assert again == once  # body already matches -> returned unchanged, no re-bump


def test_merge_block_count_mismatch_raises() -> None:
    target = _TARGET.replace(
        "<!-- PROJECT-OWNED:BEGIN (custom note — kept verbatim) -->", ""
    ).replace("<!-- PROJECT-OWNED:END -->\n\nTail OLD.", "\nTail OLD.")
    with pytest.raises(sync.SyncError, match="count mismatch"):
        sync.merge_file(_TEMPLATE, target, _SET, _TODAY, "t")


def test_merge_unbalanced_markers_raise() -> None:
    broken = _TARGET.replace(
        "<!-- PROJECT-OWNED:END -->\n\nSuite paragraph OLD.", "\nSuite paragraph OLD."
    )
    with pytest.raises(sync.SyncError, match="BEGIN without END|END without BEGIN|nested"):
        sync.merge_file(_TEMPLATE, broken, _SET, _TODAY, "t")


# --- record ----------------------------------------------------------------------

def test_record_adoption_updates_bullets_row_and_header(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    _, target = make_suite_pair()
    text = (target / "docs" / "SET_VERSION_ADOPTED.md").read_text(encoding="utf-8")
    out = sync.record_adoption(text, _SET, _TODAY, "sva")
    assert "- **Standard Set Version:** v1.5 (synced from the vault by the engine" in out
    assert f"- **Adopted on:** {_TODAY} (synced)" in out
    assert "| v1.5 | 2026-08-16 | sync (engine):" in out
    assert "| v1.4 | 2026-07-01 | Initial bootstrap |" in out  # history kept below
    assert "<!-- VERSION: 1.1 -->" in out
    assert out.index("| v1.5 |") < out.index("| v1.4 |")       # newest row on top


def test_record_adoption_without_table_raises() -> None:
    text = (
        "<!-- VERSION: 1.0 -->\n<!--\nCHANGE LOG\nv1.0 — x.\n-->\n"
        "- **Standard Set Version:** v1.4\n"
    )
    with pytest.raises(sync.SyncError, match="backport-tracking table"):
        sync.record_adoption(text, _SET, _TODAY, "sva")


# --- plan / apply / render -------------------------------------------------------

def test_plan_target_covers_every_sync_map_file(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    vault, target = make_suite_pair()
    actions = sync.plan_target(vault, target, _SET, _TODAY)
    assert len(actions) == len(sync.SYNC_MAP)
    assert all(a.changed for a in actions)  # the fixture adopter is one Set Version behind
    modes = {a.target_rel: a.mode for a in actions}
    assert modes["CLAUDE.md"] == "merge"
    assert modes["archive/LESSONS.md"] == "replace"
    assert modes["docs/SET_VERSION_ADOPTED.md"] == "record"


def test_plan_target_missing_file_raises(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    vault, target = make_suite_pair()
    (target / "archive" / "LESSONS.md").unlink()
    with pytest.raises(sync.SyncError, match="target file missing: archive/LESSONS.md"):
        sync.plan_target(vault, target, _SET, _TODAY)


def test_apply_then_replan_is_all_up_to_date(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    vault, target = make_suite_pair()
    actions = sync.plan_target(vault, target, _SET, _TODAY)
    written = sync.apply_actions(target, actions)
    assert Path("CLAUDE.md") in written and Path("archive/LESSONS.md") in written
    replay = sync.plan_target(vault, target, _SET, _TODAY)
    assert not any(a.changed for a in replay)  # idempotence: second run writes nothing
    merged = (target / "CLAUDE.md").read_text(encoding="utf-8")
    assert "Acme CLI." in merged                      # owned block survived the real write
    assert "## 3. Rules NEW." in merged               # suite section updated
    replaced = (target / "docs" / "standards" / "PROJECT_STANDARDS.md").read_text(encoding="utf-8")
    assert replaced == (vault / "docs" / "standards" / "PROJECT_STANDARDS.md").read_text(
        encoding="utf-8"
    )


def test_apply_actions_skips_unchanged(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    vault, target = make_suite_pair()
    sync.apply_actions(target, sync.plan_target(vault, target, _SET, _TODAY))
    assert sync.apply_actions(target, sync.plan_target(vault, target, _SET, _TODAY)) == []


def test_render_plan_reports_and_diffs(
    make_suite_pair: Callable[..., tuple[Path, Path]],
) -> None:
    vault, target = make_suite_pair()
    actions = sync.plan_target(vault, target, _SET, _TODAY)
    text = sync.render_plan("acme", actions, show_diff=True)
    assert "[acme]" in text and "need sync" in text
    assert "merge   CLAUDE.md" in text
    assert "--- a/CLAUDE.md" in text                  # unified diff present under --diff
    sync.apply_actions(target, actions)
    done = sync.render_plan("acme", sync.plan_target(vault, target, _SET, _TODAY), show_diff=False)
    assert "up-to-date" in done
```

#### 5F2 — `tests/conftest.py` — full replacement (0.1 → 0.2)

````python
# ==============================================================
# VERSION: 0.2
# Shared pytest fixtures — synthetic vault + adopter-project trees.
#
# CHANGE LOG
# v0.2 — 2026-08-16 — PLAN-008 (sync): make_suite_pair factory — a full vault suite +
#                     converged adopter tree covering every SYNC_MAP mode (shared by
#                     test_sync + test_cli).
# v0.1 — 2026-06-16 13:01 — Initial: make_vault + make_project factories.
# ==============================================================
"""Fixtures that build minimal on-disk vault/project trees under tmp_path.

All three fixtures return factory callables. Tests annotate the injected
parameter as ``Callable[..., Path]`` so mypy --strict is satisfied without
importing anything from this module (no cross-test imports, no type: ignore).
"""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def make_vault(tmp_path: Path) -> Callable[..., Path]:
    """Factory: build a vault root with STANDARDS_INDEX.md at the given Set Version."""

    def _make(version: str = "1.1") -> Path:
        root = tmp_path / "vault"
        _write(
            root / "docs" / "standards" / "STANDARDS_INDEX.md",
            f"## 1. Standard Set Version (current)\n\n```\nStandard Set Version: v{version}\n```\n",
        )
        (root / "config").mkdir(parents=True, exist_ok=True)
        return root

    return _make


@pytest.fixture
def make_project(tmp_path: Path) -> Callable[..., Path]:
    """Factory: build an adopter tree; adopted=None omits SET_VERSION_ADOPTED.md."""

    def _make(name: str, adopted: str | None = "1.1", open_entries: int = 0) -> Path:
        proj = tmp_path / name
        if adopted is not None:
            _write(
                proj / "docs" / "SET_VERSION_ADOPTED.md",
                f"- **Standard Set Version:** v{adopted} (notes)\n",
            )
        if open_entries:
            body = "".join(
                f"## E{i + 1:03d} — title\n- Status:      open\n\n" for i in range(open_entries)
            )
            _write(proj / "docs" / "STANDARDS_LOG.md", body)
        return proj

    return _make


def _hdr(version: str) -> str:
    return (
        f"<!-- VERSION: {version} -->\n"
        "<!-- Last Updated: 2026-08-01 -->\n"
        "<!--\n"
        "CHANGE LOG\n"
        f"v{version} — 2026-08-01 — fixture.\n"
        "-->\n"
    )


_PO = "<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->"
_PO_END = "<!-- PROJECT-OWNED:END -->"
_TO = "<!-- TEMPLATE-ONLY:BEGIN (stripped at instantiation; sync never propagates this block) -->"
_TO_END = "<!-- TEMPLATE-ONLY:END -->"

_TOPICALS = (
    "PROJECT_STANDARDS.md",
    "PROMPT_STANDARDS.md",
    "MEMORY_PROTOCOL.md",
    "ENGINEERING_STANDARDS.md",
    "VALIDATION_STANDARDS.md",
    "CICD_STANDARDS.md",
)


def _mixed(header: str, banner: str | None, heading: str, suite: str, owned2: str | None) -> str:
    parts = [header, "\n"]
    if banner is not None:
        parts += [_TO, "\n", banner, "\n", _TO_END, "\n"]
    parts += [_PO, "\n", heading, "\n", _PO_END, "\n\n", suite, "\n"]
    if owned2 is not None:
        parts += ["\n", _PO, "\n", owned2, "\n", _PO_END, "\n"]
    return "".join(parts)


@pytest.fixture
def make_suite_pair(tmp_path: Path) -> Callable[..., tuple[Path, Path]]:
    """Factory: a vault (Set v1.5) + a converged adopter one Set Version behind.

    Covers every SYNC_MAP mode: 6 stale topical files + a stale archive LESSONS
    (replace), CLAUDE.md + both session files with PROJECT-OWNED customizations
    (merge), and a v1.4 SET_VERSION_ADOPTED.md with a backport table (record).
    """

    def _make() -> tuple[Path, Path]:
        vault = tmp_path / "svault"
        target = tmp_path / "starget"
        std = vault / "docs" / "standards"
        _write(
            std / "STANDARDS_INDEX.md",
            "## 1. Standard Set Version (current)\n\n```\nStandard Set Version: v1.5\n```\n",
        )
        (vault / "config").mkdir(parents=True, exist_ok=True)
        for name in _TOPICALS:
            _write(std / name, _hdr("1.1") + f"\n# {name}\n\nSuite text NEW.\n")
            _write(
                target / "docs" / "standards" / name,
                _hdr("1.0") + f"\n# {name}\n\nSuite text OLD.\n",
            )
        _write(std / "LESSONS.md", _hdr("1.0") + "\n# LESSONS\n\nLessons NEW.\n")
        _write(target / "archive" / "LESSONS.md", _hdr("1.0") + "\n# LESSONS\n\nLessons OLD.\n")
        _write(
            std / "CLAUDE.md",
            _mixed(
                _hdr("1.4"), None, "## 1. Context\n<fill-me>", "## 3. Rules NEW.", "## 14. <agent>"
            ),
        )
        _write(
            target / "CLAUDE.md",
            _mixed(
                _hdr("1.2"), None, "## 1. Context\nAcme CLI.", "## 3. Rules OLD.", "## 14. Stub."
            ),
        )
        for tpl in ("SESSION_OPENER.md", "SESSION_CLOSER.md"):
            _write(
                std / tpl,
                _mixed(
                    _hdr("1.5"),
                    f"# {tpl} (template)\n> TEMPLATE banner.",
                    f"# {tpl} <project>",
                    "Routine NEW.",
                    None,
                ),
            )
            _write(
                target / "docs" / tpl,
                _mixed(_hdr("1.1"), None, f"# {tpl} Acme (project-local)", "Routine OLD.", None),
            )
        _write(
            target / "docs" / "SET_VERSION_ADOPTED.md",
            _hdr("1.0")
            + "\n# Standard Set Version Adopted\n\n"
            "- **Standard Set Version:** v1.4 (notes)\n"
            "- **Adopted on:** 2026-07-01\n"
            "- **Source:** the vault\n\n"
            "| Set Version | Adopted on | Notes |\n"
            "|---|---|---|\n"
            "| v1.4 | 2026-07-01 | Initial bootstrap |\n",
        )
        return vault, target

    return _make


@pytest.fixture
def write_registry() -> Callable[..., Path]:
    """Factory: write config/projects.toml from (name, path) pairs; return its path."""

    def _write_registry(vault_root: Path, projects: list[tuple[str, Path]]) -> Path:
        body = "".join(
            f'[[project]]\nname = "{name}"\npath = "{path}"\n\n' for name, path in projects
        )
        registry = vault_root / "config" / "projects.toml"
        _write(registry, body)
        return registry

    return _write_registry
````

#### 5F3 — `tests/test_transport.py` — full replacement (0.1 → 0.2)

```python
# ==============================================================
# VERSION: 0.2
# Unit tests for the pluggable target transports (local | git | ssh).
#
# CHANGE LOG
# v0.2 — 2026-08-16 — PLAN-008: full=True sessions — git sparse set adds archive; ssh
#         materializes archive/ + root CLAUDE.md alongside docs/.
# v0.1 — 2026-06-20 — Initial: make_target dispatch + Local/Git/Ssh materialize/flush + _run errors.
# ==============================================================
"""Tests for standard_document_updater.transport."""
from __future__ import annotations

import subprocess
from collections.abc import Callable
from pathlib import Path

import pytest

from standard_document_updater import transport
from standard_document_updater.registry import Project


class _FakeProc:
    """Minimal stand-in for subprocess.CompletedProcess."""

    def __init__(self, returncode: int, stdout: str = "", stderr: str = "") -> None:
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def _capture(cmds: list[list[str]]) -> Callable[[list[str]], None]:
    """A drop-in for transport._run that records the argv it was called with."""

    def _fake(cmd: list[str]) -> None:
        cmds.append(cmd)

    return _fake


# --- make_target dispatch (QA I) -------------------------------------------------

def test_make_target_local() -> None:
    t = transport.make_target(Project(name="a", path=Path("/x")))
    assert isinstance(t, transport.LocalTarget)


def test_make_target_git() -> None:
    t = transport.make_target(Project(name="b", transport="git", git_url="git@h:r.git"))
    assert isinstance(t, transport.GitTarget)


def test_make_target_ssh() -> None:
    t = transport.make_target(Project(name="c", transport="ssh", ssh_host="h", ssh_path="/p"))
    assert isinstance(t, transport.SshTarget)


def test_make_target_unknown_raises() -> None:
    with pytest.raises(transport.TransportError, match="unknown transport"):
        transport.make_target(Project(name="d", transport="bogus"))


# --- LocalTarget (QA J) ----------------------------------------------------------

def test_local_session_yields_path_in_place(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    t = transport.make_target(Project(name="a", path=repo))
    with t.session() as root:
        assert root == repo  # in place; no temp dir
    # flush + dispose are inherited no-ops — calling flush must not error or touch the repo
    t.flush(repo, [Path("docs/x.md")], "msg")
    assert repo.exists()


def test_local_missing_path_raises(tmp_path: Path) -> None:
    t = transport.make_target(Project(name="a", path=tmp_path / "nope"))
    with pytest.raises(transport.TransportError, match="path not found"):
        with t.session():
            pass


# --- GitTarget read/write/flush (QA K, L) ---------------------------------------

def test_git_read_materialize_is_shallow_blobless_sparse(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(
        Project(name="b", transport="git", git_url="git@h:r.git", git_branch="main")
    )
    with t.session():
        pass
    assert cmds[0][:2] == ["git", "clone"]
    assert "--depth" in cmds[0] and "--filter=blob:none" in cmds[0]
    assert "--no-checkout" in cmds[0] and "--branch" in cmds[0]
    assert cmds[1][3:] == ["sparse-checkout", "set", "docs"]
    assert cmds[2][3] == "checkout"


def test_git_read_full_sparse_includes_archive(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(Project(name="b", transport="git", git_url="git@h:r.git"))
    with t.session(full=True):
        pass
    assert cmds[1][3:] == ["sparse-checkout", "set", "docs", "archive"]


def test_ssh_full_materializes_archive_and_root_claude(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(
        Project(name="c", transport="ssh", ssh_host="devbox", ssh_path="/home/me/repo/")
    )
    with t.session(full=True) as root:
        assert cmds[0][2] == "devbox:/home/me/repo/docs/"
        assert cmds[1][2] == "devbox:/home/me/repo/archive/"
        assert cmds[1][3] == f"{root / 'archive'}/"
        assert cmds[2][2] == "devbox:/home/me/repo/CLAUDE.md"
        assert cmds[2][3] == f"{root / 'CLAUDE.md'}"


def test_git_write_materialize_is_full_clone(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(Project(name="b", transport="git", git_url="u", git_branch="main"))
    with t.session(writable=True):
        pass
    assert len(cmds) == 1  # one full clone; no sparse-checkout/checkout
    assert cmds[0][:2] == ["git", "clone"]
    assert "--no-checkout" not in cmds[0] and "--filter=blob:none" not in cmds[0]


def test_git_flush_commits_and_pushes(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(Project(name="b", transport="git", git_url="u", git_branch="main"))
    t.flush(Path("/root"), [Path("docs/STANDARDS_LOG.md")], "msg")
    assert cmds[0] == ["git", "-C", "/root", "add", "docs/STANDARDS_LOG.md"]
    assert "commit" in cmds[1] and "user.name=Standard DocSet" in cmds[1]
    assert cmds[2] == ["git", "-C", "/root", "push", "origin", "HEAD:main"]


def test_git_flush_default_branch_refspec(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(Project(name="b", transport="git", git_url="u"))  # no branch
    t.flush(Path("/root"), [Path("docs/x.md")], "msg")
    assert cmds[2] == ["git", "-C", "/root", "push", "origin", "HEAD"]


def test_git_missing_url_raises() -> None:
    t = transport.make_target(Project(name="b", transport="git"))  # git_url defaults to None
    with pytest.raises(transport.TransportError, match="missing git_url"):
        with t.session():
            pass


# --- SshTarget materialize/flush (QA M) -----------------------------------------

def test_ssh_materialize_rsyncs_docs_down(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(
        Project(name="c", transport="ssh", ssh_host="devbox", ssh_path="/home/me/repo/")
    )
    with t.session() as root:
        assert cmds[0][:2] == ["rsync", "-az"]
        assert cmds[0][2] == "devbox:/home/me/repo/docs/"
        assert cmds[0][3] == f"{root / 'docs'}/"


def test_ssh_flush_rsyncs_each_changed_file_up(monkeypatch: pytest.MonkeyPatch) -> None:
    cmds: list[list[str]] = []
    monkeypatch.setattr(transport, "_run", _capture(cmds))
    t = transport.make_target(
        Project(name="c", transport="ssh", ssh_host="devbox", ssh_path="/home/me/repo")
    )
    t.flush(Path("/tmp/x"), [Path("docs/STANDARDS_LOG.md")], "msg")
    assert cmds[0][:2] == ["rsync", "-az"]
    assert cmds[0][2] == str(Path("/tmp/x") / "docs/STANDARDS_LOG.md")
    assert cmds[0][3] == "devbox:/home/me/repo/docs/STANDARDS_LOG.md"


def test_ssh_missing_endpoint_raises() -> None:
    t = transport.make_target(Project(name="c", transport="ssh", ssh_host="h"))  # ssh_path None
    with pytest.raises(transport.TransportError, match="missing ssh_host or ssh_path"):
        with t.session():
            pass


# --- _run error handling ---------------------------------------------------------

def test_run_raises_on_nonzero_exit(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake(*args: object, **kwargs: object) -> _FakeProc:
        return _FakeProc(1, stderr="boom")

    monkeypatch.setattr(subprocess, "run", fake)
    with pytest.raises(transport.TransportError, match="boom"):
        transport._run(["git", "status"])


def test_run_ok_on_zero_exit(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake(*args: object, **kwargs: object) -> _FakeProc:
        return _FakeProc(0)

    monkeypatch.setattr(subprocess, "run", fake)
    transport._run(["true"])  # must not raise


def test_run_raises_when_binary_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    def boom(*args: object, **kwargs: object) -> _FakeProc:
        raise OSError("not found")

    monkeypatch.setattr(subprocess, "run", boom)
    with pytest.raises(transport.TransportError, match="could not run"):
        transport._run(["nonexistent-binary-xyz"])
```

#### 5F4 — `tests/test_cli.py` — full replacement (0.4 → 0.5)

```python
# ==============================================================
# VERSION: 0.5
# End-to-end tests for the CLI (status / drift / harvest / integrate / sync).
#
# CHANGE LOG
# v0.5 — 2026-08-16 — PLAN-008: five sync tests — empty registry; dry-run writes nothing;
#         --write applies + idempotent second run; unknown --project errors; per-target
#         failure isolation (exit 1, healthy targets still synced).
# v0.4 — 2026-06-20 — Add transport-aware tests: status over a (mocked) git target computes a row;
#                     an unreachable git target is non-fatal; integrate --write to a local target
#                     writes through the new ExitStack/session path (PLAN-007).
# v0.3 — 2026-06-18 — Add 2 integrate tests (worksheet exit 0; --apply dry-run, no write).
# v0.2 — 2026-06-16 — Add 2 harvest tests (empty registry; one project, 2 open entries).
# v0.1 — 2026-06-16 13:01 — Initial: status table, drift exit codes, empty registry.
# ==============================================================
"""Tests for standard_document_updater.cli."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest

from standard_document_updater import transport
from standard_document_updater.cli import main

Make = Callable[..., Path]


def _write_git_registry(vault_root: Path, name: str = "beta", branch: str = "main") -> None:
    reg = vault_root / "config" / "projects.toml"
    reg.parent.mkdir(parents=True, exist_ok=True)
    reg.write_text(
        f'[[project]]\nname = "{name}"\ntransport = "git"\n'
        f'git_url = "git@h:{name}.git"\ngit_branch = "{branch}"\n',
        encoding="utf-8",
    )


def test_status_empty_registry_exit_zero(
    make_vault: Make, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    root = make_vault("1.1")
    write_registry(root, [])
    assert main(["--vault", str(root), "status"]) == 0
    assert "No projects registered" in capsys.readouterr().out


def test_status_lists_project_exit_zero(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted="1.0", open_entries=2)
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "status"]) == 0
    out = capsys.readouterr().out
    assert "alpha" in out and "behind" in out and "v1.0" in out


def test_drift_behind_exits_one(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted="1.0")
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "drift"]) == 1


def test_drift_all_current_exits_zero(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted="1.1")
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "drift"]) == 0
    assert "No drift" in capsys.readouterr().out


def test_drift_unknown_counts_as_drift(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted=None)
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "drift"]) == 1


def test_harvest_empty_registry_exit_zero(
    make_vault: Make, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    root = make_vault("1.1")
    write_registry(root, [])
    assert main(["--vault", str(root), "harvest"]) == 0
    assert "No open log entries across registered projects." in capsys.readouterr().out


def test_harvest_lists_open_entries_exit_zero(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", open_entries=2)
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "harvest"]) == 0
    out = capsys.readouterr().out
    assert "E001" in out and "E002" in out and "alpha" in out


def test_integrate_worksheet_exit_zero(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", open_entries=1)
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "integrate"]) == 0
    out = capsys.readouterr().out
    assert "[alpha] E001" in out and "current Set Version v1.1" in out


def test_integrate_apply_dry_run_exit_zero(
    make_vault: Make, make_project: Make, write_registry: Make, tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", open_entries=1)
    write_registry(root, [("alpha", proj)])
    log = proj / "docs" / "STANDARDS_LOG.md"
    before = log.read_text(encoding="utf-8")
    decisions = tmp_path / "decisions.toml"
    decisions.write_text(
        '[[rejected]]\nproject = "alpha"\nentry = "E001"\nreason = "n/a"\n',
        encoding="utf-8",
    )
    assert main(["--vault", str(root), "integrate", "--apply", str(decisions)]) == 0
    assert "DRY-RUN" in capsys.readouterr().out
    assert log.read_text(encoding="utf-8") == before


def test_integrate_apply_write_local_writes(
    make_vault: Make, make_project: Make, write_registry: Make, tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", open_entries=1)
    write_registry(root, [("alpha", proj)])
    log = proj / "docs" / "STANDARDS_LOG.md"
    decisions = tmp_path / "decisions.toml"
    decisions.write_text(
        '[[rejected]]\nproject = "alpha"\nentry = "E001"\nreason = "n/a"\n',
        encoding="utf-8",
    )
    assert main(["--vault", str(root), "integrate", "--apply", str(decisions), "--write"]) == 0
    assert "wrote" in capsys.readouterr().out
    assert "rejected — n/a" in log.read_text(encoding="utf-8")


def test_status_git_target_row_computed(
    make_vault: Make, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    _write_git_registry(root)

    def fake_run(cmd: list[str]) -> None:
        if cmd[1] == "clone":  # populate the materialization the read path would have fetched
            dest = Path(cmd[-1])
            (dest / "docs").mkdir(parents=True, exist_ok=True)
            (dest / "docs" / "SET_VERSION_ADOPTED.md").write_text(
                "- **Standard Set Version:** v1.0\n", encoding="utf-8"
            )
            (dest / "docs" / "STANDARDS_LOG.md").write_text("", encoding="utf-8")

    monkeypatch.setattr(transport, "_run", fake_run)
    assert main(["--vault", str(root), "status"]) == 0
    out = capsys.readouterr().out
    assert "beta" in out and "behind" in out and "git:git@h:beta.git@main" in out


def test_status_unreachable_git_target_is_nonfatal(
    make_vault: Make, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    _write_git_registry(root)

    def boom(cmd: list[str]) -> None:
        raise transport.TransportError("host unreachable")

    monkeypatch.setattr(transport, "_run", boom)
    assert main(["--vault", str(root), "status"]) == 0  # non-fatal for a read command
    out = capsys.readouterr().out
    assert "beta" in out and "unknown" in out


# --- sync (PLAN-008) -------------------------------------------------------------

MakePair = Callable[..., tuple[Path, Path]]


def test_sync_empty_registry_exit_zero(
    make_vault: Make, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    root = make_vault("1.1")
    write_registry(root, [])
    assert main(["--vault", str(root), "sync"]) == 0
    assert "No registered projects to sync" in capsys.readouterr().out


def test_sync_dry_run_reports_and_writes_nothing(
    make_suite_pair: MakePair, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("acme", target)])
    before = (target / "CLAUDE.md").read_text(encoding="utf-8")
    assert main(["--vault", str(vault), "sync"]) == 0
    out = capsys.readouterr().out
    assert "DRY-RUN" in out and "need sync" in out and "(dry-run — re-run with --write" in out
    assert (target / "CLAUDE.md").read_text(encoding="utf-8") == before


def test_sync_write_applies_and_second_run_is_up_to_date(
    make_suite_pair: MakePair, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("acme", target)])
    assert main(["--vault", str(vault), "sync", "--write"]) == 0
    assert "wrote + flushed" in capsys.readouterr().out
    merged = (target / "CLAUDE.md").read_text(encoding="utf-8")
    assert "Acme CLI." in merged and "## 3. Rules NEW." in merged
    sva = (target / "docs" / "SET_VERSION_ADOPTED.md").read_text(encoding="utf-8")
    assert "- **Standard Set Version:** v1.5 (synced from the vault by the engine" in sva
    assert main(["--vault", str(vault), "sync", "--write"]) == 0
    assert "up-to-date" in capsys.readouterr().out


def test_sync_unknown_project_filter_errors(
    make_suite_pair: MakePair, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("acme", target)])
    assert main(["--vault", str(vault), "sync", "--project", "nope"]) == 2
    assert "not in the registry: nope" in capsys.readouterr().err


def test_sync_per_target_failure_is_isolated_exit_one(
    make_suite_pair: MakePair, write_registry: Make, tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("ghost", tmp_path / "missing"), ("acme", target)])
    assert main(["--vault", str(vault), "sync", "--write"]) == 1
    captured = capsys.readouterr()
    assert "ghost" in captured.err and "1 target(s) FAILED" in captured.err
    assert "[acme]" in captured.out and "wrote + flushed" in captured.out
```

#### 5F5 — `tests/test_setversion.py` — full replacement (0.1 → 0.2)

```python
# ==============================================================
# VERSION: 0.2
# Unit tests for setversion parsers.
#
# CHANGE LOG
# v0.2 — 2026-08-16 — DD-1: pin the delegated semantics — Status must equal 'open'
#         (case-insensitive), not merely start with it.
# v0.1 — 2026-06-16 13:01 — Initial: version parsing + open-log counting.
# ==============================================================
"""Tests for standard_document_updater.setversion."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest

from standard_document_updater import setversion
from standard_document_updater.errors import ParseError


def test_parse_vault_version_reads_index(make_vault: Callable[..., Path]) -> None:
    root = make_vault("1.1")
    index = root / "docs" / "standards" / "STANDARDS_INDEX.md"
    assert setversion.parse_vault_version(index) == (1, 1)


def test_parse_adopted_version_reads_bold_line(make_project: Callable[..., Path]) -> None:
    proj = make_project("p", adopted="1.0")
    adopted = proj / "docs" / "SET_VERSION_ADOPTED.md"
    assert setversion.parse_adopted_version(adopted) == (1, 0)


def test_parse_version_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(ParseError):
        setversion.parse_vault_version(tmp_path / "nope.md")


def test_parse_version_no_line_raises(tmp_path: Path) -> None:
    bad = tmp_path / "x.md"
    bad.write_text("nothing here\n", encoding="utf-8")
    with pytest.raises(ParseError):
        setversion.parse_adopted_version(bad)


def test_count_open_log_entries_counts_only_open(tmp_path: Path) -> None:
    log = tmp_path / "STANDARDS_LOG.md"
    log.write_text(
        "## E001 — a\n- Status:      open\n\n"
        "## E002 — b\n- Status:      integrated → vault L050\n\n"
        "## E003 — c\n- Status:      open\n\n"
        "## E004 — d\n- Status:      rejected — not portable\n\n",
        encoding="utf-8",
    )
    assert setversion.count_open_log_entries(log) == 2


def test_count_open_log_entries_absent_file_is_zero(tmp_path: Path) -> None:
    assert setversion.count_open_log_entries(tmp_path / "missing.md") == 0


def test_count_open_log_entries_requires_exact_open(tmp_path: Path) -> None:
    log = tmp_path / "STANDARDS_LOG.md"
    log.write_text(
        "## E001 — a\n- Status:      open\n\n"
        "## E002 — b\n- Status:      opened by mistake\n\n"
        "## E003 — c\n- Status:      Open\n\n",
        encoding="utf-8",
    )
    # DD-1: delegated to logentry.is_open — exact 'open' (case-insensitive), not startswith
    assert setversion.count_open_log_entries(log) == 2
```


### 5G — Doc restructure (verbatim FIND → REPLACE; per Rule 7)

#### 5G-1 — `docs/standards/SESSION_OPENER.md` (1.5 → 1.6) — template top region

FIND (the H1 + TEMPLATE banner, immediately after the header comment):

```
# SESSION_OPENER.md — Mandatory session-start pre-flight (template)

> **This file is a TEMPLATE.** Adopters copy it to their project's `docs/SESSION_OPENER.md`, customize the placeholder sections per project, and add the binding rule to their repo-root `CLAUDE.md` (per template `CLAUDE.md` Rule 9 / § 3). Once instantiated, the project-local copy is BINDING for every Claude session in that repository.
```

REPLACE with:

```
<!-- TEMPLATE-ONLY:BEGIN (delivery-crate banner — deleted at instantiation; sync never propagates this block) -->
# SESSION_OPENER.md — Mandatory session-start pre-flight (template)

> **This file is a TEMPLATE.** Adopters copy it to their project's `docs/SESSION_OPENER.md`, customize the placeholder sections per project, and add the binding rule to their repo-root `CLAUDE.md` (per template `CLAUDE.md` Rule 9 / § 3). Once instantiated, the project-local copy is BINDING for every Claude session in that repository. At instantiation: delete this TEMPLATE-ONLY block (markers included) and fill in the PROJECT-OWNED heading block below.
<!-- TEMPLATE-ONLY:END -->
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# SESSION_OPENER.md — Mandatory session-start pre-flight (project-local)

> **This is the BINDING project-local instance** for `<project-name>`. Every Claude session in this repository MUST read this file and execute its § 1 pre-flight, then post the § 4 first-response output block BEFORE acting on the operator's first task (per `CLAUDE.md` Rule 9).
<!-- PROJECT-OWNED:END -->
```

Header: bump 1.5 → 1.6 + CHANGE-LOG line
`v1.6 — <date> — Standard Set Version v1.6 (PLAN-008 sync-enablement): TEMPLATE-ONLY banner block + PROJECT-OWNED instance-heading block, so section-merge sync never propagates template banners and preserves the adopter's heading.`

#### 5G-2 — `docs/standards/SESSION_CLOSER.md` (1.3 → 1.4) — template top region

FIND:

```
# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (template)

> **This file is a TEMPLATE.** Adopters copy it to their project's `docs/SESSION_CLOSER.md`, customize the placeholder sections per project (output-block specifics, project-specific failure-mode rows in § 2), and add the binding rule to their repo-root `CLAUDE.md` (per template `CLAUDE.md` Rule 12 / § 3). Once instantiated, the project-local copy is BINDING for every Claude session in that repository.
```

REPLACE with:

```
<!-- TEMPLATE-ONLY:BEGIN (delivery-crate banner — deleted at instantiation; sync never propagates this block) -->
# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (template)

> **This file is a TEMPLATE.** Adopters copy it to their project's `docs/SESSION_CLOSER.md`, customize the placeholder sections per project (output-block specifics, project-specific failure-mode rows in § 2), and add the binding rule to their repo-root `CLAUDE.md` (per template `CLAUDE.md` Rule 12 / § 3). Once instantiated, the project-local copy is BINDING for every Claude session in that repository. At instantiation: delete this TEMPLATE-ONLY block (markers included) and fill in the PROJECT-OWNED heading block below.
<!-- TEMPLATE-ONLY:END -->
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (project-local)

> **This is the BINDING project-local instance** for `<project-name>`. When the operator triggers a wrap-up, Claude MUST read this file and execute its § 1 routine, then post the § 4 output block BEFORE any farewell (per `CLAUDE.md` Rule 12).
<!-- PROJECT-OWNED:END -->
```

Header: bump 1.3 → 1.4 + the analogous CHANGE-LOG line.

#### 5G-3 — `docs/SESSION_OPENER.md` (1.6 → 1.7) — wrap this vault's instance heading

FIND:

```
# SESSION_OPENER.md — Mandatory session-start pre-flight (project-local)

> **This is the BINDING project-local instance** for `Standard DocSet`. Every Claude session in this repository MUST read this file and execute its § 1 pre-flight, then post the § 4 first-response output block BEFORE acting on the operator's first task (per `CLAUDE.md` Rule 9).
```

REPLACE with the same text wrapped in markers:

```
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# SESSION_OPENER.md — Mandatory session-start pre-flight (project-local)

> **This is the BINDING project-local instance** for `Standard DocSet`. Every Claude session in this repository MUST read this file and execute its § 1 pre-flight, then post the § 4 first-response output block BEFORE acting on the operator's first task (per `CLAUDE.md` Rule 9).
<!-- PROJECT-OWNED:END -->
```

Header: bump 1.6 → 1.7 + CHANGE-LOG line (`heading block wrapped in PROJECT-OWNED — reconciles with the v1.6 template structure; owned-block count now 3 = template's 3`).

#### 5G-4 — `docs/SESSION_CLOSER.md` (1.4 → 1.5) — same wrap

FIND:

```
# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (project-local)

> **This is the BINDING project-local instance** for `Standard DocSet`. When the operator triggers a wrap-up, Claude MUST read this file and execute its § 1 routine, then post the § 4 output block BEFORE any farewell (per `CLAUDE.md` Rule 12).
```

REPLACE with the same text wrapped in `<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->` /
`<!-- PROJECT-OWNED:END -->` (exactly as 5G-3). Header: bump 1.4 → 1.5 + the analogous line
(owned-block count now 2 = template's 2).

#### 5G-5 — `docs/standards/CLAUDE.md` (1.4 → 1.5) — § 14 marker stub-keep wording

FIND:

```
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) — single-agent adopters delete this entire § 14 block -->
```

REPLACE with:

```
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) — single-agent adopters replace the § 14 body with a "NOT IN USE" stub INSIDE this block; keep the markers (sync matches blocks by position) -->
```

Header: bump 1.4 → 1.5 + CHANGE-LOG line (`§ 14 marker comment: stub-keep wording — deleting the
block would break sync's ordinal block matching; aligns with SETUP step 4's stub guidance`).

#### 5G-6 — `docs/standards/SETUP.md` (1.5 → 1.6) — instantiation wording

FIND:

```
   - Instantiate project-local TARGET/docs/SESSION_OPENER.md and TARGET/docs/SESSION_CLOSER.md from the
     templates (drop the "TEMPLATE" banner; customize §§ 2–3 for this project: branch name, the
     environment/registry mapping, failure-mode rows; no remote rows if there's no remote infra).
```

REPLACE with:

```
   - Instantiate project-local TARGET/docs/SESSION_OPENER.md and TARGET/docs/SESSION_CLOSER.md from the
     templates: delete the TEMPLATE-ONLY block (markers included); fill the PROJECT-OWNED heading block
     with this project's name; customize the PROJECT-OWNED blocks (§ 2 environment/registry mapping,
     § 3.2 project rows — branch name, no remote rows if there's no remote infra). § 3.1 (the universal
     catalog) stays suite-owned VERBATIM — project-specific patterns + N/A annotations go in § 3.2, so
     a future `sync` can update § 3.1. Keep every PROJECT-OWNED marker.
```

Plus the L053 parity retarget: every live `v1.5` suite reference outside CHANGE LOGs → `v1.6`
(QA-F greps the gate). Header bump + CHANGE-LOG line.

#### 5G-7 — `docs/standards/NEW_PROJECT_BOOTSTRAP.md` (1.5 → 1.6) — same, long-form

FIND:

```
Then edit `docs/SESSION_OPENER.md` and `docs/SESSION_CLOSER.md`: drop the "(template)" banner, and
customize §§ 2–3 for this project — the branch name, the environment/registry mapping, the failure-mode
rows (drop the remote-host rows if there's no remote infra). Keep the `PROJECT-OWNED` markers so a future
`sync` preserves your customizations.
```

REPLACE with:

```
Then edit `docs/SESSION_OPENER.md` and `docs/SESSION_CLOSER.md`: delete the TEMPLATE-ONLY block (markers
included); fill the PROJECT-OWNED heading block with this project's name; customize the PROJECT-OWNED
blocks — § 2 environment/registry mapping and § 3.2 project rows (branch name; no remote-host rows if
there's no remote infra). § 3.1 (the universal catalog) stays suite-owned VERBATIM — project-specific
patterns + N/A annotations belong in § 3.2, so a future `sync` can update § 3.1. Keep every
`PROJECT-OWNED` marker so sync preserves your customizations.
```

Plus the same live v1.5 → v1.6 retarget. Header bump + CHANGE-LOG line.

### 5H — Release mechanics (mechanical rules, per the v1.4/v1.5 precedent)

1. `docs/standards/STANDARDS_INDEX.md` 1.5 → 1.6: § 1 block (Set v1.6, released <date>; baseline +=
   "+ sync-enablement markers (v1.6)"; adopter contract counts UNCHANGED — 15 rules / 67 lessons);
   § 3 caption → v1.6 + cells for the five touched suite files (CLAUDE.md 1.5, SESSION_OPENER 1.6,
   SESSION_CLOSER 1.4, SETUP 1.6, NEW_PROJECT_BOOTSTRAP 1.6, STANDARDS_INDEX 1.6); § 6 v1.6 history
   entry (additive Minor: TEMPLATE-ONLY convention + instance-heading PROJECT-OWNED blocks + § 14
   stub-keep wording; the `sync` engine ships; adopters may stay on v1.5 — pre-v1.6 instances lack
   the heading wrap and will count-mismatch on their FIRST sync, by design: wrap once by hand or via
   adopt-mode, then sync forever).
2. `docs/SET_VERSION_ADOPTED.md` 1.6 → 1.7: adopt v1.6 same-commit; backport row; counts unchanged.
3. `docs/architecture.md` 0.9 → 0.10 (§ 4 drift rule — same commit as the engine change): § 7 adds
   the TEMPLATE-ONLY convention + ordinal-matching + stub-keep note; § 8 `sync` row → implemented ✅
   + a behavior note (dry-run default; --write / --project / --diff; per-target isolation exit 1;
   manifest note; SVA record update); § 8 transport paragraph += full-footprint sessions (DD-B);
   § 10 Slice 5 ✅; § 11 records the D8/DD decisions as DECIDED.
4. `docs/documents_manifest.md` 2.16 → 2.17: register `sync.py` + `test_sync.py` (appended entries,
   Engine quick-index range extended); bump touched cells (engine: __init__ 0.5, cli 0.5, setversion
   0.2, transport 0.2; tests: conftest 0.2, test_setversion 0.2, test_cli 0.5, test_transport 0.2;
   docs: both templates, both instances, template CLAUDE.md, INDEX, SVA, SETUP, NPB, architecture,
   folder_structure); quick-index suite caption → Set v1.6; PLAN-008 rows → 1.0/CLOSED; self-row +
   header (grep the stamps — L063).
5. `docs/folder_structure.md` 0.13: tree lines for `sync.py` + `test_sync.py`; suite caption v1.6.
6. `CHANGELOG.md`: top entry — Set v1.6 + engine Slice 5, with the § 8 QA list as the Rule 11 record.
7. This plan + `PLAN-008_tracker.md` → 1.0 / CLOSED same commit (§ 7 rows 24–25).

## 6. Spec update map

| Artifact | § 5 block | Change class |
|---|---|---|
| `sync.py` + `test_sync.py` | 5A, 5F1 | new engine module + tests |
| `transport.py` / `cli.py` / `setversion.py` / `__init__.py` | 5B–5E | engine edits (full-file replacement) |
| `conftest.py` + 3 extended test files | 5F2–5F5 | test support |
| Both session templates + both vault instances + template CLAUDE.md | 5G-1…5G-5 | Set v1.6 marker enablement |
| SETUP + NPB | 5G-6, 5G-7 | instantiation wording + L053 parity |
| INDEX, SVA, architecture, manifest, folder, CHANGELOG, plan+tracker | 5H | release cascade |

## 7. Phase-3 ALLOWLIST (the enumeration IS the count — 25 files)

1. `src/standard_document_updater/sync.py` (NEW) · 2. `src/standard_document_updater/transport.py` ·
3. `src/standard_document_updater/cli.py` · 4. `src/standard_document_updater/setversion.py` ·
5. `src/standard_document_updater/__init__.py` · 6. `tests/test_sync.py` (NEW) ·
7. `tests/conftest.py` · 8. `tests/test_transport.py` · 9. `tests/test_cli.py` ·
10. `tests/test_setversion.py` · 11. `docs/standards/SESSION_OPENER.md` ·
12. `docs/standards/SESSION_CLOSER.md` · 13. `docs/SESSION_OPENER.md` · 14. `docs/SESSION_CLOSER.md` ·
15. `docs/standards/CLAUDE.md` · 16. `docs/standards/STANDARDS_INDEX.md` ·
17. `docs/SET_VERSION_ADOPTED.md` · 18. `docs/standards/SETUP.md` ·
19. `docs/standards/NEW_PROJECT_BOOTSTRAP.md` · 20. `docs/architecture.md` ·
21. `docs/documents_manifest.md` · 22. `docs/folder_structure.md` · 23. `CHANGELOG.md` ·
24. `docs/Plans/PLAN-008_sync.md` (→ 1.0/CLOSED) · 25. `docs/Plans/PLAN-008_tracker.md` (→ 1.0/CLOSED)

(`config/projects.toml` is deliberately NOT touched.)

## 8. Validation gate (Phase 4 — QA scenarios per Rule 11; C/D are the Rule 15 feature-ON half)

| ID | Verify | How | Pass |
|---|---|---|---|
| A | tools at ship indentation | `.venv/bin/ruff check src tests`; `MYPYPATH=src .venv/bin/python -m mypy`; full pytest | all clean; 110 tests pass |
| B | sync unit behavior | `tests/test_sync.py` (14 cases: header split/bump, TEMPLATE-ONLY strip, merge + idempotence + mismatch/unbalanced errors, record, plan/apply/render) | green |
| C | CLI feature-ON, local transport | the 5 `test_cli.py` sync cases + a manual run: scratch adopter fixture + temp registry → `sync` (dry-run) → `sync --write` → `sync --write` again | dry-run writes nothing; write merges/replaces/records; owned blocks byte-preserved; second run "up-to-date" |
| D | git transport feature-ON vs LOCAL bare remote | script: bare repo ← push converged adopter tree; register `transport="git"`, `git_url=<path>`; `sync --write`; fresh clone | pushed commit present ("Standard DocSet: sync to Standard Set Version …"); merged CLAUDE.md preserves owned blocks; SVA row added |
| E | ssh path | **operator-waived** to the post-registration live smoke (Rule 15 waiver recorded in tracker; pairs with PLAN-007 QA K–N) | waiver recorded |
| F | v1.6 stamp/parity greps (L063/L053) | INDEX § 1/§ 3/§ 6; SVA; no live v1.5 refs outside CHANGE LOGs in SETUP/NPB; manifest header = self-row | all stamps equal the new values |
| G | marker integrity | template owned-block counts == instance counts (opener 3/3, closer 2/2, CLAUDE 4/4); TEMPLATE-ONLY balanced; grep both marker forms | exact |
| H | governance | both Rule-2 scripts | exit 0 |
| I | domain-neutral zero-hit | grep the § 5G new/changed text (diff added lines) with the standing domain pattern | 0 hits |
| J | manifest completeness | new files registered; folder_structure matches tree | consistent |

## 9. Operator approval decision point (Phase 2)

- **APPROVE D8.A** — implement § 5 as specified (recommended). Includes the two design decisions:
  **D1** = TEMPLATE-ONLY markers + instance-heading PROJECT-OWNED blocks (Set v1.6) — without them,
  section-merge would re-insert template banners into every adopter and clobber instance headings;
  **D2** = § 3.1 (universal failure-mode catalog) stays suite-owned — adopter-specific rows/N-A
  annotations live in § 3.2 only, so sync can deliver new universal rows (the point of the loop).
- **D8.B** — engine only, defer the doc/marker changes (NOT recommended: `sync` would ship unusable
  for the three mixed files — template banners would land in adopters on every merge).
- **D8.C** — request changes (name them).

## 10. Rollback path

Single commit → `git revert` restores everything (engine files, tests, docs); no real target repo is
written during this plan (empty registry; QA targets are tmp fixtures + a scratch bare repo that dies
with the session). A future bad `sync --write` against a real target is recoverable target-side:
git transport = revert the sync commit; local/ssh = restore from that project's own VCS/backup — and
dry-run-first remains the operating procedure.

## 11. Known risks

| # | Risk | Mitigation | Status |
|---|---|---|---|
| R1 | An adopter deleted a PROJECT-OWNED block (old "delete § 14" guidance) → ordinal matching breaks | strict count check fails that FILE loudly, nothing written; 5G-5 fixes the guidance (stub-keep); legacy layouts reconcile via PLAN-011 adopt-mode | mitigated |
| R2 | ssh sync path unverified live | QA-E waiver → post-registration live smoke; the transform + flush logic is shared with the proven git/local paths | waived (operator) |
| R3 | SETUP/NPB parity drift vs the new template structure (L053) | 5G-6/5G-7 ride the same commit; QA-F greps | mitigated |
| R4 | Sync normalizes suite-owned § 3.1 rows in adopters (loses in-table customizations) | by design (D2); instantiation wording now routes customizations to § 3.2; documented in § 6 history entry | documented |
| R5 | `date.today()` stamps machine-local dates into targets | acceptable (matches operator practice); tests inject fixed dates for determinism | documented |
| R6 | Pre-v1.6 adopters (none registered yet) lack the heading wrap → first sync count-mismatches | expected + loud, not silent; § 6 history entry documents the one-time wrap; PLAN-011 automates it | documented |

## 12. Acceptance criteria

- `sync` ships as the fifth subcommand: dry-run default, `--write`/`--project`/`--diff`; per-target
  isolation with exit 1 on any failure; per-file validate-all-before-write inside a target.
- Merge preserves every PROJECT-OWNED block byte-for-byte (incl. BEGIN-comment text); replace makes
  suite-owned files byte-identical to the vault; record updates SVA bullets + newest-first row;
  second run is all up-to-date (idempotence).
- Full-footprint sessions land (DD-B); existing commands' transport behavior unchanged (full=False).
- DD-1 folded; the delegated semantics pinned by test.
- Set v1.6 released: 5G marker/wording changes + 5H cascade; counts stay 15/67; QA F/G/I clean.
- QA A–D + F–J pass; E waiver recorded; governance exit 0; single commit; plan + tracker → 1.0/CLOSED
  same commit; `config/projects.toml` untouched.
