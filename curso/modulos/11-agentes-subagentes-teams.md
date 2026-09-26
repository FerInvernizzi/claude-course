# Módulo 11 — Agentes de IA, Subagentes y Agent Teams

> **🎯 Objetivos.** Al terminar este módulo vas a poder:
> - Explicar el bucle agéntico y los componentes de un agente.
> - Construir agentes con herramientas, memoria y salida estructurada (OpenAI Agents SDK y Claude Agent SDK).
> - Diseñar subagentes y equipos de agentes con el patrón de orquestación adecuado.
> - Llevar un equipo de agentes de la investigación al email con aprobación humana.
>
> **Requisitos previos:** Módulos 09 y 10 · Python básico · **Duración estimada:** 5 h

## 11.1 La revolución de los agentes

Pasamos de **modelos que responden** a **sistemas que actúan**. Tres ideas lo hicieron posible:

1. **Uso de herramientas (tool use):** el modelo decide llamar funciones (buscar, calcular, escribir archivos, enviar emails).
2. **Bucles de razonamiento:** el modelo observa el resultado de cada acción y decide el siguiente paso.
3. **Estándares de conexión (MCP):** conectar herramientas se volvió "enchufar y usar".

**Estado actual:** los agentes son muy buenos en tareas **acotadas, verificables y con herramientas claras** (código con tests, análisis de datos, investigación con fuentes, flujos de oficina). Todavía requieren **supervisión humana** en decisiones de alto impacto, acciones irreversibles y tareas con criterios de éxito ambiguos.

## 11.2 Agentes 101

> Un **agente** es un modelo de lenguaje que **usa herramientas en un bucle** para lograr un objetivo.

```text
┌──────────────────────────── BUCLE DEL AGENTE ────────────────────────────┐
│                                                                           │
│  Objetivo ─► [LLM] piensa ─► ¿necesito una herramienta?                   │
│                 ▲                 │ sí                    │ no            │
│                 │                 ▼                       ▼               │
│          resultado ◄── ejecutar herramienta        respuesta final        │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

**Componentes de un agente:**

| Componente | Qué es | Ejemplo |
|-----------|--------|---------|
| **Modelo** | El "cerebro" | Claude Sonnet / Opus |
| **Instrucciones** | Rol, objetivo, reglas | "Sos asesor financiero; nunca inventes cifras" |
| **Herramientas** | Lo que puede hacer | buscar web, leer Excel, enviar email |
| **Memoria** | Lo que recuerda | historial de sesión, archivos, base de datos |
| **Guardrails** | Límites y validaciones | no enviar sin aprobación, validar salida |
| **Orquestación** | Cómo se coordina con otros agentes | handoffs, subagentes, equipos |

**Workflow vs Agente:** un *workflow* sigue pasos predefinidos por código (predecible). Un *agente* decide los pasos en tiempo real (flexible). Regla práctica: **usá el sistema más simple que funcione**; empezá con un workflow y agregá autonomía solo donde aporta.

## 11.3 Recorrido de un agente en acción

Pedido a Claude Code: *"Encontrá por qué falla el test de login y arreglalo."*

1. **Piensa:** "Necesito ver el error" → herramienta `Bash(npm test)`.
2. **Observa:** `Expected 200, received 401`.
3. **Piensa:** "Reviso el middleware de auth" → `Grep("verifyToken")` → `Read(src/auth.ts)`.
4. **Observa:** el token se valida con la clave equivocada en tests.
5. **Actúa:** `Edit(src/auth.ts)`.
6. **Verifica:** `Bash(npm test)` → pasa.
7. **Responde:** explica causa y solución.

Cada paso es una vuelta del bucle. Esto es lo mismo que hace Cowork con tus archivos.

## 11.4 MCP 101 (desde la óptica del desarrollador)

Repaso del módulo 02: MCP estandariza cómo un agente descubre y usa herramientas externas. Como desarrollador podés:

- **Consumir** servidores MCP existentes (Gmail, Slack, Salesforce, GitHub, Postgres…).
- **Crear** tu propio servidor MCP para exponer tu API interna a cualquier agente compatible.

Servidor MCP mínimo en Python (SDK oficial `mcp`):

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("inventario")

@mcp.tool()
def stock(producto: str) -> int:
    """Devuelve el stock disponible de un producto."""
    return {"yerba": 120, "mate": 35}.get(producto.lower(), 0)

if __name__ == "__main__":
    mcp.run()   # stdio
```

