# Contrato del dataset

## Registro JSONL

Cada línea es un `ChunkRecord` independiente:

```json
{
  "id": "chunk_0123456789abcdefabcd",
  "document_id": "doc_0123456789abcdefabcd",
  "text": "Contenido normalizado y aceptado.",
  "source": {
    "kind": "md",
    "locator": "examples/payments-corpus/cards.md",
    "title": "cards.md",
    "license": null
  },
  "metadata": {"chunk_index": 0},
  "provenance": {
    "source_sha256": "...",
    "content_sha256": "..."
  },
  "quality": {
    "score": 1.0,
    "accepted": true,
    "reasons": []
  }
}
```

| Campo | Garantía |
| --- | --- |
| `id` | estable para documento, índice y contenido iguales |
| `document_id` | enlaza con unidad extraída, no necesariamente archivo completo |
| `text` | UTF-8 normalizado y transformado |
| `source` | procedencia descriptiva; `license` puede faltar |
| `metadata` | extensible por conector y contiene `chunk_index` |
| `source_sha256` | hash de bytes originales cuando el conector dispone de ellos |
| `content_sha256` | hash del texto final del chunk |
| `quality` | decisión heurística y razones/flags |

## Manifiesto

`manifest.json` registra versión de esquema, timestamp UTC, inputs, documentos cargados, chunks exportados, duplicados, rechazos, errores, formatos, outputs y snapshot de settings. Si SQLite está activo incluye su ruta.

El manifiesto prueba **qué ejecutó el pipeline**, no licencia, veracidad ni completitud de la fuente. Para reproducibilidad fuerte faltan versiones de dependencias, commit de la fuente, entorno y checksum del artefacto final; son evolución planificada.

## SQLite

`dataset.sqlite` contiene `dataset_meta` y `chunks`, con índices por documento, tipo de fuente y hash de contenido. Es un catálogo local, no un vector store ni warehouse.

## Mapping downstream

Fine-tuning requiere transformar estos registros genéricos al contrato del proveedor (`messages`, `prompt/completion` u otro). RAG requiere embeddings, estrategia de retrieval, filtros y evaluación. No mezcles esa proyección con el corpus canónico: conserva un nivel neutral trazable.

## Datos de pagos prohibidos

El corpus de referencia solo usa conceptos y referencias sintéticas. No almacenes PAN, SAD/CVV, PIN, track data, credenciales bancarias, tokens vivos, claves de webhook, documentos KYC ni transacciones de clientes. Hashing no anonimiza datos de baja entropía.
