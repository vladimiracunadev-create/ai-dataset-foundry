# 12. Pruebas y calidad

Al corte 2026-09-10, `pytest --collect-only -q` enumera **9 pruebas** en 7 archivos.

| Área | Evidencia |
| --- | --- |
| Chunking | fixed con overlap; packing de párrafos |
| Deduplicación | duplicado exacto |
| JSONL | IDs distintos por fila |
| Pipeline | texto a JSONL/TXT/manifest/SQLite |
| Privacidad | email y patrón de secreto |
| Router | URL GitHub dirigida a Git |
| Webapp | health, upload/build y descarga |

`scripts/smoke.py` ejecuta un E2E sintético y comprueba cuatro artefactos. `doctor.py` reporta requisitos. `verify_docs.py` revisa enlaces Markdown, mojibake básico, versión, inventario de cuatro workflows y pins SHA. Ruff selecciona E4/E7/E9/F; no hay umbral de cobertura, type-checker ni regla de complejidad.

CI prueba Python 3.11/3.12/3.13. Security audita dependencias; Pages publica el sitio; Release crea artefactos. Dependabot es configuración/automatización externa, no un quinto archivo workflow.

## Pruebas faltantes priorizadas

1. PDF/DOCX/HTML/web/Git/CSV y fallos de parser/red.
2. SimHash cercano, umbrales, orden y escala.
3. Controles de calidad, score combinado y email/secreto.
4. API: JSON inválido, 413, traversal, nombres repetidos, cleanup y concurrencia.
5. SQLite: esquema, índices, reemplazo, rollback y concordancia de manifest.
6. CLI, escritorio y contrato cruzado Android/Python.
7. Property tests, fuzzing, benchmarks, cobertura y análisis de tipos.

Un cambio debe mantener tests, Ruff, smoke, enlaces/coherencia y build verdes. Los cambios de esquema requieren compatibilidad o nueva `schema_version`; los PDFs exigen regeneración y revisión visual.
