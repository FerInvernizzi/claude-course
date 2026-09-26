# Código del módulo 11: agentes de IA

| Archivo | Sección | Qué muestra |
|---------|---------|-------------|
| `openai_agents/01_agente_basico.py` | 11.6 | Agent + Runner + `@function_tool` |
| `openai_agents/02_finanzas_sin_memoria.py` | 11.7 | Agente sin memoria (olvida entre turnos) |
| `openai_agents/03_finanzas_con_memoria.py` | 11.7 | `SQLiteSession` + memoria de datos en JSON |
| `openai_agents/04_equipo_agentes.py` | 11.12 | Equipo de agentes: investigar → analizar → redactar → email |
| `mcp/servidor_inventario.py` | 11.4 | Servidor MCP mínimo con el SDK oficial `mcp` 2.x (probado con un cliente MCP) |
| `claude_agent_sdk/01_agente_claude.py` | 11.9 | Herramienta propia como servidor MCP en proceso |
| `claude_agent_sdk/02_equipo_subagentes.py` | 11.10–11.12 | Orquestador + subagentes (`AgentDefinition`) |

## Instalación

```bash
cd curso/codigo
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # completá tus claves
```

- Los ejemplos de **OpenAI Agents SDK** necesitan `OPENAI_API_KEY`.
- Los ejemplos de **Claude Agent SDK** necesitan Claude Code instalado (`claude --version`) y una sesión iniciada (`claude` y login) o `ANTHROPIC_API_KEY`.

## Ejecutar

```bash
python openai_agents/01_agente_basico.py
python openai_agents/03_finanzas_con_memoria.py
python openai_agents/04_equipo_agentes.py "tu tema"
python claude_agent_sdk/01_agente_claude.py
python claude_agent_sdk/02_equipo_subagentes.py "tu tema"
```

Los resultados del equipo de agentes quedan en `salida/` (ignorado por git).
