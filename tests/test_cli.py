# ==============================================================
# VERSION: 0.6
# End-to-end tests for the CLI (status / drift / harvest / integrate / sync).
#
# CHANGE LOG
# v0.6 — 2026-09-05 — PLAN-012: handoff coverage — `sync --write` leaves docs/SYNC_HANDOFF.md
#         (content + not-a-SYNC_MAP-item idempotence) and the integrate write-back leaves it too.
# v0.5 — 2026-08-16 — PLAN-008: five sync tests — empty registry; dry-run writes nothing;
#         --write applies + idempotent second run; unknown --project errors; per-target
#         failure isolation (exit 1, healthy targets still synced).
# v0.4 — 2026-06-20 — Add transport-aware tests: status over a (mocked) git target computes a row;
#                     an unreachable git target is non-fatal; integrate --write to a local target
#                     writes through the new ExitStack/session path (PLAN-007).
# v0.3 — 2026-06-18 — Add 2 integrate tests (worksheet exit 0; --apply dry-run, no write).
# v0.2 — 2026-06-16 — Add 2 harvest tests (empty registry; one project, 2 open entries).
# v0.1 — 2026-06-16 13:01 — Initial: status table, drift exit codes, empty registry.
# ==============================================================
"""Tests for standard_document_updater.cli."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest

from standard_document_updater import transport
from standard_document_updater.cli import main

Make = Callable[..., Path]


def _write_git_registry(vault_root: Path, name: str = "beta", branch: str = "main") -> None:
    reg = vault_root / "config" / "projects.toml"
    reg.parent.mkdir(parents=True, exist_ok=True)
    reg.write_text(
        f'[[project]]\nname = "{name}"\ntransport = "git"\n'
        f'git_url = "git@h:{name}.git"\ngit_branch = "{branch}"\n',
        encoding="utf-8",
    )


def test_status_empty_registry_exit_zero(
    make_vault: Make, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    root = make_vault("1.1")
    write_registry(root, [])
    assert main(["--vault", str(root), "status"]) == 0
    assert "No projects registered" in capsys.readouterr().out


def test_status_lists_project_exit_zero(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted="1.0", open_entries=2)
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "status"]) == 0
    out = capsys.readouterr().out
    assert "alpha" in out and "behind" in out and "v1.0" in out


def test_drift_behind_exits_one(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted="1.0")
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "drift"]) == 1


def test_drift_all_current_exits_zero(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted="1.1")
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "drift"]) == 0
    assert "No drift" in capsys.readouterr().out


def test_drift_unknown_counts_as_drift(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", adopted=None)
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "drift"]) == 1


def test_harvest_empty_registry_exit_zero(
    make_vault: Make, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    root = make_vault("1.1")
    write_registry(root, [])
    assert main(["--vault", str(root), "harvest"]) == 0
    assert "No open log entries across registered projects." in capsys.readouterr().out


def test_harvest_lists_open_entries_exit_zero(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", open_entries=2)
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "harvest"]) == 0
    out = capsys.readouterr().out
    assert "E001" in out and "E002" in out and "alpha" in out


def test_integrate_worksheet_exit_zero(
    make_vault: Make, make_project: Make, write_registry: Make,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", open_entries=1)
    write_registry(root, [("alpha", proj)])
    assert main(["--vault", str(root), "integrate"]) == 0
    out = capsys.readouterr().out
    assert "[alpha] E001" in out and "current Set Version v1.1" in out


def test_integrate_apply_dry_run_exit_zero(
    make_vault: Make, make_project: Make, write_registry: Make, tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", open_entries=1)
    write_registry(root, [("alpha", proj)])
    log = proj / "docs" / "STANDARDS_LOG.md"
    before = log.read_text(encoding="utf-8")
    decisions = tmp_path / "decisions.toml"
    decisions.write_text(
        '[[rejected]]\nproject = "alpha"\nentry = "E001"\nreason = "n/a"\n',
        encoding="utf-8",
    )
    assert main(["--vault", str(root), "integrate", "--apply", str(decisions)]) == 0
    assert "DRY-RUN" in capsys.readouterr().out
    assert log.read_text(encoding="utf-8") == before


def test_integrate_apply_write_local_writes(
    make_vault: Make, make_project: Make, write_registry: Make, tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    proj = make_project("alpha", open_entries=1)
    write_registry(root, [("alpha", proj)])
    log = proj / "docs" / "STANDARDS_LOG.md"
    decisions = tmp_path / "decisions.toml"
    decisions.write_text(
        '[[rejected]]\nproject = "alpha"\nentry = "E001"\nreason = "n/a"\n',
        encoding="utf-8",
    )
    assert main(["--vault", str(root), "integrate", "--apply", str(decisions), "--write"]) == 0
    assert "wrote" in capsys.readouterr().out
    assert "rejected — n/a" in log.read_text(encoding="utf-8")
    handoff = (proj / "docs" / "SYNC_HANDOFF.md").read_text(encoding="utf-8")
    assert "- **Operation:** integrate write-back" in handoff
    assert "`docs/STANDARDS_LOG.md` (write-back)" in handoff


def test_status_git_target_row_computed(
    make_vault: Make, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    _write_git_registry(root)

    def fake_run(cmd: list[str]) -> None:
        if cmd[1] == "clone":  # populate the materialization the read path would have fetched
            dest = Path(cmd[-1])
            (dest / "docs").mkdir(parents=True, exist_ok=True)
            (dest / "docs" / "SET_VERSION_ADOPTED.md").write_text(
                "- **Standard Set Version:** v1.0\n", encoding="utf-8"
            )
            (dest / "docs" / "STANDARDS_LOG.md").write_text("", encoding="utf-8")

    monkeypatch.setattr(transport, "_run", fake_run)
    assert main(["--vault", str(root), "status"]) == 0
    out = capsys.readouterr().out
    assert "beta" in out and "behind" in out and "git:git@h:beta.git@main" in out


def test_status_unreachable_git_target_is_nonfatal(
    make_vault: Make, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    root = make_vault("1.1")
    _write_git_registry(root)

    def boom(cmd: list[str]) -> None:
        raise transport.TransportError("host unreachable")

    monkeypatch.setattr(transport, "_run", boom)
    assert main(["--vault", str(root), "status"]) == 0  # non-fatal for a read command
    out = capsys.readouterr().out
    assert "beta" in out and "unknown" in out


# --- sync (PLAN-008) -------------------------------------------------------------

MakePair = Callable[..., tuple[Path, Path]]


def test_sync_empty_registry_exit_zero(
    make_vault: Make, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    root = make_vault("1.1")
    write_registry(root, [])
    assert main(["--vault", str(root), "sync"]) == 0
    assert "No registered projects to sync" in capsys.readouterr().out


def test_sync_dry_run_reports_and_writes_nothing(
    make_suite_pair: MakePair, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("acme", target)])
    before = (target / "CLAUDE.md").read_text(encoding="utf-8")
    assert main(["--vault", str(vault), "sync"]) == 0
    out = capsys.readouterr().out
    assert "DRY-RUN" in out and "need sync" in out and "(dry-run — re-run with --write" in out
    assert (target / "CLAUDE.md").read_text(encoding="utf-8") == before


def test_sync_write_applies_and_second_run_is_up_to_date(
    make_suite_pair: MakePair, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("acme", target)])
    assert main(["--vault", str(vault), "sync", "--write"]) == 0
    assert "wrote + flushed" in capsys.readouterr().out
    merged = (target / "CLAUDE.md").read_text(encoding="utf-8")
    assert "Acme CLI." in merged and "## 3. Rules NEW." in merged
    sva = (target / "docs" / "SET_VERSION_ADOPTED.md").read_text(encoding="utf-8")
    assert "- **Standard Set Version:** v1.5 (synced from the vault by the engine" in sva
    assert main(["--vault", str(vault), "sync", "--write"]) == 0
    assert "up-to-date" in capsys.readouterr().out


def test_sync_write_leaves_handoff_and_dry_run_stays_up_to_date(
    make_suite_pair: MakePair, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("acme", target)])
    assert main(["--vault", str(vault), "sync", "--write"]) == 0
    assert "(incl. the handoff)" in capsys.readouterr().out
    handoff = (target / "docs" / "SYNC_HANDOFF.md").read_text(encoding="utf-8")
    assert "SYNC HANDOFF" in handoff
    assert "- **Operation:** sync --write" in handoff
    assert "- **Vault Standard Set Version:** v1.5" in handoff
    assert "`CLAUDE.md` (merge)" in handoff
    assert "delete this handoff" in handoff
    # the handoff is not a SYNC_MAP item: a converged target stays up-to-date
    assert main(["--vault", str(vault), "sync"]) == 0
    assert "up-to-date" in capsys.readouterr().out


def test_sync_unknown_project_filter_errors(
    make_suite_pair: MakePair, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("acme", target)])
    assert main(["--vault", str(vault), "sync", "--project", "nope"]) == 2
    assert "not in the registry: nope" in capsys.readouterr().err


def test_sync_per_target_failure_is_isolated_exit_one(
    make_suite_pair: MakePair, write_registry: Make, tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("ghost", tmp_path / "missing"), ("acme", target)])
    assert main(["--vault", str(vault), "sync", "--write"]) == 1
    captured = capsys.readouterr()
    assert "ghost" in captured.err and "1 target(s) FAILED" in captured.err
    assert "[acme]" in captured.out and "wrote + flushed" in captured.out
