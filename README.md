# Role Review Matrix

Role Review Matrix is a Codex skill family for professional multi-role review across AI-native software products and adjacent product work.

The repository is the source of truth. Installed Codex skills are synchronized from this repository into `~/.codex/skills`.

## Use Cases

- Review product ideas, PRDs, architecture briefs, implementation diffs, test plans, launch plans, incident reviews, and GTM strategy.
- Select role reviewers dynamically from lifecycle stage and risk signals.
- Combine product, business, UX, engineering, AI-native, security, privacy, performance, reliability, legal, pricing, and market perspectives.
- Keep role experience in `memory.md` while stable role rules stay in `SKILL.md`.

## What It Provides

- `role-review-matrix`: the orchestration skill for stage-aware review.
- `role-creator`: the skill for drafting missing professional review roles.
- `skills/roles/*`: individual role skills with consistent review protocols.
- `memory.md` files: role experience stores that are separate from permanent skill rules.
- Validation and sync scripts.

## Quick Start

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

After installing, open a new Codex session so the skills can be discovered.

## Example Invocation

```text
Use role-review-matrix to review this PRD before implementation.
```

The matrix will infer the lifecycle stage, read relevant context, select roles, and produce a combined review with:

- Executive summary.
- `pass`, `revise`, or `blocked` gate decision.
- Highest-risk findings.
- Role-specific findings.
- Cross-role conflicts.
- Required actions.
- Candidate missing roles.
- Role evolution notes.

See [`examples/`](examples/) for sample inputs and outputs.

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
- Do not include secrets, `.env` contents, private customer data, or proprietary artifacts in issues, examples, or memory files.

## Repository Layout

```text
.github/
  workflows/
  ISSUE_TEMPLATE/
examples/
skills/
  role-review-matrix/
  role-creator/
  roles/
scripts/
docs/
  superpowers/
    specs/
  role-authoring.md
  memory-model.md
```

## Verification

Before installing, run:

```bash
python3 scripts/validate_skill_family.py
./scripts/sync_to_codex_skills.sh --dry-run
```

After installing, restart Codex or open a new Codex session so newly installed skills can be discovered.

To keep local role experience, do not pass `--overwrite-memory`.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). New role proposals should explain why existing roles are not enough and include lifecycle stages, evidence needs, and likely conflicts.

## Security

See [`SECURITY.md`](SECURITY.md). Do not disclose sensitive exploit details, credentials, customer data, or proprietary artifacts in public issues.

## License

MIT. See [`LICENSE`](LICENSE).
