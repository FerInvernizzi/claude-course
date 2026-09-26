---
name: modelo-dcf
description: Construye modelos de valuación por flujos de caja descontados (DCF) en Excel con estándares de banca de inversión. Usar cuando pidan valuar una empresa, un DCF, flujos descontados, WACC o valor terminal.
---

# Modelo DCF

## Estructura del libro
1. **Portada:** propósito, fuentes, unidades (moneda, miles o millones), fecha.
2. **Supuestos:** todos los inputs, en azul, con una nota de la fuente o justificación.
3. **Proyección:** 5 años de ingresos → EBIT → FCFF, una fórmula por fila, consistente entre columnas.
4. **WACC:** Rf, beta (desapalancada y reapalancada con la estructura objetivo), prima de mercado, riesgo país, Kd y tasa impositiva.
5. **DCF:** valor presente de los flujos, valor terminal por Gordon y por múltiplo, puente EV → Equity → precio por acción.
6. **Sensibilidades:** WACC × g y WACC × múltiplo de salida.
7. **Chequeos:** g < WACC, % del EV que aporta el valor terminal, sin errores ni valores fijos en las fórmulas.

## Fórmulas clave
- FCFF = EBIT × (1 − t) + D&A − Capex − ΔCapital de trabajo
- WACC = E/(D+E) × Ke + D/(D+E) × Kd × (1 − t)
- Ke = Rf + β × prima de mercado (+ riesgo país)
- Valor terminal (Gordon) = FCFF(N) × (1 + g) / (WACC − g)

## Convención de colores
Azul = input · Negro = fórmula · Verde = vínculo a otra hoja · Rojo = chequeo fallido.

## Antes de entregar
- [ ] Todos los chequeos en verde.
- [ ] Si el valor terminal aporta más del 80% del EV, advertilo.
- [ ] Listá los 3 supuestos que más mueven el valor (según las sensibilidades).
- [ ] Aclará que es un análisis y no una recomendación de inversión.
