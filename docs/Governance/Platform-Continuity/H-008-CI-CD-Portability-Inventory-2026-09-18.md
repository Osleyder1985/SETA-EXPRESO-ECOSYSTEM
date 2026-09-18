# H-008 — Inventario de portabilidad de CI/CD — primera ejecución

## Estado

**Issue:** #192  
**Unidad:** 2 — Inventario de portabilidad  
**Fecha:** 2026-09-18  
**Autoridad actual:** GitHub  
**Objetivo económico:** costo monetario $0 siempre que técnicamente sea posible.

## Alcance

Inventario de los workflows identificados en `.github/workflows/` y de sus dependencias operativas principales. Este inventario es una primera ejecución; no declara equivalencia con Forgejo/Gitea.

## Matriz

| Workflow | Trigger | Dependencias externas | Secrets/token | Acciones | Ejecución local | Runner propio | Forgejo/Gitea | Riesgo |
|---|---|---|---|---|---|---|---|---|
| governance-validation.yml | PR, push main, dispatch, repository_dispatch | GitHub API, gh, jq, GitHub PR metadata | `github.token` | checkout, upload-artifact | PARCIAL | VIABLE | PARCIAL | ALTO |
| quality-validation.yml | PR, push main, dispatch, repository_dispatch | Ruby/YAML, Python, filesystem | Ningún secreto explícito | checkout | **VIABLE** | VIABLE | **ALTO/VIABLE** | MEDIO |
| security-validation.yml | PR, push main, dispatch, repository_dispatch | GitHub API, gh, jq, git | `github.token` | checkout, upload-artifact | PARCIAL | VIABLE | PARCIAL | ALTO |
| evidence-validation.yml | PR, push main, dispatch, repository_dispatch | GitHub API, gh, jq, Ruby/YAML, PR metadata | `github.token` | checkout, upload-artifact | PARCIAL | VIABLE | PARCIAL | ALTO |
| engineering-metrics.yml | PR, dispatch, schedule | GitHub API, gh, JSON schema de salida | `github.token` | checkout, upload-artifact | PARCIAL | VIABLE | PARCIAL | ALTO |

## Hallazgos

### 1. Quality Validation es el candidato principal para ejecución local

QV-001..QV-006 son controles deterministas sobre:

- Markdown;
- whitespace;
- sintaxis YAML;
- enlaces locales;
- artefactos críticos.

No requieren GitHub API ni secretos. Por ello se ha creado el validador local en:

`scripts/validation/local-quality-validation.py`

Este validador no sustituye el workflow oficial.

### 2. Governance, Security y Evidence tienen acoplamiento con GitHub

Estos workflows consultan la API de GitHub mediante `gh api`/REST y usan metadatos específicos de Pull Requests, Issues, `github.token` y/o artefactos de Actions.

Por tanto, una ejecución local equivalente requiere desacoplar primero la obtención de contexto.

### 3. Engineering Metrics tiene acoplamiento fuerte con GitHub

Consulta PRs, Issues y workflow runs mediante `gh`. La lógica de métricas puede conservarse, pero la fuente de datos debe abstraerse antes de trasladarla a otra forja.

### 4. Acciones reutilizadas

Los workflows utilizan principalmente:

- `actions/checkout@v4`
- `actions/upload-artifact@v4`

La documentación de Forgejo indica que su sintaxis es parcialmente compatible con GitHub Actions y que las variables `GITHUB_*` tienen aliases de compatibilidad; no obstante, Forgejo advierte que GitHub Actions y Forgejo Actions no son idénticos. citeturn0search1

Gitea documenta una compatibilidad orientada a GitHub Actions y permite utilizar acciones mediante URLs absolutas, pero también documenta diferencias de permisos y eventos. citeturn0search0turn0search3turn0search8

## Clasificación de portabilidad

### VERIFICADO

- GitHub continúa siendo la autoridad.
- Los cinco workflows identificados dependen de `.github/workflows/`.
- Quality Validation contiene una lógica determinista que puede reproducirse localmente.
- Existe un primer validador local en la rama de #192.
- No se requiere una plataforma alternativa para ejecutar la primera validación local de calidad.

### PENDIENTE

- Ejecutar y registrar la validación local sobre un checkout real del repositorio.
- Separar adquisición de contexto GitHub de la lógica de Governance/Evidence/Security.
- Diseñar un contrato común de evidencia independiente del proveedor.
- Evaluar equivalencia de triggers, permisos, artefactos y tokens en Forgejo y Gitea.
- Definir runner propio.
- Diseñar mirror Git.
- Ejecutar prueba controlada fuera de GitHub.

### NO VERIFICADO

- Equivalencia funcional completa con Forgejo.
- Equivalencia funcional completa con Gitea.
- Ejecución de estos cinco workflows en un runner alternativo.
- Recuperación completa del repositorio desde un mirror alternativo.
- Costo operativo total $0 de cualquier infraestructura futura.

## Decisión provisional

No se realiza migración.

La estrategia continuará por desacoplamiento progresivo:

1. validación local;
2. extracción de lógica independiente del proveedor;
3. mirror Git;
4. runner propio;
5. prueba Forgejo;
6. prueba Gitea si aporta valor;
7. evaluación de coexistencia;
8. solo después, decisión sobre autoridad/plataforma.

## Evidencia

Fuentes técnicas consultadas el 2026-09-18:

- Forgejo Actions Reference: compatibilidad parcial con GitHub Actions. citeturn0search1
- Forgejo Actions Quick Start: requiere Actions habilitadas y runner disponible. citeturn0search12
- Gitea Actions Overview: solución CI/CD integrada y runner independiente. citeturn0search5
- Gitea Actions Comparison: diferencias respecto a GitHub Actions. citeturn0search3
- Gitea token permissions: subconjunto de permisos de GitHub Actions. citeturn0search8

## Límite

Este documento es un inventario de portabilidad, no una certificación de migrabilidad. Ninguna capacidad marcada PENDIENTE o NO VERIFICADO debe tratarse como equivalente.
