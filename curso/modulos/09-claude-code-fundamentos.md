# Módulo 09 — Claude Code: instalación y fundamentos

> **🎯 Objetivos.** Al terminar este módulo vas a poder:
> - Instalar Claude Code en Mac, Windows o Linux y usarlo desde la terminal, VS Code o la app de escritorio.
> - Trabajar con modos de permiso, Plan mode y el flujo explorar → planificar → codear → verificar.
> - Crear slash commands propios y un CLAUDE.md efectivo.
> - Gestionar la ventana de contexto y configurar plugins y hooks.
>
> **Requisitos previos:** Node.js 18+ y Git instalados · **Duración estimada:** 2 h

## 9.1 ¿Qué es Claude Code?

**Claude Code** es el agente de programación de Anthropic. Vive en tu terminal (y también en VS Code, JetBrains, la app de escritorio y la web) y puede:

- Leer y entender todo tu proyecto.
- Crear y editar archivos, ejecutar comandos (tests, builds, git, servidores).
- Planificar tareas grandes, delegar en **subagentes** y usar **skills, plugins, hooks y MCP**.
- Iterar solo: escribe código → lo ejecuta → ve el error → lo corrige.

> Cowork = Claude agéntico para documentos. Claude Code = Claude agéntico para software. **Mismo motor.**

## 9.2 Método 1: Claude Code en la app de escritorio

1. Abrí **Claude Desktop** → pestaña **Code**.
2. Elegí una carpeta de proyecto (local) o un repositorio de GitHub (para trabajar en la nube).
3. Escribí tu pedido. Vas a ver el plan, los archivos que cambia (diff) y los comandos que corre.
4. Ideal si no te sentís cómodo con la terminal. Incluye **vista previa** del sitio que estás construyendo.

## 9.3 Método 2: Claude Code en VS Code (setup completo)

1. Instalá **VS Code** y **Node.js 18+** (nodejs.org, versión LTS) y **Git**.
2. Instalá Claude Code (ver 9.4).
3. En VS Code: **Extensiones** → buscá **"Claude Code"** (Anthropic) → Instalar.
4. Abrí tu carpeta de proyecto → clic en el ícono de Claude (el destello naranja) en la barra superior del editor o en la barra lateral. También podés abrir la paleta de comandos (`Ctrl/Cmd+Shift+P`) y buscar "Claude Code".
5. Iniciá sesión con tu cuenta de Claude (Pro/Max/Team/Enterprise) o una API key.

**Primer flujo:**

```text
Explicame la estructura de este proyecto y cómo lo ejecuto.
```
```text
Creá un archivo index.html con una página "Hola mundo" moderna y abrila en el navegador.
```

La extensión muestra los **diffs** en el editor para que aceptes o rechaces cambios.

## 9.4 Instalación en Mac y Windows (terminal)

**Mac / Linux / WSL:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**Alternativa con npm (cualquier SO con Node 18+):**
```bash
npm install -g @anthropic-ai/claude-code
```

**Verificar y arrancar:**
```bash
claude --version
cd mi-proyecto
claude            # abre la sesión interactiva; la primera vez te pide iniciar sesión
```

Diagnóstico: `claude doctor`. Actualizar: `claude update`.

> En Windows, Git for Windows es necesario (Claude Code usa Git Bash). Si algo falla, probá dentro de **WSL**.

## 9.5 Introducción a la interfaz

### Atajos esenciales

| Atajo | Acción |
|-------|--------|
| `Shift+Tab` | Alterna modos de permiso: normal → aceptar ediciones automáticamente → **Plan mode** (solo planifica, no toca nada) |
| `Esc` | Interrumpe a Claude |
| `Esc` `Esc` | Volver a un mensaje anterior (rewind) |
| `@archivo` | Referencia un archivo o carpeta en tu mensaje |
| `!comando` | Ejecuta un comando de shell directamente |
| `Ctrl+C` (x2) | Salir |
| `↑` | Mensajes anteriores |

### Modos de permiso

- **Normal:** pide permiso para editar archivos y ejecutar comandos.
- **Aceptar ediciones:** edita sin preguntar (sigue preguntando comandos riesgosos).
- **Plan mode:** investiga y propone un plan. **Usalo siempre para tareas grandes.**

Permisos finos en `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": ["Bash(npm run test:*)", "Bash(npm run lint)", "Edit(src/**)"],
    "deny": ["Read(./.env)", "Bash(rm -rf:*)"]
  }
}
```

### Flujo recomendado: Explorar → Planificar → Codear → Verificar → Commit

```text
1. "Leé los archivos de autenticación y explicame cómo funciona. No escribas código aún."
2. (Plan mode) "Proponé un plan para agregar login con Google."
3. "Implementá el plan. Corré los tests después de cada paso."
4. "Revisá tu propio diff buscando bugs y casos borde."
5. "Hacé commit con un mensaje descriptivo."
```

