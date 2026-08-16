<!-- VERSION: 1.6 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Source: docs/standards/ (this repo). Bootstrapped from Standard Set v1.0 on 2026-06-07. Independent versions from this point forward. -->
<!--
CHANGE LOG
v1.6 — 2026-08-16 — Standard Set Version v1.4 adoption: § 15.2 Phase-1 deliverable now requires the § 7 ALLOWLIST to include the plan + sibling-tracker promotion rows (L054); § 15.3 adds the Phase-3 reconcile-first duty (L056). No rule added or removed.
v1.5 — 2026-06-23 — PLAN-007 (remote-target transport): § 1 deployment shape retired "operates on local repository checkouts / no remote infrastructure" → "local OR remote (git/ssh) checkouts via a pluggable transport; still no server/deploy infra of its own." Project-specific (root copy only; template § 1 placeholder untouched) — no Set Version bump (engine-only change, no docs/standards/ edit).
v1.4 — 2026-06-20 — § 4 Critical files: dropped the stale "(created when the engine lands)" note on src/standard_document_updater/ (package now exists); promoted config/projects.toml (the target-suite registry) to a Critical File and updated the "Future critical files" list accordingly. Project-specific (root copy only; template § 4 generic, untouched) — no Set Version bump.
v1.3 — 2026-06-17 — Add Rule 14 (durable project memory across machines/folder moves). PLAN-005 (Standard Set Version v1.2).
v1.2 — 2026-06-14 — Project display name renamed to "Standard DocSet" (§ 1). Engine package identifier `standard_document_updater` kept unchanged (Option B). GitLab project + remote renamed to slug `standard-docset`.
v1.1 — 2026-06-13 — PLAN-002 (Slice 1): wrapped this repo's project-owned blocks (§ 1 context, § 4 critical files, § 13 domain bullet, § 14 single-agent stub) in PROJECT-OWNED markers so a future sync preserves them; fixed the stale "created when the engine lands" drift on the two docs/architecture.md references (§ 4 drift rule + § 13 domain bullet) now that the doc exists. Adopts Standard Set Version v1.1.
v1.0 — 2026-06-07 — Project bootstrap. Operating contract instantiated from the standards suite at Standard Set Version v1.0 (13 standing rules, 49 lessons L001–L049). Customized for Standard DocSet: § 1 project context (domain-neutral Python CLI tool), § 4 critical files, § 13 single sources of truth. Single-agent project — the optional Codex handoff section (§ 14 in the template) was removed; § 15.7 tracker Owner header noted as optional. All 13 standing rules, change-classification, change-workflow, validation checklist, dispatcher, and § 15 plan workflow retained verbatim from the v1.0 template (domain-neutral). Independent versions from this point forward; backports from the standards source are explicit (see docs/standards/STANDARDS_INDEX.md).
-->

# CLAUDE.md — Operating Contract

**This file is binding for every contributor (human and AI) on this repository.** It is read on every session by AI coding agents (Cursor, Claude Code, Copilot, etc.). The rules below override default agent behavior.

If a rule below conflicts with a request, **refuse or propose a compliant alternative** — do not silently override the rule.

---

## 1. Project context

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
**Project:** Standard DocSet
**Domain:** Domain-neutral CLI tool that keeps standards / governance documentation suites up to date and synchronized across any project it is given access to. Reads, diffs, version-bumps, and propagates standards documents (and their per-file VERSION headers, CHANGE LOGs, manifests, and Set-Version state) between a source suite and one or more adopting project repositories. Not tied to any single project's domain — the projects it operates on are inputs, supplied at runtime.
**Primary languages:** Python 3.11+ (with strict typing via mypy, tests via pytest, lint/format via ruff)
**Deployment shape:** Local CLI tool — installed and run on the operator's machine; operates on local **or** remote (git/ssh) repository checkouts via a pluggable transport layer (PLAN-007). Still no server/deploy infrastructure of its own — git/ssh/rsync reach repos where they already live, using the operator's existing credentials.
**Multi-agent:** No — single-agent (Claude only). The Codex handoff protocol (§ 14 in the standards template) is intentionally omitted.
<!-- PROJECT-OWNED:END -->

---

## 2. Source of truth

- **The repository is the single source of truth.** If memory, prior conversation, or cached context disagrees with what is in the repo right now, **trust the repo**. Verify via filesystem (`git status`, `cat`, `grep`) before acting.
- **The on-disk files of the suite being operated on are the single source of truth for that suite's state** — the tool never trusts a cached or remembered version of a target project's standards; it re-reads the files (VERSION headers, manifest, STANDARDS_INDEX) before acting on them.
- **Agent claims are not authoritative; filesystem state is.** "Done" is a hypothesis until `git status --short` and the relevant `grep` confirm it.

---

## 3. The 13 standing rules (binding always)

These rules apply to every interaction, regardless of task. They are numbered for stable reference (e.g., "per Rule 4"). Numbering never changes — only append.

### Rule 1 — Plans folder

All planning documents live under `docs/Plans/` and are **committed to git**. Plans are not throwaway. They get version headers and entries in the manifest like any other document.

Never put plans in `/tmp/`, in chat scrollback, in a Notion page, in a gitignored folder, or anywhere else. If a plan is worth writing, it is worth committing.

### Rule 2 — Pre-push governance is mandatory

Before every `git push`, run locally:

```bash
python scripts/check_doc_coverage.py
python scripts/check_test_coverage_drift.py --ci
```

Both must exit `0`. CI runs them too — catching failures locally saves pipeline round-trips.

If either fails: fix the gap, or add a justified entry to `scripts/doc_coverage_allowlist.toml` with metadata (rule, reason, author, date, expires). Do not push with failing governance checks.

### Rule 3 — Fix-forward via letter suffix

When a pushed commit fails its first CI run (a defect that could not be caught locally), the fix lands as a **new sub-task with letter suffix** (e.g., `Task 2.5b`, `Task 3.2b`), not as `git push --force` of an amended commit.

- Letter-suffix sub-tasks preserve the failure and the lesson in git history.
- Force-push erases both — the broken state and the learning.
- **Local-only commits (not yet pushed) may be amended freely.**

### Rule 4 — Commit messages via `-F /tmp/<file>`

Multi-paragraph commit messages containing backticks, code blocks, em-dashes, arrows, or any special shell metacharacters **must** be delivered via:

