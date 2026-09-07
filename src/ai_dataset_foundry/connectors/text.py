from __future__ import annotations

import csv
import json
from pathlib import Path

from ai_dataset_foundry.models import DocumentRecord, SourceInfo
from ai_dataset_foundry.utils.hashing import sha256_file, stable_id


def _record(path: Path, text: str, kind: str, metadata: dict | None = None) -> DocumentRecord:
    source_hash = sha256_file(path)
    return DocumentRecord(
        id=stable_id("doc", str(path.resolve()), source_hash),
        text=text,
        source=SourceInfo(kind=kind, locator=str(path), title=path.name),
        metadata=metadata or {},
        source_sha256=source_hash,
    )


def load_text(path: Path) -> list[DocumentRecord]:
    return [_record(path, path.read_text(encoding="utf-8", errors="replace"), path.suffix.lstrip(".") or "txt")]


def load_json(path: Path) -> list[DocumentRecord]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    items = []
    if path.suffix.lower() == ".jsonl":
        for line_no, line in enumerate(raw.splitlines(), 1):
            if not line.strip():
                continue
            obj = json.loads(line)
            text = obj.get("text") if isinstance(obj, dict) else None
            if text is None:
                text = json.dumps(obj, ensure_ascii=False)
            record = _record(path, str(text), "jsonl", {"line": line_no, "original": obj})
            record.id = stable_id("doc", str(path.resolve()), record.source_sha256, f"line:{line_no}")
            items.append(record)
        return items
    obj = json.loads(raw)
    seq = obj if isinstance(obj, list) else [obj]
    for idx, item in enumerate(seq):
        text = item.get("text") if isinstance(item, dict) else None
        if text is None:
            text = json.dumps(item, ensure_ascii=False)
        record = _record(path, str(text), "json", {"index": idx, "original": item})
        record.id = stable_id("doc", str(path.resolve()), record.source_sha256, f"index:{idx}")
        items.append(record)
    return items


def load_csv(path: Path) -> list[DocumentRecord]:
    source_hash = sha256_file(path)
    records = []
    with open(path, newline="", encoding="utf-8-sig", errors="replace") as fh:
        reader = csv.DictReader(fh)
        for idx, row in enumerate(reader):
            text = row.get("text") or "\n".join(f"{k}: {v}" for k, v in row.items() if v)
            records.append(DocumentRecord(
                id=stable_id("doc", str(path.resolve()), source_hash, str(idx)),
                text=text,
                source=SourceInfo(kind="csv", locator=str(path), title=path.name),
                metadata={"row": idx + 2, "original": row},
                source_sha256=source_hash,
            ))
    return records
