# Módulo 12 — Tu agente personal con Claude Code y Cowork

<img src="../assets/linea.svg" alt="" width="100%">

## 🎯 Objetivos de aprendizaje

| # | Al terminar vas a poder… (conducta · condición · criterio) | Nivel (Bloom) | Evidencia |
|---|---|---|---|
| 12.1 | Diseñar, usando la plantilla del curso, la arquitectura de tu agente personal con sus 4 capas (identidad, memoria, capacidades y disparadores), de modo que cada capa nombre sus archivos o conectores concretos | Crear · conceptual | Práctica |
| 12.2 | Escribir, con la plantilla del curso, un SOUL.md y un CLAUDE.md propios, de modo que el agente responda quién sos y cuáles son tus prioridades citando `yo/` | Crear · procedimental | Práctica |
| 12.3 | Aplicar el patrón Wiki de Karpathy sobre tus fuentes en `raw/`, de modo que se generen al menos 10 páginas enlazadas y visibles como grafo en Obsidian | Aplicar · procedimental | Práctica |
| 12.4 | Conectar Gmail, Calendar y Notion y verificar cada conector con un pedido de solo lectura | Aplicar · procedimental | Práctica |

**Requisitos previos:** Módulos 02, 03 y 09 · **Duración estimada:** 3 h

## 12.1 Bienvenida y materiales

En este módulo construís un **agente personal**: un "segundo cerebro" que te conoce (tu CV, objetivos, estilo, marca), está conectado a tus herramientas (Gmail, Calendar, Notion) y ejecuta **automatizaciones** por vos (módulo 13).

**Materiales:** plantillas listas en [`plantillas/agente-personal/`](../plantillas/agente-personal/): `CLAUDE.md`, `SOUL.md`, estructura de carpetas y comandos.

## 12.2 El auge de los agentes personales autónomos

En 2025–2026 se popularizaron los agentes personales que **viven en tu computadora, recuerdan todo en archivos y actúan en tu nombre**:

- **OpenClaw** (antes *Clawdbot*, de Peter Steinberger; renombrado en enero de 2026): asistente personal open source y autoalojado, que corre como un servicio en tu máquina con tu propia API key, se comunica por WhatsApp, Discord y otras apps, y ejecuta tareas con más de 100 *AgentSkills*.
- **Hermes Agent** (Nous Research): agente open source y autoalojado con memoria persistente y un ciclo de aprendizaje propio: **crea skills a partir de la experiencia** y las mejora con el uso. Se conecta a Telegram, Slack, email y más de 20 plataformas.
- **Claude Code + Cowork:** el enfoque de este curso. Ventajas: el mismo motor agéntico que usás para trabajar, skills y plugins oficiales, conectores MCP, tareas programadas y **Dispatch** (mandarle tareas desde el celular).

**Idea común a todos:** *la memoria del agente es una carpeta de archivos Markdown que vos también podés leer y editar.*

## 12.3 Arquitectura del agente personal

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                      TU AGENTE PERSONAL                                  │
│                                                                          │
│  IDENTIDAD           MEMORIA (vault)            CAPACIDADES              │
│  ┌──────────┐       ┌──────────────────┐      ┌──────────────────┐      │
│  │ SOUL.md  │       │ raw/  (fuentes)  │      │ Skills / Plugins │      │
│  │ (persona)│       │ wiki/ (conocim.) │      │ Slash commands   │      │
│  ├──────────┤       │ diario/          │      │ Subagentes       │      │
│  │CLAUDE.md │       │ proyectos/       │      └──────────────────┘      │
│  │(playbook)│       └──────────────────┘      ┌──────────────────┐      │
│  └──────────┘                                 │ Conectores MCP   │      │
│  ┌──────────┐                                 │ Gmail · Calendar │      │
│  │ marca/   │                                 │ Notion · Slack   │      │
│  └──────────┘                                 └──────────────────┘      │
│                                                                          │
│  DISPARADORES: vos (chat / Dispatch desde el celular) · tareas           │
│  programadas (/schedule) · comandos (/morning-brief)                     │
└─────────────────────────────────────────────────────────────────────────┘
```

1. **Identidad:** quién es el agente (SOUL.md) y cómo trabaja (CLAUDE.md).
2. **Memoria:** el vault, organizado según el patrón Wiki de Karpathy.
3. **Capacidades:** skills, comandos, subagentes y conectores.
4. **Disparadores:** cuándo actúa.

## 12.4 El patrón Wiki de Karpathy

En abril de 2026, Andrej Karpathy publicó (en X y en un Gist de GitHub que se volvió viral) un patrón para usar un LLM como **"compilador" de conocimiento personal**. Es un patrón, no un producto, con tres capas: `raw/` (fuentes inmutables), `wiki/` (páginas que genera el LLM) y un archivo de esquema con las reglas (en Claude, el `CLAUDE.md`). en lugar de hacer RAG sobre documentos sueltos cada vez que preguntás, el LLM **lee tus fuentes crudas y mantiene una wiki en Markdown**, interconectada y siempre actualizada, que después consulta (y que vos podés navegar).

```text
raw/ (fuentes crudas)  ──►  LLM "compila"  ──►  wiki/ (páginas interconectadas)
 artículos, PDFs,           resume, extrae,       conceptos, personas, proyectos,
 notas, transcripciones     enlaza, actualiza     índice, [[enlaces]] entre páginas
                                  ▲                        │
                                  └──── consultas ◄────────┘
