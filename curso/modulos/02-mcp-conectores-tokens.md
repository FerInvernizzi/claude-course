# Módulo 02 — MCP, conectores, tokens y ventana de contexto

<img src="../assets/linea.svg" alt="" width="100%">

## 🎯 Objetivos de aprendizaje

| # | Al terminar vas a poder… (conducta · condición · criterio) | Nivel (Bloom) | Evidencia |
|---|---|---|---|
| 2.1 | Explicar, con un diagrama propio, cómo se comunican host, cliente y servidor MCP y qué son tools, resources y prompts, sin errores conceptuales | Comprender · conceptual | Autoevaluación |
| 2.2 | Conectar dos conectores (por ejemplo Gmail y Slack) y ejecutar un flujo entre plataformas en el que nada se envíe sin tu aprobación explícita | Aplicar · procedimental | Práctica |
| 2.3 | Configurar un servidor MCP en Claude Code con `claude mcp add` o `.mcp.json` y verificar con `/mcp` que está conectado | Aplicar · procedimental | Práctica |
| 2.4 | Estimar el tamaño en tokens de un documento dado, con un error menor al 30%, y decidir con justificación si conviene procesarlo entero o por partes | Evaluar · procedimental | Práctica |

**Requisitos previos:** Módulo 01 · **Duración estimada:** 1 h 15 min

## 2.1 Model Context Protocol (MCP)

**MCP** es un estándar abierto (creado por Anthropic) para conectar modelos de IA con herramientas y datos externos. Pensalo como el **"USB‑C de la IA"**: un único enchufe para conectar Claude con Gmail, Slack, Salesforce, Notion, bases de datos, GitHub, etc.

### Arquitectura

```text
┌──────────────┐        ┌──────────────┐        ┌──────────────────┐
│   HOST       │        │  CLIENTE MCP │  JSON  │  SERVIDOR MCP    │
│ (Claude      │◄──────►│  (dentro del │◄──────►│  (Gmail, Slack,  │──► API real
│ Desktop/Code)│        │   host)      │  -RPC  │   Salesforce...) │
└──────────────┘        └──────────────┘        └──────────────────┘
```

Un servidor MCP expone tres tipos de cosas:

| Primitiva | Qué es | Ejemplo |
|-----------|--------|---------|
| **Tools** (herramientas) | Acciones que Claude puede ejecutar | `send_email`, `create_lead`, `post_message` |
| **Resources** (recursos) | Datos que Claude puede leer | Un archivo, un registro del CRM |
| **Prompts** | Plantillas predefinidas | "Resumir hilo de Slack" |

**Transportes:** `stdio` (servidor local, proceso en tu máquina) y `HTTP` (servidor remoto, con OAuth).

### Conectores vs. MCP

En Claude (web/Desktop/Cowork) los **Conectores** son servidores MCP ya empaquetados, que se activan con un clic y OAuth: *Configuración → Conectores*. Ejemplos: Gmail, Google Calendar, Google Drive, Slack, Notion, Asana, Linear, Salesforce, HubSpot, Stripe, Figma, Canva, etc.

En **Claude Code** los agregás por terminal:

```bash
# Servidor remoto (HTTP)
claude mcp add --transport http notion https://mcp.notion.com/mcp

# Servidor local (stdio)
claude mcp add mi-db -- npx -y @modelcontextprotocol/server-postgres postgresql://localhost/ventas

# Listar / revisar estado
claude mcp list
# Dentro de Claude Code:
/mcp
```

O compartido con el equipo en un archivo `.mcp.json` en la raíz del proyecto:

```json
{
  "mcpServers": {
    "slack": { "type": "http", "url": "https://mcp.slack.com/mcp" },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "${DATABASE_URL}"]
    }
  }
}
```

> 🔐 **Seguridad:** instalá solo servidores MCP de fuentes confiables. Un servidor MCP puede leer y actuar en tu nombre. Revisá los permisos de cada herramienta y aprobá manualmente acciones de escritura (enviar, borrar, pagar).

