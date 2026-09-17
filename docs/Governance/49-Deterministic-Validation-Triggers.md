# Deterministic Validation Triggers

## Propósito
Definir cuándo deben ejecutarse automáticamente las validaciones de Gobernanza, Calidad, Seguridad y Evidencia.

## Contrato

| Evento | Validaciones | Motivo |
|---|---|---|
| PR `opened` | Todas | Nueva unidad de cambio |
| PR `synchronize` | Todas | Cambio de código/commits |
| PR `reopened` | Todas | Reapertura de una unidad de cambio |
| PR `edited` | Todas | Cambios de metadata o estado declarativo |
| PR `labeled` / `unlabeled` | Todas | El estado de clasificación cambia |
| `push` a `main` | Todas | Integridad del estado estable |
| `workflow_dispatch` | Todas las validaciones ejecutables | Reejecución manual explícita |
| `repository_dispatch` | Todas las validaciones ejecutables | Solicitud explícita desde automatización |

## Restricción de recursión
Las automatizaciones que escriben mediante `GITHUB_TOKEN` no deben depender de que esas escrituras generen otra cadena automática de workflows. Cuando una automatización necesite solicitar una validación adicional, debe utilizar un mecanismo explícito de dispatch.

## Seguridad
No se utilizará `pull_request_target` para ejecutar código procedente de ramas de trabajo. Las validaciones continúan ejecutándose sobre el contenido de la rama de la PR cuando el evento dispone de contexto de pull request.

## Trazabilidad
Toda ejecución relevante debe conservar su workflow, evento, commit evaluado, resultado y contexto suficiente para reproducir la decisión.

## Estado
🟡 **TRABAJO EN CURSO — ISSUE #156.**

## Validación dirigida por PR

Los eventos `workflow_dispatch` y `repository_dispatch` permiten validar una PR concreta sin depender de eventos secundarios. Para una PR objetivo se proporciona su número mediante `workflow_dispatch.pr_number` o `repository_dispatch.client_payload.pr_number`; el workflow resuelve la referencia y SHA actuales de la PR antes de ejecutar los controles específicos.

Cuando no se proporciona una PR objetivo, los controles que requieren contexto de PR se consideran **NOT_APPLICABLE**; no se presentan como una validación integral de una PR.

La evidencia debe conservar al menos: workflow, evento, PR objetivo cuando exista, SHA evaluado y resultado global. El mecanismo evita crear dependencias en eventos recursivos generados por `GITHUB_TOKEN`.
