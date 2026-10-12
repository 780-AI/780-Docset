<!-- VERSION: 0.1 -->
<!-- Last Updated: 2026-10-12 -->
<!-- Status: DRAFT — awaiting Phase 2 approval -->
<!--
CHANGE LOG
v0.1 — 2026-10-12 — Initial draft. § 15.9 intake (operator request "start 2.8"; no document) → the v2.8
inventory in chat (every recorded candidate, with source and recommendation; Rule 16 list for the adopter
items) → operator answers DL-004 … DL-009 → Phase 0 audit against the live source (`9366b7a`) → Phase 1
design. Proven text first: § 5 (67 blocks) applied to a scratch export of HEAD → 21 files; domain-neutral
gate 0 hits (planted-name control 1); structure harness 8b CLEAN (control 3 FAILs); engine-as-oracle
harness 8c on copies of the 4 reachable projects → 13 / 13 (HEAD baseline 5 / 5 up-to-date; control
2 FAILs); governance 0 / 0 on the scratch tree. Rule 13 pass on the complete plan + tracker (record at the
foot).
-->

# PLAN-020 — Standard Set Version v2.8: lessons batch, senior-review checklist, template fixes, decision-log template

## 1. Goal

Release **Standard Set Version v2.8** — a documents-only Set Minor (operator Q1 = A, DL-004) — and deliver
it to every reachable project:

1. **Eight new lessons** in the canonical archive: **L082–L088** consolidate about 25 data points the
   curator recorded since 2026-06 into seven lessons; **L089** is an adopter lesson confirmed at the
   Rule 16 gate (DL-005). L080 gains an adopter data point.
2. **The senior-review checklist** in CLAUDE.md § 15.8 (positive controls, tools on the extracted text,
   varied inputs, reachable fixtures, content-checking gates, verified premises).
3. **Template fixes:** the four dangling `PROJECT_INSTRUCTIONS_TEMPLATE.md` references (Q3 = A, DL-006);
   the Rule 12 alias's leftover identifier; the § 1 / § 14 "delete § 14" vs "keep a stub" conflict; the
   Windows junction wording; the leftover-`memory/` opener line (adopter, DL-005); `STANDARDS_INDEX`
   § 4 self-service wording.
4. **Three notes:** PROMPT § 3.12 relayed prompts and guides; ENGINEERING § 2.7 shell safety; PROJECT
   § 8.10 publishing a repository to a wider audience.
5. **The decision log, step 1** (Q5 = A, DL-008): a `DECISION_LOG.md` template in the suite (not yet
   delivered to projects) and the vault's own `docs/DECISION_LOG.md`, seeded with today's nine decisions
   verbatim, bound by a vault `CLAUDE.md` § 10 rule (D-1).
6. **Delivery:** `sync --write` to the four reachable projects (D-4); 780-Automation catches up when its
   host answers.

No engine change. No rule added or renumbered (template 15, vault 16).

## 2. Operator constraints + intake record (binding)

- **Intake (§ 15.9):** operator request in chat ("start 2.8"), no document. The investigation is § 3;
  the candidate inventory was posted in the session-10 chat and answered there.
- **Operator answers (verbatim, `docs/DECISION_LOG.md`):** Q1 "Q1 A, but record the rest for planning and
  getting them done right away" (DL-004); Q2 "Q2. yes" (DL-005 — the Rule 16 gate for A1, A2, A3, A5);
  Q3 "Q3. eplain in simple words" → "Q3 A" (DL-006); Q4 "Q4. yes this is very important we should have
  descision log" (DL-007); Q5 + Q6 "Q5 A, Q6 yes" (DL-008, DL-009).
- **Adopt / deviate per inventory item:**

