# Módulo 06 — Claude en Excel

> **🎯 Objetivos.** Al terminar este módulo vas a poder:
> - Instalar y usar Claude en Excel sobre datos reales.
> - Obtener estadísticas y filtrar, ordenar y visualizar con fórmulas dinámicas.
> - Aplicar formato condicional e imputar valores faltantes de forma trazable.
> - Construir un dashboard con KPIs y segmentadores.
>
> **Requisitos previos:** Módulo 01 · Excel de Microsoft 365 · **Duración estimada:** 2 h 30 min

## 6.1 Instalación de Claude en Excel

1. Abrí Excel (Microsoft 365, escritorio o web).
2. **Inicio → Complementos → Obtener complementos** (o *Insertar → Complementos*).
3. Buscá **"Claude"** (publicado por Anthropic) → **Agregar**.
4. Aparece un panel lateral: iniciá sesión con tu cuenta de Claude.
5. En organizaciones, puede que el administrador de Microsoft 365 tenga que habilitarlo.

**Versiones compatibles:** Excel en la web, Excel para Windows con Microsoft 365 (compilación 16.0.13127.20296 o posterior) y Excel para Mac 16.46 o posterior. **No funciona** en Excel 2016/2019 de licencia perpetua, iPad ni Android. Disponible en planes Pro, Max, Team y Enterprise.

**Cómo trabaja:** Claude lee el libro abierto (todas las hojas, rangos y fórmulas) y responde con **citas a nivel de celda** en las que podés hacer clic para ir a la celda. Puede escribir valores y fórmulas **manteniendo las relaciones entre fórmulas**, depurar errores (`#¡REF!`, `#¡DIV/0!`) hasta su causa, construir o completar modelos, y hacer operaciones nativas: **ordenar, filtrar, editar tablas dinámicas, aplicar formato condicional y crear listas desplegables de validación de datos**. Antes de sobrescribir datos existentes te avisa.

**Lo que hoy NO hace:** tablas de datos de Excel (*Datos → Análisis de hipótesis → Tabla de datos*) ni **macros/VBA**. Para sensibilidades, pedí una grilla armada con fórmulas (ver módulo 07).

**Funciones poco conocidas:**
- **Instrucciones persistentes:** en *Configuración* del panel, el campo *Instrucciones* guarda preferencias para todas tus conversaciones en Excel (ej.: *"separador de miles, encabezados en negrita, moneda ARS"*). Son independientes de las de PowerPoint y Word.
- **Contexto entre apps:** Claude para Excel comparte contexto con PowerPoint, Word y Outlook: una misma conversación puede usar tu libro abierto, tu presentación y tu bandeja de entrada.
- **Skills y conectores:** aplica tus skills habilitadas y puede traer datos externos con conectores financieros (S&P Global, LSEG, Daloopa).
- **Compactación automática:** las conversaciones largas se compactan solas. El historial del chat se guarda localmente en tu navegador, no se sincroniza entre dispositivos.

> ⚠️ **Inyección de prompts:** usalo solo con planillas confiables. Un archivo externo (plantilla descargada, archivo de proveedor) puede traer instrucciones ocultas para extraer o modificar datos. Revisá con atención cada confirmación que te pida.

> ✅ Buenas prácticas: trabajá sobre una **copia**; convertí los datos en **Tabla** (Ctrl+T) para que Claude entienda los encabezados; revisá las celdas que Claude indica que modificó.

## 6.2 Dataset de práctica

Pedile a Claude (en el panel) o en Cowork:

```text
Creá en una hoja nueva "Datos" un dataset de 1.000 pedidos de e-commerce con columnas:
ID_Pedido, Fecha (2025), Cliente, Ciudad, Categoría (Electrónica, Hogar, Moda, Deportes,
Libros), Producto, Cantidad, Precio_Unitario, Descuento_%, Método_Pago, Calificación (1-5),
Días_Entrega. Incluí ~6% de celdas vacías en Precio_Unitario, Calificación y Días_Entrega,
y algunos outliers. Formatealo como Tabla.
```

## 6.3 Insights generales

```text
Analizá la tabla de la hoja Datos y dame los 7 insights más relevantes para el gerente
comercial. Para cada uno: el dato, por qué importa y una acción sugerida. Indicá qué
celdas o cálculos usaste.
```

Seguimiento típico: *"¿Por qué cae la calificación en Electrónica? Cruzá con Días_Entrega."*

## 6.4 Resumen estadístico y filtrado por condiciones

```text
En una hoja "Estadística" creá un resumen de Cantidad, Precio_Unitario, Descuento_%,
Calificación y Días_Entrega con: n, faltantes, media, mediana, desvío, mín, P25, P75, máx.
Usá fórmulas de Excel (PROMEDIO, MEDIANA, DESVEST.M, CUARTIL.INC, CONTAR.BLANCO) para que
se actualice.
```

```text
En una hoja "Filtro" traé con la función FILTRAR las filas donde Categoría = "Electrónica",
Calificación <= 2 y Días_Entrega > 7, ordenadas por fecha descendente.
```

**Tip:** los nombres de funciones dependen del idioma de tu Excel (`FILTRAR` = `FILTER`, `SUMAR.SI.CONJUNTO` = `SUMIFS`, `JERARQUIA.EQV` = `RANK.EQ`). Claude usa los de tu instalación. Pedir **fórmulas dinámicas** (`FILTRAR`, `ORDENAR`, `UNICOS`, `SUMAR.SI.CONJUNTO`) hace el libro vivo; pedir "valores" genera una foto estática.

## 6.5 Visualización

