---
name: revision-calidad-curso
description: Revisa y corrige la calidad educativa de cursos, módulos, tutoriales y material didáctico (Markdown u otros textos), con una rúbrica puntuable basada en estándares de diseño instruccional (Quality Matters, Bloom, alineación constructiva, Merrill, carga cognitiva), verificación de exactitud técnica y corrección de estilo en español. Usala siempre que alguien pida revisar, auditar, puntuar, corregir, pulir o "controlar la calidad" de un curso, clase, lección, guía, bootcamp, workshop o material de capacitación, aunque no diga "rúbrica" ni "diseño instruccional", y también antes de publicar o entregar un curso propio.
---

# Revisión de calidad de cursos

El objetivo no es opinar sobre el curso sino **dejarlo mejor**: encontrar lo que impide que una persona aprenda (errores técnicos, saltos de nivel, objetivos que nunca se practican, instrucciones que no funcionan) y corregirlo, dejando una evaluación puntuada que muestre dónde estaba y dónde quedó.

## Flujo de trabajo

### 1. Mapear el curso
- Leé el índice o README y listá los módulos con su objetivo declarado.
- Identificá el **público** (conocimientos previos) y la **promesa** del curso (los objetivos generales). Todo se evalúa contra eso: un curso para no programadores que asume saber usar la terminal tiene un problema, uno para desarrolladores no.

### 2. Chequeos automáticos
Corré `python scripts/chequeos.py <carpeta-del-curso>`. Detecta enlaces internos rotos, anclas inexistentes, bloques de código sin cerrar, palabras repetidas ("de de"), títulos duplicados, módulos sin práctica o solución y marcadores pendientes (TODO, XXX, [VERIFICAR]). Arreglá todo lo que reporte antes de seguir: son errores objetivos y baratos de corregir.

### 3. Evaluar con la rúbrica
Leé `references/rubrica.md` y puntuá cada módulo en las 8 dimensiones (de 1 a 4). Para cada puntaje menor que 4, anotá **la evidencia concreta** (archivo y sección) y **la corrección**. Un puntaje sin evidencia no le sirve a nadie.

Las dos dimensiones que más importan, porque son las que más rompen el aprendizaje, son:
- **Exactitud técnica:** comandos, nombres de productos, APIs, rutas y cifras. Verificá todo lo que sea verificable: ejecutá el código, compilalo, consultá `--help` y los archivos instalados. Si algo no se puede verificar y puede cambiar (interfaces de producto, precios, nombres de modelos), el curso tiene que decirlo y remitir a la documentación oficial, en lugar de afirmarlo como definitivo.
- **Alineación:** cada objetivo prometido tiene que tener contenido, práctica y evaluación. Hacé la matriz objetivo × módulo (`references/rubrica.md`, sección "Matriz de alineación") y buscá objetivos huérfanos.

### 4. Corregir
Aplicá las correcciones directamente en los archivos, priorizando:
1. 🔴 **Bloqueantes:** errores técnicos, pasos que no funcionan, enlaces rotos, contenido prometido que falta.
2. 🟡 **Importantes:** saltos de nivel sin andamiaje, prácticas sin criterios de éxito, soluciones incompletas, inconsistencias de terminología.
3. 🟢 **Pulido:** estilo, redacción, formato.

Preservá la voz y la estructura del autor: corregí, no reescribas por gusto. Si un cambio es grande (reordenar módulos, agregar uno nuevo), hacelo solo si una dimensión puntúa 1 o 2 y explicá por qué.

### 5. Re‑evaluar e informar
Volvé a correr los chequeos automáticos y a puntuar. Generá el informe con la plantilla de `references/informe.md`: puntajes antes/después por módulo, correcciones aplicadas por prioridad, verificaciones realizadas y limitaciones (lo que no pudiste verificar).

## Estilo en español
- Mantené una sola variante (por ejemplo, rioplatense con "vos") en todo el curso; no mezcles "tú", "vos" y "usted".
- Usá los signos de apertura (¿ ¡), las tildes y la puntuación de la RAE.
- Los términos técnicos en inglés van en su forma habitual (prompt, plugin, commit) y se explican la primera vez que aparecen.
- Frases cortas en las instrucciones: un paso, una acción.

## Qué evitar
- Puntuar alto "por esfuerzo": la rúbrica mide lo que aprende el alumno.
- Afirmar que algo funciona sin haberlo probado. Si no lo probaste, decilo en el informe.
- Agregar contenido de relleno para "completar" una dimensión; es preferible una práctica bien diseñada a tres superficiales.
