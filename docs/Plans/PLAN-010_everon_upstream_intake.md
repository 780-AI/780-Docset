<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Status: CLOSED -->
<!--
CHANGE LOG
v1.0 — 2026-08-16 — Phase 3 implemented (fresh session, single commit): 21-file § 7 ALLOWLIST landed;
reconcile-first pass (§ 15.3 / L056) found no plan defects; § 5 blocks sanitized per L062 (straight
quotes; lesson prose mapped onto the live #### Incident/Diagnosis/Codification/Cross-references
format; archive L050 tail anchored on its project-instance wording). One-time `adopt` migration run as
the final implementation step (memory + transcripts → .claude/project-data/). QA A–H + J passed; QA-I
verifies at the next session open. § 11 R1 CLOSED. Plan CLOSED; Standard Set Version v1.5 released.
v0.1b — 2026-08-16 — Phase 2: **APPROVE D10.A** (operator, 2026-08-16). Status → APPROVED; Phase 3 to run in a fresh session per § 15.3. Capital-Signal pilot decision recorded operator-side (PLAN-009 Phase-4 verification target — see OPEN_TASKS).
v0.1a — 2026-08-16 — Rule 13 senior-review pass (last task of Phase 1; per L051 + recurrence #4 the
tools were ACTUALLY RUN). Mechanical results: (1) § 5E script extracted from this file verbatim →
`bash -n` clean; live fixture runs in scratchpad — fixture A (un-adopted harness dir → `adopt` →
STATUS OK, data moved), fixture B (folder move → NOT LINKED → `link` → OK), fixture C (pre-v1.5
memory-symlink layout → `adopt` absorbs both halves: "absorbed old in-repo memory store" + transcript
moved + old dir gone + idempotent re-adopt) — ALL PASS. (2) QA-D domain grep run against the § 5A–5G
texts as committed: found 2 false-positive hits on bare `sweep` in L060's own grep-sweep prose →
QA-D pattern refined (bare `sweep` excluded, noted in § 8; domain sense already genericized to
"decision event"); re-run = 0 hits. (3) Counts pre-computed and cross-checked: 56+11=67 lessons,
14+1=15 rules, consistent across § 1/§ 3/§ 5H/§ 12. (4) § 5F/§ 5G anchors reconciled against live
files: template rows 14/15 + project row 13 + both CLOSER § 1.6 headings + SETUP Step 6.5 + NPB
Step 8 all verified as claimed. (5) Deletion blast-radius grep (L060 applied to this plan): every
live `bootstrap_memory` reference is covered by the § 7 ALLOWLIST; § 5H-3/5H-4 strengthened to
"sweep EVERY reference" (3 sites in SETUP, 5 in NPB); historical/immutable mentions enumerated and
deliberately untouched; untracked `.claude/README_memory.md` added to the 3.22 operational step.
No new design decision beyond D1/D2. Plan finalized → ready for Phase 2.
v0.1 — 2026-08-16 — Initial DRAFT. Phase 0 (audit of EverOn.Equinex's post-split standards delta,
read-only) + Phase 1 (design). Operator decisions settled at design time: D1 = A1 (upgrade vault
Rule 14 in place to project-data locality AND port the claude_project_data.sh mechanism, wired into
the session open/close routines); D2 = Equinex only (Capital-Signal intake deferred to PLAN-011).
Sibling tracker: PLAN-010_tracker.md.
-->

# PLAN-010 — Upstream intake: EverOn v2.x standards delta → vault (Set v1.5)

> **Type:** Major / vital — edits `docs/standards/` (Critical File), both CLAUDE.md copies (Critical),
> and the session routines; adds one governance script; removes one. Runs under the § 15 plan workflow.
> **Sibling tracker:** [`PLAN-010_tracker.md`](PLAN-010_tracker.md) (big plan: multi-scenario § 8
> verify + spans sessions — Phase 3 is a fresh session).
> **Read-only toward EverOn.Equinex** — its repo is never written; only this vault updates.

---

## 1. Goal

Fold EverOn.Equinex's post-split standards evolution (its own line v2.7: 2 new rules + 12 new lessons,
commits `c0940f6..b9c8fe6`, 2026-06-08 → 2026-08-16) into the vault as **Standard Set Version v1.5**:
11 new genericized lessons (vault L057–L067), one new binding rule (vault Rule 15 —
post-implementation verification), one strengthened rule (vault Rule 14 upgraded from memory-only
durability to full **project-data locality**, mechanism included), and the session-routine anchors that
make both enforceable. After this plan, the vault contract is **15 rules / 67 lessons** and nothing
portable in the upstream line is lost.

## 2. Operator constraints (settled at design)

- **D1 = A1 (2026-08-16):** upgrade Rule 14 in place (not a new Rule 16); port
  `claude_project_data.sh` as the suite's mechanism (status/adopt/link); wire it into
  SESSION_OPENER § 1.5 (every open) **and** SESSION_CLOSER (close-side confirm) — "make sure
  everything is consistent" (operator).
