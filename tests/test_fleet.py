# ==============================================================
# VERSION: 0.1
# Unit tests for the fleet view (docs/fleet.csv).
#
# CHANGE LOG
# v0.1 — 2026-10-05 — Initial (PLAN-016): row building (reachable, unreachable carry-over,
#                     no history), machine-neutral ~/ locations, CSV round trip (UTF-8 BOM
#                     for spreadsheet apps) + tolerant reads, atomic write, registry_mismatches.
# ==============================================================
"""Tests for standard_document_updater.fleet."""
from __future__ import annotations

from pathlib import Path

import pytest

from standard_document_updater import fleet
from standard_document_updater.registry import Project, ProjectInfo, load_registry
from standard_document_updater.report import ProjectStatus, State

_AS_OF = "2026-10-04T10:00:00Z"
_INFO = ProjectInfo(
    owner="team", delivery="direct+handoff", lifecycle="active", caveats="DHCP IP, one at a time"
)


def _ssh(name: str = "beta") -> Project:
    return Project(name=name, transport="ssh", ssh_host="u@10.0.0.1", ssh_path="/r", info=_INFO)


def _probe(project: Project, *, reachable: bool = True, writes: int = 0) -> fleet.Probe:
    if not reachable:
        status = ProjectStatus(project, None, (2, 7), State.UNKNOWN, 0, "host down")
        return fleet.Probe(status, False, None)
    return fleet.Probe(ProjectStatus(project, (2, 6), (2, 7), State.BEHIND, 3), True, writes)


def test_build_rows_reachable_row_has_every_column() -> None:
    row = fleet.build_rows([_probe(_ssh(), writes=2)], {}, _AS_OF, "abc1234")[0]
    assert sorted(row) == sorted(fleet.COLUMNS)  # the writer fixes the column order
    assert (row["project"], row["owner"], row["transport"]) == ("beta", "team", "ssh")
    assert row["location"] == "ssh:u@10.0.0.1:/r"
    assert (row["adopted_set"], row["vault_set"], row["state"]) == ("v2.6", "v2.7", "behind")
    assert (row["open_log"], row["handoff_pending"], row["reachable"]) == ("3", "2", "yes")
    assert row["last_seen"] == row["as_of"] == _AS_OF
    assert row["vault_sha"] == "abc1234"


def test_build_rows_unreachable_keeps_last_known_values() -> None:
    previous = {
        "beta": {
            "adopted_set": "v2.7",
            "open_log": "12",
            "handoff_pending": "1",
            "last_seen": "2026-10-03T14:46:51Z",
            "state": "current",
        }
    }
    row = fleet.build_rows([_probe(_ssh(), reachable=False)], previous, _AS_OF, "")[0]
    assert (row["reachable"], row["state"], row["vault_set"]) == ("no", "unknown", "v2.7")
    assert (row["adopted_set"], row["open_log"], row["handoff_pending"]) == ("v2.7", "12", "1")
    assert row["last_seen"] == "2026-10-03T14:46:51Z"  # not advanced: the probe failed
    assert row["owner"] == "team"  # registry columns are always fresh


def test_build_rows_unreachable_without_history_is_blank() -> None:
    row = fleet.build_rows([_probe(_ssh(), reachable=False)], {}, _AS_OF, "")[0]
    assert row["adopted_set"] == row["open_log"] == row["last_seen"] == ""
    assert row["reachable"] == "no"


def test_local_location_under_home_renders_with_tilde(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("HOME", str(tmp_path))
    inside = Project(name="a", path=tmp_path / "Projects" / "a")
    outside = Project(name="b", path=Path("/srv/b"))
    assert fleet.registry_columns(inside)["location"] == "~/Projects/a"
    assert fleet.registry_columns(outside)["location"] == "/srv/b"


def test_write_then_read_round_trips(tmp_path: Path) -> None:
    probes = [_probe(_ssh("beta"), writes=1), _probe(_ssh("gamma"), reachable=False)]
    rows = fleet.build_rows(probes, {}, _AS_OF, "abc1234")
    path = fleet.write_fleet(tmp_path, rows)
    assert path == tmp_path / "docs" / "fleet.csv"
    assert not path.with_name("fleet.csv.tmp").exists()
    assert path.read_bytes().startswith(b"\xef\xbb\xbf")  # BOM: Excel reads UTF-8 correctly
    assert path.read_text(encoding="utf-8-sig").splitlines()[0] == ",".join(fleet.COLUMNS)
    assert fleet.read_rows(path) == {row["project"]: row for row in rows}  # commas quoted


def test_read_rows_is_tolerant(tmp_path: Path) -> None:
    assert fleet.read_rows(tmp_path / "missing.csv") == {}
    odd = tmp_path / "odd.csv"
    odd.write_text("project,open_log\nbeta,4,extra-cell\n,5\n", encoding="utf-8")
    assert fleet.read_rows(odd) == {"beta": {"project": "beta", "open_log": "4"}}
    bom = tmp_path / "bom.csv"  # a spreadsheet re-save adds a BOM and CRLF line ends
    bom.write_bytes(b"\xef\xbb\xbfproject,open_log\r\nbeta,4\r\n")
    assert fleet.read_rows(bom) == {"beta": {"project": "beta", "open_log": "4"}}


_REG = (
    '[[project]]\nname = "beta"\ntransport = "ssh"\nssh_host = "u@10.0.0.1"\n'
    'ssh_path = "/r"\nowner = "team"\n'
)
_GAMMA = '\n[[project]]\nname = "gamma"\npath = "/srv/g"\n'


def _registry(vault: Path, body: str) -> Path:
    reg = vault / "config" / "projects.toml"
    reg.parent.mkdir(parents=True, exist_ok=True)
    reg.write_text(body, encoding="utf-8")
    return reg


def test_registry_mismatches_names_every_drift(tmp_path: Path) -> None:
    beta = load_registry(_registry(tmp_path, _REG))[0]
    fleet.write_fleet(tmp_path, fleet.build_rows([_probe(beta)], {}, _AS_OF, ""))
    assert fleet.registry_mismatches(tmp_path) == []
    _registry(tmp_path, _REG.replace('owner = "team"', 'owner = "operator"') + _GAMMA)
    assert fleet.registry_mismatches(tmp_path) == [
        "beta: stale column(s): owner",
        "gamma: in the registry but not in docs/fleet.csv",
    ]
    _registry(tmp_path, _GAMMA)
    assert fleet.registry_mismatches(tmp_path) == [
        "beta: in docs/fleet.csv but not in the registry",
        "gamma: in the registry but not in docs/fleet.csv",
    ]
