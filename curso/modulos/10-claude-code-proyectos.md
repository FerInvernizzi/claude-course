# Módulo 10 — Claude Code: proyectos full‑stack de punta a punta

En este módulo construís 4 proyectos reales: landing pages (con y sin skill), un slash command de marca, un plugin de análisis de competencia y una app full‑stack con IA (Calorie Tracker), mejorada con **Ralph Loops** y desplegada en internet.

> **Plugins usados:** `frontend-design`, `plugin-dev`, `ralph-loop`, `feature-dev`, `code-review`, `marketing`. Ya están declarados en [`.claude/settings.json`](../../.claude/settings.json) de este repo.

---

## Proyecto 1 — Landing pages

### Parte A: sin skill (la línea base)

```bash
mkdir landing-cafe && cd landing-cafe && claude
```

```
Creá una landing page para "Tostado", una cafetería de especialidad en Rosario.
Secciones: hero, sobre nosotros, menú destacado (6 ítems), testimonios, ubicación y
horario, footer con redes. HTML + CSS + JS vanilla en un solo index.html, responsive.
Abrila en el navegador cuando termine.
```

Para la **vista previa en vivo**: `npx serve .` (o `python3 -m http.server`) y abrí `http://localhost:3000` (o `:8000`). En la app de escritorio, Claude Code muestra la vista previa integrada.

**Observá el resultado:** funciona, pero suele verse "genérico de IA": degradado violeta, tarjetas iguales, tipografía por defecto, emojis como íconos.

### Qué es la skill Front‑End Design

Es una skill oficial de Anthropic que le da a Claude **criterio de diseño**: elegir una dirección estética específica para el tema (no plantillas), tipografía con personalidad, jerarquía, composición, detalles y animaciones con intención. Parte de una premisa: *"actuá como director de diseño de un estudio cuyo cliente ya rechazó propuestas genéricas"*.

### Instalar la skill

```bash
# dentro de Claude Code
/plugin marketplace add anthropics/claude-plugins-official
/plugin install frontend-design@claude-plugins-official
```

O manualmente: copiá la carpeta de la skill a `~/.claude/skills/frontend-design/` (personal) o `.claude/skills/frontend-design/` (proyecto). Verificá con `/skills` o preguntando *"¿Qué skills tenés disponibles?"*.

### Parte B: con la skill

```
Usando la skill frontend-design, rediseñá la landing de Tostado. Antes de codear,
proponé 2 direcciones estéticas distintas (paleta, tipografías de Google Fonts,
concepto visual, tratamiento del hero) inspiradas en el mundo del café de especialidad.
Elegimos una y la implementás.
```

**Compará A vs B** en: identidad propia, tipografía, jerarquía, espacio en blanco, microinteracciones, coherencia con el rubro.

### ¿Por qué existen las carpetas `.agents/` y `.claude/` con el mismo SKILL.md?

Algunos instaladores de skills (por ejemplo, herramientas de la comunidad como `npx skills add ...`) guardan la skill en una carpeta **neutral** `.agents/skills/` para que la usen **varios agentes** (Claude Code, Codex, Cursor, etc.) y crean una copia o **enlace simbólico** en `.claude/skills/`, que es donde Claude Code busca. Resultado: ves el mismo `SKILL.md` en ambos lugares.

- Claude Code **solo lee** `.claude/skills/` (proyecto) y `~/.claude/skills/` (personal), además de las skills de plugins.
- Si editás una skill, editá la **fuente** (si es symlink, cualquiera de las dos rutas apunta al mismo archivo; si es copia, mantenelas sincronizadas o borrá una).

### 🧪 Práctica: landing page para una peluquería canina

Construí la landing de **"Patitas Spa"** (peluquería canina a domicilio). Requisitos: hero con CTA "Reservar turno", servicios con precios, cómo funciona (3 pasos), galería antes/después, preguntas frecuentes (acordeón), formulario de reserva con validación y botón de WhatsApp flotante.

### ✅ Solución

```
Usando la skill frontend-design, creá la landing de "Patitas Spa", peluquería canina a
domicilio en Montevideo. Público: dueños de perros de 25-45 años que valoran la
comodidad. Tono: cálido, divertido, confiable.

Estructura:
1. Hero: titular con beneficio ("Tu perro, bañado y feliz, sin salir de casa"), CTA
   "Reservar turno", ilustración/imagen cálida.
2. Servicios (baño, corte, uñas, spa completo) con precio y duración.
3. Cómo funciona: 3 pasos con íconos SVG propios (no emojis).
4. Galería antes/después con slider comparativo.
5. FAQ en acordeón accesible (teclado + aria-expanded).
6. Formulario de reserva: nombre, teléfono, raza, tamaño, servicio, fecha; validación
   en el cliente con mensajes claros.
7. Botón flotante de WhatsApp.

Técnico: un solo index.html (o Vite si lo preferís), responsive mobile-first, Lighthouse
accesibilidad > 90. Antes de codear, proponé 2 direcciones visuales. Al terminar,
levantá un servidor local, revisá en ancho 375px y 1440px y corregí lo que se rompa.
```

