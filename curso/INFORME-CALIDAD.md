# Informe de calidad — Curso de Claude

<img src="assets/linea.svg" alt="" width="100%">

Fecha: 2026-09-26 · Revisión con la skill `revision-calidad-curso` (incluida en `.claude/skills/`) · Rúbrica: 8 dimensiones × 4 niveles (Quality Matters, Bloom revisada, alineación constructiva, Merrill, carga cognitiva)

## Resumen

- **Puntaje global:** 2,7 → **3,8** (sobre 4)
- **Veredicto:** listo para publicar (promedio ≥ 3,5, ninguna dimensión en 1, exactitud técnica ≥ 3)
- **Objetivos de aprendizaje:** 67 objetivos ABCD, **9,4/10** de promedio, 100% ≥ 8 (antes: 3,8/10). Ver [OBJETIVOS.md](OBJETIVOS.md)
- **Correcciones aplicadas:** 14 bloqueantes, 11 importantes y más de 115 de pulido

## Puntajes por módulo

Dimensiones: **Obj** objetivos · **Alin** alineación · **Exact** exactitud técnica · **Progr** progresión · **Práct** práctica · **Clar** claridad · **Aplic** aplicabilidad · **Leng** lenguaje y formato. "Antes" es la primera versión completa del curso; "Después", la actual.

| Módulo | Obj | Alin | Exact | Progr | Práct | Clar | Aplic | Leng | Prom. antes | Prom. después |
|--------|-----|------|-------|-------|-------|------|-------|------|-------------|---------------|
| 00 Introducción | 4 | 3 | 4 | 4 | 3 | 4 | 3 | 4 | 2,6 | 3,6 |
| 01 Cowork | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 2,5 | 3,9 |
| 02 MCP y tokens | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,9 | 4,0 |
| 03 Skills y plugins | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3,0 | 3,9 |
| 04 Claude Chat | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 2,5 | 3,8 |
| 05 Prompt y contexto | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3,1 | 4,0 |
| 06 Excel | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | 2,6 | 3,8 |
| 07 Modelos financieros | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 2,5 | 3,5 |
| 08 PowerPoint | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 2,5 | 3,9 |
| 09 Claude Code | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,6 | 4,0 |
| 10 Proyectos | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 3,0 | 3,8 |
| 11 Agentes | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 2,9 | 3,8 |
| 12 Agente personal | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 2,8 | 3,9 |
| 13 Automatizaciones | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 4 | 2,5 | 3,5 |
| 14 Funciones avanzadas | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | — (nuevo) | 3,8 |
| 15 Skills de nicho | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — (nuevo) | 4,0 |
| **Curso** | | | | | | | | | **2,7** | **3,8** |

Por qué no todo está en 4:
- **Exactitud 3** (01, 04, 06, 07, 08, 12, 13): describen interfaces de Cowork, Claude en Excel/PowerPoint y conectores que se verificaron contra la documentación oficial, pero no se pudieron ejecutar en este entorno (no hay Office ni cuentas conectadas). Las interfaces cambian rápido, y el curso lo advierte.
- **Práctica 3** (00, 07, 13): el 00 no tiene práctica propia (solo autoevaluación, que es adecuado para una introducción); en el 07 y el 13 la práctica es grande y conviene dividirla en entregas parciales.
- **Claridad 3** (03, 06, 07, 10, 11, 14): módulos largos y densos; conviene recorrerlos en dos o más sesiones.

## Matriz de alineación (objetivos del curso)

| Objetivo del curso | Contenido | Demostración | Práctica | Criterio / solución | Estado |
|---|---|---|---|---|---|
| 1 Automatizar con Cowork | 01, 03 | ✅ | ✅ | ✅ | OK |
| 2 App full‑stack con Claude Code | 09, 10 | ✅ | ✅ | ✅ | OK |
| 3 Crear skill y plugin | 03, 09, 10 | ✅ | ✅ | ✅ | OK |
| 4 Datos → análisis → informe | 03 | ✅ | ✅ | ✅ | OK |
| 5 MCP entre plataformas | 02, 11 | ✅ | ✅ | ✅ | OK |
| 6 Claude en Excel | 06 | ✅ | ✅ | ✅ | OK |
| 7 PowerPoint e informes de marca | 04, 08 | ✅ | ✅ | ✅ | OK |
| 8 Prompt y context engineering | 05, 14 | ✅ | ✅ | ✅ | OK |
| 9 Modelos financieros | 07 | ✅ | ✅ | ✅ | OK |
| 10 Equipo de agentes | 11, 13 | ✅ | ✅ | ✅ | OK |
| 11 Subagentes y agent teams | 11, 14 | ✅ | ✅ (autoevaluación) | ✅ | OK |
| 12 Agente personal + automatizaciones | 12, 13 | ✅ | ✅ | ✅ | OK |
| 13 Funciones avanzadas | 14 | ✅ | ✅ | ✅ | OK |
| 14 Skills de nicho | 15 | ✅ | ✅ | ✅ | OK |

## Correcciones aplicadas

