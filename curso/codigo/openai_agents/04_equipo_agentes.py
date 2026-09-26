"""Módulo 11.11 — Equipo de agentes: de la investigación al email final.

Arquitectura (patrón "manager" / orquestador con agentes como herramientas):

    Director de proyecto (orquestador)
      ├── Investigador   → busca en la web y devuelve hallazgos con fuentes
      ├── Analista       → convierte hallazgos en insights y recomendaciones
      ├── Redactor       → escribe el informe ejecutivo en Markdown
      └── Comunicador    → redacta el email y lo "envía" (guarda un borrador)

El envío real de emails se deja como borrador en disco a propósito: en producción
reemplazá guardar_borrador_email por una integración (Gmail API, SendGrid, MCP)
con aprobación humana antes de enviar.

Ejecutar:
    python 04_equipo_agentes.py "mercado de apps de delivery en Uruguay"
"""

import sys
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
from agents import Agent, Runner, WebSearchTool, function_tool, trace

load_dotenv()

SALIDA = Path(__file__).with_name("salida")
SALIDA.mkdir(exist_ok=True)


class Hallazgos(BaseModel):
    tema: str
    hallazgos: list[str]
    fuentes: list[str]


@function_tool
def guardar_informe(nombre_archivo: str, contenido_markdown: str) -> str:
    """Guarda el informe en la carpeta salida/ y devuelve la ruta."""
    ruta = SALIDA / nombre_archivo
    ruta.write_text(contenido_markdown, encoding="utf-8")
    return str(ruta)


@function_tool
def guardar_borrador_email(para: str, asunto: str, cuerpo: str) -> str:
    """Guarda un borrador de email (no lo envía). Devuelve la ruta del borrador."""
    ruta = SALIDA / "borrador_email.txt"
    ruta.write_text(f"Para: {para}\nAsunto: {asunto}\n\n{cuerpo}", encoding="utf-8")
    return f"Borrador guardado en {ruta}. Requiere aprobación humana para enviarse."


investigador = Agent(
    name="Investigador",
    instructions=(
        "Investigá el tema en la web. Devolvé entre 6 y 10 hallazgos concretos "
        "(con cifras y año cuando existan) y la lista de URLs usadas. "
        "No inventes datos: si algo no se encuentra, decilo."
    ),
    tools=[WebSearchTool()],
    output_type=Hallazgos,
)

analista = Agent(
    name="Analista",
    instructions=(
        "Recibís hallazgos de investigación. Devolvé: 3-5 insights (qué significa cada "
        "hallazgo para el negocio), riesgos, oportunidades y 3 recomendaciones "
        "accionables priorizadas. Diferenciá hechos de inferencias."
    ),
)

redactor = Agent(
    name="Redactor",
    instructions=(
        "Escribí un informe ejecutivo en Markdown (máx. 600 palabras): título, resumen "
        "de 3 líneas, hallazgos clave, análisis, recomendaciones y fuentes. "
        "Guardalo con guardar_informe como informe.md y devolvé la ruta y el texto."
    ),
    tools=[guardar_informe],
)

comunicador = Agent(
    name="Comunicador",
    instructions=(
        "Redactá un email profesional y breve (máx. 150 palabras) que presente el "
        "informe: saludo, 3 bullets con lo más importante, próximo paso sugerido y "
        "firma 'Equipo de Research'. Guardalo con guardar_borrador_email."
    ),
    tools=[guardar_borrador_email],
)

director = Agent(
    name="Director de proyecto",
    instructions=(
        "Coordinás un equipo para producir un informe de investigación y enviarlo por "
        "email. Seguí SIEMPRE este orden: 1) investigar, 2) analizar los hallazgos, "
        "3) redactar el informe, 4) preparar el email para el destinatario indicado. "
        "Pasá a cada especialista toda la información que necesita. "
        "Al final, resumí qué se produjo y dónde quedó cada archivo."
    ),
    tools=[
        investigador.as_tool("investigar", "Investiga un tema en la web y devuelve hallazgos con fuentes."),
        analista.as_tool("analizar", "Convierte hallazgos en insights, riesgos y recomendaciones."),
        redactor.as_tool("redactar_informe", "Escribe y guarda el informe ejecutivo en Markdown."),
        comunicador.as_tool("preparar_email", "Redacta y guarda el borrador del email de envío."),
    ],
)

if __name__ == "__main__":
    tema = sys.argv[1] if len(sys.argv) > 1 else "mercado de apps de delivery en Uruguay"
    with trace("Equipo de research"):
        resultado = Runner.run_sync(
            director,
            f"Tema: {tema}. Destinatario del email: direccion@empresa.com",
            max_turns=30,
        )
    print(resultado.final_output)
