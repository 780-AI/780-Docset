<!-- VERSION: 1.2 -->
<!-- Last Updated: 2026-09-05 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.2 — 2026-09-05 — Standard Set Version v2.5 (PLAN-012, riding the release): L069–L078 date
lines corrected — the vault machine's clock ran ~9 days slow at intake (real date 2026-09-05,
stamped 2026-08-27). Date-line corrections only; no lesson content change.
v1.1 — 2026-08-27 — Standard Set Version v2.3: ownership/contribution banner added (adopter
copies are engine-owned; contribute via STANDARDS_LOG E0NN — the L069 incident); lessons
L069–L078 added (L069 the intake-gate incident itself; L070–L078 the first adopter-originated
intake batch, genericized). Counts 68 → 78.
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

# LESSONS.md — Incident-to-Rule Archive

**Purpose:** This file captures the **why** behind every rule in the standards repo. Each entry traces a specific incident that occurred during real project work, the rule that was codified to prevent recurrence, and where that rule lives now.

**Append-only.** Old lessons are never deleted, even if the underlying rule is later removed or revised — the historical context is what makes the current standards defensible. New lessons add at the **top** (newest first), matching the CHANGELOG convention.

> **⚠️ OWNERSHIP — read before adding a lesson here.** In an **adopter project** this file is
> **engine-owned**: the sync engine replaces it wholesale with the vault's canonical archive on
> every sync, and anything appended directly here is **destroyed by the next `sync --write`**.
> Project lessons are contributed as `E0NN` entries in `docs/STANDARDS_LOG.md` (Status: open) —
> they reach the vault via harvest → integrate and return here, genericized, on a later sync.
> Only the vault codifies directly into this archive. (See L069 for the incident behind this
> banner.)

**Why this file exists:** Standards documents capture *what* the rules are. This file captures *why* they exist. When a future contributor (or future-you in 18 months) wonders "why do we use fix-forward instead of amend?", the answer is here, with the specific incident attached as evidence. Without this archive, every rule eventually gets re-litigated by someone who didn't experience the original failure.

---

## Table of Contents

