# Registro de autoridad de decisiones

| Decision ID | Decisión | Accountable | Approval | Blocking | Evidence | Escalation |
|---|---|---|---|---|---|---|
| DEC-001 | Valor/prioridad | Product Owner | Product Owner | — | Objectives + impact | System Owner |
| DEC-002 | Alcance sistémico | System Owner | System Owner | — | Objectives + requirements | Product Owner |
| DEC-003 | Baseline de requisitos | Requirements Owner | Requirements Owner | QA Owner | Requirements + traceability | System Owner |
| DEC-004 | Arquitectura de sistema | System Architect | System Architect | Security Owner when applicable | ADR + risks | System Owner |
| DEC-005 | Arquitectura software | Software Architect | Software Architect | Security/QA when applicable | ADR + design evidence | System Architect |
| DEC-006 | Seguridad | Security Owner | Security Owner | Security Owner | Security evidence + risk | System Owner |
| DEC-007 | Datos | Data Owner | Data Owner | Security when applicable | Classification + lineage | System Owner |
| DEC-008 | Calidad/gate | QA Owner | QA Owner | QA Owner | Metrics + test evidence | System Owner |
| DEC-009 | Plataforma | DevOps/Platform Owner | DevOps/Platform Owner | Security when applicable | Configuration evidence | Operations Owner |
| DEC-010 | Operación | Operations Owner | Operations Owner | Security when applicable | Readiness + operational metrics | System Owner |
| DEC-011 | Investigación | Research Owner | Research Owner | — | Method + reproducibility evidence | System Owner |
| DEC-012 | Cambio controlado | Change Authority | Change Authority | Domain Owner when applicable | Impact + validations + decision record | System Owner |

## Regla

La autoridad accountable no puede inferirse únicamente del autor del commit, PR o documento. Debe derivarse del registro de autoridad vigente.


## Mirror contract

**Fuente canónica:** `Decision-Authority-Matrix.yml`  
**Rol de este documento:** vista legible derivada; no es fuente de autoridad independiente.

Los cambios de roles, decisiones, accountable, approval, blocking, consulted o evidence se realizan primero en YAML y el MD se sincroniza en el mismo cambio controlado. Ante discrepancia, **prevalece YAML** y el drift debe registrarse como no conformidad.

La autoría de un documento, commit o PR no confiere autoridad decisoria. Este registro no asigna personas y el estado propuesto de la matriz no se convierte en autoridad operacional por esta regla.
