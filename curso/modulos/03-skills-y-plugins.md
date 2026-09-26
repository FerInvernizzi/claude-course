# Módulo 03 — Agent Skills y Plugins en Cowork

> **🎯 Objetivos.** Al terminar este módulo vas a poder:
> - Explicar qué es una skill, su estructura y la carga progresiva.
> - Crear una skill propia con `skill-creator`.
> - Diferenciar skills de plugins e instalar un plugin.
> - Limpiar datos, hacer análisis estadístico, dashboards y slides con el plugin de datos.
> - Diseñar y empaquetar un plugin de finanzas propio.
>
> **Requisitos previos:** Módulos 01 y 02 · **Duración estimada:** 4 h

## 3.1 ¿Qué es una Agent Skill?

Una **Skill** es una carpeta con instrucciones, scripts y recursos que Claude **carga automáticamente cuando son relevantes** para la tarea. Es la forma de "enseñarle un oficio" a Claude una vez y reutilizarlo siempre.

> Analogía: Claude es un empleado brillante. Una skill es el **manual de procedimientos** de tu empresa para una tarea concreta.

### Estructura de una skill

```text
mi-skill/
├── SKILL.md          ← obligatorio: frontmatter + instrucciones
├── reference.md      ← opcional: documentación extra (se lee solo si hace falta)
├── ejemplos/         ← opcional: ejemplos de buenos resultados
├── plantillas/       ← opcional: plantillas .pptx, .docx, logos
└── scripts/
    └── validar.py    ← opcional: código que Claude ejecuta
```

### El archivo SKILL.md

```markdown
---
name: posts-linkedin
description: Redacta posts de LinkedIn con el tono y formato de la marca. Usar cuando
  el usuario pida un post, publicación o contenido para LinkedIn.
---

# Posts de LinkedIn

## Proceso
1. Pedí (o inferí) el tema, el público objetivo y el objetivo del post.
2. Leé `ejemplos/` para imitar el estilo.
3. Escribí 3 variantes: storytelling, lista de aprendizajes, opinión contraria.

## Reglas de formato
- Gancho en la primera línea (máx. 12 palabras).
- Párrafos de 1–2 líneas. Máximo 1.300 caracteres.
- Cerrá con una pregunta para generar comentarios.
- Máximo 3 hashtags, al final.
- Nada de emojis en exceso (máx. 2).
```

**Lo más importante es la `description`:** Claude decide si usar la skill leyendo solo el nombre y la descripción. Tiene que decir **qué hace y cuándo usarla**.

### Progressive disclosure (carga progresiva)

```text
Nivel 1: name + description      → siempre en contexto (muy pocos tokens)
Nivel 2: cuerpo de SKILL.md      → se carga cuando la tarea coincide
Nivel 3: archivos y scripts      → se leen/ejecutan solo si hacen falta
```

Por eso podés tener decenas de skills instaladas sin saturar el contexto.

### Skills incluidas de Anthropic

- **xlsx** — Excel con fórmulas, formato, gráficos.
- **pptx** — presentaciones PowerPoint.
- **docx** — documentos Word.
- **pdf** — leer, extraer, crear y rellenar PDFs.
- **frontend-design** — interfaces web con diseño de calidad (módulos 04 y 10).
- **skill-creator** — te ayuda a crear nuevas skills (¡usala!).

### Cómo instalar/crear skills en Cowork / Claude app

1. *Configuración → Capacidades/Skills* → activar las skills de ejemplo.
2. Subir una skill propia como `.zip` de la carpeta, o pedirle a Claude:
   ```text
   Usá skill-creator para crear una skill llamada "informe-semanal" que ...
   ```
3. En Claude Code, las skills viven en `~/.claude/skills/<nombre>/SKILL.md` (personales) o `.claude/skills/<nombre>/SKILL.md` (del proyecto).

## 3.2 Demo práctica: usar skills y crear posts de LinkedIn

1. Creá la carpeta `Marca/` con: `tono.md` (cómo habla tu marca), 3–5 posts que te gustaron en `ejemplos/`.
2. Pedile a Cowork:

```text
Usá la skill skill-creator para crear una skill "posts-linkedin" basada en mi carpeta
/Marca: extraé el tono, estructura y longitud de los ejemplos y convertilo en reglas.
Incluí en la skill una checklist de calidad que debas verificar antes de entregar.
```

3. Probala:

```text
Escribí un post de LinkedIn sobre cómo automatizamos el cierre contable con IA
y ahorramos 3 días por mes.
```

4. **Iterá la skill**, no solo el post: *"Actualizá la skill: los ganchos deben ser preguntas o cifras"*.

## 3.3 ¿Qué es un Plugin?

Un **Plugin** es un **paquete instalable** que agrupa varias piezas para un rol o flujo:

