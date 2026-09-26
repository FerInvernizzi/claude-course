# Módulo 02 — MCP, conectores, tokens y ventana de contexto

## 2.1 Model Context Protocol (MCP)

**MCP** es un estándar abierto (creado por Anthropic) para conectar modelos de IA con herramientas y datos externos. Pensalo como el **"USB‑C de la IA"**: un único enchufe para conectar Claude con Gmail, Slack, Salesforce, Notion, bases de datos, GitHub, etc.

### Arquitectura

```
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

```
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

```
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

```
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
- **Desactivá conectores MCP que no uses:** cada uno agrega definiciones de herramientas al contexto.
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

➡️ Siguiente: [Módulo 03 — Agent Skills y Plugins](03-skills-y-plugins.md)
