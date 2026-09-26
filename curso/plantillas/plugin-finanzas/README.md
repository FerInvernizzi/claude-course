# Plugin de ejemplo: finanzas-pyme

Plugin del módulo 03.6. Contiene:

| Tipo | Nombre | Uso |
|------|--------|-----|
| Skill | `modelo-dcf` | Se activa sola cuando pedís una valuación por DCF |
| Comando | `/forecast <archivo.xlsx>` | Forecast de 12 meses con 3 escenarios |
| Comando | `/one-pager <empresa o archivo>` | Resumen financiero de 1 slide |
| Subagente | `revisor-financiero` | Audita modelos en Excel buscando errores |

## Probar en Claude Code

```bash
claude --plugin-dir ./plantillas/plugin-finanzas
```

## Instalar en Cowork

Comprimí la carpeta `plugin-finanzas/` en un `.zip` y subila desde **Customize → Plugins** (opción de subir archivo).
