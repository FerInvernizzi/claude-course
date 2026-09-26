# Módulo 13 — Las 10 automatizaciones de tu agente personal

<img src="../assets/linea.svg" alt="" width="100%">

## 🎯 Objetivos de aprendizaje

| # | Al terminar vas a poder… (conducta · condición · criterio) | Nivel (Bloom) | Evidencia |
|---|---|---|---|
| 13.1 | Construir al menos 5 automatizaciones como procedimiento escrito + comando + disparador, a partir de los blueprints del módulo | Crear · procedimental | Práctica |
| 13.2 | Programar al menos 2 automatizaciones con `/schedule` y disparar 1 con Dispatch desde el celular, registrando cada ejecución en el diario | Aplicar · procedimental | Práctica |
| 13.3 | Evaluar cada automatización con los 6 criterios de calidad (definición escrita, idempotencia, seguridad, observabilidad, tolerancia a fallos, medición), documentando el tiempo ahorrado por semana | Evaluar · metacognitivo | Práctica |

**Requisitos previos:** Módulo 12 · **Duración estimada:** 8 h o más

## 13.1 Visión general de los 10 blueprints

| # | Automatización | Qué hace | Conectores | Frecuencia |
|---|----------------|----------|-----------|-----------|
| 1 | **Sprint Tracker** | Seguimiento semanal de objetivos y tareas | Notion / archivos | Lunes y viernes |
| 2 | **Morning Brief** | Resumen del día: agenda, emails clave, prioridades | Calendar, Gmail | Diario 7:30 |
| 3 | **Market Pulse** | Noticias y datos de mercado de tus temas/acciones | Web | Diario |
| 4 | **Research Team** | Equipo de subagentes → deck PPT + informe PDF | Web | A pedido |
| 5 | **Personal CRM** | Fichas de contactos actualizadas desde email y reuniones | Gmail, Calendar | Diario |
| 6 | **Meeting Intel** | Brief antes de cada reunión y minuta después | Calendar, Gmail, web | Por reunión |
| 7 | **Email Triage** | Clasifica la bandeja y prepara borradores | Gmail | 2 veces/día |
| 8 | **Expense Wrangler** | Recibos/facturas → Excel de gastos categorizado | Gmail, Drive | Semanal |
| 9 | **Content Machine** | Ideas → posts con tu estilo y marca | Web | Semanal |
| 10 | **Weekly Executive Report** | Informe ejecutivo semanal con KPIs | Todos | Viernes |

### Anatomía de un blueprint

Cada automatización tiene:

1. **Definición** en `automatizaciones/<nombre>.md` (objetivo, entradas, pasos, salida, reglas).
2. **Comando** en `.claude/commands/<nombre>.md` que ejecuta la definición.
3. **Salida** en `diario/`, `salidas/` o `wiki/`.
4. **Disparador:** manual (`/morning-brief`), **programado** (tarea programada en Cowork con `/schedule` o una rutina en Claude Code) o **desde el celular** (Dispatch).

**Plantilla de comando** ([`plantillas/commands/automatizacion.md`](../plantillas/commands/automatizacion.md)):

```markdown
---
description: <qué hace en una línea>
---
Leé SOUL.md y automatizaciones/<nombre>.md y ejecutá el procedimiento completo.
Reglas: nunca envíes nada sin aprobación; si un conector falla, seguí con el resto y
reportalo; guardá la salida donde indica la definición; registrá la ejecución en
diario/<hoy>.md.
```

### Intro: agentes personales y automatizaciones

Una automatización = **procedimiento escrito + agente + disparador**. El procedimiento vive en archivos (versionable, editable), no en tu cabeza ni en un prompt perdido. Cuando algo sale mal, **editás la definición**, no repetís el prompt.

---

## 1. Sprint Tracker

### Parte 1 — Construcción

`automatizaciones/sprint-tracker.md`:

