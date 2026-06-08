<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.0 — 2026-06-07 — Clean domain-neutral baseline. Project identity and source-domain
specifics removed; examples genericized. Established as Standard Set Version v1.0.
-->

# CICD_STANDARDS.md — Pipeline Architecture & Deploy Patterns

**Scope:** CI/CD pipeline architecture, stage and job topology, deploy patterns (registry-pull, SSH-based), smoke testing requirements, rollback design, production deploy gating, operator workflows. Loaded when the work touches `.gitlab-ci.yml`, deploy scripts, rollback scripts, registry configuration, or pipeline architecture.

For test framework details (which tier runs when, ownership model) → `VALIDATION_STANDARDS.md`. For Docker discipline (image tagging, healthcheck design, container layout) → `ENGINEERING_STANDARDS.md`. For the governance side (CHANGELOG entries, manifest, doc updates that accompany pipeline changes) → `PROJECT_STANDARDS.md`.

**Why this file exists:** CI/CD pipelines are unforgiving. A subtle defect in a job graph or a deploy script can silently corrupt production state, ship the wrong image, or leave operators unable to roll back. Every pattern below was learned from a specific incident on a reference project — silent fallback bugs, env-var-export-across-SSH issues, registry-pull refactors, smoke gating, auto-rollback design. The file exists so future projects don't re-discover these the hard way.

---

## Table of Contents

