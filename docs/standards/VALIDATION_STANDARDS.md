<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

# VALIDATION_STANDARDS.md — Test Framework & Validation Discipline

**Scope:** Test framework architecture, tier definitions, ownership model, CI integration patterns, deliberate-failure protocol, drift detection, and notification design. Loaded when the work involves writing tests, modifying validators, configuring test ownership, or designing CI test stages.

For pipeline structure (jobs, stages, deploy gating) → `CICD_STANDARDS.md`. For coding test code → `ENGINEERING_STANDARDS.md`. For documenting validation in CHANGELOG/manifest → `PROJECT_STANDARDS.md`.

**Why this file exists:** Tests that "pass when correct" but never get exercised against real failures provide false confidence. A validation framework needs explicit tier definitions, ownership rules tying tests to source files, drift detection when tests fall behind code, and a deliberate-failure protocol that proves the failure path actually works. Every rule below was learned from a specific incident on a reference project where one of those mechanisms was missing.

---

## Table of Contents

1. [Validation philosophy](#1-validation-philosophy)
2. [The 7-tier test model](#2-the-7-tier-test-model)
3. [Test runner & directory layout](#3-test-runner--directory-layout)
4. [The ownership model](#4-the-ownership-model)
5. [CI integration — which tier runs when](#5-ci-integration--which-tier-runs-when)
6. [Test database seeding](#6-test-database-seeding)
7. [Deliberate-failure testing protocol](#7-deliberate-failure-testing-protocol)
8. [Failure notification design](#8-failure-notification-design)
9. [Drift detection (test ↔ code ↔ doc)](#9-drift-detection-test--code--doc)
10. [Anti-patterns to refuse](#10-anti-patterns-to-refuse)

---

## 1. Validation philosophy

Five principles that govern every test in the suite.

### 1.1 Test what fails, not just what passes

A test that asserts "happy path produces expected output" only validates the success branch. The failure branch — the `if error: send_alert` code — is not exercised by happy-path tests. When real failure occurs months later, the alert path may have a syntax bug that has been silently broken since day one.

**Per `LESSONS L009`**: every new alerting, validation, or check code must be tested by **deliberately inducing the failure mode** and confirming the failure path fires correctly.

### 1.2 Tests document behavior — they are part of the spec

A test name describes a behavior the system guarantees. When tests are well-named, the test file is a readable specification of what the module promises.

- ✅ `test_signal_filter_rejects_below_min_pip_distance`
- ❌ `test_signal_filter_1`

If a test is hard to name, the behavior it asserts is probably unclear. Rename or restructure.

### 1.3 Tests are first-class code

Test files have VERSION headers. They follow the same coding standards as production code. They go through the same review process. They are NOT throwaway support files.

### 1.4 Determinism is non-negotiable

A test that fails intermittently is worse than no test. Sources of non-determinism:
- Time / timezone (use frozen time in tests)
- Random numbers (seed explicitly)
- File system order (don't rely on directory listing order)
- Network calls (mock or use deterministic fixtures)
- Concurrent execution (avoid in unit tests; isolate when integration testing concurrency)
- **Live data settlement windows** — for time-series live data, rows may rewrite during a settlement window (e.g., a candle bar's high/low/close updating during the first ~10 min as later ticks arrive). Tests that operate against live data must either run post-settlement OR be mutability-tolerant. See `ENGINEERING_STANDARDS.md` § 1.7 and `archive/LESSONS.md` L021.

If a test is flaky, fix or delete — never tolerate "re-run and it passes."

### 1.5 Coverage is a signal, not a goal

100% coverage on trivial code is less valuable than 60% coverage on critical paths. Focus testing effort where:
- Logic is non-obvious
- Failure has high cost
- Edge cases are subtle
- Integration boundaries are crossed

Skip explicit testing for trivial getters, framework boilerplate, and code whose correctness is obvious by inspection.

---

## 2. The 7-tier test model

Tests are organized by purpose, not by file location. Each tier has a different runner trigger, a different cost, and a different role in the pipeline.

| # | Tier | Purpose | Runs on | Typical duration |
|---|---|---|---|---|
| 1 | `governance` | Repo health: doc drift, coverage gaps, ownership map sanity | Every push, pre-commit hook | <30s |
| 2 | `logic` | Pure-logic unit tests: formulas, transformations, decisions | Every push, pre-commit hook | <2min |
| 3 | `integration` | Module-boundary tests: component A talks to component B correctly | MR pipeline, master pipeline | 2-10min |
| 4 | `contracts` | API/data contract tests: wire format, envelope schemas, persistence shape | Every push | <2min |
| 5 | `smoke` | Post-deploy verification: services up, image sources correct, basic functionality | After deploy | <2min |
| 6 | `scheduled` | Long-running validators against seeded DB: end-to-end pipeline checks | Nightly cron | 5-30min |
| 7 | `audits` | One-off historical analyses, run on demand | Manual | varies |

### 2.1 Tier 1 — `governance`

Catches drift between code, docs, and config:

- Doc coverage: every env var documented, every API route documented, every DB table documented, every VERSION-bearing file in the manifest
- Test coverage drift: every source file under monitored paths has its expected test/doc per the ownership map
- CHANGELOG freshness: recent commits have corresponding CHANGELOG entries
- Folder structure drift: new files appear in `docs/folder_structure.md`
- Import boundary violations: lower-layer modules don't import from higher-layer modules

Implementation: scripts under `scripts/` (`check_doc_coverage.py`, `check_test_coverage_drift.py`). Fast, no DB needed.

### 2.2 Tier 2 — `logic`

Pure-function unit tests. No I/O, no DB, no network. Each test runs in milliseconds.

Examples: pattern detection algorithms, signal filtering rules, configuration resolution logic, transformation functions, formula calculations.

These are the tests that should run on every keystroke (in IDE) and every push (in CI).

### 2.3 Tier 3 — `integration`

Tests that exercise multiple modules together. May use a test database (seeded with fixture data, not production data) or in-memory equivalents.

Examples: signal builder + filter + persistence pipeline, config resolver + strategy initialization, market data loader → engine → output.

### 2.4 Tier 4 — `contracts`

Tests that verify external/serialized formats stay stable:

- Wire format tests: every field in the API response, every type in the WebSocket envelope
- Persistence shape: DB row format matches the model, serialization roundtrips intact
- Config schema: all required keys present, types correct, no forbidden keys

Why separate from logic: contract tests catch breaking changes that pure logic tests would miss because the change happens at a serialization boundary.

### 2.5 Tier 5 — `smoke`

Post-deploy verification. Runs against the just-deployed environment. Checks:

- All services responding
- Image source verification (the running container's image matches what was intended to deploy — per `ENGINEERING_STANDARDS.md` § 7.4)
- Basic functionality (e.g., one API call, one DB query)

Smoke tests must be fast (<2min) and must clearly distinguish "deploy worked" from "deploy worked but the service is broken." Used as the gate for promoting a deploy from staging → production.

<!--
Example:
post_deploy_smoke.sh v0.2 — 20 checks across 5 sections:
1. Container state (all services running)
2. HTTP endpoints (API, charting return 200)
3. DB connectivity (write + read roundtrip)
4. Telegram notification reachability (send test alert)
5. Image source verification (per ENGINEERING_STANDARDS.md § 7.4) — REQUIRED tier; fails the smoke if any service runs an unexpected image
-->

### 2.6 Tier 6 — `scheduled`

Long-running tests against a seeded test database. Run nightly via cron — too slow for per-push pipelines.

Examples: full pipeline validators (`validate_<instrument>` style), end-to-end scenarios with realistic data volumes, cross-day behavior tests.

Test DB is seeded fresh per run via fixture scripts (per § 6).

### 2.7 Tier 7 — `audits`

One-off analyses that don't fit the regular cadence. Run manually for investigations, postmortems, capacity planning.

Not exercised by CI. Lives in the test directory for discoverability but not in the orchestrator's default run set.

---

## 3. Test runner & directory layout

### 3.1 Runner choice

Use a mainstream test runner for the language:
- **Python:** pytest (with conftest plugins as needed)
- **JavaScript/TypeScript:** Vitest, Jest, or Playwright depending on test type
- **Rust:** built-in `cargo test`
- **Go:** built-in `go test`

Don't write custom test runners. The runner ecosystem provides parallelization, fixture management, output formatting, and CI integration that custom code can't easily match.

### 3.2 Directory structure

```
validation/
├── __init__.py
├── run_all.py # CLI orchestrator
├── runner.py # Tier execution + result collection
├── result.py # Result types
├── conftest.py # Shared pytest fixtures
├── fixtures/ # Test data + DB seeding
│ ├── seed_ci_db.py
│ ├── ohlc_<instrument>_<n>.py
│ └── ...
├── tier1_governance/ # Tier 1 tests
│ ├── test_<surface>.py
│ └── ...
├── tier2_logic/ # Tier 2 tests
├── tier3_integration/
├── tier4_contracts/
├── tier5_smoke/ # OR scripts/post_deploy_smoke.sh
├── tier6_scheduled/
└── tier7_audits/
```

The tier-prefixed subdirectories let the orchestrator run a single tier (`python -m validation.run_all --tier logic`) or all tiers (`python -m validation.run_all`).

### 3.3 The CLI orchestrator

`python -m validation.run_all` is the **single authoritative entry point** for running validation. It:

- Selects which tiers to run (`--tier <name>`, `--tiers logic,contracts`, default = all)
- Discovers tests in the matching tier directories
- Runs them via pytest under the hood
- Collects results into a single JSON report
- Sends a final-summary notification (per § 8) — one notification per run, not one per test

Don't expose pytest directly to operators or CI. The orchestrator is the abstraction that makes the test framework approachable.

### 3.4 Test naming

- File: `test_<thing-being-tested>.py`
- Function: `test_<behavior>_<expected_outcome>`
- Class (if needed for grouping): `Test<ConceptName>`

Each test name reads as a sentence describing what's tested.

### 3.5 Fixture discipline

- Shared fixtures live in `conftest.py` at the appropriate scope (top-level, tier-level, file-level)
- Fixture data lives in `fixtures/` — Python modules or JSON files; never embedded in test files
- Each fixture is documented (one-line docstring describing what it represents)
- Don't over-share fixtures — narrow fixtures are more readable than mega-fixtures

---

## 4. The ownership model

The ownership model maps source files to the tests that validate them and the docs that describe them. It's the contract between code, tests, and docs.

### 4.1 The ownership file

`scripts/validation_ownership.toml` (or equivalent for non-Python projects):

```toml
[rules.pattern_engine]
source_paths = ["core/pattern_engine.py"]
test_paths = ["validation/tier2_logic/test_pattern_engine.py"]
doc_paths = ["docs/<domain-spec>.md", "docs/api_reference.md"]
strictness = "strict"
require_docs = true
reason = "Core detection logic — silent changes here corrupt every signal."

[rules.signal_filter]
source_paths = ["strategies/engine/signal_filter.py"]
test_paths = ["validation/tier2_logic/test_signal_filter.py"]
doc_paths = ["docs/<domain-spec>.md"]
strictness = "strict"
require_docs = true
reason = "Filter accept/reject decisions are visible in production output."

# ... one rule per critical source file ...

[monitored_paths]
strict = ["core/", "config/", "strategies/engine/", "domain/"]
soft = ["live/", "api/", "telegram/", "tools/"]
```

### 4.2 Rule fields

- **source_paths:** files this rule covers (glob or explicit list)
- **test_paths:** test files that must exist and contain tests for the source
- **doc_paths:** docs that describe the source's behavior
- **strictness:** `strict` (changes to source require matching test/doc updates) or `soft` (warning only)
- **require_docs:** `true` enforces same-commit doc updates when source changes; `false` only checks test updates
- **reason:** human-readable explanation of why this rule exists

### 4.3 Strict vs soft paths

**Strict paths** = source files where any change must have a corresponding test change AND (if `require_docs=true`) doc change in the same commit. Drift detector blocks the commit/CI if not satisfied.

**Soft paths** = source files where change without test/doc update produces a warning, not a block. Used for areas where test infrastructure isn't yet mature enough to enforce.

Promote soft paths to strict as test coverage matures. The goal is for all monitored paths to eventually become strict.

### 4.4 Unmapped file detection

The ownership map should cover every file under `monitored_paths`. New files appearing in monitored paths without an ownership rule trigger a warning (or block, for strict paths). Forces the author to either add an ownership rule or move the file out of a monitored path.

### 4.5 Exceptions

Some source files genuinely don't need tests (e.g., `__init__.py` re-exports, generated code, shims). Document these as exceptions:

```toml
[exceptions]
"core/__init__.py" = { rule = "init_reexports", reason = "Re-export only", author = "yaser", date = "2026-04-21", expires = "" }
"strategies/legacy_v1.py" = { rule = "deprecated", reason = "Pre-deprecation, not in active use", author = "yaser", date = "2026-04-15", expires = "2026-06-01" }
```

Exceptions:
- Are **structured** (rule name + reason + author + date + optional expiry)
- **Expire** if `expires` is set; expired exceptions become errors
- Are **reviewed quarterly** — accumulated exceptions are technical debt

### 4.6 Updating ownership when adding files

When a new source file lands under a monitored path, the same commit:
1. Adds the source file
2. Adds a corresponding ownership rule
3. Adds the test file referenced by the rule (or adds an exception with reason)
4. Adds the doc reference if `require_docs=true`

Per CLAUDE.md Rule 6 — verify via `git status --short` that all four landed before commit.

---

## 5. CI integration — which tier runs when

Different tiers have different cost and different roles. Map them to pipeline triggers explicitly.

### 5.1 Standard mapping

| Trigger | Tiers run | Why |
|---|---|---|
| Pre-commit hook (local) | governance, logic | Catch obvious failures before push, fast feedback |
| MR pipeline | governance, logic, contracts, integration | Full test suite before merge; validates contract changes |
| Master push | governance, logic, contracts, integration | Same as MR; protects master |
| Post-deploy (staging) | smoke | Verify the deployment worked |
| Post-deploy (production) | smoke | Same as staging; gates production from being marked good |
| Nightly cron | scheduled (and audits if scheduled) | Long-running validators with seeded DB |
| Manual / on-demand | audits | Investigations |

### 5.2 Job naming in CI

CI jobs are named after the tier they run:
- `governance` → runs Tier 1
- `logic-tests` → runs Tier 2
- `contract-tests` → runs Tier 4
- `integration-tests` → runs Tier 3 (or split per integration domain)
- `smoke-staging`, `smoke-production` → runs Tier 5 against the named environment
- `nightly` → runs Tier 6 (and Tier 7 if scheduled)

Naming consistency makes pipeline visualization readable.

### 5.3 Required vs allow_failure

- **Required (`allow_failure: false`):** governance, logic, contracts, integration, smoke. Failure blocks merge or deploy progression.
- **Allowed-failure (`allow_failure: true`):** **none in steady state.** Per `LESSONS L016` — sustained `allow_failure: true` jobs become decoration that operators learn to ignore.

If a tier is failing reliably and you can't fix it immediately:
- Mark it `allow_failure: true` **with an explicit expiry date** in the rationale
- Add a tracker entry committing to fix or remove by the expiry
- Do not let it run as `allow_failure` indefinitely

### 5.4 Test database in CI

Tier 6 (scheduled) needs a database. CI provides this via:

```yaml
nightly:
 services:
 - name: <db-image>:<version>
 alias: <db-host-alias>
 variables:
 POSTGRES_DB: test_db
 POSTGRES_USER: test_user
 POSTGRES_PASSWORD: test_password
 # ... script: seed DB then run scheduled tier
```

Seeded by `validation/fixtures/seed_ci_db.py` (or equivalent) before the test run begins.

### 5.5 Pipeline change validation

Per CLAUDE.md Rule 5 / `LESSONS L005`: local YAML parse and governance scripts validate Python and YAML syntax — **not** GitLab/GitHub-specific job-graph semantics.

For any change to `.gitlab-ci.yml` (or workflows file) touching `needs:`, `stage:`, `rules:`, `dependencies:`, or `stages:`, the dispositive validation is the real pipeline run. Push and observe; fix-forward (Rule 3) if defects surface.

### 5.6 First-fire expectations for new gates

Per `archive/LESSONS.md` L017 — never-exercised gates fire bugs in cascade. When a CI gate (alerting, validation check, schedule, deliberate-failure flow) is fired for the first time, expect **3-5 iterations** before fully green:

1. First fire reveals one config issue (missing env var, wrong scope, masking edge case)
2. Fix → second fire reveals different config issue (auth, aliasing, permissions)
3. Fix → third fire reveals data / timing issue (fixtures, dependencies)
4. Fix → fourth fire reveals notification / alerting issue
5. Fix → fifth fire green

**Practical implications:**

- Budget 1-2 hours of iteration time for the first fire of any new gate
- Don't schedule the first fire close to a deadline
- Each fix is its own commit (don't batch fixes — they obscure the cascade in retrospect)
- Track each iteration in the project's CI/CD tracker so the cascade is visible

This is not pessimism — it's the empirical baseline from a reference project Phase 3 (X11 nightly Telegram cascade went 4 iterations before fully green) and Phase 3 Task 3.4 deliberate-failure cycle (2 iterations on auto-rollback before the auth gap was found and fixed via F-1). Trust gates that have been exercised under their full failure mode; investigate gates that haven't.

---

## 6. Test database seeding

Tier 6 (scheduled) and some Tier 3 (integration) tests need realistic data. Use deterministic fixture data, not production snapshots.

### 6.1 The seeding script

`validation/fixtures/seed_ci_db.py` (or equivalent) is invoked by CI before the test run:

```bash
.venv/bin/python -m validation.fixtures.seed_ci_db --target $DATABASE_URL
```

It:
1. Connects to the empty test DB
2. Runs all migrations to current schema
3. Inserts deterministic fixture data
4. Verifies the seed by querying back a known row
5. Exits non-zero if any step fails

### 6.2 Why seeded data, not production snapshots

- **Determinism:** same seed = same data = same test outcomes
- **Privacy:** no PII, no sensitive data in CI
- **Size:** fixture data is small (KB), production snapshots are large (GB)
- **Reproducibility:** the fixture file is in git, so anyone can recreate the test environment

### 6.3 Fixture data design

- One Python module per domain entity (`fixtures/users.py`, `fixtures/orders.py`)
- Each module exports a `seed(conn)` function
- The orchestrator (`seed_ci_db.py`) calls each in order, respecting FK dependencies
- Documented in `docs/testing.md` so operators know what's loaded

### 6.4 When fixtures need to change

Fixture changes are Major (per CLAUDE.md § 5) — they affect test outcomes:
- Update the fixture
- Re-run affected tier tests locally
- Update any test assertions that depended on the old fixture values
- CHANGELOG entry noting the change and which tests were affected

---

## 7. Deliberate-failure testing protocol

The single most underrated discipline in validation. Per `LESSONS L009`.

### 7.1 The protocol

For any new alerting code, validation check, or healthcheck:

1. **Implement the success path** — verify it works under normal conditions
2. **Deliberately induce the failure mode** — break the system in the way the alert/check is supposed to detect
3. **Confirm the failure path fires** — alert is sent, check exits non-zero, error is logged correctly
4. **Restore the system** — undo the deliberate break
5. **Document the test in the tracker** — so the deliberate-failure exercise is repeatable

### 7.2 What counts as "inducing failure"

The induced failure should match the real failure mode:

- **For "service is down" alert:** stop the service container, confirm alert fires within the configured window
- **For "database unreachable" alert:** block the DB port (firewall rule, network namespace), confirm alert fires
- **For "image source verification" check:** deliberately deploy with the wrong image, confirm smoke fails
- **For "config validation" check:** introduce a malformed config, confirm validation rejects it

If the induced failure can't be made to look like the real one, the test is testing a different scenario than the alert/check actually handles.

### 7.3 Mandatory for new alerting/check code

This is not optional. New alerting / validation / healthcheck code is incomplete until it has been deliberately failure-tested.

Add a checklist item to the prompt for any task that adds such code:
- [ ] Deliberate-failure test was run
- [ ] Failure path confirmed working
- [ ] Test procedure documented in tracker incident block

### 7.4 Examples

<!--
a reference project deliberate-failure tests:

Task 2.5d (image source verification):
- Deliberately deployed with `myapp/backend:latest` instead of registry-tagged image
- Confirmed smoke-staging Section 5 detected the mismatch and exited non-zero
- Documented the test procedure in tracker incident block for Task 2.5d
- Caught a genuine bug in the verification regex during the test (over-matched some valid images)

Task M (healthcheck Telegram delivery):
- Deliberately stopped the `charts` container
- Confirmed healthcheck.sh detected the down state, sent NOTICE alert via Telegram
- Confirmed alert text included hostname tag for routing
- Bonus catch: discovered cosmetic empty-state bug ("Optional service down: charts ")
 added as Phase 3 deferred D6

Task 3.2 (rollback):
- Tests 1-5 covered: bad SHA, missing image, explicit happy path with write-back,
 idempotent NO-OP, auto-detect forward
- Each test deliberately set up the failure or edge condition, then verified rollback.sh
 responded correctly
-->

### 7.5 24-hour staging soak required before production deploy

Per `archive/LESSONS.md` L022 — for systems operating on time-series live data (or any data shape where slow-burn regressions are possible), **no production deploy until 24 hours after the same commit's staging deploy timestamp**. The soak window resets if any new commit lands in the deploy-candidate.

Why this is here (not just in `CICD_STANDARDS.md` § 9):

- Smoke verification catches "the deploy is technically running" failure modes
- Some regressions only surface under live-data load over hours (compaction effects, accumulated state, slow memory leaks, cron-fired downstream effects)
- The 24h soak is the **slow-burn equivalent of deliberate-failure injection** — it catches the failure class smoke can't

Soak is **in addition to** smoke verification — both must pass. Smoke gates on the technical level; soak gates on the behavioral level. They catch different failure classes.

**Operator authorization protocol for prod promotion (per `archive/LESSONS.md` L030):**

The operator session that asks for "PROD deploy" must include:

- The staging-deploy timestamp (when soak started)
- The calculated soak-completion timestamp (when prod-eligibility opens)

If either is missing, the request is malformed and must be rejected pending the missing data.

**When 24h is not enough:**

For specific high-risk deploys (schema migrations, major refactors, infrastructure changes), the soak window may extend beyond 24h. Document in the project's runbook under "deploy-window override" with the specific trigger conditions.

---

## 8. Failure notification design

When tests fail in CI or on a scheduled run, operators need to know — but not so noisily that they tune out.

### 8.1 One notification per run

Send a **final-summary notification** at the end of a test run, not a notification per test. A notification per failed test produces alert fatigue; a single summary tells operators what they need to know.

### 8.2 Notification content

- **Tier name** that ran (governance, logic, scheduled, etc.)
- **Pass/fail count**
- **Total duration**
- **Top 3-5 failures** with test names and one-line failure reasons
- **Link to full report** (CI job URL, JSON report file location)
- **Hostname / environment tag** so operators can route by environment

### 8.3 Channels

- **Tier-specific channels:** governance failures might go to a developer channel; scheduled validator failures go to an ops channel
- **Severity routing:** critical failures (smoke fails on production deploy) get higher-priority routing than soft warnings

### 8.4 Dedicated sender / chat ID per environment

Use separate notification credentials for staging and production:

- Staging notifications use a staging bot / staging chat ID
- Production notifications use a production bot / production chat ID
- Operators can mute one without muting the other

This prevents staging noise from training operators to ignore production alerts.

### 8.5 Test the notification path

Per § 7 — deliberate-failure-test the notification:
- Force a test to fail
- Confirm the notification arrives at the configured channel
- Confirm the content is readable and actionable

---

## 9. Drift detection (test ↔ code ↔ doc)

The drift detector (`scripts/check_test_coverage_drift.py` or equivalent) enforces the ownership model from § 4.

### 9.1 What it checks

For each commit / MR:
- For each source file changed, find the matching ownership rule
- Verify the rule's test files were also changed (if `strictness=strict`)
- Verify the rule's doc files were also changed (if `require_docs=true`)
- Surface unmapped files under monitored paths
- Validate exceptions (not expired, structured correctly)

### 9.2 Strictness gradient

- **Strict + require_docs:** must update both test AND doc when source changes; otherwise BLOCK
- **Strict + not require_docs:** must update test when source changes; otherwise BLOCK
- **Soft:** WARN only; doesn't block

### 9.3 GitLab MR diff base

When run in CI:
- Use `$CI_MERGE_REQUEST_DIFF_BASE_SHA` for MR pipelines
- Use `$CI_COMMIT_BEFORE_SHA` for push pipelines
- Use `HEAD~1` as fallback for local runs

Don't use `HEAD~1` in CI — it's fragile when CI runs on a single commit (no parent in the working tree).

### 9.4 Audit mode

Periodic full-repo scans:
- Walk every source file in monitored paths
- Verify each has an ownership rule (or exception)
- Report orphaned rules (rule references files that don't exist)
- Report duplicate ownership (same source file in multiple rules)
- Report stale docs (referenced doc files don't exist)

Run quarterly or after major reorganization.

### 9.5 Pre-commit hook

Optional but recommended:

```bash
#!/usr/bin/env bash
# scripts/pre-commit
# Symlink: .git/hooks/pre-commit -> ../../scripts/pre-commit
set -euo pipefail
.venv/bin/python scripts/check_doc_coverage.py
.venv/bin/python scripts/check_test_coverage_drift.py --ci
.venv/bin/python -m validation.run_all --tier governance,logic
```

Catches issues before they reach the push, saving CI round-trips.

---

## 10. Anti-patterns to refuse

### 10.1 "Run it again" for flaky tests

❌ Pattern: test fails intermittently; operator re-runs CI; test passes; operator merges.

Why bad: flaky tests teach the team to ignore failures. The signal value of the entire test suite degrades.

✅ Fix: investigate the flake. Either fix the source of non-determinism (per § 1.4) or delete the test. Never tolerate "re-run and it passes."

### 10.2 Tests that mock the thing they're testing

❌ Pattern: `test_signal_builder` mocks the signal builder and asserts the mock was called.

Why bad: the test passes whether the real code works or not. Provides false confidence.

✅ Fix: test the real code with real (or fixture-realistic) inputs. Mock only the boundaries (DB, network, external APIs).

### 10.3 100% coverage as a goal

❌ Pattern: enforce 100% coverage; engineers add trivial tests for getters and constants to hit the metric.

Why bad: trivial tests aren't tests — they're noise. They take time to maintain and obscure the meaningful tests.

✅ Fix: focus coverage effort on critical paths (per § 1.5). Set coverage targets for monitored paths separately from non-critical code.

### 10.4 New alerting code without deliberate-failure test

❌ Pattern: add an alert path, verify the success path, ship.

Why bad: per `LESSONS L009`, the failure path is untested. Real failures may not produce the alert.

✅ Fix: deliberate-failure protocol from § 7. Always.

### 10.5 Sustained `allow_failure: true` jobs

❌ Pattern: a CI job has been failing every run for weeks; nobody has fixed it; nobody removes it.

Why bad: per `LESSONS L016`, allow-failure jobs become decoration. Operators learn to ignore the red X. Real failures blend in.

✅ Fix: when a job's underlying rationale changes, revisit it. Either restore real teeth (remove `allow_failure`) or remove the job. Don't leave it as decoration.

### 10.6 Notification per test failure

❌ Pattern: every failed test sends a separate Telegram message.

Why bad: alert fatigue. Operators silence the channel; real failures get missed.

✅ Fix: one summary notification per test run, per § 8.1.

### 10.7 Production data in test fixtures

❌ Pattern: copying a production DB snapshot to use as test fixture.

Why bad: PII risk, size bloat, non-determinism (production data changes), CI environment exposure.

✅ Fix: deterministic fixture data per § 6.2. Synthetic but realistic.

### 10.8 Tests that depend on test execution order

❌ Pattern: `test_b` only passes if `test_a` ran first because `test_a` set up some state.

Why bad: pytest runs tests in arbitrary order. Parallelization breaks the assumption. Refactoring the test file breaks the assumption.

✅ Fix: each test sets up its own state (via fixtures) and tears it down. Tests are independent.

### 10.9 Skipping the ownership model for "small" files

❌ Pattern: new file lands under a monitored path; ownership rule "will be added later"; later never comes.

Why bad: drift starts. By the time anyone notices, there are 5+ unmapped files and the ownership model has degraded.

✅ Fix: ownership rule lands in the same commit as the file. Per CLAUDE.md Rule 6.

### 10.10 Catching all exceptions in tests to make them "pass"

❌ Pattern: `try: assert_thing except: pass`

Why bad: the test passes regardless of whether the assertion held. Worse than no test.

✅ Fix: let assertions raise. If the test is genuinely expected to handle multiple outcomes, structure it explicitly with `pytest.raises` or equivalent.

### 10.11 Skipping the 24-hour staging soak

❌ Pattern: deploy to staging, smoke passes, promote to production within 30 min "because smoke verified it."

Why bad: per `archive/LESSONS.md` L022, some regressions only surface under live-data load over hours. Smoke is necessary but not sufficient for prod promotion. Skipping the soak window is gambling — the deploy MIGHT be fine, or it might exhibit a slow-burn regression that smoke structurally cannot catch.

✅ Fix: per § 7.5 — minimum 24 hours of staging soak between same-commit staging deploy timestamp and prod-eligibility. Soak is non-negotiable; the cost of waiting (~1 day) is dwarfed by the cost of a production regression that smoke didn't catch.

### 10.12 Treating first-fire of a new gate as production-grade

❌ Pattern: a new automated gate (smoke check, nightly job, deliberate-failure flow) passes its first fire in dev → operator marks it "ready" and schedules production work that depends on it.

Why bad: per `archive/LESSONS.md` L017, never-exercised gates accumulate latent assumptions. First fire reveals one of those assumptions; each fix reveals the next. Plan for 3-5 iterations before the gate is trustworthy. A gate that has been green once is not a verified gate.

✅ Fix: per § 5.6 — budget 1-2 hours for new gate first-fires; don't schedule them near deadlines; commit each iteration's fix separately so the cascade is visible in retrospect. Only after a gate has been exercised under its actual failure mode is it production-grade.

---

## End of standards

Validation is the only mechanism that catches regressions before they reach production. The patterns above feel like overhead until the day a deliberate-failure test catches a bug that would have caused a silent outage.

When a new validation pattern emerges from a debugging session, **add it here** with a cross-reference to the lesson in `archive/LESSONS.md`. When a rule above stops paying its weight, surface it for review — but never delete a rule without an explicit reason captured in `archive/LESSONS.md`.

The discipline scales: 5 minutes adding an ownership rule prevents hours of "why didn't anyone notice this drift" debugging. Slow down to validate well.
