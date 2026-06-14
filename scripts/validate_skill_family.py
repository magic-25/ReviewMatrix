#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

from generate_roles import REQUIRED_ROLE_FIELDS, SLUG_RE, skill_content

ROOT = Path(__file__).resolve().parents[1]

MATRIX_REFS = [
    "lifecycle-stages.md",
    "role-registry.json",
    "review-output-template.md",
    "context-reading-policy.md",
]

CREATOR_REFS = [
    "role-skill-template.md",
    "role-quality-checklist.md",
]

LIST_ROLE_FIELDS = ["applies_to", "triggers", "review_focus", "evidence_needs", "conflicts_with"]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"Missing file: {path.relative_to(ROOT)}")


def require_dir(path: Path) -> None:
    if not path.is_dir():
        fail(f"Missing directory: {path.relative_to(ROOT)}")


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"Unclosed YAML frontmatter: {path.relative_to(ROOT)}")
    frontmatter = text[4:end].strip().splitlines()
    data = {}
    for line in frontmatter:
        if ":" not in line:
            fail(f"Invalid frontmatter line in {path.relative_to(ROOT)}: {line}")
        key, value = line.split(":", 1)
        value = value.strip()
        quoted = False
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError as exc:
                fail(f"Invalid quoted frontmatter value in {path.relative_to(ROOT)}: {exc}")
            quoted = True
        if isinstance(value, str) and not quoted:
            value = value.strip('"')
        data[key.strip()] = value
    if not data.get("name"):
        fail(f"Frontmatter missing name: {path.relative_to(ROOT)}")
    if not data.get("description"):
        fail(f"Frontmatter missing description: {path.relative_to(ROOT)}")
    return data


def require_contains(path: Path, patterns: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for pattern in patterns:
        if re.search(pattern, text, re.MULTILINE) is None:
            fail(f"Pattern not found in {path.relative_to(ROOT)}: {pattern}")


def validate_registry() -> list[dict]:
    registry_path = ROOT / "skills/role-review-matrix/references/role-registry.json"
    require_file(registry_path)
    try:
        data = json.loads(registry_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON registry: {exc}")
    roles = data.get("roles")
    if not isinstance(roles, list) or not roles:
        fail("Registry must contain a non-empty roles list")
    seen = set()
    for role in roles:
        missing = REQUIRED_ROLE_FIELDS - set(role)
        if missing:
            fail(f"Role {role.get('slug', '<unknown>')} missing fields: {sorted(missing)}")
        slug = role["slug"]
        if not isinstance(slug, str) or SLUG_RE.fullmatch(slug) is None:
            fail(f"Role slug is not directory-safe: {slug!r}")
        if slug in seen:
            fail(f"Duplicate role slug: {slug}")
        seen.add(slug)
        for list_field in LIST_ROLE_FIELDS:
            if not isinstance(role[list_field], list):
                fail(f"Role {slug} field {list_field} must be a list")
    for role in roles:
        missing_conflicts = sorted(set(role["conflicts_with"]) - seen)
        if missing_conflicts:
            fail(f"Role {role['slug']} conflicts_with unknown roles: {missing_conflicts}")
    if len(roles) != 18:
        fail(f"Expected 18 V1 roles, found {len(roles)}")
    return roles


def validate_main_skills() -> None:
    matrix_skill = ROOT / "skills/role-review-matrix/SKILL.md"
    creator_skill = ROOT / "skills/role-creator/SKILL.md"
    require_file(matrix_skill)
    require_file(creator_skill)
    parse_frontmatter(matrix_skill)
    parse_frontmatter(creator_skill)
    require_contains(
        matrix_skill,
        [
            r"review brief",
            r"gate decision",
            r"Read each selected role's `SKILL\.md`",
            r"Read each selected role's `memory\.md`",
            r"temporary_role_view",
            r"conflict",
            r"evolution_notes",
        ],
    )
    require_contains(
        creator_skill,
        [
            r"candidate role brief",
            r"draft a role skill",
            r"Proposed role skill content",
            r"Do not install",
            r"role explosion",
        ],
    )
    for ref in MATRIX_REFS:
        require_file(ROOT / "skills/role-review-matrix/references" / ref)
    for ref in CREATOR_REFS:
        require_file(ROOT / "skills/role-creator/references" / ref)


def validate_roles(roles: list[dict]) -> None:
    roles_dir = ROOT / "skills/roles"
    require_dir(roles_dir)
    for role in roles:
        role_dir = roles_dir / role["slug"]
        skill_path = role_dir / "SKILL.md"
        memory_path = role_dir / "memory.md"
        require_file(skill_path)
        require_file(memory_path)
        frontmatter = parse_frontmatter(skill_path)
        if frontmatter["name"] != role["slug"]:
            fail(f"Role skill name mismatch for {role['slug']}")
        expected_skill = skill_content(role)
        actual_skill = skill_path.read_text(encoding="utf-8")
        if actual_skill != expected_skill:
            fail(f"Generated role skill is stale: {skill_path.relative_to(ROOT)}")
        require_contains(
            skill_path,
            [
                r"## Role Boundary",
                r"## Review Protocol",
                r"## Output Contract",
                r"Read this role's `memory\.md`",
                r"gate_impact",
                r"evolution_notes",
            ],
        )
        require_contains(
            memory_path,
            [
                r"# .* Memory",
                r"## Stable Lessons",
                r"## Candidate Improvements",
                r"## Review Patterns",
            ],
        )


def validate_support_files() -> None:
    require_file(ROOT / "README.md")
    require_file(ROOT / ".gitignore")
    require_file(ROOT / "scripts/generate_roles.py")
    require_file(ROOT / "scripts/sync_to_codex_skills.sh")
    require_contains(
        ROOT / "README.md",
        [
            r"Role Review Matrix",
            r"Installation",
            r"Safety Model",
            r"Memory Backflow",
            r"sync installed memory back",
        ],
    )
    require_contains(ROOT / ".gitignore", [r"__pycache__/", r"\*\.pyc"])


def main() -> None:
    validate_support_files()
    validate_main_skills()
    roles = validate_registry()
    validate_roles(roles)
    print("OK: skill family structure is valid")


if __name__ == "__main__":
    main()
