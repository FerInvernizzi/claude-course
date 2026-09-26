# Módulo 14 — Funciones avanzadas que nadie te cuenta

<img src="../assets/linea.svg" alt="" width="100%">

Este módulo reúne lo que **no vas a descubrir usando Claude "de oído"**: atajos, comandos y configuraciones que están en la documentación oficial pero casi nadie usa. Todo fue verificado contra la documentación de Anthropic (septiembre de 2026) y, cuando fue posible, contra la CLI instalada. Las funciones marcadas *(vista previa)* o *(experimental)* pueden cambiar.

## 🎯 Objetivos de aprendizaje

| # | Al terminar vas a poder… (conducta · condición · criterio) | Nivel (Bloom) | Evidencia |
|---|---|---|---|
| 14.1 | **Recuperar** una sesión de Claude Code que se desvió, usando `/rewind` (resumir desde un punto), `/btw` y `/branch`, sin perder el código correcto y sin volver a empezar | Aplicar · procedimental | Práctica A |
| 14.2 | **Configurar** la memoria de un proyecto con `CLAUDE.md` de menos de 200 líneas, `@imports` y al menos una regla en `.claude/rules/` limitada por rutas, y **comprobar** con `/context` y `/memory` qué se carga | Aplicar · procedimental | Práctica A |
| 14.3 | **Automatizar** una tarea hasta un criterio verificable con `/goal` y **justificar** cuándo usar `/goal`, `/loop`, Ralph Loop o una rutina | Evaluar · metacognitivo | Práctica B y autoevaluación |
| 14.4 | **Escribir** una skill avanzada que use al menos tres campos de frontmatter (`disable-model-invocation`, `context: fork`, `allowed-tools`, `paths`, `arguments`) e inyección de contexto con `` !`comando` `` | Crear · procedimental | Práctica C |
| 14.5 | **Paralelizar** trabajo con el mecanismo adecuado (subagente, `/subtask`, worktree, `/batch`, workflow o agent team), según el aislamiento y la coordinación que necesite la tarea | Analizar · conceptual | Autoevaluación |
| 14.6 | **Configurar**, para tu trabajo real, instrucciones persistentes en Cowork (globales y de carpeta) y en los complementos de Excel y PowerPoint, de modo que el resultado respete tus preferencias sin repetirlas en el prompt | Aplicar · procedimental | Práctica D |
| 14.7 | **Elegir**, dado un escenario de tarea, el modo de permiso de Cowork (Manual, Auto o Skip) o de Claude Code, justificando al menos un riesgo que el modo mitiga | Evaluar · conceptual | Práctica D |

**Requisitos previos:** módulos 01, 06, 08, 09 y 11 · **Duración estimada:** 3 h

### 🗺️ Ruta de estudio y base de cada sección

| Sesión | Secciones | Se apoya en | Resultado |
|---|---|---|---|
| 1 · 60 min | 14.1 a 14.3 | Módulos 05 (contexto) y 09 (CLAUDE.md) | Práctica A |
| 2 · 60 min | 14.4 a 14.6 | Módulos 09 (comandos) y 10 (Ralph Loop) | Prácticas B y C |
| 3 · 45 min | 14.7 a 14.11 | Módulo 11 (subagentes) | Autoevaluación |
| 4 · 30 min | 14.12 | Módulos 01, 06 y 08 | Práctica D |

No hace falta usar todo: elegí 3 funciones que resuelvan un problema que ya tuviste y practicalas primero.


---

## 14.1 Claude Code: sesiones que no se arruinan

