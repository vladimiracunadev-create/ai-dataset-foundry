# 15. Riesgos y deuda técnica

Este registro informa; no implica corrección automática.

| Hallazgo | Severidad/prob. | Evidencia | Impacto y recomendación |
| --- | --- | --- | --- |
| SSRF si API se expone | Alta/Media | `web.py` + POST locators | bloquear red interna/redirects; mantener loopback |
| Parsers no aislados | Alta/Media | PDF/DOCX/Git en proceso | workers con budgets antes de producción |
| Detector incompleto | Alta/Alta | regex de `privacy.py` | DLP y revisión humana |
| Sin auth/RBAC | Alta/Media | `webapp.py` | no exponer; añadir controles si cambia alcance |
| Escritura no atómica global | Media/Media | pipeline/exportadores | staging + rename/commit coordinado |
| Manifest SQLite diverge | Media/Alta | DB recibe manifest antes de clave `sqlite` | finalizar manifest antes de ambos |
| Dedup antes de calidad | Media/Media | `pipeline.py` | copia rechazada puede ocultar posterior; reordenar/elegir mejor |
| SimHash O(n²) | Media/Alta a escala | lista de hashes | LSH/banding y benchmark |
| Git/FS sin budgets | Alta/Media | router/git | cuotas y cancelación |
| Retención indefinida | Media/Alta | `work/ui-runs` | TTL/cuota/borrado |
| Excepciones crudas | Media/Media | `str(exc)` | tipar y redactar |
| IDs truncados | Baja/Baja | 80 bits en `stable_id` | documentar; ampliar si escala |
| `Connector` sin uso | Baja/Alta | `base.py` | adoptar o retirar |
| Android duplica lógica | Media/Media | implementación separada | fixtures contractuales cruzados |
| Cobertura estrecha | Media/Alta | 9 tests | ejecutar plan del documento 12 |
| Sin firma/SBOM | Media/Media | sólo checksums | provenance, SBOM y firma |

Obsolescencia concreta no se afirma sin auditoría fechada. Licencias de fuentes, límites de rendimiento y compatibilidad JDK requieren validación.
