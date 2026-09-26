"""Módulo 11.6 — Definir y ejecutar un agente con OpenAI Agents SDK.

Ejecutar:
    pip install -r ../requirements.txt
    export OPENAI_API_KEY=...        (o completar ../.env)
    python 01_agente_basico.py
"""

from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

load_dotenv()


@function_tool
def convertir_moneda(monto: float, tasa: float) -> float:
    """Convierte un monto multiplicándolo por la tasa de cambio indicada."""
    return round(monto * tasa, 2)


agente = Agent(
    name="Asistente financiero",
    instructions=(
        "Sos un asistente financiero claro y preciso. Respondé en español. "
        "Usá la herramienta convertir_moneda cuando te pidan conversiones; "
        "no hagas la cuenta de memoria."
    ),
    tools=[convertir_moneda],
)

if __name__ == "__main__":
    resultado = Runner.run_sync(
        agente, "Tengo 1.250 dólares. ¿Cuántos euros son si la tasa es 0,92?"
    )
    print(resultado.final_output)
