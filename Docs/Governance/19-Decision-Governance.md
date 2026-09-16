# Gobernanza de decisiones de arquitectura e ingeniería

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.2.0  
**Estado:** Baseline propuesta para revisión  
**Issue:** #33

---

## Integración con Decision Authority

Toda decisión material debe identificar explícitamente su autoridad. La política de Decision Governance conserva el razonamiento de la decisión; la capacidad Decision Authority determina qué rol es accountable, quién aprueba, quién puede bloquear, quién debe ser consultado y cómo se escala el conflicto.

Fuentes de autoridad:

- `Docs/Governance/48-Decision-Authority-Governance.md`
- `Docs/Governance/Decision/Role-Register.yml`
- `Docs/Governance/Decision/Decision-Authority-Matrix.yml`
- `Docs/Governance/Decision/Decision-Authority-Register.md`
- `Docs/Governance/Decision/Decision-Authority-Escalation.md`

Regla: el autor de un commit, Issue o PR no adquiere por ese hecho autoridad empresarial sobre la decisión.

## Campos adicionales obligatorios cuando aplique

Los Decision Records deberán identificar:

- `accountable_role`;
- `approval_authority`;
- `blocking_authority` cuando exista;
- `consulted_roles`;
- `escalation_path`;
- `authority_evidence`.

## Acumulación de roles

Una misma persona puede desempeñar múltiples roles inicialmente. La acumulación debe permanecer visible y considerarse en el análisis de riesgos e independencia. La autoridad sigue perteneciendo conceptualmente al rol, no al commit ni a una identidad técnica.

## Preservación del contenido anterior

El resto de esta política mantiene los requisitos existentes para Context, Decision, Alternatives, Criteria, Trade-offs, Consequences, Risks, Evidence, Supersession, estados, trazabilidad, lifecycle y automatización futura. Esta actualización añade la dimensión de autoridad sin convertir decisiones hipotéticas en decisiones aprobadas.
