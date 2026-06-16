# ==============================================================
# VERSION: 0.1
# Parse Set Versions + open-log counts from standards files (live reads).
#
# CHANGE LOG
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

_VAULT_RE = re.compile(r"^Standard Set Version:\s*v(\d+(?:\.\d+)+)", re.MULTILINE)
_ADOPTED_RE = re.compile(r"\*\*Standard Set Version:\*\*\s*v(\d+(?:\.\d+)+)")
_ENTRY_RE = re.compile(r"^##\s+E\d+\b", re.MULTILINE)
_STATUS_RE = re.compile(r"^-\s*Status:\s*(\S+)", re.MULTILINE)


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
    """Count STANDARDS_LOG.md entries whose Status begins with 'open'.

    Returns 0 when the log file is absent (a project may not have started one).
    """
    if not log_path.exists():
        return 0
    text = log_path.read_text(encoding="utf-8")
    headings = list(_ENTRY_RE.finditer(text))
    count = 0
    for i, heading in enumerate(headings):
        start = heading.start()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        status = _STATUS_RE.search(text[start:end])
        if status is not None and status.group(1).lower().startswith("open"):
            count += 1
    return count
