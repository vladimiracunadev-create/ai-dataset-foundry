"""Audit links, versions, workflow pins and documentation drift."""

from __future__ import annotations

import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
ACTION = re.compile(r"uses:\s+[^\s@]+@([^\s#]+)")
FULL_SHA = re.compile(r"[0-9a-f]{40}")


def local_target(document: Path, raw: str) -> Path | None:
    target = raw.split("#", 1)[0].strip()
    if not target or "://" in target or target.startswith(("mailto:", "#")):
        return None
    return (document.parent / target).resolve()


def main() -> int:
    failures: list[str] = []
    markdown = [p for p in sorted(ROOT.rglob("*.md")) if not {".git", ".venv"} & set(p.parts)]
    for document in markdown:
        text = document.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = local_target(document, raw)
            if target is not None and not target.exists():
                failures.append(f"broken link: {document.relative_to(ROOT)} -> {raw}")
        if "mÃ" in text or "ðŸ" in text or "â€" in text:
            failures.append(f"possible mojibake: {document.relative_to(ROOT)}")

    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    version = project["project"]["version"]
    init_text = (ROOT / "src/ai_dataset_foundry/__init__.py").read_text(encoding="utf-8")
    android_text = (ROOT / "android/app/build.gradle.kts").read_text(encoding="utf-8")
    for source, text in {"__init__": init_text, "Android": android_text, "STATUS": (ROOT / "STATUS.md").read_text(encoding="utf-8")}.items():
        if version not in text:
            failures.append(f"current version {version} missing from {source}")

    workflows = sorted((ROOT / ".github/workflows").glob("*.yml"))
    expected = {"ci.yml", "pages.yml", "release.yml", "security.yml"}
    found = {path.name for path in workflows}
    if found != expected:
        failures.append(f"workflow inventory differs: expected {sorted(expected)}, found {sorted(found)}")
    for workflow in workflows:
        for ref in ACTION.findall(workflow.read_text(encoding="utf-8")):
            if not FULL_SHA.fullmatch(ref):
                failures.append(f"unpinned action: {workflow.name} -> {ref}")

    system_docs = ROOT / "docs" / "system-documentation"
    names = [
        "system-overview", "installation-and-execution", "architecture", "code-map",
        "technical-reference", "deep-code-explanation", "database", "data-flow",
        "apis-and-integrations", "configuration", "security", "testing-and-quality",
        "deployment-and-operations", "troubleshooting", "risks-and-technical-debt",
        "glossary", "executive-summary", "new-developer-guide", "traceability-matrix",
    ]
    required_sources = [system_docs / "README.md"] + [
        system_docs / f"{number:02d}-{name}.md" for number, name in enumerate(names, 1)
    ]
    for source in required_sources:
        if not source.is_file() or source.stat().st_size < 300:
            failures.append(f"missing or empty system document: {source.relative_to(ROOT)}")
        pdf = system_docs / "pdf" / f"{source.stem}.pdf"
        if not pdf.is_file() or pdf.stat().st_size < 1000:
            failures.append(f"missing or empty PDF: {pdf.relative_to(ROOT)}")
    if failures:
        print("Repository coherence verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    tests = len(list((ROOT / "tests").glob("test_*.py")))
    print(f"[OK] version {version}; {len(markdown)} Markdown; {tests} Python test files; {len(workflows)} pinned workflows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
