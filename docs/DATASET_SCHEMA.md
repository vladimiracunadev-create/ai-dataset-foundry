# Contrato de datos

JSONL es la representación canónica: un objeto JSON autónomo por línea. Esto permite streaming, particionado y recuperación puntual sin cargar todo el corpus.

```json
{
  "id": "chunk_…",
  "document_id": "doc_…",
  "text": "Contenido normalizado",
  "source": {"kind": "pdf", "locator": "manual.pdf", "title": "Manual", "license": null},
  "metadata": {"page": 4, "chunk_index": 2},
  "provenance": {"source_sha256": "…", "content_sha256": "…"},
  "quality": {"score": 1.0, "accepted": true, "reasons": []}
}
```

## Semántica

`id` identifica el fragmento de manera estable para la misma fuente, índice y contenido. `document_id` permite reagrupar. `source` describe adquisición, no autoría. `metadata` conserva atributos específicos del conector. Los hashes detectan cambios; no prueban autenticidad ni derechos. `quality` registra la decisión automática aplicada durante ese build.

## Artefactos

- `dataset.jsonl`: intercambio y streaming.
- `dataset.txt`: inspección o tokenización simple; pierde estructura rica.
- `dataset.parquet`: análisis columnar a escala con PyArrow.
- `dataset.sqlite`: catálogo consultable y manifest local.
- `manifest.json`: recibo del proceso; es obligatorio para auditoría.

Los consumidores deben validar `schema_version`, tratar metadata como extensible y no inferir que un registro aceptado es verdadero o apropiado para cualquier objetivo.
