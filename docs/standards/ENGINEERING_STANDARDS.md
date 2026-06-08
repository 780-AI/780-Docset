<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

# ENGINEERING_STANDARDS.md — Engineering Substrate

**Scope:** Coding standards, architecture invariants, secrets and configuration handling, error/logging philosophy, container discipline, healthcheck design, and operational patterns. Loaded when the work is "anything code" or architecture-shaping.

For testing specifics → `VALIDATION_STANDARDS.md`. For pipeline / deploy automation → `CICD_STANDARDS.md`. For governance / docs / manifest → `PROJECT_STANDARDS.md`.

**Why this file exists:** Every project re-discovers the same engineering trade-offs — when to add a layer, how to handle secrets, what to log, how to fail safely. Without a shared substrate, each project starts from scratch and the first month is spent re-litigating decisions that prior projects already paid for. This file captures those decisions as defaults.

---

## Table of Contents

1. [Architecture invariants](#1-architecture-invariants)
2. [Coding standards](#2-coding-standards)
3. [Configuration & secrets](#3-configuration--secrets)
4. [Error handling philosophy](#4-error-handling-philosophy)
5. [Logging standards](#5-logging-standards)
6. [Database access patterns](#6-database-access-patterns)
7. [Container discipline](#7-container-discipline)
8. [Healthcheck design](#8-healthcheck-design)
9. [Secrets rotation & token discipline](#9-secrets-rotation--token-discipline)
10. [Anti-patterns to refuse](#10-anti-patterns-to-refuse)

---

## 1. Architecture invariants

These are the load-bearing structural rules. Violating them creates silent coupling that's expensive to undo later.

### 1.1 Dependency direction (strict)

Modules form a directed acyclic graph. Dependencies flow in **one direction only**:

```
config/ ← lowest layer (no upstream deps)
core/ ← depends on config/
domain/ ← depends on config/, core/
strategies/ ← depends on config/, core/, domain/
live/, api/ ← depends on everything below
charting/ ← depends on config/, core/, domain/
```

**Rule:** lower-layer modules **never** import from higher-layer modules. `config/` and `core/` cannot import from `strategies/`, `live/`, `api/`, `charting/`.

Why: cycles in the dependency graph make the codebase impossible to reason about. A change in a "leaf" module (e.g., a strategy) should never force a change in a "root" module (e.g., config). When that pressure exists, the design is wrong, not the rule.

<!--
Example:
config/, core/ → never import from strategies/, live/, api/, charting/
config/instrument_config_bt.py → import-guarded; only config/config_resolver.py may import it
strategies/engine/persistence/ → may import from market_data/ but not vice versa
charting/ → depends on config/, strategies/engine/persistence/, market_data/models/
-->

### 1.2 Single source of truth (SSoT)

Each piece of information lives in exactly **one** canonical location:

- Configuration values: in the config file for that domain (e.g., `config/instrument_config.py` for instrument parameters)
- Schema definitions: in the migration file for that table (`migrations/NNN_*.sql`)
- API contracts: in the route definition + `docs/api_reference.md`
- Domain rules: in the source-of-truth doc + the code that implements them

If you find the same fact in two places, that is a **defect** per `PROJECT_STANDARDS.md` § 9. Resolve it: keep the canonical, replace duplicates with pointers.

### 1.3 Reuse before new modules

Before adding a new module:

1. `grep` for existing implementations
2. Check if existing module can be extended (with a parameter, an additional method, a config key)
3. Only add a new module if the responsibility is genuinely new

When in doubt: **extend, don't add**. New modules add surface area; extended modules consolidate it.

### 1.4 No new top-level directories without approval

Adding a new top-level folder (`api/`, `workers/`, `tools/`) is an architecture change requiring full Major workflow per `CLAUDE.md` §§ 5-6. Update `docs/folder_structure.md` and `docs/system_architecture.md` in the same commit.

### 1.5 Legacy / archive isolation

Files no longer in active use go to `archive/` and are excluded from manifest tracking (per CLAUDE.md Rule 8). Active code **never imports from** `archive/`.

If something in `archive/` is needed again: extract the relevant logic into an active module (with a fresh VERSION header), don't import from archive. Archive is for reference, not runtime.

### 1.6 Backtest vs live isolation (when applicable)

When a project has both backtest and live execution paths, isolate them at the configuration layer:

- A single resolver module bridges live and backtest configs
- Backtest configs are import-guarded — only the resolver may import them
- Backtest path forces the appropriate flags (e.g., historical mode) at config level, not at runtime

Why: the most expensive bug class in trading systems is "live config leaked into backtest" or vice versa. Architectural isolation prevents the bug, not runtime checks.

<!--
Example:
config/config_resolver.py — the ONLY module that bridges live + backtest
get_live_config — returns live config (DB_LOAD_MODE may be live_tail)
get_backtest_config — hard-forces db_load_mode="historical"
config/instrument_config_bt.py — runtime import-guarded; only config_resolver may import
BaseStrategy — gains config_override param; runtime guards detect mutation
-->

### 1.7 Live data invariants (when applicable)

Projects that operate on time-series live data face a class of bugs invisible to single-shot DB reads: data feeds may rewrite the same row multiple times during a settlement window. Detection logic operating inside that window sees mutable values; backtest detection operates on settled values. Per `archive/LESSONS.md` L021.

**Pattern:** every data row carries a "settlement state." Detection logic must declare which state it operates against.

- **Settled row:** all updates for this row are complete. Detection produces deterministic output.
- **Unsettled row:** the row's values may still update. Detection may produce different output across consecutive reads of the "same" row.

**Two acceptable designs:**

1. **Mutability-tolerant detection** — the function produces the same decision even as values evolve within the settlement window. Requires explicit design (e.g., only treat a row as decided once its settlement state flips).
2. **Settlement-delayed detection** — detection runs only against settled rows. Live operations have a built-in latency equal to the settlement window.

Document the settlement window per data provider in the project's domain doc. Backtest-vs-live reconciliation tests must account for the window: divergence within it is expected, not a bug.

<!--
Example:
Live data feed: each new candle row gets rewritten 6-7 times during the first ~10 min
as later ticks arrive (gap-fill window). Pattern detection running inside this window
sees mutable OHLC; backtest detection operates on settled OHLC. Detection logic adopted
the "settlement-delayed" pattern (max_age_minutes default 15.0; was 5.0 before D18 hotfix).
-->

### 1.8 Time-window parsing pitfalls (when applicable)

Projects that parse time-of-day windows (HH:MM strings → integer minute-of-day → range check) face two non-obvious behaviors. Per `archive/LESSONS.md` L037.

**Wrap-window with end="00:00".** When `start > end` is interpreted as "the window wraps midnight" (returning true for `now >= start OR now <= end`), an `end` value of `"00:00"` (= integer 0) causes the window to fire for exactly the minute `00:00` of the same day — `now <= 0` matches when `now = 0`. Operators who configured the window intending "until end of day" see a 1-minute false-positive fire at midnight before the window's intended start time.

**Recommendation — convention for "end of day" intent:**

- Use `"23:59"` (integer 1439) for "end of weekday" intent. This avoids the wrap-window branch entirely (`start < end` → normal in-day check).
- Reserve `end="00:00"` only when the wrap-into-the-next-day match IS intentional (e.g., `start="22:00" / end="02:00"` for an overnight window).

**Document both conventions** in the operator-facing input reference. The wrap-window behavior is correct semantically; it surfaces non-obviously at the day boundary. A clear convention prevents operator surprise.

**Implementation alternative — rejected as anti-pattern:** special-casing `end="00:00"` to mean "minute 1439" introduces a second non-obvious behavior. Prefer the explicit `23:59` convention.

**Inclusive-vs-exclusive endpoints.** Document whether the window includes its endpoints (`now >= start AND now <= end`) or excludes them (`now >= start AND now < end`). Both are valid; both must be documented. Operator-facing spec should show one example per direction (`08:30/12:30` → "matches 08:30:00 through 12:30:59" makes the inclusivity explicit).

<!--
Example:
Friday_NoTrade_Start=20:00 / Friday_NoTrade_End=00:00 → start=1200 > end=0 →
wrap-window branch. At Friday 00:00:00 broker time, dt.day_of_week==5 (Friday)
AND now=0 <= end=0 → matches for one minute. Operator-facing spec recommends
"23:59" for end-of-Friday intent. Project docs: docs/<domain-spec>/09_session_filter.md.
-->

### 1.9 Refactor blast-radius — grep all reads before splitting a globally-read state variable

When a globally-read state variable (a module-global, a singleton, a process-wide flag, a context-bound state field) needs to be **split** into multiple typed concerns, the refactor must include an explicit grep-and-classify pass BEFORE any edits. Per `archive/LESSONS.md` L039.

The anti-pattern this prevents: a "single mutable string with multiple meanings" that accreted over a project's history. Different consumers read it for different concerns (e.g., one reads for "auth status," another for "trade-block reason"). Refactoring it without an audit either:

1. **Strands a consumer** — leaves a site reading the old variable while peer sites move to the new helper. Compiles, behaves wrong at runtime.
2. **Over-aggressively rewrites a sibling concern** — converts an unrelated read site to use the new helper, breaking its semantic.

The pattern:

1. **Grep all reads first.** `grep -n '<varname>' <file>` (or multi-file equivalent). List every site.
2. **Classify each read** — which concern is it serving? (e.g., "auth diagnostic", "trade-block reason", "log-line content".) Three+ concerns surfacing in the grep is the canonical signal that a split is needed.
3. **Route each consumer in the same commit** as the refactor — either to the new helper that replaces this concern, OR explicitly leave it on the old variable with a one-line comment naming why.
4. **No silent stranding.** Every read site has an explicit disposition in the refactor commit.

This complements multi-file prompts (PROMPT_STANDARDS.md § 3): the grep-and-classify pass produces the per-site transformation rules that go into the prompt's § 5.

<!--
Example:
g_authStatus (a single string) carried two concerns — auth diagnostics
("not_checked", "auth_session_expired") AND trade-block reason codes ("no_trade_time_friday",
"closeout_management_only"). PLAN-004 split off the trade-block reasons into a
TradeBlockFlags struct + FormatBlockReasonText helper, leaving auth diagnostics
on the legacy variable. Plan § 11 risk #6 explicitly called for grep-and-classify
before Phase 3. Seven read sites, two concerns, clean split.
-->

---

## 2. Coding standards

### 2.1 Naming

- **Files:** lowercase with underscores (`pattern_engine.py`, `trade_simulator.py`). No camelCase, no kebab-case, no spaces.
- **Modules / packages:** lowercase, single word when possible (`config`, `core`, `strategies`)
- **Classes:** PascalCase (`PatternEngine`, `TradeSimulator`)
- **Functions / variables:** lowercase with underscores (`resolve_config`, `instrument_name`)
- **Constants:** UPPERCASE with underscores (`DEFAULT_PIP_SIZE`, `MAX_RETRIES`)
- **Private:** leading underscore (`_internal_helper`, `_DEFAULTS`)

Branch names follow a convention too: `<type>/<task-id>-<short-description>` (e.g., `feat/3.4-auto-rollback`, `fix/2.5b-image-source`). Stable branch names make tracker cross-references possible.

### 2.2 Type hints

- **Use type hints on all public functions** — signatures, return types, parameter defaults
- Internal helpers may skip type hints if the type is obvious from a 5-line function body
- Use `from __future__ import annotations` for forward references
- Avoid `Any` — if you find yourself reaching for `Any`, the design probably needs a Protocol or Union

### 2.3 Function size & structure

- **Functions should fit on one screen** (~30-50 lines). If a function is longer, it's doing more than one thing — extract.
- **One responsibility per function.** Name the responsibility in the function name. If the name needs `_and_` to be accurate, split.
- **Early return over nested conditionals.** Bail out on edge cases first; let the main logic flow at the lowest indentation level.
- **No mutation of arguments.** If you need to modify a dict or list passed in, deep-copy first. Mutation-by-reference is a major source of cross-module bugs.

### 2.4 Imports

- **Standard library first, third-party second, local third.** Three groups, blank line between.
- **No wildcard imports** (`from foo import *`) outside `__init__.py` re-exports.
- **No deep imports of internal symbols** — if you need `module._private`, the design is wrong. Either expose it properly or compose differently.
- **Import at top of file**, not inside functions, except for circular-dependency breakers (rare; usually a sign of architecture problem per § 1.1).

### 2.5 Comments & docstrings

- **Docstrings on all public functions** — one-line summary + parameter/return notes if not obvious.
- **Comments explain WHY, not WHAT.** If you find yourself describing what the code does, the code probably needs renaming or restructuring instead.
- **No commented-out code.** If it's not running, delete it. Git history preserves it if needed.
- **TODO comments are forbidden.** Per `PROJECT_STANDARDS.md` § 10.4, technical debt goes in the tracker's Deferred Items table, not in comments. Comments are silent; trackers are visible.

### 2.6 Quality bar

- Linter exits 0 on touched files
- Type checker (mypy/pyright) exits 0 on touched files (when configured)
- No new warnings introduced
- Tests pass (per `VALIDATION_STANDARDS.md`)

If a linter rule is genuinely wrong for the project's context, suppress it with an inline comment + reason — don't disable the rule globally.

---

## 3. Configuration & secrets

### 3.1 Configuration sources, in priority order

1. **Environment variables** — runtime overrides, secrets, infrastructure config
2. **Config files** (Python modules under `config/`, JSON, YAML) — domain parameters, defaults
3. **Database** — runtime state and per-instance preferences (e.g., active strategy profile per instrument)
4. **Hard-coded defaults in code** — last resort; only when the value would never plausibly change

Higher-priority sources override lower-priority sources.

### 3.2 Environment variable rules

- **All env vars documented in `docs/config_reference.md`** + `.env.example`
- **Naming:** UPPERCASE_WITH_UNDERSCORES, prefixed by domain (`DB_HOST`, `TELEGRAM_BOT_TOKEN`, `CI_REGISTRY_IMAGE`)
- **Booleans:** read as strings, parse explicitly. `os.getenv("FLAG", "false").lower == "true"`. Don't assume boolean coercion.
- **Required vars:** fail loudly at startup if missing, not silently with a default

### 3.3 Secrets handling

- **Never commit secrets.** Add to `.gitignore`: `.env`, `.env.local`, `*.pem`, `*.key`, `secrets/`
- **Provide `.env.example`** with all required variable names but no values (or placeholder values like `<your-token-here>`)
- **In CI:** secrets go in the CI provider's secret store (GitLab CI/CD Variables, GitHub Actions Secrets), marked Protected and Masked
- **In production:** secrets injected via environment, not baked into images
- **Rotation:** see § 9

### 3.4 Configuration access pattern

- Provide a `get_config` function or equivalent that returns a deep copy
- **Never expose the underlying config dict for mutation**
- **Read configs via the accessor; never import the dict directly**

Why: mutation-by-reference is the silent-bug pattern. Deep copy at the boundary prevents one module from corrupting config for another.

<!--
Example:
config/instrument_config.py: get_config returns a deep copy
config/config_resolver.py: get_live_config / get_backtest_config
ALLOWED_CFG_OVERRIDES frozenset: explicitly enumerates which keys may be overridden
-->

### 3.5 Configuration changes are Major

Per CLAUDE.md § 5: changes to config keys, defaults, or strategy parameters are Major. Full workflow applies. Changes update the config reference doc in the same commit.

### 3.6 Verify config source-of-truth before manual edits

Per `archive/LESSONS.md` L025 — when CI injects a config file on every deploy (e.g., `.env` from a CI variable), manual edits to the file on the host are **ephemeral**. The change survives until the next deploy, then disappears silently.

**Before any manual edit to a config file on a deployed host:**

1. Grep the CI configuration to see whether the file is injected
2. If injected: the host file is not the source of truth — the CI variable is
3. Manual edits to the host file are diagnostic-only; revert before next deploy
4. Durable changes go in the CI variable (which deploys to all envs)

**Line-count divergence between staging and prod `.env` files is a CI-injection tell** — if one has more lines than the other and both are supposed to be the same shape, one of them was edited locally and the other was re-injected by CI. Investigate before assuming either side is correct.

---

## 4. Error handling philosophy

### 4.1 Fail loud, fail fast, fail clearly

- **At startup:** validate required env vars, DB connections, external service reachability. Fail with a clear message if any are missing. Don't proceed with degraded state silently.
- **At runtime:** unrecoverable errors raise, get logged, and propagate to a top-level handler that decides whether to crash the process or degrade gracefully.
- **Never silently swallow exceptions.** Bare `except:` and `except Exception: pass` are forbidden in production paths.

### 4.2 Raise vs return

- **Raise** when the caller cannot reasonably proceed (invalid input, missing required state, broken invariant)
- **Return** a result type or sentinel when the caller expects to handle multiple outcomes (parsing, search, optional state lookup)
- **Don't mix** — if a function sometimes raises and sometimes returns None for the same logical condition, callers can't reason about it

### 4.3 Exception hierarchies

For meaningful exception handling, define project-specific exception classes:

```
class ProjectError(Exception):
 """Base for all project exceptions."""

class ConfigError(ProjectError):
 """Configuration is invalid or missing."""

class DataError(ProjectError):
 """Data is malformed or inconsistent."""
```

Catch specific types in handlers; never `except Exception:` except at top-level entry points.

### 4.4 Top-level error handlers

Every long-running process (worker, web server, CLI command) has a top-level exception handler that:

1. Logs the exception with full traceback (`logger.exception`)
2. Sends an alert if the failure is operationally significant (Telegram, PagerDuty, etc.)
3. Exits non-zero with a clear cause message (for CLI / job processes)
4. Restarts gracefully or crashes loudly (for long-running services)

**Never** print exceptions to stdout and continue. Stdout is for normal output; errors go to logs and alerting.

### 4.5 Retry policy

When retrying a failed operation:

- **Bounded retries** with explicit max count
- **Exponential backoff** for network/external service calls
- **Jitter** to prevent thundering herd if multiple instances retry simultaneously
- **Distinguish retryable vs non-retryable failures** — don't retry on auth failures, malformed input, etc.
- **Log every retry attempt** with attempt number and failure reason

### 4.6 Fail-safe defaults for external-data sources that may be unavailable

When integrating with an external data source that can degrade silently — test environment without prod data, missing optional config, third-party outage, regional unavailability — the module's "no data returned" branch must be a **no-op that lets the rest of the system run normally**, not an error branch that propagates upward. Per `archive/LESSONS.md` L040.

The pattern:

1. **Treat zero/empty as the fail-safe state.** Typically "no events found, no block, no warning" — whatever the safest default is for the consuming logic.
2. **Do not warn or error on absence.** These are normal degraded-environment behaviors, not bugs. The data source returning empty is a legitimate runtime state in non-prod environments.
3. **Log once at startup** — operator sees that the module is enabled but the data source is empty / unavailable; informational, not a warning.
4. **Continue running.** The rest of the system runs without the optional safety this module would have provided. The operator can re-enable it once the data source comes back.

This complements § 8.7 deliberate-failure testing: deliberate-failure ensures alerting fires when something IS wrong; fail-safe defaults ensure the absence of optional data doesn't masquerade as something being wrong.

Generalizes to: optional integrations (analytics, feature flags, second-opinion APIs, observability sinks); environments where production data isn't available (test, CI, staging-without-prod-mirroring); third-party services with regional or quota limits.

<!--
Example:
the application language CalendarValueHistory returns 0/-1 in Strategy Tester (calendar feed not populated
in tester mode); brokers without calendar feed return 0 always. The news-block module
treats this as "no events this poll" — silent skip, no warning, news block stays inactive.
Backtest runs without news data; EA runs cleanly on brokers without the feature.
-->

### 4.7 Safety tripwire for pattern-match drift against external catalogs

When pattern-matching against an external catalog of strings (event names, error codes, API status messages, ticker symbols, third-party object identifiers), include a **safety tripwire** that surfaces uncategorized items the operator might care about. Per `archive/LESSONS.md` L041.

Failure mode without a tripwire: a third party renames an item in the catalog (e.g., `"Nonfarm Payrolls"` → `"US NFP"`). The substring pattern stops matching silently. The module continues running, classifies the renamed item as "not matched, skip" — exactly the same code path as a legitimately-uninteresting item. Silent drift; only surfaces in post-hoc analysis or when a known item stops triggering the expected behavior.

The pattern:

- For each item the matcher receives that does NOT match any known pattern AND meets a "the operator might care about this" predicate (e.g., HIGH-impact tier, fatal error class, top-N volume ticker), log a single operator-visible line:

 ```
 UNCATEGORIZED <type>: "<value>" (<context>) — operator: review patterns.
 ```

- Log only the **first** occurrence per refresh cycle to avoid log spam — `uncategorized` is a "review your config" signal, not a per-event alert.
- Log location must be **operator-visible** (terminal log, chart panel, monitoring dashboard) — not silent in a debug-only stream.

The tripwire converts a silent miss into a noisy miss. The operator updates the pattern (one-line fix) when they see it. No automation needed — the LogInfo line IS the signal.

<!--
Example:
RefreshNewsBlockState matches calendar events by substring patterns against event.name.
Any HIGH or MOD-HIGH event on a tracked currency that does NOT match any pattern logs
`UNCATEGORIZED news event: "<name>" (<currency>, importance=<n>) — operator: review News_*
category patterns.` Operator sees it in the runtime platform Experts log; updates the pattern; one-line fix.
-->

---

## 5. Logging standards

### 5.1 Log levels

- **DEBUG:** developer-facing trace info; off in production
- **INFO:** lifecycle events (startup, shutdown, completion of significant operations)
- **WARNING:** unexpected-but-recoverable conditions; possible degradation
- **ERROR:** failures that affected behavior; operator should investigate
- **CRITICAL:** failures threatening system integrity; immediate operator attention

Don't ladder log levels artificially. If something is genuinely INFO, log INFO. Don't log everything as DEBUG to be "safe."

### 5.2 Structured logging

Prefer structured key-value logging over freeform strings:

```python
# ❌ Wrong
logger.info(f"Processed order {order_id} for user {user_id} in {duration}ms")

# ✅ Right
logger.info("Order processed", extra={"order_id": order_id, "user_id": user_id, "duration_ms": duration})
```

Why: structured logs are queryable. `grep` works on freeform strings; SQL/jq/log aggregators work on structured fields.

### 5.3 What to log

- **Lifecycle:** startup with config summary, shutdown, restart
- **External calls:** API requests/responses (sanitized), DB queries (timing, not content unless DEBUG)
- **Decisions:** significant branches taken (e.g., "switching to fallback provider", "skipping this instrument because criteria not met")
- **Errors:** every exception caught, with traceback at ERROR level

### 5.4 What NOT to log

- **Secrets:** tokens, passwords, API keys, full DB connection strings — even at DEBUG, even temporarily
- **PII:** user emails, phone numbers, addresses — unless required and audited
- **Full request bodies for high-traffic endpoints:** sample, don't log every request

### 5.5 Log format

- Timestamp in ISO 8601 with timezone (UTC preferred)
- Process / module identifier
- Level
- Structured fields
- Message

Example:
```
2026-04-25T11:52:39+03:00 [worker-1] [INFO] [signal_builder] Signal generated instrument=EURUSD direction=long entry=1.0852
```

### 5.6 Log retention

Application logs: rotate by size or time, keep ~30 days locally, ship to centralized aggregation if available.
Healthcheck logs: append-only, kept indefinitely or per project policy.
Audit logs (auth, admin actions): retained per regulatory requirements; never auto-purged.

---

## 6. Database access patterns

### 6.1 Single repository per concern

Each domain entity has **one** repository module that handles all its DB access. Other modules go through the repository — they never write SQL directly.

Why: scattered SQL is impossible to refactor when schema changes. Single repository = single point of update.

### 6.2 Connection management

- **Connection pool at application level**, not per-request
- **Connections returned to pool on context exit** — use `with` blocks, not bare `connect` / `close`
- **No long-held transactions** — keep transaction scope as small as possible
- **Read replicas** for heavy queries when available; writes always go to primary

### 6.3 Schema migrations

- Every schema change is a numbered migration: `001_initial.sql`, `002_add_users.sql`, ...
- Migrations are **append-only** — once a migration is applied to any environment, it's immutable
- Schema changes need a new migration; never edit an existing one
- Use `IF NOT EXISTS` / `IF EXISTS` for idempotency where supported
- Document the migration in `docs/database_schema.md` in the same commit

### 6.4 Column types & conventions

- **Timestamps:** `TIMESTAMPTZ` (timezone-aware), default `now`. Never `TIMESTAMP` (naive).
- **Timezone for stored times:** UTC. Convert to user/display timezone at presentation layer.
- **Primary keys:** auto-incrementing integer or UUID, depending on distribution requirements
- **Foreign keys:** explicit, with `ON DELETE` behavior specified (CASCADE, RESTRICT, SET NULL)
- **Indexes:** add when query patterns demand them, document in the migration that adds them

### 6.5 Upsert policy

- Use database-native upsert (`INSERT ... ON CONFLICT DO UPDATE` for Postgres, `MERGE` for others) when both insert and update paths are valid
- Never simulate upsert via `SELECT then INSERT or UPDATE` — race condition between check and act
- If an upsert needs additional logic, wrap it in a stored procedure or transaction

### 6.6 Direct API → DB writes

API endpoints generally **do not write directly to DB**. Routes call service modules that call repositories. The exception: simple configuration mutations (e.g., updating an active profile) where the write is the entire operation and there's no business logic in between. Document these exceptions in the API reference.

---

## 7. Container discipline

### 7.1 Dockerfile patterns

- **Multi-stage builds** to keep production images small (build stage + runtime stage)
- **Pin base image versions:** `python:3.11.15-slim`, not `python:3.11-slim` (which moves) and definitely not `python:latest`
- **Copy only what's needed:** use `.dockerignore` aggressively
- **Run as non-root user** in production images
- **Single CONCERN per image** — the image runs one service. Multi-service images create operational mess.

### 7.2 Image tagging

- **CI tags images with the commit SHA** — this is the canonical tag
- **A `latest` tag** is acceptable for development/staging convenience but never for production references
- **Never deploy to production using `latest`** — always pin to a specific SHA so rollbacks are deterministic

### 7.3 SHA length gotcha

Different CI providers use different SHA lengths. GitLab's `$CI_COMMIT_SHORT_SHA` is **8 characters**, not git's default 7. Test image existence using the SHA length your CI provider uses, not what `git rev-parse --short` returns locally.

### 7.4 Image source verification

When deploying, verify the running container's image source matches what was intended:

```bash
docker inspect <container> --format '{{.Config.Image}}'
```

For each application service, the image should match `<expected_registry_prefix>:<expected_sha>`. For upstream services (postgres, redis), the image should match a hardcoded expected prefix.

This catches silent fallback bugs (e.g., container running `myapp/backend:latest` instead of the intended registry-tagged image because of a `docker-compose.yml` substitution issue).

<!--
Example:
post_deploy_smoke.sh v0.2 Section 5 verifies:
- 6 application services match $EXPECTED_IMAGE_REGISTRY pattern
- 2 upstream services (postgres, redis) match hardcoded expected prefixes
Caught silent fallback bug from Task 2.5c where compose substituted `myapp/backend:latest`
when CI_REGISTRY_IMAGE was unset across SSH boundary.
-->

### 7.5 Upstream image pinning

For supply-chain hygiene, pin upstream images by digest:

```yaml
image: timescale/timescaledb@sha256:abc123...
```

Floating tags (`:latest-pg16`, `:7-alpine`) can change underneath you without warning. Digests are immutable. Trade-off: digest-pinned images don't get security patches automatically — pair with Renovate/Dependabot to propose bumps.

### 7.6 Compose pre-flight check

Before deploying:

```bash
docker compose config --quiet
```

This catches malformed compose files. For stricter checks, also verify that resolved image names match the expected pattern:

```bash
docker compose config | grep -E '^\s+image:' | grep -v <expected_prefix> && exit 1
```

Catches the silent-fallback class of bugs at deploy time, complementing § 7.4 which catches them at smoke time.

### 7.7 Volume management

- **Named volumes for data persistence** — never bind-mount host paths in production
- **Read-only mounts for code/config** that ships in the image
- **Backup procedures documented** for every persistent volume

### 7.8 Never run raw `docker compose up` on staging or production hosts

Per `archive/LESSONS.md` L024 — compose-file env-var substitution is silent. Running `docker compose up -d` interactively on a deploy host without exporting the right image-tag env vars silently downgrades the running container to a stale local-cache tag or empty-string fallback. The downgraded container looks identical (HTTP-wise) to a correctly-deployed container — caught only by image-source verification (§ 7.4).

**Rule:** on staging or production hosts, NEVER run raw `docker compose up`. Use either:

- `scripts/deploy.sh` (which exports all required env vars + pulls SHA-tagged image), OR
- Pre-tag the registry image with `docker tag <full-registry-path>:<sha> <local-alias>:<sha>` then restart via the deploy script

This applies in any environment beyond local development. Even diagnostic restarts go through the deploy script. The smoke check from § 7.4 is the catch-net, but the goal is to not need the catch-net — the manual command itself is the anti-pattern.

---

## 8. Healthcheck design

### 8.1 What healthchecks check

- **Service is responsive** (HTTP endpoint returns 200, container is "running")
- **Service can reach its dependencies** (DB, Redis, external APIs)
- **Service has not entered a degraded state** (queue depth, error rate over threshold)

The healthcheck verifies the service can do its job, not just that the process exists.

### 8.2 Healthcheck script structure

```bash
#!/usr/bin/env bash
# ==============================================================
# VERSION: X.Y
# Healthcheck for <project>
#
# CHANGE LOG
# vX.Y — YYYY-MM-DD HH:MM — <summary>
# ==============================================================
set -euo pipefail

# Layout-aware: detect script location, derive project paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="${PROJECT_DIR:-$(dirname "$SCRIPT_DIR")}"
ENV_DIR="${ENV_DIR:-$PROJECT_DIR}"

# Source environment for alerting credentials
[[ -f "$ENV_DIR/.env" ]] && { set -a; . "$ENV_DIR/.env"; set +a; }

# ... checks ...

# Report state, send alerts on transitions, exit with appropriate code
```

The layout-awareness pattern (detecting script location relative to project paths) makes the script reusable across staging and production environments without configuration changes.

### 8.3 Cron schedule

- **Every 5 minutes** is a typical cadence — frequent enough to catch issues quickly, infrequent enough to avoid alerting noise
- **Run as the application's operator user**, not root
- **Output to a log file**, not just exit codes — operators need a trail for postmortem

### 8.4 Alerting tiers

- **CRITICAL:** required services down, system non-operational. Immediate alert.
- **NOTICE:** optional services down, system degraded but functional. Lower-priority alert.
- **RECOVERY:** previously-down service back up. Closes the alert loop.

### 8.5 Recovery notifications

When a service transitions from DOWN → UP, emit a recovery notice. Without this, operators see the alert when something breaks but get no signal when it's resolved — they have to manually check.

Implementation: maintain a state file tracking last-known-state per service. On each run, compare current vs previous; if a transition happened, emit the appropriate notice.

### 8.6 Hostname tagging

Multi-environment deployments need to know which host generated an alert:

```
[CRITICAL] [project-staging-srv01] Service api is down
```

Tag the hostname in every alert. Operators can route by tag (staging issues to a dev channel, production to ops channel).

### 8.7 Deliberate-failure testing

Per `LESSONS L009` — every healthcheck change must be verified by deliberately inducing the failure mode and confirming the alert fires correctly. "Passes when correct" is insufficient.

---

## 9. Secrets rotation & token discipline

### 9.1 Rotation triggers

Rotate immediately when:
- Token suspected compromised (logs leaked, CI artifact exposed, ex-contributor)
- Token expiring within ~7 days
- Annual rotation hygiene (regardless of any other signal)

### 9.2 Rotation procedure

1. Generate new token in the source system (provider's UI / API)
2. Update the CI variable / secret store with the new token
3. Verify a test deployment succeeds with the new token
4. Revoke the old token in the source system
5. Document the rotation date in `archive/postmortems/` if it was triggered by a security event, otherwise just in tracker incident block

**Order matters:** add new before revoking old, to avoid downtime window.

### 9.3 Operator vs CI credentials

If both operators and CI use the same credential type (e.g., docker registry token), be aware that:
- CI runs may overwrite operator-installed credentials on the deploy host
- Manual operations after a CI run may need re-authentication
- Consider save/restore of operator credentials in the CI deploy script, OR document the manual re-auth wrapper as the canonical post-CI workflow

<!--
Example:
deploy.sh v3.0 overwrites /home/deploy/.docker/config.json on every CI run
with CI's short-lived deploy token. Manual rollback.sh after a CI deploy
fails until operator re-logs in. Documented as Phase 3 deferred item D8;
resolution is either save/restore in deploy.sh or accept the manual wrapper.
-->

### 9.4 Token expiry tracking

For tokens with expiry dates (deploy tokens, JWT-style tokens):
- **Tracker entry:** record token name + expiry date in the project tracker or a dedicated secrets log
- **Alert ~7 days before expiry** — calendar reminder, monitoring system, or manual schedule
- **Never let a token expire silently** — production incidents from expired tokens are entirely preventable

### 9.5 Where credentials live (forbidden vs allowed)

**Forbidden locations:**
- Committed code (any file in git)
- Application logs
- Public CI artifacts
- Slack/chat messages, email, document files
- Memory entries (per `MEMORY_PROTOCOL.md` — secrets are not memory candidates)

**Allowed locations:**
- CI provider's secret store (Protected, Masked)
- Server `.env` files (gitignored, file permissions `600`, owned by application user)
- Password manager / vault (1Password, Bitwarden, HashiCorp Vault)

### 9.6 Never type/display sensitive content in web-based VPS consoles

Per `archive/LESSONS.md` L035 — browser-based remote-terminal interfaces from cloud providers (a cloud VPS provider cloud console, AWS Session Manager web shell, GCP cloud console terminal, etc.) generally render typed and displayed content over the browser-to-cloud connection without the end-to-end encryption that SSH-from-local-terminal provides.

**Rule:** never use a web-based VPS console to type or display sensitive files:

- `.env` content, SSH keys, deploy tokens, API keys, passwords
- Database connection strings, certificate keys, signing keys
- Anything from the "Forbidden locations" list in § 9.5

**Alternatives:**

- SCP files to / from the host (`scp -i ~/.ssh/<key> <file> user@host:<path>`)
- SSH from your local terminal (end-to-end encrypted)
- Use the cloud provider's secrets-management UI (which has appropriate masking) for secret rotation

Applies to ALL cloud providers' web consoles, not just one specific provider. Phase 1 of a reference project codified this as a binding rule from day 1.

### 9.7 macOS disk-full recovery — restart, don't hunt caches first

Per `archive/LESSONS.md` L034 — on operator machines (especially macOS), "disk full" symptoms often present as misleading downstream errors (Rosetta hangs, container build failures, Docker pull errors). The instinct to "hunt caches" — clearing npm cache, Docker volumes, build directories — usually doesn't find the bottleneck because the actual disk pressure comes from filesystem snapshots that those caches don't account for.

**Procedure on macOS disk-full / "Rosetta hang" / "container build fails for no reason":**

1. Run `tmutil listlocalsnapshots /` first
2. If snapshots exist, restart the machine (which deletes them automatically) OR purge manually via `tmutil deletelocalsnapshots <date>`
3. Restart frees 30+ GB reliably
4. Skip cache-hunting until snapshot purge has been tried

Cross-platform applicability: the specific `tmutil` recipe is macOS-only. The general principle "investigate snapshot/checkpoint accumulation before hunting caches" applies to other OSes too (Linux: ZFS snapshots; Windows: shadow copies; Btrfs subvolumes).

---

## 10. Anti-patterns to refuse

### 10.1 Importing across layer boundaries

❌ Pattern: `config/foo.py` imports from `strategies/bar.py`

Why bad: violates dependency direction (§ 1.1). Creates a cycle that makes both modules harder to test and reason about.

✅ Fix: invert the dependency. The strategy depends on config, not the other way around. If config genuinely needs strategy data, the design is wrong — surface it for refactor.

### 10.2 Mutation of returned config dicts

❌ Pattern: `cfg = get_config; cfg["key"] = new_value`

Why bad: silent cross-module corruption. Other code reading `get_config` later sees the mutated value without knowing why.

✅ Fix: `get_config` returns a deep copy. Treat the returned dict as immutable in caller code. If you need to override, pass an `override` parameter through the legitimate mechanism.

### 10.3 Bare `except:` in production paths

❌ Pattern: `try: do_thing except: pass`

Why bad: silently swallows every error including KeyboardInterrupt and SystemExit. Bugs become invisible.

✅ Fix: catch specific exception types. If you genuinely don't care about a specific error, catch THAT specific error and log it.

### 10.4 Logging with f-strings (when structured logging is available)

❌ Pattern: `logger.info(f"Order {order_id} processed in {duration}ms")`

Why bad: log aggregators can't query the structured fields. Ad-hoc grep is the only retrieval method.

✅ Fix: use structured logging with `extra={}` (per § 5.2). Reserve f-strings for log formatting where the entire message is for human reading and never queried.

### 10.5 Direct DB writes from API routes

❌ Pattern: route handler executes SQL directly

Why bad: scattered SQL becomes impossible to refactor. Schema changes break in unpredictable places.

✅ Fix: route → service → repository. Each layer has one responsibility. SQL lives only in repositories.

### 10.6 Floating image tags in production

❌ Pattern: production deploys reference `:latest`

Why bad: rollback to "the previous version" is undefined — `:latest` may have changed multiple times. Production behavior becomes non-reproducible.

✅ Fix: always pin production deploys to specific commit SHAs. Rollback = pull the previous SHA, not the previous `:latest`.

### 10.7 Healthcheck that only verifies the process exists

❌ Pattern: `pgrep myservice && exit 0`

Why bad: a hung process is "running" but useless. Healthcheck passes; service is actually broken.

✅ Fix: verify the service can do its job — hit its actual endpoint, check it can reach its dependencies, check it's processing work.

### 10.8 Secrets in `.env.example`

❌ Pattern: committing `.env.example` with real (or even "test") values

Why bad: even test credentials are credentials. Once in git history, permanently leaked.

✅ Fix: `.env.example` has variable names only, with placeholder text like `<your-token-here>` or empty values.

### 10.9 Token rotation without overlap

❌ Pattern: revoke old token, then add new token

Why bad: deployments / cron jobs running during the gap fail with auth errors.

✅ Fix: add new token, verify it works, then revoke old. Always overlap.

### 10.10 New module instead of extending existing one

❌ Pattern: every new feature gets a new module

Why bad: surface area explodes. Future contributors have to learn N small modules instead of M well-structured larger ones.

✅ Fix: extend before adding. Per § 1.3 — new modules only when responsibility is genuinely new, not when convenient.

### 10.11 Manual edits to CI-injected config files

❌ Pattern: SSH to a deployed host, edit `.env` directly, expect the change to persist.

Why bad: per `archive/LESSONS.md` L025, if CI injects `.env` from a CI variable on every deploy, the manual edit is ephemeral. The change works until the next deploy, then disappears silently. Operator wastes ~45 min debugging "why is my config change reverting" before finding the CI-injection pattern.

✅ Fix: per § 3.6 — verify source-of-truth before manual edits. Grep CI config FIRST. Durable changes go in the CI variable, not the host file. Line-count divergence between staging and prod `.env` is a CI-injection tell.

### 10.12 Raw `docker compose up` on staging or production hosts

❌ Pattern: interactively run `docker compose up -d` on a deploy host to "restart services."

Why bad: per `archive/LESSONS.md` L024, compose-file env-var substitution is silent. Missing-or-unset image-tag vars resolve to empty strings or stale local-cache tags. The downgraded container looks identical to a correct deploy — caught only by image-source verification (§ 7.4).

✅ Fix: per § 7.8 — never raw `compose up` on deploy hosts. Use the deploy script (or pre-tag the registry image). Even diagnostic restarts go through the deploy script.

---

## End of standards

The engineering substrate is the layer most exposed to the daily flow of work. Every shortcut taken here costs compound interest later. The patterns above feel like overhead in week one and feel like sanity in month six.

When a new engineering pattern emerges from a debugging session, **add it here** with a cross-reference to the lesson in `archive/LESSONS.md`. When a rule above stops paying its weight, surface it for review — but never delete a rule without an explicit reason captured in `archive/LESSONS.md`.

The discipline scales: a 10-minute design discussion prevents a 2-hour cleanup later. Slow down to architect well.
