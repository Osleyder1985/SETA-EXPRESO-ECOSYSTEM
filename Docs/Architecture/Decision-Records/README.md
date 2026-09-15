# Decision Records

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Estado:** Estructura controlada propuesta  
**Fecha:** 2026-09-15  
**Gobernanza:** `Docs/Governance/19-Decision-Governance.md`

---

## 1. Propósito

Este directorio contiene los Architecture Decision Records (ADR) y Engineering Decision Records (EDR) que forman parte de la evidencia histórica de decisiones del Ecosistema.

Los Decision Records son artefactos controlados. No constituyen un sustituto de requisitos, arquitectura, diseño, riesgos, pruebas ni aprobaciones; registran el razonamiento que conecta esos artefactos cuando existe una decisión relevante.

## 2. Fuente de reglas

Las reglas de creación, evaluación, aprobación, revisión y supersession están definidas en:

`Docs/Governance/19-Decision-Governance.md`

## 3. Convención

- ADR: `ADR-NNN` para decisiones de arquitectura.
- EDR: `EDR-NNN` para decisiones de ingeniería relevantes no arquitectónicas.
- Los identificadores son estables y no se reutilizan.
- Las decisiones superseded se conservan.
- Las nuevas decisiones deben enlazar las decisiones que reemplazan cuando corresponda.

## 4. Regla de almacenamiento

Los records se almacenarán en este directorio como Markdown para favorecer revisión humana, versionado y trazabilidad mediante Git.

El índice `Decision-Record-Index.md` constituye el punto de navegación de las decisiones registradas.

Las plantillas no son decisiones y nunca deben aparecer como decisiones aceptadas.

## 5. Regla de evidencia

Un Decision Record aceptado debe poder relacionarse, cuando corresponda, con requisitos, arquitectura, riesgos, Issues, Pull Requests, pruebas, análisis comparativos, evidencia externa y Quality Gates.

## 6. Regla de historia

No se eliminará una decisión para ocultar su historia. Si deja de ser válida, se actualizará su estado y se registrará la relación `Supersedes` / `Superseded by` con la decisión posterior.

## 7. Estado inicial

No existen todavía ADRs/EDRs aceptados en esta baseline. Esto es deliberado: las decisiones técnicas concretas deben esperar al contexto y evidencia obtenidos durante las fases correspondientes del ciclo de vida.
