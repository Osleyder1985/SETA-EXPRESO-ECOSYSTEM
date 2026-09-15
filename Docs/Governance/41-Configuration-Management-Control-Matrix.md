# Matriz de controles de Configuration Management

**Versión:** 1.0.0  
**Issue:** #45  
**Estado:** Propuesto

| Control | Objetivo | Clase inicial | Evidencia |
|---|---|---|---|
| CM-001 | CI único y estable | AUTOMATED/HYBRID | CI Register |
| CM-002 | Owner definido | AUTOMATED | CI Register |
| CM-003 | Estado de CI válido | AUTOMATED | CI Register |
| CM-004 | Versión registrada | AUTOMATED | CI Register |
| CM-005 | Baseline identificada | AUTOMATED | Baseline Register |
| CM-006 | Dependencias registradas | HYBRID | CI Register / Impact Analysis |
| CM-007 | Cambio trazable a Issue/PR | HYBRID | Change history / PR |
| CM-008 | Aprobación trazable | HYBRID | Approval evidence |
| CM-009 | Evidence disponible | HYBRID | Evidence index |
| CM-010 | Baseline consistente con CIs | HYBRID | Configuration audit |
| CM-011 | No CI crítico sin owner | AUTOMATED | CI Register |
| CM-012 | No baseline sin aprobación | AUTOMATED/HYBRID | Baseline Register |
| CM-013 | Status accounting actualizado | HYBRID | Status Accounting |
| CM-014 | Desviaciones identificadas | HYBRID | Audit record |
| CM-015 | Reconciliation con Git/CI-CD | FUTURE | Reconciliation report |

## Estados de automatización

- `AUTOMATED`: puede comprobarse con reglas deterministas.
- `HYBRID`: requiere comprobación automática y juicio humano/evidencia.
- `FUTURE`: capacidad todavía no implementada.

La matriz no declara automatización inexistente.
