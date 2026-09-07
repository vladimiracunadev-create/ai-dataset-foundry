# Preparación para aprendizaje de modelos

## La foundry produce materia prima, no aprendizaje garantizado

Un mismo corpus neutral puede alimentar cuatro procesos, pero cada uno exige un contrato distinto.

## Pretraining y continued pretraining

Objetivo: aprender distribución de lenguaje/dominio mediante predicción de tokens. Requiere gran escala, mezcla de fuentes, tokenizer, packing, sampling weights, deduplicación global, filtros de calidad, control de contaminación y presupuesto de cómputo.

Salida recomendada desde la foundry: JSONL/Parquet con texto, fuente, licencia, idioma, timestamps y hashes. Paso downstream: tokenizar y construir shards inmutables con distribución documentada.

## Fine-tuning supervisado

Objetivo: enseñar comportamiento mediante pares instrucción-respuesta o conversaciones. Los chunks extraídos **no son respuestas correctas por sí mismos**. Se necesita diseñar tareas, redactar/etiquetar ejemplos, revisar exactitud y exportar al schema del trainer.

```json
{"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}
```

Conserva `source_chunk_ids` fuera o dentro de metadata para auditar cada respuesta. Separa train/validation/test antes de generar variantes cercanas.

## Embeddings y RAG

Objetivo: recuperar evidencia al responder sin incorporarla permanentemente en pesos. Usa chunks con título, jerarquía, URL/ruta, página, ACL y fecha. Genera embeddings, indexa y evalúa retrieval antes de evaluar generación.

Métricas: Recall@k, MRR/nDCG, context precision/recall, faithfulness, citation correctness, latencia y costo. Un vector database no corrige chunks pobres ni permisos rotos.

## Evaluación

Un dataset de evaluación debe permanecer independiente del entrenamiento. Incluye input, referencia/rúbrica, metadata de slice, fuente y versión. Evita contamination por duplicados exactos y semánticos.

## Dataset card mínima

- propósito y usos prohibidos;
- composición, idiomas, dominios y periodo;
- origen, licencia/autoridad y método de colección;
- transformaciones y filtros;
- PII, riesgos, sesgos y población ausente;
- splits y estrategia anti-leakage;
- versión, hashes y responsable;
- métricas y limitaciones conocidas.

## Criterios de aceptación

El dataset está listo solo si puede reproducirse, todo registro tiene procedencia suficiente, los errores obligatorios están resueltos, no contiene secretos conocidos, los splits no filtran documentos entre sí, el formato carga en el trainer/indexador y un domain reviewer aprueba muestras y extremos.