```markdown
# Sprint Tracker
Objetivo: mantener mis objetivos semanales alineados con yo/objetivos.md.

## Lunes (planificación)
1. Leé yo/objetivos.md y el sprint anterior en proyectos/sprints/.
2. Proponé 3-5 objetivos de la semana (SMART) y las tareas de cada uno con estimación.
3. Creá proyectos/sprints/AAAA-Wnn.md con tabla: objetivo | tarea | estimación | estado.
4. Si tengo Notion conectado, creá/actualizá la base "Sprints".

## Viernes (revisión)
1. Actualizá el estado de cada tarea (preguntame las que no puedas inferir del diario).
2. Calculá % de cumplimiento y horas estimadas vs. reales.
3. Escribí una retro: qué funcionó, qué no, qué cambio para la próxima semana.
4. Actualizá wiki/log.md.
```

### Parte 2 — Prueba y mejora

```text
/sprint-tracker lunes
```

Iterá: si las tareas son demasiado grandes, agregá la regla *"ninguna tarea > 3 horas; si es mayor, dividila"*.

## 2. Morning Brief

### Construcción

```markdown
# Morning Brief
Salida: diario/<hoy>.md (sección "Brief") — lectura de máximo 2 minutos.

1. Calendar: reuniones de hoy con hora, asistentes y objetivo (buscá contexto en
   wiki/personas y crm/). Marcá conflictos y reuniones sin agenda.
2. Gmail: los 5 emails no leídos más importantes de las últimas 24 h (criterio: remitente
   en crm/ con prioridad alta, menciona plazos, espera mi respuesta). Una línea c/u.
3. Tareas: lo pendiente del sprint para hoy.
4. "Las 3 cosas que importan hoy" según yo/objetivos.md.
5. Un dato útil: clima y cualquier vencimiento de los próximos 3 días.
Formato: títulos cortos, bullets, nada de relleno.
```

### Prueba

```text
/morning-brief
```

Verificá: ¿cabe en 2 minutos? ¿las prioridades son las correctas? Ajustá los criterios de importancia en la definición.

### Dispatch: ejecutarlo desde el celular

**Dispatch** permite enviarle tareas a tu agente desde la app de Claude en el celular, y que se ejecuten **en tu computadora**: con tus archivos locales, tus conectores e incluso controlando tus aplicaciones de escritorio (por ejemplo, actualizar un Excel). Requiere plan Pro o Max.

1. En Cowork (en la computadora o en el celular) → **Dispatch** en la barra lateral → *Get started* → activá el acceso a archivos y el permiso para mantener la computadora despierta → *Finish setup*.
2. Desde el celular: *"Corré el morning brief y mandame el resumen acá"*.
3. La tarea corre en tu computadora con acceso a tu vault y conectores; el resultado llega al teléfono.

> Para Dispatch, la computadora tiene que estar **encendida y despierta**, con Claude Desktop abierto. Es una sola conversación persistente (no varios hilos). Ojo con la cadena de confianza: una instrucción desde el celular puede leer, mover o borrar archivos y usar tus apps.

**Programarlo:** en Cowork, `/schedule` → *"Todos los días hábiles a las 7:30, ejecutá /morning-brief"*. Claude redacta el prompt de la tarea y vos lo aprobás. Un truco: hacé la tarea una vez a mano, verificá que el resultado sea el correcto y recién ahí escribí `/schedule` para convertir *ese mismo proceso* en recurrente. Las tareas programadas de Cowork **corren en la nube**, sin necesidad de que tu equipo esté encendido. Si necesitan archivos locales, usá las tareas programadas de Claude Desktop, que corren en tu máquina.

## 3. Market Pulse

### Construcción

```markdown
# Market Pulse
Entradas: wiki/conceptos/watchlist.md (tickers, sectores, temas, competidores).
1. Para cada ítem, buscá noticias de las últimas 24 h en fuentes confiables.
2. Datos: variación diaria de los tickers, índices principales y tipo de cambio.
3. Filtrá: solo lo que cambie una decisión o una opinión. Máx. 7 ítems.
4. Para cada ítem: qué pasó (1 línea), por qué importa para mí (1 línea), fuente.
5. Guardá en salidas/market-pulse/<hoy>.md y agregá una línea al diario.
Nunca des recomendaciones de compra/venta.
```

Plugins útiles: **market-researcher** y **financial-analysis** (instalados en este repo).

### Prueba

```text
/market-pulse
```

Revisá que cada ítem tenga **fuente** y **fecha**, y que no haya noticias viejas.

## 4. Research Team (equipo de agentes)

### Construcción

