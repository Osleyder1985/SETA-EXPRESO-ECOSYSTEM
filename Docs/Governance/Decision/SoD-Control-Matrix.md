# Matriz de controles — Segregación de funciones

**Issue:** #49  
**Problema:** #11  
**Versión:** 1.0.0  

| ID | Control | Clase | Evidencia | Resultado esperado |
|---|---|---|---|---|
| SOD-001 | Clasificar el riesgo antes de determinar independencia | HYBRID | Risk record + classification | Nivel R1–R4 trazable |
| SOD-002 | Determinar la combinación DEFINE/EXECUTE/APPROVE/VERIFY/VALIDATE | HYBRID | SoD matrix | Combinación clasificada |
| SOD-003 | Impedir aprobación independiente cuando R3/R4 lo exija y no exista excepción válida | HUMAN | Decision record + evidence | Independencia aplicada o excepción registrada |
| SOD-004 | Registrar excepciones de segregación | HYBRID | Exception record | Justificación + riesgo residual + compensación |
| SOD-005 | Aplicar revisión independiente a cambios de riesgo moderado cuando corresponda | HUMAN | Review evidence | Revisión trazable |
| SOD-006 | Aplicar separación reforzada a cambios R4 | HUMAN | Approval/validation evidence | No concentración indebida |
| SOD-007 | Mantener autoridad de bloqueo separada de aprobación | HYBRID | Block/escalation evidence | Bloqueo no confundido con aprobación |
| SOD-008 | Verificar SoD en cambios controlados | HYBRID | PR + validation evidence | Control evaluado antes del cierre |
| SOD-009 | Medir excepciones y desviaciones | AUTOMATED/HYBRID | Metrics | Tendencia observable cuando haya datos |

## Regla de evidencia

Un control se considera satisfecho solo cuando existe evidencia verificable correspondiente al cambio concreto. La existencia de esta matriz no constituye por sí misma evidencia de ejecución del control.
