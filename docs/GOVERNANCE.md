# Gobierno, derechos y procedencia

Un pipeline técnicamente correcto puede producir un dataset legal o éticamente inaceptable. Antes de adquirir una fuente registra propietario, licencia o base de autorización, propósito, jurisdicción, sensibilidad, retención y contacto responsable.

## Puertas de decisión

1. **Admisión:** ¿está permitido copiar, transformar y usar para el objetivo declarado?
2. **Minimización:** ¿puede excluirse información personal, secreta o irrelevante?
3. **Curación:** ¿hay idioma, dominio, fecha, calidad y representación suficientes?
4. **Separación:** ¿train, validation, test y material confidencial están aislados?
5. **Publicación:** ¿artefactos, muestras, logs y manifest pueden hacerse públicos?
6. **Retiro:** ¿es posible localizar y eliminar una fuente y sus derivados?

## Lineage mínimo

Conserva locator, hash de fuente, hash de contenido, fecha de corte, versión del pipeline, configuración, licencia declarada y decisiones humanas. Un hash ayuda a responder “qué cambió”; no responde “quién autorizó”. Esa evidencia vive fuera del texto de entrenamiento y debe conservarse durante todo su ciclo de vida.

## Privacidad

La detección incluida es una barrera ligera. Para producción incorpora clasificación, DLP, revisión humana, políticas de retención, control de acceso, cifrado, borrado verificable y evaluación de reidentificación. Evita publicar fragmentos de ejemplo obtenidos de fuentes privadas.
