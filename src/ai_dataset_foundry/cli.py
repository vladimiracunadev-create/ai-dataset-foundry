from __future__ import annotations

import json
import webbrowser
from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console
from rich.table import Table

from ai_dataset_foundry.config import BuildConfig
from ai_dataset_foundry.pipeline import build_dataset

app = typer.Typer(help="Build auditable corpora for training, fine-tuning and RAG.", no_args_is_help=True)
console = Console()


@app.command()
def build(
    inputs: Annotated[Optional[list[str]], typer.Argument(help="Files, directories, URLs or .git URLs")] = None,
    out: Annotated[str, typer.Option("--out", "-o", help="Output directory")] = "work/dataset",
    format: Annotated[Optional[list[str]], typer.Option("--format", "-f", help="jsonl, txt or parquet")] = None,
    chunk_strategy: Annotated[str, typer.Option(help="paragraph, fixed, sentence or markdown")] = "paragraph",
    chunk_size: Annotated[int, typer.Option(help="Target chunk size in characters")] = 1200,
    overlap: Annotated[int, typer.Option(help="Overlap for fixed chunking")] = 120,
    config: Annotated[Optional[Path], typer.Option("--config", "-c", exists=True, dir_okay=False)] = None,
) -> None:
    """Run the full ingest-to-export pipeline."""
    if config:
        cfg = BuildConfig.from_yaml(config)
    else:
        if not inputs:
            raise typer.BadParameter("Provide at least one input or use --config")
        cfg = BuildConfig(
            inputs=inputs,
            out_dir=out,
            formats=format or ["jsonl"],
            chunk={"strategy": chunk_strategy, "size": chunk_size, "overlap": overlap},
        )
    records, manifest = build_dataset(cfg)
    console.print(f"[bold green]Dataset ready:[/bold green] {len(records)} chunks -> {cfg.out_dir}")
    if manifest["duplicates_removed"]:
        console.print(f"Duplicates removed: {manifest['duplicates_removed']}")
    if manifest["ingestion_errors"]:
        console.print(f"[yellow]Inputs with errors: {len(manifest['ingestion_errors'])}[/yellow]")


@app.command()
def stats(dataset: Annotated[Path, typer.Argument(exists=True, dir_okay=False)]) -> None:
    """Show basic statistics for a JSONL dataset."""
    if dataset.suffix.lower() != ".jsonl":
        raise typer.BadParameter("stats currently expects a .jsonl file")
    rows = []
    with open(dataset, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    chars = sum(len(row.get("text", "")) for row in rows)
    sources = len({row.get("document_id") for row in rows})
    table = Table(title="Dataset statistics")
    table.add_column("Metric")
    table.add_column("Value", justify="right")
    table.add_row("Chunks", f"{len(rows):,}")
    table.add_row("Documents", f"{sources:,}")
    table.add_row("Characters", f"{chars:,}")
    table.add_row("Approx. tokens", f"{round(chars / 4):,}")
    console.print(table)


@app.command()
def validate(config: Annotated[Path, typer.Argument(exists=True, dir_okay=False)]) -> None:
    """Validate a YAML configuration without running ingestion."""
    cfg = BuildConfig.from_yaml(config)
    console.print("[green]Configuration valid[/green]")
    console.print_json(data=cfg.model_dump())


@app.command()
def serve(
    host: Annotated[str, typer.Option(help="Bind address; keep 127.0.0.1 for local use")] = "127.0.0.1",
    port: Annotated[int, typer.Option(help="Local HTTP port")] = 8765,
    open_browser: Annotated[bool, typer.Option("--open/--no-open")] = True,
) -> None:
    """Start the compact local web interface."""
    try:
        import uvicorn
    except ImportError as exc:
        raise RuntimeError("UI support requires: uv sync --extra ui") from exc
    if open_browser:
        webbrowser.open(f"http://{host}:{port}")
    uvicorn.run("ai_dataset_foundry.webapp:create_app", host=host, port=port, factory=True)


@app.command()
def desktop() -> None:
    """Open the Windows desktop interface backed by the local server."""
    from ai_dataset_foundry.desktop import main

    main()


if __name__ == "__main__":
    app()
