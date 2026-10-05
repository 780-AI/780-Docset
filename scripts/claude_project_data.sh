#!/usr/bin/env bash
# ==============================================================
# VERSION: 0.2
# Claude project-data locality tool (CLAUDE.md Rule 14) — keeps the Claude Code
# per-project data (memory + session transcripts) physically INSIDE the project
# folder at <repo>/.claude/project-data/, with a link left at the harness path
# ~/.claude/projects/<path-key>/ so Claude Code keeps working unchanged — a
# symlink on macOS / Linux, a directory junction on Windows (Git Bash).
#
# Usage:
#   bash scripts/claude_project_data.sh status   # report physical home + link health
#   bash scripts/claude_project_data.sh adopt    # one-time on a machine that already has
#                                                # data under ~/.claude: move it in + link
#   bash scripts/claude_project_data.sh link     # new machine, or after a folder move/rename:
#                                                # (re)point the harness path at the in-repo data,
#                                                # merging any stray harness-created dir first
#
# The <path-key> is the repo's absolute path with every non-alphanumeric
# character replaced by "-" (Claude Code's own convention), so it changes
# whenever the folder moves — run `link` after any move/rename. On Windows the
# key is built from the drive form of the path (e:/dir/repo, drive lowercased).
#
# Windows (Git Bash): run `adopt` / `link` from a Git Bash window with Claude Code
# CLOSED for this project (a live session holds files in the harness dir; the tool
# refuses while a transcript changed in the last 2 minutes). There the harness dir is
# renamed to a backup (<key>.pre-locality-<stamp>), its files are copied into the
# in-repo home without overwriting, and a junction is created; the backup stays until
# you delete it. Junctions are removed with rmdir, never rm.
#
# CHANGE LOG
# v0.2 — 2026-10-05 — PLAN-017: Windows (Git Bash) support — drive-form path-key, directory
#         junction (mklink /J) in place of the symlink, junctions removed with rmdir (never
#         rm), rename-to-backup + no-overwrite copy in place of mv, refusal while a session
#         is live. An adopter's E002: the merge recurses into same-name dirs and drops the
#         empty ones Claude Code creates (link/adopt no longer abort on its empty memory/);
#         status names `link`, not `adopt`, when in-repo data already exists; link absorbs
#         the pre-v1.5 memory layout too.
# v0.1 — 2026-08-16 — Initial for this suite (PLAN-010 upstream intake): ported from an
#         upstream project's locality tool; added the pre-v1.5 memory-symlink layout
#         branch in adopt() (absorbs a harness dir whose memory/ entry symlinks to
#         <repo>/.claude/memory — the old Rule 14 mechanism). Replaces bootstrap_memory.sh.
# ==============================================================
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$REPO/.claude/project-data"

case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) WINDOWS=1; LINKWORD="junction" ;;
  *) WINDOWS=0; LINKWORD="symlink" ;;
esac

if [ "$WINDOWS" = 1 ]; then
  WINPATH="$(cygpath -m "$REPO")"
  DRIVE="$(printf '%s' "$WINPATH" | cut -c1 | tr '[:upper:]' '[:lower:]')"
  KEY="$(printf '%s%s' "$DRIVE" "$(printf '%s' "$WINPATH" | cut -c2-)" | sed 's#[^A-Za-z0-9]#-#g')"
else
  KEY="$(printf '%s' "$REPO" | sed 's#[^A-Za-z0-9]#-#g')"
fi
HARNESS_DIR="$HOME/.claude/projects/$KEY"

say() { printf '%s\n' "$*"; }

is_link() {  # $1 is a symlink, or (Windows) a junction Git Bash may not report as one
  [ -L "$1" ] && return 0
  if [ "$WINDOWS" = 1 ] && [ -e "$1" ]; then
    [ "$(readlink -f "$1")" != "$(readlink -f "$(dirname "$1")")/$(basename "$1")" ]
    return
  fi
  return 1
}

link_target() {
  if [ "$WINDOWS" = 1 ]; then readlink -f "$1"; else readlink "$1"; fi
}

points_home() {  # the link at $1 resolves to this repo's project-data
  if [ "$WINDOWS" = 1 ]; then
    [ -d "$DATA" ] && [ "$(readlink -f "$1")" = "$(readlink -f "$DATA")" ]
  else
    [ "$(readlink "$1")" = "$DATA" ] && [ -d "$DATA" ]
  fi
}

make_link() {  # harness path -> $DATA
  mkdir -p "$(dirname "$HARNESS_DIR")"
  if [ "$WINDOWS" = 1 ]; then
    cmd //c mklink //J "$(cygpath -w "$HARNESS_DIR")" "$(cygpath -w "$DATA")" >/dev/null
  else
    ln -s "$DATA" "$HARNESS_DIR"
  fi
}

drop_link() {  # remove the link at $1 — never what it points to
  if [ "$WINDOWS" = 1 ]; then
    cmd //c rmdir "$(cygpath -w "$1")" >/dev/null
  else
    rm "$1"
  fi
}

status() {
  say "repo:          $REPO"
  say "path-key:      $KEY"
  say "harness path:  $HARNESS_DIR"
  say "physical home: $DATA"
  if is_link "$HARNESS_DIR"; then
    say "$LINKWORD:       -> $(link_target "$HARNESS_DIR")"
    if points_home "$HARNESS_DIR"; then
      say "STATUS: OK — data lives in the project folder ($(ls -1 "$DATA/memory" 2>/dev/null | wc -l | tr -d ' ') memory files)"
    else
      say "STATUS: BROKEN — $LINKWORD does not resolve to this repo's project-data. Run: link"
      return 1
    fi
  elif [ -d "$HARNESS_DIR" ]; then
    if [ -d "$DATA" ]; then
      say "STATUS: NOT LINKED — Claude Code created a real directory at the harness path, and in-repo data exists. Run: link"
    else
      say "STATUS: NOT ADOPTED — real directory at the harness path (data outside the project folder). Run: adopt"
    fi
    return 1
  elif [ -d "$DATA" ]; then
    say "STATUS: NOT LINKED — in-repo data exists but the harness path is absent (fresh machine / folder moved). Run: link"
    return 1
  else
    say "STATUS: EMPTY — no data on either side (brand-new project on this machine). Run: link (creates the home + $LINKWORD)"
    return 1
  fi
}

