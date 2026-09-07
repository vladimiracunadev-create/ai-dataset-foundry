# Caso sintético: wallet y QR

Un comercio muestra un QR dinámico con identificador, importe, moneda, expiración y nonce. La wallet del cliente resuelve el payload y ofrece dos fuentes: saldo almacenado o tarjeta tokenizada. Aunque la experiencia visual es la misma, cada selección usa un rail, un modelo de disputa y un settlement diferentes.

El backend valida comercio e importe desde su propia orden, no confía en lo que envía el dispositivo. Rechaza QR expirado o nonce repetido. Para tarjeta conserva la referencia del token de red y las reglas de tarjeta; para saldo conserva movimientos del ledger de la wallet y reglas de redención.

## Evidencia esperada

- QR se modela como canal, no como fuente de fondos;
- tokenización se distingue de cifrado;
- replay no produce un segundo cobro;
- conciliación conserva el rail subyacente.
