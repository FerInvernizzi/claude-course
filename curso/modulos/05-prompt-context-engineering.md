# Módulo 05 — Prompt Engineering y Context Engineering

## 5.1 Fundamentos: qué es un buen prompt

Un prompt es una **especificación de trabajo**. Claude no puede leer tu mente: todo lo que no escribís, lo tiene que adivinar.

### La fórmula de 6 componentes

| Componente | Pregunta | Ejemplo |
|-----------|----------|---------|
| **Rol / perspectiva** | ¿Desde qué experiencia? | "Sos analista senior de FP&A" |
| **Tarea** | ¿Qué hacer exactamente? | "Analizá la variación presupuesto vs real" |
| **Contexto** | ¿Por qué, para quién, con qué? | "Para el CFO, que decidirá recortes el lunes" |
| **Formato** | ¿Cómo se entrega? | "Tabla + 5 bullets + Excel" |
| **Restricciones** | ¿Qué evitar / límites? | "Máx. 1 página, sin jerga, no inventar cifras" |
| **Ejemplos** | ¿Cómo se ve lo bueno? | "Así se veía el informe del mes pasado: ..." |

### Antes / después

❌ *"Hacé un resumen de este contrato."*

✅
```
Sos abogado corporativo. Resumí el contrato adjunto para el gerente comercial (no abogado),
que debe decidir hoy si lo firma.
Formato:
1. Qué nos obliga (5 bullets máx.)
2. Riesgos principales, ordenados por gravedad, citando la cláusula.
3. Qué cláusulas negociaría y por qué.
Restricciones: lenguaje simple, máx. 400 palabras. Si algo es ambiguo, decilo; no supongas.
```

### Principios

1. **Sé explícito y específico.** Si querés "algo excelente, con todos los detalles", pedilo.
2. **Explicá el porqué.** "Usá frases cortas *porque lo leerán en el celular*" → Claude generaliza mejor.
3. **Decí qué hacer, no solo qué no hacer.** "Escribí en párrafos fluidos" > "no uses bullets".
4. **Ejemplos coherentes.** Claude imita mucho los ejemplos: que sean exactamente lo que querés.
5. **Pedí verificación.** "Antes de entregar, verificá X, Y, Z".

## 5.2 Técnicas avanzadas

### 1. Etiquetas XML para estructurar

```
<contexto>Empresa SaaS B2B, 40 empleados, churn mensual 3%.</contexto>
<datos>{{pegar CSV}}</datos>
<tarea>Identificá los 3 segmentos con mayor churn y proponé acciones.</tarea>
<formato>Tabla markdown + recomendaciones numeradas.</formato>
```

Separa claramente instrucciones de datos (y reduce el riesgo de que el modelo confunda datos con instrucciones).

### 2. Few‑shot (ejemplos)

```
Clasificá el sentimiento y el tema de cada reseña.
Ejemplo: "La app se cuelga al pagar" → {sentimiento: negativo, tema: pagos}
Ejemplo: "Me encantó la atención de Sofía" → {sentimiento: positivo, tema: soporte}
Reseñas: ...
```

### 3. Pensamiento paso a paso / extended thinking

Para problemas complejos: *"Pensá el problema paso a paso antes de responder"* o activá el **pensamiento extendido** en la interfaz. Útil en matemáticas, lógica, debugging, estrategia.

### 4. Encadenamiento de prompts (prompt chaining)

Dividí tareas grandes en etapas con salidas intermedias revisables:

```
Etapa 1: Extraé los datos → revisás
Etapa 2: Analizá → revisás
Etapa 3: Redactá el informe → revisás
Etapa 4: Autocrítica y versión final
```

### 5. Autocrítica / reflexión

```
Ahora revisá tu respuesta como si fueras un revisor exigente: listá 5 debilidades
y entregá una versión mejorada.
```

### 6. Rol + audiencia

"Explicalo como consultor de McKinsey a un CEO" produce estructura piramidal; "como profesor a estudiantes de 1er año" produce didáctica.

### 7. Prefijar el formato de salida

"Respondé solo con JSON válido con las claves: `nombre`, `monto`, `fecha`" — ideal para automatizaciones.

### 8. Pedir preguntas primero

```
Antes de empezar, hacé las preguntas que necesites para hacerlo bien (máx. 5).
```

### Prompts para generación de código avanzada

```
Contexto: API en Next.js 15 (App Router) + TypeScript + Prisma + PostgreSQL.
Tarea: endpoint POST /api/pedidos que cree un pedido con sus ítems en una transacción.
Requisitos:
- Validación con Zod; errores 400 con mensajes claros.
- Verificar stock y descontarlo atómicamente.
- Tests con Vitest: caso feliz, stock insuficiente, payload inválido.
Seguí el estilo de src/app/api/clientes/route.ts. No agregues dependencias nuevas.
Primero proponé el diseño; después implementá; al final corré los tests.
```

