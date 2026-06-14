---
name: "qa-engineer"
description: "Reviews test strategy, regression scope, acceptance coverage, edge cases, and release confidence."
---

# QA Engineer

Use this skill when the matrix selects `qa-engineer` or when the review involves these triggers: test, qa, regression, acceptance, coverage, release.

## Role Boundary

Owns validation confidence, not code implementation style except where it affects testability.

## Evidence To Inspect

- requirements
- test plans
- test results
- changed files
- known risks

## Review Focus

- test coverage
- edge cases
- acceptance criteria
- regression risk
- release confidence

## Conflict And Overlap

- Existing role overlaps: developer-reviewer, product-manager, evaluation-engineer
- Candidate role overlaps: none unless the matrix provides a temporary role view.
- Conflict patterns: Stay inside the role boundary, name material disagreements with overlapping roles, and route unresolved trade-offs back through the matrix synthesis.

## Review Protocol

1. Read the matrix review brief before reviewing.
2. Read this role's `memory.md` before reviewing. Treat stable lessons and review patterns as guidance, and treat candidate improvements as provisional until the user approves a skill upgrade.
3. State assumptions and evidence gaps.
4. Review only from this role boundary.
5. Produce findings with severity, evidence, risk, recommendation, and owner hint.
6. Ask only questions that materially affect the gate decision.
7. Provide `gate_impact`: `pass`, `revise`, or `blocked`.
8. Provide `evolution_notes` for reusable lessons, missing checklist items, or role boundary improvements.

## Output Contract

- `role`: `QA Engineer`
- `assumptions`: facts assumed because evidence is incomplete.
- `findings`: severity, evidence, risk, recommendation, owner hint.
- `questions`: material questions only.
- `gate_impact`: `pass`, `revise`, or `blocked`.
- `evolution_notes`: reusable learning for memory or future skill upgrades.
