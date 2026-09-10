# 14. Solución de problemas

| Síntoma | Diagnóstico/solución | Riesgo/ubicación |
| --- | --- | --- |
| Dependencia ausente | `doctor.py`; instalar el extra indicado | no instalar globalmente sin control |
| Archivo ignorado | revisar extensión en `load_path`; convertir o implementar conector | extensión desconocida devuelve vacío |
| GitHub tratado como Git | revisar heurística URL | `router.py` |
| Clone falla | `git --version`, acceso y URL | no poner token en URL/manifest |
| PDF sin texto | comprobar escaneado; OCR externo autorizado | OCR no implementado |
| Muchos duplicados | revisar orden/SimHash; bajar umbral | puede crecer costo/dataset |
| Todos rechazados | revisar `manifest.rejected`; ajustar con criterio | riesgo de ruido/secretos |
| Parquet falla | instalar extra `parquet` | memoria en grandes volúmenes |
| UI 400 | revisar locators/formats JSON, permisos y parser | error puede mostrar rutas |
| UI 413 | usar CLI o reducir archivo | CLI no impone mismo límite |
| Artefacto 404 | usar run_id/nombre devueltos | la corrida se limpia al fallar |
| Puerto/UI no inicia | comprobar puerto, firewall y extra | no usar `0.0.0.0` sin hardening |
| SQLite bloqueado | cerrar lectores; nueva ruta | no borrar la única copia |
| PDF/docs stale | `verify_docs.py` y generador `--check` | no editar PDF manualmente |
| CI rojo | `gh run view <id> --log-failed` | no borrar rama sin resolver |

Comandos seguros: `pytest -q`, `ruff check`, `python scripts/smoke.py`, `python scripts/verify_docs.py`, `python scripts/generate_system_pdfs.py --check`, `git status --short`. Antes de eliminar outputs, confirme la ruta absoluta y que son derivados regenerables.
