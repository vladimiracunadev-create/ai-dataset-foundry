import json
from pathlib import Path

from ai_dataset_foundry.config import BuildConfig
from ai_dataset_foundry.pipeline import build_dataset


def test_pipeline_text(tmp_path: Path):
    source = tmp_path / "source.txt"
    source.write_text("Paragraph one with enough text to pass quality. " * 4 + "\n\n" + "Paragraph two with enough text to pass quality. " * 4, encoding="utf-8")
    out = tmp_path / "out"
    config = BuildConfig(
        inputs=[str(source)],
        out_dir=str(out),
        formats=["jsonl", "txt"],
        chunk={"strategy": "paragraph", "size": 500, "overlap": 0},
        quality={"min_chars": 20, "max_control_ratio": 0.02, "reject_secrets": False},
    )
    records, manifest = build_dataset(config)
    assert records
    assert (out / "dataset.jsonl").exists()
    assert (out / "dataset.txt").exists()
    assert (out / "manifest.json").exists()
    assert (out / "dataset.sqlite").exists()
    parsed = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    assert parsed["chunks_exported"] == len(records)
    assert manifest["documents_loaded"] == 1
