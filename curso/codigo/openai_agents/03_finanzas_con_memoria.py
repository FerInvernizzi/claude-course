"""Módulo 11.8 — El mismo agente CON memoria.

Dos tipos de memoria:
1. Memoria de conversación: SQLiteSession guarda el historial entre turnos
   (y entre ejecuciones, porque se persiste en un archivo .db).
2. Memoria de datos: los gastos se guardan en un JSON a través de herramientas,
   así sobreviven aunque se borre la conversación.
"""

import json
from datetime import date
from pathlib import Path

from dotenv import load_dotenv
from agents import Agent, Runner, SQLiteSession, function_tool

load_dotenv()

ARCHIVO_GASTOS = Path(__file__).with_name("gastos.json")


def _leer() -> list[dict]:
    if ARCHIVO_GASTOS.exists():
        return json.loads(ARCHIVO_GASTOS.read_text(encoding="utf-8"))
    return []


@function_tool
def registrar_gasto(categoria: str, monto: float, descripcion: str = "") -> str:
    """Registra un gasto con fecha de hoy en la memoria persistente."""
    gastos = _leer()
    gastos.append(
        {"fecha": date.today().isoformat(), "categoria": categoria.lower(),
         "monto": monto, "descripcion": descripcion}
    )
    ARCHIVO_GASTOS.write_text(json.dumps(gastos, ensure_ascii=False, indent=2), encoding="utf-8")
    return f"Registrado: ${monto:,.0f} en {categoria}."


@function_tool
def total_por_categoria() -> str:
    """Devuelve el total gastado por categoría según la memoria persistente."""
    totales: dict[str, float] = {}
    for g in _leer():
        totales[g["categoria"]] = totales.get(g["categoria"], 0) + g["monto"]
    if not totales:
        return "Todavía no hay gastos registrados."
    return "\n".join(f"{c}: ${t:,.0f}" for c, t in sorted(totales.items()))


asesor = Agent(
    name="Asesor con memoria",
    instructions=(
        "Sos un asesor de finanzas personales. Respondé en español, en forma breve. "
        "Cuando el usuario mencione un gasto, registralo con registrar_gasto. "
        "Para totales, usá total_por_categoria; no sumes de memoria."
    ),
    tools=[registrar_gasto, total_por_categoria],
)

if __name__ == "__main__":
    sesion = SQLiteSession("usuario_demo", "memoria_conversacion.db")
    turnos = [
        "Hoy gasté $45.000 en comida en el super.",
        "Y $12.000 en transporte.",
        "¿Cuánto llevo gastado en total por categoría?",
        "¿Qué fue lo primero que te conté hoy?",  # ← lo recuerda gracias a la sesión
    ]
    for t in turnos:
        print(f"\n👤 {t}")
        print(f"🤖 {Runner.run_sync(asesor, t, session=sesion).final_output}")
