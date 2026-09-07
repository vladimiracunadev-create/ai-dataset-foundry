"""Verify the local prerequisites without changing the environment."""

from __future__ import annotations

import importlib.util
import shutil
import sys


def main() -> int:
    checks = {
        "Python >= 3.11": sys.version_info >= (3, 11),
        "Git executable": shutil.which("git") is not None,
        "pydantic": importlib.util.find_spec("pydantic") is not None,
        "typer": importlib.util.find_spec("typer") is not None,
        "rich": importlib.util.find_spec("rich") is not None,
        "yaml": importlib.util.find_spec("yaml") is not None,
    }
    for name, passed in checks.items():
        print(f"[{'OK' if passed else 'FAIL'}] {name}")
    optional = {
        "PDF (pypdf)": "pypdf",
        "DOCX (docx)": "docx",
        "Web HTML (bs4)": "bs4",
        "Web extraction (trafilatura)": "trafilatura",
        "Parquet (pyarrow)": "pyarrow",
    }
    for name, module in optional.items():
        available = importlib.util.find_spec(module) is not None
        print(f"[{'OPTIONAL' if available else 'SKIP'}] {name}")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