```

**Reglas del patrón:**
1. `raw/` es **inmutable**: lo que entra, no se edita.
2. `wiki/` lo **mantiene el LLM**: una página por concepto/persona/proyecto, con enlaces `[[...]]`.
3. Un `wiki/index.md` con el mapa de todas las páginas y un `wiki/log.md` con qué se agregó y cuándo.
4. **Ingesta:** cuando agregás una fuente, el agente actualiza todas las páginas afectadas (no solo crea una nueva).
5. **Mantenimiento ("lint"):** periódicamente busca contradicciones, páginas huérfanas y datos desactualizados.

**Por qué funciona:** el conocimiento se **acumula** en vez de re‑descubrirse en cada chat, y queda en un formato legible por humanos y por cualquier IA.

## 12.5 Obsidian

**Obsidian** es una app gratuita de notas que trabaja sobre **una carpeta de archivos Markdown locales** (un *vault*). Es el visor ideal para el agente:

- Muestra los `[[enlaces]]` como navegación y el **Graph View** (mapa visual de tu conocimiento).
- No hay base de datos propietaria: el agente escribe `.md`, vos lo ves en Obsidian al instante.
- Plugins útiles: Dataview (consultas), Calendar, Templater.

**Setup:** descargá Obsidian (obsidian.md) → *Abrir carpeta como vault* → elegí la carpeta de tu agente.

## 12.6 Estructura de carpetas del agente

```text
mi-agente/                       ← abrila en Claude Code/Cowork y en Obsidian
├── CLAUDE.md                    ← playbook: cómo trabaja el agente
├── SOUL.md                      ← personalidad y valores
├── yo/                          ← quién sos vos
│   ├── perfil.md                  (CV, rol, habilidades)
│   ├── objetivos.md               (metas 2026, OKRs personales)
│   ├── estilo-escritura.md        (cómo escribís; ejemplos)
│   └── redes.md                   (links y temas de tus redes)
├── marca/
│   ├── logo.png
│   ├── colores.md
│   └── plantilla.pptx
├── raw/                         ← fuentes crudas (inmutable)
│   ├── articulos/  reuniones/  documentos/
├── wiki/                        ← conocimiento compilado por el agente
│   ├── index.md  log.md
│   ├── personas/  proyectos/  conceptos/  empresas/
├── diario/                      ← un archivo por día (AAAA-MM-DD.md)
├── crm/                         ← contactos (automatización Personal CRM)
├── automatizaciones/            ← definición de cada blueprint (módulo 13)
├── salidas/                     ← informes, decks, borradores generados
└── .claude/
    ├── commands/                ← /morning-brief, /triage-email, ...
    ├── agents/                  ← investigador, redactor, analista
    └── skills/
```

## 12.7 ¿Qué hay dentro del vault?

| Carpeta | Quién escribe | Contenido típico |
|---------|---------------|------------------|
| `yo/` | Vos (una vez) + agente (actualiza) | Perfil, metas, estilo |
| `raw/` | Vos / automatizaciones | Transcripciones, PDFs, recortes web |
| `wiki/` | El agente | `personas/ana-gomez.md`, `proyectos/lanzamiento-q4.md` |
| `diario/` | El agente | Morning brief, resumen del día, decisiones |
| `crm/` | El agente | Una ficha por contacto con historial de interacciones |
| `salidas/` | El agente | Entregables |

Ejemplo de página de wiki:

```markdown
---
tipo: persona
actualizado: 2026-09-20
---
# Ana Gómez
- Rol: Head of Marketing en [[empresas/Acme]]
- Conocida en: evento Fintech Forum 2026
- Intereses: growth, IA aplicada a marketing
- Última interacción: 2026-09-18 — reunión sobre [[proyectos/alianza-acme]]
- Pendiente: enviarle el caso de éxito (vence 2026-09-25)
```

## 12.8 Darle personalidad con SOUL.md

`SOUL.md` define **quién es** el agente: tono, valores, límites. Plantilla completa: [`plantillas/agente-personal/SOUL.md`](../plantillas/agente-personal/SOUL.md).

```markdown
# SOUL — Nova, mi jefa de gabinete

