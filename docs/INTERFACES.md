# Interfaces y aplicaciones

Las tres interfaces comparten un principio: el procesamiento debe ser visible, local y exportable.

## CLI

Es la superficie de automatización y reproducibilidad. `build` ejecuta una receta; `stats` resume JSONL; `validate` comprueba que cada línea sea JSON válido; `serve` inicia la UI y `desktop` crea una ventana local.

## Web localhost y Windows

FastAPI expone una API limitada y sirve un frontend sin framework. La aplicación Windows empaqueta ese mismo backend con PyInstaller y lo muestra mediante pywebview. Escucha en `127.0.0.1`, selecciona un puerto libre y no convierte el equipo en un servidor público. El límite demo de carga es 50 MiB por archivo.

## Android mínima

La APK usa el selector de documentos de Android, lee hasta 5 MB de TXT, Markdown, JSON o CSV, normaliza texto, segmenta por párrafos, calcula SHA-256 y guarda JSONL. No declara permiso `INTERNET`; por tanto no descarga sitios ni repositorios. PDF, DOCX, OCR, deduplicación aproximada y catálogo SQLite continúan en Python/Windows.

Esta asimetría es deliberada: una primera aplicación móvil honesta y pequeña es preferible a prometer paridad inexistente. Los artefactos publicados incluyen checksums SHA-256.