| Item | Source | Decision | Lands in |
|---|---|---|---|
| A1 verify an environmental premise | 780-estimator PLAN-013 § 14.4 (gate #4) | integrate | L080 data point (5a.4) |
| A2 a TLS handshake is not reachability | 780-estimator CHANGELOG 2026-09-05 (gate #5) | integrate | L089 (5a.3) |
| A3 Rule 13 tested one input size | 780-estimator PLAN-004 v0.3 (gate #8) | integrate | § 15.8 checklist "varied inputs" + L082 |
| A4 ALLOWLIST-count automation | 780-estimator (gate #6) | defer → vault tooling (OPEN_TASKS) | — |
| A5 leftover `memory/` | Capital-Signal E002 Suggested (3) + lesson | integrate | SESSION_OPENER § 1.5 + L087 |
| B1–B7 curator lesson candidates | OPEN_TASKS sessions 3–9 + older | integrate | L082–L088 |
| C1 relayed prompts / guides | OPEN_TASKS session 7 | integrate | PROMPT § 3.12 |
| C2 Rule 13 checklist | OPEN_TASKS (D2 family) | integrate | CLAUDE.md § 15.8 |
| C3 shell safety | OPEN_TASKS sessions 8–9 | integrate | ENGINEERING § 2.7 |
| C4 publishing to a wider audience | OPEN_TASKS 2026-10-05 | integrate | PROJECT § 8.10 |
| C5 QA when a run moves machines | OPEN_TASKS session 8 | **defer** (DL-009) | — |
| C6 agent safety check blocks recovery | OPEN_TASKS session 5 | **reject** — tool-specific (DL-009) | — |
| D1 dangling Project Instructions refs | OPEN_TASKS 2026-10-03 | fix (Q3 = A) | 5b.6, 5e, 5f.3, 5g + skill 5m.3 |
| D2 `Closeout_Mode` in Rule 12 | OPEN_TASKS 2026-10-03 | fix | 5b.3 (+ vault 5o.2) |
| D3 § 14 delete vs stub | PLAN-018 gap 4 (3 data points) | fix | 5b.2, 5b.7 |
| D4 INDEX § 4 self-service | PLAN-018 § 2 | fix | 5j.6 |
| D5 junction wording | OPEN_TASKS (PLAN-017) | fix | 5b.4, 5c.3, 5d.2 (+ vault 5o.3, 5q.3, 5r.2) |
| E1 / E2 locality-tool delivery + do-not-edit header | E002 delivery half, PLAN-017 D-2 | **next plan (PLAN-021)** per DL-004 | — |
| E3 skill / Windows fixes W1–W3, bootstrap gaps 1/2/3/5 | PLAN-018 | **separate change** per DL-004 | — |
| F vault tooling + engine candidates | OPEN_TASKS | **separate changes** per DL-004 | — |
| G dropped | clock skew (= L079), fresh-clone identity (in L081), portability (v2.4), scrub coverage (v2.2), machine-affine paths (in the registry), premise-stamping + commit bundling (single soft points), tool caches (vault-only `NEW_MACHINE_SETUP` note), workflow guard (memory) | not codified | — |

- **Deviations from the inventory, named:** (1) the § 12 note sits *below* the dispatcher table, not
  wrapped around its row — a marker line inside a Markdown table breaks the table; the effect (vault-only
  line) is the operator's Q3 = A. (2) Rule 14 gains a "never handle the link by hand" bullet (L087's
  codification home — part of B6 as confirmed). (3) Two skill lines (5m, 5n) so bootstrap / adopt strip
  `TEMPLATE-ONLY` blocks from CLAUDE.md — surfaced as D-2. (4) The two historical
  `PROJECT_INSTRUCTIONS_TEMPLATE` mentions inside old lessons (L015, line 2155) stay: lessons are
  append-only records of where a rule lived at the time.

## 3. Scope summary

### Phase 0 audit findings (2026-10-12, live source at `9366b7a`)

- **Sync ownership** (`src/standard_document_updater/sync.py:67-87`): `CLAUDE.md`, `SESSION_OPENER.md`,
  `SESSION_CLOSER.md` merge (template body with `TEMPLATE-ONLY` blocks stripped, `:132-141` + `:196`);
  the six topical standards and `LESSONS.md` replace whole. So the § 12 row can be vault-only via a
  `TEMPLATE-ONLY` block, but the three prose references (replace-mode files) must be reworded — exactly
  Q3 = A. The strip removes a block plus one following blank line (`:136-141`): placed below the table,
  the projects' text equals today's minus one row.
- **A new suite file never reaches existing projects** without a `SYNC_MAP` change (engine) — why the
  decision log is two-step (DL-008). The skill's bootstrap copies an explicit file list
  (`skill/modes/bootstrap.md:25`, `:40-58`), so the new template cannot leak into new projects early.
- **Bootstrap / adopt do not strip `TEMPLATE-ONLY` from CLAUDE.md** (`skill/modes/bootstrap.md:40-51`
  strips it only for the opener / closer; `skill/modes/adopt.md:73` says nothing) — and
  `bootstrap.md:49-51` says the project's § 12 "still names" the template file → D-2.
- **Dangling references** (`PROJECT_INSTRUCTIONS_TEMPLATE.md`, never in `SYNC_MAP`): template
  `CLAUDE.md:660`, `MEMORY_PROTOCOL.md:224`, `PROMPT_STANDARDS.md:891`, `CICD_STANDARDS.md:1009`. One
  adopter had removed the § 12 row itself in 2026-06 and sync re-imposed it (their `CLAUDE.md` v1.1 log
  line) — an L068 recurrence.
- **Stamp drift (L063 class), fixed here:** `docs/standards/LESSONS.md` still 1.2 although v2.6 / v2.7
  added L079–L081; the vault's `archive/LESSONS.md` still 1.0 although v2.3 / v2.6 / v2.7 added entries;
  `docs/folder_structure.md` captions "Set Version v2.0" and "L001–L067".
- **Other sites:** template Rule 12 alias `CLAUDE.md:198`; Rule 14 `:250-254`, `:258-259`; § 1 `:31`;
  § 14 `:685`; § 15.8 `:867`; opener template § 1.5 `:86-91`, row 14 `:144`; closer template `:100`;
  vault `CLAUDE.md:193`, `:245-249`, `:253-254`, `:614`, `:706`, `:850`; vault opener `:91-96`, `:145`;
  vault closer `:71`. Insertion points: PROMPT after § 3.11 (`:505-516`), ENGINEERING after § 2.6
  (`:234-246`), PROJECT after § 8.9 (`:784-803`); their TOCs list top-level sections only (no TOC edit).
- **Out of scope, observed:** `docs/standards/README.md` carries older stale counts (line 102 "16
  lessons", line 137 "10 binding files", line 161 "14 files"); `STANDARDS_INDEX` § 4.2 still describes
  manual backports (pre-engine). Neither was in the confirmed inventory — left for a later sweep.

### Pre-tests (2026-10-12, scratch export of `9366b7a`)

| Check | Result |
|---|---|
| § 5 applied (67 blocks: 65 replace + 2 create) | CLEAN — 21 files written; no `<P3-DATE>` left |
| Corrupted-FIND control | exactly the corrupted block FAILs |
| Domain-neutral gate (§ 8 pattern) over `docs/standards/` `skill/` `scripts/claude_project_data.sh` | 0 lines (HEAD baseline 0; planted-name control 1) |
| Structure harness 8b | CLEAN — 89 + 73 TOC links resolve, fences closed in 21 files, 16 INDEX rows == headers, 89 lesson headings; control → 3 FAILs |
| Oracle harness 8c, HEAD vault, `uptodate` | 5 / 5 — the copies are current at v2.7 |
| Oracle harness 8c, draft vault, `delta` | 13 / 13 — each project exactly the 10-item delta; merged CLAUDE.md: PROJECT-OWNED 4 / 4, no `TEMPLATE-ONLY`, no template-file reference, checklist present; re-run up-to-date |
| Oracle control (HEAD vault in `delta` mode) | 2 FAILs |
| Governance on the scratch tree | exit 0 / 0 (note: both scripts are scaffolds — manifest cells are checked by the § 6 script) |

### Files (Phase 3)

Commit 1 (release, § 7.1): 25 files. Commit 2 (delivery record + close, § 7.2): 4 files. Plus one write
per reachable project (their trees, not this repo).

## 4. Phase tracker (high-level — granular sub-tasks in `PLAN-020_tracker.md`)

| Phase | Status | Date |
|---|---|---|
| 0 — Audit (+ § 15.9 intake, inventory, operator answers) | ✅ | 2026-10-12 |
| 1 — Design (+ Rule 13 pass) | ✅ | 2026-10-12 |
| 2 — Operator approval | ⏸ pending | — |
| 3a — Release commit (fresh session) | ⏸ pending | — |
| 3b — Delivery to the reachable projects + record commit | ⏸ pending | — |
| 4 — Validate (QA-V1…V8) | ⏸ pending | — |
| 5 — Operator gate (push both remotes + tag `set-v2.8`) | ⏸ pending | — |

## 5. Verbatim transformation rules (text proven in scratch; Phase 3 copies byte-for-byte)

**How to apply (Phase 3).** Each block carries a machine-readable marker (`<!-- block … -->`):
`kind=replace` (a FIND and a REPLACE body) or `kind=create` (one body = the whole new file; the file must
not exist). Each body is exactly the lines between its two 4-backtick fence lines, plus a final newline —
so every FIND is whole lines. The reconcile pass (§ 15.3) re-extracts every block from THIS file and checks
it against the live tree: each FIND matches exactly once — in order per file, a later FIND against the text
after the earlier REPLACEs. Any mismatch is a named plan defect (D1, D2, …) — stop and surface it. Replace
every `<P3-DATE>` with the Phase 3 date checked against an external time authority (L079). Then the § 6
mechanical rules.

<!-- §5-GENERATED:BEGIN -->

### 5a — `docs/standards/LESSONS.md` — 1.2 → 1.3: lessons L082–L089 + an L080 data point

<!-- block id=5a.1 path=docs/standards/LESSONS.md kind=replace -->

**5a.1** — header 1.2 → 1.3 (also covers the L079–L081 additions that shipped without a bump). FIND:

````text
<!-- VERSION: 1.2 -->
<!-- Last Updated: 2026-09-05 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.3 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.3 — <P3-DATE> — Standard Set Version v2.8: lessons L082–L089 added (L082–L088 the curator's
own lesson candidates, consolidated from about 25 recorded data points; L089 an adopter-originated
lesson confirmed at the intake gate); L080 gains a data-point paragraph (verify an environmental
premise before designing — adopter-originated, confirmed at the intake gate). Stamp catch-up: L079
(v2.6) and L080–L081 (v2.7) were added without a VERSION bump — this 1.3 covers them too (L063
class). Counts 81 → 89.
````

<!-- block id=5a.2 path=docs/standards/LESSONS.md kind=replace -->

**5a.2** — table of contents: eight new entries at the top of § 3's list. FIND:

````text
3. [The lessons (newest first)](#3-the-lessons-newest-first)
 - [L081 — A cloud-synced repository folder needs explicit operating rules; gitignored is not sync-ignored](#l081--a-cloud-synced-repository-folder-needs-explicit-operating-rules-gitignored-is-not-sync-ignored)
````

REPLACE WITH:

````text
3. [The lessons (newest first)](#3-the-lessons-newest-first)
 - [L089 — A connection that opens is not a service that answers: only a real request proves reachability](#l089--a-connection-that-opens-is-not-a-service-that-answers-only-a-real-request-proves-reachability)
 - [L088 — Check before acting or telling: a derived path, a message for someone else, an identity fact](#l088--check-before-acting-or-telling-a-derived-path-a-message-for-someone-else-an-identity-fact)
 - [L087 — A folder shared by several machines: no git command is read-only, links into real data are never handled by hand, same name is not same content](#l087--a-folder-shared-by-several-machines-no-git-command-is-read-only-links-into-real-data-are-never-handled-by-hand-same-name-is-not-same-content)
 - [L086 — Writes into another repository: explanations accumulate, and a landing is proven by the branch, not by a deleted note](#l086--writes-into-another-repository-explanations-accumulate-and-a-landing-is-proven-by-the-branch-not-by-a-deleted-note)
 - [L085 — Engine as oracle: verify a produced artifact with the program that will consume it](#l085--engine-as-oracle-verify-a-produced-artifact-with-the-program-that-will-consume-it)
 - [L084 — A gate is its own step: run it before the action, read its result, and check content rather than a commit id](#l084--a-gate-is-its-own-step-run-it-before-the-action-read-its-result-and-check-content-rather-than-a-commit-id)
 - [L083 — Prove the change first, then generate the plan's blocks from it and re-extract them from the plan](#l083--prove-the-change-first-then-generate-the-plans-blocks-from-it-and-re-extract-them-from-the-plan)
 - [L082 — A proof must be able to fail: show every check, test and gate failing once before trusting its pass](#l082--a-proof-must-be-able-to-fail-show-every-check-test-and-gate-failing-once-before-trusting-its-pass)
 - [L081 — A cloud-synced repository folder needs explicit operating rules; gitignored is not sync-ignored](#l081--a-cloud-synced-repository-folder-needs-explicit-operating-rules-gitignored-is-not-sync-ignored)
````

<!-- block id=5a.3 path=docs/standards/LESSONS.md kind=replace -->

**5a.3** — the eight lessons, newest first, above L081. FIND:

````text
## 3. The lessons (newest first)

### L081 — A cloud-synced repository folder needs explicit operating rules; gitignored is not sync-ignored
````

REPLACE WITH:

````text
## 3. The lessons (newest first)

### L089 — A connection that opens is not a service that answers: only a real request proves reachability

**Date:** 2026-09-05
**Project:** an adopter project (team) → vault
**Phase / Task:** an adopter's cloud-publication plan, blocked by an outbound network filter → its change log → intake gate (confirmed) → Standard Set Version v2.8

#### Incident

A project behind an organization's outbound filter needed a cloud storage API. After the security
team opened one hostname, a TLS probe reported three API hosts "REACHABLE": each completed the
handshake and presented a genuine certificate from the provider's own authority. Two of the three
then dropped every real request ("remote disconnected"). The filter could see only the hostname
announced in the handshake — a host allowlist, not a path filter — so the handshake succeeded while
requests through it were cut. The project spent a month treating the API as blocked, then as open,
before real requests against further hostnames found one that served; a full live run then passed.

#### Diagnosis

A handshake proves that a socket opened and a certificate was presented. It says nothing about
whether the service will process a request on that path: filtering proxies, hostname allowlists,
maintenance pages and half-open load balancers all complete the handshake and then refuse. A probe
that stops at the handshake reports false positives exactly where reachability is in doubt.

#### Codification

Reachability is proven only by a real application-level request. Any response from the service
counts as reached — an authentication error or a not-found is still the service answering; a
disconnect or a timeout after the handshake counts as unreachable. Probes, health checks and QA
scenarios that claim "reachable" make a real request and record the status it returned.

#### Cross-references

- L082 (a check that cannot fail — a handshake probe cannot report the failure that matters)
- L079 (environment facts are untrusted until verified against an authority)

---

### L088 — Check before acting or telling: a derived path, a message for someone else, an identity fact

**Date:** 2026-10-03 → 2026-10-08
**Project:** cross-project (the curator vault and its adopters)
**Phase / Task:** a delivery-skill audit, a message drafted for a project owner, a registry record

#### Incident

Three separate near-misses shared one cause. (1) A delivery script resolved a missing link to an
empty string; `git -C ""` and `cd ""` then ran silently in the current folder — a different
repository from the one intended. (2) A message drafted for a project owner told their agent to
update seven manifest cells (only four existed in that project) and to "fix any other reference" to
an old script — which would have edited a tool copied verbatim from the vault; a check against a
fresh clone of their repository caught both before the message was sent. (3) "This machine belongs
to a team member" was inferred from an account name and recorded as fact; it stayed in the records
for five weeks before the operator said it was their own second machine.

#### Diagnosis

Each value was derived, not observed: a path computed from a link, a list of cells assumed from the
curator's own repository, an owner guessed from an account name. A derived value inherits none of
the certainty of its source, and each was acted on — or nearly sent to someone else — as if it had
been checked.

#### Codification

- **Before running anything in a derived path**, check its identity (`git rev-parse
  --show-toplevel`, an expected marker file) and stop on an empty or unexpected value.
- **Before sending instructions to another person or their agent**, check every concrete claim
  (file names, counts, rows, commands) against their live files.
- **Record identity facts with their source** — who said it and when; an unsourced identity fact
  is a guess and is marked as one.

#### Cross-references

- L032 (investigate the underlying data — the same discipline, applied before acting)
- L059 (verify evidence provenance before recording a result)

---

### L087 — A folder shared by several machines: no git command is read-only, links into real data are never handled by hand, same name is not same content

**Date:** 2026-10-03 → 2026-10-07
**Project:** cross-project (the curator vault and its adopters)
**Phase / Task:** work in cloud-synced repository folders shared by two machines; a project-data store recovery; an adopter's experiences-log entry (confirmed at the intake gate)

#### Incident

(1) `git status` and `git log` were run from one machine while a session on another machine was
active in the same synced repository; `git status` can rewrite `.git/index`. No damage, caught
mid-session. (2) On a project owner's machine, a file-manager move of the per-project harness link
(a directory junction on Windows) emptied the in-repo store it pointed into — and the locality
tool's own message had sent the owner to that folder. (3) Recovering from that, an agent kept the
older of two same-name transcript files because the other looked newer; the "newer" file was a
stub and the "older" one held half a session. (4) An adopter reported that a session started before
`link` leaves an empty `memory/` in the harness directory, and that the locality tool's `link` and
`adopt` aborted on it.

#### Diagnosis

A synced folder makes every write visible to every machine, and git's index is a write. A link into
real data, sitting in a folder a person can browse, looks like an ordinary folder — moving or
deleting it acts on the data behind it. After a move, file names and modification times say nothing
about content.

#### Codification

- **No git command is read-only in a shared synced folder** while another machine's session is
  active there; read the `.git` files directly if a state check is needed.
- **Never move, copy or delete the harness link by hand** (a symlink; a junction on Windows) — use
  the locality tool's verbs.
- **Compare content, not names or dates**, before choosing between two same-name files (first and
  last entries, sizes).
- **A session started before `link` leaves an empty `memory/`** in the harness directory: the
  locality tool absorbs it from 0.2 on; an older copy aborts — remove the empty directory, rerun
  `link` (SESSION_OPENER § 1.5).

#### Cross-references

- L050 (project data lives inside the repo — the link this lesson protects)
- L081 (operating rules for a cloud-synced repository folder — this lesson adds three)

---

### L086 — Writes into another repository: explanations accumulate, and a landing is proven by the branch, not by a deleted note

**Date:** 2026-09-05 → 2026-10-05
**Project:** cross-project (the sync engine and its adopters)
**Phase / Task:** engine writes into adopter working trees; the engine's per-write handoff note

#### Incident

(1) The engine left a handoff note in a target explaining each write, but rewrote the note on every
write; when writes stacked up before the target landed them, the earlier explanations were lost —
the very failure the note existed to prevent. (2) Engine-written files sat uncommitted in one
target across four releases, and in another target a session silently discarded uncommitted
engine writes. (3) A target session deleted the handoff note without committing the files it
described; the fleet view then read "0 pending" while the write was still uncommitted.

#### Diagnosis

Uncommitted writes in someone else's working tree survive only until a session there decides what
they are. A note that the next write overwrites cannot explain several writes, and a note's absence
proves nothing about the files it described.

#### Codification

- **Explanations accumulate**: while a write is un-landed, each further write appends its own
  record; nothing is overwritten.
- **A landing is proven by the target branch moving past the write** (plain reads of `.git` refs
  and logs are safe across machines) — never by the note having been deleted.
- **Keep the exposure window short**: the target's session opener checks for an un-landed note
  first (SESSION_OPENER § 1.1) and lands it before other work.

#### Cross-references

- L069 (engine-owned files invite edits; contributions need a visible channel)
- L082 (a "0 pending" reading that cannot see the failure is not a check)

---

### L085 — Engine as oracle: verify a produced artifact with the program that will consume it

**Date:** 2026-08-17 → 2026-10-05
**Project:** cross-project (the delivery skill, the sync engine and their adopters)
**Phase / Task:** delivery-skill QA; an old adopter's catch-up; replace-mode deltas

#### Incident

(1) The delivery skill produced an adoption-record file that passed review against its own spec but
lacked fields the sync engine requires; it was found only when the engine's own planner was run on
a freshly produced fixture. (2) A documented catch-up path for old adopters named one of the three
preparation steps actually needed; a dry run of the engine against the real repository exposed the
other two. (3) A dry run proposed removing lines from replace-mode files in a target; whether that
was safe depended on whether the target's copy was byte-identical to the vault's tagged release —
one hash comparison settled it.

#### Diagnosis

A spec reviewed against itself agrees with itself; only the consumer knows its hard requirements.
A documented path that has never run on a real target is a hypothesis, and a delta that removes
content is safe only if the content removed is the vault's own.

#### Codification

- **Feature-ON QA for any producer runs the consumer's own parser or planner** on the produced
  output (for example the sync engine's dry-run planner on a fresh bootstrap).
- **A delivery path is supported only after a run** on a real target, or on a faithful copy of one.
- **Before trusting a replace-mode delta that removes content**, prove the target copy equals the
  vault's tag for its adopted version (`git rev-parse <tag>:<path>` against `git hash-object`).

#### Cross-references

- L067 (verification must exercise the new behavior itself)
- L068 (template cross-references must resolve in the adopter)

---

### L084 — A gate is its own step: run it before the action, read its result, and check content rather than a commit id

**Date:** 2026-10-03 → 2026-10-12
**Project:** cross-project (the curator vault and its adopters)
**Phase / Task:** a pre-write idle check; two plan pre-checks

#### Incident

(1) A pre-write idle check and the write it guarded ran in one shell command. The check found a
session transcript on another machine changed minutes earlier — and the write ran anyway, because
the check only printed. No collision, by luck. (2) A plan gate required "HEAD equals the release
commit"; a legitimate bookkeeping commit moved HEAD while every protected file stayed identical, so
the gate would have blocked a correct run. (3) A pre-check copied from a predecessor plan ("HEAD
equals both remotes") would have blocked its successor, whose planning commits were legitimately
still unpushed.

#### Diagnosis

A check printed alongside its action is output, not a gate. A gate keyed to an exact commit id tests
history instead of the content it protects: routine commits trip it, and it says nothing about the
files that matter.

#### Codification

- **Every precondition runs as its own step**, and its result is read before the guarded action
  starts.
- **A gate checks the content it protects** (`git diff --quiet <ref> HEAD -- <paths>`, ancestry via
  `git merge-base --is-ancestor`), not equality with a commit id.
- **When two machines share a folder**, the "is it idle?" question to the operator comes with the
  evidence (recent session-transcript times on the other side).

#### Cross-references

- L082 (a gate is a check — it too must be shown able to stop)
- L081 (one machine at a time in a cloud-synced folder)

---

### L083 — Prove the change first, then generate the plan's blocks from it and re-extract them from the plan

**Date:** 2026-08-16 → 2026-10-12
**Project:** cross-project (the curator vault and its adopters)
**Phase / Task:** ten consecutive plans drafted and implemented this way (up to 85 blocks across 24 files)

#### Incident

Hand-composed find-and-replace blocks kept carrying defects into implementation: anchors written as
inline code with backslash-escaped backticks the source never had; code that read correctly but
failed the linter at its real indentation. From one large plan on, the order was reversed — the
change was made and tool-proven in a scratch copy of the tree first; the plan's blocks were
generated from that proven copy, each with a machine-readable marker; the senior-review pass
re-extracted the blocks from the plan file and re-ran the tools on the extracted text; the
implementing session re-extracted them again with a freshly written parser. Across ten plans the
reconcile pass found zero plan defects, and two independently written extractors produced
byte-identical files.

#### Diagnosis

The tools prove the code, not its copy: hand-copying between a working tree and a plan is where
drift enters. Markdown is a lossy carrier — inline code mangles backticks, and a block that itself
contains fences ends early unless its own fence is longer.

#### Codification

- **Prove first**, in a scratch copy of the tree, with the real tools.
- **Generate the blocks from the proven copy** — each with a marker (`<!-- block id=… path=…
  kind=… -->`); FIND and REPLACE as raw fenced text (4-backtick fences when the content holds
  fences), never inline code.
- **Re-extract from the plan file** and re-run the tools on the extracted text (Rule 13); the
  implementing session re-extracts again and applies byte-for-byte — every FIND matches exactly
  once, in order, and a corrupted-FIND control proves the checker.
- **When a change must touch a file that an approved-but-unimplemented plan anchors**, shift that
  plan's anchors in the same commit and re-prove them.

#### Cross-references

- L049 (the senior-review pass) and L051 (it must run the tools)
- L062 (plan-embedded code must satisfy the plan's own criteria at every site)
- L082 (the corrupted-FIND control is a positive control)

---

### L082 — A proof must be able to fail: show every check, test and gate failing once before trusting its pass

**Date:** 2026-06-22 → 2026-10-12
**Project:** cross-project (the curator vault and its adopters)
**Phase / Task:** a series of green results that proved nothing, across plans, QA scenarios and governance checks

#### Incident

Again and again a "pass" turned out to have checked nothing; each was caught only because a number
or an output looked wrong. A shell `&&` chain broke on a typo, the patch step never ran, and
the tests went green on the unpatched code — one test short of the expected count. A shell glob
error aborted a search, and its exit code read as "no matches". A comparison loop assigned a
variable the shell ties to its command path; every later command vanished and every row compared
empty with empty — "OK". An after-check's `find` was a different implementation that rejected the
date format, and a redirect hid the error — "nothing created". A bench test's extractor matched the
examples in the document it was testing. A QA harness ran a hung probe with output redirected, so
every later failure line vanished. An adopter's test fixture hard-coded one input size; the review
tried only that size and missed that every other size crashed before reaching the guard under test.
A renderer that parses its own output passed one-write tests and truncated content on the third
successive write. And a QA scenario named a fixture state that could never reach the code it
claimed to test.

#### Diagnosis

A check that cannot fail looks exactly like a check that passed. Negative results — no matches,
exit 1, an empty diff, equal values — are the easiest to produce by accident: a broken tool, a
swallowed error, an empty input or a probe that never ran all yield them.

#### Codification

- **Positive control**: before trusting a check, run it once against a known-bad input (the old
  code, a corrupted anchor, a planted hit) and see it fail *by the check*, not by a crash.
- **Never hide a check's errors**; an empty value is a failure, never a match.
- **Assert that it ran**: state the expected counts (tests, files, blocks, rows) before the run and
  compare after.
- **Vary the input**: more than one size and shape, including each degraded input the code claims
  to handle; code that reads its own output gets at least three successive writes (the composed
  round trip).
- **A QA fixture must provably reach** the code path it claims to exercise.

Lives in CLAUDE.md § 15.8 (the senior-review checklist) and ENGINEERING_STANDARDS § 2.7 (shell
safety).

#### Cross-references

- L051 (the senior-review pass must run the tools — this lesson says how to trust what they print)
- L067 (verification must exercise the new behavior itself)
- L016 (a check that is allowed to fail is decoration — the same failure from the other side)

---

### L081 — A cloud-synced repository folder needs explicit operating rules; gitignored is not sync-ignored
````

<!-- block id=5a.4 path=docs/standards/LESSONS.md kind=replace -->

**5a.4** — L080 gains a data-point paragraph (adopter-originated, confirmed at the intake gate). FIND:

````text
#### Cross-references

- L042 (plan-first — § 15.9 sits upstream of it)
````

REPLACE WITH:

````text
#### Data point (Set v2.8 — an adopter, confirmed at the intake gate)

A plan to make a daily scheduled job survive a nightly server reboot was drafted, senior-reviewed
and approved before the server was probed — the probe had been deferred as "trigger choice only".
When it finally ran, a one-command process check showed there was no scheduler process at all:
nothing was being killed. Two of the plan's three premises were false, and most of its sub-tasks
became unnecessary. Step 2 of § 15.9 covers environmental facts too: **when a design rests on an
unverified fact about the environment, verify the fact before Phase 1 design, not after Phase 2
approval** — a one-command probe is cheaper than any design.

#### Cross-references

- L042 (plan-first — § 15.9 sits upstream of it)
````

### 5b — `docs/standards/CLAUDE.md` (template) — 1.7 → 1.8: D1, D2, D3, D5, C2 + an L087 Rule 14 bullet

<!-- block id=5b.1 path=docs/standards/CLAUDE.md kind=replace -->

**5b.1** — header 1.7 → 1.8. FIND:

````text
<!-- VERSION: 1.7 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Source: standards-source/ (canonical, domain-neutral). TEMPLATE — adopters copy to repo root and fill <placeholders>. -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.8 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). TEMPLATE — adopters copy to repo root and fill <placeholders>. -->
<!--
CHANGE LOG
v1.8 — <P3-DATE> — Standard Set Version v2.8: § 15.8 gains the senior-review checklist (positive controls, final-indentation tool runs, varied inputs, fixture reachability, content-checking gates, verified environmental premises — L080, L082–L084); Rule 14 names the Windows form of the harness link (a directory junction) and gains the never-handle-the-link-by-hand bullet (L087); § 12 dispatcher row for the Project Instructions template moved into a TEMPLATE-ONLY note — the file is never delivered to projects, so their copies no longer point at it (L068 recurrence); Rule 12 alias text genericized (a leftover domain identifier removed); § 1 + § 14 single-agent wording aligned with the delivery skill — replace § 14 with a "NOT IN USE" stub, never delete the block. No rule added or renumbered (15).
````

<!-- block id=5b.2 path=docs/standards/CLAUDE.md kind=replace -->

**5b.2** — § 1 Multi-agent placeholder (D3). FIND:

````text
**Multi-agent:** `<yes — Claude + a second agent (keep § 14); or no — single-agent (delete § 14)>`
````

REPLACE WITH:

````text
**Multi-agent:** `<yes — Claude + a second agent (keep § 14); or no — single-agent (replace the § 14 body with a "NOT IN USE" stub, markers kept)>`
````

<!-- block id=5b.3 path=docs/standards/CLAUDE.md kind=replace -->

**5b.3** — Rule 12 alias text (D2). FIND:

````text
When the operator says **"wrap up"** (or any of these aliases: `wrap` / `end session` / `close out` [context-disambiguated from `Closeout_Mode`] / `end of session` / `finish up`), Claude MUST read [`docs/SESSION_CLOSER.md`](docs/SESSION_CLOSER.md) and execute its § 1 routine BEFORE posting any farewell message. The § 4 first-response output block MUST be posted before the session is considered closed.
````

REPLACE WITH:

````text
When the operator says **"wrap up"** (or any of these aliases: `wrap` / `end session` / `close out` [context-disambiguated — not a session-end trigger when the talk is about project-specific closeout logic] / `end of session` / `finish up`), Claude MUST read [`docs/SESSION_CLOSER.md`](docs/SESSION_CLOSER.md) and execute its § 1 routine BEFORE posting any farewell message. The § 4 first-response output block MUST be posted before the session is considered closed.
````

<!-- block id=5b.4 path=docs/standards/CLAUDE.md kind=replace -->

**5b.4** — Rule 14: the Windows link form (D5). FIND:

````text
**`<repo>/.claude/project-data/`**, with a symlink left at the harness path, managed by
`scripts/claude_project_data.sh`:

```bash
bash scripts/claude_project_data.sh status   # health check (symlink + store)
````

REPLACE WITH:

````text
**`<repo>/.claude/project-data/`**, with a link left at the harness path (a symlink; a directory
junction on Windows), managed by `scripts/claude_project_data.sh`:

```bash
bash scripts/claude_project_data.sh status   # health check (link + store)
````

<!-- block id=5b.5 path=docs/standards/CLAUDE.md kind=replace -->

**5b.5** — Rule 14: never handle the link by hand (L087). FIND:

````text
- **`.claude/` stays gitignored** — memory may carry local-only sensitive values; the data travels
  with folder sync/copies, never the git remote.
````

REPLACE WITH:

````text
- **`.claude/` stays gitignored** — memory may carry local-only sensitive values; the data travels
  with folder sync/copies, never the git remote.
- **Never handle the link by hand** — moving, copying or deleting it in a file manager acts on the
  data behind it; use the tool's verbs (L087).
````

<!-- block id=5b.6 path=docs/standards/CLAUDE.md kind=replace -->

**5b.6** — § 12 dispatcher: the Project Instructions row becomes a vault-only note below the table (D1, Q3 = A). FIND:

````text
| Memory hygiene (what to memorize, what NOT to) | `docs/standards/MEMORY_PROTOCOL.md` |
| Setting up Claude.ai Project Instructions for a new project | `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md` |
| Researching a past decision or incident ("why does X exist?") | `archive/LESSONS.md` and `archive/postmortems/` |
| Drafting OR executing a vital change to a Critical File (central domain logic) | this file, § 15 (plan workflow) — and the plan in `docs/Plans/` |

---
````

REPLACE WITH:

````text
| Memory hygiene (what to memorize, what NOT to) | `docs/standards/MEMORY_PROTOCOL.md` |
| Researching a past decision or incident ("why does X exist?") | `archive/LESSONS.md` and `archive/postmortems/` |
| Drafting OR executing a vital change to a Critical File (central domain logic) | this file, § 15 (plan workflow) — and the plan in `docs/Plans/` |

<!-- TEMPLATE-ONLY:BEGIN (curator-only dispatcher note — sync never propagates this block; projects do not receive the file it names) -->
> **Curator only (the vault):** setting up Claude.ai Project Instructions for a new project →
> `docs/standards/PROJECT_INSTRUCTIONS_TEMPLATE.md`. The file stays in the vault; projects never
> receive it, so their copy of this table does not name it.
<!-- TEMPLATE-ONLY:END -->

---
````

<!-- block id=5b.7 path=docs/standards/CLAUDE.md kind=replace -->

**5b.7** — § 14 opening sentence (D3). FIND:

````text
Single-agent projects delete this section entirely** and set § 1 Multi-agent to "no".
````

REPLACE WITH:

````text
Single-agent projects replace this section's body with a short "NOT IN USE" stub — inside the PROJECT-OWNED markers, which stay (sync matches blocks by position)** — and set § 1 Multi-agent to "no".
````

<!-- block id=5b.8 path=docs/standards/CLAUDE.md kind=replace -->

**5b.8** — § 15.8: the senior-review checklist (C2; A3 + L080, L082–L084). FIND:

````text
- Any newly-exposed design decision surfaced as an explicit operator choice (not silently resolved).
````

REPLACE WITH:

````text
- Any newly-exposed design decision surfaced as an explicit operator choice (not silently resolved).

**Checklist the pass walks** (each line exists because a plan once shipped without it):

- **Positive controls** — every check, test, gate and QA harness the plan relies on is shown to fail
  once on a known-bad input before its pass is trusted (L082).
- **Tools on the extracted text** — linter, type checker and tests run on the code as extracted
  from the plan file, at its final indentation (L051, L083).
- **Varied inputs** — more than one size and shape, every degraded input the code claims to handle,
  and at least three successive writes for code that reads its own output (L082).
- **Reachable fixtures** — each QA scenario's fixture provably reaches the code path it claims to
  exercise (L082).
- **Gates check content** — every gate is its own step, read before the guarded action, and checks
  the content it protects (a diff, ancestry) rather than a commit id (L084).
- **Verified premises** — every environmental fact the design rests on was probed before design,
  not assumed (L080).
````

### 5c — `docs/standards/SESSION_OPENER.md` (template) — 1.8 → 1.9: § 1.5 leftover-`memory/` line (A5) + Windows link wording (D5)

<!-- block id=5c.1 path=docs/standards/SESSION_OPENER.md kind=replace -->

**5c.1** — header 1.8 → 1.9. FIND:

````text
<!-- VERSION: 1.8 -->
<!-- Last Updated: 2026-09-05 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.9 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.9 — <P3-DATE> — Standard Set Version v2.8: § 1.5 gains the leftover-`memory/` line (a session started before `link` leaves an empty `memory/` in the harness directory; older locality tools abort on it — adopter-originated, confirmed at the intake gate; L087); § 3.1 row 14 names the Windows form of the harness link (a junction).
````

<!-- block id=5c.2 path=docs/standards/SESSION_OPENER.md kind=replace -->

**5c.2** — § 1.5 leftover-`memory/` line. FIND:

````text
- Store **unexpectedly empty** when prior sessions are known to have written memory → **STOP**
  and warn the operator in the § 4 block (Rule 14 + `LESSONS.md` L050); do not proceed
  as if there is genuinely no history.
````

REPLACE WITH:

````text
- Store **unexpectedly empty** when prior sessions are known to have written memory → **STOP**
  and warn the operator in the § 4 block (Rule 14 + `LESSONS.md` L050); do not proceed
  as if there is genuinely no history.
- **A session that started before `link`** leaves an empty `memory/` in the harness directory;
  `link` absorbs it (locality tool 0.2 and later). If `link` aborts on it, the project's copy of
  the tool is older — remove that empty directory, rerun `link`, and note it in the § 4 block
  (`LESSONS.md` L087).
````

<!-- block id=5c.3 path=docs/standards/SESSION_OPENER.md kind=replace -->

**5c.3** — § 3.1 row 14 wording. FIND:

````text
| 14 | Project data written or left outside the project folder — locality symlink absent/broken after a machine change or folder move, silently orphaning memory + transcripts | § 1.5 probe on every session-open; any tool creating project state outside the repo | `CLAUDE.md` Rule 14 + `LESSONS.md` L050 (+ v1.5 generalization) |
````

REPLACE WITH:

````text
| 14 | Project data written or left outside the project folder — locality link (a symlink; a junction on Windows) absent/broken after a machine change or folder move, silently orphaning memory + transcripts | § 1.5 probe on every session-open; any tool creating project state outside the repo | `CLAUDE.md` Rule 14 + `LESSONS.md` L050 (+ v1.5 generalization) |
````

### 5d — `docs/standards/SESSION_CLOSER.md` (template) — 1.7 → 1.8: Windows link wording (D5)

<!-- block id=5d.1 path=docs/standards/SESSION_CLOSER.md kind=replace -->

**5d.1** — header 1.7 → 1.8. FIND:

````text
<!-- VERSION: 1.7 -->
<!-- Last Updated: 2026-08-27 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.8 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.8 — <P3-DATE> — Standard Set Version v2.8: § 1.6 locality confirm names the Windows form of the harness link (a junction).
````

<!-- block id=5d.2 path=docs/standards/SESSION_CLOSER.md kind=replace -->

**5d.2** — § 1.6 wording. FIND:

````text
If any new project state landed outside the folder this session, move it in (same symlink pattern)
````

REPLACE WITH:

````text
If any new project state landed outside the folder this session, move it in (same link pattern — a symlink; a junction on Windows)
````

### 5e — `docs/standards/MEMORY_PROTOCOL.md` — 1.1 → 1.2: dangling reference reworded (D1)

<!-- block id=5e.1 path=docs/standards/MEMORY_PROTOCOL.md kind=replace -->

**5e.1** — header 1.1 → 1.2. FIND:

````text
<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-08-19 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.2 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.2 — <P3-DATE> — Standard Set Version v2.8: § 4.6 fix line no longer names the Project Instructions template file (never delivered to projects — the reference dangled in every copy; L068 recurrence).
````

<!-- block id=5e.2 path=docs/standards/MEMORY_PROTOCOL.md kind=replace -->

**5e.2** — the reference. FIND:

````text
✅ Fix: Project-specific facts go in the **Project Instructions** field of that project (Tier B per `PROJECT_INSTRUCTIONS_TEMPLATE.md`), not in user-wide memory. Memory is for facts that span all projects.
````

REPLACE WITH:

````text
✅ Fix: Project-specific facts go in the **Project Instructions** field of that project (Tier B — the curator keeps the Project Instructions template), not in user-wide memory. Memory is for facts that span all projects.
````

### 5f — `docs/standards/PROMPT_STANDARDS.md` — 1.0 → 1.1: relayed prompts and guides (C1) + dangling reference (D1)

<!-- block id=5f.1 path=docs/standards/PROMPT_STANDARDS.md kind=replace -->

**5f.1** — header 1.0 → 1.1. FIND:

````text
<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.1 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.1 — <P3-DATE> — Standard Set Version v2.8: NEW § 3.12 relayed prompts and step guides (sent as a file; one self-checking block per step; one results file; bench-tested; plain words — L082, L084, L088); § 6.12 no longer names the Project Instructions template file (never delivered to projects; L068 recurrence).
````

<!-- block id=5f.2 path=docs/standards/PROMPT_STANDARDS.md kind=replace -->

**5f.2** — new § 3.12. FIND:

````text
If Codex deviated from the prompt's ALLOWLIST or scope, the recovery prompt to Codex follows the **PRIOR DEVIATION WARNING** pattern in § 9.5.

---

## 4. Anchor selection for FIND blocks
````

REPLACE WITH:

````text
If Codex deviated from the prompt's ALLOWLIST or scope, the recovery prompt to Codex follows the **PRIOR DEVIATION WARNING** pattern in § 9.5.

### 3.12 Relayed prompts and step guides (for another person or their agent)

When the operator relays a prompt or a step-by-step guide to someone else — a project owner, or
the agent in their project — through a chat app:

- **Send it as a file** (a `.txt` attachment), never as pasted text: chat apps render paired `*`
  and `_` as formatting and silently drop them — a pattern once lost its `*` this way, and only the
  prompt's own gate caught it.
- **One block per step, and every block prints its own verdict** — `>>> OK`, `>>> NOT YET` or
  `>>> STOP: <reason>`, computed by the block itself, not judged by the reader.
- **Every block appends to one results file** that the person sends back — the curator reads the
  evidence, not a summary of it.
- **A step that would do harm if run too early checks its own precondition first**, so a mistimed
  paste is harmless (L084).
- **Bench-test the guide** against the real tool in a mock of the recipient's layout, including
  negative controls (L082), and check every concrete claim — file names, counts, rows — against
  their live files before sending (L088).
- **Plain words** — for each step: what it does, what you should see, what to do if you don't.

---

## 4. Anchor selection for FIND blocks
````

<!-- block id=5f.3 path=docs/standards/PROMPT_STANDARDS.md kind=replace -->

**5f.3** — § 6.12 reference (D1). FIND:

````text
Why bad: popup UIs break the conversational flow. The operator has to click through a modal instead of reading and replying inline. For session protocols that run "one task per message" (per `PROJECT_INSTRUCTIONS_TEMPLATE.md`), popups add a context-switch that linear chat avoids.
````

REPLACE WITH:

````text
Why bad: popup UIs break the conversational flow. The operator has to click through a modal instead of reading and replying inline. For session protocols that run "one task per message" (as set in the project's Claude.ai Project Instructions), popups add a context-switch that linear chat avoids.
````

### 5g — `docs/standards/CICD_STANDARDS.md` — 1.0 → 1.1: dangling reference reworded (D1)

<!-- block id=5g.1 path=docs/standards/CICD_STANDARDS.md kind=replace -->

**5g.1** — header 1.0 → 1.1. FIND:

````text
<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.1 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.1 — <P3-DATE> — Standard Set Version v2.8: § 11.4 token-storage bullet no longer names the Project Instructions template file (never delivered to projects; L068 recurrence).
````

<!-- block id=5g.2 path=docs/standards/CICD_STANDARDS.md kind=replace -->

**5g.2** — the reference. FIND:

````text
Project Instructions Tier B (per `PROJECT_INSTRUCTIONS_TEMPLATE.md` § 5.9)
````

REPLACE WITH:

````text
Project Instructions Tier B (the curator keeps the Project Instructions template)
````

### 5h — `docs/standards/ENGINEERING_STANDARDS.md` — 1.0 → 1.1: NEW § 2.7 shell safety (C3)

<!-- block id=5h.1 path=docs/standards/ENGINEERING_STANDARDS.md kind=replace -->

**5h.1** — header 1.0 → 1.1. FIND:

````text
<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.1 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.1 — <P3-DATE> — Standard Set Version v2.8: NEW § 2.7 shell safety — variable-name clashes, zsh `=` and glob traps, guarded destructive commands, never-hidden check errors, per-machine tool differences, precondition checks as their own step, pinned tool recipes (L082, L084).
````

<!-- block id=5h.2 path=docs/standards/ENGINEERING_STANDARDS.md kind=replace -->

**5h.2** — new § 2.7. FIND:

````text
If a linter rule is genuinely wrong for the project's context, suppress it with an inline comment + reason — don't disable the rule globally.

---

## 3. Configuration & secrets
````

REPLACE WITH:

````text
If a linter rule is genuinely wrong for the project's context, suppress it with an inline comment + reason — don't disable the rule globally.

### 2.7 Shell safety — scripts and one-off commands

Shell mistakes fail quietly; each item below once turned a broken check into a "pass" (L082).

- **Never reuse the shell's own variable names.** In zsh, `path` is tied to `PATH`: assigning it
  empties the command search path and every later command silently vanishes. Use distinct names
  (`file_path`, `rel`).
- **zsh expands a leading `=`** (`echo =====` fails with "not found") — quote separators.
- **An unmatched glob aborts the whole command in zsh** ("no matches found"), and its exit code can
  read as "no results" — quote globs passed to tools (`--include='*.py'`).
- **Guard every variable in a destructive command**: `rm -rf "${DIR:?}"/*`, never
  `rm -rf "$DIR"/*` — an empty variable turns the second into `rm -rf /*`.
- **Never hide a check's errors** — `2>/dev/null` on the check itself turns a broken check into a
  pass; treat an empty value as a failure.
- **Tools differ by machine** — `find`, `sed`, `date` and `timeout` may be a different
  implementation on another machine, or absent; name the binary, or test the exact command on the
  target platform.
- **A precondition check is its own command**, read before the guarded action (L084) — a check
  chained with `;` or printed beside the action does not stop it.
- **Pin the tool recipe** in synced or editable environments — for example a type checker with an
  explicit module path and a fresh cache directory; a stale cache inside a synced folder once
  reported phantom errors.

---

## 3. Configuration & secrets
````

### 5i — `docs/standards/PROJECT_STANDARDS.md` — 1.1 → 1.2: NEW § 8.10 publishing to a wider audience (C4)

<!-- block id=5i.1 path=docs/standards/PROJECT_STANDARDS.md kind=replace -->

**5i.1** — header 1.1 → 1.2. FIND:

````text
<!-- VERSION: 1.1 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.2 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.2 — <P3-DATE> — Standard Set Version v2.8: NEW § 8.10 — before the first push to a new audience, scan the tree and the full history for secrets and audience-sensitive content, ask the operator with concrete examples, trust a new host key only on a fingerprint match, verify every remote after the push.
````

<!-- block id=5i.2 path=docs/standards/PROJECT_STANDARDS.md kind=replace -->

**5i.2** — new § 8.10. FIND:

````text
Effect: pipeline run count drops ~5-10× during multi-commit sessions. Pipeline UI stays meaningful. Each pipeline run has a purpose.

---

## 9. Sources of truth — single canonical authority per topic
````

REPLACE WITH:

````text
Effect: pipeline run count drops ~5-10× during multi-commit sessions. Pipeline UI stays meaningful. Each pipeline run has a purpose.

### 8.10 Publishing a repository to a wider audience

Before the first push to a new audience — a new remote, an organization, a public mirror:

1. **Scan the tracked tree AND the full history** — for secrets, and for content that audience
   should not see: other projects' names, internal addresses, account names, host fingerprints,
   personal data.
2. **Ask the operator with concrete examples** of what the scan found ("these three files name
   another project — acceptable for this audience?") and record the answer.
3. **Trust a new host key only on a fingerprint match** with the provider's published keys.
4. **After the push, verify every remote shows the same tip** (`git ls-remote`, L055).

---

## 9. Sources of truth — single canonical authority per topic
````

### 5j — `docs/standards/STANDARDS_INDEX.md` — 2.7 → 2.8: the release record

<!-- block id=5j.1 path=docs/standards/STANDARDS_INDEX.md kind=replace -->

**5j.1** — header 2.7 → 2.8. FIND:

````text
<!-- VERSION: 2.7 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 2.8 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v2.8 — <P3-DATE> — Standard Set Version v2.8 (lessons batch + senior-review checklist + template fixes + decision-log template): lessons L082–L089 (L082–L088 the curator's own, consolidated; L089 adopter-originated, confirmed at the intake gate) + an L080 data point; CLAUDE.md 1.8 (§ 15.8 checklist, Rule 14 junction + never-by-hand, TEMPLATE-ONLY dispatcher note, Rule 12 alias, § 1/§ 14 stub wording); PROMPT_STANDARDS 1.1 (§ 3.12), ENGINEERING_STANDARDS 1.1 (§ 2.7), PROJECT_STANDARDS 1.2 (§ 8.10), MEMORY_PROTOCOL 1.2 + CICD_STANDARDS 1.1 (dangling reference), SESSION_OPENER 1.9, SESSION_CLOSER 1.8, LESSONS 1.3, README 1.6; NEW meta template DECISION_LOG.md 0.1. § 1 block → v2.8; § 2 rows; § 3 caption + cells + totals (16 files = 11 binding + 5 meta; 89 lessons); § 4 self-service wording; § 6 v2.8 entry.
````

<!-- block id=5j.2 path=docs/standards/STANDARDS_INDEX.md kind=replace -->

**5j.2** — § 1 block. FIND:

````text
Standard Set Version: v2.7
Released:             2026-10-03
Baseline:             v2.6 (clock trust — L079 + PROJECT_STANDARDS § 5.6) + fleet-convergence intake: lesson L080 + CLAUDE.md § 15.9 Feature intake (before Phase 0) — preserve the document, investigate, redesign from scratch, then plan; lesson L081 + the Rule 14 cloud-synced-folder bullet; Rule 12 step 6 aligned with SESSION_CLOSER § 1.6.
Adopter contract:     11 binding files + 3 meta files (+ STANDARDS_LOG.md); 81 lessons (L001–L081); 15 standing rules in CLAUDE.md
````

REPLACE WITH:

````text
Standard Set Version: v2.8
Released:             <P3-DATE>
Baseline:             v2.7 (fleet-convergence intake — L080 feature intake, L081 cloud-synced folders) + lessons batch: L082–L088 (proof must be able to fail; prove first, generate and re-extract plan blocks; gates as their own step; engine as oracle; writes into another repository; shared folders; check before acting or telling) + L089 (a connection that opens is not a service that answers); CLAUDE.md § 15.8 senior-review checklist; template fixes (dangling Project Instructions references, Rule 12 alias, § 14 stub wording, Windows junction); PROMPT § 3.12 relayed guides; ENGINEERING § 2.7 shell safety; PROJECT § 8.10 publishing; the DECISION_LOG.md template.
Adopter contract:     11 binding files + 3 meta files (+ STANDARDS_LOG.md); 89 lessons (L001–L089); 15 standing rules in CLAUDE.md. Vault-only for now: the DECISION_LOG.md template (delivered to projects at a later Set Version).
````

<!-- block id=5j.3 path=docs/standards/STANDARDS_INDEX.md kind=replace -->

**5j.3** — § 2 Tier 1 row 9 (count). FIND:

````text
| 9 | `LESSONS.md` | Incident-to-rule archive — 81 lessons (append-only), each with incident + cost + codification + cross-references |
````

REPLACE WITH:

````text
| 9 | `LESSONS.md` | Incident-to-rule archive — 89 lessons (append-only), each with incident + cost + codification + cross-references |
````

<!-- block id=5j.4 path=docs/standards/STANDARDS_INDEX.md kind=replace -->

**5j.4** — § 2 Tier 2: the decision-log template row. FIND:

````text
| + | `STANDARDS_LOG.md` | **Experiences-log template** — the per-project contribution channel; the delivery skill copies it to the project's `docs/STANDARDS_LOG.md` (an adopter artifact, not a binding rule) |
````

REPLACE WITH:

````text
| + | `STANDARDS_LOG.md` | **Experiences-log template** — the per-project contribution channel; the delivery skill copies it to the project's `docs/STANDARDS_LOG.md` (an adopter artifact, not a binding rule) |
| + | `DECISION_LOG.md` | **Decision-log template** — one entry per operator decision, with the operator's verbatim answer; the vault keeps its own `docs/DECISION_LOG.md` from v2.8; delivery to projects comes with a later Set Version |
````

<!-- block id=5j.5 path=docs/standards/STANDARDS_INDEX.md kind=replace -->

**5j.5** — § 3 caption + per-file table + totals. FIND:

````text
Current state as of Set Version v2.7 (2026-10-03). Files unchanged since v1.0 keep their 2026-06-07 dates.

| File | Tier | Version | Last Updated |
|---|---|---|---|
| `CLAUDE.md` | Binding | 1.7 | 2026-10-03 |
| `PROJECT_STANDARDS.md` | Binding | 1.1 | 2026-10-03 |
| `PROMPT_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Binding | 1.1 | 2026-08-19 |
| `MEMORY_PROTOCOL.md` | Binding | 1.1 | 2026-08-19 |
| `ENGINEERING_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `VALIDATION_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `CICD_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `LESSONS.md` | Binding | 1.2 | 2026-09-05 |
| `SESSION_OPENER.md` | Binding | 1.8 | 2026-09-05 |
| `SESSION_CLOSER.md` | Binding | 1.7 | 2026-08-27 |
| `README.md` | Meta | 1.5 | 2026-10-03 |
| `STANDARDS_INDEX.md` | Meta | 2.7 | 2026-10-03 |
| `HOW_TO_USE.md` | Meta | 1.1 | 2026-08-17 |
| `STANDARDS_LOG.md` | Meta | 1.1 | 2026-08-17 |

**Total file count:** 15 (11 binding + 4 meta).
**Total lesson count in `LESSONS.md`:** 81 (L001–L081).
````

REPLACE WITH:

````text
Current state as of Set Version v2.8 (<P3-DATE>). Files unchanged since v1.0 keep their 2026-06-07 dates.

| File | Tier | Version | Last Updated |
|---|---|---|---|
| `CLAUDE.md` | Binding | 1.8 | <P3-DATE> |
| `PROJECT_STANDARDS.md` | Binding | 1.2 | <P3-DATE> |
| `PROMPT_STANDARDS.md` | Binding | 1.1 | <P3-DATE> |
| `PROJECT_INSTRUCTIONS_TEMPLATE.md` | Binding | 1.1 | 2026-08-19 |
| `MEMORY_PROTOCOL.md` | Binding | 1.2 | <P3-DATE> |
| `ENGINEERING_STANDARDS.md` | Binding | 1.1 | <P3-DATE> |
| `VALIDATION_STANDARDS.md` | Binding | 1.0 | 2026-06-07 |
| `CICD_STANDARDS.md` | Binding | 1.1 | <P3-DATE> |
| `LESSONS.md` | Binding | 1.3 | <P3-DATE> |
| `SESSION_OPENER.md` | Binding | 1.9 | <P3-DATE> |
| `SESSION_CLOSER.md` | Binding | 1.8 | <P3-DATE> |
| `README.md` | Meta | 1.6 | <P3-DATE> |
| `STANDARDS_INDEX.md` | Meta | 2.8 | <P3-DATE> |
| `HOW_TO_USE.md` | Meta | 1.1 | 2026-08-17 |
| `STANDARDS_LOG.md` | Meta | 1.1 | 2026-08-17 |
| `DECISION_LOG.md` | Meta | 0.1 | <P3-DATE> |

**Total file count:** 16 (11 binding + 5 meta).
**Total lesson count in `LESSONS.md`:** 89 (L001–L089).
````

<!-- block id=5j.6 path=docs/standards/STANDARDS_INDEX.md kind=replace -->

**5j.6** — § 4 self-service wording (D4). FIND:

````text
The delivery path is the **standard-docset skill** (vault-side): concierge — the curator runs
it against the target; or self-service — clone the vault repo and run
`bash scripts/bootstrap_skill.sh` once, then invoke the skill in a session opened at the
target. Bootstrap mode covers new projects; adopt mode migrates existing ones (dry-run gated).
````

REPLACE WITH:

````text
The delivery path is the **standard-docset skill** (vault-side). **Concierge:** the curator runs
it against the target. **Self-service:** paste one of the launcher prompts from the vault's
README into a Claude Code session — Claude clones the vault into a named folder, checks that it
is a vault, and reads the skill from that clone; nothing is installed
(`bash scripts/bootstrap_skill.sh` remains an optional macOS / Linux convenience). Modes:
**bootstrap** (new projects), **adopt** (existing ones, dry-run gated) and **selftest** (a
throwaway practice run that proves the skill works on the machine). Every mode ends with a
handoff report for the curator.
````

<!-- block id=5j.7 path=docs/standards/STANDARDS_INDEX.md kind=replace -->

**5j.7** — § 6: the v2.8 history entry. FIND:

````text
### v2.7 — 2026-10-03 — Fleet-convergence intake (feature intake + cloud-synced folders)
````

REPLACE WITH:

````text
### v2.8 — <P3-DATE> — Lessons batch, senior-review checklist, template fixes, decision-log template

Additive Minor, mostly authored by the curator. Lessons **L082–L088** consolidate about 25
recorded data points into seven lessons: a proof must be able to fail (positive controls); prove
the change first, then generate the plan's blocks and re-extract them; a gate is its own step and
checks content, not a commit id; engine as oracle; writes into another repository (explanations
accumulate, a landing is proven by the branch); a folder shared by several machines; check before
acting or telling. **L089** (adopter-originated, confirmed at the intake gate): a connection that
opens is not a service that answers. L080 gains an adopter data point (verify an environmental
premise before designing). **CLAUDE.md → 1.8:** § 15.8 gains the senior-review checklist; Rule 14
names the Windows form of the harness link (a directory junction) and forbids handling it by hand;
the dispatcher row for the Project Instructions template becomes a TEMPLATE-ONLY note — projects
never receive that file (an L068 recurrence; MEMORY_PROTOCOL → 1.2, PROMPT_STANDARDS and
CICD_STANDARDS → 1.1 reword the same reference); the Rule 12 alias text loses a leftover domain
identifier; § 1 and § 14 tell single-agent projects to keep a "NOT IN USE" stub, matching the
delivery skill. **PROMPT_STANDARDS** § 3.12 relayed prompts and step guides; **ENGINEERING_STANDARDS
→ 1.1** § 2.7 shell safety; **PROJECT_STANDARDS → 1.2** § 8.10 publishing a repository to a wider
audience; **SESSION_OPENER → 1.9** (§ 1.5 leftover-`memory/` line — adopter-originated, confirmed
at the intake gate; § 3.1 row 14 junction wording); **SESSION_CLOSER → 1.8** (junction wording).
New meta template **DECISION_LOG.md** (0.1): one entry per operator decision with the operator's
verbatim answer — the vault keeps its own log from this release; delivery to projects comes with a
later Set Version. § 4 self-service wording updated (launcher prompts, selftest mode, handoff
report). LESSONS → 1.3, which also covers L079–L081 (added at v2.6–v2.7 without a header bump).
Lesson count → 89; no rule change (15). Sync note: adopters receive a 10-item delta — CLAUDE.md,
SESSION_OPENER and SESSION_CLOSER merges; LESSONS, MEMORY_PROTOCOL, PROMPT_STANDARDS,
CICD_STANDARDS, ENGINEERING_STANDARDS and PROJECT_STANDARDS replaces; the SET_VERSION_ADOPTED
record — plus the handoff.

### v2.7 — 2026-10-03 — Fleet-convergence intake (feature intake + cloud-synced folders)
````

### 5k — `docs/standards/README.md` — 1.5 → 1.6: lesson count

<!-- block id=5k.1 path=docs/standards/README.md kind=replace -->

**5k.1** — header 1.5 → 1.6. FIND:

````text
<!-- VERSION: 1.5 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.6 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.6 — <P3-DATE> — Standard Set Version v2.8: LESSONS row count 81 → 89 (L001–L089; L082–L089 the v2.8 lessons batch).
````

<!-- block id=5k.2 path=docs/standards/README.md kind=replace -->

**5k.2** — the LESSONS row. FIND:

````text
| `LESSONS.md` | Humans researching "why" | 81 lessons (L001–L081, append-only), each with incident + cost + codification |
````

REPLACE WITH:

````text
| `LESSONS.md` | Humans researching "why" | 89 lessons (L001–L089, append-only), each with incident + cost + codification |
````

### 5l — `docs/standards/DECISION_LOG.md` — NEW 0.1: the decision-log template (Q5 = A, step 1)

<!-- block id=5l.1 path=docs/standards/DECISION_LOG.md kind=create -->

**5l.1** — create with this exact content:

````markdown
<!-- VERSION: 0.1 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v0.1 — <P3-DATE> — Initial (Standard Set Version v2.8): decision-log template — one entry per operator decision, with the operator's verbatim answer. Vault-only at v2.8; delivered to projects at a later Set Version.
-->

<!-- TEMPLATE-ONLY:BEGIN (template banner — deleted at instantiation; sync never propagates this block) -->
> **This file is a TEMPLATE.** A project copies it to `docs/DECISION_LOG.md`, deletes this
> TEMPLATE-ONLY block (markers included), resets the header to VERSION 1.0 with a one-line
> creation entry, and records its decisions below. The project-local copy is project-owned:
> no sync ever overwrites it.
<!-- TEMPLATE-ONLY:END -->

# DECISION_LOG.md — Operator decisions

**What this file is:** the single record of every decision the operator makes for this project —
scope, design options, approvals, intake-gate answers, waivers — written once, in plain words,
with the operator's exact reply. Plans, CHANGELOG entries and memory cite an entry by its id
(`DL-NNN`) instead of restating the decision.

## Rules

1. **One entry per decision**, added at the top (newest first). Ids are permanent and never reused.
2. **The question as it was asked** — in plain words, with the options and what each one does.
3. **The answer is the operator's verbatim reply**, in quotes, with its date — never paraphrased.
   A reply that answers several questions is quoted in each entry it answers.
4. **Applied in** names where the decision was carried out (plan section, commit, file); filled in
   when known, completed later by an appended line.
5. **Entries are never edited or deleted.** A changed decision is a NEW entry that says
   "Supersedes DL-NNN"; the old entry gets one appended line, "Superseded by DL-MMM".
6. **What counts:** any choice between options the operator was asked to make. Routine "go on
   commit?" / "push" confirmations are not entries — the commit and the push record them.
7. The file's VERSION bumps once per commit that adds entries.

## Entry format

```markdown
### DL-NNN — YYYY-MM-DD — <short title>

- **Question:** <plain words — what was asked>
- **Options:** A — <what it does> / B — <what it does> (recommended: <X>)
- **Answer:** "<the operator's verbatim reply>" — YYYY-MM-DD
- **Decision:** <one line: what was decided>
- **Applied in:** <plan § / commit / file>
```

---

## Decisions (newest first)

_(none yet)_
````

### 5m — `skill/modes/bootstrap.md` — 0.3 → 0.4: TEMPLATE-ONLY blocks never reach a new project (D-2)

<!-- block id=5m.1 path=skill/modes/bootstrap.md kind=replace -->

**5m.1** — header 0.3 → 0.4. FIND:

````text
<!-- VERSION: 0.3 -->
<!-- Last Updated: 2026-10-08 -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 0.4 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.4 — <P3-DATE> — Standard Set Version v2.8: § 3 — instantiating CLAUDE.md deletes every TEMPLATE-ONLY block (the § 12 Project Instructions note is curator-only since v2.8); the PROJECT_INSTRUCTIONS_TEMPLATE bullet no longer says the project's dispatcher names the file.
````

<!-- block id=5m.2 path=skill/modes/bootstrap.md kind=replace -->

**5m.2** — CLAUDE.md instantiation deletes TEMPLATE-ONLY blocks. FIND:

````text
  multi-agent: keep § 14 and name the second agent. Reset the header to VERSION 1.0 with a one-line
````

REPLACE WITH:

````text
  multi-agent: keep § 14 and name the second agent. Delete every TEMPLATE-ONLY block (markers
  included — e.g. the § 12 curator-only note). Reset the header to VERSION 1.0 with a one-line
````

<!-- block id=5m.3 path=skill/modes/bootstrap.md kind=replace -->

**5m.3** — the PROJECT_INSTRUCTIONS_TEMPLATE bullet. FIND:

````text
- `$SUITE/PROJECT_INSTRUCTIONS_TEMPLATE.md` → NOT copied (vault-side reference; the dispatcher row
  in the instantiated CLAUDE.md § 12 still names it — the project loads it from the vault when that
  topic is in scope, via the curator).
````

REPLACE WITH:

````text
- `$SUITE/PROJECT_INSTRUCTIONS_TEMPLATE.md` → NOT copied (curator-only; since Set v2.8 the project's
  CLAUDE.md does not name it — the curator uses it from the vault when setting up a Claude.ai
  Project).
````

### 5n — `skill/modes/adopt.md` — 0.4 → 0.5: TEMPLATE-ONLY blocks never reach an adopted project (D-2)

<!-- block id=5n.1 path=skill/modes/adopt.md kind=replace -->

**5n.1** — header 0.4 → 0.5. FIND:

````text
<!-- VERSION: 0.4 -->
<!-- Last Updated: 2026-10-08 -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 0.5 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.5 — <P3-DATE> — Standard Set Version v2.8: § 5 — every instantiated template has its TEMPLATE-ONLY blocks deleted (markers included), CLAUDE.md included.
````

<!-- block id=5n.2 path=skill/modes/adopt.md kind=replace -->

**5n.2** — § 5 apply. FIND:

````text
Per the approved list, copying suite content from `$SUITE` (read-only on the vault), preserving
````

REPLACE WITH:

````text
Per the approved list, copying suite content from `$SUITE` (read-only on the vault) — deleting every
TEMPLATE-ONLY block (markers included) from each template it instantiates, CLAUDE.md included — preserving
````

### 5o — `CLAUDE.md` (the vault's own contract) — 1.9 → 1.10: mirror the v2.8 template changes + the decision-log rule (D-1)

<!-- block id=5o.1 path=CLAUDE.md kind=replace -->

**5o.1** — header 1.9 → 1.10. FIND:

````text
<!-- VERSION: 1.9 -->
<!-- Last Updated: 2026-10-03 -->
<!-- Source: docs/standards/ (this repo). Bootstrapped from Standard Set v1.0 on 2026-06-07. Independent versions from this point forward. -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.10 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: docs/standards/ (this repo). Bootstrapped from Standard Set v1.0 on 2026-06-07. Independent versions from this point forward. -->
<!--
CHANGE LOG
v1.10 — <P3-DATE> — Standard Set Version v2.8 adoption (PLAN-020): mirrors the template — § 15.8 senior-review checklist; Rule 14 names the Windows junction + the never-handle-the-link-by-hand bullet (L087); Rule 12 alias text genericized. NEW § 10 "Record every operator decision" + § 13 single-source line — this vault keeps `docs/DECISION_LOG.md` from v2.8 (PLAN-020 D-1 = § 10 bullet, no rule number; projects receive the log and the rule at a later Set Version). § 12 keeps the Project Instructions row — the file exists in this repo. No rule added or renumbered (16).
````

<!-- block id=5o.2 path=CLAUDE.md kind=replace -->

**5o.2** — Rule 12 alias text. FIND:

````text
When the operator says **"wrap up"** (or any of these aliases: `wrap` / `end session` / `close out` [context-disambiguated from `Closeout_Mode`] / `end of session` / `finish up`), Claude MUST read [`docs/SESSION_CLOSER.md`](docs/SESSION_CLOSER.md) and execute its § 1 routine BEFORE posting any farewell message. The § 4 first-response output block MUST be posted before the session is considered closed.
````

REPLACE WITH:

````text
When the operator says **"wrap up"** (or any of these aliases: `wrap` / `end session` / `close out` [context-disambiguated — not a session-end trigger when the talk is about project-specific closeout logic] / `end of session` / `finish up`), Claude MUST read [`docs/SESSION_CLOSER.md`](docs/SESSION_CLOSER.md) and execute its § 1 routine BEFORE posting any farewell message. The § 4 first-response output block MUST be posted before the session is considered closed.
````

<!-- block id=5o.3 path=CLAUDE.md kind=replace -->

**5o.3** — Rule 14 link wording. FIND:

````text
**`<repo>/.claude/project-data/`**, with a symlink left at the harness path, managed by
`scripts/claude_project_data.sh`:

```bash
bash scripts/claude_project_data.sh status   # health check (symlink + store)
````

REPLACE WITH:

````text
**`<repo>/.claude/project-data/`**, with a link left at the harness path (a symlink; a directory
junction on Windows), managed by `scripts/claude_project_data.sh`:

```bash
bash scripts/claude_project_data.sh status   # health check (link + store)
````

<!-- block id=5o.4 path=CLAUDE.md kind=replace -->

**5o.4** — Rule 14: never handle the link by hand. FIND:

````text
- **`.claude/` stays gitignored** — memory may carry local-only sensitive values; the data travels
  with folder sync/copies (Dropbox here), never the git remote.
````

REPLACE WITH:

````text
- **`.claude/` stays gitignored** — memory may carry local-only sensitive values; the data travels
  with folder sync/copies (Dropbox here), never the git remote.
- **Never handle the link by hand** — moving, copying or deleting it in a file manager acts on the
  data behind it; use the tool's verbs (L087).
````

<!-- block id=5o.5 path=CLAUDE.md kind=replace -->

**5o.5** — § 10: record every operator decision (D-1). FIND:

````text
- If the data confirms the original answer, paste the data verbatim. If the data contradicts, update the answer and note the correction.

---

## 11. Commit policy
````

REPLACE WITH:

````text
- If the data confirms the original answer, paste the data verbatim. If the data contradicts, update the answer and note the correction.

### Record every operator decision

Every choice the operator is asked to make — scope, design options, plan approvals, Rule 16 gate
answers, waivers — is recorded once in `docs/DECISION_LOG.md` as a `DL-NNN` entry: the question in
plain words, the options, the operator's **verbatim** answer with its date, and where it was
applied. It lands in the same commit as the work it governs (or the next commit, when no work
follows). Plans' § 9.1 decision records and CHANGELOG entries cite the `DL-NNN` id. Ask in plain
words first — what the decision is, a real example, each option and its downside, a
recommendation, a one-line reply format. Routine "go on commit?" / "push" confirmations are not
entries. Decisions before 2026-10-12 live in each plan's § 9.1.

---

## 11. Commit policy
````

<!-- block id=5o.6 path=CLAUDE.md kind=replace -->

**5o.6** — § 13 single-source line. FIND:

````text
- **Cross-cutting project history:** `CHANGELOG.md` (root)
- **Folder layout authoritative reference:** `docs/folder_structure.md`
````

REPLACE WITH:

````text
- **Cross-cutting project history:** `CHANGELOG.md` (root)
- **Operator decisions:** `docs/DECISION_LOG.md` (from 2026-10-12; earlier decisions live in each plan's § 9.1)
- **Folder layout authoritative reference:** `docs/folder_structure.md`
````

<!-- block id=5o.7 path=CLAUDE.md kind=replace -->

**5o.7** — § 15.8 checklist (mirrors template 5b.8). FIND:

````text
- Any newly-exposed design decision surfaced as an explicit operator choice (not silently resolved).
````

REPLACE WITH:

````text
- Any newly-exposed design decision surfaced as an explicit operator choice (not silently resolved).

**Checklist the pass walks** (each line exists because a plan once shipped without it):

- **Positive controls** — every check, test, gate and QA harness the plan relies on is shown to fail
  once on a known-bad input before its pass is trusted (L082).
- **Tools on the extracted text** — linter, type checker and tests run on the code as extracted
  from the plan file, at its final indentation (L051, L083).
- **Varied inputs** — more than one size and shape, every degraded input the code claims to handle,
  and at least three successive writes for code that reads its own output (L082).
- **Reachable fixtures** — each QA scenario's fixture provably reaches the code path it claims to
  exercise (L082).
- **Gates check content** — every gate is its own step, read before the guarded action, and checks
  the content it protects (a diff, ancestry) rather than a commit id (L084).
- **Verified premises** — every environmental fact the design rests on was probed before design,
  not assumed (L080).
````

### 5p — `archive/LESSONS.md` (the vault's own archive) — 1.0 → 1.1: the L082–L089 provenance entry

<!-- block id=5p.1 path=archive/LESSONS.md kind=replace -->

**5p.1** — header 1.0 → 1.1. FIND:

````text
<!-- VERSION: 1.0 -->
<!-- Last Updated: 2026-06-07 -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.1 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: standards-source/ (canonical, domain-neutral). -->
<!--
CHANGE LOG
v1.1 — <P3-DATE> — Standard Set Version v2.8 (PLAN-020): the L082–L089 provenance entry (sources per lesson; the full texts live in docs/standards/LESSONS.md). Stamp catch-up: the v2.3 (L070–L078), v2.6 (L079) and v2.7 (L080–L081) entries were added without a VERSION bump — this 1.1 covers them too (L063 class).
````

<!-- block id=5p.2 path=archive/LESSONS.md kind=replace -->

**5p.2** — table of contents line. FIND:

````text
 - [L080–L081 — Fleet-convergence intake from EverOn.Equinex (PLAN-011)](#l080l081--fleet-convergence-intake-from-everonequinex-plan-011)
````

REPLACE WITH:

````text
 - [L082–L089 — v2.8 lessons batch: curator candidates + two 780-estimator intake items (PLAN-020)](#l082l089--v28-lessons-batch-curator-candidates--two-780-estimator-intake-items-plan-020)
 - [L080–L081 — Fleet-convergence intake from EverOn.Equinex (PLAN-011)](#l080l081--fleet-convergence-intake-from-everonequinex-plan-011)
````

<!-- block id=5p.3 path=archive/LESSONS.md kind=replace -->

**5p.3** — the provenance entry. FIND:

````text
## 3. The lessons (newest first)

### L080–L081 — Fleet-convergence intake from EverOn.Equinex (PLAN-011)
````

REPLACE WITH:

````text
## 3. The lessons (newest first)

### L082–L089 — v2.8 lessons batch: curator candidates + two 780-estimator intake items (PLAN-020)

**Date:** <P3-DATE>
**Project:** Standard DocSet (vault) — curator lesson candidates recorded 2026-06-16 → 2026-10-12 in the
local OPEN_TASKS register; 780-estimator (L089 + the L080 data point); EverOn.Capital-Signal (E002's
remainder → L087)
**Phase / Task:** v2.8 inventory → operator answers 2026-10-12 (`docs/DECISION_LOG.md` DL-004 … DL-009;
Rule 16 gate "Q2. yes" = DL-005) → PLAN-020 → Standard Set Version v2.8

**Provenance record** (project-voice entry; the full genericized lessons live in the canonical
`docs/standards/LESSONS.md` — dual-voice practice per L068):

| Vault # | Source | Title (canonical) |
|---|---|---|
| L082 | "a green proof must prove it ran" data points #1–#9 (PLAN-013 D2 session → PLAN-019 harness) + PLAN-013 D2 composed round trip + PLAN-013 QA-K3 fixture reachability + 780-estimator PLAN-004 v0.3 (one input size — gate item #8) | A proof must be able to fail |
| L083 | proven-code-first + generated plan blocks, data points #1–#10 (PLAN-008 → PLAN-019) + PLAN-009 raw-anchor note + approved-plan anchor shifts (PLAN-011 0.4, PLAN-016 0.3) | Prove first; generate and re-extract plan blocks |
| L084 | PLAN-017 QA-M7 incident (check printed beside the write) + PLAN-011 D1 (sha-keyed gate) + PLAN-019 tracker 3.0 pre-check | A gate is its own step and checks content |
| L085 | PLAN-009 D3 (SVA shape vs `record_adoption`) + PLAN-017 catch-up path (1 of 3 prep steps documented) + PLAN-017 D1 replace-mode provenance | Engine as oracle |
| L086 | PLAN-012 → PLAN-013 handoff overwrite + 780-Automation's discarded v2.3 + v2.4 writes + Capital-Signal's uncommitted v2.1–v2.5 writes + Equinex's deleted-but-unlanded handoff (2026-10-05) | Writes into another repository |
| L087 | cross-machine `git status` (2026-10-03) + 780-estimator store-loss incident (2026-10-06, Explorer move of the junction) + the same-name transcript choice + Capital-Signal E002 Suggested (3) + its lesson half | A folder shared by several machines |
| L088 | PLAN-018 audit (Step 0 `git -C ""`) + the owner message checked against a fresh clone (2026-10-05 wrap-up) + the 780-VPN machine-ownership record (corrected 2026-10-03) | Check before acting or telling |
| L089 | 780-estimator CHANGELOG 2026-09-05 (their PLAN-014 — a TLS handshake reported REACHABLE) — gate item #5 | A connection that opens is not a service that answers |
| L080 + data point | 780-estimator PLAN-013 § 14.4 (no scheduler process at all) — gate item #4 | (data-point paragraph in L080) |

**Gate:** the 780-estimator items #4, #5 and #8 were first confirmed at the 2026-10-05 PLAN-017 gate and
confirmed again for integration at the v2.8 Rule 16 gate (DL-005), together with Capital-Signal E002's
remainder; item #6 (ALLOWLIST-count automation) went to the vault-tooling queue, not the suite. E002's
status in Capital-Signal's log already reads `integrated` (its script half shipped in PLAN-017); its
lesson half lands here as L087 item 4 — no further write-back.

**Not codified** (operator Q6 = yes, DL-009): C5 (QA when a run moves machines) deferred; C6 (an agent
safety check blocking transcript recovery) rejected as tool-specific; the dropped list (already
codified, already done, or single soft data points) is in the PLAN-020 § 2 intake record.

---

### L080–L081 — Fleet-convergence intake from EverOn.Equinex (PLAN-011)
````

### 5q — `docs/SESSION_OPENER.md` (the vault's own opener) — 1.21 → 1.22

<!-- block id=5q.1 path=docs/SESSION_OPENER.md kind=replace -->

**5q.1** — header 1.21 → 1.22 + Source ref. FIND:

````text
<!-- VERSION: 1.21 -->
<!-- Last Updated: 2026-10-05 -->
<!-- Source: docs/standards/SESSION_OPENER.md (template) v1.7. Project-local instance for Standard DocSet. -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.22 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: docs/standards/SESSION_OPENER.md (template) v1.9. Project-local instance for Standard DocSet. -->
<!--
CHANGE LOG
v1.22 — <P3-DATE> — Standard Set Version v2.8 adoption (PLAN-020): § 1.5 leftover-`memory/` line + § 3.1 row 13 junction wording (mirrors template 1.9); header Source ref → template v1.9 (stale since v2.5 — deferred-minor cleared). The template's § 1.1 engine-handoff check stays out of this instance by design: the engine never writes into the vault.
````

<!-- block id=5q.2 path=docs/SESSION_OPENER.md kind=replace -->

**5q.2** — § 1.5 leftover-`memory/` line. FIND:

````text
- Store **unexpectedly empty** when prior sessions are known to have written memory → **STOP**
  and warn the operator in the § 4 block (Rule 14 + `archive/LESSONS.md` L050); do not proceed
  as if there is genuinely no history.
````

REPLACE WITH:

````text
- Store **unexpectedly empty** when prior sessions are known to have written memory → **STOP**
  and warn the operator in the § 4 block (Rule 14 + `archive/LESSONS.md` L050); do not proceed
  as if there is genuinely no history.
- **A session that started before `link`** leaves an empty `memory/` in the harness directory;
  `link` absorbs it (locality tool 0.2 and later). If `link` aborts on it, the copy of the tool is
  older — remove that empty directory, rerun `link`, and note it in the § 4 block (L087).
````

<!-- block id=5q.3 path=docs/SESSION_OPENER.md kind=replace -->

**5q.3** — § 3.1 row 13 wording. FIND:

````text
| 13 | Project data written or left outside the project folder — locality symlink absent/broken after a machine change or folder move, silently orphaning memory + transcripts | § 1.5 probe on every session-open; any tool creating project state outside the repo | `CLAUDE.md` Rule 14 + `LESSONS.md` L050 (+ v1.5 generalization) |
````

REPLACE WITH:

````text
| 13 | Project data written or left outside the project folder — locality link (a symlink; a junction on Windows) absent/broken after a machine change or folder move, silently orphaning memory + transcripts | § 1.5 probe on every session-open; any tool creating project state outside the repo | `CLAUDE.md` Rule 14 + `LESSONS.md` L050 (+ v1.5 generalization) |
````

### 5r — `docs/SESSION_CLOSER.md` (the vault's own closer) — 1.8 → 1.9

<!-- block id=5r.1 path=docs/SESSION_CLOSER.md kind=replace -->

**5r.1** — header 1.8 → 1.9 + Source ref. FIND:

````text
<!-- VERSION: 1.8 -->
<!-- Last Updated: 2026-10-05 -->
<!-- Source: docs/standards/SESSION_CLOSER.md (template) v1.7. Project-local instance for Standard DocSet. -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.9 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: docs/standards/SESSION_CLOSER.md (template) v1.8. Project-local instance for Standard DocSet. -->
<!--
CHANGE LOG
v1.9 — <P3-DATE> — Standard Set Version v2.8 adoption (PLAN-020): § 1.6 locality confirm names the Windows junction (mirrors template 1.8); header Source ref → template v1.8.
````

<!-- block id=5r.2 path=docs/SESSION_CLOSER.md kind=replace -->

**5r.2** — § 1.6 wording. FIND:

````text
If any new project state landed outside the folder this session, move it in (same symlink pattern)
````

REPLACE WITH:

````text
If any new project state landed outside the folder this session, move it in (same link pattern — a symlink; a junction on Windows)
````

### 5s — `docs/SET_VERSION_ADOPTED.md` — 1.15 → 1.16: adopt v2.8

<!-- block id=5s.1 path=docs/SET_VERSION_ADOPTED.md kind=replace -->

**5s.1** — header 1.15 → 1.16. FIND:

````text
<!-- VERSION: 1.15 -->
<!-- Last Updated: 2026-10-03 -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 1.16 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v1.16 — <P3-DATE> — Adopt Standard Set Version v2.8 (PLAN-020: lessons L082–L089 + L080 data point — the 780-estimator items and Capital-Signal E002's remainder confirmed at the Rule 16 gate, DL-005; § 15.8 checklist; template fixes; PROMPT § 3.12, ENGINEERING § 2.7, PROJECT § 8.10; the DECISION_LOG template). Counts → 89 lessons / 16-own rules. Own-instance reconcile same-commit: root CLAUDE.md → 1.10 (mirrors + the § 10 decision-log rule), `archive/LESSONS.md` → 1.1 (L082–L089 provenance entry), SESSION_OPENER → 1.22, SESSION_CLOSER → 1.9; NEW `docs/DECISION_LOG.md`; added the v2.8 backport row.
````

<!-- block id=5s.2 path=docs/SET_VERSION_ADOPTED.md kind=replace -->

**5s.2** — the Standard Set Version bullet. FIND:

````text
- **Standard Set Version:** v2.7 (fleet-convergence intake: lesson L080 + CLAUDE.md § 15.9 Feature
````

REPLACE WITH:

````text
- **Standard Set Version:** v2.8 (lessons batch: L082–L088 from the curator's own recorded
  candidates + L089 and an L080 data point from an adopter, confirmed at the Rule 16 gate; the
  CLAUDE.md § 15.8 senior-review checklist; template fixes — the dangling Project Instructions
  references, the Rule 12 alias, § 14 stub wording, the Windows junction; PROMPT § 3.12 relayed
  guides, ENGINEERING § 2.7 shell safety, PROJECT § 8.10 publishing; the DECISION_LOG template,
  which this vault instantiates as `docs/DECISION_LOG.md`.
  Atop v2.7: fleet-convergence intake: lesson L080 + CLAUDE.md § 15.9 Feature
````

<!-- block id=5s.3 path=docs/SET_VERSION_ADOPTED.md kind=replace -->

**5s.3** — Adopted on. FIND:

````text
- **Adopted on:** 2026-10-03 (v2.6 adopted 2026-10-03; v2.5 adopted 2026-09-05; v2.4 adopted 2026-08-27; v2.3 adopted 2026-08-27; v2.2 adopted 2026-08-19; v2.1 adopted 2026-08-18; v2.0 adopted 2026-08-17; v1.6 adopted 2026-08-16; v1.5 adopted 2026-08-16; v1.4 adopted 2026-08-16; v1.3 adopted 2026-06-20; v1.2 adopted 2026-06-17; v1.1 adopted 2026-06-13; v1.0 baseline 2026-06-07)
````

REPLACE WITH:

````text
- **Adopted on:** <P3-DATE> (v2.7 adopted 2026-10-03; v2.6 adopted 2026-10-03; v2.5 adopted 2026-09-05; v2.4 adopted 2026-08-27; v2.3 adopted 2026-08-27; v2.2 adopted 2026-08-19; v2.1 adopted 2026-08-18; v2.0 adopted 2026-08-17; v1.6 adopted 2026-08-16; v1.5 adopted 2026-08-16; v1.4 adopted 2026-08-16; v1.3 adopted 2026-06-20; v1.2 adopted 2026-06-17; v1.1 adopted 2026-06-13; v1.0 baseline 2026-06-07)
````

<!-- block id=5s.4 path=docs/SET_VERSION_ADOPTED.md kind=replace -->

**5s.4** — the adopted-state counts. FIND:

````text
- **81 lessons** (L001–L081) in `archive/LESSONS.md` (L070–L078 and L080–L081 recorded there as
  provenance-table intake entries; full genericized texts in the canonical file).
- The suite per `docs/standards/STANDARDS_INDEX.md` (11 binding files + 3 meta files + the
  `STANDARDS_LOG.md` template).
````

REPLACE WITH:

````text
- **89 lessons** (L001–L089) in `archive/LESSONS.md` (L070–L078, L080–L081 and L082–L089 recorded
  there as provenance-table entries; full genericized texts in the canonical file).
- The suite per `docs/standards/STANDARDS_INDEX.md` (11 binding files + 3 meta files + the
  `STANDARDS_LOG.md` and `DECISION_LOG.md` templates).
````

<!-- block id=5s.5 path=docs/SET_VERSION_ADOPTED.md kind=replace -->

**5s.5** — the v2.8 backport row. FIND:

````text
| Set Version | Adopted on | Notes |
|---|---|---|
````

REPLACE WITH:

````text
| Set Version | Adopted on | Notes |
|---|---|---|
| v2.8 | <P3-DATE> | Lessons batch + senior-review checklist + template fixes + decision-log template (PLAN-020; operator answers DL-004 … DL-009, Rule 16 gate DL-005): L082–L088 (curator candidates, consolidated) + L089 and the L080 data point (780-estimator, gate items #5 / #4) + Capital-Signal E002's remainder (opener § 1.5 line, L087); template CLAUDE.md → 1.8, SESSION_OPENER → 1.9, SESSION_CLOSER → 1.8, MEMORY_PROTOCOL → 1.2, PROMPT / CICD / ENGINEERING → 1.1, PROJECT_STANDARDS → 1.2, LESSONS → 1.3, README → 1.6, NEW DECISION_LOG template 0.1; skill bootstrap / adopt modes strip TEMPLATE-ONLY blocks from CLAUDE.md (D-2). Own-instance reconcile: root `CLAUDE.md` → 1.10 (mirrors + the § 10 decision-log rule, D-1), `archive/LESSONS.md` → 1.1, `docs/SESSION_OPENER.md` → 1.22, `docs/SESSION_CLOSER.md` → 1.9, NEW `docs/DECISION_LOG.md`. Counts → 89 lessons / 16-own rules. |
````

### 5t — `docs/DECISION_LOG.md` — NEW 1.0: the vault's own decision log (Q5 = A, step 1)

<!-- block id=5t.1 path=docs/DECISION_LOG.md kind=create -->

**5t.1** — create with this exact content (Phase 3 then adds the PLAN-020 Phase 2 entries per § 6 rule 5):

````markdown
<!-- VERSION: 1.0 -->
<!-- Last Updated: <P3-DATE> -->
<!-- Source: docs/standards/DECISION_LOG.md (template) v0.1. Project-local instance for Standard DocSet. -->
<!--
CHANGE LOG
v1.0 — <P3-DATE> — Created (PLAN-020, Standard Set Version v2.8): the vault's decision log; seeded with the decisions of 2026-10-12 (DL-001 … DL-009, verbatim). Decisions before 2026-10-12 live in each plan's § 9.1.
-->

# DECISION_LOG.md — Operator decisions

**What this file is:** the single record of every decision the operator makes for this project —
scope, design options, approvals, intake-gate answers, waivers — written once, in plain words,
with the operator's exact reply. Plans, CHANGELOG entries and memory cite an entry by its id
(`DL-NNN`) instead of restating the decision. Binding per `CLAUDE.md` § 10 "Record every operator
decision".

## Rules

1. **One entry per decision**, added at the top (newest first). Ids are permanent and never reused.
2. **The question as it was asked** — in plain words, with the options and what each one does.
3. **The answer is the operator's verbatim reply**, in quotes, with its date — never paraphrased.
   A reply that answers several questions is quoted in each entry it answers.
4. **Applied in** names where the decision was carried out (plan section, commit, file); filled in
   when known, completed later by an appended line.
5. **Entries are never edited or deleted.** A changed decision is a NEW entry that says
   "Supersedes DL-NNN"; the old entry gets one appended line, "Superseded by DL-MMM".
6. **What counts:** any choice between options the operator was asked to make. Routine "go on
   commit?" / "push" confirmations are not entries — the commit and the push record them.
7. The file's VERSION bumps once per commit that adds entries.

## Entry format

```markdown
### DL-NNN — YYYY-MM-DD — <short title>

- **Question:** <plain words — what was asked>
- **Options:** A — <what it does> / B — <what it does> (recommended: <X>)
- **Answer:** "<the operator's verbatim reply>" — YYYY-MM-DD
- **Decision:** <one line: what was decided>
- **Applied in:** <plan § / commit / file>
```

---

## Decisions (newest first)

### DL-009 — 2026-10-12 — v2.8: the remaining recommendations (lessons, notes, template fixes)

- **Question:** Are the recommendations for the seven new lessons (B), the notes (C — C5 deferred,
  C6 rejected) and the template fixes (D) fine as listed?
- **Options:** yes / name the items to change (recommended: yes)
- **Answer:** "Q5 A, Q6 yes" — 2026-10-12
- **Decision:** B1–B7 → L082–L088; C1–C4 integrated, C5 deferred, C6 rejected; D1–D5 fixed.
- **Applied in:** PLAN-020 (Standard Set Version v2.8).

### DL-008 — 2026-10-12 — The decision log: how far it goes

- **Question:** A decision log — one file recording every decision once, with the operator's exact
  words. A brand-new file cannot reach existing projects without an engine change. How far should
  it go?
- **Options:** A — two steps: the vault starts its own log in v2.8 and the projects' template is
  written; PLAN-021 delivers it to every project with the rule that tells their sessions to use it /
  B — vault only, never in projects / C — everything in v2.8, pulling an engine change in
  (recommended: A)
- **Answer:** "Q5 A, Q6 yes" — 2026-10-12
- **Decision:** A — vault log + template in v2.8; delivery to projects in PLAN-021.
- **Applied in:** PLAN-020 (this file, `docs/standards/DECISION_LOG.md`, `CLAUDE.md` § 10); PLAN-021 (queued).

### DL-007 — 2026-10-12 — Plain-language decisions + a decision log

- **Question:** The "explain decisions in plain language with a small table and a one-line reply
  format" pattern has 12 data points. Save it as a feedback memory now?
- **Options:** yes / no (recommended: yes)
- **Answer:** "Q4. yes this is very important we should have descision log" — 2026-10-12
- **Decision:** feedback memory saved (marked very important); a decision log requested (→ DL-008).
- **Applied in:** memory `feedback_plain_language_decisions.md`; DL-008.

### DL-006 — 2026-10-12 — v2.8: the four dangling Project Instructions references

- **Question:** Four places in the standards point at `PROJECT_INSTRUCTIONS_TEMPLATE.md`, a file
  projects never receive. Take the pointers out of the projects' copies, or point them at the
  vault's copy?
- **Options:** A — remove them from the projects' copies (the vault keeps a curator-only note) /
  B — point all four at the vault's location (recommended: A)
- **Answer:** "Q3. eplain in simple words" (first reply), then "Q3 A" — 2026-10-12
- **Decision:** A.
- **Applied in:** PLAN-020 § 5b.6, 5e, 5f.3, 5g (Standard Set Version v2.8).

### DL-005 — 2026-10-12 — v2.8 Rule 16 intake gate

- **Question:** Confirm for integration: A1 (780-estimator #4 → an L080 data point), A2 (#5 → a new
  lesson), A3 (#8 → a Rule 13 checklist line), A5 (Capital-Signal E002's remainder → an opener
  § 1.5 line + a lesson); A4 (#6, ALLOWLIST-count automation) deferred to vault tooling?
- **Options:** yes / no / name the items to change (recommended: yes)
- **Answer:** "Q2. yes" — 2026-10-12
- **Decision:** A1, A2, A3, A5 integrated; A4 deferred; nothing rejected.
- **Applied in:** PLAN-020 (L080 data point, L089, § 15.8 checklist, SESSION_OPENER § 1.5, L087).

### DL-004 — 2026-10-12 — v2.8 scope

- **Question:** Should v2.8 be documents only (lessons, notes, template fixes), with the locality-tool
  delivery and the skill / Windows fixes as their own changes — or one bigger release including
  the engine change?
- **Options:** A — documents only; the rest separately / B — everything in one v2.8 (recommended: A)
- **Answer:** "Q1 A, but record the rest for planning and getting them done right away" — 2026-10-12
- **Decision:** A; the rest queued to start right after v2.8 (PLAN-021, the skill Minor, vault tooling).
- **Applied in:** PLAN-020; OPEN_TASKS "Right after v2.8".

### DL-003 — 2026-10-12 — PLAN-019 approval

- **Question:** Approve PLAN-019 (the git transport fails fast) with the two design answers, and its
  draft + approval commits?
- **Options:** approve (D19.A) / revise (recommended: approve)
- **Answer:** "D1. A , D2. A", then "go" — 2026-10-12
- **Decision:** D19.A approved.
- **Applied in:** `63e6c1f` (approval); `9366b7a` (Phase 3, plan CLOSED).

### DL-002 — 2026-10-12 — PLAN-019 D-2: a cap on every transport command

- **Question:** Should every git / rsync command stop after a time limit, to catch a slow-but-alive
  transfer the ssh options cannot see?
- **Options:** A — 300 s on every command / B — no cap, ssh options only (recommended: A)
- **Answer:** "D1. A , D2. A" — 2026-10-12
- **Decision:** A — 300 s.
- **Applied in:** `src/standard_document_updater/transport.py` 0.4 (`9366b7a`).

### DL-001 — 2026-10-12 — PLAN-019 D-1: whose ssh command git runs

- **Question:** When the engine adds its fail-fast ssh options, should it keep the operator's own ssh
  command (`GIT_SSH_COMMAND`, else `core.sshCommand`) and append to it — or always use plain `ssh`?
- **Options:** A — keep the operator's own and append; a legacy `GIT_SSH` program left alone / B —
  always `ssh` + the options (overrides an operator setting a Windows machine needs) (recommended: A)
- **Answer:** "D1. A , D2. A" — 2026-10-12
- **Decision:** A.
- **Applied in:** `src/standard_document_updater/transport.py` 0.4 (`9366b7a`).
````

### 5u — `docs/folder_structure.md` — 0.18 → 0.19: the two decision-log files + two stale captions

<!-- block id=5u.1 path=docs/folder_structure.md kind=replace -->

**5u.1** — header 0.18 → 0.19. FIND:

````text
<!-- VERSION: 0.18 -->
<!-- Last Updated: 2026-10-08 -->
<!--
CHANGE LOG
````

REPLACE WITH:

````text
<!-- VERSION: 0.19 -->
<!-- Last Updated: <P3-DATE> -->
<!--
CHANGE LOG
v0.19 — <P3-DATE> — PLAN-020 (Standard Set Version v2.8): added docs/DECISION_LOG.md (the vault's decision log) and docs/standards/DECISION_LOG.md (the template) to the tree; caught up two stale captions — suite "Set Version v2.0" → v2.8, template LESSONS "L001–L067" → L001–L089.
````

<!-- block id=5u.2 path=docs/folder_structure.md kind=replace -->

**5u.2** — `docs/DECISION_LOG.md` line + suite caption. FIND:

````text
│   ├── STANDARDS_LOG.md           # this project's experiences log (contribution channel; kept file)
````

REPLACE WITH:

````text
│   ├── STANDARDS_LOG.md           # this project's experiences log (contribution channel; kept file)
│   ├── DECISION_LOG.md            # operator decisions — one DL-NNN entry each, verbatim answer (CLAUDE.md § 10; from Set v2.8)
````

<!-- block id=5u.3 path=docs/folder_structure.md kind=replace -->

**5u.3** — suite caption + template LESSONS caption. FIND:

````text
│   ├── standards/                 # canonical domain-neutral suite (Set Version v2.0)
│   │   ├── CLAUDE.md             # operating-contract TEMPLATE (with placeholders)
│   │   ├── LESSONS.md            # lessons archive (canonical template, L001–L067)
│   │   ├── CICD_STANDARDS.md
````

REPLACE WITH:

````text
│   ├── standards/                 # canonical domain-neutral suite (Set Version v2.8)
│   │   ├── CLAUDE.md             # operating-contract TEMPLATE (with placeholders)
│   │   ├── LESSONS.md            # lessons archive (canonical template, L001–L089)
│   │   ├── CICD_STANDARDS.md
│   │   ├── DECISION_LOG.md       # decision-log TEMPLATE (vault-only until a later Set Version delivers it)
````

<!-- §5-GENERATED:END -->

## 6. Spec update map (mechanical rules)

**Commit 1 (release, Phase 3a):**

1. **`docs/documents_manifest.md`:** set the version cell of every file § 5 bumps, found BY PATH (the
   row numbers are not relied on): `CLAUDE.md` 1.10, `docs/folder_structure.md` 0.19,
   `docs/SESSION_OPENER.md` 1.22, `docs/SESSION_CLOSER.md` 1.9, `docs/SET_VERSION_ADOPTED.md` 1.16,
   `docs/standards/CLAUDE.md` 1.8, `docs/standards/LESSONS.md` 1.3, `docs/standards/PROJECT_STANDARDS.md`
   1.2, `docs/standards/PROMPT_STANDARDS.md` 1.1, `docs/standards/MEMORY_PROTOCOL.md` 1.2,
   `docs/standards/ENGINEERING_STANDARDS.md` 1.1, `docs/standards/CICD_STANDARDS.md` 1.1,
   `docs/standards/SESSION_OPENER.md` 1.9, `docs/standards/SESSION_CLOSER.md` 1.8,
   `docs/standards/README.md` 1.6, `docs/standards/STANDARDS_INDEX.md` 2.8, `archive/LESSONS.md` 1.1,
   `skill/modes/bootstrap.md` 0.4, `skill/modes/adopt.md` 0.5; this plan + tracker → 0.3 (titles
   `(APPROVED)` → `(EXECUTING)`). Append two rows after the last row: `Decision Log — template (meta)` |
   0.1 | Standards | `docs/standards/DECISION_LOG.md`, and `Decision Log — operator decisions` | 1.0 |
   Governance | `docs/DECISION_LOG.md`; quick-index: the template's number joins "Canonical standards
   suite" (its stale caption "Set v2.0" → "Set v2.8"), the vault log's joins "Operating contract +
   project docs".
   Self-row 5 + header → next version; a new top CHANGE LOG line; the `## Last updated` block rotated.
   Then run harness 8d → `SUMMARY CLEAN` (it fails on any stale or empty cell and on an unlisted
   `docs/*.md` / `docs/standards/*.md` file — on the § 5-applied tree before this rule it reports exactly
   21 failures: 19 cells + the 2 new files).
2. **`docs/DECISION_LOG.md`:** add one entry per Phase 2 answer (D20, D-1, D-2, D-3, D-4) above DL-009,
   newest first (DL-010 …), each quoting the operator's reply verbatim from § 9.1; § 9.1 cites the ids.
   The file stays 1.0 (its creation commit).
3. **`CHANGELOG.md`:** a new top entry `## [<P3-DATE>] — Standard Set Version v2.8: lessons batch,
   senior-review checklist, template fixes, decision-log template (PLAN-020)` — Type, What changed (per
   file group), Intake (DL ids), Versions, Impact ("no engine change; adopters receive a 10-item delta at
   their next sync"), and a `### QA scenarios` sub-section listing QA-V1…V8 with their results so far
   (Rule 11).
4. **This plan + tracker:** → 0.3 EXECUTING; § 4 Phase 3a ✅; tracker sub-tasks with evidence.

**Commit 2 (delivery record + close, Phase 3b):**

5. **Tracker:** the per-project delivery results (QA-V6) → 1.0 CLOSED. **This plan:** → 1.0, Status
   `CLOSED — <P3-DATE>`, § 4 Phases 3b + 4 ✅ (Phase 5 stays ⏸ until the push). **Manifest:** plan + tracker
   cells → 1.0, titles `(CLOSED)`; self-row + Last updated. **CHANGELOG:** a delivery entry (what each
   project received, its handoff, the re-run, `status`).

**Outside the commits:**

6. **`docs/Plans/OPEN_TASKS.md`** (gitignored): the v2.8 block → done; delete every lesson candidate now
   codified (sessions 3–9 + older items mapped in § 2); keep the "Right after v2.8" list as NEXT.
7. **Phase 5 (operator "push"):** governance → `git push origin master` + `git push github master` →
   `git tag -a set-v2.8 <commit-1-sha> -m "Standard Set Version v2.8"` → `git push origin set-v2.8` +
   `git push github set-v2.8` → `git ls-remote` both: master == HEAD, tag == commit 1.

## 7. ALLOWLIST (the bullet enumeration IS the count — L038; plan + tracker included per L054)

### 7.1 Commit 1 — release (Phase 3a) — 25 files

- `docs/standards/LESSONS.md`
- `docs/standards/CLAUDE.md`
- `docs/standards/SESSION_OPENER.md`
- `docs/standards/SESSION_CLOSER.md`
- `docs/standards/MEMORY_PROTOCOL.md`
- `docs/standards/PROMPT_STANDARDS.md`
- `docs/standards/CICD_STANDARDS.md`
- `docs/standards/ENGINEERING_STANDARDS.md`
- `docs/standards/PROJECT_STANDARDS.md`
- `docs/standards/STANDARDS_INDEX.md`
- `docs/standards/README.md`
- `docs/standards/DECISION_LOG.md` (new)
- `skill/modes/bootstrap.md`
- `skill/modes/adopt.md`
- `CLAUDE.md`
- `archive/LESSONS.md`
- `docs/SESSION_OPENER.md`
- `docs/SESSION_CLOSER.md`
- `docs/SET_VERSION_ADOPTED.md`
- `docs/DECISION_LOG.md` (new)
- `docs/folder_structure.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`
- `docs/Plans/PLAN-020_set_v2_8.md`
- `docs/Plans/PLAN-020_tracker.md`

### 7.2 Commit 2 — delivery record + close (Phase 3b) — 4 files

- `docs/Plans/PLAN-020_set_v2_8.md`
- `docs/Plans/PLAN-020_tracker.md`
- `docs/documents_manifest.md`
- `CHANGELOG.md`

Anything else in `git status --short` → STOP and report (Rule 6). `docs/fleet.csv` is gitignored.
The project writes in Phase 3b land in THEIR trees (handoff + their own landing commit), never here.

## 8. Validation gate (Rule 11 scenarios; Rule 15 feature-ON marked ⚑; status in the tracker)

Python = the vault's `.venv/bin/python`. Harnesses 8b, 8c, 8d are extracted from this file into the
session scratchpad (`kind=harness` blocks) and run with `-I`.

- **QA-V1 — apply.** 67 blocks re-extracted from this file; every FIND exactly once in order, both
  creates new → CLEAN; corrupted-FIND control → exactly that block FAILs; afterwards no `<P3-DATE>` in
  the 21 files.
- **QA-V2 — domain-neutral gate.** `grep -rniE
  "780|estimator|everon|equinex|capital-signal|bahereh|parsaazad|a780|yaserkhosravi|mql5|hetzner|metatrader|graphify|dropbox"
  docs/standards/ skill/ scripts/claude_project_data.sh` → no output (exit 1). Control: the same grep on
  a scratch copy with one planted project name → exactly that hit.
- **QA-V3 — structure.** Harness 8b on the vault → `SUMMARY CLEAN` (TOC anchors resolve in both
  LESSONS files, every fence closed in the 21 files, 16 INDEX § 3 rows == file headers, 89 lesson
  headings). Control: a scratch copy with a broken anchor, a stale INDEX cell and an unclosed fence →
  three FAILs.
- **QA-V4 ⚑ — engine as oracle, on copies** (never the real projects). Harness 8c with the vault in
  `delta` mode over copies of the four reachable projects (three local folders + a fresh shallow clone of
  the git project) → `SUMMARY pass=13 fail=0`: each copy exactly the 10-item delta; after `--write` on the
  copies the merged `CLAUDE.md` keeps every PROJECT-OWNED block, has no `TEMPLATE-ONLY` text, no
  Project Instructions template reference below its header, and carries the § 15.8 checklist; a re-run
  reports up-to-date. Baseline: the same copies against an export of the pre-release commit in
  `uptodate` mode → `pass=5 fail=0`. Control: that export in `delta` mode → FAILs.
- **QA-V5 — governance + manifest.** `python scripts/check_doc_coverage.py` and `python
  scripts/check_test_coverage_drift.py --ci` → exit 0, stdout pasted verbatim (Rule 6); harness 8d →
  `SUMMARY CLEAN` (before the § 6 rule 1 edits it reported 21 failures — its control).
- **QA-V6 ⚑ — delivery to the reachable projects** (Phase 3b, after commit 1). For each project, as
  separate steps (L084): (a) idle evidence shown to the operator — for the three local projects the
  newest session-transcript time in their `.claude/project-data/` and any Claude process whose working
  folder is theirs; the git project needs none (a concurrent push makes the write fail, never
  overwrite); (b) operator "go"; (c) `sync --project NAME --write` → "10 of 11", the handoff written or
  appended; (d) dry-run re-run → up-to-date. Then `status` → the four at `v2.8 v2.8 current`;
  780-Automation `unknown` (recorded; catch-up when reachable). A project the operator holds is recorded
  as held, not written.
- **QA-V7 — the decision log in use.** After § 6 rule 2: `docs/DECISION_LOG.md` holds DL-001 … DL-009
  plus one entry per Phase 2 answer, each with a verbatim quoted answer and a date; § 9.1 cites the ids;
  harness 8b's fence check passes on it.
- **QA-V8 — the skill change (D-2).** Mechanical: the engine's own `strip_template_only` on the template
  `CLAUDE.md` removes the curator note and leaves the § 12 table rows contiguous; `bootstrap.md` /
  `adopt.md` name the TEMPLATE-ONLY deletion. Real-run evidence per D-3.

<!-- block id=8b path=qa_struct.py kind=harness -->
````python
"""PLAN-020 QA-V3 — structure checks on a vault tree: TOC anchors, fence balance, INDEX § 3 cells ==
file headers, lesson count. Usage: python -I qa_struct.py <vault-root>. Exit 1 on any failure; an empty
value is a failure, never a match."""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
fails = 0


def slug(h: str) -> str:
    return re.sub(r"[^\w\- ]", "", h.strip().lower()).replace(" ", "-")


def bad(msg: str) -> None:
    global fails
    fails += 1
    print("FAIL", msg)


for rel in ["docs/standards/LESSONS.md", "archive/LESSONS.md"]:
    t = (root / rel).read_text(encoding="utf-8")
    heads = {slug(h) for h in re.findall(r"^#{2,4} (.+)$", t, re.M)}
    links = re.findall(r"^ - \[[^\]]+\]\(#([^)]+)\)", t, re.M)
    if not links:
        bad(f"{rel}: no TOC links found")
    miss = [a for a in links if a not in heads]
    for a in miss:
        bad(f"{rel}: TOC anchor not found: {a}")
    print(f"{'OK  ' if links and not miss else 'FAIL'} {rel}: {len(links)} TOC links")

CHANGED = [f"docs/standards/{f}" for f in (
    "LESSONS.md", "CLAUDE.md", "SESSION_OPENER.md", "SESSION_CLOSER.md", "MEMORY_PROTOCOL.md",
    "PROMPT_STANDARDS.md", "CICD_STANDARDS.md", "ENGINEERING_STANDARDS.md", "PROJECT_STANDARDS.md",
    "STANDARDS_INDEX.md", "README.md", "DECISION_LOG.md")] + [
    "skill/modes/bootstrap.md", "skill/modes/adopt.md", "CLAUDE.md", "archive/LESSONS.md",
    "docs/SESSION_OPENER.md", "docs/SESSION_CLOSER.md", "docs/SET_VERSION_ADOPTED.md",
    "docs/DECISION_LOG.md", "docs/folder_structure.md"]
for rel in CHANGED:
    open_fence = ""
    for ln in (root / rel).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(`{3,})", ln)
        if not m:
            continue
        if not open_fence:
            open_fence = m.group(1)
        elif ln.strip() == open_fence:
            open_fence = ""
    if open_fence:
        bad(f"{rel}: unclosed fence {open_fence!r}")
print(f"fences checked in {len(CHANGED)} files")

idx = (root / "docs/standards/STANDARDS_INDEX.md").read_text(encoding="utf-8")
rows = re.findall(r"^\| `([A-Z_]+\.md)` \| (?:Binding|Meta) \| ([0-9.]*) \| ([0-9-]*) \|$", idx, re.M)
if len(rows) != 16:
    bad(f"INDEX § 3: {len(rows)} rows parsed, expected 16")
for f, ver, date in rows:
    t = (root / "docs/standards" / f).read_text(encoding="utf-8")
    hv = re.search(r"<!-- VERSION: ([0-9.]+) -->", t)
    hd = re.search(r"<!-- Last Updated: ([0-9-]+) -->", t)
    hv_s, hd_s = (hv.group(1) if hv else ""), (hd.group(1) if hd else "")
    if not (ver and hv_s and ver == hv_s and date and hd_s and date == hd_s):
        bad(f"INDEX row {f}: cell {ver!r}/{date!r} vs header {hv_s!r}/{hd_s!r}")
print(f"INDEX § 3: {len(rows)} rows checked")
lessons = (root / "docs/standards/LESSONS.md").read_text(encoding="utf-8")
n = len(re.findall(r"^### L0\d\d — ", lessons, re.M))
print("lesson headings:", n)
if n != 89:
    bad(f"lesson count {n} != 89")
print("SUMMARY", "CLEAN" if not fails else f"{fails} FAILURE(S)")
sys.exit(1 if fails else 0)
````

<!-- block id=8c path=qa_oracle.py kind=harness -->
````python
"""PLAN-020 QA-V4 — engine as oracle on COPIES of the targets (never the real ones).

Usage: python -I qa_oracle.py <vault-tree> <scratch-dir> <mode> <target-dir>...
  mode = uptodate : the vault tree's dry-run must report every copy up-to-date (baseline / control)
  mode = delta    : dry-run must report exactly DELTA for every copy; --write on the copies; the
                    merged CLAUDE.md is checked; a re-run must report up-to-date (idempotence)
Copies docs/ + archive/ + CLAUDE.md of each target into <scratch-dir>; writes a scratch registry
inside a scratch copy of the vault tree; runs the vault tree's own engine (src/). Prints PASS/FAIL
lines and SUMMARY.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

DELTA = {
    "merge   CLAUDE.md", "replace docs/standards/PROJECT_STANDARDS.md",
    "replace docs/standards/PROMPT_STANDARDS.md", "replace docs/standards/MEMORY_PROTOCOL.md",
    "replace docs/standards/ENGINEERING_STANDARDS.md", "replace docs/standards/CICD_STANDARDS.md",
    "replace archive/LESSONS.md", "merge   docs/SESSION_OPENER.md",
    "merge   docs/SESSION_CLOSER.md", "record  docs/SET_VERSION_ADOPTED.md",
}
RESULTS: list[bool] = []


def check(name: str, ok: bool, detail: str) -> None:
    RESULTS.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}")


def run_sync(vault: Path, *extra: str) -> str:
    code = (f"import sys; sys.path.insert(0, {str(vault / 'src')!r}); "
            "from standard_document_updater.cli import main; "
            f"sys.exit(main(['--vault', {str(vault)!r}, 'sync', *{list(extra)!r}]))")
    p = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True,
                       timeout=300, check=False)
    return p.stdout + p.stderr


def per_target(out: str) -> dict[str, list[str]]:
    rows: dict[str, list[str]] = {}
    cur = ""
    for ln in out.splitlines():
        m = re.match(r"^\[(.+?)\] ", ln)
        if m:
            cur = m.group(1)
            rows[cur] = [ln]
        elif cur and ln.startswith("  "):
            rows[cur].append(ln)
    return rows


def main() -> None:
    src_vault, scratch, mode = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    targets = [Path(t) for t in sys.argv[4:]]
    if scratch.exists():
        shutil.rmtree(scratch)
    vault = scratch / "vault"
    shutil.copytree(src_vault, vault, ignore=shutil.ignore_patterns(".git", ".venv", "__pycache__"))
    reg = []
    for t in targets:
        dest = scratch / "targets" / t.name
        dest.mkdir(parents=True)
        for part in ("docs", "archive", "CLAUDE.md"):
            s = t / part
            (shutil.copytree if s.is_dir() else shutil.copy2)(s, dest / part)
        reg.append(f'[[project]]\nname = "{t.name}"\npath = "{dest}"\n')
    (vault / "config" / "projects.toml").write_text("\n".join(reg), encoding="utf-8")
    out = run_sync(vault)
    rows = per_target(out)
    check("dry-run covers every copy", sorted(rows) == sorted(t.name for t in targets),
          f"{len(rows)} of {len(targets)} targets reported")
    for t in targets:
        lines = rows.get(t.name, [""])
        if mode == "uptodate":
            check(f"{t.name} up-to-date", "up-to-date" in lines[0], lines[0].strip())
            continue
        got = {re.sub(r"^\s+changed ", "", ln) for ln in lines[1:] if "changed" in ln}
        check(f"{t.name} delta", got == DELTA, f"{len(got)} changed; extra={sorted(got - DELTA)} "
              f"missing={sorted(DELTA - got)}")
    if mode == "delta":
        before = {t.name: (t / "CLAUDE.md").read_text(encoding="utf-8").count("PROJECT-OWNED:BEGIN")
                  for t in targets}
        run_sync(vault, "--write")
        for t in targets:
            merged = (scratch / "targets" / t.name / "CLAUDE.md").read_text(encoding="utf-8")
            body = merged[merged.find("-->", merged.find("CHANGE LOG")) + 3:]  # below the header
            ok = ("TEMPLATE-ONLY" not in merged
                  and "PROJECT_INSTRUCTIONS_TEMPLATE" not in body
                  and merged.count("PROJECT-OWNED:BEGIN") == before[t.name]
                  and "**Checklist the pass walks**" in merged
                  and "Closeout_Mode" not in merged)
            check(f"{t.name} merged CLAUDE.md", ok,
                  f"PO {merged.count('PROJECT-OWNED:BEGIN')}/{before[t.name]}, "
                  f"TO {merged.count('TEMPLATE-ONLY')}, checklist "
                  f"{merged.count('**Checklist the pass walks**')}")
        again = per_target(run_sync(vault))
        for t in targets:
            first = again.get(t.name, [""])[0]
            check(f"{t.name} idempotent", "up-to-date" in first, first.strip())
    print(f"SUMMARY pass={RESULTS.count(True)} fail={RESULTS.count(False)}")
    sys.exit(0 if all(RESULTS) else 1)


if __name__ == "__main__":
    main()
````

<!-- block id=8d path=qa_cells.py kind=harness -->
````python
"""PLAN-020 QA-V5 — manifest check (L063): every manifest row's version cell == its file's header.

Usage: python -I qa_cells.py <vault-root>. A row whose file is missing FAILs; a row whose file has no
VERSION header must show "-"; an empty cell FAILs. The self-row (the manifest itself) is checked like
any other row. Every docs/*.md and docs/standards/*.md file must appear in a row.
"""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
manifest = (root / "docs/documents_manifest.md").read_text(encoding="utf-8")
rows = re.findall(r"^\| (\d+) \| .*? \| ([^|]*?) \| [^|]+ \| `([^`]+)` \|$", manifest, re.M)
fails = 0


def bad(msg: str) -> None:
    global fails
    fails += 1
    print("FAIL", msg)


if not rows:
    bad("no manifest rows parsed")
for n, cell, rel in rows:
    f = root / rel
    if not f.is_file():
        bad(f"row {n} {rel}: file missing")
        continue
    m = re.search(r"VERSION: ([0-9.]+)", f.read_text(encoding="utf-8", errors="replace"))
    head = m.group(1) if m else "-"
    if not cell or cell != head:
        bad(f"row {n} {rel}: cell {cell!r} != header {head!r}")
listed = {rel for _, _, rel in rows}
for f in sorted([*(root / "docs/standards").glob("*.md"), *(root / "docs").glob("*.md")]):
    rel = f.relative_to(root).as_posix()
    if rel not in listed:
        bad(f"unlisted: {rel}")
print(f"{len(rows)} rows checked; SUMMARY {'CLEAN' if not fails else f'{fails} FAILURE(S)'}")
sys.exit(1 if fails else 0)
````

## 9. Operator decision points (Phase 2 — answer with the approval)

Asked in plain words (`feedback_plain_language_decisions`). Reply on one line, e.g. **"approve 020, all A"**.

- **D20 — approve PLAN-020?** A — approve as written / B — revise first.
- **D-1 — where the vault's decision-log rule lives.** The vault's sessions need a rule that says
  "record every decision in `docs/DECISION_LOG.md`". **A (recommended):** a short sub-section in
  CLAUDE.md § 10 (AI behavior rules) — no new rule number, so nothing renumbers when projects get the
  same rule in PLAN-021. **B:** a new standing Rule 17 in the vault only — more prominent, but the vault's
  rule numbers would then drift further from the template's, which projects use.
- **D-2 — fix the skill now so the curator-only note never reaches a new project.** The § 12 line about
  the Project Instructions template becomes a hidden-from-projects note. Sync already strips such notes,
  but the skill's bootstrap / adopt modes don't — so a project set up before the fix would carry the note
  in its CLAUDE.md until its first sync. **A (recommended):** include two small skill edits in this plan
  (5m, 5n). **B:** leave it for the separate skill change — a project set up in between shows the note
  until its first sync (harmless, self-healing).
- **D-3 — proving the skill change in a real run (Rule 15).** The new skill lines run only when someone
  bootstraps, adopts or self-tests a project. **A (recommended):** waive the real-run proof until the
  next real use (the next bootstrap / adopt / selftest report is the evidence), keeping the mechanical
  check QA-V8 — the effect of a miss is cosmetic and sync removes it. **B:** make it ship-gating — after
  the push, you run the selftest launcher on this Mac (about 5 minutes) before the plan closes.
- **D-4 — deliver v2.8 to the projects in the same session.** **A (recommended):** yes — after the
  release commit, for each reachable project I show you its idle evidence, you say "go", I write and
  re-check (QA-V6); 780-Automation catches up when its host answers. **B:** release only; deliver later
  (the plan stays open until then).

## 10. Rollback path

`git revert` of commit 2 then commit 1 restores the v2.7 suite and the vault's own files; delete the
`set-v2.8` tag if pushed (`git push --delete`). Projects already written: each holds a handoff; a project
that has not landed it discards the engine-written files (`git checkout -- <files>` + delete the
handoff); a landed project reverts its landing commit — or the curator re-syncs from the reverted vault,
which rewrites the v2.7 content (merge and replace are content-driven).

## 11. Known risks + mitigation

- **R1 — a project session active during the write** (two machines share the folder): idle evidence is
  its own step, shown to the operator before each write (L084); the operator can hold a project.
- **R2 — the git project's `main` moved** between clone and push: the push is fast-forward only, so it
  fails and nothing is overwritten; re-run.
- **R3 — a project with an un-landed earlier write:** the handoff accumulates (PLAN-013); none holds one
  today (`handoff_pending` 0 at session open).
- **R4 — the decision-log rule is vault-only until PLAN-021** — projects do not record decisions yet
  (accepted, DL-008).
- **R5 — consolidating ~25 data points into seven lessons loses detail:** the vault archive's provenance
  table (5p.3) keeps every source per lesson.
- **R6 — 780-Automation stays at v2.7** until its host answers; the catch-up write is one command (and
  its 12 open log entries get their own Rule 16 gate).
- **R7 — the engine's sync handoff names "Set Version v2.8"** while the tag is pushed only at Phase 5 —
  the order matches v2.7 (delivered, then pushed).

## 12. Acceptance criteria

1. The 67 § 5 blocks apply clean; no `<P3-DATE>` left (QA-V1).
2. Zero domain-neutral hits in the suite, the skill and the delivered script (QA-V2).
3. Structure clean: anchors, fences, INDEX cells, 89 lessons (QA-V3).
4. The engine delivers exactly the 10-item delta to every reachable project, keeps every PROJECT-OWNED
   block, and is idempotent — on copies (QA-V4 ⚑) and live (QA-V6 ⚑).
5. Governance exit 0 / 0; every manifest cell == its file header; both new files registered (QA-V5).
6. The vault's decision log holds every 2026-10-12 decision verbatim, Phase 2 answers included (QA-V7).
7. Bootstrap / adopt instructions delete `TEMPLATE-ONLY` blocks from CLAUDE.md (QA-V8; real run per D-3).
8. `docs/architecture.md` unchanged — no engine behavior changes (the § 4 drift rule does not fire).

## Rule 13 senior-review pass

Run once on the complete plan + tracker with the § 15.8 prompt; every tool ran on the text EXTRACTED from
this file (L051, L083). § 5 + the three harnesses parsed back onto a fresh export of `9366b7a` → 70 / 70
blocks clean (67 edits + 3 harnesses); the resulting tree byte-identical to the proven scratch copy (21
files); harnesses 8c / 8d byte-identical to the proven scripts. On the extracted tree: domain-neutral
gate no output; harness 8b CLEAN (control: broken anchor + stale INDEX cell + unclosed fence → 3 FAILs);
harness 8c `delta` 13 / 13, baseline `uptodate` 5 / 5, control 2 FAILs; harness 8d 21 failures before
§ 6 rule 1 and CLEAN (96 rows) after a simulation of rule 1 — the rule's list is complete; QA-V8 — the
engine's `strip_template_only` leaves the § 12 table's 11 rows contiguous and no template-file reference.
The real project folders were only read (their `CLAUDE.md` times unchanged, no handoff written).

Found + fixed in the pass:

1. **Harness 8d failed `ruff`** (semicolon statements, a combined import) → rewritten clean, re-embedded,
   re-proven (HEAD 94 rows CLEAN; § 5-applied tree 21 failures; after rule 1 CLEAN).
2. **§ 6 rule 1 named quick-index rows that do not exist** ("Standards / Governance") → now the real rows,
   plus the stale "Set v2.0" caption on the standards row.
3. **Harness 8b's fence check was simplified for the plan** (one open-fence variable instead of a stack)
   → re-proven on the extracted text with the three-defect control.

Caught while drafting, before the pass (the proving loop working): six FINDs that ended mid-line — every
body ends in a newline, so a FIND must be whole lines (5b.3, 5b.8, 5c.3, 5e.2, 5f.3, 5s.3); two wrong
section numbers in change-log lines (MEMORY_PROTOCOL § 4.6, CICD § 11.4); "ten times in ten days" in L082
contradicted its own June data point → reworded.

Checked, no change: § 1 ↔ § 5 ↔ § 6 ↔ § 7 ↔ § 8 ↔ § 12 consistent (§ 7.1's 25 files = the 21 files § 5
writes + manifest + CHANGELOG + plan + tracker); the template's own header line still contains the word
`TEMPLATE-ONLY` — harmless (sync keeps each project's header; bootstrap resets it); no hedge words (Rule
7). **New design decisions surfaced** (not decided silently): D-1 (where the vault's decision-log rule
lives), D-2 (the two skill lines), D-3 (Rule 15 for the skill change), D-4 (delivery in the same session)
— § 9.
