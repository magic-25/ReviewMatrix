# Security Policy

## Supported Versions

Security fixes are accepted for the current `main` branch.

## Reporting a Vulnerability

Please report security issues through GitHub private vulnerability reporting if it is available for this repository. If private reporting is not available, open an issue with a minimal description and avoid publishing sensitive exploit details, credentials, tokens, private data, or proprietary project material.

## Scope

Security-sensitive areas include:

- Sync behavior that could overwrite or expose local skill memory.
- Instructions that encourage reading secrets or unrelated private files.
- Role logic that weakens security, privacy, or compliance review.
- Scripts that execute unexpected commands or write outside intended paths.

## Handling Sensitive Data

Do not include secrets, `.env` contents, private customer data, or proprietary project artifacts in issues, examples, tests, or memory files.

## Response Expectations

Maintainers should acknowledge security reports when possible, investigate the impact, and publish a fix or mitigation note before encouraging public discussion of details.
