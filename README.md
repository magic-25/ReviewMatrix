# Role Review Matrix

Role Review Matrix is a Codex skill family for professional multi-role review across AI-native software products and adjacent product work.

The repository is the source of truth. Installed Codex skills are synchronized from this repository into `~/.codex/skills`.

## What It Provides

- `role-review-matrix`: the orchestration skill for stage-aware review.
- `role-creator`: the skill for drafting missing professional review roles.
- `skills/roles/*`: individual role skills with consistent review protocols.
- `memory.md` files: role experience stores that are separate from permanent skill rules.
- Validation and sync scripts.

## Quick Start

During staged development, validation and sync become fully usable after the skill source tree has been generated. Until then, validation may fail on the next missing planned file and sync may report missing source skill directories.

Validate the repository:

```bash
python3 scripts/validate_skill_family.py
```

Preview installation:

```bash
./scripts/sync_to_codex_skills.sh --dry-run
```

Install or update skills:

```bash
./scripts/sync_to_codex_skills.sh
```

## Installation

The sync script mirrors these source directories into `~/.codex/skills`:

- `skills/role-review-matrix`
- `skills/role-creator`
- every directory under `skills/roles`

During sync, non-source files inside installed skill directories are removed to match the repository. Existing installed `memory.md` files are preserved by default. To replace installed memory files from the repository, run:

```bash
./scripts/sync_to_codex_skills.sh --overwrite-memory
```

## Memory Backflow

Installed role memory can evolve in `~/.codex/skills/<role>/memory.md` while repository memory stays unchanged. To sync installed memory back into the repository, copy the installed role memory into the matching source role directory, review the diff, then commit it:

```bash
cp ~/.codex/skills/product-manager/memory.md skills/roles/product-manager/memory.md
git diff -- skills/roles/product-manager/memory.md
```

Only sync installed memory back after reviewing it. Candidate improvements should stay provisional until you decide they are stable enough to become repository memory or a skill upgrade.

## Safety Model

- The matrix can recommend role memory updates, but it does not automatically rewrite skill files.
- Role upgrades require explicit user approval.
- Missing roles are first represented as temporary role views.
- `role-creator` drafts new role skills; it does not install them without confirmation.
- External web research is not performed unless the user explicitly asks for it.

## Repository Layout

```text
skills/
  role-review-matrix/
  role-creator/
  roles/
scripts/
docs/
  superpowers/
    specs/
    plans/
```

## Verification

Before installing, run:

```bash
python3 scripts/validate_skill_family.py
./scripts/sync_to_codex_skills.sh --dry-run
```

After installing, restart Codex or open a new Codex session so newly installed skills can be discovered.

To keep local role experience, do not pass `--overwrite-memory`.
