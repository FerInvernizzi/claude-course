"""Hook de MkDocs: convierte enlaces a archivos que no forman parte del sitio
(plantillas, código, configuración de Claude) en enlaces al repositorio de GitHub.

Así el contenido sigue funcionando igual en GitHub y en el sitio publicado.
"""

import posixpath
import re

REPO = "https://github.com/FerInvernizzi/claude-nube"
RAMA = "main"
FUERA_DEL_SITIO = ("plantillas/", "codigo/", "../.claude/", "../hooks/")
ENLACE = re.compile(r"\]\((?!https?:|mailto:|#)([^)\s#]+)(#[^)\s]*)?\)")


def on_page_markdown(markdown, page, config, files):
    carpeta = posixpath.dirname(page.file.src_uri)  # relativo a curso/

    def reemplazar(m):
        destino, ancla = m.group(1), m.group(2) or ""
        ruta = posixpath.normpath(posixpath.join(carpeta, destino))
        if destino.endswith("/"):
            ruta += "/"
        if not ruta.startswith(FUERA_DEL_SITIO):
            return m.group(0)
        en_repo = posixpath.normpath(posixpath.join("curso", ruta))
        tipo = "tree" if destino.endswith("/") else "blob"
        return f"]({REPO}/{tipo}/{RAMA}/{en_repo}{ancla})"

    return ENLACE.sub(reemplazar, markdown)
