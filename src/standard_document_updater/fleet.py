# ==============================================================
# VERSION: 0.1
# Fleet view: docs/fleet.csv rendered from the registry + live target probes.
#
# CHANGE LOG
# v0.1 — 2026-10-05 — Initial (PLAN-016): Probe + build_rows (registry columns fresh on every
#                     run; live columns from the probe, last-known values carried while a
#                     target is unreachable) + CSV read / render / atomic write +
#                     registry_mismatches (the pre-push freshness check).
# ==============================================================
"""The fleet view — one CSV row per registered project (PLAN-016).

docs/fleet.csv is GENERATED: never edited by hand, never committed (gitignored).
Written as UTF-8 with a byte-order mark so spreadsheet apps (Excel) read non-ASCII text
correctly; read back BOM-tolerantly. Three column groups:

  registry — copied from config/projects.toml on every run. The registry is the
             single source of truth for fixed facts; scripts/check_doc_coverage.py
             fails a push while the file disagrees with it.
  live     — read from each target by the probe. While a target cannot be reached,
             the previous file's values are kept (reachable=no, last_seen unchanged).
  run      — when the file was generated, and from which vault commit.

Pure: no transport here — cli.py probes the targets and hands the readings in.
"""
from __future__ import annotations

import csv
import io
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path

from standard_document_updater.registry import Project, load_registry
from standard_document_updater.report import ProjectStatus, fmt_version

FLEET_REL = Path("docs/fleet.csv")

REGISTRY_COLUMNS = (
    "project",
    "owner",
    "git_remote",
    "part_of",
    "transport",
    "location",
    "work_machine",
    "delivery",
    "onboarding",
    "onboarded_on",
    "onboarded_set",
    "registered_on",
    "plan",
    "lifecycle",
    "caveats",
)
LIVE_COLUMNS = (
    "adopted_set",
    "vault_set",
    "state",
    "open_log",
    "handoff_pending",
    "reachable",
    "last_seen",
)
RUN_COLUMNS = ("as_of", "vault_sha")
COLUMNS = REGISTRY_COLUMNS + LIVE_COLUMNS + RUN_COLUMNS

# Live values kept from the previous file while a target cannot be reached.
_CARRIED = ("adopted_set", "open_log", "handoff_pending", "last_seen")


@dataclass(frozen=True)
class Probe:
    """One target's live reading: its status row, reachability, un-landed handoff writes."""

    status: ProjectStatus
    reachable: bool
    handoff_writes: int | None  # None when the target could not be reached


def _location(project: Project) -> str:
    """Machine-neutral location: a local path under $HOME renders as ~/… (the file is
    folder-synced between machines whose $HOME differs)."""
    if project.transport == "local" and project.path is not None:
        try:
            return "~/" + project.path.relative_to(Path.home()).as_posix()
        except ValueError:
            pass
    return project.location


def registry_columns(project: Project) -> dict[str, str]:
    """The fixed-fact columns for one project, straight from the registry."""
    info = project.info
    return {
        "project": project.name,
        "owner": info.owner,
        "git_remote": info.git_remote,
        "part_of": info.part_of,
        "transport": project.transport,
        "location": _location(project),
        "work_machine": info.work_machine,
        "delivery": info.delivery,
        "onboarding": info.onboarding,
        "onboarded_on": info.onboarded_on,
        "onboarded_set": info.onboarded_set,
        "registered_on": info.registered_on,
        "plan": info.plan,
        "lifecycle": info.lifecycle,
        "caveats": info.caveats,
    }


def _live_columns(probe: Probe, previous: dict[str, str], seen: str) -> dict[str, str]:
    status = probe.status
    row = {
        "vault_set": fmt_version(status.vault),
        "state": status.state.value,
        "reachable": "yes" if probe.reachable else "no",
    }
    if probe.reachable:
        row |= {
            "adopted_set": fmt_version(status.adopted),
            "open_log": str(status.open_entries),
            "handoff_pending": str(probe.handoff_writes or 0),
            "last_seen": seen,
        }
    else:
        row |= {key: previous.get(key, "") for key in _CARRIED}
    return row


def build_rows(
    probes: list[Probe], previous: dict[str, dict[str, str]], as_of: str, vault_sha: str
) -> list[dict[str, str]]:
    """One row per probed project, in registry order; `previous` = the last file's rows."""
    rows: list[dict[str, str]] = []
    for probe in probes:
        project = probe.status.project
        prior = previous.get(project.name, {})
        rows.append(
            registry_columns(project)
            | _live_columns(probe, prior, as_of)
            | {"as_of": as_of, "vault_sha": vault_sha}
        )
    return rows


def read_rows(path: Path) -> dict[str, dict[str, str]]:
    """An existing fleet file's rows keyed by project ({} when absent or unreadable)."""
    if not path.is_file():
        return {}
    try:
        reader = csv.DictReader(io.StringIO(path.read_text(encoding="utf-8-sig")))
        return {
            row["project"]: {k: v or "" for k, v in row.items() if isinstance(k, str)}
            for row in reader
            if row.get("project")
        }
    except (OSError, UnicodeDecodeError, csv.Error):
        return {}


def render_csv(rows: list[dict[str, str]]) -> str:
    """CSV text in the fixed column order; the header row is always present."""
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def write_fleet(vault_root: Path, rows: list[dict[str, str]]) -> Path:
    """Atomically replace docs/fleet.csv (a reader never sees a half-written file)."""
    path = vault_root / FLEET_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(render_csv(rows), encoding="utf-8-sig")  # BOM: Excel reads UTF-8 right
    os.replace(tmp, path)
    return path


def vault_sha(vault_root: Path) -> str:
    """Short HEAD sha of the vault repo ("" when git or the repository is unavailable)."""
    try:
        proc = subprocess.run(
            ["git", "-C", str(vault_root), "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return ""
    return proc.stdout.strip() if proc.returncode == 0 else ""


def registry_mismatches(vault_root: Path) -> list[str]:
    """Where docs/fleet.csv's registry columns disagree with config/projects.toml ([] = fresh).

    Run by scripts/check_doc_coverage.py before every push; the fix is always to
    regenerate the file (`python -m standard_document_updater fleet`).
    """
    projects = load_registry(vault_root / "config" / "projects.toml")
    rows = read_rows(vault_root / FLEET_REL)
    names = {project.name for project in projects}
    problems = [
        f"{name}: in docs/fleet.csv but not in the registry" for name in sorted(set(rows) - names)
    ]
    for project in projects:
        row = rows.get(project.name)
        if row is None:
            problems.append(f"{project.name}: in the registry but not in docs/fleet.csv")
            continue
        stale = [col for col, value in registry_columns(project).items() if row.get(col) != value]
        if stale:
            problems.append(f"{project.name}: stale column(s): {', '.join(stale)}")
    return problems
