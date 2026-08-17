#!/usr/bin/env bash
# ==============================================================
# VERSION: 0.1
# Per-machine installer for the standard-docset delivery skill: symlinks
# ~/.claude/skills/standard-docset -> <this repo>/skill so Claude Code loads
# the skill from the live vault (PLAN-009, Set v2.0). Idempotent; machine-local
# state cataloged in docs/NEW_MACHINE_SETUP.md per CLAUDE.md Rule 14.
#
# CHANGE LOG
# v0.1 — 2026-08-16 — Initial (PLAN-009).
# ==============================================================
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$REPO/skill"
LINK="$HOME/.claude/skills/standard-docset"

[ -f "$TARGET/SKILL.md" ] || { echo "ERROR: $TARGET/SKILL.md missing — run from a vault checkout."; exit 1; }

mkdir -p "$HOME/.claude/skills"
if [ -L "$LINK" ]; then
  current="$(readlink "$LINK")"
  if [ "$current" = "$TARGET" ]; then
    echo "Already installed: $LINK -> $TARGET"
    exit 0
  fi
  echo "Re-pointing (was -> $current)"
  rm "$LINK"
elif [ -e "$LINK" ]; then
  echo "ERROR: $LINK exists and is not a symlink — resolve manually."
  exit 1
fi
ln -s "$TARGET" "$LINK"
echo "Installed: $LINK -> $TARGET"
echo "New Claude Code sessions on this machine will list the 'standard-docset' skill."
