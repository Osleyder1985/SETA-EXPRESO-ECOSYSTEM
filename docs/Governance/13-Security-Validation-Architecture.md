# Arquitectura de Security Validation

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.2.0  
**Estado:** Baseline operacional de aplicabilidad y evidencia  
**Fecha:** 2026-09-18  
**Issue de implementación:** #180  
**Issue de origen:** #171 / H-004

Security Validation es una capa transversal para detectar condiciones objetivas de riesgo antes de integrar cambios en `main`. No sustituye threat modeling, arquitectura de seguridad, análisis de riesgos, pruebas de penetración, revisión humana ni gestión de vulnerabilidades.

## Cadena de control

```text
Issue → Branch → Pull Request → Governance → Quality → Security → Evidence → Review → Merge → main
```

## Inventario técnico verificado para H-004

La revisión del árbol de `main` en el commit de referencia de #179 identificó:

- workflows de GitHub Actions;
- archivos de configuración y catálogos YAML;
- documentación Markdown;
- plantillas de gobernanza e investigación.

No se identificaron manifiestos/lockfiles de paquetes de aplicación, código fuente de aplicación en lenguajes soportados por SAST, Dockerfiles/imágenes, Terraform/IaC del producto ni artefactos de componentes de software que justifiquen SCA, container scanning o SBOM de producto en esta fase.

Las referencias `uses:` de GitHub Actions son dependencias de automatización y se mantienen como riesgo de supply chain separado; su presencia por sí sola no convierte SV-005 en SCA de aplicación.

## Matriz de controles

| ID | Control | Aplicabilidad actual | Mecanismo | Estado verificable | Evidencia | Condición de reevaluación |
|---|---|---|---|---|---|---|
| SV-001 | Secret Material Scan | Aplicable | Patrones deterministas sobre contenido versionado | PASS | Run de `Security Validation` | Revisar al introducir secretos/formatos nuevos |
| SV-001A | Secret scanning especializado | Capacidad no verificable desde esta integración | Plataforma GitHub / scanner especializado | NOT_VERIFIED | Limitación de acceso a capacidades administrativas | Revaluar cuando exista acceso verificable a Security/Secret Scanning |
| SV-002 | Workflow Least Privilege | Aplicable | Validación de `permissions` en todos los workflows | PASS | Run de `Security Validation` | Reevaluar ante nuevos workflows |
| SV-003 | Dangerous Workflow Trigger | Aplicable | Detección de `pull_request_target` | PASS | Run de `Security Validation` | Reevaluar ante cambios de triggers |
| SV-004 | Security Workflow Integrity | Aplicable | Presencia, integridad y autoconsistencia básica | PASS | Run de `Security Validation` | Reevaluar ante cambios del control |
| SV-005 | Dependency Security | No aplicable al producto actual | Sin manifiestos/lockfiles de aplicación; no se declara SCA | NOT_APPLICABLE | Inventario reproducible | Al introducir manifest/lockfile o dependencia de producto |
| SV-006 | SAST de producto | No aplicable al producto actual | No existe código de aplicación analizable | NOT_APPLICABLE | Inventario reproducible | Al introducir código de aplicación soportado |
| SV-006A | SAST de workflows | Aplicable | GitHub CodeQL para GitHub Actions | IMPLEMENTED | Workflow `CodeQL` + run | Mantener mientras existan workflows |
| SV-007 | IaC Security | No aplicable | No existe IaC del producto | NOT_APPLICABLE | Inventario reproducible | Al introducir Terraform, cloud/IaC u otra infraestructura declarativa |
| SV-008 | Container Security | No aplicable | No existen Dockerfiles/imágenes del producto | NOT_APPLICABLE | Inventario reproducible | Al introducir Dockerfile, imagen o pipeline de contenedor |
| SV-009 | SBOM | No aplicable al producto actual | No existe composición de producto que genere un SBOM significativo | NOT_APPLICABLE | Inventario reproducible | Al introducir software/dependencias/componentes de producto |

## Supply chain de GitHub Actions

Los workflows contienen referencias externas mediante `uses:`. Estas referencias constituyen una superficie de supply chain de automatización, pero no se presentan como SCA de aplicación ni como SBOM.

La política aplicable es:

1. mantener permisos mínimos;
2. evitar `pull_request_target` salvo excepción justificada;
3. revisar cambios de acciones dentro de PR;
4. preferir referencias mantenidas y versiones controladas;
5. reevaluar Dependabot/dependency review cuando la capacidad del repositorio lo permita.

La documentación de GitHub indica que Dependency Review analiza cambios de dependencias en pull requests y que la acción puede usarse como gate cuando el repositorio dispone de las capacidades requeridas. No se afirma que esa capacidad esté habilitada aquí. 

## Política de fallo y estados

Los estados `PASS`, `NOT_APPLICABLE`, `NOT_VERIFIED` e `IMPLEMENTED` tienen semántica distinta:

- `PASS`: el mecanismo aplicable se ejecutó y satisfizo el criterio definido.
- `IMPLEMENTED`: el mecanismo está integrado; su ejecución concreta debe conservar evidencia.
- `NOT_APPLICABLE`: el inventario actual demuestra que el objeto del control no existe; debe existir condición explícita de reevaluación.
- `NOT_VERIFIED`: la capacidad puede ser pertinente, pero la integración disponible no permite verificarla; no equivale a PASS ni a NOT_APPLICABLE.

Un control no puede cambiar de estado por inferencia documental.

## Integración con Governance Core

La evidencia de esta evaluación se integra con:

- `03-Artifacts-And-Evidence.md`: evidencia reproducible de workflow y matriz de aplicabilidad;
- `14-Evidence-Validation-Architecture.md`: cadena de evidencia y trazabilidad;
- `17-Risk-Management-System.md`: riesgo residual cuando una capacidad no puede verificarse;
- `50-Non-Conformance-Management.md`: desviación solo cuando exista incumplimiento de un control aplicable, no por la mera existencia de un N/A justificado;
- `04-Quality-Gates.md`: Security Validation sigue siendo un gate de validación, no una certificación de seguridad.

## Criterio de verdad

Nunca se afirmará que el Ecosistema está «seguro» únicamente porque Security Validation haya pasado. La afirmación permitida es que los controles automatizados aplicables ejecutados en esa revisión fueron satisfechos.

La existencia de esta matriz tampoco demuestra eficacia de controles futuros. Cada control debe conservar evidencia de ejecución o una justificación verificable de no aplicabilidad.

## Evidencia mínima

`Issue → Branch → Commit → Workflow Run → Resultado → PR → Review → Merge → main`
