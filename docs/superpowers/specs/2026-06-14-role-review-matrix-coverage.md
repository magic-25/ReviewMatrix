# Role Review Matrix V1 Coverage Audit

## Spec Coverage

- Natural invocation: covered by `skills/role-review-matrix/SKILL.md`.
- Lifecycle detection: covered by `references/lifecycle-stages.md`.
- Stage-aware context reading: covered by `references/context-reading-policy.md`.
- Core plus dynamic role selection: covered by `references/role-registry.json` and matrix instructions.
- Missing role handling: covered by `temporary_role_view` instructions and `role-creator`.
- Combined report: covered by `references/review-output-template.md`.
- Conflict preservation and recommendation: covered by matrix synthesis protocol and output template.
- Role evolution: covered by role skill output contract and `memory.md`.
- Human-approved upgrades: covered by README safety model and role creator rules.
- Repository-backed installation: covered by `scripts/sync_to_codex_skills.sh`.

## V1 Role Count

The V1 registry contains 18 roles.

## Known V1 Limits

- The matrix does not execute role skills automatically; Codex uses the skill instructions to perform the review.
- The sync script uses `rsync`, which must be available in the local shell.
- Memory preservation is file-based and simple.
- Role creation produces drafts and requires user confirmation before activation.
