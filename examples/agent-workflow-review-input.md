# Example Input: Agent Workflow Review

Use Role Review Matrix to review this agent workflow before implementation.

## Workflow

An agent reads a GitHub issue, inspects related files, proposes a patch, runs tests, and opens a draft PR.

## Tools

- GitHub issue and PR access.
- Local file read/write.
- Test runner.
- Git commit and push.

## Decision Needed

Is this safe enough to implement as an internal developer workflow?

## Constraints

- The agent must not push directly to `main`.
- It must not read `.env` files.
- It should ask for confirmation before destructive changes.
