# ==============================================================
# VERSION: 0.1
# Consolidate open experiences-log entries across registered projects.
#
# CHANGE LOG
# v0.1 — 2026-06-16 — Initial: collect/group-by-area, cautious dup flag, render.
# ==============================================================
"""Build the harvest report: every open log entry, grouped by area.

Read-only. Flags likely cross-project duplicates conservatively (PLAN-004 D3):
two open entries are flagged only when their normalized titles match AND they
come from different projects. Always informational; the CLI exits 0 (D4).
"""
from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass

from standard_document_updater.logentry import LogEntry

_NORM_RE = re.compile(r"[^a-z0-9]+")


@dataclass(frozen=True)
class OpenItem:
    """An open log entry paired with the project it came from."""

    project_name: str
    entry: LogEntry


def _normalize(title: str) -> str:
    """Lowercase, drop punctuation, collapse whitespace — for dup matching."""
    return _NORM_RE.sub(" ", title.lower()).strip()


def _duplicate_refs(items: list[OpenItem]) -> dict[int, list[str]]:
    """Map item index -> refs of same-title items from *other* projects."""
    by_title: dict[str, list[int]] = defaultdict(list)
    for index, item in enumerate(items):
        key = _normalize(item.entry.title)
        if key:
            by_title[key].append(index)
    refs: dict[int, list[str]] = {}
    for indices in by_title.values():
        if len({items[i].project_name for i in indices}) < 2:
            continue
        for i in indices:
            others = [
                f"{items[j].project_name}/{items[j].entry.entry_id}"
                for j in indices
                if items[j].project_name != items[i].project_name
            ]
            if others:
                refs[i] = others
    return refs


def render_report(items: list[OpenItem]) -> str:
    """Render the consolidated report grouped by area (stable, deterministic)."""
    if not items:
        return "No open log entries across registered projects."
    refs = _duplicate_refs(items)
    by_area: dict[str, list[int]] = defaultdict(list)
    for index, item in enumerate(items):
        by_area[item.entry.area or "(unspecified)"].append(index)

    project_count = len({item.project_name for item in items})
    plural = "y" if len(items) == 1 else "ies"
    lines = [
        f"Harvest — {len(items)} open entr{plural} "
        f"across {project_count} project(s), {len(by_area)} area(s)."
    ]
    for area in sorted(by_area):
        lines.append("")
        lines.append(f"## {area} ({len(by_area[area])})")
        ordered = sorted(
            by_area[area],
            key=lambda i: (items[i].project_name, items[i].entry.entry_id),
        )
        for i in ordered:
            item = items[i]
            suffix = f"  ({item.entry.portability})" if item.entry.portability else ""
            lines.append(
                f"  [{item.project_name}] {item.entry.entry_id} — {item.entry.title}{suffix}"
            )
            if i in refs:
                lines.append(f"      ⚠ possible duplicate of {', '.join(refs[i])}")
    return "\n".join(lines)
