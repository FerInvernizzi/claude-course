# Módulo 03 — Agent Skills y Plugins en Cowork

<img src="../assets/linea.svg" alt="" width="100%">

## 🎯 Objetivos de aprendizaje

| # | Al terminar vas a poder… (conducta · condición · criterio) | Nivel (Bloom) | Evidencia |
|---|---|---|---|
| 3.1 | Explicar, usando un SKILL.md de ejemplo, cómo la carga progresiva decide qué partes de una skill entran al contexto y cuándo, identificando correctamente sus 3 niveles (descripción, cuerpo, archivos) | Comprender · conceptual | Autoevaluación |
| 3.2 | Crear con `skill-creator` una skill propia con una `description` que diga qué hace y cuándo usarla, y verificar que se activa sola con un pedido que no la nombra | Crear · procedimental | Práctica |
| 3.3 | Diferenciar, dado un caso de uso, si corresponde una skill, un plugin, un slash command o un subagente, justificando con la tabla del módulo | Analizar · conceptual | Autoevaluación |
| 3.4 | Limpiar un dataset con el plugin de datos, dejando un log de limpieza con regla aplicada y filas afectadas en cada paso | Aplicar · procedimental | Práctica |
| 3.5 | Producir, a partir de un dataset limpio, un análisis estadístico con supuestos verificados, un dashboard y 5 slides cuyos números coincidan con el Excel | Crear · procedimental | Práctica |
| 3.6 | Empaquetar un plugin propio con al menos una skill, un comando y un subagente, que pase `claude plugin validate` | Crear · procedimental | Práctica |

**Requisitos previos:** Módulos 01 y 02 · **Duración estimada:** 4 h

### 🗺️ Ruta de estudio (4 sesiones)

| Sesión | Secciones | Resultado |
|---|---|---|
| 1 · 60 min | 3.1 a 3.3 | Tu primera skill (posts de LinkedIn) funcionando |
| 2 · 60 min | 3.4, partes 1 a 3, y la práctica de visualización | Dataset limpio con log y dashboard HTML |
| 3 · 60 min | 3.4, parte 4, y 3.5 | Análisis estadístico, slides y forecast |
| 4 · 60 min | 3.6 y la práctica final | Plugin propio validado y análisis de RR.HH. |


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

1. Requisito: activá **Code execution and file creation** en *Settings → Capabilities* (las skills corren en el entorno de código de Claude). Disponible en planes Pro, Max, Team y Enterprise.
2. Abrí **Customize → Skills** (en claude.ai o en la app de escritorio). La pestaña *Your skills* agrupa las tuyas por origen (creadas por vos, de tu organización, compartidas, de Anthropic y partners), y *Discover* muestra las que podés agregar. Activá cada una con **Turn on**.
3. Para usar una a propósito, escribí `/` en el cuadro de mensaje y elegila. Si no, Claude la carga sola cuando tu pedido coincide con su descripción.
4. Para crear una propia, subí la carpeta de la skill o pedíselo a Claude:
   ```text
   Usá skill-creator para crear una skill llamada "informe-semanal" que ...
   ```
5. En Claude Code, las skills viven en `~/.claude/skills/<nombre>/SKILL.md` (personales) o `.claude/skills/<nombre>/SKILL.md` (del proyecto). **Ojo:** Cowork **no lee** la carpeta `~/.claude` de tu computadora; carga las skills y plugins habilitados en tu cuenta de claude.ai. Para usar en Cowork una skill que solo tenés en `~/.claude`, agregala desde *Customize*.

Las skills siguen un estándar abierto ([Agent Skills](https://agentskills.io/specification)), así que una skill que escribís para Claude también funciona en otras herramientas que lo adopten.

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

Anthropic publica plugins de ejemplo para roles (datos, finanzas, legal, ventas, marketing, soporte, productividad…) en su marketplace. En Cowork: **Customize → Plugins → Discover** → elegí el plugin → **Install**. Instalar no conecta los conectores que trae: después abrí la pestaña *Connectors* del plugin y conectá cada uno. Un plugin instalado queda guardado en tu cuenta, así que sus skills y conectores también están disponibles en el chat y en Claude Code. En Claude Code: `/plugin` (módulo 09).

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

1. Comprimí la carpeta del plugin en `.zip`, o subila a un repositorio de GitHub.
2. En Cowork → **Customize → Plugins**: usá la opción de subir un archivo, o **Add marketplace** con la URL del repositorio (acepta `https://github.com/usuario/repo` o `usuario/repo`). Con **Check for updates** o **Sync automatically** recibís las nuevas versiones.
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

## 📌 Ideas clave

- Una skill es una carpeta con `SKILL.md`; su `description` decide cuándo se usa.
- La carga progresiva hace que tener muchas skills cueste poco contexto.
- Un plugin empaqueta skills, comandos, subagentes, hooks y conectores; se instala desde *Customize → Plugins* o `/plugin`.
- Al limpiar datos, dejá un log; al analizar, verificá los supuestos; al presentar, que los números coincidan.
- Un plugin propio es un producto: validalo (`claude plugin validate`) y versionalo.

## 🧠 Autoevaluación

1. ¿Qué parte de una skill decide si Claude la usa?
   <details><summary>Ver respuesta</summary>El `name` y sobre todo la `description`: tiene que decir qué hace y cuándo usarla.</details>

2. ¿Qué contiene un plugin que no contiene una skill?
   <details><summary>Ver respuesta</summary>Puede agrupar varias skills, slash commands, subagentes, hooks y servidores MCP en un paquete instalable.</details>

3. ¿Por qué pedir un "log de limpieza" al limpiar datos?
   <details><summary>Ver respuesta</summary>Para que cada cambio sea auditable: qué regla se aplicó y a cuántas filas.</details>

## Fuentes oficiales

- [Skills overview](https://claude.com/docs/skills/overview) · [Create custom skills](https://claude.com/docs/skills/how-to) · [Especificación Agent Skills](https://agentskills.io/specification)
- [Plugins](https://claude.com/docs/plugins/overview) · [Install plugins in Cowork](https://claude.com/docs/cowork/guide/plugins) · [Plugins en Claude Code](https://code.claude.com/docs/en/plugins/overview)
- [Repositorio oficial de skills de Anthropic](https://github.com/anthropics/skills) · [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

➡️ Siguiente: [Módulo 04 — Claude Chat](04-claude-chat.md)
