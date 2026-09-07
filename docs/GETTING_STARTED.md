# Primer recorrido

Esta guía lleva una fuente sintética hasta un dataset verificable sin ocultar decisiones. AI Dataset Foundry prepara datos; el entrenamiento ocurre después, en el framework o servicio elegido.

## 1. Preparar el entorno

Requiere [uv](https://docs.astral.sh/uv/), Python 3.11 o superior y Git. La interfaz, PDF, Word, web y Parquet se instalan con el extra `all`.

```bash
uv sync --extra all --extra dev --locked
uv run python scripts/doctor.py
```

## 2. Probar la interfaz

```bash
foundry serve
```

Abre `http://127.0.0.1:8765`. Arrastra un archivo, elige JSONL y ejecuta. Cada ejecución vive bajo `work/ui-runs/<id>` y expone su manifest y artefactos. El servidor escucha solo en loopback: no es un servicio multiusuario.

## 3. Ejecutar una receta reproducible

```bash
foundry build --config examples/config.yaml
foundry stats work/example-from-config/dataset.jsonl
foundry validate examples/config.yaml
```

Revisa `manifest.json` antes del dataset: enumera entradas, configuración, documentos, rechazos, duplicados, errores y salidas. Después inspecciona una muestra de JSONL y comprueba que el texto, la licencia y la procedencia sean aceptables.

## 4. Incorporar fuentes reales

Empieza con una copia autorizada y pequeña. Añade una modalidad por vez, conserva los originales fuera de `work/`, fija el commit de repositorios cuando la reproducibilidad importe y documenta licencia, fecha de corte y responsable. Nunca uses el corpus de evaluación para ajustar el modelo.

Siguiente lectura: [conectores](CONNECTORS.md), [configuración](CONFIGURATION.md) y [preparación para entrenamiento](TRAINING_READINESS.md).
