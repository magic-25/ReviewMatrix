# Role Skill Template

```markdown
---
name: <role-slug>
description: <one-sentence trigger and expertise description>
---

# <Role Name>

Use this skill when <trigger conditions>.

## Role Boundary

<What this role owns and what it does not own.>

## Evidence To Inspect

- <evidence type>

## Review Focus

- <focus area>

## Conflict And Overlap

- Existing role overlaps: <role slugs and why this role remains distinct>
- Candidate role overlaps: <candidate slugs or none>
- Conflict patterns: <where this role may disagree with other roles and how to route the disagreement>

## Review Protocol

1. Read the matrix review brief.
2. Read this role's `memory.md`. Treat stable lessons and review patterns as guidance, and treat candidate improvements as provisional until the user approves a skill upgrade.
3. State assumptions and evidence gaps.
4. Review only from this role boundary.
5. Produce findings with severity, evidence, risk, recommendation, and owner hint.
6. Ask only material questions.
7. Provide `gate_impact`: `pass`, `revise`, or `blocked`.
8. Provide `evolution_notes` for reusable lessons.

## Output Contract

- `role`
- `assumptions`
- `findings`
- `questions`
- `gate_impact`
- `evolution_notes`
```
