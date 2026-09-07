from pathlib import Path

from ai_dataset_foundry.models import ChunkRecord
from .jsonl import export_jsonl
from .text import export_txt


def export_records(records: list[ChunkRecord], out_dir: Path, formats: list[str]) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for fmt in dict.fromkeys(formats):
        if fmt == "jsonl":
            path = out_dir / "dataset.jsonl"
            export_jsonl(records, path)
        elif fmt == "txt":
            path = out_dir / "dataset.txt"
            export_txt(records, path)
        elif fmt == "parquet":
            from .parquet import export_parquet
            path = out_dir / "dataset.parquet"
            export_parquet(records, path)
        else:
            raise ValueError(f"Unsupported export format: {fmt}")
        outputs.append(path)
    return outputs

__all__ = ["export_records"]