```bash
claude mcp add inventario -- python servidor_inventario.py
```

## 11.5 Frameworks agénticos

| Framework | Fortaleza | Cuándo |
|-----------|-----------|--------|
| **Claude Agent SDK** (Python/TS) | El motor de Claude Code como librería: herramientas de archivos, shell, web, skills, MCP, subagentes, hooks, permisos | Agentes que trabajan con archivos/código/documentos; máxima capacidad "de fábrica" |
| **OpenAI Agents SDK** | Minimalista: Agent, Runner, tools, handoffs, guardrails, sessions, tracing. Multi‑proveedor vía LiteLLM | Aprender los conceptos; orquestación ligera |
| **LangGraph** | Grafos de estado explícitos, control fino | Workflows complejos con ramas y persistencia |
| **CrewAI** | Metáfora de "tripulación" con roles | Prototipos rápidos de equipos |
| **Anthropic API (tool use)** | Control total, sin framework | Casos a medida, producción |

El curso usa **OpenAI Agents SDK** para aprender los conceptos (es muy didáctico) y **Claude Agent SDK** para construir agentes con todo el poder de Claude Code.

> 💡 El OpenAI Agents SDK puede usar modelos de Claude: `pip install "openai-agents[litellm]"` y `model=LitellmModel(model="anthropic/claude-sonnet-5", api_key=...)` (importado de `agents.extensions.models.litellm_model`). Consultá la documentación vigente para el identificador exacto del modelo.

## 11.6 OpenAI Agents SDK 101

Cuatro primitivas:

| Primitiva | Qué es |
|-----------|--------|
| `Agent` | Modelo + instrucciones + herramientas (+ `output_type` para salida estructurada) |
| `Runner` | Ejecuta el bucle del agente (`run`, `run_sync`, `run_streamed`) |
| `@function_tool` | Convierte una función Python en herramienta (usa el docstring y los tipos) |
| `handoffs` / `as_tool` | Delegar en otro agente (transferir el control o usarlo como herramienta) |

Extras: **Sessions** (memoria), **Guardrails** (validación de entrada/salida), **Tracing** (ver cada paso).

### Definir y ejecutar un agente

Archivo: [`codigo/openai_agents/01_agente_basico.py`](../codigo/openai_agents/01_agente_basico.py)

```python
from agents import Agent, Runner, function_tool

@function_tool
def convertir_moneda(monto: float, tasa: float) -> float:
    """Convierte un monto multiplicándolo por la tasa de cambio indicada."""
    return round(monto * tasa, 2)

agente = Agent(
    name="Asistente financiero",
    instructions="Sos un asistente financiero. Usá convertir_moneda para conversiones.",
    tools=[convertir_moneda],
)

print(Runner.run_sync(agente, "¿Cuántos euros son 1.250 dólares a 0,92?").final_output)
```

```bash
cd curso/codigo
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # completá OPENAI_API_KEY
python openai_agents/01_agente_basico.py
```

## 11.7 Proyecto: agente de finanzas personales — visión general

Un asesor que registra gastos, consulta presupuestos y calcula ahorro. Lo construimos en dos versiones para entender **la memoria**:

| Versión | Memoria de conversación | Memoria de datos |
|---------|------------------------|------------------|
| Sin memoria (`02_...`) | ❌ cada turno empieza de cero | ❌ |
| Con memoria (`03_...`) | ✅ `SQLiteSession` | ✅ `gastos.json` vía herramientas |

### Sin memoria — recorrido del código

[`codigo/openai_agents/02_finanzas_sin_memoria.py`](../codigo/openai_agents/02_finanzas_sin_memoria.py): dos herramientas (`consultar_presupuesto`, `calcular_ahorro`). En el segundo turno ("¿cuánto llevo gastado?") el agente **no sabe** lo que dijiste antes: cada `Runner.run_sync` es independiente.

### Con memoria — recorrido del código

[`codigo/openai_agents/03_finanzas_con_memoria.py`](../codigo/openai_agents/03_finanzas_con_memoria.py):

```python
sesion = SQLiteSession("usuario_demo", "memoria_conversacion.db")
Runner.run_sync(asesor, "Hoy gasté $45.000 en comida", session=sesion)
Runner.run_sync(asesor, "¿Qué fue lo primero que te conté?", session=sesion)  # lo recuerda
```

