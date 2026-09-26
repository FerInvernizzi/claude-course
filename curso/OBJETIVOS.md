# Medición de los objetivos de aprendizaje

<img src="assets/linea.svg" alt="" width="100%">

Medición con el instrumento de [Metodología de objetivos](METODOLOGIA-OBJETIVOS.md) (B conducta · O objeto · C condición · D criterio · E evidencia; 0 a 2 cada uno, total sobre 10). La puntúa el script reproducible `.claude/skills/revision-calidad-curso/scripts/medir_objetivos.py`. Es una heurística: una persona revisó además la redacción de cada objetivo. En la segunda pasada se ampliaron sus patrones de condición y criterio en español (por ejemplo "menor al 30%" o "que se entienda en 60 segundos"), y se volvieron a medir las tres versiones con el mismo script.

## Resumen

| Versión | Qué es | Objetivos | Promedio | % ≥ 8 |
|---|---|---|---|---|
| v1 | Las 12 promesas del curso original ("Master…", "Understand…") | 12 | 3,8 | 0% |
| v2 | Primera versión de objetivos por módulo (verbos observables, sin condición ni criterio) | 54 | 5,7 | 9% |
| **v3** | **Objetivos ABCD actuales, con nivel de Bloom y evidencia** | 68 | 9,7 | 100% |

**Qué cambió de v1 a v3:** se eliminaron los verbos no observables ("dominar", "entender", "aprovechar"). Cada objetivo pasó a tener una sola conducta, la condición en que se realiza y un criterio verificable (tests que pasan, cifras que coinciden, menos de N líneas, al menos N elementos), y apunta a la práctica o entrega del módulo que lo mide.

## Distribución por nivel de Bloom (v3)

| Nivel | Objetivos |
|---|---|
| Recordar | 0 |
| Comprender | 4 |
| Aplicar | 27 |
| Analizar | 4 |
| Evaluar | 10 |
| Crear | 23 |

El curso concentra los objetivos en **aplicar** y **crear**, como corresponde a un curso práctico de herramientas. Los niveles de comprensión, análisis y evaluación aparecen donde hace falta un modelo mental (MCP, agentes, contexto) o criterio propio (elegir herramientas, auditar resultados).

## v3 — objetivo por objetivo

