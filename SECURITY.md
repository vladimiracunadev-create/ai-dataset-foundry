# Política de seguridad

Reporta vulnerabilidades mediante **Security → Report a vulnerability** en GitHub; no publiques exploits, credenciales ni muestras privadas en issues.

## Modelo de amenazas

Las entradas son hostiles: PDF/DOCX comprimidos, HTML activo, repositorios con rutas maliciosas, URLs internas, archivos enormes, Unicode engañoso y secretos incrustados. La v0.2.0 es un laboratorio local, no un servicio expuesto ni un sandbox de documentos.

- Ejecuta con privilegios mínimos y fuentes confiables.
- No abras la UI fuera de `127.0.0.1`.
- Limita tamaño, tiempo, red y almacenamiento en despliegues reales.
- No pases credenciales en URL ni publiques `work/`.
- Escanea dependencias y artefactos; valida checksums del release.
- Trata el detector de secretos como señal auxiliar, no garantía.

Android no solicita permiso Internet. Windows inicia un servidor efímero solo en loopback. Las versiones soportadas son la última release y `main` hasta que exista una política LTS.
