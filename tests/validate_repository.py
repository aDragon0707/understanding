"""Static repository checks used by the GitHub Actions CI."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skill" / "lijie"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_utf8(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is not valid UTF-8: {exc}")
    if "\ufffd" in text:
        fail(f"{path.relative_to(ROOT)} contains a replacement character")
    return text


def validate_skill() -> None:
    skill_md = SKILL_ROOT / "SKILL.md"
    content = read_utf8(skill_md)
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        fail("SKILL.md has invalid YAML frontmatter delimiters")

    frontmatter = yaml.safe_load(match.group(1))
    if not isinstance(frontmatter, dict):
        fail("SKILL.md frontmatter must be a mapping")
    if frontmatter.get("name") != "lijie":
        fail("SKILL.md frontmatter name must be lijie")
    if not isinstance(frontmatter.get("description"), str):
        fail("SKILL.md frontmatter description must be a string")

    references = set(re.findall(r"`(references/[^`]+)`", content))
    for reference in references:
        if not (SKILL_ROOT / reference).is_file():
            fail(f"missing skill reference: {reference}")

    metadata = yaml.safe_load(read_utf8(SKILL_ROOT / "agents" / "openai.yaml"))
    if metadata.get("interface", {}).get("display_name") != "Lijie":
        fail("agents/openai.yaml has an unexpected display name")


def validate_readme() -> None:
    readme = read_utf8(ROOT / "README.md")
    links = [
        match.group(1)
        for match in re.finditer(r"\]\(([^)#]+)(?:#[^)]*)?\)", readme)
        if not match.group(1).startswith(("http://", "https://"))
    ]
    for link in links:
        if not (ROOT / link).exists():
            fail(f"README points to a missing local path: {link}")
    print(f"README local links: {len(links)} OK")


def validate_document_encoding() -> None:
    candidates = [ROOT / "README.md", ROOT / "CHANGELOG.md"]
    candidates.extend((ROOT / "docs").rglob("*.md"))
    candidates.extend((ROOT / "skill" / "lijie").rglob("*.md"))
    for path in candidates:
        read_utf8(path)
    print(f"UTF-8 documents: {len(candidates)} OK")


def validate_git_scope() -> None:
    tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True)
    leaked = [line for line in tracked.splitlines() if "source-snapshot" in line]
    if leaked:
        fail("source-snapshot must not be tracked: " + ", ".join(leaked))
    print("source-snapshot: not tracked")


if __name__ == "__main__":
    validate_skill()
    validate_readme()
    validate_document_encoding()
    validate_git_scope()
    print("Repository validation passed")
