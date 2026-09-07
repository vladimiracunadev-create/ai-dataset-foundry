from __future__ import annotations

import re


def _fixed(text: str, size: int, overlap: int) -> list[str]:
    if not text:
        return []
    overlap = min(overlap, max(0, size - 1))
    step = size - overlap
    return [text[i:i + size].strip() for i in range(0, len(text), step) if text[i:i + size].strip()]


def _pack(parts: list[str], size: int) -> list[str]:
    chunks: list[str] = []
    buf: list[str] = []
    count = 0
    for part in parts:
        part = part.strip()
        if not part:
            continue
        extra = len(part) + (2 if buf else 0)
        if buf and count + extra > size:
            chunks.append("\n\n".join(buf))
            buf, count = [], 0
        if len(part) > size and not buf:
            chunks.extend(_fixed(part, size, 0))
            continue
        buf.append(part)
        count += extra
    if buf:
        chunks.append("\n\n".join(buf))
    return chunks


def chunk_text(text: str, strategy: str, size: int, overlap: int = 0) -> list[str]:
    if strategy == "fixed":
        return _fixed(text, size, overlap)
    if strategy == "sentence":
        sentences = re.split(r"(?<=[.!?])\s+", text)
        return _pack(sentences, size)
    if strategy == "markdown":
        sections = re.split(r"(?=^#{1,6}\s+)", text, flags=re.MULTILINE)
        return _pack(sections, size)
    paragraphs = re.split(r"\n\s*\n", text)
    return _pack(paragraphs, size)
