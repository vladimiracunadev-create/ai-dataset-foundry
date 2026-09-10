# Documentación integral de AI Dataset Foundry

AI Dataset Foundry es una factoría local-first que convierte fuentes heterogéneas en corpus auditables para pretraining, fine-tuning, RAG y evaluación. Esta carpeta reúne una lectura verificable del repositorio para personas no técnicas, desarrollo, operación, auditoría y agentes de IA.

**Corte del análisis:** 2026-09-10. **Versión:** 0.2.0. **Commit base:** `322e298`. **Estado:** completa y verificada contra el código; las inferencias y ausencias se señalan expresamente.

## Índice y estado

| Documento | Finalidad | Estado |
| --- | --- | --- |
| [01. Descripción general](01-system-overview.md) | propósito, actores y alcance | Verificado |
| [02. Instalación y ejecución](02-installation-and-execution.md) | preparar, ejecutar y probar | Verificado |
| [03. Arquitectura](03-architecture.md) | componentes, secuencias y despliegue | Verificado |
| [04. Mapa del código](04-code-map.md) | inventario y responsabilidades | Verificado |
| [05. Referencia técnica](05-technical-reference.md) | contratos, símbolos, rutas y errores | Verificado |
| [06. Explicación profunda](06-deep-code-explanation.md) | recorrido interno del pipeline | Verificado |
| [07. Base de datos](07-database.md) | esquema SQLite y persistencia | Verificado |
| [08. Flujo de datos](08-data-flow.md) | entradas, transformaciones y salidas | Verificado |
| [09. APIs e integraciones](09-apis-and-integrations.md) | HTTP local y proveedores | Verificado |
| [10. Configuración](10-configuration.md) | YAML, CLI y valores | Verificado |
| [11. Seguridad](11-security.md) | controles y superficie de ataque | Verificado |
| [12. Pruebas y calidad](12-testing-and-quality.md) | CI, pruebas y brechas | Verificado |
| [13. Despliegue y operación](13-deployment-and-operations.md) | releases, Pages y runbook | Verificado |
| [14. Troubleshooting](14-troubleshooting.md) | diagnóstico práctico | Verificado |
| [15. Riesgos y deuda](15-risks-and-technical-debt.md) | hallazgos priorizados | Verificado |
| [16. Glosario](16-glossary.md) | lenguaje técnico y del dominio | Verificado |
| [17. Resumen ejecutivo](17-executive-summary.md) | lectura para decisión | Verificado |
| [18. Guía de incorporación](18-new-developer-guide.md) | itinerario para contribuir | Verificado |
| [19. Trazabilidad](19-traceability-matrix.md) | función a implementación y prueba | Verificado |
| [PDF](pdf/) | versiones generadas desde Markdown | Generado y revisado |

## Convenciones

- **Comprobado:** visible en código, manifest, prueba o workflow.
- **Inferencia basada en el código:** conclusión razonable no declarada como contrato.
- **No documentado en el repositorio:** no existe evidencia suficiente.
- Rutas, nombres de símbolos y comandos se conservan literalmente; no se reproducen secretos.

## Pendientes de validación humana

- Política formal de retención/borrado, SLA, soporte LTS y propietario operativo: no documentados.
- Modelo jurídico para derechos de cada corpus, clasificación de PII y base legal: depende del operador.
- Carga, rendimiento máximo y seguridad de parsers ante documentos hostiles: requieren pruebas aisladas.
- La UI y el host Windows no son un servicio multiusuario ni un sandbox.

Los PDF se regeneran con `python scripts/generate_system_pdfs.py`; Markdown es la única fuente editable.
