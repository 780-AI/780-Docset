# ==============================================================
# VERSION: 0.1
# Unit tests for the registry loader.
#
# CHANGE LOG
# v0.1 — 2026-06-16 13:01 — Initial: load / empty / missing / malformed.
# ==============================================================
"""Tests for standard_document_updater.registry."""
from __future__ import annotations

from pathlib import Path

import pytest

from standard_document_updater.errors import RegistryError
from standard_document_updater.registry import load_registry


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_load_registry_parses_projects_in_order(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(
        reg,
        '[[project]]\nname = "alpha"\npath = "/tmp/alpha"\n\n'
        '[[project]]\nname = "beta"\npath = "/tmp/beta"\n',
    )
    projects = load_registry(reg)
    assert [p.name for p in projects] == ["alpha", "beta"]
    assert projects[0].path == Path("/tmp/alpha")


def test_load_registry_empty_is_empty_list(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, "# no projects\n")
    assert load_registry(reg) == []


def test_load_registry_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(RegistryError):
        load_registry(tmp_path / "absent.toml")


def test_load_registry_missing_name_raises(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, '[[project]]\npath = "/tmp/x"\n')
    with pytest.raises(RegistryError):
        load_registry(reg)
