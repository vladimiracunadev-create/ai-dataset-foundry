"""Small end-to-end build against committed synthetic content."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from ai_dataset_foundry.config import BuildConfig
from ai_dataset_foundry.pipeline import build_dataset

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "work" / "smoke"


def main() -> int:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    config = BuildConfig(
        inputs=[str(ROOT / "examples" / "sample.txt")],
        out_dir=str(OUTPUT),
        formats=["jsonl", "txt"],
        quality={"min_chars": 40, "reject_secrets": True},
    )
    records, manifest = build_dataset(config)
    required = ["dataset.jsonl", "dataset.txt", "dataset.sqlite", "manifest.json"]
    missing = [name for name in required if not (OUTPUT / name).is_file()]
    lines = (OUTPUT / "dataset.jsonl").read_text(encoding="utf-8").splitlines()
    valid = [json.loads(line) for line in lines]
    if missing or not records or len(valid) != len(records) or manifest["ingestion_errors"]:
        raise SystemExit(f"Smoke failed: missing={missing}, records={len(records)}, errors={manifest['ingestion_errors']}")
    print(f"[OK] {manifest['documents_loaded']} document; {len(records)} chunks; {len(required)} artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
