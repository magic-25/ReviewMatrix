# Context Reading Policy

Read enough context to make an evidence-based review. Do not scan the whole repository by default.

## Default Reading

- Always inspect user-provided material first.
- Honor explicit user file, directory, commit, or diff scope. Do not expand beyond it unless the review cannot be evidence-based without doing so; state the reason before expanding.
- Use `rg --files` or equivalent fast file listing before reading many files.
- Avoid unrelated private files and personal notes outside the requested project or review scope.
- Do not read secrets, credentials, `.env` files, key files, local tokens, or private config unless explicitly necessary for the review and safe to inspect.
- Skip generated, vendor, dependency, build, cache, and coverage artifacts by default, including `node_modules`, `vendor`, `dist`, `build`, `.next`, `.turbo`, `.cache`, `coverage`, lockfile-generated payloads, and large binaries.
- If in a repository, inspect README and docs relevant to the detected stage.
- Prefer changed files and nearby tests for implementation review.
- Prefer docs and specs for product, definition, design, architecture, and launch review.
- Prefer logs, runbooks, metrics notes, and incident artifacts for operation and postmortem review.

## External Research

- Default to local evidence.
- Browse externally when the user asks for external research, when current external facts materially affect market, legal, security, pricing, or AI ecosystem review, or when platform policy requires browsing.
- Cite external sources and clearly separate external research from local repository or user-provided evidence.
- Treat external research as support for the review, not a substitute for missing local evidence.

## Stage-Aware Reading

- `discovery` and `definition`: README, docs, PRDs, strategy notes, market notes.
- `design`: UX docs, flow specs, diagrams, frontend route/component structure if relevant.
- `architecture`: directory structure, API contracts, configs, dependency manifests, architectural docs.
- `implementation`: git diff, changed files, nearby tests, related modules, lint/type config.
- `verification`: test plans, test files, CI config, known failure output, coverage notes.
- `launch`: release notes, environment config, rollout plan, observability, rollback instructions.
- `operation` and `postmortem`: logs, incident notes, metrics notes, runbooks, alerts, recovery notes.

## Deep Review

If the user says `deep review`, `full lifecycle review`, or `全面 review`, expand reading to more files, commit history, tests, configs, and documentation.

Keep deep review scoped to relevant evidence. Continue to avoid secrets, unrelated private files, generated/vendor/build artifacts, and large binaries unless explicitly necessary and safe.

## Evidence Gaps

When evidence is missing, distinguish:

- Findings supported by current evidence.
- Questions that materially affect judgment.
- Gaps that limit confidence.
- Gaps that force `revise` or `blocked`.
