# Atlas de medios de pago

## Criterio de cobertura

«Todos» no puede significar cada marca comercial del planeta: aparecen proveedores y variantes a diario. En este laboratorio significa **todas las familias funcionales relevantes**, sus principales variantes y la tecnología que cambia su integración, riesgo u operación. Una wallet que transporta una tarjeta sigue heredando el rail de tarjetas; un QR es un canal que puede iniciar tarjeta, cuenta a cuenta o saldo almacenado.

## Matriz maestra

| Familia / variante | Fuente de fondos | Iniciación | Confirmación típica | Reversibilidad | Tecnología y control dominante |
| --- | --- | --- | --- | --- | --- |
| Efectivo | billetes/monedas | entrega física | inmediata por conteo | baja; devolución separada | caja, arqueo, transporte, falsificación |
| Contra entrega | efectivo/tarjeta al recibir | courier/POS | al despacho o entrega | según instrumento | logística, prueba de entrega, recaudo |
| Voucher/gift card cerrado | pasivo del emisor | código/POS/app | online u offline | contractual | ledger stored-value, expiración, breakage |
| Cheque | cuenta bancaria | documento firmado | diferida | devolución por causales | truncamiento, cámara, firma, fondos |
| Vale vista/cashier's check | fondos bancarios reservados | documento | diferida | limitada | emisión bancaria y verificación |
| Giro/money order | prepago al emisor | papel/digital | diferida | limitada | red de agentes, KYC, seriales |
| Tarjeta de crédito | línea de crédito | chip/NFC/web/app | autorización en segundos | chargeback y refund | EMV, ISO 8583, 3DS, tokenización, PCI |
| Tarjeta de débito | cuenta | chip/NFC/web/app | segundos | disputa/refund | EMV, PIN/CDCVM, red de tarjetas |
| Tarjeta prepago | saldo provisionado | chip/NFC/web/app | segundos | disputa/refund | ledger del emisor, salvaguarda de fondos |
| Charge card | deuda pagadera completa | tarjeta | segundos | disputa/refund | underwriting y billing mensual |
| Commercial/fleet | crédito empresarial | tarjeta/datos nivel II-III | segundos | disputa/refund | controles MCC, centro de costo, enhanced data |
| Tarjeta virtual | cuenta/crédito | credencial digital | segundos | según esquema | PAN/token dinámico, límites por uso |
| Card-on-file/recurring | cuenta/crédito | merchant initiated | segundos | disputa/refund | token vault, MIT/CIT, account updater |
| Transferencia tradicional/TEF | cuenta | banca web/app/API | segundos a días | return/recall limitado | directorio, ACH, ISO 20022 o formato local |
| Transferencia instantánea | cuenta | alias/QR/API | segundos 24/7 | normalmente nueva transferencia | instant rail, confirmación de beneficiario, fraude APP |
| Wire/RTGS | cuenta/liquidez bancaria | banco/API | intradía/segundos | muy limitada | RTGS, SWIFT/ISO 20022, controles duales |
| Débito directo | cuenta | mandato del pagador | batch o mismo día | devoluciones reguladas | mandate store, ACH, prenotificación |
| Standing order | cuenta | instrucción del pagador | según calendario | cancelable hacia futuro | scheduler bancario |
| Request to Pay | cuenta | solicitud + aceptación | depende del rail | depende del credit transfer | mensajería ISO 20022, consentimiento |
| Wallet pass-through | tarjeta/cuenta subyacente | NFC/app/web | hereda rail | hereda rail | network token, device token, CDCVM |
| Wallet de saldo | pasivo del wallet | app/QR/alias | inmediata en ledger | contractual | ledger interno, cash-in/out, safeguarding |
| QR merchant-presented | variable | cliente escanea | variable | hereda rail | EMV QRCPS o estándar local, firma/CRC |
| QR consumer-presented | variable | comercio escanea | variable | hereda rail | token de un solo uso, terminal/cámara |
| NFC/wearable | tarjeta/wallet | tap | segundos | hereda rail | EMV contactless, token, secure element/HCE |
| Cuotas del emisor | crédito | checkout/tarjeta | segundos | disputa/refund | plan de cuotas, interchange y ledger emisor |
| BNPL | crédito del proveedor | checkout | segundos | refund + crédito | underwriting, schedule, merchant settlement |
| POS financing | préstamo | comercio | minutos | contrato de crédito | KYC, scoring, firma, desembolso |
| Pay-later B2B | crédito comercial | factura/API | días | notas de crédito | límite, factura, ERP, collections |
| Payment link | cualquiera soportado | URL | hereda instrumento | hereda instrumento | hosted checkout, expiración, anti-phishing |
| Invoice payment | cuenta/tarjeta | portal/ERP | variable | variable | referencia estructurada, virtual account |
| USSD/SMS | cuenta/wallet/telco | feature phone | segundos | variable | session gateway, SIM security, OTP |
| Carrier billing | saldo/factura telco | web/app/SMS | segundos | refund contractual | telco billing, revenue share, límites |
| Agente/corresponsal | efectivo↔cuenta/wallet | POS de agente | minutos | variable | agent network, float, recibo, geolocalización |
| Remesa | efectivo/cuenta/wallet | agente/web/app | minutos a días | limitada tras payout | KYC/AML, FX, corresponsales, payout network |
| Corresponsalía bancaria | cuenta bancaria | banco | días | recall limitado | SWIFT, nostro/vostro, sanctions screening |
| Cross-border acquiring | tarjeta | comercio remoto | segundos + settlement | chargeback | adquirencia local, FX, reglas territoriales |
| Criptoactivo no estable | activo digital | firma on-chain | bloques/finality | irreversible en protocolo | wallet, claves, fee market, chain analytics |
| Stablecoin | token referenciado | on-chain/off-chain | según red | normalmente irreversible | reservas, emisor, smart contract, bridges |
| CBDC | pasivo de banco central | wallet/infraestructura | diseño específico | diseño específico | ledger central/DLT, privacidad, offline |
| Depósito tokenizado | depósito bancario | plataforma autorizada | diseño específico | contractual | identidad, ledger programable, interoperabilidad |

