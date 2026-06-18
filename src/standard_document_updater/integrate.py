# ==============================================================
# VERSION: 0.1
# Integration worksheet + status write-back (the deterministic half of `integrate`).
#
# CHANGE LOG
# v0.1 — 2026-06-18 — Initial: Area routing, next-L0NN, worksheet, decisions parse, write-back.
# ==============================================================
"""The deterministic spine of `integrate` (architecture § 6c).

A1 division of labor: this module does only the mechanical parts — collect open
entries, propose the next canonical L0NN, route each entry's Area to a topical
file, and (operator-gated) write the Status line back into each project's log.
The genericization, the L0NN lesson prose, and the vault edits (LESSONS, topical
file, Set Version) are authored by Claude in-session under the § 15 flow; this
module never calls a model and never edits the vault.

Read-only by default. The write-back re-reads each target log immediately before
writing (docs/architecture.md § 9) and rewrites only the matching Status line.
"""
from __future__ import annotations

import re
import tomllib
from dataclasses import dataclass
from pathlib import Path

from standard_document_updater.errors import StandardDocSetError
from standard_document_updater.harvest import OpenItem

# Area (controlled vocab from STANDARDS_LOG) -> destination doc under docs/standards/.
_AREA_TO_TOPICAL: dict[str, str] = {
    "engineering": "ENGINEERING_STANDARDS.md",
    "cicd": "CICD_STANDARDS.md",
    "validation": "VALIDATION_STANDARDS.md",
    "project": "PROJECT_STANDARDS.md",
    "prompt": "PROMPT_STANDARDS.md",
    "memory": "MEMORY_PROTOCOL.md",
    "governance": "CLAUDE.md",
}
_DEFAULT_TOPICAL = "PROJECT_STANDARDS.md"

_LESSON_ID_RE = re.compile(r"^###\s+L(\d+)\b", re.MULTILINE)
# A Status field line in a STANDARDS_LOG.md entry (leading "-", any spacing).
_STATUS_LINE_RE = re.compile(r"^(?P<prefix>-\s*Status:\s*).*$", re.MULTILINE)
_HEADING_RE = re.compile(r"^##[ \t]+(E\d+)\b", re.MULTILINE)


class IntegrateError(StandardDocSetError):
    """A decisions file is malformed, or a write-back target entry cannot be resolved."""


@dataclass(frozen=True)
class WorksheetRow:
    """One open entry, enriched with the deterministic integration proposals."""

    project_name: str
    entry_id: str
    area: str
    topical: str          # routed destination doc
    routed: bool          # False when Area was unknown/empty (catch-all used)
    title: str
    context: str
    learned: str
    suggested: str


def route_area(area: str) -> tuple[str, bool]:
    """Map an entry Area to (destination doc, routed?). Unknown/empty -> catch-all."""
    key = area.lower().strip()
    if key in _AREA_TO_TOPICAL:
        return _AREA_TO_TOPICAL[key], True
    return _DEFAULT_TOPICAL, False


def next_lesson_id(lessons_path: Path) -> str:
    """Next canonical lesson id (max existing L#### + 1), e.g. 'L051'. 'L001' if none/absent."""
    if not lessons_path.exists():
        return "L001"
    text = lessons_path.read_text(encoding="utf-8")
    nums = [int(m.group(1)) for m in _LESSON_ID_RE.finditer(text)]
    return f"L{(max(nums) + 1) if nums else 1:03d}"


def build_rows(items: list[OpenItem]) -> list[WorksheetRow]:
    """Enrich open items with Area routing (pure; deterministic order preserved)."""
    rows: list[WorksheetRow] = []
    for item in items:
        topical, routed = route_area(item.entry.area)
        rows.append(
            WorksheetRow(
                project_name=item.project_name,
                entry_id=item.entry.entry_id,
                area=item.entry.area or "(unspecified)",
                topical=topical,
                routed=routed,
                title=item.entry.title,
                context=item.entry.context,
                learned=item.entry.learned,
                suggested=item.entry.suggested,
            )
        )
    return rows


