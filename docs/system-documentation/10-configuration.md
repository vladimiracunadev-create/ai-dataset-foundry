# 10. Configuración

La configuración canónica es `BuildConfig`, creada por CLI/API o YAML (`examples/config.yaml`). No se leen variables de entorno. Los secretos no deben almacenarse en configuración; una URL con credenciales terminaría en manifest.

| Campo | Default | Obligatorio/rango | Consecuencia |
| --- | --- | --- | --- |
| `inputs` | `[]` | al ejecutar debe haber al menos uno | vacío desde CLI/API se rechaza; llamada directa puede producir dataset vacío |
| `out_dir` | `work/dataset` | ruta escribible | se crean/reemplazan artefactos con nombres fijos |
| `formats` | `[jsonl]` | jsonl/txt/parquet | parquet requiere extra |
| `recursive` | `true` | bool | recorre subdirectorios |
| `write_sqlite` | `true` | bool | crea catálogo SQLite |
| `chunk.strategy` | `paragraph` | paragraph/fixed/sentence/markdown | cambia límites/contexto |
| `chunk.size` | 1200 | 100..100000 | tamaño objetivo en caracteres |
| `chunk.overlap` | 120 | 0..20000; efectivo en fixed | se limita internamente a size-1 |
| `quality.min_chars` | 80 | >=1 | fragmentos menores se rechazan |
| `quality.max_control_ratio` | .02 | 0..1 | controles excesivos se rechazan |
| `quality.reject_secrets` | false | bool | API usa true por defecto |
| `dedup.enabled` | true | bool | desactivarlo conserva copias |
| `dedup.near_duplicate` | true | bool | activa SimHash |
| `dedup.simhash_distance` | 3 | 0..32 | umbral mayor descarta más |

```yaml
inputs:
  - examples/sample.txt
out_dir: work/example
formats: [jsonl, txt]
recursive: true
write_sqlite: true
chunk: {strategy: paragraph, size: 1200, overlap: 120}
quality: {min_chars: 80, max_control_ratio: 0.02, reject_secrets: true}
dedup: {enabled: true, near_duplicate: true, simhash_distance: 3}
```

No existen perfiles formales dev/test/prod ni feature flags externas. Las diferencias dependen del extra instalado y del punto de entrada. Configuración incorrecta puede descartar demasiado, consumir memoria/tiempo, sobrescribir outputs derivados o descargar fuentes no autorizadas. Valide con `foundry validate` y use un `out_dir` nuevo para corridas comparables.
