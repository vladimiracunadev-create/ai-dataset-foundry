# Política de seguridad

## Reportar una vulnerabilidad

No abras un issue público con detalles explotables, secretos ni datos personales. Usa el canal privado **Security → Report a vulnerability** del repositorio en GitHub. Incluye versión/commit, impacto, prerequisitos, pasos mínimos y mitigación propuesta. No incluyas datos reales de pago.

Se intentará confirmar recepción dentro de 5 días hábiles y comunicar evaluación/plan dentro de 10; son objetivos de mantenedor, no SLA contractual.

## Versiones soportadas

Mientras el proyecto esté en `0.x`, solo la rama `main` y la última release reciben correcciones.

## Alcance permitido

Pruebas sobre tu copia local con datos sintéticos. No se autoriza atacar GitHub, proveedores enlazados, sistemas financieros, cuentas, comercios ni terceros. Detén la prueba si accedes a datos que no te pertenecen.

## Prohibiciones del repositorio

- PAN/CVV/PIN/track data o credenciales reales, incluso en fixtures;
- secretos en commits, issues, logs o capturas;
- apuntar ejemplos a producción;
- presentar el detector de privacidad como DLP/PCI;
- ejecutar contenido ingerido;
- desactivar validación TLS o firma para «hacer funcionar» una demo.

Modelo completo: [`docs/SECURITY_MODEL.md`](docs/SECURITY_MODEL.md).
