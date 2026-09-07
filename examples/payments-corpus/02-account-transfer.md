# Caso sintético: transferencia cuenta a cuenta

Una empresa paga una factura mediante transferencia push. El portal crea una referencia estructurada y redirige al entorno de autorización de la institución. El retorno del navegador indica que el flujo terminó, pero el pedido continúa pendiente hasta que un evento firmado o una consulta autenticada confirma la aceptación.

El rail procesa la instrucción en segundos. El sistema distingue fondos informados al beneficiario, settlement entre participantes y payout/abono visible para el comercio. Si la consulta queda en timeout después de enviar, el intento pasa a reconciliación; no se crea una segunda transferencia con una referencia nueva.

## Evidencia esperada

- el navegador nunca decide `SETTLED`;
- la referencia sobrevive desde factura hasta cartola/reporte;
- `UNKNOWN` tiene owner, aging y consulta segura;
- un return posterior crea una transición y asiento compensatorio.
