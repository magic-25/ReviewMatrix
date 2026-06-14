# Role Authoring Guide

Role Review Matrix works best when each role has a durable professional boundary. A role should represent a perspective that can find decision-relevant risks across many reviews.

## Good Roles

A good role:

- Has a clear professional perspective.
- Needs specific evidence.
- Can produce findings that change a gate decision.
- Has known overlaps or conflicts with other roles.
- Is useful in more than one artifact or project.

Examples:

- `security-reviewer`
- `evaluation-engineer`
- `sales-gtm-reviewer`

## Weak Roles

A weak role:

- Exists for only one artifact.
- Duplicates an existing role.
- Mixes unrelated perspectives.
- Has no clear evidence needs.
- Produces generic advice that cannot affect a decision.

## Adding Roles

Add roles through `skills/role-review-matrix/references/role-registry.json`. Then regenerate role skills:

```bash
python3 scripts/generate_roles.py
python3 scripts/validate_skill_family.py
```

Do not hand-edit generated role `SKILL.md` files unless you are changing the generator.

## Avoiding Role Explosion

Before adding a role, ask:

- Can an existing role cover this with a memory update?
- Is this expertise reusable?
- Does it need distinct evidence?
- Will it create useful disagreement with other roles?
- Can it affect `pass`, `revise`, or `blocked`?

If the answer is mostly no, keep it as a temporary role view instead.