### 🔴 Bloqueantes (errores técnicos o pasos que no funcionaban)
- 09 § Slash commands: los argumentos posicionales son **base 0** (`$0` es el primero); el curso indicaba `$1` como primero.
- 09 § Hooks: el hook de Prettier formateaba todo el proyecto en cada edición; ahora formatea solo el archivo editado (lee `tool_input.file_path` con `jq`).
- 10 § Calorie Tracker: el fragmento TypeScript de la API de Claude no compilaba en modo estricto; corregido con un *type guard* y verificado con `tsc --strict`.
- 07 § Sensibilidades: se pedía la función *Tabla de datos* de Excel, que el complemento de Claude no soporta; ahora se usan grillas con fórmulas.
- 06: se aclara que el complemento no soporta tablas de datos ni macros/VBA, y se detallan las versiones compatibles.
- 01: Cowork se describía como una VM local; hoy ejecuta en la nube y la tarea sigue aunque cierres la laptop.
- 13 § Dispatch: faltaban requisitos (plan Pro/Max, computadora despierta) y había que distinguirlo de las tareas programadas, que corren en la nube.
- 02: se exageraba el costo de contexto de los conectores MCP (hoy cargan solo los nombres de sus herramientas hasta usarlas).
- 09, 11 y 12: `/agents` ya no abre un asistente de creación de subagentes.
- 09: Git for Windows se recomienda pero no es obligatorio; se agregaron `winget` y `brew`.
- 09: el atajo de VS Code indicado no estaba documentado; se reemplazó por el procedimiento oficial.
- 09: `/cost` es alias de `/usage`.
- 13: el curso "terminaba" en el 13; ahora enlaza a los módulos 14 y 15.
- 06/08: se eliminaron secciones de objetivos duplicadas.

### 🟡 Importantes
- Los 16 módulos tienen objetivos ABCD con nivel de Bloom y evidencia (antes: ninguno medible).
- Se agregaron prácticas con solución y criterios de éxito en 01, 02 (MCP), 04, 08 y 09, que no tenían.
- Autoevaluación con respuestas plegables en los 16 módulos (práctica de recuperación).
- Se cerraron huecos de alineación: pasos nuevos en las prácticas de 02 (servidor MCP en Claude Code) y 06 (instrucciones persistentes).
- Módulo 14 nuevo: funciones avanzadas verificadas en la documentación oficial.
- Módulo 15 nuevo: 30 skills y plugins de nicho verificados (los repositorios existen).
- Cowork: modos Manual/Auto/Skip, instrucciones globales y de carpeta, proyectos y consumo.
- Excel: citas por celda, instrucciones persistentes, contexto entre apps de Office y riesgo de inyección de prompts.
- `/schedule`: el truco de hacer la tarea una vez antes de programarla.
- Nota sobre los nombres de funciones de Excel según el idioma.
- Costo real medido del ejemplo del equipo de subagentes (≈ USD 1,13).

### 🟢 Pulido
- 113 bloques de código etiquetados (`text`) para un renderizado uniforme.
- Español rioplatense consistente (voseo) en todo el curso.
- Estética mínima: encabezado, línea de acento y logo al pie con la paleta de Agency.

## Verificaciones realizadas

- **Enlaces internos y anclas:** 0 rotos (`scripts/chequeos.py`, 41 archivos).
- **Código Python** (6 scripts): compilan e importan con `openai-agents` y `claude-agent-sdk` actuales.
- **Claude Agent SDK, ejecución real:** `01_agente_claude.py` respondió correctamente (1.250 × 0,92 = 1.150). `02_equipo_subagentes.py` generó un informe con fuentes y límites de datos declarados, más un borrador de email (6 turnos, ≈ USD 1,13).
- **TypeScript:** las dos rutas del Calorie Tracker (Gemini y Claude) pasan `tsc --strict` con los SDK actuales.
- **Plugin de ejemplo:** `claude plugin validate ./plantillas/plugin-finanzas` → aprobado.
- **CLI:** se comprobó que existen `--plugin-dir`, `--worktree`, `--continue`, `--name`, `--cloud`, `--teleport`, `claude doctor`, `claude update`, `claude mcp` y los comandos `/skills`, `/context`, `/usage`, `/rewind`, `/memory`, `/hooks`, `/schedule`.
- **Plugins del curso:** 22 instalados y declarados en `.claude/settings.json`.
- **Repositorios de skills de nicho:** 18 de terceros verificados con `git ls-remote`, más el repositorio oficial `anthropics/skills`.
- **Documentación:** más de 50 páginas oficiales de Claude Code y los artículos de ayuda de Cowork, Dispatch, Excel y PowerPoint (septiembre de 2026).

## Limitaciones

- No se pudieron ejecutar en este entorno Cowork, los complementos de Excel y PowerPoint, los conectores de Gmail, Slack y Notion, ni Dispatch. Se verificaron contra la documentación oficial, no en uso real.
- Los ejemplos del OpenAI Agents SDK se verificaron por compilación e importación, no ejecutándolos (no hay clave de OpenAI en el entorno).
- La app Calorie Tracker no se construyó de punta a punta; se verificaron sus fragmentos clave.
- La medición de objetivos usa una heurística reproducible; la redacción final la revisó una persona, pero conviene validarla con alumnos reales (por ejemplo, con tasas de éxito en cada práctica).
- Varias funciones de Claude Code están en vista previa o son experimentales (rutinas, agent teams, canales, advisor) y pueden cambiar; el curso las marca como tales.
