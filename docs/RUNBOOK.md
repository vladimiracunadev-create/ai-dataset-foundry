# Runbook operativo

## Secuencia segura

1. Ejecuta `python scripts/doctor.py`.
2. Prueba con una muestra autorizada.
3. Ejecuta `foundry build --config <receta>`.
4. Revisa `ingestion_errors`, `rejected` y conteos del manifest.
5. Valida JSONL y abre muestras aleatorias contra la fuente.
6. Calcula checksums, mueve el artefacto a almacenamiento controlado y registra aprobación.

## Diagnóstico

- **PDF vacío:** probablemente escaneado; v0.2.0 no ejecuta OCR.
- **Web devuelve poco texto:** JavaScript, autenticación o anti-bot; usa una exportación autorizada.
- **Repositorio falla:** confirma Git, URL, credenciales y tamaño. No coloques tokens en la URL.
- **Muchos rechazados:** inspecciona razones antes de relajar umbrales.
- **Cero chunks:** confirma encoding, extracción y `min_chars`.
- **Parquet ausente:** instala `.[parquet]` o `.[all]`.
- **UI no abre:** visita `http://127.0.0.1:8765` y verifica que el puerto esté libre.

## Recuperación

Los builds viven en directorios nuevos. Conserva originales y receta; ante fallo elimina únicamente el directorio de salida exacto y reconstruye. No edites JSONL a mano sin generar un nuevo manifest.