- **Memoria de corto plazo** = historial de la sesión (se guarda en SQLite; sobrevive reinicios).
- **Memoria de largo plazo** = datos estructurados que el agente lee/escribe con herramientas (`registrar_gasto`, `total_por_categoria`).
- Lección: **los números nunca se "recuerdan" en el modelo; se guardan en un sistema y se consultan con herramientas.**

## 11.8 Automatizar la construcción de agentes con Claude Code

No hace falta escribir los agentes a mano: Claude Code puede construirlos, probarlos e iterarlos.

### Parte 1 — Especificación

Creá `SPEC.md`:

```markdown
# Agente: Asistente de viajes
- Objetivo: planificar viajes de fin de semana dentro de un presupuesto.
- Herramientas: buscar_vuelos (mock), buscar_hoteles (mock), clima (API pública), calcular_presupuesto.
- Memoria: preferencias del usuario en SQLiteSession.
- Salida estructurada: Itinerario (pydantic) con días, actividades, costo total.
- Guardrail: rechazar si el presupuesto es < 0 o el destino no existe.
- Tests: pytest con herramientas mockeadas.
```

### Parte 2 — Construcción

```text
Leé SPEC.md y la documentación del OpenAI Agents SDK. Implementá el agente en
agente_viajes/ con: tools.py, models.py, agent.py, main.py (CLI), tests/.
Usá Plan mode primero. Corré los tests al final.
```

### Parte 3 — Prueba e iteración

```text
Ejecutá main.py con 3 escenarios (presupuesto bajo, medio y alto) y mostrame las
trazas. Si el agente llama herramientas innecesarias o inventa datos, mejorá las
instrucciones y las descripciones de las herramientas, y repetí.
```

### Parte 4 — Refinar como producto

```text
Agregá: manejo de errores de red con reintentos, logging, un README con ejemplos, y una
versión equivalente con el Claude Agent SDK en agente_viajes_claude/. Compará ambas.
```

> El plugin **agent-sdk-dev** agrega `/new-sdk-app` para crear un proyecto del Claude Agent SDK con la estructura correcta y agentes verificadores.

## 11.9 Claude Agent SDK

[`codigo/claude_agent_sdk/01_agente_claude.py`](../codigo/claude_agent_sdk/01_agente_claude.py) — herramientas propias como servidor MCP en proceso:

```python
from claude_agent_sdk import ClaudeAgentOptions, create_sdk_mcp_server, query, tool

@tool("convertir_moneda", "Convierte un monto usando una tasa de cambio", {"monto": float, "tasa": float})
async def convertir_moneda(args):
    return {"content": [{"type": "text", "text": str(round(args["monto"] * args["tasa"], 2))}]}

servidor = create_sdk_mcp_server(name="finanzas", version="1.0.0", tools=[convertir_moneda])
opciones = ClaudeAgentOptions(
    mcp_servers={"finanzas": servidor},
    allowed_tools=["mcp__finanzas__convertir_moneda"],
)
async for mensaje in query(prompt="¿1.250 USD a 0,92 cuántos euros son?", options=opciones):
    ...
```

**Diferencia clave:** el Claude Agent SDK ya trae las herramientas de Claude Code (`Read`, `Write`, `Edit`, `Bash`, `Grep`, `WebSearch`, `WebFetch`, `Agent`…), skills, hooks, permisos y gestión de contexto automática.

---

## 11.10 Subagentes

Un **subagente** es un agente especializado al que el agente principal **delega una subtarea**. Características:

- Tiene **su propia ventana de contexto** (aislada): puede leer 50 archivos sin llenar el contexto del principal.
- Tiene **sus propias instrucciones, herramientas y modelo**.
- Devuelve **solo un resumen** del resultado.
- Pueden correr **en paralelo**.

```text
                    ┌──────────────────────┐
                    │  Agente principal    │  (contexto limpio: plan + resultados)
                    └───┬───────┬───────┬──┘
             delega     │       │       │     devuelven resúmenes
                 ┌──────▼─┐ ┌───▼────┐ ┌▼────────┐
                 │Explorer│ │Tester  │ │Reviewer │   (cada uno con su propio contexto)
                 └────────┘ └────────┘ └─────────┘
```

### Subagentes en Claude Code

Crealos pidiéndoselo a Claude (*"creá un subagente revisor de código para este proyecto"*) o escribiendo un archivo Markdown en `.claude/agents/<nombre>.md` (proyecto) o `~/.claude/agents/` (personal). En las versiones recientes, `/agents` solo te recuerda estas dos opciones:

