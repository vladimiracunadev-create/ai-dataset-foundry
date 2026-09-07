# Calidad y evaluación

La calidad no es un único score. Se mide por capas y contra el uso previsto.

| Dimensión | Pregunta | Medida típica |
| --- | --- | --- |
| extracción | ¿se perdió texto, orden o estructura? | muestreo contra originales, cobertura por página |
| limpieza | ¿se retiró ruido sin borrar significado? | diff y revisión estratificada |
| duplicación | ¿el corpus sobrepondera fuentes repetidas? | exact hash, SimHash, MinHash |
| privacidad | ¿quedan secretos o PII innecesaria? | detectores + revisión humana |
| representación | ¿idiomas, dominios y periodos están equilibrados? | distribución por metadato |
| contaminación | ¿train contiene respuestas del benchmark? | matching exacto y aproximado |
| utilidad | ¿mejora el objetivo real? | ablation y evaluación downstream |

Divide por documento o fuente antes de fragmentar cuando sea posible; dividir chunks al azar deja casi duplicados a ambos lados y produce métricas optimistas. Congela el conjunto de evaluación, versiona sus criterios y evita usar sus resultados como etiquetas de entrenamiento.

Para RAG mide recuperación (`recall@k`), calidad de contexto, respuesta fundamentada y citas. Para SFT evalúa cumplimiento, exactitud, seguridad y regresiones por segmento. Para pretraining observa pérdida por dominio y benchmarks externos, pero también memorization y comportamiento no deseado.
