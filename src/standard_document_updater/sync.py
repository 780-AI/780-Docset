# ==============================================================
# VERSION: 0.4
# Section-aware suite propagation (`sync`): replace | merge | record per file.
#
# CHANGE LOG
# v0.4 — 2026-10-05 — PLAN-016: handoff_write_count — how many engine writes an un-landed
#         handoff records (the fleet view's handoff_pending column); reuses _prior_records.
# v0.3 — 2026-10-03 — PLAN-013: handoffs ACCUMULATE (an un-landed handoff's write records are
#         kept and the new write appended as the next record) + newest_stamp / check_clock —
#         the floor guard that refuses an engine write when the local clock is behind the
#         target's newest stamp (L079). Phase 3 D2 fix: the § 2 anchor is found from the
#         end (rfind), so a fenced unrecognized handoff survives later writes intact.
# v0.2 — 2026-09-05 — PLAN-012: HANDOFF_REL + render_handoff — EVERY engine write into a target
#         (sync --write AND integrate write-back) leaves a handoff report so the target's next
#         session finds engine-landed changes explained.
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


HANDOFF_REL = Path("docs/SYNC_HANDOFF.md")

_HANDOFF_S1 = "## 1. What the engine did\n"
_HANDOFF_S2 = "## 2. What this project's next session must do"
_WRITE_HEADING_RE = re.compile(r"^### Write \d+", re.MULTILINE)
_PROJECT_LINE_RE = re.compile(r"^- \*\*Project:\*\*[^\n]*\n", re.MULTILINE)


def _prior_records(existing: str) -> tuple[str, int]:
    """Write records kept verbatim from an un-landed handoff, plus how many there are.

    PLAN-013: a second engine write before the target lands the first must not
    erase the first write's explanation. Three shapes: the accumulating format
    (`### Write N` records), the single-write PLAN-012 format (wrapped as one
    record), and anything else (kept verbatim in a fence — nothing is lost).
    """
    start = existing.find(_HANDOFF_S1)
    end = existing.rfind(_HANDOFF_S2)  # the engine's own § 2 is always last
    if start == -1 or end < start:
        fenced = f"````text\n{existing.rstrip()}\n````"
        return f"### Write 1 — earlier handoff (unrecognized format, kept verbatim)\n\n{fenced}", 1
    body = _PROJECT_LINE_RE.sub("", existing[start + len(_HANDOFF_S1) : end], count=1).strip()
    if not body:
        return "", 0
    count = len(_WRITE_HEADING_RE.findall(body))
    if count:
        return body, count
    return f"### Write 1 — earlier engine write\n\n{body}", 1


def render_handoff(
    project_name: str,
    operation: str,
    set_version: str,
    today: str,
    files: list[tuple[str, str]],
    existing: str | None = None,
) -> str:
    """The handoff report every engine write leaves in the target (PLAN-012).

    Written on every write — `sync --write` and the integrate write-back — so
    the target's NEXT session finds engine-landed changes explained: what was
    written, by which operation and vault release, and the residual bookkeeping
    the engine deliberately leaves to the target (manifest cells, CHANGELOG
    entry, the landing commit). The target session deletes the file in the
    commit that lands the changes. PLAN-013: when the target still holds an
    un-landed handoff (`existing`), its write records are kept and this write is
    appended as the next record — every write since the last landing stays listed.
    """
    prior, count = _prior_records(existing) if existing is not None else ("", 0)
    lines = [
        "# SYNC HANDOFF — engine-written changes landed in this repository",
        "",
        "> **READ ME FIRST.** The Standard DocSet engine wrote the files below directly",
        "> into this working tree. They are NOT unexplained local edits. Land them per § 2,",
        "> then DELETE this file in that same commit. If several writes are listed, land them",
        "> ALL in that one commit.",
        "",
        "## 1. What the engine did",
        "",
        f"- **Project:** {project_name}",
        "",
    ]
    if prior:
        lines += [prior, ""]
    lines += [
        f"### Write {count + 1}",
        "",
        f"- **Operation:** {operation}",
        f"- **Vault Standard Set Version:** {set_version}",
        f"- **Run date:** {today} (stamped by the curator machine's clock — the engine refuses",
        "  to stamp behind this repository's newest stamp; if ordering still looks wrong",
        "  against local history, trust an external time authority)",
        "- **Files written (suite-owned sections updated; PROJECT-OWNED blocks preserved):**",
    ]
    for rel, mode in files:
        lines.append(f"  - `{rel}` ({mode})")
    lines += [
        "",
        "## 2. What this project's next session must do (the engine does NOT do these)",
        "",
        "1. Review the diffs (`git diff`) against EVERY file list above. Suite files modified but",
        "   listed in no record come from engine writes made before handoffs accumulated —",
        "   review them against the vault and land them in the same commit.",
        "2. Reconcile `docs/documents_manifest.md` version cells for the files above (skip any",
        "   whose header version did not move).",
        "3. Add a CHANGELOG entry recording the engine write (operation + file list).",
        "4. Commit the engine-written files + bookkeeping together — and **delete this handoff",
        "   file in that commit** (done = deleted).",
        "5. Do NOT add this file to the project's manifest — it is engine-transient (Rule 8",
        "   exempt by design); it must never survive a landing commit.",
        "6. New lessons/observations still land ONLY as `E0NN` entries in",
        "   `docs/STANDARDS_LOG.md` — never in engine-owned files.",
        "",
        "*Engine-generated on every engine write; a later write before landing appends to it.*",
        "",
    ]
    return "\n".join(lines)


def handoff_write_count(text: str) -> int:
    """How many engine writes an un-landed handoff records (PLAN-016 fleet view).

    Reuses the accumulation parser, so the count is the record number the next write
    would append after: N for `### Write N` records, 1 for a pre-accumulation or an
    unrecognized handoff, 0 for one whose § 1 is empty.
    """
    return _prior_records(text)[1]


_STAMP_RES = (
    re.compile(r"<!-- Last Updated: (\d{4}-\d{2}-\d{2}) -->"),
    re.compile(r"^v\d+\.\d+ — (\d{4}-\d{2}-\d{2}) — ", re.MULTILINE),
)
_STAMPED_RELS = (*(item.target_rel for item in SYNC_MAP), "docs/STANDARDS_LOG.md")


def newest_stamp(target_root: Path) -> str | None:
    """Newest header / CHANGE LOG date (ISO text) in the target's engine-touched files, or None.

    PLAN-013 (L079): the floor the local clock must not be behind before any
    engine write stamps dates into this target. Only stamp positions count
    (`Last Updated` headers + `vX.Y — YYYY-MM-DD — ` change-log lines), never
    dates quoted in prose.
    """
    newest: str | None = None
    for rel in _STAMPED_RELS:
        path = target_root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in _STAMP_RES:
            for match in pattern.finditer(text):
                if newest is None or match.group(1) > newest:
                    newest = match.group(1)
    return newest


def check_clock(project_name: str, today: str, floor: str | None) -> None:
    """Refuse an engine write when the local clock is behind the target's newest stamp (L079)."""
    if floor is not None and today < floor:
        raise SyncError(
            f"{project_name}: refusing to write — the local clock reads {today} but this target "
            f"already carries a stamp dated {floor} (the clock is behind, L079). Verify the "
            "clock against an external time authority and fix it; if the target's stamp is the "
            "wrong one, correct it there (PROJECT_STANDARDS § 5.6) and re-run."
        )
