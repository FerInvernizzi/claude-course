#!/usr/bin/env python3
"""Mide la calidad de objetivos de aprendizaje con la rúbrica ABCD + alineación (0-10).

Uso:
    python medir_objetivos.py <carpeta-de-modulos>            # tablas de objetivos por módulo
    python medir_objetivos.py --lista archivo.txt [--evidencia-parcial]   # un objetivo por línea

Criterios (0-2 cada uno), ver references/rubrica.md y METODOLOGIA-OBJETIVOS.md:
  B  conducta observable (verbo de Bloom, uno solo, no vago)
  O  objeto específico (herramienta, comando o artefacto concreto)
  C  condición (con qué, dado qué, en qué contexto)
  D  criterio de logro verificable
  E  evidencia: la práctica/autoevaluación citada existe en el módulo

Es una heurística transparente: sirve para comparar versiones y detectar objetivos
débiles; el juicio final sobre un objetivo lo hace una persona.
"""

import re
import sys
from pathlib import Path

VAGOS = r"^(entender|comprender|conocer|saber|aprender|familiarizarse|dominar|explorar|apreciar|mejorar|master|understand|leverage|learn|know)\b"
OBSERVABLES = r"^(reformular|agregar|identificar|nombrar|listar|explicar|comparar|clasificar|diferenciar|resumir|configurar|instalar|ejecutar|aplicar|usar|conectar|generar|escribir|formular|diagnosticar|descomponer|auditar|perfilar|verificar|evaluar|justificar|seleccionar|construir|diseñar|crear|empaquetar|automatizar|producir|adaptar|implementar|recuperar|paralelizar|redactar|extraer|imputar|calcular|estimar|interpretar|desplegar|depurar|programar|convertir|investigar|elegir|ubicar|desarrollar|build|connect|construct|automate|design)\b"
CONDICION = r"\b(dado|dada|con |a partir de|usando|mediante|sobre |en un|en una|en tu|desde|para un|para una|sin salir|partiendo|using |with |from |through )"
CRITERIO = r"(sin |de modo que|que (pase|pasen|coincid|cumpl|respet|funcion)|coincid|menos de|al menos|como mínimo|≥|<|verific|exit|código de salida|0 errores|cada |todas? |todos |con fuente|trazab|reproducib|en menos de|hasta que)"
ESPECIFICO = r"(`|excel|powerpoint|cowork|claude code|mcp|skill|plugin|subagente|dcf|lbo|gmail|slack|salesforce|claude\.md|soul\.md|/[a-z]|api|dashboard|landing|tokens|ralph|git|obsidian|research|pptx|xlsx|hook|ventana de contexto|prompt)"


def puntuar(texto: str, evidencia_ok: bool | None) -> dict:
    t = re.sub(r"\*\*", "", texto).strip()
    t_low = t.lower()
    verbo = t_low.split()[0] if t_low else ""
    if re.match(VAGOS, t_low):
        b = 0
    elif re.match(OBSERVABLES, t_low):
        primeras = " ".join(t_low.split()[:6])
        b = 1 if re.search(r"\b(y|e)\s+(usar|aplicar|configurar|crear|hacer|trabajar|ejecutar|instalar)\b", primeras) else 2
    else:
        b = 1
    o = 2 if re.search(ESPECIFICO, t_low) else (1 if len(t_low.split()) > 4 else 0)
    c = 2 if re.search(CONDICION, t_low) else 0
    d = 2 if re.search(CRITERIO, t_low) else (1 if re.search(r"(correct|adecuad|efectiv|profesional|de calidad)", t_low) else 0)
    e = 0 if evidencia_ok is None else (2 if evidencia_ok else 1)
    return {"verbo": verbo, "B": b, "O": o, "C": c, "D": d, "E": e, "total": b + o + c + d + e}


def objetivos_de_modulo(texto: str):
    """Filas de la tabla '🎯 Objetivos de aprendizaje': (id, objetivo, evidencia)."""
    if "🎯 Objetivos de aprendizaje" not in texto:
        return []
    bloque = texto.split("🎯 Objetivos de aprendizaje", 1)[1].split("\n## ", 1)[0]
    filas = []
    for l in bloque.splitlines():
        m = re.match(r"^\|\s*([\d.]+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", l)
        if m:
            filas.append((m.group(1), m.group(2), m.group(4)))
    return filas


def evidencia_existe(evidencia: str, texto: str) -> bool:
    ev = evidencia.lower()
    if "autoevaluación" in ev and "🧠 Autoevaluación" in texto:
        return True
    if "práctica" in ev and "🧪" in texto:
        return True
    if "código" in ev or "proyecto" in ev or "demo" in ev:
        return True
    return False


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--lista":
        # --evidencia-parcial: los objetivos no citan práctica, pero el módulo tiene alguna (E=1)
        parcial = "--evidencia-parcial" in sys.argv
        filas = [l.strip() for l in Path(sys.argv[2]).read_text(encoding="utf-8").splitlines() if l.strip()]
        res = [puntuar(f, False if parcial else None) for f in filas]
        for f, r in zip(filas, res):
            print(f"{r['total']:>2}/10  B{r['B']} O{r['O']} C{r['C']} D{r['D']} E{r['E']}  {f[:90]}")
    else:
        res = []
        for f in sorted(Path(sys.argv[1]).glob("*.md")):
            texto = f.read_text(encoding="utf-8")
            for id_, obj, ev in objetivos_de_modulo(texto):
                r = puntuar(obj, evidencia_existe(ev, texto))
                res.append(r)
                print(f"{r['total']:>2}/10  B{r['B']} O{r['O']} C{r['C']} D{r['D']} E{r['E']}  {id_:<5} {obj[:80]}")
    if res:
        prom = sum(r["total"] for r in res) / len(res)
        ok = sum(r["total"] >= 8 for r in res)
        print(f"\nObjetivos: {len(res)} · promedio {prom:.1f}/10 · ≥8: {ok} ({ok / len(res):.0%})")


if __name__ == "__main__":
    main()
