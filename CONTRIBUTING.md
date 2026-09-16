# Contributing Guide

## Propósito

Este documento define el flujo obligatorio de contribución al repositorio `SETA-EXPRESO-ECOSYSTEM`.

Su objetivo es garantizar que cada cambio sea trazable, revisable, verificable y alineado con la gobernanza del Ecosistema.

---

# Flujo obligatorio de trabajo

Todo cambio debe seguir esta cadena:

```text
Issue
 ↓
Branch
 ↓
Commit
 ↓
Pull Request
 ↓
Validaciones
 ↓
Review
 ↓
Merge
 ↓
main
```

Ningún cambio debe saltarse etapas.

---

# 1. Creación de un Issue

Antes de implementar cualquier cambio significativo se debe crear un Issue.

El Issue debe describir:

- Objetivo del cambio.
- Problema, necesidad u oportunidad.
- Alcance.
- Artefactos afectados.
- Criterios de aceptación.
- Evidencia esperada.
- Riesgos o impacto conocido.

Un Issue debe permitir entender qué se cambia, por qué se cambia y cómo se comprobará el resultado.

---

# 2. Creación de Branch

Toda implementación debe realizarse en una branch asociada a un Issue.

Formato recomendado:

```text
issue-<numero>-<descripcion-corta>
```

Ejemplos:

```text
issue-102-contributing-manual
issue-25-api-security-review
issue-40-documentation-update
```

No se permite trabajar directamente sobre `main`.

---

# 3. Commits

Los commits deben ser:

- Pequeños y coherentes.
- Relacionados con el Issue correspondiente.
- Descriptivos.
- Fáciles de revisar.

Ejemplo:

```text
docs(governance): add contributing workflow manual
```

El commit debe explicar la intención del cambio, no solamente la acción realizada.

---

# 4. Pull Request

Todo cambio hacia `main` requiere un Pull Request.

El Pull Request debe incluir obligatoriamente:

```md
## Objetivo

## Cambios

## Análisis de impacto

## Evidencia esperada

## Relación
```

Debe existir relación explícita con el Issue que originó el cambio.

---

# 5. Validaciones obligatorias

Antes de fusionar un Pull Request deben completarse las validaciones definidas por el repositorio.

Incluyen, según corresponda:

- Evidence Validation.
- Governance Validation.
- Quality Validation.
- Security Validation.

Un cambio no puede fusionarse si las validaciones requeridas fallan.

---

# 6. Revisión y Merge

El flujo final es:

```text
Pull Request
 ↓
Validaciones exitosas
 ↓
Review
 ↓
Aprobación
 ↓
Merge
 ↓
main
```

`main` representa la línea base integrada y controlada.

---

# Reglas no permitidas

No se acepta:

- Commits directos a `main`.
- Pull Requests sin Issue asociado.
- Pull Requests sin análisis de impacto.
- Cambios sin evidencia.
- Documentación desactualizada respecto al cambio implementado.
- Saltarse validaciones obligatorias.
- Fusionar cambios con trabajo pendiente no declarado.

---

# Principio general

En este repositorio el cambio no se considera terminado solamente porque funciona.

Un cambio está terminado cuando existe:

```text
Necesidad
 ↓
Decisión
 ↓
Implementación
 ↓
Evidencia
 ↓
Validación
 ↓
Integración controlada
```

La trazabilidad forma parte del producto.
