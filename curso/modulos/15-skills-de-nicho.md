# Módulo 15 — Skills de nicho: arte, diseño y cualquier pasión

<img src="../assets/linea.svg" alt="" width="100%">

Claude no es solo para planillas y código. Con las skills y plugins correctos se convierte en **taller de arte generativo, estudio de diseño, productora de video y podcast, motor de videojuegos, tutor de matemática olímpica o agencia de redes**. Este módulo es un catálogo curado de **30 skills y plugins reales** (todos verificados en los marketplaces oficiales o en el repositorio de Anthropic), organizado por intereses, con un ejercicio para cada perfil.

## 🎯 Objetivos de aprendizaje

| # | Al terminar vas a poder… (conducta · condición · criterio) | Nivel (Bloom) | Evidencia |
|---|---|---|---|
| 15.1 | **Seleccionar** del catálogo al menos 3 skills o plugins adecuados a un interés propio, justificando cada elección con su función y su requisito (cuenta externa, API key o ninguno) | Evaluar · conceptual | Práctica 1 |
| 15.2 | **Instalar** skills de nicho desde el marketplace oficial de Anthropic y desde un marketplace de terceros, y **verificar** con `/skills` o `/plugin` que quedaron activas | Aplicar · procedimental | Práctica 1 |
| 15.3 | **Producir** una pieza creativa completa (obra generativa, póster, video, episodio de audio, prototipo de juego o diseño de interfaz) con una skill de nicho, iterando al menos dos veces sobre el resultado | Crear · procedimental | Práctica 2 |
| 15.4 | **Adaptar** con `skill-creator` una skill existente a tu estilo personal (paleta, tono, restricciones), de modo que, ante la misma consigna, tu variante cumpla al menos 3 reglas que la original no cumple | Crear · metacognitivo | Práctica 3 |

**Requisitos previos:** módulos 03 y 09 · **Duración estimada:** 2 h + tiempo libre de exploración

---

## 15.1 Cómo instalar skills de nicho

**Skills oficiales de ejemplo de Anthropic** (repositorio `anthropics/skills`):

