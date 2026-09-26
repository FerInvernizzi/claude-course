"""Módulo 11.9 — El mismo concepto con el Claude Agent SDK.

El Claude Agent SDK expone el "motor" de Claude Code como librería: el agente
ya trae herramientas para leer/escribir archivos, ejecutar comandos, buscar en
la web, usar skills, MCP y subagentes.

Requisitos: Claude Code instalado (`claude --version`) y sesión iniciada o
ANTHROPIC_API_KEY definida.

Ejecutar:
    python 01_agente_claude.py
"""

import asyncio

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    create_sdk_mcp_server,
    query,
    tool,
)


@tool("convertir_moneda", "Convierte un monto usando una tasa de cambio", {"monto": float, "tasa": float})
async def convertir_moneda(args: dict) -> dict:
    total = round(args["monto"] * args["tasa"], 2)
    return {"content": [{"type": "text", "text": f"{total}"}]}


# Las herramientas propias se exponen como un servidor MCP en el mismo proceso.
servidor = create_sdk_mcp_server(name="finanzas", version="1.0.0", tools=[convertir_moneda])


async def main() -> None:
    opciones = ClaudeAgentOptions(
        system_prompt="Sos un asistente financiero. Respondé en español y usá las herramientas para calcular.",
        mcp_servers={"finanzas": servidor},
        allowed_tools=["mcp__finanzas__convertir_moneda"],
        max_turns=5,
    )
    async for mensaje in query(
        prompt="Tengo 1.250 dólares. ¿Cuántos euros son si la tasa es 0,92?", options=opciones
    ):
        if isinstance(mensaje, AssistantMessage):
            for bloque in mensaje.content:
                if isinstance(bloque, TextBlock):
                    print(bloque.text)
        elif isinstance(mensaje, ResultMessage):
            print(f"\n[fin — turnos: {mensaje.num_turns}]")


if __name__ == "__main__":
    asyncio.run(main())
