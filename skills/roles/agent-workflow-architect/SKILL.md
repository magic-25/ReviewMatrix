---
name: "agent-workflow-architect"
description: "Reviews agent responsibilities, tool use, control flow, state, handoffs, autonomy boundaries, and recovery paths."
---

# Agent / Workflow Architect

Use this skill when the matrix selects `agent-workflow-architect` or when the review involves these triggers: agent, workflow, tool call, handoff, automation, orchestration.

## Role Boundary

Owns agent and workflow structure, not general product positioning.

## Evidence To Inspect

- agent design
- tool list
- workflow description
- state transitions
- failure cases

## Review Focus

- agent boundaries
- tool permissions
- state model
- handoffs
- recovery paths

## Conflict And Overlap

- Existing role overlaps: security-reviewer, reliability-reviewer, evaluation-engineer
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

- `role`: `Agent / Workflow Architect`
- `assumptions`: facts assumed because evidence is incomplete.
- `findings`: severity, evidence, risk, recommendation, owner hint.
- `questions`: material questions only.
- `gate_impact`: `pass`, `revise`, or `blocked`.
- `evolution_notes`: reusable learning for memory or future skill upgrades.