## 5.3 Context Engineering

**Prompt engineering** = cómo escribís *una* instrucción.
**Context engineering** = diseñar **todo lo que entra en la ventana de contexto** del agente a lo largo de una tarea: instrucciones del sistema, memoria (CLAUDE.md), skills, herramientas, archivos, historial y resultados.

> En agentes que trabajan horas, el contexto es el recurso más escaso. El objetivo es: **el conjunto mínimo de tokens de alta señal que maximiza la probabilidad del resultado deseado.**

### Las 4 estrategias

| Estrategia | Qué es | Cómo en Claude |
|-----------|--------|----------------|
| **Escribir** (persistir fuera) | Guardar info fuera del contexto para recuperarla | `CLAUDE.md`, archivos de notas/`progress.md`, memoria del Project |
| **Seleccionar** | Traer solo lo relevante, cuando hace falta | Skills (carga progresiva), búsqueda en archivos, referencias `@archivo` |
| **Comprimir** | Resumir lo acumulado | `/compact`, resúmenes intermedios, pedir "resumí el estado en 10 líneas" |
| **Aislar** | Separar trabajo en contextos distintos | **Subagentes**, sesiones nuevas por tarea, Agent Teams (módulo 11) |

### Técnicas concretas

1. **Archivo de memoria del proyecto (`CLAUDE.md`)**: comandos, convenciones, arquitectura. Corto y actualizado (módulo 09).
2. **Notas de progreso**: en tareas largas, pedí *"Mantené un archivo PROGRESO.md con lo hecho, decisiones y pendientes"*. Si el contexto se reinicia, Claude lo relee.
3. **Just‑in‑time**: en vez de pegar 30 archivos, dejá que el agente busque (`grep`, lectura parcial) cuando lo necesite.
4. **Pocas herramientas, bien descritas**: desactivá MCPs irrelevantes.
5. **Subagentes para exploración**: la investigación ruidosa ocurre en otro contexto; vuelve solo el resumen.
6. **Planes explícitos**: un plan escrito en un archivo sirve de "ancla" para no perder el rumbo.

## 5.4 Plantillas reutilizables

**Análisis**
```
<rol>Analista senior de {{área}}</rol>
<objetivo>{{decisión que se va a tomar}}</objetivo>
<audiencia>{{quién lo lee}}</audiencia>
<datos>{{archivos o datos}}</datos>
<entregable>{{formato exacto}}</entregable>
<criterios>Citá los datos que respaldan cada conclusión. Marcá supuestos. Máx {{N}} palabras.</criterios>
```

**Contenido**
```
Público: {{}} | Objetivo: {{informar/persuadir/vender}} | Canal: {{}}
Tono: {{}} | Longitud: {{}} | Llamado a la acción: {{}}
Ejemplos de estilo: {{}}
Entregá 3 variantes con enfoques distintos y decí cuál recomendás y por qué.
```

**Resolución de problemas**
```
Problema: {{}}. Lo que ya probé: {{}}. Restricciones: {{}}.
1) Reformulá el problema. 2) Listá hipótesis de causa ordenadas por probabilidad.
3) Proponé cómo verificar cada una. 4) Recomendá la solución y el plan B.
```

## 🧪 Práctica

Reescribí este prompt aplicando la fórmula y al menos 3 técnicas: *"Haceme un plan de marketing para mi cafetería."*

### ✅ Solución

```
<rol>Consultor de marketing para negocios gastronómicos locales.</rol>
<contexto>Cafetería de especialidad en Córdoba (barrio universitario), 2 años abierta,
ticket promedio $6.000, clientes: estudiantes y trabajadores remotos. Presupuesto
mensual de marketing: $300.000. Problema: ventas bajas de 15 a 19 h.</contexto>
<tarea>Diseñá un plan de marketing de 90 días enfocado en aumentar las ventas de la tarde.</tarea>
<formato>
1. Diagnóstico (5 bullets)
2. 3 estrategias priorizadas, cada una con: acciones, costo, KPI y meta
3. Calendario semanal en tabla
</formato>
<restricciones>Acciones ejecutables por 2 personas sin agencia. Nada de TV/radio.</restricciones>
Antes de responder, hacé hasta 3 preguntas si falta información clave.
Al final, criticá tu plan: ¿qué podría fallar?
```

Técnicas aplicadas: rol, XML, contexto rico, formato explícito, restricciones, preguntas previas y autocrítica.

➡️ Siguiente: [Módulo 06 — Claude en Excel](06-claude-en-excel.md)
