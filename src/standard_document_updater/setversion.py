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
