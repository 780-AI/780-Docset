#!/usr/bin/env bash
# ==============================================================
# VERSION: 0.1
# Claude project-data locality tool (CLAUDE.md Rule 14) — keeps the Claude Code
# per-project data (memory + session transcripts) physically INSIDE the project
# folder at <repo>/.claude/project-data/, with a symlink left at the harness
# path ~/.claude/projects/<path-key>/ so Claude Code keeps working unchanged.
#
# Usage:
#   bash scripts/claude_project_data.sh status   # report physical home + symlink health
#   bash scripts/claude_project_data.sh adopt    # one-time on a machine that already has
#                                                # data under ~/.claude: move it in + symlink
#   bash scripts/claude_project_data.sh link     # new machine, or after a folder move/rename:
#                                                # (re)point the harness path at the in-repo data,
#                                                # merging any stray harness-created dir first
#
# The <path-key> is the repo's absolute path with every non-alphanumeric
# character replaced by "-" (Claude Code's own convention), so it changes
# whenever the folder moves — run `link` after any move/rename.
#
# CHANGE LOG
# v0.1 — 2026-08-16 — Initial for this suite (PLAN-010 upstream intake): ported from an
#         upstream project's locality tool; added the pre-v1.5 memory-symlink layout
#         branch in adopt() (absorbs a harness dir whose memory/ entry symlinks to
#         <repo>/.claude/memory — the old Rule 14 mechanism). Replaces bootstrap_memory.sh.
# ==============================================================
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$REPO/.claude/project-data"
KEY="$(printf '%s' "$REPO" | sed 's#[^A-Za-z0-9]#-#g')"
HARNESS_DIR="$HOME/.claude/projects/$KEY"

say() { printf '%s\n' "$*"; }

status() {
  say "repo:          $REPO"
  say "path-key:      $KEY"
  say "harness path:  $HARNESS_DIR"
  say "physical home: $DATA"
  if [ -L "$HARNESS_DIR" ]; then
    target="$(readlink "$HARNESS_DIR")"
    say "symlink:       -> $target"
    if [ "$target" = "$DATA" ] && [ -d "$DATA" ]; then
      say "STATUS: OK — data lives in the project folder ($(ls -1 "$DATA/memory" 2>/dev/null | wc -l | tr -d ' ') memory files)"
    else
      say "STATUS: BROKEN — symlink does not resolve to this repo's project-data. Run: link"
      return 1
    fi
  elif [ -d "$HARNESS_DIR" ]; then
    say "STATUS: NOT ADOPTED — real directory at the harness path (data outside the project folder). Run: adopt"
    return 1
  elif [ -d "$DATA" ]; then
    say "STATUS: NOT LINKED — in-repo data exists but the harness path is absent (fresh machine / folder moved). Run: link"
    return 1
  else
    say "STATUS: EMPTY — no data on either side (brand-new project on this machine). Run: link (creates the home + symlink)"
    return 1
  fi
}

merge_dir_into_data() {
  # move contents of a real dir ($1) into $DATA without clobbering
  find "$1" -mindepth 1 -maxdepth 1 -print0 | while IFS= read -r -d '' item; do
    base="$(basename "$item")"
    if [ -e "$DATA/$base" ]; then
      say "  skip (exists at destination): $base"
    else
      mv "$item" "$DATA/" && say "  moved: $base"
    fi
  done
}

adopt() {
  if [ -L "$HARNESS_DIR" ]; then
    say "Already adopted — harness path is a symlink."; status; return 0
  fi
  if [ ! -d "$HARNESS_DIR" ]; then
    say "Nothing to adopt at $HARNESS_DIR — use: link"; return 1
  fi
  mkdir -p "$REPO/.claude"
  # Pre-v1.5 layout (old Rule 14): harness dir is real, but its memory/ entry is a
  # symlink to <repo>/.claude/memory — absorb both halves before the generic merge.
  if [ -L "$HARNESS_DIR/memory" ]; then
    rm "$HARNESS_DIR/memory"
    if [ -d "$REPO/.claude/memory" ] && [ ! -e "$DATA/memory" ]; then
      mkdir -p "$DATA"
      mv "$REPO/.claude/memory" "$DATA/memory"
      say "  absorbed old in-repo memory store -> project-data/memory"
    fi
  fi
  if [ -d "$DATA" ]; then
    say "In-repo home exists — merging harness dir into it:"
    merge_dir_into_data "$HARNESS_DIR"
    leftover="$(find "$HARNESS_DIR" -mindepth 1 | head -1)"
    if [ -n "$leftover" ]; then
      say "ABORT: harness dir not empty after merge (name collisions above) — resolve manually."; return 1
    fi
    rmdir "$HARNESS_DIR"
  else
    mv "$HARNESS_DIR" "$DATA"
  fi
  ln -s "$DATA" "$HARNESS_DIR"
  say "Adopted."; status
}

link() {
  mkdir -p "$DATA"
  if [ -L "$HARNESS_DIR" ]; then
    target="$(readlink "$HARNESS_DIR")"
    if [ "$target" = "$DATA" ]; then say "Already linked."; status; return 0; fi
    say "Re-pointing stale symlink (was -> $target)"
    rm "$HARNESS_DIR"
  elif [ -d "$HARNESS_DIR" ]; then
    say "Harness-created dir found (session started before link) — merging it in:"
    merge_dir_into_data "$HARNESS_DIR"
    leftover="$(find "$HARNESS_DIR" -mindepth 1 | head -1)"
    if [ -n "$leftover" ]; then
      say "ABORT: harness dir not empty after merge (name collisions above) — resolve manually."; return 1
    fi
    rmdir "$HARNESS_DIR"
  fi
  mkdir -p "$HOME/.claude/projects"
  ln -s "$DATA" "$HARNESS_DIR"
  say "Linked."; status
}

case "${1:-status}" in
  status) status ;;
  adopt)  adopt ;;
  link)   link ;;
  *) say "Usage: $0 [status|adopt|link]"; exit 2 ;;
esac
