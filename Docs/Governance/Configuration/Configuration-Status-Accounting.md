# Configuration Status Accounting

**Versión:** 1.0.0  
**Issue:** #45  
**Estado:** Propuesto

## Propósito

Registrar el estado actual de los Configuration Items y permitir reconstruir su evolución, baseline, cambios y evidencia.

## Estados iniciales

| CI | Estado | Versión | Baseline | Observación |
|---|---|---|---|---|
| CI-001 | PROPOSED | 0.1.0 | — | Requisitos todavía no baselined |
| CI-002 | PROPOSED | 0.1.0 | — | Arquitectura todavía no baselined |
| CI-003 | PROPOSED | 0.1.0 | — | Schema todavía no definido |
| CI-004 | PROPOSED | 0.1.0 | — | Contrato todavía no definido |
| CI-005 | PROPOSED | 0.1.0 | — | Security baseline todavía no baselined |
| CI-006 | PROPOSED | 0.1.0 | — | Infraestructura todavía no definida |
| CI-007 | ACTIVE | 0.1.0 | — | Existe código controlado en Git |
| CI-008 | ACTIVE | 0.1.0 | — | Existe estructura de pruebas controlada |
| CI-009 | PROPOSED | 0.1.0 | — | Configuración de despliegue todavía no definida |

## Regla

Ningún CI deberá marcarse `BASELINED` hasta que exista evidencia de aprobación y pertenencia a una baseline identificada.

## Accounting futuro

Cada transición deberá registrar:

```text
CI
→ versión anterior
→ cambio
→ Issue
→ PR
→ commit
→ nueva versión
→ nueva baseline, si corresponde
→ aprobación
→ evidencia
```

Los estados y valores `TBD` no representan datos operacionales inexistentes como si fueran hechos; representan explícitamente una capacidad pendiente de maduración.