## 2.2 Demo práctica: conectar Gmail y enviar emails desde Cowork

1. En Claude Desktop: **Configuración → Conectores → Gmail → Conectar**. Autorizá con OAuth.
2. En Cowork, verificá que el conector está activo para la sesión.
3. Prompt:

```text
1. Buscá en mi Gmail los emails de la última semana que contengan "factura" o "invoice".
2. Hacé un Excel "Facturas_semana.xlsx" con: remitente, fecha, monto (si aparece),
   vencimiento y si tiene adjunto.
3. Redactá un BORRADOR (no lo envíes) para contabilidad@miempresa.com con el resumen
   y el Excel adjunto.
Mostrame el borrador antes de hacer nada más.
```

4. Revisá el borrador. Luego: *"Está bien, envialo"*.

**Buenas prácticas:**
- Empezá con **borradores**, nunca envío directo, hasta que confíes en el flujo.
- Para envíos masivos, pedí primero un Excel con destinatario + asunto + cuerpo y aprobalo.

### Automatización cross‑platform (ejemplo)

Con Gmail + Slack + Salesforce conectados:

```text
Cada vez que te pida "sync de leads":
1. Leé en Gmail los emails nuevos con asunto "Demo request".
2. Creá o actualizá el Lead en Salesforce (nombre, empresa, email, fuente = "Email").
3. Publicá en #ventas de Slack un resumen: cuántos leads nuevos y links a Salesforce.
```

Ese pedido luego se convierte en una **skill** o **tarea programada** (módulos 03 y 13).

## 2.3 Tokens y ventana de contexto

### ¿Qué es un token?

Un **token** es la unidad mínima de texto que procesa el modelo: un fragmento de palabra. Aproximaciones:

- En inglés: ~1 token ≈ 4 caracteres ≈ 0,75 palabras.
- En español suele haber **algo más de tokens por palabra** que en inglés.
- 1 página de texto ≈ 500–800 tokens. Imágenes y PDFs también consumen tokens.

### ¿Qué es la ventana de contexto?

Es la **memoria de trabajo** del modelo en una conversación: todo lo que Claude "ve" a la vez. Incluye:

```text
┌──────────────────────── VENTANA DE CONTEXTO ────────────────────────┐
│ Instrucciones del sistema │ Skills cargadas │ Definiciones de tools   │
│ (MCP) │ Archivos leídos │ Historial de mensajes │ Resultados de tools │
│ │ Tu mensaje actual │ ...espacio para la respuesta                    │
└──────────────────────────────────────────────────────────────────────┘
```

Los modelos actuales de Claude tienen ventanas de ~200.000 tokens (y algunos hasta 1 millón en ciertos planes/API). Suena mucho, pero se llena rápido con archivos grandes, muchas herramientas MCP y conversaciones largas.

### Por qué importa

1. **Límite duro:** si se llena, Claude tiene que resumir (compactar) o la conversación termina.
2. **Calidad:** con demasiado contenido irrelevante, la atención se diluye ("context rot"). Más contexto ≠ mejor resultado.
3. **Costo y velocidad:** más tokens = más uso de tu cuota y respuestas más lentas.

### Reglas prácticas

- **Una tarea, una conversación.** Nueva tarea → nueva sesión.
- Pasá **solo los archivos relevantes**; si un PDF es enorme, pedí que extraiga solo las secciones necesarias.
- **Desactivá conectores MCP que no uses.** Al inicio, Claude carga solo los *nombres* de las herramientas de cada conector y trae los esquemas completos cuando las usa, así que el costo fijo es bajo. Pero muchos conectores igual suman ruido, y cada resultado de herramienta (un hilo de email, un registro del CRM) sí ocupa contexto.
- Pedí **resúmenes intermedios** y arrancá una nueva sesión con el resumen.
- En Claude Code: `/context` (ver uso), `/compact` (resumir), `/clear` (limpiar). Ver módulo 09.

## 🧪 Práctica: entender los tokens y el contexto

