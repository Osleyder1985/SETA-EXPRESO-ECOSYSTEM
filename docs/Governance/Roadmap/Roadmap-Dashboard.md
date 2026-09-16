# 🗺️ SETA EXPRESO ECOSYSTEM — Roadmap Dashboard

> **Estado:** 🟢 PR #28 — integrado en `main`
>
> **Versión de la vista:** 0.2.1
>
> El Dashboard HTML es una vista visual derivada del Roadmap Maestro.

## 🧭 Fuente canónica

`Docs/Governance/08-Software-Roadmap.md`

Los estados, fechas, Gates, dependencias y resultados deben mantenerse primero en el Roadmap canónico. El Dashboard no constituye una fuente de verdad independiente.

## 🎛️ Interacción

- Filtros: Todos, Completados y Pendientes.
- Detalles desplegables por fase.
- Recorrido visual A–O.
- Vista de progreso y trazabilidad.
- Diseño responsive.
- Sin dependencias externas obligatorias.

La fase B es actualmente la **próxima fase planificada**, no una fase marcada como `En curso` en el Roadmap canónico.

## 🔗 Trazabilidad

`Roadmap → Issue → Branch → Change → Governance → Quality → Security → Evidence → PR → main → Evidence`

## 📜 Integración de PR #28

PR #28 fue integrado en `main` mediante el merge commit `fd0e4d09a558f226c6b7f1df76057df0ed9631a2`.

La documentación del PR conserva su estado histórico previo a la integración. Este documento registra el estado efectivo posterior al merge sin reescribir la evidencia histórica del PR.

## 📌 Regla de actualización

Cualquier modificación de estados, fechas, Gates, Issues, PRs o evidencias debe realizarse mediante `Issue → Branch → PR → Validaciones → Revisión → Merge`. No se permite corregir únicamente la representación visual para alterar el estado del proyecto.

## ⚙️ Consistencia

El Dashboard debe permanecer reconciliado con `Docs/Governance/08-Software-Roadmap.md`. Una divergencia entre la fuente canónica y esta representación derivada constituye un defecto de consistencia y debe corregirse mediante el flujo controlado.

## 🧾 Cierre post-merge

La reconciliación de la vista derivada se ejecuta mediante el Issue #29 y su PR asociado. La evidencia de validación queda vinculada al commit evaluado y a los cuatro controles transversales aplicables.
