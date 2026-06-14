#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "skills/role-review-matrix/references/role-registry.json"
ROLES_DIR = ROOT / "skills/roles"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_ROLE_FIELDS = {
    "slug",
    "name",
    "group",
    "description",
    "applies_to",
    "triggers",
    "boundary",
    "review_focus",
    "evidence_needs",
    "conflicts_with",
}
LIST_ROLE_FIELDS = {
    "applies_to",
    "triggers",
    "review_focus",
    "evidence_needs",
    "conflicts_with",
}
STRING_ROLE_FIELDS = {
    "slug",
    "name",
    "group",
    "description",
    "boundary",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    sys.exit(1)


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def frontmatter_scalar(value: str) -> str:
    return json.dumps(value)


def validate_single_line(value: object, field: str, slug: str) -> None:
    if not isinstance(value, str) or not value.strip():
        fail(f"Role {slug} field {field} must be a non-empty string")
    if "\n" in value or "\r" in value:
        fail(f"Role {slug} field {field} must be a single line")
    if value.strip() == "---":
        fail(f"Role {slug} field {field} must not be a frontmatter delimiter")


def validate_registry(registry: dict) -> list[dict]:
    roles = registry.get("roles")
    if not isinstance(roles, list) or not roles:
        fail("Registry must contain a non-empty roles list")

    slugs = []
    for role in roles:
        if not isinstance(role, dict):
            fail("Each registry role must be an object")
        missing = REQUIRED_ROLE_FIELDS - set(role)
        if missing:
            fail(f"Role {role.get('slug', '<unknown>')} missing fields: {sorted(missing)}")
        for field in STRING_ROLE_FIELDS:
            validate_single_line(role[field], field, role.get("slug", "<unknown>"))
        for field in LIST_ROLE_FIELDS:
            if not isinstance(role[field], list):
                fail(f"Role {role['slug']} field {field} must be a list")
            for item in role[field]:
                validate_single_line(item, field, role["slug"])
        slug = role.get("slug")
        if SLUG_RE.fullmatch(slug) is None:
            fail(f"Role slug is not directory-safe: {slug!r}")
        slugs.append(slug)

    seen = set()
    for slug in slugs:
        if slug in seen:
            fail(f"Duplicate role slug: {slug}")
        seen.add(slug)

    known_slugs = set(slugs)
    for role in roles:
        slug = role["slug"]
        conflicts = role.get("conflicts_with")
        if not isinstance(conflicts, list):
            fail(f"Role {slug} field conflicts_with must be a list")
        missing = sorted(set(conflicts) - known_slugs)
        if missing:
            fail(f"Role {slug} conflicts_with unknown roles: {missing}")

    return roles


def skill_content(role: dict) -> str:
    triggers = ", ".join(role["triggers"])
    conflicts = ", ".join(role["conflicts_with"]) if role["conflicts_with"] else "none"
    return f"""---
name: {frontmatter_scalar(role["slug"])}
description: {frontmatter_scalar(role["description"])}
---

# {role["name"]}

Use this skill when the matrix selects `{role["slug"]}` or when the review involves these triggers: {triggers}.

## Role Boundary

{role["boundary"]}

## Evidence To Inspect

{bullet(role["evidence_needs"])}

## Review Focus

{bullet(role["review_focus"])}

## Conflict And Overlap

- Existing role overlaps: {conflicts}
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

- `role`: `{role["name"]}`
- `assumptions`: facts assumed because evidence is incomplete.
- `findings`: severity, evidence, risk, recommendation, owner hint.
- `questions`: material questions only.
- `gate_impact`: `pass`, `revise`, or `blocked`.
- `evolution_notes`: reusable learning for memory or future skill upgrades.
"""


def memory_content(role: dict) -> str:
    return f"""# {role["name"]} Memory

This file stores experience for `{role["slug"]}`. Memory is not a permanent rule until the user approves a skill upgrade.

## Stable Lessons

- Start with the role boundary: {role["boundary"]}

## Candidate Improvements

- No candidate improvements recorded yet.

## Review Patterns

- Useful lifecycle stages: {", ".join(role["applies_to"])}
- Common triggers: {", ".join(role["triggers"])}
- Expected evidence: {", ".join(role["evidence_needs"])}

## Upgrade Proposals

- No upgrade proposals recorded yet.
"""


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    roles = validate_registry(registry)
    ROLES_DIR.mkdir(parents=True, exist_ok=True)
    for role in roles:
        role_dir = ROLES_DIR / role["slug"]
        role_dir.mkdir(parents=True, exist_ok=True)
        (role_dir / "SKILL.md").write_text(skill_content(role), encoding="utf-8")
        memory_path = role_dir / "memory.md"
        if not memory_path.exists():
            memory_path.write_text(memory_content(role), encoding="utf-8")
    print(f"Generated {len(roles)} role skills")


if __name__ == "__main__":
    main()
