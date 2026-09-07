from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from ai_dataset_foundry.connectors.router import load_path
from ai_dataset_foundry.models import DocumentRecord


_ALLOWED_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".rs", ".go", ".php", ".rb",
    ".c", ".h", ".cpp", ".hpp", ".cs", ".kt", ".swift", ".scala", ".sh", ".ps1",
    ".sql", ".md", ".txt", ".rst", ".toml", ".yaml", ".yml", ".json", ".xml",
    ".html", ".css", ".scss", ".vue", ".svelte", ".ipynb",
}


def _load_repo(path: Path, repo_locator: str) -> list[DocumentRecord]:
    records: list[DocumentRecord] = []
    for file in path.rglob("*"):
        if not file.is_file() or ".git" in file.parts:
            continue
        if file.suffix.lower() not in _ALLOWED_EXTENSIONS:
            continue
        try:
            loaded = load_path(file)
        except Exception:
            continue
        rel = str(file.relative_to(path))
        for record in loaded:
            record.source.kind = "git"
            record.source.locator = f"{repo_locator}#{rel}"
            record.metadata["repository"] = repo_locator
            record.metadata["path"] = rel
            records.append(record)
    return records


def load_git(locator: str) -> list[DocumentRecord]:
    local = Path(locator)
    if local.exists() and (local / ".git").exists():
        return _load_repo(local, str(local.resolve()))

    if shutil.which("git") is None:
        raise RuntimeError("git executable is required for remote repository ingestion")

    with tempfile.TemporaryDirectory(prefix="foundry-git-") as temp:
        dest = Path(temp) / "repo"
        subprocess.run(
            ["git", "clone", "--depth", "1", "--filter=blob:none", locator, str(dest)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return _load_repo(dest, locator)
