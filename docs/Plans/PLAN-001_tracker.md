<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Status: DRAFT -->
<!--
CHANGE LOG
v0.1 — 2026-06-07 — Sibling tracker for PLAN-001 created at Phase-1 (big plan: Phase 3 lands as >1 commit). Single-agent project — Owner header omitted (optional per CLAUDE.md § 14 stub).
-->

# PLAN-001 tracker — Domain-neutral canonical suite + SETUP prompt

Granular sub-task status for PLAN-001. Updated **same-commit** as the work it tracks. Status markers:
⏸ pending · 🔄 in-progress · ✅ done · ❌ blocked. Promoted to v1.0 / CLOSED with the plan.

## Phase 0 — Audit
- ✅ 2026-06-07 — grep'd suite for project/domain refs (~340 hits); contexts sampled.

## Phase 1 — Design
- ✅ 2026-06-07 — PLAN-001 drafted (§§ 1–12).
- ✅ 2026-06-07 — sibling tracker created (this file).
- ✅ 2026-06-07 — Rule 13 senior-review-and-optimize pass run; fixes applied.

## Phase 2 — Operator approval
- ✅ 2026-06-07 — operator approved PLAN-001; D-A = keep § 14 in the template.

## Phase 3 — Implement (grouped commits; ALLOWLIST per PLAN § 7)

**Commit 3.1 — Scrub focused standards (8 files)**
- ⏸ CICD_STANDARDS.md · ENGINEERING_STANDARDS.md · MEMORY_PROTOCOL.md · PROJECT_INSTRUCTIONS_TEMPLATE.md · PROJECT_STANDARDS.md · PROMPT_STANDARDS.md · VALIDATION_STANDARDS.md · SESSION_OPENER.md(template) · SESSION_CLOSER.md(template)

**Commit 3.2 — Scrub meta files + reset Set Version**
- ⏸ STANDARDS_INDEX.md (§1/§3/§6 reset to v1.0) · README.md(standards) · NEW_PROJECT_BOOTSTRAP.md

**Commit 3.3 — Add canonical templates**
- ⏸ docs/standards/CLAUDE.md (clean template, §14 per D-A) · docs/standards/LESSONS.md (scrubbed L001–L049)

**Commit 3.4 — One-shot setup**
- ⏸ docs/standards/SETUP.md (paste-and-run prompt) · HOW_TO_USE.md slimmed to pointer

**Commit 3.5 — Reconcile adopter files to v1.0**
- ⏸ archive/LESSONS.md (= scrubbed canonical) · root CLAUDE.md (Source/v1.0) · SET_VERSION_ADOPTED.md · docs/SESSION_OPENER.md · docs/SESSION_CLOSER.md · docs/documents_manifest.md · docs/folder_structure.md · README.md(root) · CHANGELOG.md · PLAN-001 + tracker → v1.0/CLOSED

## Phase 4 — Validate
- ⏸ § 8.1 zero-hit grep · ⏸ § 8.2 version-cell drift · ⏸ governance exit 0 · ⏸ py_compile · ⏸ § 8.5 SETUP dry-run

## Phase 5 — Operator gate
- ⏸ push (only if/when a remote is configured) · ⏸ tag (optional)

## QA scenarios (Rule 11)
- ⏸ S1 — `grep` scrub check returns zero hits (the dispositive domain-neutral test).
- ⏸ S2 — SETUP.md dry-run: every referenced source path exists in the canonical suite.
