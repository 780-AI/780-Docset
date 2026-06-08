# standard-document-updater

A domain-neutral CLI tool that keeps **standards / governance documentation suites** up to date and
synchronized across any project it is given access to.

It reads a canonical standards suite (the "source"), compares it against one or more adopting
project repositories (the "targets"), and helps propagate updates — per-file `VERSION` headers,
`CHANGE LOG` entries, the documents manifest, and the `STANDARDS_INDEX` Set-Version state — under
the explicit-backport discipline the suite itself defines. It is not tied to any single project's
domain; the projects it operates on are inputs, supplied at runtime.

> Status: **bootstrapped** (governance scaffold in place). The engine is not yet implemented — that
> is the next milestone. See `docs/Plans/` and `CHANGELOG.md`.

## Quick start

```bash
# (once the engine lands)
python -m standard_document_updater --help
```

Until the engine exists, this repository is a governed, empty project: the operating contract,
standards suite, governance scripts, and CI scaffold are in place so that all feature work follows
the same discipline from the first commit.

## How it's organized

- `CLAUDE.md` — the binding operating contract (read first; 13 standing rules).
- `docs/standards/` — the adopted standards suite (Standard Set Version v1.0) + `SET_VERSION_ADOPTED.md`.
- `docs/SESSION_OPENER.md` / `docs/SESSION_CLOSER.md` — binding session start/end routines (Rules 9 & 12).
- `docs/documents_manifest.md` — the version index of every tracked doc and code file.
- `docs/folder_structure.md` — the authoritative layout.
- `docs/Plans/` — committed planning documents (per Rule 1).
- `scripts/` — governance scripts (run before every push, per Rule 2).
- `archive/LESSONS.md` — the incident-to-rule archive (49 lessons).

## Standards

This project was bootstrapped from the standards suite at **Standard Set Version v1.0**
(see `docs/standards/SET_VERSION_ADOPTED.md`). The binding contract is `CLAUDE.md` at the repo root.
Backports from the standards source are explicit — see `docs/standards/STANDARDS_INDEX.md` § 4.3.
