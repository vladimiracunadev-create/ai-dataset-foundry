# 19. Matriz de trazabilidad

| Funcionalidad/regla | Interfaz | Símbolo | Persistencia | Prueba | Estado |
| --- | --- | --- | --- | --- | --- |
| Ingerir locator | CLI/API | `ingest/load_path`, loaders | DocumentRecord | router/JSON | Parcial |
| Provenance | build | loaders + `Provenance` | JSONL/Parquet/SQLite | pipeline/webapp | Ruta textual validada |
| Normalizar/limpiar | build | `normalize_text/clean_text` | texto | pipeline indirecta | Parcial |
| Chunking | config | `chunk_text/_fixed/_pack` | chunks | chunking | Parcial |
| Dedup | config | `Deduplicator` | manifest | exacto | Cercano pendiente |
| Privacidad/calidad | config/API | `detect_sensitive/assess_quality` | razones/score | privacy | Parcial |
| JSONL/TXT | build | `export_records` | archivos | pipeline/smoke | Validado |
| Parquet | build | `export_parquet` | Parquet | ninguna directa | Pendiente extra |
| SQLite | build | `write_sqlite` | dos tablas | pipeline/smoke | Contrato parcial |
| Manifest | build | `build_dataset` | JSON/DB | pipeline/smoke | Divergencia conocida |
| Stats/validate | CLI | `stats/from_yaml` | lectura/ninguna | no directa | Pendiente CLI |
| UI | HTTP | `create_app` | `work/ui-runs` | webapp | Camino feliz |
| Windows | desktop | `desktop.main` | outputs | release | Evidencia release |
| Android | app | `DatasetBuilder/MainActivity` | JSONL | JUnit mínima | Release mínima |
| Git remoto | URL | `load_git` | chunks | routing mock | Integración pendiente |
| Coherencia | CI/script | `verify_docs.py` | stdout | CI | Validado |
| PDFs | script | `generate_system_pdfs.py` | pdf/ | check + render | Validado al generar |

La relación detallada interfaz → módulo → datos → prueba se amplía en los documentos 04 a 12. “Parcial” indica camino principal con combinaciones o errores aún sin prueba.
