#!/usr/bin/env python3
# ==============================================================
# VERSION: 0.1
# Doc-coverage governance — surface drift between code, docs, and the manifest.
#
# Initial scaffold (permissive — exits 0). Extend with project-specific checks
# as the project grows: tracked .md presence in manifest, CLI flags documented,
# tracked code-file VERSION-header presence, etc.
#
# CHANGE LOG
# v0.1 — 2026-06-07 — Bootstrap scaffold. No real checks yet; structural validation only.
# ==============================================================

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

# TODO: extend with project-specific drift checks
#   - every tracked .md present in documents_manifest.md
#   - every .py/.sh in scripts/ carries a VERSION header
#   - CLI flags / commands documented in docs/architecture.md (once the engine lands)

print("doc coverage: OK (scaffold — structural checks only)")
sys.exit(0)
