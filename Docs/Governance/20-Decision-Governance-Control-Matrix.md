# Matriz de controles de Decision Governance

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.1  
**Estado:** Matriz propuesta para revisión  
**Fecha:** 2026-09-15  
**Issue:** #33

---

## 1. Propósito

Definir controles verificables para evitar que las decisiones arquitectónicas y de ingeniería relevantes queden únicamente en conocimiento informal o en preferencias no trazables.

## 2. Controles

| ID | Control | Riesgo controlado | Mecanismo | Naturaleza | Evidencia | Estado |
|---|---|---|---|---|---|---|
| DG-001 | Decision Record Structure | Decisión sin razonamiento mínimo | Plantilla ADR/EDR | G | Decision Record | Implementado documentalmente |
| DG-002 | Stable Decision ID | Referencias ambiguas | `ADR-NNN` / `EDR-NNN` | G/D futuro | Index | Implementado documentalmente |
| DG-003 | Context | Decisión sin problema o drivers | Campo obligatorio | G | Record | Implementado documentalmente |
| DG-004 | Alternatives | Selección sin comparación | Campo obligatorio | G | Record | Implementado documentalmente |
| DG-005 | Criteria | Preferencia presentada como ingeniería | Criterios explícitos | G | Record + Evidence | Implementado documentalmente |
| DG-006 | Trade-offs | Costes y compromisos ocultos | Campo obligatorio | G | Record | Implementado documentalmente |
| DG-007 | Consequences | Impactos no evaluados | Campo obligatorio | G | Record | Implementado documentalmente |
| DG-008 | Risk Linkage | Decisión desconectada de riesgos | Referencia a Risk Register | G/D futuro | Record + Register | Implementado documentalmente |
| DG-009 | Evidence | Decisión no verificable | Referencias a evidencia | G | Record | Implementado documentalmente |
| DG-010 | Status Control | Estado ambiguo | Taxonomía controlada | G/D futuro | Record | Implementado documentalmente |
| DG-011 | Supersession | Pérdida de historia | `Supersedes` / `Superseded by` | G | Records + Index | Implementado documentalmente |
| DG-012 | Traceability | Decisión aislada | Requirements / Architecture / Risks / Issues / PRs / Gates | G | Traceability section | Implementado documentalmente |
| DG-013 | Decision Approval | Decisión relevante sin autoridad | Reviewer/Approver según impacto | G | Approval section | Implementado documentalmente |
| DG-014 | Premature Decision Control | Tecnología elegida antes de contexto | Regla explícita durante B/C | G | Decision review | Implementado documentalmente |
| DG-015 | Index Integrity | Decision Records no descubribles | Índice controlado | D futuro | Workflow futuro | No implementado |
| DG-016 | Schema Validation | Record estructuralmente inválido | Validador futuro | D | Workflow futuro | No implementado |
| DG-017 | Link Validation | Referencias rotas | Validador futuro | D | Workflow futuro | No implementado |
| DG-018 | Supersession Consistency | Cadena histórica inconsistente | Validador futuro | D | Workflow futuro | No implementado |
| DG-019 | Decision Metrics | Falta de visibilidad | Métricas futuras | M | Dashboard futuro | No implementado |

## 3. Regla de madurez

Esta baseline establece capacidad documental inicial. Los controles DG-015 a DG-019 son evolución futura y no deben presentarse como automatizados antes de existir implementación y evidencia ejecutable.

## 4. Integración

```text
Need / Problem
      ↓
Requirement / Constraint
      ↓
Decision Record
      ↓
Architecture / Design
      ↓
Implementation
      ↓
Verification / Validation
      ↓
Evidence
```

La Decision Governance complementa Governance Enforcement, Risk Management, Quality, Security y Evidence Validation.

## 5. Aplicación en Quality Gates

Los controles DG son evidencia de gobernanza de decisiones y no sustituyen los Quality Gates. G5 y G6 deberán considerar Decision Records materiales cuando sean aplicables; G12 deberá considerar supersession o actualización de decisiones cuando una evolución modifique la baseline.
