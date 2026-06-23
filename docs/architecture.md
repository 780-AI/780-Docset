<!-- VERSION: 0.9 -->
<!-- Last Updated: 2026-06-23 -->
<!--
CHANGE LOG
v0.9 — 2026-06-23 — PLAN-007 (remote-target transport) landed. § 1 adds the "Reach" note (local or remote git/ssh via a pluggable transport; no server). § 8 registry note → per-target `transport` + connection fields; new "Transport" paragraph (materialize → operate → flush; git fast-forward push; per-target failure non-fatal for reads). § 9 read-before-write extended to fetch-fresh materialization + per-target atomic write-back. § 10 marks PLAN-007 ✅ done. § 11 records the transport decisions (D1–D4 / DD-1…DD-6) as DECIDED. Engine behavior added; read-only on the vault (no docs/standards/ edit) → no Set Version change.
v0.8 — 2026-06-21 — Drift fix: § 10 roadmap corrected the stale slice→plan numbering. `sync` is PLAN-008 (was PLAN-007); PLAN-007 is the remote-target transport infrastructure expansion inserted before `sync`. Matches the live planning state. Doc-only; no engine behavior change.
v0.7 — 2026-06-18 — PLAN-006 (Slice 4): `integrate` landed. § 8 marks integrate implemented (read-only worksheet + operator-gated Status write-back; A1 division of labor — tool = deterministic spine, Claude authors the lesson + vault edits in-session) + adds the integrate behavior note. § 10 ticks Slice 4 ✅. § 11 resolves the last OPEN decision (genericization hands off to a Claude session — A1; the tool is pure-Python, never calls a model). Read-only on the vault; no Set Version change (no docs/standards/ file touched).
v0.6 — 2026-06-17 — PLAN-005 (durable memory): engine-slice plan numbers shifted — § 10 annotates Slice 4 = PLAN-006 (`integrate`), Slice 5 = PLAN-007 (`sync`), with a note that PLAN-005 is the durable-memory governance change (not a slice); § 11 OPEN item now resolves at PLAN-006. No engine behavior change.
v0.5 — 2026-06-16 — PLAN-004 (Slice 3): `harvest` landed. § 8 marks harvest implemented (stdout report grouped by area; cautious cross-project dup flag) + adds the harvest behavior note. § 10 ticks Slice 3 ✅. Read-only; no Set Version change (no docs/standards/ file touched).
v0.4 — 2026-06-16 — PLAN-003 (Slice 2): first engine code landed. § 8 marks status/drift implemented (registry stores name + path only; adopted version read live). § 10 ticks Slice 2 ✅. § 11 strikes the three now-decided items (registry format/location; CLI entry point; status/drift = two commands). Read-only; no Set Version change (no docs/standards/ file touched).
v0.3 — 2026-06-14 — Project display name → "Standard DocSet" (doc title). Engine package `standard_document_updater` unchanged.
v0.2 — 2026-06-13 — PLAN-002 (Slice 1) landed at the document layer (Set Version v1.1): SETUP.md now performs the strip; the STANDARDS_LOG.md template and the PROJECT-OWNED markers exist; SET_VERSION_ADOPTED moved to docs/. Ticked § 10 Slice 1 done and updated the § 4 "not yet" note and the § 7 markers note to past tense.
v0.1 — 2026-06-13 — Initial system-design record. Captures the design converged with the operator across the 2026-06-13 design session: the vault model, the project footprint (operative standard kept / setup machinery stripped), the setup-and-strip delivery, the experiences-log contribution channel, the harvest→integrate→sync loop, and the section-ownership (PROJECT-OWNED marker) model for non-clobbering sync. This is the design reference the engine implements; kept in sync with the engine per CLAUDE.md § 4.
-->
# Architecture — Standard DocSet

> **Status: design (engine not yet built).** This is the agreed system design. Implementation is sliced
> into plans under `docs/Plans/` (§ 10). The engine source, once it lands, is the dispositive truth and
> this doc is kept in sync per `CLAUDE.md` § 4.

## 1. Purpose & objective

