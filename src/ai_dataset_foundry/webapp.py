from __future__ import annotations

import asyncio
import json
import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, HTMLResponse

from ai_dataset_foundry import __version__
from ai_dataset_foundry.config import BuildConfig
from ai_dataset_foundry.pipeline import build_dataset

ROOT = Path.cwd()
RUNS_DIR = ROOT / "work" / "ui-runs"
UI_FILE = Path(__file__).parent / "ui" / "index.html"
MAX_UPLOAD_BYTES = 50 * 1024 * 1024


def create_app() -> FastAPI:
    app = FastAPI(title="AI Dataset Foundry", version=__version__, docs_url=None, redoc_url=None)

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        return UI_FILE.read_text(encoding="utf-8")

    @app.get("/api/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "version": __version__}

    @app.post("/api/build")
    async def build(
        files: list[UploadFile] = File(default=[]),
        locators: str = Form(default="[]"),
        formats: str = Form(default='["jsonl"]'),
        chunk_strategy: str = Form(default="paragraph"),
        chunk_size: int = Form(default=1200),
        overlap: int = Form(default=120),
        reject_secrets: bool = Form(default=True),
    ) -> dict:
        run_id = uuid4().hex[:12]
        run_dir = RUNS_DIR / run_id
        input_dir = run_dir / "inputs"
        output_dir = run_dir / "output"
        input_dir.mkdir(parents=True, exist_ok=False)
        try:
            source_list = _decode_list(locators, "locators")
            format_list = _decode_list(formats, "formats")
            for upload in files:
                safe_name = Path(upload.filename or "upload.bin").name
                destination = input_dir / safe_name
                if destination.exists():
                    destination = input_dir / f"{uuid4().hex[:8]}-{safe_name}"
                size = await _save_upload(upload, destination)
                if size > MAX_UPLOAD_BYTES:
                    raise HTTPException(413, f"{safe_name} exceeds the 50 MiB demo limit")
                source_list.append(str(destination))
            if not source_list:
                raise HTTPException(400, "Add at least one file, directory, URL or Git repository")
            config = BuildConfig(
                inputs=source_list,
                out_dir=str(output_dir),
                formats=format_list,
                chunk={"strategy": chunk_strategy, "size": chunk_size, "overlap": overlap},
                quality={"min_chars": 80, "reject_secrets": reject_secrets},
            )
            records, manifest = await asyncio.to_thread(build_dataset, config)
            artifacts = [path.name for path in output_dir.iterdir() if path.is_file()]
            return {
                "run_id": run_id,
                "documents": manifest["documents_loaded"],
                "chunks": len(records),
                "duplicates": manifest["duplicates_removed"],
                "rejected": manifest["rejected"],
                "errors": manifest["ingestion_errors"],
                "artifacts": artifacts,
            }
        except HTTPException:
            shutil.rmtree(run_dir, ignore_errors=True)
            raise
        except Exception as exc:
            shutil.rmtree(run_dir, ignore_errors=True)
            raise HTTPException(400, str(exc)) from exc

    @app.get("/api/runs/{run_id}/artifacts/{name}")
    def artifact(run_id: str, name: str) -> FileResponse:
        if not run_id.isalnum() or Path(name).name != name:
            raise HTTPException(400, "Invalid artifact path")
        path = RUNS_DIR / run_id / "output" / name
        if not path.is_file():
            raise HTTPException(404, "Artifact not found")
        return FileResponse(path, filename=name)

    return app


def _decode_list(raw: str, field: str) -> list[str]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise HTTPException(400, f"{field} must be a JSON array") from exc
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise HTTPException(400, f"{field} must be a JSON array of strings")
    return [item.strip() for item in value if item.strip()]


async def _save_upload(upload: UploadFile, destination: Path) -> int:
    size = 0
    with destination.open("wb") as target:
        while block := await upload.read(1024 * 1024):
            size += len(block)
            if size > MAX_UPLOAD_BYTES:
                break
            target.write(block)
    await upload.close()
    return size
