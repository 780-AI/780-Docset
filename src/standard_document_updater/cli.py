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
