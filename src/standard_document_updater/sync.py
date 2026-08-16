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
