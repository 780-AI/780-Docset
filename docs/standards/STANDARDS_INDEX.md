<!-- VERSION: 2.2 -->
<!-- Last Updated: 2026-08-19 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v2.2 — 2026-08-19 — Standard Set Version v2.2 (domain-neutral scrub): 4 example paths carrying a real username (survived the v1.0 genericization; found by the v2.1 gate grep) scrubbed to `/Users/you/...` — MEMORY_PROTOCOL (3) + PROJECT_INSTRUCTIONS_TEMPLATE (1), both → 1.1. § 1 block → v2.2 (counts unchanged — 68 lessons / 15 rules); § 3 caption → v2.2 + cells (MEMORY_PROTOCOL 1.1, PROJECT_INSTRUCTIONS_TEMPLATE 1.1, STANDARDS_INDEX 2.2); § 6 history entry added. No rule or lesson content change.
v2.1 — 2026-08-18 — Standard Set Version v2.1 (first harvest → integrate cycle — adopter entry E001): SESSION_CLOSER § 1.2 Set-Version reference retargeted to docs/SET_VERSION_ADOPTED.md (adopters don't carry the INDEX) + lesson L068 (template cross-references must resolve in the adopter) + README stale LESSONS count fixed 48 → 68 (drifted since v1.4; L060-class sweep). § 1 block → v2.1 (lesson count → 68; files unchanged); § 2 row 9 → 68; § 3 caption → v2.1 + cells (SESSION_CLOSER 1.6, README 1.2, STANDARDS_INDEX 2.1; LESSONS cell unchanged per the no-per-lesson-bump practice) + lesson total → 68; § 6 history entry added. No rule change.
v2.0 — 2026-08-17 — Standard Set Version v2.0 (PLAN-009 skill delivery): SETUP.md + NEW_PROJECT_BOOTSTRAP.md + MEMORY_DURABILITY_ROLLOUT_PROMPT.md retired in favor of the vault-side live-reference delivery skill (skill/SKILL.md + skill/modes/ + scripts/bootstrap_skill.sh — vault machinery, never copied to adopters). § 1 block → v2.0 (counts unchanged — 15 rules / 67 lessons; total → 15 files = 11 binding + 4 meta); § 2 Tier 2 table pruned to README / STANDARDS_INDEX / HOW_TO_USE (+ STANDARDS_LOG) + delivery note added; § 3 caption → v2.0 + cells (README 1.1, HOW_TO_USE 1.1, STANDARDS_LOG 1.1, SESSION_OPENER 1.7, SESSION_CLOSER 1.5, STANDARDS_INDEX 2.0); § 4 delivery path rewritten (skill, concierge/self-service); § 5 unchanged (live-reference — no release-procedure step added); § 6 v2.0 history entry with the adopter-migration note.
v1.6 — 2026-08-16 — Standard Set Version v1.6 (PLAN-008 sync-enablement): TEMPLATE-ONLY marker convention + PROJECT-OWNED instance-heading blocks in the two session templates + § 14 stub-keep wording; the `sync` engine ships (Slice 5). § 1 block → v1.6 (counts unchanged — 15 rules / 67 lessons); § 3 caption → v1.6 + cells (CLAUDE.md 1.5, SESSION_OPENER 1.6, SESSION_CLOSER 1.4, SETUP 1.6, NEW_PROJECT_BOOTSTRAP 1.6, STANDARDS_INDEX 1.6); § 6 history entry added. No rule or lesson content change.
v1.5 — 2026-08-16 — Standard Set Version v1.5 (PLAN-010 upstream intake): eleven lessons L057–L067 + NEW Rule 15 (post-implementation verification of the NEW behavior) + Rule 14 upgraded to project-data locality (claude_project_data.sh replaces bootstrap_memory.sh; verified at session open AND close). § 1 counts → 67 lessons / 15 rules; § 2 rows 1 + 9; § 3 caption → v1.5 + cells (CLAUDE.md 1.4, SESSION_OPENER 1.5, SESSION_CLOSER 1.3, STANDARDS_INDEX 1.5, NEW_PROJECT_BOOTSTRAP 1.5, SETUP 1.5, MEMORY_DURABILITY_ROLLOUT_PROMPT 1.2) + total → 67 (LESSONS cell unchanged per the no-per-lesson-bump practice); § 4.1 count swept 13 → 15 (per L060); § 6 history entry added.
v1.4 — 2026-08-16 — Standard Set Version v1.4: five process-hardening lessons L052–L056 + L051 recurrence #4 (final-indentation clause). § 1 counts → 56 lessons; § 2 row 9 → 56; § 3 caption → v1.4 + cells (CLAUDE.md 1.3, SESSION_OPENER 1.4, SESSION_CLOSER 1.2, STANDARDS_INDEX 1.4, NEW_PROJECT_BOOTSTRAP 1.4, SETUP 1.4; MEMORY_DURABILITY_ROLLOUT_PROMPT cell caught up to its already-shipped 1.1) + total → 56 (LESSONS cell unchanged per the no-per-lesson-bump practice); § 6 history entry added. Anchors: SESSION_OPENER § 1.1 + § 3.1 row (L055 / L051), SESSION_CLOSER § 1.4 + § 2.1 row (L055), CLAUDE.md § 15.2 (L054) + § 15.3 (L056). No rule added or removed.
v1.3 — 2026-06-20 — Standard Set Version v1.3: lesson L051 (the Rule 13 senior-review pass must mechanically run the linter / type-checker / tests against the plan's embedded code, not eyeball it) + a SESSION_OPENER § 3.1 universal row. § 1 lesson count → 51; § 2 row 9 → 51; § 3 caption → v1.3, SESSION_OPENER cell → 1.3, STANDARDS_INDEX cell → 1.3, total → 51 (LESSONS cell unchanged per the no-per-lesson-bump practice); § 6 history entry added. No existing rule changed (Rule 13 expectations sharpened, not rewritten).
v1.2 — 2026-06-17 — Standard Set Version v1.2 (PLAN-005): added Rule 14 (durable memory) to CLAUDE.md; SESSION_OPENER § 1.5 + § 3.1 row; lesson L050; new meta file MEMORY_DURABILITY_ROLLOUT_PROMPT.md. § 1 counts → 50 lessons / 14 rules; § 3 → 18 files (11 binding + 7 meta); CLAUDE.md + SESSION_OPENER cells → 1.2; § 6 history entry added.
v1.1 — 2026-06-13 — Standard Set Version v1.1 (PLAN-002, Slice 1): registered the STANDARDS_LOG.md
experiences-log template (meta "+"); recorded the PROJECT-OWNED marker convention + setup-and-strip;
bumped § 3 per-file versions for the edited files; refreshed counts (17 files) and added the § 6 history entry.
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; prior version history reset. Established as Standard Set Version v1.0.
-->

# STANDARDS_INDEX.md — Versioned Set Manifest

**Purpose:** The canonical record of the Standard Set Version and the per-file versions inside it.
Adopters name the version they adopted, backport changes deliberately, and see the suite at a glance.

**Why this file exists:** Per-file `VERSION` headers track each file's evolution. The **Standard Set
Version** tracks the suite as a whole — files added, structure changed, patterns codified across files.

---

## Table of Contents

1. [Standard Set Version (current)](#1-standard-set-version-current)
2. [What's in this set](#2-whats-in-this-set)
3. [Per-file version table](#3-per-file-version-table)
4. [How to apply this set to a new project](#4-how-to-apply-this-set-to-a-new-project)
5. [How to bump the Set Version](#5-how-to-bump-the-set-version)
6. [Standard Set Version history](#6-standard-set-version-history)

---

## 1. Standard Set Version (current)

```
Standard Set Version: v2.2
Released:             2026-08-19
Baseline:             v2.1 (E001 adopter-reference fix + L068, atop v2.0 skill delivery + the v1.x line) + domain-neutral scrub: residual real-username example paths genericized (identifier-token class; MEMORY_PROTOCOL + PROJECT_INSTRUCTIONS_TEMPLATE).
Adopter contract:     11 binding files + 3 meta files (+ STANDARDS_LOG.md); 68 lessons (L001–L068); 15 standing rules in CLAUDE.md
```

When adopting this suite, record the Set Version in the new project's `CHANGELOG.md` or its own
`docs/SET_VERSION_ADOPTED.md` so future updates can be back-ported deliberately.

---

## 2. What's in this set

### Tier 1 — Binding files (the 11-file modular suite)

Adopters copy these into their project. Each is loaded by the dispatcher (`CLAUDE.md` § 12) when its
topic is in scope, except `SESSION_OPENER.md` (loaded every session per Rule 9) and `SESSION_CLOSER.md`
(invoked on the wrap-up command per Rule 12).

| # | File | Role |
|---|---|---|
| 1 | `CLAUDE.md` | Binding contract — 15 standing rules, classification, workflow, validation checklist, dispatcher, plan workflow (§ 15), optional Codex handoff (§ 14) |
| 2 | `PROJECT_STANDARDS.md` | Governance — manifest mechanics, CHANGELOG conventions, tracker structure, commit discipline, sync triggers |
| 3 | `PROMPT_STANDARDS.md` | Prompt-craft — multi-file edit prompts, ALLOWLIST + verbatim FIND/REPLACE, retry-with-deviation-warning, Codex handoff variant |
| 4 | `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Claude.ai Project Instructions — three-tier template (static frame, project-specific, per-session) |
| 5 | `MEMORY_PROTOCOL.md` | Memory hygiene — four categories, what to store / not store, verify-before-recommending |
| 6 | `ENGINEERING_STANDARDS.md` | Engineering substrate — architecture invariants, coding standards, secrets, container discipline, ops |
| 7 | `VALIDATION_STANDARDS.md` | Test framework — tiered model, ownership map, deliberate-failure protocol, soak, first-fire expectations |
| 8 | `CICD_STANDARDS.md` | Pipeline architecture — staged shape, registry-pull deploy, smoke gating, auto-rollback, soak gate, explicit PROD authorization |
| 9 | `LESSONS.md` | Incident-to-rule archive — 68 lessons (append-only), each with incident + cost + codification + cross-references |
| 10 | `SESSION_OPENER.md` | Session-start pre-flight (binding per Rule 9) — environment mapping + failure-mode catalog + first-response output template |
| 11 | `SESSION_CLOSER.md` | Session-end wrap-up (binding per Rule 12) — wrap-up routine + failure-mode catalog + output template |

### Tier 2 — Meta files (about the suite)

| # | File | Role |
|---|---|---|
| 1 | `README.md` | Entry point — overview, mental model, dispatcher reference, orientation |
| 2 | `STANDARDS_INDEX.md` | This file — versioned set manifest, per-file table, bump policy |
| 3 | `HOW_TO_USE.md` | Practical usage guide — supporting prompts (Day-One, code review, audit); delivery is the vault-side skill |
| + | `STANDARDS_LOG.md` | **Experiences-log template** — the per-project contribution channel; the delivery skill copies it to the project's `docs/STANDARDS_LOG.md` (an adopter artifact, not a binding rule) |

> **Delivery (not part of the set):** the suite is delivered by the vault-side skill
> (`skill/SKILL.md` + `skill/modes/` + `scripts/bootstrap_skill.sh`) — live-reference vault
> machinery, versioned in the vault's own manifest, never copied to adopters.

---

## 3. Per-file version table

Current state as of Set Version v2.2 (2026-08-19). Files unchanged since v1.0 keep their 2026-06-07 dates.

| File | Tier | Version | Last Updated |
|---|---|---|---|
| `CLAUDE.md` | Binding | 1.5 | 2026-08-16 |
| `PROJECT_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `PROMPT_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Binding | 1.1 | 2026-08-19 |
| `MEMORY_PROTOCOL.md` | Binding | 1.1 | 2026-08-19 |
| `ENGINEERING_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `VALIDATION_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `CICD_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `LESSONS.md` | Binding | 1.0 | 2026-06-07 |
| `SESSION_OPENER.md` | Binding | 1.7 | 2026-08-17 |
| `SESSION_CLOSER.md` | Binding | 1.6 | 2026-08-18 |
| `README.md` | Meta | 1.2 | 2026-08-18 |
| `STANDARDS_INDEX.md` | Meta | 2.2 | 2026-08-19 |
| `HOW_TO_USE.md` | Meta | 1.1 | 2026-08-17 |
| `STANDARDS_LOG.md` | Meta | 1.1 | 2026-08-17 |

**Total file count:** 15 (11 binding + 4 meta).
**Total lesson count in `LESSONS.md`:** 68 (L001–L068).

---

## 4. How to apply this set to a new project

The delivery path is the **standard-docset skill** (vault-side): concierge — the curator runs
it against the target; or self-service — clone the vault repo and run
`bash scripts/bootstrap_skill.sh` once, then invoke the skill in a session opened at the
target. Bootstrap mode covers new projects; adopt mode migrates existing ones (dry-run gated).

### 4.1 What you get

- Repo-root `CLAUDE.md` carrying the 15 standing rules + project-specific critical-files list
- `docs/standards/` containing the focused standards files
- `archive/LESSONS.md` carrying the incident-to-rule archive
- Project-local `docs/SESSION_OPENER.md` + `docs/SESSION_CLOSER.md`
- Optional Codex handoff protocol (`CLAUDE.md` § 14) if the project uses a second AI agent
- Governance scripts, CI scaffold, MR template, manifest, folder structure

### 4.2 Set-Version drift management

Once adopted, the local copy lives independently. Backports from the source set are **explicit**:

1. Read the new Set Version's history entry (§ 6).
2. Decide which changes are relevant.
3. Cherry-pick the per-file edits into the local copy; bump the affected per-file versions.
4. Record the new adopted version in `docs/SET_VERSION_ADOPTED.md`.

Major Set-Version bumps include explicit migration notes — read them before backporting.

---

## 5. How to bump the Set Version

The Set Version is the coarse-grained maturity of the suite, distinct from per-file versions.

- **Minor (v1.X → v1.X+1):** additive — new lessons, new sub-sections, new optional features,
  refinements. Adopters may backport or stay. No migration required.
- **Major (v1.X → v2.0):** structural — a new binding file, a file split/merge, a dispatcher
  reorganization, a critical-file rename, a removed rule. Adopters migrate; notes go in § 6.

### Bump procedure

1. Decide Minor or Major.
2. Add an entry at the top of § 6 with the date and a summary.
3. Bump this file's `VERSION` header.
4. Update the § 3 per-file table for any per-file bumps that landed alongside.
5. Commit the bump with the changes that warranted it.

Per-file bumps and Set-Version bumps are independent: a single-file typo fix is per-file only; a
coordinated multi-file pattern is a Set-Version Minor; a structural change is a Set-Version Major.

---

## 6. Standard Set Version history

Newest first. Append-only.

### v2.2 — 2026-08-19 — Domain-neutral scrub (identifier-token class)

Additive Minor. Four example paths in the suite still carried a real username
that survived the v1.0 genericization — the identifier-token scrub gap
(usernames, SSH users, image names) the scrub-sweep discipline warns about. Found by the v2.1
release-gate grep; scrubbed to `/Users/you/...` (the registry-example convention):
MEMORY_PROTOCOL.md (3 sites) + PROJECT_INSTRUCTIONS_TEMPLATE.md (1 site), both → 1.1. Counts
unchanged (68 lessons / 15 rules); no rule or lesson content change. Sync note: MEMORY_PROTOCOL
is replace-class in the SYNC_MAP — adopters receive the fix at their next `sync`;
PROJECT_INSTRUCTIONS_TEMPLATE is vault-side only (not in the SYNC_MAP).

### v2.1 — 2026-08-18 — Adopter-reference fix (first harvest → integrate cycle)

Additive Minor — the first Set bump produced by the experiences-log loop end-to-end. The adopt-mode
pilot logged E001 (its instantiated SESSION_CLOSER § 1.2 pointed at the vault-side
`STANDARDS_INDEX.md`, which adopters don't carry), `harvest` surfaced it, `integrate` mapped it to
lesson **L068** (template cross-references must resolve in the adopter — SYNC_MAP items +
skill-created files only), and the template fix retargets § 1.2 to `docs/SET_VERSION_ADOPTED.md`
(present on both sides — the vault self-adopts). SESSION_CLOSER → 1.6; README → 1.2 (stale LESSONS
count swept 48 → 68, drifted since v1.4); lesson count → 68; no rule
change. The engine's Status write-back closes the adopter's entry
(`integrated → vault L068`). E001's suggested mechanized delivery-QA grep (template refs vs
SYNC_MAP + skill-created files) is deferred — recorded as an open candidate, not shipped here.

### v2.0 — 2026-08-17 — Skill delivery (machinery retired)

Structural Major (PLAN-009). The delivery machinery — `SETUP.md` (the one-shot bootstrap prompt),
`NEW_PROJECT_BOOTSTRAP.md` (the Day-Zero walkthrough), and `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`
(the Rule 14 retrofit prompt) — is retired from the set. Delivery is now the vault-side
**standard-docset skill** (`skill/SKILL.md` + `skill/modes/bootstrap.md` + `skill/modes/adopt.md`
+ the per-machine installer `scripts/bootstrap_skill.sh`): **live-reference** — the skill carries
no copy of the suite; it resolves the vault through its own symlink, self-pulls at step 0, and
reads `docs/standards/` directly at delivery time, so there is no bundle, no export script, and no
re-export release step (the L053 delivery-parity class is removed structurally, not managed).
Distribution is a plugin-free dual route: **concierge** (the curator runs the skill against the
target — team machines need nothing installed) and **self-service** (clone the vault repo, run the
installer once). Bootstrap mode covers new projects; adopt mode migrates existing ones (dry-run
gated, customization-preserving, performs the one-time v1.6 heading-wrap) and ships gated on a
real pilot adoption. No release-procedure step is added to § 5 — live-reference means the skill
needs no per-release refresh.

**No adopter action required** — the retired files were setup machinery that never survived in
adopters (the strip removed them), so no adopter footprint changes and `sync` is unaffected. New
deliveries use the skill; old-SETUP adopters just register + heading-wrap + sync.

### v1.6 — 2026-08-16 — Sync-enablement markers (PLAN-008: the `sync` engine ships)

Additive Minor. Marker/wording enablement only — no rule or lesson content change (counts stay
15 rules / 67 lessons). The two session templates gain a `TEMPLATE-ONLY` banner block (deleted at
instantiation; never propagated by sync) and a `PROJECT-OWNED` instance-heading block (so
section-merge sync preserves each adopter's own heading); the template `CLAUDE.md` § 14 marker
comment switches to stub-keep wording (single-agent adopters replace the § 14 body with a
"NOT IN USE" stub INSIDE the block — deleting the block would break sync's ordinal block matching);
`SETUP.md` + `NEW_PROJECT_BOOTSTRAP.md` instantiation wording updated to match (delete the
TEMPLATE-ONLY block, fill the heading block, keep every marker; § 3.1 stays suite-owned VERBATIM —
customizations go to § 3.2). The engine's `sync` command ships alongside (dry-run by default;
suite-owned files replaced whole, mixed files section-merged with PROJECT-OWNED blocks preserved,
`SET_VERSION_ADOPTED.md` mechanically updated). Adopters may stay on v1.5 — pre-v1.6 instances lack
the heading wrap and will count-mismatch on their FIRST sync, by design (loud, per-file, nothing
written): wrap once by hand or via adopt-mode, then sync forever.

### v1.5 — 2026-08-16 — Upstream-intake batch (L057–L067 + Rule 15 + Rule 14 project-data locality)

Additive Minor. First upstream intake: an adopter lineage that evolved independently on its own Set
line (2026-06 → 2026-08) folded back into the vault. Eleven genericized lessons: **L057** — identical
code + different behavior ⇒ runtime cause, instrument first; **L058** — audit every caller before
fixing a shared utility at one site; **L059** — verify evidence provenance before recording a result;
**L060** — grep every name-form of a removed identifier across code AND docs; **L061** — a reused
helper imports its implicit gates, enumerate them per new context; **L062** — plan-embedded code must
satisfy the plan's own acceptance criteria across all sites, sanitize before pasting; **L063** —
version stamps drift from their own change logs, grep the actual stamp; **L064** — validate on a
version-matched runtime with real dependencies, fakes return real driver types; **L065** — reconstruct
system state from its own event stream; **L066** — a liveness signal comes from the monitored layer's
own traffic on the monitor's own clock; **L067** — ship-gating verification must exercise the NEW
behavior itself. One NEW binding rule: **Rule 15** — post-implementation verification of the NEW
behavior is mandatory (pairs with L067). One strengthened rule: **Rule 14** upgraded in place from
memory-only durability to full **project-data locality** — physical home `.claude/project-data/`
(memory + session transcripts), managed by `scripts/claude_project_data.sh`
(`status`/`adopt`/`link`; replaces `bootstrap_memory.sh`), verified at session open
(`SESSION_OPENER` § 1.5) AND close (`SESSION_CLOSER` § 1.6); L050 carries a generalization note.
Session files gain three § 3.1 catalog rows (project-data locality / Rule 15 feature-ON / L063
stamp-vs-log). The intake mapping (upstream ↔ vault numbering) is recorded permanently in the vault's
PLAN-010 § 3 and its CHANGELOG. Adopters may stay on v1.4; to migrate, run the updated
`MEMORY_DURABILITY_ROLLOUT_PROMPT.md` (its `adopt` verb absorbs the old memory-symlink layout).

### v1.4 — 2026-08-16 — Process-hardening batch (L052–L056 + L051 recurrence #4)

Additive Minor. Five lessons from live adoption + plan-workflow experience: **L052** — an installer must
create every file it references, not just account for it; **L053** — the bootstrap delivery docs are a
parity set updated in the same pass (catch-up to an already-released Set Version is installer-only, never
a Set-Version bump; inventory changes update the lay-down + strip set-cover same-commit); **L054** — the
Phase-3 ALLOWLIST enumerates the plan file + sibling tracker as same-commit promotion rows so the count
matches `git status`; **L055** — recorded push-state is reconciled against the *real* remote
(`git ls-remote`) at session open and flipped in the same wrap-up as the push; **L056** — the Phase-3
implementer's first act is a reconcile pass of the plan against the live source (the backstop to Rule 13).
Plus **L051 recurrence #4**: the Rule 13 tools must run against the embedded code at the exact final
indentation it ships at. Anchors: `SESSION_OPENER.md` § 1.1 + § 3.1 row; `SESSION_CLOSER.md` § 1.4 +
§ 2.1 row; `CLAUDE.md` § 15.2 + § 15.3. No binding file added or removed and no existing rule changed —
adopters may backport or stay on v1.3.

### v1.3 — 2026-06-20 — Rule 13 senior-review pass must mechanically run the tools (L051)

Additive Minor. Adds lesson **L051** — the Rule 13 senior-review-and-optimize pass MUST mechanically run
the linter + type-checker + tests against the EXACT code a plan commits in its § 5 transformation rules
(not eyeball it), the fix MUST land in § 5 itself (not only be narrated in the CHANGE LOG), and the
recorded result MUST name the specific lines / checks it fixed — codifying a defect class that recurred
across three consecutive plans. Adds a matching `SESSION_OPENER.md` § 3.1 universal catalog row. No binding
file added or removed and **no existing rule changed** — Rule 13's expectations are sharpened, not
rewritten; adopters may backport or stay on v1.2.

### v1.2 — 2026-06-17 — Durable project memory (Rule 14)

Additive Minor (PLAN-005). Adds binding **Rule 14** (the Claude memory store lives inside the repo at
`./.claude/memory/` with the harness dir symlinked to it, so memory survives a machine change and a folder
move; repaired idempotently by `scripts/bootstrap_memory.sh`); a self-healing `SESSION_OPENER.md` § 1.5
pre-flight (verify + auto-repair + halt-on-empty) + a § 3.1 catalog row; lesson **L050**; and the
`MEMORY_DURABILITY_ROLLOUT_PROMPT.md` meta file for adopters. No binding file removed and no existing rule
changed — adopters may backport or stay on v1.1.

### v1.1 — 2026-06-13 — Experiences log + PROJECT-OWNED markers + setup-and-strip

Additive Minor (PLAN-002, Slice 1). Adds the `STANDARDS_LOG.md` experiences-log template (the per-project
contribution channel fed by `SESSION_CLOSER.md` § 1.7); wraps the project-customizable blocks in
`CLAUDE.md` + the session files (template and adopter) in `PROJECT-OWNED` markers so a future `sync`
preserves them; reworks `SETUP.md` into setup-and-strip (install the operative standard, create the log,
write `SET_VERSION_ADOPTED.md` to `docs/`, then strip the setup machinery as a second commit). No binding
file added or removed and no rule changed — adopters may backport or stay on v1.0.

### v1.0 — 2026-06-07 — Clean domain-neutral baseline

Initial domain-neutral release. The suite carries the 13 standing rules (`CLAUDE.md` § 3), 49 lessons
(L001–L049), and the session start/end forcing functions (Rules 9 & 12). All project identity and
source-domain specifics from the originating projects were removed; examples are role-based and
generic. This is the canonical baseline that `SETUP.md` distributes to new projects.

---

## End of index

When a new Set Version is released, add an entry to § 6 and bump this file's `VERSION` header. Per-file
CHANGE LOG entries capture finer-grained evolution; both layers stay in sync.