Tres subagentes en `.claude/agents/` (plantillas en [`plantillas/agents/`](../plantillas/agents/)): `investigador`, `analista`, `redactor`.

```markdown
# Research Team
Entrada: tema + audiencia + formato (deck, pdf o ambos).
1. Planificá 3-5 preguntas de investigación.
2. Lanzá subagentes "investigador" EN PARALELO, uno por pregunta. Cada uno devuelve
   hallazgos con fuente y fecha.
3. Subagente "analista": sintetiza, detecta contradicciones y arma la storyline
   (situación → complicación → resolución).
4. Subagente "redactor":
   - deck: 10-12 slides con marca/plantilla.pptx (skill pptx), títulos-acción, fuentes al pie.
   - pdf: informe de 4-6 páginas (skill pdf/docx) con resumen ejecutivo.
5. Guardá en salidas/research/<slug>/ y creá la página wiki/conceptos/<tema>.md.
```

### Prueba parte 1 — Deck de PowerPoint

```text
/research-team "Impacto de la IA agéntica en estudios contables de LATAM" audiencia=socios formato=deck
```

Revisión: títulos‑acción, datos con fuente, marca aplicada, sin slides de texto denso.

### Prueba parte 2 — Informe PDF y Dispatch

```text
/research-team "..." formato=pdf
```

Probalo desde el celular vía Dispatch: *"Lanzá el research team sobre X y avisame cuando esté el PDF"*.

## 5. Personal CRM

### Construcción y prueba

```markdown
# Personal CRM
1. Gmail (últimas 24 h) + Calendar (reuniones de ayer): identificá personas con las
   que interactué.
2. Para cada una: creá o actualizá crm/<nombre-apellido>.md con frontmatter
   (empresa, rol, email, prioridad, ultima_interaccion, proximo_paso, fecha_proximo_paso)
   y agregá la interacción al historial (fecha, canal, resumen de 1 línea).
3. Enlazá con [[wiki/empresas/...]] y [[wiki/proyectos/...]].
4. Listá en el diario: seguimientos vencidos y contactos importantes sin interacción
   en 30+ días.
Nunca guardes datos sensibles (salud, documentos, contraseñas).
```

```text
/personal-crm
```

Verificá en Obsidian que las fichas se enlazan con empresas y proyectos.

> Si usás **Salesforce** o **HubSpot**, el plugin **Sales** trae skills (`account-research`, `call-prep`, `log-activity`) que sincronizan con el CRM de la empresa.

## 6. Meeting Intel

### Construcción

```markdown
# Meeting Intel
## Antes (30 min antes de cada reunión)
1. Leé el evento de Calendar: asistentes, agenda, documentos adjuntos.
2. Por asistente: ficha de crm/ o wiki/, y si es externo, investigación web breve
   (rol, empresa, noticias recientes).
3. Hilo de emails relacionado (últimos 30 días).
4. Brief de 1 página: objetivo, contexto, 3 preguntas para hacer, riesgos, resultado deseado.
## Después
1. Con mis notas o la transcripción en raw/reuniones/, generá la minuta: decisiones,
   próximos pasos (responsable + fecha), temas abiertos.
2. Actualizá crm/ y wiki/proyectos/.
3. Prepará (no envíes) el email de seguimiento.
```

### Prueba

```text
/meeting-intel antes "Reunión con Acme — jueves 15:00"
/meeting-intel despues raw/reuniones/2026-09-24-acme.md
```

## 7. Email Triage

### Construcción

```markdown
# Email Triage
Clasificá los emails no leídos de las últimas 12 h en:
- 🔴 Responder hoy (requiere mi decisión o tiene plazo < 48 h)
- 🟡 Responder esta semana
- 🔵 Solo leer / FYI
- ⚪ Archivar (newsletters, notificaciones)
Para cada 🔴 y 🟡: resumen de 1 línea + BORRADOR de respuesta con mi estilo
(yo/estilo-escritura.md), guardado como borrador en Gmail.
Nunca envíes. Nunca borres. Informe en diario/<hoy>.md.
```

### Prueba

```text
/email-triage
```

Métrica: ¿cuántos borradores enviaste con cambios mínimos? Si < 50%, mejorá las reglas de estilo.

## 8. Expense Wrangler

