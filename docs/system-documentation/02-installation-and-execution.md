# 02. Instalación y ejecución

## Requisitos

- Python `>=3.11` (CI prueba 3.11, 3.12 y 3.13).
- `uv` para reproducir `uv.lock`; Git para repositorios remotos.
- Android: JDK/Gradle compatible con los plugins declarados; versión exacta del JDK no está documentada y requiere validación.
- No se requiere Docker para el núcleo.

## Preparación

```bash
git clone https://github.com/vladimiracunadev-create/ai-dataset-foundry.git
cd ai-dataset-foundry
uv sync --extra all --extra dev --locked
uv run python scripts/doctor.py
```

`all` instala documentos, web, Parquet y UI, pero no `pywebview`; para escritorio use `uv sync --extra desktop --extra dev --locked`. No hay variables de entorno obligatorias ni migración previa. La base SQLite se crea por build.

## Ejecución

```bash
# Configuración versionada
uv run foundry build --config examples/config.yaml

# Argumentos directos
uv run foundry build examples/sample.txt --out work/demo --format jsonl --format txt

# Inspección y validación
uv run foundry stats work/demo/dataset.jsonl
uv run foundry validate examples/config.yaml

# UI local (mantener loopback)
uv run foundry serve --host 127.0.0.1 --port 8765

# Host de escritorio
uv run foundry desktop
```

Producción como servicio no está documentada; la API carece de autenticación y fue diseñada para loopback. El ejecutable y APK se obtienen desde Releases. Android también puede compilarse desde `android/` con el wrapper/Gradle disponible en CI; el repositorio no incluye wrapper, por lo que la reproducción local requiere Gradle instalado.

## Verificación

```bash
uv run pytest -q
uv run ruff check src tests scripts
uv run python scripts/smoke.py
uv run python scripts/verify_docs.py
uv build
uv run python scripts/generate_system_pdfs.py --check
```

## Fallos frecuentes

| Síntoma | Causa probable | Acción |
| --- | --- | --- |
| `uv` no reconocido | binario fuera de `PATH` | instalar uv o invocar su ruta absoluta |
| “requires: uv sync --extra …” | dependencia opcional ausente | instalar `documents`, `web`, `parquet`, `ui` o `desktop` |
| Git remoto falla | Git ausente/red/autenticación | ejecutar `doctor.py`, validar URL y credenciales del propio usuario |
| PDF vacío | documento escaneado | OCR no implementado; preprocesar fuera de la foundry |
| HTTP 413 | carga mayor a 50 MiB | usar CLI/directorio o reducir el archivo; evaluar límites antes de producción |
| chunks rechazados | `min_chars`, controles o secretos | revisar manifest y configuración; no desactivar controles sin evaluar riesgo |

Nunca incluya claves reales en YAML, URL, ejemplos ni `work/`.
