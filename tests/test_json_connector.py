import json
from pathlib import Path

from ai_dataset_foundry.connectors.text import load_json


def test_jsonl_document_ids_are_unique(tmp_path: Path):
    path = tmp_path / "items.jsonl"
    path.write_text("\n".join(json.dumps({"text": f"row {i}"}) for i in range(3)), encoding="utf-8")
    records = load_json(path)
    assert len({r.id for r in records}) == 3
