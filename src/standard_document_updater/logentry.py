# ==============================================================
# VERSION: 0.1
# Parse a STANDARDS_LOG.md into structured experience entries.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: LogEntry dataclass + parse_log (full-entry parser).
# ==============================================================
"""Parse a project's experiences log (docs/STANDARDS_LOG.md) into entries.

Re-reads the file on every call (never cached) per docs/architecture.md § 9.
The entry schema is fixed by docs/standards/STANDARDS_LOG.md:

    ## E001 — <title>
    - Date:        YYYY-MM-DD
    - Area:        <engineering | cicd | validation | project | prompt | memory | governance>
    - Status:      open                 # open | integrated | rejected
    - Context:     <free text, may span multiple indented lines>
    - Learned:     <free text>
    - Suggested:   <free text>
    - Portability: <project-specific | general>

Controlled-vocabulary fields (area / status / portability) keep only their
first whitespace-delimited token, so a trailing "# comment" or a status
write-back such as "integrated -> vault L050 (...)" reduces to "integrated".
Free-text fields (context / learned / suggested) keep continuation lines,
joined with single spaces.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

_HEADING_RE = re.compile(r"^##[ \t]+(E\d+)\b[ \t]*(?:[—-][ \t]*(.*))?$", re.MULTILINE)
_FIELD_RE = re.compile(r"^-[ \t]*([A-Za-z]+):[ \t]*(.*)$")


@dataclass(frozen=True)
class LogEntry:
    """One experiences-log entry. Free-text fields may be empty."""

    entry_id: str
    title: str = ""
    date: str = ""
    area: str = ""
    status: str = ""
    context: str = ""
    learned: str = ""
    suggested: str = ""
    portability: str = ""

    @property
    def is_open(self) -> bool:
        """True when the entry has not yet been harvested/integrated."""
        return self.status.lower() == "open"


def parse_log(log_path: Path) -> list[LogEntry]:
    """Parse STANDARDS_LOG.md into entries, in file order.

    Returns an empty list when the file is absent (a project may not have
    started a log). Malformed or partial entries are tolerated: missing
    fields default to "".
    """
    if not log_path.exists():
        return []
    text = log_path.read_text(encoding="utf-8")
    headings = list(_HEADING_RE.finditer(text))
    entries: list[LogEntry] = []
    for i, heading in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        body = text[heading.end() : end]
        entries.append(_build_entry(heading.group(1), heading.group(2), body))
    return entries


def _build_entry(entry_id: str, title: str | None, body: str) -> LogEntry:
    fields = _parse_fields(body)
    return LogEntry(
        entry_id=entry_id,
        title=(title or "").strip(),
        date=fields.get("date", ""),
        area=_token(fields.get("area", "")),
        status=_token(fields.get("status", "")),
        context=fields.get("context", ""),
        learned=fields.get("learned", ""),
        suggested=fields.get("suggested", ""),
        portability=_token(fields.get("portability", "")),
    )


def _parse_fields(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: str | None = None
    for line in body.splitlines():
        match = _FIELD_RE.match(line)
        if match:
            current = match.group(1).lower()
            fields[current] = match.group(2).strip()
        elif current is not None and line.strip():
            fields[current] = f"{fields[current]} {line.strip()}".strip()
    return fields


def _token(value: str) -> str:
    """First whitespace-delimited token, lowercased ('' when value is empty)."""
    parts = value.split()
    return parts[0].lower() if parts else ""
