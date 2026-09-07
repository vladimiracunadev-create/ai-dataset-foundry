from __future__ import annotations

from pathlib import Path

from ai_dataset_foundry.models import DocumentRecord


def load_path(path: Path) -> list[DocumentRecord]:
    suffix = path.suffix.lower()
    if suffix in {".txt", ".md", ".rst", ".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".rs", ".go", ".php", ".rb", ".c", ".h", ".cpp", ".hpp", ".cs", ".kt", ".swift", ".scala", ".sh", ".ps1", ".sql", ".toml", ".yaml", ".yml", ".xml", ".css", ".scss", ".vue", ".svelte"}:
        from .text import load_text
        return load_text(path)
    if suffix in {".json", ".jsonl"}:
        from .text import load_json
        return load_json(path)
    if suffix == ".csv":
        from .text import load_csv
        return load_csv(path)
    if suffix == ".pdf":
        from .pdf import load_pdf
        return load_pdf(path)
    if suffix == ".docx":
        from .docx import load_docx
        return load_docx(path)
    if suffix in {".html", ".htm"}:
        from .html import load_html
        return load_html(path)
    return []


def ingest(locator: str, recursive: bool = True) -> list[DocumentRecord]:
    if locator.startswith(("http://", "https://")):
        if locator.endswith(".git") or "github.com/" in locator and not locator.endswith((".pdf", ".html")):
            if locator.endswith(".git"):
                from .git import load_git
                return load_git(locator)
        from .web import load_url
        return load_url(locator)

    path = Path(locator).expanduser()
    if not path.exists():
        raise FileNotFoundError(locator)
    if path.is_dir():
        if (path / ".git").exists():
            from .git import load_git
            return load_git(str(path))
        pattern = "**/*" if recursive else "*"
        records: list[DocumentRecord] = []
        for file in path.glob(pattern):
            if file.is_file():
                records.extend(load_path(file))
        return records
    return load_path(path)