## 9.6 Slash commands

### Comandos incorporados más útiles

| Comando | Para qué |
|---------|----------|
| `/help` | Ayuda y lista de comandos |
| `/init` | Analiza el proyecto y crea `CLAUDE.md` |
| `/clear` | Borra la conversación (contexto limpio) |
| `/compact [instrucciones]` | Resume la conversación para liberar contexto |
| `/context` | Muestra qué ocupa la ventana de contexto |
| `/usage` (alias `/cost`) | Costo de la sesión, uso del plan y estadísticas |
| `/model` | Cambiar de modelo |
| `/memory` | Editar los archivos de memoria (CLAUDE.md) |
| `/agents` | Crear y gestionar subagentes |
| `/mcp` | Estado de servidores MCP |
| `/plugin` | Instalar/gestionar plugins y marketplaces |
| `/hooks` | Configurar hooks |
| `/permissions` | Ver/editar permisos |
| `/resume` | Retomar una sesión anterior |
| `/rewind` | Volver a un punto anterior (código y conversación) |
| `/review` | Revisión de código |

### Comandos personalizados

Un slash command propio es un archivo Markdown:

- **Del proyecto:** `.claude/commands/<nombre>.md` → se invoca como `/<nombre>` (compartido por git).
- **Personal:** `~/.claude/commands/<nombre>.md` → disponible en todos tus proyectos.
- Hoy también podés crearlo como **skill** en `.claude/skills/<nombre>/SKILL.md`: se invoca igual con `/<nombre>` y además Claude puede usarlo solo cuando es relevante.

```markdown
---
description: Crea un componente React con test y story
argument-hint: <NombreComponente>
allowed-tools: Read, Write, Edit, Bash(npm run test:*)
---

Creá el componente $ARGUMENTS en src/components/$ARGUMENTS/:
1. $ARGUMENTS.tsx con TypeScript y props tipadas.
2. $ARGUMENTS.test.tsx con Testing Library (render + interacción principal).
3. Seguí el estilo de src/components/Button/.
4. Corré los tests y mostrame el resultado.
```

Variables: `$ARGUMENTS` (todo el texto) y `$0`, `$1`, `$2`… para argumentos posicionales. **Ojo: empiezan en 0**: `$0` es el primer argumento. También podés declarar nombres con `arguments: [cliente, mes]` en el frontmatter y usar `$cliente` y `$mes`. Podés incluir la salida de comandos con `` !`git status` `` y archivos con `@ruta`.

## 9.7 CLAUDE.md: mejores prácticas

`CLAUDE.md` es la **memoria del proyecto**: Claude lo lee automáticamente al iniciar cada sesión.

**Ubicaciones (se combinan):**

| Archivo | Alcance |
|---------|---------|
| `~/.claude/CLAUDE.md` | Tus preferencias en todos los proyectos |
| `./CLAUDE.md` | El proyecto (va a git, lo comparte el equipo) |
| `./CLAUDE.local.md` | Personal para este proyecto (no se commitea) |
| `./subcarpeta/CLAUDE.md` | Se carga cuando Claude trabaja en esa carpeta |

**Qué poner:**

```markdown
# Proyecto: Calorie Tracker

## Stack
Next.js 15 (App Router), TypeScript, Tailwind, Prisma + SQLite, Vitest.

## Comandos
- `npm run dev` — servidor en http://localhost:3000
- `npm test` — tests; correr antes de cada commit
- `npm run lint` — debe pasar sin errores

## Convenciones
- Componentes en src/components, un componente por archivo, PascalCase.
- Llamadas a la IA SOLO desde src/app/api (nunca desde el cliente).
- Validar toda entrada con Zod.

## Importante
- NUNCA commitear .env ni claves.
- Ver @docs/arquitectura.md para el flujo de datos.
```

**Reglas de oro:**
1. **Corto y específico** (< ~200 líneas). Cada línea compite por atención en cada sesión.
2. Escribí lo que **Claude no puede inferir** del código: comandos, decisiones, trampas conocidas.
3. Usá **énfasis** solo en reglas críticas ("IMPORTANTE", "NUNCA").
4. Enlazá documentos largos con `@ruta` en vez de pegarlos.
5. **Mantenelo vivo:** cuando Claude comete el mismo error dos veces, agregá una regla. Revisalo con `/memory`.
6. Empezá con `/init` y editalo a mano.

## 9.8 Gestión de la ventana de contexto en Claude Code

