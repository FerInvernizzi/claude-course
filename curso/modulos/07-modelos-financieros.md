# Módulo 07 — Modelos financieros nivel Wall Street con Cowork + Excel

> **🎯 Objetivos.** Al terminar este módulo vas a poder:
> - Aplicar los estándares de un modelo financiero profesional (colores, chequeos, escenarios).
> - Construir un modelo de 3 estados, un DCF y un LBO con Claude.
> - Interpretar sensibilidades y detectar errores típicos de valuación.
>
> **Requisitos previos:** Módulos 03 y 06 · nociones de contabilidad · **Duración estimada:** 3 h

> **Plugins recomendados:** `model-builder` (skills `dcf-model`, `lbo-model`, `3-statement-model`, `comps-analysis`, `audit-xls`) y `Finance`. Ver [SKILLS-Y-PLUGINS.md](../SKILLS-Y-PLUGINS.md).
>
> ⚠️ Los modelos son herramientas de análisis, no recomendaciones de inversión. Revisá cada supuesto.

## 7.1 Estándares de un modelo profesional

1. **Separación Inputs → Cálculos → Outputs.** Supuestos en una hoja; nada "hardcodeado" en fórmulas.
2. **Código de colores:** azul = input; negro = fórmula; verde = vínculo a otra hoja; rojo = alerta/chequeo.
3. **Una fórmula por fila**, consistente a lo largo de las columnas (sin fórmulas distintas en años distintos).
4. **Chequeos:** balance cuadra (Activo = Pasivo + PN), caja del flujo = caja del balance, sin errores `#¡REF!`.
5. **Escenarios** (base / optimista / pesimista) conmutables desde un selector.
6. **Sensibilidades** en grillas (con fórmulas explícitas si trabajás con el complemento de Excel, que no soporta la función *Tabla de datos*; o con *Tabla de datos* si el modelo lo genera Cowork con la skill `xlsx`).
7. **Documentación:** hoja "Portada" con propósito, fuentes, unidades y fecha.

## 7.2 Construir modelos con Cowork (flujo general)

```text
Sos analista de banca de inversión. En /Modelo tengo los estados financieros históricos
(3 años) de la empresa X en PDF. Construí un modelo de 3 estados integrado en Excel:
- Hojas: Portada, Supuestos, Hist, EERR, Balance, Flujo, Deuda, Chequeos.
- Proyección 5 años con drivers: crecimiento de ventas, margen bruto, gastos % ventas,
  días de cobro/pago/inventario, capex % ventas, D&A % capex, tasa impositiva.
- Selector de escenarios en Supuestos (1=base, 2=optimista, 3=pesimista) con ELEGIR.
- Convención de colores estándar. Hoja Chequeos con semáforo.
Antes de construir, listá los supuestos que vas a usar y su justificación.
```

## 7.3 Discounted Cash Flow (DCF): intuición

**Idea:** una empresa vale el **valor presente de los flujos de caja libres** que generará.

```text
FCFF = EBIT × (1 – t) + D&A – Capex – ΔCapital de trabajo

Valor Empresa (EV) = Σ FCFF_t / (1 + WACC)^t  +  Valor Terminal / (1 + WACC)^N

Valor Terminal (Gordon)   = FCFF_N × (1 + g) / (WACC – g)
Valor Terminal (múltiplo) = EBITDA_N × múltiplo EV/EBITDA

WACC = E/(D+E) × Ke + D/(D+E) × Kd × (1 – t)
Ke (CAPM) = Rf + β × Prima de riesgo de mercado (+ riesgo país si aplica)

Equity Value = EV – Deuda neta ;  Precio por acción = Equity Value / acciones diluidas
```

**Errores comunes:** g ≥ WACC (explota), g mayor al crecimiento de largo plazo de la economía, mezclar flujos nominales con tasas reales, olvidar la convención de mitad de año, que el valor terminal sea >85% del EV sin cuestionarlo.

## 7.4 Construir un DCF con Claude

```text
Usando el modelo de 3 estados, agregá una hoja DCF:
1. FCFF 5 años enlazado a EERR/Balance/Flujo.
2. Hoja WACC con inputs: Rf, beta apalancada (desapalancá/reapalancá con estructura
   objetivo), prima de mercado, riesgo país, Kd, tasa impositiva, D/E objetivo.
3. Valor terminal por Gordon y por múltiplo; mostrá ambos y el EV implícito.
4. Convención de mitad de año (opcional con interruptor).
5. Puente EV → Equity → precio por acción.
6. Tablas de sensibilidad: WACC (±2%) × g (±1%) y WACC × múltiplo de salida, armadas como grillas con fórmulas que recalculan el precio por acción en cada celda (no uses la función *Tabla de datos* de Excel: el complemento de Claude no la soporta).
7. Chequeo: % del EV que viene del valor terminal.
Formato banca de inversión. Explicá cada supuesto en comentarios de celda.
```