```bash
# dentro de Claude Code
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

En Claude (web, escritorio o Cowork) las skills y plugins se agregan desde **Customize → Skills** y **Customize → Plugins** (en *Plugins* podés sumar `anthropics/skills` como marketplace con **Add marketplace**).

**Plugins de los marketplaces oficiales:**

```bash
/plugin marketplace add anthropics/claude-plugins-official
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install <nombre>@<marketplace>
```

> ⚠️ Varios plugins de partners (Canva, Figma, Adobe, Runway, Spotify, Unity…) **necesitan una cuenta en ese servicio** y a veces una API key o un plan pago del servicio. Leé el README de cada uno antes de instalarlo, e instalá solo lo que vas a usar: cada skill suma su descripción al contexto.

## 15.2 Catálogo (30)

### 🎨 Arte visual y generativo

| # | Skill / plugin | Qué hace | Requiere | Dónde |
|---|---|---|---|---|
| 1 | **algorithmic-art** | Arte generativo con p5.js: primero escribe una "filosofía algorítmica" (un manifiesto estético) y después la expresa en código con aleatoriedad por semilla, campos de flujo y partículas, con un visor interactivo para explorar parámetros | Nada | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) |
| 2 | **canvas-design** | Pósters, láminas y piezas de arte estático en PNG o PDF a partir de una filosofía de diseño original | Nada | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/canvas-design) |
| 3 | **slack-gif-creator** | GIFs animados optimizados (tamaño, cuadros, loops) para Slack o redes | Nada | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator) |
| 4 | **theme-factory** | 10 temas curados de colores y tipografías (*Arctic Frost*, *Botanical Garden*, *Midnight Galaxy*, *Golden Hour*…) para aplicar a slides, documentos o webs | Nada | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/theme-factory) |
| 5 | **/dataviz** | Guía de diseño para gráficos y dashboards: elige la forma según los datos y valida la paleta para daltonismo | Nada (incluida en Claude Code) | [Comandos](https://code.claude.com/docs/en/commands) |

### ✏️ Diseño gráfico, UI y marca

| # | Skill / plugin | Qué hace | Requiere | Dónde |
|---|---|---|---|---|
| 6 | **frontend-design** | Dirección estética con criterio para webs e interfaces, que evita el look de plantilla | Nada | [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| 7 | **/design** (Claude Design) | Bocetos de UI, flujos de pantallas, landing pages o pósters como mesas de trabajo en un lienzo | Plan de Claude con Design | [Comandos](https://code.claude.com/docs/en/commands) |
| 8 | **web-artifacts-builder** | Artifacts HTML complejos con React, Tailwind y shadcn/ui | Nada | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) |
| 9 | **brand-guidelines** | Plantilla para aplicar colores y tipografía de una marca; se adapta a la tuya | Nada | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) |
| 10 | **Design** (plugin) | Crítica de diseño, sistema de diseño, UX writing, auditorías de accesibilidad y handoff a desarrollo | Nada (conectores opcionales) | [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| 11 | **brand-voice** | Descubre tu voz de marca a partir de tus textos, genera guías aplicables y valida contenido nuevo contra ellas | Nada | [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| 12 | **canva** | Crear, editar, redimensionar y revisar la marca de diseños de Canva | Cuenta de Canva | [canva-sdks/canva-skills](https://github.com/canva-sdks/canva-skills) |
| 13 | **figma** | Leer archivos de diseño, componentes y tokens, y traducir diseños a código | Cuenta de Figma | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) |
| 14 | **adobe-for-creativity** | Herramientas de Creative Cloud para imágenes, vectores, diseño y video, con edición en lote y adaptación a plataformas | Cuenta de Adobe | [adobe/skills](https://github.com/adobe/skills) |
| 15 | **superdesign** | Diseños y rediseños de UI y gráficos de marketing en un lienzo infinito, con borradores ramificables | Cuenta de Superdesign | [superdesigndev/superdesign-skill](https://github.com/superdesigndev/superdesign-skill) |
| 16 | **miro** | Leer tableros de Miro, crear diagramas y mapas | Cuenta de Miro | [miroapp/miro-ai](https://github.com/miroapp/miro-ai) |

### 🎬 Video, audio y música

| # | Skill / plugin | Qué hace | Requiere | Dónde |
|---|---|---|---|---|
| 17 | **hyperframes** (HeyGen) | Escribís HTML y obtenés video: composiciones, animaciones GSAP, subtítulos, voz en off, visuales que reaccionan al audio y captura de sitios web a video | Ver README | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) |
| 18 | **runway-api** | Generación de video, imágenes y audio a escala: campañas, videos de producto e historias con varias tomas | API key de Runway | [runwayml/skills](https://github.com/runwayml/skills) |
| 19 | **save-to-spotify** | Episodios de audio con narración TTS, línea de tiempo y portada, guardados en Spotify | Cuenta de Spotify | [spotify/save-to-spotify](https://github.com/spotify/save-to-spotify) |
| 20 | **huggingface-skills** | Usar, entrenar y evaluar modelos abiertos, incluidos modelos de imagen, audio y música | Cuenta de Hugging Face | [huggingface/skills](https://github.com/huggingface/skills) |
| 21 | **togetherai-skills** | Inferencia de modelos de imagen, video y audio en la plataforma Together AI | API key de Together | [togethercomputer/skills](https://github.com/togethercomputer/skills) |

### 🎮 Videojuegos, 3D y mundos

| # | Skill / plugin | Qué hace | Requiere | Dónde |
|---|---|---|---|---|
| 22 | **unity** | Plugin oficial de Unity: desarrollo de juegos, monetización y optimización | Unity instalado | [Unity-Technologies/unity-agent-plugin](https://github.com/Unity-Technologies/unity-agent-plugin) |
| 23 | **unreal-engine-skills** | Controla Unreal Editor por MCP: actores, blueprints, materiales, Niagara, Sequencer | Unreal Engine instalado | [EpicGames/unreal-engine-skills-for-claude-code-plugin](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin) |
| 24 | **mapbox** | Mapas y apps con ubicación: herramientas geoespaciales y estilos de mapa (rutas de viaje, mapas ilustrados) | Cuenta de Mapbox | [mapbox/mapbox-agent-skills](https://github.com/mapbox/mapbox-agent-skills) |

### 📚 Aprender, pensar y explorar

| # | Skill / plugin | Qué hace | Requiere | Dónde |
|---|---|---|---|---|
| 25 | **playground** | Genera "playgrounds" interactivos en un solo HTML (controles visuales y vista previa en vivo) para explorar un concepto, una paleta o un dataset | Nada | [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| 26 | **math-olympiad** | Resuelve matemática de competencia (IMO, Putnam) con verificadores adversarios que atacan cada demostración; se abstiene antes que inventar | Nada | [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| 27 | **learn-with-coursera** | Tres preguntas (tema, nivel, formato) → el siguiente paso de aprendizaje en el catálogo de Coursera | Nada (cuenta para cursar) | [coursera/skills](https://github.com/coursera/skills) |
| 28 | **doc-coauthoring** | Flujo guiado para coescribir documentos largos (propuestas, ensayos, especificaciones) por etapas | Nada | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) |

### 🛍️ Creadores que venden o publican

| # | Skill / plugin | Qué hace | Requiere | Dónde |
|---|---|---|---|---|
| 29 | **postiz** | Programa publicaciones y mide analíticas en más de 28 redes (Instagram, TikTok, YouTube, LinkedIn, X…) | Cuenta de Postiz | [gitroomhq/postiz-agent](https://github.com/gitroomhq/postiz-agent) |
| 30 | **wix** | Crear, administrar y publicar sitios Wix (portfolio, tienda, blog) | Cuenta de Wix | [wix/skills](https://github.com/wix/skills) |

> 💡 ¿No está tu nicho? Revisá los marketplaces con `/plugin` (hay cientos) y, si no existe, **creala vos** con `skill-creator` (módulo 03): una skill de recetas de cocina con tus restricciones, de entrenamiento de running, de análisis de ajedrez, de escritura de canciones o de planificación de viajes es solo un `SKILL.md` bien escrito.

## 15.3 Recetas por perfil

**Artista generativo** (algorithmic-art + theme-factory)
```text
Usá la skill algorithmic-art. Quiero una serie de 3 obras inspiradas en las olas del
Río de la Plata al atardecer. Primero escribí la filosofía algorítmica; después el
sketch en p5.js con semilla configurable y controles para densidad, turbulencia y
paleta. Aplicá la paleta "Golden Hour" de theme-factory. Exportá 3 variaciones en PNG
con semillas distintas.
```

**Ilustrador o diseñador de pósters** (canvas-design)
```text
Usá canvas-design para un póster A3 de un festival de jazz en Montevideo, estilo
Bauhaus, tipografía geométrica, 3 colores planos. Entregá PDF para imprimir y PNG
para redes. Proponé dos direcciones antes de elegir una.
```

**Creador de video** (hyperframes)
```text
Con hyperframes, convertí esta receta de chipá en un video vertical de 30 segundos:
título animado, 5 pasos con texto en pantalla, subtítulos y un cierre con mi usuario.
Ritmo rápido, estética cálida.
```

**Podcaster** (save-to-spotify)
```text
Convertí mis notas de /notas/historia-del-tango.md en un episodio de 10 minutos:
guion con intro, 3 segmentos y cierre, narración TTS con tono cálido y una portada
simple. Mostrame el guion antes de generar el audio.
```

**Desarrollador de juegos** (unity o unreal)
```text
En este proyecto de Unity, creá un prototipo de juego de plataformas 2D: movimiento
con salto variable, 3 plataformas móviles y un coleccionable con contador. Explicá
cada script que crees.
```

**Diseñador de producto** (Design + frontend-design + figma)
```text
Hacé una crítica de diseño de esta pantalla (captura adjunta): jerarquía, contraste,
accesibilidad y UX writing. Priorizá 5 cambios y después implementalos con
frontend-design, respetando los tokens de nuestro archivo de Figma.
```

**Estudiante curioso** (playground + math-olympiad)
```text
Creá un playground interactivo que explique la serie de Fourier: sliders para la
cantidad de armónicos y la frecuencia, con el gráfico en vivo. Después proponeme
un problema olímpico relacionado y resolvelo con verificación adversaria.
```

---

## 🧪 Prácticas

### Práctica 1 — Tu kit personal (objetivos 15.1 y 15.2)

1. Elegí **tu** interés (arte, música, juegos, cocina, deporte, viajes…).
2. Seleccioná 3 skills o plugins del catálogo (o de `/plugin`) y completá: *qué hace · por qué la elegís · qué requiere*.
3. Instalá al menos una del marketplace de Anthropic y una de un tercero.
4. Verificá con `/skills` o `/plugin` que están activas.

**Criterios de éxito:** las 3 elecciones tienen justificación y requisito; `/skills` o `/plugin` muestran lo instalado.

### Práctica 2 — Una pieza terminada (objetivo 15.3)

Producí **una pieza completa** con una de tus skills (obra, póster, video, episodio, prototipo o pantalla). Guardá la versión 1, pedí al menos **dos iteraciones** con cambios concretos ("más contraste", "ritmo más lento", "otra semilla") y guardá la versión final.

**Criterios de éxito:** tenés v1 y vfinal; cada iteración cambia algo específico y visible; la pieza cumple el brief original.

### Práctica 3 — Hacela tuya (objetivo 15.4)

Con `skill-creator`, creá una variante de la skill que usaste con **tu estilo**: tu paleta, tu tono, tus restricciones (por ejemplo: *"nunca uses violeta", "siempre en formato vertical", "tipografías de Google Fonts sin serifas"*). Repetí la misma consigna con la skill original y con la tuya.

**Criterios de éxito:** la variante tiene una `description` clara de cuándo usarla; comparando las dos salidas, la tuya respeta al menos 3 de tus reglas y la original no.

## 📌 Ideas clave

- Instalá solo las skills que vas a usar: cada una suma contexto.
- Revisá qué cuenta o API key pide cada plugin de terceros.
- Las buenas skills creativas empiezan por un concepto o filosofía, no por una plantilla.
- Iterá con cambios concretos y guardá versiones.
- Si tu nicho no existe, creá la skill con `skill-creator`.

## 🧠 Autoevaluación

1. ¿Por qué no conviene instalar las 30 skills "por las dudas"?
   <details><summary>Ver respuesta</summary>Cada skill suma su descripción al contexto en cada sesión y aumenta la probabilidad de que Claude elija una skill equivocada. Conviene instalar solo lo que usás y desactivar el resto (<code>/skills</code> o <code>/skill-doctor</code> muestran el costo).</details>

2. ¿Qué tienen en común algorithmic-art y canvas-design en su método de trabajo?
   <details><summary>Ver respuesta</summary>Ambas empiezan por una <strong>filosofía</strong> o concepto estético escrito y recién después lo expresan: en código p5.js o en una pieza visual estática. Eso produce resultados originales en lugar de plantillas.</details>

3. Querés un video vertical con subtítulos a partir de un texto, sin herramientas de edición. ¿Qué plugin probás primero y qué revisás antes de instalarlo?
   <details><summary>Ver respuesta</summary><strong>hyperframes</strong> (HTML → video con subtítulos y animaciones). Antes, revisá en su README qué cuenta o credenciales necesita.</details>

## Fuentes oficiales

- [Repositorio oficial de skills de Anthropic](https://github.com/anthropics/skills) · [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)
- Cada fila del catálogo enlaza al repositorio del plugin; todos se verificaron con `git ls-remote` en septiembre de 2026.

➡️ Volvé al [índice del curso](../README.md).
