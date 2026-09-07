# Estado verificable

Fecha de corte: **2026-09-07** · versión canónica: **0.1.0**

Este archivo separa implementación, demostración documental y trabajo futuro. Una marca `DOCUMENTADO` significa que existe una explicación utilizable, no que exista una conexión certificada con una red de pagos.

| Superficie | Estado | Evidencia |
| --- | --- | --- |
| CLI `build`, `stats`, `validate` | `OPERATIVO` | `src/ai_dataset_foundry/cli.py` |
| Ingesta texto/Markdown, JSON/JSONL, CSV | `OPERATIVO` | conectores + pruebas |
| PDF, DOCX, HTML, URL y Git | `OPERATIVO-CON-EXTRAS` | extras `documents` y `web`; Git externo |
| Normalización, limpieza, chunking y deduplicación | `OPERATIVO` | procesadores + pruebas |
| JSONL, TXT, SQLite | `OPERATIVO` | exportadores + prueba end-to-end |
| Parquet | `OPERATIVO-CON-EXTRA` | extra `parquet` |
| Detección de secretos/PII | `BÁSICO` | heurísticas; no es DLP ni control PCI |
| Atlas de medios de pago | `DOCUMENTADO` | `docs/PAYMENT_METHODS.md` |
| Arquitectura de pago y operación | `DOCUMENTADO` | ciclo, integración, seguridad, riesgo y operaciones |
| Corpus sintético de pagos | `OPERATIVO` | `examples/payments-corpus/` + `examples/payments.yaml` |
| PSP/acquirer/emisor real | `NO-IMPLEMENTADO` | fuera de alcance de esta versión |
| Procesamiento de dinero o PAN | `PROHIBIDO` | límites del README y `SECURITY.md` |
| Docker Compose de infraestructura | `PLANIFICADO` | no es necesario para ejecutar la versión actual |

## Hechos medidos

| Hecho | Valor actual | Fuente de verdad |
| --- | ---: | --- |
| Versión | 0.1.0 | `pyproject.toml` |
| Python mínimo | 3.11 | `requires-python` y matriz CI |
| Workflows | 3 | `.github/workflows/{ci,pages,release}.yml` |
| Actions con pin inmutable | 6/6 acciones externas | SHA completo + comentario de versión en workflows |
| Versiones Python en CI | 3 | 3.11, 3.12, 3.13 en `ci.yml` |
| Archivos de prueba | 5 | `tests/test_*.py` |
| Casos de prueba | 7 | colección de pytest |
| Familias de pago documentadas | 9 | tabla maestra en `docs/PAYMENT_METHODS.md` |

## Cómo reproducir la verificación

```bash
python -m pip install -e ".[all,dev]"
python scripts/doctor.py
python scripts/smoke.py
python scripts/verify_docs.py
python -m pytest --basetemp .tmp/pytest --collect-only -q
python -m pytest --basetemp .tmp/pytest -q
python -m ruff check src tests scripts
```

El smoke test crea su salida en un directorio temporal, comprueba JSONL, manifiesto y SQLite y la elimina al terminar.

## Limitaciones conocidas

- Las dependencias tienen rangos compatibles, no lockfile reproducible por plataforma.
- La ingesta web realiza una descarga de página individual y no implementa crawler, robots scheduler ni rate limiter distribuido.
- El score de calidad es heurístico; no mide veracidad, licencia, sesgo ni adecuación pedagógica.
- La deduplicación near-match usa SimHash y puede unir falsos positivos o conservar falsos negativos.
- La documentación de pagos es transversal y Chile-first en regulación, pero cada implementación debe revalidarse para su país, proveedor y contrato.
- No existen credenciales, llamadas a sandbox de PSP ni datos de titulares dentro del repositorio.

## Criterio de salida para una integración real futura

Una integración solo puede pasar de `PLANIFICADO` a `OPERATIVO-SANDBOX` si incluye contrato versionado, fixtures sintéticos, verificación de firmas, idempotencia, pruebas de replay y desorden, conciliación, runbook, SLO y evidencia CI. `OPERATIVO-PRODUCCIÓN` exigiría además certificación/proceso del proveedor y evidencia externa que no puede declararse desde este repositorio.
