<!-- VERSION: 0.3 -->
<!-- Last Updated: 2026-10-03 -->
<!--
CHANGE LOG
v0.3 — 2026-10-03 — PLAN-011 (S2): § 3 lessons-archive bullet made explicit — archive/LESSONS.md is a SYNC_MAP replace item, so a converging project's own archive is preserved verbatim as archive/LESSONS_LEGACY.md (frozen, carrying the numbering crosswalk) and every entry is classified; nothing dropped silently.
v0.2 — 2026-08-19 — W-D1 fix: the sync-ready SVA shape gains the required CHANGE LOG comment block — the engine's record-update (sync.py _split_header) hard-requires it; the spec omitted it (the pilot adoption dodged the defect only because its session wrote the block unprompted).
v0.1 — 2026-08-16 — Initial (PLAN-009, Set v2.0). Migration mode for EXISTING projects: dry-run
gated, customization-preserving; absorbs the MEMORY_DURABILITY_ROLLOUT_PROMPT retrofit; performs
the one-time v1.6 heading-wrap sync needs.
-->

# adopt mode — migrate an EXISTING project onto the suite

Precondition: SKILL.md Step 0 ran (`$VAULT` / `$SUITE` / `$SET_VERSION` / `$VAULT_SHA` resolved).

**This is a migration, not a bootstrap.** The worst case is clobbering the project's own
customizations — therefore NOTHING is written before the operator approves the dry-run list (§ 4).

## 1. Target + pre-flight gates (all three are hard gates)

- Ask for TARGET. Confirm it is a git repo (`git -C <TARGET> rev-parse --show-toplevel`).
- **Clean tree required:** `git -C <TARGET> status --short` must be empty. Otherwise STOP — the
  operator commits or stashes first (the adoption diff must stand alone).
- Ask the operator which state the project is in: (a) never-standardized; (b) old-SETUP adopter
  (carries the suite at an older Set Version); (c) divergent line (evolved its own variant of the
  suite). If (b): STOP — no adoption needed; the path is register + one-time v1.6 heading-wrap +
  `sync` catch-up (see SKILL.md).

## 2. Intake-first check

Ask: does this project hold novelties the vault should learn from (its own lessons, rules,
conventions)? If yes and they have not been intaken, PAUSE adoption and tell the operator the
intake flow runs FIRST (grab → genericize → vault — the PLAN-010 pattern, curator-side). Adoption
NEVER copies target novelties into the vault silently, and it must not overwrite them locally
before they are captured.

## 3. Inventory + mapping table (posted in chat, before any dry-run)

Walk the target and post one table: existing artifact → suite slot → planned action
(`keep` | `wrap in PROJECT-OWNED` | `merge` | `replace` | `create`). Cover at minimum:

- Root `CLAUDE.md` (or equivalent contract): its project-specific content (§ 1 context, § 4
  critical files, § 13 domain bullet, § 14 agency) maps INTO the suite template's PROJECT-OWNED
  blocks; local rules map to the matching vault rule number, or to project-specific rows/sections.
- Any existing lessons archive (`archive/LESSONS.md` or wherever the project keeps it): the suite's
  `archive/LESSONS.md` is a SYNC_MAP **replace** item — it arrives suite-owned from the vault and
  every later sync overwrites it — so the project's own archive can never survive in place.
  (1) Classify EVERY entry in this table: already in the vault canonical LESSONS (cite the vault
  L-number) | portable and not yet in the vault | project-specific. (2) Portable entries not yet
  in the vault are intake items (§ 2) — they reach the vault BEFORE adoption, never by being
  merged into the suite's `LESSONS.md` locally. (3) The archive itself is preserved verbatim:
  `git mv` it to `archive/LESSONS_LEGACY.md` (history follows the file), then prepend a freeze
  banner — frozen on the adoption date, read-only, NOT a SYNC_MAP item, new lessons go to
  `docs/STANDARDS_LOG.md` as `E0NN` entries — plus a **numbering crosswalk** (own lesson and rule
  numbers → suite numbers) whenever the project's numbering diverged; own-line numbers cited in
  documents dated before adoption resolve through it. Register it in the project manifest.
  Nothing is dropped silently.