| Función | Qué hace | Cuándo te salva |
|---------|----------|-----------------|
| `Esc` | Interrumpe a Claude y conserva el contexto | Ves que va por mal camino: frenás y redirigís |
| `Esc Esc` o `/rewind` (alias `/undo`, `/checkpoint`) | Menú para restaurar **conversación, código o ambos** a cualquier mensaje anterior | Una idea no funcionó: volvés atrás en segundos |
| `/rewind` → **Resumir desde aquí** / **Resumir hasta aquí** | Compacta **solo una parte** de la conversación | Querés liberar contexto sin perder lo reciente (o lo antiguo) |
| `/btw <pregunta>` | Pregunta al margen: la respuesta **nunca entra al historial** | Dudás de un nombre de archivo o una decisión anterior y no querés ensuciar el contexto |
| `/branch [nombre]` | Crea una rama de la **conversación** para probar otra dirección | Querés comparar dos enfoques sin perder el actual |
| `/compact <foco>` | Resume con un foco (ej.: `/compact conservá la lista de archivos modificados`) | La tarea sigue pero el historial es largo |
| `/clear [nombre]` | Contexto nuevo; el nombre la deja fácil de encontrar en `/resume` | Cambiás de tarea |
| `claude -c` / `claude -r` | Continuar la última conversación / elegir una | Cerraste la terminal por error |
| `claude -n "nombre"` o `/rename` | Pone nombre a la sesión | Tenés muchas sesiones abiertas |

**Regla de oro oficial:** si corregiste a Claude **más de dos veces** sobre lo mismo, el contexto está lleno de intentos fallidos. Hacé `/clear` y empezá con un prompt mejor que incorpore lo aprendido: una sesión limpia casi siempre supera a una larga llena de correcciones.

**Checkpoints:** cada mensaje tuyo crea un punto de restauración, y sobreviven aunque cierres la terminal. Limitación: **solo registran los cambios hechos con las herramientas de edición de Claude**, no los de comandos Bash ni los de procesos externos. No reemplazan a git.

## 14.2 Memoria: lo que Claude recuerda y cómo controlarlo

1. **`CLAUDE.md` de menos de 200 líneas.** Se carga completo en **cada** mensaje. Si crece, mové material de referencia a skills o a `.claude/rules/`.
2. **Imports:** `@docs/arquitectura.md` dentro de `CLAUDE.md` incluye ese archivo, con hasta 4 niveles de imports anidados. Para mencionar una ruta **sin** importarla, escribila entre backticks: `` `@README` ``.
3. **`CLAUDE.local.md`:** preferencias personales del proyecto; agregalo al `.gitignore`.
4. **`.claude/rules/`:** reglas modulares, un tema por archivo (`testing.md`, `seguridad.md`). Con `paths:` en el frontmatter, una regla se carga **solo** cuando Claude trabaja con archivos que coinciden:

   ```markdown
   ---
   paths: ["src/api/**/*.ts"]
   ---
   Toda ruta de API valida la entrada con Zod y devuelve errores con { error, code }.
   ```

5. **Memoria automática:** Claude guarda aprendizajes entre sesiones sin que escribas nada ("Saved 2 memories"). Se carga el índice `MEMORY.md` (primeras 200 líneas o 25 KB) y los archivos de tema se leen a demanda. La revisás, editás o desactivás desde `/memory`.
6. **`AGENTS.md`:** si tu repo ya tiene instrucciones para otros agentes de código, Claude Code puede leerlas también.
7. **Instrucción para la compactación:** agregá a `CLAUDE.md` algo como *"Al compactar, conservá siempre la lista de archivos modificados y los comandos de test"*, así lo crítico sobrevive al resumen automático.
8. **`/context`** muestra una grilla de qué ocupa la ventana, con sugerencias para liberarla.

## 14.3 Verificación: que Claude se corrija solo

> *"Dale a Claude una forma de verificar su trabajo. Es la diferencia entre una sesión que vigilás y una de la que te podés ir."* — Guía oficial de buenas prácticas.

- En cada pedido, incluí **el chequeo**: tests, código de salida del build, un linter, un script que compare contra un resultado esperado o una captura de pantalla contra un diseño.
- **`/verify`** construye y **ejecuta tu app** para confirmar que el cambio hace lo que debe, sin quedarse solo con tests o chequeos de tipos. **`/run`** la lanza y la maneja. **`/run-skill-generator`** les enseña a ambos cómo levantar tu proyecto.
- **Patrón Escritor/Revisor:** una sesión escribe y **otra sesión nueva** revisa. El contexto limpio evita el sesgo hacia el código recién escrito.
- Revisión de código integrada: `/code-review` y `/review` (con niveles `low` a `max`), `/simplify` (cuatro agentes en paralelo buscan reutilización, simplificación y eficiencia), `/security-review` (vulnerabilidades del diff) y `/ultrareview` (revisión profunda multiagente en la nube).