```text
mi-plugin/
├── .claude-plugin/
│   └── plugin.json        ← metadatos (nombre, versión, autor)
├── skills/                ← una o más skills
│   └── limpieza-datos/SKILL.md
├── commands/              ← slash commands (/analizar, /dashboard)
│   └── analizar.md
├── agents/                ← subagentes especializados
│   └── estadistico.md
├── hooks/                 ← automatismos ante eventos (opcional)
└── .mcp.json              ← conectores MCP que necesita (opcional)
```

| | Skill | Plugin |
|---|---|---|
| Qué es | Un "manual" para una tarea | Un "kit" completo para un rol |
| Contiene | SKILL.md + archivos | Skills + comandos + agentes + MCP + hooks |
| Se activa | Automáticamente por relevancia | Se instala; sus comandos se invocan con `/` |

Anthropic publica plugins de ejemplo para roles (datos, finanzas, legal, ventas, marketing, soporte, productividad…) en su marketplace. En Cowork: *Plugins → Explorar → Instalar*. En Claude Code: `/plugin` (módulo 09).

## 3.4 Demo: plugin de datos (Data Plugin)

### Parte 1 — Instalar y explorar

1. Instalá el plugin de **Datos / Data** desde el catálogo de plugins.
2. Escribí `/` en Cowork para ver los comandos que agrega (por ejemplo, explorar, limpiar, analizar, visualizar, construir dashboard — los nombres exactos dependen de la versión).
3. Generá un dataset de práctica:

```text
Generá "ventas_2025.csv" con 2.000 filas: fecha, id_cliente, region (Norte, Sur, Este,
Oeste), producto (8 productos), canal (Online, Tienda, Mayorista), unidades, precio,
descuento, satisfaccion (1-5). Introducí a propósito: 5% de valores faltantes, 20 filas
duplicadas, regiones mal escritas ("norte", "N0rte"), 10 outliers de precio y
fechas en 2 formatos distintos.
```

### Parte 2 — Limpieza de datos

```text
Hacé un perfil de calidad de ventas_2025.csv y después limpialo:
- Normalizá regiones y fechas.
- Eliminá duplicados exactos.
- Detectá outliers de precio con el método IQR; no los borres, marcálos en una columna.
- Imputá faltantes: numéricos con la mediana por producto, categóricos con la moda.
Entregá ventas_limpio.xlsx con una hoja "Log de limpieza" que documente cada cambio
(regla aplicada y filas afectadas).
```

**Clave:** el **log de limpieza** hace que el proceso sea auditable.

### Parte 3 — Visualización

```text
Con ventas_limpio.xlsx creá 6 visualizaciones que respondan:
1. ¿Cómo evolucionan las ventas por mes?
2. ¿Qué región y canal venden más?
3. ¿Qué productos tienen mejor margen después de descuentos?
4. ¿Hay relación entre descuento y satisfacción?
5. Distribución de ticket promedio.
6. Top 10 clientes.
Usá títulos que digan la conclusión (ej: "El canal Online crece 18% en el 2º semestre"),
no solo el tema.
```

## 🧪 Práctica: visualización de datos

Con el mismo dataset, pedile a Claude un **dashboard interactivo en HTML** de una sola página con: 4 KPIs arriba (ventas totales, ticket promedio, satisfacción media, % online), filtros por región y canal, y 3 gráficos. Debe verse bien en celular.

### ✅ Solución (prompt modelo)

```text
Construí dashboard.html (un solo archivo, usando Chart.js desde CDN) a partir de
ventas_limpio.xlsx:
- Fila de 4 tarjetas KPI: Ventas totales, Ticket promedio, Satisfacción media, % Online.
- Filtros (desplegables) por Región y Canal que actualicen KPIs y gráficos.
- Gráfico de líneas: ventas mensuales. Barras: ventas por producto. Dispersión:
  descuento vs satisfacción.
- Paleta sobria (azul/gris), tipografía legible, responsive para móvil.
- Incrustá los datos agregados en el HTML como JSON para que funcione sin servidor.
Abrilo y verificá que los filtros funcionan antes de entregarlo.
```

**Criterios de revisión:** los KPIs coinciden con el Excel; los filtros afectan a *todo*; los títulos son claros; se ve bien en pantalla chica.

### Parte 4 — Análisis estadístico y PowerPoint

```text
Hacé un análisis estadístico de ventas_limpio.xlsx:
1. Estadística descriptiva por región y canal.
2. ¿Las ventas medias difieren entre regiones? (ANOVA + post-hoc Tukey; verificá supuestos).
3. Correlación descuento–satisfacción (Pearson y Spearman) con interpretación.
4. Regresión lineal: unidades ~ precio + descuento + canal. Reportá coeficientes,
   p-valores y R².
Explicá cada resultado en lenguaje de negocio (sin jerga). Luego generá una presentación
de 8 slides "Insights de Ventas 2025" con la skill pptx: portada, resumen ejecutivo,
3 slides de hallazgos con gráfico, 1 de estadística, recomendaciones y próximos pasos.
```