## 1. Efectivo, contra entrega y valor cerrado

El efectivo ofrece finalidad práctica inmediata entre las partes y alta accesibilidad, pero introduce custodia física, error de conteo, robo, falsificación y conciliación de caja. En comercio electrónico, contra entrega desplaza el momento del pago hacia la logística: aumenta rechazo en puerta, efectivo en ruta y discrepancias entre pedido, transportista y caja.

Un gift card cerrado no es «dinero gratis»: al emitirlo nace un pasivo. El ledger debe distinguir emisión, activación, canje, expiración, reversa y breakage; las reglas contables y de protección al consumidor dependen de la jurisdicción.

## 2. Instrumentos de papel

Cheque y giros separan emisión, presentación, compensación y pago. La recepción del documento no equivale a fondos finales. Los sistemas modernos pueden truncar la imagen, pero persisten riesgos de alteración, duplicado, firma, falta de fondos y plazos de presentación.

## 3. Tarjetas

En el modelo de cuatro partes intervienen titular, emisor, comercio y adquirente, conectados por un esquema. El gateway no reemplaza necesariamente al adquirente. Una compra suele ejecutar autenticación, autorización, captura, clearing y settlement.

Tecnologías asociadas:

- **EMV chip/contactless**: credenciales y criptogramas dinámicos para presentación física.
- **ISO 8583**: familia de mensajes ampliamente usada en autorización de tarjetas; cada red define perfiles.
- **EMV 3-D Secure**: intercambio de datos y autenticación del titular en card-not-present.
- **Tokenización**: reemplaza PAN por un valor con dominio de uso; no es lo mismo que cifrado.
- **Hosted fields/redirect**: desplazan captura de datos al proveedor y pueden reducir alcance PCI, nunca lo eliminan automáticamente.
- **MCC, AVS, CVV result, risk signals**: señales; ninguna prueba por sí sola legitimidad.

