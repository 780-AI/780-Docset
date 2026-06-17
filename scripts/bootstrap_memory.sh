#!/usr/bin/env bash
# ==============================================================
# VERSION: 0.1
# Re-point Claude's per-project memory dir at the in-repo, Dropbox-synced store.
#
# WHY: Claude memory normally lives at
#   ~/.claude/projects/<sanitized-abs-path>/memory/
# which is (a) machine-local (NOT inside the project folder, so Dropbox never
# carries it) and (b) keyed by the folder's absolute path (so renaming/moving
# the folder orphans it). A new machine + a folder move wiped it once already.
#
# FIX: keep the real memory files inside the repo at <repo>/.claude/memory/
# (rides Dropbox, survives renames) and symlink the harness key dir to them.
# Run this once on every new machine and after any folder move/rename.
#
# CHANGE LOG
# v0.1 — 2026-06-17 — Initial: derive key from repo path, create/refresh symlink.
# ==============================================================
set -euo pipefail

# Repo root = parent of this script's dir (scripts/). MEM_STORE is the in-repo store.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
MEM_STORE="$REPO_ROOT/.claude/memory"

# Harness key: absolute path with '/' and ' ' replaced by '-'.
KEY="$(printf '%s' "$REPO_ROOT" | sed 's#/#-#g; s/ /-/g')"
KEY_DIR="$HOME/.claude/projects/$KEY"
LINK="$KEY_DIR/memory"

mkdir -p "$MEM_STORE"
mkdir -p "$KEY_DIR"

if [ -L "$LINK" ]; then
  # Already a symlink — refresh its target (handles a stale post-rename target).
  rm "$LINK"
elif [ -d "$LINK" ]; then
  # A real dir already lives there. Preserve any files it holds, then replace.
  if [ -n "$(ls -A "$LINK" 2>/dev/null)" ]; then
    echo "note: copying pre-existing harness memory into the repo store before linking"
    cp -an "$LINK"/. "$MEM_STORE"/ 2>/dev/null || true
    mv "$LINK" "$LINK.pre-symlink.bak"
    echo "note: original harness memory dir backed up at $LINK.pre-symlink.bak"
  else
    rmdir "$LINK"
  fi
elif [ -e "$LINK" ]; then
  echo "error: $LINK exists and is neither a dir nor a symlink — resolve manually" >&2
  exit 1
fi

ln -s "$MEM_STORE" "$LINK"

echo "linked:  $LINK"
echo "    ->   $MEM_STORE"
echo "key:     $KEY"
echo "files in store: $(ls -1 "$MEM_STORE" 2>/dev/null | wc -l | tr -d ' ')"