**Revisión (pedísela a Claude o al agente `audit-xls`):**
```text
Auditá la hoja DCF: fórmulas inconsistentes entre columnas, valores hardcodeados,
referencias circulares no intencionales, signos de capex/ΔCT, y si g < WACC.
```

## 7.5 Leveraged Buyout (LBO): intuición

Un fondo de private equity **compra una empresa usando mucha deuda**, la mejora durante 3–7 años, **paga deuda con el flujo de caja** y la vende. El retorno viene de:

1. **Crecimiento del EBITDA** (operaciones).
2. **Desapalancamiento** (el flujo paga deuda → crece el equity).
3. **Expansión de múltiplo** (vender a un múltiplo mayor al de compra).

Métricas: **IRR** (TIR, objetivo típico 20–25%) y **MOIC** (múltiplo del dinero, típicamente 2–3x).

```text
Precio de compra = EBITDA_0 × múltiplo de entrada
Fuentes = Deuda senior + Deuda subordinada + Equity del sponsor
Usos    = Precio de compra + refinanciación + fees
Salida  = EBITDA_N × múltiplo de salida – Deuda neta_N  → Equity de salida
MOIC = Equity salida / Equity inicial ;  IRR = MOIC^(1/N) – 1 (sin flujos intermedios)
```

## 7.6 Construir un LBO con Claude

```text
Construí un modelo LBO en Excel para una empresa con EBITDA de USD 50M:
- Supuestos: múltiplo de entrada 8x, salida 8x, deuda senior 4x EBITDA (tasa 9%,
  amortización 5%/año), subordinada 1,5x (12%, bullet), fees 2%, horizonte 5 años.
- Hojas: Supuestos, Fuentes y Usos, Proyección operativa, Cronograma de deuda
  (con cash sweep del 75% del exceso de caja), Retornos (IRR con TIR.NO.PER y MOIC).
- Sensibilidades: IRR por múltiplo de entrada × salida, y por apalancamiento × crecimiento.
- Atribución de retornos: cuánto viene de crecimiento de EBITDA, desapalancamiento y
  expansión de múltiplo.
Manejá la circularidad de intereses con promedio de saldos e interruptor de iteración.
```

## 7.7 Forecasting con skills

Ver sección 3.5. Combinalo con el modelo: el forecast de ventas alimenta la hoja Supuestos.

## 🧪 Práctica

Con los datos de una empresa pública que elijas (o sintéticos): construí un DCF y respondé: 1) precio por acción en escenario base, 2) rango con sensibilidades, 3) ¿qué supuesto mueve más el valor?, 4) one pager en PowerPoint con la conclusión.

### ✅ Solución (guía)

1. Extraer 3 años de estados (PDF → Excel, módulo 04.6).
2. Modelo de 3 estados con chequeos en verde.
3. DCF con WACC documentado; verificar % de valor terminal (si >80%, revisar horizonte o g).
4. Sensibilidad WACC × g → rango de precios; **tornado** (pedí: *"hacé un gráfico tornado variando ±10% cada supuesto clave"*) → identifica el supuesto dominante (suele ser margen o WACC).
5. One pager con `pptx`: tesis, valuación (football field: DCF, comps, rango 52 semanas), riesgos.

## 🧠 Autoevaluación

1. ¿Por qué g tiene que ser menor que el WACC?
   <details><summary>Ver respuesta</summary>En la fórmula de Gordon, si g ≥ WACC el denominador es cero o negativo y el valor terminal no tiene sentido.</details>

2. ¿De dónde viene el retorno de un LBO?
   <details><summary>Ver respuesta</summary>Crecimiento del EBITDA, desapalancamiento (pago de deuda con el flujo) y expansión del múltiplo.</details>

3. ¿Qué indica un valor terminal que supera el 85% del EV?
   <details><summary>Ver respuesta</summary>Que la valuación depende casi toda de supuestos de largo plazo: conviene revisar el horizonte, g o el múltiplo.</details>

➡️ Siguiente: [Módulo 08 — Claude en PowerPoint](08-claude-en-powerpoint.md)
