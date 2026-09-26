# Módulo 01 — Claude Cowork: fundamentos

<img src="../assets/linea.svg" alt="" width="100%">

## 🎯 Objetivos de aprendizaje

| # | Al terminar vas a poder… (conducta · condición · criterio) | Nivel (Bloom) | Evidencia |
|---|---|---|---|
| 1.1 | Configurar Cowork con una carpeta de trabajo dedicada, instrucciones globales y el modo de permiso adecuado, sin dar acceso a carpetas con credenciales | Aplicar · procedimental | Práctica |
| 1.2 | Formular un pedido con objetivo, entradas, formato de salida, restricciones y plan previo, de modo que Cowork muestre el plan y espere tu aprobación antes de modificar archivos | Aplicar · procedimental | Práctica |
| 1.3 | Generar, a partir de archivos crudos de tu área, un Excel con fórmulas (no valores pegados), formato y un resumen de hallazgos en el que cada conclusión cite su dato | Crear · procedimental | Práctica |
| 1.4 | Adaptar, a partir de casos reales, el patrón de pedido a 2 áreas distintas (finanzas, legal, marketing, datos o investigación), de modo que cada pedido declare entregable y criterio de revisión | Aplicar · procedimental | Práctica |

**Requisitos previos:** Módulo 00 · Claude Desktop instalado · **Duración estimada:** 1 h 30 min

## 1.1 ¿Qué es Claude Cowork?

**Claude Cowork** es el espacio de trabajo agéntico de Claude pensado para trabajo de conocimiento (no solo programadores). Usa la **misma arquitectura agéntica que Claude Code**, pero sin terminal: describís el resultado que querés y volvés más tarde a buscar el trabajo terminado.

- Está disponible en **Claude Desktop** (Mac y Windows), en **claude.ai** y en las apps móviles, en planes pagos (Pro, Max, Team y Enterprise).
- En el escritorio, **lee y escribe archivos de las carpetas que le das**, sin subir ni descargar nada a mano.
- Le describís una tarea en lenguaje natural; Claude **planifica, divide el trabajo en subtareas (con subagentes en paralelo si conviene), crea y modifica archivos** y te muestra el progreso.
- El código se ejecuta en un **entorno aislado**, separado de tu computadora y de tu red. Según el centro de ayuda, las tareas corren en servidores de Anthropic y **siguen aunque cierres la laptop**, salvo las que dependen de tu computadora (carpetas locales o apps de escritorio vía Dispatch). Las sesiones quedan en tu cuenta y las retomás desde cualquier dispositivo.
- Podés dejarlo trabajando en tareas largas mientras hacés otra cosa.