merge_dir_into() {  # move the contents of real dir $1 into dir $2 without clobbering;
                    # same-name dirs merge recursively and are dropped once empty (E002)
  find "$1" -mindepth 1 -maxdepth 1 -print0 | while IFS= read -r -d '' item; do
    base="$(basename "$item")"
    dest="$2/$base"
    if [ ! -e "$dest" ] && [ ! -L "$dest" ]; then
      mv "$item" "$2/" && say "  moved: $base"
    elif [ -d "$item" ] && [ ! -L "$item" ] && [ -d "$dest" ] && [ ! -L "$dest" ]; then
      merge_dir_into "$item" "$dest"
      if rmdir "$item" 2>/dev/null; then say "  merged: $base/"; fi
    else
      say "  skip (exists at destination): $base"
    fi
  done
}

copy_missing() {  # copy every file under $1 that is absent under $2 — never overwrite
  ( cd "$1" && find . -type f -print0 ) | while IFS= read -r -d '' rel; do
    rel="${rel#./}"
    if [ -e "$2/$rel" ]; then
      say "  skip (exists at destination): $rel"
    else
      mkdir -p "$2/$(dirname "$rel")"
      cp -p "$1/$rel" "$2/$rel" || { say "  FAILED to copy: $rel"; exit 1; }
    fi
  done
}

absorb_old_memory() {  # pre-v1.5 layout (old Rule 14): $1/memory links to <repo>/.claude/memory
  if is_link "$1/memory"; then
    drop_link "$1/memory"
    if [ -d "$REPO/.claude/memory" ] && [ ! -e "$DATA/memory" ]; then
      mkdir -p "$DATA"
      mv "$REPO/.claude/memory" "$DATA/memory"
      say "  absorbed old in-repo memory store -> project-data/memory"
    elif [ -d "$REPO/.claude/memory" ]; then
      say "  note: project-data/memory already exists — the old store stays at .claude/memory; merge it by hand"
    fi
  fi
}

absorb_harness_dir() {  # bring the real dir at the harness path into $DATA; frees the path
  if [ "$WINDOWS" = 1 ]; then
    recent="$(find "$HARNESS_DIR" -maxdepth 1 -name '*.jsonl' -mmin -2 2>/dev/null | head -n 1 || true)"
    if [ -n "$recent" ]; then
      say "ABORT: a Claude Code session for this project looks active (a transcript changed in the last 2 minutes)."
      say "       Close Claude Code, then run this again from a Git Bash window."
      return 1
    fi
    backup="$HARNESS_DIR.pre-locality-$(date +%Y%m%d-%H%M%S)"
    if ! mv "$HARNESS_DIR" "$backup"; then
      say "ABORT: could not move the harness dir aside (in use?) — close Claude Code and retry."
      return 1
    fi
    say "Harness dir moved aside to $backup — copying its data in (nothing is overwritten)."
    say "  (if anything below fails, restore with: mv \"$backup\" \"$HARNESS_DIR\")"
    absorb_old_memory "$backup"
    mkdir -p "$DATA"
    if ! copy_missing "$backup" "$DATA"; then
      say "ABORT: copy failed — nothing was deleted; the original is still at $backup"
      return 1
    fi
    say "  original kept at $backup — delete it once Claude Code shows your memories"
    return 0
  fi
  absorb_old_memory "$HARNESS_DIR"
  if [ -d "$DATA" ]; then
    say "$1"
    merge_dir_into "$HARNESS_DIR" "$DATA"
    leftover="$(find "$HARNESS_DIR" -mindepth 1 | head -n 1 || true)"
    if [ -n "$leftover" ]; then
      say "ABORT: harness dir not empty after merge (name collisions above) — resolve manually."; return 1
    fi
    rmdir "$HARNESS_DIR"
  else
    mv "$HARNESS_DIR" "$DATA"
  fi
}

adopt() {
  if is_link "$HARNESS_DIR"; then
    say "Already adopted — harness path is a $LINKWORD."; status; return 0
  fi
  if [ ! -d "$HARNESS_DIR" ]; then
    say "Nothing to adopt at $HARNESS_DIR — use: link"; return 1
  fi
  mkdir -p "$REPO/.claude"
  absorb_harness_dir "In-repo home exists — merging harness dir into it:"
  make_link
  say "Adopted."; status
}

link() {
  mkdir -p "$DATA"
  if is_link "$HARNESS_DIR"; then
    if points_home "$HARNESS_DIR"; then say "Already linked."; status; return 0; fi
    say "Re-pointing stale $LINKWORD (was -> $(link_target "$HARNESS_DIR"))"
    drop_link "$HARNESS_DIR"
  elif [ -d "$HARNESS_DIR" ]; then
    absorb_harness_dir "Harness-created dir found (session started before link) — merging it in:"
  fi
  make_link
  say "Linked."; status
}

case "${1:-status}" in
  status) status ;;
  adopt)  adopt ;;
  link)   link ;;
  *) say "Usage: $0 [status|adopt|link]"; exit 2 ;;
esac