**Checklist de evaluación:** ¿Se ve distinto a una plantilla? ¿El CTA es visible sin scrollear en móvil? ¿El formulario valida? ¿El acordeón funciona con teclado?

---

## Proyecto 2 — Tu slash command de marca

**Objetivo:** un comando `/brand-landing` que genere cualquier landing respetando **tu** identidad de marca.

### Parte 1 — Carpeta de marca

```
marca/
├── brand.md          ← misión, público, tono de voz, palabras sí/no
├── colores.md        ← paleta con HEX y uso (primario, acento, fondo, texto)
├── tipografia.md     ← fuentes y jerarquía
└── logo.svg
```

Pedile a Claude que te ayude: *"Entrevistame con 10 preguntas para definir mi marca y generá los archivos de /marca"*.

### Parte 2 — Crear el comando

`.claude/commands/brand-landing.md` (plantilla completa en [`plantillas/commands/brand-landing.md`](../plantillas/commands/brand-landing.md)):

```markdown
---
description: Genera una landing page aplicando la identidad de marca de /marca
argument-hint: <producto o campaña>
---

Leé @marca/brand.md, @marca/colores.md y @marca/tipografia.md.
Creá una landing para: $ARGUMENTS

Reglas:
- Usá SOLO los colores y tipografías de la marca. El logo es marca/logo.svg.
- Textos con el tono de voz definido; evitá las palabras prohibidas.
- Usá la skill frontend-design para la composición.
- Guardá el resultado en landings/<slug>/index.html.
- Verificá contraste AA de todos los textos.
Al final, listá qué decisiones de marca aplicaste.
```

### Parte 3 — Probar e iterar

```
/brand-landing Lanzamiento del plan anual con 20% de descuento
```

Iterá el **comando**, no solo el resultado: si el tono falla, mejorá `brand.md`; si el layout falla, agregá reglas al comando. Commit a git para compartirlo con el equipo.

### 🧪 Práctica: slash command para tu marca

Creá `/post-marca <tema>` que genere 3 posts (LinkedIn, Instagram, X) con el tono de tu marca y guarde un `.md` por red.

### ✅ Solución

```markdown
---
description: Genera posts para LinkedIn, Instagram y X con el tono de la marca
argument-hint: <tema del post>
---
Leé @marca/brand.md. Tema: $ARGUMENTS

Generá 3 archivos en posts/<fecha>-<slug>/:
- linkedin.md: 900-1300 caracteres, gancho en línea 1, cierre con pregunta, máx 3 hashtags.
- instagram.md: caption de 150-300 palabras + 10 hashtags + idea de imagen/carrusel.
- x.md: hilo de 4-6 tweets de máx 270 caracteres.
Aplicá el tono y las palabras prohibidas de la marca. Al final autoevaluá cada post
del 1 al 10 contra brand.md y mejorá los que saquen menos de 8.
```

---

## Proyecto 3 — Plugin de análisis de competencia

**Objetivo:** empaquetar un flujo completo de **análisis competitivo y posicionamiento** en un plugin reutilizable.

### Parte 1 — Diseño del plugin

```
competencia/
├── .claude-plugin/plugin.json
├── commands/
│   ├── analizar-competidor.md     → /analizar-competidor <url o nombre>
│   └── mapa-posicionamiento.md    → /mapa-posicionamiento
├── agents/
│   └── investigador-mercado.md    → subagente que investiga en la web
└── skills/
    └── matriz-competitiva/SKILL.md → cómo construir la matriz y el informe
```

### Parte 2 — Construcción

Usá el plugin **plugin-dev** para que Claude te guíe:

```
/plugin-dev:create-plugin
```

O pedilo directo:

```
Creá un plugin "competencia" con la estructura [pegar árbol]. El subagente
investigador-mercado usa WebSearch y WebFetch, tiene modelo sonnet y devuelve una ficha
por competidor (propuesta de valor, precios, público, canales, fortalezas, debilidades,
reseñas). La skill matriz-competitiva define cómo puntuar 8 atributos del 1 al 5 y
generar un mapa de posicionamiento 2x2 en HTML.
```

`plugin.json` mínimo:

```json
{
  "name": "competencia",
  "version": "0.1.0",
  "description": "Análisis competitivo y mapa de posicionamiento",
  "author": { "name": "Tu nombre" }
}
```

