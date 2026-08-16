<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-08-16 -->
<!-- Source: docs/standards/STANDARDS_LOG.md (template) v1.0. Project-local instance for Standard DocSet. -->
<!--
CHANGE LOG
v1.0 — 2026-08-16 — Project instantiation from the v1.0 template. Created retroactively: the suite's
self-adoption (PLAN-002 era) skipped this step; the gap sat in OPEN_TASKS since 2026-06-20. Example
entry removed per the template's instantiation note. Note: because this repo IS the vault, portable
lessons codify directly into archive/LESSONS.md + docs/standards/LESSONS.md (e.g. L052–L056 at Set
v1.4) rather than round-tripping through harvest/integrate; this log still captures session
experiences per SESSION_CLOSER § 1.7 so the project exercises the same channel as any adopter.
-->

# STANDARDS_LOG.md — Experiences log (the contribution channel)

**What this is:** a committed, append-only log of governance experiences from *this* project — the
outbox that feeds improvements back to the canonical standards suite. The wrap-up routine
(`docs/SESSION_CLOSER.md` § 1.7) scans each session for lesson candidates; confirmed candidates are
appended here as `open` entries. The vault later **harvests** the `open` entries, **integrates** the
portable ones (genericize → new `L0NN` lesson → topical update → Set-Version bump), and **writes the
status back** into this file. See `docs/architecture.md` §§ 5–6 for the full loop.

**Self-adoption note:** this project is also the vault, so in practice its portable lessons codify
directly into `archive/LESSONS.md` + `docs/standards/LESSONS.md` without the harvest/integrate
round-trip. This log exists so the project exercises the same contribution channel as any adopter
(and so `harvest` has a real in-repo target to read).

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

> Newest at the bottom (append-only).

_(no entries yet — the first entry will be E001)_