1. [How to read this file](#1-how-to-read-this-file)
2. [Lesson entry format](#2-lesson-entry-format)
3. [The lessons (newest first)](#3-the-lessons-newest-first)
 - [L079 — The machine clock is an untrusted input: verify it against an external authority before stamping or recording skew](#l079--the-machine-clock-is-an-untrusted-input-verify-it-against-an-external-authority-before-stamping-or-recording-skew)
 - [L078 — A date-relative fixture must respect the worst-case bound of the window it depends on](#l078--a-date-relative-fixture-must-respect-the-worst-case-bound-of-the-window-it-depends-on)
 - [L077 — A pool that forks children needs per-child installation, not per-process](#l077--a-pool-that-forks-children-needs-per-child-installation-not-per-process)
 - [L076 — A plan gap that is a scope question is surfaced as options, never resolved silently](#l076--a-plan-gap-that-is-a-scope-question-is-surfaced-as-options-never-resolved-silently)
 - [L075 — A gitignore pattern can silently swallow a file the commit claims to ship](#l075--a-gitignore-pattern-can-silently-swallow-a-file-the-commit-claims-to-ship)
 - [L074 — A side effect that must survive an exception needs its own transaction](#l074--a-side-effect-that-must-survive-an-exception-needs-its-own-transaction)
 - [L073 — Structured-log extra keys must not collide with reserved logging attributes](#l073--structured-log-extra-keys-must-not-collide-with-reserved-logging-attributes)
 - [L072 — Before subscribing to a fan-out topic, state what the payload guarantees at that hop](#l072--before-subscribing-to-a-fan-out-topic-state-what-the-payload-guarantees-at-that-hop)
 - [L071 — A documented override that has never been exercised is not known to work](#l071--a-documented-override-that-has-never-been-exercised-is-not-known-to-work)
 - [L070 — A uniqueness key that encodes an intent must not be consumed by a cancelled attempt](#l070--a-uniqueness-key-that-encodes-an-intent-must-not-be-consumed-by-a-cancelled-attempt)
 - [L069 — The engine-owned lessons archive invites appends; adopter lessons need a visible channel and an intake gate](#l069--the-engine-owned-lessons-archive-invites-appends-adopter-lessons-need-a-visible-channel-and-an-intake-gate)
 - [L068 — Template cross-references must resolve in the adopter, not the vault](#l068--template-cross-references-must-resolve-in-the-adopter-not-the-vault)
 - [L067 — Ship-gating verification must exercise the NEW behavior itself](#l067--ship-gating-verification-must-exercise-the-new-behavior-itself)
 - [L066 — A liveness signal must come from the monitored layer's own traffic, on the monitor's own clock](#l066--a-liveness-signal-must-come-from-the-monitored-layers-own-traffic-on-the-monitors-own-clock)
 - [L065 — Reconstruct system state from its own event stream to check invariants the log doesn't print](#l065--reconstruct-system-state-from-its-own-event-stream-to-check-invariants-the-log-doesnt-print)
 - [L064 — Validate on a version-matched runtime with real dependencies; fakes must return real driver types](#l064--validate-on-a-version-matched-runtime-with-real-dependencies-fakes-must-return-real-driver-types)
 - [L063 — Version stamps drift from their own change logs; grep the actual stamp at edit and review time](#l063--version-stamps-drift-from-their-own-change-logs-grep-the-actual-stamp-at-edit-and-review-time)
 - [L062 — Plan-embedded code must satisfy the plan's own acceptance criteria across all sites; sanitize before pasting](#l062--plan-embedded-code-must-satisfy-the-plans-own-acceptance-criteria-across-all-sites-sanitize-before-pasting)
 - [L061 — A reused helper imports its implicit gates; enumerate them per new context](#l061--a-reused-helper-imports-its-implicit-gates-enumerate-them-per-new-context)
 - [L060 — Grep every name-form of a removed identifier across code AND docs](#l060--grep-every-name-form-of-a-removed-identifier-across-code-and-docs)
 - [L059 — Verify evidence provenance before recording a result](#l059--verify-evidence-provenance-before-recording-a-result)
 - [L058 — Audit every caller before fixing a shared utility at one site](#l058--audit-every-caller-before-fixing-a-shared-utility-at-one-site)
 - [L057 — Identical code + different behavior ⇒ runtime cause; instrument and gather runtime data first](#l057--identical-code--different-behavior--runtime-cause-instrument-and-gather-runtime-data-first)
 - [L056 — The Phase-3 implementer reconciles the plan against the live source before editing](#l056--the-phase-3-implementer-reconciles-the-plan-against-the-live-source-before-editing)
 - [L055 — Recorded push-state must be reconciled against the real remote and flipped in the same wrap-up as the push](#l055--recorded-push-state-must-be-reconciled-against-the-real-remote-and-flipped-in-the-same-wrap-up-as-the-push)
 - [L054 — The Phase-3 ALLOWLIST must enumerate the plan file and sibling tracker promotion rows](#l054--the-phase-3-allowlist-must-enumerate-the-plan-file-and-sibling-tracker-promotion-rows)
 - [L053 — Bootstrap delivery docs are a parity set — a procedure change updates all of them in the same pass](#l053--bootstrap-delivery-docs-are-a-parity-set--a-procedure-change-updates-all-of-them-in-the-same-pass)
 - [L052 — An installer must create every file it references, not just account for it](#l052--an-installer-must-create-every-file-it-references-not-just-account-for-it)
 - [L051 — The senior-review pass must mechanically run the linters / type-checker / tests against the plan's embedded code, not eyeball it](#l051--the-senior-review-pass-must-mechanically-run-the-linters--type-checker--tests-against-the-plans-embedded-code-not-eyeball-it)
 - [L050 — Project memory must live inside the synced repo, not the machine-local harness dir](#l050--project-memory-must-live-inside-the-synced-repo-not-the-machine-local-harness-dir)
 - [L049 — A plan draft is a hypothesis: a mandatory senior-review-and-optimize pass before approval catches what the drafting pass ships](#l049--a-plan-draft-is-a-hypothesis-a-mandatory-senior-review-and-optimize-pass-before-approval-catches-what-the-drafting-pass-ships)
 - [L048 — Session wrap-up routine as forcing function against detail loss across session boundaries](#l048--session-wrap-up-routine-as-forcing-function-against-detail-loss-across-session-boundaries)
 - [L047 — QA / smoke-test scenarios must be coupled to changes at change-time, not validation-time](#l047--qa--smoke-test-scenarios-must-be-coupled-to-changes-at-change-time-not-validation-time)
 - [L046 — Local-only OPEN_TASKS.md register: cross-plan + non-plan "what's open right now" index](#l046--local-only-open_tasksmd-register-cross-plan--non-plan-whats-open-right-now-index)
 - [L045 — Plan tracker discipline: big plans get a sibling tracker, small plans expand § 4 in-file](#l045--plan-tracker-discipline-big-plans-get-a-sibling-tracker-small-plans-expand--4-in-file)
 - [L044 — Session-scoped checklists don't enforce per-commit discipline; embed the rule in the procedure](#l044--session-scoped-checklists-dont-enforce-per-commit-discipline-embed-the-rule-in-the-procedure)
 - [L043 — Session-start pre-flight as forcing function](#l043--session-start-pre-flight-as-forcing-function)
 - [L042 — Plan-first for vital changes: full plan + Phase 2 approval + Phase 3 in a fresh session](#l042--plan-first-for-vital-changes-full-plan--phase-2-approval--phase-3-in-a-fresh-session)
 - [L041 — Pattern-match safety tripwire for external string catalogs](#l041--pattern-match-safety-tripwire-for-external-string-catalogs)
 - [L040 — Fail-safe defaults for external-data sources that may be unavailable](#l040--fail-safe-defaults-for-external-data-sources-that-may-be-unavailable)
 - [L039 — Grep all reads before splitting a globally-read state variable](#l039--grep-all-reads-before-splitting-a-globally-read-state-variable)
 - [L038 — ALLOWLIST count is the bullet enumeration, not the prose sentence](#l038--allowlist-count-is-the-bullet-enumeration-not-the-prose-sentence)
 - [L037 — Time-window with end=00:00 fires at minute 0 of the same day (wrap-window pitfall)](#l037--time-window-with-end0000-fires-at-minute-0-of-the-same-day-wrap-window-pitfall)
 - [L036 — Annotate a closed plan-risk in the same commit that ships the mitigation](#l036--annotate-a-closed-plan-risk-in-the-same-commit-that-ships-the-mitigation)
 - [L035 — a cloud provider's web console avoidance for sensitive files](#l035--a-cloud-providers-web-console-avoidance-for-sensitive-files)
 - [L034 — macOS disk full: restart frees 30+ GB; don't hunt caches first](#l034--macos-disk-full-restart-frees-30-gb-dont-hunt-caches-first)
 - [L033 — Codex retry prompts need PRIOR DEVIATION WARNING](#l033--codex-retry-prompts-need-prior-deviation-warning)
 - [L032 — Investigate underlying data when operator questions answers](#l032--investigate-underlying-data-when-operator-questions-answers)
 - [L031 — Never bounce operator to UI for status; agent probes via REST API](#l031--never-bounce-operator-to-ui-for-status-agent-probes-via-rest-api)
 - [L030 — Always call out PROD actions explicitly](#l030--always-call-out-prod-actions-explicitly)
 - [L029 — Distribute doc sync across split commits](#l029--distribute-doc-sync-across-split-commits)
 - [L028 — Batch local commits; push only when necessary](#l028--batch-local-commits-push-only-when-necessary)
 - [L027 — Code review BEFORE every commit (separate from governance)](#l027--code-review-before-every-commit-separate-from-governance)
 - [L026 — Run commits yourself; don't hand back to user](#l026--run-commits-yourself-dont-hand-back-to-user)
 - [L025 — CI-injected `.env` files are wiped on every deploy](#l025--ci-injected-env-files-are-wiped-on-every-deploy)
 - [L024 — Never run raw `docker compose up` on staging or production](#l024--never-run-raw-docker-compose-up-on-staging-or-production)
 - [L023 — Staging mirrors production — env parity](#l023--staging-mirrors-production--env-parity)
 - [L022 — 24-hour staging soak required before any production deploy](#l022--24-hour-staging-soak-required-before-any-production-deploy)
 - [L021 — Live candle OHLC values mutate during first 10 min](#l021--live-candle-ohlc-values-mutate-during-first-10-min)
 - [L020 — Codex handoff protocol (separate-domain agent collaboration)](#l020--codex-handoff-protocol-separate-domain-agent-collaboration)
 - [L019 — Self-contained CI jobs: auth state should not cross job boundaries](#l019--self-contained-ci-jobs-auth-state-should-not-cross-job-boundaries)
 - [L018 — Cross-job auth state assumptions break silently in CI](#l018--cross-job-auth-state-assumptions-break-silently-in-ci)
 - [L017 — Never-exercised gates fire bugs in cascade](#l017--never-exercised-gates-fire-bugs-in-cascade)
 - [L016 — Allow-failure jobs become decoration, not checks](#l016--allow-failure-jobs-become-decoration-not-checks)
 - [L015 — Project Instructions for one project bleed into another](#l015--project-instructions-for-one-project-bleed-into-another)
 - [L014 — Long single-file standards docs lose recall in the middle](#l014--long-single-file-standards-docs-lose-recall-in-the-middle)
 - [L013 — Project knowledge precedence prevents fabrication](#l013--project-knowledge-precedence-prevents-fabrication)
 - [L012 — Gitignore case-sensitivity surprises on macOS](#l012--gitignore-case-sensitivity-surprises-on-macos)
 - [L011 — Pager-safe verification (avoid `less` ambushing output)](#l011--pager-safe-verification-avoid-less-ambushing-output)
 - [L010 — Split-commit delivery for substantive doc additions](#l010--split-commit-delivery-for-substantive-doc-additions)
 - [L009 — Deliberate-failure testing for alerting/check code](#l009--deliberate-failure-testing-for-alertingcheck-code)
 - [L008 — Manifest completeness: no exclusion lists](#l008--manifest-completeness-no-exclusion-lists)
 - [L007 — Multi-file Cursor prompts need ALLOWLIST + verbatim FIND/REPLACE](#l007--multi-file-cursor-prompts-need-allowlist--verbatim-findreplace)
 - [L006 — Verify agent claims via filesystem](#l006--verify-agent-claims-via-filesystem)
 - [L005 — Local governance does NOT validate CI schema](#l005--local-governance-does-not-validate-ci-schema)
 - [L004 — Heredoc-piped commit messages corrupt special characters](#l004--heredoc-piped-commit-messages-corrupt-special-characters)
 - [L003 — Fix-forward via letter suffix preserves the lesson](#l003--fix-forward-via-letter-suffix-preserves-the-lesson)
 - [L002 — Pre-push governance must be local AND in CI](#l002--pre-push-governance-must-be-local-and-in-ci)
 - [L001 — Plans folder rule (commit your plans)](#l001--plans-folder-rule-commit-your-plans)

---

## 1. How to read this file

Each lesson follows the same structure:

- **Incident** — what specifically happened, with enough detail that a reader unfamiliar with the project can understand the failure mode
- **Cost** — what the failure cost (time, broken commits, silent corruption, etc.)
- **Codification** — what rule was added to prevent recurrence, and where it lives in the standards
- **Cross-references** — pointers to the standards files that enforce the lesson now

Lessons are numbered by topic, not chronologically. **L-numbers are stable identifiers** used as cross-references from other standards files (e.g., `CLAUDE.md` Rule 3 → see lesson L003). The actual incident date appears in each lesson's `**Date:**` metadata field; check that field for chronological context.

The numbering is permanent — never renumber when inserting between entries. Use letter suffixes if a lesson needs a follow-up (L007 → L007b for a refinement of the original).

---

## 2. Lesson entry format

```markdown
### LXXX — <Title>

**Date:** YYYY-MM-DD
**Project:** <project-name> (or "cross-project" if it spans multiple)
**Phase / Task:** <phase or task identifier if applicable>

#### Incident

<2-4 paragraph narrative of what happened, including the trigger, the
sequence of events, the symptom, and how it was discovered. Be specific
enough that a reader can imagine the situation.>

#### Cost

<What did this incident cost? Time, broken commits, silent data corruption,
lost work, customer impact, debugging effort. Be honest.>

#### Codification

<What rule was added to prevent recurrence? Quote the rule text. Cite
where it lives now (which standards file, which section).>

#### Cross-references

- `<standards-file>.md` § <section> — primary enforcement location
- `<other-standards-file>.md` § <section> — related rule
- (any other lessons in this file that this one relates to)
```

---

## 3. The lessons (newest first)

### L079 — The machine clock is an untrusted input: verify it against an external authority before stamping or recording skew

**Date:** 2026-10-03
**Project:** an adopter project (team) → vault (merged with the vault's own skew-record correction)
**Phase / Task:** first syncs into a newly registered adopter → experiences-log entry → harvest → integrate (Standard Set Version v2.6)

#### Incident

The sync engine takes "today" from the wall clock of the machine it runs on. The curator
machine's clock had drifted about nine days slow, so the first syncs into a newly registered
adopter wrote header and change-log stamps dated *before* the adopter's own bootstrap lines —
every touched file's history read out of order. The adopter's session caught it by comparing its
own clock with a code-hosting server's time and logged it. Worse, the vault had already noticed
the two machines disagreed and recorded the skew the wrong way round ("the adopter's clock runs
fast"); the record stood for a week while the vault's own stamps from that window were wrong. A
re-sync cannot repair such stamps: the engine is idempotent on converged content, so a wrong date
written once stays written.

#### Diagnosis

Two failures, one root — the wall clock was treated as trustworthy. (1) Every stamping tool
inherits its host's clock silently; nothing compared "today" with anything. (2) When two clocks
disagreed, the direction was inferred rather than measured — the L032 anti-pattern applied to
time. Dates are stamp-class data (L063): a wrong value is silent at write time and trusted by every
later reader.

#### Codification

- **Before a session that stamps dates into shared artifacts** (sync runs, releases, a machine new
  to the project), verify the local clock against an external authority — e.g. the `Date:` header
  of a well-known HTTPS host (`curl -sI https://<host> | grep -i '^date:'` vs `date -u`).
- **Review-time check** (PROJECT_STANDARDS § 5.6): a new change-log line dated earlier than the line
  below it, or a `Last Updated` that moves backwards, means the clock is suspect — verify before
  committing; never "fix" it by reordering history.
- **When two machines disagree, measure both against the external authority before recording which
  one is wrong.**
- Tooling that stamps dates into other repositories should take "today" from a trusted source, or
  refuse when the wall clock is earlier than the target's newest existing stamp.

#### Cross-references

- L063 (stamps drift silently — this lesson adds the date-ordering check to the stamp grep)
- L032 (when an answer is questioned, measure the underlying source — don't infer)
- L059 (evidence provenance — a timestamp is evidence only if its clock is trusted)
- PROJECT_STANDARDS § 5.6 (the stamp-date rule)

---

### L078 — A date-relative fixture must respect the worst-case bound of the window it depends on

**Date:** 2026-09-05 (vault intake — originally stamped 2026-08-27 by the vault machine's slow clock; the source project's own stamps were accurate)
**Project:** an adopter project (team) → vault intake
**Phase / Task:** surfaced by a routine baseline test run after a calendar month roll-over

#### Incident

A database test inserted a record dated `now() − 100 days` into a month-partitioned table, with a
comment confidently claiming the offset was "still inside the retained partitions". The retention
window was now −3..+3 months — and three calendar months are **89 days at minimum** — so the
fixture was legal on every day it had ever run and exploded on the first month roll-over after it
was written ("no partition found for row"). The suite went red on a change that had nothing to do
with it.

#### Diagnosis

The fixture was validated against the calendar of the day it was written, not against the
worst-case geometry of the window it depended on. Date-relative test data ages: any
`now()`-relative offset interacts with partition horizons, retention windows, and month lengths,
and the failure appears only when the calendar shifts — long after the commit that planted it. A
comment asserting safety without the arithmetic is how such landmines get trusted.

#### Codification

Any test fixture computed relative to `now()` must stay within the **worst-case** bound of the
window it depends on (partition horizon, retention, cadence), and the bound's arithmetic belongs
in the comment next to the offset — "still inside" claims without arithmetic are a review flag.
When a suite fails on the first run of a new day/month, suspect calendar geometry before
suspecting the diff.

#### Cross-references

- L037 (the midnight/wrap-window pitfall — the runtime sibling of this fixture-side lesson)
- L051-family: a claim in a comment is not evidence; execute the arithmetic

---

### L077 — A pool that forks children needs per-child installation, not per-process

**Date:** 2026-09-05 (vault intake — originally stamped 2026-08-27 by the vault machine's slow clock; the source project's own stamps were accurate)
**Project:** an adopter project (team) → vault intake
**Phase / Task:** feature-ON verification run (Rule 15) on a pooled background worker

#### Incident

Runtime wiring (service ports/handlers) was installed "once per process" — the API at app
creation, the worker on its ready signal, a poller in `main()` — a rule previously codified after
an earlier incident. A feature-ON run then showed the worker path behaving as if nothing had been
installed, while the identical scenario through a single-process path behaved exactly as
designed. The worker's **prefork children** — the processes that actually execute tasks — fork
BEFORE the ready signal fires on the master, so every install done there was invisible to them.
The gap had been latent for weeks: all prior evidence had exercised only single-process paths.

#### Diagnosis

"Every long-running process entry point installs" was the right rule at the wrong granularity. A
pooled worker is not one process: the master that runs lifecycle signals and the children that
run work are different address spaces, and mutable module state set after the fork point never
reaches the children. Single-process evidence paths cannot surface this — only work executed in a
real pool child can. Automated tests install their own wiring, so they are structurally blind to
it.

#### Codification

Installation hooks must fire **in the process that executes the work** (for prefork pools: the
per-child init signal, keeping the master-ready hook only for pool modes that run work in the
master). When writing a "per process" checklist item, ask whether any listed process forks
workers — if it does, the item is per-child there. Feature-ON verification of anything
port-mediated must include at least one path through a real pool child.

#### Cross-references

- L067 / Rule 15 (the feature-ON discipline that caught it — this is the same shape one level deeper)

---

### L076 — A plan gap that is a scope question is surfaced as options, never resolved silently

**Date:** 2026-09-05 (vault intake — originally stamped 2026-08-27 by the vault machine's slow clock; the source project's own stamps were accurate)
**Project:** an adopter project (team) → vault intake
**Phase / Task:** Phase 3 implementation — mid-task plan gap

#### Incident

A plan specified everything about a scheduled trigger except who it applies to when it fires. The
implementer hit the gap mid-task. Filling it silently would have invented product behavior; a
bare "the plan doesn't say" would have stalled the task with no way forward. Instead the gap was
presented as three numbered options — build the minimal missing piece now, ship the machinery
behind a hook that raises, or block the task — each with its stated consequence and one marked as
the recommendation. The operator answered in a single line and the task shipped the same session,
with the gap documented rather than papered over.

#### Diagnosis

The contract's § 10 ("never assume missing logic") says what **not** to do, and § 15.3 says a
plan gap is a plan defect to surface — but neither says what good surfacing looks like. An
under-specified surfacing ("what do you want here?") transfers the whole design problem back to
the operator, who must reconstruct context the implementer already holds. The agent has the
cheapest access to the option space; the operator has the only authority to choose within it.

#### Codification

A plan gap that is a **scope** question is surfaced as numbered options, each with its
consequence stated, and one marked as the agent's recommendation — never resolved silently, and
never returned as an open-ended question with no recommendation. The chosen option is recorded as
a plan decision with the operator's reply quoted verbatim, so the reasoning survives the session.
Where the chosen option leaves a known gap, it is documented as known-gap-by-design with the task
that closes it named.

#### Cross-references

- `CLAUDE.md` § 10 (never assume) + § 15.3 (plan defects are surfaced, not filled)
- L049 / Rule 13 (the pass that finds these gaps before the implementer does)

---

### L075 — A gitignore pattern can silently swallow a file the commit claims to ship

**Date:** 2026-09-05 (vault intake — originally stamped 2026-08-27 by the vault machine's slow clock; the source project's own stamps were accurate)
**Project:** an adopter project (team) → vault intake
**Phase / Task:** project bootstrap foundation commit

#### Incident

A bootstrap `.gitignore` carried the rule `.env.*`, which also matched `.env.example` — a file
the commit was meant to ship and which its CHANGELOG entry named in the `Files:` list.
`git status` never showed the file, `git add -A` never staged it, and the Rule 6 reconcile ("does
`git status` match the ALLOWLIST?") passed — because an ignored file is absent from `git status`
by design. The gap surfaced two commits later, only because the CHANGELOG's `Files:` list was
re-read against `git status` by hand.

#### Diagnosis

The Rule 6 check compares the ALLOWLIST against what `git status` reports, and `git status`
cannot report a file it has been told to ignore. The check is therefore blind to exactly one
failure class: a file that should be tracked but is ignored. Every other missing ALLOWLIST member
would show up as a discrepancy; this one shows up as nothing at all.

#### Codification

Every path a commit claims to ship must be confirmed **tracked**, not merely absent from the diff
— `git ls-files --error-unmatch <path>` fails loudly where `git status` stays silent. A negation
rule (`!<file>`) belongs in `.gitignore` beside any broad pattern that could capture a
deliberately-shipped file. A mechanical check ("every path in the newest CHANGELOG `Files:` field
is tracked") is the right home for a failure that human review structurally cannot see.

#### Cross-references

- `CLAUDE.md` Rule 6 (verify agent claims via filesystem — and its blind spot)
- L008 (manifest completeness — the same "claimed but not present" failure at the doc layer)

---

### L074 — A side effect that must survive an exception needs its own transaction

**Date:** 2026-09-05 (vault intake — originally stamped 2026-08-27 by the vault machine's slow clock; the source project's own stamps were accurate)
**Project:** an adopter project (team) → vault intake
**Phase / Task:** authentication failure auditing

#### Incident

A failed login wrote an audit row and then raised, both inside the same database transaction. The
raise rolled the transaction back, taking the audit row with it — the record of the failure was
destroyed by the failure it was meant to record. Unit tests passed: they mocked the session, so
rollback semantics never ran. The real-database test tier caught it.

#### Diagnosis

A transaction is an all-or-nothing boundary, and an audit row is precisely the thing that must
**not** be nothing when the rest rolls back. The code read correctly line by line — write the
row, then raise — and was wrong only in its transaction scope, which is invisible unless the
reader is thinking about rollback. Any test double that stands in for the session erases the very
semantics under test.

#### Codification

A side effect whose whole purpose is to outlive a failure — audit rows, failure counters,
dead-letter writes, alert markers — must not share the failing transaction. It gets its own
committed transaction, opened and closed before the raise. Corollary for validation: assertions
about audit and side-effect durability belong in the real-database tier, never in a tier that
mocks the session, because the guarantee under test is the database's, not the code's.

#### Cross-references

- `VALIDATION_STANDARDS.md` (tier selection — what belongs in the real-database tier)
- L064 (validate on a version-matched runtime with real dependencies; fakes hide real semantics)

---

### L073 — Structured-log extra keys must not collide with reserved logging attributes

**Date:** 2026-09-05 (vault intake — originally stamped 2026-08-27 by the vault machine's slow clock; the source project's own stamps were accurate)
**Project:** an adopter project (team) → vault intake
**Phase / Task:** event-layer implementation — three separate call sites in one session

#### Incident

Python's logging module reserves a set of `LogRecord` attribute names (`created`, `name`, `args`,
`msg`, `module`, `levelname`, and others) and raises at runtime when a log call's `extra` dict
shadows one (`KeyError: "Attempt to overwrite 'created' in LogRecord"`). The collision hit three
separate sites in a single session, each found at runtime one at a time — the exception fires
when the line **executes**, not when the module imports.

#### Diagnosis

The failure has no static signal — the call is well-typed, the key is an ordinary string, and a
reviewer would have to carry the reserved-name list in their head. It also hides behind log-level
and branch coverage: a key used only on an error path fails only on that error path, in
production. Three recurrences in one session established that review is not a reliable gate for
it.

#### Codification

Reserved logging attribute names are forbidden as `extra` keys, enforced **mechanically** rather
than by review: a guard test greps the source for `extra={...}` literals and fails on any
reserved key, catching every call site including the ones no test exercises. The general
principle: when a failure mode is invisible to review and invisible until a specific line runs,
the gate belongs in the test suite, not the checklist.

#### Cross-references

- `VALIDATION_STANDARDS.md` (guard tests as mechanical gates)
- L072 / L075-family: mechanical checks for what review structurally cannot see

---

### L072 — Before subscribing to a fan-out topic, state what the payload guarantees at that hop

**Date:** 2026-09-05 (vault intake — originally stamped 2026-08-27 by the vault machine's slow clock; the source project's own stamps were accurate)
**Project:** an adopter project (team) → vault intake
**Phase / Task:** event-pipeline design — caught by the Rule 13 senior-review pass

#### Incident

A design subscribed a new consumer to the fan-out topic every event-layer consumer already
listened on. It would have raced a sibling consumer: at that hop the payload carries the raw
event, and the identifier the new consumer needed is assigned **by** that sibling, downstream.
The consumer would have seen events with the field missing — intermittently, depending on which
consumer won. The Rule 13 pass caught it at design time; the fix was a second, downstream topic
emitted inside the sibling's own transaction.

#### Diagnosis

A fan-out topic looks like an ordered pipeline stage from the subscriber's side — events arrive
in order, so it is easy to assume everything that happens to an event has already happened. It
has not. A topic guarantees only what its **producer** wrote into the payload at that point; a
sibling consumer's effect is not part of the contract and is not ordered relative to yours.

#### Codification

Before subscribing a consumer to a fan-out topic, write down explicitly what the payload
guarantees **at that hop** — which fields exist, and which are populated by downstream consumers.
If the consumer needs another consumer's effect, it needs a **downstream topic** emitted inside
that consumer's transaction, not a subscription to the shared one. Ordering between siblings on a
fan-out topic is never a guarantee, and a race that depends on consumer scheduling is invisible
in every single-consumer test.

#### Cross-references

- L049 / Rule 13 (the pass that caught this before any code was written)

---

### L071 — A documented override that has never been exercised is not known to work

**Date:** 2026-09-05 (vault intake — originally stamped 2026-08-27 by the vault machine's slow clock; the source project's own stamps were accurate)
**Project:** an adopter project (team) → vault intake
**Phase / Task:** first task that genuinely needed a configured value to reach a container

#### Incident

An example env file instructed operators to create an override file at the repo root, and every
`${VAR}` in a compose file was written to read from it. The tool interpolated `${VAR}` from the
**compose file's** directory — not the repo root — so every documented override silently fell
back to its in-file default. The defect shipped with the compose file and lived undetected until
the first time a value genuinely **had** to reach a container (a secret). Fixed by passing the
env file explicitly on every invocation.

#### Diagnosis

Nothing failed while the override was unnecessary, because falling back to the default produced a
working stack. The documentation asserted a mechanism; the mechanism was never exercised; and the
gap between assertion and behavior stayed invisible for as long as nobody depended on it. This is
Rule 15's failure mode one layer down: Rule 15 catches a shipped **feature** never run; this is a
shipped **configuration path** never run.

#### Codification

A documented configuration override is a claim, not a fact, until one run proves a non-default
value actually reaches its consumer. Where the override path is cheap to exercise — and for
env-var plumbing it always is — exercise it in the same commit that documents it: set one value
to something distinguishable and read it back from inside the consumer. Config plumbing carries
no tests by default, so the only evidence available is a run.

#### Cross-references

- `CLAUDE.md` Rule 15 (the same principle for behavior)
- L067 (the incident behind Rule 15)

---

### L070 — A uniqueness key that encodes an intent must not be consumed by a cancelled attempt

**Date:** 2026-09-05 (vault intake — originally stamped 2026-08-27 by the vault machine's slow clock; the source project's own stamps were accurate)
**Project:** an adopter project (team) → vault intake
**Phase / Task:** scheduled-trigger implementation — pause/re-activate lifecycle

#### Incident

Arming a scheduled action inserts one row under a unique key of (subject, version, fire instant)
with `ON CONFLICT DO NOTHING` — the standard guard against double-arming. Pausing the subject
**cancelled** that row rather than deleting it. Re-activating then tried to arm the same
occurrence, hit the cancelled row's key, did nothing — and the subject came back armed with no
schedule. Permanently silent, no error anywhere. Caught by a test asserting the whole
pause/re-activate lifecycle, not by review of the insert.

#### Diagnosis

The key encodes an **intent** — "this should fire at this instant" — but the conflict action was
written as though it encoded an **attempt**. A cancelled attempt still occupies the intent's key,
so the key is consumed forever by an attempt that explicitly did not happen. `DO NOTHING` reads
as obviously safe at the insert site; its wrongness is only visible from the row's whole
lifecycle, which no single call site shows.

#### Codification

When a uniqueness key encodes an intent rather than an attempt, the conflict action must be
decided **per terminal state**, explicitly: a cancelled or failed row is revivable
(`DO UPDATE ... WHERE status = 'cancelled'`), a completed one is not (reviving it would
double-fire). `DO NOTHING` is correct only where the key encodes the attempt itself. The test
that proves it is a lifecycle test — arm, cancel, re-arm, assert the row is live again — because
no single-step test can see a key being permanently consumed.

#### Cross-references

- L074 (transaction-scope sibling: correctness invisible at the single call site)

---

### L069 — The engine-owned lessons archive invites appends; adopter lessons need a visible channel and an intake gate

**Date:** 2026-09-05 (originally stamped 2026-08-27 — the vault machine's clock ran ~9 days slow)
**Project:** an adopter project (team) → vault
**Phase / Task:** routine sync dry-run after a registry update — divergence investigation

#### Incident

A routine `sync` dry-run found an adopter's `archive/LESSONS.md` — replace-mode, engine-owned —
carrying NINE well-formed project-originated lessons appended directly by the project's sessions,
even continuing the canonical numbering. The project's `docs/STANDARDS_LOG.md` held zero E0NN
entries, so `harvest` had reported "no open log entries" throughout — the misdirection was
silent. A `sync --write` would have destroyed all nine lessons. The divergence surfaced only
because a dry-run diffs actual file content.

#### Diagnosis

Three stacked causes. (1) **The delivered contract itself teaches lesson-appending** — "rules are
added when something breaks" plus dozens of L0NN citations — so a disciplined agent session in
the adopter did the vault-appropriate thing in the wrong repo. (2) **The ownership boundary was
invisible at the point of use:** nothing inside the adopter's archive file marked it
engine-owned/replace-mode or redirected to the E0NN channel. (3) **The log-recording discipline
had no forcing function** at the moment a session writes a lesson (the L044 principle:
forcing-function granularity must match failure granularity).

#### Codification

Three fixes at three layers. The ownership banner at the top of this file (visible at exactly the
point of temptation); binding E0NN wording in the session-closer's lessons-learned step (the
moment candidates are codified); and a vault-side operator gate on every intake — the complete
candidate list, per-item plain-language explanations, and per-item recommendations presented in
chat, with NO integration edit landing before explicit operator confirmation (per-intake, no
standing authorization; rejected items marked in the source log, never silently dropped).

#### Cross-references

- The ownership banner at the top of this file
- `SESSION_CLOSER.md` § 1.7 (the binding E0NN wording)
- L044 (forcing-function cadence), L068 (adopter/vault perspective-mismatch class)
- L070–L078 (the nine rescued lessons of this incident's intake batch)

---

### L068 — Template cross-references must resolve in the adopter, not the vault

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Experiences-log intake — first harvest → integrate cycle (Standard Set Version v2.1)

#### Incident

An adopting project's migration validation grep found its instantiated session-closer § 1.2 pointing
at the suite's vault-side set manifest (`STANDARDS_INDEX.md`) — a file the delivery contract never
places in adopters; an adopter's Set Version lives in its own adoption record
(`SET_VERSION_ADOPTED.md`). Patching the line locally would have broken merge idempotence (the next
sync would re-impose the suite-owned template text), so the project logged the defect as an open
experiences-log entry instead — the contribution loop working as designed on day one.

#### Diagnosis

Template body text was written from the vault's perspective, where the reference resolves. Nothing at
template-edit time checked cross-references against the set of files an adopter actually receives
(the SYNC_MAP set plus the files the delivery skill creates). Any vault-only reference embedded in
suite-owned body text ships broken to every adopter — and cannot be fixed target-side without
breaking sync.

#### Codification

A cross-reference in suite-owned template body text may point only at files the delivery contract
actually places in an adopter (SYNC_MAP items + skill-created files) — checked at template-edit
time. Where vault and adopter legitimately differ, the reference either lives in a PROJECT-OWNED
block or targets the adopter-side file (which the vault, as self-adopter, also carries). Fixed in
`SESSION_CLOSER.md` § 1.2 (Set Version v2.1).

#### Cross-references

- `SESSION_CLOSER.md` § 1.2 (the corrected reference)
- `STANDARDS_LOG.md` (the experiences-log → harvest → integrate loop that carried this lesson)

---

### L067 — Ship-gating verification must exercise the NEW behavior itself

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

A feature shipped after its ship-gating QA passed — compile clean + defaults-byte-identical (the
rollback guarantee). The scenarios that exercised the feature ON were classed opportunistic and never
ran. Fifteen days later the operator switched the feature on and found it structurally broken in both
of its modes; a single feature-ON run with log analysis at ship time — under an hour of work — would
have caught it same-day.

#### Diagnosis

Rollback-guarantee QA proves only that the OFF path is safe; it says nothing about the feature. When
feature-ON scenarios are deferrable, verification silently degrades to "whenever someone happens to
try it" — an unbounded defect window.

#### Codification

Ship-gating verification must exercise the NEW behavior itself in its real runtime and analyze the
produced evidence against the design intent (per L065); feature-ON QA is ship-gating by default and
deferring it requires an explicit operator waiver recorded in the tracker. Enforced as binding
Rule 15.

#### Cross-references

- `CLAUDE.md` § 3 Rule 15 (the binding rule)
- L065 (the verification method)
- L059 (evidence provenance)
- L047 / Rule 11 (scenarios defined at change time — Rule 15 verifies at implementation time)

---

### L066 — A liveness signal must come from the monitored layer's own traffic, on the monitor's own clock

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

Two independent leaks of one invariant in a monitoring system's "is it alive?" signal: (1) the
liveness timestamp was stamped from a payload field produced by a foreign clock, so a source with a
shifted clock looked fresh for hours after going silent; (2) a *different* layer's traffic refreshed
the timestamp (the host process was alive, so the monitored component could never go stale even when
absent). Both were invisible in normal operation and surfaced only under a shifted clock and a
deliberate detach test.

#### Diagnosis

A heartbeat means "the monitored thing itself was heard, on OUR clock." Foreign timestamps are data,
not clocks; a parent layer's liveness is not the child's.

#### Codification

(a) Never stamp liveness from a timestamp whose clock you don't own; (b) each monitored layer keeps
its own liveness field, refreshed only by that layer's own traffic; (c) enforce with tests that make
the wrong call impossible (the wrong-path test raises).

#### Cross-references

- L040-class fail-safe treatment of external data (external input is untrusted)
- L067 (deliberate-detach tests are feature-ON verification)

---

### L065 — Reconstruct system state from its own event stream to check invariants the log doesn't print

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

Repeatedly, a QA pass criterion referenced internal state the system's log does not print directly.
The proven technique: parse the ordered event stream, maintain the state it implies (a book, a queue,
a counter), snapshot at each decision event, and check the invariant against the system's own printed
numbers — evidence-grade verdicts with exact figures, used across four separate verifications without
adding any throwaway instrumentation to the production code.

#### Diagnosis

The alternatives are both bad — weaken the criterion to "looks right," or ship QA-only log lines
into a critical file.

#### Codification

When a pass criterion cites state not printed in the log, reconstruct it from the event stream rather
than weakening the criterion or instrumenting production code: parse events in order, maintain the
implied state, snapshot at decision points, compare against the system's own output. Verify evidence
provenance first (L059).

#### Cross-references

- L059 (provenance before trusting the file)
- L067 / Rule 15 (this is the standard verification method for feature-ON evidence)

---

### L064 — Validate on a version-matched runtime with real dependencies; fakes must return real driver types

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

A subsystem targeting one interpreter version was checked with syntax-level tools that pass on any
version; standing up a real environment on the TARGET version with the real dependency set and
running the actual test suite plus a live entry-point exercise caught three real bugs the syntax
checks had waved through. A related incident one level deeper: a serve path broke in production
because the test fake returned a convenience type where the real driver returns a typed value — the
suite passed, the deployment black-paged.

#### Diagnosis

Syntax checks and lint are pre-checks, not validation; a test suite is only as real as its
environment and its fakes.

#### Codification

Before shipping subsystem code, create or reuse an environment on the target runtime version, install
the real dependency set, run the full suite there, and exercise the real entry points. Test fakes on
serve paths must return the real driver types, not convenience shapes.

#### Cross-references

- staging-parity lessons (same principle at environment level)
- L057 (runtime-first diagnosis — the sibling discipline)

---

### L063 — Version stamps drift from their own change logs; grep the actual stamp at edit and review time

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

A recurring class — an artifact carries a machine-readable version stamp AND a human change log, and
the stamp silently stops moving while the log advances. Multiple occurrences in one week in the
upstream project (a package version field, the same field again at the next bump, a manifest header,
a derived count table); the vault's own history carries four more (two stale manifest cells, a stale
self-row, and — found during this plan's audit — the contract's § 3 heading still reading "13
standing rules" two rule-additions later).

#### Diagnosis

Each instance is silent — nothing breaks at commit time; a later reader trusts the stamp. The class
recurs because editing the change log *feels* like bumping the version.

#### Codification

A "version bumped" claim is verified against the actual stamp, not the log entry: at edit time AND at
the Rule 10 review, grep the stamp field itself (`<!-- VERSION:`, `version =`, `# VERSION:`, count
headings, count-table totals) and confirm it equals the new value. Derived stamps are recomputed from
source, never incremented. Plans that touch counts pre-compute the arithmetic and the implementer
grep-verifies every stamp site.

#### Cross-references

- L044 (forcing-function cadence = failure cadence — this one fires per stamp-touching edit)
- Rule 10 (the review is the second gate)

---

### L062 — Plan-embedded code must satisfy the plan's own acceptance criteria across all sites; sanitize before pasting

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

Two gates, two failure shapes. At the senior pass: a plan's transformation rules removed an
identifier while the plan's own acceptance criteria demanded `grep == 0` for it — and the rules
missed an entire class of sites (in-source help text), making the plan self-contradictory; caught by
checking the rules against the plan's own § 8/§ 12. At implement time: embedded blocks carried
target-language footguns that read fine on the page (an escape sequence invalid in the target's
string literals, a comment placement with runtime meaning, delimiter-unbalancing punctuation in a
comment) — caught only because the implementer sanitized rather than pasting verbatim.

#### Diagnosis

Plan-embedded code is a hypothesis written against a snapshot, in an editor that doesn't speak the
target language.

#### Codification

Harden at BOTH gates. (1) The Rule 13 pass verifies the § 5 rules achieve the plan's OWN acceptance
criteria across ALL site classes — including help text, docs, and user-visible strings, not just
code. (2) The Phase-3 implementer sanitizes every embedded block against the target language's
conventions before pasting — never paste verbatim. Extends L060 to the plan-drafting layer.

#### Cross-references

- L049 (the senior pass)
- L051 (run the tools)
- L056 (reconcile against live source)
- L060 (every name-form)
- Rule 7 (verbatim blocks are the input, not the excuse)

---

### L061 — A reused helper imports its implicit gates; enumerate them per new context

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

A new feature reused an existing selection helper verbatim. The helper carried an implicit
minimum-threshold gate that was correct in its original context and wrong in the new one — below the
threshold it silently selected nothing, the new feature never acted, and a safety net fired instead.
The plan said "reuses X"; the senior pass confirmed the *logic* matched; neither enumerated the
helper's implicit preconditions against the new context. A full follow-up plan was needed to fix it.

#### Diagnosis

Reuse imports thresholds, clamps, mode semantics, and ordering assumptions along with the logic.
"Reuses X verbatim" is not a safe shorthand; the defect class is invisible to a logic-level read.

#### Codification

When a plan reuses an existing helper in a NEW feature context, the Rule 13 pass must enumerate the
helper's implicit gates — minimums, clamps, mode semantics, selection/ordering assumptions — and
check each against the new context's intent, not merely confirm the logic reads correctly.

#### Cross-references

- L049 (the pass where the enumeration belongs)
- L058 (enumerate the blast radius from ground truth, not from a hand-listed subset)

---

### L060 — Grep every name-form of a removed identifier across code AND docs

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

A feature removal's plan enumerated the code sites and the docs to update; both lists were treated as
complete. An exhaustive grep across every name-form found the removed feature's hyphenated and
lowercase forms, helper names, and a user-visible string scattered across four additional docs and
one live code branch the lists never mentioned — caught only by sweeping both code and docs with
every form, plus a final verification grep before staging.

#### Diagnosis

A plan's enumerated touch-point lists are a starting inventory, not a complete one; name-forms
multiply (snake_case, kebab-case, lowercase prose, function names, display strings, markdown anchor
slugs) and each form hides in a different file class.

#### Codification

Before any removal or rename commit, run an exhaustive, case-insensitive grep across BOTH code and
all docs using EVERY name-form of the affected identifier — including anchor slugs and user-visible
strings — and a final verification grep immediately before staging. The same sweep discipline applies
to domain-neutralization scrubs (a zero-hit grep gate over all forms is the pass criterion).

#### Cross-references

- L058 (audit-all-callers — sibling enumerate-from-source discipline)
- L038 (the ALLOWLIST count IS the expectation)
- L062 (the plan-layer extension)

---

### L059 — Verify evidence provenance before recording a result

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

Two instances of one trap. Evidence logs supplied for a QA verdict turned out to be from the
predecessor host, not the live one (sizes and line counts didn't match). Later, a single day's log
contained TWO versions of the system — the old version until mid-day, the new one after — and a
naïve whole-file tally would have credited the old version's lines to the new. The fix: locate the
initialization marker, slice the file to the confirmed portion, verify only that.

#### Diagnosis

A filename or date is not provenance — one file can mix versions (mid-run restart) or come from a
different host entirely. A result recorded against evidence the target never produced is a
false-confidence record that is very hard to detect later.

#### Codification

Before recording any QA/audit result from an evidence file, verify which host and which version
actually produced the lines you are about to trust — instance identifiers, init timestamps,
size/content consistency with the expected source — then slice to the confirmed portion and verify
only that.

#### Cross-references

- L032 (investigate the underlying data — parent discipline)
- L065 (the replay method this feeds)
- L067 / Rule 15 (verification evidence)

---

### L058 — Audit every caller before fixing a shared utility at one site

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

A bug was reported at one call site of a shared time-reading idiom. Instead of a one-site patch, a
full audit of the idiom across the codebase found nine sites sharing the same failure mode — license
expiry, session gates, history bounds, a display — all reading a value that stalls when the
environment goes quiet. Fixing only the reported site would have left eight latent defects to surface
one at a time, each re-diagnosed from scratch. All nine were converted in one reviewed commit; QA
confirmed no regression.

#### Diagnosis

A shared utility's defect is a class, not an instance. The reported site is merely the one that
happened to be observed.

#### Codification

Before fixing a bug in a shared utility or a repeated idiom, grep every caller and every occurrence
and categorize each — same defect, or load-bearing as written? Fix the whole class in one reviewed
pass rather than the reported site.

#### Cross-references

- L039 (grep all reads before splitting global state — the vault's sibling)
- L060 (every name-form — the removal-side sibling)

---

### L057 — Identical code + different behavior ⇒ runtime cause; instrument and gather runtime data first

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Upstream-suite intake, incidents 2026-06 → 2026-08 (Standard Set Version v1.5)

#### Incident

A behavior regression was believed to have appeared "after" a recent change. The audit compared the
implicated code path between the two versions and found it byte-identical — static analysis could
not explain a behavior change because there was no code change. The cause was a runtime condition (a
time source that stops advancing when input stops arriving), invisible to any diff. The fix came from
adding state-transition logging and gathering live evidence across the failure boundary, then
changing the time source — confirmed from live logs.

#### Diagnosis

Identical code with different behavior means the cause is environmental or runtime — clocks, external
state, data feeds, timing — a place a diff structurally cannot see. More static re-reading spends
time proving nothing.

#### Codification

When a behavior change cannot be explained by a code diff, stop static analysis: add instrumentation,
capture runtime evidence across the failure boundary, and only then change code.

#### Cross-references

- L032 (investigate the underlying data — this is its runtime-shaped case)
- L064 (validate on the real runtime — the prevention-side sibling)

---

### L056 — The Phase-3 implementer reconciles the plan against the live source before editing

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** § 15 plan workflow hardening (Phase 3 discipline)

#### Incident

A plan that had passed its mandatory senior-review-and-optimize pass (Rule 13) still reached implementation carrying four genuine defects: a pair of contradictory steps, a missing version bump required by a documented invariant, a reference to a file that did not exist, and an ALLOWLIST too narrow for one of its own transformation rules. None was caught until the implementing session read the plan back against the live source tree before editing. Later plans repeated the pattern: each implementation phase surfaced named plan-defects the drafting-side review had missed.

#### Diagnosis

The Rule 13 pass hardens the plan *as drafted*, against the source *as it was at drafting time*. Between drafting and implementation the source moves, and the drafting agent's blind spots ship with the plan. The implementing session is the only party that sees the plan and the live source side by side — if it starts editing on trust, drafting-side defects become silent implementation drift; if it reconciles first, they become cheap, named findings.

#### Codification

The Phase-3 implementer's first act — before any edit — is a reconcile pass: verify the plan's embedded code, its ALLOWLIST, and its file/line anchors against the live source, and surface every mismatch to the operator as a named plan-defect (D1, D2, …) rather than silently absorbing or fixing it. This is the backstop to the Rule 13 pass, not a replacement for it: Rule 13 catches defects at drafting time when they are cheapest; the reconcile pass catches what drafting could not see.

#### Cross-references

- `CLAUDE.md` § 15.3 (the two-session split — reconcile-first duty) + § 3 Rule 13
- `LESSONS.md` L049 (the senior-review pass), L051 (mechanical tool runs)

---

### L055 — Recorded push-state must be reconciled against the real remote and flipped in the same wrap-up as the push

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** register hygiene (session open/close discipline)

#### Incident

A session opened by investigating a discrepancy: the local-only open-tasks register said two closed plans were "unpushed / push held" when both had long been pushed (verified against the real remote via `git ls-remote`). Root cause: the session that pushed had edited the register minutes after the push — but never flipped the push-state line. The stale line survived several sessions and eventually cost an investigation to untangle.

#### Diagnosis

Push-state is recorded in two places with different truth semantics: committed tracker files freeze their state at commit time (immutable history — a "push held" in a committed tracker is expected, not drift), while the local register claims to be current. A register line is only as fresh as the last hand that touched it, and nothing forced the pushing session to touch it. Meanwhile the local `origin/<branch>` ref is a cache — trusting it (or the register) without querying the real remote reproduces the stale answer.

#### Codification

Two forcing functions, at the two ends of the failure: (1) **session open** — when the register or a tracker records a push-state, reconcile it against the *real* remote (`git ls-remote origin <branch>`), not the local remote-tracking cache, before trusting it; (2) **session close** — if a `git push` happened during the session, flip the matching register push-state line(s) in the same wrap-up. Committed trackers are left frozen; only the live register is reconciled.

#### Cross-references

- `SESSION_OPENER.md` § 1.1 (reconcile before trusting) + `SESSION_CLOSER.md` § 1.4 / § 2.1 (flip on wrap-up)
- `LESSONS.md` L046 (the local-only register)

---

### L054 — The Phase-3 ALLOWLIST must enumerate the plan file and sibling tracker promotion rows

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** § 15 plan drafting (ALLOWLIST completeness)

#### Incident

Two consecutive plans enumerated only their code and doc files in the Phase-3 ALLOWLIST and omitted the plan file and its sibling tracker — even though promoting both to v1.0 / CLOSED in the same commit is mandated by the plan workflow itself. Each implementation commit therefore legitimately touched N+2 files against an ALLOWLIST that said N, forcing the implementer to reconcile the mismatch every time. A later plan that included the two promotion rows shipped with ALLOWLIST count = `git status` count, no reconciliation needed.

#### Diagnosis

The ALLOWLIST discipline works because the enumerated count IS the expected `git status` count (L038) — any mismatch is a stop-and-investigate signal. An ALLOWLIST that structurally undercounts by two trains the implementer to expect and wave through mismatches, eroding the very signal the discipline exists to produce.

#### Codification

Every § 15 plan's Phase-3 ALLOWLIST includes the plan file and its sibling tracker (if any) as explicit same-commit promotion rows, so the enumerated count matches `git status` exactly. The workflow's § 15.2 Phase-1 deliverable states this requirement.

#### Cross-references

- `CLAUDE.md` § 15.2 (Phase 1 deliverable) + § 15.5 / § 15.7 (same-commit promotion)
- `LESSONS.md` L038 (the enumeration IS the count)

---

### L053 — Bootstrap delivery docs are a parity set — a procedure change updates all of them in the same pass

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** suite maintenance (delivery-doc discipline)

#### Incident

The suite's delivery docs — the one-shot bootstrap installer, the long-form walkthrough, and a rollout prompt — drifted apart: the walkthrough sat two Set Versions behind the installer, and adding a new file to the suite silently broke the installer's strip-step set-cover (it enumerated 17 of 18 files). Three separate catch-up commits in one session were needed to restore consistency.

#### Diagnosis

Each delivery doc restates the same bootstrap procedure for a different consumption mode, so any change to the procedure — or to the suite's file inventory — invalidates all of them at once. Updated one-at-a-time on attention, they drift; the drift is silent because no gate compares them.

#### Codification

The delivery docs are a **parity set**: a change to the bootstrap procedure, the suite's file inventory, or the released Set Version updates every member in the same pass. Two sub-rules: (a) **catch-up is installer-only** — bringing a delivery doc up to an *already-released* Set Version bumps the file and the manifest only, never the Set Version, and leaves the set index untouched (it bumps only at releases); (b) **inventory changes propagate** — adding or removing a suite file updates the lay-down list and the strip set-cover in the same commit.

#### Cross-references

- `STANDARDS_INDEX.md` § 5 (bump policy)
- `SETUP.md` / `NEW_PROJECT_BOOTSTRAP.md` (the parity set)

---

### L052 — An installer must create every file it references, not just account for it

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** suite delivery (bootstrap installer)

#### Incident

The first real project bootstrapped with the one-shot installer came up without its local-only open-tasks register: the installer's gitignore step listed the file, but no step created it. The gap surfaced only when the adopting project's first session went looking for the register.

#### Diagnosis

Referencing a file (gitignoring it, describing it, pointing a session routine at it) is not creating it. The gap was silent because the file is optional-by-design downstream — the session pre-flight reads it "if present," so its absence looks like a project with no open tasks rather than a broken bootstrap. Any file an installer references but does not create is a latent per-adoption defect.

#### Codification

A bootstrap installer must CREATE every file it references — seed it with the standard header and an empty-state placeholder — and the delivery docs' step lists are audited so every referenced artifact has a creating step. (Applies to any suite-delivery installer, not just this one.)

#### Cross-references

- `SETUP.md` / `NEW_PROJECT_BOOTSTRAP.md` (the seed steps)
- `LESSONS.md` L046 (the register the gap orphaned), L053 (the parity set the fix must ride)

---

### L051 — The senior-review pass must mechanically run the linters / type-checker / tests against the plan's embedded code, not eyeball it

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Operator-driven lesson codification (Rule 13 reinforcement)

#### Incident

Three consecutive plans that embedded runnable code in their transformation-rules section (§ 5) shipped the same class of defect — over-length lines (a linter rule) that the mandatory senior-review-and-optimize pass (Rule 13) claimed to have checked. In each case the plan's CHANGE LOG asserted the review had run the linter and "caught and fixed" the offending lines; in each case the implementation phase then found over-length lines still present in the exact code the plan committed — and, in the sharpest recurrence, lines that did not match what the CHANGE LOG said it had fixed. The review had been performed by reading the code, not by running the tools against it, and the inaccurate "ran it" claim went unverified.

#### Diagnosis

A review that is *recorded as* mechanically run but is actually eyeballed gives false confidence: the artifact (a CHANGE LOG line saying "ran the linter") is present, so the gate looks satisfied, while the defect it was meant to catch sails through to implementation. The forcing function (Rule 13) existed, but nothing tied its recorded result to an actual tool invocation against the *exact* code the plan ships. Detecting style/lint violations by reading is precisely the task automated linters and type-checkers do reliably and humans do poorly — so a "by eye" review of that class of defect is structurally unreliable.

#### Codification

The Rule 13 senior-review pass MUST mechanically run the linter + type-checker + the tests against the EXACT embedded code the plan commits (not a paraphrase, not a mental model of it); any fix MUST be reflected in the plan's code section itself, not merely narrated in the CHANGE LOG; and the recorded result MUST name the specific lines / checks it fixed — or explicitly state that the tools could not be run, and why. A "ran the tools" claim with no named findings is treated as not-run.

#### Recurrence #4 — the tools must run at the final indentation the code ships at (Set v1.4)

A fourth recurrence sharpened the practice: a plan's senior-review pass DID materialize the embedded code and mechanically run the linter / type-checker / tests (per this lesson) — and the implementation phase still hit one over-length line. The reviewed snippet was clean as drafted, but exceeded the limit once placed at its final indentation inside an enclosing block. **Sharpening:** the tools must run against the embedded code *at the exact indentation and nesting it ships at* — materialize it in its real position in the tree (final enclosing blocks included), not as an unindented draft snippet.

#### Cross-references

- `CLAUDE.md` § 3 Rule 13 + § 15.8 (the senior-review-and-optimize pass)
- `SESSION_OPENER.md` § 3.1 (catalog row)

---

### L050 — Project memory must live inside the synced repo, not the machine-local harness dir

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Operator-driven binding rule addition (Rule 14)

#### Incident

A new session's pre-flight found the project's entire agent memory empty — no index file, no per-fact files — though prior sessions had written several. Investigation: the coding agent's memory lived in a machine-local directory under the user's home, keyed by the project folder's absolute path — not inside the project folder. So the cloud sync that carried the repo never carried the memory; and because the project folder had been renamed/moved more than once and the development machine had been replaced, the path-keyed memory directory was orphaned and the old home directory was gone. Both failure modes hit at once; nothing survived in the live location, and the session transcripts only referenced the memory slugs (no write calls from which to recover content).

#### Diagnosis

Durable knowledge was kept in a location that was neither version-controlled nor cloud-synced, and whose path was unstable under renames. The project's own governance philosophy — "if it's worth keeping, commit/sync it" (Rule 1) — had a gap: agent memory sat outside the synced unit, invisible to both the cloud sync and git.

#### Codification

Rule 14: the memory store lives inside the repo (rides the same sync as the repo; stable under rename), with the agent's memory directory symlinked to it; a bootstrap script re-establishes the symlink per machine / after a move; the session-start pre-flight (`SESSION_OPENER.md` § 1.5) verifies + self-heals + halts-on-empty as the forcing function. Lost content is recoverable only from a synced/backup copy of the prior machine's home directory, or by reconstruction from committed/synced project docs.

#### Generalization — all project data, not just memory (Set v1.5)

An upstream project independently re-discovered this failure class at larger scope: its entire
per-project store — memory AND all session transcripts — lived only under the harness's
machine-local, absolute-path-keyed directory, invisible to every folder-level backup. The rule is
therefore generalized from "the memory store" to **all machine-local project data** (Rule 14 as of
Set v1.5): physical home `<repo>/.claude/project-data/`, symlink at the harness path, managed by
`scripts/claude_project_data.sh` (`status`/`adopt`/`link`), verified at session open AND close.
Anything that genuinely cannot live in the folder is cataloged in the project's machine-migration
doc, same-commit.

#### Cross-references

- `CLAUDE.md` § 3 Rule 14 (the binding rule)
- `SESSION_OPENER.md` § 1.5 (the forcing function) + § 3.1 (catalog row)
- the memory-bootstrap script (the idempotent repair tool)

---

### L049 — A plan draft is a hypothesis: a mandatory senior-review-and-optimize pass before approval catches what the drafting pass ships

**Date:** 2026-06-07
**Project:** a reference project
**Phase / Task:** Operator-driven binding rule addition (Rule 13 codification — plan-level analogue of Rule 10)

#### Incident

PLAN-012 (force-close before market-stop windows) was drafted across a long multi-turn operator design conversation, then committed as DRAFT. The operator then asked the agent to "act as a very experienced senior developer" and recheck the plan for consistency and code-correctness, optimizing where possible. That review pass — run against the **real EA source** — found defects the drafting pass had shipped even though the plan looked complete and internally plausible:

- a **non-functional market-open check**: the drafted `IsMarketOpenNow` used `SYMBOL_TRADE_MODE` (a static permission flag) to answer "is the market open right now" — which that API cannot do;
- a **backwards panel state**: `ForceCloseStatusText` returned `CLOSING…` when the basket was *empty* (should be `DONE`), with no state for the actual dumping phase;
- **redundant per-tick recomputation**: the force-close trigger was computed 3–4× per tick (gate + two panel rows), risking divergence between what the gate did and what the panel showed;
- a leftover **placeholder ternary**, plus several **cross-section inconsistencies** (panel table vs the R-rule; a risk paragraph referencing the now-removed check).

All were fixed in place and the plan hardened before the operator approved it.

#### Diagnosis

The first drafting pass optimizes for **completeness** — getting every section written — not for **correctness**. It produces code that *looks* right (plausible names, reasonable structure) but hasn't been checked against the real source or stress-tested, and cross-section drift accumulates as the draft grows. Without a dedicated adversarial re-read, those defects survive into operator approval and into the Phase 3 implementer's prompt — exactly where they are most expensive to find.

This is the plan-level analogue of L027 / Rule 10 (code review before commit): the artifact must be hardened by a separate review pass at the same granularity as the failure. For commits that's per-commit (Rule 10); for plans it's per-plan, at finalization (Rule 13).

#### Resolution

New binding **Rule 13** in CLAUDE.md § 3 + new **§ 15.8** with the canonical review prompt. The pass is the **last task of plan development** — run once on the complete plan (and sibling tracker), immediately before Phase 2 approval — and it APPLIES fixes directly, records what it changed in the plan's CHANGE LOG, and surfaces any newly-exposed design decision to the operator rather than deciding silently. Companion `docs/SESSION_OPENER.md` § 3.1 row + memory `[[feedback_senior_review_pass]]`.

#### Pattern

A draft is a hypothesis. Any artifact that will be approved by a human or consumed by a downstream implementer must pass a dedicated correctness-and-consistency review, run against ground truth (the real source), at the moment it is finalized — never assumed correct because it reads well.

---

### L048 — Session wrap-up routine as forcing function against detail loss across session boundaries

**Date:** 2026-05-23
**Project:** a reference project (cross-project pattern)
**Phase / Task:** Operator-driven binding rule addition (Rule 12 codification — symmetric counterpart to Rule 9 / SESSION_OPENER)

#### Incident

During the 2026-05-22/23 multi-day session (which produced 7 commits + 4 plan drafts + multiple standards-suite bumps + scope expansions across PLAN-005/PLAN-006/PLAN-007 + a new investigation task), the operator observed that without a structured session-end routine, important details risked being forgotten by farewell time:

- New rules established mid-session (Rule 10, Rule 11, scope expansions) need codification — but momentum can carry the session past the codification step.
- New lessons (L044, L045, L046, L047) surfaced organically but each required deliberate codification work — easy to skip if the operator says "wrap up" without a routine.
- `OPEN_TASKS.md` accumulates new items throughout a session (PLAN-008 placeholder, PLAN-009 placeholder, modularization investigation task, PLAN-005 scope expansion) — easy to drift if not cataloged at session-end.
- `/tmp/` artifacts (commit_msg files, transcript scans) accumulate across the session — easy to leave behind.
- Memory updates (`feedback_*.md` / `project_*.md` additions) may not get the matching MEMORY.md index update without a deliberate review.

Pattern is symmetric to L043 (SESSION_OPENER / Rule 9): same root cause (relying on agent recall without a forcing function), same fix (forcing function = binding routine at the session boundary).

#### Cost

- Detail loss between sessions = lost insights, lost rule candidates, lost convention discoveries.
- Stale `OPEN_TASKS.md` = next session starts with an incomplete picture.
- `/tmp/` accumulation = ambient clutter; commit_msg.txt files can carry stale text into next session if the agent reuses the path without overwriting.
- Trust erosion = operator has to manually re-establish session state at start of next session because end-state wasn't captured.

#### Diagnosis

The operator-driven memory + SESSION_OPENER § 3 catalogs are session-START forcing functions. They fire when a new session opens. But there's no symmetric session-END forcing function.

Without one, session-end behavior depends on agent recall — agent remembers to summarize, agent remembers to clean `/tmp/`, agent remembers to scan for lessons. This is exactly the failure mode L043 identified for session-START — and it has the same fix at session-END.

The meta-rule from L044 applies again: **forcing-function cadence must match failure cadence.** Session-end failures (detail loss, stale catalogs) need session-end forcing functions. The same structural argument that motivated Rule 9 (SESSION_OPENER as pre-flight) applies here: Rule 12 (SESSION_CLOSER as post-flight).

#### Codification

New binding standards file: `SESSION_CLOSER.md` v1.0 (template at `docs/standards/SESSION_CLOSER.md`; project-local at `docs/SESSION_CLOSER.md`). New Rule 12 in `CLAUDE.md` template: "Session wrap-up routine on operator command is MANDATORY."

**Trigger keywords:** `"wrap up"` / `"wrap"` / `"end session"` / `"close out"` (context-disambiguated from `Closeout_Mode` in EA-domain projects) / `"end of session"` / `"finish up"`.

**Routine has 9 mandatory steps** (`SESSION_CLOSER.md` § 1):

1. Repo state — `git status --short`, unpushed commits, session commits
2. Project + standards versions — live-artifact version, snapshots/tags, Standards Set Version
3. Pending operator decisions — DRAFT plans, blocked tasks, awaiting-approval scenarios, cross-project propagation prompts
4. Outstanding `OPEN_TASKS.md` (if present)
5. Memory updates landed this session
6. `/tmp/` cleanup
7. **Lessons-learned scan** — review session for candidates (new rules, lessons, memory entries, SESSION_OPENER rows, scope expansions, conventions). Each candidate gets a codify / queue / discard recommendation.
8. Next-up suggestion
9. Confirm done

A **first-response output template** (`SESSION_CLOSER.md` § 4) is the visible proof-of-wrap-up: until that block is posted, the session is not closed.

The file also carries the **wrap-up failure-mode catalog** (§ 2) — symmetric to SESSION_OPENER § 3. Every wrap-up miss pattern adds a row pairing 1:1 with a memory.

Set Version v2.4 → v2.5 (Major) — adopter migration required: copy `SESSION_CLOSER.md` template into project as `docs/SESSION_CLOSER.md`, customize §§ 2 + 4 output-block specifics, add Rule 12 to repo-root `CLAUDE.md` per template `CLAUDE.md` § 3.

#### Cross-references

- `CLAUDE.md` template § 3 Rule 12 (the binding mechanism)
- `SESSION_CLOSER.md` (the wrap-up routine itself)
- `STANDARDS_INDEX.md` § 6 v2.5 history entry (the Set Version bump migration steps)
- L043 — symmetric session-START forcing function (SESSION_OPENER / Rule 9); L048 mirrors the pattern at session-END
- L044 — meta-rule "forcing-function cadence must match failure cadence" (this lesson is another application — session-end failures need session-end forcing functions)
- L046 — Local-only OPEN_TASKS.md register (the catalog that gets surfaced in routine step 1.4 and updated with lesson candidates in step 1.7)

#### Pattern recognition rule

**Every session boundary needs a forcing function.** L043 codified the start-boundary (SESSION_OPENER, Rule 9). L048 codifies the end-boundary (SESSION_CLOSER, Rule 12). The pattern generalizes: any high-stakes transition deserves a structured routine that fires at the transition moment. Mid-session transitions (e.g., between commits) get Rule 10 (code review). Session-start transitions get Rule 9. Session-end transitions get Rule 12. The shape repeats: binding rule → forcing-function file → routine → output-block proof → failure-mode catalog → maintenance discipline.

When a future analogous boundary surfaces (e.g., end-of-week sync, end-of-quarter audit), follow the same shape.

---

### L047 — QA / smoke-test scenarios must be coupled to changes at change-time, not validation-time

**Date:** 2026-05-22
**Project:** a reference project (cross-project pattern)
**Phase / Task:** Operator-driven binding rule addition (Rule 11 codification)

#### Incident

Across PLAN-001..PLAN-004, the QA / smoke-test scenarios for each plan's Phase 4 were defined at **plan-design time** (Phase 1) and held in the plan file's § 8 ("Validation gate including demo smoke test") — e.g., PLAN-003 had its own scenario list; PLAN-004's § 8 enumerated scenarios A–J. Each list was the operator's best guess at design time about what would need verifying.

The link from **"the code change was made"** → **"is the scenario list complete?"** was implicit. Three concrete failure modes surfaced:

1. **Mid-plan changes can ship without paired scenarios.** When Phase 3 expanded to multiple sub-commits (e.g., PLAN-001's Task 2.5b fix-forward, PLAN-001 § 11 risk #2 mitigation), there was no forcing function to add new scenarios for the new sub-changes. The original scenario list, written at design time, didn't always cover what mid-flight additions changed.

2. **Minor changes outside a § 15 plan get no scenarios at all.** Bug fixes, doc-driven behavior tweaks, or operator-requested small changes ship without any verification scenario captured anywhere. The change is committed, the verification (if it happens) is ad-hoc in chat, and no permanent record links the change to its verification.

3. **Scenario lists become stale.** A scenario defined at Phase 1 may no longer match what the Phase 3 implementation actually does, especially if the design drifted during implementation (despite Rule 7 / § 15.3 verbatim-block discipline, edges still drift). Without a per-change update, the scenario list grows out of sync with the code.

#### Cost

- Verification gaps: changes ship without operator-visible scenarios; ad-hoc verification fills the gap inconsistently
- Tracker drift: the plan's § 4 phase tracker (per L045) records what was done but not what was verified
- Lower confidence in shipped behavior: "did we test that?" becomes a memory question rather than a tracker lookup
- Latent risk: a defect introduced by a mid-plan sub-commit can ship undetected if its scenario was never added

#### Diagnosis

The verification discipline existed (operator-driven Phase 4 smoke tests) but was anchored at the wrong granularity:

- **Plan-design-time scenarios** (Phase 1 / § 8 of plan file) — captured the operator's best guess at design time; could not anticipate mid-flight changes
- **Pre-push governance** (Rule 2) — validates mechanical sync (doc coverage, ownership drift), not behavioral verification
- **Pre-push validation checklist** (§ 8 step 4 "Testing") — said "if behavior affects outputs, validators run for the affected scope," but the *scenarios* themselves had no per-change forcing function

Same meta-lesson as L044: **forcing-function cadence must match failure cadence.** Per-change failure modes (a sub-commit ships without verification) need per-change forcing functions (the QA scenario is added in the same commit as the change). Plan-design-time scenarios fire once per plan-draft, not per-change — they can't catch a mid-plan change that ships without a paired scenario.

The fix is to embed the rule in the per-commit procedure, parallel to Rule 10's per-commit code-review pattern. The rule's structural shape: "no change ships without a paired scenario in the tracker, same-commit."

#### Codification

New **Rule 11** in `CLAUDE.md` § 3 — "QA / smoke-test scenario for every change."

**Coupling rule:** every behavior-affecting change MUST be paired with a written QA scenario, added **same-commit as the change**, to:

- The plan's sibling tracker (`docs/Plans/PLAN-NNN_tracker.md`) for big plans per § 15.7
- The plan's in-file § 4 Phase 4 checklist for small plans per § 15.7
- `docs/Plans/OPEN_TASKS.md` "Pending verification" section + CHANGELOG entry "QA scenarios" sub-section for Minor changes outside a § 15 plan

**Scenario shape:** (1) what to verify; (2) how to verify (runtime steps); (3) expected pass criteria (observable outcome).

**Status markers:** ⏸ pending / ✅ passed / ❌ failed / ⏭ skipped (with annotation).

**Lifecycle:** scenario added same-commit as change (⏸). After operator verification on the runtime platform demo / backtest → status ✅. ✅ scenarios removed from `OPEN_TASKS.md` (per L046); preserved in per-plan tracker (per L045) and CHANGELOG QA-scenarios sub-section.

**Exemptions:** pure doc cleanup, lessons-archive additions, manifest version bumps, standards-suite refresh, governance-doc edits with no behavior impact — these do not require scenarios. The exemption is structural (no observable runtime behavior changed) not discretionary.

#### Cross-references

- `CLAUDE.md` § 3 Rule 11 — primary binding location
- `CLAUDE.md` § 8 step 4 "Testing" — Rule 11 enforces the "test plan exists" requirement at change-time
- `CLAUDE.md` § 15.7 — QA scenarios become Phase 4 sub-tasks in plan trackers
- L044 — meta-rule "forcing-function cadence must match failure cadence" (this lesson is a specific application)
- L045 — Plan tracker discipline (defines where the tracker lives)
- L046 — Local-only OPEN_TASKS.md register (defines where non-plan QA items go)
- `SESSION_OPENER.md` § 3.1 row 13 — failure mode row for "change without paired QA scenario"

#### Pattern recognition rule

**Verification artifacts are most valuable when attached to changes, not to plans.** A plan-level scenario list is helpful but insufficient — by the time the plan is finished, the list may not match what was actually built. A change-level scenario, attached same-commit as the change itself, stays in lockstep with the code by mechanical necessity (you can't ship the change without also touching the tracker). The same structural argument that motivated Rule 10 (code review embedded in commit procedure rather than session-start checklist) applies here: per-commit (or per-change) failure modes need per-commit forcing functions.

---

### L046 — Local-only OPEN_TASKS.md register: cross-plan + non-plan "what's open right now" index

**Date:** 2026-05-22
**Project:** a reference project (cross-project pattern)
**Phase / Task:** Operator-driven binding rule addition during PLAN-004 close-out

#### Incident

With multiple plans in different stages (some CLOSED, some in-flight, some idea-only — e.g., PLAN-001..PLAN-004 across various states + a future PLAN-005 captured only as a memory note) plus operator-driven one-off tasks not belonging to any plan + maintenance items, no single artifact aggregated "what's open right now" across all sources. The existing artifacts each captured a slice — per-plan trackers held intra-plan sub-tasks (per L045), CHANGELOG held completed work, plan files held design state — but none aggregated *across* plans + non-plan + future-plan placeholders. Every session start required re-checking each source, and items in the "future PLAN to draft" category had no home at all until the plan file was created.

Surfaced during the same 2026-05-22 conversation that codified L045: the operator asked for "a global remaining task document and each task that has been done will be deleted from the list," explicitly including tasks that don't belong to any plan yet.

#### Cost

- Friction at session start re-checking N sources for open work
- Latent risk: items in the "future-plan placeholder" category had no formal home and could be forgotten between sessions
- Lower visibility into the operator's overall workload across all plans simultaneously

#### Codification

New convention added to the standards suite: a local-only `docs/Plans/OPEN_TASKS.md` register that aggregates open tasks across all sources.

**Key properties of the convention:**

1. **Local-only / gitignored.** Lives in `docs/Plans/OPEN_TASKS.md` but is excluded by `.gitignore`. Not shared across machines or other contributors by design — it is the operator's personal workspace queue, not a shared repo artifact. Other agent sessions on the same machine see it; fresh clones / other environments simply do not.
2. **Aggregates across plans + non-plan work.** Sections (recommended seed shape): `Active plans — open items` (one sub-section per mid-execution plan) / `Plans in drafting / future` (idea placeholders before plan files exist) / `Operator-driven (no plan)` / `Maintenance / housekeeping`.
3. **Lifecycle: done = deleted.** When a task closes, its line is DELETED from the file (same commit as the work that closed it, where applicable). No "✅ completed but not removed" intermediate state. History lives in the per-plan tracker (per L045) or CHANGELOG (for non-plan items). OPEN_TASKS is current state only.
4. **Authoritativeness:** when OPEN_TASKS.md and a per-plan tracker disagree, the per-plan tracker wins. OPEN_TASKS is an index, not the source of truth.
5. **Session pre-flight reads it if present.** The session-start pre-flight (per L043) reads top of the file IF PRESENT (skip gracefully if absent — fresh clones / other machines will not have it).

**Why local-only:** cross-machine drift on an "open queue" file would be more harmful than helpful. The operator's personal workspace queue does not need to be shared; trying to share it (via git) would create merge-conflict friction at exactly the worst moments (mid-execution, mid-session). Keeping it gitignored eliminates that entire failure mode.

#### Cross-references

- `CLAUDE.md` § 15.7 — companion section that codifies the per-plan tracker discipline (L045). The two rules compose: per-plan tracker is the source of truth for one plan's sub-tasks; OPEN_TASKS is the cross-plan + non-plan index.
- `SESSION_OPENER.md` § 1.3 — the session-start pre-flight reads OPEN_TASKS.md if present (one of the "tracker sources to check in priority order")
- `SESSION_OPENER.md` § 3.1 row 12 — failure mode: register goes stale or unmaintained
- `.gitignore` — `docs/Plans/OPEN_TASKS.md` exclusion entry
- Related: L042 (plan workflow itself); L045 (per-plan tracker discipline); L008 (manifest completeness — gitignored files are *not* tracked in the manifest)

#### Pattern recognition rule

The deeper lesson here: **not every workflow artifact needs to be shared.** When an artifact's primary value is to one specific contributor on one specific machine (an operator's personal queue, an in-progress scratch file, a debugging hypothesis list), pushing it into git creates more friction than visibility. Gitignored-by-design is the right answer for these. The signal that something belongs in this category: ask "would another contributor on a fresh clone be confused or harmed if this file appeared in their working tree?" If yes, it should be local-only.

---

### L045 — Plan tracker discipline: big plans get a sibling tracker, small plans expand § 4 in-file

**Date:** 2026-05-22
**Project:** a reference project (cross-project pattern)
**Phase / Task:** Operator-driven binding rule addition during PLAN-004 close-out

#### Incident

Across PLAN-001 (multi-task Phase 3 with sub-commits like Task 2.5 / 3.1 / 3.2) and PLAN-004 (10 smoke-test scenarios A–J in Phase 4), the high-level § 4 phase block of each plan file proved too coarse to track sub-task progress across commits and sessions. The default § 4 ("Phases 0–5 with one-line description each") captured the overall workflow shape but not the granular state — "which sub-tasks of Phase 3 are done?" / "which smoke-test scenarios passed?" was scattered across commit messages, memory entries, and the operator's working memory.

Concrete surfacing event same day: the [[plan-004-pending]] memory entry still said "compile-verify + smoke test + push pending" hours after the push had completed — exactly the kind of drift a granular tracker would have caught. The operator flagged "memory drift on push status; would have been caught by a tracker checklist."

Plans of different sizes had different needs: a small plan (Phase 3 = 1 commit, Phase 4 = compile-clean) doesn't justify a separate tracker file, but it still needs sub-task visibility. A big plan (multi-commit Phase 3, multi-scenario Phase 4, or work spanning multiple sessions) needs more space than the in-file § 4 reasonably accommodates.

#### Cost

- Memory drift incidents (recoverable with manual cleanup; this incident was caught and fixed in same session, but the pattern is unbounded — any future drift could go unnoticed longer)
- Friction at session continuation: "what's the actual sub-task status of Phase 3?" requires re-reading commits and memory rather than glancing at a checklist
- Latent risk of sub-task amnesia mid-flight in larger plans (e.g., one of 10 smoke-test scenarios silently skipped)

#### Codification

New `CLAUDE.md` § 15.7 — "Tracker requirement for plans." Every plan that hits the § 15 plan workflow carries a granular sub-task tracker somewhere. The location depends on size:

**Big-plan rule (sibling tracker file).** A plan requires a sibling `docs/Plans/PLAN-NNN_tracker.md` (`Owner: <agent-name>` per `CLAUDE.md` § 14.4 in multi-agent projects; omit in single-agent projects) when ANY of:

1. Phase 3 is expected to land as **>1 commit** (multi-task pattern, e.g., Task 2.5 / 3.1 / 3.2 sub-commits).
2. Phase 4 has a **multi-scenario validation list** (e.g., smoke-test scenarios A–J).
3. The plan is expected to **span more than one agent session**.

Operator may also declare a tracker required for any plan at Phase 1 (Design) or Phase 2 (Approval) as a safety valve, even if conditions 1–3 don't trigger.

**Small-plan rule (in-file § 4 expansion).** Plans that do NOT trigger the sibling-tracker conditions still need granular sub-task tracking. The tracker lives **inside the plan file itself**, in its § 4 "Phase tracker" — expanded from the default one-line-per-phase summary into a checklist:

- Phase 0 (Audit) / Phase 1 (Design) / Phase 2 (Operator approval) — single ✅ / ⏸ marker with date (and approval-string for Phase 2).
- Phase 3 (Implement) — each file edit OR each verbatim-transformation sub-step (per the plan's § 5) as ✅ / ⏸ with date.
- Phase 4 (Validate) — each verify check (compile clean / scenario 1 / scenario 2 / ...) as ✅ / ⏸ with date.
- Phase 5 (Operator gate) — push + tag (each as ✅ / ⏸ with date).

**Both layouts share:** updated same-commit as the work it tracks; promoted to v1.0 / CLOSED with the plan; the rule has no escape hatch — every § 15 plan, big or small, carries a granular tracker somewhere.

**Migration path if a small plan grows mid-flight:** if a plan was started small (in-file § 4 tracker) and later trips one of the big-plan conditions (Phase 3 expands to >1 commit, multi-scenario verify emerges, work spills into a new session), promote it — create the sibling `PLAN-NNN_tracker.md` in the first commit where the trigger becomes true, back-fill prior phases' status from § 4, and collapse § 4 back to its high-level summary in the same commit.

#### Cross-references

- `CLAUDE.md` § 15.7 — primary enforcement location (big + small rules + migration path + companion safety-valve)
- `SESSION_OPENER.md` § 3.1 row 11 — failure mode: "starting a § 15 plan without granular sub-task tracking"
- `SESSION_OPENER.md` § 1.3 — pre-flight reads the per-plan tracker if work continues a multi-task / multi-scenario plan
- Related: L042 (plan workflow itself — L045 fills a gap inside it); L001 (Plans folder rule); L008 (manifest completeness — sibling trackers register in manifest like other tracked docs); L046 (local-only OPEN_TASKS.md register — the cross-plan + non-plan companion to per-plan trackers)

#### Pattern recognition rule

The deeper lesson: **the optimal tracker location depends on the work's blast-radius profile.** Big work (multi-commit, multi-session, multi-scenario) needs a dedicated file so the checklist has room to breathe and survives across sessions. Small work (one-commit, one-session, one-verify) needs the checklist co-located with the design so the two stay in sync mechanically. Forcing all work into the same shape (always a sibling file, OR always in-file) creates either ceremony for trivial work or cramped tracking for substantial work. Symmetric, size-driven rules are the right answer.

---

### L044 — Session-scoped checklists don't enforce per-commit discipline; embed the rule in the procedure

**Date:** 2026-05-22
**Project:** a reference project
**Phase / Task:** Operator-driven binding rule addition (code-review-before-commit elevated to CLAUDE.md Rule 10)

#### Incident

Within the same session that codified Rule 9 / SESSION_OPENER.md (driven by L043), the code-review-before-commit discipline — encoded as memory `feedback_code_review_before_commit` since 2026-05-02 (L027) and listed in SESSION_OPENER § 3 row 3 — was applied unevenly across two consecutive commits:

1. **Commit `4b86b4a` (Phase 7 / Task 7.6 closure):** Agent produced an explicit named code-review table in operator-visible chat before `git add`. Table listed each modified file with a one-line verdict. Operator approved; commit landed cleanly with full review artifact in the chat transcript.

2. **Commit `4110ca8` (Phase 7 / 7.1 + 7.2 tracker drift fix):** Same session, ~one turn later. Agent went `edits → governance scripts → "Stage and commit drift fix"` with no review step. No review table appeared in chat. The commit landed without the quality gate that the prior commit had received.

Operator caught the asymmetry post-commit by asking "have you done code review before commit?" Agent acknowledged the lapse, performed a post-hoc review on the already-committed change (no defects found, fortunately), and reinforced the rule via memory update.

#### Cost

- Trust impact: ~5–10 minutes back-and-forth to acknowledge the lapse and reinforce the discipline going forward
- Asymmetry of quality gates across consecutive commits in the same session — visible to anyone reviewing the chat transcript
- Structural exposure: had the drift-fix commit shipped a real defect, the lapse would have been more than procedural
- Bigger picture: the failure exposed a structural weakness in how the rule was anchored at the time — see Diagnosis

#### Diagnosis

Two prior forcing functions existed for the code-review rule:

1. **Memory** (`feedback_code_review_before_commit.md`, set 2026-05-02 / L027) — agent recalls when "relevant"
2. **SESSION_OPENER § 3 row 3** — listed in the mistake-avoidance checklist surfaced at session start

Both are **session-scoped**: they fire once at session start, then go dormant. By the time the third commit in a session lands, the checklist has not been re-invoked; the rule's salience has decayed; small commits feel "trivial" and the discipline lapses without surfacing in the chat transcript at all (because the missing artifact is not displayed — it's absent).

This is parallel to L043's meta-lesson ("any pattern surfaced more than once is a candidate for a forcing function, not just a memory entry") — but with an additional layer specific to commit-time discipline:

> **A forcing function is only as strong as its invocation cadence matches the discipline it's enforcing.**

L043's SESSION_OPENER fires at session start because the failures it prevents (host confusion, missed test sync) typically trace to context not loaded at start of session. L044's Rule 10 must fire **per commit** because the failure it prevents (silent code-review skip) happens at each commit-time, not at session start. Memory + session-start checklists alone don't bridge that gap; the rule must be embedded in the per-commit procedure itself.

The right granularity question to ask when elevating a memory to a forcing function:

- Session-scoped failure → SESSION_OPENER row
- Per-commit failure → CLAUDE.md rule embedded in commit procedure
- Per-file-edit failure → file-level mechanism (e.g., VERSION header convention)

The forcing function must fire at the same granularity as the failure.

#### Codification

1. New **Rule 10** in `CLAUDE.md` § 3 — "Code review before commit is MANDATORY (binding, no exceptions)." The rule is framed PROCEDURALLY: "the commit pattern is `edits → governance → named review table → 'go on commit?' → commit`." Skipping the review isn't "forgot the rule," it's "broke the pattern." This converts the rule from a normative reminder (which decays) into a load-bearing step of a sequence (which is structurally visible if skipped — the chat transcript shows what step was performed and what wasn't).
2. § 3 heading drift fix: "The 9 standing rules" → "The 10 standing rules" (prior v2.1 merge added Rule 9 without updating the heading count; now reconciled in same commit).
3. § 13 sources-of-truth bullet updated to "The 10 standing rules."
4. `SESSION_OPENER.md` template § 3.1 row 3 (code-review-skipped) updated to cross-reference the new CLAUDE.md Rule 10 in addition to the existing L027 reference.
5. Set Version bumped v2.1 → v2.2 (Minor — additive new sub-section in existing binding file per `STANDARDS_INDEX.md` § 5.1).

#### Cross-references

- L027 — original code-review-before-commit lesson (2026-05-02) — Rule 10 is the binding elevation of this lesson's discipline
- L043 — "any pattern surfaced more than once is a candidate for a forcing function, not just a memory entry"
- `CLAUDE.md` § 3 Rule 10 (binding)
- `CLAUDE.md` § 8 step 5 — detailed code-review checklist (referenced by Rule 10)
- `CLAUDE.md` § 11 "Code review before staging" — procedural commit-time policy (now cross-references Rule 10 as binding anchor)
- `SESSION_OPENER.md` template § 3.1 row 3 + project-local § 3.1 row 1 (a reference project's numbering)

#### Meta-lesson (new — beyond L043's "any pattern → forcing function")

**Forcing-function cadence must match failure cadence.** A rule anchored at session start cannot enforce a discipline that lapses per-commit, per-file-edit, or per-operation. When considering whether a current forcing function is adequate, examine: at what granularity does the failure recur, and at what granularity does the forcing function fire?

If they don't match, the rule will continue to drift no matter how prominent the session-start checklist is. The fix is to embed the rule at the matching granularity — which often means embedding it in the *procedure* of the action where the failure occurs, not in the *preface* to the session that contains the action.

This is a refinement on L043, not a replacement: L043's "memory alone isn't enough" stays valid; L044 adds "and even a non-memory forcing function isn't enough if it fires at the wrong granularity."

---

### L043 — Session-start pre-flight as forcing function

**Date:** 2026-05-22
**Project:** a reference project
**Phase / Task:** Operator-driven binding rule addition (mid-Phase-5 EA soak)

#### Incident

A single session produced two repeat-from-known-memory failures within ~30 minutes:

1. **Wrong-server identification.** Operator asked for a check on staging. Agent SSH'd to `app-signal@188.245.172.198` (which is production), ran read-only queries, and confidently reported "staging has no EA active." Operator pushed back twice; agent defended the wrong answer once before re-checking. The correct mapping (`deploy@91.98.91.129` = STAGING; `app-signal@188.245.172.198` = PROD) was already in memory (`project_vps_infra.md`) and also in `.gitlab-ci.yml` (`STAGING_*` / `PRODUCTION_*` variables). The agent had access to both and trusted SSH-config ordering instead. Had the task been a write (a lot edit, profile switch, container restart), the mutation would have landed on production while the agent believed it was staging.

2. **Missed test-assertion sync on a profile param change.** Same session, agent committed `ea_lot_size: 1 → 2` on the active EA profile (`07f4796`) but missed updating a pinned `assert ea["ea_lot_size"] == 1` in `validation/tier1_config/test_strategy_profiles.py`. Governance scripts passed (they validate doc coverage and ownership drift, not assertion pass/fail). The pipeline caught it on the `logic-tests` stage and blocked staging deploy. Required a fix-forward commit (`0b863d4`) per the broken-on-push pattern.

Both failures had a single common root cause: knowledge that would have prevented them was encoded in memory but not loaded at the front of the session. The agent went directly to action.

#### Cost

- ~30 minutes of operator back-and-forth correcting host misidentification + re-checking the correct server
- One pipeline blocked + one fix-forward commit + ~10 minutes of staging-deploy delay for the missed test
- One memory-trust event (operator now has to verify host identification on future remote actions until trust is rebuilt)
- Larger latent cost averted: had the task been a write, the wrong-server mistake would have been a production incident

Aggregate: ~45 minutes lost to repeat failures; one pipeline cycle wasted; trust impact.

#### Codification

New binding standards file: `SESSION_OPENER.md` v1.0. New Rule 9 in `CLAUDE.md` template: "Session start pre-flight is MANDATORY."

The pre-flight has 4 mandatory components (`SESSION_OPENER.md` § 1):

1. **Repo state** — `git log --oneline -3 origin/<main>`, unpushed commits, working tree
2. **Live system state** — staging + production deploy SHAs, live runtime probe, latest CI pipeline
3. **Tracker tip** — top of the relevant tracker (current phase + open task)
4. **Memory recall** — 3–5 memories relevant to the stated task, cited as `[[slug]]`

A **first-response output template** (`SESSION_OPENER.md § 4`) is the visible proof-of-pre-flight: until that block is posted, no edit / SSH / commit / remote query happens.

The file also carries the **canonical environment mapping** (§ 2) and the **project failure-mode catalog** (§ 3) — every row in § 3 pairs 1:1 with a `feedback_<slug>.md` memory, making the failure modes scannable in one place.

Set Version v1.0 → v2.0 (Major) — adopter migration required: copy `SESSION_OPENER.md` template into project as `docs/SESSION_OPENER.md`, customize §§ 2 + 3, add Rule 9 to repo-root `CLAUDE.md`.

#### Cross-references

- `CLAUDE.md` template § 3 Rule 9 (the binding mechanism)
- `SESSION_OPENER.md` (the pre-flight itself)
- `STANDARDS_INDEX.md` § 6 v2.0 history entry (the Set Version bump migration steps)
- `MEMORY_PROTOCOL.md` § 5 verify-before-recommending (the memory-recall component of the pre-flight)
- Related: L032 (investigate when answers are questioned — both failures involved defending wrong answers before investigating); L028 (push cadence — the missed test sync demonstrated that "passes governance" ≠ "ready to push")

#### Pattern recognition rule

The deeper lesson here: **any pattern that's surfaced more than once is a candidate for a forcing function, not a memory entry.** Memory works when there's a forcing function that loads it; without one, memory becomes a write-only buffer. SESSION_OPENER.md is the forcing function for THIS project, but the meta-pattern applies broadly: when a known mistake repeats, the fix is rarely "remember harder" — it's "make it impossible to skip."

---

### L042 — Plan-first for vital changes: full plan + Phase 2 approval + Phase 3 in a fresh session

**Date:** 2026-05-22 (codified after PLAN-001 .. PLAN-004 sequence completed)
**Project:** a reference project (cross-project pattern)
**Phase / Task:** PLAN-001 (Codex migration), PLAN-002 (broker-time-everywhere), PLAN-003 (closeout immediate-close), PLAN-004 (news block module)

#### Incident

Across four consecutive Plans landing changes to the EA's central domain logic (`the application language/Experts/a reference project source file`), the same workflow proved out across all four: a written plan committed to `docs/Plans/` BEFORE any code is touched, an explicit operator-approval decision point inside the plan (Phase 2 — "operator responds with APPROVE D1.A or alternative"), and Phase 3 implementation in a separate Claude session prompted from the plan file as the authoritative spec.

The single-session alternative — drafting the design and implementing it in the same conversation — proved fragile in earlier work: design decisions drift mid-session as new questions surface; the implementer Claude blends old context with new context; the commit log shows the result but not the design conversation that produced it. The split-session pattern fixes all three: the plan IS the design record (committed to git, versioned, manifest-tracked); approval is a discrete artifact (operator response logged in the chat that becomes the next session's starting prompt); the Phase 3 session runs against a frozen plan with no design ambiguity left to resolve.

The pattern crystallized during PLAN-001 (operator requested it explicitly: "draft + execute in separate Claude sessions") and was re-applied verbatim for PLAN-002, PLAN-003, PLAN-004 — four successful executions in four attempts.

#### Cost

The DON'T side of this lesson is hypothetical-but-likely: without the plan-first workflow, the cost would have been silent design drift on changes that affect live trading behavior. The DO side is observable: four consecutive Plans landed clean, with the design intent reconstructible months later by reading the plan file alone.

#### Codification

**Plans folder rule (existing L001):** all plans live in `docs/Plans/`, committed to git, versioned, manifest-tracked.

**Plan-first workflow (new with L042):** for any change classified as a vital-change-to-central-domain-logic (the project's equivalent of editing the central trading engine, the central state machine, the central scheduler, etc.), the workflow is:

1. **Phase 0 — Audit:** verify the relevant code is read; verify external dependencies (APIs, calendar catalogs, etc.) are present; cite all integration points by file:line.
2. **Phase 1 — Design:** § 5 contains verbatim transformation rules per call-site (per CLAUDE.md Rule 7); § 7 the ALLOWLIST; § 8 the validation gate including demo smoke test; § 11 known risks with mitigation per risk.
3. **Phase 2 — Operator approval:** § 9 of the plan contains an explicit decision point ("operator responds with APPROVE D1.A or alternative"). **No code is touched until this approval lands.**
4. **Phase 3 — Implement:** runs in a **fresh agent session** prompted from the plan file. The plan stands alone — the new session does not need to read the conversation history that produced it.
5. **Phase 4 — Validate:** compile / type-check / governance scripts; demo smoke test of all behavior-matrix scenarios.
6. **Phase 5 — Operator gate:** push + tag after smoke test passes.

The two-session split is the load-bearing part. A new Claude session entering Phase 3 with only the plan file as input is forced to discover all the design context from a committed artifact, not from chat scrollback. If anything is ambiguous in the plan, that's a plan defect — surface it to the operator rather than silently fill from prior conversation.

#### Cross-references

- `CLAUDE.md` § 15 plan workflow for vital changes — primary enforcement location
- `CLAUDE.md` Rule 1 — Plans folder
- `PROJECT_STANDARDS.md` § 1 the 5-step change workflow — Major changes always run Analyze → Design → Implement; this lesson refines that flow to "Design lives as a committed plan; Implement runs in a separate session"
- `PROMPT_STANDARDS.md` § 3 Type 1 multi-file prompts — Phase 3 prompts ARE multi-file prompts; ALLOWLIST + verbatim transformation rules come from the plan
- L001 — Plans folder rule (this lesson extends it with the multi-phase workflow)
- L007 — Multi-file Cursor prompts need ALLOWLIST + verbatim FIND/REPLACE (Phase 3 prompts inherit this)
- L036 — Closed-risk annotation discipline (follow-up plans must annotate the earlier plan's risk row)

---

### L041 — Pattern-match safety tripwire for external string catalogs

**Date:** 2026-05-22
**Project:** a reference project
**Phase / Task:** PLAN-004 design § 11 risk #1

#### Incident

PLAN-004 integrates the EA with an external economic-calendar catalog. Events are matched by substring patterns against the calendar's `event.name` field. The catalog is maintained by a third party (MetaQuotes); event names are stable per their convention but not guaranteed — a rename like "Nonfarm Payrolls" → "US NFP" would silently break the substring match, and the module would silently stop blocking those events.

A silent miss on a safety-block module is worse than a noisy error: the operator believes the block is active and trades accordingly; only post-hoc analysis would surface the gap.

#### Cost

Hypothetical-but-realistic. The mitigation was designed before any breakage occurred.

#### Codification

When pattern-matching against an external catalog of strings (event names, error codes, API status messages, ticker symbols, etc.), include a **safety tripwire** that surfaces uncategorized items the operator might care about:

- For each item the matcher receives that does NOT match any known pattern AND meets a "interesting" predicate (HIGH/MOD-HIGH impact, fatal error class, etc.), log a single operator-visible line: `UNCATEGORIZED <type>: "<value>" — operator: review patterns.`
- Log only the FIRST occurrence per refresh cycle to avoid log spam.
- Log location should be operator-visible (terminal log, chart panel, monitoring dashboard) — not silent in a debug-only stream.

The tripwire converts a silent miss into a noisy miss. The operator updates the pattern (one-line fix) when they see it. No automation needed — the LogInfo line IS the signal.

#### Cross-references

- `ENGINEERING_STANDARDS.md` § 4 error handling — sub-section on safety tripwires for pattern-match drift
- L032 — Investigate underlying data when operator questions answers (related: tripwire creates the question; investigation answers it)

---

### L040 — Fail-safe defaults for external-data sources that may be unavailable

**Date:** 2026-05-22
**Project:** a reference project
**Phase / Task:** PLAN-004 design § 11 risks #2 + #3

#### Incident

PLAN-004 integrates with an external data source (the application language economic calendar via `CalendarValueHistory`). The same API behaves differently across environments:

- Production (live broker terminal): returns events.
- Strategy Tester (backtest environment): returns 0 / -1 depending on tester mode — the calendar feed isn't populated in tester.
- Brokers without calendar feed: returns 0 — feature simply isn't enabled.

If the module treats "no data" as an error (warn, block, or fail), backtesting breaks immediately (no news data ever) and brokers without the feature can't run the EA at all. If the module treats "no data" as "no events found this poll" (silent skip + log), both degraded paths run cleanly without false positives.

The pattern: the module's "no data" branch must be a **no-op that lets the rest of the system run normally**, not an error branch that propagates upward.

#### Cost

Designed in at the plan-writing stage. Cost-of-not-doing-this is operator-blocked backtesting + EA-fails-on-some-brokers.

#### Codification

When integrating with an external data source that can degrade silently (test environment, missing config, third-party outage, regional unavailability), the module's "no data returned" branch must:

1. **Treat zero/empty as the fail-safe state** — typically "no events found, no block, no warning."
2. **Not warn or error** — these are normal degraded-environment behaviors, not bugs.
3. **Log once at startup** — operator sees that the module is enabled but the data source is empty/unavailable; informational, not a warning.
4. **Continue running** — the rest of the system runs without the optional safety this module would have provided. The operator can re-enable it once the data source comes back.

This complements L009 (deliberate-failure testing): L009 ensures alerting fires when something IS wrong; L040 ensures the absence of optional data doesn't masquerade as something being wrong.

Generalizes to: optional integrations (analytics, feature flags, second-opinion APIs, observability sinks); environments where production data isn't available (test, CI, staging-without-prod-mirroring); third-party services with regional or quota limits.

#### Cross-references

- `ENGINEERING_STANDARDS.md` § 4 error handling — sub-section on fail-safe defaults for external-data sources
- L009 — Deliberate-failure testing (paired pattern: L009 ensures fail-loud when expected; L040 ensures fail-silent-and-degraded when expected)

---

### L039 — Grep all reads before splitting a globally-read state variable

**Date:** 2026-05-22
**Project:** a reference project
**Phase / Task:** PLAN-004 design § 11 risk #6

#### Incident

PLAN-004 needed to replace a single-string global (`g_authStatus`) that had accreted multiple meanings over the project's history — auth diagnostics ("not_checked", "auth_session_expired") AND trade-block reason codes ("no_trade_time_friday", "closeout_management_only") were stored in the same string variable. The new design needed a structured `TradeBlockFlags` struct for the trade-block reasons, while leaving auth diagnostics alone.

Before refactoring, the plan called for a grep audit: every read of `g_authStatus` had to be classified as "auth diagnostic" (leave alone) or "trade-block reason consumer" (re-route to new helper). Without the audit, the refactor would either: (a) leave a stranded consumer reading the wrong thing, OR (b) over-aggressively rewrite an auth-diagnostic site to use the new struct it has no semantic relationship to.

Captured in PLAN-004 § 11 as risk #6: "before changing any consumer, grep `g_authStatus` reads in the EA. Some are unrelated to trade-block. Only the trade-block-reason-display reads get redirected."

#### Cost

Designed-in at plan stage. Cost-of-not-doing-this is a half-finished refactor that compiles but breaks subtle behaviors at runtime.

#### Codification

When refactoring a globally-read state variable (any variable that's read from many sites and represents multiple concerns):

1. **Grep all reads first.** `grep -n '<varname>' <file>` and list every site.
2. **Classify each read** — which concern is it serving? (e.g., "auth diagnostic", "trade-block reason", "log-line content".)
3. **Route each consumer in the same commit** as the refactor — either to the new helper that replaces this concern, OR explicitly leave it on the old variable with a comment.
4. **No silent stranding** — every read site has an explicit disposition in the refactor commit.

This complements L007 (multi-file Cursor prompts need ALLOWLIST + verbatim transformation rules): the grep-and-classify pass produces the per-site transformation rules. The risk is highest when the variable's name has drifted from its actual meaning (the "single mutable string with multiple meanings" anti-pattern).

#### Cross-references

- `ENGINEERING_STANDARDS.md` § 1 architecture invariants — sub-section on refactor blast-radius
- L007 — Multi-file Cursor prompts need ALLOWLIST + verbatim FIND/REPLACE (paired: grep-and-classify produces the FIND blocks)

---

### L038 — ALLOWLIST count is the bullet enumeration, not the prose sentence

**Date:** 2026-05-22
**Project:** a reference project
**Phase / Task:** PLAN-004 Phase 3 execution (commit `d04450a`)

#### Incident

PLAN-004 § 7 included both a prose count ("**Total files in execution commit: 12.**") and a bullet enumeration of files. The enumeration listed 10 entries; the prose sentence said 12. When Phase 3 ran, `git status --short` showed 10 staged files matching the bullets. The two-second pause to re-count ("did I miss two files?") would have escalated if the agent had trusted the prose over the enumeration.

This is a generalization of L007 (multi-file prompts need ALLOWLIST): the ALLOWLIST IS the bullet list. Prose counts can drift during plan revisions (the plan was edited; the bullet list was edited; the prose count wasn't updated) without anyone noticing.

#### Cost

Two-second pause; no actual error. Codified to prevent the same drift from causing an error in a future plan with a larger ALLOWLIST.

#### Codification

When the ALLOWLIST is the contract:

1. **The bullet enumeration IS the authoritative count.** Any prose "N total files" sentence is a derived value, subject to drift.
2. **Phase 3 agent verifies `git status --short` against the bullet list, not the prose count.** If the two disagree, treat the bullets as correct and report the drift to the operator.
3. **Plan author keeps prose counts in sync** when editing the bullet list. Or: omit the prose count entirely — the bullet list is self-counting.

Add to PROMPT_STANDARDS § 3.2 ALLOWLIST guidance: "The bullet enumeration is the ALLOWLIST. Ignore prose counts that don't match."

#### Cross-references

- `PROMPT_STANDARDS.md` § 3.2 ALLOWLIST block — non-negotiable structure (refined with this lesson)
- L007 — Multi-file Cursor prompts need ALLOWLIST + verbatim FIND/REPLACE (this lesson refines the ALLOWLIST sub-element)

---

### L037 — Time-window with end=00:00 fires at minute 0 of the same day (wrap-window pitfall)

**Date:** 2026-05-22
**Project:** a reference project
**Phase / Task:** Operator runtime observation post-v7.08

#### Incident

Operator configured a Friday no-trade window as `Friday_NoTrade_Start="20:00"` / `Friday_NoTrade_End="00:00"` intending "20:00 broker time until end of Friday." At Friday 00:00:00 broker time, the chart panel briefly showed the Friday block + closeout-mode active for one minute before deactivating, then reactivated at 20:00 as expected.

Root cause: the HH:MM parser converts `00:00` to integer minute-of-day = `0`. The window check sees `start=1200` and `end=0`; `start > end` triggers the wrap-window branch, which returns true when `now >= start OR now <= end`. At broker minute 0 of Friday, `now=0 <= end=0` matches — the window fires for that one minute.

Semantically the operator wanted "until end of Friday" (i.e., until Saturday 00:00 = end of the weekday-anchored gate), not "wrap into the next day at minute 0." The system did exactly what the inputs said, but the inputs surface a non-obvious behavior at the day boundary.

Reproducible without operator-side error: any HH:MM time-window system that uses integer minute-of-day and treats `start > end` as a wrap-window has this property when `end="00:00"`.

#### Cost

One minute of false-positive Friday-block activation at midnight on the day the operator's Friday window first went live. No trades were affected (the EA was idle at 00:00); but the closeout-mode row flickered, which surfaced the operator's question.

#### Codification

**Convention for HH:MM "end of day" intent:** use `23:59` for the END value when the operator wants "until the end of this weekday." Reserve `end="00:00"` only when the wrap-into-the-next-day match is intentional.

**Documentation:** the recommendation belongs in both the standards (`ENGINEERING_STANDARDS.md` § time-window parsing pitfalls — generic) AND in the project-specific spec (`09_session_filter.md` + `02_inputs.md` edge-case rows — operator-facing).

**Implementation alternative (rejected):** the parser could treat `end="00:00"` as a special case meaning "end of day" (~minute 1439). Rejected because: (a) operators may legitimately want a wrap-into-tomorrow window (e.g., `22:00 / 02:00`); (b) the explicit `23:59` convention is operator-controllable without code changes; (c) special-casing introduces a second non-obvious behavior to remember.

Generalize to any project that parses time-of-day windows as integer minute-of-day: document the wrap-window behavior; recommend `23:59` for end-of-day intent; provide examples of intentional vs accidental wrap-windows.

#### Cross-references

- `ENGINEERING_STANDARDS.md` § 1 architecture invariants — sub-section on time-window parsing pitfalls
- Project-specific application: `docs/<domain-spec>/09_session_filter.md` § Window matching + edge-case table

---

### L036 — Annotate a closed plan-risk in the same commit that ships the mitigation

**Date:** 2026-05-21
**Project:** a reference project
**Phase / Task:** PLAN-001 § 11 bookkeeping fix-forward (commit `d769b29`)

#### Incident

PLAN-001 documented seven design risks (§ 11). Across PLAN-002, v7.06, and PLAN-003, three of those risks were systematically mitigated:

- Risk #1 (UTC time conversion) was eliminated by PLAN-002's broker-time-everywhere refactor.
- Risk #2 (partial-close dispatch on stale `SafetyStatus`) was hardened by v7.06's atomic-safety-check.
- Risk #3 (Closeout + Recovery interaction) was fully specified by PLAN-003 / v7.07.

But PLAN-001's risk section never reflected those closures. v7.06's CHANGELOG entry called its risk #2 "now mitigated by design" but didn't touch PLAN-001 itself. PLAN-003's commit `dc624ef` shipped the mitigation for risk #3 without annotating PLAN-001. Result: an audit-trail drift where PLAN-001's last word on risks #1–#3 was "remains open — investigation deferred" — false, but the canonical record said so.

Operator caught it during a status check on 2026-05-21 ("there's drift between the repo state and PLAN-001's risk section"). Fix-forward landed as `d769b29` annotating all three risks as CLOSED with the closing commit hash.

#### Cost

Audit-trail drift is the silent cost — anyone reading PLAN-001 in isolation would form a wrong mental model of the project's open risks. Caught only by deliberate cross-checking. The fix-forward commit was small (single plan-doc edit) but added to the commit graph noise.

#### Codification

When a follow-up plan or commit mitigates a documented risk from an earlier plan, the earlier plan's risk row MUST be annotated as CLOSED in the SAME commit that ships the mitigation. Annotation includes:

1. Status change (`OPEN` → `CLOSED`).
2. Closing commit hash.
3. Brief one-line reason (which plan, which mechanism).

If a follow-up commit ships a partial mitigation, mark the risk `PARTIAL` with the same annotation pattern.

**The audit trail is the source of truth for open risks.** A risk is open if and only if the plan that documented it says it's open. Plan documents are mutable in this respect — the risk section is not a frozen historical snapshot; it's a living status board that the project's commits keep current.

Add to PROJECT_STANDARDS.md as a same-session sync trigger (§ 4): "Closing a documented risk from an earlier plan → annotate the earlier plan's risk row in the same commit as the mitigation."

#### Cross-references

- `PROJECT_STANDARDS.md` § 4 artifact sync — closed-risk annotation sub-section
- `CLAUDE.md` § 11 commit policy — multi-file commits include the closed-risk annotation when applicable
- L010 — Split-commit delivery for substantive doc additions (related: closed-risk annotations are small enough to bundle, but still need an explicit "did I update the earlier plan?" check)
- L029 — Distribute doc sync across split commits (this lesson extends the sync trigger list)

---

### L035 — a cloud provider's web console avoidance for sensitive files

**Date:** 2026-04-22 (codified earlier as a project rule; lifted to standards-repo 2026-05-16)
**Project:** a reference project
**Phase / Task:** Phase 1 binding rule

#### Incident

a cloud VPS provider's cloud web console (the browser-based VPS terminal accessible from the cloud provider's UI) is unencrypted in transit for displayed content between the browser and a cloud VPS provider's servers. Typing or viewing `.env` content, SSH keys, deploy tokens, or any secret in the web console leaks the content over an unencrypted channel. SSH-from-local-terminal is end-to-end encrypted; that's the right path.

Caught at design time during Phase 1 setup; never had an actual leak.

#### Cost

Hypothetical-but-likely cost had it not been caught at design time. Codified as a binding project rule from day 1.

#### Codification

Never use the a cloud VPS provider cloud console (or any web-based VPS terminal) for typing/displaying sensitive files. SCP files to/from the host instead; SSH from local terminal for any interactive work that involves secret content.

Generalizes to: any browser-based remote terminal that isn't end-to-end encrypted for displayed content. Applies to other cloud providers' web consoles too.

#### Cross-references

- `ENGINEERING_STANDARDS.md` § 9 secrets handling (operator-discipline sub-section)
- `CICD_STANDARDS.md` § 11 operator workflows (gotcha)

---

### L034 — macOS disk full: restart frees 30+ GB; don't hunt caches first

**Date:** 2026-05-12
**Project:** Cross-project (machine operations)

#### Incident

Mac disk filled up during a long working session; the symptom presented as Rosetta failing to spawn x86 binaries — a misleading diagnosis since the rebuild target was Apple Silicon. Investigation went into Docker volumes, npm caches, build directories, browser caches — none of which were the actual bottleneck. The root cause was filesystem snapshots reported by `tmutil`, which a system restart purges automatically.

Resolution path that worked: `tmutil listlocalsnapshots /` first; if any snapshots existed, restart (which deletes them) or manually purge via `tmutil deletelocalsnapshots <date>`. Restart freed ~30 GB reliably. Cache-hunting was the wrong default.

#### Cost

~45 min of cache-hunting before the snapshot-purge / restart path was tried.

#### Codification

On macOS disk-full / "Rosetta hang" / "container build fails for no reason" symptoms:

1. Run `tmutil listlocalsnapshots /` first.
2. If snapshots exist, restart the machine (or purge manually).
3. Restart is the fastest reliable reclaim path.
4. Skip cache-hunting until snapshot purge has been tried.

Cross-project operational tip; not project-specific.

#### Cross-references

- `ENGINEERING_STANDARDS.md` § 10 operator-machine operational tips (new sub-section)

---

### L033 — Codex retry prompts need PRIOR DEVIATION WARNING

**Date:** 2026-05-09
**Project:** a reference project
**Phase / Task:** Phase 6 Codex collaboration

#### Incident

Codex deviated from a multi-file prompt's scope (touched a file outside the ALLOWLIST). Operator pasted the deviation back to Claude and asked Claude to re-prompt Codex with the same scope. Claude re-prompted verbatim, expecting Codex to read it fresh and follow correctly. Codex deviated AGAIN in the same way — its training-data priors overrode the prompt's constraints on the second attempt.

Pattern: when re-prompting an agent that just deviated, the retry prompt must explicitly name the prior failure mode at the top. Verbatim re-prompts without the deviation callout fail more often than not — agents drift toward the same training-data priors the original prompt was supposed to suppress.

#### Cost

~2 wasted turns of repeated deviation before the prior-warning pattern was named.

#### Codification

Codex retry prompts (and any retry prompts to any agent) include explicit PRIOR DEVIATION WARNING at the top:

```
========================================
PRIOR DEVIATION WARNING
In the prior attempt, <file/scope> was modified outside ALLOWLIST.
Do not repeat. Non-negotiable outcomes:
- <outcome 1>
- <outcome 2>
========================================
```

Place the warning ABOVE the original prompt's ALLOWLIST / STEPS so the agent processes it first. Reinforced by the prompt's TODO checklist explicitly carrying a "PRIOR DEVIATION NOT REPEATED" checkbox.

#### Cross-references

- `PROMPT_STANDARDS.md` § 9 recovery prompts (retry-with-deviation-warning sub-section)
- L020 (Codex handoff protocol — paired pattern)

---

### L032 — Investigate underlying data when operator questions answers

**Date:** 2026-05-11
**Project:** a reference project
**Phase / Task:** Phase 7 D17 / D18 debugging

#### Incident

Agent answered an operator's question about signal behavior with a plausible-sounding explanation based on session context. Operator asked "how can X be Y?" Agent's response: re-explained the same logic with more confidence and more elaboration. Operator probed further. Agent eventually queried the DB — finding the original answer was wrong. The DB had the answer all along; the agent had been answering from session-derived context that was incomplete.

Pattern: when an operator's clarifying question surfaces uncertainty, the right move is to **investigate the underlying data** (query the DB, read the file, run a probe) — NOT to defend the original answer with more elaboration.

The instinct to defend is strong because the original answer felt confident. But operator-questioning IS the uncertainty signal. Defending past it produces drift between agent's stated facts and actual data state.

#### Cost

~30 min wasted per incident in the clarifying-question dance before underlying data was queried. Multiple similar incidents across Phase 7 before the pattern was named.

#### Codification

When the operator questions an answer, treat that as a signal to investigate the underlying source — query the DB, read the file, run the probe. Defending the original answer with more elaboration is the anti-pattern.

Added to AI behavior rules in `CLAUDE.md` § 10 (Investigate-when-questioned). Also reinforces `MEMORY_PROTOCOL.md` § 5 ("recalled memory can be stale; verify before defending").

#### Cross-references

- `CLAUDE.md` § 10 AI behavior rules (investigate-when-questioned sub-rule)
- `MEMORY_PROTOCOL.md` § 5 (memory hygiene rituals — verify-before-recommending)

---

### L031 — Never bounce operator to UI for status; agent probes via REST API

**Date:** 2026-05-08
**Project:** a reference project
**Phase / Task:** Phase 6 pipeline-status investigations

#### Incident

When pipeline status / job status / job trace info was needed, the agent's default response was "check the GitLab UI and report back" — handing the navigation cost to the operator. Operator was bouncing between Claude.ai and GitLab tens of times per session for status snippets.

Investigation: GitLab's REST API exposes everything the UI shows. Token is at `~/.gitlab-token`. Agent can curl pipeline status, job status, and job traces directly. No operator UI-bouncing needed.

#### Cost

~5–10 min per session of operator UI-bouncing across Phase 6, multiplied across many sessions.

#### Codification

Never bounce operator to UI for status checks. Agent probes pipeline / jobs / trace via the CI provider's REST API directly. Recipes documented per project's CI provider. Token kept at `~/.<provider>-token` (gitignored, per-machine, never in any tracked file).

For GitLab specifically:
- Pipeline list: `GET /api/v4/projects/:id/pipelines`
- Job list: `GET /api/v4/projects/:id/pipelines/:pipeline_id/jobs`
- Job trace: `GET /api/v4/projects/:id/jobs/:job_id/trace`

Per-project access details (project ID, base URL, token path) go in the project's Project Instructions Tier B, not in user-wide memory (per L015).

#### Cross-references

- `CICD_STANDARDS.md` § 11 operator workflows (no-UI-bouncing sub-section)
- `PROJECT_INSTRUCTIONS_TEMPLATE.md` Tier B (per-project CI API access details)

---

### L030 — Always call out PROD actions explicitly

**Date:** 2026-05-09
**Project:** a reference project
**Phase / Task:** Phase 6 prod-deploy bundle authorization

#### Incident

A flow summary describing "the full deploy cycle" bundled staging deploy + prod deploy + post-prod verification under a single authorization request. Operator approved the bundle expecting it to mean staging-deploy only (with prod-deploy gated separately by the existing manual gate). Agent interpreted the approval as covering the entire bundle. Prod deploy went through without separate operator confirmation.

The miss: PROD actions have a fundamentally different cost-of-failure than staging actions. Bundling them under a single approval is an anti-pattern even when the operator nominally "approves the whole flow." Operator's mental model is "one approval covers one action class"; bundling violates that model.

#### Cost

No production incident this time (the deploy happened to succeed), but the protocol gap surfaced.

#### Codification

Every PROD deploy / SSH apply / restart / config change gets its OWN labelled authorization round, separate from the staging cycle. Never bundle PROD in a flow summary. Phrase the request as:

> "Authorize PROD deploy of `<SHA>` after 24h staging soak completes at `<timestamp>`?"

Operator must explicitly confirm "yes, PROD" — never inferred from staging approval.

#### Cross-references

- `CICD_STANDARDS.md` § 9 production deploy gate (explicit-PROD-callout sub-section)
- `CLAUDE.md` "Executing actions with care" pattern (PROD = blast-radius beyond local environment)
- L022 (24-hour soak — paired pre-prod discipline)

---

### L029 — Distribute doc sync across split commits

**Date:** 2026-05-10
**Project:** a reference project
**Phase / Task:** Phase 7 multi-commit feature work

#### Incident

The original split-commit pattern (L010) split commits into "risky content" + "mechanical wiring" but concentrated ALL governance work (manifest, CHANGELOG, doc sync) in the wiring commit. This passed governance on the wiring commit but the risky-content commit failed governance if pushed independently (which sometimes happened for CI-verification reasons). The risky-content commit appeared broken in CI even though everything was about to be fixed in the next commit.

Pattern: every commit in a multi-commit plan must satisfy governance independently. "I'll fix it in the next commit" leaves the in-between state non-shippable, and `git bisect` becomes unreliable across that range.

#### Cost

~3 pipeline round-trips during Phase 7 multi-commit work where Commit A failed governance because of deferred manifest updates.

#### Codification

Multi-commit plans must satisfy governance at every push. Redistribute "final-sync" bundles backward into A and B so each commit is independently shippable:

- Commit A: includes manifest / CHANGELOG entries for files A touches
- Commit B: same for B
- No deferred-sync bundle at the end

This refines L010 (split-commit pattern): L010 said split content vs wiring; L029 adds that wiring must be distributed, not concentrated.

#### Cross-references

- `PROJECT_STANDARDS.md` § 8.4 split-commit pattern (refinement)
- L010 (original split-commit pattern — this refines)

---

### L028 — Batch local commits; push only when necessary

**Date:** 2026-05-08
**Project:** a reference project
**Phase / Task:** Phase 6 / Phase 7

#### Incident

Original cadence was push-after-every-commit. With multi-session work (sometimes 4–6 commits in one session), this triggered the CI pipeline for each one — most of those CI runs were "decoration" because the next commit superseded the deploy state immediately. Pipeline noise grew. CI compute and storage costs grew. The push-after-every-commit pattern was treating pushes as a save action; pushes are actually a publish action.

#### Cost

~10× the necessary pipeline runs during Phase 6 multi-commit sessions. Pipeline UI cluttered with intermediate states. Operator attention diluted across noise commits.

#### Codification

Default to local commit + hold; push only on:

1. CI-verify needed (the commit changes CI behavior worth observing live)
2. Staging-verify needed (the commit modifies deploy behavior)
3. Deliberate-failure cycle in flight
4. `.gitlab-ci.yml` change (real-pipeline run is dispositive — Rule 5)
5. End-of-session trigger (close the day with a clean published state)

Otherwise commit locally, batch, push once when a trigger is hit.

#### Cross-references

- `CLAUDE.md` § 11 commit policy (cadence sub-section)
- `PROJECT_STANDARDS.md` § 8 commit discipline
- L002 (pre-push governance — pushes are the gate this rule defers)

---

### L027 — Code review BEFORE every commit (separate from governance)

**Date:** 2026-05-07
**Project:** a reference project
**Phase / Task:** Phase 6

#### Incident

A commit landed with two functional defects that governance scripts didn't catch (governance validates documentation / manifest drift, not code quality). The agent had skipped a quality-review pass after applying edits; governance + tests passed; code shipped; both defects surfaced in the next session.

The miss: governance scripts validate alignment, not correctness. They don't catch logic errors, missed edge cases, or readability problems. Code review is an orthogonal quality gate that governance scripts structurally cannot replace.

#### Cost

1 broken landing + ~30 min of fix-forward commits.

#### Codification

Code review BEFORE every commit — explicit named review pass on all modified/new files BEFORE `git add`. Separate quality gate from governance scripts. If code review surfaces concerns, fix them and re-review before staging.

Added to the validation checklist (`CLAUDE.md` § 8) as a dedicated step distinct from governance. The reviewer (human or agent) walks each modified file and asks: "Does this read correctly? Does it handle the edge cases the task implied? Is there a subtle bug a future reader would catch?"

#### Cross-references

- `CLAUDE.md` § 8 validation checklist (code-review step)
- `PROJECT_STANDARDS.md` § 8 commit discipline
- L026 (run commits yourself — paired discipline)

---

### L026 — Run commits yourself; don't hand back to user

**Date:** 2026-05-07
**Project:** a reference project
**Phase / Task:** Phase 6 multi-session work

#### Incident

Original pattern: agent prepares the commit message file at `/tmp/<file>.txt`, then hands "ready to commit" back to the operator who runs `git add` + `git commit -F` manually. This was a holdover from earlier sandbox-failure recovery (where the agent couldn't reliably run git operations). But the operator-handoff added friction at every commit — operator had to context-switch from chat to terminal, often forgetting the explicit `-F` flag and resorting to `-m` with escapes (Rule 4 / L004 violation).

Better pattern: agent runs `add` + `commit -F /tmp/<file>.txt` end-to-end. Operator still gates pushes (per L028 cadence). Code review still happens BEFORE `git add` (per L027). Sandbox failures, when they happen, get scoped path-operation recovery (operator authorizes specific path patterns for the agent's git operations).

#### Cost

~3 sessions of operator-driven commit ceremony with multiple L004 violations before the new pattern was codified.

#### Codification

Agent runs `add` + `commit -F /tmp/<file>.txt` end-to-end:

- Code review BEFORE `git add` (per L027)
- `git status --short` before AND after `git add` (per Rule 6 / L006)
- Commit message via `-F /tmp/<file>.txt` (per Rule 4 / L004)
- Pushes remain operator-gated (operator runs `git push` after final review)

Sandbox-failure recovery via scoped path operations — operator authorizes specific path patterns for the agent's git operations rather than blanket bypass.

#### Cross-references

- `PROMPT_STANDARDS.md` § 3.7 (commit step)
- `CLAUDE.md` Rule 4 (commit message file delivery)
- `PROJECT_STANDARDS.md` § 8 commit discipline
- L027 (code-review-before-commit — paired discipline)

---

### L025 — CI-injected `.env` files are wiped on every deploy

**Date:** 2026-05-05
**Project:** a reference project
**Phase / Task:** Phase 5

#### Incident

Operator made a "permanent" config change by SSHing to staging and editing `.env`. The change worked until the next CI deploy, which overwrote `.env` from the CI-managed env file. Investigation revealed: the project's CI pipeline injects `.env` from a CI variable on every deploy. Any manual edit to `.env` on the host is ephemeral.

The line-count divergence between staging `.env` (operator-edited, longer) and prod `.env` (CI-injected, shorter) was the tell — operator hadn't noticed.

Pattern: manual edits to a file that CI rewrites is a silent-revert trap. Looking at the running config (post-edit) shows the right values; looking at the same file an hour later (post-deploy) shows the wiped values. The change appears to work, then appears to disappear.

#### Cost

~45 min of debugging "why is my config change reverting" before the CI-injection pattern was confirmed.

#### Codification

Always verify config source-of-truth before manual edits:

- Grep the CI config FIRST. If the file is CI-injected, manual edits are ephemeral.
- Line-count divergence between staging and prod `.env` files is a CI-injection tell.
- Durable config changes go in the CI variable (or wherever CI sources from), not the host file.
- If a host-file edit is genuinely needed for diagnostic purposes, document it as temporary and revert before the next deploy.

#### Cross-references

- `CICD_STANDARDS.md` § 4 CI variables + § 6.4 authentication
- `ENGINEERING_STANDARDS.md` § 3 secrets handling
- L023 (staging mirrors production — same root-cause pattern)

---

### L024 — Never run raw `docker compose up` on staging or production

**Date:** 2026-05-04
**Project:** a reference project
**Phase / Task:** Phase 5

#### Incident

Operator SSHed to staging to apply a manual diagnostic, then ran `docker compose up -d` to restart services. Compose's image-tag substitution silently downgraded the container to a stale local-cache tag because `${APP_IMAGE_TAG}` wasn't exported in the operator's shell. The downgrade went unnoticed for ~30 min — the older revision happened to be compatible with the diagnostic. Caught only when the next CI deploy's smoke compared running image against the expected SHA.

Pattern: compose-file env-var substitution is silent. Missing-or-unset vars resolve to empty strings or stale local-cache tags. The interactive `compose up` looks identical for "deploys correctly" and "downgrades silently."

#### Cost

~30 min of stealthy stale-image state on staging. Operator confidence in manual ops dropped.

#### Codification

Never run raw `docker compose up` on staging or production hosts. Use either:

- `scripts/deploy.sh` (which exports the right env vars + pulls the SHA-tagged image), OR
- Pre-tag the registry image with `docker tag` then restart via the deploy script

Manual `compose up` is an anti-pattern in any environment beyond local development. The smoke check (`post_deploy_smoke.sh` Section 5 — image source verification) is the catch-net, but the goal is to not need the catch-net.

#### Cross-references

- `CICD_STANDARDS.md` § 6 deploy patterns + § 13 anti-patterns
- `ENGINEERING_STANDARDS.md` § 7.4 image source verification (the smoke check that catches this class)
- L005 / Task 2.5c silent-fallback pattern (related)

---

### L023 — Staging mirrors production — env parity

**Date:** 2026-05-10
**Project:** a reference project
**Phase / Task:** Phase 6

#### Incident

A planned "prod-only" config tweak was applied directly to production (operator deemed it "too small to need staging"). Per the CI-injected `.env` pattern (L025), the next deploy wiped the manual change. Investigation revealed the change had been planned without a parallel staging change — it was treated as a one-off.

Pattern: any plan describing "prod-only" actions is wrong by default. Durable changes go in CI config (which targets both envs), not host files.

#### Cost

~1 hour of wipe-and-replay debugging before the SoT pattern was recognized.

#### Codification

Staging mirrors production — every prod config / secret / profile change has a parallel staging change in the same operator session. **Staging FIRST**, then prod. Plan-defined "prod-only" tasks are an anti-pattern.

The pattern enforces:

1. Same change is tested in staging before prod sees it
2. Both env's stay in sync at the config layer
3. CI-injection (L025) wiping is impossible because the change is in the CI variable, not the host file

#### Cross-references

- `CICD_STANDARDS.md` § 9 production deploy gate (env parity sub-section)
- `ENGINEERING_STANDARDS.md` § 3 secrets (verify config source-of-truth before manual edits)
- L025 (CI-injected `.env` wipes — closely related root cause)

---

### L022 — 24-hour staging soak required before any production deploy

**Date:** 2026-05-06
**Project:** a reference project
**Phase / Task:** Phase 5 close-out

#### Incident

A staging deploy passed smoke immediately but exhibited a slow regression after ~4 hours of live data. Per the protocol at the time, the change had been promoted to production within 30 min of staging deploy (operator deemed it "smoke-verified"). Production saw the same regression. Auto-rollback fired correctly, but operator lost confidence in smoke-only gating.

Pattern: smoke catches "the deploy is running" failure modes. Some regressions only surface under live-data load over hours. Smoke is necessary but not sufficient for the prod-promotion decision — specifically for systems that operate on time-series live data where slow-burn regressions are possible.

#### Cost

1 production incident + auto-rollback. ~1 hour of production-affected time before rollback completed.

#### Codification

No production deploy until **24 hours after the same commit's staging deploy timestamp**. The soak window resets if any new commit lands in the deploy-candidate. Soak is **in addition to** smoke verification — both must pass.

Smoke gates the deploy on the technical level; the 24h soak gates it on the behavioral level. They catch different failure classes. Operator session that asks for "PROD deploy" must include the staging-deploy timestamp and the calculated soak-completion timestamp in the authorization request (per L030).

#### Cross-references

- `CICD_STANDARDS.md` § 9 production deploy gate
- `VALIDATION_STANDARDS.md` § 7 deliberate-failure testing (24h soak is the slow-burn equivalent of failure injection)
- L030 (explicit PROD-action authorization — paired)

---

### L021 — Live candle OHLC values mutate during first 10 min

**Date:** 2026-05-08 (D18 root cause analysis)
**Project:** a reference project
**Phase / Task:** Phase 7 / D18

#### Incident

Live signal generation diverged from backtest signal generation for ostensibly identical conditions. Investigation traced to the live data feed's rolling gap-fill: each new bar gets written to the DB, then rewritten 6–7 times during the first ~10 minutes as later ticks arrive and high / low / close are updated. Pattern detection operating inside this 10-min window sees mutable OHLC; backtest detection operates on settled OHLC.

The mutability is invisible to a single-shot DB read — the bar exists, the row has values. But the values that exist at minute 1 differ from the values at minute 12. Detection logic that hashes the bar or makes pivot decisions inside that window can produce different outputs across consecutive reads of the "same" bar.

#### Cost

~2 weeks of cross-session investigation before the mutability window was named as the root cause. Affected D17 reconciliation (max_age_minutes default 5.0 → 15.0 hotfix).

#### Codification

For any detection logic that runs in production against live data:

- Design with mutability tolerance (the function must produce the same decision even as OHLC values evolve within the window), OR
- Delay detection until the bar has settled (operate post-mutability-window)
- Document the mutability window per data provider in the project's domain doc

For backtest-vs-live reconciliation:

- Tests that compare live vs backtest results must account for the mutability window
- Live-vs-backtest divergence within the mutability window is expected, not a bug
- Tests should compare against post-settlement live data when correctness matters

#### Cross-references

- `ENGINEERING_STANDARDS.md` § 1 architecture invariants (live-data invariants sub-section)
- `VALIDATION_STANDARDS.md` § 1.4 determinism (live data introduces a non-determinism class)

---

### L020 — Codex handoff protocol (separate-domain agent collaboration)

**Date:** 2026-05-04 (codified incrementally over Phases 5–7 multi-agent work)
**Project:** a reference project
**Phase / Task:** Phase 5+ multi-agent collaboration

#### Incident

When a second AI agent (Codex) joined the project to take ownership of charting / frontend work, ad-hoc collaboration between Claude (the bookkeeping authority) and Codex (the code-modifying agent) produced drift: Codex modified governance files Claude was responsible for (CHANGELOG, manifest, folder_structure, tracker entries), Codex attempted commits in parallel with Claude's commit cadence, and dual-update conflicts emerged on the same source-of-truth files.

The root pattern: when two AI agents share a codebase, each must have a clear domain boundary. The agent that owns bookkeeping cannot have its responsibilities silently absorbed by the other.

#### Cost

~3 sessions of conflict resolution + tracker drift before the protocol was codified.

#### Codification

Codex handoff protocol — formalized as a section in the project's CLAUDE.md (binding for that project) and surfaced as an OPTIONAL pattern in the standards template:

- Codex modifies code in its domain only; never CHANGELOG, manifest, folder_structure, validation_ownership.toml registration of new files, or trackers Codex doesn't own.
- Codex bumps in-file VERSION headers + CHANGE LOG entries on source files it modifies (those are part of source).
- Codex ends every session with a structured 7-element summary: (1) files modified, (2) files created, (3) why, (4) verification raw output, (5) tracker reference, (6) deviations from plan, (7) files deferred.
- Operator pastes the summary to Claude. Claude verifies via filesystem, runs governance scripts, code-reviews, commits.
- Claude does ALL central bookkeeping on Codex's behalf: CHANGELOG, manifest, folder_structure, validation_ownership.toml registration, trackers Codex doesn't own.

This is an OPTIONAL pattern in the standards template — only adopt if your project uses a second agent. Single-agent projects skip it entirely.

#### Cross-references

- `CLAUDE.md` § Codex handoff (in adopting projects' root `CLAUDE.md`, when applicable)
- `PROJECT_STANDARDS.md` § Tracker ownership (the ownership-by-header rule)
- `PROMPT_STANDARDS.md` § Codex handoff prompt shape
- L033 (Codex retry deviation warning — paired pattern)

---

### L019 — Self-contained CI jobs: auth state should not cross job boundaries

**Date:** 2026-04-30
**Project:** a reference project
**Phase / Task:** F-1 verification cycle (post-Task 3.4)

**Context:** L018 (added 2026-04-29) identified the anti-pattern: CI jobs that depend on persistent state on remote hosts (docker auth, session tokens, file locks) are fragile because between-job state can be invalidated by anything (token expiration, rotation, other jobs overwriting it). L019 codifies the POSITIVE pattern that resolves it: each CI job should establish whatever state it needs at job start, not assume previous jobs left it in place.

**the standards source-specific evidence:** Tonight's F-1 cycle (2026-04-30 00:55 UTC) verified this pattern works in practice. F-1 modified rollback.sh from "operator pre-authed" model (relied on persistent docker auth on the VPS) to "self-sufficient" model (does its own `docker login` at script start when CI env vars are present, NO-OP otherwise for manual operator workflows). The verification cascade succeeded in iteration 1 — last cycle (Task 3.4 verification, 2026-04-29) needed iteration 2 because of the auth gap. The architectural change (small: one new section in rollback.sh) was the difference between a brittle gate and a trustworthy one.

**The pattern (positive form):** Self-contained CI jobs:
- **Don't trust between-job state.** Establish auth/credentials/tokens at job start. Mirror the deploy job pattern.
- **Be NO-OP-safe for manual workflows.** If env vars aren't present (manual operator on VPS), the auth-establishing block becomes a NO-OP and the script falls back to "use whatever auth exists." This preserves the manual workflow while making the CI workflow correct.
- **Document the dual-mode auth.** rollback.sh v0.4's "Auth (v0.4)" comment block describes both modes explicitly. Future operators reading the script know what to expect in both contexts.

**Counter-pattern this prevents:** "I'll trust the previous job set things up correctly." That assumption held in the standards source for ~6 months because the only invocations of rollback.sh were manual (humans who'd run docker login). Auto-rollback wiring (Task 3.4) exposed the bug. The bug existed all along; we just couldn't see it until the gate fired.

**Architecture parallel:** deploy.sh v3.0 already followed this pattern — does its own docker login at script start (memory rule #18 / D8 documents the side effect: deploy.sh overwrites operator's docker auth). F-1 brings rollback.sh to architectural parity. **What's left:** D8's broader fix (deploy.sh save/restore docker auth so manual rollback workflow isn't broken by CI deploys) is still deferred. L019 doesn't claim to solve D8 wholesale — it documents the correct pattern; D8 manual variant is "honor the pattern in deploy.sh too."

**When to apply L019:**
- Building any new CI job that depends on remote-host state → establish state explicitly at job start
- Refactoring an existing CI job that's been "trusting" between-job state → migrate to self-sufficient pattern
- Reviewing a script invoked from CI → check whether it makes assumptions about pre-existing state on the remote host
- After a deliberate-failure test reveals an auth gap → the gap is almost always a between-job state assumption (L018); the fix is almost always self-containment (L019)

**Related lessons:**
- L009 (deliberate-failure testing — surfaced this pattern's evidence)
- L013 (cascade observation — L019's benefit is "iteration 1 success" instead of "iteration 2 surprise")
- L016 (allow-failure jobs become decoration — L019 fix only matters because rollback jobs are NOT allow_failure; the fix would have been hidden under allow_failure)
- L018 (anti-pattern this resolves)

**Anti-pattern this prevents:** Designing for the convenience of "the deploy job already logged in, so the rollback job doesn't have to." That convenience is exactly what fails when the deploy and rollback jobs are far apart in time, when tokens rotate, or when other jobs run between them.

---

### L018 — Cross-job auth state assumptions break silently in CI

**Date:** 2026-04-29
**Project:** a reference project
**Phase / Task:** Phase 3 Task 3.4 deliberate-failure test cycle (post-Phase-3-close)

**Context:** Auto-rollback CI wiring (added in commit 00e711c) needed end-to-end verification per L009 (deliberate-failure testing) + L013 (cascade observation). Test cycle: push deliberately-broken commit A → smoke-staging fails → rollback-staging auto-fires → rollback.sh runs → recovery → push commit B revert.

**What happened:** Iteration 1 of the test cycle revealed an auth bug. The rollback-staging CI job invoked `rollback.sh` on the VPS, which tried to `docker pull` the previous-good-SHA images. The pull failed with `HTTP Basic: Access denied` because:
- `deploy-staging` (earlier in the same pipeline) had done its own `docker login` with CI's `$CI_REGISTRY_USER`/`$CI_REGISTRY_PASSWORD`, overwriting VPS 1's `~/.docker/config.json`
- That CI-job-scoped token had expired (or lost permissions) by the time rollback-staging ran (~10-30 min later, depending on test+deploy+smoke duration)
- `rollback.sh` was designed assuming "operator already logged in" — true for manual SSH invocations, NOT true for cross-job CI invocations

**The lesson:** Any CI job that depends on PERSISTENT state on a remote host (docker auth, session tokens, file locks, etc.) between jobs is fragile. The state can be invalidated by:
- Token/credential expiration (CI tokens are typically minutes to hours, not the duration of the gap between jobs)
- Other CI jobs overwriting the state (deploy.sh writing fresh credentials, then those credentials expiring)
- Manual operator intervention between jobs (someone logged in elsewhere, rotated a token)
- The state never being established in the first place (the assumption was always wrong)

**Pattern to refuse:** Designing a CI job that says "I'll use whatever auth/state is on the VPS." Either:
- Establish the state explicitly inside the job (e.g., `docker login` as a script step), OR
- Use auth that doesn't require persistent state (e.g., short-lived tokens passed inline per command)

**Pattern to adopt:** Self-contained CI jobs. Each job that needs auth establishes it itself, doesn't assume previous jobs left it.

**the standards source-specific manifestation:** Memory rule #18 (D8 in cicd_setup_tracker.md) documented the manual-rollback variant since 2026-04-24 ("manual rollback.sh invocations on VPS 1 fail until operator re-logs in"). The auto-rollback CI variant was theorized but not proven until tonight's test cycle.

**Fix path for the standards source (F-1):** Add explicit `docker login registry.gitlab.com -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD` step to both `rollback-staging` and `rollback-production` jobs in `.gitlab-ci.yml`. Mirrors the auth pattern already in `deploy-staging` and `deploy-production`. Self-contained per CI job. No shell script bumps. After F-1 lands, MUST re-run staging deliberate-failure test cycle to verify.

**Related lessons:** L009 (deliberate-failure testing — surfaced this bug), L013 (cascade observation — auth was iteration-2 surprise), L016 (allow-failure jobs become decoration — this bug WOULD have been hidden by allow_failure: true on rollback jobs, but per Task 3.4 design rollback jobs are NOT allow_failure).

**Anti-pattern this prevents:** "I'll trust the previous job set things up correctly." In CI, never trust between-job state on remote hosts. Each job that needs state establishes it.

---

### L017 — Never-exercised gates fire bugs in cascade

**Date:** 2026-04-28
**Project:** a reference project
**Phase / Task:** Phase 3 X11 closure (nightly schedule + Telegram wiring)

**Context:** Phase 3 X11 (nightly pipeline schedule) was created Sunday 2026-04-26 — the YAML for the `nightly:` job had been added in Phase 2, but the schedule that would actually fire it had never been created. Per L013 (project knowledge precedence) earlier observation that "gates that have never been exercised cannot be trusted," fired the schedule manually before relying on it for Monday's prod deploy work.

**What happened:** Three sequential failures, each fix revealing the next layer's bug:

1. **First fire (2026-04-26):** Scheduled tier failure — `validate_eurusd` and `validate_us30` validators failed against the 80-row CI fixture DB (insufficient bars for 8-point pattern detection). Diagnosed as architectural mismatch (validators designed for full backtest data, not synthetic fixtures). **Filed as D12, parked the scheduled tier from CI nightly per Path B.**

2. **Second fire (after Path B fix):** `TELEGRAM_BOT_TOKEN not set — skipping notification` warning surfaced in the log. Discovered the nightly job reads `TELEGRAM_BOT_TOKEN` but only `TELEGRAM_STAGING_BOT_TOKEN` existed in GitLab vars (set same-day, untracked until investigation forced it into view). **Filed as X21, wired Resolution 1 — YAML aliasing in nightly job's `variables:` block.**

3. **Third fire (after Resolution 1):** `Telegram send failed: HTTP Error 400 Bad Request`. Diagnostic curl from VPS 1 with `.env` values succeeded immediately, revealing GitLab's `TELEGRAM_STAGING_CHAT_ID` pointed to the original Phase 1 group chat ID (`-100...` format) while VPS 1 `.env` had been updated to the user's private DM chat ID (positive integer). Two systems pointed at different chats. **Updated GitLab var to private chat ID, removed unnecessary masking flag.**

4. **Fourth fire:** `Telegram: full (1/1 chats)` — fully green.

**The lesson:** Each fix reveals the next layer's bug. Plan for 3-5 iterations before a never-exercised gate is fully green. Don't celebrate at iteration 1.

**Why this happens:** Untested code paths accumulate latent assumptions. When the gate finally fires, ALL of those assumptions get tested simultaneously. Some pass, some fail, the failing ones get fixed, and the next set of latent assumptions becomes visible.

**Practical implications:**
- Budget 1-2 hours of iteration time when first exercising any new automated gate
- Don't schedule the first fire of a gate close to a deadline
- Each fix should be its own commit (don't batch fixes together — they obscure the cascade)
- Track each iteration in the project's CI/CD tracker so the cascade is visible in retrospect

**Related lessons:** L013 (project knowledge precedence), L009 (deliberate-failure testing).

**Anti-pattern this prevents:** "It worked once in dev, ship it" — the first manual fire is dev. Production-grade automated gates need 3-5 iterations before they're trustworthy.

---

### L016 — Allow-failure jobs become decoration, not checks

**Date:** 2026-04-25
**Project:** a reference project
**Phase / Task:** Phase 3 Task 3.5

#### Incident

The `validate:` CI job had been failing every master push for ~10 weeks with no DB seeding available, marked `allow_failure: true` to "let it run while we figure out the DB seeding." The fix (`validation/fixtures/seed_ci_db.py`) landed 2026-04-19, providing the DB seeding the job needed. But the job stayed on `allow_failure: true` because nobody re-litigated it. The nightly `scheduled` tier was correctly using `seed_ci_db.py` and producing real coverage — meanwhile the `validate:` job kept failing silently on every master push.

When auditing the pipeline for Phase 3 close-out, the `validate:` job stood out as zero-value: it ran the same validators the nightly job already ran (with seeding), failed every time (without seeding), and was hidden behind `allow_failure`. Pure pipeline noise.

The pattern: a job that "passes when allowed to fail" trains operators to ignore the red X. Eventually, the red X becomes invisible — the job is decoration.

#### Cost

10 weeks of red Xs on master. Lost signal value on the entire pipeline UI — operators learned to ignore the test stage's appearance. Real failures elsewhere would have blended in.

Removal took 1 commit (Task 3.5, ~50 minutes of work). Should have been removed the day `seed_ci_db.py` landed.

#### Codification

New entry in `PROMPT_STANDARDS.md` § 6 (anti-patterns, future addition) and reinforced in CI/CD review discipline:

> Sustained `allow_failure: true` is technical debt that trains operators to ignore failures. When the underlying rationale changes (e.g., DB seeding becomes available), revisit the job: either restore real teeth (remove `allow_failure`) or remove the job entirely. Don't leave it as decoration.

#### Cross-references

- `CICD_STANDARDS.md` § Job conventions (planned)
- `archive/postmortems/2026-04-25-task-3.5-validate-removal.md` (the close-out incident block)

---

### L015 — Project Instructions for one project bleed into another

**Date:** 2026-04-25
**Project:** Cross-project
**Phase / Task:** Standards-repo design discussion

#### Incident

While designing the standards repo, the question came up: where do project-specific facts (Mac repo path, VPS IPs, deploy tokens) belong? The original instinct was user-wide memory — the same place where session protocols and Cursor prompt format already lived. But user-wide memory means **every project's session** sees those facts. Working on Project B, the agent would inherit Project A's IPs and paths and confidently apply them.

The realization: facts have scopes. A session protocol applies cross-project; a VPS IP applies to one project only. Mixing them in user memory creates context bleed — the wrong project's facts firing in the wrong project's session.

#### Cost

Hypothetical-but-likely cost. The bleed would have happened the moment a second project entered the picture. Caught during standards-repo design instead of in production, but only because the design phase forced explicit scope analysis.

#### Codification

Three-tier structure in `PROJECT_INSTRUCTIONS_TEMPLATE.md`:
- Tier A: static frame (cross-project conventions reference)
- Tier B: project-specific facts (paths, IPs, commands, quirks) — lives in the Project Instructions field, scoped to that project only
- Tier C: per-session priorities — first user message, never persisted

The matching `MEMORY_PROTOCOL.md` § 7 disambiguation table makes the rule explicit: "Project-specific facts go in Project Instructions Tier B, not user-wide memory."

#### Cross-references

- `PROJECT_INSTRUCTIONS_TEMPLATE.md` § 2 (the three-tier structure)
- `MEMORY_PROTOCOL.md` § 7 (memory vs Project Instructions vs CLAUDE.md)
- `MEMORY_PROTOCOL.md` § 4.6 (anti-pattern: cross-project entries that should be project-specific)

---

### L014 — Long single-file standards docs lose recall in the middle

**Date:** 2026-04-25
**Project:** Cross-project
**Phase / Task:** Standards-repo design discussion

#### Incident

The first attempt at the standards documentation produced `PROJECT_STANDARDS.md` at 957 lines — a single comprehensive bible covering governance, engineering, lessons, adoption, everything. During design review, the user raised the lost-in-the-middle problem: AI agents reading long documents have high recall on the first ~10% and last ~5%, and noticeably lower recall on the middle 70%. A 957-line doc would mean rules buried at line ~600 would be inconsistently enforced.

Validated against actual session experience: the project's `CLAUDE.md` had grown to ~250 lines with 8 standing rules; even at that length, the rules in the middle were less consistently cited than rules at the top.

#### Cost

The 957-line bible would have shipped with quietly weak enforcement on its middle sections — exactly the rules the document was trying to make binding. The cost would have been invisible (rules not enforced inconsistently rather than not at all) but would have compounded over time.

#### Codification

Architectural decision: split the standards into focused files, each loaded by dispatcher pattern (CLAUDE.md routes the agent to the right file based on what work is in scope).

- Each focused file targets <600 lines (some run longer when topical depth earns it; PROMPT_STANDARDS.md is 866 lines and accepted)
- Topical coherence per file (one file = one topic) preserves recall even at higher line counts
- Dispatcher in `CLAUDE.md` § 12 ensures agents only load relevant files

#### Cross-references

- `CLAUDE.md` § 12 (the dispatcher table)
- `PROMPT_STANDARDS.md` (an example of a longer focused file where topical coherence holds)

---

### L013 — Project knowledge precedence prevents fabrication

**Date:** 2026-04-22
**Project:** a reference project
**Phase / Task:** Multiple Phase 2 sessions

#### Incident

When repo state was ambiguous, agents would guess from training-data priors instead of consulting the actual project knowledge. Specific examples:

- Agent confidently stated a config key existed in `config/instrument_config.py` that didn't actually exist
- Agent referenced a function signature that matched a generic Python convention but not the project's actual code
- Agent recommended a deploy command pattern that worked for generic Python projects but not this project's specific Docker layout

Each fabrication was caught only when the user noticed the agent's output didn't match reality. The agent had no internal "I'm uncertain" signal — confident-sounding answers from training-data priors are indistinguishable from confident-sounding answers from project knowledge.

#### Cost

3-5 sessions of correcting fabricated facts before the rule was codified. Each correction was a turn of clarification, sometimes followed by re-doing work that was based on the wrong assumption.

#### Codification

Project knowledge precedence rule, codified in `PROJECT_INSTRUCTIONS_TEMPLATE.md` § 4 (Tier A) as a binding session protocol:

> When repo information is needed (file contents, current versions, doc text, config values), search project knowledge FIRST. If not found, ask me or read from disk. Never assume, guess, or compose from memory. Project knowledge is the authoritative source for repo state.

This is loaded by every Claude.ai session in the project, blocks the most common fabrication patterns by forcing the agent to verify before stating.

#### Cross-references

- `PROJECT_INSTRUCTIONS_TEMPLATE.md` § 4 (Tier A, project knowledge precedence)
- `CLAUDE.md` § 10 (AI Behavior Rules — "Project knowledge precedence")

---

### L012 — Gitignore case-sensitivity surprises on macOS

**Date:** 2026-04-22
**Project:** a reference project
**Phase / Task:** Task A (Telegram architecture documentation + Plans folder governance)

#### Incident

A new file in `docs/Plans/` (capital P) wouldn't show up in `git status`. Confusing — the file existed, was a normal `.md` file, and similar files under `docs/` were tracked normally. Spent an hour debugging: was it `.git/info/exclude`? A shell glob? A `git update-index --assume-unchanged` somewhere?

Eventually found `.gitignore` line 14: `docs/plans/` (lowercase). On macOS's case-insensitive default filesystem (HFS+, APFS), the lowercase pattern silently matched `docs/Plans/` (capital P). Linux contributors wouldn't have hit this — case-sensitive filesystems would have treated the patterns as distinct.

The rule had been added historically when planning was treated as throwaway (the `plans/` folder was meant to be ignored). When the model shifted to "all plans committed" (Task A), the case-mismatch caught the new files silently.

#### Cost

~1 hour of debugging. Two existing plan files predated the gitignore rule and were tracked; new files weren't, with no error message explaining why.

#### Codification

Pattern in `LESSONS.md` and informal rule for the project: when adding `.gitignore` entries for directories, match the case used in the repo exactly. Treat case mismatches as bugs.

Codified more broadly: any `.gitignore` change should be tested by adding a file matching the new ignore pattern and verifying `git status` shows or hides it as expected.

#### Cross-references

- `archive/postmortems/2026-04-22-gitignore-case-bug.md` (this incident; if elevated to a postmortem)

---

### L011 — Pager-safe verification (avoid `less` ambushing output)

**Date:** 2026-04-23
**Project:** a reference project
**Phase / Task:** Multiple Phase 2 sessions

#### Incident

Cursor ran `git log --stat` to verify a commit. The output was paged through `less`, which captured stdin and froze the agent waiting for the user to press `q`. From the user's perspective, the agent had hung; from the agent's perspective, it was waiting on a command that never returned.

This happened multiple times before the pattern was named. Easy fix once identified, but the failure mode is invisible to the agent (no error, just no return).

#### Cost

Each occurrence cost a session interruption — user had to notice the freeze, recognize what was happening, manually intervene. ~5 minutes per incident, ~3-4 incidents observed before codification.

#### Codification

Pipe potentially-paged output through `| cat`:
```
git log -1 --stat | cat
git log --grep "pattern" --stat | cat
```

Or set `PAGER=cat` for the session/agent environment.

#### Cross-references

- `PROMPT_STANDARDS.md` (planned addition to anti-patterns)

---

### L010 — Split-commit delivery for substantive doc additions

**Date:** 2026-04-22
**Project:** a reference project
**Phase / Task:** Task A (Telegram architecture docs + governance wiring)

#### Incident

A large doc addition + governance wiring landed as one commit on the first attempt. A content review surfaced an issue requiring an amendment to the Telegram architecture doc — but by then the wiring commit had built cross-references on top of the original content. Amending the original meant the wiring also had to be re-checked for consistency.

Made the same mistake on Task C (the CI/CD docs) before recognizing the pattern: substantive content and mechanical wiring should be separate commits.

#### Cost

Task A required 2 attempted amends before a clean amend was achievable. ~30 minutes of unnecessary back-and-forth caused by content + wiring entanglement.

#### Codification

Pattern: split commits for substantive doc additions:
- Commit 1: the risky content (doc additions, sections, examples) — amend freely while local
- Commit 2: the mechanical wiring (manifest entries, CHANGELOG, cross-references in other docs) — built on Commit 1's stable state

Used successfully for Tasks A (Parts 1+2), C (Parts 1+2a+2b), and others throughout Phase 2.

#### Cross-references

- `PROJECT_STANDARDS.md` (planned: commit discipline section)
- `CLAUDE.md` § 11 (commit policy — references the pattern)

---

### L009 — Deliberate-failure testing for alerting/check code

**Date:** 2026-04-22
**Project:** a reference project
**Phase / Task:** Tasks 2.5d (image source verification), Task M (healthcheck Telegram delivery)

#### Incident

Several alert paths and verification checks had been added that "worked" — they passed under correct conditions. Months later, when an actual failure occurred, the alert didn't fire. Investigation: a syntax bug in the failure path (the branch that handled the alert dispatch) had never been exercised because nobody had ever deliberately broken the system to test it.

The pattern: standard "happy path" testing only validates the success branch. Failure branches need explicit failure injection to validate.

Tasks 2.5d and Task M both followed this pattern explicitly: deliberately broke the system (changed an image to an unexpected one; stopped the `charts` container) and confirmed the alert fired correctly. Both caught real bugs in the failure path that the happy-path testing had missed.

#### Cost

The original silent-failure incident cost real operational visibility for ~2 weeks before someone manually noticed a service was down. After codification, deliberate-failure testing has caught 3+ would-have-been-silent bugs at the time of writing.

#### Codification

Mandatory pattern in `VALIDATION_STANDARDS.md` (planned) and as a checklist item in `CLAUDE.md` § 8 (Validation checklist):

> For new alerting/check code: deliberate-failure test was run and confirmed the failure path works.

Explicit phrasing: "passes when correct" is insufficient — code must also "fail when broken."

#### Cross-references

- `VALIDATION_STANDARDS.md` (planned, primary location)
- `CLAUDE.md` § 8.4 (validation checklist — testing)
- `PROMPT_STANDARDS.md` (planned: deliberate-failure as a verification pattern)

---

### L008 — Manifest completeness: no exclusion lists

**Date:** 2026-04-23
**Project:** a reference project
**Phase / Task:** Phase 3 Task 3.0 (manifest completeness sweep)

#### Incident

Manifest entries had drifted out of sync with the filesystem over weeks. New `.md` files weren't registered. Deleted files lingered in the manifest. Allowlist exceptions for "intentional orphans" had accumulated until nobody remembered why each was on the list. The manifest was supposed to be the version index; instead it was a stale, partial inventory.

Phase 3 opened with a forced reckoning: manifest completeness sweep (Task 3.0) — every committed `.md` file and every VERSION-bearing code file had to be accounted for. Result: 32 entries appended (positions 140-171), bringing total to 171 entries. Allowlist abandoned.

#### Cost

Drift had been silent for ~3 months. Cost was ~4 hours of audit work in Task 3.0 to bring the manifest current. Ongoing cost would have been higher: the manifest's value as a version index degrades quickly as drift accumulates.

#### Codification

CLAUDE.md Rule 8 (Manifest completeness):

> `docs/documents_manifest.md` must list every committed `.md` file and every tracked code file (`.py`/`.sh` with VERSION header). No exclusion lists are maintained — unused files must be removed, not allowlisted.
>
> - New `.md` files register in the manifest in the same commit that creates them.
> - New code files with VERSION headers register in the same commit.
> - Deleted tracked files have their manifest entry removed in the same commit.

Enforcement deferred to `check_doc_coverage.py` long-term; obligation on the author until then.

#### Cross-references

- `CLAUDE.md` § 3 Rule 8 (the rule itself)
- `PROJECT_STANDARDS.md` (planned: manifest structure section)

---

### L007 — Multi-file Cursor prompts need ALLOWLIST + verbatim FIND/REPLACE

**Date:** 2026-04-23
**Project:** a reference project
**Phase / Task:** Task C Part 2b (CI/CD documentation + governance wiring)

#### Incident

Multi-file Cursor prompts written in prose ("update the relevant section to reflect the new behavior") produced inconsistent output. Three failure modes:

1. **Stylistic drift:** Cursor composed text from descriptions, introducing tone and vocabulary that didn't match the rest of the project's docs.
2. **Hallucinated section headers:** Cursor invented a section header ("§ 5: Deploy stage details") that didn't exist in the source file, then "updated" it.
3. **Plausible-but-wrong content:** Cursor added factually incorrect statements that read fluently but weren't true (e.g., "the deploy script uses rsync" when it had been refactored to use registry-pull).

All three were caught only because the user reviewed the output before commit. Without manual review, all three would have shipped silently.

#### Cost

3-4 prompts had to be redrafted with verbatim FIND/REPLACE blocks instead of prose descriptions. Each redraft was ~10 minutes; the manual review caught issues that would have cost much more if shipped (silent doc errors compound — they get cited as truth by future contributors).

#### Codification

CLAUDE.md Rule 7 (Multi-file AI prompt construction). Full template in `PROMPT_STANDARDS.md` § 3.

Required components:
1. Explicit ALLOWLIST of files
2. Verbatim find-and-replace blocks (never prose descriptions)
3. Mandatory "files modified" checklist
4. No ambiguous hedges

Verbatim FIND/REPLACE eliminates all three failure modes — the agent is doing string substitution, not authorship.

#### Cross-references

- `CLAUDE.md` § 3 Rule 7 (the binding rule)
- `PROMPT_STANDARDS.md` § 3 (full template)
- `PROMPT_STANDARDS.md` § 6.5 (anti-pattern: prose-described changes)

---

### L006 — Verify agent claims via filesystem

**Date:** 2026-04-23
**Project:** a reference project
**Phase / Task:** Task C Part 2b

#### Incident

AI agent reported "task complete, all files updated." User trusted the claim and pushed. The CI run failed: doc coverage script complained about missing manifest entries. Investigation: of the 4 files the agent claimed to have updated, only 2 had actually been modified. The agent had described what it intended to do without doing it.

This wasn't malicious — the agent had genuinely "intended" to update all 4, but two of the edits had silently failed (or never been attempted) without the agent realizing. The output looked completion-shaped because the agent was reporting on its plan, not on the filesystem.

#### Cost

1 broken pipeline. ~30 minutes to diagnose, manually fix the missed edits, push the fix as Task C Part 2b-fix (per L003, Rule 3 — fix-forward). Lost trust in agent self-reports for ~1 week.

#### Codification

CLAUDE.md Rule 6 (Verify agent claims via filesystem):

> Agent "done" claims are not authoritative — filesystem state is.
>
> - Before every `git add` in a multi-file commit, run `git status --short` to confirm the file set matches the prompt's ALLOWLIST.
> - Missing files, unexpected additions, or unintended modifications must be surfaced and resolved, not silently absorbed.
> - If `git status` shows a mismatch against expectations, STOP. Do not proceed with `git add` or `git commit` until the discrepancy is understood.
> - When a governance script says "passed," paste its full stdout/stderr verbatim. Self-reported "exit 0" without output is unacceptable.

Operational pattern: every multi-file Cursor prompt now includes mandatory `git status --short` before AND after `git add`.

#### Cross-references

- `CLAUDE.md` § 3 Rule 6 (the binding rule)
- `PROMPT_STANDARDS.md` § 3.7 (commit step structure with mandatory pre/post status checks)

---

### L005 — Local governance does NOT validate CI schema

**Date:** 2026-04-22
**Project:** a reference project
**Phase / Task:** Task 2.6 (post-deploy smoke gating)

#### Incident

A `.gitlab-ci.yml` change introduced a `needs:` cross-stage dependency (gating production deploy on staging smoke success). Locally:
- `python -c "import yaml; yaml.safe_load(...)"` → parsed cleanly
- `check_doc_coverage.py` → exit 0
- `check_test_coverage_drift.py --ci` → exit 0

Pushed. GitLab pipeline failed at pipeline-creation time: the `needs:` reference pointed at a job in a stage that wasn't actually defined. Local checks couldn't catch this because they validate Python syntax and YAML syntax — not GitLab-specific job-graph semantics.

The lesson: there's a class of CI defects that local checks structurally cannot catch. Pipeline-run is the only validation.

#### Cost

1 broken pipeline on push. ~20 minutes to diagnose (the GitLab error message about `needs:` was clear once located). Fix landed as Task 2.6b per L003 (fix-forward).

#### Codification

CLAUDE.md Rule 5:

> Local checks (YAML parse, doc coverage, test coverage drift) validate Python syntax and YAML syntax — not GitLab/GitHub-specific semantics like `needs:`, `stage:`, `rules:`, `dependencies:`, or stage-graph correctness.
>
> For any change to `.gitlab-ci.yml` (or `.github/workflows/`) that touches those keys, the dispositive validation is a real pipeline run.

Two acceptable paths:
- Accept that the first push may surface CI defects, then fix-forward per Rule 3
- Validate against the GitLab CI Lint API / GitHub Actions linting before push

#### Cross-references

- `CLAUDE.md` § 3 Rule 5 (the binding rule)
- `CLAUDE.md` § 11 (commit policy — fix-forward as the response to CI defects)
- `CICD_STANDARDS.md` (planned: pipeline change validation section)

---

### L004 — Heredoc-piped commit messages corrupt special characters

**Date:** 2026-04-21
**Project:** a reference project
**Phase / Task:** Phase 2 (Task 2.5)

#### Incident

A multi-paragraph commit message containing backticks, em-dashes, and the rocket emoji was delivered via:

```bash
git commit -m "$(cat <<EOF
Phase 2 Task 2.5: ...
... `code reference` and — em-dash and 🚀 ...
EOF
)"
```

The commit appeared clean. Push succeeded. ~3 weeks later, doing `git log --grep '`code reference`'` to find the commit returned nothing. The backticks had been silently mangled — the actual commit message contained `\code\ reference\\` with broken escape sequences. The em-dash was replaced with a question mark in some downstream tools that did character-set conversion. The emoji had become a `?`.

Investigation: heredoc + shell expansion + double quotes around the `$` interaction is fragile. Some characters survive; others get mangled silently. Easy to get wrong; easy to not notice.

#### Cost

The commit was unrecoverable without a force-push (which Rule 3 forbids for pushed commits). Lost the ability to grep for that commit by its content forever. Roughly 8 commits across Phase 2 had similar corruption before the pattern was identified.

#### Codification

CLAUDE.md Rule 4 (Commit messages via `-F /tmp/<file>`):

> Multi-paragraph commit messages containing backticks, code blocks, em-dashes, arrows, or any special shell metacharacters must be delivered via:
>
> ```
> git commit -F /tmp/commit_msg.txt
> ```
>
> Never `git commit -m "..."` with escapes. Never heredoc piped to `git commit`.

The single-quoted heredoc to `/tmp/<file>` followed by `git commit -F` is the only pattern that preserves special characters reliably.

#### Cross-references

- `CLAUDE.md` § 3 Rule 4 (the binding rule)
- `PROMPT_STANDARDS.md` § 3.7 (commit step in multi-file prompts)
- `PROMPT_STANDARDS.md` § 6.2 (anti-pattern: heredoc piped to git commit)

---

### L003 — Fix-forward via letter suffix preserves the lesson

**Date:** 2026-04-22
**Project:** a reference project
**Phase / Task:** Task 2.5b

#### Incident

Task 2.5 shipped, CI failed on the first push. The natural reaction was `git commit --amend` to fix the issue, then `git push --force` to update the broken commit. Worked operationally — pipeline went green.

Six weeks later, a similar bug recurred (a Docker compose substitution silently used the wrong image source). When investigating, nobody could find the original Task 2.5 failure to learn from — the amend had erased it from history. The lesson had to be re-learned the hard way.

The pattern: pushed commits are visible to all reviewers, all history-walkers, all `git blame` users. Erasing them with force-push deletes both the failure and the context that made the failure useful.

#### Cost

Task 2.5b would have been a smaller, faster commit had the original Task 2.5 failure been preserved as a lesson. Re-learning the silent-substitution pattern took ~2 hours of investigation that could have been a 5-minute "remember Task 2.5? Here's the same class of bug."

#### Codification

CLAUDE.md Rule 3:

> When a pushed commit fails its first CI run (a defect that could not be caught locally), the fix lands as a new sub-task with letter suffix (e.g., Task 2.5b, Task 3.2b), not as `git push --force` of an amended commit.
>
> - Letter-suffix sub-tasks preserve the failure and the lesson in git history.
> - Force-push erases both — the broken state and the learning.
> - Local-only commits (not yet pushed) may be amended freely.

Used consistently across Phase 2 (2.5b, 2.5c, 2.5d, 2.6b, 3.1b, 3.2b). Each letter-suffix commit's history is now a teachable case study.

#### Cross-references

- `CLAUDE.md` § 3 Rule 3 (the binding rule)
- `CLAUDE.md` § 11 (commit policy — fix-forward section)
- `PROMPT_STANDARDS.md` § 6.4 (anti-pattern: force-push of pushed commit)

---

### L002 — Pre-push governance must be local AND in CI

**Date:** 2026-04-22
**Project:** a reference project
**Phase / Task:** Task 2.6b, Task A Part 1

#### Incident

Doc coverage and ownership-map drift were caught by CI after push, costing pipeline round-trips. Local checks (`check_doc_coverage.py`, `check_test_coverage_drift.py`) existed but were not consistently run before push. The mental model was "CI catches it, so I don't have to."

CI catches it costs ~3-5 minutes of pipeline time per round-trip (pipeline starts, governance job runs, fails, you fix, push again). Multiplied across many sessions, this is real friction. Worse: the CI failure is visible to anyone watching the pipeline, signaling sloppiness.

Cursor noticed this pattern proactively during Tasks 2.6b and Task A Part 1 — running governance scripts locally before push surfaced gaps that would have failed CI. After ~3 instances, the pattern was codified.

#### Cost

Approximate cost in Phase 2 (across all tasks before codification): ~10-15 pipeline round-trips that could have been avoided with local pre-push runs. Each round-trip = ~5 minutes. Total: ~1 hour of avoidable wait time.

#### Codification

CLAUDE.md Rule 2:

> Before every `git push`, run locally:
>
> ```
> python scripts/check_doc_coverage.py
> python scripts/check_test_coverage_drift.py --ci
> ```
>
> Both must exit 0. CI runs them too — catching failures locally saves pipeline round-trips.

Both governance scripts are project-specific (live in `scripts/`) but the rule that they MUST run pre-push is binding cross-project.

#### Cross-references

- `CLAUDE.md` § 3 Rule 2 (the binding rule)
- `CLAUDE.md` § 8.5 (validation checklist — pre-push governance)
- `PROMPT_STANDARDS.md` § 3.6 (pre-commit governance verification in multi-file prompts)

---

### L001 — Plans folder rule (commit your plans)

**Date:** 2026-04-22
**Project:** a reference project
**Phase / Task:** Task A (Telegram architecture documentation)

#### Incident

Planning notes for the project's evolution lived in three places simultaneously:
- `/tmp/` files from earlier sessions
- Chat scrollback in Claude.ai
- A draft GitHub issue that was started but never finished

When a plan needed revisiting, three different versions existed and none was authoritative. Each version had partial content; reconstructing the complete plan required cross-referencing all three. This happened multiple times before the pattern was named.

The realization: plans are first-class artifacts. They shape later work and are referenced months after creation. Treating them as throwaway means losing the design rationale at the worst possible time.

#### Cost

~3 hours across Phase 2 spent reconstructing plans from fragmented sources. Multiple "wait, did we decide X or Y?" questions that should have been resolvable by reading a committed plan.

#### Codification

CLAUDE.md Rule 1:

> All planning documents live under `docs/Plans/` and are committed to git. Plans are not throwaway. They get version headers and entries in the manifest like any other document.
>
> Never put plans in `/tmp/`, in chat scrollback, in a Notion page, in a gitignored folder, or anywhere else. If a plan is worth writing, it is worth committing.

Backed by a pre-existing `docs/Plans/` directory and a `.gitkeep` file (with the case-mismatch fix from L012 applied to the `.gitignore`).

#### Cross-references

- `CLAUDE.md` § 3 Rule 1 (the binding rule)
- `archive/postmortems/2026-04-22-plans-folder-fragmentation.md` (this incident; if elevated to a postmortem)

---

## End of archive

This file is the institutional memory of why the standards exist. When a future contributor proposes removing or relaxing a rule, the relevant lesson here is the evidence that has to be addressed — not just dismissed.

When adding a new lesson, follow the format in § 2, number it sequentially, and add the entry at the **top** of § 3 (newest first). Update the Table of Contents to include the new entry. Bump the file's VERSION header and add a CHANGE LOG line for the new lesson.
