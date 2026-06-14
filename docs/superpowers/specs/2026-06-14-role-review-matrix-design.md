# Role Review Matrix Skill Family Design

## Summary

Build a Codex skill family for professional multi-role review across the full lifecycle of AI-native software products and adjacent product work. The system starts from natural user input, detects the lifecycle stage, reads relevant project context, selects review roles, coordinates role-specific review, resolves conflicts, and produces a decision-oriented review report.

The first version is a source repository that can be synced into the Codex skills directory. It includes a matrix orchestration skill, a role creator skill, an initial library of role skills, shared references, role memory files, and installation guidance.

## Goals

- Let the user invoke a professional review naturally from any project or artifact.
- Support arbitrary inputs such as ideas, PRDs, strategy memos, architecture notes, code diffs, test plans, launch plans, incident reviews, and repository context.
- Detect the lifecycle stage before selecting reviewers.
- Use stable core roles plus dynamically selected extended roles.
- Cover product, business, design, engineering, AI-native, quality, risk, marketing, market, and operational perspectives.
- Produce a concise executive decision first, then detailed role findings.
- Expose cross-role conflicts and provide a recommended decision.
- Let roles evolve through accumulated experience and human-approved upgrades.
- Create missing role skills through a dedicated role creator flow.

## Non-Goals

- Do not build a UI in V1.
- Do not automatically research the web unless the user explicitly asks for external research.
- Do not automatically modify role skill files without user approval.
- Do not force every role to participate in every review.
- Do not automatically promote temporary roles into permanent roles.
- Do not try to cover every possible industry role in the initial role library.

## Skill Family

The V1 system contains three categories of skills.

### Matrix Skill

`role-review-matrix` is the main entry point. It is responsible for:

- Understanding the user request.
- Reading project context according to the context policy.
- Producing a structured review brief.
- Selecting role skills.
- Creating temporary role views when a needed role does not exist.
- Coordinating role outputs.
- Deduplicating findings.
- Surfacing conflicts.
- Producing the final gate decision and action plan.
- Capturing evolution notes for role memory.

### Role Creator Skill

`role-creator` creates missing roles from candidate role briefs generated during review. It produces a draft role skill and supporting memory seed, but does not install or activate the role without user confirmation.

### Role Skills

Role skills each own one professional perspective. They receive the same review brief and produce findings from their own boundary. They should avoid repeating other roles unless overlap is necessary to explain a conflict.

## Initial Role Library

The initial role library is organized into three groups.

### Product And Business Roles

- Product Manager
- AI Product Strategist
- Market Research Analyst
- Marketing Strategist
- Growth Strategist
- Sales / GTM Reviewer
- Customer Success Reviewer
- Business Model Reviewer
- Competitive Intelligence Reviewer
- Brand / Positioning Reviewer
- Community / Ecosystem Reviewer
- Finance / Pricing Reviewer

### Design And Engineering Roles

- Interaction / UX Reviewer
- Software Architect
- Agent / Workflow Architect
- Developer Reviewer
- Frontend Reviewer
- Backend Reviewer
- DevOps / Infrastructure Reviewer
- Data Engineer Reviewer

### Quality And Risk Roles

- Security Reviewer
- Privacy Reviewer
- Performance Reviewer
- Reliability Reviewer
- QA Engineer
- Evaluation Engineer
- Legal / Compliance Reviewer
- Domain Expert Reviewer
- Accessibility Reviewer

The V1 implementation should create a practical subset first and keep the registry ready for expansion. The first concrete role set is:

- Product Manager
- AI Product Strategist
- Interaction / UX Reviewer
- Software Architect
- Agent / Workflow Architect
- Developer Reviewer
- Evaluation Engineer
- QA Engineer
- Security Reviewer
- Privacy Reviewer
- Performance Reviewer
- Reliability Reviewer
- Marketing Strategist
- Market Research Analyst
- Growth Strategist
- Sales / GTM Reviewer
- Legal / Compliance Reviewer
- Finance / Pricing Reviewer

## Invocation Flow

The user can invoke the matrix with natural language, for example:

- "Review this PRD with the role review matrix."
- "Run a deep review on this agent workflow."
- "Review the current diff before I merge."
- "Do a launch readiness review."
- "Use the matrix to review this market strategy."

The matrix skill performs these steps:

