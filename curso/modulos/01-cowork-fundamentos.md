# Módulo 01 — Claude Cowork: fundamentos

## 1.1 ¿Qué es Claude Cowork?

**Claude Cowork** es el modo agéntico de **Claude Desktop** pensado para trabajo de conocimiento (no solo programadores). Usa el mismo "motor" que Claude Code, pero con una interfaz visual:

- Le das acceso a **una carpeta** de tu computadora.
- Le describís una tarea en lenguaje natural.
- Claude **planifica, ejecuta en un entorno aislado (sandbox/VM), crea y modifica archivos**, y te muestra el progreso.
- Podés dejarlo trabajando en tareas largas mientras hacés otra cosa, y encolar varias tareas.

**Casos de uso por área:**

| Área | Ejemplos |
|------|----------|
| Finanzas | Consolidar extractos, conciliaciones, modelos de forecast, reportes mensuales |
| Legal | Revisar contratos contra un checklist, extraer cláusulas a Excel, comparar versiones |
| Marketing | Calendarios de contenido, análisis de campañas, posts para LinkedIn, briefs |
| Análisis de datos | Limpiar CSV, estadística descriptiva, dashboards, informes |
| Investigación | Leer decenas de PDFs, sintetizar hallazgos, bibliografía, informe final |
| Operaciones | Ordenar carpetas, renombrar archivos, extraer datos de facturas/recibos |

## 1.2 Capacidades y cómo funciona

### El ciclo agéntico

```
 Objetivo ──► Plan (lista de tareas) ──► Ejecutar paso ──► Observar resultado
                     ▲                                          │
                     └────────── ajustar / siguiente paso ◄─────┘
                                                                │
                                                     Entregable final
```

### Componentes

1. **Carpeta de trabajo:** Cowork solo ve lo que le das. Todo lo que crea queda ahí.
2. **Sandbox:** ejecuta código (Python, etc.) en un entorno aislado para procesar archivos, generar gráficos, crear `.xlsx`/`.pptx`/`.docx`/`.pdf`.
3. **Skills:** instrucciones empaquetadas (ej. la skill de Excel sabe crear hojas con fórmulas, formato y gráficos correctos). Ver módulo 03.
4. **Conectores (MCP):** acceso a Gmail, Google Drive, Calendar, Slack, Notion, etc. Ver módulo 02.
5. **Plugins:** paquetes de skills + comandos + conectores para un rol (finanzas, datos, legal, marketing…).
6. **Navegador (Claude in Chrome):** opcionalmente puede navegar la web por vos.
7. **Tareas programadas y Dispatch:** puede ejecutar tareas recurrentes y podés mandarle tareas desde el celular (módulo 13).

### Permisos y seguridad

- Claude pide confirmación antes de acciones sensibles (borrar, enviar emails, etc.).
- **Buenas prácticas:** trabajá sobre **copias** de archivos importantes; no le des acceso a carpetas con credenciales; revisá las acciones externas (emails, mensajes) antes de aprobarlas.
- Cuidado con la **inyección de prompts**: un documento o web puede contener instrucciones maliciosas. Si Claude propone algo raro, frenalo.

## 1.3 Primeros pasos

1. Descargá e instalá **Claude Desktop** (claude.ai/download) e iniciá sesión.
2. Abrí la pestaña/modo **Cowork**.
3. Elegí (o creá) una carpeta de trabajo, por ejemplo `~/Cowork/curso`.
4. Escribí tu primera tarea.

## 1.4 Demo práctica: organizar archivos y usar la skill de Excel

### Parte A — Organizar una carpeta caótica

**Preparación:** poné en la carpeta una mezcla de archivos (PDFs, imágenes, CSV, docs). Si no tenés, pedile:

```
Creá en esta carpeta 25 archivos de ejemplo variados (facturas en PDF, fotos .jpg,
CSV de ventas, notas .txt y documentos .docx) con nombres desordenados, para practicar
la organización.
```

**Prompt de la demo:**

```
Organizá esta carpeta:
1. Creá subcarpetas por tipo: /Facturas, /Imagenes, /Datos, /Documentos, /Otros.
2. Renombrá cada archivo con el formato AAAA-MM-DD_descripcion-corta.ext
   (usá la fecha que aparece en el contenido; si no hay, la fecha de modificación).
3. No borres nada. Si hay duplicados, movelos a /Duplicados.
4. Al terminar, generá un archivo INDICE.xlsx con: nombre original, nombre nuevo,
   carpeta destino, tipo y tamaño.
Antes de mover nada, mostrame el plan y esperá mi OK.
```

**Qué observar:**
- Claude muestra su **plan** y espera aprobación (porque se lo pediste).
- Crea una lista de tareas y la va tachando.
- Lee el contenido de los PDFs para inferir fechas.
- Usa la **skill de Excel** para el índice.

### Parte B — Skill de Excel: de datos crudos a reporte

```
En /Datos hay CSV de ventas. Consolidalos en un único Excel "Ventas_Consolidado.xlsx" con:
- Hoja "Datos": todas las filas, con columnas normalizadas (fecha ISO, región en mayúsculas,
  monto numérico).
- Hoja "Resumen": tabla dinámica de ventas por región y mes, usando FÓRMULAS (SUMIFS),
  no valores pegados.
- Hoja "Gráficos": gráfico de líneas de ventas mensuales y barras por región.
- Formato: encabezados en negrita con color, números con separador de miles, filas alternas.
Explicame al final qué problemas de calidad de datos encontraste.
```

**Puntos de aprendizaje:**
- Pedir **fórmulas** en lugar de valores hace que el Excel sea auditable y actualizable.
- Pedir que **reporte problemas de calidad** te da control sobre la limpieza.
- Podés iterar: *"Agregá una hoja con el top 10 de clientes"*.

## 1.5 Patrones de tareas para cada área

**Finanzas**
```
Tengo los extractos bancarios de enero a marzo en /Extractos (PDF). Extraé todas las
transacciones a Excel, categorizalas (Nómina, Proveedores, Impuestos, Otros) y armá
un resumen de flujo de caja mensual con gráfico.
```

**Legal**
```
Revisá los 12 contratos de /Contratos contra este checklist: plazo, renovación automática,
cláusula de rescisión, penalidades, jurisdicción, confidencialidad. Generá una matriz en
Excel (contrato × cláusula) con el texto citado y un semáforo de riesgo. No des consejo
legal definitivo; marcá lo que requiere revisión de un abogado.
```

**Marketing**
```
Con el brief de /Brief.docx y el tono de marca de /Marca/tono.md, creá un calendario de
contenido de 4 semanas para LinkedIn e Instagram en Excel, y redactá los 8 primeros posts
en un Word.
```

**Investigación**
```
Leé los 20 papers de /Papers. Hacé una tabla comparativa (autor, año, método, muestra,
hallazgo principal, limitaciones) y un informe de síntesis de 2 páginas en Word con
referencias en formato APA.
```

## ✅ Resumen del módulo

- Cowork = Claude agéntico sobre **tus archivos**, con sandbox, skills, conectores y plugins.
- Estructura de un buen pedido: **objetivo + entradas + formato de salida + restricciones + "mostrame el plan"**.
- La skill de Excel produce hojas reales con fórmulas, formato y gráficos.

➡️ Siguiente: [Módulo 02 — MCP, conectores, tokens y contexto](02-mcp-conectores-tokens.md)
