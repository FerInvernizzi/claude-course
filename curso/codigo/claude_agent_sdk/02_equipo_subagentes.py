"""Módulo 11.11 — Equipo de agentes con subagentes del Claude Agent SDK.

El agente principal (orquestador) delega en subagentes especializados. Cada
subagente trabaja en su PROPIA ventana de contexto y devuelve solo el resultado,
lo que mantiene limpio el contexto del orquestador.

Ejecutar:
    python 02_equipo_subagentes.py "mercado de apps de delivery en Uruguay"
Los archivos quedan en ./salida
"""

import asyncio
import sys
from pathlib import Path

from claude_agent_sdk import (
    AgentDefinition,
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    query,
)

SALIDA = Path(__file__).with_name("salida")
SALIDA.mkdir(exist_ok=True)

subagentes = {
    "investigador": AgentDefinition(
        description="Investiga un tema en la web y devuelve hallazgos con fuentes. Usar para cualquier búsqueda.",
        prompt=(
            "Sos investigador de mercado. Buscá en la web, leé fuentes confiables y devolvé "
            "6-10 hallazgos con cifras, año y URL. No inventes datos."
        ),
        tools=["WebSearch", "WebFetch"],
        model="sonnet",
    ),
    "analista": AgentDefinition(
        description="Convierte hallazgos en insights, riesgos y recomendaciones de negocio.",
        prompt="Sos analista de estrategia. Diferenciá hechos de inferencias. Priorizá recomendaciones.",
        tools=[],
        model="sonnet",
    ),
    "redactor": AgentDefinition(
        description="Escribe informes ejecutivos y emails y los guarda como archivos.",
        prompt=(
            "Sos redactor ejecutivo. Escribís claro, sin relleno. Guardás los archivos que te piden "
            "en la carpeta indicada."
        ),
        tools=["Write", "Read"],
        model="sonnet",
    ),
}


async def main(tema: str) -> None:
    opciones = ClaudeAgentOptions(
        cwd=str(SALIDA),
        agents=subagentes,
        allowed_tools=["Agent", "Read", "Write", "WebSearch", "WebFetch"],
        permission_mode="acceptEdits",
        max_turns=40,
        system_prompt=(
            "Sos el director de un equipo de research. Delegá SIEMPRE en tus subagentes en este orden: "
            "investigador → analista → redactor. El redactor debe crear informe.md (máx. 600 palabras) y "
            "borrador_email.txt (para: direccion@empresa.com, máx. 150 palabras). No envíes emails reales."
        ),
    )
    async for mensaje in query(prompt=f"Tema del proyecto: {tema}", options=opciones):
        if isinstance(mensaje, AssistantMessage):
            for bloque in mensaje.content:
                if isinstance(bloque, TextBlock):
                    print(bloque.text)
        elif isinstance(mensaje, ResultMessage):
            costo = f"USD {mensaje.total_cost_usd:.4f}" if mensaje.total_cost_usd else "n/d"
            print(f"\n[fin — turnos: {mensaje.num_turns}, costo: {costo}]")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "mercado de apps de delivery en Uruguay"))
