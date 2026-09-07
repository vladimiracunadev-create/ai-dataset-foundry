# Contribuir

Abre un issue con una fuente sintética mínima, resultado esperado, sistema operativo y versión de Python. Para cambios de código crea una rama, limita el alcance y acompaña cada comportamiento con pruebas y documentación.

```bash
uv sync --extra all --extra dev --locked
uv run ruff check src tests scripts
uv run pytest -q
uv run python scripts/smoke.py
uv run python scripts/verify_docs.py
```

No incluyas documentos privados, credenciales, PII ni contenido sin licencia. Los nuevos conectores deben aislar adquisición, conservar provenance, fallar por fuente y declarar límites. Los cambios de esquema requieren compatibilidad o una nueva `schema_version`.