Respondé:

1. Tenés un informe de 120 páginas en español. ¿Cuántos tokens aproximados ocupa? ¿Entra en una ventana de 200K?
2. Tu sesión de Cowork tiene 10 conectores activos, leíste 5 Excels grandes y llevás 2 horas conversando. Las respuestas empiezan a "olvidar" instrucciones del inicio. ¿Por qué pasa y qué hacés?
3. ¿Por qué una skill bien diseñada ahorra contexto frente a pegar las mismas instrucciones en cada chat?

### ✅ Solución

1. 120 páginas × ~700 tokens ≈ **84.000 tokens** (rango razonable 60K–100K). **Entra** en 200K, pero ocupa casi la mitad: queda menos espacio para otros archivos, herramientas y respuestas. Mejor: pedir que lo procese por capítulos o extraiga solo lo relevante.
2. La ventana está muy llena (definiciones de 10 conectores + Excels + historial). Las instrucciones iniciales quedan "enterradas" o fueron compactadas. **Solución:** pedir un resumen del estado y decisiones, abrir una **sesión nueva** con ese resumen, activar solo los conectores necesarios y referenciar los Excels por ruta en lugar de volcarlos enteros.
3. Por la **carga progresiva (progressive disclosure)**: al inicio Claude solo ve el *nombre y la descripción* de la skill (pocas decenas de tokens). El contenido completo se carga **solo cuando la tarea lo necesita**, y los scripts se ejecutan sin cargarse en el contexto.

## 🧪 Práctica: automatización entre plataformas con MCP

Conectá **dos o más** conectores (por ejemplo Gmail + Slack, o Gmail + Google Calendar; si tu empresa usa Salesforce o HubSpot, sumalo) y construí un flujo que lea de uno y escriba en otro, con aprobación humana antes de cualquier acción externa.

### ✅ Solución (Gmail → Slack)

```text
1. Buscá en Gmail los emails de clientes de los últimos 3 días que mencionen
   "reclamo", "problema" o "no funciona".
2. Para cada uno: cliente, resumen en una línea, urgencia (alta/media/baja) y si ya
   respondimos.
3. Prepará un mensaje para el canal #soporte de Slack con la tabla, ordenada por urgencia.
4. Mostrame el mensaje y NO lo publiques hasta que te diga "publicar".
```

**Criterios de éxito:**
- [ ] El flujo usa al menos dos conectores distintos.
- [ ] Nada se envía ni se publica sin tu aprobación explícita.
- [ ] Solo activaste los conectores que el flujo necesita (así ahorrás contexto, como viste en 2.3).
- [ ] Podés describir qué herramientas (tools) de cada servidor MCP usó Claude. Las ves en el detalle de cada paso.

**Variante en Claude Code:** agregá un servidor con `claude mcp add --transport http notion https://mcp.notion.com/mcp` (o el de tu herramienta), autenticalo desde `/mcp` y verificá que aparece como conectado. Pedile una consulta de solo lectura.

## 🧠 Autoevaluación

1. ¿Qué diferencia hay entre un conector y un servidor MCP?
   <details><summary>Ver respuesta</summary>Un conector es un servidor MCP ya empaquetado que se activa con un clic y OAuth desde la configuración de Claude.</details>

2. ¿Por qué desactivar conectores que no usás?
   <details><summary>Ver respuesta</summary>Aunque hoy cada conector carga solo los nombres de sus herramientas hasta que se usan, muchos conectores suman ruido y opciones que pueden distraer al modelo, y sus resultados ocupan contexto. Activá solo los que la tarea necesita.</details>

3. Tu sesión está muy larga y Claude olvida instrucciones. ¿Qué hacés?
   <details><summary>Ver respuesta</summary>Pedís un resumen del estado y las decisiones, y abrís una sesión nueva con ese resumen (en Claude Code: `/compact` o `/clear`).</details>

➡️ Siguiente: [Módulo 03 — Agent Skills y Plugins](03-skills-y-plugins.md)
