from __future__ import annotations

from pathlib import Path

from ai_dataset_foundry.models import DocumentRecord, SourceInfo
from ai_dataset_foundry.utils.hashing import sha256_file, stable_id


def load_html(path: Path) -> list[DocumentRecord]:
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise RuntimeError("HTML support requires: uv sync --extra web") from exc

    source_hash = sha256_file(path)
    html = path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "template"]):
        tag.decompose()
    title = soup.title.string.strip() if soup.title and soup.title.string else path.name
    text = "\n".join(s.strip() for s in soup.stripped_strings if s.strip())
    return [DocumentRecord(
        id=stable_id("doc", str(path.resolve()), source_hash),
        text=text,
        source=SourceInfo(kind="html", locator=str(path), title=title),
        metadata={},
        source_sha256=source_hash,
    )]
