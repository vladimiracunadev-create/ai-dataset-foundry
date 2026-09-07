# Playbook de integración de pagos

## Antes de escribir código

Documenta países, monedas, entidades legales, merchant of record, canales, medios, volúmenes, ticket, recurrencia, split, refund, disputa, payout, settlement, FX y retención. Confirma quién posee la relación regulada y quién soporta cada pérdida.

## Selección de proveedor

Evalúa capacidades por flujo, no por lista de logos:

| Dimensión | Evidencia que pedir |
| --- | --- |
| Cobertura | entidades, países, monedas, MCC y medios contratables |
| API | OpenAPI/esquemas, versionado, idempotencia, errores y rate limits |
| Checkout | hosted, fields, redirect, app SDK, accesibilidad y localización |
| Seguridad | PCI Attestation, cifrado, tokenización, firmas y segregación |
| Operación | status page, SLA/SLO, soporte, incidentes y mantenimiento |
| Finanzas | pricing completo, reservas, FX, settlement, reportes y facturas |
| Disputas | evidencia, plazos, API/portal, representment y fees |
| Portabilidad | exportación de tokens permitida, migración y terminación |

## Contrato de API

- importe en unidad menor entera y currency explícita;
- idempotency key estable por operación lógica;
- request ID y correlation ID propagados;
- referencias propias y del proveedor persistidas;
- error tipado: usuario, negocio, transitorio, permanente o desconocido;
- versión de API fijada y calendario de deprecación;
- timestamps UTC y semantics de fecha valor separados.

Nunca loguees el body completo por conveniencia. Diseña una allowlist de campos observables.

## Idempotencia correcta

La key debe mapear a hash del comando. Si llega igual key con payload distinto, rechaza conflicto. Guarda estado de ejecución y respuesta materializada. La ventana de retención debe superar retries y replays previsibles.

```text
UNSEEN → IN_PROGRESS → SUCCEEDED
                    └→ FAILED_RETRYABLE
          └→ FAILED_FINAL
```

Un lock en memoria no basta entre procesos; un UUID nuevo por retry destruye la protección.

## Webhooks

1. Conserva bytes exactos recibidos mientras lo permita la política.
2. Resuelve secreto/clave por endpoint y versión.
3. Verifica algoritmo permitido, firma y timestamp con comparación constante.
4. Rechaza replay fuera de ventana y deduplica `event_id`.
5. Encola, responde y procesa fuera del request.
6. Valida transición; si hay duda, consulta la API del proveedor.
7. Rota secretos aceptando ventana dual controlada.

## Redirects y retorno del navegador

El navegador no es fuente de verdad: el usuario puede cerrarlo, manipular parámetros o llegar antes que el webhook. La return URL mejora UX; el backend decide usando evento verificado o consulta autenticada. Protege `state`, session binding, open redirect y CSRF.

## Adaptadores y normalización

Cada adaptador traduce comandos/eventos y conserva el objeto nativo redacted. El dominio común no debe exponer nombres de un proveedor. No reduzcas códigos de rechazo a `FAILED`; conserva categoría accionable y mensaje seguro para cliente.

## Testing contract-first

Prueba al menos:

- approve, decline, pending y requires-action;
- timeout antes/después de aceptación;
- webhook duplicado, fuera de orden, inválido y tardío;
- capture parcial, void, refund parcial/múltiple;
- cambio de moneda y redondeo;
- payout con fees/ajustes y archivo faltante;
- credencial expirada, rate limit y rotación de secreto;
- retry concurrente con misma idempotency key.

Sandbox no reproduce riesgo, settlement, ventanas ni indisponibilidad real. Complementa con simuladores deterministas, contract tests y certificación del proveedor.

## Cutover

Usa feature flags por merchant/país/medio, canary de bajo monto permitido, límites conservadores, dashboards antes del tráfico, runbook, on-call y rollback. Reconcilia desde la primera transacción; no esperes al cierre mensual.

## Definition of done

- flujos y estados documentados;
- secretos fuera del código;
- PCI scope revisado por responsable competente;
- idempotencia y webhooks probados;
- ledger y conciliación balancean;
- observabilidad no filtra datos;
- SLO, alertas y runbooks ejercitados;
- refunds/disputas soportados;
- privacidad, retención y contratos aprobados;
- evidencia de sandbox/certificación archivada.
