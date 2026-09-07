from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from ai_dataset_foundry.config import BuildConfig
from ai_dataset_foundry.connectors import ingest
from ai_dataset_foundry.exporters import export_records
from ai_dataset_foundry.models import ChunkRecord, Provenance
from ai_dataset_foundry.processors import Deduplicator, assess_quality, chunk_text, clean_text, normalize_text
from ai_dataset_foundry.utils.hashing import sha256_text, stable_id


def build_dataset(config: BuildConfig) -> tuple[list[ChunkRecord], dict]:
    documents = []
    ingestion_errors: list[dict[str, str]] = []
    for locator in config.inputs:
        try:
            documents.extend(ingest(locator, recursive=config.recursive))
        except Exception as exc:
            ingestion_errors.append({"input": locator, "error": str(exc)})

    dedup = Deduplicator(
        near_duplicate=config.dedup.near_duplicate,
        max_distance=config.dedup.simhash_distance,
    )
    chunks: list[ChunkRecord] = []
    rejected = Counter()
    duplicate_count = 0

    for document in documents:
        text = clean_text(normalize_text(document.text))
        for index, piece in enumerate(chunk_text(text, config.chunk.strategy, config.chunk.size, config.chunk.overlap)):
            piece = piece.strip()
            if not piece:
                continue
            if config.dedup.enabled and dedup.is_duplicate(piece):
                duplicate_count += 1
                continue
            quality = assess_quality(piece, config.quality)
            if not quality.accepted:
                rejected.update(quality.reasons)
                continue
            content_hash = sha256_text(piece)
            metadata = dict(document.metadata)
            metadata["chunk_index"] = index
            chunks.append(ChunkRecord(
                id=stable_id("chunk", document.id, str(index), content_hash),
                document_id=document.id,
                text=piece,
                source=document.source,
                metadata=metadata,
                provenance=Provenance(
                    source_sha256=document.source_sha256,
                    content_sha256=content_hash,
                ),
                quality=quality,
            ))

    out_dir = Path(config.out_dir)
    outputs = export_records(chunks, out_dir, config.formats)
    manifest = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "inputs": config.inputs,
        "documents_loaded": len(documents),
        "chunks_exported": len(chunks),
        "duplicates_removed": duplicate_count,
        "rejected": dict(rejected),
        "ingestion_errors": ingestion_errors,
        "formats": config.formats,
        "outputs": [str(path) for path in outputs],
        "settings": config.model_dump(),
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    if config.write_sqlite:
        from ai_dataset_foundry.storage import write_sqlite
        sqlite_path = out_dir / "dataset.sqlite"
        write_sqlite(chunks, manifest, sqlite_path)
        manifest["sqlite"] = str(sqlite_path)
        (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return chunks, manifest
