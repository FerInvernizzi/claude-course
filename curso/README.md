# Masterclass de Claude: Cowork, Code, Skills, Plugins, MCP y Agentes

Curso práctico y en español para dominar el ecosistema de Claude de punta a punta: desde automatizar tareas de oficina con **Claude Cowork**, **Claude en Excel** y **Claude en PowerPoint**, hasta construir y desplegar aplicaciones full‑stack con **Claude Code**, diseñar **equipos de agentes autónomos** y montar tu propio **agente personal** con 10 automatizaciones reales.

---

## Qué vas a lograr

Al terminar el curso vas a poder:

| # | Objetivo | Módulos |
|---|----------|---------|
| 1 | Dominar los agentes de **Claude Cowork** para automatizar tareas de finanzas, legal, marketing, análisis de datos e investigación | 01, 02, 03 |
| 2 | Construir, depurar y desplegar apps y webs full‑stack con **Claude Code** y sus capacidades agénticas | 09, 10 |
| 3 | Entender qué son las **Agent Skills** y los **Plugins** y cómo dan nuevas capacidades a Claude | 03, 09, 10 |
| 4 | Usar plugins especializados para **limpiar datos, hacer estadística, dashboards e informes** | 03 |
| 5 | Conectar Claude con **Gmail, Slack, Salesforce**, etc. mediante **MCP** | 02, 11 |
| 6 | Dominar **Claude en Excel**: limpieza, formato condicional, valores faltantes, gráficos y dashboards | 06 |
| 7 | Automatizar **presentaciones PowerPoint con tu marca** e informes ejecutivos | 08 |
| 8 | Dominar **prompt engineering y context engineering** | 04, 05 |
| 9 | Construir **modelos financieros nivel Wall Street** (DCF, LBO) con Cowork + Excel | 07 |
| 10 | Diseñar y gestionar un **equipo de agentes autónomos** de la investigación al envío de emails | 11, 12, 13 |
| 11 | Entender **Subagentes** y **Agent Teams** para proyectos complejos multi‑paso | 11 |
| 12 | Usar Claude Code para **scaffolding, diseño y despliegue** de webs con orquestación agéntica y previsualización en vivo | 10 |

---

## Temario

| Módulo | Archivo | Contenido |
|--------|---------|-----------|
| 00 | [Introducción y mapa del ecosistema](modulos/00-introduccion.md) | El poder de Claude Code y Cowork, esquema del curso, consejos de éxito |
| 01 | [Claude Cowork: fundamentos](modulos/01-cowork-fundamentos.md) | Qué es Cowork, cómo funciona, demo: organizar archivos y usar la skill de Excel |
| 02 | [MCP, conectores, tokens y ventana de contexto](modulos/02-mcp-conectores-tokens.md) | Model Context Protocol, demo Gmail, tokens, práctica |
| 03 | [Agent Skills y Plugins en Cowork](modulos/03-skills-y-plugins.md) | Skills, demo LinkedIn, plugin de datos (4 partes), plugin de finanzas (3 partes), prácticas |
| 04 | [Claude Chat: investigación, escritura y creatividad](modulos/04-claude-chat.md) | Research, Deep Research, escritura creativa, brainstorming, dashboards, PDF→Excel→PPT |
| 05 | [Prompt Engineering y Context Engineering](modulos/05-prompt-context-engineering.md) | Fundamentos, técnicas avanzadas, context engineering, plantillas |
| 06 | [Claude en Excel](modulos/06-claude-en-excel.md) | Instalación, insights, estadística, gráficos, orden, filtros, formato condicional, imputación |
| 07 | [Modelos financieros nivel Wall Street](modulos/07-modelos-financieros.md) | Forecasting, 3 estados, DCF, LBO, práctica |
| 08 | [Claude en PowerPoint e informes ejecutivos](modulos/08-claude-en-powerpoint.md) | Add‑in, notas del orador, diseño, PDFs→slides, plantillas de marca, coaching; Claude vs Copilot vs NotebookLM |
| 09 | [Claude Code: instalación y fundamentos](modulos/09-claude-code-fundamentos.md) | Desktop, VS Code, terminal, slash commands, CLAUDE.md, gestión de contexto, plugins |
| 10 | [Claude Code: proyectos full‑stack](modulos/10-claude-code-proyectos.md) | Landing pages con/sin skill, slash command de marca, plugin de competencia, Calorie Tracker con IA y Ralph Loops, despliegue |
| 11 | [Agentes de IA, Subagentes y Agent Teams](modulos/11-agentes-subagentes-teams.md) | Agentes 101, MCP 101, frameworks, OpenAI Agents SDK, Claude Agent SDK, agente financiero con memoria, equipos de agentes |
| 12 | [Tu agente personal con Claude Code y Cowork](modulos/12-agente-personal.md) | Arquitectura, patrón Wiki de Karpathy, Obsidian, vault, SOUL.md, CLAUDE.md, carpeta de marca, setup |
| 13 | [Las 10 automatizaciones](modulos/13-automatizaciones.md) | Sprint Tracker, Morning Brief, Market Pulse, Research Team, CRM, Meeting Intel, Email Triage, Expense Wrangler, Content Machine, Weekly Exec Report |
| — | [Skills y plugins del curso](SKILLS-Y-PLUGINS.md) | Qué skills/plugins usa el curso, cuáles ya tenés y cómo instalar el resto |
| — | [Plantillas](plantillas/) | SKILL.md, slash commands, subagentes, plugin de finanzas, SOUL.md, CLAUDE.md |
| — | [Código](codigo/) | Ejemplos de agentes en Python (OpenAI Agents SDK y Claude Agent SDK) |

---

## Cómo usar este curso

1. **Seguí el orden.** Los módulos 00–08 no requieren programar. Los módulos 09–13 usan terminal y algo de código.
2. **Hacé cada práctica antes de mirar la solución.** Cada sección "🧪 Práctica" tiene su "✅ Solución" debajo.
3. **Copiá las plantillas.** La carpeta [`plantillas/`](plantillas/) está lista para pegar en `~/.claude/` o en tu proyecto.
4. **Llevá un diario de prompts.** Guardá los prompts que te funcionaron: se convierten en skills y slash commands.

### Requisitos

- Cuenta de Claude (plan Pro, Max, Team o Enterprise para Cowork, Claude Code y los add‑ins de Office).
- **Claude Desktop** (Mac o Windows) para Cowork.
- Microsoft Excel y PowerPoint (365) para los módulos 06–08.
- Node.js 18+ y Git para los módulos 09–13. Python 3.10+ para el módulo 11.

> ⚠️ **Nota:** las interfaces de Claude cambian rápido. Si un botón o comando tiene otro nombre en tu versión, buscá la función equivalente o escribí `/help` en Claude Code. La lógica y los patrones del curso siguen siendo válidos.
