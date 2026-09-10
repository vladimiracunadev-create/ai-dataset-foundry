# 16. Glosario

| Término | Definición |
| --- | --- |
| Corpus/dataset | conjunto organizado de textos y metadatos para sistemas de IA |
| Foundry | pipeline que transforma fuentes en artefactos repetibles |
| Local-first | procesamiento pensado para el equipo local |
| Locator | ruta, URL o repositorio de una fuente |
| Conector | adaptador que produce documentos comunes |
| `DocumentRecord` | texto adquirido con fuente, metadata y hash |
| Chunk / `ChunkRecord` | fragmento y su provenance/calidad |
| Provenance/lineage | evidencia del origen y trazabilidad |
| SHA-256 | huella de identidad/cambio; no prueba autoría |
| NFKC | normalización Unicode de representaciones compatibles |
| SimHash/Hamming | huella aproximada y distancia entre huellas |
| Quality gate | reglas que aceptan o rechazan un fragmento |
| PII / DLP | datos identificables / controles contra fuga |
| JSONL | un objeto JSON por línea |
| Parquet | formato columnar analítico |
| Manifest | resumen de entradas, ajustes, errores y salidas |
| SQLite/WAL | base embebida y su registro transaccional |
| RAG | recuperación de fragmentos para fundamentar respuestas |
| Fine-tuning/SFT | ajuste supervisado; la foundry no lo realiza |
| Pretraining | aprendizaje a gran escala; necesita preparación adicional |
| Loopback | red del propio equipo (`127.0.0.1`) |
| SSRF | peticiones abusivas del servidor a redes no previstas |
| OCR | texto desde imágenes; planificado, no implementado |
| Smoke test | prueba corta del flujo completo |
| Release mínima | producto funcional con alcance reducido, como Android 0.2.0 |
