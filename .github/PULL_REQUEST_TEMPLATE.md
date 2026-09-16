# Pull Request

## Objetivo

<!-- Explicar qué objetivo persigue este cambio y por qué es necesario. -->


## Cambios

<!-- Enumerar los cambios realizados. -->


## Análisis de impacto

<!-- Describir impacto técnico, documental, arquitectónico o de proceso. -->


## Evidencia esperada

<!-- Declarar las evidencias y validaciones esperadas. Los resultados reales son producidos por CI. -->

- La metadata estructurada de gobernanza es válida.
- Las validaciones declaradas como `required` serán ejecutadas por CI.


## Relación

Closes #<Issue>

- Issue:
- PR relacionado:
- Artefactos afectados:


## Governance Metadata

```yaml
governance:
  schema_version: "1"
  validation:
    evidence: required
    governance: required
    quality: required
    security: required
```

<!--
  Contrato de metadata estructurada.
  Los valores `required` declaran controles esperados; no sustituyen el resultado real de CI.
  Los estados `passed`/`failed` son resultados de validación y no deben declararse manualmente.
-->

## Estado de integración

🟡 **NO FUSIONAR — TRABAJO PENDIENTE.**
