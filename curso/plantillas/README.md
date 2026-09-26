# Plantillas del curso

Copiá estas carpetas a tu proyecto (`.claude/`) o a tu carpeta personal (`~/.claude/`).

| Carpeta | Destino | Módulo |
|---------|---------|--------|
| `skills/posts-linkedin/` | `.claude/skills/posts-linkedin/` | 03 |
| `skills/resumen-ejecutivo/` | `.claude/skills/resumen-ejecutivo/` | 03, 05 |
| `commands/brand-landing.md` | `.claude/commands/` | 10 |
| `commands/post-marca.md` | `.claude/commands/` | 10 |
| `commands/automatizacion.md` | `.claude/commands/<nombre>.md` | 13 |
| `commands/morning-brief.md` | `.claude/commands/` | 13 |
| `agents/*.md` | `.claude/agents/` | 11, 13 |
| `plugin-finanzas/` | cargalo con `claude --plugin-dir ./plugin-finanzas` o subilo a Cowork como .zip | 03, 07 |
| `agente-personal/` | raíz de tu vault (`mi-agente/`) | 12, 13 |

```bash
# ejemplo: instalar todo en tu proyecto actual
mkdir -p .claude/{skills,commands,agents}
cp -r plantillas/skills/* .claude/skills/
cp plantillas/commands/*.md .claude/commands/
cp plantillas/agents/*.md .claude/agents/
```
