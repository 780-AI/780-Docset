# ==============================================================
# VERSION: 0.3
# Unit tests for the registry loader.
#
# CHANGE LOG
# v0.3 — 2026-10-05 — PLAN-016: fleet-information keys (parsed + stripped, absent = empty
#                     ProjectInfo) and their validation (unknown key, bad choice, bad date,
#                     bad Set Version, non-string value).
# v0.2 — 2026-06-20 — Add transport parse cases (git / ssh / bare-local default) + per-transport
#                     validation (missing required field, unknown transport) — PLAN-007.
# v0.1 — 2026-06-16 13:01 — Initial: load / empty / missing / malformed.
# ==============================================================
"""Tests for standard_document_updater.registry."""
from __future__ import annotations

from pathlib import Path

import pytest

from standard_document_updater.errors import RegistryError
from standard_document_updater.registry import ProjectInfo, load_registry


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


def test_load_registry_bare_entry_defaults_local(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, '[[project]]\nname = "alpha"\npath = "/tmp/alpha"\n')
    [p] = load_registry(reg)
    assert p.transport == "local"
    assert p.path == Path("/tmp/alpha")
    assert p.location == "/tmp/alpha"


def test_load_registry_parses_git_transport(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(
        reg,
        '[[project]]\nname = "beta"\ntransport = "git"\n'
        'git_url = "git@gitlab.com:org/beta.git"\ngit_branch = "main"\n',
    )
    [p] = load_registry(reg)
    assert p.transport == "git"
    assert p.git_url == "git@gitlab.com:org/beta.git"
    assert p.git_branch == "main"
    assert p.location == "git:git@gitlab.com:org/beta.git@main"


def test_load_registry_git_default_branch(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, '[[project]]\nname = "beta"\ntransport = "git"\ngit_url = "u"\n')
    [p] = load_registry(reg)
    assert p.git_branch == ""
    assert p.location == "git:u"


def test_load_registry_parses_ssh_transport(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(
        reg,
        '[[project]]\nname = "gamma"\ntransport = "ssh"\n'
        'ssh_host = "devbox"\nssh_path = "/home/me/gamma"\n',
    )
    [p] = load_registry(reg)
    assert p.transport == "ssh"
    assert p.ssh_host == "devbox" and p.ssh_path == "/home/me/gamma"
    assert p.location == "ssh:devbox:/home/me/gamma"


def test_load_registry_local_missing_path_raises(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, '[[project]]\nname = "alpha"\ntransport = "local"\n')
    with pytest.raises(RegistryError, match="path"):
        load_registry(reg)


def test_load_registry_git_missing_url_raises(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, '[[project]]\nname = "beta"\ntransport = "git"\n')
    with pytest.raises(RegistryError, match="git_url"):
        load_registry(reg)


def test_load_registry_ssh_missing_path_raises(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, '[[project]]\nname = "gamma"\ntransport = "ssh"\nssh_host = "devbox"\n')
    with pytest.raises(RegistryError, match="ssh_path"):
        load_registry(reg)


def test_load_registry_unknown_transport_raises(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, '[[project]]\nname = "x"\ntransport = "carrier-pigeon"\n')
    with pytest.raises(RegistryError, match="unknown transport"):
        load_registry(reg)


def test_load_registry_reads_fleet_info(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(
        reg,
        '[[project]]\nname = "alpha"\npath = "/tmp/alpha"\nowner = "team"\n'
        'delivery = "direct+handoff"\nonboarding = "bootstrap"\nonboarded_on = "2026-08-19"\n'
        'onboarded_set = "v2.1"\nlifecycle = "active"\ncaveats = "  DHCP IP  "\n',
    )
    info = load_registry(reg)[0].info
    assert (info.owner, info.delivery, info.onboarding) == ("team", "direct+handoff", "bootstrap")
    assert (info.onboarded_on, info.onboarded_set) == ("2026-08-19", "v2.1")
    assert info.lifecycle == "active"
    assert info.caveats == "DHCP IP"  # surrounding whitespace stripped
    assert info.plan == ""  # an absent key reads as ""


def test_load_registry_without_info_has_empty_info(tmp_path: Path) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, '[[project]]\nname = "alpha"\npath = "/tmp/alpha"\n')
    assert load_registry(reg)[0].info == ProjectInfo()


@pytest.mark.parametrize(
    ("line", "message"),
    [
        ('ownr = "team"', "unknown key"),
        ('owner = "someone"', "'owner' must be one of"),
        ('lifecycle = "live"', "'lifecycle' must be one of"),
        ('registered_on = "2026/10/04"', "YYYY-MM-DD"),
        ('onboarded_set = "2.7"', "must look like v2.7"),
        ("plan = 16", "'plan' must be a string"),
    ],
)
def test_load_registry_rejects_bad_fleet_info(tmp_path: Path, line: str, message: str) -> None:
    reg = tmp_path / "projects.toml"
    _write(reg, f'[[project]]\nname = "alpha"\npath = "/tmp/alpha"\n{line}\n')
    with pytest.raises(RegistryError, match=message):
        load_registry(reg)
