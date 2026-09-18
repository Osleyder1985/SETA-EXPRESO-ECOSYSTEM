# H-005 — Matriz de operacionalización transversal SoD

**Issue:** #185  
**Fecha:** 2026-09-18  
**Baseline:** `main` / `e2933ebccb873d944e2431dafb024d76b9d335d2`

## Criterio

Una integración sólo se considera **operacionalizada** cuando existe un mecanismo ejecutable y evidencia reproducible de su ejecución. Una referencia documental o un estado `INTEGRATED` no constituyen por sí solos evidencia de efectividad.

| Dominio | Punto de decisión SoD | Mecanismo verificable en baseline | Evidencia de ejecución | Estado |
|---|---|---|---|---|
| Decision Authority | Autoridad/independencia de decisiones | Matrix + Register | Estructura documental | DOCUMENTAL |
| Risk Management | Risk Level → independencia | Risk/SoD matrices | No se identificó ejecución transversal específica en esta auditoría | DOCUMENTAL |
| Quality Gates | Gates de riesgo → revisión/independencia | Quality Gates + SoD matrices | Validaciones de PR existentes, pero no prueban por sí mismas decisión SoD del gate | PENDIENTE |
| Change Control | Cambio → clasificación SoD | Change Workflow + SoD | Flujo Issue/Branch/PR verificable; clasificación SoD específica no demostrada para cada cambio | PENDIENTE |
| Configuration Management | CI/baseline → independencia | CM policy + SoD | Política y registro; ejecución SoD no demostrada | PENDIENTE |
| Security | Impacto seguridad → independencia | Security Validation + SoD | Security Validation ejecuta controles técnicos; no demuestra independencia SoD por sí sola | PENDIENTE |
| Data | Decisión de datos → independencia | Data Governance + SoD | No hay evidencia de ejecución específica en esta baseline | PENDIENTE |
| AI | Decisión IA → independencia | AI Governance + SoD | No hay evidencia de ejecución específica en esta baseline | PENDIENTE |
| Supplier | Selección/aprobación/aceptación → independencia | Supplier Governance + SoD | No hay evidencia de ejecución específica en esta baseline | PENDIENTE |
| Metrics | Excepciones/desviaciones SoD → medición | Metrics Governance + Metric Catalog | Métricas operacionales de primera capa existen; no se demostró métrica SoD transversal ejecutada | PENDIENTE |

## Evidencia ya existente que no debe sobreinterpretarse

- Governance/Quality/Security/Evidence validations demuestran ejecución de sus respectivos workflows.
- El registro SoD demuestra el **alcance y estado registral** de las integraciones.
- Las matrices SoD demuestran reglas y vocabulario.
- Ninguno de estos elementos, aislado, demuestra que una decisión real haya sido sometida a independencia SoD.

## Resultado H-005

**No se declara H-005 completamente resuelto.**

La primera capa de operacionalización queda definida de forma reproducible y la auditoría establece qué evidencia falta para convertir cada integración documental en integración operacional.

## Próxima evidencia mínima

Para cada dominio pendiente se requiere, cuando exista un caso aplicable:

1. ID de cambio/decisión;
2. clasificación de riesgo;
3. regla SoD aplicable;
4. función/rol requerido;
5. decisión o aprobación;
6. evidencia fechada;
7. resultado;
8. trazabilidad al Issue/PR/artefacto;
9. excepción registrada si no puede cumplirse la independencia;
10. evidencia de efectividad cuando corresponda.

## Regla de no ficción

Si no existe un caso real aplicable, no se fabricará una ejecución. Se conservará `PENDING` o `NOT_APPLICABLE` con condición de reevaluación.

## Metadata

```yaml
governance:
  schema_version: "1"
  classification:
    domain: governance
    work_type: process
  validation:
    evidence: required
    governance: required
    quality: required
    security: required
```
