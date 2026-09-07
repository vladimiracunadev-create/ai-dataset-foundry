# Actualizaciones incrementales

La versión 0.2.0 calcula hashes estables, pero reconstruye el conjunto completo. La evolución incremental debe convertir cada build en una transformación explicable, no en una sobrescritura silenciosa.

## Diseño objetivo

1. Resolver una identidad estable de fuente.
2. Comparar `source_sha256` con el registro anterior.
3. Reprocesar solo altas y cambios; emitir tombstones para bajas.
4. Mantener relación entre versión de documento y chunks derivados.
5. Publicar un manifest inmutable y un diff: añadidos, modificados, retirados y rechazados.
6. Reconstruir índices derivados de forma transaccional.

Versiona dataset, esquema, código, configuración y tokenizer por separado. Un SemVer de aplicación no sustituye una versión de datos. Para grandes volúmenes, Apache Iceberg, Delta Lake o lakeFS pueden aportar snapshots; DVC puede rastrear artefactos; MLflow registra experimentos. Su adopción depende del entorno y no forma parte del núcleo actual.
