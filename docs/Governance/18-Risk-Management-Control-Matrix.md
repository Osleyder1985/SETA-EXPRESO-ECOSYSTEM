# Matriz de controles de Risk Management

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Matriz propuesta para revisión  
**Fecha:** 2026-09-15  
**Issue:** #31

---

## 1. Propósito

Definir controles verificables para que el Risk Management System no dependa únicamente de la existencia de un documento o de memoria humana.

Los controles se clasifican como gobernanza, preventivos/compensatorios, detectivos o métricos. Ninguno debe describirse como automatizado hasta disponer de una implementación ejecutable y evidencia de ejecución.

## 2. Controles

| ID | Control | Riesgo controlado | Mecanismo inicial | Naturaleza | Evidencia | Estado |
|---|---|---|---|---|---|---|
| RM-001 | Risk Register presente | Riesgos relevantes sin registro | Archivo estructurado versionado | G/D | `Risk-Register.yml` | Implementado |
| RM-002 | Risk ID único | Riesgos duplicados o referencias ambiguas | Regla de identificador `RISK-NNN` | G/D | Register | Implementado |
| RM-003 | Estructura mínima | Riesgos sin información esencial | Campos obligatorios definidos | G | Register + System | Implementado |
| RM-004 | Probability válida | Valoraciones inconsistentes | Escala 1–5 documentada | G/D futuro | Register | Implementado documentalmente |
| RM-005 | Impact válido | Valoraciones inconsistentes | Escala 1–5 documentada | G/D futuro | Register | Implementado documentalmente |
| RM-006 | Exposure reproducible | Priorización no trazable | `P × I` | D futuro | Register | Implementado documentalmente |
| RM-007 | Owner obligatorio | Riesgo sin responsabilidad | Campo obligatorio | G/D | Register | Implementado documentalmente |
| RM-008 | Review Date obligatoria | Riesgo sin seguimiento | Campo obligatorio | G/D | Register | Implementado documentalmente |
| RM-009 | Treatment explícito | Respuesta ambigua | Taxonomía controlada | G | Register | Implementado documentalmente |
| RM-010 | Mitigation/Contingency/Trigger separados | Respuesta mal definida | Campos separados | G | Register | Implementado documentalmente |
| RM-011 | Residual Risk | Tratamiento sin reevaluación | Valoración posterior | G/D futuro | Register | Implementado documentalmente |
| RM-012 | Evidencia trazable | Riesgo sin soporte verificable | Referencias controladas | G/D | Register | Implementado documentalmente |
| RM-013 | Revisión por evento | Riesgo obsoleto | Trigger + regla de revisión | G | Register / records | Implementado documentalmente |
| RM-014 | Integración con Quality Gates | Gate sin consideración de riesgos | Criterios de gates | G | `04-Quality-Gates.md` + Risk System | Implementado por política existente |
| RM-015 | Actualización normativa | Método de riesgo desactualizado | Revisión de matriz de estándares | G | `02-Standards-Lifecycle-Matrix.md` | Implementado |
| RM-016 | Validación de esquema | Register estructuralmente inválido | YAML/schema validation | D | Workflow futuro | No implementado |
| RM-017 | Cálculo automático | Exposure incorrecta | Script de validación | D | Workflow futuro | No implementado |
| RM-018 | Riesgo vencido | Review Date superada sin revisión | Automatización de fecha | D | Workflow futuro | No implementado |
| RM-019 | Métricas | Falta de visibilidad de cartera | Métricas del register | M | Dashboard futuro | No implementado |

## 3. Regla de madurez

La baseline actual proporciona un **sistema documental operativo en construcción**, no un sistema de automatización completa.

Los controles RM-016 a RM-019 son trabajo futuro y no deben presentarse como implementados hasta que exista código/workflow y evidencia ejecutable.

## 4. Relación con controles existentes

```text
Risk Management
      ↓
Governance Enforcement
      ↓
Quality Validation
      ↓
Security Validation
      ↓
Evidence Validation
      ↓
Quality Gates
```

El Risk Management System complementa las cuatro capas de validación. No las sustituye.

## 5. Relación con el riesgo residual de gobernanza

`RISK-001` es el primer riesgo registrado porque ya existe evidencia objetiva de la limitación de enforcement nativo de `main` bajo las condiciones actuales. Su valoración y tratamiento deben revisarse cuando cambie la plataforma, el plan de GitHub, la configuración del repositorio o la arquitectura de control.