### Construcción

```markdown
# Expense Wrangler
1. Buscá en Gmail recibos y facturas de la última semana (asunto o adjunto con
   factura/recibo/invoice/receipt) y archivos en raw/recibos/.
2. Extraé: fecha, comercio, CUIT/RUT si aparece, monto, moneda, medio de pago, categoría
   (Comida, Transporte, Software, Viajes, Oficina, Otros), deducible (sí/no/revisar).
3. Agregá las filas a salidas/gastos/gastos-2026.xlsx (hoja Datos) sin duplicar
   (clave: fecha+comercio+monto).
4. Hoja Resumen con fórmulas: total por categoría y mes; gráfico de barras.
5. Marcá en amarillo lo que no pudiste leer con certeza.
```

Plugin útil: **Finance** (`reconciliation`, `variance-analysis`).

### Prueba

```text
/expense-wrangler
```

Verificá 5 filas al azar contra el recibo original.

## 9. Content Machine

### Construcción

```markdown
# Content Machine
1. Ideas: revisá diario/ y wiki/log.md de la semana + Market Pulse; proponé 5 ideas
   alineadas con yo/redes.md y yo/objetivos.md. Esperá mi elección.
2. Para las elegidas: post de LinkedIn (skill posts-linkedin), carrusel de 6 slides
   con marca/ (skill pptx → PDF) y un hilo de X.
3. Autoevaluación contra yo/estilo-escritura.md (nota 1-10); reescribí si < 8.
4. Guardá en salidas/contenido/<fecha>/ y agregá al calendario de contenido
   (salidas/contenido/calendario.xlsx).
```

### Prueba

```text
/content-machine
```

Plugins útiles: **Marketing** (`content-creation`, `brand-review`) y **brand-voice**.

## 10. Weekly Executive Report

### Construcción

```markdown
# Weekly Executive Report
Cada viernes, un informe para mí (o mi jefe/equipo):
1. KPIs de la semana (de salidas/ y de las fuentes conectadas): cumplimiento del sprint,
   reuniones, contactos nuevos, gastos, contenido publicado.
2. Logros (3-5), bloqueos, decisiones tomadas (de las minutas).
3. Próxima semana: prioridades y riesgos.
4. Salidas: deck de 5 slides con marca/plantilla.pptx + PDF de 2 páginas.
5. Borrador de email con el PDF adjunto para la lista en yo/destinatarios-reporte.md.
```

### Prueba

```text
/weekly-report
```

Programalo: `/schedule` → *"Viernes 17:00, /weekly-report"*.

---

## 🧪 Práctica final: proyecto integrador

Implementá **al menos 5** de las 10 automatizaciones, con al menos **2 programadas** y **1 disparada por Dispatch**. Documentá en `automatizaciones/README.md`: qué hace cada una, disparador, conectores y cuánto tiempo te ahorra por semana.

### ✅ Criterios de calidad de una automatización

1. **Definición escrita** y versionada (no solo un prompt).
2. **Idempotente:** si la corrés dos veces, no duplica datos.
3. **Segura:** nada externo sin aprobación; no borra.
4. **Observable:** deja registro en el diario.
5. **Tolerante a fallos:** si un conector falla, sigue y avisa.
6. **Medible:** sabés cuánto tiempo te ahorra.

## 🧠 Autoevaluación

1. ¿Por qué la definición de una automatización va en un archivo y no solo en un prompt?
   <details><summary>Ver respuesta</summary>Porque se puede versionar, revisar y mejorar: cuando algo falla, se corrige el procedimiento y no hay que reescribir el prompt.</details>

2. ¿Qué significa que una automatización sea idempotente?
   <details><summary>Ver respuesta</summary>Que si la corrés dos veces no duplica datos ni acciones.</details>

3. ¿Qué requisito tiene Dispatch?
   <details><summary>Ver respuesta</summary>Plan Pro o Max, y la computadora encendida y despierta con Claude Desktop abierto. Las tareas programadas de Cowork, en cambio, corren en la nube.</details>

🎓 **¡Completaste el recorrido principal!** Seguí con los dos módulos de profundización.

➡️ Siguiente: [Módulo 14 — Funciones avanzadas que nadie te cuenta](14-funciones-avanzadas.md)
