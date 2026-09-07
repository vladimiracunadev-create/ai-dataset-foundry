# Operación de pagos

## Objetivo operacional

No basta que el endpoint responda: la obligación debe terminar en el estado correcto, el ledger debe balancear, el comercio debe recibir el payout esperado y toda diferencia debe tener dueño.

## SLI y SLO

| SLI | Definición recomendada |
| --- | --- |
| Disponibilidad de creación | intents válidos aceptados / intents válidos |
| Latencia | p50/p95/p99 por proveedor, medio, país y fase |
| Tasa de aprobación | aprobados / intentos elegibles; segmentada, no SLO puro |
| Webhook lag | recepción/proceso menos timestamp del proveedor |
| Unknown age | tiempo de intentos ambiguos sin resolver |
| Reconciliation completeness | movimientos conciliados / movimientos esperados |
| Payout accuracy | lotes sin diferencia material / lotes recibidos |
| Ledger integrity | transacciones balanceadas y sin secuencias imposibles |

Separa error propio, proveedor, emisor, usuario y riesgo. Una caída en approvals no siempre es incidente técnico.

## Dashboards

- funnel por método: created → action → authorized → captured → settled;
- latencia y errores por operación/proveedor;
- retries, circuit breaker, cola, DLQ y webhook lag;
- dinero `pending`, `unknown`, refunds y disputas;
- payouts esperados/recibidos y aging de diferencias;
- reglas de riesgo, challenges y falsos positivos;
- cambios de configuración y accesos privilegiados.

No uses importe total sin control de acceso ni identificadores sensibles como labels de alta cardinalidad.

## Alertas accionables

Una alerta especifica impacto, umbral/ventana, runbook, owner y condición de cierre. Ejemplos: crecimiento de `UNKNOWN`, webhook lag sobre presupuesto, payout ausente tras cutoff, ledger desbalanceado (página inmediata), diferencia de conciliación sobre tolerancia o approvals anómalos contra baseline segmentado.

## Runbook de pago desconocido

1. Congela retry automático que pueda duplicar efecto.
2. Busca por idempotency key y referencia propia/nativa.
3. Consulta API y eventos autenticados del proveedor.
4. Revisa ledger, outbox/inbox y reporte de transacciones.
5. Clasifica `succeeded`, `failed` o `pending`; nunca lo fuerces por intuición.
6. Si no hay evidencia, envía a conciliación y comunica estado honesto.
7. Documenta causa, monto expuesto y prevención.

## Runbook de proveedor degradado

Confirma alcance por medio/región, activa circuit breaker, preserva idempotencia, enruta solo si el contrato semántico es equivalente, deshabilita selectivamente el medio, informa sin prometer resultado, procesa backlog controlado y reconcilia la ventana completa al recuperar.

## Cierre y conciliación

Ingiere archivos/API de proveedor de forma inmutable, valida checksum/esquema/totales, normaliza, realiza matching determinista, produce excepciones con aging y aprueba ajustes maker-checker. Reconciliación diaria no reemplaza monitoring intradía en pagos inmediatos.

## Disputas

Mantén deadline, reason, monto, transacción, evidencia requerida, owner y estado. Automatiza recopilación, no falsifiques narrativa. Mide dispute rate por cohorte y causa, win rate ajustada, costo y tiempo de resolución.

## Continuidad

Define RTO/RPO por componente, dependencia de proveedor, procedimientos manuales seguros, respaldo/restauración probados, capacidad de procesar backlog y reconciliación posterior. Un sistema 24/7 necesita gestión de liquidez y soporte 24/7, no solo servidores encendidos.

## Postmortem

Incluye timeline UTC, impacto técnico/financiero/cliente, detección, decisiones, factores contribuyentes, controles que funcionaron, gaps y acciones con owner/fecha. Separa corrección de balances de restauración del servicio.
