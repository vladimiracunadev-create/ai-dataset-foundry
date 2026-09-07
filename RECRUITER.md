# Recorrido técnico en 10 minutos

AI Dataset Foundry demuestra ingeniería de datos aplicada a IA, no una pantalla decorativa. Empieza por el diagrama del README, ejecuta `python scripts/smoke.py`, inspecciona `manifest.json` y un registro JSONL, y abre `foundry serve`.

Aspectos evaluables:

- arquitectura hexagonal ligera: conectores, procesadores, exportadores y almacenamiento;
- IDs y SHA-256 estables para trazabilidad;
- errores aislados por fuente y decisiones de calidad registradas;
- una UI compartida entre localhost y Windows;
- Android offline con alcance explícitamente menor;
- CI multiversión, auditoría de dependencias, Pages y release con checksums;
- documentación que separa capacidades reales, límites y roadmap.

La conversación de diseño relevante no es “cuántos formatos enumera”, sino cómo evita datos no autorizados, pérdida de estructura, duplicados, leakage y métricas engañosas.
