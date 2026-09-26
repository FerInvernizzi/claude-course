# CLAUDE.md

Repositorio del **Curso de Claude en español** (publicado en https://ferinvernizzi.github.io/claude-nube/).

- Antes de trabajar, leé @HANDOFF.md: estado del proyecto, estructura, convenciones del contenido y pendientes.
- Idioma del contenido: español rioplatense con voseo. Sin mezclar "tú" ni "usted".
- Después de cualquier cambio en `curso/`: corré `python3 .claude/skills/revision-calidad-curso/scripts/chequeos.py curso` (0 errores) y `mkdocs build --strict` (sin advertencias). El workflow de Pages falla si hay advertencias.
- Módulo nuevo: agregarlo al `nav` de `mkdocs.yml` y a la tabla del temario de `curso/README.md`.
- Para revisar calidad educativa usá la skill `revision-calidad-curso`.