Crédito, débito y prepago comparten parte de la aceptación, pero difieren en fuente de fondos, crédito, reservas, regulación y experiencia de disputa. Virtual, contactless y wallet suelen ser forma-factor o credencial, no un rail nuevo.

## 4. Cuenta a cuenta

Incluye credit transfers push, débitos pull, batch ACH, instant payments, wires y RTGS. Debe modelarse:

- identidad/datos del originador y beneficiario;
- cuenta, alias o proxy y resolución del directorio;
- validación y confirmación del beneficiario;
- cutoff, calendario, moneda y disponibilidad 24/7;
- estado entre aceptado, enviado, recibido, liquidado, retornado y recalled;
- razón estructurada y referencia para conciliación.

En Chile, TEF, efectivo, cheques y tarjetas forman parte del sistema minorista descrito por el Banco Central. El país opera además LBTR para alto valor y una cámara de bajo valor para TEF. La regulación y el diseño de pagos inmediatos evolucionan; hay que revalidar antes de implementar.

## 5. Billeteras, QR y dispositivos

Clasifica primero la fuente de fondos:

1. **Pass-through**: la wallet presenta una tarjeta o cuenta tokenizada; conserva economics y disputas del rail subyacente.
2. **Stored value**: la wallet mantiene un saldo; requiere ledger, cash-in/cash-out, protección de fondos y reglas de redención.
3. **Orquestadora**: selecciona entre varios medios y puede no custodiar valor.

QR merchant-presented y consumer-presented describen quién muestra y quién escanea. Un payload estático es barato pero puede ser sustituido; uno dinámico enlaza importe, comercio, expiración y nonce. NFC/wearables añaden device token, secure element o HCE y verificación del usuario en el dispositivo.

## 6. Crédito embebido

Cuotas, BNPL y POS financing son crédito, no solo UX. Deben separar la decisión de underwriting, el pago inmediato al comercio, el calendario del cliente, refunds parciales, mora, cobranza, reporte y costo total. El merchant no debe asumir que cancelar una orden cancela automáticamente el contrato de crédito.

## 7. Canales de cobro remoto y asistido

Payment link, invoice portal, QR, USSD y agentes reducen barreras de integración, pero introducen phishing, expiración, vinculación incorrecta del pedido, sesiones compartidas, float del agente y comprobantes falsos. La referencia de negocio debe viajar de extremo a extremo y nunca confiarse solo al texto libre.

## 8. Pagos transfronterizos

Intervienen más libros, intermediarios, horarios, jurisdicciones y conversiones. Modela por separado principal, fee, spread FX, moneda de presentación, moneda de liquidación, fecha valor, bancos corresponsales, beneficiario final y pruebas de origen. SWIFT transporta mensajes; no es por sí mismo el activo de liquidación.

## 9. Activos digitales y dinero tokenizado

Criptoactivos, stablecoins, CBDC y depósitos tokenizados no son equivalentes. Antes de aceptar uno pregunta:

- ¿Quién es el emisor y qué derecho tiene el tenedor?
- ¿Qué respalda el valor, dónde se custodia y cómo se redime?
- ¿Qué red, contrato, bridge o custodio puede fallar?
- ¿Cuándo existe finality técnica y jurídica?
- ¿Quién administra claves, listas, upgrades y congelamiento?
- ¿Cómo se ejecutan AML, sanciones, impuestos y refund?

Una transferencia irreversible no elimina fraude; cambia el punto de control hacia onboarding, autorización, custodia y recuperación operacional.

## Cómo elegir un medio

Evalúa alcance del cliente, conversión, costo total, velocidad de fondos, finality, refunds, disputas, fraude, datos, regulación, disponibilidad, conciliación y dependencia del proveedor. El medio con menor fee nominal puede costar más cuando se incorporan operación manual, fraude, FX, capital retenido y abandono.

> Fuente conceptual base: glosario CPMI/BIS y documentos oficiales enlazados en [`REFERENCES.md`](REFERENCES.md). La matriz es pedagógica y no sustituye reglas de esquema o contrato de proveedor.
