# ==============================================================
# VERSION: 0.1
# Module entry point for `python -m standard_document_updater`.
#
# CHANGE LOG
# v0.1 — 2026-06-16 13:01 — Initial: delegate to cli.main().
# ==============================================================
"""Enable `python -m standard_document_updater`."""
from __future__ import annotations

from standard_document_updater.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
