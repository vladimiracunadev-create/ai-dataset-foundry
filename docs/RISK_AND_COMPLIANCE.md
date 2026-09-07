# Riesgo, fraude y compliance

## Cuatro problemas diferentes

- **Fraude**: engaño o uso no autorizado para obtener valor.
- **Crédito**: contraparte/cliente no paga una obligación.
- **Operacional**: proceso, persona, sistema o tercero falla.
- **Compliance**: se incumple norma, licencia, contrato, esquema o política.

Una regla antifraude no realiza KYC; PCI no es una ley antifraude; AML no garantiza que un pago sea legítimo. Diseña controles y responsables separados, con señales compartidas bajo propósito autorizado.

## Fraud lifecycle

```text
prevenir → detectar → decidir → autenticar/revisar → monitorear → aprender
```

### Señales

Identidad y antigüedad, device/session, IP/geografía, velocidad, importe, beneficiario, historial, comportamiento, resultado de autenticación, código del emisor y graph relationships. Evalúa calidad, consentimiento, sesgo, explicabilidad, estabilidad y costo de cada señal.

### Decisiones

`ALLOW`, `CHALLENGE`, `REVIEW`, `LIMIT` o `DENY`, siempre con versión y reason codes internos. Mide fraude capturado, falsos positivos, conversión, latencia, costo de revisión y drift. Una tasa baja puede esconder rechazo excesivo.

## AML/CFT y sanciones

El programa aplicable depende de actividad, licencia y jurisdicción. Puede incluir customer/business due diligence, beneficiario final, monitoreo, sanciones/PEP, recordkeeping y reportes. List screening sin desambiguación genera falsos positivos; pagos instantáneos requieren decisiones dentro de latencias estrictas.

No incluyas datos KYC reales en esta foundry. Para entrenamiento/evaluación usa casos sintéticos y revisión de privacidad.

## Protección al consumidor

Precio y moneda claros, consentimiento, comprobante, estado entendible, refunds, cancelación de recurrencia, atención y disputa. Dark patterns y consentimiento empaquetado aumentan riesgo aunque la API sea correcta. BNPL y crédito requieren disclosures y evaluaciones correspondientes.

## Privacidad

Inventario de datos, base/propósito, minimización, retención, derechos, transferencias internacionales, encargados, seguridad y evaluación de impacto. Distingue tokenización, seudonimización y anonimización real.

## Chile-first

El Banco Central vela por el normal funcionamiento de pagos y regula infraestructuras y medios dentro de sus atribuciones; la CMF supervisa actores y normativa aplicable. El sistema incluye efectivo, cheques, tarjetas y TEF; para alto valor opera LBTR. La Ley 20.950 habilitó emisión/operación de medios con provisión de fondos por no bancos. La Ley Fintec 21.521 y la NCG 514 conforman el Sistema de Finanzas Abiertas, cuya implementación es dinámica.

No conviertas este resumen en checklist legal. Antes de producción revalida Compendio de Normas Financieras, normativa CMF, protección de datos/consumidor, tributación, contratos y reglas del esquema con especialistas responsables.

## Matriz de obligaciones

Para cada flujo registra:

| Campo | Pregunta |
| --- | --- |
| Actividad/rol | ¿merchant, PSP, operador, emisor, custodio, agente? |
| Entidad/jurisdicción | ¿quién contrata y desde dónde presta? |
| Licencia/registro | ¿propio, patrocinado o exento? |
| Fondos | ¿quién recibe, salvaguarda, liquida y concilia? |
| Datos | ¿qué categoría, propósito, ubicación y retención? |
| Consumidor | ¿disclosure, consentimiento, refund y disputa? |
| Seguridad | ¿PCI, autenticación, cifrado y notificación? |
| Evidencia | ¿contrato, opinión, certificación y fecha de revisión? |

## Riesgo de terceros

Evalúa solvencia, continuidad, subprocesadores, residencia, incidentes, auditorías, concentración, exit plan y portabilidad. Un proveedor multi-rail puede ser un single point of commercial failure aunque su infraestructura sea redundante.

Fuentes oficiales con fecha de consulta: [`REFERENCES.md`](REFERENCES.md).