Keep **every project in the organization developing the same standard way**, and **improve that
standard over time** by harvesting real experience from those projects. The standard is a *living* body
of governance documents; this tool operationalizes the loop that grows it and keeps every project
current.

**Primary objective: org-wide consistency** — every project, over time, follows the same evolving
standard. (Not IP secrecy — the concern is uniform practice, not concealment.)

**Reach (PLAN-007).** The tool runs locally but operates on each project *wherever it lives* — a folder
on this machine, or a remote repo reached over git/ssh — via a pluggable transport layer. It stands up
no server of its own: git/ssh/rsync use the operator's existing credentials to reach repos that already
exist. (This retires the earlier "operates on local repository checkouts / no remote infrastructure"
framing; see `CLAUDE.md` § 1.)

## 2. The vault model

- **This repo is the VAULT** — the single canonical home of the full, domain-neutral standards suite
  (`docs/standards/`) plus the engine that runs the loop.
- **Projects ADOPT the suite** but keep only the **operative standard** (§ 3), not the
  setup/maintenance machinery.
- **Source-of-truth split:** the vault owns the *generic* standard; each project owns *its own
  customizations* (its context, its critical-files list, its environment mapping). Sync reconciles the
  two without either clobbering the other.

## 3. Project footprint — what a set-up project carries

| Category | Files | In project? | Why |
|---|---|---|---|
| **Operative standard** (governs how you build) | `CLAUDE.md` (root), the topical library (ENGINEERING / CICD / VALIDATION / PROJECT / PROMPT / MEMORY), `LESSONS.md`, project-local `SESSION_OPENER/CLOSER`, governance scripts, CI, manifest | **Kept** | this is *what makes every project behave identically*; dropping it causes drift |
| **Contribution channel** | `docs/STANDARDS_LOG.md` (§ 5) | **Kept** | the project's outbox of experiences to feed back |
| **Setup / maintenance machinery** (only used to *deliver or maintain* the suite) | `SETUP.md`, `NEW_PROJECT_BOOTSTRAP.md`, `STANDARDS_INDEX.md`, meta `README.md`, `HOW_TO_USE.md`, `PROJECT_INSTRUCTIONS_TEMPLATE.md`, the CLAUDE/LESSONS/SESSION **templates** | **Stripped** | never runs during normal development → zero operational cost to remove |

Deleting the machinery satisfies "don't leave the whole ready-to-deploy package in the project" with no
effect on how the project operates.

## 4. Setup-and-strip (delivery: vault → project)

