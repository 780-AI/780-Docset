#!/usr/bin/env python3
# ==============================================================
# VERSION: 0.2
# Doc-coverage governance — surface drift between code, docs, and the manifest.
#
# Initial scaffold (permissive — exits 0). Extend with project-specific checks
# as the project grows: tracked .md presence in manifest, CLI flags documented,
# tracked code-file VERSION-header presence, etc.
#
# CHANGE LOG
# v0.2 — 2026-10-05 — PLAN-016: fleet-view freshness — docs/fleet.csv (generated, gitignored)
#                     must exist locally and its registry columns must match
#                     config/projects.toml; skipped in CI, where the file never exists.
# v0.1 — 2026-06-07 — Bootstrap scaffold. No real checks yet; structural validation only.
# ==============================================================

import os
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
manifest = repo_root / "docs" / "documents_manifest.md"
folder_structure = repo_root / "docs" / "folder_structure.md"
claude_md = repo_root / "CLAUDE.md"

missing = []
if not manifest.exists():
    missing.append("docs/documents_manifest.md")
if not folder_structure.exists():
    missing.append("docs/folder_structure.md")
if not claude_md.exists():
    missing.append("CLAUDE.md")

if missing:
    print("ERROR: required governance docs missing:")
    for path in missing:
        print(f"  - {path}")
    sys.exit(1)

# PLAN-016: the fleet view is generated + gitignored — locally it must agree with the registry.
fleet_csv = repo_root / "docs" / "fleet.csv"
fleet_fix = "Fix: .venv/bin/python -m standard_document_updater fleet"
if not fleet_csv.exists():
    if not os.environ.get("CI"):
        print("ERROR: docs/fleet.csv missing (it is generated, never committed).")
        print(fleet_fix)
        sys.exit(1)
    print("fleet view: skipped in CI (docs/fleet.csv is generated locally, never committed)")
else:
    sys.path.insert(0, str(repo_root / "src"))
    from standard_document_updater.errors import StandardDocSetError
    from standard_document_updater.fleet import registry_mismatches

    try:
        problems = registry_mismatches(repo_root)
    except StandardDocSetError as exc:
        print(f"ERROR: fleet view check could not read the registry: {exc}")
        sys.exit(1)
    if problems:
        print("ERROR: docs/fleet.csv disagrees with config/projects.toml:")
        for problem in problems:
            print(f"  - {problem}")
        print(fleet_fix)
        sys.exit(1)
    print("fleet view: OK (docs/fleet.csv registry columns match config/projects.toml)")

# TODO: extend with project-specific drift checks
#   - every tracked .md present in documents_manifest.md
#   - every .py/.sh in scripts/ carries a VERSION header
#   - CLI flags / commands documented in docs/architecture.md (once the engine lands)

print("doc coverage: OK (scaffold — structural checks only)")
sys.exit(0)
