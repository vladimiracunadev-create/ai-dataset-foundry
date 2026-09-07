"""Run the payment corpus through the real pipeline in a temporary directory."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_dataset_foundry.config import BuildConfig  # noqa: E402
from ai_dataset_foundry.pipeline import build_dataset  # noqa: E402


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="foundry-smoke-", ignore_cleanup_errors=True) as temporary:
        out = Path(temporary) / "payments"
        config = BuildConfig(
            inputs=[str(ROOT / "examples" / "payments-corpus")],
            out_dir=str(out),
            formats=["jsonl", "txt"],
            chunk={"strategy": "markdown", "size": 1400, "overlap": 120},
            quality={"min_chars": 80, "reject_secrets": True},
        )
        records, manifest = build_dataset(config)
        required = [
            out / "dataset.jsonl",
            out / "dataset.txt",
            out / "dataset.sqlite",
            out / "manifest.json",
        ]
        assert records, "the reference corpus produced no records"
        assert all(path.exists() for path in required), "one or more artifacts are missing"
        persisted = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
        assert persisted["chunks_exported"] == len(records)
        assert manifest["documents_loaded"] == 3
        print(f"[OK] {len(records)} chunks from 3 documents; JSONL/TXT/SQLite/manifest verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
