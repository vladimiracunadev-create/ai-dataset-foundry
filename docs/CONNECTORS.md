# Modalidades de lectura y bibliotecas

## Regla común

Extraer texto no basta. Cada modalidad debe conservar estructura útil, provenance y señales de pérdida. La salida canónica es `DocumentRecord`, nunca una cadena anónima.

## Texto, Markdown y código

Implementación: `pathlib.Path.read_text(encoding="utf-8", errors="replace")`.

Adecuado para TXT, MD, RST y extensiones de código registradas. Markdown conserva encabezados para chunking; el código se trata hoy como texto. Para producción de code datasets convienen tree-sitter, símbolos, imports, lenguaje, licencia por archivo, filtros de vendored/generated y deduplicación a nivel repositorio.

Riesgos: encoding mal detectado, archivos minificados/generados, secretos, comentarios legales y binarios con extensión engañosa.

## PDF

Implementación: `pypdf.PdfReader`; una unidad por página, con `page` y `pages`.

Un PDF es un formato de presentación, no una estructura semántica. Orden de lectura, columnas, tablas, encabezados, ligaduras y guiones pueden degradarse. Si `extract_text()` no produce texto, el documento probablemente necesita OCR; v0.2.0 lo omite en vez de fingir contenido.

Tecnologías afines:

- PyMuPDF/pdfplumber: layout, bounding boxes y tablas;
- OCRmyPDF: agrega capa OCR preservando PDF;
- Tesseract, PaddleOCR, EasyOCR, docTR: reconocimiento;
- LayoutParser, Docling, Unstructured: segmentación documental;
- Apache Tika: extracción amplia mediante proceso aislado.

## Word DOCX

Implementación: `python-docx`; párrafos y celdas de tabla se unen en orden lógico disponible.

DOCX es un contenedor ZIP de XML. Estilos, encabezados, notas, comentarios, tracked changes, cuadros de texto e imágenes requieren políticas explícitas. `python-docx` es ligero para el baseline; OOXML directo, Mammoth o Tika cubren necesidades distintas.

## HTML local y páginas web

HTML local usa Beautiful Soup y elimina `script`, `style`, `noscript` y `template`. Web usa Requests, timeout de 30 segundos, User-Agent identificable y Trafilatura; BS4 es fallback.

El conector actual descarga una sola URL. Un crawler serio debe respetar robots.txt y términos, limitar dominio/profundidad, aplicar rate limit y backoff, canonicalizar URL, detectar idioma/contenido, cachear ETag/Last-Modified, registrar redirects y evitar SSRF/redes privadas.

Tecnologías: Trafilatura/Readability para contenido principal; Scrapy/Playwright para crawling/render; sitemap/RSS para descubrimiento; WARC para captura reproducible. Renderizar JavaScript amplía ataque, costo y variabilidad.

## Repositorios Git

Local: exige `.git`; remoto: shallow clone `--depth 1 --filter=blob:none`. Solo procesa extensiones allowlisted y conserva `repository` y `path`.

Para reproducibilidad se debe fijar commit, registrar remoto, filtrar submodules/LFS, binarios, secretos, vendored y generated. Para actualización incremental, `git diff old..new` identifica archivos añadidos, modificados y eliminados.

## JSON y JSONL

JSON array produce una unidad por elemento; objeto único, una unidad. JSONL produce una por línea. Si existe `text`, se usa; si no, se serializa el objeto. Metadata conserva índice/línea y objeto original.

En producción conviene JSON Schema, JSONPath/JMESPath configurable, límite de profundidad/tamaño y política para campos sensibles.

## CSV

`csv.DictReader` conserva nombres y fila. Usa columna `text` si existe; de lo contrario concatena pares no vacíos. UTF-8 BOM está soportado.

Pendientes: detección de dialecto/encoding, schemas, columnas seleccionables, valores nulos tipados y formatos tabulares grandes mediante Polars/PyArrow.

## Modalidades planificadas

| Modalidad | Pipeline recomendado | Consideración crítica |
| --- | --- | --- |
| Imagen | EXIF → OCR/caption → regiones | no confundir caption con verdad visual |
| Audio | decode → VAD → ASR → diarización | consentimiento, timestamps, hablantes |
| Vídeo | escenas + audio ASR + frames/OCR | costo, sincronización, copyright |
| Base SQL | snapshot/CDC → mapping → records | consistencia, PII, carga sobre origen |
| API | paginación/checkpoint → schema | rate limit, auth, cambios de contrato |
| S3/Blob/Drive | inventory → object versions | permisos, egress y version IDs |
| Email/chat | threads → mensajes/adjuntos | privacidad, identidad, contexto |

Nombrar una biblioteca no implementa una modalidad. Cada una permanece `PLANIFICADO` hasta tener código, pruebas, fixtures, manifest y límites.
