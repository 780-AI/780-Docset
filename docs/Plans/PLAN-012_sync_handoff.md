<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-09-05 -->
<!-- Status: DRAFT (awaiting Phase 2 operator approval) -->
<!--
CHANGE LOG
v0.1 — 2026-09-05 — Initial draft (Phase 0 audit + Phase 1 design). Code developed + tool-proven
in a scratch overlay FIRST (proven-code-first pattern): ruff lint clean, mypy error-delta zero
vs baseline (25 pre-existing both sides), pytest 111 passed (+1 new). Rule 13 pass recorded
below same-day.
-->

# PLAN-012 — Sync handoff report: every engine write leaves an explanation in the target

## 1. Goal

Every `sync --write` that changes a target leaves **`docs/SYNC_HANDOFF.md`** in that target: what
the engine wrote, at which Standard Set Version, and the exact residual bookkeeping the target's
next session must do (manifest cells, CHANGELOG entry, landing commit, delete-the-handoff). The
SESSION_OPENER **template** gains a § 1.1 handoff check so any session opening an adopter reads
the handoff FIRST instead of facing unexplained modified files. Ships as **Standard Set Version
v2.5**, which also carries the canonical LESSONS date-line corrections from the 2026-09-05
clock-skew finding.

**Origin (operator directive, 2026-09-05):** a 780-VPN session opened to four engine-written
uncommitted files it did not make and had to reverse-engineer their provenance. Operator: *"after
any change there should be a hands-off report so claude code in other projects will not face
unknown changes to the files."* This is the L044 principle applied to the sync boundary: the
forcing function (the handoff file) fires at exactly the granularity of the failure (every engine
write into a repo someone else will open).

## 2. Operator constraints

- The handoff must appear on **every** write, every transport (local / ssh / git) — no opt-out.
- No behavior change to what the engine writes otherwise; dry-run untouched.
- The target-side ritual stays lightweight: read → land → delete (done = deleted).

## 3. Scope summary

- **Engine:** `sync.py` gains `HANDOFF_REL` + `render_handoff(...)` (pure text). `cli.py`
  `_cmd_sync` writes the handoff after `apply_actions` and appends it to the flushed set, so
  every transport carries it in the same flush; console note updated.
- **Tests:** one end-to-end test — write leaves the handoff with correct content; a converged
  target still reports up-to-date (the handoff is not a SYNC_MAP item).
- **Template (Set v2.5):** SESSION_OPENER § 1.1 handoff check.
- **Riding the same release:** canonical LESSONS date-line corrections (L069–L078 stamped
  2026-08-27 by the slow vault clock; real date 2026-09-05).
- **Out of scope:** integrate's STANDARDS_LOG write-back (single-file, self-explanatory —
  recorded as a § 11 risk/candidate); making the handoff a SYNC_MAP item (it must not be —
  idempotence).

## 4. Phase tracker (high-level — granular sub-tasks in PLAN-012_tracker.md)

- Phase 0 — Audit: ✅ 2026-09-05
- Phase 1 — Design (this file) + Rule 13 pass: ✅ 2026-09-05
- Phase 2 — Operator approval: ⏸ awaiting "APPROVE PLAN-012"
- Phase 3 — Implement (fresh session, single commit): ⏸
- Phase 4 — Validate (QA-H1..H5): ⏸
- Phase 5 — Operator gate (push + tag set-v2.5): ⏸

## 5. Verbatim transformation rules (code proven in overlay; Phase 3 copies byte-for-byte)

### 5a. `src/standard_document_updater/sync.py` — header bump

FIND:

```text
# VERSION: 0.1
# Section-aware suite propagation (`sync`): replace | merge | record per file.
#
# CHANGE LOG
```

REPLACE:

```text
# VERSION: 0.2
# Section-aware suite propagation (`sync`): replace | merge | record per file.
#
# CHANGE LOG
# v0.2 — 2026-09-05 — PLAN-012: HANDOFF_REL + render_handoff — every `sync --write` leaves a
#         handoff report in the target so its next session finds engine-landed changes explained.
```

### 5b. `src/standard_document_updater/sync.py` — append at end of file (after `render_plan`)

