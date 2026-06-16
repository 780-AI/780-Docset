# ==============================================================
# VERSION: 0.1
# Shared pytest fixtures — synthetic vault + adopter-project trees.
#
# CHANGE LOG
# v0.1 — 2026-06-16 13:01 — Initial: make_vault + make_project factories.
# ==============================================================
"""Fixtures that build minimal on-disk vault/project trees under tmp_path.

All three fixtures return factory callables. Tests annotate the injected
parameter as ``Callable[..., Path]`` so mypy --strict is satisfied without
importing anything from this module (no cross-test imports, no type: ignore).
"""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def make_vault(tmp_path: Path) -> Callable[..., Path]:
    """Factory: build a vault root with STANDARDS_INDEX.md at the given Set Version."""

    def _make(version: str = "1.1") -> Path:
        root = tmp_path / "vault"
        _write(
            root / "docs" / "standards" / "STANDARDS_INDEX.md",
            f"## 1. Standard Set Version (current)\n\n```\nStandard Set Version: v{version}\n```\n",
        )
        (root / "config").mkdir(parents=True, exist_ok=True)
        return root

    return _make


@pytest.fixture
def make_project(tmp_path: Path) -> Callable[..., Path]:
    """Factory: build an adopter tree; adopted=None omits SET_VERSION_ADOPTED.md."""

    def _make(name: str, adopted: str | None = "1.1", open_entries: int = 0) -> Path:
        proj = tmp_path / name
        if adopted is not None:
            _write(
                proj / "docs" / "SET_VERSION_ADOPTED.md",
                f"- **Standard Set Version:** v{adopted} (notes)\n",
            )
        if open_entries:
            body = "".join(
                f"## E{i + 1:03d} — title\n- Status:      open\n\n" for i in range(open_entries)
            )
            _write(proj / "docs" / "STANDARDS_LOG.md", body)
        return proj

    return _make


@pytest.fixture
def write_registry() -> Callable[..., Path]:
    """Factory: write config/projects.toml from (name, path) pairs; return its path."""

    def _write_registry(vault_root: Path, projects: list[tuple[str, Path]]) -> Path:
        body = "".join(
            f'[[project]]\nname = "{name}"\npath = "{path}"\n\n' for name, path in projects
        )
        registry = vault_root / "config" / "projects.toml"
        _write(registry, body)
        return registry

    return _write_registry
