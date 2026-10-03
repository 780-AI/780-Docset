<!-- VERSION: 2.44 -->
<!-- Last Updated: 2026-10-03 -->
<!--
CHANGE LOG
v2.44 — 2026-10-03 — Registered PLAN-013 (engine write safety: clock floor + accumulating handoffs)
DRAFT + tracker: new rows 84–85 (0.1). Design commit only; Phase 3 runs after "APPROVE PLAN-013".
Self-row 2.43 → 2.44 (grep-verified against the header per L063).
v2.43 — 2026-10-03 — PLAN-011 Phase 2 approval recorded ("plan 011 is appvoved"): rows 82–83 → 0.2
(DRAFT → APPROVED). Phase 3 runs in a fresh session per § 15.3. Self-row 2.42 → 2.43
(grep-verified against the header per L063).
v2.42 — 2026-10-03 — Standard Set Version v2.6 (clock trust — 780-VPN E001 → L079): bumped cells 10
(SET_VERSION_ADOPTED 1.13→1.14, v2.6 backport row), 13 (PROJECT_STANDARDS 1.0→1.1, § 5.6), 22 (standards
README 1.3→1.4, count 79), 23 (STANDARDS_INDEX 2.5→2.6). Rows 12 + 30 (LESSONS template + adopter
copy) unchanged per the no-per-lesson-bump practice (L079 added to both). Self-row 2.41 → 2.42
(grep-verified against the header per L063).
v2.41 — 2026-10-03 — Registered PLAN-011 (fleet convergence: Equinex intake + adoption, EverOn
line retirement) DRAFT + tracker: new rows 82–83 (0.1). Design commit only; Phase 3 runs after
"APPROVE PLAN-011". Self-row 2.40 → 2.41 (grep-verified against the header per L063).
v2.40 — 2026-10-03 — PLAN-012 QA-H5 ✅ (loop closure observed in 780-VPN `de1de37`): bumped cell
81 (PLAN-012 tracker 1.1→1.2, post-close QA annotation). Self-row 2.39 → 2.40 (grep-verified
against the header per L063).
v2.39 — 2026-10-03 — 780-VPN re-pointed ssh → local `~/` (shared Dropbox folder): bumped cell 8
(project SESSION_OPENER 1.15→1.16, § 2 target row). config/projects.toml carries no VERSION
header (not manifest-tracked, per the standing note). Last-updated block rotated — it had drifted
since 2026-08-19 (v2.27–v2.38 skipped the rotation; disclosed, not back-filled). Self-row 2.38 →
2.39 (grep-verified against the header per L063).
v2.38 — 2026-09-05 — v2.5 catch-up bookkeeping: 780-Automation returned — catch-up write
converged it to v2.5 (fleet current on all three targets); QA-H3 flipped complete in the v2.5
CHANGELOG entry; PLAN-012 tracker 1.0→1.1 (row 81, post-close QA annotation + Phase 5 record).
Self-row 2.37 → 2.38 (grep-verified against the header per L063).
v2.37 — 2026-09-05 — PLAN-012 Phase 3 implemented (Standard Set Version v2.5 — sync handoff):
bumped cells 7 (architecture 0.11→0.12, § 7 handoff paragraph), 10 (SET_VERSION_ADOPTED
1.12→1.13, v2.5 backport row), 12 (LESSONS template 1.1→1.2, L069–L078 date-line corrections),
20 (template SESSION_OPENER 1.7→1.8, § 1.1 engine-handoff check), 23 (STANDARDS_INDEX 2.4→2.5),
46 (cli 0.5→0.6, both write paths leave the handoff), 51 (test_cli 0.5→0.6, handoff coverage),
72 (sync 0.1→0.2, HANDOFF_REL + render_handoff); promoted PLAN-012 + tracker (80–81) 0.3/APPROVED
→ 1.0/CLOSED. docs/SYNC_HANDOFF.md is engine-transient in TARGETS — never manifest-listed on
either side by design. Self-row 2.36 → 2.37 (grep-verified against the header per L063).
v2.36 — 2026-09-05 — PLAN-012 Phase 2 approval recorded ("approve plan 012"): rows 80–81 → 0.3
(DRAFT → APPROVED). Phase 3 runs in a fresh session per § 15.3. Self-row 2.35 → 2.36
(grep-verified against the header per L063).
v2.35 — 2026-09-05 — PLAN-012 hardened to v0.2 (operator-directed re-review): rows 80–81 →
0.2 — scope extended to the integrate write-back path (the full-codebase sweep's finding) +
manifest-exemption step + QA-H6. Self-row 2.34 → 2.35 (grep-verified against the header per
L063).
v2.34 — 2026-09-05 — Registered PLAN-012 (sync handoff report — every engine write leaves an
explanation in the target; operator directive after the 780-VPN unknown-changes incident) DRAFT +
tracker: new rows 80–81 (0.1). Design commit only; the Phase-3 implement commit lands separately
after "APPROVE PLAN-012". Self-row 2.33 → 2.34 (grep-verified against the header per L063).
v2.33 — 2026-09-05 — Clock-skew record correction: bumped cell 8 (project SESSION_OPENER
1.14→1.15 — § 2 row corrected: the VAULT machine was ~9 days slow, the team Macs were accurate;
verified vs gitlab.com + apple.com). Entries above dated 2026-08-27 were written under the slow
clock (real date 2026-09-05). Self-row 2.32 → 2.33 (grep-verified against the header per L063).
v2.32 — 2026-08-27 — Bookkeeping + deferred-minor sweep: QA-P4 flipped ✅ in the v2.4 CHANGELOG
entry (full-fleet write verified); stale header Source refs fixed in both session instances —
bumped cells 8 (project SESSION_OPENER 1.13→1.14, ref v1.4→v1.7) + 9 (project SESSION_CLOSER
1.5→1.6, ref v1.3→v1.7). Self-row 2.31 → 2.32 (grep-verified against the header per L063).
v2.31 — 2026-08-27 — Standard Set Version v2.4 (environment portability): bumped cells 10
(SET_VERSION_ADOPTED 1.11→1.12, v2.4 backport row), 11 (template CLAUDE.md 1.5→1.6, Rule 2
Runner note + Rule 5/§ 8.6 neutralization), 23 (STANDARDS_INDEX 2.3→2.4). Self-row 2.30 → 2.31
(grep-verified against the header per L063).
v2.30 — 2026-08-27 — Standard Set Version v2.3 (first adopter-originated lesson intake): bumped
cells 10 (SET_VERSION_ADOPTED 1.10→1.11, v2.3 backport row), 12 (LESSONS template 1.0→1.1 —
ownership banner + L069–L078; first header bump since baseline, banner is structural not
per-lesson), 21 (SESSION_CLOSER template 1.6→1.7, § 1.7 binding E0NN rule), 22 (standards README
1.2→1.3, count 68→78), 23 (STANDARDS_INDEX 2.2→2.3). Row 30 (adopter-copy archive) unchanged per
the no-per-lesson-bump practice. Self-row 2.29 → 2.30 (grep-verified against the header per
L063).
v2.29 — 2026-08-27 — Rule 16 codification (operator intake gate): bumped cells 1 (root CLAUDE.md
1.7→1.8, new Rule 16 + heading/bullet counts 15→16) + 8 (project SESSION_OPENER 1.12→1.13, § 3.2
row 1). archive/LESSONS.md L069 added (archive excluded from the manifest per Rule 8; no
per-lesson header bump per standing practice). Self-row 2.28 → 2.29 (grep-verified against the
header per L063).
v2.28 — 2026-08-27 — 780-Automation DHCP IP change: bumped entry 8 (project SESSION_OPENER)
1.11→1.12 (§ 2 registry row re-pointed 172.16.10.61 → 172.16.11.60). config/projects.toml carries
no VERSION header (not manifest-tracked, per the standing note). Self-row 2.27 → 2.28
(grep-verified against the header per L063).
v2.27 — 2026-08-27 — Third target registration (780-VPN, ssh transport): bumped entry 8 (project
SESSION_OPENER) 1.10→1.11 (§ 2 registry row added). config/projects.toml carries no VERSION
header (not manifest-tracked, per the standing note). Self-row 2.26 → 2.27 (grep-verified against
the header per L063).
v2.26 — 2026-08-19 — W-D1 fix-forward (skill mode specs): bumped cells 77 (bootstrap mode 0.1→0.2)
+ 78 (adopt mode 0.1→0.2) — the sync-ready SVA shape in both gains the CHANGE LOG comment block
the engine's record-update hard-requires. Self-row 2.25 → 2.26 (grep-verified against the header
per L063).
v2.25 — 2026-08-19 — Standard Set Version v2.2 (domain-neutral scrub): bumped cells 15
(PROJECT_INSTRUCTIONS_TEMPLATE 1.0→1.1) + 16 (MEMORY_PROTOCOL 1.0→1.1) (residual `/Users/parsaazad/...`
example paths → `/Users/you/...`), 23 (STANDARDS_INDEX 2.1→2.2), 10 (SET_VERSION_ADOPTED 1.9→1.10,
v2.2 backport row). Self-row 2.24 → 2.25 (grep-verified against the header per L063).
v2.24 — 2026-08-19 — Second target registration (780-Automation, ssh transport): bumped entry 8
(project SESSION_OPENER) 1.9→1.10 (§ 2 registry row added). config/projects.toml carries no
VERSION header (not manifest-tracked, per the standing note). Self-row 2.23 → 2.24 (grep-verified
against the header per L063).
v2.23 — 2026-08-18 — Standard Set Version v2.1 (E001 via the first harvest → integrate cycle):
bumped cells 10 (SET_VERSION_ADOPTED 1.8→1.9, v2.1 backport row), 21 (template SESSION_CLOSER
1.5→1.6, § 1.2 reference fix), 22 (standards README 1.1→1.2, stale lesson count 48→68 swept),
23 (STANDARDS_INDEX 2.0→2.1). LESSONS rows unchanged per the no-per-lesson-bump practice
(archive excluded from the manifest per Rule 8). Self-row 2.22 → 2.23 (grep-verified against the
header per L063).
v2.22 — 2026-08-18 — Capital-Signal Dropbox-move re-registration: bumped entry 8 (project
SESSION_OPENER) 1.8→1.9 (§ 2 target row → ~-based Dropbox path, machine-affinity resolved).
config/projects.toml itself carries no VERSION header (not manifest-tracked, per the standing
note). Self-row 2.21 → 2.22 (grep-verified against the header per L063).
v2.21 — 2026-08-17 — PLAN-009 closure (D-5 stage 2): promoted PLAN-009 + tracker (74–75) to
1.0/CLOSED (QA-E pilot adoption + QA-F registration/sync-no-op/harvest all passed same day).
Self-row 2.20 → 2.21 (grep-verified against the header per L063).
v2.20 — 2026-08-17 — First target registration (PLAN-009 QA-F): bumped entry 8 (project
SESSION_OPENER) 1.7→1.8 (§ 2 registry filled — Dropbox vault path, canonical source, the
Capital-Signal target row). config/projects.toml carries no VERSION header (not manifest-tracked,
per the standing note). Self-row 2.19 → 2.20 (grep-verified against the header per L063).
v2.19 — 2026-08-17 — PLAN-009 (skill delivery, Standard Set Version v2.0) implemented: registered
skill/SKILL.md + skill/modes/bootstrap.md + skill/modes/adopt.md + scripts/bootstrap_skill.sh as
entries 76–79 (all 0.1; new Delivery quick-index row 76–79); DELETED the rows for the three retired
files (24 NEW_PROJECT_BOOTSTRAP, 26 SETUP, 57 MEMORY_DURABILITY_ROLLOUT_PROMPT — row removal, no
renumbering of surviving entries; suite range → 11–23, 25, 27); bumped touched cells —
6 folder_structure 0.13→0.14, 7 architecture 0.10→0.11, 10 SVA 1.7→1.8, 20 template OPENER 1.6→1.7,
21 template CLOSER 1.4→1.5, 22 standards README 1.0→1.1, 23 STANDARDS_INDEX 1.6→2.0, 25 HOW_TO_USE
1.0→1.1, 27 STANDARDS_LOG template 1.0→1.1, 58 NEW_MACHINE_SETUP 1.1→1.2, 74 PLAN-009 0.2→0.3
(EXECUTING), 75 tracker 0.1→0.2; quick-index suite caption Set v1.6 → v2.0; self-row 2.18 → 2.19
(grep-verified against the header per L063).
v2.18 — 2026-08-16 — Registered PLAN-009 (skill-based delivery, Set v2.0; APPROVED D9.A same session)
+ its sibling tracker as entries 74–75 (plan 0.2, tracker 0.1; appended, not inserted); quick-index
Plans range → 31–39, 59–60, 63–64, 68–71, 74–75; self-row 2.17 → 2.18 (grep-verified against the
header per L063). Design session only; the Phase-3 implement commit lands the 21-file § 7.2 ALLOWLIST
(skill/ + bootstrap_skill.sh + 3 retirements + Set v2.0).
v2.17 — 2026-08-16 — PLAN-008 (Slice 5: sync, Standard Set Version v1.6) implemented: registered
sync.py + test_sync.py as entries 72–73 (v0.1; appended — Engine quick-index range → 40–55, 61–62,
65–66, 72–73); bumped touched cells — engine (40 __init__ 0.4→0.5, 44 setversion 0.1→0.2, 46 cli
0.4→0.5 + description "+ sync", 65 transport 0.1→0.2), tests (47 conftest 0.1→0.2, 48 test_setversion
0.1→0.2, 51 test_cli 0.4→0.5, 66 test_transport 0.1→0.2), docs (6 folder_structure 0.12→0.13,
7 architecture 0.9→0.10, 8 SESSION_OPENER 1.6→1.7, 9 SESSION_CLOSER 1.4→1.5, 10 SVA 1.6→1.7,
11 template CLAUDE.md 1.4→1.5, 20 template OPENER 1.5→1.6, 21 template CLOSER 1.3→1.4,
23 STANDARDS_INDEX 1.5→1.6, 24 NPB 1.5→1.6, 26 SETUP 1.5→1.6); promoted PLAN-008 + tracker (70–71)
to 1.0/CLOSED; quick-index suite caption Set v1.5 → v1.6; self-row 2.16 → 2.17 (grep-verified against
the header per L063).
v2.16 — 2026-08-16 — Registered PLAN-008 (Slice 5: sync, Set v1.6; APPROVED D8.A same session) + its sibling tracker as
entries 70–71 (v0.1; appended, not inserted); quick-index Plans range → 31–39, 59–60, 63–64, 68–71;
self-row 2.15 → 2.16 (grep-verified against the header per L063). Design session only; the Phase-3
implement commit lands the 25-file § 7 ALLOWLIST.
v2.15 — 2026-08-16 — PLAN-010 (Standard Set Version v1.5) implemented: entry 56 swapped
bootstrap_memory.sh → claude_project_data.sh (0.1; Rule 8 delete + register, slot reused to avoid a
renumber); bumped touched cells (1 root CLAUDE.md → 1.7, 6 folder_structure → 0.12, 8 SESSION_OPENER
→ 1.6, 9 SESSION_CLOSER → 1.4, 10 SVA → 1.6, 11 template CLAUDE.md → 1.4, 20 template OPENER → 1.5,
21 template CLOSER → 1.3, 23 STANDARDS_INDEX → 1.5, 24 NPB → 1.5, 26 SETUP → 1.5, 57 rollout prompt
→ 1.2, 58 NEW_MACHINE_SETUP → 1.1); LESSONS cells (12, 30) unchanged per the no-per-lesson-bump
practice; promoted PLAN-010 + tracker (68–69) to 1.0/CLOSED; quick-index caption Set v1.4 → v1.5;
self-row caught up 2.13 → 2.15 (v2.14's log claimed the bump but the cell never moved — the L063
class, fixed here).
v2.14 — 2026-08-16 — Registered PLAN-010 (upstream intake: EverOn v2.x → vault, Set v1.5) DRAFT +
its sibling tracker as entries 68–69 (v0.1; appended, not inserted); quick-index Plans range →
31–39, 59–60, 63–64, 68–69; self-row 2.13→2.14. **Fix-forward for v2.13 (`2c7833d`, pushed):** the
entry-67 table row (`docs/STANDARDS_LOG.md`) was never actually added — v2.13's CHANGE LOG and
quick-index referenced it but the row was missing (the L063 stamp-vs-log class, caught during the
PLAN-010 Rule 13 pass); row registered now. Design session only; the Phase-3 implement commit lands
the 21-file § 7 ALLOWLIST.
v2.13 — 2026-08-16 — Registered docs/STANDARDS_LOG.md (this project's own experiences-log instance,
created retroactively — the self-adoption had skipped the instantiation step) as entry 67 (v1.0;
appended, not inserted, to avoid a renumber); quick-index "Operating contract + project docs" range →
1–10, 58, 67; bumped entry 6 (folder_structure.md) cell 0.9→0.11 (cell was stale — the v2.11 commit
bumped the file to 0.10 but not this cell; filesystem-verified) and self-row 2.12→2.13. Doc-only.
v2.12 — 2026-08-16 — Standard Set Version v1.4 (process-hardening batch: lessons L052–L056 + L051
recurrence #4): bumped touched cells — entry 1 (root CLAUDE.md) 1.5→1.6, entry 8 (project SESSION_OPENER)
1.4→1.5, entry 9 (project SESSION_CLOSER) 1.2→1.3, entry 10 (SET_VERSION_ADOPTED) 1.4→1.5, entry 11
(template CLAUDE.md) 1.2→1.3, entry 20 (template SESSION_OPENER) 1.3→1.4, entry 21 (template
SESSION_CLOSER) 1.1→1.2, entry 23 (STANDARDS_INDEX) 1.3→1.4, entry 24 (NEW_PROJECT_BOOTSTRAP) 1.3→1.4,
entry 26 (SETUP) 1.3→1.4. LESSONS rows (12 template, 30 adopter) left at 1.0 per the established
no-per-lesson-bump practice. Also caught up two stale cells: self-row (entry 5) 2.10→2.12 (was never
bumped at v2.11) and the quick-index caption "Set v1.2" → "Set v1.4". Doc-only; no engine change.
v2.11 — 2026-06-23 — PLAN-007 (remote-target transport) implemented: registered transport.py + test_transport.py as entries 65–66 (v0.1; Engine quick-index range → 40–55, 61–62, 65–66); bumped touched cells — entry 1 (root CLAUDE.md) 1.4→1.5, entry 7 (architecture.md) 0.8→0.9, entry 40 (__init__) 0.3→0.4, entry 43 (registry) 0.1→0.2, entry 45 (report) 0.1→0.2, entry 46 (cli) 0.3→0.4, entry 49 (test_registry) 0.1→0.2, entry 50 (test_report) 0.1→0.2, entry 51 (test_cli) 0.3→0.4; promoted PLAN-007 + tracker (63–64) 0.1/DRAFT → 1.0/CLOSED. Engine behavior added; read-only on the vault → no Set Version change.
v2.10 — 2026-06-21 — Installer fix (bootstrap gap from first real adoption): bumped entry 26 (SETUP.md)
1.2→1.3 and entry 24 (NEW_PROJECT_BOOTSTRAP.md) 1.2→1.3 — both now SEED `docs/Plans/OPEN_TASKS.md` at
bootstrap (it was gitignored but never created). Installer-only; OPEN_TASKS is gitignored/local so it is
not itself a tracked entry. No Set-Version bump (v1.3 suite CONTENT unchanged).
v2.9 — 2026-06-21 — Drift fix: bumped entry 7 (architecture.md) 0.6→0.8 (roadmap slice→plan numbering
corrected: sync = PLAN-008, PLAN-007 = remote transport). Also corrected two pre-existing stale version
cells the v2.2 CHANGE LOG already claimed but never edited in the table: entry 5 (this manifest, self-row)
2.1→2.9 and entry 6 (folder_structure.md) 0.8→0.9. Filesystem-verified (Rule 2). Doc-only; the version
column is not governance-validated, which is how the cells drifted. No Set-Version bump.
v2.8 — 2026-06-20 — Bumped entry 57 (MEMORY_DURABILITY_ROLLOUT_PROMPT.md) 1.0→1.1 — reconciled its step-5
wording with the settled Rule 14 practice (gitignore `.claude/`) + added `.gitignore` to its ALLOWLIST.
Wording fix only; no Set-Version bump, STANDARDS_INDEX untouched.
v2.7 — 2026-06-20 — Bumped entry 24 (NEW_PROJECT_BOOTSTRAP.md) 1.1→1.2 — the long-form walkthrough caught
up to full Standard Set Version v1.3 parity with SETUP.md (added session-file instantiation + experiences
log + Step 8 durable memory + Step 10.5 strip; v1.1→v1.3; counts 9→14 rules / 10→11 binding). Installer/
walkthrough only; v1.3 suite content unchanged → no Set-Version bump, STANDARDS_INDEX untouched.
v2.6 — 2026-06-20 — Bumped entry 26 (SETUP.md) 1.1→1.2 — the bootstrap installer caught up to Standard
Set Version v1.3 (v1.3 refs + Step 6.5 durable memory + rollout-prompt registered in lay-down/strip,
fixing the strip set-cover). Installer-only; the v1.3 suite content is unchanged → no Set-Version bump,
STANDARDS_INDEX untouched (it bumps only at Set-Version releases).
v2.5 — 2026-06-20 — Registered PLAN-007 (remote transport) DRAFT + its sibling tracker as entries 63–64
(v0.1); quick-index Plans range → "31–39, 59–60, 63–64" (appended, not inserted, to avoid an Engine
renumber). Design session only; the Phase-3 implement commit lands transport.py + tests (→ 2.6).
v2.4 — 2026-06-20 — Standard Set Version v1.3 (lesson L051 — Rule 13 senior-review pass must mechanically
run the linter/type-checker/tests): bumped touched cells — entry 8 (project SESSION_OPENER) 1.3→1.4,
entry 10 (SET_VERSION_ADOPTED) 1.3→1.4, entry 20 (template SESSION_OPENER) 1.2→1.3, entry 23
(STANDARDS_INDEX) 1.2→1.3. LESSONS rows (12 template, 30 adopter) left at 1.0 per the established
no-per-lesson-bump practice. No new tracked files.
v2.3 — 2026-06-20 — Root CLAUDE.md § 4 cleanup: bumped entry 1 (Operating Contract) 1.3→1.4 (dropped the
stale "created when the engine lands" note; promoted config/projects.toml to a Critical File). Doc-only,
project-specific — no new tracked files, no Set Version change.
v2.2 — 2026-06-18 — PLAN-006 (Slice 4: integrate) implemented: registered integrate.py + test_integrate.py
as entries 61–62 (v0.1; Engine range 38–55 → +61, Engine-test +62); bumped touched cells (__init__ 40, cli 46,
test_cli 51) 0.2→0.3 and the cli description (+ integrate); promoted PLAN-006 + its tracker (59–60) 0.1/DRAFT
→ 1.0/CLOSED. architecture 0.6→0.7, folder_structure 0.8→0.9 synced same-commit. No Set Version change.
v2.1 — 2026-06-18 — Registered PLAN-006 (Slice 4: integrate) DRAFT + its sibling tracker as entries 59–60
(v0.1); quick-index Plans range → "31–39, 59–60" (appended, not inserted, to avoid an Engine renumber).
Design session only; the Phase-3 implement commit lands integrate.py + tests (→ 2.2).
v2.0 — 2026-06-17 — PLAN-005 implemented (Standard Set Version v1.2 — durable memory): promoted PLAN-005 +
tracker (38–39) 0.1/DRAFT → 1.0/CLOSED; bumped touched cells — root CLAUDE.md 1.2→1.3, template CLAUDE.md
1.1→1.2, project SESSION_OPENER 1.2→1.3, template SESSION_OPENER 1.1→1.2, STANDARDS_INDEX 1.1→1.2;
registered the three new tracked files (`scripts/bootstrap_memory.sh`, `MEMORY_DURABILITY_ROLLOUT_PROMPT.md`,
`docs/NEW_MACHINE_SETUP.md`) as entries 56–58 — appended rather than inserted-in-category to avoid a
full-table renumber (quick-index ranges extended: 1–10,58 / 11–27,57 / 28–29,56). archive/LESSONS.md +
L050 (archive excluded from manifest per Rule 8; LESSONS header unchanged per the established no-per-lesson-bump practice).
v1.9 — 2026-06-17 — Registered PLAN-005 (durable memory — Rule 14 + Set v1.2) DRAFT + its sibling tracker
as entries 38–39 (v0.1). Quick-index Plans range 31–37 → 31–39; Engine range 38–53 → 40–55 (shifted by the
two inserted plan rows). Design session only; the Phase-3 implement commit lands the suite edits (→ 2.0).
v1.8 — 2026-06-16 — PLAN-004 (Slice 3: harvest) implemented: registered the two new engine modules +
two test modules as entries 50–53 (v0.1) — Engine quick-index range 38–49 → 38–53; bumped the touched
code cells (__init__ row 38, cli row 44, test_cli row 49) 0.1→0.2; promoted PLAN-004 + its tracker
(rows 36–37) 0.1/DRAFT → 1.0/CLOSED in the same commit the slice ships. architecture 0.4→0.5,
folder_structure 0.6→0.7 synced same-commit. No Set Version change (no docs/standards/ file touched).
v1.7 — 2026-06-16 — Registered PLAN-004 (Slice 3: harvest) DRAFT + its sibling tracker as entries
36–37 (v0.1). Quick-index Plans range 31–35 → 31–37; Engine range 36–47 → 38–49 (shifted by the two
inserted plan rows). Design session only; engine code lands in the Phase-3 commit (→ 1.8).
v1.6 — 2026-06-16 — PLAN-003 (Slice 2) implemented: registered the first engine code as entries 36–47
(7 src modules + 5 test modules, all v0.1) under a new Engine quick-index range; promoted PLAN-003 +
its tracker (rows 34–35) from 0.1/DRAFT → 1.0/CLOSED in the same commit the slice ships. `config/projects.toml`
+ `pyproject.toml` carry no VERSION header → not manifest-tracked (documented in folder_structure.md).
v1.5 — 2026-06-16 — Registered PLAN-003 (Slice 2: registry + status/drift) DRAFT + its sibling tracker
as entries 34–35 (v0.1). Quick-index Plans range 31–33 → 31–35. Design session only; no engine code yet.
v1.4 — 2026-06-14 — Project rename: display name → "Standard DocSet" across root CLAUDE.md (1.2), session files (1.2), SET_VERSION_ADOPTED (1.2), architecture (0.3), folder_structure (0.5); version cells updated. Engine package `standard_document_updater` unchanged (Option B). GitLab project/remote → slug `standard-docset`.
v1.3 — 2026-06-13 — PLAN-002 (Slice 1): added docs/standards/STANDARDS_LOG.md (experiences-log template);
moved SET_VERSION_ADOPTED.md docs/standards/ → docs/ (path + category updated); bumped the marker/SETUP
edits to v1.1 (root CLAUDE.md, docs SESSION_OPENER/CLOSER + their templates, SETUP, NEW_PROJECT_BOOTSTRAP,
STANDARDS_INDEX, SET_VERSION_ADOPTED) and architecture.md to 0.2 / folder_structure.md to 0.4; promoted
PLAN-002 to 1.0 (CLOSED). Renumbered the table and corrected the module quick-index ranges + the manifest
self-version cell (was stale at 1.0). Standard Set Version v1.1.
v1.2 — 2026-06-13 — Registered PLAN-002 (Slice 1) as entry 32.
v1.1 — 2026-06-13 — Registered docs/architecture.md (system-design record) as entry 31.
v1.0 — 2026-06-07 — PLAN-001: domain-neutral v1.0 baseline. All standards-suite version cells reset to
1.0; added canonical templates docs/standards/CLAUDE.md + LESSONS.md + SETUP.md. Bumped from v0.1.
v0.1 — 2026-06-07 — Project bootstrap. Initial manifest scaffold.
-->
# Document & Code Manifest

Lists every committed `.md` file and every tracked code file (`.py`/`.sh` with a VERSION header), per
`CLAUDE.md` Rule 8. Updated in the **same commit** that creates, renames, or deletes a tracked file.

## Module quick index

| Module / Section | Entry range |
|---|---|
| Operating contract + project docs | 1–10, 58, 67 |
| Canonical standards suite (Set v2.0) | 11–23, 25, 27 |
| Governance scripts | 28–29, 56 |
| Archive | 30 |
| Plans | 31–39, 59–60, 63–64, 68–71, 74–75 |
| Engine (src + tests) | 40–55, 61–62, 65–66, 72–73 |
| Delivery skill (vault-side) | 76–79 |

## Manifest table

| # | Title | Version | Category | Path |
|---|---|---|---|---|
| 1 | Operating Contract (binding) | 1.8 | Governance | `CLAUDE.md` |
| 2 | Project README | - | Docs | `README.md` |
| 3 | CHANGELOG | - | Docs | `CHANGELOG.md` |
| 4 | Docs Index | - | Docs | `docs/README.md` |
| 5 | Documents Manifest | 2.44 | Governance | `docs/documents_manifest.md` |
| 6 | Folder Structure | 0.14 | Governance | `docs/folder_structure.md` |
| 7 | Architecture (system-design record) | 0.12 | Docs | `docs/architecture.md` |
| 8 | Session Opener (project-local, binding) | 1.16 | Governance | `docs/SESSION_OPENER.md` |
| 9 | Session Closer (project-local, binding) | 1.6 | Governance | `docs/SESSION_CLOSER.md` |
| 10 | Set Version Adopted | 1.14 | Governance | `docs/SET_VERSION_ADOPTED.md` |
| 11 | CLAUDE.md (template) | 1.6 | Standards | `docs/standards/CLAUDE.md` |
| 12 | Lessons Archive (template) | 1.2 | Standards | `docs/standards/LESSONS.md` |
| 13 | Project Standards | 1.1 | Standards | `docs/standards/PROJECT_STANDARDS.md` |
| 14 | Prompt Standards | 1.0 | Standards | `docs/standards/PROMPT_STANDARDS.md` |
| 15 | Project Instructions Template | 1.1 | Standards | `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` |
| 16 | Memory Protocol | 1.1 | Standards | `docs/standards/MEMORY_PROTOCOL.md` |
| 17 | Engineering Standards | 1.0 | Standards | `docs/standards/ENGINEERING_STANDARDS.md` |
| 18 | Validation Standards | 1.0 | Standards | `docs/standards/VALIDATION_STANDARDS.md` |
| 19 | CI/CD Standards | 1.0 | Standards | `docs/standards/CICD_STANDARDS.md` |
| 20 | Session Opener (template) | 1.8 | Standards | `docs/standards/SESSION_OPENER.md` |
| 21 | Session Closer (template) | 1.7 | Standards | `docs/standards/SESSION_CLOSER.md` |
| 22 | Standards README (meta) | 1.4 | Standards | `docs/standards/README.md` |
| 23 | Standards Index (meta) | 2.6 | Standards | `docs/standards/STANDARDS_INDEX.md` |
| 25 | How To Use (meta) | 1.1 | Standards | `docs/standards/HOW_TO_USE.md` |
| 27 | Standards Log — experiences-log template (meta) | 1.1 | Standards | `docs/standards/STANDARDS_LOG.md` |
| 28 | Doc Coverage Check | 0.1 | Governance script | `scripts/check_doc_coverage.py` |
| 29 | Test Coverage Drift Check | 0.1 | Governance script | `scripts/check_test_coverage_drift.py` |
| 30 | Lessons Archive (adopter copy) | 1.0 | Governance | `archive/LESSONS.md` |
| 31 | PLAN-001 — domain-neutral suite (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-001_domain_neutral_suite.md` |
| 32 | PLAN-001 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-001_tracker.md` |
| 33 | PLAN-002 — Slice 1 (setup-strip + log + markers) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-002_setup_strip_log_markers.md` |
| 34 | PLAN-003 — Slice 2 (registry + status/drift) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-003_registry_status_drift.md` |
| 35 | PLAN-003 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-003_tracker.md` |
| 36 | PLAN-004 — Slice 3 (harvest) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-004_harvest.md` |
| 37 | PLAN-004 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-004_tracker.md` |
| 38 | PLAN-005 — durable memory (Rule 14 + Set v1.2) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-005_durable_memory.md` |
| 39 | PLAN-005 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-005_tracker.md` |
| 40 | Engine — package marker + CLI version | 0.5 | Engine | `src/standard_document_updater/__init__.py` |
| 41 | Engine — module entry point | 0.1 | Engine | `src/standard_document_updater/__main__.py` |
| 42 | Engine — exception hierarchy | 0.1 | Engine | `src/standard_document_updater/errors.py` |
| 43 | Engine — registry loader | 0.2 | Engine | `src/standard_document_updater/registry.py` |
| 44 | Engine — Set-Version / open-log parsers | 0.2 | Engine | `src/standard_document_updater/setversion.py` |
| 45 | Engine — comparison report | 0.2 | Engine | `src/standard_document_updater/report.py` |
| 46 | Engine — CLI (status / drift / harvest / integrate / sync) | 0.6 | Engine | `src/standard_document_updater/cli.py` |
| 47 | Engine test — shared fixtures | 0.2 | Engine test | `tests/conftest.py` |
| 48 | Engine test — setversion | 0.2 | Engine test | `tests/test_setversion.py` |
| 49 | Engine test — registry | 0.2 | Engine test | `tests/test_registry.py` |
| 50 | Engine test — report | 0.2 | Engine test | `tests/test_report.py` |
| 51 | Engine test — cli | 0.6 | Engine test | `tests/test_cli.py` |
| 52 | Engine — experiences-log entry parser | 0.1 | Engine | `src/standard_document_updater/logentry.py` |
| 53 | Engine — harvest report (open-entry consolidation) | 0.1 | Engine | `src/standard_document_updater/harvest.py` |
| 54 | Engine test — logentry | 0.1 | Engine test | `tests/test_logentry.py` |
| 55 | Engine test — harvest | 0.1 | Engine test | `tests/test_harvest.py` |
| 56 | Project-data locality script | 0.1 | Governance script | `scripts/claude_project_data.sh` |
| 58 | New-Machine Setup (re-home checklist + Rule 14 migration catalog) | 1.2 | Docs | `docs/NEW_MACHINE_SETUP.md` |
| 59 | PLAN-006 — Slice 4 (integrate) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-006_integrate.md` |
| 60 | PLAN-006 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-006_tracker.md` |
| 61 | Engine — integration worksheet + status write-back | 0.1 | Engine | `src/standard_document_updater/integrate.py` |
| 62 | Engine test — integrate | 0.1 | Engine test | `tests/test_integrate.py` |
| 63 | PLAN-007 — remote transport (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-007_remote_transport.md` |
| 64 | PLAN-007 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-007_tracker.md` |
| 65 | Engine — pluggable target transports (local \| git \| ssh) | 0.2 | Engine | `src/standard_document_updater/transport.py` |
| 66 | Engine test — transport | 0.2 | Engine test | `tests/test_transport.py` |
| 67 | Standards Log — project experiences log | 1.0 | Governance | `docs/STANDARDS_LOG.md` |
| 68 | PLAN-010 — upstream intake: EverOn v2.x → vault (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-010_everon_upstream_intake.md` |
| 69 | PLAN-010 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-010_tracker.md` |
| 70 | PLAN-008 — Slice 5: sync (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-008_sync.md` |
| 71 | PLAN-008 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-008_tracker.md` |
| 72 | Engine — section-aware suite propagation (sync) | 0.2 | Engine | `src/standard_document_updater/sync.py` |
| 73 | Engine test — sync | 0.1 | Engine test | `tests/test_sync.py` |
| 74 | PLAN-009 — skill-based delivery (Set v2.0) (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-009_skill_delivery.md` |
| 75 | PLAN-009 tracker (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-009_tracker.md` |
| 76 | Delivery skill — mode dispatch + step-0 vault resolve | 0.1 | Delivery | `skill/SKILL.md` |
| 77 | Delivery skill — bootstrap mode | 0.2 | Delivery | `skill/modes/bootstrap.md` |
| 78 | Delivery skill — adopt mode | 0.2 | Delivery | `skill/modes/adopt.md` |
| 79 | Delivery-skill installer (per-machine symlink) | 0.1 | Delivery | `scripts/bootstrap_skill.sh` |
| 80 | PLAN-012 — sync handoff report (CLOSED) | 1.0 | Plan | `docs/Plans/PLAN-012_sync_handoff.md` |
| 81 | PLAN-012 tracker (CLOSED) | 1.2 | Plan | `docs/Plans/PLAN-012_tracker.md` |
| 82 | PLAN-011 — fleet convergence: Equinex intake + adoption (APPROVED) | 0.2 | Plan | `docs/Plans/PLAN-011_fleet_convergence.md` |
| 83 | PLAN-011 tracker (APPROVED) | 0.2 | Plan | `docs/Plans/PLAN-011_tracker.md` |
| 84 | PLAN-013 — engine write safety: clock floor + accumulating handoffs (DRAFT) | 0.1 | Plan | `docs/Plans/PLAN-013_engine_write_safety.md` |
| 85 | PLAN-013 tracker (DRAFT) | 0.1 | Plan | `docs/Plans/PLAN-013_tracker.md` |

> `.toml` config (`scripts/doc_coverage_allowlist.toml`, `scripts/validation_ownership.toml`) and
> non-versioned config (`.gitlab-ci.yml`, `.gitignore`, MR template) carry no VERSION header and are not
> manifest-tracked per Rule 8; they are documented in `docs/folder_structure.md`.

## Last updated

- **Date**: 2026-10-03
- **Change**: PLAN-013 DRAFT registered — plan + tracker (84–85, 0.1).
- **Previous change**: PLAN-011 Phase 2 APPROVED — plan + tracker (82–83) → 0.2.
- **Previous audit**: (none — first audit will be quarterly per `PROJECT_STANDARDS.md` § 2.9)