## 14.4 Autonomía con criterio: `/goal`, `/loop` y rutinas

| Mecanismo | Qué hace | Dónde corre | Usalo para |
|-----------|----------|-------------|-----------|
| **`/goal <condición>`** | Trabaja turno tras turno hasta que un evaluador confirma que se cumple la condición | Tu sesión | "Todos los tests de `test/auth` pasan y el lint está limpio" |
| **Ralph Loop** (plugin) | Repite el mismo prompt hasta una "promesa" de finalización | Tu sesión | Iteración larga guiada por un archivo de tareas (módulo 10) |
| **`/loop [intervalo] [prompt]`** | Repite un prompt mientras la sesión está abierta | Tu sesión | Sondear algo cada 5 minutos |
| **Rutinas** (`/schedule`) *(vista previa)* | Prompt + repos + conectores que corren por horario, por llamada a una API o por eventos de GitHub | Nube de Anthropic | Revisión nocturna de PRs, informe semanal. Funciona con la laptop cerrada |
| **Tareas programadas de Desktop** | Como las rutinas, pero en tu máquina | Tu computadora | Tareas que necesitan archivos locales |

**Cómo escribir una buena condición de `/goal`:** un estado final medible ("`npm test` sale con 0"), cómo probarlo y las restricciones ("sin modificar otros archivos de test"). Acotala con `o parar después de 20 turnos`. El evaluador **no ejecuta comandos**: juzga lo que Claude muestra en la conversación. Para que corra sin pedirte permisos, usalo en modo **auto**.

## 14.5 Modos de permiso (los 6)

| Modo | Qué corre sin preguntar | Ideal para |
|------|-------------------------|------------|
| `default` (**Manual**) | Solo lecturas | Trabajo sensible |
| `acceptEdits` | Lecturas, ediciones y comandos comunes de archivos (`mkdir`, `mv`, `cp`) | Iterar sobre código que revisás |
| `plan` | Lecturas (y comandos aprobados por el clasificador si hay modo auto) | Explorar antes de cambiar |
| `auto` | Todo, con **controles de seguridad en segundo plano** | Tareas largas sin "fatiga de permisos" |
| `dontAsk` | Lecturas y herramientas preaprobadas; lo demás se rechaza | CI y scripts bloqueados |
| `bypassPermissions` | Todo | **Solo** contenedores o VMs aislados |

Se alternan con `Shift+Tab` (o `/plan <tarea>` para entrar directo a Plan mode). `/fewer-permission-prompts` analiza tus sesiones y propone una lista de comandos de solo lectura para permitir, y `/auto-mode-setup` prepara la configuración del modo auto.

## 14.6 Skills avanzadas: los campos que casi nadie usa

```markdown
---
name: resumen-pr
description: Resume un pull request con sus cambios y riesgos
disable-model-invocation: true     # solo se ejecuta si escribís /resumen-pr
context: fork                      # corre en un subagente: no ensucia tu contexto
agent: Explore                     # tipo de subagente (de solo lectura)
allowed-tools: Bash(gh *)          # sin pedir permiso durante ese turno
arguments: [numero]                # $numero = primer argumento
---
## Diff
!`gh pr diff $numero`

## Comentarios
!`gh pr view $numero --comments`

Resumí qué cambia, los riesgos y qué revisaría primero.
```