1. Intake the user's request and any attached or pasted artifact.
2. Detect the artifact type and lifecycle stage.
3. Read relevant project context using the stage-aware context policy.
4. Produce a structured review brief.
5. Select core and dynamic roles.
6. Identify missing roles and create temporary role views if needed.
7. Run role-specific review.
8. Merge findings, questions, gate impacts, and evolution notes.
9. Resolve conflicts and produce a recommended decision.
10. Save or propose role memory updates when useful.
11. Suggest candidate role creation or role skill upgrades when warranted.

## Review Brief

The matrix normalizes arbitrary input into a review brief with these fields:

- `artifact_type`: idea, PRD, design spec, architecture brief, code diff, test plan, launch plan, incident review, strategy memo, or mixed artifact.
- `lifecycle_stage`: discovery, definition, design, architecture, implementation, verification, launch, operation, postmortem, or unknown.
- `domain_signals`: AI-native, agent workflow, data/privacy, market/GTM, infrastructure, security-sensitive, performance-sensitive, compliance-sensitive, pricing, growth, or other relevant signals.
- `decision_needed`: continue exploration, enter implementation, merge code, ship release, choose direction, improve operations, or complete postmortem.
- `evidence_sources`: user input, repository docs, git diff, recent commits, tests, configs, issues, PRs, logs, or external research if explicitly requested.
- `risk_profile`: high-risk areas, missing evidence, role gaps, uncertainty, and likely blocker categories.

## Context Reading Policy

The default policy is stage-aware and depth-controlled.

The matrix should not scan the whole repository by default. It should read likely relevant evidence for the detected stage:

- Discovery and definition: README, docs, product notes, strategy memos, user research, market notes.
- Design: UX docs, flow specs, diagrams, interface descriptions, frontend structure if present.
- Architecture: directory structure, API contracts, configs, dependency manifests, core modules, architectural docs.
- Implementation: git diff, changed files, nearby tests, related modules, lint or type configuration.
- Verification: test plans, test files, CI config, known failures, coverage notes.
- Launch: release notes, environment config, rollout plan, observability, rollback instructions.
- Operation and postmortem: logs, incidents, metrics notes, runbooks, alerts, recovery notes.

If the user requests "deep review", "full lifecycle review", or "全面 review", the matrix can expand the context scan to more files, history, configs, tests, and project documentation.

When evidence is incomplete, the final report must distinguish:

- Findings supported by current evidence.
- Questions that materially affect judgment.
- Gaps that limit confidence.
- Gaps that force `revise` or `blocked`.

## Role Selection Protocol

Role selection has three layers.

### Core Coverage

The matrix selects baseline roles from the lifecycle stage. Examples:

- Idea or PRD: Product Manager, UX, Market Research, Business Model, AI Product Strategist when AI-native.
- Architecture: Software Architect, Security, Performance, Reliability, Agent / Workflow Architect when agent-related.
- Implementation: Developer, QA, Security, Performance, affected frontend/backend/infrastructure roles.
- Verification: QA, Evaluation Engineer, Reliability, Security, Privacy when data or access is involved.
- Launch: Launch / Operations if present, Reliability, Security, GTM, Customer Success, Marketing or Sales when relevant.

### Risk-Triggered Expansion

The matrix adds roles based on domain signals and risk profile:

- User data: Privacy, Legal / Compliance, Security.
- Model quality: Evaluation Engineer, AI Product Strategist, AI Safety or temporary role if no permanent role exists.
- Agent autonomy: Agent / Workflow Architect, Security, Reliability, Evaluation Engineer.
- Business model or pricing: Finance / Pricing, Business Model, GTM.
- Market uncertainty: Market Research, Competitive Intelligence, Brand / Positioning.
- Growth motion: Growth, Marketing, Community, Customer Success.
- Frontend experience: UX, Accessibility, Frontend, Performance.
- Production change: Reliability, DevOps / Infrastructure, Security, QA.

### Missing Role Detection

If the matrix detects that a needed role does not exist, it creates a `temporary_role_view` for the current review. This temporary view should cover the most important questions for the missing expertise without blocking the review.

After the review, the matrix lists the missing role as a candidate role and can hand it to `role-creator` if the user wants to formalize it.

## Role Review Protocol

Each role skill receives the same review brief and follows this protocol:

- State the role boundary and assumptions.
- Review only from that role's perspective.
- Produce findings with severity, evidence, risk, recommendation, and owner hint.
- Ask only questions that materially affect the decision.
- Provide a role-level `gate_impact`: pass, revise, or blocked.
- Include `evolution_notes` when the review reveals a reusable checklist item, risk pattern, judgment rule, role boundary improvement, or missing evidence pattern.

Findings should prioritize concrete risks over generic advice. The role should explicitly say when evidence is insufficient.

## Final Review Output

