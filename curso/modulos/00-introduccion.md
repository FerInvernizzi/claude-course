# Módulo 00 — Introducción: el poder de Claude Code y Cowork

<img src="../assets/linea.svg" alt="" width="100%">

## 🎯 Objetivos de aprendizaje

| # | Al terminar vas a poder… (conducta · condición · criterio) | Nivel (Bloom) | Evidencia |
|---|---|---|---|
| 0.1 | Clasificar, a partir de una lista de 6 tareas reales de tu trabajo, cuáles conviene resolver con Chat, Cowork, Claude Code o un complemento de Office, justificando cada elección en una línea | Comprender · conceptual | Práctica (parte A) |
| 0.2 | Reformular, a partir de un pedido vago de tu trabajo, un objetivo delegable (objetivo, entradas, formato, restricciones, plan previo), de modo que cumpla al menos 4 de los 8 consejos de éxito | Aplicar · procedimental | Práctica (parte B) |

**Requisitos previos:** Ninguno · **Duración estimada:** 40 min

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
   │ (web/app)    │      │   │ (Desktop,web,│   │ (terminal,   │ │
   │ Research,    │      │   │ Archivos,    │   │  VS Code,    │ │
   │ Artifacts    │      │   │ móvil)       │   │  Desktop)    │ │
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

### ¿Qué herramienta uso?

| Si tu tarea… | Usá | Por qué |
|---|---|---|
| Es una pregunta, una idea o un texto corto | **Claude Chat** | Respuesta inmediata, sin archivos |
| Necesita investigar muchas fuentes con citas | **Chat con Research** | Hace búsquedas encadenadas y cita las fuentes |
| Trabaja sobre varios archivos o carpetas y produce entregables (Excel, PPT, informes) | **Cowork** | Lee y escribe tus archivos, trabaja por pasos |
| Se hace dentro de una planilla o una presentación que ya tenés abierta | **Claude en Excel / PowerPoint** | Edita en el lugar, respetando fórmulas y plantillas |
| Es software: código, tests, apps, automatizaciones con scripts | **Claude Code** | Terminal, git, ejecución y verificación |
| Se repite todas las semanas | **Skill + tarea programada** | Lo definís una vez y corre solo |

## 0.3 Esquema del curso

1. **Bloque Cowork (módulos 01–03):** automatización de oficina sin código.
2. **Bloque Chat y prompting (04–05):** investigar, escribir y hablarle bien a Claude.
3. **Bloque Office (06–08):** Excel, modelos financieros y PowerPoint.
4. **Bloque Claude Code (09–10):** construir software real desde la terminal.
5. **Bloque Agentes (11–13):** agentes con SDK, equipos de agentes, tu agente personal y 10 automatizaciones.
6. **Profundización (14–15):** funciones avanzadas que no son evidentes y skills de nicho para arte, diseño y otros intereses.

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

## 🧪 Práctica: tu mapa de delegación

**Parte A.** Escribí 6 tareas reales de tu semana (no inventadas) y clasificá cada una con la tabla *¿Qué herramienta uso?*, justificando en una línea.

**Parte B.** Elegí la tarea más repetitiva y reescribila como pedido delegable: objetivo, entradas, formato de salida, restricciones y "mostrame el plan antes de ejecutar". Guardala: la vas a usar en el módulo 01.

### ✅ Solución (ejemplo de una analista de marketing)

| Tarea | Herramienta | Justificación |
|---|---|---|
| Responder un email a un proveedor | Chat | Texto corto, sin archivos |
| Comparar precios de 6 competidores | Chat con Research | Muchas fuentes y hacen falta citas |
| Consolidar 12 CSV de campañas en un informe | Cowork | Varios archivos → Excel + resumen |
| Ajustar el formato del forecast abierto | Claude en Excel | Edición dentro de la planilla, sin romper fórmulas |
| Script que baja métricas de una API | Claude Code | Es código y hay que probarlo |
| Reporte semanal de redes | Skill + tarea programada | Se repite todos los lunes |

Pedido delegable (parte B):

```text
Objetivo: informe semanal de rendimiento de campañas para la gerenta de marketing,
que decide dónde mover presupuesto.
Entradas: los CSV de /Campañas/semana-actual (Meta y Google Ads).
Salida: Excel con KPIs por campaña (CTR, CPA, ROAS) en fórmulas + 5 bullets con
recomendaciones que citen el dato.
Restricciones: no borres los CSV; si faltan datos de una campaña, marcala.
Antes de ejecutar, mostrame tu plan y esperá mi OK.
```

**Criterios de éxito:**
- [ ] Las 6 tareas son reales y cada una tiene herramienta y justificación.
- [ ] El pedido de la parte B tiene objetivo, entradas, formato, restricciones y plan previo, y aplica al menos 4 de los 8 consejos (en el ejemplo: 1, 2, 3 y 6).

## 📌 Ideas clave

- Un agente recibe un **objetivo**, no una pregunta: planifica, usa herramientas, verifica y entrega archivos.
- Elegí la herramienta según la tarea: Chat, Research, Cowork, complementos de Office o Claude Code.
- Un buen pedido tiene objetivo, entradas, formato, restricciones y plan previo.
- Lo que repetís tres veces se convierte en skill.

## 🧠 Autoevaluación

1. ¿Qué cambia cuando pasás de "chat" a "agente"?
   <details><summary>Ver respuesta</summary>Delegás un objetivo en vez de hacer una pregunta: el agente planifica, usa herramientas (archivos, apps, terminal), verifica su trabajo y entrega archivos reales.</details>

2. ¿Qué tienen en común Cowork y Claude Code?
   <details><summary>Ver respuesta</summary>El mismo motor agéntico y las mismas capas de extensión: skills, plugins, MCP y subagentes.</details>

3. ¿Cuándo conviene convertir un prompt en una skill?
   <details><summary>Ver respuesta</summary>Cuando lo repetís: la regla práctica del curso es la tercera vez.</details>

## Fuentes oficiales

- [Cowork overview](https://claude.com/docs/cowork/overview) · [Claude Code overview](https://code.claude.com/docs/en/overview) · [Claude para Microsoft 365](https://claude.com/docs/office-agents/overview)
- [Building effective agents — Anthropic](https://www.anthropic.com/engineering/building-effective-agents)

➡️ Siguiente: [Módulo 01 — Claude Cowork: fundamentos](01-cowork-fundamentos.md)
