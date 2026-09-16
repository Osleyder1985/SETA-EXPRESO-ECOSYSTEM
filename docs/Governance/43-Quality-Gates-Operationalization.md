# Quality Gates — Operacionalización

## Problema #8

Los Quality Gates existentes definen decisiones y controles, pero todavía no están suficientemente operacionalizados para permitir una evaluación consistente, reproducible y progresivamente automatizable.

## Objetivo

Convertir cada Quality Gate en una especificación operacional con:

- Entry Criteria
- Required Inputs
- Checks
- Metrics
- Evidence
- Decision Authority
- PASS
- CONDITIONAL
- BLOCKED
- REOPEN
- Exit Criteria

El diseño deberá permitir que una máquina compruebe progresivamente los criterios objetivos, sin sustituir el juicio de ingeniería donde este sea necesario.

## G4 — Requirements Baseline

Como ejemplo inicial, G4 deberá poder comprobar criterios cuantitativos y verificables como:

- 100% de los requisitos tienen ID.
- 100% de los requisitos tienen owner.
- 100% tienen acceptance criteria.
- ≥95% tienen trazabilidad.
- 0 requisitos críticos ambiguos.
- 100% de los requisitos críticos son verificables.

Los umbrales deberán considerarse criterios del gate únicamente cuando exista una justificación y una definición operacional verificable. No deberán inventarse métricas por conveniencia.

## Alcance

La operacionalización deberá cubrir G0–G13 y distinguir claramente entre:

1. criterios completamente automatizables;
2. criterios parcialmente automatizables;
3. criterios que requieren juicio o aprobación humana.

También deberá definir el modelo de evidencia, autoridad de decisión, condiciones de reapertura y trazabilidad de cada resultado.

## Relación

El trabajo se ejecutará mediante Issue → Branch → PR → Governance Validation → Quality Validation → Security Validation → Evidence Validation → Review → Merge.
