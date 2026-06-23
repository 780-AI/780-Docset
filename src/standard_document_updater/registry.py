# ==============================================================
# VERSION: 0.2
# Managed-projects registry loader (config/projects.toml).
#
# CHANGE LOG
# v0.2 — 2026-06-20 — Project grows a per-target transport (local | git | ssh) + connection fields;
#                     load_registry validates the fields required by each transport (PLAN-007).
# v0.1 — 2026-06-16 13:01 — Initial: parse name + path tables into Project list.
# ==============================================================
"""Load the managed-projects registry.

Stores each project's name + transport + the connection fields for that transport
(local: path; git: git_url/git_branch; ssh: ssh_host/ssh_path). A project's adopted
Set Version is NOT stored here — it is read live from the materialized
<root>/docs/SET_VERSION_ADOPTED.md at report time (single source of truth, per
docs/architecture.md § 9).
"""
from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

from standard_document_updater.errors import RegistryError

_VALID_TRANSPORTS = ("local", "git", "ssh")


@dataclass(frozen=True)
class Project:
    """A managed project: name + transport + the connection fields for that transport."""

    name: str
    transport: str = "local"
    path: Path | None = None        # local
    git_url: str | None = None      # git
    git_branch: str = ""            # git (empty -> the remote's default branch)
    ssh_host: str | None = None     # ssh
    ssh_path: str | None = None     # ssh

    @property
    def location(self) -> str:
        """Human-readable location for the report table."""
        if self.transport == "git":
            branch = f"@{self.git_branch}" if self.git_branch else ""
            return f"git:{self.git_url}{branch}"
        if self.transport == "ssh":
            return f"ssh:{self.ssh_host}:{self.ssh_path}"
        return str(self.path) if self.path is not None else "(no path)"


def _require(entry: dict[str, object], key: str, name: str) -> str:
    value = entry.get(key)
    if not isinstance(value, str) or not value.strip():
        raise RegistryError(f"project '{name}': missing a non-empty '{key}'")
    return value


def _build_project(name: str, transport: str, entry: dict[str, object]) -> Project:
    if transport == "local":
        return Project(name=name, path=Path(_require(entry, "path", name)).expanduser())
    if transport == "git":
        branch = entry.get("git_branch", "")
        if not isinstance(branch, str):
            raise RegistryError(f"project '{name}': 'git_branch' must be a string")
        return Project(
            name=name, transport="git", git_url=_require(entry, "git_url", name), git_branch=branch
        )
    if transport == "ssh":
        return Project(
            name=name,
            transport="ssh",
            ssh_host=_require(entry, "ssh_host", name),
            ssh_path=_require(entry, "ssh_path", name),
        )
    raise RegistryError(
        f"project '{name}': unknown transport '{transport}' "
        f"(expected one of: {', '.join(_VALID_TRANSPORTS)})"
    )


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
        if not isinstance(name, str) or not name.strip():
            raise RegistryError(f"project #{index} is missing a non-empty 'name'")
        transport = entry.get("transport", "local")
        if not isinstance(transport, str):
            raise RegistryError(f"project '{name}': 'transport' must be a string")
        projects.append(_build_project(name, transport, entry))
    return projects
