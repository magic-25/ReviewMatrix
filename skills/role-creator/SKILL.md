---
name: role-creator
description: Drafts new professional review role skills from candidate role briefs produced by role-review-matrix.
---

# Role Creator

Use this skill when `role-review-matrix` identifies a missing professional review role or the user asks to create a new review role.

## Required References

Read these files before drafting a role:

- `references/role-skill-template.md`
- `references/role-quality-checklist.md`

## Candidate Role Brief

Require or infer these fields:

- `role_name`
- `why_needed`
- `lifecycle_stages`
- `expertise_boundary`
- `required_inputs`
- `review_checklist`
- `output_expectations`
- `overlap_with_existing_roles`
- `conflict_patterns`
- `memory_seeds`

## Registry Entry Schema

Every proposed role must include a registry entry with these exact fields:

- `slug`: stable kebab-case role identifier.
- `name`: human-readable role name.
- `group`: durable role family or review group.
- `description`: one-sentence purpose and trigger summary.
- `applies_to`: lifecycle stages, artifacts, or situations where the role applies.
- `triggers`: signals that should activate this role.
- `boundary`: what the role owns and explicitly does not own.
- `review_focus`: concrete review concerns the role evaluates.
- `evidence_needs`: inputs, artifacts, or context the role must inspect.
- `conflicts_with`: existing role slugs or declared candidate role slugs with likely overlap or tension.

Map candidate brief fields to registry fields this way:

- `role_name` maps to `name`; derive `slug` from it unless the brief gives a better stable slug.
- `why_needed` maps to `description` and helps justify `triggers`.
- `lifecycle_stages` maps to `applies_to`.
- `expertise_boundary` maps to `boundary` and informs `group`.
- `required_inputs` maps to `evidence_needs`.
- `review_checklist` maps to `review_focus`.
- `output_expectations` informs `description`, `review_focus`, and the role skill output contract.
- `overlap_with_existing_roles` maps to `conflicts_with` when overlap creates routing ambiguity.
- `conflict_patterns` maps to `conflicts_with` and the role skill conflict/overlap section.
- `memory_seeds` maps to the proposed `memory.md` sections.

## Memory Content

Draft `memory.md` with these expected sections:

- `Stable Lessons`: durable principles, constraints, and domain rules the role should remember.
- `Candidate Improvements`: concrete changes that would make the draft role more useful before installation.
- `Review Patterns`: repeated signals, evidence patterns, and finding shapes the role should watch for.
- `Upgrade Proposals`: future refinements, split/merge candidates, or registry changes.

Assign each memory seed to the section where it will be most reusable. Do not leave unclassified memory seeds.

## Creation Protocol

1. Check whether an existing role can cover the need through memory or a skill upgrade.
2. If a new role is justified, draft a role skill using the template.
3. Draft an initial `memory.md` with memory seeds.
4. Explain overlap and conflict boundaries.
5. Do not install, activate, or sync the role without explicit user confirmation.
6. Do not create narrow one-off roles when a broader durable role is more useful.
7. Avoid role explosion by preferring reusable expertise boundaries.

## Output

Return:

- Proposed role slug.
- Proposed role skill content.
- Proposed memory content.
- Registry entry.
- Reason existing roles are insufficient.
- Installation instructions after user approval.
