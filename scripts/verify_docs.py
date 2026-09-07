"""Check local Markdown links and current repository facts used by documentation."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def local_target(document: Path, raw: str) -> Path | None:
    target = raw.split("#", 1)[0].strip()
    if not target or "://" in target or target.startswith(("mailto:", "#")):
        return None
    return (document.parent / target).resolve()


def main() -> int:
    failures: list[str] = []
    markdown = sorted(ROOT.rglob("*.md"))
    for document in markdown:
        if any(part in {".git", ".venv"} for part in document.parts):
            continue
        text = document.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = local_target(document, raw)
            if target is not None and not target.exists():
                failures.append(f"{document.relative_to(ROOT)} -> {raw}")

    tests = list((ROOT / "tests").glob("test_*.py"))
    workflows = list((ROOT / ".github" / "workflows").glob("*.yml"))
    if len(tests) != 5:
        failures.append(f"STATUS expects 5 test files; found {len(tests)}")
    if len(workflows) != 3:
        failures.append(f"STATUS expects 3 workflows; found {len(workflows)}")

    if failures:
        print("Documentation verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"[OK] {len(markdown)} Markdown files, local links, 5 test files and 3 workflows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