| # | Total | B | O | C | D | E | Objetivo |
|---|---|---|---|---|---|---|---|
| 0.1 | 10 | 2 | 2 | 2 | 2 | 2 | Clasificar, a partir de una lista de 6 tareas reales de tu trabajo, cuáles convi |
| 0.2 | 9 | 2 | 1 | 2 | 2 | 2 | Reformular, a partir de un pedido vago de tu trabajo, un objetivo delegable (obj |
| 1.1 | 10 | 2 | 2 | 2 | 2 | 2 | Configurar Cowork con una carpeta de trabajo dedicada, instrucciones globales y  |
| 1.2 | 10 | 2 | 2 | 2 | 2 | 2 | Formular un pedido con objetivo, entradas, formato de salida, restricciones y pl |
| 1.3 | 10 | 2 | 2 | 2 | 2 | 2 | Generar, a partir de archivos crudos de tu área, un Excel con fórmulas (no valor |
| 1.4 | 9 | 2 | 1 | 2 | 2 | 2 | Adaptar, a partir de casos reales, el patrón de pedido a 2 áreas distintas (fina |
| 2.1 | 10 | 2 | 2 | 2 | 2 | 2 | Explicar, con un diagrama propio, cómo se comunican host, cliente y servidor MCP |
| 2.2 | 8 | 2 | 2 | 0 | 2 | 2 | Conectar dos conectores (por ejemplo Gmail y Slack) y ejecutar un flujo entre pl |
| 2.3 | 10 | 2 | 2 | 2 | 2 | 2 | Configurar un servidor MCP en Claude Code con `claude mcp add` o `.mcp.json` y v |
| 2.4 | 10 | 2 | 2 | 2 | 2 | 2 | Estimar el tamaño en tokens de un documento dado, con un error menor al 30%, y d |
| 3.1 | 10 | 2 | 2 | 2 | 2 | 2 | Explicar, usando un SKILL.md de ejemplo, cómo la carga progresiva decide qué par |
| 3.2 | 10 | 2 | 2 | 2 | 2 | 2 | Crear con `skill-creator` una skill propia con una `description` que diga qué ha |
| 3.3 | 10 | 2 | 2 | 2 | 2 | 2 | Diferenciar, dado un caso de uso, si corresponde una skill, un plugin, un slash  |
| 3.4 | 9 | 1 | 2 | 2 | 2 | 2 | Limpiar un dataset con el plugin de datos, dejando un log de limpieza con regla  |
| 3.5 | 10 | 2 | 2 | 2 | 2 | 2 | Producir, a partir de un dataset limpio, un análisis estadístico con supuestos v |
| 3.6 | 10 | 2 | 2 | 2 | 2 | 2 | Empaquetar un plugin propio con al menos una skill, un comando y un subagente, q |
| 4.1 | 10 | 2 | 2 | 2 | 2 | 2 | Investigar un mercado con el modo Research y entregar un informe en el que cada  |
| 4.2 | 10 | 2 | 2 | 2 | 2 | 2 | Verificar, dado un informe generado con Research, al menos 3 cifras abriendo las |
| 4.3 | 10 | 2 | 2 | 2 | 2 | 2 | Extraer los estados financieros de un PDF a Excel con fórmulas de ratios y el ch |
| 4.4 | 10 | 2 | 2 | 2 | 2 | 2 | Generar con la skill pptx un one pager de una empresa o sector que se entienda e |
| 5.1 | 10 | 2 | 2 | 2 | 2 | 2 | Escribir, a partir de un pedido de una línea, un prompt que incluya los 6 compon |
| 5.2 | 10 | 2 | 2 | 2 | 2 | 2 | Aplicar al menos 3 técnicas avanzadas (XML, few-shot, encadenamiento, autocrític |
| 5.3 | 9 | 2 | 1 | 2 | 2 | 2 | Diseñar el contexto de un agente para una tarea larga usando las 4 estrategias ( |
| 6.1 | 10 | 2 | 2 | 2 | 2 | 2 | Configurar el complemento de Claude en Excel en una versión compatible, con inst |
| 6.2 | 10 | 2 | 2 | 2 | 2 | 2 | Calcular, en una tabla de Excel dada, un resumen estadístico por grupo con fórmu |
| 6.3 | 10 | 2 | 2 | 2 | 2 | 2 | Imputar valores faltantes con la mediana por grupo, dejando columnas imputadas,  |
| 6.4 | 10 | 2 | 2 | 2 | 2 | 2 | Construir en Excel, a partir de un dataset limpio, un dashboard con 4 KPIs, 3 gr |
| 7.1 | 10 | 2 | 2 | 2 | 2 | 2 | Aplicar a un modelo financiero la convención de colores, la separación supuestos |
| 7.2 | 10 | 2 | 2 | 2 | 2 | 2 | Construir con Claude un DCF a partir de estados financieros, con WACC documentad |
| 7.3 | 9 | 2 | 1 | 2 | 2 | 2 | Evaluar una valuación dada identificando al menos 3 errores típicos (g ≥ WACC, v |
| 7.4 | 10 | 2 | 2 | 2 | 2 | 2 | Calcular el MOIC y la TIR de un LBO a partir de sus supuestos, de modo que el mo |
| 8.1 | 10 | 2 | 2 | 2 | 2 | 2 | Generar con Claude en PowerPoint un deck de 6-8 slides sobre la plantilla de tu  |
| 8.2 | 10 | 2 | 2 | 2 | 2 | 2 | Verificar que todos los números de un deck generado coinciden con el Excel de or |
| 8.3 | 10 | 2 | 2 | 2 | 2 | 2 | Automatizar un informe ejecutivo recurrente como skill o slash command, de modo  |
| 8.4 | 9 | 2 | 1 | 2 | 2 | 2 | Elegir entre Claude, Copilot y NotebookLM para 3 casos dados, justificando cada  |
| 9.1 | 10 | 2 | 2 | 2 | 2 | 2 | Instalar Claude Code en tu sistema operativo y verificar la instalación con `cla |
| 9.2 | 10 | 2 | 2 | 2 | 2 | 2 | Escribir un `CLAUDE.md` de menos de 60 líneas para un proyecto dado, con comando |
| 9.3 | 10 | 2 | 2 | 2 | 2 | 2 | Crear un slash command propio con frontmatter y argumentos, que aparezca en el m |
| 9.4 | 10 | 2 | 2 | 2 | 2 | 2 | Configurar, en un proyecto propio, un permiso `deny` en `.claude/settings.json`, |
| 9.5 | 9 | 2 | 2 | 2 | 1 | 2 | Diferenciar `/clear`, `/compact` y `/rewind` dado un escenario de sesión larga,  |
| 10.1 | 10 | 2 | 2 | 2 | 2 | 2 | Construir dos versiones de una landing page, con y sin la skill frontend-design, |
| 10.2 | 10 | 2 | 2 | 2 | 2 | 2 | Crear un slash command de marca que lea tu carpeta de marca y genere landings co |
| 10.3 | 8 | 2 | 2 | 2 | 0 | 2 | Empaquetar un plugin con un subagente investigador, probarlo con `claude --plugi |
| 10.4 | 10 | 2 | 2 | 2 | 2 | 2 | Desarrollar una app full-stack con una ruta de API que llame a un modelo de visi |
| 10.5 | 10 | 2 | 2 | 2 | 2 | 2 | Implementar mejoras con un Ralph Loop hasta que `npm test`, lint y typecheck pas |
| 11.1 | 9 | 2 | 1 | 2 | 2 | 2 | Explicar el bucle agéntico sobre la traza de una ejecución real, señalando en ca |
| 11.2 | 10 | 2 | 2 | 2 | 2 | 2 | Implementar con el OpenAI Agents SDK un agente con herramientas y memoria (`SQLi |
| 11.3 | 10 | 2 | 2 | 2 | 2 | 2 | Construir con el Claude Agent SDK un equipo de al menos 3 subagentes que produzc |
| 11.4 | 9 | 2 | 1 | 2 | 2 | 2 | Seleccionar el patrón de orquestación (secuencial, paralelo, orquestador, evalua |
| 11.5 | 9 | 2 | 1 | 2 | 2 | 2 | Agregar con el OpenAI Agents SDK un agente editor evaluador-optimizador que rees |
| 12.1 | 9 | 2 | 1 | 2 | 2 | 2 | Diseñar, usando la plantilla del curso, la arquitectura de tu agente personal co |
| 12.2 | 10 | 2 | 2 | 2 | 2 | 2 | Escribir, con la plantilla del curso, un SOUL.md y un CLAUDE.md propios, de modo |
| 12.3 | 10 | 2 | 2 | 2 | 2 | 2 | Aplicar el patrón Wiki de Karpathy sobre tus fuentes en `raw/`, de modo que se g |
| 12.4 | 10 | 2 | 2 | 2 | 2 | 2 | Conectar Gmail, Calendar y Notion y verificar cada conector con un pedido de sol |
| 13.1 | 9 | 2 | 1 | 2 | 2 | 2 | Construir al menos 5 automatizaciones como procedimiento escrito + comando + dis |
| 13.2 | 10 | 2 | 2 | 2 | 2 | 2 | Programar al menos 2 automatizaciones con `/schedule` y disparar 1 con Dispatch  |
| 13.3 | 9 | 2 | 1 | 2 | 2 | 2 | Evaluar cada automatización con los 6 criterios de calidad (definición escrita,  |
| 14.1 | 10 | 2 | 2 | 2 | 2 | 2 | Recuperar una sesión de Claude Code que se desvió, usando `/rewind` (resumir |
| 14.2 | 10 | 2 | 2 | 2 | 2 | 2 | Configurar la memoria de un proyecto con `CLAUDE.md` de menos de 200 líneas, |
| 14.3 | 10 | 2 | 2 | 2 | 2 | 2 | Automatizar una tarea hasta un criterio verificable con `/goal` y justific |
| 14.4 | 10 | 2 | 2 | 2 | 2 | 2 | Escribir una skill avanzada que use al menos tres campos de frontmatter (`di |
| 14.5 | 9 | 2 | 2 | 2 | 1 | 2 | Paralelizar trabajo con el mecanismo adecuado (subagente, `/subtask`, worktr |
| 14.6 | 10 | 2 | 2 | 2 | 2 | 2 | Configurar, para tu trabajo real, instrucciones persistentes en Cowork (glob |
| 14.7 | 10 | 2 | 2 | 2 | 2 | 2 | Elegir, dado un escenario de tarea, el modo de permiso de Cowork (Manual, Au |
| 15.1 | 10 | 2 | 2 | 2 | 2 | 2 | Seleccionar del catálogo al menos 3 skills o plugins adecuados a un interés  |
| 15.2 | 10 | 2 | 2 | 2 | 2 | 2 | Instalar skills de nicho desde el marketplace oficial de Anthropic y desde u |
| 15.3 | 10 | 2 | 2 | 2 | 2 | 2 | Producir una pieza creativa completa (obra generativa, póster, video, episod |
| 15.4 | 10 | 2 | 2 | 2 | 2 | 2 | Adaptar con `skill-creator` una skill existente a tu estilo personal (paleta |

## v1 — promesas originales

| Total | B | O | C | D | E | Objetivo |
|---|---|---|---|---|---|---|
| 2 | 0 | 2 | 0 | 0 | 0 | Master Claude Cowork Agents to automate tasks in finance, legal, marketing, data analysis, |
| 6 | 2 | 2 | 2 | 0 | 0 | Build, debug, and deploy full-stack applications and websites using the Claude Code termin |
| 2 | 0 | 2 | 0 | 0 | 0 | Understand the concept of "Agent Skills" and "Plugins" to give Claude agents new capabilit |
| 2 | 0 | 2 | 0 | 0 | 0 | Leverage specialized plugins to clean data, perform statistical analysis, and automaticall |
| 6 | 2 | 2 | 2 | 0 | 0 | Connect Claude to external tools like Gmail, Slack, and Salesforce using the Model Context |
| 2 | 0 | 2 | 0 | 0 | 0 | Master Claude in Excel to clean data, perform conditional formatting, handle missing value |
| 6 | 2 | 2 | 2 | 0 | 0 | Automate the creation of branded PowerPoint presentations and professional executive repor |
| 2 | 0 | 2 | 0 | 0 | 0 | Master prompt engineering & context Engineering techniques to optimize Claude's output for |
| 6 | 2 | 2 | 2 | 0 | 0 | Construct professional, Wallstreet-level financial models using the combined power of Clau |
| 6 | 2 | 2 | 2 | 0 | 0 | Design and manage a team of autonomous AI agents to handle end-to-end projects, from initi |
| 1 | 0 | 1 | 0 | 0 | 0 | Understand the concept of "Subagents" and "Agent Teams" to handle multi-step, advanced com |
| 4 | 0 | 2 | 2 | 0 | 0 | Master Claude Code to autonomously scaffold, design, and deploy full-stack websites throug |

## v2 — primera versión por módulo

| Total | B | O | C | D | E | Objetivo |
|---|---|---|---|---|---|---|
| 4 | 2 | 1 | 0 | 0 | 1 | Explicar la diferencia entre un chatbot y un agente. |
| 5 | 2 | 2 | 0 | 0 | 1 | Ubicar Chat, Cowork, Code y los add-ins de Office en el ecosistema de Claude. |
| 4 | 2 | 1 | 0 | 0 | 1 | Aplicar los 8 consejos de éxito al formular un pedido. |
| 7 | 2 | 2 | 2 | 0 | 1 | Configurar Cowork con una carpeta de trabajo segura. |
| 6 | 2 | 1 | 2 | 0 | 1 | Formular pedidos con objetivo, entradas, formato, restricciones y plan previo. |
| 7 | 2 | 2 | 2 | 0 | 1 | Generar un Excel con fórmulas y formato a partir de archivos crudos. |
| 4 | 2 | 1 | 0 | 0 | 1 | Adaptar el patrón de pedido a finanzas, legal, marketing e investigación. |
| 5 | 2 | 2 | 0 | 0 | 1 | Explicar la arquitectura de MCP (host, cliente, servidor; tools, resources, prompts). |
| 6 | 1 | 2 | 2 | 0 | 1 | Conectar un conector (Gmail) y ejecutar un flujo con aprobación humana. |
| 7 | 2 | 2 | 2 | 0 | 1 | Agregar servidores MCP en Claude Code con `claude mcp add` o `.mcp.json`. |
| 4 | 1 | 2 | 0 | 0 | 1 | Estimar tokens y aplicar reglas para cuidar la ventana de contexto. |
| 5 | 2 | 2 | 0 | 0 | 1 | Explicar qué es una skill, su estructura y la carga progresiva. |
| 7 | 2 | 2 | 2 | 0 | 1 | Crear una skill propia con `skill-creator`. |
| 4 | 1 | 2 | 0 | 0 | 1 | Diferenciar skills de plugins e instalar un plugin. |
| 6 | 1 | 2 | 2 | 0 | 1 | Limpiar datos, hacer análisis estadístico, dashboards y slides con el plugin de datos. |
| 5 | 2 | 2 | 0 | 0 | 1 | Diseñar y empaquetar un plugin de finanzas propio. |
| 9 | 2 | 2 | 2 | 2 | 1 | Investigar con búsqueda web y con el modo Research, con fuentes verificables. |
| 4 | 2 | 1 | 0 | 0 | 1 | Usar Claude para escritura creativa, brainstorming, aprendizaje y código. |
| 5 | 2 | 2 | 0 | 0 | 1 | Extraer estados financieros de un PDF a Excel y a PowerPoint. |
| 4 | 2 | 1 | 0 | 0 | 1 | Elegir entre Claude y un generador de imágenes según la tarea. |
| 7 | 2 | 2 | 2 | 0 | 1 | Escribir prompts con los 6 componentes (rol, tarea, contexto, formato, restricciones, ejem |
| 4 | 2 | 1 | 0 | 0 | 1 | Aplicar técnicas avanzadas: XML, few-shot, encadenamiento, autocrítica y preguntas previas |
| 6 | 2 | 1 | 2 | 0 | 1 | Diseñar el contexto de un agente con las 4 estrategias (escribir, seleccionar, comprimir,  |
| 6 | 1 | 2 | 2 | 0 | 1 | Instalar y usar Claude en Excel sobre datos reales. |
| 5 | 1 | 1 | 2 | 0 | 1 | Obtener estadísticas y filtrar, ordenar y visualizar con fórmulas dinámicas. |
| 6 | 2 | 1 | 0 | 2 | 1 | Aplicar formato condicional e imputar valores faltantes de forma trazable. |
| 7 | 2 | 2 | 2 | 0 | 1 | Construir un dashboard con KPIs y segmentadores. |
| 5 | 2 | 1 | 0 | 1 | 1 | Aplicar los estándares de un modelo financiero profesional (colores, chequeos, escenarios) |
| 7 | 2 | 2 | 2 | 0 | 1 | Construir un modelo de 3 estados, un DCF y un LBO con Claude. |
| 4 | 2 | 1 | 0 | 0 | 1 | Interpretar sensibilidades y detectar errores típicos de valuación. |
| 6 | 2 | 1 | 2 | 0 | 1 | Crear presentaciones con títulos-acción y notas del orador. |
| 4 | 0 | 1 | 2 | 0 | 1 | Mejorar el diseño y generar slides desde PDFs, la web y plantillas de marca. |
| 4 | 2 | 1 | 0 | 0 | 1 | Automatizar un informe ejecutivo recurrente. |
| 4 | 2 | 1 | 0 | 0 | 1 | Elegir entre Claude, Copilot y NotebookLM según el caso. |
| 7 | 2 | 2 | 2 | 0 | 1 | Instalar Claude Code en Mac, Windows o Linux y usarlo desde la terminal, VS Code o la app  |
| 7 | 1 | 1 | 2 | 2 | 1 | Trabajar con modos de permiso, Plan mode y el flujo explorar → planificar → codear → verif |
| 6 | 2 | 2 | 0 | 1 | 1 | Crear slash commands propios y un CLAUDE.md efectivo. |
| 4 | 1 | 2 | 0 | 0 | 1 | Gestionar la ventana de contexto y configurar plugins y hooks. |
| 9 | 2 | 2 | 2 | 2 | 1 | Construir y comparar landing pages con y sin la skill frontend-design. |
| 7 | 2 | 2 | 2 | 0 | 1 | Crear un slash command de marca y un plugin con subagente. |
| 7 | 2 | 2 | 2 | 0 | 1 | Desarrollar una app full-stack con IA (rutas de API, validación, tests). |
| 8 | 1 | 2 | 2 | 2 | 1 | Iterar con Ralph Loops usando criterios de fin verificables y desplegar en producción. |
| 4 | 2 | 1 | 0 | 0 | 1 | Explicar el bucle agéntico y los componentes de un agente. |
| 6 | 2 | 1 | 2 | 0 | 1 | Construir agentes con herramientas, memoria y salida estructurada (OpenAI Agents SDK y Cla |
| 8 | 2 | 2 | 2 | 1 | 1 | Diseñar subagentes y equipos de agentes con el patrón de orquestación adecuado. |
| 5 | 1 | 1 | 2 | 0 | 1 | Llevar un equipo de agentes de la investigación al email con aprobación humana. |
| 4 | 2 | 1 | 0 | 0 | 1 | Diseñar la arquitectura de un agente personal (identidad, memoria, capacidades, disparador |
| 5 | 2 | 2 | 0 | 0 | 1 | Aplicar el patrón Wiki de Karpathy y visualizarlo en Obsidian. |
| 7 | 2 | 2 | 2 | 0 | 1 | Escribir un SOUL.md y un CLAUDE.md para tu agente. |
| 5 | 2 | 2 | 0 | 0 | 1 | Conectar Gmail, Calendar y Notion y configurar tu marca. |
| 4 | 2 | 1 | 0 | 0 | 1 | Construir automatizaciones como procedimiento escrito + comando + disparador. |
| 8 | 2 | 1 | 2 | 2 | 1 | Implementar al menos 5 de los 10 blueprints con conectores reales. |
| 6 | 2 | 1 | 2 | 0 | 1 | Programar tareas y dispararlas desde el celular con Dispatch. |
| 7 | 2 | 1 | 2 | 1 | 1 | Evaluar una automatización con 6 criterios de calidad. |
