<!-- VERSION: 0.2 -->
<!-- Last Updated: 2026-06-13 -->
<!--
CHANGE LOG
v0.2 — 2026-06-13 — PLAN-002 (Slice 1) landed at the document layer (Set Version v1.1): SETUP.md now performs the strip; the STANDARDS_LOG.md template and the PROJECT-OWNED markers exist; SET_VERSION_ADOPTED moved to docs/. Ticked § 10 Slice 1 done and updated the § 4 "not yet" note and the § 7 markers note to past tense.
v0.1 — 2026-06-13 — Initial system-design record. Captures the design converged with the operator across the 2026-06-13 design session: the vault model, the project footprint (operative standard kept / setup machinery stripped), the setup-and-strip delivery, the experiences-log contribution channel, the harvest→integrate→sync loop, and the section-ownership (PROJECT-OWNED marker) model for non-clobbering sync. This is the design reference the engine implements; kept in sync with the engine per CLAUDE.md § 4.
-->
# Architecture — standard-document-updater

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
| `status` / `drift` | vault + each project's Set Version + open log count | — | none (read-only) |
| `harvest` | every project's `STANDARDS_LOG.md` | a consolidated report | none (read-only) |
| `integrate` | the harvest report | the **vault** (LESSONS + topical + Set Version) and project logs (mark-done) | operator-approved per entry |
| `sync` | vault Set Version | every project (honoring `PROJECT-OWNED` markers) | operator-approved |
| `setup` | the delivery crate | the new project (then strips) | operator-run; this is `SETUP.md` |

**Registry:** a vault-side config (e.g. `config/projects.toml`) listing each managed project — name,
path, adopted Set Version. `status`/`harvest`/`sync` iterate it.

## 9. Invariants

- **No project name anywhere** in the suite (the domain-neutral rule — the dispositive scrub grep stays
  green). Integration genericizes before anything enters the vault.
- **Lessons are append-only**; the vault assigns the canonical `L0NN` (project logs use their own
  `E0NN` ids; integration maps `E→L`).
- **Every change to the suite** bumps per-file `VERSION` + the `Set Version`.
- **Sync never clobbers** a `PROJECT-OWNED` block.
- **Read before write**: the engine re-reads a target's on-disk files before acting (never a cached
  version) — per `CLAUDE.md` § 2.

## 10. Implementation roadmap (slices → plans)

Each slice is a vital change → its own `PLAN-NNN` (§ 15 workflow). Suggested order (mechanical/low-risk
first; judgment-heavy last):

1. ✅ **Slice 1 — Setup-and-strip + log + markers** (done — PLAN-002, Set Version v1.1). Added the strip
   step to `SETUP.md`; defined the kept/stripped manifest; added the `STANDARDS_LOG.md` template; added
   `PROJECT-OWNED` markers to the CLAUDE.md + session templates **and** this repo's adopter instances;
   moved `SET_VERSION_ADOPTED` to `docs/`. *(Docs/prompt only — no engine yet.)*
2. **Slice 2 — Registry + `status`/`drift`.** Vault config + first Python: read-only report of each
   project's Set Version vs vault and its open log count. *(First engine code.)*
3. **Slice 3 — `harvest`.** Parse every `STANDARDS_LOG.md`; consolidate `open` entries; dedup hints.
4. **Slice 4 — `integrate` assist.** Genericize → new lesson → topical update → version/Set bumps;
   write-back mark-done. *(Operator-gated; judgment-heavy.)*
5. **Slice 5 — `sync`.** Section-aware propagation honoring `PROJECT-OWNED`; whole-file for suite-owned.

## 11. Open decisions (to resolve as each slice is planned)

- Registry format + location (`config/projects.toml` proposed).
- CLI name / entry point (`python -m standard_document_updater …`).
- Final home of `STANDARDS_LOG.md` (`docs/` proposed).
- Whether `integrate`'s genericization runs a model in-process or hands off to a Claude session
  (affects whether the tool is pure-Python or CLI + agent workflow).