### Parte 3 — Probar localmente y distribuir

```bash
claude --plugin-dir ./competencia     # carga el plugin sin instalarlo
```

```
/analizar-competidor Mercado Pago
/mapa-posicionamiento
```

Para distribuirlo: subilo a GitHub con un `.claude-plugin/marketplace.json` y los demás lo agregan con `/plugin marketplace add tu-usuario/tu-repo`.

### 🧪 Práctica: competencia y posicionamiento de marca con el plugin

Elegí tu negocio (o "Patitas Spa") y 4 competidores. Entregables: fichas por competidor, matriz de 8 atributos, mapa 2x2, 3 oportunidades de posicionamiento y una propuesta de valor nueva.

### ✅ Solución (flujo)

1. `/analizar-competidor` para cada uno → el subagente trabaja en paralelo si se lo pedís: *"Lanzá 4 subagentes investigador-mercado en paralelo, uno por competidor"*.
2. `/mapa-posicionamiento` con ejes elegidos por relevancia (ej.: precio vs. conveniencia).
3. Pedí: *"Identificá espacios vacíos del mapa y proponé 3 posicionamientos defendibles, con la evidencia de las fichas"*.
4. Complementá con la skill `competitive-brief` del plugin **Marketing**.
5. Cerrá con `/brand-landing` para crear una landing con el nuevo posicionamiento.

---

## Proyecto 4 — Calorie Tracker (app full‑stack con IA)

App donde el usuario **sube una foto de su comida** y la IA estima calorías y macronutrientes; guarda el historial diario y muestra el progreso contra una meta.

> El proyecto original usa la **API de Gemini** para visión. Todo el flujo funciona igual con la **API de Claude** (también analiza imágenes): solo cambia el cliente en la ruta de API. Mostramos ambos.

### Fase 1 — Setup y clave de API

1. Obtené una API key:
   - Gemini: Google AI Studio → *Get API key*.
   - Claude: console.anthropic.com → *API Keys*.
2. Creá el proyecto:
   ```bash
   npx create-next-app@latest calorie-tracker --ts --tailwind --app --eslint
   cd calorie-tracker
   echo "GEMINI_API_KEY=tu_clave" > .env.local     # o ANTHROPIC_API_KEY=...
   claude
   ```
3. Verificá que `.env.local` está en `.gitignore`. **Nunca** pegues la clave en el chat ni en el código.
4. `/init` para crear `CLAUDE.md` y agregá las reglas del proyecto (ver 9.7).

### Fase 1 — App básica (sin IA)

En **Plan mode** (`Shift+Tab`):

```
Quiero una app de seguimiento de calorías. Fase 1, SIN IA todavía:
- Pantalla "Hoy": meta diaria editable, total consumido, barra de progreso, lista de
  comidas del día (nombre, calorías, proteínas, carbohidratos, grasas, hora).
- Formulario para agregar comida manualmente.
- Historial de los últimos 7 días con gráfico de barras.
- Persistencia en localStorage (fase 1).
- Diseño mobile-first con la skill frontend-design.
Proponé la estructura de componentes y archivos. No codees hasta que apruebe.
```

Aprobá, implementá, y verificá: `npm run dev` → http://localhost:3000.

### Fase 2 — Agregar la IA: plan de rutas de API

```
Fase 2: al agregar una comida, el usuario puede subir una foto. Planificá:
- Ruta POST /api/analizar-comida (server-side) que recibe la imagen, llama al modelo
  de visión y devuelve JSON: { nombre, porciones, calorias, proteinas_g, carbohidratos_g,
  grasas_g, confianza (0-1), notas }.
- Validación con Zod de la respuesta del modelo (si no valida, reintentar 1 vez).
- Límite de tamaño de imagen (4 MB) y tipos permitidos.
- Manejo de errores y estado de carga en la UI; el usuario puede editar los valores
  antes de guardar.
- Tests de la ruta con el cliente de IA mockeado.
```

### Fase 2 — Implementación

Ejemplo de la ruta con **Gemini**:

```ts
// src/app/api/analizar-comida/route.ts
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";

const Resultado = z.object({
  nombre: z.string(),
  porciones: z.string(),
  calorias: z.number(),
  proteinas_g: z.number(),
  carbohidratos_g: z.number(),
  grasas_g: z.number(),
  confianza: z.number().min(0).max(1),
  notas: z.string().optional(),
});

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

export async function POST(req: Request) {
  const form = await req.formData();
  const file = form.get("imagen") as File | null;
  if (!file) return Response.json({ error: "Falta la imagen" }, { status: 400 });
  if (file.size > 4 * 1024 * 1024)
    return Response.json({ error: "La imagen supera 4 MB" }, { status: 413 });

  const base64 = Buffer.from(await file.arrayBuffer()).toString("base64");
  const res = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: [
      { inlineData: { mimeType: file.type, data: base64 } },
      { text: "Estimá la comida de la foto. Respondé SOLO JSON con: nombre, porciones, calorias, proteinas_g, carbohidratos_g, grasas_g, confianza (0-1), notas." },
    ],
    config: { responseMimeType: "application/json" },
  });

  const parsed = Resultado.safeParse(JSON.parse(res.text ?? "{}"));
  if (!parsed.success)
    return Response.json({ error: "Respuesta inválida del modelo" }, { status: 502 });
  return Response.json(parsed.data);
}
```

