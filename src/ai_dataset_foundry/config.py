from __future__ import annotations

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, Field


class ChunkConfig(BaseModel):
    strategy: Literal["paragraph", "fixed", "sentence", "markdown"] = "paragraph"
    size: int = Field(default=1200, ge=100, le=100_000)
    overlap: int = Field(default=120, ge=0, le=20_000)


class QualityConfig(BaseModel):
    min_chars: int = Field(default=80, ge=1)
    max_control_ratio: float = Field(default=0.02, ge=0, le=1)
    reject_secrets: bool = False


class DedupConfig(BaseModel):
    enabled: bool = True
    near_duplicate: bool = True
    simhash_distance: int = Field(default=3, ge=0, le=32)


class BuildConfig(BaseModel):
    inputs: list[str] = Field(default_factory=list)
    out_dir: str = "work/dataset"
    formats: list[Literal["jsonl", "txt", "parquet"]] = Field(default_factory=lambda: ["jsonl"])
    recursive: bool = True
    write_sqlite: bool = True
    chunk: ChunkConfig = Field(default_factory=ChunkConfig)
    quality: QualityConfig = Field(default_factory=QualityConfig)
    dedup: DedupConfig = Field(default_factory=DedupConfig)

    @classmethod
    def from_yaml(cls, path: str | Path) -> "BuildConfig":
        with open(path, "r", encoding="utf-8") as fh:
            return cls.model_validate(yaml.safe_load(fh) or {})
