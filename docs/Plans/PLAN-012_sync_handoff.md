<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Status: CLOSED (Phase 3 shipped 2026-09-05 as Standard Set Version v2.5; QA-H1..H4 verified; H5/H6 close later per their defined triggers; Phase 5 push + tag at the operator gate) -->
<!--
CHANGE LOG
v1.1 — 2026-10-03 — Closed-risk annotation (§ 15.4, PLAN-013 Phase 3): § 11 clock-caveat risk CLOSED (newest-stamp floor shipped); stale-handoff row notes the next write now appends.
v1.0 — 2026-09-05 — Phase 3 implemented in a fresh session (single commit, 12-file ALLOWLIST):
reconcile pass clean (no plan defects); § 5a–5h applied byte-for-byte; § 6 spec map walked
(architecture § 7 paragraph, INDEX v2.5, SVA v2.5 row, manifest, CHANGELOG). QA-H1 ✅ (ruff
clean, mypy delta zero src 25↔25 + full 42↔42, pytest 111). QA-H2 ✅ + QA-H3 ✅ + QA-H4 ✅ on the
two reachable targets (CS + 780-VPN — exact 3-item delta, handoff delivered + content verified,
re-run up-to-date 11/11); 780-Automation host DOWN at QA time (warn+skip as designed — catch-up
write when it returns). Promoted to 1.0/CLOSED per § 15.5.
v0.3 — 2026-09-05 — Phase 2 operator approval recorded ("approve plan 012"). Status DRAFT → APPROVED. No content change.
v0.2 — 2026-09-05 — Operator-directed re-review ("double check the plan… consistency check with
the whole code base"): full-codebase write-path sweep found the gap — `integrate --write`
write-back ALSO writes into targets (STANDARDS_LOG status flips) with no explanation left.
Design generalized: EVERY engine write leaves the handoff (render_handoff gains `operation` +
`(rel, mode)` files; integrate flush hook added). Handoff § 2 gains the manifest-exemption step
(protects git-transport targets' Rule 8 / doc-coverage gates from the engine-committed handoff).
E001's trusted-clock suggestion explicitly routed to its own intake (§ 3). Overlay re-proven:
ruff clean, mypy delta zero (25↔25), pytest 111 passed (sync + integrate handoff tests). Rule 13
pass re-run + re-recorded.
v0.1 — 2026-09-05 — Initial draft (Phase 0 audit + Phase 1 design). Code developed + tool-proven
in a scratch overlay FIRST (proven-code-first pattern): ruff lint clean, mypy error-delta zero
vs baseline (25 pre-existing both sides), pytest 111 passed (+1 new). Rule 13 pass recorded
below same-day.
-->

# PLAN-012 — Sync handoff report: every engine write leaves an explanation in the target

## 1. Goal

**Every engine write into a target** — `sync --write` AND the `integrate --write` write-back —
leaves **`docs/SYNC_HANDOFF.md`** in that target: what the engine wrote, by which operation and
vault Standard Set Version, and the exact residual bookkeeping the target's next session must do
(review diffs, manifest cells, CHANGELOG entry, one landing commit that also deletes the
handoff). The SESSION_OPENER **template** gains a § 1.1 handoff check so any session opening an
adopter reads the handoff FIRST instead of facing unexplained modified files. Ships as **Standard
Set Version v2.5**, which also carries the canonical LESSONS date-line corrections from the
2026-09-05 clock-skew finding.

**Origin (operator directive, 2026-09-05):** a 780-VPN session opened to four engine-written
uncommitted files it did not make and had to reverse-engineer their provenance. Operator: *"after
any change there should be a hands-off report so claude code in other projects will not face
unknown changes to the files."* This is the L044 principle applied to the engine-write boundary:
the forcing function (the handoff file) fires at exactly the granularity of the failure (every
engine write into a repo someone else will open). The v0.2 re-review confirmed "any change" must
mean BOTH engine write paths — the write-back would otherwise reproduce the same incident on a
smaller scale (an unexplained modified STANDARDS_LOG).

## 2. Operator constraints

- The handoff must appear on **every** engine write, every operation, every transport (local /
  ssh / git) — no opt-out.
- No other behavior change; dry-run and worksheet paths untouched.
- The target-side ritual stays lightweight: read → land → delete (done = deleted).

## 3. Scope summary

- **Engine (`sync.py`):** `HANDOFF_REL` + `render_handoff(project, operation, set_version,
  today, files)` (pure text; files as `(rel, mode)` tuples so both call sites fit).
- **Engine (`cli.py`):** `_cmd_sync` writes the handoff after `apply_actions` and appends it to
  the flushed set; `_cmd_integrate`'s write branch writes it per flushed target and includes it
  in the flush list. Console notes updated.
- **Tests:** sync end-to-end handoff test (content + converged-target idempotence) + handoff
  assertions added to the existing integrate write-back test.
- **Template (Set v2.5):** SESSION_OPENER § 1.1 engine-handoff check.
- **Riding the same release:** canonical LESSONS date-line corrections (L069–L078 stamped
  2026-08-27 by the then-slow vault clock; real date 2026-09-05).
- **Out of scope (explicitly routed elsewhere):** the trusted-clock engine change suggested by
  780-VPN's **E001** (derive "today" from a trusted source / newest-stamp floor + refuse when
  behind) — that arrives via its own harvest → Rule 16 gate → integrate cycle and, being
  behavior-affecting, its own plan. The handoff's run-date line carries a clock-trust caveat in
  the meantime. Also out: making the handoff a SYNC_MAP item (it must not be — idempotence).

## 4. Phase tracker (high-level — granular sub-tasks in PLAN-012_tracker.md)

- Phase 0 — Audit: ✅ 2026-09-05 (extended by the v0.2 full-write-path sweep)
- Phase 1 — Design + Rule 13 pass: ✅ 2026-09-05 (v0.1); re-run ✅ 2026-09-05 (v0.2)
- Phase 2 — Operator approval: ✅ 2026-09-05 — "approve plan 012" (on the v0.2 draft)
- Phase 3 — Implement (fresh session, single commit): ✅ 2026-09-05
- Phase 4 — Validate (QA-H1..H6): 🔄 H1–H4 ✅ 2026-09-05 (H3 on the 2 reachable targets;
  780-Automation down — catch-up pending); H5 (target loop closure) + H6 (E001 intake) close at
  their defined later triggers
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
# v0.2 — 2026-09-05 — PLAN-012: HANDOFF_REL + render_handoff — EVERY engine write into a target
#         (sync --write AND integrate write-back) leaves a handoff report so the target's next
#         session finds engine-landed changes explained.
```

### 5b. `src/standard_document_updater/sync.py` — append at end of file (after `render_plan`)

```python


HANDOFF_REL = Path("docs/SYNC_HANDOFF.md")


def render_handoff(
    project_name: str, operation: str, set_version: str, today: str, files: list[tuple[str, str]]
) -> str:
    """The handoff report every engine write leaves in the target (PLAN-012).

    Written on every write — `sync --write` and the integrate write-back — so
    the target's NEXT session finds engine-landed changes explained: what was
    written, by which operation and vault release, and the residual bookkeeping
    the engine deliberately leaves to the target (manifest cells, CHANGELOG
    entry, the landing commit). The target session deletes the file in the
    commit that lands the changes; the next engine write recreates it.
    """
    lines = [
        "# SYNC HANDOFF — engine-written changes landed in this repository",
        "",
        "> **READ ME FIRST.** The Standard DocSet engine wrote the files below directly",
        "> into this working tree. They are NOT unexplained local edits. Land them per § 2,",
        "> then DELETE this file in that same commit.",
        "",
        "## 1. What the engine did",
        "",
        f"- **Project:** {project_name}",
        f"- **Operation:** {operation}",
        f"- **Vault Standard Set Version:** {set_version}",
        f"- **Run date:** {today} (stamped by the curator machine's clock — if stamp ordering",
        "  looks wrong against local history, trust an external time authority)",
        "- **Files written (suite-owned sections updated; PROJECT-OWNED blocks preserved):**",
    ]
    for rel, mode in files:
        lines.append(f"  - `{rel}` ({mode})")
    lines += [
        "",
        "## 2. What this project's next session must do (the engine does NOT do these)",
        "",
        "1. Review the diffs (`git diff`) against the file list above.",
        "2. Reconcile `docs/documents_manifest.md` version cells for the files above (skip any",
        "   whose header version did not move).",
        "3. Add a CHANGELOG entry recording the engine write (operation + file list).",
        "4. Commit the engine-written files + bookkeeping together — and **delete this handoff",
        "   file in that commit** (done = deleted).",
        "5. Do NOT add this file to the project's manifest — it is engine-transient (Rule 8",
        "   exempt by design); it must never survive a landing commit.",
        "6. New lessons/observations still land ONLY as `E0NN` entries in",
        "   `docs/STANDARDS_LOG.md` — never in engine-owned files.",
        "",
        "*Engine-generated on every engine write; the next write rewrites it.*",
        "",
    ]
    return "\n".join(lines)
```

### 5c. `src/standard_document_updater/cli.py` — the sync write hook

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
                        sync.render_handoff(
                            project.name,
                            "sync --write",
                            set_version,
                            today,
                            [(a.target_rel, a.mode) for a in changed],
                        ),
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

### 5d. `src/standard_document_updater/cli.py` — the integrate write-back hook

FIND:

```text
        report_lines = integrate.apply_writeback(dispositions, log_path_for, write=args.write)
        if args.write:
            count = len(dispositions)
            message = f"Standard DocSet: integrate write-back ({count} status update(s))"
            for name in sorted(named & set(targets)):
                targets[name].flush(roots[name], [Path("docs/STANDARDS_LOG.md")], message)
```

REPLACE:

```text
        report_lines = integrate.apply_writeback(dispositions, log_path_for, write=args.write)
        if args.write:
            set_version = "v" + ".".join(str(n) for n in setversion.parse_vault_version(index))
            today = date.today().isoformat()
            count = len(dispositions)
            message = f"Standard DocSet: integrate write-back ({count} status update(s))"
            for name in sorted(named & set(targets)):
                (roots[name] / sync.HANDOFF_REL).write_text(
                    sync.render_handoff(
                        name,
                        "integrate write-back",
                        set_version,
                        today,
                        [("docs/STANDARDS_LOG.md", "write-back")],
                    ),
                    encoding="utf-8",
                )
                targets[name].flush(
                    roots[name], [Path("docs/STANDARDS_LOG.md"), sync.HANDOFF_REL], message
                )
```

Plus `cli.py` header: `# VERSION: 0.5` → `# VERSION: 0.6` and a CHANGE LOG line above the v0.5
line:

```text
# v0.6 — 2026-09-05 — PLAN-012: every engine write leaves docs/SYNC_HANDOFF.md in the target —
#                     `sync --write` (per written target, listing the changed files) AND the
#                     integrate write-back (per flushed target); write-notes updated.
```

### 5e. `tests/test_cli.py` — new sync test inserted immediately BEFORE `def test_sync_unknown_project_filter_errors(`

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
    assert "- **Operation:** sync --write" in handoff
    assert "- **Vault Standard Set Version:** v1.5" in handoff
    assert "`CLAUDE.md` (merge)" in handoff
    assert "delete this handoff" in handoff
    # the handoff is not a SYNC_MAP item: a converged target stays up-to-date
    assert main(["--vault", str(vault), "sync"]) == 0
    assert "up-to-date" in capsys.readouterr().out


```

### 5f. `tests/test_cli.py` — integrate write-back handoff assertions

FIND:

```text
    assert main(["--vault", str(root), "integrate", "--apply", str(decisions), "--write"]) == 0
    assert "wrote" in capsys.readouterr().out
    assert "rejected — n/a" in log.read_text(encoding="utf-8")
```

REPLACE:

```text
    assert main(["--vault", str(root), "integrate", "--apply", str(decisions), "--write"]) == 0
    assert "wrote" in capsys.readouterr().out
    assert "rejected — n/a" in log.read_text(encoding="utf-8")
    handoff = (proj / "docs" / "SYNC_HANDOFF.md").read_text(encoding="utf-8")
    assert "- **Operation:** integrate write-back" in handoff
    assert "`docs/STANDARDS_LOG.md` (write-back)" in handoff
```

Plus `tests/test_cli.py` header `# VERSION: 0.5` → `# VERSION: 0.6` and log line:

```text
# v0.6 — 2026-09-05 — PLAN-012: handoff coverage — `sync --write` leaves docs/SYNC_HANDOFF.md
#         (content + not-a-SYNC_MAP-item idempotence) and the integrate write-back leaves it too.
```

### 5g. `docs/standards/SESSION_OPENER.md` (template, 1.7 → 1.8) — § 1.1 handoff check

FIND (the L055 paragraph, ends § 1.1):

```text
If a local register (`OPEN_TASKS.md`) or a tracker records a push-state ("unpushed" / "push held"), reconcile it against the **real** remote (`git ls-remote origin <main-branch>`) — not the local remote-tracking cache — before trusting it (per `LESSONS.md` L055). Committed trackers stay frozen at their commit; only the live register is reconciled.
```

REPLACE (same paragraph + the new check):

```text
If a local register (`OPEN_TASKS.md`) or a tracker records a push-state ("unpushed" / "push held"), reconcile it against the **real** remote (`git ls-remote origin <main-branch>`) — not the local remote-tracking cache — before trusting it (per `LESSONS.md` L055). Committed trackers stay frozen at their commit; only the live register is reconciled.

**Engine-handoff check:** if `docs/SYNC_HANDOFF.md` exists — or `git status` shows modified suite files this project's sessions did not change — the Standard DocSet engine landed changes here. Read the handoff FIRST and land it per its § 2 steps (review diffs → manifest cells → CHANGELOG entry → one commit that also deletes the handoff) BEFORE any other work. Engine-written changes are explained changes, never unknown edits.
```

Header 1.7 → 1.8, Last Updated 2026-09-05, CHANGE LOG line naming PLAN-012.

### 5h. `docs/standards/LESSONS.md` (1.1 → 1.2) — date-line corrections

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
  (engine-owned transient `docs/SYNC_HANDOFF.md`, written by BOTH engine write paths, not a
  SYNC_MAP item, never manifest-listed, target deletes on landing) — the § 4 drift rule demands
  this ride the engine change.
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
  (sync handoff test + integrate write-back handoff assertions included). Proven in the overlay
  2026-09-05 (v0.1 and re-proven at v0.2); re-run at Phase 3.
- **QA-H2** — pre-release oracle: fleet `sync` dry-run shows exactly the v2.5 delta per target
  (SESSION_OPENER merge + LESSONS replace + SVA record = 3 items) and nothing else.
- **QA-H3** — feature-ON, sync half (Rule 15): the v2.5 `sync --write` itself delivers the
  handoff — spot `docs/SYNC_HANDOFF.md` on all three targets, content shows the operation, v2.5,
  and the 3 files.
- **QA-H4** — idempotence: immediate dry-run re-run = up-to-date 11/11 everywhere (handoff
  presence does not perturb the plan).
- **QA-H5** — loop closure (operator-observed, target-side): the next session in any target
  reads the handoff, lands the changes per its § 2, and deletes it. First observation closes.
- **QA-H6** — feature-ON, write-back half (Rule 15): the next real `integrate --write` — the
  named trigger is the pending intake of 780-VPN's **E001** (already open in its log) — leaves
  the write-back handoff in that target; spot-grep on that run. Not silently deferred: the
  trigger is scheduled work, and the engine-level behavior is already test-covered (QA-H1).

## 9. Operator approval decision point

No code is touched until the operator replies **"APPROVE PLAN-012"** (or names changes).

## 10. Rollback path

Single revert of the Phase 3 commit restores engine + templates. Handoff files already delivered
to targets are inert text — delete manually; no persistent state, no schema.

## 11. Known risks + mitigations

- **Git-transport flush commits the handoff into target history** — and a committed, unlisted
  `.md` could trip the target's Rule 8 / doc-coverage gate on its next CI run. Mitigated three
  ways: the handoff's § 2 step 5 declares it manifest-exempt by design; the architecture § 7
  paragraph codifies the exemption; and no git-transport target exists yet — revisit the
  commit-vs-MR-body question at DD-6b before the first git `--write`.
- **Target session ignores the handoff** → stale file. Mitigated by the § 1.1 opener check (the
  reader is forced at session start) and by the next engine write rewriting it. *(PLAN-013,
  2026-10-03: the next write now APPENDS to an un-landed handoff; the sync dry-run surfaces it.)*
- **Clock caveat**: the run-date line carries the trust note; the real fix (trusted time source /
  newest-stamp floor) is E001's suggestion and arrives via its own gated intake. **CLOSED
  2026-10-03 by PLAN-013** — the engine refuses to stamp behind a target's newest stamp
  (`sync.newest_stamp` / `check_clock`); E001's lesson half shipped as Set v2.6 (L079).
- **Two call sites construct the files list differently** (FileActions vs a literal tuple) —
  accepted: the tuple interface is the narrow waist; both sites are covered by tests.

## 12. Acceptance criteria

1. Every `sync --write` that changes a target writes + flushes `docs/SYNC_HANDOFF.md` with
   project, operation, Set Version, run date, file list, and the six § 2 steps.
2. Every `integrate --write` write-back leaves the same handoff (operation "integrate
   write-back") in each flushed target.
3. Dry-run and worksheet behavior unchanged; converged targets report up-to-date with a handoff
   present.
4. Template SESSION_OPENER carries the § 1.1 engine-handoff check.
5. Canonical LESSONS date lines corrected per § 5h.
6. `ruff check` clean, mypy delta zero, 111 tests green.
7. Set v2.5 released, fleet synced current, handoff observed on all three targets (QA-H3), at
   least one target session closes the loop (QA-H5), and the write-back half fires at the E001
   intake (QA-H6).

---

**Rule 13 senior-review-and-optimize pass — RUN 2026-09-05, RE-RUN same day at v0.2 (recorded
per § 15.8):** the § 5 code was developed and tool-proven in a scratch overlay BEFORE embedding
(proven-code-first): full `src`+`tests` overlay, edits applied, then `ruff check` (clean),
`mypy` (25 errors baseline, 25 overlay — delta zero), `pytest` (111 passed; sync + integrate
handoff coverage) — all at the exact ship indentation. The v0.2 re-review additionally swept
EVERY write-into-target site in the codebase (`grep flush\|write_text` over `cli.py`; the two
sites are `_cmd_sync` and `_cmd_integrate`'s write branch — both now covered; `harvest`/`status`
are read-only; the skill runs in the target's own session) and every `date.today()` site (one:
`cli.py:146`; the integrate hook adds the second deliberately). Cross-section consistency
walked: § 5 blocks ↔ § 7 ALLOWLIST (12 = 12) ↔ § 8 scenarios ↔ § 12 acceptance; § 5c/5d
REPLACE blocks and § 5e/5f test blocks byte-verified against the proven overlay; § 5g/5h FIND
anchors grep-verified unique in live source. Edge cases: zero-changed sync targets write no
handoff (hook inside `if changed`); write-back materializes `docs/` on every transport
(`full=False` still fetches `docs/` — handoff path exists); git-transport committed-handoff →
§ 11 risk with the doc-coverage consequence; handoff-not-in-SYNC_MAP idempotence asserted by
test. No unresolved design decision remains beyond Phase 2 approval itself.