```text
Creá en una hoja "Gráficos":
1. Columnas: ventas totales (Cantidad × Precio × (1-Descuento)) por Categoría.
2. Líneas: ventas por mes.
3. Circular (máx. 5 porciones): Método de pago.
4. Dispersión: Días_Entrega vs Calificación.
Títulos que expresen la conclusión, ejes rotulados, colores coherentes.
```

## 6.6 Ordenamiento

```text
Ordená la tabla por Categoría (A-Z), luego por ventas descendente. Agregá una columna
"Ranking_en_Categoría" con JERARQUIA.EQV o una fórmula equivalente.
```

## 6.7 Filtrado

```text
Aplicá autofiltros para mostrar solo pedidos de Buenos Aires y Córdoba con descuento
mayor a 15%. Decime cuántas filas quedan y el total de ventas visible (usá SUBTOTALES).
```

## 6.8 Formato condicional y códigos de color

```text
Aplicá formato condicional:
- Calificación: escala de 3 colores (rojo 1 → amarillo 3 → verde 5).
- Días_Entrega > 7: relleno rojo claro con texto rojo oscuro.
- Top 10% de ventas: negrita + relleno verde.
- Barras de datos en Cantidad.
- Filas completas con Precio_Unitario vacío: gris (fórmula con ESBLANCO).
Explicá cada regla.
```

## 6.9 Valores faltantes (imputación)

### Estrategias

| Estrategia | Cuándo | Riesgo |
|-----------|--------|--------|
| Eliminar filas | Pocas filas, faltantes al azar | Perder información, sesgo |
| Media | Variable numérica simétrica sin outliers | Reduce la varianza |
| **Mediana** | Numérica con outliers/asimetría | Reduce la varianza |
| **Mediana por grupo** | Cuando la variable depende de una categoría (precio por producto) | Mejor opción típica |
| Moda | Categóricas | Sobre‑representa la categoría dominante |
| Forward fill | Series temporales | Arrastra valores viejos |
| Regresión / KNN | Relaciones fuertes entre variables | Más complejo |

### Prompt

```text
1. Hacé un diagnóstico de faltantes por columna (cantidad y %), y decime si parecen
   aleatorios o concentrados en alguna categoría/mes.
2. Imputá: Precio_Unitario con la mediana del mismo Producto; Calificación con la mediana
   de la Categoría; Días_Entrega con la mediana por Ciudad.
3. No sobrescribas los originales: creá columnas *_imputado y una columna "Fue_imputado"
   (Sí/No). Marcá las celdas imputadas en celeste.
4. Compará media y desvío antes/después en una tabla.
```

**Clave profesional:** siempre dejar **trazabilidad** (qué se imputó y cómo).

## 6.10 Dashboard en Excel

```text
Creá una hoja "Dashboard" (sin líneas de cuadrícula) con:
- Fila de 4 KPIs: Ventas totales, Pedidos, Ticket promedio, Calificación media.
- Filtro de Categoría y Mes: pedí segmentadores (slicers) conectados a las tablas dinámicas; si tu versión del complemento no los crea, usá una celda con lista desplegable de validación y fórmulas `FILTRAR` que dependan de ella.
- 3 gráficos dinámicos: ventas por mes, por categoría y top 10 productos.
- Paleta: azul oscuro, gris y un color de acento. Todo alineado en una grilla.
```

## 🧪 Práctica: análisis de datos con Claude en Excel

Dataset: generá 800 registros de **empleados** (ID, Área, Puesto, Fecha_Ingreso, Salario, Horas_Extra, Evaluación 1–5, Capacitación_Horas, Ausencias, Ciudad) con 5% de faltantes.

Tareas: 1) Insights, 2) resumen estadístico por Área, 3) imputación trazable, 4) formato condicional de Evaluación y Ausencias, 5) 3 gráficos, 6) dashboard con segmentador por Área, 7) conclusión en 5 bullets.

### ✅ Solución (secuencia de prompts)

1. `Diagnosticá calidad de datos: faltantes, duplicados, valores imposibles (salario<0, evaluación fuera de 1-5).`
2. `Hoja "Por Área": con PROMEDIO.SI.CONJUNTO y CONTAR.SI.CONJUNTO calculá dotación, salario medio, evaluación media, ausencias medias y horas de capacitación por Área.`
3. `Imputá Salario con mediana por Puesto, Evaluación con mediana por Área; columnas *_imp y bandera; celdas en celeste.`
4. `Formato condicional: Evaluación escala 3 colores; Ausencias > P90 en rojo.`
5. `Gráficos: salario medio por área (barras), evaluación vs capacitación (dispersión con línea de tendencia), ingresos por año (líneas).`
6. `Dashboard con KPIs (dotación, salario medio, evaluación media, % con horas extra) y segmentador de Área.`
7. `Escribí 5 conclusiones con el número que las respalda y una recomendación por cada una.`

**Autoevaluación:** ¿las fórmulas se recalculan si cambio un dato? ¿La imputación es trazable? ¿El dashboard responde al segmentador?

## 🧠 Autoevaluación

1. ¿Por qué imputar con la mediana por grupo en vez de la media general?
   <details><summary>Ver respuesta</summary>La mediana resiste los outliers, y el grupo (producto, categoría) respeta la estructura de los datos.</details>

2. ¿Qué significa imputar "de forma trazable"?
   <details><summary>Ver respuesta</summary>Conservar los originales, crear columnas imputadas, marcar qué se imputó y documentar el método.</details>

3. ¿Qué ventaja tiene `FILTRAR` frente a copiar filas filtradas?
   <details><summary>Ver respuesta</summary>Es dinámico: el resultado se actualiza solo cuando cambian los datos.</details>

➡️ Siguiente: [Módulo 07 — Modelos financieros](07-modelos-financieros.md)