```python


HANDOFF_REL = Path("docs/SYNC_HANDOFF.md")


def render_handoff(
    project_name: str, set_version: str, today: str, written: list[FileAction]
) -> str:
    """The handoff report `sync --write` leaves in the target (PLAN-012).

    Written on every write so the target's NEXT session finds engine-landed
    changes explained — what was written, by which release, and the residual
    bookkeeping the engine deliberately leaves to the target (manifest cells,
    CHANGELOG entry, the landing commit). The target session deletes the file
    in the commit that lands the sync; the next write recreates it.
    """
    lines = [
        "# SYNC HANDOFF — engine-written changes landed in this repository",
        "",
        "> **READ ME FIRST.** The Standard DocSet sync engine wrote the files below directly",
        "> into this working tree. They are NOT unexplained local edits. Land them per § 2,",
        "> then DELETE this file in that same commit.",
        "",
        "## 1. What the engine did",
        "",
        f"- **Project:** {project_name}",
        f"- **Standard Set Version applied:** {set_version}",
        f"- **Run date:** {today} (stamped by the curator machine's clock — if stamp ordering",
        "  looks wrong against local history, trust an external time authority)",
        "- **Files written (suite-owned sections updated; PROJECT-OWNED blocks preserved):**",
    ]
    for action in written:
        lines.append(f"  - `{action.target_rel}` ({action.mode})")
    lines += [
        "",
        "## 2. What this project's next session must do (the engine does NOT do these)",
        "",
        "1. Review the diffs (`git diff`) against the file list above.",
        "2. Reconcile `docs/documents_manifest.md` version cells for the files above.",
        "3. Add a CHANGELOG entry recording the sync (Set Version + file list).",
        "4. Commit the sync files + bookkeeping together — and **delete this handoff file",
        "   in that commit** (done = deleted).",
        "5. New lessons/observations still land ONLY as `E0NN` entries in",
        "   `docs/STANDARDS_LOG.md` — never in engine-owned files.",
        "",
        "*Engine-generated on every `sync --write`; the next sync rewrites it.*",
        "",
    ]
    return "\n".join(lines)
```

### 5c. `src/standard_document_updater/cli.py` — the write hook

FIND:

```text
                if args.write and changed:
                    written = sync.apply_actions(root, changed)
                    message = f"Standard DocSet: sync to Standard Set Version {set_version}"
                    target.flush(root, written, message)
                    print(f"  -> wrote + flushed {len(written)} file(s)")
                    print(
                        "  note: sync does not edit the target's documents_manifest — "
                        "reconcile its cells at that project's next session"
                    )
```

REPLACE:

```text
                if args.write and changed:
                    written = sync.apply_actions(root, changed)
                    (root / sync.HANDOFF_REL).write_text(
                        sync.render_handoff(project.name, set_version, today, changed),
                        encoding="utf-8",
                    )
                    written.append(sync.HANDOFF_REL)
                    message = f"Standard DocSet: sync to Standard Set Version {set_version}"
                    target.flush(root, written, message)
                    print(f"  -> wrote + flushed {len(written)} file(s) (incl. the handoff)")
                    print(
                        "  note: sync does not edit the target's documents_manifest — "
                        "docs/SYNC_HANDOFF.md tells the target's next session what remains"
                    )
```

Plus `cli.py` header: `# VERSION: 0.5` → `# VERSION: 0.6` and a CHANGE LOG line above the v0.5
line:

```text
# v0.6 — 2026-09-05 — PLAN-012: `sync --write` writes + flushes docs/SYNC_HANDOFF.md into each
#                     written target (render_handoff) so the target's next session finds the
#                     changes explained; write-note updated.
```

### 5d. `tests/test_cli.py` — new test inserted immediately BEFORE `def test_sync_unknown_project_filter_errors(`

```python
def test_sync_write_leaves_handoff_and_dry_run_stays_up_to_date(
    make_suite_pair: MakePair, write_registry: Make, capsys: pytest.CaptureFixture[str]
) -> None:
    vault, target = make_suite_pair()
    write_registry(vault, [("acme", target)])
    assert main(["--vault", str(vault), "sync", "--write"]) == 0
    assert "(incl. the handoff)" in capsys.readouterr().out
    handoff = (target / "docs" / "SYNC_HANDOFF.md").read_text(encoding="utf-8")
    assert "SYNC HANDOFF" in handoff
    assert "- **Standard Set Version applied:** v1.5" in handoff
    assert "`CLAUDE.md` (merge)" in handoff
    assert "delete this handoff file" in handoff
    # the handoff is not a SYNC_MAP item: a converged target stays up-to-date
    assert main(["--vault", str(vault), "sync"]) == 0
    assert "up-to-date" in capsys.readouterr().out


```