| Campo | Para qué |
|-------|----------|
| `disable-model-invocation: true` | Solo la invocás vos con `/nombre` (flujos con efectos: deploy, envío) |
| `user-invocable: false` | Solo la usa Claude; no aparece en el menú `/` (conocimiento de fondo) |
| `context: fork` + `agent` | Corre en un subagente aislado |
| `allowed-tools` / `disallowed-tools` | Permite o prohíbe herramientas durante la skill |
| `paths` | Se activa sola solo con ciertos archivos |
| `model` / `effort` | Modelo y nivel de esfuerzo propios mientras corre |
| `arguments`, `$ARGUMENTS`, `$0`, `$1` | Argumentos; **`$0` es el primero** |
| `` !`comando` `` | Ejecuta el comando **antes** de enviar la skill y pega su salida |
| `when_to_use` | Frases disparadoras extra (cuentan en el límite de 1.536 caracteres de la descripción) |

`/skills` lista tus skills; con `t` las ordenás por tokens. `/reload-skills` recarga las que editaste sin reiniciar.

## 14.7 Trabajo en paralelo: elegir el mecanismo

| Necesitás… | Usá |
|------------|-----|
| Investigar mucho sin llenar tu contexto | **Subagente** (`@"nombre (agent)"` para forzar uno específico) |
| Una tarea lateral que necesita **todo** el contexto actual | **`/subtask <tarea>`**: un fork en segundo plano que hereda la conversación |
| Varias sesiones completas editando el mismo repo sin pisarse | **`claude -w nombre`** (worktree aislado por sesión) |
| Ver y despachar muchas sesiones en segundo plano | **`claude agents`** (agent view) y **`/background`** para desacoplar la sesión actual |
| Un cambio grande en 5 a 30 partes independientes | **`/batch <instrucción>`** |
| Orquestar muchos subagentes con un script que podés reusar | **Workflows dinámicos**, por ejemplo **`/deep-research <pregunta>`** (búsquedas en paralelo con fuentes cruzadas) |
| Compañeros que se coordinan y se mandan mensajes | **Agent teams** *(experimental)* |

Subagentes con **memoria persistente**: agregá `memory: project` (o `user`/`local`) en su frontmatter y el subagente acumula aprendizajes entre conversaciones.

## 14.8 Personalizar cómo te responde

- **Estilos de salida** (`/output-style`): **Concise** (va al resultado), **Explanatory** (agrega bloques *Insight* que explican las decisiones), **Learning** (explica y **te deja partes de código para que escribas vos**, ideal para aprender), **Proactive** (asume decisiones rutinarias sin preguntar).
- **Entrevista antes de construir:** *"Quiero construir [X]. Entrevistame en detalle con la herramienta AskUserQuestion sobre implementación, UX, casos borde y tradeoffs. Después escribí la especificación completa en SPEC.md."* Luego abrí una sesión nueva para implementarla.
- **Advisor** *(experimental)*: `/advisor` empareja tu modelo con uno más fuerte al que Claude consulta en momentos clave (antes de elegir un enfoque o de declarar algo terminado).
- **`/effort`** y **modo rápido** (`/fast`, `Option/Alt+O`): más razonamiento o más velocidad según la tarea.

## 14.9 Atajos de teclado que ahorran horas

| Atajo | Acción |
|-------|--------|
| `?` | Panel de atajos |
| `Ctrl+G` | Escribir el prompt en tu editor de texto (prompts largos) |
| `Ctrl+S` | Guardar el prompt a medio escribir y recuperarlo después |
| `Ctrl+V` (`Cmd+V` en iTerm2) | Pegar una **imagen** (captura de un error, un diseño) |
| `Ctrl+B` | Mandar tareas en ejecución a segundo plano |
| `Ctrl+T` | Mostrar u ocultar la lista de tareas de Claude |
| `Ctrl+O` | Ver la transcripción completa |
| `Ctrl+R` | Buscar en el historial de prompts |
| `Option/Alt+P` | Cambiar de modelo |
| `Option/Alt+T` | Activar o desactivar el pensamiento extendido |
| `Shift+Tab` | Alternar modos de permiso |

## 14.10 Trabajar desde cualquier lugar

