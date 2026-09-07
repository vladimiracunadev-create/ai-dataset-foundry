from __future__ import annotations

import json
from pathlib import Path

from ai_dataset_foundry.models import ChunkRecord


def export_jsonl(records: list[ChunkRecord], path: Path) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record.to_dict(), ensure_ascii=False) + "\n")