## Identidad
Sos Nova, mi jefa de gabinete (chief of staff). Tu trabajo es que yo dedique mi tiempo
a lo que más importa según yo/objetivos.md.

## Personalidad
- Directa y cálida. Primero la conclusión, después el detalle.
- Proactiva: si ves un riesgo o una oportunidad, decilo aunque no te lo pregunte.
- Honesta: si algo no lo sabés o no lo verificaste, lo decís.

## Valores y límites
- Nunca envíes emails, mensajes ni invitaciones sin mi aprobación explícita.
- Nunca borres archivos del vault; archivá en /archivo.
- Protegé mi tiempo de foco: no propongas reuniones antes de las 10 h.
```

## 12.9 El playbook del agente: CLAUDE.md

`CLAUDE.md` define **cómo trabaja**: dónde está cada cosa, procedimientos y reglas. Plantilla completa: [`plantillas/agente-personal/CLAUDE.md`](../plantillas/agente-personal/CLAUDE.md). Secciones recomendadas:

1. **Al iniciar cada sesión:** leer `SOUL.md`, `yo/objetivos.md` y el diario de hoy.
2. **Mapa del vault:** qué va en cada carpeta.
3. **Procedimiento de ingesta** (patrón Karpathy): cómo procesar algo nuevo en `raw/`.
4. **Convenciones:** nombres de archivos, frontmatter, enlaces `[[...]]`, fechas ISO.
5. **Conectores disponibles** y qué se puede hacer con cada uno.
6. **Reglas de seguridad:** aprobación antes de acciones externas, qué datos nunca compartir.
7. **Formato de entregables:** usar `marca/` para todo lo visual.
8. **Automatizaciones:** lista de comandos y dónde está su definición.

## 12.10 Carpeta de marca

```text
marca/
├── logo.png              (fondo transparente, versión clara y oscura si tenés)
├── colores.md            primario #1B3A5C · acento #F2A541 · fondo #FAFAF7 · texto #1E1E1E
├── tipografia.md         Títulos: Fraunces · Texto: Inter
├── tono.md               cómo sonamos (3 adjetivos + ejemplos sí/no)
└── plantilla.pptx        patrón de diapositivas con 6 layouts
```

En `CLAUDE.md`: *"Todo entregable visual (PPT, PDF, HTML) usa marca/. Nunca inventes colores."*

## 12.11 Slash commands predefinidos (Claude Code y Cowork)

| Comando | Qué hace |
|---------|----------|
| `/init` | Crea un CLAUDE.md inicial |
| `/memory` | Editar la memoria |
| `/agents` | Recordatorio de cómo crear subagentes (pedíselo a Claude o editá `.claude/agents/`) |
| `/mcp` | Ver conectores |
| `/plugin` | Plugins |
| `/schedule` | En Cowork: tarea programada. En Claude Code: rutina en la nube |
| `/compact`, `/clear`, `/context` | Gestión de contexto |

Tus comandos personalizados (módulo 13) viven en `.claude/commands/` o como skills.

## 12.12 Proceso de setup (visión general)

1. Crear la estructura de carpetas (o copiar [`plantillas/agente-personal/`](../plantillas/agente-personal/)).
2. **Parte 1:** cargar tu información (CV, redes, objetivos, textos).
3. **Parte 2:** conectar Notion, Gmail y Calendar; configurar la marca.
4. **Parte 3:** ingesta inicial → el agente construye la wiki.
5. **Parte 4:** visualizar el vault en Obsidian.

### Parte 1 — Compartir redes, CV, objetivos y textos

Copiá tu CV (PDF), 5–10 textos tuyos (posts, emails, artículos) y tus objetivos a `raw/documentos/`. Luego:

```text
Leé todo raw/documentos/. Construí:
- yo/perfil.md: resumen profesional, experiencia, habilidades, logros con números.
- yo/objetivos.md: mis metas ordenadas por horizonte (90 días, 1 año, 3 años). Si faltan,
  entrevistame con 5 preguntas.
