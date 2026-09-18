# H-010 — Diseño de runner propio y continuidad CI/CD $0

## Estado

**Issue:** #192  
**Unidad:** 4 — Runner propio  
**Fecha:** 2026-09-18  
**Autoridad actual:** GitHub  
**Objetivo económico:** reducir dependencia de minutos alojados sin introducir infraestructura de pago.

## Objetivo

Definir la arquitectura de un runner administrado por el proyecto para ejecutar validaciones sin consumir minutos alojados de GitHub Actions cuando la plataforma y la topología lo permitan.

## Decisión de diseño

El runner propio se tratará como **capacidad de ejecución**, no como autoridad del repositorio.

La secuencia será:

1. GitHub continúa como autoridad.
2. Las validaciones deterministas se ejecutan localmente primero.
3. El runner propio se prueba en aislamiento.
4. Solo después se estudia su integración con una forja alternativa.
5. Ningún cambio de autoridad se deriva de esta unidad.

## Hallazgos técnicos

Forgejo Actions requiere que exista un runner disponible para ejecutar workflows. citeturn0search3

Gitea utiliza `act_runner` como programa independiente para ejecutar Gitea Actions. Su documentación contempla ejecución directamente en host, mediante Docker y mediante Docker-in-Docker; Docker es el modo recomendado en la documentación actual. citeturn0search0turn0search5

Por tanto, un runner propio es técnicamente viable, pero **no es por sí mismo una solución $0 completa**: todavía se necesita una máquina encendida, almacenamiento, red y mantenimiento. El costo monetario puede ser $0 si se utiliza hardware ya disponible y software libre, pero esto debe verificarse en la prueba real.

## Arquitectura propuesta

### Capa A — Validación local

Primera línea:

- scripts reproducibles;
- sin GitHub Actions;
- sin proveedor CI;
- sin secretos;
- ejecución sobre checkout local.

### Capa B — Runner propio

Segunda línea:

- máquina/hardware existente;
- usuario sin privilegios innecesarios;
- ejecución aislada;
- almacenamiento local;
- logs conservados como evidencia;
- sin secretos persistentes innecesarios.

### Capa C — Forja

Tercera línea:

- GitHub actualmente;
- Forgejo/Gitea únicamente durante pruebas controladas;
- autoridad independiente del runner.

## Seguridad

La ejecución de workflows equivale a ejecutar código del repositorio con los privilegios del runner. Por ello:

- no se utilizará un runner compartido con proyectos no confiables;
- no se concederán privilegios administrativos al runner;
- no se almacenarán PAT ni claves privadas en el repositorio;
- el runner deberá estar aislado de información ajena al proyecto;
- Docker socket solo se utilizará después de una revisión específica de riesgo.

La documentación de Gitea advierte explícitamente sobre los riesgos de confianza asociados a runners y sobre la exposición potencial al montar el socket de Docker. citeturn0search8turn0search0

## Estrategia $0

### Ruta primaria

Usar un equipo ya disponible:

`hardware existente + Linux + Git + runner open source`

sin contratar infraestructura adicional.

### Ruta de contingencia

Si no existe hardware disponible:

- no contratar inmediatamente;
- mantener validación local;
- conservar Git mirror;
- evaluar posteriormente alternativas gratuitas concretas;
- registrar cualquier límite antes de depender de ellas.

## Compatibilidad

No se declara que los workflows actuales de GitHub sean directamente ejecutables en Forgejo/Gitea.

El inventario H-008 identificó acoplamientos con GitHub API, `gh`, metadatos de PR/Issue y permisos específicos. Por ello, el runner propio debe probarse primero con una carga mínima y determinista, especialmente Quality Validation.

## Unidad de prueba propuesta

Primera prueba:

**Quality Validation local → runner propio → resultado reproducible**

Criterios:

- mismo checkout/commit;
- mismo conjunto de controles QV-001..QV-006;
- resultado PASS/FAIL equivalente;
- logs conservados;
- cero consumo de GitHub Actions durante la prueba.

Después:

**runner → workflow compatible → Forgejo/Gitea**, únicamente en una unidad posterior.

## Criterios de aceptación

- [x] Arquitectura del runner definida.
- [x] Separación runner/autoridad definida.
- [x] Ruta $0 documentada.
- [x] Riesgos de seguridad documentados.
- [x] Compatibilidad no sobredeclarada.
- [ ] Hardware real seleccionado.
- [ ] Runner instalado.
- [ ] Runner registrado.
- [ ] Prueba QV reproducible.
- [ ] Evidencia de costo operativo $0 verificada.
- [ ] Prueba en Forgejo/Gitea.

## Estado

**VERIFICADO:** diseño y límites técnicos.  
**PENDIENTE:** instalación y prueba sobre hardware real.  
**NO VERIFICADO:** costo operativo real $0, rendimiento, aislamiento y equivalencia CI/CD.

## Límite

Esta unidad no instala un runner, no registra credenciales y no cambia la plataforma de autoridad. La instalación real requiere identificar primero el hardware donde se ejecutará.
