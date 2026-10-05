<!-- VERSION: 0.3 -->
<!-- Last Updated: 2026-10-05 -->
<!-- Status: EXECUTING (Phase 3 shipped 2026-10-05; QA-M8 / M9 open on the owner's Windows PC) -->
<!--
CHANGE LOG
v0.3 — 2026-10-05 — Phase 3 executed in a fresh session. Reconcile pass: all 33 blocks re-extracted from
this file, every FIND / pre-image / absence check passed on the live trees — zero block defects. § 5
applied byte-for-byte with `<P3-DATE>` = 2026-10-05 (clock checked against gitlab.com / apple.com).
Estimator: prep `b4cae64` + the engine's sync `fdb87b9` on their `main` (the fleet's first live git
write); vault: tool 0.2 + tests, registry entry, opener row, skill, folder tree; Capital-Signal E002
written back. QA-M1…M7 + M10 ✅ (evidence in the tracker). Plan defect D1 (wording; operator D1 = A):
§ 8.1 listed the merge / record files only — the dry-run also removes 3 non-header lines from the
replace-mode MEMORY_PROTOCOL, explained before the write (the target's replace-mode copies are
byte-identical to `set-v1.3`; the lines are the v2.2 identifier scrub) — § 8.1 gains one sentence.
Process note: QA-M7's idle re-check printed instead of gating (tracker). Status APPROVED → EXECUTING.
v0.2 — 2026-10-05 — Phase 2 operator approval recorded ("Plan-017 is approved"); § 9.1 decision record
added: D17.A approved; D-1…D-5 = A (the recommended options the § 5 code and the § 5n entry implement).
No § 5 change — the 33 blocks re-extracted from this file stay byte-identical to the proven blocks.
Status DRAFT → APPROVED.
v0.1 — 2026-10-05 — Initial draft. § 15.9 intake (operator request, no document) → Rule 16 gate
(12 candidates; operator: "yes to all recommended") → Phase 0 audit (read-only: a scratch clone of
780-estimator `45d7c75`) → Phase 1 design. Code proven FIRST in scratch overlays: the locality tool
v0.2 + 11 tests (ruff clean, mypy --strict 0 in 25 files, pytest 151 = 140 + 11; positive control —
the same tests against v0.1 fail exactly the 6 new-behavior cases); the whole catch-up run end-to-end
over the git transport against a local bare remote standing in for GitHub (status behind → dry-run
7/11 → write 8 files in one engine commit → re-run up-to-date 11/11 → status current). § 5 is
GENERATED from the proven blocks (no hand-copying). Rule 13 pass run the same day on the complete
plan + tracker (record at the foot): blocks RE-EXTRACTED from this file onto fresh copies of both
repos — QA-M1 / M2 / M10 green, the catch-up reproduced over the git transport with § 8.1's counts
exact; 1 defect (domain-neutrality of the delivered tool) + 1 ordering defect (§ 5d/5e before the
prep push) + 3 cross-section gaps fixed; 2 optimizations applied, 2 declined.
-->

# PLAN-017 — 780-estimator catch-up (Set v1.3 → v2.7, the first git target) + a Windows-capable locality tool

## 1. Goal

Bring **780-estimator** — a team project (owner Bahereh Hassanpour, GitHub `780-AI/780-estimator`)
that bootstrapped the suite at **Set v1.3** on 2026-06-21 and has run under the contract since — onto
the vault's current Set and under `sync` for good, **without breaking its owner's Claude memory on
Windows**:

1. **Make the project-data locality tool Windows-capable** (`scripts/claude_project_data.sh` 0.1 →
   0.2): the synced Rule 14 makes every estimator session call it, and v0.1 only works on macOS /
   Linux. Absorbs the two Rule 16 intake items confirmed for this plan (§ 2): the estimator's own
   Windows junction logic and Capital-Signal's E002.
2. **One-time prep commit in the estimator** (the old-SETUP catch-up path, SKILL.md): v1.6 heading
   wrap of the session opener + closer, `docs/SET_VERSION_ADOPTED.md` in the engine's sync-ready shape,
   the locality tool copied in, and the two pieces of local text the sync would otherwise drop moved
   into PROJECT-OWNED blocks (or accepted at the gate).
3. **Register and catch up**: a `git`-transport registry entry (the fleet's first) with the full fleet
   keys, then `sync --write` — the engine's first live git write, Delivery A (direct to `main`).
4. **Verify on the owner's Windows PC** (Rule 15): the `adopt` migration and the handoff landing.

After this plan the fleet has five targets on all three transports, and the old-SETUP catch-up path
is documented completely in the skill.

## 2. Operator constraints + intake record (binding)

- **Operator inputs (2026-10-05):** name `780-estimator`; repo `https://github.com/780-AI/780-estimator`;
  owner Bahereh Hassanpour; **Delivery A** (direct + handoff); Bahereh works on a **Windows PC**
  (confirmed); **transport = git** (operator chose it over ssh after the comparison: a Windows PC has no
  rsync and is often unreachable; git commits cannot be silently discarded); **Option A** — the locality
  tool is fixed inside this plan; the operator **will tell Bahereh** before the first push.
- **§ 15.9 intake:** no feature document (operator request only) — step 1's copy is skipped, never the
  discipline; the investigation (step 2) is the § 3 Phase 0 audit; the design's core hypothesis was
  pre-tested end-to-end before approval (§ 3, "numbers").
- **Rule 16 gate — record (2026-10-05).** Complete list presented in chat (all 60 commits, governance
  files, CHANGELOG, 44 plan files, scripts scanned; Bahereh's machine-local Claude memory not reachable
  and not scanned). Operator: **"yes to all recommended"**. Dispositions:

  | # | Candidate (source) | Disposition |
  |---|---|---|
  | 1 | Windows junction support (estimator `scripts/bootstrap_memory.sh`, bootstrap `66ac85c`) | **integrate (genericized)** — § 5a |
  | 2 | CS E002 — locality tool aborts after a folder move (Capital-Signal `STANDARDS_LOG.md` E002) | **integrate** — § 5a; Status write-back § 5p; delivery to existing adopters → v2.8 (D-2) |
  | 3 | "Ask in plain chat, never via popup" (estimator `CLAUDE.md` § 10 + opener § 3.2 row 1, `8b7f1fe`) | **kept project-local** — the § 3.2 row survives the sync; the § 10 line is dropped by it (accepted) |
  | 4 | Verify an environmental premise before designing (estimator PLAN-013 § 14.4) | **v2.8** — a data-point paragraph in L080 |
  | 5 | A TLS handshake is not reachability (estimator CHANGELOG, PLAN-014) | **v2.8** — genericized new lesson |
  | 6 | ALLOWLIST-count governance check (estimator CHANGELOG, PLAN-011) | covered by L038; automation idea → the queued mechanize-checks candidate |
  | 7 | Header vs own change log (estimator CHANGELOG, PLAN-012) | covered by L063 |
  | 8 | Rule 13 tested one input size (estimator PLAN-004 v0.3) | **v2.8** — data point for the queued Rule 13 checklist candidate |
  | 9 | Re-base version bumps before Phase 3 (estimator PLAN-002b § 4) | covered by L056 |
  | 10 | Stale push markers (estimator PLAN-006c) | covered by L055 |
  | 11 | `PLAN-NNN_rules_n_assumptions.md` companion files (estimator `docs/Plans/`) | **kept project-local** |
  | 12 | The estimator's two governance scripts | nothing to take (a project scaffold) |

  None of the 12 is an `E0NN` log entry except #2, so nothing else is marked `rejected` anywhere;
  the v2.8 items are queued in `docs/Plans/OPEN_TASKS.md`.
- **The owner's repo is theirs.** Only governance files + the one new script are touched; no runtime,
  domain, test or data path under `src/`, `tests/`, `scripts/run_daily.sh`, `requirements*`, `.env*`.
- **Never assume paths / hosts** — every value in § 5d came from the operator or the live repo.
- **Rule 4 in both repos** — every curator-made commit uses `git commit -F <file>`.
- **Plan-first, two-session split** (§ 15.3) — Phase 3 runs in a fresh session from this file.
- **Clock trust (L079)** — the Phase 3 date is checked against an external time authority; the
  engine refuses to stamp behind the target's newest stamp.

## 3. Scope summary

**In scope**

- **S1 — locality tool 0.2 (vault):** Windows (Git Bash) branch — drive-form path-key, directory
  junction via `mklink /J`, junctions removed only with `rmdir` (never `rm` — `rm -r` on a junction can
  follow into the target), rename-to-backup + no-overwrite copy in place of `mv` (Windows cannot move a
  directory a live session holds; the harness dir and the repo often sit on different drives),
  refusal while a transcript changed in the last 2 minutes; E002 — the merge recurses into same-name
  dirs and drops the empty ones Claude Code creates, `status` names `link` when in-repo data exists,
  `link` absorbs the pre-v1.5 layout too. POSIX behavior otherwise unchanged (the four Mac/Linux
  targets and the vault itself). New test module (11 cases incl. a Windows branch through stand-in
  `uname` / `cygpath` / `cmd`).
- **S2 — skill fix (vault):** SKILL.md's old-SETUP paragraph names the whole prep (it named only the
  heading wrap; this audit hit the other two gaps).
- **S3 — estimator prep commit** (§ 5h–5n; message § 5o), pushed to their `main`.
- **S4 — registration + catch-up:** registry entry (§ 5d) + SESSION_OPENER § 2 row (§ 5e); `sync
  --project 780-estimator --write` over git (one engine commit, author "Standard DocSet").
