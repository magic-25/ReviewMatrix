---
name: role-review-matrix
description: Stage-aware multi-role review for product, AI-native, engineering, quality, risk, market, launch, and operations artifacts.
---

# Role Review Matrix

Use this skill when the user asks for a professional multi-role review, role review matrix, launch readiness review, lifecycle review, PRD review, architecture review, AI-native product review, code review from multiple roles, GTM review, or any request that needs several professional perspectives.

## Required References

Read these files before producing the review:

- `references/lifecycle-stages.md`
- `references/role-registry.json`
- `references/context-reading-policy.md`
- `references/review-output-template.md`

## Operating Rules

1. Accept arbitrary input from the user. Do not require a fixed template.
2. Build a structured review brief before selecting roles.
3. Read project context according to the stage-aware context policy.
4. Select baseline roles from lifecycle stage and dynamic roles from risk signals.
5. If a needed role is missing, create a `temporary_role_view` for this review and list the role as a candidate for `role-creator`.
6. Ask for missing evidence only when it materially affects the gate decision.
7. Produce a gate decision: `pass`, `revise`, or `blocked`.
8. Preserve role conflicts, then provide a recommended decision.
9. Capture `evolution_notes` separately from permanent rules.
10. Do not automatically modify skill files or role memory without user confirmation.
11. Use local evidence first. Browse externally when the user asks, when current external facts materially affect market, legal, security, pricing, or AI ecosystem judgment, or when platform policy requires it. Cite external sources and separate them from local evidence.

## Review Brief Contract

Create a review brief with these fields:

- `artifact_type`
- `lifecycle_stage`
- `domain_signals`
- `decision_needed`
- `evidence_sources`
- `risk_profile`
- `selected_roles`
- `temporary_role_views`
- `evidence_gaps`

## Role Selection

Use three passes:

1. **Core coverage:** select roles based on lifecycle stage.
2. **Risk-triggered expansion:** add roles for AI, agent, data, privacy, security, performance, reliability, GTM, pricing, legal, growth, launch, and market signals.
3. **Missing role detection:** create a temporary role view when needed expertise is absent from the registry.

### Baseline Stage Mapping

Start with these registry roles:

| Stage | Baseline roles |
| --- | --- |
| `discovery` | `product-manager`, `market-research-analyst`, `ai-product-strategist`, `marketing-strategist` |
| `definition` | `product-manager`, `interaction-ux-reviewer`, `qa-engineer`, `market-research-analyst` |
| `design` | `product-manager`, `interaction-ux-reviewer`, `software-architect`, `agent-workflow-architect` |
| `architecture` | `software-architect`, `security-reviewer`, `privacy-reviewer`, `reliability-reviewer` |
| `implementation` | `developer-reviewer`, `qa-engineer`, `software-architect`, `security-reviewer` |
| `verification` | `qa-engineer`, `developer-reviewer`, `evaluation-engineer`, `reliability-reviewer` |
| `launch` | `product-manager`, `qa-engineer`, `marketing-strategist`, `sales-gtm-reviewer`, `reliability-reviewer` |
| `operation` | `reliability-reviewer`, `performance-reviewer`, `security-reviewer`, `growth-strategist`, `sales-gtm-reviewer` |
| `postmortem` | `reliability-reviewer`, `developer-reviewer`, `software-architect`, `qa-engineer` |
| `unknown` | `product-manager`, `software-architect`, `qa-engineer` |

### Risk-Triggered Additions

Add roles when the input, files, domain, or requested decision includes these signals:

| Signal | Add roles |
| --- | --- |
| AI or model behavior | `ai-product-strategist`, `evaluation-engineer` |
| Agent, tool use, workflow, or orchestration | `agent-workflow-architect`, `evaluation-engineer`, `security-reviewer` |
| Data, PII, retention, consent, or privacy | `privacy-reviewer`, `security-reviewer` |
| Authentication, authorization, secrets, abuse, or supply chain | `security-reviewer` |
| Latency, scale, throughput, resource use, model cost, or load | `performance-reviewer` |
| Availability, rollback, observability, incidents, or recovery | `reliability-reviewer` |
| Market, competitor, category, demand, GTM, sales, buyer, or launch motion | `market-research-analyst`, `sales-gtm-reviewer`, `marketing-strategist` |
| Pricing, packaging, margins, revenue, cost model, or unit economics | `finance-pricing-reviewer`, `performance-reviewer` |
| Legal, compliance, regulation, policy, contracts, or terms | `legal-compliance-reviewer`, `privacy-reviewer` |
| Growth, activation, retention, funnel, referral, or experiment loops | `growth-strategist`, `marketing-strategist` |

### Cap, Tie-Breakers, and Missing Roles

- Target 4-7 roles for normal review. Use at least 3 roles for `unknown` or narrow reviews.
- Allow more than 7 roles only for `deep review`, `full lifecycle review`, `全面 review`, regulated domains, launch readiness, production incidents, or cross-functional decisions.
- If too many roles match, keep roles with direct evidence in the artifact, direct responsibility for the requested decision, high-risk triggers, and lifecycle-stage fit.
- Prefer the more specific role over a general role when their findings would overlap.
- Keep conflicting roles when the conflict is material to the decision.
- If a required expertise is absent from `role-registry.json`, create a `temporary_role_view` with boundary, assumptions, evidence needs, and why no registry role covers it.

## Role Review Protocol

For each selected role, produce:

- Read each selected role's `SKILL.md` before performing that role review.
- Read each selected role's `memory.md` before performing that role review. Treat stable lessons and review patterns as guidance, and treat candidate improvements as provisional until the user approves a skill upgrade.
- Role boundary and assumptions.
- Findings with severity, evidence, risk, recommendation, and owner hint.
- Material questions.
- `gate_impact`: `pass`, `revise`, or `blocked`.
- `evolution_notes` for reusable patterns or possible role improvement.

## Synthesis Protocol

After role review:

1. Deduplicate overlapping findings.
2. Preserve conflicting role positions.
3. Rank highest-risk findings.
4. Convert role gate impacts into one final gate decision.
5. Separate required actions from optional improvements.
6. List candidate missing roles.
7. List memory or skill upgrade proposals only as recommendations.

## Output

Follow `references/review-output-template.md`.
