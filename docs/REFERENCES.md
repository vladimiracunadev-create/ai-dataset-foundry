# Fuentes oficiales y revalidación

Fecha de consulta: **2026-09-07**. Se enlazan fuentes primarias; el repositorio no redistribuye estándares sujetos a licencia. Las versiones y normas cambian: verifica el documento vigente antes de una implementación.

## Fundamentos e infraestructura

- [CPMI/BIS — Glossary](https://www.bis.org/committees/cpmi/glossary): terminología de pagos, clearing, settlement, actores e infraestructura.
- [CPMI-IOSCO — Principles for Financial Market Infrastructures](https://www.bis.org/cpmi/publ/d101a.htm): principios de riesgo para infraestructuras de mercado.
- [ISO 20022](https://www.iso20022.org/): metodología y repositorio de mensajes financieros. Un mensaje compatible no garantiza reglas de negocio interoperables sin un implementation guideline.

## Tarjetas, autenticación y web

- [PCI SSC — PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/): requisitos para proteger datos de cuenta; consultar biblioteca para versión vigente.
- [PCI SSC — Document Library](https://www.pcisecuritystandards.org/document_library/): PCI DSS 4.0.1, SAQ y documentos relacionados.
- [EMVCo — EMV 3-D Secure](https://www.emvco.com/emv-technologies/3-d-secure/): autenticación e intercambio de datos CNP.
- [EMVCo — Payment Tokenisation](https://www.emvco.com/emv-technologies/payment-tokenisation/): tokens con restricciones de dominio y roles del framework.
- [EMVCo — QR Codes](https://www.emvco.com/emv-technologies/qr-codes/): modos merchant-presented y consumer-presented.
- [W3C — Payment Request API](https://www.w3.org/TR/payment-request/): interfaz del navegador entre pagador, payee y payment method. La publicación 2026 es Candidate Recommendation Draft; no debe presentarse como garantía universal de soporte.

## Pagos instantáneos y regionales

- [Federal Reserve — FedNow](https://www.federalreserve.gov/paymentsystems/fednow_about.htm): servicio RTGS 24x7x365 para instituciones depositarias de EE. UU., operativo desde 2023.
- [European Central Bank — TIPS](https://www.ecb.europa.eu/paym/target/tips/html/index.en.html): settlement de pagos instantáneos en dinero de banco central 24/7/365.
- [European Payments Council — SEPA schemes](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-payment-schemes): credit transfer, instant y direct debit bajo reglas SEPA.
- [Nacha — ACH Network](https://www.nacha.org/content/ach-network): recursos oficiales del esquema ACH de EE. UU.

## Chile

- [Banco Central de Chile — Sistemas de pagos](https://www.bcentral.cl/areas/sistemas-de-pagos): alto valor, bajo valor, LBTR, instrumentos y normativa.
- [Banco Central de Chile — Informe de Sistemas de Pago](https://www.bcentral.cl/es/areas/politica-financiera/informe-de-sistemas-de-pago): tendencias, riesgos y agenda regulatoria; revisar edición vigente.
- [Banco Central de Chile — Compendio de Normas Financieras](https://www.bcentral.cl/es/web/banco-central/areas/normativas/compendio-de-normas-financieras): capítulos III.H y III.J, entre otros aplicables.
- [BCN — Ley 20.950](https://www.bcn.cl/leychile/navegar?idNorma=1096097): medios de pago con provisión de fondos por entidades no bancarias.
- [BCN — Ley 21.521](https://www.bcn.cl/leychile/navegar?idNorma=1187323): Ley Fintec y marco del Sistema de Finanzas Abiertas.
- [CMF — normativa del Sistema de Finanzas Abiertas](https://www.cmfchile.cl/portal/principal/613/w3-propertyvalue-43591.html): NCG 514, anexos y calendario vigente.

## Protocolo de actualización

1. Abrir la fuente oficial, no un blog de proveedor.
2. Registrar versión/fecha de vigencia y jurisdicción.
3. Comparar el flujo afectado, no reemplazar números globalmente.
4. Actualizar resumen y fecha de consulta sin modificar historia del changelog.
5. Ejecutar `python scripts/verify_docs.py` y revisar enlaces en CI.

## Límite de interpretación

Las fuentes explican estándares y normas generales. La aplicación a una entidad depende de rol, contrato, licencia, flujo de fondos, datos, país y hechos. Este laboratorio enseña a formular y verificar esas preguntas; no emite una opinión jurídica.
