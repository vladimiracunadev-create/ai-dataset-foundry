# Evaluación técnica en 10 minutos

## Qué mirar

1. [`README.md`](README.md): alcance, mapa y honestidad sobre lo que no hace.
2. [`docs/PAYMENT_METHODS.md`](docs/PAYMENT_METHODS.md): taxonomía funcional de 40 variantes en 9 familias.
3. [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md): separación de dominio, ledger, inbox/outbox y conciliación.
4. [`docs/SECURITY_MODEL.md`](docs/SECURITY_MODEL.md): amenazas, PCI, secretos, IAM y logging.
5. [`STATUS.md`](STATUS.md): evidencia frente a promesa.

## Demostración reproducible

```bash
python -m pip install -e ".[all,dev]"
python scripts/doctor.py
python scripts/smoke.py
python -m pytest -q
```

El smoke usa el código real, procesa tres documentos sintéticos de pagos y comprueba JSONL, TXT, SQLite y manifest. No necesita Docker, cuenta cloud ni API key.

## Decisiones que revela

- El motor de datos permanece agnóstico del dominio.
- El caso de pagos enseña operación real sin simular certificaciones.
- Los estados financieros no se reducen a `paid=true`.
- Idempotencia, ledger y conciliación se tratan como requisitos de producto.
- Las fuentes regulatorias son primarias, fechadas y revalidables.
- CI usa permisos mínimos y acciones fijadas a SHA.

## Preguntas de entrevista sugeridas

1. ¿Cómo cambiarías el manifest para reproducibilidad criptográfica completa?
2. ¿Qué diferencia existe entre confirmar checkout y confirmar settlement?
3. ¿Cómo introducirías un segundo PSP sin perder semántica ni trazabilidad?
4. ¿Qué componente ejecutarías aislado primero y por qué?
5. ¿Qué evidencia exigirías antes de marcar una integración `OPERATIVO-PRODUCCIÓN`?