1. Copy the suite into the new project's `docs/standards/` — a transient **delivery crate**.
2. Run `SETUP.md` inside the project. It:
   - instantiates the operative files (root `CLAUDE.md` with placeholders filled; project-local
     `docs/SESSION_OPENER/CLOSER.md`; governance scripts; CI; manifest; `docs/STANDARDS_LOG.md`),
   - copies the **kept** files to their permanent homes (the topical library + `LESSONS.md` stay; the
     instantiated `CLAUDE.md` → root; `SET_VERSION_ADOPTED.md` → `docs/` so it survives),
   - makes everything operational (governance exits 0, first commit),
   - **deletes the setup-machinery files** from `docs/standards/` (the crate's packing materials).
3. The **vault keeps its own `docs/standards/` permanently** — the strip only ever happens in *target*
   projects.

> Note: `SETUP.md` performs the strip as of Slice 1 (PLAN-002, Set Version v1.1) — see § 10.

## 5. The experiences log — the contribution channel

A committed, append-only file per project: **`docs/STANDARDS_LOG.md`** (a kept file; survives the
strip). Entry schema:

```
## E007 — Enumerate every read site before splitting a global state variable
- Date:        2026-06-13
- Area:        engineering / refactor        # routes to the right topical file
- Status:      open                          # open | integrated | rejected
- Context:     <what happened — the incident/observation>
- Learned:     <the takeaway>
- Suggested:   <e.g. ENGINEERING_STANDARDS sub-section + a lesson>
- Portability: <project-specific | general>  # a hint for the curator
```

**Lifecycle:** `open` → harvest reads it → vault integrates → harvest **writes the status back**:
`Status: integrated → vault L050 (ENGINEERING_STANDARDS § 1.10, Set Version v1.1)`  (or
`Status: rejected — project-specific, not portable`). That write-back is "mark each item done."

**Feed:** `SESSION_CLOSER.md` § 1.7 (the wrap-up routine) already scans each session for lesson
candidates. Confirmed candidates are appended to `STANDARDS_LOG.md` — giving the existing routine a
committed, harvestable destination instead of the throwaway `OPEN_TASKS.md`.

## 6. The closed loop

```
   VAULT  ──(4 setup)──►  PROJECT  ──(append)──►  STANDARDS_LOG (open items)
     ▲                                                  │
     │                                                  │ (a) harvest  [read-only]
     │  (c) integrate [gated: genericize → L0NN →       ▼
     │      topical update → bump Set Version]      consolidated report
     │                                                  │
     └──────────────────────────────────────────────────┘
     │
     └──(d) sync [gated: push new Set Version to every project, honoring ownership]──►  all PROJECTS
                                                                                        (b) mark-done write-back
```

- **(a) harvest** — read every registered project's `STANDARDS_LOG.md`; collect `open` entries;
  emit a consolidated report grouped by area, flagging likely cross-project duplicates. *Read-only.*
- **(b) mark-done** — after integration, write each entry's new status + vault back-ref into its
  project's log.
- **(c) integrate** — operator + AI: per entry decide integrate / defer / reject; genericize (no
  names); assign the vault's next `L0NN`; write the lesson into `LESSONS.md`; update the routed topical
  file; bump per-file `VERSION` + the **Set Version**. *Operator-gated; a Critical-File edit → follows
  the § 15 plan/review discipline.*
- **(d) sync** — propagate the new Set Version to every project (§ 7). *Operator-gated.*

## 7. Ownership model + non-clobbering sync

Sync must update the standard in each project **without** overwriting that project's customizations.
The difficulty is concentrated, because most of the suite is **100% suite-owned**:

| File(s) | Ownership | Sync behavior |
|---|---|---|
| topical library, `LESSONS.md` | suite-owned | **whole-file replace** + version bump |
| `CLAUDE.md` | mixed | **section-merge** — overwrite suite sections (§3 rules, §5–12, §15); preserve project sections (§1 context, §4 critical files, §13 domain bullet, §14 agent choice) |
| `docs/SESSION_OPENER/CLOSER.md` | mixed | **section-merge** — overwrite the routine; preserve §2 environment mapping + §3.2 project rows |

**Mechanism — `PROJECT-OWNED` markers.** Customizable blocks are wrapped in explicit markers so sync
knows what never to touch:

```
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
## 1. Project context
...the project's own values...
<!-- PROJECT-OWNED:END -->
```

Sync replaces everything **except** marked blocks. Simple, explicit, agent-verifiable. The markers were
added to the CLAUDE.md + session **templates** (so every adopter inherits them) and to this repo's own
adopter instances in Slice 1 (PLAN-002, Set Version v1.1).

**The enabling protocol:** per-file `VERSION` headers + the `Set Version` are what make drift
machine-detectable ("is this project's copy behind the vault?"). The suite's own discipline *is* the
protocol the engine runs on.

## 8. The engine (command surface)

A Python CLI (per `CLAUDE.md` § 1). All write commands are operator-gated; read commands are safe.

| Command | Reads | Writes | Gate |
|---|---|---|---|
| `status` / `drift` ✅ | vault + each project's Set Version + open log count | — | none (read-only) |
| `harvest` ✅ | every project's `STANDARDS_LOG.md` | a consolidated report (to stdout) | none (read-only) |
| `integrate` ✅ | open log entries (worksheet) + the decisions TOML (write-back) | project logs (the matched `Status:` line, gated); the **vault** edits (LESSONS + topical + Set Version) are authored by Claude in-session, not by the tool | operator-approved (write-back is dry-run unless `--write`) |
| `sync` | vault Set Version | every project (honoring `PROJECT-OWNED` markers) | operator-approved |
| `setup` | the delivery crate | the new project (then strips) | operator-run; this is `SETUP.md` |

**Registry:** a vault-side config (`config/projects.toml`) listing each managed project — its
**`transport`** (`local` | `git` | `ssh`; default `local`) plus the connection fields that transport
needs (local: `path`; git: `git_url`/`git_branch`; ssh: `ssh_host`/`ssh_path`). A project's adopted Set
Version is **read live** from the materialized `docs/SET_VERSION_ADOPTED.md` at report time (never cached
in the registry — single source of truth, § 9). `status`/`harvest`/`sync` iterate it. *(Registry
implemented Slice 2 — PLAN-003; per-target transport fields added PLAN-007.)*

> `harvest` implemented Slice 3 — PLAN-004: parses every project's `STANDARDS_LOG.md`, collects the
> `open` entries, prints a consolidated report grouped by area to stdout, and conservatively flags
> likely cross-project duplicates (same normalized title across *different* projects). Read-only;
> always exits 0 (no persisted file — the source logs are the durable record).
>
> `integrate` implemented Slice 4 — PLAN-006 (A1 division of labor: the tool is the **deterministic
> spine**; Claude authors the genericized lesson + the vault edits in-session under the § 15 flow — the
> tool never calls a model and never edits the vault). Two modes: (a) `integrate` prints a **read-only
> worksheet** — each open entry enriched with its Area→topical routing (unknown Area → `PROJECT_STANDARDS.md`
> + a visible `⚠ unrouted` flag), a proposed sequential `L0NN`, and the current Set Version; always exit 0.
> (b) `integrate --apply <decisions.toml>` performs the operator-gated **Status write-back** — default is a
> **dry-run** diff; `--write` actually writes. It validates every disposition first (no partial writes),
> re-reads each target log immediately before writing (§ 9), and rewrites **only** the matched `Status:`
> line, leaving the rest byte-identical. Read-only on the vault — no Set Version change when the tool is run.

**Transport (PLAN-007).** All four commands are **transport-aware**: each target is *materialized* to a
local root — `local` = the folder in place; `git` = a shallow + blobless + sparse-`docs/` clone (the
write path materializes the full branch tip so a commit can be pushed); `ssh` = an rsync of `docs/` — and
the engine performs its existing Path-based I/O against that root. On the write path the transport
*flushes* the change back: `git` = commit + **fast-forward** `push origin HEAD:<branch>` with a fixed
`Standard DocSet <standard-docset@localhost>` identity (never mutating the target's git config, no
`--force`); `ssh` = rsync the changed files back. The engine stays transport-agnostic — the seam is
`cli.py` only (the read/write functions keep their Path-based signatures). A per-target transport failure
is **non-fatal for reads** (`status`/`drift` show the target `unknown`; `harvest`/`integrate` warn on
stderr and skip); a write-path failure is fatal for that run, but every named target is materialized +
validated before any push, so a fetch failure aborts before anything is written. No secrets are handled —
git/ssh/rsync use the operator's existing SSH agent/keys.

## 9. Invariants

- **No project name anywhere** in the suite (the domain-neutral rule — the dispositive scrub grep stays
  green). Integration genericizes before anything enters the vault.
- **Lessons are append-only**; the vault assigns the canonical `L0NN` (project logs use their own
  `E0NN` ids; integration maps `E→L`).
- **Every change to the suite** bumps per-file `VERSION` + the `Set Version`.
- **Sync never clobbers** a `PROJECT-OWNED` block.
- **Read before write**: the engine re-reads a target's on-disk files before acting (never a cached
  version) — per `CLAUDE.md` § 2. Across a transport (PLAN-007) this means a **fetch-fresh
  materialization** immediately before the run, and a **per-target atomic** write-back:
  `integrate.apply_writeback` validates **every** disposition before **any** write, then each target's
  change is flushed/pushed independently. True cross-target atomicity across N independent remotes is
  impossible, so a mid-sequence push failure is reported loudly — never a silent partial success.

