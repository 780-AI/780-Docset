# Standard DocSet

A domain-neutral standards vault and CLI tool that keeps **standards / governance documentation
suites** up to date across the projects that adopt them.

It holds the canonical suite (`docs/standards/`), the delivery skill that sets a project up on it
(`skill/`), and the engine that keeps every registered project current afterwards
(`src/standard_document_updater/`). It is not tied to any single project's domain — the projects it
operates on are inputs, supplied at runtime.

## Use the standards — one prompt in Claude Code

You need: read access to this repository with an SSH key registered at its host, `git`, and Claude
Code (on Windows, Claude Code runs its commands in Git Bash). Nothing from this repository is
installed and nothing in it changes — Claude reads it from a clone in your home folder. Claude Code
asks before it runs a command; approve them.

**1. Test it first — changes nothing on your computer.** Open Claude Code in your home folder (not
inside a project) and send:

```text
Run the Standard DocSet self-test on this computer.

1. Clone git@github.com:780-AI/780-Docset.git into the new folder docset-selftest in my home folder (it is cloned for this self-test). If that folder already exists, stop and tell me.
2. Read skill/SKILL.md in that folder and follow it in selftest mode. The vault folder is that docset-selftest folder.
```

Claude works on its own (about 10 minutes), deletes everything it made, and leaves
`standard-docset-selftest-report-<time>.txt` on your Desktop. Send that file to the curator.

**2. Set up a project.** Open Claude Code in the project's folder and send:

```text
Set up the Standard DocSet standards for the project in this folder.

1. If the folder Standard-DocSet exists in my home folder, update it with git pull --ff-only; otherwise clone git@github.com:780-AI/780-Docset.git into that folder.
2. Read skill/SKILL.md in that folder and follow it. The vault folder is that Standard-DocSet folder; the project is the folder this session was opened in.
```

Claude asks a few questions about the project, one at a time, sets it up in one commit (it never
pushes), and leaves a handoff report on your Desktop. Send that file to the curator, who registers
the project — from then on, suite updates reach it without running this again.

A project that already carries the suite needs neither prompt: its updates come from the curator.

## For the curator

- `CLAUDE.md` — the binding operating contract; read it first.
- Engine: `python -m standard_document_updater {status,drift,fleet,harvest,integrate,sync}` —
  behavior in `docs/architecture.md`; the registry of projects is `config/projects.toml`.
- The current Standard Set Version and its history: `docs/standards/STANDARDS_INDEX.md`.
- `docs/SESSION_OPENER.md` / `docs/SESSION_CLOSER.md` — binding session start / end routines.
- `docs/documents_manifest.md` — the version index; `docs/folder_structure.md` — the layout.
- `docs/Plans/` — committed plans; `archive/LESSONS.md` — the incident-to-rule archive.
- A new machine: `docs/NEW_MACHINE_SETUP.md`.