Plus `tests/test_cli.py` header `# VERSION: 0.5` → `# VERSION: 0.6` and log line:

```text
# v0.6 — 2026-09-05 — PLAN-012: handoff test — `sync --write` leaves docs/SYNC_HANDOFF.md in
#         the target (content + not-a-SYNC_MAP-item idempotence).
```

### 5e. `docs/standards/SESSION_OPENER.md` (template, 1.7 → 1.8) — § 1.1 handoff check

FIND (the L055 paragraph, ends § 1.1):

```text
If a local register (`OPEN_TASKS.md`) or a tracker records a push-state ("unpushed" / "push held"), reconcile it against the **real** remote (`git ls-remote origin <main-branch>`) — not the local remote-tracking cache — before trusting it (per `LESSONS.md` L055). Committed trackers stay frozen at their commit; only the live register is reconciled.
```

REPLACE (same paragraph + the new check):

```text
If a local register (`OPEN_TASKS.md`) or a tracker records a push-state ("unpushed" / "push held"), reconcile it against the **real** remote (`git ls-remote origin <main-branch>`) — not the local remote-tracking cache — before trusting it (per `LESSONS.md` L055). Committed trackers stay frozen at their commit; only the live register is reconciled.

**Engine-handoff check:** if `docs/SYNC_HANDOFF.md` exists — or `git status` shows modified suite files this project's sessions did not change — the Standard DocSet sync engine landed changes here. Read the handoff FIRST and land it per its § 2 steps (review diffs → manifest cells → CHANGELOG entry → one commit that also deletes the handoff) BEFORE any other work. Engine-written changes are explained changes, never unknown edits.
```

Header 1.7 → 1.8, Last Updated 2026-09-05, CHANGE LOG line naming PLAN-012.

### 5f. `docs/standards/LESSONS.md` (1.1 → 1.2) — date-line corrections

- Replace **all 9 occurrences** of:
  `**Date:** 2026-08-27 (vault intake; incident in the source project days earlier)`
  with:
  `**Date:** 2026-09-05 (vault intake — originally stamped 2026-08-27 by the vault machine's slow clock; the source project's own stamps were accurate)`
- Replace the L069 pair (unique two-line anchor):
  `**Date:** 2026-08-27` + newline + `**Project:** an adopter project (team) → vault`
  with:
  `**Date:** 2026-09-05 (originally stamped 2026-08-27 — the vault machine's clock ran ~9 days slow)` + newline + `**Project:** an adopter project (team) → vault`
- Header 1.1 → 1.2, Last Updated 2026-09-05, CHANGE LOG line: date-line corrections, no content
  change.

## 6. Spec update map (same commit as Phase 3)

- `docs/architecture.md` (0.11 → 0.12): § 7 gains a closing paragraph documenting the handoff
  (engine-owned transient `docs/SYNC_HANDOFF.md`, not a SYNC_MAP item, target deletes on
  landing) — the § 4 drift rule demands this ride the engine change.
- `docs/standards/STANDARDS_INDEX.md` → v2.5 (§ 1 block, § 3 cells: SESSION_OPENER 1.8,
  LESSONS 1.2, STANDARDS_INDEX 2.5; § 6 history entry with the sync note).
- `docs/SET_VERSION_ADOPTED.md` → v2.5 row + header bump.
- `docs/documents_manifest.md` → cells for every touched tracked file + self-row.
- `CHANGELOG.md` → v2.5 release entry with the QA scenarios.
- This plan + tracker → v1.0 / CLOSED in the same commit (§ 15.5).

## 7. ALLOWLIST (the bullet enumeration IS the count — 12 files)

