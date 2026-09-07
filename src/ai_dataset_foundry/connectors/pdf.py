from __future__ import annotations

from pathlib import Path

from ai_dataset_foundry.models import DocumentRecord, SourceInfo
from ai_dataset_foundry.utils.hashing import sha256_file, stable_id


def load_pdf(path: Path) -> list[DocumentRecord]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("PDF support requires: uv sync --extra documents") from exc

    source_hash = sha256_file(path)
    reader = PdfReader(str(path))
    records: list[DocumentRecord] = []
    for page_no, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if not text.strip():
            continue
        records.append(DocumentRecord(
            id=stable_id("doc", str(path.resolve()), source_hash, f"page:{page_no}"),
            text=text,
            source=SourceInfo(kind="pdf", locator=str(path), title=path.name),
            metadata={"page": page_no, "pages": len(reader.pages)},
            source_sha256=source_hash,
        ))
    return records
