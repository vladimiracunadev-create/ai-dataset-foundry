from __future__ import annotations

from pathlib import Path

from ai_dataset_foundry.models import ChunkRecord


def export_txt(records: list[ChunkRecord], path: Path) -> None:
    path.write_text("\n\n".join(record.text for record in records), encoding="utf-8")
