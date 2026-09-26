# claude-nube

<img src="curso/assets/encabezado.svg" alt="Curso de Claude — guía práctica en español" width="100%">

Este repositorio contiene un **curso práctico de Claude en español**: Cowork, Claude Code, Skills, Plugins, MCP, Excel, PowerPoint, modelos financieros, agentes, un agente personal con 10 automatizaciones, funciones avanzadas y skills de nicho.

🌐 **Leelo como sitio web:** [ferinvernizzi.github.io/claude-nube](https://ferinvernizzi.github.io/claude-nube/)

➡️ O en GitHub: **[índice del curso](curso/README.md)**

El repositorio también trae configurados, en `.claude/settings.json`, los plugins oficiales que usa el curso, y la skill `revision-calidad-curso` en `.claude/skills/`. Al abrirlo con Claude Code quedan disponibles.

## Publicación

El sitio se genera con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) a partir de la carpeta `curso/` (configuración en `mkdocs.yml`) y se publica automáticamente en GitHub Pages con cada cambio en `main` (`.github/workflows/pages.yml`).

Para verlo en tu computadora:

```bash
pip install -r requirements-docs.txt
mkdocs serve        # http://127.0.0.1:8000
```
