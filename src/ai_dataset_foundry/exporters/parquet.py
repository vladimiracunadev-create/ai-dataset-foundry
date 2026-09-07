from __future__ import annotations

from pathlib import Path

from ai_dataset_foundry.models import ChunkRecord


def export_parquet(records: list[ChunkRecord], path: Path) -> None:
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq
    except ImportError as exc:
        raise RuntimeError("Parquet support requires: uv sync --extra parquet") from exc

    table = pa.Table.from_pylist([record.to_dict() for record in records])
    pq.write_table(table, path, compression="zstd")