1. [Pipeline architecture philosophy](#1-pipeline-architecture-philosophy)
2. [The standard 6-stage shape](#2-the-standard-6-stage-shape)
3. [Job conventions](#3-job-conventions)
4. [CI variables — types and discipline](#4-ci-variables--types-and-discipline)
5. [Build patterns — registry & image lifecycle](#5-build-patterns--registry--image-lifecycle)
6. [Deploy patterns — the registry-pull model](#6-deploy-patterns--the-registry-pull-model)
7. [Smoke testing & deploy gating](#7-smoke-testing--deploy-gating)
8. [Rollback design](#8-rollback-design)
9. [Production deploy gate (manual click)](#9-production-deploy-gate-manual-click)
10. [Auto-rollback on smoke failure](#10-auto-rollback-on-smoke-failure)
11. [Operator workflows & common gotchas](#11-operator-workflows--common-gotchas)
12. [Pipeline change validation](#12-pipeline-change-validation)
13. [Anti-patterns to refuse](#13-anti-patterns-to-refuse)

---

## 1. Pipeline architecture philosophy

Five principles that shape every job in the pipeline.

### 1.1 Stages are gates, not buckets

Each stage represents a guarantee about what came before. If `test` passes, the next stage can assume tests pass. If `build` passes, the next stage can assume there's a valid image. Don't put unrelated jobs in the same stage just because they have similar names — a bucket holds things of any kind; a gate holds back what hasn't earned passage.

### 1.2 Tier mapping per `VALIDATION_STANDARDS.md`

Test tiers (governance, logic, contracts, integration, smoke, scheduled) map to specific pipeline jobs and triggers. Don't invent ad-hoc job structure — use the tier mapping from § 5 of VALIDATION_STANDARDS.md.

### 1.3 Build once, deploy many

The image built in the `build` stage is the **same image** deployed to staging and (later) to production. Never rebuild between environments — that breaks the "what was tested is what was deployed" guarantee.

### 1.4 The deploy host is dumb

Deploy hosts (VPS, cloud instances, Kubernetes nodes) should not build images, fetch source code, or run governance scripts. They pull pre-built images from the registry and run them. This shrinks the deploy host's responsibility surface to "run containers correctly" — easier to operate, easier to swap, easier to harden.

### 1.5 Production gating is dispositive

A staging smoke pass is the only condition under which production deploy can proceed. No staging smoke = no production deploy. This is non-negotiable. The cost of waiting for staging smoke (~2-5 minutes) is dwarfed by the cost of a production failure.

---

## 2. The standard 6-stage shape

```
test → build → deploy → verify → deploy-prod → verify-prod
```

Each stage runs only after all prior stages pass.

### 2.1 Stage 1 — `test`

Runs every test tier appropriate for per-push validation: governance, logic, contracts, integration. Per `VALIDATION_STANDARDS.md` § 5.

Jobs in this stage are **required (`allow_failure: false`)** in steady state. A failing test stage blocks the pipeline.

### 2.2 Stage 2 — `build`

Builds the Docker image, tags with the commit SHA, pushes to the registry.

Single job typically. Image tag uses the CI's short SHA (8 chars on GitLab — see `ENGINEERING_STANDARDS.md` § 7.3).

### 2.3 Stage 3 — `deploy` (staging)

Pulls the just-built image to the staging host and starts it. Auto-runs on every push to master (no manual gate).

Single job. SSH-based deploy is common; the deploy script lives in `scripts/deploy.sh`.

### 2.4 Stage 4 — `verify` (staging smoke)

Runs `scripts/post_deploy_smoke.sh` (or equivalent) against staging. Verifies all services responsive, image sources match expectations, basic functionality works.

Required (`allow_failure: false`). Failure here blocks promotion to production deploy. See § 7 for content; § 9-10 for gating semantics.

### 2.5 Stage 5 — `deploy-prod`

Identical mechanics to staging deploy, but targets production host and is **manually triggered** (per § 9). Does not auto-run.

### 2.6 Stage 6 — `verify-prod`

Production smoke. Same script as staging smoke (`post_deploy_smoke.sh`), but pointed at production host.

If this stage fails, auto-rollback (per § 10) kicks in — the production deploy is reverted to the previous SHA without operator intervention.

---

## 3. Job conventions

### 3.1 Job naming

Job names tie to the tier or stage they represent:

- `governance` — Tier 1 governance scripts (doc coverage, drift)
- `logic-tests` — Tier 2 unit tests
- `contract-tests` — Tier 4 contract tests
- `integration-tests` — Tier 3 integration tests
- `build` — image build + push to registry
- `deploy-staging` — pull + run on staging
- `smoke-staging` — Tier 5 smoke against staging
- `deploy-production` — pull + run on production (manual trigger)
- `smoke-production` — Tier 5 smoke against production
- `rollback-production` — fix-forward fallback if `smoke-production` fails (per § 10)
- `nightly` — Tier 6 scheduled runs (separate scheduled pipeline, not in the per-push pipeline)

Naming consistency makes the pipeline visualization readable and makes failures easier to triage.

### 3.2 Job structure (GitLab CI example)

```yaml
job-name:
 stage: <stage>
 image: <runner-image>
 needs:
 - <prior-job> # cross-stage dependencies
 rules:
 - if: $CI_COMMIT_BRANCH == "master"
 - when: manual # for manual-gate jobs
 variables:
 KEY: value
 before_script:
 - <setup commands>
 script:
 - <main commands>
 after_script:
 - <cleanup; runs even on failure>
 artifacts:
 paths:
 - <files to preserve>
 expire_in: 1 week
```

### 3.3 `needs:` for cross-stage shortcuts

Use `needs:` to express job-level (rather than stage-level) dependencies. A `verify` job that only depends on `deploy-staging` (not on every test job) lets the pipeline parallelize where possible.

But: `needs:` references must point at jobs in earlier stages (or the same stage with `needs: []` allowed). Cross-stage references in the wrong direction cause pipeline-creation failure (per `LESSONS L005` — the dispositive validation is the real pipeline run).

### 3.4 `allow_failure` — use sparingly, with expiry

Per `LESSONS L016` and `VALIDATION_STANDARDS.md` § 5.3:

- **No sustained `allow_failure: true`** in steady state
- If genuinely needed temporarily: state expiry in the rationale (commit message + tracker entry)
- Revisit when the underlying rationale changes — either restore real teeth or remove the job

### 3.5 Artifacts vs cache

- **Artifacts** = outputs preserved across jobs (test reports, built binaries, deploy logs)
- **Cache** = speedups for individual jobs (pip cache, npm cache, build cache)

Don't conflate. Artifacts are observable; cache is invisible. Use the right one.

### 3.6 Artifact retention

- **Test reports:** 1-4 weeks (long enough to investigate flaky tests after the fact)
- **Built images:** stored in the registry, not as artifacts (registry is the canonical store)
- **Deploy logs:** 1-2 weeks (long enough for operator investigation; archive if longer is needed)

---

## 4. CI variables — types and discipline

### 4.1 Variable types

Most CI providers support multiple variable types. Use them correctly:

- **Variable** — plain string. Visible in job logs unless masked. Use for non-secret config (hostnames, image registries, environment names).
- **File** — written to a temp file, path injected as the variable's value. Use for SSH private keys, certificates, multi-line secrets.
- **Masked** — value is redacted in job logs. Use for secrets that might appear in script output.
- **Protected** — only available on protected branches/tags. Use for production credentials.

### 4.2 Standard variable taxonomy

Most projects need these classes of variables:

| Class | Example names | Type | Protected? |
|---|---|---|---|
| Registry credentials | `CI_REGISTRY_USER`, `CI_REGISTRY_PASSWORD` | Variable / Masked | Yes |
| Deployment SSH keys | `STAGING_SSH_KEY`, `PRODUCTION_SSH_KEY` | File | Yes (prod), No (staging) |
| Host addresses | `STAGING_HOST`, `STAGING_USER`, `PRODUCTION_HOST` | Variable | Yes (prod) |
| Service tokens | `TELEGRAM_BOT_TOKEN`, `DATABASE_URL` | Variable / Masked | Yes |
| Image references | `CI_REGISTRY_IMAGE` (provider-supplied) | Variable | n/a |

### 4.3 Variable scope

- **Project-level variables** — apply to all pipelines for the project
- **Group-level variables** — apply to all projects in the group (organization-wide secrets)
- **Pipeline-level variables** — set when manually triggering a pipeline (rare)

Prefer project-level for project-specific secrets; group-level for organization-wide secrets like Slack webhook URLs.

### 4.4 The export-across-SSH gotcha

When a CI job SSHes to a deploy host and runs commands there, **CI variables are NOT automatically inherited** by the SSH session. The remote shell starts fresh with no environment.

Wrong:
```yaml
script:
 - ssh user@host "docker pull $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
```

The `$CI_REGISTRY_IMAGE` is interpolated locally before SSH (this part works), but if the remote command needs the variable to exist as an env var (e.g., for a docker-compose substitution), it won't be there.

Right:
```yaml
script:
 - ssh user@host "export CI_REGISTRY_IMAGE='$CI_REGISTRY_IMAGE' CI_COMMIT_SHORT_SHA='$CI_COMMIT_SHORT_SHA' && docker pull \"\$CI_REGISTRY_IMAGE:\$CI_COMMIT_SHORT_SHA\""
```

Or pass via environment file scp'd to the host. See § 6 for the canonical deploy pattern that handles this correctly.

<!--
Example:
deploy.sh v2.x silently used `myapp/backend:latest` because docker-compose's
${CI_REGISTRY_IMAGE} substitution resolved to empty string in the SSH session
where CI_REGISTRY_IMAGE wasn't exported. The compose file's fallback `${VAR:-fallback}`
syntax kicked in and pulled the wrong image. Smoke test passed because the wrong image
also responded to HTTP. Caught only by image-source verification (Task 2.5d) which
explicitly checks `docker inspect` output against expected registry prefix.

Resolution: deploy.sh v3.0 (Task 3.3) eliminated the SSH-substitution dependency
entirely by switching to `docker pull <full-image-path-with-sha>` from the registry,
no compose-file substitution involved.
-->

### 4.5 Documenting variables

`docs/ci_cd.md` must list every CI variable the pipeline expects, with:
- Variable name
- Type (Variable, File, Masked, Protected)
- Purpose (one line)
- Where it's set (provider's UI path)
- Rotation policy (if applicable)

When a new variable is added, update this doc in the same commit per `PROJECT_STANDARDS.md` § 4.

---

## 4.6 Telegram integration conventions

CI/CD pipelines that send notifications via Telegram bots must follow these conventions to prevent silent delivery failures and configuration drift.

### Chat ID formats

Telegram chat IDs come in two distinct formats:

- **Private DM:** Positive integer (e.g., `2022764690`). Used for direct messages between a user and the bot. Requires the user to have started a conversation with the bot via `/start`.
- **Group/Channel:** Negative integer with `-100` prefix (e.g., `-1001234567890`). Used for groups, supergroups, and channels. Requires the bot to be a member of the chat with appropriate permissions (admin if posting to channels).

These are NOT interchangeable. A bot configured to post to a `-100...` group ID will return HTTP 400 if it's no longer a member of that group. A bot configured for a private DM cannot post to a group it has never been added to.

### CI variable masking rule

GitLab CI variable masking is for **secrets only** — tokens, passwords, API keys, signing keys. Identifiers like chat IDs, host names, paths, and usernames must NOT be masked.

**Rationale:**
- Masking has minimum-length and character-shape requirements that often conflict with identifier formats (e.g., negative chat IDs starting with `-` have masking edge cases that cause silent expansion failures)
- YAML aliasing of masked variables (e.g., `TELEGRAM_BOT_TOKEN: "$TELEGRAM_STAGING_BOT_TOKEN"`) has known expansion bugs with masked sources in some GitLab runner versions
- Identifiers leak into logs anyway via API responses and error messages, so the security benefit of masking is illusory
- Defensive over-application of masking creates more bugs than it prevents

**Rule:**
- **Mask:** `*_BOT_TOKEN`, `*_PASSWORD`, `*_API_KEY`, `*_SECRET`, `*_PRIVATE_KEY`
- **Don't mask:** `*_CHAT_ID`, `*_HOST`, `*_PATH`, `*_USER`, `*_PORT`

### Naming and aliasing convention

Use environment-namespaced variable names in the GitLab CI/CD Variables UI:

- `TELEGRAM_STAGING_BOT_TOKEN`
- `TELEGRAM_STAGING_CHAT_ID`
- `TELEGRAM_PROD_BOT_TOKEN`
- `TELEGRAM_PROD_CHAT_ID`

Then alias to canonical names in job-level `variables:` blocks for jobs that read the canonical names (e.g., the validation framework's notifier reads `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID`):

````yaml
nightly:
 stage: test
 variables:
 TELEGRAM_BOT_TOKEN: "$TELEGRAM_STAGING_BOT_TOKEN"
 TELEGRAM_CHAT_ID: "$TELEGRAM_STAGING_CHAT_ID"
````

**Rationale:**
- No value duplication — the staging token lives in exactly one GitLab var
- Env-namespace clarity preserved in the GitLab UI
- Future prod jobs follow same pattern with `TELEGRAM_PROD_*` source vars
- Validation framework (or whatever code reads the vars) doesn't need to know about env-namespacing

### Pre-deploy verification

Before relying on a new Telegram-notification path in CI, verify end-to-end with a manual fire of the schedule/job. Per `LESSONS.md` L017 cascade observation, never-exercised gates often fire bugs in cascade — first run reveals one config issue → fix → second run reveals different config issue → etc. Plan for 3-5 iterations before the gate is fully green. See also `VALIDATION_STANDARDS.md` § 5.6.

---

## 4.7 CI-injected config files are wiped on every deploy

When CI injects a config file (`.env`, secrets file, `config/runtime.json`, etc.) from a CI variable on every deploy, manual edits to that file on the host are **ephemeral**. Per `archive/LESSONS.md` L025.

**Symptoms:**

- Operator edits `.env` on staging/prod; the change works
- Hours later, the change has reverted with no edit history visible on the host
- Line-count divergence between staging `.env` and prod `.env` files (one has been operator-edited, the other CI-re-injected) — **this is the CI-injection tell**

**Rule — verify source-of-truth before any manual edit to a deployed-host config file:**

1. Grep the CI configuration to see whether the file is injected
2. If injected: the host file is not the source of truth — the CI variable is
3. Manual edits to the host file are diagnostic-only; revert before next deploy
4. Durable changes go in the CI variable (which deploys to all envs — see § 9.8 staging mirrors production)

**Document in `docs/ci_cd.md`:** which config files are CI-injected, which are durable on the host, and the path to the CI variable that sources each injected file.

See also `ENGINEERING_STANDARDS.md` § 3.6 (same rule, code-side framing).

---

## 5. Build patterns — registry & image lifecycle

### 5.1 The build job

```yaml
build:
 stage: build
 image: docker:latest
 services:
 - docker:dind
 script:
 - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
 - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA .
 - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
```

Output: a registry-stored image tagged with the commit SHA. Same image used for staging and (later) production.

### 5.2 Image tagging — the canonical SHA tag

- **Always tag with the commit SHA** (`$CI_COMMIT_SHORT_SHA`)
- **Optionally also tag `latest`** for development convenience — but **never deploy production using `latest`** per `ENGINEERING_STANDARDS.md` § 7.2
- **Never tag with branch names** for deployable images — branches are mutable; deployed image tags must be immutable

### 5.2.1 Smoke verification: prefix-only vs freshness

Smoke tests that verify "the right image is running" can do so at two levels of strictness:

**Prefix-only verification (current the standards source pattern):**
- Smoke checks: `RUNNING_IMG` starts with `${EXPECTED_REGISTRY_PREFIX}:` or `${EXPECTED_REGISTRY_PREFIX}@`
- Catches: wrong-registry deploys (e.g., a Docker Hub image accidentally deployed instead of the project's registry image)
- Does NOT catch: stale-image silent deploys (e.g., `:latest` tag pointing at an older image because deploy never actually pulled the new SHA)

This pattern is acceptable when:
- `deploy.sh` has explicit `exit 1` on `docker pull` failure (Scenario B silent-fallback requires a Docker-level bug, which is rare)
- Rollback is fast and well-tested
- Platform is solo-operator and pre-customer
- Deploy frequency is low

**Freshness verification (option (a) upgrade path):**

When the platform grows, upgrade smoke to verify the running image matches the expected SHA, not just the registry prefix:

- Compose references `${APP_IMAGE_TAG}` directly: `image: ${CI_REGISTRY_IMAGE}/backend:${APP_IMAGE_TAG}`
- `deploy.sh` exports `APP_IMAGE_TAG=$CI_COMMIT_SHORT_SHA` before `compose up`
- `rollback.sh` exports `APP_IMAGE_TAG=$ROLLBACK_SHA` before `compose up`
- Smoke Section 5 checks: `RUNNING_IMG` ends with `:${CI_COMMIT_SHORT_SHA}` or `@<digest>`

**Trigger conditions for the upgrade:**
- Multiple operators deploying (more chance of silent confusion)
- Paying customers affected by downtime (cost of stale deploy is real)
- High deploy frequency (more opportunities for the rare Docker bug to hit)
- Compliance/audit requirements that demand provable image-source freshness

**the standards source status (as of 2026-04-28):** Prefix-only pattern accepted per D10 (see `cicd_setup_tracker.md` Phase 3 Deferred Items). Upgrade to freshness verification deferred to Phase 4 architectural work when one or more trigger conditions hold.

### 5.3 The 8-char SHA gotcha

GitLab's `$CI_COMMIT_SHORT_SHA` is **8 characters**, not git's default 7. Image tags use 8 chars throughout. When probing the registry for image existence (e.g., in rollback scripts), use 8-char SHAs:

```bash
docker manifest inspect $CI_REGISTRY_IMAGE:${SHA:0:8} # Correct
docker manifest inspect $CI_REGISTRY_IMAGE:${SHA:0:7} # Wrong; returns NOT FOUND
```

Per `ENGINEERING_STANDARDS.md` § 7.3.

### 5.4 Multi-stage builds

Per `ENGINEERING_STANDARDS.md` § 7.1 — use multi-stage Dockerfiles to keep production images small. Build stage installs dev dependencies; runtime stage copies only the application.

### 5.5 Registry hygiene

Old SHA-tagged images accumulate in the registry. Without cleanup, the registry grows indefinitely. Mitigations:

- **Registry retention policies** at the provider (delete tags older than N days, except specific protected tags)
- **Periodic manual cleanup** of legacy tags (e.g., the `latest` migration left old `myapp/backend:latest` images that are no longer used)
- **Don't auto-delete tags currently deployed** — provider policies usually have allowlist syntax for this

Track legacy-image cleanup as a tracker Deferred Item; address during quiet windows.

### 5.6 Upstream image pinning

Per `ENGINEERING_STANDARDS.md` § 7.5 — pin upstream images by digest:

```yaml
services:
 - name: postgres@sha256:abc...
```

Pair with Renovate/Dependabot to propose digest bumps automatically.

---

## 6. Deploy patterns — the registry-pull model

This is the canonical pattern: CI builds image → registry stores image → deploy host pulls image → runs it.

### 6.1 The deploy script structure

```bash
#!/usr/bin/env bash
# ==============================================================
# VERSION: X.Y
# Deploy <project> to <environment>
#
# CHANGE LOG
# vX.Y — YYYY-MM-DD HH:MM — <summary>
# ==============================================================
set -euo pipefail

# Required environment (provided by CI):
: "${CI_REGISTRY_IMAGE:?missing}"
: "${CI_COMMIT_SHORT_SHA:?missing}"
: "${TARGET_HOST:?missing}"
: "${TARGET_USER:?missing}"
: "${SSH_KEY:?missing}"

# Layout-aware: where do we deploy on the host?
PROJECT_DIR="${PROJECT_DIR:-/home/$TARGET_USER/<project>}"

# 1. Authenticate to registry on the deploy host
ssh -i "$SSH_KEY" "$TARGET_USER@$TARGET_HOST" "docker login -u <user> -p <token> $CI_REGISTRY"

# 2. Pull the SHA-tagged image
ssh -i "$SSH_KEY" "$TARGET_USER@$TARGET_HOST" \
 "docker pull $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"

# 3. Update compose file or equivalent to reference the new image
# (compose substitution requires careful handling — see § 4.4)

# 4. Restart services
ssh -i "$SSH_KEY" "$TARGET_USER@$TARGET_HOST" \
 "cd $PROJECT_DIR && docker compose up -d"

# 5. Record the deploy SHA for rollback
ssh -i "$SSH_KEY" "$TARGET_USER@$TARGET_HOST" \
 "echo $CI_COMMIT_SHORT_SHA > $PROJECT_DIR/.last-deploy"

# 6. Wait briefly for services to start
sleep 5
```

### 6.2 Layout-awareness

The deploy script accepts `PROJECT_DIR`, `ENV_DIR`, and similar paths as overridable env vars. Different environments (staging, production) may have different directory layouts; the script adapts rather than hardcoding.

This is the same layout-awareness pattern as `ENGINEERING_STANDARDS.md` § 8.2 (healthcheck design).

### 6.3 The `.last-deploy` state file

After every successful deploy, write the deployed SHA to `$PROJECT_DIR/.last-deploy`. The rollback script (per § 8) reads this to determine "the previous good SHA."

```bash
echo "$CI_COMMIT_SHORT_SHA" > "$PROJECT_DIR/.last-deploy"
```

This is a **post-success write** — only update `.last-deploy` after the deploy verification passes (or after smoke success). Otherwise rollback would target a known-bad SHA.

### 6.4 Authentication on the deploy host

The deploy host needs registry credentials to pull images. Two patterns:

- **Operator credentials:** human operator runs `docker login` once on the host with their personal token. Long-lived but personal.
- **CI credentials:** every CI deploy run logs in fresh with a short-lived deploy token, overwriting any prior auth.

The CI-credentials pattern is more secure (short-lived, rotatable, scoped to deploy permission only) but introduces an operator-interaction gotcha: after a CI deploy, manual operations (like `rollback.sh` invocation) need re-authentication because CI overwrote the operator's auth.

<!--
Example:
deploy.sh v3.0 overwrites /home/deploy/.docker/config.json with CI's deploy token
on every CI run. Manual rollback.sh after a CI deploy fails until operator
re-logs in. Documented as Phase 3 deferred item; resolution is either save/restore
of operator credentials in deploy.sh OR document the manual re-auth wrapper as the
canonical post-CI workflow.

Manual re-auth wrapper:
read -s -p "Token: " T && echo "$T" | ssh -i ~/.ssh/staging \
 user@host 'docker login registry.gitlab.com -u <token-name> --password-stdin' \
 && unset T
-->

### 6.5 Deploy host has no source code

The deploy host pulls **only the image** from the registry. It does not clone the repo, does not have git, does not run governance scripts. The image contains everything needed to run.

The exception: small operational scripts (`scripts/deploy.sh`, `scripts/rollback.sh`, `scripts/post_deploy_smoke.sh`, `scripts/healthcheck.sh`) can live on the host because they orchestrate Docker rather than being part of the application. CI scp's these to the host on each deploy (so they stay in sync with the repo) or they're managed via configuration management.

### 6.6 Compose file management

`docker-compose.prod.yml` lives on the host. CI's deploy script either:

- **scp's the compose file** to the host as part of each deploy (keeps host in sync with repo)
- **Edits the compose file in place** to reference the new image SHA (older pattern; harder to audit)

The scp pattern is preferred: the host's compose file is always whatever's in the repo at the deployed SHA.

### 6.7 The "DO NOT PUSH" handoff doesn't apply here

Unlike the multi-file Cursor prompts (where the human pushes), CI deploys ARE the autonomous step. The human "pushed" by triggering the pipeline; the deploy job is the agent acting on that intent. No further human gate per push — but per § 9, production deploys still require manual click.

---

## 7. Smoke testing & deploy gating

The post-deploy smoke (`scripts/post_deploy_smoke.sh` or equivalent) is the canonical "did the deploy actually work" check. Per `VALIDATION_STANDARDS.md` § 2.5.

### 7.1 What the smoke verifies

- **Container state:** all services in the compose file are running (not Exited, not Restarting)
- **HTTP endpoints:** application services return 200 on health endpoints
- **DB connectivity:** services can reach the DB (write + read roundtrip)
- **Notification reachability:** alerting channel is reachable (e.g., Telegram bot can send a test message)
- **Image source verification:** the running container's image matches the expected registry prefix and SHA (per `ENGINEERING_STANDARDS.md` § 7.4)

### 7.2 Image source verification — required

This is the check that catches the silent-fallback bug class (per `LESSONS L005` and Task 2.5c/2.5d on the standards source). For every application service:

```bash
ACTUAL_IMAGE=$(docker inspect <container> --format '{{.Config.Image}}')
case "$ACTUAL_IMAGE" in
 "$EXPECTED_REGISTRY_PREFIX:$EXPECTED_SHA") ok ;;
 *) fail "Service <name> running unexpected image: $ACTUAL_IMAGE" ;;
esac
```

For upstream services (postgres, redis), check against hardcoded expected prefixes — they shouldn't change SHAs per deploy.

This check is **required**, not optional. Without it, silent-fallback bugs are undetected.

### 7.3 Smoke is required, not allow_failure

Per § 3.4 and `LESSONS L016` — smoke jobs must be `allow_failure: false`. A smoke failure means the deploy is broken; the pipeline must reflect that.

### 7.4 Smoke runs against the just-deployed environment

- `smoke-staging` SSHes to the staging host, runs `post_deploy_smoke.sh` there (or runs equivalent checks remotely)
- `smoke-production` does the same for production

The script is identical; the target host differs. Layout-awareness (per § 6.2) handles environment differences.

### 7.5 Smoke duration target

Smoke should run in **under 2 minutes**. Faster means quicker pipeline turnaround; slower means smoke-staging's gate becomes a bottleneck for production deploys.

If smoke is slow:
- Parallelize independent checks
- Cache slow setup (SSH connection reuse, container inspect calls)
- Move slow non-essential checks to a separate post-deploy job that doesn't gate production

### 7.6 Smoke failure → no progression

If `smoke-staging` fails:
- The pipeline fails at the verify stage
- The deploy-production job stays unavailable (manual gate from § 9 doesn't appear)
- Operator investigates, fixes, fix-forward (per CLAUDE.md Rule 3) ships a new commit

If `smoke-production` fails:
- Auto-rollback fires (per § 10)
- Operators are alerted (per `VALIDATION_STANDARDS.md` § 8)
- Postmortem follows

---

## 8. Rollback design

Rollback is the recovery path when production deploys go bad. Two flavors: manual operator rollback and auto-rollback (per § 10).

### 8.1 The rollback script structure

```bash
#!/usr/bin/env bash
# ==============================================================
# VERSION: X.Y
# Rollback <project> to a previous SHA
#
# CHANGE LOG
# vX.Y — YYYY-MM-DD HH:MM — <summary>
# ==============================================================
set -euo pipefail

# Layout-aware
PROJECT_DIR="${PROJECT_DIR:-/home/<user>/<project>}"
LAST_DEPLOY_FILE="$PROJECT_DIR/.last-deploy"

# Mode 1: explicit target SHA passed as arg
# Mode 2: no arg = read from .last-deploy and use the SHA *before* the current one

TARGET_SHA="${1:-}"

if [[ -z "$TARGET_SHA" ]]; then
 # Auto-detect: get current deployed SHA, find the one before it
 TARGET_SHA=$(get_previous_sha_from_history)
fi

# Validate target SHA exists in registry
docker manifest inspect "$REGISTRY:$TARGET_SHA" >/dev/null 2>&1 \
 || fail "Image $REGISTRY:$TARGET_SHA not found in registry"

# Pull and switch
docker pull "$REGISTRY:$TARGET_SHA"
update_compose_to_use_sha "$TARGET_SHA"
docker compose up -d

# Write back to .last-deploy
echo "$TARGET_SHA" > "$LAST_DEPLOY_FILE"

# Send rollback notification
send_alert "Rolled back to $TARGET_SHA"
```

### 8.2 Two invocation modes

**Mode 1 — explicit target:** operator provides the SHA they want to roll back to. Used for "I know exactly which deploy was good."

**Mode 2 — auto-detect previous:** no SHA arg; script reads the current deployed SHA, queries deploy history (or `.last-deploy` file), and picks the previous good SHA.

Both modes verify the target SHA exists in the registry before pulling.

### 8.3 The `.last-deploy` write-back

After a successful rollback, **update `.last-deploy`** to reflect the rolled-back SHA. Without this, subsequent rollback invocations would treat the bad SHA as the previous good one — a rollback-of-the-rollback that returns to the broken state.

### 8.4 Idempotent NO-OP rollback

If the operator runs rollback when the target SHA is already the deployed SHA, the script should detect this and exit cleanly (not error):

```
[INFO] Already at SHA $TARGET_SHA. No-op.
```

This handles the "operator double-clicked the rollback button" case.

### 8.5 Auto-detect forward (recovery)

After rolling back, if the operator wants to re-deploy a fixed forward SHA, the same script handles it:

```bash
./rollback.sh <new-fix-forward-sha>
```

The script doesn't care about direction — it just switches to whatever SHA you tell it. "Rollback" is a name for the script, not a constraint on motion.

### 8.6 Rollback test cases

Before shipping a rollback script, run these tests deliberately (per `VALIDATION_STANDARDS.md` § 7):

1. **Bad SHA:** rollback to a SHA that doesn't exist in the registry → script exits non-zero with clear message
2. **Missing image:** rollback to a SHA whose image was registry-purged → script exits non-zero
3. **Explicit happy path:** rollback to a known-good SHA → services switch, `.last-deploy` updates
4. **Idempotent NO-OP:** rollback to the currently-deployed SHA → script exits zero, no-op message
5. **Auto-detect forward:** after a rollback, run rollback again with the original SHA → script switches forward correctly

If any test fails, fix-forward (Rule 3); don't ship until all 5 pass.

### 8.7 Manual rollback authentication caveat

Per § 6.4 — after a CI deploy, manual rollback invocations may need re-authentication if CI overwrote the operator's docker login. Document the manual re-auth wrapper as the canonical post-CI workflow.

### 8.8 Telegram alert dependency on `.env` sourcing

If the rollback script sends Telegram alerts using credentials from `.env`, the operator's manual invocation must source `.env` first:

```bash
ssh -i ~/.ssh/key user@host 'cd ~/project && set -a && . ~/.env && set +a && bash scripts/rollback.sh <SHA>'
```

Without sourcing `.env`, alerts skip silently — script appears to work but no notification trail. Document this as the canonical wrapper.

---

## 9. Production deploy gate (manual click)

Production deploys are not autonomous. Every production deploy requires explicit operator action.

### 9.1 The manual gate

```yaml
deploy-production:
 stage: deploy-prod
 needs:
 - smoke-staging # gated on staging smoke success
 rules:
 - if: $CI_COMMIT_BRANCH == "master"
 when: manual # require manual trigger
 script:
 - bash scripts/deploy.sh
```

`when: manual` means the job appears in the pipeline UI but doesn't auto-run. Operator clicks "Play" to trigger it.

### 9.2 Why manual

Production has higher cost-of-failure than staging. Even with strong smoke gating, a final human gate prevents:

- Auto-deploying changes the operator hasn't reviewed yet
- Auto-deploying during operator-incompatible windows (lunch, on-call handoff, etc.)
- Auto-deploying when external context (incident in another system, customer event) suggests waiting

The operator's click is the affirmative "yes, ship this now."

### 9.3 Gating on smoke-staging success

The `needs: [smoke-staging]` clause means `deploy-production` is only available after `smoke-staging` passes. If staging smoke fails, the manual button doesn't appear — operators can't accidentally promote a broken deploy.

### 9.4 Production smoke

After the manual deploy-production job runs, `smoke-production` runs automatically (no second manual gate). The "click to deploy" is the human-in-the-loop checkpoint; smoke verification is autonomous.

### 9.5 Alternative: scheduled deploy windows

For higher-risk projects, augment the manual gate with scheduled deploy windows:

- Allow production deploys only during specified hours (e.g., business hours, never on Fridays)
- Implement via CI rules with date/time conditions
- Document the policy in `docs/runbook.md`

the standards source doesn't use scheduled windows currently, but the pattern is available if needed.

### 9.6 Operator preparation before clicking

Before clicking "deploy production":

- Verify staging smoke is green
- Read the diff between the last production SHA and the candidate SHA (`git log --oneline <last-prod>..<candidate>`)
- Note any concerning changes for monitoring during smoke
- Have the rollback procedure ready (per § 8) in case smoke fails

These are operator-discipline patterns that go in `docs/runbook.md`, not in the CI script.

### 9.7 24-hour staging soak required before production deploy

Per `archive/LESSONS.md` L022 — for systems operating on time-series live data (or any data shape where slow-burn regressions are possible), **no production deploy until 24 hours after the same commit's staging deploy timestamp**. The soak window resets if any new commit lands in the deploy-candidate.

Rationale (see also `VALIDATION_STANDARDS.md` § 7.5):

- Smoke catches "the deploy is technically running" failure modes
- Some regressions only surface under live-data load over hours (compaction effects, accumulated state, slow memory leaks)
- The 24h soak is the slow-burn equivalent of deliberate-failure injection — it catches the failure class smoke can't

Soak is **in addition to** smoke verification — both must pass. The 24h window is the minimum; high-risk deploys (schema migrations, infrastructure changes) may extend further per the project's runbook.

**Operator soak tracking:**

- Document the staging deploy timestamp in the tracker incident block for the deploy
- Calculate prod-eligibility = staging-deploy + 24h
- The PROD-deploy authorization request (per § 9.9) MUST include both timestamps

If staging deploy is older than 24h AND a newer commit landed in the deploy-candidate during the window, the soak resets to start from the newer commit's staging deploy.

### 9.8 Staging mirrors production — env parity

Per `archive/LESSONS.md` L023 — every prod config / secret / profile change has a parallel staging change in the same operator session. **Staging FIRST**, then prod.

**Anti-pattern this prevents:** plans that describe "prod-only" actions. Any plan defining a one-off prod-only change is wrong by default. Durable changes go in CI config (which targets both envs), not host files (which get wiped by the next deploy — see § 4.7 / L025).

**Procedure:**

1. Identify the change (config, secret, profile, env var, etc.)
2. Apply to staging first via the CI variable (or via the documented procedure for non-CI durable state)
3. Verify on staging (smoke, soak if applicable per § 9.7)
4. Apply to prod via the same mechanism (different variable scope: prod-protected vs staging)
5. Verify on prod

Both env's stay in sync at the config layer. CI-injection (L025) wiping is impossible because the change is in the CI variable, not the host file.

**Exception — genuinely env-specific values:**

Some values are legitimately env-specific (staging IP vs prod IP; staging chat ID vs prod chat ID). These have parallel-but-different values in their respective CI variable scopes. Document the env-specific pairs in `docs/ci_cd.md` so the parallelism is auditable.

### 9.9 Explicit PROD-action authorization (no bundling)

Per `archive/LESSONS.md` L030 — every PROD deploy / SSH apply / restart / config change gets its OWN labelled authorization round, separate from any staging cycle. **Never bundle PROD in a flow summary.**

**Wrong pattern:**

> "Approve the full deploy cycle: staging deploy → staging smoke → prod deploy → prod smoke?"

The operator's "approve" may mean "approve the staging part" (with prod gated separately). Ambiguity breeds drift between operator intent and agent interpretation.

**Right pattern:**

> Step 1 authorization: "Approve staging deploy of `<SHA>`?"
> [staging deploys, smoke passes, 24h soak completes]
> Step 2 authorization (separate round): "Authorize PROD deploy of `<SHA>` after 24h staging soak completed at `<timestamp>`?"

Operator must explicitly confirm "yes, PROD" — never inferred from staging approval.

**The PROD authorization request must include:**

1. The candidate SHA
2. The staging deploy timestamp (proves soak started)
3. The calculated soak-completion timestamp (proves prod-eligibility)
4. Any diff highlights worth flagging during prod smoke watch

If the request is malformed (missing any element), reject it pending the missing data. Malformed prod requests are how operators end up approving things they didn't fully review.

---

## 10. Auto-rollback on smoke failure

When `smoke-production` fails, auto-rollback returns production to the previous good SHA without operator intervention.

### 10.1 The rollback-prod job

```yaml
rollback-production:
 stage: verify-prod
 needs:
 - deploy-production
 rules:
 - if: $CI_COMMIT_BRANCH == "master"
 when: on_failure # only run if a prior job in the stage failed
 script:
 - bash scripts/rollback.sh
 - bash scripts/post_deploy_smoke.sh # re-verify after rollback
```

`when: on_failure` means this job runs only when an earlier same-stage or upstream-needed job failed. Specifically, it runs when `smoke-production` fails (the only job that fails into `verify-prod` stage).

### 10.2 Why auto-rollback

Smoke failure on production means the just-deployed SHA is broken. Three possible operator responses:

1. Manually trigger rollback (slow; operator may not be present)
2. Leave production broken (worst; users see the failure)
3. Auto-rollback (immediate; production returns to last-known-good)

Option 3 is the only one that maintains availability without depending on operator presence.

### 10.3 Auto-rollback notification

When auto-rollback runs, send a high-priority alert immediately:

```
[CRITICAL] Production smoke failed for $CI_COMMIT_SHORT_SHA
[CRITICAL] Auto-rollback initiated to <previous-sha>
```

After rollback completes:

```
[RECOVERY] Auto-rollback complete; production now at <previous-sha>
```

If the rollback ALSO fails (rare but possible — registry unreachable, target SHA deleted):

```
[CRITICAL] Auto-rollback FAILED. Manual intervention required.
```

### 10.4 Post-rollback smoke

After auto-rollback completes, re-run smoke against the rolled-back state. This confirms the rollback target was actually good (it passed smoke when originally deployed, but may have decayed since).

### 10.5 Auto-rollback is idempotent

Per § 8.4 — if the rolled-back SHA is somehow the same as the failed SHA (edge case: rollback target wasn't recorded), the script no-ops cleanly with a clear message rather than failing.

### 10.6 Disable conditions

Some scenarios warrant disabling auto-rollback:

- **Schema migrations:** if the failed deploy applied a migration, rolling back the image but not the migration leaves the system in an inconsistent state. Schema migrations should be deployed during dedicated maintenance windows with auto-rollback temporarily disabled (operator-coordinated process documented in runbook).
- **Investigation deploys:** rare cases where the operator explicitly wants to investigate a failed deploy before rolling back (e.g., reproducing a customer-impacting bug live).

**Implementation guidance — two paths depending on platform maturity:**

**Doc-only mitigation (initial implementation, suitable for pre-customer / solo-operator platforms):**
- No CI variable override mechanism.
- Document the schema migration risk in `docs/runbook.md` "Auto-rollback behavior" section.
- Schema migration deploys are coordinated manually: operator pauses the auto-rollback regime by NOT running deploys during the migration window, OR temporarily comments out the rollback-production rule in `.gitlab-ci.yml` for that pipeline run.
- Acceptable when migration cadence is low (months between schema changes) and operator count is small (one person knows the procedure).

**Code override (mature implementation, suitable for production-customer platforms):**
- CI variable `DISABLE_AUTO_ROLLBACK=1` set per-pipeline via "Run pipeline" UI.
- `rollback-production` job rule extended: `when: on_failure` AND `$DISABLE_AUTO_ROLLBACK != "1"`.
- Operator sets the variable when triggering a migration deploy.
- Required when migration cadence is higher OR multi-operator (procedure must be discoverable in the tool, not just the runbook).

**Trigger conditions for upgrading from doc-only to code override:**
- Schema migration deploys happen more than monthly.
- More than one operator has push access to master.
- Customer impact of an accidentally-rolled-back migration is non-trivial (data inconsistency, downtime).

**the standards source status (as of 2026-04-28):** Doc-only mitigation per Task 3.4 e-2 decision. Schema is currently stable (no near-term migrations planned). Upgrade to code override deferred to Phase 4 if/when trigger conditions hold.

### 10.7 Deliberate-failure test

Per `VALIDATION_STANDARDS.md` § 7 / `LESSONS L009` — auto-rollback must be deliberate-failure tested:

- Deliberately deploy a known-broken image to staging (auto-rollback fires for staging too in this test setup)
- Confirm rollback executes, target SHA is correct, post-rollback smoke passes
- Confirm alerts arrived (CRITICAL → RECOVERY chain)
- Document the test in tracker

Without this test, auto-rollback is unverified — the failure path may have a syntax bug that has never been exercised.

---

## 11. Operator workflows & common gotchas

### 11.1 Operator workflows documented in `docs/runbook.md`

- "How to deploy to staging" (push to master, watch pipeline, observe smoke)
- "How to deploy to production" (verify staging smoke, click deploy-production, observe smoke-production)
- "How to manually rollback" (per § 8, including the `.env` sourcing wrapper)
- "How to investigate a smoke failure" (logs, container state, common causes)
- "How to handle auto-rollback firing" (read alerts, check post-rollback smoke, postmortem the original failure)

### 11.2 Common gotchas (from the standards source experience)

**Gotcha 1: 8-char vs 7-char SHA**

GitLab's `$CI_COMMIT_SHORT_SHA` is 8 characters. Local `git rev-parse --short HEAD` returns 7 by default. Mixing these in scripts causes "image not found" errors. Always use 8 chars when querying the registry.

**Gotcha 2: docker auth overwrite**

CI deploys overwrite the deploy host's docker auth. Manual rollback after a CI deploy needs re-authentication first (per § 6.4 / § 8.7).

**Gotcha 3: env-var-export-across-SSH**

CI variables don't auto-propagate across SSH. Use the export pattern from § 4.4 or pass via env file.

**Gotcha 4: stale `.last-deploy` after manual rollback**

If manual rollback doesn't update `.last-deploy`, subsequent rollback invocations target wrong SHAs. Always write back per § 8.3.

**Gotcha 5: legacy `:latest` images on the deploy host**

Old `:latest` tags accumulate. Periodic cleanup needed (track as Deferred Item).

**Gotcha 6: auto-rollback during a schema-migration deploy**

Rolling back an image without rolling back its migration leaves an inconsistent system. Disable auto-rollback for migration deploys per § 10.6.

### 11.3 Production deploy day checklist

Before clicking deploy-production:

- [ ] Staging smoke passed (verify in pipeline UI)
- [ ] **24-hour staging soak completed** (per § 9.7 — confirm staging-deploy timestamp + 24h has elapsed)
- [ ] **No new commits landed in deploy-candidate during the soak window** (per § 9.7 — soak resets if newer commit lands)
- [ ] **Explicit PROD-action authorization issued** (per § 9.9 — separate round from staging approval)
- [ ] Diff reviewed (`git log <last-prod>..<candidate>`)
- [ ] CHANGELOG entry present for the deploy
- [ ] No active incidents elsewhere that would conflict with deploying
- [ ] Operator is available for next ~30 minutes to monitor smoke
- [ ] Rollback procedure (manual + auto) understood for this deploy

After clicking deploy-production:

- [ ] smoke-production passes
- [ ] Healthcheck (per `ENGINEERING_STANDARDS.md` § 8) shows all services healthy
- [ ] No customer-impacting alerts firing
- [ ] CHANGELOG / tracker updated to reflect the deploy

### 11.4 Never bounce operator to CI UI for status — agent probes via REST API

Per `archive/LESSONS.md` L031 — when pipeline status / job status / job trace info is needed, the agent's default is to probe the CI provider's REST API directly. **Never bounce the operator to the CI UI** to copy-paste status snippets.

**Why:** in any session that involves CI monitoring, operator UI-bouncing accumulates 5-10 min per session of context-switching cost. Multiplied across many sessions, it adds up. The CI provider's API exposes everything the UI shows.

**Token storage (operator-machine convention):**

- Token kept at `~/.<provider>-token` (gitignored, per-machine, file permissions `600`)
- Never in any tracked file, never in user-wide memory
- Per-project access details (project ID, base URL, token path) go in the project's Project Instructions Tier B (per `PROJECT_INSTRUCTIONS_TEMPLATE.md` § 5.9)

**GitLab REST API recipes (use as template; adapt for other providers):**

```bash
TOKEN=$(cat ~/.gitlab-token)
PROJECT_ID=<your-project-id>
BASE=https://gitlab.com/api/v4

# List pipelines:
curl -s -H "PRIVATE-TOKEN: $TOKEN" "$BASE/projects/$PROJECT_ID/pipelines?per_page=10" | jq .

# Latest pipeline status:
curl -s -H "PRIVATE-TOKEN: $TOKEN" "$BASE/projects/$PROJECT_ID/pipelines?per_page=1" | jq '.[0]'

# Jobs in a pipeline:
PIPELINE_ID=<pipeline-id>
curl -s -H "PRIVATE-TOKEN: $TOKEN" "$BASE/projects/$PROJECT_ID/pipelines/$PIPELINE_ID/jobs" | jq '.[] | {name, status, stage}'

# Job trace (full log output):
JOB_ID=<job-id>
curl -s -H "PRIVATE-TOKEN: $TOKEN" "$BASE/projects/$PROJECT_ID/jobs/$JOB_ID/trace"
```

For GitHub Actions, use the equivalent `gh` CLI or REST API endpoints (`/repos/:owner/:repo/actions/runs`, `/jobs/:job_id/logs`, etc.).

**Pattern:** any time the operator would have to copy status from a CI UI for the agent, the agent runs the curl recipe instead. Surface the relevant fields (status, duration, failed steps, trace excerpt) directly in the chat.

---

## 12. Pipeline change validation

Per CLAUDE.md Rule 5 / `LESSONS L005` — local YAML parse and governance scripts validate Python and YAML syntax — **not** GitLab/GitHub-specific job-graph semantics.

### 12.1 What local checks DO catch

- YAML syntax errors (`python -c "import yaml; yaml.safe_load(...)"`)
- Doc coverage drift (`scripts/check_doc_coverage.py`)
- Test ownership drift (`scripts/check_test_coverage_drift.py --ci`)

### 12.2 What local checks DO NOT catch

- `needs:` references to jobs that don't exist
- `stage:` values not in the `stages:` array
- `rules:` clause logic errors
- `dependencies:` graph cycles or missing entries
- `extends:` template inheritance issues

### 12.3 The dispositive validation is the real pipeline run

For any change to `.gitlab-ci.yml` (or `.github/workflows/`) touching `needs:`, `stage:`, `rules:`, `dependencies:`, or `stages:`:

- Push to a feature branch first if possible — observe the pipeline behavior
- If pushing directly to master: accept that the first push may surface CI defects
- Per CLAUDE.md Rule 3 — fix-forward as letter-suffix sub-tasks; never `git push --force`

### 12.4 GitLab CI Lint API

GitLab provides a CI Lint API (`/api/v4/projects/:id/ci/lint`) that validates the YAML against GitLab's job-graph rules without running the pipeline. For projects where every CI defect costs time, integrate this into pre-push checks. Most projects find the cost of integration outweighs the benefit and accept the fix-forward pattern.

### 12.5 Pipeline change checklist

Before pushing a CI YAML change:

- [ ] YAML parses cleanly (`python -c "..."`)
- [ ] Doc coverage check passes
- [ ] If touching `needs:`, `stage:`, `rules:`, etc. — accept that first push may fail; have fix-forward plan ready
- [ ] `docs/ci_cd.md` updated if pipeline structure changed (per `PROJECT_STANDARDS.md` § 4)
- [ ] CHANGELOG entry mentions pipeline change with explicit impact

---

## 13. Anti-patterns to refuse

### 13.1 Building images on the deploy host

❌ Pattern: `ssh deploy-host "git pull && docker build && docker compose up"`

Why bad: deploy host needs source code, build tools, and CI-equivalent state. Slow (rebuilds every deploy). Breaks "build once, deploy many" guarantee. Couples deploy reliability to source availability.

✅ Fix: build in CI, push to registry, deploy host pulls per § 6.

### 13.2 Floating tags in production

❌ Pattern: `docker pull myimage:latest` in production deploy.

Why bad: `:latest` is mutable. Yesterday's `:latest` and today's `:latest` may be different images. Rollback to "previous version" is undefined.

✅ Fix: always pin to commit SHA per § 5.2 / `ENGINEERING_STANDARDS.md` § 7.2.

### 13.3 Skipping smoke after deploy

❌ Pattern: deploy job marks success based solely on `docker compose up` exit code.

Why bad: containers can start and exit, or start and be unresponsive, or start with the wrong image (silent fallback). Compose's exit code only tells you the command ran.

✅ Fix: always run smoke per § 7. Smoke is required, not optional.

### 13.4 `allow_failure: true` on smoke or test jobs

❌ Pattern: smoke job marked `allow_failure: true` "until we figure out the flaky test."

Why bad: per `LESSONS L016`, allow-failure jobs become decoration. The whole pipeline UI degrades.

✅ Fix: fix the flake. If genuinely impossible short-term, mark allow-failure WITH expiry date in commit message + tracker entry. Revisit on the expiry date.

### 13.5 Production deploys without manual gate

❌ Pattern: every push to master auto-deploys to production.

Why bad: operator has no chance to review before production ships. Bad changes ship as fast as good ones.

✅ Fix: manual gate per § 9. The 30 seconds for an operator to click is worth the safety.

### 13.6 Auto-rollback without deliberate-failure test

❌ Pattern: ship auto-rollback CI job, verify it doesn't fire on green deploys, ship to production.

Why bad: the failure path is untested. When auto-rollback is needed for the first time, syntax bugs in the failure-handling code surface in production.

✅ Fix: deliberately deploy a broken image to staging (or a test environment) and verify the auto-rollback path fires correctly. Per `VALIDATION_STANDARDS.md` § 7.

### 13.7 Force-pushing CI YAML changes

❌ Pattern: CI YAML change fails on push; amend and force-push to "fix it."

Why bad: violates CLAUDE.md Rule 3 / `LESSONS L003`. Erases the broken state from history. The lesson is lost.

✅ Fix: fix-forward as a new commit with letter suffix. Per § 12.3.

### 13.8 Hardcoded credentials in deploy scripts

❌ Pattern: deploy.sh contains `docker login -u user -p hardcoded_token`.

Why bad: token in git history is permanently leaked. Even if rotated, the old token leaked the auth pattern. Secrets in code are a forbidden location per `ENGINEERING_STANDARDS.md` § 9.5.

✅ Fix: secrets via CI variables (Protected, Masked) or environment files on the deploy host. Never in scripts.

### 13.9 Different commands in `deploy.sh` vs `rollback.sh`

❌ Pattern: deploy.sh uses `docker compose up` but rollback.sh uses `docker run` directly.

Why bad: rollback path is exercised rarely, so divergence accumulates. When rollback is finally needed, behavior differs from deploy in unexpected ways.

✅ Fix: rollback.sh is structurally identical to deploy.sh except for the SHA being targeted. Same compose file, same restart sequence, same notifications.

### 13.10 Skipping the `.last-deploy` write

❌ Pattern: deploy.sh succeeds but never updates `.last-deploy`; rollback can't auto-detect the previous SHA.

Why bad: rollback in auto-detect mode targets stale or empty `.last-deploy` content. Wrong rollback target or no rollback at all.

✅ Fix: deploy.sh writes `.last-deploy` only after successful deploy + smoke. Rollback.sh reads from it. Per § 6.3 / § 8.

### 13.11 Raw `docker compose up` on staging or production hosts

❌ Pattern: SSH to a deploy host and run `docker compose up -d` interactively to "restart services."

Why bad: per `archive/LESSONS.md` L024, compose-file env-var substitution is silent. Missing-or-unset image-tag vars resolve to empty strings or stale local-cache tags. The downgraded container looks identical to a correct deploy — caught only by image-source verification (§ 7.2). Operator's confidence in manual ops drops every time this happens.

✅ Fix: use `scripts/deploy.sh` (which exports all required env vars + pulls the SHA-tagged image), OR pre-tag the registry image with `docker tag` then restart via the deploy script. Never raw compose-up on staging or production. See also `ENGINEERING_STANDARDS.md` § 7.8.

### 13.12 Bouncing operator to CI UI for status checks

❌ Pattern: agent asks operator to "check the pipeline UI and tell me if it's green."

Why bad: per `archive/LESSONS.md` L031, this accumulates ~5-10 min per session of operator context-switching. The CI provider's REST API exposes everything the UI shows; the agent can probe directly.

✅ Fix: per § 11.4 — agent runs the documented API curl recipes. Token at `~/.<provider>-token`. Per-project access details in Project Instructions Tier B.

### 13.13 Skipping the 24-hour staging soak

❌ Pattern: staging smoke passes → promote to production within an hour because "smoke verified it."

Why bad: per `archive/LESSONS.md` L022, some regressions only surface under live-data load over hours (compaction effects, accumulated state, slow leaks). Smoke is necessary but not sufficient. Skipping the soak is gambling.

✅ Fix: per § 9.7 — minimum 24 hours of staging soak between same-commit staging deploy timestamp and prod-eligibility. Soak resets if a newer commit lands in the deploy-candidate. Soak is non-negotiable.

### 13.14 "Prod-only" config or secret changes

❌ Pattern: plan describes a config / secret / profile change that's applied only to production, "because staging doesn't need it."

Why bad: per `archive/LESSONS.md` L023, any plan describing "prod-only" actions is wrong by default. Durable changes go in CI config (which targets both envs), not host files. Manual prod-host edits get wiped by the next CI deploy (per § 4.7 / L025). Staging and prod drift in config-shape.

✅ Fix: per § 9.8 — staging mirrors production. Every prod change has a parallel staging change in the same operator session. Staging FIRST, then prod. Both env's stay in sync at the CI variable layer.

---

## End of standards

CI/CD pipelines are the machinery between intent (a commit on master) and production state. Every defect in this machinery is a production defect by proxy. The patterns above feel like overhead in week one and feel like sanity when production smoke fails at 11 PM and auto-rollback restores service while you're still reading the alert.

When a new pipeline pattern emerges from a debugging session, **add it here** with a cross-reference to the lesson in `archive/LESSONS.md`. When a rule above stops paying its weight, surface it for review — but never delete a rule without an explicit reason captured in `archive/LESSONS.md`.

The discipline scales: 30 minutes designing the auto-rollback flow prevents 4 hours of "production is broken and we don't know how to revert" panic. Slow down to architect well.
