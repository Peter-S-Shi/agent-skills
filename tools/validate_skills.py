"""Validate repository Skills without installing application dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
WINDOWS_PATH_RE = re.compile(r"(?i)(?:[a-z]:\\|[a-z]:/users/)")
UUID_RE = re.compile(r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")


def parse_frontmatter(text: str, source: Path) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{source}: missing YAML frontmatter")
    values: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip() or raw_line.startswith((" ", "\t")):
            continue
        key, separator, value = raw_line.partition(":")
        if separator:
            values[key.strip()] = value.strip().strip("\"'")
    return values


def validate_skill(raw_path: str) -> list[str]:
    errors: list[str] = []
    root = Path(raw_path).resolve()
    entry = root / "SKILL.md"
    if not root.is_dir() or not entry.is_file():
        return [f"{raw_path}: missing Skill directory or SKILL.md"]
    try:
        text = entry.read_text(encoding="utf-8")
        meta = parse_frontmatter(text, entry)
    except (OSError, UnicodeError, ValueError) as exc:
        return [str(exc)]
    name = meta.get("name", "")
    if name != root.name or not NAME_RE.fullmatch(name):
        errors.append(f"{entry}: name must equal lowercase hyphenated folder name")
    if not meta.get("description"):
        errors.append(f"{entry}: description is required")
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            errors.append(f"{path}: symlinks are not allowed in an independent Skill")
            continue
        if not path.is_file():
            continue
        try:
            body = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"{path}: expected UTF-8 text")
            continue
        if WINDOWS_PATH_RE.search(body) or UUID_RE.search(body):
            errors.append(f"{path}: possible private local path or Session identifier")
        if path.suffix.lower() != ".md":
            continue
        for raw_target in LINK_RE.findall(body):
            target = unquote(raw_target.strip().split()[0].strip("<>"))
            split = urlsplit(target)
            if target.startswith(("#", "mailto:")):
                continue
            if split.scheme == "file" or WINDOWS_PATH_RE.match(target) or target.startswith(("/", "\\")):
                errors.append(f"{path}: absolute local link is not allowed: {raw_target}")
                continue
            if split.scheme:
                continue
            relative = split.path
            if not relative:
                continue
            candidate = (path.parent / relative).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                errors.append(f"{path}: link escapes Skill root: {raw_target}")
                continue
            if not candidate.exists():
                errors.append(f"{path}: missing linked resource: {raw_target}")
    return errors


def main(arguments: list[str]) -> int:
    if not arguments:
        print("usage: validate_skills.py <skill-directory> [...]")
        return 2
    errors: list[str] = []
    for argument in arguments:
        errors.extend(validate_skill(argument))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Validated {len(arguments)} independently installable Skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
