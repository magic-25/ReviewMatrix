# Contributing

Thanks for helping improve Role Review Matrix. This project is a Codex skill family, so contributions should keep the skills usable, predictable, and easy to validate.

## Local Checks

Run these before opening a PR:

```bash
python3 scripts/validate_skill_family.py
python3 scripts/generate_roles.py
git diff --exit-code
```

## Contribution Types

### Improve an existing role

Update the role source in `skills/role-review-matrix/references/role-registry.json`, then run:

```bash
python3 scripts/generate_roles.py
python3 scripts/validate_skill_family.py
```

Do not edit generated role `SKILL.md` files by hand unless you are also updating the generator.

### Add a new role

Before adding a role, check whether an existing role can cover the need through a clearer boundary, trigger, or memory update. New roles should be reusable across more than one review.

A registry entry must include:

- `slug`
- `name`
- `group`
- `description`
- `applies_to`
- `triggers`
- `boundary`
- `review_focus`
- `evidence_needs`
- `conflicts_with`

### Update memory

Role memory lives in `skills/roles/<role>/memory.md`. Treat memory as experience, not permanent law. Candidate improvements should stay provisional until they are stable enough to become a skill rule.

If installed memory evolves locally in `~/.codex/skills/<role>/memory.md`, copy it back intentionally:

```bash
cp ~/.codex/skills/product-manager/memory.md skills/roles/product-manager/memory.md
git diff -- skills/roles/product-manager/memory.md
```

Review the diff before committing memory changes.

## Pull Requests

PRs should include:

- What changed.
- Why it changed.
- Which roles or references are affected.
- Validation commands and results.
- Whether memory files changed.

Keep changes focused. A role addition, generator change, and documentation rewrite should usually be separate PRs.
