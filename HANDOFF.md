# Handoff — Curso de Claude (estado al 2026-09-26)

Resumen para retomar el proyecto en una sesión nueva sin perder contexto.

## Qué es

Curso práctico de Claude **en español rioplatense (voseo)**, publicado en GitHub Pages:

- **Sitio en vivo:** https://ferinvernizzi.github.io/claude-nube/
- **Repo público:** https://github.com/FerInvernizzi/claude-nube (rama por defecto `main`)
- **Contenido:** `curso/` (16 módulos en `curso/modulos/`, recursos en la raíz de `curso/`)

## Estructura

| Ruta | Qué hay |
|---|---|
| `curso/README.md` | Índice del curso = portada del sitio |
| `curso/modulos/00…15-*.md` | Los 16 módulos |
| `curso/SKILLS-Y-PLUGINS.md` | Skills y plugins que usa el curso y cómo instalarlos |
| `curso/METODOLOGIA-OBJETIVOS.md` · `curso/OBJETIVOS.md` | Cómo se escribieron y midieron los objetivos (ABCD, Bloom, Quality Matters) |
| `curso/INFORME-CALIDAD.md` | Revisión con rúbrica: todas las dimensiones en 4 |
| `curso/plantillas/` · `curso/codigo/` | Plantillas (skills, comandos, subagentes, plugin, agente personal) y scripts Python del módulo 11 |
| `curso/assets/` · `curso/stylesheets/agency.css` | Encabezado, línea de acento, logo y estilos del sitio |
| `mkdocs.yml` · `hooks/enlaces_github.py` · `requirements-docs.txt` | Configuración del sitio (MkDocs Material) |
| `.github/workflows/pages.yml` | Publica el sitio en cada push a `main` que toque `curso/**` o la config |
| `.claude/settings.json` | 22 plugins oficiales que usa el curso |
| `.claude/skills/revision-calidad-curso/` | Skill de revisión de calidad educativa (rúbrica, `scripts/chequeos.py`, `scripts/medir_objetivos.py`) |

## Convenciones del contenido

- Cada módulo: título H1 → línea de acento (`<img src="../assets/linea.svg">`) → **🎯 Objetivos de aprendizaje** (tabla: # · objetivo ABCD · nivel Bloom · evidencia) → requisitos y duración → ruta de estudio (módulos largos) → secciones numeradas → **🧪 Práctica** con **✅ Solución** y criterios → **📌 Ideas clave** → **🧠 Autoevaluación** (respuestas en `<details>`) → **Fuentes oficiales** → "➡️ Siguiente".
- Objetivos: una conducta observable + condición + criterio verificable + práctica que lo mide. Nada de "entender", "conocer" ni "dominar".
- Bloques de prompt con ```` ```text ````; comandos con ```` ```bash ````.
- Lo que cambia rápido (interfaces de Cowork, Office, planes) se marca como tal y enlaza a la documentación oficial.
- Estética: paleta de Agency (negro #000, lima #BFEB30, oliva #879E3E, oliva oscuro #4E6B00 para links en modo claro). Logo solo al pie del índice; tono de guía, no de producto.

## Cómo trabajar

```bash
# Chequeos de calidad (enlaces, anclas, prácticas, etc.)
python3 .claude/skills/revision-calidad-curso/scripts/chequeos.py curso
# Medición de objetivos (hoy: 68 objetivos, 9,7/10)
python3 .claude/skills/revision-calidad-curso/scripts/medir_objetivos.py curso/modulos
# Sitio local
pip install -r requirements-docs.txt && mkdocs serve
mkdocs build --strict   # tiene que pasar sin advertencias (lo exige el workflow)
```

- Módulo nuevo: crear `curso/modulos/NN-nombre.md` con la estructura de arriba **y agregarlo al `nav` de `mkdocs.yml`** y a la tabla del temario en `curso/README.md`.
- Los enlaces a `plantillas/`, `codigo/` y `.claude/` se reescriben a GitHub con el hook; apuntan a la rama `main`.
- `mkdocs` está fijado en `<2` (MkDocs 2.0 rompe compatibilidad con Material).

## Verificado

- `mkdocs build --strict` sin advertencias; sitio publicado por el workflow (run exitoso).
- Scripts del Claude Agent SDK ejecutados de punta a punta; servidor MCP (`mcp` 2.x, `MCPServer`) probado con un cliente real; fragmentos TypeScript del módulo 10 con `tsc --strict`; plugin de ejemplo con `claude plugin validate`.
- Hechos de producto contrastados con code.claude.com/docs, claude.com/docs y support.claude.com (septiembre de 2026).

## No verificado en uso real

Cowork, complementos de Excel/PowerPoint, conectores (Gmail, Slack, Notion) y Dispatch (solo contra documentación). Ejemplos del OpenAI Agents SDK: solo compilados (sin API key). La app Calorie Tracker del módulo 10 no se construyó entera.

## Pendientes / ideas

- Difusión: post corto para r/ClaudeAI o LinkedIn enlazando al sitio.
- Validar el curso con alumnos reales (tasa de éxito por práctica) y ajustar objetivos.
- Revisar cada tanto la documentación oficial: Cowork, Office y Claude Code cambian seguido (sobre todo funciones en vista previa: rutinas, agent teams, canales, advisor).
- Opcional: quitar `.claude/settings.json` si no se quiere que el repo público sugiera plugins al abrirlo con Claude Code.
