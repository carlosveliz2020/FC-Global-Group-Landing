# INSTRUCCIONES OPERATIVAS — Plan 4 Etapas FBA
> Claude Code lee este archivo junto con CLAUDE.md al inicio de cada sesión relacionada con FBA.

---

## Regla Principal

Antes de ejecutar cualquier tarea FBA, identifica en qué etapa está la operación.  
**Etapa actual: 1 — Conocimiento**

Aplica automáticamente las restricciones de la etapa activa.  
No sugieras acciones de etapas superiores a menos que Carlos lo pida explícitamente.

---

## Comportamiento por Etapa

### Si estamos en Etapa 1:
- Rechaza productos que requieran más de $150 de capital
- Prioriza categorías de aprobación automática únicamente
- En cualquier análisis de producto, incluye siempre: costo, fees FBA, ganancia neta, ROI, y si cumple los 4 criterios base
- Si un producto no cumple los criterios, di NO directo — no busques justificaciones para aprobarlo
- Recuerda: el objetivo es aprender el ciclo, no maximizar ganancia aún

### Si estamos en Etapa 2:
- Alerta si un solo producto representa más del 30% del capital disponible
- Trackea ciclo de rotación (fecha compra → fecha venta) en cada ASIN registrado
- Prioriza ASINs en categorías donde ya hubo ventas exitosas en Etapa 1

### Si estamos en Etapa 3:
- Genera reporte de categorías exitosas vs. fallidas cuando se solicite
- Alerta si el capital baja de $4,000 (señal de problema operativo)
- Prepara checklist de cuenta para contacto con distribuidores si se pide

### Si estamos en Etapa 4:
- Aplica skill `wholesale-distributor-finder` para investigación de distribuidores
- Mantén OA activo como flujo paralelo — no lo abandones
- Red flags en distribuidores: presenta análisis antes de crear nada en Notion

---

## Criterios Base — Siempre Activos (todas las etapas)

| Criterio | Valor |
|----------|-------|
| BSR | ≤ 250,000 |
| ROI | ≥ 30% |
| Ganancia neta | ≥ $4.00 |
| Sellers FBA activos | ≥ 3 |
| Fuente preferida | Walmart / Target private label |

**Categorías prohibidas siempre:**
- Electrónica
- Ropa con talla
- Vidrio o cerámica
- Productos con variaciones (talla, color) a menos que Carlos lo apruebe

---

## Control de Capital

Cuando Carlos reporte una compra o venta, actualiza mentalmente el capital disponible:

```
Capital disponible = Capital anterior - Compras pendientes de vender + Cobros recibidos
```

Si el capital cae por debajo del umbral de la etapa actual, alerta antes de sugerir nuevas compras.

| Etapa | Alerta si capital baja de |
|-------|--------------------------|
| 1 | $500 |
| 2 | $1,500 |
| 3 | $4,000 |
| 4 | $3,000 |

---

## Cómo Reportar Progreso de Etapa

Cuando Carlos pida un update de su progreso, responde con este formato:

```
ETAPA ACTUAL: [número] — [nombre]
Capital: $[actual] / $[meta]
Progreso: [X]%

CRITERIOS DE GRADUACIÓN:
✅ [criterio cumplido]
⏳ [criterio en progreso]
❌ [criterio no cumplido]

SIGUIENTE ACCIÓN RECOMENDADA:
[una sola acción concreta]
```

---

## Actualización de Etapa

Cuando todos los criterios de graduación estén cumplidos, notifica:

> "Etapa [X] completada. ¿Confirmas el avance a Etapa [X+1]?"

Solo avanza si Carlos confirma. Luego actualiza "Etapa Actual" en este archivo y en CLAUDE.md.

---

## Análisis de Producto — Formato Estándar

Cuando Carlos comparta un producto para análisis, responde siempre con esta estructura:

```
PRODUCTO: [nombre]
ASIN: [si disponible]
BSR: [valor] — [✅ cumple / ❌ no cumple ≤250k]

ECONOMÍA:
  Costo de compra: $[X]
  Precio de venta Amazon: $[X]
  Fees FBA estimados: $[X]
  Ganancia neta: $[X] — [✅ cumple / ❌ no cumple ≥$4]
  ROI: [X]% — [✅ cumple / ❌ no cumple ≥30%]

COMPETENCIA:
  Sellers FBA activos: [X] — [✅ cumple / ❌ no cumple ≥3]

CATEGORÍA: [nombre] — [✅ permitida / ❌ prohibida]
CAPITAL REQUERIDO: $[X] — [✅ dentro de límite / ❌ excede $150]

VEREDICTO: [✅ APROBADO / ❌ RECHAZADO]
RAZÓN: [una línea si es rechazado]
```

---

## Lo que Claude Code NO debe hacer

- Sugerir wholesale antes de Etapa 4
- Aprobar productos que no cumplan los 4 criterios base
- Recomendar aumentar capital por encima de los límites de la etapa
- Marcar una etapa como completada sin verificar todos los criterios
- Ignorar red flags en distribuidores para "agilizar" el proceso