- Session opener/closer files (any form) → instantiated suite templates with the project's § 2
  registry + § 3.2 rows carried over; **the PROJECT-OWNED instance-heading wrap is applied** (the
  v1.6 requirement sync's ordinal matching needs).
- Governance scripts / CI / manifest / folder-structure docs: keep what exists and works; create
  the missing scaffolds.

## 4. DRY-RUN GATE (hard)

Post the full would-change list — every file to be created, replaced, merged, or wrapped, with a
one-line "what changes" per file — and WAIT for the operator's written approval. Nothing is
written before that approval. If the run later deviates from the approved list, STOP and re-gate.

## 5. Apply (only after § 4 approval)

Per the approved list, copying suite content from `$SUITE` (read-only on the vault), preserving
every mapped customization inside PROJECT-OWNED markers. Also:

- TARGET/`docs/SET_VERSION_ADOPTED.md` — Standard Set Version `$SET_VERSION`, vault commit
  `$VAULT_SHA`, adopted <today>, delivered by the standard-docset skill (adopt mode). Write it
  **sync-ready** — the engine's mechanical record-update hard-requires this shape (SyncError
  otherwise): `<!-- VERSION: 0.1 -->` + `<!-- Last Updated: <today> -->` comment lines; a CHANGE
  LOG comment block — `<!--`, then `CHANGE LOG`, then the line `v0.1 — <today> — Adoption record
  created by the standard-docset skill (adopt mode): Standard Set Version $SET_VERSION, vault
  commit $VAULT_SHA.`, then `-->` — the record-update splits the header at this block's closing
  `-->` and prepends its own log line into it; omitting the block breaks every future
  record-update (W-D1); the two
  exact bullets `- **Standard Set Version:** $SET_VERSION (…)` and `- **Adopted on:** <today> (…)`;
  and a seeded backport table (header `| Set Version | Adopted on | Notes |`, separator
  `|---|---|---|`, one initial row for this adoption).
- TARGET/`docs/STANDARDS_LOG.md` — instantiate from `$SUITE/STANDARDS_LOG.md` (drop the example)
  if absent; existing log kept as-is.
- Project-data locality (Rule 14): COPY `$VAULT/scripts/claude_project_data.sh` verbatim; run
  `adopt` (machine already has harness data for this path) or `link`; paste output; seed
  `docs/MACHINE_MIGRATION.md` if absent; ensure `.claude/` + `docs/Plans/OPEN_TASKS.md` are
  gitignored; seed `OPEN_TASKS.md` if absent.
- Governance scaffolds (the two check scripts + TOMLs) if absent — never overwrite existing ones.

## 6. Validate

- Governance scripts exit 0 (paste stdout verbatim).
- Marker integrity: every `PROJECT-OWNED:BEGIN` has its `END`; the three mixed files carry the
  instance-heading block; counts match the template (sync's strict count check will enforce this —
  verify it here first).
- `git status --short` matches the approved § 4 list EXACTLY — any extra/missing file is a STOP.

## 7. Review + commit

Named review table → "go on commit?" → `git add -A`, re-check `git status --short`,
`git commit -F /tmp/adopt_commit_msg.txt` (single "adopt-standards" commit). **DO NOT PUSH.**

## 8. Post-adopt (curator-side, outside this session)

(1) Register the project in the vault's `config/projects.toml` (transport per where it lives);
(2) run a vault-side `sync` dry-run — a freshly-adopted target should report current/no-op;
(3) the project's log-recording discipline is now binding: new experience lands ONLY as `E0NN`
entries in its `STANDARDS_LOG.md` (`Status: open`), harvested by the vault — never as edits to its
own suite files.