- **`/remote-control`**: continuás la sesión local desde el celular o el navegador.
- **`claude --cloud "tarea"`**: arranca una sesión en la nube; **`/teleport`** (o `claude --teleport`) la trae a tu terminal.
- **`/desktop`**: pasa la sesión de la terminal a la app de escritorio para revisar diffs visualmente.
- **Canales** *(vista previa)*: Telegram, Discord o iMessage empujan mensajes a tu sesión abierta.
- **`claude -p "prompt" --output-format json`**: modo no interactivo para scripts, CI y hooks de git (`stream-json` para streaming).

## 14.11 Aprender y medir tu propio uso

- **`/powerup`**: lecciones interactivas con demos animadas de funciones de Claude Code.
- **`/insights`**: informe HTML de tus sesiones: en qué proyectos trabajás, dónde fallan las cosas y funciones para probar.
- **`/usage`** (alias `/cost`, `/stats`): costo de la sesión, límites del plan y estadísticas.
- **`/skill-doctor`**: cuánto contexto consume cada skill y cuánto se usa, para detectar las que conviene apagar.
- **`/team-onboarding`**: genera una guía de onboarding para tu equipo a partir de tu uso real.

## 14.12 Cowork y Office: lo que no está a la vista

**Cowork**
- **Instrucciones globales** (tono, formato y rol para todas las tareas) e **instrucciones de carpeta** (contexto de cada carpeta; Claude las puede actualizar solo).
- **Modos:** Manual, Auto (con revisión de seguridad automática y algo más de consumo) y Skip.
- **`/schedule` después de hacer la tarea una vez:** convierte *ese* proceso probado en recurrente.
- Las tareas que no dependen de tu computadora siguen aunque cierres la laptop; las que usan carpetas locales y **Dispatch** necesitan la computadora despierta. Dispatch divide tu pedido en tareas hijas (hacia Code o hacia un proyecto de Cowork), y si no respondés un pedido de permiso en 10 minutos, se deniega.
- **Proyectos de Cowork:** carpetas, instrucciones, links, memoria propia y proyectos de claude.ai vinculados; viven solo en tu computadora.
- Nunca borra archivos permanentemente sin pedirte permiso explícito.

**Claude en Excel y PowerPoint**
- Campo **Instrucciones** en la configuración de cada complemento (separado por app): tus convenciones de formato o de marca para siempre.
- **Citas a nivel de celda** en las respuestas de Excel; clic para navegar.
- **Contexto compartido** entre Excel, PowerPoint, Word y Outlook en una misma conversación.
- En PowerPoint: **seleccioná una slide** y pedí el cambio; edita solo esa, respetando el patrón.
- Límites de Excel: sin *Tablas de datos* ni macros/VBA.
- Usalos **solo con archivos confiables**: un archivo externo puede traer instrucciones ocultas (inyección de prompts).

---

## 🧪 Prácticas

### A. Sesión a prueba de errores (objetivos 14.1 y 14.2)

1. En un proyecto con git, pedile a Claude un cambio chico y después uno que **no te guste**.
2. Volvé atrás con `Esc Esc` restaurando **solo el código**.
3. Preguntá con `/btw` algo sobre un archivo que Claude ya leyó y comprobá con `/context` que no creció el historial.
4. Creá `.claude/rules/tests.md` con `paths` limitado a `tests/**` y verificá con `/memory` que existe.

**Criterios de éxito:** el código volvió exactamente al estado anterior (`git diff` lo confirma); la respuesta de `/btw` no aparece en la conversación; `CLAUDE.md` tiene menos de 200 líneas.

### B. `/goal` con criterio verificable (objetivo 14.3)

```text
/goal todos los tests de la carpeta tests/ pasan con `npm test` (código de salida 0),
el lint no reporta errores y no se modificó ningún archivo dentro de tests/.
Parar después de 15 turnos.
```

**Criterios de éxito:** la condición tiene un estado final medible, un chequeo explícito, una restricción y un límite. Podés explicar por qué el evaluador necesita ver la salida de `npm test` en la conversación.

### C. Skill avanzada (objetivo 14.4)

Creá `/estado-repo`: una skill con `disable-model-invocation: true`, `context: fork` y `allowed-tools: Bash(git *)` que inyecte `` !`git log --oneline -10` `` y `` !`git status --short` `` y resuma el estado del repositorio en 5 bullets.

