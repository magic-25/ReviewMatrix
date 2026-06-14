# Memory Model

Role Review Matrix separates stable rules from evolving experience.

## `SKILL.md`

`SKILL.md` contains stable role instructions:

- Role boundary.
- Evidence to inspect.
- Review focus.
- Conflict and overlap guidance.
- Output contract.

These files are generated from the registry and should remain predictable.

## `memory.md`

`memory.md` contains experience:

- Stable lessons.
- Candidate improvements.
- Review patterns.
- Upgrade proposals.

Role skills read `memory.md` before reviewing. Candidate improvements are provisional until a user approves a skill upgrade.

## Installed Memory

Installed memory can evolve in:

```text
~/.codex/skills/<role>/memory.md
```

The sync script preserves installed memory by default. This prevents local experience from being overwritten during updates.

## Repository Memory

Repository memory lives in:

```text
skills/roles/<role>/memory.md
```

To promote installed memory back to the repository, copy it intentionally and review the diff:

```bash
cp ~/.codex/skills/product-manager/memory.md skills/roles/product-manager/memory.md
git diff -- skills/roles/product-manager/memory.md
```

Only commit memory after reviewing whether it should remain memory or become a permanent role rule.