```markdown
---
name: revisor-codigo
description: Revisor de código experto. Usar PROACTIVAMENTE después de escribir o modificar código.
tools: Read, Grep, Glob, Bash
model: sonnet
---

Sos un revisor de código senior. Al ser invocado:
1. Corré `git diff` para ver los cambios.
2. Revisá: bugs, seguridad (secretos, inyección), manejo de errores, legibilidad, tests.
3. Devolvé hallazgos por prioridad: 🔴 crítico, 🟡 advertencia, 🟢 sugerencia,
   cada uno con archivo:línea y cómo arreglarlo.
```

Más ejemplos en [`plantillas/agents/`](../plantillas/agents/).

**Invocación:** automática (Claude decide según la `description`) o explícita: *"Usá el subagente revisor-codigo para revisar mis cambios"*. Paralelismo: *"Lanzá 3 subagentes en paralelo: uno investiga el frontend, otro la API y otro la base de datos."*

### Subagentes en el Claude Agent SDK

[`codigo/claude_agent_sdk/02_equipo_subagentes.py`](../codigo/claude_agent_sdk/02_equipo_subagentes.py):

```python
subagentes = {
    "investigador": AgentDefinition(
        description="Investiga un tema en la web y devuelve hallazgos con fuentes.",
        prompt="Sos investigador de mercado...",
        tools=["WebSearch", "WebFetch"],
        model="sonnet",
    ),
    "analista": AgentDefinition(...),
    "redactor": AgentDefinition(..., tools=["Write", "Read"]),
}
opciones = ClaudeAgentOptions(agents=subagentes, allowed_tools=["Agent", ...])
```

### Cuándo usar subagentes

✅ Exploración/búsqueda amplia, tareas paralelizables, revisiones independientes (un revisor que no "vio" cómo se escribió el código es más objetivo), tareas que generan mucho ruido.
❌ Tareas pequeñas, tareas que requieren todo el contexto de la conversación, pasos muy acoplados.

## 11.11 Agent Teams (equipos de agentes)

Un **equipo de agentes** va un paso más allá: varios agentes **colaboran como compañeros**, con roles, una lista de tareas compartida y **comunicación directa entre ellos**, coordinados por un líder.

| | Subagentes | Agent Team |
|---|---|---|
| Relación | Jefe → ayudante (jerárquica) | Líder + compañeros (colaborativa) |
| Comunicación | Solo devuelven el resultado al principal | Se mandan mensajes entre sí |
| Duración | Una subtarea y terminan | Sesiones largas; toman varias tareas |
| Coordinación | El principal decide todo | Lista de tareas compartida; se autoasignan |
| Ideal para | Delegar trabajo aislado | Proyectos grandes con partes interdependientes |

### Agent Teams en Claude Code (función experimental)

Claude Code incluye equipos de agentes como **función experimental**. Se habilita con una variable de entorno (verificá el nombre vigente en la documentación oficial):

```json
// .claude/settings.json o ~/.claude/settings.json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```

Luego:

```text
Armá un equipo de 3 agentes para construir la funcionalidad de reservas:
- "backend": API REST y base de datos.
- "frontend": pantallas de reserva y confirmación.
- "qa": escribe tests end-to-end y reporta bugs a los otros dos.
Coordiná con una lista de tareas compartida. Cada agente trabaja solo en su carpeta.
```

**Buenas prácticas:** dividir el trabajo por **áreas de archivos** que no se pisen; definir contratos (ej.: el formato de la API) antes de empezar; tener un rol de **QA/revisor**; vigilar el consumo (varios agentes = varias ventanas de contexto = más uso).

### Patrones de orquestación

| Patrón | Descripción | Ejemplo |
|--------|-------------|---------|
| **Secuencial (pipeline)** | A → B → C | Investigar → analizar → redactar → enviar |
| **Paralelo (fan‑out/fan‑in)** | Varios a la vez, luego se combinan | 5 subagentes investigan 5 competidores |
| **Orquestador‑trabajadores** | Un director reparte y sintetiza | Director de proyecto + especialistas |
| **Evaluador‑optimizador** | Uno produce, otro critica, se itera | Redactor + editor hasta nota ≥ 8 |
| **Handoff** | Un agente transfiere la conversación a otro | Triage → soporte técnico o facturación |

## 11.12 Proyecto: equipo de agentes de punta a punta (investigación → email)

**Objetivo:** dado un tema, el equipo investiga en la web, analiza, redacta un informe ejecutivo y prepara el email de distribución.

