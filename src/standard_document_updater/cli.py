# ==============================================================
# VERSION: 0.4
# Command-line interface: `python -m standard_document_updater <command>`.
#
# CHANGE LOG
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
from pathlib import Path

from standard_document_updater import __version__, harvest, integrate, logentry, report, setversion
from standard_document_updater.errors import StandardDocSetError
from standard_document_updater.registry import load_registry
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
    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse argv and run the chosen command. Returns the process exit code."""
    args = build_parser().parse_args(argv)
    handlers = {
        "status": _cmd_status,
        "drift": _cmd_drift,
        "harvest": _cmd_harvest,
        "integrate": _cmd_integrate,
    }
    try:
        return handlers[args.command](args)
    except StandardDocSetError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
