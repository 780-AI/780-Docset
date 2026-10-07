#!/usr/bin/env bash
# ==============================================================
# VERSION: 0.3
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
#   bash scripts/claude_project_data.sh cleanup  # remove this project's backups — each only when
#                                                # every file in it is also in the project folder
#
# The <path-key> is the repo's absolute path with every non-alphanumeric
# character replaced by "-" (Claude Code's own convention), so it changes
# whenever the folder moves — run `link` after any move/rename. On Windows the
# key is built from the drive form of the path (e:/dir/repo, drive lowercased).
#
# Never move, rename or delete the harness path in a file manager: it is a link, and
# Windows Explorer moves or deletes the real files behind a junction. Use this script.
#
# Windows (Git Bash): run `adopt` / `link` from a Git Bash window with Claude Code
# CLOSED for this project (a live session holds files in the harness dir; the tool
# refuses while a transcript changed in the last 2 minutes). There the harness dir is
# renamed to a backup in ~/.claude/locality-backups/ (<key>.pre-locality-<stamp>) —
# away from the link, on the same drive — its files are copied into the in-repo home
# without overwriting, and a junction is created. `cleanup` removes a backup once every
# file in it is in the project folder (same bytes, or grown); it never deletes through
# a link and never uses rm -r. Junctions are removed with rmdir, never rm.
#
# CHANGE LOG
# v0.3 — 2026-10-07 — PLAN-017 Phase 3b (a Windows adopter's lost-store incident): status
#         reports an EMPTY in-repo store as empty and says STOP instead of recommending
#         link, warns on an OK link with no memory files, and lists kept backups; Windows
#         backups go to ~/.claude/locality-backups/ instead of beside the link; adopt/link
#         warn never to handle the link in a file manager; new `cleanup` verb removes a
#         backup only when every file in it is in the store (verified file by file, never
#         rm -r, never through a link) and moves a kept old-location backup away from the link.
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
BACKUP_ROOT="$HOME/.claude/locality-backups"

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

has_files() {  # dir $1 exists and holds at least one file
  [ -d "$1" ] && [ -n "$(find "$1" -type f 2>/dev/null | head -n 1 || true)" ]
}

mem_count() {  # number of entries in $1/memory (0 when absent)
  { ls -1 "$1/memory" 2>/dev/null || true; } | wc -l | tr -d ' '
}

