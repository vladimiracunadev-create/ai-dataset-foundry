from fastapi.testclient import TestClient

from ai_dataset_foundry import webapp


def test_ui_health_and_build(tmp_path, monkeypatch):
    monkeypatch.setattr(webapp, "RUNS_DIR", tmp_path / "runs")
    client = TestClient(webapp.create_app())
    health = client.get("/api/health")
    assert health.status_code == 200
    assert health.json()["version"] == "0.2.0"

    content = ("Este documento sintético explica cómo preparar información trazable. " * 8).encode()
    response = client.post(
        "/api/build",
        files={"files": ("guide.txt", content, "text/plain")},
        data={"formats": '["jsonl","txt"]', "locators": "[]", "chunk_size": "300"},
    )
    assert response.status_code == 200, response.text
    result = response.json()
    assert result["documents"] == 1
    assert result["chunks"] >= 1
    assert {"dataset.jsonl", "dataset.txt", "manifest.json", "dataset.sqlite"} <= set(result["artifacts"])
    artifact = client.get(f"/api/runs/{result['run_id']}/artifacts/dataset.jsonl")
    assert artifact.status_code == 200
    assert b'"provenance"' in artifact.content
