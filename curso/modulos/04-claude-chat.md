# Módulo 04 — Claude Chat: investigación, escritura, creatividad y datos

Claude Chat (claude.ai o la app) es la puerta de entrada. Aunque no trabaja sobre tus carpetas como Cowork, tiene herramientas muy potentes: **búsqueda web, Research (investigación profunda), Artifacts, ejecución de código, creación de archivos, Projects y conectores**.

## 4.1 Investigación y visualización de datos en Chat

1. Activá **búsqueda web** en el menú de herramientas.
2. Subí un CSV/Excel o pedí datos públicos.

```
Buscá datos oficiales de inflación mensual de Argentina, Chile, Uruguay y México de los
últimos 24 meses. Citá las fuentes. Armá una tabla y un gráfico comparativo interactivo
como Artifact. Destacá en 3 bullets las conclusiones.
```

**Artifacts:** contenido que se abre en un panel lateral (código, HTML, gráficos React, documentos) que podés editar, versionar, publicar y compartir.

## 4.2 Deep Research (modo Investigación)

El modo **Research** hace que Claude realice **decenas de búsquedas encadenadas**, lea fuentes, contraste y entregue un **informe con citas**. Tarda varios minutos.

**Cuándo usarlo:** análisis de mercado, due diligence de competidores, estado del arte, regulación, preparar una decisión importante.

**Prompt modelo:**

```
Investigá el mercado de software de gestión para clínicas veterinarias en Latinoamérica.
Quiero:
1. Tamaño de mercado y crecimiento (con fuentes y año de cada dato).
2. Top 8 competidores: precio, funcionalidades, segmento, fortalezas/debilidades.
3. Tendencias 2025-2026 (IA, telemedicina, pagos).
4. Oportunidades no cubiertas.
Formato: informe ejecutivo con tabla comparativa. Marcá explícitamente los datos con
baja confianza o fuentes de marketing.
```

**Tips:** definí el **alcance** (región, periodo), el **formato**, y pedí que **marque la incertidumbre**. Verificá las cifras críticas abriendo las fuentes.

## 4.3 Claude para escritura creativa

```
Escribí un cuento corto (800 palabras) de ciencia ficción ambientado en Montevideo en 2060.
Tono: melancólico pero esperanzador. Narrador en primera persona, una bibliotecaria.
Evitá clichés (nada de robots rebeldes). Final abierto.
Antes de escribir, proponeme 3 premisas distintas y elegimos una.
```

Técnicas: **restricciones creativas** (qué evitar), **referencias de estilo** ("con el ritmo de Cortázar"), **iterar por partes** (primero estructura, luego escenas), pedir **variaciones**.

## 4.4 Claude para brainstorming

```
Actuá como facilitador de innovación. Generá 20 ideas para aumentar la retención de
clientes de un gimnasio de barrio. Agrupalas en: rápidas y baratas / medianas /
ambiciosas. Para cada grupo elegí la mejor y evaluala en impacto, costo y riesgo (1-5).
Después hacé de "abogado del diablo" contra la idea ganadora.
```

Técnicas útiles: **SCAMPER**, **6 sombreros**, **inversión** ("¿cómo haríamos que TODOS los clientes se vayan?" y luego invertir), **cantidad primero, filtro después**.

## 4.5 Dashboards con la skill Front‑End Design

La skill **frontend-design** hace que Claude diseñe interfaces con criterio visual (tipografía, jerarquía, espaciado, paleta), evitando el aspecto "genérico de IA".

```
Usando la skill de frontend design, creá un dashboard ejecutivo de ventas como Artifact
(React). Estética: editorial, fondo claro, tipografía serif para títulos, un color de
acento. KPIs arriba, gráfico principal grande, tabla de top productos. Datos de ejemplo
realistas. Que se sienta como un producto premium, no una plantilla.
```

## 4.6 Extraer datos financieros de PDF → Excel → PowerPoint

1. Subí el **informe anual** o estados financieros en PDF.

```
Del PDF adjunto extraé el Estado de Resultados, Balance y Flujo de Caja de los últimos
3 años a un Excel (una hoja por estado). Mantené los nombres de las cuentas originales.
Agregá una hoja "Ratios" con fórmulas: margen bruto, margen EBITDA, margen neto, ROE,
ROA, liquidez corriente, deuda/EBITDA, días de cobranza. Validá que Activo = Pasivo + PN
cada año e informá cualquier diferencia.
```

2. Luego:

```
Con ese Excel, creá una presentación de 5 slides para el directorio con la skill pptx:
evolución de ingresos y márgenes, rentabilidad, solidez financiera, 3 riesgos y
3 fortalezas.
```

## 4.7 Análisis financiero y "One Pager" con la skill PPTX

```
Generá un One Pager (1 slide, formato A4 horizontal) de la empresa del PDF:
- Encabezado: nombre, sector, ticker.
- Columna izquierda: descripción (3 líneas), 6 métricas clave en tarjetas.
- Centro: gráfico de ingresos y margen EBITDA 3 años.
- Derecha: tesis de inversión (3 bullets), riesgos (3 bullets).
Estilo sobrio de banco de inversión. Todo legible impreso.
```

## 4.8 Aprender con Claude

- **Modo tutor socrático:** *"Enseñame estadística inferencial. No me des las respuestas: hacé preguntas y corregime."*
- **Explicaciones por niveles:** *"Explicame qué es un DCF como si tuviera 12 años, luego como estudiante de finanzas, luego como analista."*
- **Planes de estudio:** *"Armame un plan de 30 días para aprender SQL con ejercicios diarios de 30 minutos."*
- **Projects:** subí apuntes y material del curso a un Project para que Claude responda sobre ellos.

## 4.9 Programar con Claude Chat

Útil para scripts cortos, entender código, fórmulas de Excel, SQL y prototipos en Artifacts.

```
Escribí un script Python que lea todos los .xlsx de una carpeta, unifique la hoja
"Ventas" y exporte un CSV. Manejá archivos con columnas en distinto orden. Explicá cómo
ejecutarlo en Windows paso a paso.
```

Para proyectos reales con muchos archivos → **Claude Code** (módulo 09).

## 4.10 Escribir con Claude

- **Emails difíciles:** *"Redactá un email declinando la propuesta de un proveedor sin cerrar la puerta. Tono cordial y firme. 120 palabras."*
- **Edición:** *"Editá este texto: más claro, frases cortas, sin perder datos. Mostrá los cambios en una tabla antes/después."*
- **Estilo propio:** pegá 3 textos tuyos y pedí *"Describí mi estilo en reglas y usalas de ahora en adelante"* (guardalo en un Project o skill).

## 4.11 Generación de imágenes: Claude vs Gemini

| | Claude | Gemini (Imagen / "Nano Banana") |
|---|---|---|
| Imágenes fotorrealistas | ❌ No genera imágenes nativamente | ✅ Sí |
| Diagramas, gráficos, SVG, infografías con código | ✅ Excelente (SVG, HTML, Mermaid, Python) | ⚠️ Correcto |
| Interpretar imágenes (visión) | ✅ Muy bueno | ✅ Muy bueno |
| Prompts para otros generadores | ✅ Excelente para escribirlos | — |

**Flujo recomendado:** usá Claude para **diagramas, infografías y visualizaciones con código**, y para **redactar prompts detallados** que luego usás en un generador de imágenes.

➡️ Siguiente: [Módulo 05 — Prompt Engineering y Context Engineering](05-prompt-context-engineering.md)
