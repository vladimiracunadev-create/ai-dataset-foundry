# 05. Referencia técnica

## Configuración y contratos

| Símbolo | Firma/campos y propósito | Validación / efecto |
| --- | --- | --- |
| `ChunkConfig` | `strategy`, `size=1200`, `overlap=120` | estrategia literal; tamaño 100..100000; overlap 0..20000 |
| `QualityConfig` | `min_chars=80`, `max_control_ratio=.02`, `reject_secrets=False` | rangos Pydantic |
| `DedupConfig` | `enabled`, `near_duplicate`, `simhash_distance=3` | distancia 0..32 |
| `BuildConfig` | inputs, out_dir, formats, recursive, write_sqlite y subconfigs | `from_yaml(path)` puede lanzar I/O, YAML o ValidationError |
| `DocumentRecord` | id, text, source, metadata, source_sha256 | salida común de adquisición |
| `ChunkRecord.to_dict()` | `() -> dict` | serialización recursiva con `asdict` |

## Funciones del núcleo

| Símbolo | Entrada → retorno | Llama / efectos / riesgos |
| --- | --- | --- |
| `build_dataset(config)` | `BuildConfig → (list[ChunkRecord], dict)` | ingiere, transforma y escribe artefactos; aísla sólo errores de locator |
| `ingest(locator, recursive=True)` | texto → documentos | red/Git/FS; `FileNotFoundError`; directorios omiten extensiones desconocidas |
| `load_path(path)` | Path → documentos | despacho por extensión; desconocida devuelve `[]` |
| `chunk_text(text,strategy,size,overlap=0)` | texto → piezas | estrategia desconocida cae a párrafos; normalmente Pydantic lo evita |
| `Deduplicator.is_duplicate(text)` | texto → bool | muta sets/lista; exacto y SimHash; memoria por build |
| `assess_quality(text,config)` | texto → `QualityResult` | marca/rechaza por longitud, controles y posible secreto |
| `export_records(records,out_dir,formats)` | registros → rutas | crea directorio; formato inválido `ValueError`; salida parcial posible |
| `write_sqlite(records,manifest,path)` | → `None` | crea esquema, borra tablas y reinserta en transacción SQLite |
| `sha256_bytes/text/file` | datos → hex SHA-256 | lectura de archivo puede fallar |
| `stable_id(prefix,*parts)` | componentes → ID | usa separador U+001F y 20 hex; riesgo teórico de colisión por truncado |

Los loaders locales generan uno o varios `DocumentRecord`: JSON array/JSONL y CSV generan registros por elemento/fila; PDF por página; DOCX combina párrafos/tablas; HTML y web extraen texto visible; Git reetiqueta los registros con repo y ruta. Consulte [Conectores](../CONNECTORS.md) para límites detallados.

## API y comandos

| Interfaz | Contrato |
| --- | --- |
| `GET /` | HTML embebido; 200 o error de lectura del recurso |
| `GET /api/health` | `{"status":"ok","version":"0.2.0"}` |
| `POST /api/build` | multipart: files, locators JSON, formats JSON, chunk settings, reject_secrets; 200 resultado, 400 validación/build, 413 carga |
| `GET /api/runs/{run_id}/artifacts/{name}` | descarga; 400 ruta inválida, 404 ausente |
| `foundry build` | pipeline por argumentos o YAML |
| `foundry stats` | métricas simples de JSONL |
| `foundry validate` | valida YAML sin ingerir |
| `foundry serve/desktop` | UI localhost / ventana Windows |

No hay variables de entorno consumidas por el código. Constantes relevantes: `RUNS_DIR`, `UI_FILE`, `MAX_UPLOAD_BYTES=50 MiB`, `_ALLOWED_EXTENSIONS`, `_SECRET_PATTERNS`, `_SCHEMA`. Eventos/estados formales no existen; estados observables son documento cargado, chunk duplicado/rechazado/aceptado y error de ingestión.

## Códigos y razones

Razones de calidad: `too_short`, `too_many_control_characters`, `possible_secret`, y flags informativos `flag:contains_email`. Errores de extras incluyen mensajes `... requires: uv sync --extra ...`. Git propaga `CalledProcessError`; la API lo transforma a HTTP 400 sin tipado estable.
