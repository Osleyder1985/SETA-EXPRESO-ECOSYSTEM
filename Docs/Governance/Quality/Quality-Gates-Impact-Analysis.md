# Análisis de impacto — Quality Gates Operationalization

**Issue:** #43  
**Branch:** `issue-43-quality-gates-operationalization`  
**Estado:** Controlado en PR #44  
**Fecha:** 2026-09-15

## 1. Objetivo

Evaluar el impacto de operacionalizar los Quality Gates G0–G13 y de introducir un catálogo machine-readable con criterios, checks, métricas, evidencia y decisiones.

## 2. Artefactos afectados

| Área | Impacto | Acción |
|---|---|---|
| Lifecycle | Alto | Gates asociados a fases A–O |
| Governance | Alto | Criterios de avance y decisión operacionalizados |
| Requirements | Alto | G3 incorpora checks objetivos y futuros automatizables |
| Architecture | Medio | G5 exige evidencia y Decision Records aplicables |
| Design | Medio | G6 exige trazabilidad de decisiones materiales |
| Testing | Alto | G8 consume evidencia de verificación |
| Security | Medio | Gates consideran evidencia de Security Validation |
| Evidence | Alto | Cada gate define evidencia requerida |
| Risk | Medio | Riesgos y condiciones forman parte de la decisión |
| Decision Governance | Alto | Autoridad y Decision Records quedan integrados |
| Metrics | Alto | Métricas pasan a ser evidencia formal cuando exista fuente confiable |
| AI Governance | Medio | Aplicabilidad de controles de IA incorporada |
| Data Governance | Medio | Se reserva integración conforme exista contexto de datos |
| Supplier/Third-Party | Medio | Dependencias y proveedores se consideran en gates aplicables |
| Quality Validation | Alto | QV queda explícitamente como fuente de evidencia, no como gate |

## 3. Riesgos y mitigaciones

- **Riesgo:** convertir criterios provisionales en resultados reales. **Mitigación:** no inventar valores; registrar estado y limitaciones.
- **Riesgo:** confundir QV PASS con Gate PASS. **Mitigación:** separación explícita de responsabilidades.
- **Riesgo:** automatizar juicio humano. **Mitigación:** clasificación AUTOMATED/HYBRID/HUMAN.
- **Riesgo:** renumerar G3/G4 sin trazabilidad. **Mitigación:** conservar IDs vigentes y exigir Decision Record + análisis de impacto para una renumeración futura.
- **Riesgo:** catálogo desactualizado respecto de los gates documentales. **Mitigación:** ambos artefactos forman parte de la unidad de cambio.

## 4. Trazabilidad

```text
Issue #43
  ↓
PR #44
  ↓
04-Quality-Gates.md
  ↓
Quality-Gate-Catalog.yml
  ↓
12-Quality-Validation-Architecture.md
  ↓
Validation Evidence
  ↓
Quality Gate Decision
```

## 5. Resultado

El impacto se considera controlado para esta unidad documental. La automatización completa queda condicionada a la existencia de fuentes estructuradas para requisitos, arquitectura, pruebas, datos, infraestructura y telemetría operacional.
