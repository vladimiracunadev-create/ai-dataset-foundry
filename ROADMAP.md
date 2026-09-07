# Roadmap

El roadmap expresa resultados y gates; no promete fechas. El estado actual permanece en [`STATUS.md`](STATUS.md).

## 0.2 · Reproducibilidad fuerte

- manifest con versión del paquete, commit, entorno y checksums de outputs;
- lock/constraints verificables por plataforma;
- esquema JSON versionado y validación contractual;
- reporte de cobertura y property tests para IDs, chunks y ledger de ejemplo.

Gate: dos ejecuciones con mismas fuentes/config producen artefactos equivalentes salvo campos temporales declarados.

## 0.3 · Calidad y gobierno

- allowlists de fuentes y política de red para web;
- detector modular de secretos/PII con reporte de falsos positivos;
- dataset cards, licencias y flujo de takedown;
- evaluaciones de completitud, contamination y leakage.

Gate: una fuente rechazada no deja contenido sensible en output, cache ni logs.

## 0.4 · Payment simulation lab

- modelo ejecutable de payment intent/attempt;
- state machine por rail y ledger de doble entrada;
- simulador determinista de duplicate/out-of-order/timeout;
- conciliación de reportes y panel local de excepciones.

Gate: escenarios de tarjeta, A2A y wallet mantienen invariantes monetarias bajo fallos inyectados. Seguirá sin mover dinero.

## 0.5 · Sandboxes de proveedor

- adaptadores opt-in aislados del core;
- Docker Compose solo cuando agregue cola, ledger y simuladores;
- contract tests, firma de webhook y rotación de secretos;
- evidencia de certificación/sandbox por adaptador.

Gate: cero credenciales en repo, replay probado, reconciliación completa y runbook ejercitado. Cada proveedor se etiqueta por separado.

## 1.0 · Contrato estable

CLI y esquema estables, compatibilidad documentada, threat model revisado, SBOM/provenance de release, restauración probada y documentación de migración.

## Fuera de alcance por diseño

Actuar como PSP/adquirente/emisor, custodiar fondos, procesar credenciales reales, ofrecer asesoría regulatoria o afirmar certificación sin evidencia externa.
