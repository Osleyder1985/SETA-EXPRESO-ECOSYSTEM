# 22 — Engineering Metrics Control Matrix

**Versión:** 0.1.0

| ID | Control | Estado | Evidencia esperada |
|---|---|---|---|
| EM-001 | Política formal de métricas | Implementado documentalmente | 21-Engineering-Metrics-Governance.md |
| EM-002 | Identificador único de métrica | Implementado documentalmente | Catálogo |
| EM-003 | Definición operacional | Implementado documentalmente | Catálogo |
| EM-004 | Fórmula reproducible | Implementado documentalmente | Catálogo |
| EM-005 | Numerador y denominador explícitos | Implementado documentalmente | Catálogo |
| EM-006 | Unidad de medida | Implementado documentalmente | Catálogo |
| EM-007 | Fuente identificada | Implementado documentalmente | Catálogo |
| EM-008 | Método de recolección | Implementado documentalmente | Catálogo |
| EM-009 | Frecuencia de medición | Implementado documentalmente | Catálogo |
| EM-010 | Owner de métrica | Implementado documentalmente | Catálogo |
| EM-011 | Baseline fechada | Preparado; requiere datos reales | Evidencia de medición |
| EM-012 | Target contextualizado | Preparado; puede ser TBD | Decisión/objetivo |
| EM-013 | Threshold contextualizado | Preparado; puede ser TBD | Regla de control |
| EM-014 | Estado de disponibilidad | Implementado documentalmente | Catálogo |
| EM-015 | Limitaciones y calidad de datos | Implementado documentalmente | Catálogo |
| EM-016 | Trazabilidad hacia evidencia | Implementado documentalmente | Registro de evidencia |
| EM-017 | Relación con riesgos | Preparado | Risk Register |
| EM-018 | Relación con decisiones | Preparado | ADR/EDR |
| EM-019 | Dashboard derivado | Implementado como diseño inicial | Dashboard |
| EM-020 | Histórico reproducible | Futuro | Snapshots |
| EM-021 | Extracción automática | Futuro | Workflow/script |
| EM-022 | Cálculo automático | Futuro | Workflow/script |
| EM-023 | Validación automática del catálogo | Futuro | Workflow |
| EM-024 | Detección de tendencias | Futuro | Dashboard |
| EM-025 | Alertas accionables | Futuro | Dashboard/workflow |
| EM-026 | Correlación entre métricas | Futuro | Analysis |
| EM-027 | Métricas de salud global | Futuro | Dashboard |
| EM-028 | Revisión periódica del sistema métrico | Preparado | Registro de revisión |

## Regla de control

Una métrica no puede presentarse como indicador confiable si carece de definición operacional, fuente y método de cálculo reproducible.

La ausencia de datos se representa explícitamente; no se transforma en cero ni se oculta.
