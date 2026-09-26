# Plantilla del agente personal (módulos 12 y 13)

Creá el vault con esta estructura y copiá `SOUL.md` y `CLAUDE.md` a la raíz:

```bash
mkdir -p mi-agente/{yo,marca,raw/{articulos,reuniones,documentos,recibos},wiki/{personas,proyectos,conceptos,empresas},diario,crm,automatizaciones,salidas,archivo,.claude/{commands,agents,skills}}
cp SOUL.md CLAUDE.md mi-agente/
cp ../commands/morning-brief.md mi-agente/.claude/commands/
cp ../agents/{investigador,analista,redactor}.md mi-agente/.claude/agents/
touch mi-agente/wiki/index.md mi-agente/wiki/log.md
```

Después abrí `mi-agente/` en Claude Code o Cowork (para trabajar) y en Obsidian (para visualizar).

Pasos siguientes: módulo 12, sección 12.12 (setup en 4 partes).
