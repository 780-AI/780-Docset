# ==============================================================
# VERSION: 0.2
# Shared pytest fixtures — synthetic vault + adopter-project trees.
#
# CHANGE LOG
# v0.2 — 2026-08-16 — PLAN-008 (sync): make_suite_pair factory — a full vault suite +
#                     converged adopter tree covering every SYNC_MAP mode (shared by
#                     test_sync + test_cli).
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


def _hdr(version: str) -> str:
    return (
        f"<!-- VERSION: {version} -->\n"
        "<!-- Last Updated: 2026-08-01 -->\n"
        "<!--\n"
        "CHANGE LOG\n"
        f"v{version} — 2026-08-01 — fixture.\n"
        "-->\n"
    )


_PO = "<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->"
_PO_END = "<!-- PROJECT-OWNED:END -->"
_TO = "<!-- TEMPLATE-ONLY:BEGIN (stripped at instantiation; sync never propagates this block) -->"
_TO_END = "<!-- TEMPLATE-ONLY:END -->"

_TOPICALS = (
    "PROJECT_STANDARDS.md",
    "PROMPT_STANDARDS.md",
    "MEMORY_PROTOCOL.md",
    "ENGINEERING_STANDARDS.md",
    "VALIDATION_STANDARDS.md",
    "CICD_STANDARDS.md",
)


def _mixed(header: str, banner: str | None, heading: str, suite: str, owned2: str | None) -> str:
    parts = [header, "\n"]
    if banner is not None:
        parts += [_TO, "\n", banner, "\n", _TO_END, "\n"]
    parts += [_PO, "\n", heading, "\n", _PO_END, "\n\n", suite, "\n"]
    if owned2 is not None:
        parts += ["\n", _PO, "\n", owned2, "\n", _PO_END, "\n"]
    return "".join(parts)


@pytest.fixture
def make_suite_pair(tmp_path: Path) -> Callable[..., tuple[Path, Path]]:
    """Factory: a vault (Set v1.5) + a converged adopter one Set Version behind.

    Covers every SYNC_MAP mode: 6 stale topical files + a stale archive LESSONS
    (replace), CLAUDE.md + both session files with PROJECT-OWNED customizations
    (merge), and a v1.4 SET_VERSION_ADOPTED.md with a backport table (record).
    """

    def _make() -> tuple[Path, Path]:
        vault = tmp_path / "svault"
        target = tmp_path / "starget"
        std = vault / "docs" / "standards"
        _write(
            std / "STANDARDS_INDEX.md",
            "## 1. Standard Set Version (current)\n\n```\nStandard Set Version: v1.5\n```\n",
        )
        (vault / "config").mkdir(parents=True, exist_ok=True)
        for name in _TOPICALS:
            _write(std / name, _hdr("1.1") + f"\n# {name}\n\nSuite text NEW.\n")
            _write(
                target / "docs" / "standards" / name,
                _hdr("1.0") + f"\n# {name}\n\nSuite text OLD.\n",
            )
        _write(std / "LESSONS.md", _hdr("1.0") + "\n# LESSONS\n\nLessons NEW.\n")
        _write(target / "archive" / "LESSONS.md", _hdr("1.0") + "\n# LESSONS\n\nLessons OLD.\n")
        _write(
            std / "CLAUDE.md",
            _mixed(
                _hdr("1.4"), None, "## 1. Context\n<fill-me>", "## 3. Rules NEW.", "## 14. <agent>"
            ),
        )
        _write(
            target / "CLAUDE.md",
            _mixed(
                _hdr("1.2"), None, "## 1. Context\nAcme CLI.", "## 3. Rules OLD.", "## 14. Stub."
            ),
        )
        for tpl in ("SESSION_OPENER.md", "SESSION_CLOSER.md"):
            _write(
                std / tpl,
                _mixed(
                    _hdr("1.5"),
                    f"# {tpl} (template)\n> TEMPLATE banner.",
                    f"# {tpl} <project>",
                    "Routine NEW.",
                    None,
                ),
            )
            _write(
                target / "docs" / tpl,
                _mixed(_hdr("1.1"), None, f"# {tpl} Acme (project-local)", "Routine OLD.", None),
            )
        _write(
            target / "docs" / "SET_VERSION_ADOPTED.md",
            _hdr("1.0")
            + "\n# Standard Set Version Adopted\n\n"
            "- **Standard Set Version:** v1.4 (notes)\n"
            "- **Adopted on:** 2026-07-01\n"
            "- **Source:** the vault\n\n"
            "| Set Version | Adopted on | Notes |\n"
            "|---|---|---|\n"
            "| v1.4 | 2026-07-01 | Initial bootstrap |\n",
        )
        return vault, target

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