The matrix produces a combined report with this structure:

1. Executive summary.
2. Gate decision: `pass`, `revise`, or `blocked`.
3. Highest-risk findings.
4. Evidence gaps.
5. Role findings grouped by role.
6. Cross-role conflicts.
7. Recommended decision and trade-off rationale.
8. Required actions before the next lifecycle stage.
9. Optional improvements.
10. Candidate missing roles.
11. Role evolution notes.

The gate decision means:

- `pass`: no known blockers for the requested decision, though optional improvements may exist.
- `revise`: important issues should be addressed before moving forward.
- `blocked`: the review cannot responsibly approve progress because critical evidence is missing or critical risk is unresolved.

## Conflict Handling

When roles disagree, the matrix preserves the conflict instead of flattening it away. Conflict handling uses this format:

- `conflict`: the disputed decision or trade-off.
- `role_positions`: each role's position and reason.
- `trade_off`: what is gained or lost by each option.
- `recommended_decision`: the matrix's recommendation.
- `why`: the evidence and priority behind the recommendation.

The matrix can recommend a decision, but it should make uncertainty explicit.

## Role Evolution

Roles can evolve through two controlled mechanisms.

### Experience Memory

Each role has a `memory.md` file. Role evolution notes can be added to memory as experience. Memory may include:

- New risk patterns.
- Reusable checklist items.
- Common false positives.
- Domain-specific heuristics.
- Evidence requirements.
- Role boundary clarifications.
- Examples of strong or weak artifacts.

Memory is not automatically treated as a permanent rule. It is a growing experience pool.

### Human-Approved Skill Upgrade

When an experience is repeated, high impact, or explicitly selected by the user, a role can propose a skill upgrade. The proposal must include:

- Target role.
- Proposed change.
- Reason for the change.
- Evidence from prior reviews or current review.
- Expected benefit.
- Possible side effects.
- Rollback note.

Only after user confirmation should the skill file be changed.

## Role Creator

`role-creator` accepts a candidate role brief:

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

It creates a draft role skill and memory file. It should check whether an existing role can be extended before creating a new role, to avoid role explosion.

## Repository Structure

The source repository should use this structure:

```text
ReviewMatrix/
  README.md
  skills/
    role-review-matrix/
      SKILL.md
      references/
        lifecycle-stages.md
        role-registry.md
        review-output-template.md
        context-reading-policy.md
    role-creator/
      SKILL.md
      references/
        role-skill-template.md
        role-quality-checklist.md
    roles/
      product-manager/
        SKILL.md
        memory.md
      ai-product-strategist/
        SKILL.md
        memory.md
      interaction-ux-reviewer/
        SKILL.md
        memory.md
      software-architect/
        SKILL.md
        memory.md
      agent-workflow-architect/
        SKILL.md
        memory.md
      developer-reviewer/
        SKILL.md
        memory.md
      evaluation-engineer/
        SKILL.md
        memory.md
      qa-engineer/
        SKILL.md
        memory.md
      security-reviewer/
        SKILL.md
        memory.md
      privacy-reviewer/
        SKILL.md
        memory.md
      performance-reviewer/
        SKILL.md
        memory.md
      reliability-reviewer/
        SKILL.md
        memory.md
      marketing-strategist/
        SKILL.md
        memory.md
      market-research-analyst/
        SKILL.md
        memory.md
      growth-strategist/
        SKILL.md
        memory.md
      sales-gtm-reviewer/
        SKILL.md
        memory.md
      legal-compliance-reviewer/
        SKILL.md
        memory.md
      finance-pricing-reviewer/
        SKILL.md
        memory.md
  docs/
    superpowers/
      specs/
```

## Installation And Sync

The repository is the source of truth. Installation copies or syncs individual skill directories into the user's Codex skills directory.

V1 should document:

- Which directories are installed.
- Where they are installed.
- How to update installed skills from the repository.
- How to avoid overwriting local memory unintentionally.
- How to review proposed role upgrades before applying them.

## V1 Acceptance Criteria

- A user can invoke the matrix from arbitrary product or project material.
- The matrix can create a review brief.
- The matrix can choose roles from lifecycle stage and risk signals.
- The matrix can identify missing roles and use temporary role views.
- Role skills share a consistent review protocol.
- The final output includes executive summary, gate decision, role findings, conflicts, required actions, and evolution notes.
- Role memory exists and is distinct from permanent skill rules.
- Role upgrades require explicit user confirmation.
- `role-creator` can draft a new role skill from a candidate brief.
- The repository can be synced into Codex skills.
