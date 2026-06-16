# ==============================================================
# VERSION: 0.1
# Exception hierarchy for the Standard DocSet engine.
#
# CHANGE LOG
# v0.1 — 2026-06-16 13:01 — Initial: base error + RegistryError + ParseError.
# ==============================================================
"""Project-specific exceptions (per ENGINEERING_STANDARDS § 4.3)."""
from __future__ import annotations


class StandardDocSetError(Exception):
    """Base for all engine errors."""


class RegistryError(StandardDocSetError):
    """The projects registry is missing or malformed."""


class ParseError(StandardDocSetError):
    """A standards file could not be parsed for the expected value."""