- `src/standard_document_updater/sync.py`
- `src/standard_document_updater/cli.py`
- `tests/test_cli.py`
- `docs/standards/SESSION_OPENER.md`
- `docs/standards/LESSONS.md`
- `docs/standards/STANDARDS_INDEX.md`
- `docs/SET_VERSION_ADOPTED.md`
- `docs/architecture.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-012_sync_handoff.md` (promotion to 1.0/CLOSED)
- `docs/Plans/PLAN-012_tracker.md` (promotion to 1.0/CLOSED)

## 8. Validation gate (Rule 11 scenarios — tracker holds status)

- **QA-H1** — suite: `ruff check` clean; mypy error-delta zero vs baseline; `pytest` 111 passed
  (the new end-to-end handoff test included). Proven in the overlay 2026-09-05; re-run at Phase 3.
- **QA-H2** — pre-release oracle: fleet `sync` dry-run shows exactly the v2.5 delta per target
  (SESSION_OPENER merge + LESSONS replace + SVA record = 3 items) and nothing else.
- **QA-H3** — feature-ON (Rule 15): the v2.5 `sync --write` itself delivers the handoff — spot
  `docs/SYNC_HANDOFF.md` on all three targets (ssh grep for 780-Automation/780-VPN; local read
  for CS), content shows v2.5 + the 3 files.
- **QA-H4** — idempotence: immediate dry-run re-run = up-to-date 11/11 everywhere (handoff
  presence does not perturb the plan).
- **QA-H5** — loop closure (operator-observed, target-side): the next session in any target
  reads the handoff, lands the sync per its § 2, and deletes it. First observation closes the
  scenario; recorded in this tracker.

## 9. Operator approval decision point

No code is touched until the operator replies **"APPROVE PLAN-012"** (or names changes).

## 10. Rollback path

Single revert of the Phase 3 commit restores engine + templates. Handoff files already delivered
to targets are inert text — delete manually; no persistent state, no schema.

## 11. Known risks + mitigations

- **Git-transport flush commits the handoff into target history.** Accepted for uniformity (no
  per-transport special case); the target's landing commit deletes it. Revisit at DD-6b if the
  MR flow wants the handoff in the MR body instead.
- **Target session ignores the handoff** → stale file. Mitigated by the § 1.1 opener check (the
  reader is forced at session start) and by the next sync rewriting it.
- **integrate write-back not covered** (out of scope): single-file STANDARDS_LOG status update,
  self-explanatory in the log itself. Candidate follow-up if it ever confuses a session.
- **Clock caveat**: run-date line carries the trust note; the real fix is the vault machine's
  clock (flagged separately).

## 12. Acceptance criteria

1. Every `sync --write` that changes a target writes + flushes `docs/SYNC_HANDOFF.md` with
   project, Set Version, run date, file list, and the five § 2 steps.
2. Dry-run behavior unchanged; converged targets report up-to-date with a handoff present.
3. Template SESSION_OPENER carries the § 1.1 engine-handoff check.
4. Canonical LESSONS date lines corrected per § 5f.
5. `ruff check` clean, mypy delta zero, 111 tests green.
6. Set v2.5 released, fleet synced current, handoff observed on all three targets (QA-H3), and
   at least one target session closes the loop (QA-H5).

---

**Rule 13 senior-review-and-optimize pass — RUN 2026-09-05 (recorded per § 15.8):** the § 5 code
was developed and tool-proven in a scratch overlay BEFORE embedding (proven-code-first): full
`src`+`tests` overlay, edits applied, then `ruff check` (clean), `ruff format --check` (delta
zero vs baseline — 3 pre-existing reformat flags on both sides), `mypy` (25 errors baseline, 25
overlay — delta zero), `pytest` (111 passed, +1 new test) — all at the exact ship indentation.
Cross-section consistency walked: § 5 blocks ↔ § 7 ALLOWLIST (12 = 12) ↔ § 8 scenarios ↔ § 12
acceptance; § 5c count-line change is asserted by the § 5d test; § 5e FIND anchor grep-verified
against the live template; § 5f anchors grep-verified (9 + 1 occurrences). Edge cases considered:
zero-changed targets write no handoff (hook is inside `if changed`); git-transport commit
inclusion (→ § 11 risk); handoff-not-in-SYNC_MAP idempotence (asserted by test). No unresolved
design decision remains beyond Phase 2 approval itself.
