---
description: Forecast de 12 meses con 3 escenarios a partir de un Excel de datos históricos
argument-hint: <archivo.xlsx>
---

Leé el archivo $ARGUMENTS (serie mensual histórica).

1. Analizá la tendencia y la estacionalidad.
2. Compará 3 métodos (media móvil, Holt-Winters y regresión con estacionalidad). Usá los últimos 6 meses como validación y reportá el MAPE de cada uno.
3. Elegí el mejor método y proyectá 12 meses en 3 escenarios: base, optimista (+1 desvío) y pesimista (−1 desvío).
4. Entregá `forecast.xlsx` con una hoja de supuestos editables (en azul), una hoja de cálculo con fórmulas enlazadas y un gráfico con los 3 escenarios.
5. Explicá en 5 bullets los resultados y las limitaciones del forecast.
