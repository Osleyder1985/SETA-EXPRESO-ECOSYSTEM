# Non-Conformance Management

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Baseline propuesta para revisión  
**Issues:** #62, #51, #52

---

## 1. Propósito

Establecer el tratamiento formal de cualquier incumplimiento de un requisito, control, gate, criterio de aceptación o condición de baseline.

Una no conformidad no se resuelve simplemente repitiendo el control fallido. Debe existir una cadena de tratamiento y evidencia.

## 2. Flujo obligatorio

```text
Detection
   ↓
Non-Conformance Record
   ↓
Classification
   ↓
Containment
   ↓
Root Cause Analysis
   ↓
Corrective Action
   ↓
Preventive Action
   ↓
Verification of Effectiveness
   ↓
Closure
```

## 3. Fuentes de detección

Una NC puede originarse en:

- Quality Gate FAIL;
- Governance Validation FAIL;
- Security Validation FAIL;
- Evidence Validation FAIL;
- incumplimiento de requisito;
- desviación de proceso;
- defecto detectado en revisión;
- auditoría;
- incidente;
- control de configuración;
- hallazgo de riesgo.

## 4. Clasificación

| Clase | Descripción | Tratamiento mínimo |
|---|---|---|
| NC-L | impacto limitado | corrección + verificación |
| NC-M | impacto material localizado | RCA + acción correctiva + prevención cuando aplique |
| NC-H | impacto alto o riesgo significativo | RCA formal + autoridad correspondiente + verificación independiente cuando aplique |
| NC-C | impacto crítico, seguridad, privacidad, financiero, regulatorio o producción crítica | contención inmediata + autoridad + validación independiente + aceptación formal del riesgo residual si procede |

La clasificación puede elevarse si la evidencia posterior demuestra mayor impacto.

## 5. Containment

Cuando el problema pueda continuar causando daño mientras se prepara la corrección, debe registrarse una medida de contención. Ejemplos: bloquear el gate, impedir merge/deployment, aislar un componente o suspender un uso.

## 6. Root Cause Analysis

La causa raíz debe explicar el mecanismo que permitió la no conformidad. "Error humano" por sí solo no constituye RCA suficiente.

Se puede utilizar:

- 5 Whys;
- Ishikawa/Fishbone;
- análisis causal;
- análisis de proceso;
- análisis de barreras y controles.

El método elegido debe ser proporcional a la severidad.

## 7. Corrective Action

La acción correctiva elimina la no conformidad observada.

Ejemplo:

```text
Gate FAIL
  ↓
corregir artefacto
  ↓
re-ejecutar validación
```

## 8. Preventive Action

La acción preventiva reduce la probabilidad de recurrencia. Puede incluir un nuevo test, control, gate, automatización, revisión, documentación o cambio de proceso.

## 9. Verification

No basta con declarar la corrección. Debe conservarse evidencia que demuestre que:

1. la acción fue ejecutada;
2. el control volvió a cumplirse;
3. cuando corresponda, la causa de recurrencia quedó mitigada.

## 10. Closure

Una NC puede cerrarse solamente cuando:

- las acciones requeridas están completadas;
- existe evidencia verificable;
- el resultado fue validado;
- los riesgos residuales fueron tratados según autoridad;
- los artefactos afectados fueron actualizados;
- se conserva la relación con Issue, PR, gate y evidencias.

## 11. Registro mínimo

Cada NC debe registrar:

```yaml
NC-ID:
Detected-Date:
Detected-By:
Source:
Related-Issue:
Related-PR:
Related-Gate:
Classification:
Description:
Impact:
Containment:
Root-Cause:
Corrective-Action:
Preventive-Action:
Verification:
Residual-Risk:
Risk-Acceptance:
Evidence:
Owner:
Approver:
Status:
Closure-Date:
```

## 12. Integridad histórica

Las NC cerradas no se eliminan para ocultar un fallo histórico. Si una conclusión cambia, se registra la nueva información conservando la historia anterior.

## 13. Relación con Gates

```text
GATE PASS → continuar
GATE FAIL → NC cuando exista incumplimiento material
```

Una excepción formal no convierte un FAIL en PASS. Si se permite avanzar bajo riesgo aceptado, debe quedar explícita la decisión y el riesgo residual.

## 14. Integración

La NC se integra con Risk, Change, Decision, Quality, Security, Evidence, Configuration, Data, AI y Research Governance.