```bash
git commit -F /tmp/commit_msg.txt
```

**Never** `git commit -m "..."` with escapes. **Never** heredoc piped to `git commit`. Both are silent-corruption patterns: the commit appears clean but Unicode and quoting are silently mangled. Discovered weeks later when grep'ing history yields nothing.

Write the message file with a single-quoted heredoc (preserves backticks literally):

```bash
cat > /tmp/commit_msg.txt <<'EOF'
First line summary

Body paragraph with `backticks` and em-dashes — preserved correctly.
EOF
```

### Rule 5 — Local governance does NOT validate CI schema

Local checks (YAML parse via `python -c "import yaml; yaml.safe_load(...)"`, `check_doc_coverage.py`, `check_test_coverage_drift.py`) validate Python syntax and YAML syntax — **not** GitLab/GitHub-specific semantics like `needs:`, `stage:`, `rules:`, `dependencies:`, or stage-graph correctness.

For any change to `.gitlab-ci.yml` (or `.github/workflows/`) that touches those keys, the **dispositive validation is a real pipeline run**.

Two acceptable paths:
- Accept that the first push may surface CI defects, then fix-forward per Rule 3.
- Validate against the GitLab CI Lint API / GitHub Actions linting before push.

### Rule 6 — Verify agent claims via filesystem

Agent "done" claims are **not authoritative** — filesystem state is.

- Before every `git add` in a multi-file commit, run `git status --short` to confirm the file set matches the prompt's ALLOWLIST.
- Missing files, unexpected additions, or unintended modifications must be **surfaced and resolved**, not silently absorbed.
- If `git status` shows a mismatch against expectations, **STOP**. Do not proceed with `git add` or `git commit` until the discrepancy is understood.
- When a governance script says "passed," **paste its full stdout/stderr verbatim**. Self-reported "exit 0" without output is unacceptable.

### Rule 7 — Multi-file AI prompt construction

Any AI-agent prompt (Cursor, Claude Code, etc.) that modifies more than one file **must** include:

1. **Explicit ALLOWLIST** of files the agent may touch. If any file outside the ALLOWLIST appears in `git status`, the agent must STOP and report.
2. **Verbatim find-and-replace blocks** or mechanical transformation rules for each edit — never prose descriptions of intended changes. Composition from descriptions produces stylistic drift and occasional semantic error; verbatim blocks eliminate both.
3. **Mandatory "Files modified this session" checklist** at the end of the prompt. The agent enumerates it in its final response. Discrepancy with `git status` must be raised, not absorbed.
4. **No ambiguous hedges** like "optionally," "if applicable," or "where relevant." Replace with explicit decision rules: "if X, do Y; otherwise skip and state so in your final output."

For the full prompt template and anchor-selection guidance, see `docs/standards/PROMPT_STANDARDS.md`.

### Rule 8 — Manifest completeness

`docs/documents_manifest.md` must list **every** committed `.md` file and **every** tracked code file (`.py`/`.sh` with VERSION header). No exclusion lists are maintained — unused files must be **removed**, not allowlisted.

- New `.md` files register in the manifest **in the same commit** that creates them.
- New code files with VERSION headers register in the same commit.
- Deleted tracked files have their manifest entry removed in the same commit.
- **Excluded from tracking:** `.cursor/rules/*.md` (tooling config), `.venv/`, `node_modules/`, `archive/`, anything that's gitignored.

### Rule 9 — Session start pre-flight is MANDATORY

Every new agent session in this repository MUST begin by reading [`docs/SESSION_OPENER.md`](docs/SESSION_OPENER.md) and executing its § 1 pre-flight (repo state, environment mapping, tracker tip, memory recall) BEFORE responding to the operator's first task. The § 4 first-response output block MUST be posted before any edit to a Critical File (§ 4), any commit, or any other action.

This is binding because repeat mistakes across sessions trace to a single root cause — skipping context-loading on session start and going straight to action. Knowledge encoded in memory (which target suites are registered, the per-file VERSION-bump discipline, the Set-Version adoption state, the plan-first discipline for vital changes) is recalled only when the agent thinks to recall it; without a forcing function that recall is unreliable. The pre-flight is the forcing function; the § 4 output block is the proof-of-pre-flight visible to the operator.

**Only permitted abbreviation:** operator explicitly says "skip pre-flight" (operator-only authorization — never self-skip). Even when abbreviated, the environment mapping (`SESSION_OPENER.md` § 2) and the project failure-mode catalog (`SESSION_OPENER.md` § 3) remain in force; only the § 4 output block is omitted.

**Maintenance:** When a new repeat-pattern is observed, append a row to `SESSION_OPENER.md` § 3.2 + create the matching `feedback_<slug>.md` (or `project_<slug>.md`) memory in the same commit per Rule 8.

See `archive/LESSONS.md` L043 for the originating incident pattern that motivated this rule.

### Rule 10 — Code review before commit is MANDATORY

Every commit, every session, every file class. Before running `git add` on any change, Claude (or any AI agent) MUST produce an explicit named code-review pass in the operator-visible chat. The review covers every modified file with a one-line verdict per file (defect | minor | clean). Governance scripts (Rule 2) run **after** the review as a separate quality gate. No exceptions for "small bookkeeping commits," "trivial typo fixes," "docs-only commits," or "fix-forward to a just-broken commit" — small commits are exactly where the discipline lapses, which is the entire failure mode.

**The commit pattern is procedural, not normative:** `edits → governance → named review table (in chat) → "go on commit?" → git add + commit -F`. The review is step 3 of a sequence — skipping it isn't "forgot the rule," it's "didn't follow the pattern." For the detailed review checklist (diff-vs-proposal, scope discipline, sync artifacts, ALLOWLIST vs `git status`), see § 8 step 5 and § 11 "Code review before staging" — both reference this rule as the binding anchor.

**Why this rule exists:** the discipline was first encoded as `archive/LESSONS.md` L027 (memory layer). On 2026-05-22 — the same session that codified Rule 9 — the rule was honored on the first commit but silently dropped on the second; operator caught it post-commit. Diagnosis: memory + SESSION_OPENER § 3 checklist are both session-scoped (fire once at session start), but code-review-skip is a per-commit failure mode. The forcing function must fire at the same granularity as the failure. This rule embeds the discipline in the per-commit procedure itself.