def render_worksheet(rows: list[WorksheetRow], proposed_lesson: str, set_version: str) -> str:
    """Render the integration worksheet (deterministic). Read-only; Claude authors from it."""
    if not rows:
        return "No open entries to integrate. (Run `harvest` to review, or check the registry.)"
    next_n = int(proposed_lesson[1:])
    lines = [
        f"Integrate — {len(rows)} open entr{'y' if len(rows) == 1 else 'ies'}; "
        f"vault next lesson {proposed_lesson}; current Set Version {set_version}.",
        "",
        "For each entry you (Claude) decide integrate/reject, then IN-SESSION "
        "(under § 15): genericize (no project names), write the lesson to "
        "docs/standards/LESSONS.md, update the routed topical file, bump per-file "
        "VERSION + the Set Version. Then record dispositions in a decisions TOML "
        "and run `integrate --apply <file>` to write the Status lines back.",
    ]
    for i, row in enumerate(rows):
        lesson = f"L{next_n + i:03d}"
        flag = "" if row.routed else "   ⚠ unrouted (Area unknown → default; route by hand)"
        lines += [
            "",
            f"[{row.project_name}] {row.entry_id} — {row.title}",
            f"    area:     {row.area} -> {row.topical}{flag}",
            f"    proposed: {lesson}  (sequential; final id is assigned when you write the lesson)",
            f"    context:  {row.context}",
            f"    learned:  {row.learned}",
            f"    suggested:{row.suggested}",
        ]
    return "\n".join(lines)


@dataclass(frozen=True)
class Disposition:
    """One write-back instruction parsed from the decisions TOML."""

    project: str
    entry: str
    status_line: str   # the full replacement text for the Status: value


def parse_decisions(decisions_path: Path) -> list[Disposition]:
    """Parse the decisions TOML into Status-line write-back instructions.

    Raises IntegrateError on a missing file, bad TOML, or a row missing required keys.
    """
    if not decisions_path.exists():
        raise IntegrateError(f"decisions file not found: {decisions_path}")
    try:
        data = tomllib.loads(decisions_path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise IntegrateError(f"could not parse decisions file {decisions_path}: {exc}") from exc

    out: list[Disposition] = []
    for row in data.get("integrated", []):
        for key in ("project", "entry", "lesson", "topical", "set_version"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise IntegrateError(f"integrated row missing '{key}': {row}")
        status = (
            f"integrated → vault {row['lesson']} "
            f"({row['topical']}, Set Version {row['set_version']})"
        )
        out.append(Disposition(row["project"], row["entry"], status))
    for row in data.get("rejected", []):
        for key in ("project", "entry", "reason"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise IntegrateError(f"rejected row missing '{key}': {row}")
        out.append(Disposition(row["project"], row["entry"], f"rejected — {row['reason']}"))
    if not out:
        raise IntegrateError("decisions file has no [[integrated]] or [[rejected]] rows")
    return out


def _rewrite_status(text: str, entry_id: str, new_status: str) -> str:
    """Return `text` with the Status line of `entry_id` replaced. Raises if not found."""
    headings = list(_HEADING_RE.finditer(text))
    for i, h in enumerate(headings):
        if h.group(1) != entry_id:
            continue
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        block = text[h.start() : end]
        new_block, n = _STATUS_LINE_RE.subn(
            lambda m: f"{m.group('prefix')}{new_status}", block, count=1
        )
        if n == 0:
            raise IntegrateError(f"entry {entry_id}: no Status line found")
        return text[: h.start()] + new_block + text[end:]
    raise IntegrateError(f"entry {entry_id} not found in log")


def apply_writeback(
    dispositions: list[Disposition], log_path_for: dict[str, Path], *, write: bool
) -> list[str]:
    """Apply (or dry-run) the Status write-backs. Re-reads each log immediately (§ 9).

    Returns a human-readable report. Raises IntegrateError (before any write) if a
    target project is unknown or an entry/Status line cannot be resolved.
    """
    # Resolve + validate everything first — no partial writes.
    planned: list[tuple[Path, str, str, str]] = []  # (path, entry, new_status, project)
    for d in dispositions:
        log_path = log_path_for.get(d.project)
        if log_path is None:
            raise IntegrateError(f"project not in registry: {d.project}")
        if not log_path.exists():
            raise IntegrateError(f"log not found for {d.project}: {log_path}")
        text = log_path.read_text(encoding="utf-8")
        _rewrite_status(text, d.entry, d.status_line)  # validate (raises if unresolvable)
        planned.append((log_path, d.entry, d.status_line, d.project))

    report: list[str] = []
    for log_path, entry, new_status, project in planned:
        if write:
            text = log_path.read_text(encoding="utf-8")  # re-read immediately before write (§ 9)
            log_path.write_text(_rewrite_status(text, entry, new_status), encoding="utf-8")
            report.append(f"wrote  [{project}] {entry}: Status -> {new_status}")
        else:
            report.append(f"DRY-RUN [{project}] {entry}: Status -> {new_status}")
    if not write:
        report.append("\n(dry-run — re-run with --write to apply)")
    return report