Variante con **Claude** (`npm i @anthropic-ai/sdk`, variable `ANTHROPIC_API_KEY`):

```ts
import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic();

const msg = await client.messages.create({
  model: "claude-sonnet-5",   // usá el modelo vigente que figure en la documentación
  max_tokens: 1024,
  messages: [{
    role: "user",
    content: [
      { type: "image", source: { type: "base64", media_type: file.type as "image/jpeg", data: base64 } },
      { type: "text", text: "Estimá la comida de la foto. Respondé SOLO JSON con: nombre, porciones, calorias, proteinas_g, carbohidratos_g, grasas_g, confianza (0-1), notas." },
    ],
  }],
});
const texto = msg.content.find((b) => b.type === "text")?.text ?? "{}";
```

Pedile a Claude Code que implemente según el plan, **corra los tests** y pruebe con 2–3 fotos reales.

### Fase 3 — Mejorar con Ralph Loops

**¿Qué es un Ralph Loop?** Una técnica (bautizada por Geoffrey Huntley en honor a Ralph Wiggum) que consiste en **darle a Claude el mismo prompt una y otra vez** en un bucle: en cada vuelta, Claude ve su trabajo anterior (archivos y git) y sigue mejorándolo, hasta que se cumple un criterio de fin verificable o se alcanza un máximo de iteraciones.

El plugin **ralph-loop** lo implementa con un *hook* `Stop`: cuando Claude intenta terminar, el hook le devuelve el mismo prompt.

```
/ralph-loop "PROMPT" --max-iterations N --completion-promise "TEXTO"
/cancel-ralph      # cortar el bucle
```

#### Plan (escribilo en un archivo, no en el prompt)

`MEJORAS.md`:

```markdown
# Objetivo fase 3
- [ ] Persistencia real con Prisma + SQLite (migrar desde localStorage)
- [ ] Autenticación simple (email mágico o NextAuth)
- [ ] Tests: cobertura > 80% en src/lib y src/app/api
- [ ] Accesibilidad: sin errores de axe en las 3 pantallas
- [ ] Lint y typecheck sin errores
- [ ] README con instrucciones de instalación y despliegue
```

#### Implementación

```
/ralph-loop "Leé MEJORAS.md. Tomá la PRIMERA tarea sin marcar, implementala, corré
npm test, npm run lint y npx tsc --noEmit. Si todo pasa, marcá la tarea con [x] en
MEJORAS.md y hacé commit. Si algo falla, arreglalo antes de seguir. Cuando TODAS las
tareas estén marcadas y los 3 comandos pasen, respondé exactamente <promise>COMPLETO</promise>." --max-iterations 25 --completion-promise "COMPLETO"
```

**Buenas prácticas de Ralph:**
1. **Criterio de fin verificable** (tests, lint, checklist), nunca subjetivo ("que quede lindo").
2. **Siempre `--max-iterations`** para acotar costo.
3. **Estado en archivos + git**, no en la conversación.
4. Tareas chicas e incrementales; una por iteración.
5. Revisá el resultado final: el bucle optimiza lo que medís, no lo que no medís.

### Despliegue (deploy)

```
Prepará la app para producción y desplegala en Vercel:
1. npm run build sin errores.
2. Documentá las variables de entorno necesarias.
3. Si usamos SQLite, migrá a Postgres (Neon/Supabase) para producción.
4. Guiame con los comandos de la CLI de Vercel (vercel, vercel env add, vercel --prod).
```

```bash
npm i -g vercel
vercel                    # primer deploy (preview)
vercel env add GEMINI_API_KEY
vercel --prod             # producción
```

Alternativas: Netlify, Railway, Render, Cloudflare Pages (sitios estáticos: arrastrar la carpeta o conectar GitHub).

### Revisión final con agentes

```
/code-review            # revisión con múltiples agentes (plugin code-review)
/feature-dev <feature>  # para la próxima funcionalidad: explorar → diseñar → implementar → revisar
```

➡️ Siguiente: [Módulo 11 — Agentes, Subagentes y Agent Teams](11-agentes-subagentes-teams.md)