**Only permitted abbreviation:** operator explicitly says "skip review" on a specific commit. Per-commit override only — "skip review for the rest of the session" is not permitted.

**Drift on this rule is a Major defect.** A commit landing without the named review-table artifact in the operator-visible chat is a rule violation; record as an incident and revisit the wording for the next reinforcement.

See `archive/LESSONS.md` L044 for the incident that motivated this rule.

### Rule 11 — QA / smoke-test scenario for every change

Every behavior-affecting change MUST be paired with a written QA / smoke-test scenario describing how to verify the change works as intended. The scenario specifies (1) **what to verify** — the specific behavior the change introduces or alters; (2) **how to verify** — the runtime steps (CLI command + flags, fixture suite / sample target repo, input state) needed to exercise the change; (3) **expected pass criteria** — the observable outcome that confirms correctness (CLI exit code, stdout/report content, files written, version cells updated, etc.).

**Where the scenario lives:**

- **Under a § 15 plan** — in the plan's tracker. Big plans (per § 15.7) → sibling `docs/Plans/PLAN-NNN_tracker.md` Phase 4 verify section. Small plans → in-file § 4 Phase 4 checklist (each scenario as a ✅ / ⏸ sub-step with date).
- **Outside a § 15 plan** (Minor changes) — in `docs/Plans/OPEN_TASKS.md` (the local-only register, per L046) under a `Pending verification` section; ALSO referenced in the change's CHANGELOG entry under an explicit `QA scenarios` sub-section so the link survives if OPEN_TASKS is wiped.

**Coupling rule:** the QA scenario is added **same-commit as the change**. No change ships without a paired scenario. Missing scenario = rule violation, treated as a Major defect.

**What counts as a "change" for this rule:**
- ✅ Anything affecting CLI behavior, command output, the diff/merge/version-bump engine, or any operator-observable behavior
- ✅ Changes to how the tool parses, compares, or writes target-suite files (VERSION headers, manifests, STANDARDS_INDEX, CHANGE LOGs)
- ✅ New commands / flags / config-key changes; default-behavior changes
- ❌ **Exempt** — pure doc cleanup; lessons-archive additions (L0NN); manifest version bumps; standards-suite refresh; governance-doc edits with no behavior impact; commit-message wording

**Status markers** (mirroring § 15.7 tracker conventions):
- ⏸ pending — scenario defined; verification not yet attempted
- ✅ passed — verification ran (operator confirms via CLI run against fixtures / a sample target repo)
- ❌ failed — verification revealed a defect; fix-forward per Rule 3
- ⏭ skipped — scenario superseded by a later change (must annotate why)

**Lifecycle:** scenario added same-commit as change (status ⏸). After verification → operator updates to ✅. ✅ scenarios removed from `OPEN_TASKS.md` (per L046 done-equals-deleted rule); they stay in the per-plan tracker history (per L045) and the CHANGELOG QA-scenarios sub-section (permanent record).

**Why this rule exists:** post-implementation verification has historically been operator-driven and ad-hoc — PLAN-004's § 8 scenarios A–J were defined in the plan file by the operator at design time, but the link from "the code change was made" → "is the scenario list complete?" was implicit. Without a forcing function at change-time, scenarios can drift — some changes get scenarios, some don't, depending on operator's attention at design time. Rule 11 makes the coupling explicit and per-change, mirroring L044's "forcing-function cadence must match failure cadence."

See `archive/LESSONS.md` L047 for the codifying pattern.

### Rule 12 — Session wrap-up routine on operator command is MANDATORY

When the operator says **"wrap up"** (or any of these aliases: `wrap` / `end session` / `close out` [context-disambiguated from `Closeout_Mode`] / `end of session` / `finish up`), Claude MUST read [`docs/SESSION_CLOSER.md`](docs/SESSION_CLOSER.md) and execute its § 1 routine BEFORE posting any farewell message. The § 4 first-response output block MUST be posted before the session is considered closed.

This is binding because session-end detail loss is a real cost — across long sessions, new patterns / new rules / new lessons / scope expansions / memory updates emerge organically and are easy to forget by farewell time. Without a forcing function at session-end, codification slips and the next session can't pick up cleanly. The wrap-up is the forcing function; the output block is the proof-of-wrap-up visible to the operator.

**Routine has 9 mandatory steps** (per `docs/SESSION_CLOSER.md` § 1):

1. **Repo state** — working tree clean, commits this session, pushed vs unpushed
2. **EA + standards versions** — current `// VERSION:`, current Set Version, any pending tag operations
3. **Pending operator decisions** — DRAFT plans awaiting approval, blocked tasks, awaiting-approval scenarios
4. **Outstanding `docs/Plans/OPEN_TASKS.md`** (if file present) — active items + lesson candidates
5. **Memory updates** landed this session — list new/modified memory files
6. **`/tmp/` cleanup** — commit-msg files, transcript files, scratch artifacts
7. **Lessons-learned scan** — review session transcript for candidates: new rules added, new lessons (L0NN candidates), new memory entries, new SESSION_OPENER § 3.x rows, new conventions / patterns, scope expansions in existing plans. Surface as recommendations; if operator confirms, formally codify; otherwise add to OPEN_TASKS "Lesson candidates" section for next-session decision.
8. **Next-up suggestion** for the next session
9. **Confirm done** — operator can close

**Only permitted abbreviation:** operator explicitly says "skip wrap-up" (operator-only authorization — never self-skip). Even when abbreviated, steps 1-3 (repo state + versions + pending decisions) remain in force; only steps 4-9 may be omitted.

**Maintenance:** when a new wrap-up failure pattern is observed (e.g., operator notices a detail was lost between sessions), append to `docs/SESSION_CLOSER.md` § 2 failure-mode catalog + create matching memory + same-commit per Rule 8.

See `archive/LESSONS.md` L048 for the originating pattern that motivated this rule.

### Rule 13 — Senior-review-and-optimize pass before a plan goes to approval is MANDATORY

Every § 15 plan, after its initial draft is written and **before** it is presented to the operator for Phase 2 approval, MUST undergo a senior-developer review-and-optimize pass by the drafting agent. This pass is the **last task of plan development** — it runs only once the entire plan (every section §§ 1–12, plus the sibling tracker if the plan is big) is drafted, and immediately precedes presenting the hardened plan for approval. A plan is not "finalized" until the pass has run.

