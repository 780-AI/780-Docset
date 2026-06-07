## Summary

<one-line description>

## Change classification

- [ ] Minor — bug fix / refactor / docs / lint
- [ ] Major — domain logic / new module / public API (CLI flags) / CI structure / critical file (incl. `CLAUDE.md`, `docs/documents_manifest.md`, anything under `docs/standards/`, or `src/standard_document_updater/`)

## Sync checklist (per `docs/standards/PROJECT_STANDARDS.md` § 4)

- [ ] VERSION header bumped on every touched `.py` / `.sh` / tracked `.md` (per `CLAUDE.md` § 7)
- [ ] CHANGE LOG line added in each touched file's header
- [ ] `docs/documents_manifest.md` updated (version cells + Last Updated rotation)
- [ ] `CHANGELOG.md` entry added at top with explicit impact statement
- [ ] If engine behavior changed: `docs/architecture.md` updated in the same commit (per `CLAUDE.md` § 4 drift rule)
- [ ] Source-of-truth doc updated if behavior changed elsewhere
- [ ] Tracker file updated if Phase/Task work
- [ ] Code review pass on all touched files BEFORE staging (per `CLAUDE.md` Rule 10 / § 8.5)
- [ ] QA / smoke-test scenario paired with any behavior-affecting change (per `CLAUDE.md` Rule 11)

## Pre-push governance

- [ ] `python scripts/check_doc_coverage.py` exits 0
- [ ] `python scripts/check_test_coverage_drift.py --ci` exits 0
- [ ] Output pasted verbatim below

```
<paste verbatim stdout here>
```

## Test plan

<Bulleted checklist of how to verify this change — CLI command + flags, fixtures / sample target repo, expected output.>

## Impact statement

- [ ] No runtime impact
- [ ] Behavior change — describe what changes and how to verify
- [ ] CI/CD change — first pipeline run will be the dispositive validation (per `CLAUDE.md` Rule 5)
