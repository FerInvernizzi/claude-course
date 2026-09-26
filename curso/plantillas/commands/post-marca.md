---
description: Genera posts para LinkedIn, Instagram y X con el tono de la marca
argument-hint: <tema del post>
---

Leé @marca/brand.md. Tema: $ARGUMENTS

Generá 3 archivos en `posts/<fecha>-<slug>/`:
- `linkedin.md`: 900-1.300 caracteres, gancho en la línea 1, cierre con pregunta, máximo 3 hashtags.
- `instagram.md`: caption de 150-300 palabras, 10 hashtags e idea de imagen o carrusel.
- `x.md`: hilo de 4-6 tweets de 270 caracteres como máximo cada uno.

Aplicá el tono y las palabras prohibidas de la marca. Al final autoevaluá cada post del 1 al 10 contra `brand.md` y reescribí los que saquen menos de 8.
