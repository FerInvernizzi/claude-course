"""Módulo 11.7 — Agente de finanzas personales SIN memoria.

Cada llamada a Runner.run_sync empieza de cero: el agente no recuerda los
gastos que registraste en el turno anterior. Ejecutalo y comparalo con
03_finanzas_con_memoria.py.
"""

from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

load_dotenv()

PRESUPUESTO = {"comida": 300_000, "transporte": 80_000, "ocio": 100_000}


@function_tool
def consultar_presupuesto(categoria: str) -> str:
    """Devuelve el presupuesto mensual de una categoría (comida, transporte, ocio)."""
    monto = PRESUPUESTO.get(categoria.lower())
    if monto is None:
        return f"No hay presupuesto para '{categoria}'. Categorías: {', '.join(PRESUPUESTO)}."
    return f"Presupuesto mensual de {categoria}: ${monto:,.0f}"


@function_tool
def calcular_ahorro(ingreso_mensual: float, gastos_mensuales: float) -> str:
    """Calcula el ahorro mensual y la tasa de ahorro."""
    ahorro = ingreso_mensual - gastos_mensuales
    tasa = ahorro / ingreso_mensual * 100 if ingreso_mensual else 0
    return f"Ahorro: ${ahorro:,.0f} ({tasa:.1f}% del ingreso)"


asesor = Agent(
    name="Asesor de finanzas personales",
    instructions=(
        "Sos un asesor de finanzas personales. Respondé en español, en forma breve. "
        "Usá las herramientas para datos y cálculos. No des consejos de inversión "
        "específicos; sugerí consultar a un profesional para eso."
    ),
    tools=[consultar_presupuesto, calcular_ahorro],
)

if __name__ == "__main__":
    turnos = [
        "Hoy gasté $45.000 en comida. ¿Cuánto presupuesto tengo para comida?",
        "¿Cuánto llevo gastado en comida en total?",  # ← no lo va a saber
    ]
    for t in turnos:
        print(f"\n👤 {t}")
        print(f"🤖 {Runner.run_sync(asesor, t).final_output}")
