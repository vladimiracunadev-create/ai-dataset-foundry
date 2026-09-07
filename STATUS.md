# Estado verificable

Fecha de corte: **2026-09-07** · versión canónica: **0.2.0**

## Matriz de madurez

| Componente | Estado | Fuente de verdad |
| --- | --- | --- |
| CLI `build`, `stats`, `validate`, `serve`, `desktop` | `OPERATIVO` | `src/ai_dataset_foundry/cli.py` |
| Texto/Markdown/código, JSON/JSONL y CSV | `OPERATIVO` | conectores + pruebas |
| PDF, DOCX, HTML y Web | `OPERATIVO-CON-EXTRAS` | extras `documents`/`web` |
| Git local y remoto | `OPERATIVO` | `connectors/git.py`; Git requerido |
| Normalize/clean/chunk/dedup/quality | `OPERATIVO` | procesadores + pruebas |
| JSONL, TXT, SQLite | `OPERATIVO` | smoke end-to-end |
| Parquet | `OPERATIVO-CON-EXTRA` | PyArrow |
| UI localhost | `OPERATIVO` | API FastAPI + frontend vanilla |
| Ejecutable Windows | `RELEASE` | job `windows-desktop` de release |
| APK Android | `RELEASE-MÍNIMA` | lector offline texto/MD/JSON/CSV |
| OCR, audio, vídeo, bases de datos y object storage | `PLANIFICADO` | roadmap; no implementado |
| Actualización incremental | `DISEÑADO` | hashes presentes; registry pendiente |

## Hechos medidos

| Hecho | Valor actual | Fuente |
| --- | ---: | --- |
| Versión | 0.2.0 | `pyproject.toml` y `__version__` |
| Python mínimo | 3.11 | manifest y CI |
| Workflows | 4 | CI, Security, Pages, Release |
| Versiones Python en CI | 3 | 3.11, 3.12, 3.13 |
| Modalidades implementadas | 9 | TXT/MD/código, PDF, DOCX, HTML, Web, Git, JSON/JSONL, CSV |
| Formatos de salida | 4 + manifest | JSONL, TXT, Parquet, SQLite |
| Aplicaciones de release | 2 | Windows `.exe`, Android `.apk` |

Los conteos de pruebas se obtienen con `pytest --collect-only`; no se fijan aquí para evitar drift manual.

## Reproducir

```bash
uv sync --extra all --extra dev --locked
uv run python scripts/doctor.py
uv run pytest -q
uv run ruff check src tests scripts
uv run python scripts/smoke.py
uv run python scripts/verify_docs.py
uv build
```

## Lo que la versión 0.2.0 no afirma

- No entrena ni sirve modelos.
- No realiza OCR de escaneados.
- No rastrea sitios completos ni ignora `robots.txt`.
- No garantiza derechos, verdad, ausencia de sesgo o anonimización.
- No ofrece procesamiento distribuido ni registro incremental persistente.
- El APK no replica los parsers pesados de Windows; es una edición mínima offline.

## Criterio para cambiar un estado

Una capacidad pasa a `OPERATIVO` solo cuando existe implementación, prueba automatizada o smoke reproducible, documentación de límites y ejecución verde en CI. Un diseño, mockup o dependencia nombrada no cuenta como implementación.
