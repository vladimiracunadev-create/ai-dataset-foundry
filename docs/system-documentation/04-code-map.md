# 04. Mapa completo del código

## Inventario jerárquico

| Ruta | Responsabilidad / consumidor | Estado e importancia |
| --- | --- | --- |
| `src/ai_dataset_foundry/models.py` | `SourceInfo`, `DocumentRecord`, `Provenance`, `QualityResult`, `ChunkRecord`; todo el pipeline | Activo, crítico |
| `config.py` | modelos `ChunkConfig`, `QualityConfig`, `DedupConfig`, `BuildConfig`; CLI/API/pipeline | Activo, crítico |
| `pipeline.py` | `build_dataset`, orquestación, manifest y SQLite | Activo, crítico |
| `connectors/router.py` | `ingest`, `load_path`, despacho por locator/extensión | Activo, crítico |
| `connectors/text.py` | `_record`, `load_text`, `load_json`, `load_csv` | Activo |
| `connectors/pdf.py`, `docx.py`, `html.py` | extracción opcional local | Activo con extras |
| `connectors/web.py` | `load_url`, fetch único HTTP(S) y extracción | Activo con extra; delicado por red |
| `connectors/git.py` | `load_git`, `_load_repo`, clone shallow temporal | Activo; delicado por subprocess/red |
| `connectors/base.py` | ABC `Connector`, no instanciada por implementaciones actuales | Experimental/no utilizado directamente |
| `processors/normalize.py`, `clean.py` | canonicalización Unicode/espacios y controles | Activo |
| `processors/chunk.py` | `_fixed`, `_pack`, `chunk_text` | Activo, crítico |
| `processors/dedup.py` | `_tokens`, `simhash`, `hamming`, `Deduplicator` | Activo, crítico; costo O(n²) aproximado |
| `processors/privacy.py`, `quality.py` | `detect_sensitive`, `assess_quality` | Activo; control heurístico |
| `exporters/*` | `export_records`, JSONL/TXT/Parquet | Activo |
| `storage/sqlite_store.py` | `_SCHEMA`, `write_sqlite` | Activo, crítico para catálogo |
| `utils/hashing.py` | hashes e IDs deterministas | Activo, crítico |
| `cli.py` | comandos `build`, `stats`, `validate`, `serve`, `desktop` | Activo |
| `webapp.py` | `create_app`, `_decode_list`, `_save_upload`; rutas UI/API | Activo; superficie local |
| `desktop.py`, `launcher.py` | puerto libre, servidor thread, ventana pywebview | Activo Windows |
| `ui/index.html` | cliente de la API local | Activo |
| `android/` | `MainActivity`, `DatasetBuilder`, prueba JUnit y build Android | Activo, release mínima independiente |
| `tests/` | 9 pruebas Python en 7 archivos | Activo, cobertura parcial |
| `scripts/doctor.py` | prerrequisitos | Activo |
| `scripts/smoke.py` | build E2E sobre muestra sintética | Activo |
| `scripts/verify_docs.py` | enlaces, versión, workflows y pins | Activo |
| `scripts/generate_system_pdfs.py` | fuente Markdown a PDF + chequeos | Activo, documental |
| `.github/workflows/` | CI, Security, Pages y Release | Activo, crítico |
| `site/` | landing estática de Pages | Activo |
| `docs/` | manual temático previo + esta documentación integral | Activo |
| `dist/`, `work/` | artefactos reproducidos/locales; ignorados parcialmente | Generado, no fuente |

## Dependencias y llamadas clave

`cli.build` y `webapp.build` crean `BuildConfig` y llaman `build_dataset`. Éste llama `connectors.ingest`, luego `normalize_text → clean_text → chunk_text → Deduplicator.is_duplicate → assess_quality`, construye `ChunkRecord`, llama `export_records` y opcionalmente `write_sqlite`. `desktop.main` aloja `create_app`. Android no llama al núcleo Python.

Archivos aparentemente duplicados: `site/index.html` (landing pública) y `src/.../ui/index.html` (aplicación) son propósitos distintos. `Connector` es una abstracción sin adopción actual. `launcher.py` existe para empaquetado y delega completamente a escritorio.