1. **`/context`** para ver qué ocupa espacio (sistema, herramientas MCP, memoria, mensajes).
2. **`/clear` entre tareas no relacionadas.** Es el hábito más importante.
3. **`/compact Enfocate en las decisiones de la API y los pendientes`** cuando la tarea sigue pero el historial es largo. Claude también compacta automáticamente cerca del límite.
4. **Subagentes** para exploraciones grandes: *"Usá un subagente para investigar cómo se maneja el caché en todo el repo y traeme un resumen"*. El ruido queda en el contexto del subagente.
5. **Archivos de plan/progreso:** en tareas largas, `PLAN.md` y `PROGRESO.md` sobreviven a `/clear` y compactaciones.
6. **Desactivá MCPs** que no uses en el proyecto (`/mcp`).
7. **Referencias precisas:** `@src/lib/auth.ts` en vez de "fijate en la autenticación".

## 9.9 Plugins en Claude Code

```bash
/plugin                                                   # gestor interactivo
/plugin marketplace add anthropics/claude-plugins-official
/plugin install frontend-design@claude-plugins-official
```

Para que todo el equipo tenga los mismos plugins, declaralos en `.claude/settings.json` del repo (este repositorio ya lo hace: mirá [`.claude/settings.json`](../../.claude/settings.json)).

Un plugin puede traer: **skills**, **commands**, **agents** (subagentes), **hooks** y **servidores MCP**. Estructura en el módulo 03.3 y plantilla en [`plantillas/plugin-finanzas/`](../plantillas/plugin-finanzas/).

## 9.10 Hooks (automatismos deterministas)

Los **hooks** ejecutan comandos de shell en momentos del ciclo de vida del agente (`PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SessionStart`, `Notification`…). A diferencia de una instrucción en CLAUDE.md, **siempre se ejecutan**.

Ejemplo: formatear automáticamente con Prettier cada archivo que Claude edita. El hook recibe por la entrada estándar un JSON con los datos de la herramienta; `jq` extrae la ruta del archivo editado (necesitás tener `jq` instalado):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write --log-level silent" }]
      }
    ]
  }
}
```

Tip: el plugin **hookify** crea hooks a partir de lo que no querés que Claude repita.

## 🧪 Práctica: tu entorno de Claude Code listo para trabajar

1. Instalá Claude Code y verificá con `claude --version` y `claude doctor`.
2. Creá una carpeta de proyecto, iniciá Git (`git init`) y abrí `claude`.
3. Corré `/init` y editá el `CLAUDE.md` para que tenga stack, comandos, convenciones y una sección "Importante".
4. Creá un slash command propio `/explicar <archivo>` que explique un archivo para alguien que recién empieza.
5. Configurá un permiso `deny` que impida leer `.env`.
6. Revisá el contexto con `/context`, hacé `/compact` y comprobá la diferencia.

### ✅ Solución

`.claude/commands/explicar.md`:

```markdown
---
description: Explica un archivo del proyecto para alguien que recién empieza
argument-hint: <ruta del archivo>
---
Leé @$ARGUMENTS y explicalo para una persona que recién empieza a programar:
1. Para qué sirve el archivo, en 2 líneas.
2. Recorrido por las partes principales, de arriba hacia abajo.
3. Conceptos nuevos que aparecen, con una definición de una línea cada uno.
4. Una pregunta de autoevaluación con su respuesta.
No modifiques el archivo.
```

`.claude/settings.json`:

```json
{
  "permissions": {
    "deny": ["Read(./.env)", "Read(./.env.*)"]
  }
}
```

**Criterios de éxito:**
- [ ] `/explicar src/index.js` (o cualquier archivo) funciona y aparece al escribir `/`.
- [ ] Si le pedís a Claude que lea `.env`, lo rechaza por el permiso.
- [ ] El `CLAUDE.md` tiene menos de 60 líneas y solo información que Claude no puede inferir del código.
- [ ] Sabés explicar la diferencia entre `/clear` y `/compact`.

## 🧠 Autoevaluación

1. ¿Qué hace Plan mode y cuándo lo usás?
   <details><summary>Ver respuesta</summary>Claude investiga y propone un plan sin modificar nada. Se usa en tareas grandes o riesgosas antes de implementar.</details>

2. ¿Qué va en CLAUDE.md y qué no?
   <details><summary>Ver respuesta</summary>Va lo que Claude no puede inferir: comandos, convenciones, decisiones y trampas conocidas. No van documentos largos (se enlazan con `@ruta`) ni lo obvio.</details>

3. ¿Cuál es la diferencia entre una instrucción en CLAUDE.md y un hook?
   <details><summary>Ver respuesta</summary>La instrucción es una guía que el modelo puede no seguir; el hook es un comando que se ejecuta siempre.</details>

➡️ Siguiente: [Módulo 10 — Proyectos full‑stack con Claude Code](10-claude-code-proyectos.md)