## 10. Implementation roadmap (slices → plans)

Each slice is a vital change → its own `PLAN-NNN` (§ 15 workflow). Suggested order (mechanical/low-risk
first; judgment-heavy last):

1. ✅ **Slice 1 — Setup-and-strip + log + markers** (done — PLAN-002, Set Version v1.1). Added the strip
   step to `SETUP.md`; defined the kept/stripped manifest; added the `STANDARDS_LOG.md` template; added
   `PROJECT-OWNED` markers to the CLAUDE.md + session templates **and** this repo's adopter instances;
   moved `SET_VERSION_ADOPTED` to `docs/`. *(Docs/prompt only — no engine yet.)*
2. ✅ **Slice 2 — Registry + `status`/`drift`** (done — PLAN-003). Shipped the registry (`config/projects.toml`,
   name + path; adopted version read live) and the first Python engine: read-only `status` / `drift`
   reports of each project's Set Version vs vault and its open log count. *(First engine code.)*
3. ✅ **Slice 3 — `harvest`** (done — PLAN-004). Parses every `STANDARDS_LOG.md`; consolidates `open`
   entries into a stdout report grouped by area; conservatively flags cross-project duplicates.
   Read-only; always exits 0. *(No Set Version change — the engine reads the log, never alters the suite.)*
