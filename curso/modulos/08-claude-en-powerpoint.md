# Módulo 08 — Claude en PowerPoint e informes ejecutivos

## 8.1 Objetivos e instalación del add‑in

**Objetivos:** crear presentaciones desde cero, agregar notas del orador, mejorar el diseño, traer contenido de fuentes online y PDFs, resumir decks existentes, usar plantillas de marca y practicar la presentación con Claude como coach.

**Instalación:** PowerPoint (365) → **Inicio → Complementos → Obtener complementos** → buscar **Claude** (Anthropic) → Agregar → iniciar sesión en el panel lateral.

**Dos caminos para crear decks:**

| Camino | Cuándo |
|--------|--------|
| **Add‑in en PowerPoint** | Editar/mejorar un deck abierto, usar el patrón de diapositivas de tu empresa, iteración visual |
| **Skill `pptx` en Chat/Cowork** | Generar decks completos desde datos, PDFs o investigación, en lote o automatizado |

## 8.2 Crear presentaciones con Claude

```
Creá una presentación de 10 diapositivas: "Plan de expansión a Chile 2026" para el
directorio. Estructura: portada, resumen ejecutivo, contexto de mercado, oportunidad,
propuesta, plan en 3 fases, inversión y retorno, riesgos y mitigaciones, decisión
requerida, anexo. Un mensaje principal por slide como título (títulos-acción).
Máximo 5 bullets por slide, 12 palabras por bullet.
```

**Principio de consultoría:** el **título de cada slide es la conclusión** ("Chile ofrece USD 40M de mercado accesible"), no el tema ("Mercado").

## 8.3 Notas del orador

```
Agregá notas del orador a todas las diapositivas: 120-150 palabras cada una, lenguaje
conversacional, con una transición a la siguiente slide y los datos clave para responder
preguntas. Marcá en [corchetes] dónde hacer pausas.
```

## 8.4 Mejorar el diseño

```
Mejorá el diseño de todo el deck respetando el patrón de la plantilla:
- Convertí listas largas en diagramas (proceso, comparación, línea de tiempo).
- Jerarquía clara: un elemento dominante por slide.
- Alineá todo a la grilla, márgenes consistentes, máx. 2 tipografías.
- Reemplazá tablas densas por gráficos cuando ayude.
Decime qué cambiaste en cada slide.
```

## 8.5 Agregar slides desde fuentes online y cambiar el tono

```
Buscá datos recientes sobre adopción de pagos digitales en Chile (fuente oficial) y
agregá 2 slides después de la 3 con un gráfico y la fuente citada al pie.
Después reescribí todo el deck con un tono más inspirador para una reunión con
inversores (sin exagerar cifras).
```

## 8.6 Slides desde PDFs

```
A partir del PDF adjunto (informe de 40 páginas), creá 8 slides: 1 de resumen ejecutivo,
5 de hallazgos (una idea por slide, con el dato y número de página de la fuente en el pie),
1 de implicancias, 1 de próximos pasos.
```

## 8.7 Resumir y organizar decks existentes

```
Este deck tiene 45 slides. 1) Hacé un índice con el mensaje de cada slide. 2) Detectá
duplicados y contradicciones. 3) Proponé una versión de 15 slides con storyline claro
(situación → complicación → resolución) y movés el resto a Anexo.
```

## 8.8 Presentaciones desde una plantilla de marca

1. Guardá la plantilla corporativa (`.potx` o `.pptx`) con: patrón de diapositivas, diseños, colores y fuentes del tema, logo.
2. Con el add‑in: abrí un archivo basado en la plantilla y pedí que use **solo los diseños del patrón**.
3. Con la skill `pptx` (Cowork):

```
Usá /Marca/plantilla.pptx como base (sus layouts, colores y fuentes; no inventes otros).
Generá el informe mensual de ventas a partir de /Datos/ventas_octubre.xlsx: portada,
KPIs, 3 slides de análisis con gráficos nativos (editables), conclusiones. Logo en
/Marca/logo.png solo en portada y cierre.
```

**Automatización de informes ejecutivos:** convertí ese prompt en una **skill** (`informe-mensual`) o en un **slash command**, y programalo (módulo 13 — Weekly Executive Reporting).

## 8.9 Claude como coach de presentación

```
Voy a presentar este deck en 10 minutos al directorio. Actuá como coach:
1. Estimá el tiempo por slide y decime dónde me voy a pasar.
2. Hacé las 10 preguntas más difíciles que podría hacer el directorio y cómo responderlas.
3. Sugerí un inicio de 30 segundos que capte la atención y un cierre con llamado a la acción.
4. Te voy a pegar mi guion: marcá muletillas, frases largas y jerga.
```

## 8.10 Claude vs Copilot vs NotebookLM

| Criterio | Claude (add‑ins + Cowork) | Microsoft Copilot | Google NotebookLM |
|----------|---------------------------|-------------------|-------------------|
| Fuerte en | Razonamiento, redacción, análisis, crear archivos complejos, agentes | Integración profunda con M365 (Outlook, Teams, SharePoint) | Estudiar y consultar **tus fuentes** con citas; resúmenes en audio |
| Excel / PPT | Add‑ins + skills xlsx/pptx; modelos complejos | Nativo en Office | No edita Office |
| Datos de la empresa | Vía conectores MCP | Microsoft Graph (nativo) | Solo lo que subís |
| Automatización/agentes | Cowork, Claude Code, plugins, subagentes | Copilot Studio | Limitada |
| Ideal para | Análisis y entregables de calidad, flujos agénticos | Empresas 100% Microsoft | Investigación y aprendizaje sobre documentos |

**Conclusión práctica:** no son excluyentes. Muchos equipos usan NotebookLM para estudiar fuentes, Copilot para el día a día en M365 y Claude para análisis, modelos y automatizaciones de extremo a extremo.

➡️ Siguiente: [Módulo 09 — Claude Code: fundamentos](09-claude-code-fundamentos.md)
