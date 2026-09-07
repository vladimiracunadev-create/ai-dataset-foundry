# Glosario operacional

| Término | Definición en este laboratorio |
| --- | --- |
| Acquirer/adquirente | participante que afilia al comercio y presenta transacciones al esquema |
| Authorization | decisión de permitir una operación; no prueba settlement |
| Beneficiary/payee | receptor previsto de fondos |
| Capture | presentación de un importe autorizado para clearing |
| Card-on-file | credencial de tarjeta almacenada, idealmente como token, para uso posterior |
| Chargeback | reversión bajo reglas de disputa del esquema |
| Clearing | transmisión/validación y cálculo de obligaciones antes de settlement |
| CNP | transacción card-not-present |
| Credential-on-file | credencial conservada para transacciones futuras |
| CVV/CVC | dato de autenticación de tarjeta; no almacenar tras autorización |
| Dispute | proceso formal que cuestiona una transacción |
| Double-entry ledger | registro donde débitos y créditos balancean por transacción |
| EMV | especificaciones de interoperabilidad para pagos, chip/contactless y tecnologías asociadas |
| Finality | punto en que una transferencia es final bajo reglas/ley; no elimina nuevas obligaciones |
| Gateway | interfaz técnica que transmite/abstrae; puede no custodiar ni adquirir |
| Idempotency key | identificador que hace que retries del mismo comando tengan un solo efecto |
| Interchange | fee entre participantes en determinados esquemas de tarjetas |
| Issuer/emisor | entidad que emite instrumento/cuenta y decide disponibilidad/autorización |
| KYC/KYB | diligencia de conocimiento de cliente/empresa |
| MCC | código de categoría del comercio |
| Merchant of record | vendedor contractual responsable ante cliente y flujo de cobro |
| Network token | sustituto del PAN con dominio de uso administrado en esquema de tokenización |
| PAN | número principal de cuenta de tarjeta, dato protegido |
| Payment intent | objetivo de cobrar/pagar importe y moneda, independiente de intentos |
| Payment rail | infraestructura por la que se intercambian instrucciones y/o se liquidan valores |
| Payout | abono agrupado del proveedor al comercio |
| PSP | proveedor de servicios de pago; el alcance exacto depende del contrato/regulación |
| Reconciliation | comparación y resolución entre registros internos, proveedor y banco |
| Refund | pago compensatorio iniciado para devolver importe capturado |
| Return | devolución iniciada/producida según reglas del rail |
| RTGS/LBTR | settlement bruto, transacción por transacción, en tiempo real |
| Scheme/esquema | reglas, participantes, estándares y gobierno compartidos |
| Settlement | descarga de obligaciones mediante transferencia del activo de liquidación |
| Tokenización | sustitución de un dato por token; distinta de cifrado |
| Void | cancelación/liberación antes de captura cuando está soportada |
| Webhook | notificación HTTP asíncrona; debe verificarse y deduplicarse |

Para definiciones normativas, usa el [glosario CPMI](https://www.bis.org/committees/cpmi/glossary); este documento adapta lenguaje al diseño del laboratorio.