The agent assumes the role of a very experienced developer and:

1. **Verifies every code block / transformation rule against the actual current source** — real function names, signatures, line references, language correctness. The code must actually work, not merely look right.
2. **Checks consistency across ALL sections** — inputs ↔ behavior ↔ § 5 transformation rules ↔ panel/display ↔ § 6 spec map ↔ § 7 ALLOWLIST ↔ § 8 QA ↔ § 12 acceptance. No section may contradict another.
3. **Stress-tests edge cases and failure modes** — boundaries, midnight/timezone, market-closed, empty/partial states, ordering, redundancy.
4. **Optimizes and APPLIES the improvements directly to the plan file** (correctness, clarity, efficiency, idiomatic patterns, reuse) — it does not merely list them.
5. **Surfaces any genuinely new design decision** the review exposes to the operator rather than silently choosing (per § 10 never-assume).
6. **Records the pass in the plan's CHANGE LOG** (what it found + fixed) and reports a summary to the operator.

The canonical review prompt the agent runs verbatim is stored in § 15.8.

**Why this rule exists:** a plan draft is a hypothesis. The first drafting pass optimizes for completeness, not correctness, and reliably ships API-misuse, backwards logic, redundant computation, and cross-section drift that only a dedicated adversarial re-read catches. The operator must not be asked to approve — nor an implementer be prompted from — a plan that has not been hardened. The forcing function fires at plan-finalization, the same granularity as the failure (each plan).

**Only permitted abbreviation:** operator explicitly says "skip review" on a specific plan.

**Drift on this rule is a Major defect** — a plan presented for approval (or shipped to a Phase 3 implementer) without the recorded review-pass artifact in its CHANGE LOG is a rule violation.

See `archive/LESSONS.md` L049 for the incident that motivated this rule.

### Rule 14 — Project memory must be durable across machines and folder moves

The Claude memory store MUST live **inside the repository** at `./.claude/memory/` — the single physical copy — with the harness's per-project memory directory (`~/.claude/projects/<sanitized-abs-path>/memory/`) pointed at it via a **symlink**. Because the repository folder is the unit that is version-controlled and/or cloud-synced (Dropbox here), keeping the real memory files inside it means memory travels with the project: it survives a **machine change** (the synced repo carries the content) and a **folder rename/move** (the repo-relative path is stable).

The harness memory path is machine-local and keyed by the folder's absolute path — so it is the one thing that breaks on a move or a new machine. Repair is mechanical and idempotent: `scripts/bootstrap_memory.sh` re-derives the key from the current repo path and (re)creates the symlink. Run it once per machine and after any folder move.

This rule is enforced by a forcing function: `SESSION_OPENER.md` § 1.5 verifies the link resolves and the store is non-empty at every session start, **auto-repairs** a stale/missing link, and **HALTS with a warning** if the store is unexpectedly empty (the signal that memory was lost).

**Only permitted abbreviation:** none — the pre-flight check is cheap and silent when healthy.

**Drift on this rule is a Major defect** — a session that proceeds past an *unexpectedly* empty memory store (one where prior sessions are known to have written memory) without surfacing it to the operator is a rule violation. A genuinely new project with no memory yet is not a violation.

See `archive/LESSONS.md` L050 for the incident that motivated this rule.

---

## 4. Critical files (always Major; full workflow + extra care)

> **Customize this section per project.** Edits to these paths are **always Major** regardless of edit size — they require full Analyze → Design → Implement → Sync → Validate workflow.

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
```
docs/documents_manifest.md           # the version index — always Major
CLAUDE.md                            # this operating contract — always Major
docs/standards/                      # the standards suite this project adopts AND the canonical content the tool reasons about; edits define behavior — always Major
src/standard_document_updater/       # core diff / merge / version-bump logic — central domain logic — always Major
config/projects.toml                 # the target-suite registry — defines which repos the tool reads/writes; a silent edit could redirect a write to the wrong repo — always Major
```

**Drift rule for the engine vs. its design doc:** when the tool's behavior toward a standards file changes (how it parses VERSION headers, the manifest, or `STANDARDS_INDEX.md`; how it diffs / merges / version-bumps), the design doc that documents that behavior (`docs/architecture.md`) MUST be updated in the same commit (VERSION bump + CHANGE LOG entry). The code is the dispositive truth; the design doc is the navigable reference. If the two disagree, that's a defect — fix one or the other.

**Note on `docs/standards/`:** these files are both (a) this project's own adopted governance suite and (b) reference content the tool operates on. Treat any edit to them as Major. When backporting a newer Set Version into this project's own copy, follow the explicit-backport procedure in `STANDARDS_INDEX.md` § 4.3 and record it in `docs/SET_VERSION_ADOPTED.md`.

**Future critical files (add as the engine grows):**
- Any module other modules depend on (parser, differ, writer)
- Any future config / schema file beyond `config/projects.toml` (already Critical above) that defines target-suite mapping
<!-- PROJECT-OWNED:END -->

**Identification rule for adding new entries:** A file is "critical" if a silent or unintended change to it could:
- Alter documented domain behavior without trace
- Break backwards compatibility for downstream consumers
- Corrupt persistent state (DB, files, external services)
- Invalidate prior validation/test results

If unsure whether a file qualifies, classify it as critical. Cost of a false positive (slightly stricter workflow) is lower than cost of a false negative (silent breakage).

---

## 5. Change classification

Classify **every** change before implementation. Classification drives workflow strictness.

### Minor changes
- Bug fixes with **no intentional behavior change** (restoring documented behavior)
- Refactoring without contract changes (rename internals, extract function, move code) — outputs unchanged
- Naming improvements without API/config-key changes
- Comments / docstrings that **only** clarify existing behavior
- Formatting / lint fixes with **no logic change**

**Workflow:** Brief Analyze → Implement → Sync → Validate (light). Design step may be skipped.