### Parte 1 — Diseño del equipo

```text
Director de proyecto (orquestador)
  ├── Investigador  → WebSearch; salida estructurada (Hallazgos: tema, hallazgos[], fuentes[])
  ├── Analista      → insights, riesgos, oportunidades, recomendaciones
  ├── Redactor      → informe.md (máx. 600 palabras) con guardar_informe
  └── Comunicador   → email (máx. 150 palabras) con guardar_borrador_email
```

### Parte 2 — Agentes como herramientas (patrón manager)

[`codigo/openai_agents/04_equipo_agentes.py`](../codigo/openai_agents/04_equipo_agentes.py):

```python
director = Agent(
    name="Director de proyecto",
    instructions="Orden: 1) investigar 2) analizar 3) redactar_informe 4) preparar_email ...",
    tools=[
        investigador.as_tool("investigar", "Investiga un tema en la web..."),
        analista.as_tool("analizar", "Convierte hallazgos en insights..."),
        redactor.as_tool("redactar_informe", "Escribe y guarda el informe..."),
        comunicador.as_tool("preparar_email", "Redacta y guarda el borrador..."),
    ],
)
```

`as_tool` mantiene al director **en control** (recibe cada resultado y decide). La alternativa, `handoffs=[...]`, **transfiere** la conversación al otro agente (útil para triage/atención al cliente).

### Parte 3 — Salida estructurada y trazas

- `output_type=Hallazgos` obliga al investigador a devolver un objeto validado (pydantic): menos alucinaciones de formato.
- `with trace("Equipo de research"):` registra cada paso; lo ves en el panel de trazas de OpenAI para depurar.

### Parte 4 — Del borrador al envío real

El ejemplo **guarda un borrador**, a propósito. Para enviar de verdad:

1. Reemplazá `guardar_borrador_email` por una herramienta que use la Gmail API, un servicio como SendGrid/Resend, o un servidor MCP de Gmail.
2. Agregá **aprobación humana** (human‑in‑the‑loop): el agente propone, vos aprobás.
3. Agregá un **guardrail** que valide destinatarios contra una lista permitida.

### Parte 5 — Versión con Claude Agent SDK y ejecución

```bash
python openai_agents/04_equipo_agentes.py "mercado de apps de delivery en Uruguay"
python claude_agent_sdk/02_equipo_subagentes.py "adopción de billeteras digitales en Uruguay"
```

Ambos generan `salida/informe.md` y `salida/borrador_email.txt`. Compará calidad, costo y tiempo.

## 🧪 Práctica

Agregá al equipo un **Editor** (patrón evaluador‑optimizador) que puntúe el informe del 1 al 10 en claridad, evidencia y accionabilidad, y lo devuelva al redactor hasta que todas las notas sean ≥ 8 (máximo 3 rondas).

### ✅ Solución (OpenAI Agents SDK)

```python
from pydantic import BaseModel

class Evaluacion(BaseModel):
    claridad: int
    evidencia: int
    accionabilidad: int
    comentarios: list[str]

editor = Agent(
    name="Editor",
    instructions="Puntuá el informe del 1 al 10 en claridad, evidencia y accionabilidad. "
                 "Sé exigente y dá comentarios concretos para mejorar.",
    output_type=Evaluacion,
)

# En el director, agregá la herramienta y la regla:
#   editor.as_tool("evaluar_informe", "Evalúa el informe y devuelve notas y comentarios")
# Instrucción extra: "Después de redactar, llamá a evaluar_informe. Si alguna nota es < 8,
# pedile al redactor que corrija usando los comentarios. Máximo 3 rondas."
```

## 🧠 Autoevaluación

1. ¿Cuál es la ventaja principal de un subagente?
   <details><summary>Ver respuesta</summary>Trabaja en su propia ventana de contexto y devuelve solo el resultado: el agente principal no se llena de ruido.</details>

2. ¿Qué diferencia hay entre `as_tool` y `handoffs` en el OpenAI Agents SDK?
   <details><summary>Ver respuesta</summary>Con `as_tool` el orquestador mantiene el control y recibe el resultado; con un handoff transfiere la conversación al otro agente.</details>

3. ¿Dónde se guardan los datos que el agente tiene que "recordar" con exactitud?
   <details><summary>Ver respuesta</summary>En un sistema externo (archivo o base de datos) al que accede con herramientas, no en la memoria del modelo.</details>

➡️ Siguiente: [Módulo 12 — Tu agente personal](12-agente-personal.md)