> ⚠️ Pedí siempre que **verifique supuestos** y que diferencie correlación de causalidad.

## 3.5 Forecasting financiero con Cowork y Skills

```text
En /Finanzas tengo ingresos_mensuales_2021_2025.xlsx. Construí un forecast de 12 meses:
1. Analizá tendencia y estacionalidad (descomposición).
2. Compará 3 métodos: media móvil, suavizado exponencial (Holt-Winters) y regresión con
   estacionalidad. Usá los últimos 6 meses como validación y reportá MAPE de cada uno.
3. Elegí el mejor y generá 3 escenarios: base, optimista (+1 desvío), pesimista (–1 desvío).
4. Entregá forecast.xlsx con: hoja de supuestos editables (celdas azules), hoja de
   cálculo con fórmulas enlazadas a los supuestos y un gráfico con intervalos.
```

**Convención de modelado financiero** (pedísela siempre): **azul** = input/supuesto, **negro** = fórmula, **verde** = vínculo a otra hoja.

## 3.6 Demo: crear tu propio plugin de finanzas

### Parte 1 — Diseño

Decidí qué debe hacer el plugin. Ejemplo "finanzas-pyme":

| Componente | Nombre | Función |
|------------|--------|---------|
| Skill | `modelo-dcf` | Construir DCF con convenciones de color y chequeos |
| Skill | `cierre-mensual` | Checklist y conciliaciones del cierre |
| Comando | `/forecast` | Forecast de 12 meses a partir de un Excel |
| Comando | `/one-pager` | Resumen financiero de 1 página en PPT |
| Agente | `revisor-financiero` | Revisa modelos buscando errores de fórmulas |

### Parte 2 — Construcción

Tenés el plugin completo en [`plantillas/plugin-finanzas/`](../plantillas/plugin-finanzas/). Pedile a Cowork:

```text
Usá skill-creator para crear un plugin "finanzas-pyme" con esta estructura: [pegá la tabla].
Cada skill debe tener: cuándo usarse, proceso paso a paso, convenciones de formato,
y una checklist de verificación final.
```

### Parte 3 — Empaquetar, instalar y probar

1. Comprimí la carpeta del plugin en `.zip` (o subila a un repo de GitHub como marketplace).
2. Cowork → *Plugins → Subir/Instalar plugin*.
3. Probá cada comando: `/forecast ingresos.xlsx`, `/one-pager`.
4. Ajustá las skills según los errores que veas. **Un plugin es un producto: versionalo.**

## 🧪 Práctica: analizar datos con un plugin

Con tu plugin de datos (o el de finanzas), analizá un dataset de **RR.HH.** (generalo sintético: 500 empleados, departamento, antigüedad, salario, evaluación, horas extra, renunció sí/no). Objetivo: **¿qué factores explican la rotación?** Entregables: Excel limpio, 4 gráficos, análisis estadístico y 5 slides para el director de RR.HH.

### ✅ Solución (flujo)

1. **Generar datos** con relaciones plausibles (más horas extra y peor evaluación → más renuncias).
2. `Perfilá y limpiá` → Excel con log.
3. **Análisis:** tasa de rotación por departamento y rango de antigüedad; comparación de medias (renunció vs. no) con t‑test; **regresión logística** `renuncio ~ salario + horas_extra + evaluacion + antiguedad` → odds ratios interpretados ("cada 10 horas extra mensuales aumentan un X% las chances de renunciar").
4. **Gráficos:** barras de rotación por depto; boxplot de salario por estado; curva de rotación por antigüedad; importancia de factores.
5. **Slides:** 1) Resumen, 2) Dónde se concentra la rotación, 3) Qué la explica, 4) Costo estimado, 5) 3 recomendaciones accionables.
6. **Revisión:** ¿los números de las slides coinciden con el Excel? ¿Se aclara que es correlacional?

## 🧠 Autoevaluación

1. ¿Qué parte de una skill decide si Claude la usa?
   <details><summary>Ver respuesta</summary>El `name` y sobre todo la `description`: tiene que decir qué hace y cuándo usarla.</details>

2. ¿Qué contiene un plugin que no contiene una skill?
   <details><summary>Ver respuesta</summary>Puede agrupar varias skills, slash commands, subagentes, hooks y servidores MCP en un paquete instalable.</details>

3. ¿Por qué pedir un "log de limpieza" al limpiar datos?
   <details><summary>Ver respuesta</summary>Para que cada cambio sea auditable: qué regla se aplicó y a cuántas filas.</details>

➡️ Siguiente: [Módulo 04 — Claude Chat](04-claude-chat.md)