### Major changes — any of the following
- **Domain / business logic** changes (the project's core behaviors)
- **New modules, packages, or significant new files**
- **Public API or interface changes** (signatures, CLI, env vars, return types)
- **Strategy / config parameters** affecting runtime behavior
- **Folder or file moves**, new top-level areas, or anything contradicting `docs/folder_structure.md`
- **Database schema** (tables, columns, keys, migration semantics)
- **Documentation that defines behavior** when behavior is being added or changed
- **CI/CD pipeline structure** (`.gitlab-ci.yml`, GitHub Actions workflows)
- **Any edit to a Critical File** (§ 4 above), regardless of edit size

**Workflow:** Full Analyze → Design → Implement → Sync → Validate. **No skipping Design.**

### Ambiguity rule

If unsure whether a change is Minor or Major: **classify as Major** or ask the user. Defaulting to Major costs ~10 minutes; defaulting to Minor when wrong costs hours.

---

## 6. Change workflow

### Core sequence (mandatory for Major; simplified for Minor)

1. **Analyze** — understand context, existing behavior, docs, structure. Read `docs/folder_structure.md` for placement. Search for existing implementations — prefer reuse over new code.
2. **Design** (Major only) — purpose, acceptance criteria, files/modules to touch, dependencies, integration points, risk.
3. **Implement** — follow architecture, coding standards, domain rules. No temporary hacks in production paths.
4. **Sync** — code, docs, and config aligned in the **same commit**. See `docs/standards/PROJECT_STANDARDS.md` for the full sync trigger table.
5. **Validate** — walk the validation checklist (§ 8) before declaring done.

If this sequence is broken for a Major change → **stop and correct course.**

### Response shape (when reporting completed work)

Every "I'm done" report — human or AI — uses these labelled sections, in this order:

1. **Analysis** — what was the situation
2. **Plan / Design** (if Major) — what was decided
3. **Implementation** — what was actually changed
4. **Documentation / config updates** — which docs got touched
5. **Version bumps** — every `.py`/`.sh` and tracked-doc version that moved
6. **Changelog / impact statement** — explicit "no runtime impact" or "yes, behavior X changes"

### Propose before implementing (Major changes)

For Major changes: outline plan and affected files **before** large edits. If the user only asked for a plan, **do not** implement until they confirm.

---

## 7. Versioning (mandatory for every touched code file)

Every `.py` and substantial `.sh` file carries a VERSION header. Every touched file bumps the header **and** appends a CHANGE LOG line. **No exceptions, even for single-line fixes.**

### Header template (Python)

```python
# ==============================================================
# VERSION: X.Y
# <one-line file description>
#
# CHANGE LOG
# vX.Y — YYYY-MM-DD HH:MM — <one-line summary of this change>
# vX.Y-1 — YYYY-MM-DD HH:MM — <previous summary>
# ...
# ==============================================================
```

### Header template (Shell)

```bash
#!/usr/bin/env bash
# ==============================================================
# VERSION: X.Y
# <one-line script description>
#
# CHANGE LOG
# vX.Y — YYYY-MM-DD HH:MM — <one-line summary>
# ==============================================================
set -euo pipefail
```

### Bump rules

- **Minor bump** (1.2 → 1.3): bug fixes, small tweaks, refactors that don't change outputs
- **Major bump** (1.9 → 2.0): structural changes, new features, interface changes
- **First version on a new file:** start at `0.1`. Promote to `1.0` when the interface stabilizes.

### Why this matters

The version trail is how a future contributor (or future AI session) reconstructs *what changed and when* without re-reading every commit. Skipping the bump erases that trail.

---

## 8. Validation checklist (the pre-push gate)

Walk this list before every push.

### 1. Versioning
- [ ] Every touched `.py`/`.sh` has its VERSION header bumped + CHANGE LOG line for this edit
- [ ] Every touched tracked `.md` has its VERSION comment bumped if substantive

### 2. Artifact sync
- [ ] All sync triggers walked (see `docs/standards/PROJECT_STANDARDS.md` § Artifact Sync)
- [ ] Manifest Last Updated block rotated
- [ ] CHANGELOG entry added at the top with explicit impact statement

### 3. Architecture & logic consistency
- [ ] Dependency direction preserved (lower-layer modules don't import from higher-layer)
- [ ] Source-of-truth files not duplicated elsewhere
- [ ] No new top-level directory without explicit approval
- [ ] Domain behavior matches the domain doc (or doc updated to match)

### 4. Testing
- [ ] If behavior affects outputs, validators run for the affected scope
- [ ] Test results stated honestly — never claim tests passed if they didn't run
- [ ] For new alerting/check code: deliberate-failure test was run and confirmed the failure path works

### 5. Code review (separate from governance)

Explicit named review pass on all modified/new files BEFORE `git add`. Governance scripts validate alignment (drift, manifest, coverage) — they don't catch logic errors, missed edge cases, or readability problems. Code review is an orthogonal quality gate that governance scripts structurally cannot replace. See `archive/LESSONS.md` L027.

- [ ] Each modified file walked: does it read correctly?
- [ ] Edge cases the task implied are handled
- [ ] No subtle bug a future reader would catch
- [ ] If concerns surface: fix and re-review BEFORE staging (not after)

### 6. Pre-push governance (mandatory)

```bash
python scripts/check_doc_coverage.py
python scripts/check_test_coverage_drift.py --ci
```

Both must exit `0`. For `.yml` CI changes, also:

```bash
python -c "import yaml; yaml.safe_load(open('.gitlab-ci.yml')); print('YAML valid')"
```

(YAML parse validates parseability only — not CI schema, per Rule 5.)

### 7. Self-check questions
- Would another developer understand **why** this change is safe from the changelog + doc diff?
- Could this change **silently** alter live or test results? If yes, is it documented and intended?
- Does any reasonable reading of this change conflict with the rules above?

### 8. Final consistency
- [ ] Code behavior matches docs that describe it
- [ ] No orphan docs describing removed code
- [ ] All config keys referenced in code exist and are documented
- [ ] `git status --short` shows ONLY the files you intended to commit

---

## 9. Conflict resolution priority

When two rules or goals conflict, resolve in this order (highest first):

1. **Domain logic integrity** — no silent changes to documented behavior
2. **System correctness** — bugs, data integrity, deterministic outcomes
3. **Architecture consistency** — layout, module boundaries, single sources of truth
4. **Performance** — only after correctness; no premature optimization
5. **Convenience** — doc churn, verbosity, minor friction — lowest priority

If you cannot resolve at your level, **escalate**. Do not paper over.

---

## 10. AI behavior rules

### Never assume missing logic
- Do not fill gaps with unstated rules. If requirements or docs are incomplete, **state assumptions explicitly** or **ask** the user.
- Prefer reading the codebase and the domain doc over guessing.

### Analyze before coding
- **Major changes:** read relevant modules and docs first; then design; then implement.
- **Minor changes:** at minimum, locate call sites and confirm no unintended side effects.

### Ask when ambiguous
- If classification (Minor vs Major), scope, or product intent is unclear, **ask 1-2 focused questions** instead of choosing arbitrarily.

### Self-validation before finishing
- Walk through the Validation Checklist (§ 8) — mentally or literally.
- Confirm artifact sync scope is satisfied for the change class.
- Summarize what changed, why, and any runtime/behavior impact.

### Honesty about risk
- Flag **breaking changes**, **behavior changes**, and **config migrations** clearly.
- Do not claim tests were run if they were not; say what was verified and what was not.

### Scope discipline
- Implement **only** what was requested unless the user asked to expand scope.
- **No drive-by refactors** unrelated to the task.

### Conflict with user request
- If a user request violates documented rules or would cause undocumented behavior, **refuse or propose a compliant alternative** and explain briefly.

### Verify agent claims via filesystem
- Per Rule 6: agent "done" is a hypothesis. `git status --short` is truth.
- Both **before** AND **after** `git add` in a multi-file commit.

### Project knowledge precedence
- When information is needed, search project knowledge / read the file FIRST.
- Only ask the user or guess if the information is genuinely not retrievable.
- The standards files in `docs/standards/` are authoritative — load them when their topic is in scope.

### Investigate when answers are questioned

When the user questions an answer ("how can X be Y?" / "but isn't Y supposed to be Z?"), treat the question as a signal to investigate the underlying source — query the DB, read the file, run the probe. Defending the original answer with more elaboration is the anti-pattern. See `archive/LESSONS.md` L032.

- The operator's clarifying question IS the uncertainty signal. Defending past it produces drift between stated facts and actual state.
- Right move: query the underlying state. Wrong move: re-explain with more confidence.
- If the data confirms the original answer, paste the data verbatim. If the data contradicts, update the answer and note the correction.

---

## 11. Commit policy

### When to commit
- After a **coherent task is complete** — not after every individual file edit.
- Multiple files changed for one logical task → **one commit**.
- **Never** commit half-finished work, broken states, or changes that haven't passed validation.

### Commit message structure

```
<Type/Scope>: <Title — present tense, imperative>

<Body paragraph 1 — what changed and why>

<Body paragraph 2 — context, design choice, alternatives considered>

<Optional: explicit impact statement — "No domain logic impact." etc.>

<Optional: ties to tracker — "Closes Phase X Task Y.Z">
```

### Multi-paragraph messages

Per Rule 4: write to `/tmp/<file>.txt` with single-quoted heredoc, then `git commit -F`. Never `-m` with escapes. Never heredoc piped to `git commit`.

### Verify before staging (Rule 6)

```bash
git status --short          # Verify file set matches ALLOWLIST
git add -A
git status --short          # Verify staged set unchanged
git commit -F /tmp/commit_msg.txt
```

### Code review before staging

Per `archive/LESSONS.md` L027 — explicit named review pass on all modified/new files BEFORE `git add`. Separate quality gate from governance scripts. If review surfaces concerns, fix and re-review before staging — don't add-then-fix.

### Agent runs commits end-to-end

Per `archive/LESSONS.md` L026 — if an AI agent prepares the commit, the agent also runs `git add` + `git commit -F /tmp/<file>.txt`. Operator gating happens at **push**, not at commit. Sandbox-failure recovery (rare) uses scoped path-operation authorization rather than blanket bypass.

### Push cadence — batch local commits

Per `archive/LESSONS.md` L028 — default to local commit + hold. Push only when:

1. CI-verify is needed for this specific commit
2. Staging-verify is needed (deploy behavior changed)
3. Deliberate-failure test cycle is in flight
4. `.gitlab-ci.yml` change (real-pipeline run is dispositive per Rule 5)
5. End-of-session trigger (close the day cleanly)

Otherwise commit locally, batch, push once when a trigger is hit. Push-after-every-commit produces pipeline noise and dilutes the signal value of the pipeline UI.

### Fix-forward (Rule 3)

When a pushed commit fails CI:
- ❌ Do NOT `git push --force` an amended version
- ✅ DO create a new commit (e.g., `Task 2.5b: fix-forward for Task 2.5 CI failure`)

---

## 12. Dispatcher — load these focused docs when their topic is in scope

`CLAUDE.md` is the binding contract. The focused standards files below are the working references for specific kinds of work. Load each only when its topic is in play — keeps agent attention narrow and recall high.

| When working on... | Load this doc |
|---|---|
| Anything code (any `.py`/`.ts`/`.sh`) | `docs/standards/ENGINEERING_STANDARDS.md` |
| Architecture (modules, imports, layer boundaries, new packages) | `docs/standards/ENGINEERING_STANDARDS.md` |
| CI/CD (`.gitlab-ci.yml`, deploy scripts, release pipelines) | `docs/standards/CICD_STANDARDS.md` |
| Tests / validators / coverage / drift detection | `docs/standards/VALIDATION_STANDARDS.md` |
| Documentation (any `.md`, manifest, CHANGELOG, version headers) | `docs/standards/PROJECT_STANDARDS.md` |
| Drafting a multi-file AI agent prompt (Cursor, Claude Code) | `docs/standards/PROMPT_STANDARDS.md` |
| Memory hygiene (what to memorize, what NOT to) | `docs/standards/MEMORY_PROTOCOL.md` |
| Setting up Claude.ai Project Instructions for a new project | `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` |
| Researching a past decision or incident ("why does X exist?") | `archive/LESSONS.md` and `archive/postmortems/` |
| Drafting OR executing a vital change to a Critical File (central domain logic) | this file, § 15 (plan workflow) — and the plan in `docs/Plans/` |

---

## 13. Single sources of truth (do not duplicate elsewhere)

- **Version header format & bump rules:** this file, § 7
- **Minor vs Major workflow:** this file, §§ 5-6
- **The 13 standing rules:** this file, § 3
- **Critical files list:** this file, § 4
- **Document version index:** `docs/documents_manifest.md`
- **Cross-cutting project history:** `CHANGELOG.md` (root)
- **Folder layout authoritative reference:** `docs/folder_structure.md`
<!-- PROJECT-OWNED:BEGIN (sync preserves this block) -->
- **Domain behavior:** the engine source under `src/standard_document_updater/` is the dispositive truth for how the tool reads, diffs, merges, and version-bumps standards documents. `docs/architecture.md` is the navigable reference and MUST be kept in sync per § 4. Until the engine exists, this README + the `docs/standards/` suite describe intended behavior.
<!-- PROJECT-OWNED:END -->

If you find content in multiple places, that is a **defect**. Resolve it: keep the canonical one, replace the others with pointers.

---

<!-- PROJECT-OWNED:BEGIN (sync preserves this block) — single-agent: Codex § 14 omitted; this stub is project-owned -->
## 14. Codex handoff protocol — NOT IN USE (single-agent project)

This project is single-agent (Claude only). The standards template defines an OPTIONAL multi-agent (Codex / Devin) handoff protocol here; it is intentionally **omitted**. There is no second-agent domain boundary, no handoff summary, and no per-agent tracker ownership. If a second AI coding agent is ever adopted, restore § 14 from the template at `docs/standards/` (and from a reference multi-agent project) and set § 1 Multi-agent to Yes.

Wherever the rest of this contract references `§ 14.4` (tracker `Owner:` headers), that convention is **not required** in a single-agent project — the `Owner:` header on tracker files is optional.
<!-- PROJECT-OWNED:END -->

---

## 15. Plan workflow for vital changes

Some change classes are vital enough that a written plan must exist BEFORE any code is touched, and Phase 3 (Implement) runs in a SEPARATE agent session from Phase 1 (Design). The plan is the design record; the two-session split prevents design drift mid-implementation.

### 15.1 When to use the plan workflow

A change is "vital" if any of:

- It edits a **Critical File** listed in § 4 (project-specific definition).
- It changes domain logic that affects live behavior, persistent state, or downstream consumers.
- It introduces a new module that other modules will depend on.
- It refactors a globally-read state variable (see LESSONS L039).
- It integrates with an external data source where the integration behavior matters for safety (see LESSONS L040, L041).

If you're unsure, classify as vital. Cost of a written plan is ~30–60 minutes; cost of a half-finished refactor or silent design drift is hours-to-days.

### 15.2 The six phases

| Phase | Owner | Deliverable |
|---|---|---|
| 0 — Audit | Plan author | All integration points cited by `file:line`; external dependencies verified to exist; existing behavior summarized. |
| 1 — Design | Plan author | Plan committed to `docs/Plans/` per Rule 1. Contains: § 1 goal, § 2 operator constraints, § 3 scope summary, § 4 phase tracker, § 5 verbatim transformation rules per call-site (per Rule 7), § 6 spec update map, § 7 explicit ALLOWLIST (the bullet enumeration IS the count — see LESSONS L038 — and it MUST include the plan file + sibling tracker as same-commit promotion rows, per L054), § 8 validation gate including demo smoke test, § 9 explicit operator-approval decision point, § 10 rollback path, § 11 known risks with mitigation, § 12 acceptance criteria. **The final task of Phase 1 is the Rule 13 senior-review-and-optimize pass (§ 15.8) — run once on the complete plan + sibling tracker, immediately before Phase 2; the plan is not finalized until it has run.** |
| 2 — Operator approval | Operator | Written response: "APPROVE D1.A" (or alternative). No code is touched until this approval lands. |
| 3 — Implement | Fresh agent session | Single commit, ALLOWLIST-bounded. Prompted from the plan file as the authoritative spec. The new session does not need to read the conversation history that produced the plan. |
| 4 — Validate | Implementer + operator | Type-check / compile clean; governance scripts pass; § 8 demo smoke test walked. |
| 5 — Operator gate | Operator | Authorizes push + tag. Plan promoted to v1.0 / CLOSED in the same commit as Phase 3 ships. |

### 15.3 The two-session split

Phase 1 (Design) and Phase 3 (Implement) MUST run in separate Claude / agent sessions when the plan is non-trivial. The Phase 3 session opens with the operator pasting a Phase 3 prompt that references the committed plan file (`docs/Plans/PLAN-NNN_*.md`) as the authoritative spec.

The Phase 3 prompt:

- Names the plan file and the section (§ 5 transformation rules + § 7 ALLOWLIST).
- States the operator's explicit approval ("APPROVE D1.A").
- Lists the key behaviors that MUST be preserved (this is the operator's last-mile safety net — see PLAN-004 prompt for an example).
- Notes any operator-side deltas from the plan (e.g., "drop the X suffix per operator request").
- Reminds the implementer to follow the operating contract (CLAUDE.md, Rule 4, Rule 6, Rule 7).

If the implementer Claude finds any ambiguity in the plan, that's a plan defect — surface it to the operator rather than silently fill from prior conversation (per § 10 AI behavior rules). Before any edit, the implementer's first act is a **reconcile pass**: verify the plan's § 5 code, § 7 ALLOWLIST, and file/line anchors against the live source, and surface any mismatch as a named plan-defect (D1, D2, …) — the backstop to the Rule 13 pass (per LESSONS L056).

### 15.4 Closed-risk annotation (Rule 6 sync trigger)

When a Phase 3 commit ships the mitigation for a risk documented in an earlier plan's § 11 risks section, the earlier plan's risk row MUST be annotated as CLOSED in the **same commit** as the mitigation (see LESSONS L036 + PROJECT_STANDARDS § 4 closed-risk sync trigger). This keeps the audit trail current — a risk is open if and only if the plan that documented it says it's open.

### 15.5 Versioning the plan

Plan files use the same VERSION header convention as other tracked docs (§ 7). They progress: `0.1` (DRAFT) → `1.0` (CLOSED after Phase 3 commit). Status field in the header reflects the current phase: DRAFT / APPROVED / EXECUTING / CLOSED / SUPERSEDED.

The manifest row for the plan reflects the same versions. When the plan promotes to `1.0`, the manifest row updates in the same commit.

### 15.6 What the plan workflow is NOT

- Not for bug fixes that don't change documented behavior — those are Minor per § 5; one-commit fix-forward is fine.
- Not for new tests or test fixtures — those follow VALIDATION_STANDARDS.
- Not for doc-only edits — those follow PROJECT_STANDARDS § 4 sync triggers directly.
- Not a substitute for the multi-file prompt template (PROMPT_STANDARDS § 3) — the plan SUPPLIES the FIND/REPLACE blocks the Phase 3 prompt will pass to the agent. The two layers compose; they're not alternatives.

See LESSONS L042 for the proven-out incident pattern.

### 15.7 Tracker requirement for big plans

Big plans get a sibling tracker file so sub-tasks, verification scenarios, and cross-session work are visible at a glance — not buried in the plan's § 4 high-level phase block.

**Tracker is required if ANY of the following is true:**

1. Phase 3 is expected to land as **>1 commit** (multi-task pattern, e.g., PLAN-001's Task 2.5 / 3.1 / 3.2 sub-commits).
2. Phase 4 has a **multi-scenario validation list** (e.g., PLAN-003 / PLAN-004's smoke-test scenarios A–J).
3. The plan is expected to **span more than one Claude session** (i.e., not finishable in the session that drafted it).

**Safety valve:** the operator may declare a tracker required for **any** plan at Phase 1 (Design) or Phase 2 (Approval), even if conditions 1–3 don't trigger. Cost of an unneeded tracker is one file; cost of mid-flight sub-task amnesia is hours.

**Tracker file:**

- Path: `docs/Plans/PLAN-NNN_tracker.md` — same folder as the plan it tracks.
- Header: `Owner: Claude` (per § 14.4 — multi-agent projects only). Single-agent projects may omit.
- Body: phase-by-phase sub-task list with status markers (⏸ pending / 🔄 in-progress / ✅ done / ❌ blocked) and date stamps on transitions.
- Updated **same-commit** as the work it tracks (any sub-task status change rides with the commit that made the change).
- Promoted to v1.0 / CLOSED in the **same commit** that closes the plan itself.

**When the tracker is created:**

- Default: in the **same commit as the Phase 1 plan draft**.
- Retroactive: if the trigger only becomes true mid-flight (e.g., Phase 3 was scoped as 1 commit but expanded to 3), create the tracker in the **first commit where the trigger becomes true** and back-fill the prior phases' status.

**Sibling tracker is NOT:**

- Not a replacement for the plan's § 4 phase block — the plan's phase block stays as a high-level summary; the sibling tracker breaks each phase into enumerable sub-tasks.
- Not required for plans where Phase 3 = 1 commit AND Phase 4 = simple compile-clean check AND operator hasn't declared one — those are "small plans" and use the in-file pattern below instead.

#### Small plans — in-file tracker

Plans that do **NOT** trigger the sibling-tracker conditions 1–3 above and have not been operator-declared still need granular sub-task tracking. The tracker lives **inside the plan file itself**, in § 4 "Phase tracker" — expanded from the default one-line-per-phase summary into a checklist of sub-tasks per phase.

**Required in § 4 of every small plan:**

- Phase 0 (Audit) — single ✅ / ⏸ marker with date.
- Phase 1 (Design) — single ✅ / ⏸ marker with date.
- Phase 2 (Operator approval) — single ✅ / ⏸ marker with date + approval-string ("APPROVE D1.A" etc.).
- Phase 3 (Implement) — each file edit OR each verbatim-transformation sub-step (per § 5 of the plan) as ✅ / ⏸ with date.
- Phase 4 (Validate) — each verify check (compile clean / scenario 1 / scenario 2 / ...) as ✅ / ⏸ with date.
- Phase 5 (Operator gate) — push + tag (each as ✅ / ⏸ with date).

Updated **same-commit** as the work it tracks (same discipline as the sibling tracker). Promoted to v1.0 / CLOSED with the plan.

**Symmetry with big-plan sibling tracker:** every plan, regardless of size, has a single visible place where sub-task status is current. Big plans use a sibling file (volume / cross-session); small plans embed it in § 4 (lighter weight, fewer files). The rule has no escape hatch — every § 15 plan, big or small, carries a granular tracker somewhere.

**Migration path if a "small" plan grows mid-flight:** if a plan was started small (in-file § 4 tracker) and later trips one of the big-plan conditions (Phase 3 expands to >1 commit, a multi-scenario verify list emerges, work spills into a new session), promote it: create the sibling `PLAN-NNN_tracker.md` in the first commit where the trigger becomes true, back-fill the prior phases' status from § 4, and collapse § 4 back to the high-level summary in the same commit.

Companion: SESSION_OPENER § 3.2 row 13 catches both failure modes (starting a big plan without the sibling tracker OR starting a small plan without granular § 4 sub-tasks).

### 15.8 Senior-review-and-optimize pass (Rule 13)

Per Rule 13, the **final task of every plan's development** — after all sections are drafted and immediately before the plan is presented for Phase 2 approval — is a senior-developer review-and-optimize pass run by the drafting agent. It is binding for every § 15 plan, big or small (small plans embed representative code in their § 5 transformation rules just as big plans do).

**The canonical review prompt** (run verbatim each time):

> *Act as a very experienced senior developer. Recheck this plan end-to-end: make sure it is consistent in every detail and in the code itself, verified against the real current source; make it the best possible version to serve its purpose; and where you can optimize it, apply the optimization directly and execute it — don't just suggest it. Surface any genuinely new design decision to the operator rather than deciding silently.*

**What the pass produces:**

- The plan file edited in place with every fix + optimization applied — § 5 code corrected against the real source, cross-section contradictions resolved, edge cases handled, redundancy removed.
- A CHANGE LOG entry on the plan recording what the review found and changed.
- An operator-facing summary of the findings.
- Any newly-exposed design decision surfaced as an explicit operator choice (not silently resolved).

**Ordering (the "last task" requirement):** the pass MUST see the complete plan. It does not run section-by-section during drafting; it runs once, at the end, on the finished plan (and its sibling tracker, if any). If the plan is materially revised after the pass but before approval, re-run it.

**Relationship to other gates:** Rule 13 hardens the **plan** (the design + its embedded transformation code) at Phase 1; Rule 10 (code review before commit) hardens the **actual edits** at Phase 3 commit time. They are complementary, not duplicative.

See `archive/LESSONS.md` L049 + § 3 Rule 13.

---

## End of contract

Every contributor (human and AI) operating on this repository operates under the rules above. If a rule needs to change, change it deliberately — through a commit that updates this file, with a CHANGELOG entry explaining why, and a corresponding update to `archive/LESSONS.md` capturing the incident that motivated the change.

**Rules are added when something breaks. They are not removed lightly.**
