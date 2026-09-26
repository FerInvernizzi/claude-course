# Módulo 07 — Modelos financieros nivel Wall Street con Cowork + Excel

<img src="../assets/linea.svg" alt="" width="100%">

## 🎯 Objetivos de aprendizaje

| # | Al terminar vas a poder… (conducta · condición · criterio) | Nivel (Bloom) | Evidencia |
|---|---|---|---|
| 7.1 | Aplicar a un modelo financiero la convención de colores, la separación supuestos/cálculos/resultados y una hoja de chequeos, con todos los chequeos en verde | Aplicar · procedimental | Práctica |
| 7.2 | Construir con Claude un DCF a partir de estados financieros, con WACC documentado y grillas de sensibilidad por fórmulas, sin errores en la auditoría del revisor | Crear · procedimental | Práctica |
| 7.3 | Evaluar una valuación dada identificando al menos 3 errores típicos (g ≥ WACC, valor terminal > 85% del EV, signos de capex) y proponiendo la corrección | Evaluar · conceptual | Autoevaluación |
| 7.4 | Calcular el MOIC y la TIR de un LBO a partir de sus supuestos, de modo que el modelo construido con Claude coincida con el cálculo manual (± 0,5 pp) | Aplicar · procedimental | Práctica (entrega 4) |

**Requisitos previos:** Módulos 03 y 06 (el glosario del módulo cubre los términos contables) · **Duración estimada:** 3 h

> **Plugins recomendados:** `model-builder` (skills `dcf-model`, `lbo-model`, `3-statement-model`, `comps-analysis`, `audit-xls`) y `Finance`. Ver [SKILLS-Y-PLUGINS.md](../SKILLS-Y-PLUGINS.md).
>
> ⚠️ Los modelos son herramientas de análisis, no recomendaciones de inversión. Revisá cada supuesto.

### 🗺️ Ruta de estudio (3 sesiones)

| Sesión | Secciones | Resultado |
|---|---|---|
| 1 · 60 min | Glosario, 7.1 y 7.2 | Modelo de 3 estados con chequeos (entrega 1 de la práctica) |
| 2 · 60 min | 7.3 y 7.4 (con el ejemplo resuelto) | DCF, WACC y sensibilidades (entregas 2 y 3) |
| 3 · 60 min | 7.5 a 7.7 | LBO y one pager (entregas 4 y 5) |

### 📖 Glosario mínimo

| Término | Qué es |
|---|---|
| **EBIT / EBITDA** | Resultado operativo antes de intereses e impuestos / lo mismo, antes también de depreciaciones y amortizaciones (D&A) |
| **Capex** | Inversión en activos fijos (máquinas, software, edificios) |
| **Capital de trabajo (CT)** | Cuentas por cobrar + inventario − cuentas por pagar. Si crece, consume caja |
| **FCFF** | Flujo de caja libre para la firma: la caja que genera la operación después de impuestos, capex y CT |
| **WACC** | Costo promedio del capital (deuda y acciones): la tasa con la que se descuentan los flujos |
| **Rf · β · prima de mercado** | Tasa libre de riesgo · sensibilidad de la acción al mercado · retorno extra que se exige por invertir en acciones |
| **g** | Crecimiento perpetuo de los flujos después del horizonte proyectado |
| **Valor terminal (VT)** | Valor de todos los flujos posteriores al último año proyectado |
| **EV / Equity** | Valor de la empresa (para deuda y accionistas) / valor para los accionistas = EV − deuda neta |
| **Múltiplo EV/EBITDA** | Cuántas veces el EBITDA se paga por la empresa |
| **TIR (IRR) · MOIC** | Rentabilidad anual de la inversión · cuántas veces se multiplicó el dinero |
| **Cash sweep · bullet** | Uso del excedente de caja para prepagar deuda · deuda que se paga toda al vencimiento |

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

**Ejemplo resuelto** (antes de pedírselo a Claude, hacelo a mano o en una planilla para entender qué debería dar):

| | Año 1 | Año 2 | Año 3 |
|---|---|---|---|
| FCFF | 100 | 110 | 120 |
| Factor de descuento (WACC 10%) | 1/1,10 | 1/1,10² | 1/1,10³ |
| Valor presente | 90,9 | 90,9 | 90,2 |