- **D2:** PLAN-010 scope = **Equinex only**; EverOn.Capital-Signal intake deferred to PLAN-011.
- Domain-neutral gate binding: zero-hit grep for project/domain terms on every § 5 text
  (per the domain-neutral definition memory + new L060's every-name-form discipline).
- EverOn numbering ≠ vault numbering: the § 3 mapping table is the single source of truth for the
  correspondence; it is repeated in the CHANGELOG entry.
- No EverOn-repo write. No engine (`src/`) change. No `config/projects.toml` change.

## 3. Scope summary — the mapping table (dispositive)

| EverOn | Vault | Title (genericized) | Disposition |
|---|---|---|---|
| L050 | **L057** | Identical code + different behavior ⇒ runtime cause; instrument and gather runtime data first | new lesson |
| L051 | **L058** | Audit every caller before fixing a shared utility at one site | new lesson |
| L052 | **L059** | Verify evidence provenance before recording a result | new lesson |
| L053 | **L060** | Grep every name-form of a removed identifier across code AND docs | new lesson (absorbs the queued "domain-neutral scrub sweep" candidate) |
| L054 | **L061** | A reused helper imports its implicit gates; enumerate them per new context | new lesson |
| L055 | **L062** | Plan-embedded code must satisfy the plan's own acceptance criteria across all sites; sanitize before pasting | new lesson (composes with L049/L051/L056) |
| L056 | **L063** | Version stamps drift from their own change logs; grep the actual stamp at edit and review time | new lesson (vault has 4 native occurrences incl. the § 3-heading find of this audit) |
| L057 | **L064** | Validate on a version-matched runtime with real dependencies; fakes must return real driver types | new lesson |
| L058 | **L065** | Reconstruct system state from its own event stream to check invariants the log doesn't print | new lesson |
| L059 | **L066** | A liveness signal must come from the monitored layer's own traffic, on the monitor's own clock | new lesson |
| L060 | **L067** | Ship-gating verification must exercise the NEW behavior itself | new lesson; pairs with new Rule 15 |
| L061 | — | Project data lives in the project folder | merged into the **Rule 14 upgrade** + an L050 generalization note (D1) |
| R14 (theirs) | **Rule 15** | Post-implementation verification investigation is MANDATORY | new binding rule |
| R15 (theirs) | **Rule 14** (upgraded) | Project data lives in the project folder | in-place strengthening + mechanism port |

Out of scope: their `d838097` PROJECT_STANDARDS row (project-local EA-CSV trigger); their project-specific
§ 3.2 rows; Capital-Signal (PLAN-011); any topical-file (ENGINEERING/VALIDATION) rewrites — the lessons
carry the content; topical folds can ride a later Set bump if wanted.

## 4. Phase tracker (high-level — granular sub-tasks in the sibling tracker)

- Phase 0 — Audit ✅ 2026-08-16 (all 12 lessons + both rule texts read in full; ripple commits
  `f066fde`/`ad0230a`/`b9c8fe6` inspected; their script read in full; vault anchors verified —
  incl. the native § 3-heading "13 standing rules" drift find in BOTH CLAUDE.md copies)
- Phase 1 — Design ✅ 2026-08-16 (this file; Rule 13 pass run + recorded v0.1a)
- Phase 2 — Operator approval ✅ 2026-08-16 — **APPROVE D10.A**
- Phase 3 — Implement ✅ 2026-08-16 (fresh session; single commit per § 7 ALLOWLIST — 21 files + the
  one-time `adopt` migration run as the final implementation step; reconcile-first pass found no plan
  defects)
- Phase 4 — Validate ✅ 2026-08-16 (§ 8 QA A–H + J passed in the Phase-3 session; QA-I ⏸ at the next
  session open)
- Phase 5 — Operator gate ⏸ (push + tag `set-v1.5`)

## 5. Transformation rules (verbatim)

> Formatting note: every new lesson lands **identically in BOTH** `docs/standards/LESSONS.md` (template)
> and `archive/LESSONS.md` (adopter copy) — same text, per the baseline convention: header fields
> `**Date:** 2026-06-07` / `**Project:** a reference project` /
> `**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)`.
> ToC: eleven new anchor lines above the L056 line, newest (L067) first, slug rules as at v1.4.
> Entries insert above `### L056`, order L067 → L057 top-down. LESSONS headers stay 1.0
> (no-per-lesson-bump practice).

### 5A — The eleven new lessons (both LESSONS files)

#### L067 — Ship-gating verification must exercise the NEW behavior itself

Incident: a feature shipped after its ship-gating QA passed — compile clean + defaults-byte-identical
(the rollback guarantee). The scenarios that exercised the feature ON were classed opportunistic and
never ran. Fifteen days later the operator switched the feature on and found it structurally broken in
both of its modes; a single feature-ON run with log analysis at ship time — under an hour of work —
would have caught it same-day.
Diagnosis: rollback-guarantee QA proves only that the OFF path is safe; it says nothing about the
feature. When feature-ON scenarios are deferrable, verification silently degrades to "whenever someone
happens to try it" — an unbounded defect window.
Codification: ship-gating verification must exercise the NEW behavior itself in its real runtime and
analyze the produced evidence against the design intent (per L065); feature-ON QA is ship-gating by
default and deferring it requires an explicit operator waiver recorded in the tracker. Enforced as
binding Rule 15.
Cross-references: `CLAUDE.md` § 3 Rule 15; L065 (the verification method); L059 (evidence provenance);
L047/Rule 11 (scenarios defined at change time — Rule 15 verifies at implementation time).

#### L066 — A liveness signal must come from the monitored layer's own traffic, on the monitor's own clock

Incident: two independent leaks of one invariant in a monitoring system's "is it alive?" signal:
(1) the liveness timestamp was stamped from a payload field produced by a foreign clock, so a source
with a shifted clock looked fresh for hours after going silent; (2) a *different* layer's traffic
refreshed the timestamp (the host process was alive, so the monitored component could never go stale
even when absent). Both were invisible in normal operation and surfaced only under a shifted clock and
a deliberate detach test.
Diagnosis: a heartbeat means "the monitored thing itself was heard, on OUR clock." Foreign timestamps
are data, not clocks; a parent layer's liveness is not the child's.
Codification: (a) never stamp liveness from a timestamp whose clock you don't own; (b) each monitored
layer keeps its own liveness field, refreshed only by that layer's own traffic; (c) enforce with tests
that make the wrong call impossible (the wrong-path test raises).
Cross-references: L040-class fail-safe treatment of external data (external input is untrusted);
L067 (deliberate-detach tests are feature-ON verification).

#### L065 — Reconstruct system state from its own event stream to check invariants the log doesn't print

Incident: repeatedly, a QA pass criterion referenced internal state the system's log does not print
directly. The proven technique: parse the ordered event stream, maintain the state it implies (a book,
a queue, a counter), snapshot at each decision event, and check the invariant against the system's own
printed numbers — evidence-grade verdicts with exact figures, used across four separate verifications
without adding any throwaway instrumentation to the production code.
Diagnosis: the alternatives are both bad — weaken the criterion to "looks right," or ship QA-only log
lines into a critical file.
Codification: when a pass criterion cites state not printed in the log, reconstruct it from the event
stream rather than weakening the criterion or instrumenting production code: parse events in order,
maintain the implied state, snapshot at decision points, compare against the system's own output.
Verify evidence provenance first (L059).
Cross-references: L059 (provenance before trusting the file); L067/Rule 15 (this is the standard
verification method for feature-ON evidence).

#### L064 — Validate on a version-matched runtime with real dependencies; fakes must return real driver types

Incident: a subsystem targeting one interpreter version was checked with syntax-level tools that pass
on any version; standing up a real environment on the TARGET version with the real dependency set and
running the actual test suite plus a live entry-point exercise caught three real bugs the syntax checks
had waved through. A related incident one level deeper: a serve path broke in production because the
test fake returned a convenience type where the real driver returns a typed value — the suite passed,
the deployment black-paged.
Diagnosis: syntax checks and lint are pre-checks, not validation; a test suite is only as real as its
environment and its fakes.
Codification: before shipping subsystem code, create or reuse an environment on the target runtime
version, install the real dependency set, run the full suite there, and exercise the real entry points.
Test fakes on serve paths must return the real driver types, not convenience shapes.
Cross-references: staging-parity lessons (same principle at environment level); L057-class runtime-first
diagnosis (L057).

#### L063 — Version stamps drift from their own change logs; grep the actual stamp at edit and review time

Incident: a recurring class — an artifact carries a machine-readable version stamp AND a human change
log, and the stamp silently stops moving while the log advances. Multiple occurrences in one week in
the upstream project (a package version field, the same field again at the next bump, a manifest
header, a derived count table); the vault's own history carries four more (two stale manifest cells, a
stale self-row, and — found during this plan's audit — the contract's § 3 heading still reading "13
standing rules" two rule-additions later).
Diagnosis: each instance is silent — nothing breaks at commit time; a later reader trusts the stamp.
The class recurs because editing the change log *feels* like bumping the version.
Codification: a "version bumped" claim is verified against the actual stamp, not the log entry: at edit
time AND at the Rule 10 review, grep the stamp field itself (`<!-- VERSION:`, `version =`,
`# VERSION:`, count headings, count-table totals) and confirm it equals the new value. Derived stamps
are recomputed from source, never incremented. Plans that touch counts pre-compute the arithmetic and
the implementer grep-verifies every stamp site.
Cross-references: L044 (forcing-function cadence = failure cadence — this one fires per
stamp-touching edit); Rule 10 (the review is the second gate).

#### L062 — Plan-embedded code must satisfy the plan's own acceptance criteria across all sites; sanitize before pasting

Incident: two gates, two failure shapes. At the senior pass: a plan's transformation rules removed an
identifier while the plan's own acceptance criteria demanded `grep == 0` for it — and the rules missed
an entire class of sites (in-source help text), making the plan self-contradictory; caught by checking
the rules against the plan's own § 8/§ 12. At implement time: embedded blocks carried target-language
footguns that read fine on the page (an escape sequence invalid in the target's string literals, a
comment placement with runtime meaning, delimiter-unbalancing punctuation in a comment) — caught only
because the implementer sanitized rather than pasting verbatim.
Diagnosis: plan-embedded code is a hypothesis written against a snapshot, in an editor that doesn't
speak the target language.
Codification: harden at BOTH gates. (1) The Rule 13 pass verifies the § 5 rules achieve the plan's OWN
acceptance criteria across ALL site classes — including help text, docs, and user-visible strings, not
just code. (2) The Phase-3 implementer sanitizes every embedded block against the target language's
conventions before pasting — never paste verbatim. Extends L060 to the plan-drafting layer.
Cross-references: L049 (the senior pass); L051 (run the tools); L056 (reconcile against live source);
L060 (every name-form); Rule 7 (verbatim blocks are the input, not the excuse).

#### L061 — A reused helper imports its implicit gates; enumerate them per new context

Incident: a new feature reused an existing selection helper verbatim. The helper carried an implicit
minimum-threshold gate that was correct in its original context and wrong in the new one — below the
threshold it silently selected nothing, the new feature never acted, and a safety net fired instead.
The plan said "reuses X"; the senior pass confirmed the *logic* matched; neither enumerated the
helper's implicit preconditions against the new context. A full follow-up plan was needed to fix it.
Diagnosis: reuse imports thresholds, clamps, mode semantics, and ordering assumptions along with the
logic. "Reuses X verbatim" is not a safe shorthand; the defect class is invisible to a logic-level
read.
Codification: when a plan reuses an existing helper in a NEW feature context, the Rule 13 pass must
enumerate the helper's implicit gates — minimums, clamps, mode semantics, selection/ordering
assumptions — and check each against the new context's intent, not merely confirm the logic reads
correctly.
Cross-references: L049 (the pass where the enumeration belongs); L058 (enumerate the blast radius from
ground truth, not from a hand-listed subset).

#### L060 — Grep every name-form of a removed identifier across code AND docs

Incident: a feature removal's plan enumerated the code sites and the docs to update; both lists were
treated as complete. An exhaustive grep across every name-form found the removed feature's hyphenated
and lowercase forms, helper names, and a user-visible string scattered across four additional docs and
one live code branch the lists never mentioned — caught only by sweeping both code and docs with every
form, plus a final verification grep before staging.
Diagnosis: a plan's enumerated touch-point lists are a starting inventory, not a complete one; name-forms
multiply (snake_case, kebab-case, lowercase prose, function names, display strings, markdown anchor
slugs) and each form hides in a different file class.
Codification: before any removal or rename commit, run an exhaustive, case-insensitive grep across BOTH
code and all docs using EVERY name-form of the affected identifier — including anchor slugs and
user-visible strings — and a final verification grep immediately before staging. The same sweep
discipline applies to domain-neutralization scrubs (a zero-hit grep gate over all forms is the pass
criterion).
Cross-references: L058 (audit-all-callers — sibling enumerate-from-source discipline); L038 (the
ALLOWLIST count IS the expectation); L062 (the plan-layer extension).

#### L059 — Verify evidence provenance before recording a result

Incident: two instances of one trap. Evidence logs supplied for a QA verdict turned out to be from the
predecessor host, not the live one (sizes and line counts didn't match). Later, a single day's log
contained TWO versions of the system — the old version until mid-day, the new one after — and a naïve
whole-file tally would have credited the old version's lines to the new. The fix: locate the
initialization marker, slice the file to the confirmed portion, verify only that.
Diagnosis: a filename or date is not provenance — one file can mix versions (mid-run restart) or come
from a different host entirely. A result recorded against evidence the target never produced is a
false-confidence record that is very hard to detect later.
Codification: before recording any QA/audit result from an evidence file, verify which host and which
version actually produced the lines you are about to trust — instance identifiers, init timestamps,
size/content consistency with the expected source — then slice to the confirmed portion and verify
only that.
Cross-references: L032 (investigate the underlying data — parent discipline); L065 (the replay method
this feeds); L067/Rule 15 (verification evidence).

#### L058 — Audit every caller before fixing a shared utility at one site

Incident: a bug was reported at one call site of a shared time-reading idiom. Instead of a one-site
patch, a full audit of the idiom across the codebase found nine sites sharing the same failure mode —
license expiry, session gates, history bounds, a display — all reading a value that stalls when the
environment goes quiet. Fixing only the reported site would have left eight latent defects to surface
one at a time, each re-diagnosed from scratch. All nine were converted in one reviewed commit; QA
confirmed no regression.
Diagnosis: a shared utility's defect is a class, not an instance. The reported site is merely the one
that happened to be observed.
Codification: before fixing a bug in a shared utility or a repeated idiom, grep every caller and every
occurrence and categorize each — same defect, or load-bearing as written? Fix the whole class in one
reviewed pass rather than the reported site.
Cross-references: L039 (grep all reads before splitting global state — the vault's sibling); L060
(every name-form — the removal-side sibling).

#### L057 — Identical code + different behavior ⇒ runtime cause; instrument and gather runtime data first

Incident: a behavior regression was believed to have appeared "after" a recent change. The audit
compared the implicated code path between the two versions and found it byte-identical — static
analysis could not explain a behavior change because there was no code change. The cause was a runtime
condition (a time source that stops advancing when input stops arriving), invisible to any diff. The
fix came from adding state-transition logging and gathering live evidence across the failure boundary,
then changing the time source — confirmed from live logs.
Diagnosis: identical code with different behavior means the cause is environmental or runtime — clocks,
external state, data feeds, timing — a place a diff structurally cannot see. More static re-reading
spends time proving nothing.
Codification: when a behavior change cannot be explained by a code diff, stop static analysis: add
instrumentation, capture runtime evidence across the failure boundary, and only then change code.
Cross-references: L032 (investigate the underlying data — this is its runtime-shaped case); L064
(validate on the real runtime — the prevention-side sibling).

### 5B — L050 generalization note (both LESSONS files)

Append inside L050, immediately before its `#### Cross-references`, in both files:

> #### Generalization — all project data, not just memory (Set v1.5)
>
> An upstream project independently re-discovered this failure class at larger scope: its entire
> per-project store — memory AND all session transcripts — lived only under the harness's
> machine-local, absolute-path-keyed directory, invisible to every folder-level backup. The rule is
> therefore generalized from "the memory store" to **all machine-local project data** (Rule 14 as of
> Set v1.5): physical home `<repo>/.claude/project-data/`, symlink at the harness path, managed by
> `scripts/claude_project_data.sh` (`status`/`adopt`/`link`), verified at session open AND close.
> Anything that genuinely cannot live in the folder is cataloged in the project's machine-migration
> doc, same-commit.

### 5C — Rule 14 upgraded in place (root `CLAUDE.md` + `docs/standards/CLAUDE.md`)

Replace the entire `### Rule 14` section body (title line through its final "See …" line) with:

> ### Rule 14 — Project data lives in the project folder (durable across machines and moves)
>
> All machine-local project data MUST physically live **inside the repository**, so that syncing or
> copying the folder moves the project completely — nothing project-related may exist ONLY outside
> it. The Claude Code per-project store (persistent memory + session transcripts) is the canonical
> case: the harness keeps it at `~/.claude/projects/<path-key>/`, keyed to the folder's **absolute
> path** — a folder move or rename orphans it silently; a machine change loses it. Its physical home
> is **`<repo>/.claude/project-data/`**, with a symlink left at the harness path, managed by
> `scripts/claude_project_data.sh`:
>
> ```bash
> bash scripts/claude_project_data.sh status   # health check (symlink + store)
> bash scripts/claude_project_data.sh adopt    # one-time move-in of existing harness data
> bash scripts/claude_project_data.sh link     # new machine, or after any folder move/rename
> ```
>
> - **`.claude/` stays gitignored** — memory may carry local-only sensitive values; the data travels
>   with folder sync/copies, never the git remote.
> - **Session-open forcing function:** `SESSION_OPENER.md` § 1.5 runs `status` on every pre-flight,
>   self-heals via the verb `status` names (`link`/`adopt`), and **HALTS with a warning** if the store
>   is unexpectedly empty (the signal that data was lost).
> - **Session-close confirm:** `SESSION_CLOSER.md` § 1.6 re-confirms locality and that no new project
>   state landed outside the folder during the session.
> - **New out-of-folder state is forbidden by default.** Anything that genuinely cannot live in the
>   folder is cataloged with migration steps in the project's machine-migration doc, same-commit.
>
> **Only permitted abbreviation:** none — the probe is one command.
>
> **Drift on this rule is a Major defect** — a session that proceeds past an *unexpectedly* empty
> store without surfacing it, or that leaves new project state outside the folder uncataloged, is a
> rule violation. A genuinely new project with no data yet is not a violation.
>
> See `archive/LESSONS.md` L050 (+ its Set v1.5 generalization note) and PLAN-010 § 3 (the upstream
> L061 mapping).

Per-file variances: root copy adds "(Dropbox here)" after "folder sync/copies" and names the
machine-migration doc as `docs/NEW_MACHINE_SETUP.md`; template copy stays generic ("e.g.
`docs/MACHINE_MIGRATION.md`").

Same edit set, both CLAUDE.md copies: § 3 heading `## 3. The 13 standing rules (binding always)` →
`## 3. The 15 standing rules (binding always)`; § 13 bullet `**The 13 standing rules:**` →
`**The 15 standing rules:**` (the audit's native L063 find — two rule-additions stale).

### 5D — NEW Rule 15 (both CLAUDE.md copies, inserted after Rule 14, before `---`/§ 4)

> ### Rule 15 — Post-implementation verification of the NEW behavior is MANDATORY
>
> After every implementation of a behavior-affecting change (every § 15 plan Phase 3, and any Minor
> change that alters runtime behavior), a post-implementation verification investigation MUST confirm
> the implemented change actually behaves as designed — before the plan closes and before the change
> is treated as usable:
>
> 1. **The NEW behavior itself is exercised** in its real runtime, and the evidence it produces
>    (logs, outputs, event streams) is analyzed against the design intent — reconstructing state from
>    the event stream when the log doesn't print it directly (L065). Compile/type-clean and
>    "defaults unchanged" prove only the rollback guarantee; they say nothing about the feature.
> 2. **The agent drives the verification loop:** defines the exact runs needed, requests any
>    operator-driven halves, and analyzes the returned evidence to an explicit evidence-based verdict
>    ("the output shows X, matching/contradicting the design") — not a checkbox flip.
> 3. **Feature-ON QA cannot be silently deferred.** A scenario that exercises the new behavior ON is
>    ship-gating by default; classifying it opportunistic/deferred requires an explicit operator
>    waiver recorded in the plan's tracker.
> 4. **Expected ≠ observed = defect.** Fix-forward per Rule 3; evidence recorded with provenance
>    verified (L059).
>
> **Why this rule exists:** a change shipped after rollback-guarantee QA alone sat structurally
> broken for fifteen days until the operator happened to exercise it — a single feature-ON run with
> evidence analysis at ship time would have caught it same-day (L067). Rule 11 forces scenarios to be
> DEFINED at change time; Rule 13 hardens the plan BEFORE code; Rule 15 forces the behavior to be
> VERIFIED at implementation-completion — the same granularity as the failure.
>
> **Only permitted abbreviation:** operator explicitly waives verification for a specific change —
> per-change only, recorded in the tracker.
>
> **Drift on this rule is a Major defect** — a plan closing (or a behavior-affecting Minor recorded
> done) without the feature-ON verification evidence, or an explicit waiver, in its tracker.
>
> See `archive/LESSONS.md` L067 for the incident that motivated this rule.

Also both copies, § 8 checklist "### 4. Testing" gains a final row:
`- [ ] Post-implementation verification ran for the NEW behavior itself (Rule 15): feature-ON
evidence analyzed to an explicit verdict, or an operator waiver recorded in the tracker`

### 5E — `scripts/claude_project_data.sh` (NEW; replaces `bootstrap_memory.sh`, which is DELETED)

Full file as shipped (port of the upstream v0.1 + the pre-v1.5 memory-symlink `adopt` branch;
genericized header):

```bash
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
```

`scripts/bootstrap_memory.sh` is **deleted** in the same commit (Rule 8: unused files removed, not
allowlisted); its manifest row is removed and `claude_project_data.sh` registered.

### 5F — SESSION_OPENER (project `docs/SESSION_OPENER.md` + template `docs/standards/SESSION_OPENER.md`)

1. **§ 1.5 replaced** (title + body), both copies:

   > ### 1.5 Project-data locality (durability check — per `CLAUDE.md` Rule 14)
   >
   > Confirm the in-repo project-data store is live BEFORE relying on recall (§ 1.4):
   >
   > ```bash
   > bash scripts/claude_project_data.sh status
   > ls -1 .claude/project-data/memory/*.md 2>/dev/null | wc -l
   > ```
   >
   > - `STATUS: OK` → proceed. Any other status names its fix verb — run it (`link` after a
   >   move/new machine; `adopt` on a machine with un-adopted harness data) and note the repair in
   >   the § 4 block.
   > - Store **unexpectedly empty** when prior sessions are known to have written memory → **STOP**
   >   and warn the operator in the § 4 block (Rule 14 + L050); do not proceed as if there is
   >   genuinely no history.

2. **§ 1.3 addition** (both copies, end of the section): `Read the register WHOLE — top to bottom,
   every time; never a partial slice. Approved or live items can sit low in the file.`

3. **§ 4 output line** (both copies): `- Memory link: <…>` → `- Project data: <OK: N memory files |
   repaired (link/adopt run) | EMPTY — operator warned>`

4. **§ 3.1 rows** — upgrade + two new (project numbering / template numbering):
   - Row 13 (project) / row 14 (template) — replace the memory-loss row text with:
     `Project data written or left outside the project folder — locality symlink absent/broken after
     a machine change or folder move, silently orphaning memory + transcripts | § 1.5 probe on every
     session-open; any tool creating project state outside the repo | CLAUDE.md Rule 14 +
     LESSONS.md L050 (+ v1.5 generalization)`
   - NEW row 15 (project) / 16 (template):
     `Implementation closed on rollback-guarantee QA alone — the NEW behavior never exercised; broken
     feature ships with an unbounded defect window | every behavior-affecting implementation, at
     completion | CLAUDE.md Rule 15 (binding) + LESSONS.md L067`
   - NEW row 16 (project) / 17 (template):
     `Version stamp edited in the change log but not in the stamp field itself (headers, § 3 heading
     counts, manifest cells, count tables) | every stamp-touching edit + the Rule 10 review |
     LESSONS.md L063`

### 5G — SESSION_CLOSER (project + template)

§ 1.6 retitled `### 1.6 /tmp cleanup + locality confirm`; after the existing cleanup content, add:

> **Locality confirm (Rule 14):** `bash scripts/claude_project_data.sh status` → expect `STATUS: OK`.
> If any new project state landed outside the folder this session, move it in (same symlink pattern)
> or catalog it in the machine-migration doc — same-commit.

### 5H — Release mechanics (mechanical rules, per the v1.4 precedent)

1. `docs/standards/STANDARDS_INDEX.md` 1.4→1.5: § 1 block (Set v1.5, released <date>, counts **15
   standing rules / 67 lessons (L001–L067)**; baseline line += "+ upstream-intake process-hardening
   batch (v1.5)"); § 2 row 1 "14 standing rules" → 15, row 9 "56 lessons" → 67; § 3 caption + cells
   for every § 7 suite file touched + totals ("**Total lesson count:** 67 (L001–L067)"); § 6 v1.5
   history entry (additive Minor; the § 3 mapping table summarized; adopters may stay on v1.4).
2. `docs/SET_VERSION_ADOPTED.md` 1.5→1.6: adopt v1.5 same-commit; counts 15/67; backport row.
3. `docs/standards/SETUP.md` 1.4→1.5: live refs v1.4→v1.5 (line-guarded, CHANGE LOG untouched);
   Step 6.5 rewritten — lay down `scripts/claude_project_data.sh` (not bootstrap_memory.sh), run
   `link`, seed a minimal machine-migration doc (`docs/MACHINE_MIGRATION.md`, from inline content:
   title + "catalog of project state that cannot live in the folder" + empty table). **Sweep EVERY
   `bootstrap_memory` reference in the file** (Step 6.5 body, lay-down list, strip/confirm list —
   audit found 3 sites), per L060.
4. `docs/standards/NEW_PROJECT_BOOTSTRAP.md` 1.4→1.5: same retarget + its Step 8 mirrors Step 6.5.
   **Sweep EVERY `bootstrap_memory` reference** (tree, Step 8 body, confirm list, troubleshooting —
   audit found 5 sites), per L060. Historical/immutable mentions elsewhere (closed plans, CHANGELOG
   history, L050's original body, SVA backport rows, STANDARDS_INDEX § 6 history) stay untouched.
5. `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md` 1.1→1.2: retrofit prompt retargeted to the
   project-data pattern (`claude_project_data.sh` + `adopt` for existing data + closer confirm);
   notes PLAN-009 will absorb it into the skill's retrofit mode.
6. `docs/NEW_MACHINE_SETUP.md`: extend with the machine-migration catalog role (Rule 14 names it) +
   the new script verbs; header bump.
7. `docs/documents_manifest.md`: cells for every touched entry; bootstrap_memory row REMOVED;
   `claude_project_data.sh` registered; quick-index caption "Set v1.4" → v1.5; self-row; header.
8. `docs/folder_structure.md`: scripts listing swap + `.claude/project-data` note; header bump.
9. `CHANGELOG.md`: top entry — Set v1.5, the full § 3 mapping table reproduced, Rule 11 exemption
   note for the doc side + § 8 QA list for the script/mechanism side.
10. This plan + `PLAN-010_tracker.md` → 1.0 / CLOSED same commit (§ 7 rows 20–21).

**One-time migration on THIS repo (operational, not a file edit):** run
`bash scripts/claude_project_data.sh adopt` as the **final step** of the Phase-3 session (§ 11 R1);
verify `status` = OK + memory ≥ 11 files at the next session open (§ 8 QA-I confirms). Also update or
remove the untracked `.claude/README_memory.md` (references the old script) in the same step.

## 6. Spec update map

| Artifact | § 5 block | Change class |
|---|---|---|
| Both LESSONS files | 5A, 5B | 11 new lessons + L050 note; headers stay 1.0 |
| Both CLAUDE.md | 5C, 5D | Rule 14 upgrade + Rule 15 new + § 3/§ 13 count fix + § 8.4 row |
| New script / deleted script | 5E | mechanism port |
| Both SESSION_OPENER | 5F | § 1.3/§ 1.5/§ 4 + rows |
| Both SESSION_CLOSER | 5G | § 1.6 confirm |
| Release docs (index, SVA, SETUP, NPB, rollout, machine-setup, manifest, folder, CHANGELOG) | 5H | Set v1.5 cascade |

## 7. Phase-3 ALLOWLIST (the enumeration IS the count — 21 files)

1. `docs/standards/LESSONS.md` · 2. `archive/LESSONS.md` · 3. `CLAUDE.md` ·
4. `docs/standards/CLAUDE.md` · 5. `docs/SESSION_OPENER.md` · 6. `docs/standards/SESSION_OPENER.md` ·
7. `docs/SESSION_CLOSER.md` · 8. `docs/standards/SESSION_CLOSER.md` ·
9. `scripts/claude_project_data.sh` (NEW) · 10. `scripts/bootstrap_memory.sh` (DELETED) ·
11. `docs/standards/STANDARDS_INDEX.md` · 12. `docs/SET_VERSION_ADOPTED.md` ·
13. `docs/standards/SETUP.md` · 14. `docs/standards/NEW_PROJECT_BOOTSTRAP.md` ·
15. `docs/standards/MEMORY_DURABILITY_ROLLOUT_PROMPT.md` · 16. `docs/NEW_MACHINE_SETUP.md` ·
17. `docs/documents_manifest.md` · 18. `docs/folder_structure.md` · 19. `CHANGELOG.md` ·
20. `docs/Plans/PLAN-010_everon_upstream_intake.md` (→ 1.0/CLOSED) ·
21. `docs/Plans/PLAN-010_tracker.md` (→ 1.0/CLOSED)

(+ the operational `adopt` run — no additional file. `docs/MACHINE_MIGRATION.md` is NOT created in
this repo — `docs/NEW_MACHINE_SETUP.md` already fills the role, extended per 5H-6.)

## 8. Validation gate (Phase 4 — QA scenarios per Rule 11; C/I are the Rule 15 feature-ON half)

| ID | Verify | How | Pass |
|---|---|---|---|
| A | script syntax | `bash -n scripts/claude_project_data.sh` | exit 0 |
| B | script behavior on fixtures | scratchpad fixture repo: fake harness dir with files → `adopt` → `status`; simulate folder move → `link` → `status`; old memory-symlink layout → `adopt` absorbs both halves | every verb behaves; OK states; no data loss |
| C | THIS repo adopted (live feature-ON) | run `adopt` (final Phase-3 step) then `status` | `STATUS: OK`; memory files ≥ 11; transcripts present under `.claude/project-data/` |
| D | domain-neutral zero-hit | `grep -riE 'everon|equinex|mql5|mt5|metaeditor|lirunex|strategy tester|\bEA\b|\bbot\b|basket|broker|\btick\b|deal stream' docs/standards/LESSONS.md archive/LESSONS.md CLAUDE.md docs/standards/CLAUDE.md docs/SESSION_OPENER.md docs/standards/SESSION_OPENER.md` on the § 5-touched ranges (bare `sweep` deliberately excluded — legitimate grep-sweep prose; the domain sense was genericized to "decision event") | 0 hits in new/changed text |
| E | stamp/count greps (L063 applied) | § 3 headings + § 13 bullets = "15 standing rules" (both CLAUDE.md); STANDARDS_INDEX § 1/§ 2/§ 3 counts = 15/67; SVA counts; manifest header vs self-row | all stamps equal the new values |
| F | LESSONS integrity | ToC anchors ↔ `### L0NN` headings 1:1 in both files; heading count = 67 | exact |
| G | governance | both Rule-2 scripts | exit 0 |
| H | delivery-doc parity | no live `v1.4` refs outside CHANGE LOGs in SETUP/NPB; rollout prompt retargeted | greps clean |
| I | opener § 1.5 live | next session-open runs the new § 1.5 verbatim | `STATUS: OK` + count line works |
| J | manifest completeness | new script registered; bootstrap_memory row gone; folder_structure matches tree | consistent |

## 9. Operator approval decision point (Phase 2)

- **APPROVE D10.A** — implement § 5 as specified (D1=A1 and D2 baked in).
- **D10.B** — approve minus the mechanism port (5E/5F-§1.5/5G reduced; Rule 14 text-only — weaker,
  not recommended).
- **D10.C** — request changes (name them).

## 10. Rollback path

Single commit → `git revert` restores all docs and resurrects `bootstrap_memory.sh`. The `adopt`
migration is independently reversible: `rm` the harness symlink, `mv .claude/project-data/memory
.claude/memory`, `mv` transcripts back to a recreated harness dir, re-run the old bootstrap (from git
history). No EverOn-side state to roll back (read-only).

## 11. Known risks

| # | Risk | Mitigation | Status |
|---|---|---|---|
| R1 | `adopt` moves the live session's own transcript mid-session | run `adopt` as the LAST Phase-3 step; harness recreates its handle on next write; stray dir merged by `link` (script handles it); QA-I verifies at next open | CLOSED 2026-08-16 — adopt ran as the final Phase-3 step, QA-C OK; QA-I re-confirms at next open |
| R2 | Future vault↔upstream numbering divergence | § 3 mapping table is the permanent record (plan + CHANGELOG); PLAN-011 convergence ends the second line | documented |
| R3 | Domain terms slip genericization | QA-D exhaustive case-insensitive multi-form grep (per new L060) at final text | mitigated |
| R4 | Count/stamp cells drift during the big cascade | QA-E recomputes every stamp from source (per new L063); pre-computed here: rules 14→15, lessons 56→67 | mitigated |
| R5 | Old-pattern adopters (first bootstrapped project) break against upgraded docs | their layout keeps working (old symlink untouched until they migrate); rollout prompt updated now; PLAN-011 migrates them via `adopt` (memory-symlink branch built for exactly this) | mitigated |
| R6 | Script portability (macOS bash 3.2) | port uses only bash-3.2-safe constructs (verified upstream-identical core); QA-A/B exercise on this machine | mitigated |

## 12. Acceptance criteria

- Both LESSONS files carry L057–L067 + the L050 note; ToC/heading parity; headers still 1.0.
- Both CLAUDE.md copies: Rule 14 upgraded, Rule 15 present, § 3/§ 13 say **15**, § 8.4 row added.
- `claude_project_data.sh` shipped + `bootstrap_memory.sh` gone; fixture QA-B green; this repo
  adopted (QA-C/I) with zero memory loss.
- Session files carry the new § 1.3/§ 1.5/§ 1.6/§ 4 text + the three § 3.1 row changes, both copies.
- Set v1.5 released (index/SVA/SETUP/NPB/rollout/manifest/folder/CHANGELOG cascade; QA-E/H clean).
- QA A–J all pass; governance exit 0; zero-hit domain grep; no EverOn-repo write; single commit;
  plan + tracker promoted 1.0/CLOSED same commit.

