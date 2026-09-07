# Configuración

## Contrato completo

```yaml
inputs:
  - examples/payments-corpus
out_dir: work/payments-lab
formats: [jsonl, txt]
recursive: true
write_sqlite: true
chunk:
  strategy: markdown
  size: 1400
  overlap: 120
quality:
  min_chars: 80
  max_control_ratio: 0.02
  reject_secrets: true
dedup:
  enabled: true
  near_duplicate: true
  simhash_distance: 3
```

## Campos

| Ruta | Tipo / default | Propósito |
| --- | --- | --- |
| `inputs` | lista vacía | archivos, directorios, URL o repos Git |
| `out_dir` | `work/dataset` | directorio de artefactos derivados |
| `formats` | `[jsonl]` | `jsonl`, `txt`, `parquet` |
| `recursive` | `true` | recorre directorios |
| `write_sqlite` | `true` | crea catálogo `dataset.sqlite` |
| `chunk.strategy` | `paragraph` | `paragraph`, `sentence`, `markdown`, `fixed` |
| `chunk.size` | `1200` | objetivo en caracteres, entre 100 y 100.000 |
| `chunk.overlap` | `120` | solapamiento del modo fixed, 0 a 20.000 |
| `quality.min_chars` | `80` | rechaza piezas demasiado breves |
| `quality.max_control_ratio` | `0.02` | tolerancia de caracteres de control |
| `quality.reject_secrets` | `false` | rechaza flags de secreto; el ejemplo seguro lo activa |
| `dedup.enabled` | `true` | deduplicación exacta |
| `dedup.near_duplicate` | `true` | activa SimHash |
| `dedup.simhash_distance` | `3` | distancia Hamming, 0 a 32 |

## Estrategias de chunking

- `paragraph`: empaqueta párrafos hasta el objetivo; adecuado para prosa.
- `sentence`: conserva límites de oración detectados heurísticamente.
- `markdown`: intenta preservar secciones bajo encabezados; recomendado para el corpus de pagos.
- `fixed`: ventanas por caracteres con overlap; útil para pruebas controladas, menos semántico.

`size` no equivale a tokens. Mide el tokenizer del modelo downstream antes de fijar límites productivos.

## Prioridad CLI frente a YAML

Cuando se pasa `--config`, el archivo define inputs, output y formatos. No mezcles mentalmente flags de la otra ruta. Valida antes:

```bash
foundry validate examples/payments.yaml
foundry build --config examples/payments.yaml
```

## Fallos parciales

Un input fallido aparece en `manifest.json > ingestion_errors`; los inputs válidos continúan. En producción define un umbral: «dataset generado» no debe significar «dataset completo» si faltó una fuente obligatoria.

## Configuración segura

- No pongas tokens en YAML ni URL; usa un secret manager en conectores futuros.
- Mantén `work/`, `datasets/` y `exports/` fuera de Git.
- Usa `reject_secrets: true` como defensa auxiliar, no como permiso para ingerir material sensible.
- Guarda la configuración junto al manifiesto y controla cambios como código.
