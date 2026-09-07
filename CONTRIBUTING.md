# Contribuir

## Principios

Cambios pequeños, evidencia reproducible, compatibilidad explícita y documentación honesta. Una capacidad documentada no se marca operativa sin prueba.

## Entorno

```bash
python -m venv .venv
python -m pip install -e ".[all,dev]"
python scripts/doctor.py
python -m pytest --basetemp .tmp/pytest -q
python -m ruff check src tests scripts
python scripts/verify_docs.py
```

## Pull request

1. Explica problema, decisión, alternativas y riesgo.
2. Añade pruebas para comportamiento nuevo o corregido.
3. Actualiza README/docs/estado cuando cambie una afirmación actual.
4. No reescribas referencias históricas del changelog.
5. Usa Conventional Commits cuando sea razonable (`feat:`, `fix:`, `docs:`).
6. Confirma que no hay secretos ni datasets generados en el diff.

## Nuevos conectores

Declara formatos, límites, timeout, errores, metadatos, hash y consideraciones de seguridad. No ejecutes macros/scripts ni sigas redirecciones/URLs sin una política clara. Registra el conector en el router y prueba input válido, vacío y malformado.

## Contenido de pagos

Usa fuentes primarias, incluye jurisdicción y fecha, distingue norma de recomendación y etiqueta `DOCUMENTADO`, `OPERATIVO-SANDBOX` u otro estado verificable. Las marcas comerciales son ejemplos, no cobertura garantizada.

## Commits

Stagea rutas explícitas. No incluyas `.env`, `work/`, `datasets/`, `exports/`, bases SQLite ni documentos con datos internos.
