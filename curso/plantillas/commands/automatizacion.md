---
description: Plantilla genérica para ejecutar una automatización del agente personal
argument-hint: [parámetros opcionales]
---

Leé @SOUL.md y @automatizaciones/NOMBRE.md y ejecutá el procedimiento completo.
Parámetros: $ARGUMENTS

Reglas:
- Nunca envíes emails, mensajes ni invitaciones sin mi aprobación explícita: dejá borradores.
- Nunca borres archivos; archivá en `archivo/`.
- Si un conector falla, seguí con el resto de los pasos y reportá el fallo al final.
- No dupliques datos si esta automatización ya corrió hoy.
- Guardá la salida donde indica la definición.
- Registrá la ejecución en `diario/<hoy>.md`: hora, qué se hizo, dónde quedó la salida y problemas.
