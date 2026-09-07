# Gobierno de datos

Preparar datos de entrenamiento o RAG es un problema de derechos, privacidad, seguridad y calidad, no solo parsing.

## Gates obligatorios

| Gate | Evidencia mínima |
| --- | --- |
| Autoridad | propietario/licencia/términos y uso permitido |
| Propósito | finalidad, audiencia, modelo y uso prohibido |
| Privacidad | categorías, base, minimización, retención y acceso |
| Seguridad | clasificación, secret scan, almacenamiento y transferencia |
| Procedencia | localizador, fecha, hash, versión y transformaciones |
| Calidad | cobertura, idioma, duplicados, ruido, sesgos y rechazo |
| Evaluación | split por documento/fuente, leakage y criterios |
| Publicación | revisión humana, manifest, license y rollback |

## Regla especial para pagos

No se aceptan PAN, CVV/CVC, PIN/PIN block, track data, tokens vivos, API keys, secretos de webhook, datos KYC, cuentas reales ni transacciones de clientes. Los ejemplos deben ser conceptuales o sintéticos y no parecer credenciales utilizables. Si una fuente autorizada contiene datos sensibles, se rechaza antes de la foundry; el detector ligero no es una zona de descontaminación.

## Procedencia y transformaciones

Conserva originales inmutables fuera del repo, hash, licencia, fecha de obtención, configuración, versión del pipeline, manifest y aprobador. Un hash demuestra igualdad de bytes, no autenticidad ni legalidad.

## Separación de datasets

Divide train/validation/test por documento, entidad o fuente según el riesgo de leakage; nunca por chunks aleatorios del mismo documento. Mantén un holdout que no haya influido en prompts, reglas ni selección.

## Corrección y retiro

Un dataset publicado necesita identificador/version, lineage hacia chunks afectados, procedimiento de takedown, capacidad de regeneración y registro de consumidores. El borrado del archivo fuente no retira automáticamente embeddings, caches, checkpoints o exportaciones.

## Roles

- Data owner: autoriza propósito y riesgo.
- Steward: mantiene procedencia, calidad y catálogo.
- Security/privacy: revisa datos sensibles y controles.
- Domain reviewer: valida significado y vigencia.
- Operator: ejecuta pipeline y preserva evidencia.

Nadie debe autoaprobar una excepción que haya solicitado.
