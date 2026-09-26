#!/usr/bin/env python3
"""Chequeos automáticos de calidad para cursos en Markdown.

Uso: python chequeos.py <carpeta-del-curso>

Reporta: enlaces internos rotos, anclas inexistentes, bloques de código sin
cerrar o sin lenguaje, palabras repetidas, títulos duplicados dentro de un
archivo, módulos sin práctica/solución y marcadores pendientes.
Sale con código 1 si encuentra errores (no advertencias).
"""

import re
import sys
import unicodedata
from pathlib import Path

ENLACE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
TITULO = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
REPETIDA = re.compile(r"\b(\w{2,})\s+\1\b", re.IGNORECASE)
PENDIENTE = re.compile(r"\b(TODO|FIXME|XXX)\b|\[VERIFICAR\]")
EXCEPCIONES_REPETIDA = {"que", "la", "lo", "no", "sí", "si"}


def ancla(texto: str) -> str:
    """Convierte un título en el ancla que genera GitHub."""
    texto = re.sub(r"[`*_~]", "", texto).strip().lower()
    texto = "".join(c for c in texto if c.isalnum() or c in " -_" or unicodedata.category(c).startswith("L"))
    return texto.replace(" ", "-")


def sin_codigo(lineas):
    """Devuelve (nro, línea) fuera de bloques de código."""
    dentro = False
    for i, l in enumerate(lineas, 1):
        if l.lstrip().startswith("```"):
            dentro = not dentro
            continue
        if not dentro:
            yield i, l


def anclas_de(archivo: Path) -> set[str]:
    vistos: dict[str, int] = {}
    res = set()
    for _, l in sin_codigo(archivo.read_text(encoding="utf-8").splitlines()):
        m = TITULO.match(l)
        if m:
            a = ancla(m.group(2))
            n = vistos.get(a, 0)
            res.add(a if n == 0 else f"{a}-{n}")
            vistos[a] = n + 1
    return res


def revisar(raiz: Path) -> int:
    errores = advertencias = 0
    archivos = sorted(raiz.rglob("*.md"))
    for f in archivos:
        rel = f.relative_to(raiz)
        lineas = f.read_text(encoding="utf-8").splitlines()

        # Bloques de código
        abiertos = 0
        for i, l in enumerate(lineas, 1):
            s = l.lstrip()
            if s.startswith("```"):
                if abiertos == 0 and s.strip() == "```":
                    print(f"  ADVERTENCIA {rel}:{i} bloque de código sin lenguaje")
                    advertencias += 1
                abiertos ^= 1
        if abiertos:
            print(f"  ERROR {rel}: bloque de código sin cerrar")
            errores += 1

        titulos: dict[str, int] = {}
        for i, l in sin_codigo(lineas):
            # Enlaces
            for _, destino in ENLACE.findall(l):
                if re.match(r"^(https?:|mailto:)", destino):
                    continue
                ruta, _, frag = destino.partition("#")
                objetivo = (f.parent / ruta).resolve() if ruta else f
                if ruta and not objetivo.exists():
                    print(f"  ERROR {rel}:{i} enlace roto → {destino}")
                    errores += 1
                elif frag and objetivo.is_file() and objetivo.suffix == ".md" and frag not in anclas_de(objetivo):
                    print(f"  ERROR {rel}:{i} ancla inexistente → {destino}")
                    errores += 1
            # Palabras repetidas
            for m in REPETIDA.finditer(re.sub(r"`[^`]*`", "", l)):
                if m.group(1).lower() not in EXCEPCIONES_REPETIDA:
                    print(f"  ADVERTENCIA {rel}:{i} palabra repetida: '{m.group(0)}'")
                    advertencias += 1
            # Pendientes
            if PENDIENTE.search(l) and "PENDIENTE" not in str(rel):
                print(f"  ADVERTENCIA {rel}:{i} marcador pendiente: {l.strip()[:80]}")
                advertencias += 1
            # Títulos duplicados
            m = TITULO.match(l)
            if m:
                t = m.group(2).strip().lower()
                if t in titulos:
                    print(f"  ADVERTENCIA {rel}:{i} título duplicado (también en línea {titulos[t]}): {m.group(2)}")
                    advertencias += 1
                titulos[t] = i

        # Módulos: práctica y solución
        if "modulos" in f.parts and not f.name.startswith("00"):
            texto = "\n".join(lineas)
            if "Práctica" not in texto:
                print(f"  ADVERTENCIA {rel}: módulo sin sección de práctica")
                advertencias += 1
            elif "Solución" not in texto and "Criterios" not in texto:
                print(f"  ADVERTENCIA {rel}: práctica sin solución ni criterios de éxito")
                advertencias += 1

    print(f"\n{len(archivos)} archivos · {errores} errores · {advertencias} advertencias")
    return 1 if errores else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(revisar(Path(sys.argv[1])))