4. ✅ **Slice 4 — `integrate`** (done — PLAN-006). Read-only worksheet (open entries + Area→topical +
   proposed `L0NN` + Set Version) for Claude to author each genericized lesson in-session; operator-gated
   `--apply` Status write-back (dry-run unless `--write`; validate-all-before-write; rewrite only the
   matched `Status:` line). A1: the tool is the deterministic spine — the genericization + vault edits stay
   in-session. *(No Set Version change — building the tool is read-only on the vault.)*
5. **Slice 5 — `sync` (PLAN-008).** Section-aware propagation honoring `PROJECT-OWNED`; whole-file for
   suite-owned. Sequenced after PLAN-007 (remote-target transport, ✅ done — see note below), which `sync`
   builds on to write to many remote adopters.

> Plan numbering: PLAN-005 is the durable-memory governance change (Rule 14 / Set v1.2), not an engine
> slice. **PLAN-007 — the remote-target transport (`local` | `git` | `ssh`) — ✅ done**: a non-slice
> infrastructure expansion inserted before `sync` (since `sync` writes to many remote adopters), it made
> all four commands transport-aware in one plan. The `sync` engine slice is therefore PLAN-008. (Earlier
> revisions mapped `sync` → PLAN-007; corrected here.)

## 11. Open decisions (to resolve as each slice is planned)

- ✅ **DECIDED (PLAN-003, Slice 2)** — Registry format + location: `config/projects.toml`, storing
  **name + path only**; the adopted Set Version is read live (not cached in the registry).
- ✅ **DECIDED (PLAN-003, Slice 2)** — CLI name / entry point: `python -m standard_document_updater <command>`
  (`status` / `drift` are two subcommands, not one command with a flag).
- ✅ **DECIDED** — Final home of `STANDARDS_LOG.md`: `docs/STANDARDS_LOG.md` (survives the setup strip).
- ✅ **DECIDED (PLAN-006, Slice 4)** — `integrate`'s genericization **hands off to a Claude session**
  (A1): the tool is pure-Python — it builds the worksheet and writes the `Status:` lines back, but never
  calls a model and never edits the vault. The lesson prose + the LESSONS/topical/Set-Version edits are
  authored by Claude in-session under the § 15 flow.
- ✅ **DECIDED (PLAN-007)** — Remote-target transport: a per-target `transport` key in
  `config/projects.toml` (`local` default = full back-compat) — **DD-1**; *materialize-to-local-root*
  abstraction, the transport seam confined to `cli.py` — **D1 / DD-2**; git write-back = **fast-forward
  direct push** with a fixed `Standard DocSet` commit identity (the `glab`/`gh` merge-request variant
  deferred) — **D2 / DD-5 / DD-6b**; **all** commands transport-aware in one plan — **D3**; git read fetch
  = shallow + blobless + sparse `docs/` — **D4**; per-target atomic write-back, per-target transport
  failure non-fatal for reads — **DD-3 / DD-4**; building the transport is read-only on the vault → **no
  Set-Version bump** — **DD-6**.
