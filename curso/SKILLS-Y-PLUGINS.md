# Skills y plugins del curso: inventario e instalación

<img src="assets/linea.svg" alt="" width="100%">

Estas son las skills y plugins que el curso usa o recomienda, agrupadas por prioridad. Todos los plugins listados son del **Anthropic Directory** (directorio oficial), salvo los marcados como *comunidad* o *partner*.

## A. Skills ya incluidas en tu cuenta ✅ (no requieren instalación)

| Skill | Para qué la usa el curso | Módulos |
|-------|--------------------------|---------|
| `xlsx` | Excel con fórmulas, formato, gráficos; limpieza de datos | 01, 03, 06, 07 |
| `pptx` | Presentaciones, one pagers, decks de marca | 03, 04, 08, 13 |
| `docx` | Informes ejecutivos en Word | 01, 13 |
| `pdf` | Extraer datos de PDFs, generar informes PDF | 04, 08, 13 |
| `skill-creator` | Crear y mejorar tus propias skills y plugins | 03, 09, 10, 12 |

## B. Plugins esenciales (instalar) ⭐

| Plugin | Qué agrega | Módulos |
|--------|-----------|---------|
| **Data** | `explore-data`, `validate-data`, `statistical-analysis`, `data-visualization`, `create-viz`, `build-dashboard`, `analyze`, `sql-queries` | 03 (Data Plugin partes 1–4), 06 |
| **Finance** | `financial-statements`, `variance-analysis`, `reconciliation`, `close-management`, `journal-entry`, `audit-support` | 03 (finanzas), 07, 13 (Expense Wrangler) |
| **model-builder** (Anthropic FSI) | `dcf-model`, `lbo-model`, `3-statement-model`, `comps-analysis`, `audit-xls` — modelos en Excel | 07 (DCF, LBO) |
| **frontend-design** | Skill de diseño front‑end de calidad | 04 (dashboards), 10 (landing pages) |
| **Marketing** | `content-creation`, `draft-content`, `brand-review`, `competitive-brief`, `campaign-plan`, `performance-report`, `seo-audit` | 03 (LinkedIn), 10 (competencia y marca), 13 (Content Machine) |
| **Productivity** | `task-management`, `memory-management`, `start`, `update` + conectores Gmail/Calendar/Slack/Notion | 12 (agente personal), 13 (Morning Brief, Sprint Tracker, Email Triage) |
| **plugin-dev** | Skills para crear agentes, comandos, hooks, MCP y estructura de plugins; comando `/create-plugin` | 03, 09, 10 (crear plugins propios) |
| **ralph-loop** | Comando `/ralph-loop` (técnica Ralph Wiggum) | 10 (Calorie Tracker fase 3) |

## C. Plugins recomendados (opcionales según tu perfil)

| Plugin | Qué agrega | Módulos |
|--------|-----------|---------|
| **Legal** | `review-contract`, `triage-nda`, `compliance-check`, `legal-risk-assessment` | 01 (casos legales) |
| **Sales** | `account-research`, `call-prep`, `pipeline-review`, `forecast` + conector **Salesforce**/HubSpot | 02 (Salesforce), 13 (Personal CRM, Meeting Intel) |
| **pitch-agent** (Anthropic FSI) | Comps + LBO → pitch deck de marca de punta a punta | 07, 08 |
| **market-researcher** (Anthropic FSI) | Sector overview, competencia, comps | 07, 13 (Market Pulse, Research Team) |
| **investment-banking** | One pager, teaser, CIM, merger model | 07, 08 |
| **feature-dev** | Flujo de desarrollo con agentes `code-explorer`, `code-architect`, `code-reviewer` | 10, 11 (subagentes) |
| **agent-sdk-dev** | `/new-sdk-app` para crear apps con Claude Agent SDK | 11 |
| **code-review** | Revisión automática de código con múltiples agentes | 10 |
| **hookify** | Crear hooks para evitar comportamientos no deseados | 09 |
| **Exa Deep Research** (partner) | Búsqueda web y research multi‑paso vía MCP | 04, 13 (Research Team) |
| **obsidian-sync** (comunidad) | Sincroniza markdown del proyecto con tu vault de Obsidian | 12 |

## D. Conectores (MCP) que pide el curso

Se activan en *Configuración → Conectores* (no son plugins): **Gmail, Google Calendar, Google Drive, Slack, Notion, Salesforce** (o HubSpot). Varios plugins de arriba ya los traen declarados.

## E. Cómo instalar

**En Claude (web / Desktop / Cowork):** *Configuración → Plugins* (o *Personalizar*) → buscar el nombre → **Instalar**. Las skills sueltas se activan en *Configuración → Capacidades*.

**En Claude Code (terminal):**

```bash
# Dentro de una sesión de Claude Code
/plugin                                   # abre el gestor de plugins
/plugin marketplace add anthropics/claude-plugins-official
/plugin install frontend-design@claude-plugins-official
/plugin install ralph-loop@claude-plugins-official
/plugin install plugin-dev@claude-plugins-official
/plugin install feature-dev@claude-plugins-official

/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install data@knowledge-work-plugins
/plugin install finance@knowledge-work-plugins
/plugin install marketing@knowledge-work-plugins
/plugin install productivity@knowledge-work-plugins

/plugin marketplace add anthropics/financial-services
# luego elegí model-builder, pitch-agent o market-researcher desde /plugin
```

> Los nombres exactos del marketplace pueden variar con las versiones: si un `install` falla, abrí `/plugin`, entrá en el marketplace y elegí el plugin desde el menú.