backups() {  # this project's locality backups: the backup root, then the old spot beside the link
  for b in "$BACKUP_ROOT/$KEY".pre-locality-* "$HOME/.claude/projects/$KEY".pre-locality-*; do
    if [ -e "$b" ] || [ -L "$b" ]; then printf '%s\n' "$b"; fi
  done
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

warn_link() {  # after a link is made: the one action that destroys data
  say "Note: never move, rename or delete $HARNESS_DIR in a file manager —"
  say "      it is a $LINKWORD to the project folder, and a file manager can move or delete the real files behind it."
}

status() {
  say "repo:          $REPO"
  say "path-key:      $KEY"
  say "harness path:  $HARNESS_DIR"
  say "physical home: $DATA"
  backups | while IFS= read -r b; do
    say "backup kept:   $b (once a new session shows your memories: bash scripts/claude_project_data.sh cleanup)"
  done
  if is_link "$HARNESS_DIR"; then
    say "$LINKWORD:       -> $(link_target "$HARNESS_DIR")"
    if points_home "$HARNESS_DIR"; then
      n="$(mem_count "$DATA")"
      say "STATUS: OK — data lives in the project folder ($n memory files)"
      if [ "$n" = 0 ]; then
        say "WARNING: no memory files — normal for a new project; if this project had memories before, STOP: they are not in the project folder."
      fi
    else
      say "STATUS: BROKEN — $LINKWORD does not resolve to this repo's project-data. Run: link"
      return 1
    fi
  elif [ -d "$HARNESS_DIR" ]; then
    if has_files "$DATA"; then
      say "STATUS: NOT LINKED — Claude Code created a real directory at the harness path, and in-repo data exists. Run: link"
    elif [ -d "$DATA" ]; then
      say "STATUS: NOT LINKED — the in-repo store is EMPTY (no files in .claude/project-data/); the harness directory holds $(mem_count "$HARNESS_DIR") memory files."
      say "        If this project had memories that are in neither place, STOP and recover them before running link (link would join Claude Code to an empty store). Otherwise run: link"
    else
      say "STATUS: NOT ADOPTED — real directory at the harness path (data outside the project folder). Run: adopt"
    fi
    return 1
  elif has_files "$DATA"; then
    say "STATUS: NOT LINKED — in-repo data exists but the harness path is absent (fresh machine / folder moved). Run: link"
    return 1
  elif [ -d "$DATA" ]; then
    say "STATUS: EMPTY — the in-repo store exists but holds no files, and the harness path is absent."
    say "        New project: run link. If this project had memories before, STOP and recover them first."
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
    mkdir -p "$BACKUP_ROOT"
    backup="$BACKUP_ROOT/$KEY.pre-locality-$(date +%Y%m%d-%H%M%S)"
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
    say "  backup kept at $backup — once a NEW Claude Code session shows your memories, run: bash scripts/claude_project_data.sh cleanup"
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
  say "Adopted."; warn_link; status
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
  say "Linked."; warn_link; status
}

backup_problems() {  # print every file of backup $1 the store does not hold with the same
                     # leading bytes, and every link in it; prints nothing when all is covered
  rb="$(readlink -f "$1")"
  ( cd "$1" && find . \( -type f -o -type l \) -print0 ) | while IFS= read -r -d '' rel; do
    rel="${rel#./}"
    f="$1/$rel"
    if [ -L "$f" ]; then say "link (never followed): $rel"; continue; fi
    case "$(readlink -f "$f")" in
      "$rb"/*) ;;
      *) say "reached through a link (never followed): $rel"; continue ;;
    esac
    if [ ! -f "$DATA/$rel" ]; then say "missing from the project folder: $rel"; continue; fi
    size="$(wc -c < "$f" | tr -d ' ')"
    if ! head -c "$size" "$DATA/$rel" | cmp -s - "$f"; then
      say "differs from the project folder copy: $rel"
    fi
  done
}

remove_backup() {  # delete the files of verified backup $1, then its emptied dirs — never rm -r
  ( cd "$1" && find . -type f -print0 ) | while IFS= read -r -d '' rel; do
    rm -f -- "$1/${rel#./}"
  done
  find "$1" -depth -type d -exec rmdir {} \; 2>/dev/null || true
  if [ -e "$1" ]; then say "  partly kept (not empty after removing verified files): $1"; else say "  removed: $1"; fi
}

cleanup() {  # remove this project's locality backups, each only when fully covered by the store
  if ! status >/dev/null; then
    say "cleanup refused — status is not OK. Run: bash scripts/claude_project_data.sh status"
    return 1
  fi
  list="$(backups)"
  if [ -z "$list" ]; then say "No backups to clean up for this project."; return 0; fi
  say "Checking backups (each is removed only when every file in it is also in the project folder):"
  printf '%s\n' "$list" | while IFS= read -r b; do
    if [ -L "$b" ] || is_link "$b"; then
      say "KEPT (a link, not a backup folder — remove it by hand only after checking): $b"
      continue
    fi
    problems="$(backup_problems "$b" || true)"
    if [ -z "$problems" ]; then remove_backup "$b"; continue; fi
    say "KEPT $b — not everything in it is in the project folder:"
    printf '%s\n' "$problems" | sed 's/^/    /'
    case "$b" in
      "$HOME/.claude/projects/"*)
        mkdir -p "$BACKUP_ROOT"
        if mv "$b" "$BACKUP_ROOT/"; then
          b="$BACKUP_ROOT/$(basename "$b")"
          say "    moved away from the link to: $b"
        fi
        ;;
    esac
    say "    Copy anything you need into $DATA; this backup is a plain folder (not the link) — delete it yourself once checked."
  done
}

case "${1:-status}" in
  status)  status ;;
  adopt)   adopt ;;
  link)    link ;;
  cleanup) cleanup ;;
  *) say "Usage: $0 [status|adopt|link|cleanup]"; exit 2 ;;
esac
