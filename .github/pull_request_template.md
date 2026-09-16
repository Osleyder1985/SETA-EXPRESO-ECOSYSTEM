# Pull Request Template

## Issue

Closes #

## Objetivo

<!-- Qué problema resuelve este PR y cuál es el resultado esperado. -->

## Cambios

<!-- Lista concreta de cambios realizados. -->

## Análisis de impacto

### Impacto técnico

### Impacto de proceso

### Impacto de seguridad

### Impacto de SoD

## Evidencia esperada

<!-- Indicar qué evidencia debe demostrar que el cambio cumple su objetivo. -->

- Governance Validation
- Quality Validation
- Security Validation
- Evidence Validation
- Evidencia específica del cambio:

## Relación

<!-- Mantener trazabilidad explícita. -->

- Issue → Branch → Commits → PR
- PR → Validaciones → Review → Merge
- Artefactos relacionados:
- Riesgos / decisiones / no conformidades / lecciones relacionadas:

## Estado de integración

🟡 **NO FUSIONAR — PENDIENTE DE VALIDACIONES Y REVISIÓN.**

## Checklist de preparación del PR

- [ ] Existe Issue de origen y está enlazado con `Closes #N`, `Fixes #N` o `Resolves #N`.
- [ ] La branch no es `main` y corresponde a la Issue.
- [ ] El PR contiene todas las secciones obligatorias.
- [ ] `## Evidencia esperada` declara los cuatro workflows aplicables.
- [ ] `## Relación` documenta la trazabilidad completa.
- [ ] Se revisaron los requisitos de los workflows que validan el PR.
- [ ] Se revisaron las lecciones de ingeniería aplicables antes de marcarlo listo.
- [ ] Todo Markdown nuevo comienza con un encabezado H1 válido.
- [ ] No se presenta como evidencia una aprobación o revisión que no exista.
- [ ] No se mergea hasta que las validaciones y revisión requeridas estén satisfechas.
