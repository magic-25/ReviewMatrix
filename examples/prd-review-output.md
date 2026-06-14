# Example Output: PRD Review

## Executive Summary

Lifecycle stage: `definition`. Selected roles: Product Manager, AI Product Strategist, Privacy Reviewer, Evaluation Engineer, Interaction / UX Reviewer.

Gate decision: `revise`.

The product direction is promising, but the PRD needs clearer success metrics, privacy handling, and evaluation criteria before design work begins.

## Highest-Risk Findings

- `P1` Privacy Reviewer: The PRD says customer PII should not be stored, but does not define retention, redaction, or deletion behavior.
- `P1` Evaluation Engineer: There is no quality bar for feedback clustering or decision memo usefulness.
- `P2` Product Manager: Target users are clear, but the initial scope needs a sharper first workflow.

## Required Actions

- Define data retention and deletion rules.
- Add evaluation examples for good and bad clustering.
- Narrow the first version to one import source.

## Role Evolution Notes

- Product Manager memory candidate: PRDs involving imported user feedback should always define source ownership and auditability.
