# Review Output Template

Use this structure for final matrix reviews.

## Executive Summary

State the artifact reviewed, inferred lifecycle stage, selected roles, and the top decision implication.

## Gate Decision

Use exactly one:

- `pass`: no known blockers for the requested decision.
- `revise`: important issues should be addressed before moving forward.
- `blocked`: critical evidence is missing or critical risk is unresolved.

Explain the decision in 2-5 bullets.

## Severity Scale

Use these severities for findings:

- `critical`: likely failure, unsafe release, legal/compliance exposure, security vulnerability, data/privacy harm, or decision cannot be made with current evidence.
- `high`: material risk to user value, correctness, reliability, launch readiness, business outcome, or trust that should be fixed before the next lifecycle stage.
- `medium`: meaningful issue that can cause rework, confusion, degraded quality, or avoidable risk but does not block the immediate decision alone.
- `low`: polish, clarity, maintainability, or optional improvement with limited risk.

Map severity to gate decision:

- Any unresolved `critical` finding or blocker evidence gap normally makes the gate `blocked`.
- Any unresolved `high` finding normally makes the gate `revise`.
- Multiple related `medium` findings may make the gate `revise` when their combined risk affects the requested decision.
- Only `medium` or `low` findings with clear mitigation or low decision impact may still allow `pass`.
- If severity signals conflict across roles, choose the stricter gate and explain the trade-off in Cross-Role Conflicts.

## Highest-Risk Findings

List the most important findings first. Each finding must include severity, evidence, risk, recommendation, and owner hint.

## Evidence Gaps

Separate confidence-limiting gaps from blockers.

## Role Findings

Group findings by role. Keep each role focused on its boundary.

## Cross-Role Conflicts

For each conflict, include:

- `conflict`
- `role_positions`
- `trade_off`
- `recommended_decision`
- `why`

## Required Actions

List actions required before the next lifecycle stage.

## Optional Improvements

List useful improvements that are not gate blockers.

## Candidate Missing Roles

List temporary roles that should become formal role skills, if any.

## Role Evolution Notes

List memory updates or skill upgrade proposals. Do not apply them without user confirmation.
