from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from ai_dataset_foundry.models import ChunkRecord

_SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS dataset_meta (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS chunks (
  id TEXT PRIMARY KEY,
  document_id TEXT NOT NULL,
  text TEXT NOT NULL,
  source_kind TEXT NOT NULL,
  source_locator TEXT NOT NULL,
  source_title TEXT,
  source_license TEXT,
  metadata_json TEXT NOT NULL,
  source_sha256 TEXT NOT NULL,
  content_sha256 TEXT NOT NULL,
  quality_score REAL NOT NULL,
  quality_reasons_json TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_chunks_document_id ON chunks(document_id);
CREATE INDEX IF NOT EXISTS idx_chunks_source_kind ON chunks(source_kind);
CREATE INDEX IF NOT EXISTS idx_chunks_content_sha256 ON chunks(content_sha256);
"""


def write_sqlite(records: list[ChunkRecord], manifest: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as conn:
        conn.executescript(_SCHEMA)
        conn.execute("DELETE FROM chunks")
        conn.execute("DELETE FROM dataset_meta")
        conn.executemany(
            "INSERT INTO dataset_meta(key, value) VALUES(?, ?)",
            [("manifest", json.dumps(manifest, ensure_ascii=False))],
        )
        conn.executemany(
            """INSERT INTO chunks(
                id, document_id, text, source_kind, source_locator, source_title, source_license,
                metadata_json, source_sha256, content_sha256, quality_score, quality_reasons_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            [
                (
                    record.id, record.document_id, record.text, record.source.kind, record.source.locator,
                    record.source.title, record.source.license,
                    json.dumps(record.metadata, ensure_ascii=False),
                    record.provenance.source_sha256, record.provenance.content_sha256,
                    record.quality.score, json.dumps(record.quality.reasons, ensure_ascii=False),
                )
                for record in records
            ],
        )
