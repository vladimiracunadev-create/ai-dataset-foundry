# Configuración

La CLI recibe un YAML validado por Pydantic. Una configuración es parte de la evidencia del dataset y debe versionarse junto con el código.

```yaml
inputs:
  - corpus/manuales
  - https://example.org/guia
  - https://github.com/organizacion/repositorio.git
out_dir: work/dataset-v1
formats: [jsonl, txt, parquet]
recursive: true
write_sqlite: true
chunk:
  strategy: paragraph
  size: 1200
  overlap: 120
quality:
  min_chars: 80
  max_control_ratio: 0.02
  reject_secrets: true
dedup:
  enabled: true
  near_duplicate: true
  simhash_distance: 3
```

## Entradas y salidas

`inputs` acepta archivos, directorios, URL HTTP(S) y repositorios Git. `recursive` gobierna el descenso por directorios. `formats` admite `jsonl`, `txt` y `parquet`; SQLite se controla separadamente. `out_dir` debe ser desechable: el pipeline puede regenerarlo, pero nunca modifica la fuente.

## Segmentación

- `paragraph`: agrupa párrafos hasta el tamaño objetivo; buen valor general.
- `sentence`: respeta fronteras aproximadas de oración.
- `markdown`: favorece encabezados y bloques documentales.
- `fixed`: ventanas deterministas; útil como baseline, menos semántico.

`size` y `overlap` se expresan en caracteres, no tokens. El tokenizer del modelo debe medir el resultado final. Un solapamiento grande mejora continuidad pero incrementa duplicación, almacenamiento y riesgo de leakage.

## Calidad y deduplicación

`min_chars` rechaza fragmentos triviales. `max_control_ratio` limita caracteres de control. `reject_secrets` detecta patrones evidentes, pero no sustituye DLP ni revisión. SimHash aproxima similitud léxica; una distancia menor es más conservadora. Para corpus críticos conserva el registro de rechazados y revisa falsos positivos.
