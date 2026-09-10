# 09. APIs e integraciones

## API HTTP local

Base predeterminada: `http://127.0.0.1:8765`. Sin autenticación, autorización, CORS configurado, CSRF token ni versionado de URL; no debe exponerse en red.

| Método/ruta | Solicitud | Respuesta / errores |
| --- | --- | --- |
| `GET /` | sin parámetros | frontend HTML |
| `GET /api/health` | sin parámetros | 200, estado y versión |
| `POST /api/build` | multipart; `files*`, `locators` JSON, `formats` JSON, `chunk_strategy`, `chunk_size`, `overlap`, `reject_secrets` | 200 con run/conteos/artefactos; 400 datos/build; 413 >50 MiB por archivo |
| `GET /api/runs/{run_id}/artifacts/{name}` | segmentos simples | archivo; 400 traversal/ID, 404 ausente |

```bash
curl -F 'files=@examples/sample.txt;type=text/plain' \
  -F 'locators=[]' -F 'formats=["jsonl"]' \
  http://127.0.0.1:8765/api/build
```

Respuesta abreviada: `{"run_id":"…","documents":1,"chunks":n,"artifacts":[…]}`. No existe OpenAPI pública porque `/docs` y `/redoc` están deshabilitados, aunque FastAPI puede mantener `/openapi.json` por defecto (inferencia basada en configuración).

## Integraciones externas

- **HTTP(S):** Requests realiza una descarga de página con User-Agent propio; Trafilatura o BS4 extraen HTML. Timeout/reintentos/límites/robots: revisar `connectors/web.py`; no hay crawler.
- **Git:** ejecutable externo, clone shallow y temporal. Autenticación utiliza el entorno de Git del usuario; no almacena tokens.
- **Documentos:** pypdf y python-docx; HTML local con BS4.
- **Parquet:** PyArrow con compresión Zstd.
- **UI/desktop:** FastAPI, Uvicorn, multipart y pywebview en loopback.
- **GitHub:** Actions para CI, auditoría, Pages y release; Dependabot para actualizaciones.

No hay webhooks, OAuth, proveedores de modelos, bases remotas ni límites de proveedor modelados. Los códigos HTTP remotos no se exponen como contrato propio; excepciones se registran en manifest (CLI) o terminan como 400 (API).
