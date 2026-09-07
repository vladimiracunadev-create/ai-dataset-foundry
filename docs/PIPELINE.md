# Pipeline de preparación

## Orden operacional

```text
descubrir → adquirir → extraer → normalizar → limpiar → segmentar
→ evaluar → deduplicar → exportar → manifestar → validar downstream
```

La implementación actual deduplica sobre piezas segmentadas y evalúa calidad durante su construcción. El orden exacto es una decisión versionada: mover una etapa cambia el dataset.

## Descubrimiento y adquisición

Define inventario, permiso, snapshot y criterio de completitud antes de descargar. Una carpeta accesible no implica autorización. Registra fuente esperada frente a cargada para distinguir build exitoso de build completo.

## Normalización

Unicode NFKC, finales de línea y whitespace coherente reducen duplicados artificiales. NFKC puede cambiar caracteres con significado; datasets multilingües, matemáticos o de código deben evaluar NFC o política por fuente.

## Limpieza

Elimina controles y ruido repetitivo sin borrar evidencia. Encabezados/pies, navegación, OCR garbage y boilerplate requieren reglas explicables. Conserva raw y normalized por capas si necesitas auditoría fuerte.

## Segmentación

| Estrategia | Ventaja | Riesgo |
| --- | --- | --- |
| Párrafo | semántica natural de prosa | párrafos gigantes o muy breves |
| Oración | granularidad fina | abreviaturas/idiomas rompen heurística |
| Markdown | conserva secciones | depende de headings correctos |
| Fija | determinista y simple | corta ideas y mezcla estructuras |

`size` actual se mide en caracteres, no tokens. Para un modelo concreto se debe usar su tokenizer, reservar espacio para instrucciones/metadata y medir distribución p50/p95/p99.

El overlap puede mejorar continuidad en RAG, pero multiplica volumen y contaminación entre splits. La versión actual solo lo aplica a chunking fijo.

## Calidad

Se rechaza contenido corto, exceso de controles y, opcionalmente, posibles secretos. El score no mide verdad, utilidad, sesgo, idioma o licencia. Reglas futuras deben producir reason codes, métricas y muestras revisables.

## Deduplicación

SHA/text hash elimina exactos; SimHash aproxima similitud léxica mediante distancia Hamming. Se necesita dedup antes de split para impedir leakage. A gran escala: MinHash/LSH, embeddings o suffix arrays, siempre evaluados con pares positivos/negativos.

## Exportación y manifest

JSONL es canónico para interoperabilidad. TXT pierde metadata. Parquet optimiza análisis columnar. SQLite permite inspección local. El manifest registra inputs, settings, conteos, errores y outputs; v0.3 agregará commit, dependencias y checksums finales.

## Validación downstream

Antes de entrenar:

1. parsea todo el output con el consumidor real;
2. mide tokens, idioma, dominios y longitudes;
3. inspecciona muestras aleatorias y extremos;
4. repite secret/PII/license scan;
5. deduplica contra benchmarks y evaluación;
6. divide por documento/fuente/entidad, no por chunk al azar;
7. versiona dataset, código, configuración y tokenizer.