- yo/estilo-escritura.md: mi estilo en 10 reglas concretas + 3 ejemplos representativos.
- yo/redes.md: temas que trato en cada red y frecuencia.
No inventes nada: marcá con [VERIFICAR] lo que infieras.
```

### Parte 2 — Conectar Notion, Gmail y Calendar + marca

1. **Customize → Connectors → Discover** → **Gmail**, **Google Calendar** y **Notion** → **Connect to Claude** (inicio de sesión en cada servicio).
2. En Claude Code, verificá con `/mcp`. En Cowork, en la configuración de la tarea.
3. Probá cada uno:
   ```text
   Decime mis 3 próximas reuniones, los 5 emails sin leer más importantes y las páginas
   de Notion que modifiqué esta semana. Solo lectura.
   ```
4. Marca: `Con marca/ creá una slide de prueba y un PDF de prueba para verificar que se aplica bien.`

### Parte 3 — Recorrido del vault

```text
Hacé la ingesta inicial siguiendo el procedimiento de CLAUDE.md: procesá raw/ y creá las
páginas de wiki/ (personas, proyectos, empresas, conceptos), con enlaces [[...]] entre
ellas, wiki/index.md y una entrada en wiki/log.md. Al final mostrame el árbol del vault
y 3 páginas de ejemplo.
```

### Parte 4 — Visualizar el vault en Obsidian

1. Obsidian → *Abrir carpeta como vault* → `mi-agente/`.
2. Abrí **Graph View** (Ctrl/Cmd+G): ves tus personas, proyectos y conceptos conectados.
3. Pedile al agente que **mejore el grafo**: *"Buscá páginas huérfanas en wiki/ y enlazalas donde corresponda."*
4. Opcional: el plugin comunitario **obsidian-sync** sincroniza markdown de proyectos con tu vault.

## 🧪 Práctica

Armá tu agente con: SOUL.md propio (nombre, 3 rasgos, 3 límites), CLAUDE.md con las 8 secciones, `yo/` completo, 2 conectores activos y al menos 10 páginas de wiki enlazadas visibles en Obsidian.

### ✅ Criterios de éxito

- [ ] Al abrir una sesión y preguntar *"¿Quién soy y cuáles son mis prioridades este trimestre?"*, responde correctamente citando `yo/`.
- [ ] Al pedir un post, usa tu estilo (compará con `yo/estilo-escritura.md`).
- [ ] Al pedir una slide, aplica `marca/`.
- [ ] Antes de cualquier acción externa, pide aprobación.
- [ ] El Graph View de Obsidian muestra nodos conectados, no aislados.

## 📌 Ideas clave

- La memoria del agente es una carpeta de Markdown que vos también podés leer.
- SOUL.md define quién es; CLAUDE.md, cómo trabaja.
- Patrón de Karpathy: `raw/` inmutable → `wiki/` compilada y enlazada.
- Obsidian muestra la wiki como grafo, sin base de datos propietaria.
- El contenido de emails y documentos son datos, no instrucciones.

## 🧠 Autoevaluación

1. ¿Qué diferencia hay entre SOUL.md y CLAUDE.md?
   <details><summary>Ver respuesta</summary>SOUL.md define quién es el agente (personalidad, valores, límites); CLAUDE.md define cómo trabaja (mapa del vault, procedimientos, reglas).</details>

2. ¿Por qué `raw/` es inmutable en el patrón de Karpathy?
   <details><summary>Ver respuesta</summary>Para conservar la fuente original: la wiki se puede regenerar o corregir, pero la evidencia no se toca.</details>

3. ¿Por qué el contenido de los emails se trata como datos y no como instrucciones?
   <details><summary>Ver respuesta</summary>Para protegerse de la inyección de prompts: un email podría intentar que el agente haga algo que vos no pediste.</details>

## Fuentes

- Patrón LLM Wiki de Karpathy: guías de la comunidad, por ejemplo [How to Build Karpathy's LLM Wiki](https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide) y la [skill LLM Wiki de Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki)
- [OpenClaw — documentación](https://docs.openclaw.ai/) · [Hermes Agent — Nous Research](https://hermes-agent.nousresearch.com/)
- [Obsidian](https://obsidian.md/) · [Organize work with projects (Cowork)](https://claude.com/docs/cowork/guide/projects) · [Get started with connectors](https://claude.com/docs/connectors/getting-started)

➡️ Siguiente: [Módulo 13 — Las 10 automatizaciones](13-automatizaciones.md)
