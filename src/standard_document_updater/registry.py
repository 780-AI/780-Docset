# ==============================================================
# VERSION: 0.1
# Managed-projects registry loader (config/projects.toml).
#
# CHANGE LOG
# v0.1 — 2026-06-16 13:01 — Initial: parse name + path tables into Project list.
# ==============================================================
"""Load the managed-projects registry.

Stores ONLY each project's name + path. A project's adopted Set Version is NOT
stored here — it is read live from <path>/docs/SET_VERSION_ADOPTED.md at report
time (single source of truth, per docs/architecture.md § 9).
"""
from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

from standard_document_updater.errors import RegistryError


@dataclass(frozen=True)
class Project:
    """A managed project: a display name and its repository root path."""

    name: str
    path: Path


def load_registry(registry_path: Path) -> list[Project]:
    """Parse config/projects.toml into a list of Project, in file order.

    Returns an empty list when the registry exists but declares no projects.
    Raises RegistryError when the file is missing, unreadable, or malformed.
    """
    if not registry_path.exists():
        raise RegistryError(f"registry not found: {registry_path}")
    try:
        data = tomllib.loads(registry_path.read_text(encoding="utf-8"))
    except (tomllib.TOMLDecodeError, OSError) as exc:
        raise RegistryError(f"could not read registry {registry_path}: {exc}") from exc

    raw_projects = data.get("project", [])
    if not isinstance(raw_projects, list):
        raise RegistryError("registry key 'project' must be an array of tables")

    projects: list[Project] = []
    for index, entry in enumerate(raw_projects, start=1):
        if not isinstance(entry, dict):
            raise RegistryError(f"project #{index} is not a table")
        name = entry.get("name")
        path = entry.get("path")
        if not isinstance(name, str) or not name.strip():
            raise RegistryError(f"project #{index} is missing a non-empty 'name'")
        if not isinstance(path, str) or not path.strip():
            raise RegistryError(f"project '{name}' is missing a non-empty 'path'")
        projects.append(Project(name=name, path=Path(path).expanduser()))
    return projects
