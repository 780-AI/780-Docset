# ==============================================================
# VERSION: 0.1
# Command-line interface: `python -m standard_document_updater <command>`.
#
# CHANGE LOG
# v0.1 — 2026-06-16 13:01 — Initial: status + drift subcommands, --vault override.
# ==============================================================
"""CLI entry point and command dispatch."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from standard_document_updater import __version__, report, setversion
from standard_document_updater.errors import StandardDocSetError
from standard_document_updater.registry import load_registry


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
        adopted_path = project.path / "docs" / "SET_VERSION_ADOPTED.md"
        log_path = project.path / "docs" / "STANDARDS_LOG.md"
        statuses.append(report.compute_status(project, vault_version, adopted_path, log_path))
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
    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse argv and run the chosen command. Returns the process exit code."""
    args = build_parser().parse_args(argv)
    handlers = {"status": _cmd_status, "drift": _cmd_drift}
    try:
        return handlers[args.command](args)
    except StandardDocSetError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