> ℹ️ Cowork cambia seguido. Este módulo sigue la documentación oficial de septiembre de 2026 ([Cowork overview](https://claude.com/docs/cowork/overview), [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)); si un menú tiene otro nombre en tu versión, buscá la función equivalente.

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

```text
 Objetivo ──► Plan (lista de tareas) ──► Ejecutar paso ──► Observar resultado
                     ▲                                          │
                     └────────── ajustar / siguiente paso ◄─────┘
                                                                │
                                                     Entregable final
```

### Componentes

1. **Carpetas de trabajo:** Cowork solo ve las carpetas que le das. Todo lo que crea queda ahí. Lee archivos individuales de hasta 50 MB.
2. **Entorno aislado:** ejecuta código (Python, etc.) separado de tu computadora y de tu red para procesar archivos, generar gráficos y crear `.xlsx`/`.pptx`/`.docx`/`.pdf`.
3. **Skills:** instrucciones empaquetadas (ej. la skill de Excel sabe crear hojas con fórmulas, formato y gráficos correctos). Ver módulo 03.
4. **Conectores (MCP):** acceso a Gmail, Google Drive, Calendar, Slack, Notion, etc. Ver módulo 02.
5. **Plugins:** paquetes de skills, conectores, subagentes y hooks para un rol (finanzas, datos, legal, marketing…). Todo se administra desde **Customize** en la barra lateral.
6. **Navegador (Claude in Chrome):** opcionalmente puede navegar la web por vos.
7. **Tareas programadas y Dispatch:** ejecuta tareas recurrentes (`/schedule`), y con Dispatch le delegás trabajo en segundo plano, incluso desde el celular (módulo 13).

### Permisos y seguridad

Cowork tiene tres modos de permiso, que elegís por tarea:

| Modo | Qué hace | Cuándo usarlo |
|------|----------|---------------|
| **Manual** | Claude pide tu aprobación antes de cada acción | Primeras veces, datos sensibles, acciones externas |
| **Auto** | Trabaja sin interrumpirte, pero una revisión de seguridad automática bloquea o te consulta lo riesgoso (exfiltración de datos, inyección de prompts). Consume algo más de uso | Tareas largas que ya conocés |
| **Skip** | Sin pausas ni revisión automática | Solo si confiás por completo en todos los archivos, conectores y acciones involucrados |

- Siempre pide permiso explícito antes de **borrar archivos de forma permanente**, en cualquier modo.
- **Buenas prácticas:** trabajá sobre **copias** de archivos importantes; no le des acceso a carpetas con credenciales; revisá las acciones externas (emails, mensajes) antes de aprobarlas.
- Cuidado con la **inyección de prompts**: un documento o web puede contener instrucciones maliciosas. Si Claude propone algo raro, frenalo.

### Contexto permanente: instrucciones y proyectos

Tres lugares donde Cowork guarda contexto para que no lo repitas en cada tarea:

- **Instrucciones globales** (*Settings*, instrucciones para Claude): tono, formato y rol que aplican a todas tus tareas. Ejemplo: *"Respondé en español rioplatense. Números con separador de miles. Siempre un resumen de 3 líneas al inicio."*
- **Instrucciones de carpeta:** contexto propio de la carpeta local que elegís. Claude las puede actualizar solo mientras trabaja, igual que un `CLAUDE.md` (módulo 09).
- **Proyectos de Cowork** (*Projects* → **+**): reúnen para un área de trabajo recurrente sus **carpetas locales, instrucciones, links de referencia, proyectos de claude.ai vinculados y una memoria propia** que persiste entre sesiones. Ideal para "Cierre mensual", "Cliente X" o "Tesis". Ojo: **viven solo en tu computadora** y no se comparten. Son distintos de los proyectos de claude.ai, aunque podés vincular uno para usar su conocimiento. Archivar un proyecto borra su configuración y su memoria, pero no toca tus carpetas.

**Consumo de uso:** las tareas de varios pasos consumen bastante más que una pregunta rápida (cada paso, archivo creado, conector o navegación suma). Agrupá trabajo relacionado, abrí una tarea nueva para cada tema distinto y revisá el consumo en *Settings → Usage*.

## 1.3 Primeros pasos

1. Descargá e instalá **Claude Desktop** (claude.ai/download) e iniciá sesión.
2. Abrí la pestaña/modo **Cowork**.
3. Elegí (o creá) una carpeta de trabajo, por ejemplo `~/Cowork/curso`.
4. Escribí tu primera tarea.

## 1.4 Demo práctica: organizar archivos y usar la skill de Excel

### Parte A — Organizar una carpeta caótica

**Preparación:** poné en la carpeta una mezcla de archivos (PDFs, imágenes, CSV, docs). Si no tenés, pedile:

```text
Creá en esta carpeta 25 archivos de ejemplo variados (facturas en PDF, fotos .jpg,
CSV de ventas, notas .txt y documentos .docx) con nombres desordenados, para practicar
la organización.
```

**Prompt de la demo:**

```text
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

```text
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
```text
Tengo los extractos bancarios de enero a marzo en /Extractos (PDF). Extraé todas las
transacciones a Excel, categorizalas (Nómina, Proveedores, Impuestos, Otros) y armá
un resumen de flujo de caja mensual con gráfico.
```

**Legal**
```text
Revisá los 12 contratos de /Contratos contra este checklist: plazo, renovación automática,
cláusula de rescisión, penalidades, jurisdicción, confidencialidad. Generá una matriz en
Excel (contrato × cláusula) con el texto citado y un semáforo de riesgo. No des consejo
legal definitivo; marcá lo que requiere revisión de un abogado.
```

**Marketing**
```text
Con el brief de /Brief.docx y el tono de marca de /Marca/tono.md, creá un calendario de
contenido de 4 semanas para LinkedIn e Instagram en Excel, y redactá los 8 primeros posts
en un Word.
```

**Investigación**
```text
Leé los 20 papers de /Papers. Hacé una tabla comparativa (autor, año, método, muestra,
hallazgo principal, limitaciones) y un informe de síntesis de 2 páginas en Word con
referencias en formato APA.
```

## 🧪 Práctica: tu primera automatización en Cowork

Elegí **tu área** (finanzas, legal, marketing, datos o investigación) y resolvé con Cowork una tarea real de principio a fin. Si hiciste la práctica del módulo 00, usá el pedido delegable que guardaste:

1. Prepará una carpeta con 10-20 archivos de trabajo (o pedile a Cowork que genere datos sintéticos realistas de tu área).
2. Escribí el pedido con la estructura: **objetivo + entradas + formato de salida + restricciones + "mostrame el plan"**.
3. El entregable debe incluir al menos un Excel con fórmulas (no valores pegados) y un resumen de hallazgos.
4. Iterá al menos dos veces sobre el resultado.

### ✅ Solución (ejemplo para Marketing)

```text
En /Campañas hay 12 CSV exportados de Meta Ads y Google Ads (enero a junio).
Objetivo: saber qué campañas conviene escalar y cuáles pausar.
1. Consolidá todo en Campañas_2025.xlsx, hoja "Datos", con columnas normalizadas
   (fecha, plataforma, campaña, inversión, clics, conversiones, ingresos).
2. Hoja "KPIs" con FÓRMULAS: CTR, CPC, CPA y ROAS por campaña y por mes.
3. Hoja "Gráficos": ROAS por campaña (barras) e inversión vs. ingresos por mes (líneas).
4. Un resumen de 5 bullets: qué escalar, qué pausar y por qué, con el dato de respaldo.
Restricciones: no borres los CSV originales; si hay campañas con nombres inconsistentes,
listalas antes de unificarlas. Mostrame el plan y esperá mi OK.
```

**Criterios de éxito:**
- [ ] Cowork mostró un plan y esperó tu aprobación antes de modificar archivos.
- [ ] Si cambiás un dato en "Datos", los KPIs se recalculan (hay fórmulas, no valores).
- [ ] Cada conclusión del resumen cita el número que la respalda.
- [ ] Los archivos originales siguen intactos.

## ✅ Resumen del módulo

- Cowork = Claude agéntico sobre **tus archivos**, con sandbox, skills, conectores y plugins.
- Estructura de un buen pedido: **objetivo + entradas + formato de salida + restricciones + "mostrame el plan"**.
- La skill de Excel produce hojas reales con fórmulas, formato y gráficos.

## 🧠 Autoevaluación

1. ¿Por qué conviene pedir "mostrame el plan y esperá mi OK"?
   <details><summary>Ver respuesta</summary>Porque podés corregir el rumbo antes de que Cowork mueva o modifique archivos, que es más barato que deshacer.</details>

2. ¿Por qué pedir fórmulas en lugar de valores en un Excel?
   <details><summary>Ver respuesta</summary>El libro queda auditable y se recalcula si cambian los datos.</details>

3. Nombrá dos buenas prácticas de seguridad en Cowork.
   <details><summary>Ver respuesta</summary>Trabajar sobre copias y dar acceso solo a la carpeta necesaria. También: revisar las acciones externas antes de aprobarlas y desconfiar de instrucciones que vengan dentro de documentos (inyección de prompts).</details>

## Fuentes oficiales

- [Cowork overview](https://claude.com/docs/cowork/overview) · [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Organize work with projects](https://claude.com/docs/cowork/guide/projects) · [Install plugins](https://claude.com/docs/cowork/guide/plugins)
- [Understanding usage and length limits](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits)

➡️ Siguiente: [Módulo 02 — MCP, conectores, tokens y contexto](02-mcp-conectores-tokens.md)
