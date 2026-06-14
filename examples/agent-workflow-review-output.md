# Example Output: Agent Workflow Review

## Executive Summary

Lifecycle stage: `architecture`. Selected roles: Agent / Workflow Architect, Security Reviewer, Reliability Reviewer, Developer Reviewer, QA Engineer.

Gate decision: `revise`.

The workflow is useful, but it needs stronger permission boundaries and recovery behavior before implementation.

## Highest-Risk Findings

- `P1` Security Reviewer: Tool permissions are broad and need explicit denial rules for secrets and protected branches.
- `P1` Agent / Workflow Architect: The workflow does not define when the agent stops and asks for human approval.
- `P2` Reliability Reviewer: Test failure and partial patch recovery paths are not defined.

## Required Actions

- Add a tool permission policy.
- Require PR branch creation and block direct `main` pushes.
- Define failure handling for test failures, merge conflicts, and interrupted runs.

## Candidate Missing Roles

- None.