- Suma de valores presentes: **272,0**
- Valor terminal (g = 3%): 120 × 1,03 / (0,10 − 0,03) = **1.765,7** → valor presente: 1.765,7 / 1,10³ = **1.326,6**
- EV = 272,0 + 1.326,6 = **1.598,6** → el VT es el **83%** del EV (alto: señal para revisar g y el horizonte)
- Con deuda neta de 300 y 100 acciones: Equity = 1.298,6 → **12,99 por acción**

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
Precio de compra (EV) = EBITDA_0 × múltiplo de entrada   (ya incluye refinanciar la deuda existente)
Fuentes = Deuda senior + Deuda subordinada + Equity del sponsor
Usos    = Precio de compra (EV) + fees
Equity del sponsor = Usos − deuda nueva
Salida  = EBITDA_N × múltiplo de salida – Deuda neta_N  → Equity de salida
MOIC = Equity salida / Equity inicial ;  IRR = MOIC^(1/N) – 1 (sin flujos intermedios)
```

**Ejemplo resuelto:** EBITDA 50, múltiplo de entrada y de salida 8x, deuda 5,5x, fees 2%, EBITDA que crece 5% anual durante 5 años y deuda neta de 150 a la salida.

| Paso | Cálculo | Resultado |
|---|---|---|
| Precio (EV) | 50 × 8 | 400 |
| Deuda nueva | 50 × 5,5 | 275 |
| Fees | 2% × 400 | 8 |
| Equity inicial | 400 + 8 − 275 | **133** |
| EBITDA año 5 | 50 × 1,05⁵ | 63,8 |
| EV de salida | 63,8 × 8 | 510,5 |
| Equity de salida | 510,5 − 150 | **360,5** |
| MOIC | 360,5 / 133 | **2,71x** |
| TIR | 2,71^(1/5) − 1 | **22,1%** |

Atribución de la ganancia (227,5): crecimiento del EBITDA 110,5 (13,8 × 8) + desapalancamiento 125 (275 − 150) − fees 8. No hay expansión de múltiplo porque se compra y se vende a 8x.

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

## 🧪 Práctica: valuación completa en 5 entregas

Trabajá con una empresa que cotice (o con datos sintéticos que pidas a Claude). Cada entrega tiene su criterio; no avances hasta cumplirlo.

| Entrega | Qué hacés | Criterio de éxito |
|---|---|---|
| **1. Modelo de 3 estados** | Extraé 3 años de estados (PDF → Excel, sección 4.6) y proyectá 5 años con drivers (7.2) | Hoja *Chequeos* toda en verde: el balance cuadra y la caja del flujo coincide con la del balance |
| **2. DCF** | Agregá FCFF, WACC documentado, VT por Gordon y por múltiplo, y el puente a precio por acción (7.4) | Reproducís con el modelo el ejemplo resuelto de 7.3 (EV 1.598,6 ± 1); el `revisor-financiero` o `audit-xls` no reporta errores de gravedad alta |
| **3. Sensibilidades** | Grillas WACC × g y WACC × múltiplo, y un gráfico tornado (±10% por supuesto) | Las grillas son fórmulas que recalculan; identificás el supuesto que más mueve el valor |
| **4. LBO** | Armá el LBO de 7.6 con los datos del ejemplo resuelto de 7.5 | MOIC 2,71x y TIR 22,1% (± 0,5 pp) con esos supuestos; la atribución suma la ganancia total |
| **5. One pager** | Tesis, valuación (DCF, comparables, rango de 52 semanas) y riesgos con `pptx` | Cada cifra coincide con el modelo; se entiende en 60 segundos |

### ✅ Solución (guía)

1. **Entrega 1:** si un chequeo falla, pedí *"Rastreá por qué Activo ≠ Pasivo + PN en 2027: listá las cuentas que no se vinculan"*. Lo típico es la caja o el resultado del ejercicio sin enlazar.
2. **Entrega 2:** cargá primero los datos del ejemplo resuelto (flujos 100/110/120, WACC 10%, g 3%) para validar la mecánica, y después los reales. Si el VT supera el 85% del EV, revisá el horizonte o g.
3. **Entrega 3:** *"Hacé un gráfico tornado variando ±10% cada supuesto clave (crecimiento, margen, WACC, g, capex)"*. Suele dominar el margen o el WACC.
4. **Entrega 4:** si la TIR no da 22,1%, revisá que los fees estén en *Usos* y que el equity de salida reste la deuda neta del año 5.
5. **Entrega 5:** *football field* con DCF, comparables y rango de 52 semanas; riesgos en 3 bullets.

## 📌 Ideas clave

- Un modelo profesional separa supuestos, cálculos y resultados, y tiene chequeos en verde.
- DCF: valor presente de los FCFF + valor terminal; controlá que g < WACC y el peso del VT.
- LBO: el retorno viene de crecer el EBITDA, pagar deuda y (a veces) expandir el múltiplo.
- Validá la mecánica con un ejemplo resuelto antes de cargar los datos reales.
- Sensibilidades con grillas de fórmulas, no con la *Tabla de datos* del complemento.

## 🧠 Autoevaluación

1. ¿Por qué g tiene que ser menor que el WACC?
   <details><summary>Ver respuesta</summary>En la fórmula de Gordon, si g ≥ WACC el denominador es cero o negativo y el valor terminal no tiene sentido.</details>

2. ¿De dónde viene el retorno de un LBO?
   <details><summary>Ver respuesta</summary>Crecimiento del EBITDA, desapalancamiento (pago de deuda con el flujo) y expansión del múltiplo.</details>

3. Un DCF da EV 1.000 y el VT descontado vale 900. ¿Qué hacés?
   <details><summary>Ver respuesta</summary>El VT es el 90% del EV: la valuación depende casi entera de supuestos de largo plazo. Revisá g (¿es mayor que el crecimiento de largo plazo de la economía?), extendé el horizonte proyectado y contrastá con el método de múltiplos.</details>

4. ¿Qué indica un valor terminal que supera el 85% del EV?
   <details><summary>Ver respuesta</summary>Que la valuación depende casi toda de supuestos de largo plazo: conviene revisar el horizonte, g o el múltiplo.</details>

➡️ Siguiente: [Módulo 08 — Claude en PowerPoint](08-claude-en-powerpoint.md)
