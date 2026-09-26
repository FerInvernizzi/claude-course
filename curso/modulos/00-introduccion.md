# Módulo 00 — Introducción: el poder de Claude Code y Cowork

<img src="../assets/linea.svg" alt="" width="100%">

## 🎯 Objetivos de aprendizaje

| # | Al terminar vas a poder… (conducta · condición · criterio) | Nivel (Bloom) | Evidencia |
|---|---|---|---|
| 0.1 | Clasificar, a partir de una lista de 6 tareas reales de tu trabajo, cuáles conviene resolver con Chat, Cowork, Claude Code o un complemento de Office, justificando cada elección en una línea | Comprender · conceptual | Autoevaluación |
| 0.2 | Reformular, a partir de un pedido vago de tu trabajo, un objetivo delegable (objetivo, entradas, formato, restricciones, plan previo), de modo que cumpla al menos 4 de los 8 consejos de éxito | Aplicar · procedimental | Autoevaluación |

**Requisitos previos:** Ninguno · **Duración estimada:** 20 min

## 0.1 El cambio de paradigma: de "chatbot" a "agente"

Durante años usamos la IA así: **vos preguntás → la IA responde → vos copiás y pegás**. Todo el trabajo de ejecutar recaía en vos.

Con Claude Code y Claude Cowork el modelo cambia a: **vos delegás un objetivo → Claude planifica → Claude ejecuta con herramientas → Claude verifica → vos revisás el resultado**.

| | Chat tradicional | Agente (Cowork / Code) |
|---|---|---|
| Entrada | Una pregunta | Un objetivo |
| Acceso | Solo el texto que pegás | Tus archivos, carpetas, apps (MCP), terminal |
| Salida | Texto | Archivos reales: `.xlsx`, `.pptx`, `.docx`, código, emails enviados |
| Duración | Segundos | Minutos u horas, con múltiples pasos |
| Verificación | Vos | El propio agente (ejecuta, prueba, corrige) |

## 0.2 El ecosistema de Claude (mapa mental)

```text
                         ┌──────────────── CLAUDE ────────────────┐
                         │                                         │
     Conversación        │   Trabajo de oficina       Desarrollo   │
   ┌──────────────┐      │   ┌──────────────┐   ┌──────────────┐ │
   │ Claude Chat  │      │   │ Claude Cowork│   │ Claude Code  │ │
   │ (web/app)    │      │   │ (Desktop)    │   │ (terminal,   │ │
   │ Research,    │      │   │ Archivos,    │   │  VS Code,    │ │
   │ Artifacts    │      │   │ tareas largas│   │  Desktop)    │ │
   └──────────────┘      │   └──────────────┘   └──────────────┘ │
   ┌──────────────┐      │                                         │
   │ Claude en    │      │   Capas que se comparten entre todos:   │
   │ Excel / PPT  │      │   • Skills (SKILL.md)                   │
   │ (add-ins)    │      │   • Plugins (paquetes de skills,        │
   └──────────────┘      │     comandos, agentes, conectores)      │
                         │   • MCP / Conectores (Gmail, Slack...)  │
                         │   • Subagentes y Agent Teams            │
                         └─────────────────────────────────────────┘
```

**Idea clave del curso:** Skills, Plugins y MCP son **la misma tecnología** en Cowork y en Claude Code. Lo que aprendas en uno lo reutilizás en el otro.

## 0.3 Esquema del curso

1. **Bloque Cowork (módulos 01–03):** automatización de oficina sin código.
2. **Bloque Chat y prompting (04–05):** investigar, escribir y hablarle bien a Claude.
3. **Bloque Office (06–08):** Excel, modelos financieros y PowerPoint.
4. **Bloque Claude Code (09–10):** construir software real desde la terminal.
5. **Bloque Agentes (11–13):** agentes con SDK, equipos de agentes, tu agente personal y 10 automatizaciones.

## 0.4 Consejos clave para el éxito

1. **Delegá objetivos, no pasos.** "Prepará un informe de ventas Q3 con 3 gráficos y recomendaciones para el CFO" es mejor que "hacé un gráfico".
2. **Dale contexto como a un empleado nuevo.** Quién es el público, qué formato, qué *no* hacer, ejemplos de un buen resultado.
3. **Pedí un plan antes de ejecutar.** En tareas grandes: *"Primero mostrame tu plan y esperá mi aprobación"*.
4. **Revisá siempre.** Claude es muy capaz, pero vos sos responsable del resultado (sobre todo en finanzas y legal).
5. **Convertí lo repetitivo en Skills.** Si repetís un prompt 3 veces, guardalo como skill o slash command.
6. **Trabajá en carpetas dedicadas.** Dale a Cowork/Code una carpeta de proyecto, no tu disco entero.
7. **Cuidá el contexto.** Conversaciones largas degradan la calidad: empezá sesiones nuevas por tarea (ver módulo 02).
8. **Iterá.** La primera versión es un borrador. "Mejorá el diseño", "más conciso", "agregá fuentes" son parte del flujo.

## 0.5 Materiales

Todo lo que necesitás está en este repositorio:

- [`plantillas/`](../plantillas/) — skills, comandos, agentes y plugin listos para copiar.
- [`codigo/`](../codigo/) — scripts Python de los proyectos de agentes.
- Datos de práctica: en cada ejercicio se indica cómo pedirle a Claude que **genere un dataset sintético** para que no dependas de archivos externos.

## 🧠 Autoevaluación

1. ¿Qué cambia cuando pasás de "chat" a "agente"?
   <details><summary>Ver respuesta</summary>Delegás un objetivo en vez de hacer una pregunta: el agente planifica, usa herramientas (archivos, apps, terminal), verifica su trabajo y entrega archivos reales.</details>

2. ¿Qué tienen en común Cowork y Claude Code?
   <details><summary>Ver respuesta</summary>El mismo motor agéntico y las mismas capas de extensión: skills, plugins, MCP y subagentes.</details>

3. ¿Cuándo conviene convertir un prompt en una skill?
   <details><summary>Ver respuesta</summary>Cuando lo repetís: la regla práctica del curso es la tercera vez.</details>

➡️ Siguiente: [Módulo 01 — Claude Cowork: fundamentos](01-cowork-fundamentos.md)
