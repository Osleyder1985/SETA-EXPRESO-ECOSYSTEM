# MC-001 — Control detectivo de integridad de main

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Issue:** #152  
**Naturaleza:** D-Detectivo / compensatorio  
**Workflow:** `.github/workflows/main-integrity-monitor.yml`  
**Estado:** Implementado en rama de trabajo; pendiente de validación, review y merge.

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
| Fecha/hora | `github.event.head_commit.timestamp` o timestamp UTC de ejecución manual |
| SHA actual | `github.sha` |
| SHA anterior | `github.event.before`, cuando existe |
| Mensaje | `github.event.head_commit.message` |
| Estado del push | `forced`, `created`, `deleted` |
| Archivos afectados | `git diff --name-status` |
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

La evidencia debe correlacionarse con el workflow run, su SHA y el Issue de incidente cuando exista.

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

## 10. Criterio de cierre de Issue #152

El Issue #152 podrá cerrarse únicamente después de demostrar mediante un PR real:

1. workflow válido y activado sobre `main`;
2. registro de SHA, actor, fecha/hora y archivos;
3. asociación de PR cuando exista;
4. clasificación de una integración normal mediante PR;
5. generación de Issue ante una anomalía verificable, sin auto-revert;
6. artifact de evidencia reproducible;
7. permisos mínimos justificados;
8. validaciones CI de Governance, Quality, Security y Evidence;
9. review y merge controlados.
