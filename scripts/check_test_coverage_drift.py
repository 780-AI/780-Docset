#!/usr/bin/env python3
# ==============================================================
# VERSION: 0.1
# Test-coverage-drift governance — code ↔ test ↔ doc ownership map.
#
# Initial scaffold (permissive — exits 0). Extend per VALIDATION_STANDARDS § 4
# once the engine grows monitored source paths under src/standard_document_updater/.
# "tests" here means the pytest suite plus fixture-based runs against sample
# target repositories (golden-file comparisons of diff / merge / version-bump output).
#
# CHANGE LOG
# v0.1 — 2026-06-07 — Bootstrap scaffold. Validates validation_ownership.toml presence only.
# ==============================================================

import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
ownership = repo_root / "scripts" / "validation_ownership.toml"
allowlist = repo_root / "scripts" / "doc_coverage_allowlist.toml"

missing = []
if not ownership.exists():
    missing.append("scripts/validation_ownership.toml")
if not allowlist.exists():
    missing.append("scripts/doc_coverage_allowlist.toml")

if missing:
    print("ERROR: required governance configs missing:")
    for path in missing:
        print(f"  - {path}")
    sys.exit(1)

# Accept --ci flag (CI mode — currently no behavior difference)
ci_mode = "--ci" in sys.argv

# TODO: extend per VALIDATION_STANDARDS § 4
#   - parse validation_ownership.toml
#   - for each rule, verify source/test/doc paths exist
#   - flag rule-orphans (rules referencing missing paths)
#   - flag path-orphans (source files in monitored areas without an owning rule)

print(f"test coverage drift: OK (scaffold — ownership-map checks not yet active; ci_mode={ci_mode})")
sys.exit(0)
