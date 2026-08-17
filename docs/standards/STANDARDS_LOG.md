<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-08-17 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!-- TEMPLATE — the delivery skill copies this to docs/STANDARDS_LOG.md and removes the example entry. -->
<!--
CHANGE LOG
v1.1 — 2026-08-17 — Standard Set Version v2.0 (PLAN-009): template banner + instantiation note
retargeted SETUP.md → the delivery skill (the skill copies this template and removes the example
entry).
v1.0 — 2026-06-13 — Initial release. Experiences-log template (the per-project contribution channel
fed by SESSION_CLOSER § 1.7). Schema + status legend + one worked example. Added under Standard Set
Version v1.1.
-->

# STANDARDS_LOG.md — Experiences log (the contribution channel)

**What this is:** a committed, append-only log of governance experiences from *this* project — the
outbox that feeds improvements back to the canonical standards suite. The wrap-up routine
(`SESSION_CLOSER.md` § 1.7) scans each session for lesson candidates; confirmed candidates are appended
here as `open` entries. The vault later **harvests** the `open` entries, **integrates** the portable
ones (genericize → new `L0NN` lesson → topical update → Set-Version bump), and **writes the status
back** into this file. See `docs/architecture.md` §§ 5–6 for the full loop.

This file is a **kept** file — it survives the setup strip and lives in the project permanently at
`docs/STANDARDS_LOG.md`.

---

## Status legend

| Status | Meaning |
|---|---|
| `open` | Candidate captured; not yet harvested/integrated by the vault. |
| `integrated` | Adopted into the vault — annotate with the assigned `L0NN` + topical location + Set Version. |
| `rejected` | Reviewed and not adopted — annotate why (e.g. project-specific, not portable). |

---

## Entry schema

Each entry is a level-2 heading `## E0NN — <short title>` followed by these fields:

```
## E0NN — <short imperative title of the takeaway>
- Date:        YYYY-MM-DD
- Area:        <engineering | cicd | validation | project | prompt | memory | governance>   # routes to the topical file
- Status:      open                                  # open | integrated | rejected
- Context:     <what happened — the incident or observation>
- Learned:     <the takeaway, stated generally>
- Suggested:   <where it should land — e.g. ENGINEERING_STANDARDS sub-section + a lesson>
- Portability: <project-specific | general>          # a hint for the curator
```

**Ids** are local to this project (`E001`, `E002`, …) and assigned in order; the vault maps each
adopted `E0NN` to its own canonical `L0NN` during integration. **Write-back** on integration replaces
the `Status:` line, e.g.:

```
- Status:      integrated → vault L050 (ENGINEERING_STANDARDS § 1.10, Set Version v1.1)
```

or, when not adopted:

```
- Status:      rejected — project-specific, not portable
```

---

## Entries

> Newest at the bottom (append-only). The example below is illustrative — remove it in a real project
> (the delivery skill does this automatically when it instantiates the project's copy).

## E001 — Surface plan defects before implementing, don't silently fill from prior context
- Date:        2026-06-13
- Area:        governance
- Status:      open
- Context:     During a Phase-3 implementation, the implementing agent found that the approved plan's
               strip list and the file-move step contradicted each other, and that no Set-Version bump
               was scheduled despite an architecture invariant requiring one.
- Learned:     A hardened plan can still ship cross-section contradictions; the implementer must read
               the real source and reconcile against it before writing, surfacing defects to the
               operator rather than executing a flawed spec verbatim.
- Suggested:   Reinforce § 15.3 (implementer surfaces plan defects) — possibly a LESSONS entry on
               "Rule 13 hardening is necessary but not sufficient; Phase-3 read-back is the backstop."
- Portability: general