- **S5 — CS E002 write-back** (§ 5p) via `integrate --apply`.
- **S6 — Windows verification** (QA-M8) + landing observation (QA-M9), then closure.

**Out of scope (routed)**

- Delivering tool 0.2 to the four existing adopters (none is on Windows; E002's delivery half) →
  v2.8, where the script-delivery path is designed (D-2). Sync cannot carry it today: `scripts/` is not
  a SYNC_MAP item and the ssh transport materializes only `docs/` + `archive/` + `CLAUDE.md`.
- Handoff wording for committed (git) writes → PLAN-014 (PLAN-013 R6); explained to the owner in the
  prep CHANGELOG entry meanwhile (D-4).
- Rule 16 items 4, 5, 8 → the v2.8 release.
- The estimator's CI: its repo is on GitHub but carries only `.gitlab-ci.yml`, so its Rule 2 CI half
  never runs — reported to the owner (§ 5n entry is silent on it; the operator relays), not fixed here.
- PR delivery / DD-6b (PLAN-014) — Delivery A makes it unnecessary for this repo.
- Template wording: Rule 14 (`docs/standards/CLAUDE.md:250-254`) and the opener / closer say
  "symlink"; on Windows it is a junction — a `docs/standards/` edit (Set bump), queued for v2.8.

### Phase 0 audit findings (2026-10-05, read-only; estimator `main` = `45d7c75`, vault `8b914db`)

- **The repo:** 60 commits, one author (bahereh), first `66ac85c` 2026-06-21 "Bootstrap: install
  Standard Set v1.3"; after bootstrap the governance layer changed only in `8b7f1fe` (ask inline) and
  in its § 4 Critical Files (PROJECT-OWNED). `archive/LESSONS.md` = exactly L001–L051 (the v1.3
  canon); `docs/STANDARDS_LOG.md` has no entries; `.claude/` is gitignored (`.gitignore:70-72`).
  Platform: `scripts/bootstrap_memory.sh` carries a MINGW/MSYS branch (`cygpath -m`, lowercased drive,
  `cmd //c mklink //J`, example path `E:/Bahereh_780/...`).
- **Why the engine refuses it today:** `setversion.py:33` reads `**Standard Set Version:**` (the
  estimator writes `**Set Version:**` → adopted `?`); `sync.py:212-233` `record_adoption` needs that
  bullet + `**Adopted on:**` + the backport table, and `sync.py:145` the CHANGE LOG header; `sync.py`
  `plan_target` stops at the first PROJECT-OWNED count mismatch — opener 2 vs 3, closer 1 vs 2
  (CLAUDE.md 4 = 4). Measured: `sync` dry-run → `SESSION_OPENER.md: PROJECT-OWNED block count mismatch
  (template 3 vs target 2)`.
- **After the prep (scratch proof):** `status` v1.3 / v2.7 behind; dry-run **7 of 11** need sync
  (CLAUDE.md, PROJECT_STANDARDS, MEMORY_PROTOCOL, LESSONS, opener, closer, SVA; PROMPT / ENGINEERING /
  VALIDATION / CICD byte-identical). Removed-lines review in § 8.1.
- **Git transport** (`transport.py:112-146`): a writable `--depth 1` clone of the branch; `flush` =
  `git add` + `commit -m` as `Standard DocSet <standard-docset@localhost>` (`transport.py:41-42`) +
  `push origin HEAD:main` — no force, so a concurrent push makes the write fail, never overwrite. The
  handoff rides the same commit (`cli.py:249-266`). Proven locally against a bare remote: one engine
  commit, 8 files, parent = the prep commit; re-run up-to-date 11/11; `status` current.
- **Access:** the operator's GitHub key reads the repo (`ls-remote`) and a no-op `push --dry-run` was
  accepted (GitHub refuses the receive-pack connection to keys without write access); the first real
  push is the proof.
- **Locality tool 0.1** (`scripts/claude_project_data.sh`): key from the POSIX path (`:31`), `ln -s`
  (`:103`, `:124`), the merge skips same-name entries (`:62-72`) so a harness-created `memory/` makes
  `link` / `adopt` abort (`:95-98`, `:117-120`) — E002; no Windows branch. The synced suite calls it
  from template Rule 14 (`docs/standards/CLAUDE.md:251-256`), opener § 1.5
  (`docs/standards/SESSION_OPENER.md:82`) and closer § 1.6 (`docs/standards/SESSION_CLOSER.md:99`).
- **Skill:** `skill/SKILL.md:58-61` lists only the heading wrap for an old-SETUP catch-up.
- **E002 write-back format** (`integrate.py:157-165`): dry-run against the real Capital-Signal log
  parses and resolves the entry (§ 5p).
- **Tool baseline:** ruff clean; `MYPYPATH=src mypy --cache-dir <fresh>` → 0 issues in 24 files
  (without `MYPYPATH` the editable install yields 49 `import-untyped` errors — an environment effect,
  not code); pytest 140.

## 4. Phase tracker (high-level — granular sub-tasks in `PLAN-017_tracker.md`)

| Phase | What | Status |
|---|---|---|
| 0 | Audit (read-only) | ✅ 2026-10-05 |
| 1 | Design + proven code + Rule 13 pass | ✅ 2026-10-05 |
| 2 | Operator approval | ✅ 2026-10-05 |
| 3 | Implement — fresh session: 3.0 pre-checks → 3.1 reconcile → 3.2 vault tool + skill blocks → 3.3 estimator prep commit + push → 3.4 registry + catch-up write → 3.5 CS E002 write-back → 3.6 vault commit | ✅ 2026-10-05 |
| 4 | Validate — QA-M1…M7 inside Phase 3; QA-M8 / M9 on the owner's PC | 🔄 M1…M7 + M10 ✅ 2026-10-05; M8 / M9 ⏸ |
| 5 | Operator gate — vault push (both remotes); closure commit after QA-M8 / M9 | ⏸ |

## 5. Verbatim transformation rules (code proven in scratch; Phase 3 copies byte-for-byte)

**How to apply (Phase 3).** Each block carries a machine-readable marker (`<!-- block … -->`). The
reconcile pass (§ 15.3) re-extracts every block from THIS file before the first edit and checks it
against the live trees — vault: the working tree; estimator: a fresh writable clone of `main` in the
session scratchpad (never inside the vault folder; deleted after the push): every FIND matches exactly
once, every whole-file pre-image hashes as stated, every NEW file is absent. Any mismatch is a named
plan defect (D1, D2, …) — stop and surface it. Replace every `<P3-DATE>` with the Phase 3 date checked
against an external time authority (L079). **Order:** step 3.2 applies § 5a, 5b, 5c, 5f, 5g to the vault;
step 3.3 applies § 5h–5n to the estimator clone (§ 5k copies the vault file that § 5a produced); step
3.4 applies § 5d + 5e (registry entry + opener row) only AFTER the prep commit is on their `main` — a
`status` / `fleet` / governance run before that would probe a repo the engine cannot read yet. If the
estimator's `main` moved past `45d7c75`, the reconcile pass decides: blocks that still match apply; any
that does not is a plan defect.

<!-- §5-GENERATED:BEGIN -->

### 5a — `scripts/claude_project_data.sh` (vault) — 0.1 → 0.2: Windows junction support + the E002 fix — WHOLE-FILE REPLACE
<!-- block id=5a repo=vault path=scripts/claude_project_data.sh kind=whole pre_blob=c746047406e427dce4319bed5ec05bd447fbf6c6 -->
**5a** — the live file must hash to `c746047406e427dce4319bed5ec05bd447fbf6c6` (`git hash-object`); replace its whole content with:

```text
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
# v0.2 — <P3-DATE> — PLAN-017: Windows (Git Bash) support — drive-form path-key, directory
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
```

### 5b — `tests/test_claude_project_data.py` (vault) — NEW FILE (0.1)
<!-- block id=5b repo=vault path=tests/test_claude_project_data.py kind=new -->
**5b** — the file must not exist; write:

```text
# ==============================================================
# VERSION: 0.1
# Behavior tests for scripts/claude_project_data.sh (CLAUDE.md Rule 14 locality tool).
#
# CHANGE LOG
# v0.1 — <P3-DATE> — Initial (PLAN-017): the script runs for real against throwaway repo +
#         HOME trees — POSIX status / link / adopt, the pre-v1.5 memory layout, the E002
#         folder-move merge — and its Windows branch through stand-in uname / cygpath / cmd
#         commands (a junction is simulated by a symlink; cmd calls are logged).
# ==============================================================
"""Tests for scripts/claude_project_data.sh — run the real script in temp trees."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "claude_project_data.sh"
OLD = time.time() - 3600  # an mtime well outside the live-session window

pytestmark = pytest.mark.skipif(shutil.which("bash") is None, reason="bash not available")


@dataclass
class Tree:
    repo: Path
    home: Path
    env: dict[str, str]
    log: Path | None = None

    @property
    def data(self) -> Path:
        return self.repo / ".claude" / "project-data"

    def run(self, verb: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["bash", str(self.repo / "scripts" / "claude_project_data.sh"), verb],
            env=self.env, capture_output=True, text=True, check=False,
        )

    def harness(self) -> Path:
        out = self.run("status").stdout
        match = re.search(r"^harness path:\s+(.+)$", out, re.MULTILINE)
        assert match, out
        return Path(match.group(1))


def _write(path: Path, text: str = "x", mtime: float | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if mtime is not None:
        os.utime(path, (mtime, mtime))


def _make_repo(repo: Path) -> None:
    (repo / "scripts").mkdir(parents=True)
    shutil.copy2(SCRIPT, repo / "scripts" / "claude_project_data.sh")


@pytest.fixture
def posix(tmp_path: Path) -> Tree:
    repo = tmp_path / "work" / "my repo"
    home = tmp_path / "home"
    home.mkdir()
    _make_repo(repo)
    env = {**os.environ, "HOME": str(home)}
    return Tree(repo=repo, home=home, env=env)


_SHIMS = {
    "uname": '#!/bin/bash\necho "MINGW64_NT-10.0-19045"\n',
    "cygpath": (
        "#!/bin/bash\n"
        'p="$2"; rest="${p#"$FAKE_WINROOT"/}"\n'
        '[ "$rest" != "$p" ] || exit 1\n'
        'drive="$(printf \'%s\' "${rest:0:1}" | tr \'[:lower:]\' \'[:upper:]\')"\n'
        'out="$drive:${rest:1}"\n'
        '[ "$1" = "-w" ] && out="${out//\\//\\\\}"\n'
        "printf '%s\\n' \"$out\"\n"
    ),
    "cmd": (
        "#!/bin/bash\n"
        'echo "cmd $*" >> "$SHIM_LOG"\n'
        "topath() {\n"
        '  p="${1//\\\\//}"\n'
        '  d="$(printf \'%s\' "${p:0:1}" | tr \'[:upper:]\' \'[:lower:]\')"\n'
        "  printf '%s/%s%s' \"$FAKE_WINROOT\" \"$d\" \"${p:2}\"\n"
        "}\n"
        'case "$2" in\n'
        '  mklink) ln -s "$(topath "$5")" "$(topath "$4")" ;;\n'
        '  rmdir) t="$(topath "$3")"; if [ -L "$t" ]; then rm "$t"; else rmdir "$t"; fi ;;\n'
        "  *) exit 1 ;;\n"
        "esac\n"
    ),
}


@pytest.fixture
def windows(tmp_path: Path) -> Tree:
    root = tmp_path / "win"
    repo = root / "e" / "Work_Area" / "demo-repo"
    home = root / "c" / "Users" / "someone"
    home.mkdir(parents=True)
    _make_repo(repo)
    shims = tmp_path / "shims"
    shims.mkdir()
    for name, body in _SHIMS.items():
        (shims / name).write_text(body, encoding="utf-8")
        (shims / name).chmod(0o755)
    log = tmp_path / "cmd.log"
    log.touch()
    env = {
        **os.environ, "HOME": str(home), "PATH": f"{shims}{os.pathsep}{os.environ['PATH']}",
        "FAKE_WINROOT": str(root), "SHIM_LOG": str(log),
    }
    return Tree(repo=repo, home=home, env=env, log=log)


# ---- POSIX (macOS / Linux) -------------------------------------------------


def test_posix_empty_then_link_is_idempotent(posix: Tree) -> None:
    first = posix.run("status")
    assert first.returncode == 1 and "STATUS: EMPTY" in first.stdout
    linked = posix.run("link")
    assert linked.returncode == 0 and "STATUS: OK" in linked.stdout
    harness = posix.harness()
    assert harness.is_symlink() and os.readlink(harness) == str(posix.data)
    again = posix.run("link")
    assert again.returncode == 0 and "Already linked." in again.stdout


def test_posix_adopt_moves_harness_data_in(posix: Tree) -> None:
    harness = posix.harness()
    _write(harness / "memory" / "a.md")
    _write(harness / "s1.jsonl")
    assert "Run: adopt" in posix.run("status").stdout
    out = posix.run("adopt")
    assert out.returncode == 0 and "STATUS: OK" in out.stdout
    assert (posix.data / "memory" / "a.md").is_file() and (posix.data / "s1.jsonl").is_file()
    assert harness.is_symlink()


def test_posix_adopt_absorbs_pre_v15_memory_layout(posix: Tree) -> None:
    old_store = posix.repo / ".claude" / "memory"
    _write(old_store / "a.md")
    _write(old_store / "b.md")
    harness = posix.harness()
    harness.mkdir(parents=True)
    (harness / "memory").symlink_to(old_store)
    _write(harness / "s1.jsonl")
    out = posix.run("adopt")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "absorbed old in-repo memory store" in out.stdout
    assert "(2 memory files)" in out.stdout
    assert not old_store.exists() and (posix.data / "s1.jsonl").is_file()


def test_posix_e002_folder_move_merges_harness_created_dir(posix: Tree) -> None:
    for name in ("a.md", "b.md", "c.md"):
        _write(posix.data / "memory" / name)
    harness = posix.harness()
    (harness / "memory").mkdir(parents=True)  # what Claude Code creates on session start
    _write(harness / "new.jsonl")
    status = posix.run("status")
    assert status.returncode == 1 and "Run: link" in status.stdout and "adopt" not in status.stdout
    out = posix.run("link")
    assert out.returncode == 0 and "(3 memory files)" in out.stdout, out.stdout
    assert (posix.data / "new.jsonl").is_file() and harness.is_symlink()


def test_posix_merge_recurses_into_same_name_dirs(posix: Tree) -> None:
    _write(posix.data / "memory" / "a.md")
    harness = posix.harness()
    _write(harness / "memory" / "c.md")
    out = posix.run("link")
    assert out.returncode == 0, out.stdout
    assert sorted(p.name for p in (posix.data / "memory").iterdir()) == ["a.md", "c.md"]


def test_posix_file_collision_still_aborts_without_loss(posix: Tree) -> None:
    _write(posix.data / "f.txt", "in-repo")
    harness = posix.harness()
    _write(harness / "f.txt", "harness")
    out = posix.run("link")
    assert out.returncode == 1 and "ABORT" in out.stdout
    assert (posix.data / "f.txt").read_text(encoding="utf-8") == "in-repo"
    assert (harness / "f.txt").read_text(encoding="utf-8") == "harness"


def test_posix_stale_symlink_is_repointed(posix: Tree, tmp_path: Path) -> None:
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    posix.data.mkdir(parents=True)
    harness = posix.harness()
    harness.parent.mkdir(parents=True)
    harness.symlink_to(elsewhere)
    assert "STATUS: BROKEN" in posix.run("status").stdout
    out = posix.run("link")
    assert out.returncode == 0 and "Re-pointing stale symlink" in out.stdout
    assert os.readlink(harness) == str(posix.data)


# ---- Windows (Git Bash) through stand-in uname / cygpath / cmd ---------------


def test_windows_path_key_uses_the_lowercased_drive_form(windows: Tree) -> None:
    out = windows.run("status").stdout
    assert re.search(r"^path-key:\s+e--Work-Area-demo-repo$", out, re.MULTILINE), out
    expected = windows.home / ".claude" / "projects" / "e--Work-Area-demo-repo"
    assert windows.harness() == expected


def test_windows_adopt_migrates_the_old_junction_layout(windows: Tree) -> None:
    old_store = windows.repo / ".claude" / "memory"
    _write(old_store / "m1.md", mtime=OLD)
    _write(old_store / "m2.md", mtime=OLD)
    harness = windows.harness()
    harness.mkdir(parents=True)
    (harness / "memory").symlink_to(old_store)  # bootstrap_memory.sh's junction
    _write(harness / "old.jsonl", "transcript", mtime=OLD)
    out = windows.run("adopt")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "STATUS: OK" in out.stdout and "(2 memory files)" in out.stdout
    assert harness.is_symlink() and harness.resolve() == windows.data.resolve()
    assert (windows.data / "old.jsonl").read_text(encoding="utf-8") == "transcript"
    backups = list(harness.parent.glob(f"{harness.name}.pre-locality-*"))
    assert len(backups) == 1 and (backups[0] / "old.jsonl").is_file()
    assert windows.log is not None
    calls = windows.log.read_text(encoding="utf-8")
    assert "cmd //c rmdir " in calls and "\\memory" in calls  # junction dropped via rmdir
    assert "cmd //c mklink //J " in calls


def test_windows_refuses_while_a_session_is_live(windows: Tree) -> None:
    harness = windows.harness()
    _write(harness / "live.jsonl")  # mtime = now
    out = windows.run("adopt")
    assert out.returncode == 1 and "looks active" in out.stdout
    assert harness.is_dir() and not harness.is_symlink()
    assert not list(harness.parent.glob(f"{harness.name}.pre-locality-*"))


def test_windows_e002_link_after_move_keeps_memories(windows: Tree) -> None:
    for name in ("a.md", "b.md"):
        _write(windows.data / "memory" / name)
    harness = windows.harness()
    (harness / "memory").mkdir(parents=True)
    _write(harness / "s.jsonl", mtime=OLD)
    assert "Run: link" in windows.run("status").stdout
    out = windows.run("link")
    assert out.returncode == 0 and "(2 memory files)" in out.stdout, out.stdout + out.stderr
    assert (windows.data / "s.jsonl").is_file()
    again = windows.run("link")
    assert again.returncode == 0 and "Already linked." in again.stdout
    assert "junction:" in again.stdout
```

### 5c — `scripts/validation_ownership.toml` (vault) — `[rules.locality]`
<!-- block id=5c.1 repo=vault path=scripts/validation_ownership.toml kind=replace -->
**5c.1** FIND:

```text
reason       = "Fleet view — docs/fleet.csv rows + the pre-push freshness check (PLAN-016)."

[monitored_paths]
```

REPLACE WITH:

```text
reason       = "Fleet view — docs/fleet.csv rows + the pre-push freshness check (PLAN-016)."

[rules.locality]
source_paths = ["scripts/claude_project_data.sh"]
test_paths   = ["tests/test_claude_project_data.py"]
doc_paths    = ["docs/folder_structure.md"]
strictness   = "soft"
require_docs = false
reason       = "Rule 14 locality tool — symlink / Windows junction; adopt + link merges (PLAN-017)."

[monitored_paths]
```

### 5d — `config/projects.toml` (vault) — the 780-estimator entry
<!-- block id=5d.1 repo=vault path=config/projects.toml kind=replace -->
**5d.1** FIND:

```text
# NOTE: high-stakes live project — every engine write lands in its working tree (local flush =
# write-in-place); its next session lands per docs/SYNC_HANDOFF.md BEFORE any other work.
# Write only between Equinex work sessions, one machine at a time.
```

REPLACE WITH:

```text
# NOTE: high-stakes live project — every engine write lands in its working tree (local flush =
# write-in-place); its next session lands per docs/SYNC_HANDOFF.md BEFORE any other work.
# Write only between Equinex work sessions, one machine at a time.

[[project]]                        # team project; Set v1.3 old-SETUP adopter (2026-06-21), caught up via sync (PLAN-017)
name = "780-estimator"
transport = "git"
git_url = "git@github.com:780-AI/780-estimator.git"
git_branch = "main"
owner = "team"
git_remote = "github.com/780-AI/780-estimator"
part_of = "780-AI"
work_machine = "Bahereh Hassanpour's PC (Windows)"
delivery = "direct+handoff"
onboarding = "catch-up"
onboarded_on = "2026-06-21"
onboarded_set = "v1.3"
registered_on = "<P3-DATE>"
plan = "PLAN-017"
lifecycle = "onboarding"
caveats = "first git-transport target: engine writes are commits pushed to main; Windows PC (Git Bash, Rule 14 via junctions)"
# NOTE: owner Bahereh Hassanpour. Delivery A (operator, 2026-10-05): the engine commits as
# "Standard DocSet" and pushes straight to `main` — fast-forward only, so a concurrent push makes
# the write fail, never overwrite; the owner's next session pulls and lands docs/SYNC_HANDOFF.md.
```

### 5e — `docs/SESSION_OPENER.md` (vault) — 1.20 → 1.21 + § 2 registry row
<!-- block id=5e.1 repo=vault path=docs/SESSION_OPENER.md kind=replace -->
**5e.1** FIND:

```text
<!-- VERSION: 1.20 -->
<!-- Last Updated: 2026-10-05 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.21 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5e.2 repo=vault path=docs/SESSION_OPENER.md kind=replace -->
**5e.2** FIND:

```text
CHANGE LOG
v1.20 — 2026-10-05 — PLAN-016: § 1.2 fleet-view bullet (run `status` — prints every target's state and regenerates `docs/fleet.csv`; call out unreachable / not-current / handoff-pending targets); § 4 "Registered target suites" line reads from that run.
```

REPLACE WITH:

```text
CHANGE LOG
v1.21 — <P3-DATE> — Fifth target registered: 780-estimator (§ 2 registry row — git transport, the first git target; team project on a Windows PC; Set v1.3 old-SETUP adopter caught up to v2.7 after a one-time prep commit — PLAN-017).
v1.20 — 2026-10-05 — PLAN-016: § 1.2 fleet-view bullet (run `status` — prints every target's state and regenerates `docs/fleet.csv`; call out unreachable / not-current / handoff-pending targets); § 4 "Registered target suites" line reads from that run.
```

<!-- block id=5e.3 repo=vault path=docs/SESSION_OPENER.md kind=replace -->
**5e.3** FIND:

```text
| | `EverOn.Equinex` — `~/Library/CloudStorage/Dropbox/Projects/EverOn.Equinex` (Dropbox-synced) | Registered 2026-10-03 (local transport, `~` path — resolves per machine; ONE machine at a time, let Dropbox settle). Adopted Set v2.7 2026-10-03 via the skill's adopt mode (PLAN-011); EverOn own line retired — pre-adoption archive + numbering crosswalk in `archive/LESSONS_LEGACY.md`. High-stakes live project: engine writes only between its work sessions. |
<!-- PROJECT-OWNED:END -->
```

REPLACE WITH:

```text
| | `EverOn.Equinex` — `~/Library/CloudStorage/Dropbox/Projects/EverOn.Equinex` (Dropbox-synced) | Registered 2026-10-03 (local transport, `~` path — resolves per machine; ONE machine at a time, let Dropbox settle). Adopted Set v2.7 2026-10-03 via the skill's adopt mode (PLAN-011); EverOn own line retired — pre-adoption archive + numbering crosswalk in `archive/LESSONS_LEGACY.md`. High-stakes live project: engine writes only between its work sessions. |
| | `780-estimator` — `git@github.com:780-AI/780-estimator.git` (branch `main`) | Registered <P3-DATE> — git transport, the FIRST git target: every engine write is a commit pushed straight to their `main` (Delivery A; fast-forward only — a concurrent push makes the write fail, never overwrite). Team project, owner Bahereh Hassanpour, worked on from a Windows PC (Git Bash; Rule 14 via directory junctions — `claude_project_data.sh` v0.2). Bootstrapped Set v1.3 2026-06-21 (old SETUP flow); caught up to v2.7 <P3-DATE> by `sync` after a one-time prep commit (v1.6 heading wrap + sync-ready SVA + locality tool) — PLAN-017. |
<!-- PROJECT-OWNED:END -->
```

### 5f — `skill/SKILL.md` (vault) — 0.1 → 0.2: the old-SETUP catch-up paragraph
<!-- block id=5f.1 repo=vault path=skill/SKILL.md kind=replace -->
**5f.1** FIND:

```text
<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-08-16 -->
<!--
CHANGE LOG
```

REPLACE WITH:

```text
<!-- VERSION: 0.2 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.2 — <P3-DATE> — PLAN-017: the old-SETUP catch-up paragraph names the whole one-time prep
(heading wrap, sync-ready SET_VERSION_ADOPTED, locality script) and an engine dry-run before
registering — the gaps the first catch-up exposed.
```

<!-- block id=5f.2 repo=vault path=skill/SKILL.md kind=replace -->
**5f.2** FIND:

```text
If the operator says the project is an **old-SETUP adopter** (already carries the suite, just a
stale Set Version), neither mode applies — tell them the path is: register the project in the
vault's `config/projects.toml`, hand-apply the one-time v1.6 heading-wrap if it predates v1.6, and
let `sync` catch it up. Do not run a delivery mode over an existing adopter.
```

REPLACE WITH:

```text
If the operator says the project is an **old-SETUP adopter** (already carries the suite, just a
stale Set Version), neither mode applies — tell them the path is a one-time prep commit in the
project, then registration, then `sync`. The prep commit supplies what the engine needs and an
old-SETUP copy lacks: the v1.6 PROJECT-OWNED heading-wrap of the session opener + closer if it
predates v1.6; `docs/SET_VERSION_ADOPTED.md` rewritten in the sync-ready shape `modes/adopt.md`
§ 5 specifies, still recording the version the project really has (the engine refuses any other
shape); and `scripts/claude_project_data.sh` copied verbatim from the vault if absent (sync never
delivers scripts, yet the synced Rule 14 calls it). Before registering, prove it with an engine
dry-run against the prepared copy: it must list only suite files. Then register the project in
the vault's `config/projects.toml` and let `sync` catch it up. Do not run a delivery mode over an
existing adopter.
```

### 5g — `docs/folder_structure.md` (vault) — 0.15 → 0.16 + tree
<!-- block id=5g.1 repo=vault path=docs/folder_structure.md kind=replace -->
**5g.1** FIND:

```text
<!-- VERSION: 0.15 -->
<!-- Last Updated: 2026-10-05 -->
<!--
CHANGE LOG
```

REPLACE WITH:

```text
<!-- VERSION: 0.16 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.16 — <P3-DATE> — PLAN-017: added tests/test_claude_project_data.py to the tree; the claude_project_data.sh comment notes the Windows junction.
```

<!-- block id=5g.2 repo=vault path=docs/folder_structure.md kind=replace -->
**5g.2** FIND:

```text
│   ├── test_fleet.py
│   └── test_cli.py
```

REPLACE WITH:

```text
│   ├── test_fleet.py
│   ├── test_claude_project_data.py
│   └── test_cli.py
```

<!-- block id=5g.3 repo=vault path=docs/folder_structure.md kind=replace -->
**5g.3** FIND:

```text
│   ├── claude_project_data.sh    # Rule 14 project-data locality tool (status / adopt / link)
```

REPLACE WITH:

```text
│   ├── claude_project_data.sh    # Rule 14 project-data locality tool (status / adopt / link; symlink, or a junction on Windows)
```

### 5h — `docs/SESSION_OPENER.md` (estimator) — 1.2 → 1.3: heading wrap + § 2 note into its block
<!-- block id=5h.1 repo=estimator path=docs/SESSION_OPENER.md kind=replace -->
**5h.1** FIND:

```text
<!-- VERSION: 1.2 -->
<!-- Last Updated: 2026-06-21 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.3 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5h.2 repo=estimator path=docs/SESSION_OPENER.md kind=replace -->
**5h.2** FIND:

```text
CHANGE LOG
v1.2 — 2026-06-21 — Added § 3.2 project-specific row 1: never use the AskUserQuestion popup; ask inline in chat (pairs with feedback_ask_in_chat_not_popup memory + CLAUDE.md § 10).
```

REPLACE WITH:

```text
CHANGE LOG
v1.3 — <P3-DATE> — Standard Set catch-up prep (Standard DocSet PLAN-017): instance heading + BINDING note wrapped in a PROJECT-OWNED block (the v1.6 heading wrap the vault's sync engine needs); the § 2 "Current state" note moved inside the § 2 PROJECT-OWNED block so the sync keeps it.
v1.2 — 2026-06-21 — Added § 3.2 project-specific row 1: never use the AskUserQuestion popup; ask inline in chat (pairs with feedback_ask_in_chat_not_popup memory + CLAUDE.md § 10).
```

<!-- block id=5h.3 repo=estimator path=docs/SESSION_OPENER.md kind=replace -->
**5h.3** FIND:

```text
# SESSION_OPENER.md — Mandatory session-start pre-flight (780-estimator)

> **BINDING for every Claude session in this repository.** Read this file and execute its § 1 pre-flight before acting on the operator's first task, then post the § 4 first-response block. (Mandated by repo-root `CLAUDE.md` Rule 9.)
```

REPLACE WITH:

```text
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# SESSION_OPENER.md — Mandatory session-start pre-flight (780-estimator)

> **BINDING for every Claude session in this repository.** Read this file and execute its § 1 pre-flight before acting on the operator's first task, then post the § 4 first-response block. (Mandated by repo-root `CLAUDE.md` Rule 9.)
<!-- PROJECT-OWNED:END -->
```

<!-- block id=5h.4 repo=estimator path=docs/SESSION_OPENER.md kind=replace -->
**5h.4** FIND:

```text
**Current state (2026-06-21): no remote infrastructure provisioned yet.** The target deployment shape is Dockerized + GitLab CI → VPS (registry-pull). Until the VPS and GitLab project exist, all work is local and § 1.2 live-system probes are N/A. Fill the rows below the moment each environment is provisioned — never invent a host.

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
```

REPLACE WITH:

```text
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
**Current state (2026-06-21): no remote infrastructure provisioned yet.** The target deployment shape is Dockerized + GitLab CI → VPS (registry-pull). Until the VPS and GitLab project exist, all work is local and § 1.2 live-system probes are N/A. Fill the rows below the moment each environment is provisioned — never invent a host.

```

### 5i — `docs/SESSION_CLOSER.md` (estimator) — 1.1 → 1.2: heading wrap
<!-- block id=5i.1 repo=estimator path=docs/SESSION_CLOSER.md kind=replace -->
**5i.1** FIND:

```text
<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-06-21 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.2 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5i.2 repo=estimator path=docs/SESSION_CLOSER.md kind=replace -->
**5i.2** FIND:

```text
CHANGE LOG
v1.1 — 2026-06-21 — Strip-consistency: point § 1.2 Set-Version lookup at docs/SET_VERSION_ADOPTED.md (STANDARDS_INDEX.md was stripped); corrected the Source provenance line.
```

REPLACE WITH:

```text
CHANGE LOG
v1.2 — <P3-DATE> — Standard Set catch-up prep (Standard DocSet PLAN-017): instance heading + BINDING note wrapped in a PROJECT-OWNED block (the v1.6 heading wrap the vault's sync engine needs).
v1.1 — 2026-06-21 — Strip-consistency: point § 1.2 Set-Version lookup at docs/SET_VERSION_ADOPTED.md (STANDARDS_INDEX.md was stripped); corrected the Source provenance line.
```

<!-- block id=5i.3 repo=estimator path=docs/SESSION_CLOSER.md kind=replace -->
**5i.3** FIND:

```text
# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (780-estimator)

> **BINDING for every Claude session in this repository.** On a wrap-up trigger keyword, read this file and execute its § 1 routine before any farewell, then post the § 4 block. (Mandated by repo-root `CLAUDE.md` Rule 12.)
```

REPLACE WITH:

```text
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
# SESSION_CLOSER.md — Mandatory wrap-up routine on operator command (780-estimator)

> **BINDING for every Claude session in this repository.** On a wrap-up trigger keyword, read this file and execute its § 1 routine before any farewell, then post the § 4 block. (Mandated by repo-root `CLAUDE.md` Rule 12.)
<!-- PROJECT-OWNED:END -->
```

### 5j — `docs/SET_VERSION_ADOPTED.md` (estimator) — 1.0 → 1.1: sync-ready shape — WHOLE-FILE REPLACE
<!-- block id=5j repo=estimator path=docs/SET_VERSION_ADOPTED.md kind=whole pre_blob=6ee9fc20aecd103bbbfed8ac0bdc91435c526285 -->
**5j** — the live file must hash to `6ee9fc20aecd103bbbfed8ac0bdc91435c526285` (`git hash-object`); replace its whole content with:

```text
<!-- VERSION: 1.1 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v1.1 — <P3-DATE> — Rewritten in the shape the Standard DocSet sync engine updates mechanically (Standard DocSet PLAN-017 catch-up prep): the `Standard Set Version` + `Adopted on` bullets and the backport table. Still records v1.3 — the engine's sync commit records the new version.
v1.0 — 2026-06-21 — Adoption record created at bootstrap (Standard Set v1.3).
-->

# Standard Set Version adopted

- **Standard Set Version:** v1.3 (bootstrapped 2026-06-21 from the canonical suite, old SETUP flow)
- **Adopted on:** 2026-06-21 (bootstrap)
- **Scope:** the operating contract (`CLAUDE.md`), the topical standards library (`docs/standards/`),
  the session pre-flight / wrap-up forcing functions (`docs/SESSION_OPENER.md`, `docs/SESSION_CLOSER.md`),
  the lessons archive (`archive/LESSONS.md`), and durable project data (Rule 14).

## How this file is updated

The suite's curator keeps this repo current with the Standard DocSet `sync` engine. Each sync rewrites
the two bullets above and adds a row to the table below; in `CLAUDE.md`, `docs/SESSION_OPENER.md` and
`docs/SESSION_CLOSER.md` it keeps every PROJECT-OWNED block and replaces the rest; the six
`docs/standards/` files and `archive/LESSONS.md` are replaced whole. Every engine write also leaves
`docs/SYNC_HANDOFF.md`, which tells the next session here what landed and what bookkeeping remains.
Project lessons go to `docs/STANDARDS_LOG.md` as `E0NN` entries — never into the suite files.

## Backport tracking

| Set Version | Adopted on | Notes |
|---|---|---|
| v1.3 | 2026-06-21 | bootstrap (old SETUP flow) |
```

### 5k — `scripts/claude_project_data.sh` (estimator) — NEW: byte-identical copy of the vault file after § 5a
<!-- block id=5k repo=estimator path=scripts/claude_project_data.sh kind=copy source=scripts/claude_project_data.sh -->
**5k** — copy `scripts/claude_project_data.sh` from the vault (after § 5a, dates substituted) byte-for-byte, mode 100755; `cmp` must exit 0.

### 5l — `docs/documents_manifest.md` (estimator) — 1.55 → 1.56: cells + the new script row
<!-- block id=5l.1 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.1** FIND:

```text
<!-- VERSION: 1.55 -->
<!-- Last Updated: 2026-09-14 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.56 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5l.2 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.2** FIND:

```text
| `CHANGELOG.md` | 1.38 | Cross-cutting history. |
```

REPLACE WITH:

```text
| `CHANGELOG.md` | 1.39 | Cross-cutting history. |
```

<!-- block id=5l.3 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.3** FIND:

```text
| `docs/documents_manifest.md` | 1.55 | This version index (critical). |
```

REPLACE WITH:

```text
| `docs/documents_manifest.md` | 1.56 | This version index (critical). |
```

<!-- block id=5l.4 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.4** FIND:

```text
| `docs/folder_structure.md` | 1.16 | Authoritative layout reference. |
```

REPLACE WITH:

```text
| `docs/folder_structure.md` | 1.17 | Authoritative layout reference. |
```

<!-- block id=5l.5 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.5** FIND:

```text
| `docs/SESSION_OPENER.md` | 1.2 | Session-start pre-flight (Rule 9). |
```

REPLACE WITH:

```text
| `docs/SESSION_OPENER.md` | 1.3 | Session-start pre-flight (Rule 9). |
```

<!-- block id=5l.6 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.6** FIND:

```text
| `docs/SESSION_CLOSER.md` | 1.1 | Session wrap-up (Rule 12). |
```

REPLACE WITH:

```text
| `docs/SESSION_CLOSER.md` | 1.2 | Session wrap-up (Rule 12). |
```

<!-- block id=5l.7 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.7** FIND:

```text
| `docs/SET_VERSION_ADOPTED.md` | 1.0 | Adopted Standard Set Version. |
```

REPLACE WITH:

```text
| `docs/SET_VERSION_ADOPTED.md` | 1.1 | Adopted Standard Set Version. |
```

<!-- block id=5l.8 repo=estimator path=docs/documents_manifest.md kind=replace -->
**5l.8** FIND:

```text
| `scripts/bootstrap_memory.sh` | 0.1 | Durable-memory link bootstrap (Rule 14). |
```

REPLACE WITH:

```text
| `scripts/bootstrap_memory.sh` | 0.1 | Durable-memory link bootstrap (Rule 14). |
| `scripts/claude_project_data.sh` | 0.2 | Project-data locality tool (Rule 14, Standard Set v1.5+): memory + session transcripts live in `.claude/project-data/`, linked from Claude Code's harness path — a symlink on macOS / Linux, a directory junction on Windows (Git Bash). Copied verbatim from the Standard DocSet vault (Standard DocSet PLAN-017); replaces `bootstrap_memory.sh` once `adopt` has run. |
```

### 5m — `docs/folder_structure.md` (estimator) — 1.16 → 1.17: tree line
<!-- block id=5m.1 repo=estimator path=docs/folder_structure.md kind=replace -->
**5m.1** FIND:

```text
<!-- VERSION: 1.16 -->
<!-- Last Updated: 2026-09-13 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.17 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5m.2 repo=estimator path=docs/folder_structure.md kind=replace -->
**5m.2** FIND:

```text
│   ├── run_daily.sh              # daily-flow wrapper for cron/notebook/manual + dependency gate (landed — PLAN-010)
│   └── bootstrap_memory.sh        # durable-memory link (Rule 14)
```

REPLACE WITH:

```text
│   ├── run_daily.sh              # daily-flow wrapper for cron/notebook/manual + dependency gate (landed — PLAN-010)
│   ├── claude_project_data.sh     # project-data locality tool (Rule 14, Set v1.5+; symlink / Windows junction) — replaces bootstrap_memory.sh after `adopt`
│   └── bootstrap_memory.sh        # durable-memory link (Rule 14)
```

### 5n — `CHANGELOG.md` (estimator) — 1.38 → 1.39: header + the catch-up entry
<!-- block id=5n.1 repo=estimator path=CHANGELOG.md kind=replace -->
**5n.1** FIND:

```text
<!-- VERSION: 1.38 -->
<!-- Last Updated: 2026-09-14 -->
```

REPLACE WITH:

```text
<!-- VERSION: 1.39 -->
<!-- Last Updated: <P3-DATE> -->
```

<!-- block id=5n.2 repo=estimator path=CHANGELOG.md kind=replace -->
**5n.2** FIND:

```text
All notable changes to `780-estimator`. Newest at the top. Each entry states an explicit impact.

```

REPLACE WITH:

```text
All notable changes to `780-estimator`. Newest at the top. Each entry states an explicit impact.

## <P3-DATE> — Standard Set catch-up, step 1 of 2: the one-time prep (v1.3 → v2.7)

**Impact: governance documents and one new script only — no forecasting, evaluation, publication,
test or runtime behavior changes.** This repo was bootstrapped on Standard Set v1.3 (2026-06-21). The
suite's curator now keeps adopting projects current with the Standard DocSet `sync` engine; this
commit makes the repo readable by it (Standard DocSet PLAN-017). The next commit is the engine's own
(`Standard DocSet: sync to Standard Set Version v2.7`, author "Standard DocSet"): it updates the suite
files and leaves `docs/SYNC_HANDOFF.md`.

**What this commit changes:**
- `docs/SESSION_OPENER.md` 1.3 / `docs/SESSION_CLOSER.md` 1.2 — the instance heading and its BINDING
  note are wrapped in a PROJECT-OWNED block (the engine keeps PROJECT-OWNED blocks and replaces the
  rest); the opener's § 2 "Current state" note moved inside the § 2 block so it survives.
- `docs/SET_VERSION_ADOPTED.md` 1.1 — rewritten in the shape the engine updates mechanically; it
  still records v1.3 until the sync commit records v2.7.
- `scripts/claude_project_data.sh` 0.2 (new) — the suite's Rule 14 tool since Set v1.5: memory AND
  session transcripts live in `.claude/project-data/`, linked from Claude Code's folder — a directory
  junction on Windows. It replaces `scripts/bootstrap_memory.sh`, which stays until the migration
  below has run.
- `docs/documents_manifest.md` 1.56, `docs/folder_structure.md` 1.17 — registered.

**What the sync commit will change:** `CLAUDE.md` (15 standing rules: Rule 14 upgraded to project-data
locality, new Rule 15, § 15.9 feature intake, …), `archive/LESSONS.md` (L001–L051 → L001–L081),
`docs/standards/PROJECT_STANDARDS.md` + `MEMORY_PROTOCOL.md`, everything outside the PROJECT-OWNED
blocks of the session opener and closer, and the adoption record. Two local texts do not survive it,
by design: the `CLAUDE.md` § 10 line "ask in plain chat, never via a popup" (the rule lives on in
opener § 3.2 row 1) and the "Branch convention: `main`" lines (the template now writes
`origin/<main-branch>`).

**Next session on the Windows PC, in order:**
1. `git pull` before any other work.
2. The updated opener § 1.1 finds `docs/SYNC_HANDOFF.md` — land it first. Over git the engine's files
   arrive ALREADY COMMITTED (its commit, author "Standard DocSet"), so the handoff's "review the
   diffs" step means `git show` of that commit. Then reconcile the manifest cells for the files it
   lists, add a CHANGELOG entry, and delete the handoff — one commit.
3. The updated opener § 1.5 runs `bash scripts/claude_project_data.sh status` and reports
   `NOT ADOPTED`. Note the memory count first (`ls .claude/memory | wc -l`). Close Claude Code, open
   Git Bash in the repo, run `bash scripts/claude_project_data.sh adopt`, reopen Claude Code, and
   confirm `status` says `STATUS: OK` with that same count. Keep the `*.pre-locality-*` backup it
   reports until your memories show up, then delete it.
4. Once `status` says `STATUS: OK`: delete `scripts/bootstrap_memory.sh` with its manifest row and
   its `docs/folder_structure.md` line (one commit).
5. Send the `status` / `adopt` output to the curator — it is the Windows verification of the new
   tool (Standard DocSet PLAN-017 QA-M8).

**QA scenarios** (Rule 11): step 3 above is this change's scenario — ⏸ until it runs on the Windows
PC. The curator's side (engine dry-run, sync write, idempotent re-run) is recorded in Standard
DocSet PLAN-017.

```

<!-- §5-GENERATED:END -->

### 5o — estimator prep commit message (verbatim; `git commit -F <file>`)

```text
Docs/Governance: Standard Set catch-up prep, step 1 of 2 (v1.3 -> v2.7)

One-time preparation so the Standard DocSet sync engine can bring this repo
from Standard Set v1.3 to v2.7 (Standard DocSet PLAN-017). Governance docs
and one new script only; no runtime, domain or test change.

- docs/SESSION_OPENER.md 1.3, docs/SESSION_CLOSER.md 1.2: instance heading
  wrapped in a PROJECT-OWNED block; the opener's section 2 "Current state"
  note moved inside its block.
- docs/SET_VERSION_ADOPTED.md 1.1: the engine's sync-ready shape (still v1.3).
- scripts/claude_project_data.sh 0.2 (new): Rule 14 project-data locality
  tool with Windows junction support; replaces bootstrap_memory.sh after
  `adopt` (steps in CHANGELOG.md).
- docs/documents_manifest.md 1.56, docs/folder_structure.md 1.17,
  CHANGELOG.md 1.39: registered.

Step 2 is the engine's own commit (author "Standard DocSet").

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
```

### 5p — E002 write-back decisions (verbatim TOML; `integrate --apply <file>`, then `--write`)

```toml
[[integrated]]
project = "EverOn.Capital-Signal"
entry = "E002"
lesson = "scripts/claude_project_data.sh v0.2"
topical = "PLAN-017 locality-tool fix — same-name dirs merge, status names link; adopter copies refresh at the script-delivery fix"
set_version = "v2.7"
```

Rendered Status (dry-run 2026-10-05): `integrated → vault scripts/claude_project_data.sh v0.2 (PLAN-017
locality-tool fix — same-name dirs merge, status names link; adopter copies refresh at the
script-delivery fix, Set Version v2.7)`. If the vault Set Version moved before Phase 3, `set_version`
takes the current value.

## 6. Spec update map (mechanical rules; same commit as the work)

- **6a — design commit (§ 7.1):** vault manifest — new rows **90** (PLAN-017 plan, 0.1 DRAFT, Plan) and
  **91** (tracker, 0.1, Plan); self-row 5; quick-index *Plans* `31–39, 59–60, 63–64, 68–71, 74–75` →
  `31–39, 59–60, 63–64, 68–71, 74–75, 80–87, 90–91` (90–91 new; 80–87 = the OPEN_TASKS deferred minor on
  the same line, ridden along and recorded); header + CHANGE LOG + Last-updated rotation. CHANGELOG top
  entry (plan drafted; no runtime impact).
- **6b — Phase 2 approval commit:** plan + tracker 0.1 → 0.2 APPROVED with the § 9.1 decision record;
  manifest cells 90–91; CHANGELOG line (the PLAN-016 approval-commit precedent).
- **6c — Phase 3 vault commit (§ 7.5):** manifest — row **56** 0.1 → 0.2; new row **92**
  `tests/test_claude_project_data.py` (0.1, "Project-data locality script test", category
  `Governance script test`) + quick-index *Governance scripts* `28–29, 56` → `28–29, 56, 92`; cells **6** → 0.16, **8** → 1.21,
  **76** → 0.2, **64** → 1.1 (6d), **90 / 91** → the plan / tracker headers; self-row; files without a
  VERSION header (`config/projects.toml`, `scripts/validation_ownership.toml`) have no row — say so in
  the CHANGE LOG line; grep-verify every touched cell == its file header (L063). CHANGELOG top entry:
  what shipped, the estimator commits (shas), the impact statement ("the vault's own locality tool
  changes; no engine change; one target written by git, one by integrate"), and a **QA scenarios**
  sub-section listing QA-M1…M10 with status.
- **6d — PLAN-007 tracker post-close annotation (v1.1):** the git-transport half of QA K–N is closed
  by the first live git read + write (QA-M5 evidence) — the PLAN-013 v1.1 post-close precedent.
- **6e — plan + tracker:** → 0.3 EXECUTING in the Phase 3 commit (Phase 4 Windows QA open); → 1.0 /
  CLOSED in the closure commit.
- **6f — closure commit (§ 7.6):** registry `lifecycle` → `active` (FIND `plan = "PLAN-017"` +
  `lifecycle = "onboarding"` → `lifecycle = "active"`), then `fleet`; manifest cells; CHANGELOG
  (QA-M8 / M9 evidence); plan + tracker 1.0.
- **6g — `docs/Plans/OPEN_TASKS.md`** (local, never committed): next actions + the v2.8 queue items
  from the § 2 gate.
- No engine source changes → `docs/architecture.md` untouched (§ 4 drift rule not triggered); no new
  top-level directory.

## 7. ALLOWLIST (the bullet enumeration IS the count — L038; plan + tracker included per L054)

### 7.1 Design commit (vault; 4 files)

- `docs/Plans/PLAN-017_estimator_catchup.md` (new)
- `docs/Plans/PLAN-017_tracker.md` (new)
- `docs/documents_manifest.md`
- `CHANGELOG.md`

### 7.2 Estimator prep commit (curator; 7 files)

- `docs/SESSION_OPENER.md`
- `docs/SESSION_CLOSER.md`
- `docs/SET_VERSION_ADOPTED.md`
- `scripts/claude_project_data.sh` (new)
- `docs/documents_manifest.md`
- `docs/folder_structure.md`
- `CHANGELOG.md`

### 7.3 Estimator sync commit (engine-made; 8 files — verify with `git show --stat`)

- `CLAUDE.md`
- `docs/standards/PROJECT_STANDARDS.md`
- `docs/standards/MEMORY_PROTOCOL.md`
- `archive/LESSONS.md`
- `docs/SESSION_OPENER.md`
- `docs/SESSION_CLOSER.md`
- `docs/SET_VERSION_ADOPTED.md`
- `docs/SYNC_HANDOFF.md` (new)

### 7.4 Capital-Signal write-back (engine-made, uncommitted in CS; 2 files)

- `docs/STANDARDS_LOG.md`
- `docs/SYNC_HANDOFF.md`

### 7.5 Phase 3 vault commit (12 files)

- `scripts/claude_project_data.sh`
- `tests/test_claude_project_data.py` (new)
- `scripts/validation_ownership.toml`
- `config/projects.toml`
- `docs/SESSION_OPENER.md`
- `skill/SKILL.md`
- `docs/folder_structure.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-007_tracker.md`
- `docs/Plans/PLAN-017_estimator_catchup.md`
- `docs/Plans/PLAN-017_tracker.md`

### 7.6 Closure commit (vault; 5 files)

- `config/projects.toml`
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-017_estimator_catchup.md`
- `docs/Plans/PLAN-017_tracker.md`

## 8. Validation gate (Rule 11 scenarios; Rule 15 feature-ON marked ⚑; status in the tracker)

- **QA-M1 — tools (3.2).** `ruff check src tests` clean; `MYPYPATH=src mypy --cache-dir <fresh>` 0
  issues in 25 files; pytest **151** passed (140 + 11).
- **QA-M2 — the tests exercise the new code (3.2).** The 11 new tests run against tool 0.1 (copied
  into a scratch copy) fail exactly the 6 new-behavior cases (2 E002, 4 Windows) and pass the 5
  baseline cases — a green run proves nothing unless it can go red.
- **QA-M3 ⚑ — the vault's own locality (3.2).** With 0.2 in place: `bash
  scripts/claude_project_data.sh status` → `STATUS: OK` with the pre-change memory count (macOS
  regression on the live store).
- **QA-M4 ⚑ — prep proof (3.3, before the commit).** On the prepared estimator clone: its own
  governance scripts exit 0 (output pasted); engine-as-oracle through a scratch vault whose registry
  points at the clone (local transport): `status` v1.3 / v2.7 behind; dry-run 7 of 11; the
  removed-lines set == § 8.1.
- **QA-M5 ⚑ — the first live git write (3.4).** Live GitHub: `status` → 780-estimator v1.3 / v2.7
  behind (git read path); dry-run 7 / 11 + `--diff` removed lines == § 8.1; `sync --project
  780-estimator --write` → "wrote + flushed 8 file(s)"; `git ls-remote` main = the engine commit and
  its parent = the prep commit; `git show --stat` == § 7.3; re-run → up-to-date 11/11; `status` → v2.7
  current; `docs/fleet.csv` row: registry columns == § 5d (date substituted), `reachable` yes,
  `handoff_pending` 1.
- **QA-M6 ⚑ — post-sync integrity (3.4).** In a fresh clone of `main`: PROJECT-OWNED counts CLAUDE 4 /
  opener 3 / closer 2 (BEGIN == END); 15 `### Rule` headings; Rule 14 names
  `scripts/claude_project_data.sh` and the file exists; the opener heading + § 2 "Current state" note
  intact; SVA bullets read v2.7 with rows v2.7 + v1.3.
- **QA-M7 ⚑ — E002 write-back (3.5).** Capital-Signal idle (no transcript in its project-data changed
  in the last 10 minutes; operator confirms no session there); `integrate --apply` dry-run → `--write`;
  the Status line read back verbatim == § 5p's rendering; Capital-Signal's `docs/SYNC_HANDOFF.md`
  ends with a `### Write` record for this write-back (a new handoff if it held none); `harvest` → no
  open Capital-Signal entries.
- **QA-M8 ⚑ — Windows verification (owner's PC; operator-relayed evidence).** Before: the
  `.claude/memory` file count N. In a session: `status` → `NOT ADOPTED`; `adopt` there → refused
  ("looks active"). Claude Code closed, Git Bash: `adopt` → "Adopted." + `STATUS: OK (N memory
  files)`; `cmd //c dir "%USERPROFILE%\.claude\projects"` lists the key as `<JUNCTION>`; Claude Code
  reopened → a fresh session's `status` OK and it recalls a known memory; `link` → "Already linked.".
  Ship-gating (Rule 15) — waivable only by the operator, recorded in the tracker.
- **QA-M9 ⚑ — landing observed.** On their `main`: a commit deleting `docs/SYNC_HANDOFF.md` with the
  manifest cells + a CHANGELOG entry; `scripts/bootstrap_memory.sh` removed with its manifest row +
  tree line (D-1 = A); vault `status` / `fleet` → current, `handoff_pending` 0.
- **QA-M10 — domain-neutral gate (3.2).** `grep -rniE "780|estimator|everon|equinex|capital-signal|bahereh|parsaazad|a780" skill/ docs/standards/ scripts/claude_project_data.sh tests/test_claude_project_data.py`
  prints nothing (exit 1) — the tool is copied verbatim into every adopter, so it is held to the
  suite's rule.

### 8.1 Expected removed lines (catch-up dry-run `--diff`, after the prep; header lines aside)

- `CLAUDE.md` (28 lines): the "13 standing rules" heading + § 13 bullet; the Rule 5 local-checks
  wording and the § 8.6 YAML example (template v2.4 runner note); Rule 12 step 6 title; the whole old
  Rule 14 (`.claude/memory` + `bootstrap_memory.sh`); **the § 10 "Ask in plain chat — never via a
  popup" bullet** (accepted, § 2 #3); the § 15.2 Phase 0 / Phase 1 rows and the § 15.3 ambiguity
  sentence (template v2.7 / L056 wording).
- `docs/SESSION_OPENER.md` (19 lines incl. its VERSION line): the two `origin/main` § 1.1 commands +
  "Branch convention for this project: `main`."; the old § 1.5 memory-link block; § 3.1 rows 14 / 15
  (renumbered upstream); three § 4 template lines; the freshly-bootstrapped trailer.
- `docs/SESSION_CLOSER.md` (6 lines incl. its VERSION line): the `origin/main` command + branch line;
  the Set-Version bullet; the § 1.6 title; the trailer.
- `docs/SET_VERSION_ADOPTED.md` (3 lines): its VERSION line and the two bullets (rewritten to v2.7).

If the engine's run date differs from `<P3-DATE>` (a session crossing midnight), each of the opener,
closer and SVA also loses its `Last Updated` line (+1 each) — nothing else may differ. Anything else in
the removed set ⇒ STOP and investigate before writing (the 2026-09-05 discard finding: a delta wider
than the oracle is a defect until explained).

Replace-mode files (the six `docs/standards/` files and `archive/LESSONS.md`) sit outside this list: their
removed lines are header lines plus canonical evolution PROVIDED each target copy is byte-identical to the
vault's tag for the version it adopted — check that blob match (D1, Phase 3: the estimator's three changed
replace-mode files matched `set-v1.3`; MEMORY_PROTOCOL's 3 non-header lines are the v2.2 identifier scrub).

## 9. Operator decision points (Phase 2 — answer with the approval)

- **D17.A — approve the plan** ("plan 017 is approved", or "APPROVE PLAN-017" with any D-deltas).
- **D-1 — the old `scripts/bootstrap_memory.sh`.** RECOMMEND **A**: the owner's session deletes it
  (+ manifest row + tree line) once `status` says OK — step 4 of the § 5n entry; it is their repo and
  their Rule 8, and until then it is the fallback. B: the curator removes it in a third direct commit
  at closure — the approval commit then drops step 4 from the § 5n entry and adds the commit to
  § 7 (re-run the § 5 round-trip).
- **D-2 — the four existing adopters' copies of the tool (0.1).** RECOMMEND **A**: defer to v2.8's
  script-delivery fix (none is on Windows; E002 hits them only after a folder move, with the
  documented workaround). B: hand-copy 0.2 into Capital-Signal now (outside the engine's handoff
  discipline).
- **D-3 — closure gate.** RECOMMEND **A**: the plan closes only with QA-M8 + QA-M9 evidence (Rule 15).
  B: an explicit operator waiver for QA-M8 recorded in the tracker, then close after Phase 3.
- **D-4 — the handoff's wording for a committed (git) write.** RECOMMEND **A**: explain it in the
  § 5n entry (step 2: "review" = `git show` of the engine commit) and leave the engine fix to PLAN-014
  (PLAN-013 R6). B: fix `render_handoff` here (Critical engine change; widens this plan — a plan
  revision with new § 5 blocks + a fresh Rule 13 pass before approval).
- **D-5 — registry lifecycle.** RECOMMEND **A**: `onboarding` from Phase 3, `active` at closure
  (§ 6f). B: `active` from Phase 3 — § 5d's value changes in the approval commit and § 6f's FIND drops
  out of the closure commit (config/projects.toml leaves § 7.6).

### 9.1 Decision record (Phase 2, 2026-10-05)

- **D17.A — APPROVED:** operator *"Plan-017 is approved"* (2026-10-05).
- **D-1 … D-5 = A** — not answered item by item; the agent's read (approving the drafted plan = its
  recommended options, which the § 5 blocks and the § 5n entry implement) was stated in chat and
  confirmed at the approval-commit gate:
  - **D-1 = A** — the owner's session deletes `scripts/bootstrap_memory.sh` (+ manifest row + tree line)
    once `status` says OK (§ 5n step 4).
  - **D-2 = A** — tool 0.2 reaches the four existing adopters at v2.8's script-delivery fix.
  - **D-3 = A** — the plan closes only with QA-M8 + QA-M9 evidence (Rule 15; no waiver).
  - **D-4 = A** — the handoff's wording for a committed (git) write is explained in the § 5n entry
    (step 2); the engine fix stays with PLAN-014.
  - **D-5 = A** — `lifecycle = "onboarding"` from Phase 3, `"active"` at closure (§ 6f).
- **No § 5 change:** the blocks re-extracted from this file are byte-identical to the proven blocks
  (re-verified in the approval commit).

## 10. Rollback path

- **Vault:** `git revert` the Phase 3 commit — tool 0.1 back (the vault's own link is a plain symlink,
  untouched by the change), registry entry gone (the estimator simply stops being synced).
- **Estimator:** `git revert` the engine commit, then the prep commit — new commits on `main`, never a
  force-push (their Rule 3). Their old memory link keeps working throughout: `bootstrap_memory.sh` and
  its junction stay until `adopt` succeeds (D-1 = A).
- **Owner's PC:** `adopt` keeps the original harness dir as `<key>.pre-locality-<stamp>`; to undo:
  remove the junction (`cmd //c rmdir`), rename the backup back, re-run `bash
  scripts/bootstrap_memory.sh`.
- **Capital-Signal:** the write-back only rewrites E002's Status line; its next session can revert it.

## 11. Known risks + mitigation

| # | Risk | Mitigation |
|---|---|---|
| R1 | Claude Code's Windows path-key differs from the drive-form rule | No destructive step acts on a missing path: `adopt` with no dir at the computed key says "Nothing to adopt" and touches nothing; the old junction keeps the memory reachable; QA-M8's fresh-session recall proves the key; NTFS is case-insensitive, so the drive letter's case cannot split it |
| R2 | Git Bash does not report a junction as a symlink | `is_link` falls back to comparing the entry's resolved path with its parent's; QA-M8 checks `status` OK after `adopt` and `link` idempotence |
| R3 | A live session holds the harness dir | the 2-minute transcript guard refuses first; the rename is atomic (fails clean); the restore line prints before any copy; the backup is kept |
| R4 | The owner pushes while the engine writes | push is fast-forward only → the write fails, nothing overwritten; re-run the dry-run, then `--write` |
| R5 | The owner has unpushed local work touching the synced files | governance files only; their next `git pull` merges or reports conflicts in docs they own; the operator tells them first (§ 2) |
| R6 | The handoff's "review `git diff`" does not fit a committed write | D-4 = A: the § 5n entry says what to do; PLAN-014 owns the engine wording |
| R7 | Tool 0.2 regresses the Mac/Linux targets or the vault | POSIX branch = 0.1 semantics + the E002 fix; 7 POSIX tests; QA-M3 on the live vault store |
| R8 | The estimator moved past `45d7c75` before Phase 3 | the reconcile pass re-checks all 21 estimator FINDs on the live tip; a mismatch is a plan defect |
| R9 | The vault Set Version moves before Phase 3 (a v2.8 lands first) | the catch-up delivers whatever is current; § 5e / § 5n / § 5p name v2.7 → a reconcile defect, text updated in the approval or reconcile step |
| R10 | The owner's name sits in the vault, which the 780-AI GitHub mirror shows to org members | operator-supplied for the registry (§ 2); `config/projects.toml` + the opener § 2 row only — never in `docs/standards/` or `skill/` (QA-M10) |
| R11 | Capital-Signal busy when the write-back runs | QA-M7's idle check first; the engine write accumulates in its handoff either way |

## 12. Acceptance criteria

1. QA-M1…M7 + M10 ✅ in the Phase 3 session with evidence pasted in the tracker; QA-M8 + M9 ✅ (or an
   operator waiver for M8, D-3 = B) before closure.
2. The estimator's `main` carries exactly two curator-side commits from this plan — the prep (§ 7.2)
   and the engine's sync (§ 7.3) — and no force-push.
3. Vault `status` lists 780-estimator **v2.7 / v2.7 current** over git; the re-run dry-run is a no-op.
4. The owner's Claude memory count after `adopt` equals the count before (QA-M8).
5. Capital-Signal E002 reads `integrated → vault scripts/claude_project_data.sh v0.2 (…)`.
6. Every manifest cell touched equals its file header (grep, L063); governance scripts exit 0 in the
   vault (stdout pasted, Rule 6).
7. Plan + tracker 1.0 / CLOSED; OPEN_TASKS updated; the v2.8 queue holds Rule 16 items 4, 5, 8 and
   the D-2 delivery item.

## Rule 13 senior-review pass (2026-10-05)

Run on the complete plan + tracker, after drafting, with the canonical § 15.8 prompt.

**Mechanical (L051 — tools on the code exactly as it ships):** all 33 blocks re-extracted from THIS
file by a parser (round-trip identical to the proven blocks) and applied to brand-new copies of the
vault (`8b914db`) and the estimator (`45d7c75`, re-confirmed live by `ls-remote`) with `<P3-DATE>` =
2026-10-05: every FIND matched once, both pre-image blobs matched, both new files were absent, the
§ 5k copy was byte-identical. QA-M1: ruff clean, `MYPYPATH=src mypy` 0 issues in 25 files, pytest 151.
QA-M2: the 11 tests against tool 0.1 → 6 failed / 5 passed (exactly the new-behavior cases). QA-M10:
grep clean. Estimator: its two governance scripts exit 0 / 0; the prep committed with the § 5o message
extracted from this file; over the git transport (local bare remote): `status` v1.3 / v2.7 behind →
dry-run 7 of 11 → removed lines 28 / 19 / 6 / 3 == § 8.1 → `--write` 8 files in one engine commit whose
parent is the prep → re-run up-to-date → `status` v2.7 current.

**Findings fixed in place:**

1. **Defect — domain-neutrality of the delivered tool.** The tool is copied verbatim into every
   adopter, yet its 0.2 change log named a fleet project and the Windows test fixture used a path with
   the owner's name. Both genericized (§ 5a / § 5b re-rendered); QA-M10's grep now covers the tool and
   its test.
2. **Defect — ordering.** § 5d / 5e (registry + opener row) were scheduled with the other vault blocks
   in step 3.2, before the prep commit reaches their `main`: any `status` / `fleet` / governance run in
   between would probe a repo the engine cannot read. Moved to step 3.4 (§ 5 "Order", § 4, tracker).
3. **Gap — midnight.** § 8.1's exact counts assumed the prep and the engine stamp the same date; the
   rule for a session crossing midnight is now stated (+1 `Last Updated` line per stamped doc).
4. **Gap — D-item consequences.** Each option B now says what it changes in the plan (D-1, D-4, D-5);
   choosing one means an approval-commit edit and a fresh round-trip, not a silent divergence.
5. **Gap — Windows wording in the template.** Rule 14 and the session files say "symlink"; on Windows
   it is a junction. A `docs/standards/` edit → queued for v2.8 (§ 3), not widened into this plan.

**Optimizations applied:** whole-file replace with a pinned pre-image blob for the two rewritten files
(the reconcile pass proves the live file is exactly what the plan expects, instead of 20+ hunks); the
§ 5n entry carries the owner's whole next-session sequence (handoff landing, `adopt`, cleanup, evidence)
so the git-write handoff gap (D-4) needs no engine change here.

**Considered and declined:** (a) a `trap` restoring the backup on any Windows failure — the restore
line printed before the copy plus a kept backup is simpler and leaves the operator in control;
(b) making the POSIX branch copy-then-swap like Windows — it would change proven behavior on the four
Mac / Linux targets and the vault for no benefit there.

**Edge cases walked:** a live session (guard + atomic rename), cross-drive harness/repo (copy, not
move), a pre-existing in-repo `memory/` during the old-layout migration (left in place, reported), a
concurrent owner push (fast-forward only), the estimator moving before Phase 3 (reconcile), a Set
release before Phase 3 (R9), Capital-Signal busy (idle check), a key mismatch (no destructive step on
a missing path, R1), Git Bash not reporting a junction as a symlink (R2).

**No new design decision surfaced** beyond D-1…D-5 (§ 9).
