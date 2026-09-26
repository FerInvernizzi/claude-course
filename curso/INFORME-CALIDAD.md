# Informe de calidad — Curso de Claude

<img src="assets/linea.svg" alt="" width="100%">

Fecha: 2026-09-26 · Revisión con la skill `revision-calidad-curso` (incluida en `.claude/skills/`) · Rúbrica: 8 dimensiones × 4 niveles (Quality Matters, Bloom revisada, alineación constructiva, Merrill, carga cognitiva)

## Resumen

- **Puntaje global:** 2,7 (primera versión) → 3,8 (primera revisión) → **4,0** (segunda pasada)
- **Veredicto:** listo para publicar. Las 8 dimensiones están en 4 en los 16 módulos.
- **Objetivos de aprendizaje:** 68 objetivos ABCD, **9,7/10** de promedio, 100% ≥ 8 (versión original: 3,8/10). Ver [OBJETIVOS.md](OBJETIVOS.md)
- **Correcciones:** primera revisión: 14 bloqueantes, 11 importantes y más de 115 de pulido. Segunda pasada: 9 bloqueantes, 16 importantes y 8 de pulido (detalle abajo)

## Puntajes por módulo

Dimensiones: **Obj** objetivos · **Alin** alineación · **Exact** exactitud técnica · **Progr** progresión · **Práct** práctica · **Clar** claridad · **Aplic** aplicabilidad · **Leng** lenguaje y formato. Las columnas finales muestran el promedio en la primera versión completa, después de la primera revisión y después de esta segunda pasada.

| Módulo | Obj | Alin | Exact | Progr | Práct | Clar | Aplic | Leng | 1ª versión | 1ª revisión | **2ª pasada** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 00 Introducción | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,6 | 3,6 | **4,0** |
| 01 Cowork | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,5 | 3,9 | **4,0** |
| 02 MCP y tokens | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,9 | 4,0 | **4,0** |
| 03 Skills y plugins | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3,0 | 3,9 | **4,0** |
| 04 Claude Chat | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,5 | 3,8 | **4,0** |
| 05 Prompt y contexto | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3,1 | 4,0 | **4,0** |
| 06 Excel | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,6 | 3,8 | **4,0** |
| 07 Modelos financieros | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,5 | 3,5 | **4,0** |
| 08 PowerPoint | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,5 | 3,9 | **4,0** |
| 09 Claude Code | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,6 | 4,0 | **4,0** |
| 10 Proyectos | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3,0 | 3,8 | **4,0** |
| 11 Agentes | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,9 | 3,8 | **4,0** |
| 12 Agente personal | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,8 | 3,9 | **4,0** |
| 13 Automatizaciones | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2,5 | 3,5 | **4,0** |
| 14 Funciones avanzadas | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 3,8 | **4,0** |
| 15 Skills de nicho | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 4,0 | **4,0** |
| **Curso** | | | | | | | | | **2,7** | **3,8** | **4,0** |

### Qué se hizo en la segunda pasada para llegar a 4

| Dimensión en 3 | Módulos | Evidencia del problema | Corrección |
|---|---|---|---|
| Exactitud | 01, 04, 06, 07, 08, 12, 13 | Rutas de menú desactualizadas ("Configuración → Conectores"), Cowork descripto solo como VM local, Dispatch sin su modelo de tareas hijas, afirmaciones de terceros sin fuente | Todo se verificó contra la documentación oficial de Cowork, skills, conectores, plugins y Office (claude.com/docs) y contra el centro de ayuda. Se corrigieron las rutas (*Customize → Connectors/Skills/Plugins*). Cada módulo cita sus fuentes oficiales y marca lo que cambia rápido |
| Práctica | 00, 07, 13 | 00 sin práctica; 07 y 13 con una sola práctica grande | 00: práctica de mapa de delegación con solución y criterios. 07: práctica en 5 entregas con criterio numérico. 13: 4 entregas y las 6 pruebas de calidad con un ejemplo resuelto |
| Claridad | 03, 06, 07, 10, 11, 13, 14 | Módulos de 2.000 a 3.000 palabras sin guía de lectura | Ruta de estudio por sesiones (tiempo y resultado) y cierre "📌 Ideas clave" en todos los módulos |
| Progresión | 04, 07, 10, 11, 14 | Términos financieros sin andamiaje; Node y Python dados por sabidos; el 14 depende de varios módulos | Glosario y ejemplos resueltos (DCF y LBO) en el 07; puente del 04 al glosario; mínimos de Node (10) y Python (11); mapa de "se apoya en" en el 14 |
| Alineación | 00, 13 (y objetivo 4.3) | Objetivos medidos solo por autoevaluación o por una práctica genérica | Cada objetivo apunta a una parte o entrega concreta de la práctica; nuevo objetivo 7.4 (LBO) con su entrega |
| Aplicabilidad | 00 | Sin tareas del propio alumno | Práctica sobre 6 tareas reales de la semana del alumno y guía "¿Qué herramienta uso?" |

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

## Correcciones de la primera revisión

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

## Correcciones de la segunda pasada

