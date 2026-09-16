# Non-Conformance Management

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Baseline propuesta para revisión  
**Issue principal:** #62  
**Issue relacionado:** #51 (antecedente de formalización)

## 1. Propósito

Formalizar el tratamiento de incumplimientos de requisitos, controles, gates, criterios de aceptación o condiciones de baseline.

## 2. Flujo obligatorio

```text
Detection → Non-Conformance Record → Classification → Containment
→ Root Cause Analysis → Corrective Action → Preventive Action
→ Verification of Effectiveness → Closure
```

## 3. Fuentes

Quality Gate FAIL, Governance/Quality/Security/Evidence Validation FAIL, incumplimiento de requisitos, desviación de proceso, revisión, auditoría, incidente, configuración o riesgo.

## 4. Clasificación

| Clase | Aplicación | Tratamiento mínimo |
|---|---|---|
| NC-L | impacto limitado | corrección + verificación |
| NC-M | impacto material localizado | RCA + correctiva + preventiva cuando aplique |
| NC-H | impacto alto/riesgo significativo | RCA formal + autoridad + verificación independiente cuando aplique |
| NC-C | seguridad, privacidad, financiero, regulatorio o producción crítica | contención + autoridad + validación independiente + riesgo residual formal |

La clasificación puede elevarse con nueva evidencia.

## 5. Root Cause

La causa raíz debe explicar el mecanismo que permitió el incumplimiento. "Error humano" por sí solo no es suficiente. Se puede usar 5 Whys, Ishikawa, análisis causal, de proceso o de barreras según severidad.

## 6. Corrective / Preventive Action

La acción correctiva elimina el incumplimiento observado. La preventiva reduce su recurrencia mediante cambios de test, gate, automatización, revisión, documentación o proceso.

## 7. Verification and Closure

El cierre requiere evidencia de ejecución de acciones, recuperación del control, tratamiento de riesgos residuales y actualización de artefactos afectados. Las NC históricas no se eliminan para ocultar fallos.

## 8. Registro mínimo

```yaml
NC-ID:
Detected-Date:
Detected-By:
Source:
Related-Issue:
Related-PR:
Related-Gate:
Classification: NC-L|NC-M|NC-H|NC-C
Description:
Impact:
Containment:
Root-Cause:
Corrective-Action:
Preventive-Action:
Verification:
Residual-Risk:
Risk-Acceptance:
Evidence: []
Owner:
Approver:
Status: OPEN|CONTAINED|ANALYZING|ACTION_REQUIRED|VERIFYING|CLOSED
Closure-Date:
```

## 9. Gate interaction

```text
GATE PASS → continuar
GATE FAIL → registrar/tratar NC cuando exista incumplimiento material
```

Una excepción formal no convierte un FAIL en PASS; si se autoriza avance con riesgo residual, debe existir decisión y aceptación formal.

## 10. Integración

La NC se integra con Risk, Change, Decision, Quality, Security, Evidence, Configuration, Data, AI y Research Governance.
