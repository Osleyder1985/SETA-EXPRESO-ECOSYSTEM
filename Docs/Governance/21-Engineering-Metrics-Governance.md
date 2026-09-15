# 21 — Engineering Metrics Governance

**Versión:** 0.1.0
**Estado:** Propuesta controlada

## 1. Propósito

Establecer el sistema formal para definir, medir, interpretar, gobernar y evolucionar las métricas de ingeniería del Ecosistema SETA EXPRESO.

El objetivo no es producir un número atractivo, sino obtener evidencia reproducible sobre la salud de la ingeniería y utilizarla para detectar desviaciones, decidir acciones y orientar la mejora continua.

## 2. Principios

- **Definition before measurement:** una métrica debe tener definición operacional antes de calcularse.
- **Evidence before score:** ningún indicador se declara disponible sin una fuente verificable.
- **Trend before isolated value:** la tendencia contextualizada es preferible a una observación aislada.
- **Context before threshold:** umbrales y objetivos requieren contexto del sistema.
- **No vanity metrics:** no se incorporan indicadores únicamente por ser fáciles de contar.
- **No false precision:** los datos incompletos o estimados deben declararse explícitamente.
- **Owner:** toda métrica controlada debe tener responsable.
- **Actionability:** una métrica de control debe conducir a una acción o decisión cuando se desvía.
- **Reproducibility:** otra persona debe poder reconstruir el cálculo.
- **Historical integrity:** los valores históricos no se reescriben para mejorar artificialmente la tendencia.

## 3. Modelo de una métrica

Cada métrica debe conservar como mínimo:

`Metric ID → Name → Dimension → Type → Definition → Formula → Unit → Scope → Source → Collection Method → Frequency → Owner → Baseline → Target → Thresholds → Evidence → Limitations → Status`

## 4. Tipos

- **Descriptive:** describe qué ocurrió.
- **Diagnostic:** ayuda a explicar por qué ocurrió.
- **Control:** permite detectar una condición que requiere acción.
- **Outcome:** mide un resultado de negocio, producto o sistema.
- **Leading:** proporciona señal temprana.
- **Lagging:** mide un resultado posterior.

Una métrica puede tener más de una clasificación.

## 5. Estado de disponibilidad

- `defined`: definición aprobada, todavía sin medición operacional.
- `available`: fuente confiable y cálculo reproducible disponibles.
- `provisional`: medición disponible con limitaciones conocidas.
- `blocked`: fuente o calidad de datos insuficiente.
- `deprecated`: retirada por evolución del sistema métrico.

**TBD** es un estado explícito y válido cuando todavía no existe evidencia suficiente.

## 6. Dimensiones iniciales

### Delivery

- Lead Time
- Change Failure Rate
- Deployment Frequency
- Recovery Time

### Quality

- Defect Density
- Escaped Defects
- Test Coverage
- Requirement Coverage

### Requirements

- % requisitos trazables
- % requisitos verificados
- % requisitos ambiguos
- Change Volatility

### Architecture

- Architectural Debt
- ADR Coverage
- Architecture Compliance

### Security

- Vulnerabilities
- Remediation Time
- Dependency Risk
- Secrets Exposure

### Governance

- % PR con Issue
- % PR con Impact Analysis
- % PR con Evidence
- % cambios fuera de proceso
- % Gates PASS
- % artefactos sin Owner

## 7. Reglas de cálculo

Toda fórmula debe definir explícitamente numerador, denominador, población, periodo y exclusiones relevantes.

Porcentajes:

`Percentage = Numerator / Denominator × 100`

Coberturas:

`Coverage = Covered Items / Applicable Items × 100`

Cuando el denominador sea cero o no pueda establecerse con evidencia, el resultado debe ser `N/A`, nunca cero por defecto.

## 8. Baseline, objetivo y umbrales

- **Baseline:** punto de referencia observado y fechado.
- **Target:** estado objetivo aprobado.
- **Threshold:** frontera operacional que genera atención o acción.

No se inventarán targets ni thresholds antes de disponer de datos suficientes. En ese caso se registra `TBD` junto con la razón y la evidencia requerida.

## 9. Trazabilidad

```text
Metric
  ↓
Source
  ↓
Collection
  ↓
Calculation
  ↓
Evidence
  ↓
Interpretation
  ↓
Decision / Action
  ↓
Outcome
```

Las métricas relevantes podrán relacionarse con Issues, PRs, requisitos, riesgos, ADR/EDR, Quality Gates, controles de seguridad y acciones de mejora.

## 10. Engineering Governance Dashboard

El Dashboard será una **vista derivada**, nunca la fuente de verdad.

Debe presentar como mínimo:

1. salud global y cobertura del sistema métrico;
2. Delivery;
3. Quality;
4. Requirements;
5. Architecture;
6. Security;
7. Governance;
8. tendencias temporales;
9. indicadores sin datos o con limitaciones;
10. alertas y acciones asociadas;
11. trazabilidad hacia evidencia.

## 11. Interpretación

Una métrica no debe interpretarse de forma aislada. Antes de tomar una acción se debe revisar:

- periodo de medición;
- tamaño de muestra;
- cambios de proceso;
- cambios de alcance;
- calidad de la fuente;
- posibles efectos de medición;
- relación con otras métricas;
- riesgos y decisiones relacionados.

## 12. Gobernanza del sistema métrico

Los cambios de definición, fórmula, fuente, umbral o alcance de una métrica son cambios controlados y deben conservar historial.

Las métricas materialmente relevantes para arquitectura, seguridad, calidad o gobernanza deben poder vincularse con el artefacto de decisión o control correspondiente.

## 13. Automatización futura

La primera baseline establece el modelo documental. La automatización futura podrá incluir extracción desde GitHub, validación de esquemas, cálculo reproducible, snapshots históricos, detección de tendencias, alertas, correlación entre métricas y generación automática del Dashboard.

No se declara implementada ninguna automatización que todavía no exista.

## 14. Madurez

**Problema #4 no se considera resuelto únicamente por crear este documento.** La capacidad inicial queda establecida documentalmente; la madurez aumentará cuando existan fuentes reales, baselines, series históricas, controles automatizados y decisiones de mejora basadas en evidencia.