**Criterios de éxito:** aparece en `/skills`; no se ejecuta sola; al invocarla, tu conversación principal recibe solo el resumen.

### D. Instrucciones persistentes (objetivo 14.6)

Escribí instrucciones globales de Cowork y las instrucciones del complemento de Excel para tu trabajo real (idioma, formato de números, estilo de salida). Hacé la misma tarea antes y después y compará.

**Criterios de éxito:** sin repetir tus preferencias en el prompt, el resultado ya las respeta; elegiste y justificaste el modo de permiso de la tarea.

## 📌 Ideas clave

- `/rewind`, `/btw` y `/branch` evitan arruinar una sesión larga.
- `CLAUDE.md` < 200 líneas; reglas por ruta en `.claude/rules/`; memoria automática controlable.
- Dale a Claude una forma de verificar su trabajo (tests, `/verify`).
- `/goal` con condición medible; modo auto para correr sin interrupciones.
- Elegí el mecanismo de paralelismo según el aislamiento y la coordinación que necesitás.

## 🧠 Autoevaluación

1. Tenés que migrar 200 archivos al mismo patrón nuevo, y cada archivo se puede cambiar sin mirar los demás. ¿Qué mecanismo usás?
   <details><summary>Ver respuesta</summary><code>/batch</code>: divide el trabajo en unidades independientes y las ejecuta en paralelo. Si querés un script reutilizable y auditable, un workflow dinámico.</details>

2. ¿Qué diferencia hay entre un subagente común y `/subtask`?
   <details><summary>Ver respuesta</summary>El subagente común arranca con contexto limpio (hay que explicarle la tarea). <code>/subtask</code> crea un fork que hereda toda la conversación; igual que un subagente, solo devuelve el resultado final a tu sesión.</details>

3. ¿Por qué `/goal` necesita una condición que se pueda "ver" en la conversación?
   <details><summary>Ver respuesta</summary>Porque el evaluador no ejecuta comandos ni lee archivos: juzga a partir de lo que Claude mostró, como la salida de los tests.</details>

4. Querés que una skill de deploy nunca se ejecute sola. ¿Qué campo usás?
   <details><summary>Ver respuesta</summary><code>disable-model-invocation: true</code>.</details>

5. ¿Qué estilo de salida elegís si tu objetivo es aprender a programar mientras Claude trabaja?
   <details><summary>Ver respuesta</summary><strong>Learning</strong>: explica sus decisiones y te deja partes del código para que las escribas vos.</details>

## Fuentes

- [Claude Code — documentación oficial (índice)](https://code.claude.com/docs/en/overview) · [Buenas prácticas](https://code.claude.com/docs/en/best-practices) · [Comandos](https://code.claude.com/docs/en/commands) · [Modo interactivo y atajos](https://code.claude.com/docs/en/interactive-mode) · [Memoria](https://code.claude.com/docs/en/memory) · [Skills](https://code.claude.com/docs/en/skills) · [Subagentes](https://code.claude.com/docs/en/sub-agents) · [Checkpointing](https://code.claude.com/docs/en/checkpointing) · [/goal](https://code.claude.com/docs/en/goal) · [Modos de permiso](https://code.claude.com/docs/en/permission-modes) · [Workflows](https://code.claude.com/docs/en/workflows) · [Worktrees](https://code.claude.com/docs/en/worktrees) · [Rutinas](https://code.claude.com/docs/en/routines) · [Estilos de salida](https://code.claude.com/docs/en/output-styles) · [Advisor](https://code.claude.com/docs/en/advisor) · [Canales](https://code.claude.com/docs/en/channels)
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) · [Schedule recurring tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) · [Assign tasks from anywhere (Dispatch)](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
- [Use Claude for Excel](https://claude.com/docs/office-agents/excel) · [Use Claude for PowerPoint](https://claude.com/docs/office-agents/powerpoint)

➡️ Siguiente: [Módulo 15 — Skills de nicho: arte, diseño y pasiones](15-skills-de-nicho.md)