### 🔴 Bloqueantes (segunda pasada)
- 11 § MCP 101: con el SDK `mcp` 2.x, `from mcp.server.fastmcp import FastMCP` da error de importación (la clase ahora es `MCPServer`). Se actualizó el código, se agregó `codigo/mcp/servidor_inventario.py` y se probó con un cliente MCP real (lista la herramienta `stock` y devuelve 120).
- 10 § Despliegue: en un proyecto nuevo, el primer deploy de Vercel ya va a producción (no a una vista previa). Además la API key se cargaba después de ese deploy. Ahora el orden es `vercel link` → `vercel env add` → `vercel --prod`.
- 02 y 12: rutas de menú de conectores → *Customize → Connectors → Discover → Connect to Claude*; activación por conversación con **+** y permisos por herramienta.
- 03, 15, SKILLS-Y-PLUGINS y la plantilla del plugin: rutas de skills y plugins → *Customize → Skills/Plugins*, requisito de *Code execution and file creation* y **Add marketplace** con `usuario/repo`. Además, Cowork no lee `~/.claude`.
- 01: descripción de Cowork alineada con las dos fuentes oficiales (escritorio con carpetas locales + ejecución aislada; disponible en web y móvil); proyectos de Cowork locales y distintos de los de claude.ai.
- 13 y 14: Dispatch descripto según la guía oficial (tareas hijas hacia Code o proyectos de Cowork; los permisos se deniegan a los 10 minutos). También se aclara que el morning brief lee el vault local.
- 02: se reemplazó el servidor MCP de Postgres, archivado, por `server-filesystem`, con `--transport stdio` explícito como en la documentación.
- 07: la fórmula de *Usos* del LBO contaba dos veces la refinanciación de la deuda existente.
- 07 y la skill `modelo-dcf`: umbral inconsistente del valor terminal (80% contra 85%); ahora es 85% en todos lados.

### 🟡 Importantes (segunda pasada)
- 04: generación de imágenes verificada (Claude no genera imágenes de forma nativa; puede usar generadores vía MCP; Gemini Image/"Nano Banana"). Research descripto según su artículo oficial.
- 04: el objetivo 4.3 (PDF a Excel) ahora se mide en el paso 5 de la práctica.
- 08: comparación con NotebookLM actualizada (resúmenes en audio y video, mapas mentales, cuestionarios) con fecha y fuentes.
- 12: OpenClaw, Hermes Agent y el patrón de Karpathy descriptos con fechas y fuentes.
- 10: aviso de que `generateContent` de Gemini es *legacy* y referencia a la Interactions API.
- 10: criterios de éxito explícitos del Proyecto 4, uno por objetivo.
- 07: glosario, ejemplos resueltos de DCF y LBO verificados numéricamente, práctica en 5 entregas y objetivo 7.4.
- 13: práctica en 4 entregas, las 6 pruebas de calidad, ejemplo resuelto del README y alternativa para planes sin Dispatch.
- 00: guía "¿Qué herramienta uso?", práctica con solución y esquema del curso con los módulos 14 y 15.
- Rutas de estudio en 03, 06, 07, 10, 11, 13 y 14.
- Mínimos de Node.js (10) y de Python (11).
- "📌 Ideas clave" en los 15 módulos que no tenían cierre.
- Fuentes oficiales en todos los módulos.
- Objetivos 3.1, 5.1, 6.4 y 15.4 con criterio explícito.
- Puentes entre módulos: 00 → 01 (pedido guardado) y 04 → 07 (glosario).
- Heurística de medición de objetivos ampliada para criterios en español, con v1, v2 y v3 vueltas a medir.

### 🟢 Pulido (segunda pasada)
- Títulos "Fase 1" duplicados en el 10; diagrama del ecosistema con Cowork en escritorio, web y móvil; requisitos del 07; nota de versiones del SDK `mcp`; `--transport stdio` en el 11; comentario del modelo de Gemini; aviso de fecha en las comparaciones; requisitos del 13.

## Verificaciones realizadas

- **Enlaces internos y anclas:** 0 rotos (`scripts/chequeos.py`, 41 archivos).
- **Código Python** (7 scripts): compilan e importan con `openai-agents` 0.22, `claude-agent-sdk` y `mcp` 2.2.
- **Servidor MCP del módulo 11:** probado con un cliente MCP real (`list_tools` → `stock`; `call_tool` → 120).
- **Ejemplos numéricos del 07:** DCF (EV 1.598,6; VT 83%; 12,99 por acción) y LBO (MOIC 2,71x; TIR 22,1%; atribución 110,5 + 125 − 8) calculados con un script.
- **Documentación de apps de Claude:** 16 páginas de claude.com/docs (Cowork, Dispatch, proyectos, plugins, skills, conectores, Office) más la documentación de Claude Code. Ejemplos de `claude mcp add` y `.mcp.json` contrastados con la página oficial de MCP.
- **URLs de fuentes:** 26 verificadas (HTTP 200 o, si el proxy bloqueaba el dominio, confirmadas por búsqueda o con `git ls-remote`).
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
- Puntaje 4 en exactitud significa lo que pide la rúbrica: lo verificable se verificó, y lo que depende de interfaces que cambian se contrastó con la documentación oficial vigente, se marca como tal y enlaza a su fuente. No significa que esas interfaces se hayan probado en uso real.
- La medición de objetivos usa una heurística reproducible; la redacción final la revisó una persona, pero conviene validarla con alumnos reales (por ejemplo, con tasas de éxito en cada práctica).
- Varias funciones de Claude Code están en vista previa o son experimentales (rutinas, agent teams, canales, advisor) y pueden cambiar; el curso las marca como tales.
