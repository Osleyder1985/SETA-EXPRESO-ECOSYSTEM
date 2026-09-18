# MC-001 — Control detectivo de integridad de main

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Issue:** #152  
**Naturaleza:** D-Detectivo / compensatorio  
**Workflow:** `.github/workflows/main-integrity-monitor.yml`  
**Integración:** PR #167  
**Estado:** Implementado en `main`; verificación operacional no destructiva completada.

## 1. Propósito

Detectar y documentar actualizaciones de `main` que no puedan acreditarse como integración normal mediante Pull Request. El control complementa la protección nativa y no la sustituye.

## 2. Evento controlado

El monitor se activa ante:

- `push` sobre `main`;
- `workflow_dispatch` para observación/control manual reproducible.

El evento `push` es la evidencia primaria del cambio que alcanzó `main`.

## 3. Datos mínimos registrados

Para cada ejecución se registra:

| Dato | Fuente |
|---|---|
| Evento | `github.event_name` |
| Actor | `github.actor` |
| Fecha/hora | timestamp del commit (`github.event.head_commit.timestamp`) + timestamp UTC de observación |
| SHA actual | `github.sha` |
| SHA anterior | `github.event.before`, cuando existe |
| Mensaje | `github.event.head_commit.message` |
| Estado del push | `forced`, `created`, `deleted` |
| Archivos afectados | `git diff --name-status --find-renames`, conservado en JSON y `changed-files.txt` |
| PR asociado | GitHub API `commits/{sha}/pulls` |
| Clasificación | integración esperada, anomalía u observación manual |

## 4. Clasificación

Una actualización `push` se considera `EXPECTED_PR_INTEGRATION` cuando el SHA está asociado a un Pull Request fusionado hacia `main` y el cambio no presenta un estado de push sospechoso.

Si no existe una asociación acreditable con un Pull Request fusionado hacia `main`, el evento se clasifica como `ANOMALY` y se requiere un Issue de incidente.

Los estados de push forzado, creación o eliminación de referencia se conservan como señales de `SUSPICIOUS_PUSH_STATE` y no se ocultan mediante una clasificación normal.

## 5. Incidente

Para una anomalía, el workflow crea o actualiza un Issue con título controlado:

`Gobernanza/main: Registrar incidente de integridad de main.`

El Issue incluye SHA, actor, impacto, evidencia esperada y metadata de clasificación conforme al catálogo de labels.

La actualización de un incidente existente se realiza mediante comentario para conservar la historia de detecciones.

## 6. Evidencia reproducible

Cada ejecución genera un artifact con retención de 90 días que contiene:

- `main-integrity-event.json`: registro estructurado del evento;
- `changed-files.txt`: relación reproducible de archivos afectados.

La evidencia debe correlacionarse con el workflow run, su SHA, el actor y el Issue de incidente cuando exista. El JSON incorpora la procedencia de la ejecución, la clasificación, el estado del push y la referencia al Issue generado/actualizado.

## 7. Permisos

El workflow declara explícitamente:

```yaml
permissions:
  contents: read
  issues: write
  pull-requests: read
```

No se concede permiso de escritura sobre contenidos del repositorio ni sobre Pull Requests. `issues: write` es necesario exclusivamente para crear o actualizar el registro de incidente.

## 8. No auto-revert

MC-001 no modifica `main`, no realiza rollback y no intenta corregir automáticamente el cambio detectado. Su responsabilidad es observación, clasificación, evidencia y registro del incidente.

## 9. Limitaciones

- Un control detectivo no impide que un actor con permisos de escritura actualice `main`.
- La asociación PR depende de la información que GitHub expone para el commit consultado.
- La clasificación automática no sustituye la investigación del incidente.
- La protección nativa de ramas/rulesets sigue siendo una capacidad separada y un riesgo residual mientras no esté efectivamente habilitada y verificada.

## 10. Implementación y verificación operacional

MC-001 fue implementado mediante el Issue #152 y el PR #167, integrado de forma controlada en `main`. El Issue #152 quedó cerrado como completado tras el merge.

La implementación quedó incorporada en `.github/workflows/main-integrity-monitor.yml` y conserva el flujo detectivo/compensatorio definido en este documento.

La verificación operacional no destructiva se realizó mediante `workflow_dispatch` sobre `main`. La ejecución `Main Integrity Monitor #2` finalizó en estado verde (`SUCCESS`), acreditando la capacidad del workflow para ejecutarse manualmente desde `main` y recorrer la ruta operacional de observación y generación de evidencia sin modificar el repositorio ni provocar deliberadamente una anomalía.

Esta verificación no constituye una prueba de push directo no autorizado. Dicha prueba destructiva no se ejecuta porque contradiría el proceso de control establecido. La detección de anomalías queda implementada para eventos `push` y debe evaluarse mediante evidencia real cuando exista una actualización que requiera investigación.

### Evidencia de implementación y cierre

1. workflow válido y activado sobre `main`;
2. registro implementado de SHA, actor, fecha/hora y archivos;
3. asociación de PR cuando GitHub la expone;
4. clasificación de integraciones normales mediante PR;
5. generación de Issue ante una anomalía clasificable, sin auto-revert;
6. artifact de evidencia reproducible;
7. permisos mínimos declarados y justificados;
8. validaciones CI de Governance, Quality, Security y Evidence;
9. review/decisión de integración y merge controlados del PR #167;
10. verificación operacional manual no destructiva mediante `Main Integrity Monitor #2`.

Con estas evidencias, el criterio documental de cierre de Issue #152 queda satisfecho. Se mantienen las limitaciones descritas en la sección 9 y el carácter detectivo/compensatorio del control.
