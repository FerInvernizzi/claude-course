# Metodología: cómo se escribieron y midieron los objetivos del curso

<img src="assets/linea.svg" alt="" width="100%">

Este documento explica **cómo están construidos los objetivos de aprendizaje** del curso y **cómo se midió su calidad**. Sirve también como guía si querés escribir tus propios cursos (o skills de capacitación) con Claude.

## 1. Marco de referencia

| Marco | Qué aporta | Cómo se usa en el curso |
|-------|-----------|-------------------------|
| **Modelo ABCD** (Mager, 1984): *Audience, Behavior, Condition, Degree* | Estructura de un objetivo medible: quién, qué hace (observable), en qué condiciones y con qué criterio de logro | Cada objetivo de módulo tiene conducta, condición y criterio. La audiencia es común a todo el curso: "vas a poder…" |
| **Taxonomía de Bloom revisada** (Anderson y Krathwohl, 2001) | Dos dimensiones: **proceso cognitivo** (recordar, comprender, aplicar, analizar, evaluar, crear) × **tipo de conocimiento** (factual, conceptual, procedimental, metacognitivo) | Cada objetivo declara su nivel (ej.: *Crear · procedimental*). El curso sube de nivel a medida que avanza |
| **Quality Matters, estándar 2** (rúbrica de educación superior, 6.ª ed.) | Objetivos medibles a nivel curso (2.1) y módulo (2.2), escritos desde el alumno (2.3), con relación explícita con las actividades (2.4); alineados con la evaluación (estándar 3) | Objetivos del curso en el README; objetivos de módulo al inicio de cada módulo; columna "Evidencia" que dice qué práctica lo mide |
| **Alineación constructiva** (Biggs) y **SOLO** (Biggs y Collis) | El verbo del objetivo debe ser el mismo que exige la tarea de evaluación | La práctica de cada módulo pide exactamente la conducta del objetivo (si el objetivo dice "construir", la práctica pide construir) |

## 2. Verbos que no se usan (no son observables)

*Entender, saber, conocer, aprender, familiarizarse, estar al tanto, apreciar, explorar, dominar, comprender (sin conducta asociada), mejorar.*

No se puede observar si alguien "entiende". Solo podés observar que **explica**, **compara**, **configura**, **construye** o **diagnostica**. Por eso "Dominar Claude en Excel" (promesa comercial) se traduce en objetivos como *"Imputar valores faltantes en una tabla de Excel dejando columnas imputadas, bandera y tabla comparativa antes/después"*.

## 3. Verbos por nivel (Bloom revisada)

| Nivel | Subprocesos (Anderson y Krathwohl) | Verbos usados en el curso |
|-------|-----------------------------------|---------------------------|
| Recordar | reconocer, recuperar | identificar, nombrar, listar |
| Comprender | interpretar, ejemplificar, clasificar, resumir, inferir, comparar, explicar | explicar, comparar, clasificar, diferenciar |
| Aplicar | ejecutar, implementar | configurar, instalar, ejecutar, aplicar, usar |
| Analizar | diferenciar, organizar, atribuir | diagnosticar, descomponer, auditar, perfilar |
| Evaluar | verificar, criticar | verificar, evaluar, justificar, auditar contra criterios |
| Crear | generar, planificar, producir | construir, diseñar, crear, empaquetar, automatizar |

## 4. Instrumento de medición (0 a 10 por objetivo)

Cada objetivo se puntúa en 5 criterios de 0 a 2 puntos:

| Criterio | 0 | 1 | 2 |
|----------|---|---|---|
| **B. Conducta observable** | Verbo vago (entender, conocer, dominar) | Verbo observable pero amplio o con dos acciones | Un verbo observable y preciso |
| **Objeto específico** | Genérico ("herramientas") | Nombra el tema ("MCP") | Nombra la herramienta o función concreta (`claude mcp add`, `.mcp.json`) |
| **C. Condición** | Sin contexto | Contexto implícito | Declara con qué se trabaja (datos, herramienta, entorno) |
| **D. Criterio de logro** | Sin criterio | Criterio subjetivo ("bien hecho") | Criterio verificable (pasa tests, cifras coinciden, sin errores, < N líneas) |
| **Evidencia alineada** | Ninguna práctica lo mide | Una práctica lo toca parcialmente | Una práctica o autoevaluación del módulo lo mide con el mismo verbo |

**Umbral de calidad:** ≥ 8/10 por objetivo y promedio del módulo ≥ 8,5.

## 5. Resultado de la medición

| Versión | Objetivos | Promedio | % ≥ 8 | Observaciones |
|---------|-----------|----------|-------|---------------|
| v1: promesas del curso original (README) | 12 | 3,8 | 0% | Verbos "Master", "Understand", "Leverage"; sin condición ni criterio |
| v2: primera versión de objetivos por módulo | 54 | 5,7 | 9% | Verbos observables, pero casi sin condición, criterio ni evidencia explícita |
| **v3: objetivos ABCD actuales** | **68** | **9,7** | **100%** | Una conducta, condición, criterio verificable, nivel de Bloom y práctica que lo mide |

La medición completa, objetivo por objetivo, está en [`OBJETIVOS.md`](OBJETIVOS.md).

## Fuentes

- [The ABCD model for writing objectives](https://www.academia.edu/8095310/The_ABCD_model_for_writing_objectives)
- [How to Write Measurable Learning Objectives Using Mager's Model — Amanda LXD](https://www.amandalynnlxd.com/blog/magers-model-for-learning-objectives)
- [Techniques and Methods of Performance Objectives — George Mason University](https://mason.gmu.edu/~ndabbagh/cehdclass/Resources/IDKB/objective_formats.htm)
- [QM Standard 2: Learning Objectives — Faculty eCommons](https://faculty.risepoint.com/anatomy-of-a-quality-course/qm-standard-2/)
- [Specific Review Standards from the QM Higher Education Rubric, Sixth Edition](https://www.qualitymatters.org/sites/default/files/PDFs/QM-Higher-Ed-Sixth-Edition-Specific-Review-Standards-Accessible.pdf)
- [Making Your Course Better Through Measurable Objectives — Quality Matters](https://www.qualitymatters.org/qa-resources/resource-center/articles-resources/meeting-k-12-standard-2-1-and-2-2)
- [Overview of Revised Bloom's Taxonomy — National University](https://resources.nu.edu/RevisedBloomsTaxonomy)
- [Anderson and Krathwohl — Bloom's Taxonomy Revised (Quincy College)](https://quincycollege.edu/wp-content/uploads/Anderson-and-Krathwohl_Revised-Blooms-Taxonomy.pdf)
- [Bloom's Taxonomy of Educational Objectives — University of Illinois Chicago](https://teaching.uic.edu/cate-teaching-guides/syllabus-course-design/blooms-taxonomy-of-educational-objectives/)
- [Learning Objectives — UIC CATE](https://teaching.uic.edu/cate-teaching-guides/syllabus-course-design/learning-objectives/)
- [Tip #375: Avoid Certain Verbs for Learning Objectives — Laurel and Associates](https://laurelandassociates.com/tip-375-avoid-certain-verbs-for-learning-objectives/)
- [Aligning Assessment with Outcomes — UNSW](https://www.teaching.unsw.edu.au/aligning-assessment-learning-outcomes)
- [Constructive Alignment: A Teacher's Guide to Biggs' Model](https://www.structural-learning.com/post/constructive-alignment)
- [Rubric for Rating the Quality of Student Learning Objectives — IES REL Southwest](https://ies.ed.gov/rel-southwest/2025/01/session-2-handout-rubric-rating-quality-student-learning-objectives)
