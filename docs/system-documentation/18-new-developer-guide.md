# 18. Guía para un nuevo desarrollador

## Itinerario

1. Lea `README.md`, [descripción general](01-system-overview.md) y `STATUS.md`.
2. Ejecute doctor, tests y smoke; inspeccione manifest y una fila JSONL.
3. Siga `models.py → config.py → pipeline.py`.
4. Recorra router/loaders, processors, exporters y SQLite.
5. Siga `ui/index.html → webapp.create_app → build_dataset`.
6. Compare escritorio y Android.
7. Lea seguridad, riesgos y workflows antes de tocar entradas/salidas.

```bash
uv sync --extra all --extra dev --locked
uv run python scripts/doctor.py
uv run pytest -q
uv run python scripts/smoke.py
```

Un conector nuevo debe producir `DocumentRecord`, conservar hash/localizador/metadata, declarar extra, probar éxito/error y documentar límites. Un procesador debe ser determinista y probar orden/casos límite. Un exportador serializa `ChunkRecord.to_dict` y necesita E2E. Cambios de esquema exigen compatibilidad o nueva `schema_version`.

Convenciones: Python 3.11+, type hints, Ruff 100 columnas, sin secretos/muestras privadas; no sobrescribir originales; lazy imports; UI en loopback; PDFs regenerados desde Markdown. Dedup/calidad, IDs/hashes y esquema son contratos delicados.

Tareas junior: fixtures sintéticos de loaders, errores tipados, chequeo manifest/SQLite, documentación de fixtures y cobertura. SSRF, sandboxing, esquema y release requieren revisión experimentada.
