# Caso sintético: compra con tarjeta

Una persona compra un servicio digital por CLP 25.990. El comercio crea primero el pedido y luego una intención de pago por el importe en unidad menor. El navegador captura la credencial mediante campos alojados por el proveedor y recibe un token que solo sirve dentro del entorno de prueba.

El backend envía la autorización con una idempotency key estable. El emisor solicita autenticación adicional; el cliente completa el challenge y la autorización queda aprobada. El comercio captura una sola vez cuando habilita el servicio. Un webhook duplicado llega antes que la respuesta de consulta, pero el inbox conserva un solo efecto por event ID.

Al día siguiente, el reporte del proveedor muestra importe bruto, fee y payout neto. La conciliación enlaza pedido, intento, captura, asiento y payout. Ningún PAN, CVV, secreto ni identidad real forma parte del caso.

## Evidencia esperada

- pedido e intención son entidades distintas;
- autorización, captura y settlement tienen timestamps propios;
- evento duplicado no duplica servicio ni asiento;
- suma de débitos y créditos es igual;
- bruto menos fee y ajustes coincide con payout.
