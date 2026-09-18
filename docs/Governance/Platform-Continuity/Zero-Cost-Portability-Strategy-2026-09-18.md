# Estrategia de portabilidad y continuidad tecnológica a costo $0

## Estado

**Issue:** #192  
**Estado:** implementación inicial controlada  
**Autoridad actual:** GitHub continúa siendo la plataforma principal.  
**Objetivo económico:** costo monetario $0 siempre que técnicamente sea posible.

## Propósito

El proyecto no debe depender de una única plataforma SaaS ni de una cuota de CI para conservar su capacidad de ingeniería. La estrategia desacopla progresivamente:

- repositorio Git;
- gestión de Issues y Pull Requests;
- validación;
- ejecución CI/CD;
- almacenamiento de evidencia;
- plataforma de colaboración.

La migración de plataforma **no está autorizada por este artefacto**. Este trabajo establece portabilidad y continuidad; cualquier cambio de autoridad deberá tramitarse mediante un Issue específico.

## Principios

1. **Git como núcleo portable.** El historial y las ramas deben permanecer recuperables fuera del proveedor.
2. **Validación local primero.** Los defectos deterministas deben detectarse sin consumir GitHub Actions.
3. **CI desacoplada.** Los workflows deben poder trasladarse a un runner propio o a una plataforma compatible cuando sea viable.
4. **Costo controlado.** No se ejecutan acciones potencialmente facturables sin necesidad técnica.
5. **Gobernanza preservada.** Issue → Branch → Commit → Validation → Review → PR → Merge continúa siendo obligatorio.
6. **No migración prematura.** GitHub sigue siendo la autoridad mientras se construye y verifica la portabilidad.
7. **Evidencia reproducible.** Cada capacidad se clasifica como VERIFICADA, PENDIENTE o NO VERIFICADA.

## Primera implementación

Se incorpora:

- `scripts/validation/local-quality-validation.py`
- reproducción local de QV-001..QV-006;
- inventario explícito de los artefactos críticos que ya exige Quality Validation;
- salida de máquina `QUALITY_VALIDATION_LOCAL=PASS|FAIL`.

El validador local **no sustituye** la Quality Validation oficial. Su función es detectar previamente fallos de calidad deterministas y reducir ejecuciones innecesarias de Actions.

### Dependencia local

Para QV-004 se recomienda Python 3 y PyYAML. Si PyYAML no está disponible, el validador falla explícitamente y no inventa un PASS.

## Arquitectura objetivo

```text
                         Git / historial
                              |
                +-------------+-------------+
                |                           |
          GitHub principal            Plataforma alternativa
                |                    Forgejo / Gitea
                |                           |
         GitHub Actions             Runner propio / Actions
                |                           |
                +-------------+-------------+
                              |
                     Validación reproducible
                              |
                         Evidencia
```

La coexistencia será preferible a una migración abrupta mientras no exista evidencia de equivalencia funcional.

## Plataforma alternativa de referencia

Forgejo queda como primera plataforma de evaluación técnica, con Gitea como alternativa comparable. Ambas ofrecen una arquitectura autoalojable y CI/CD basado en runners. La compatibilidad con GitHub Actions es parcial, por lo que los workflows deben someterse a una matriz de portabilidad antes de declararse equivalentes.

## Próximas unidades controladas

### Unidad 2 — Inventario de portabilidad

Inventariar cada workflow de `.github/workflows/` y clasificar:

| Campo | Estado |
|---|---|
| Workflow | pendiente de inventario |
| Trigger | pendiente |
| Dependencias externas | pendiente |
| Secrets | pendiente |
| Actions utilizadas | pendiente |
| Ejecución local | pendiente |
| Runner propio | pendiente |
| Forgejo/Gitea | pendiente |
| Riesgo de portabilidad | pendiente |

### Unidad 3 — Mirror Git

Diseñar un mirror controlado sin convertirlo automáticamente en autoridad. Debe conservar historial, ramas relevantes y capacidad de recuperación.

### Unidad 4 — Runner propio

Definir runner reproducible para CI/CD. La infraestructura debe poder ejecutarse con herramientas libres y sin minutos SaaS.

### Unidad 5 — Matriz GitHub ↔ Forgejo/Gitea

Verificar Issues, PRs, reviews, labels, Actions, secrets, artifacts, permisos, webhooks y trazabilidad.

### Unidad 6 — Prueba de recuperación

Demostrar que el proyecto puede reconstruirse y continuar desde un mirror y una copia local sin depender de una cuota mensual de Actions.

## Criterios de éxito

La estrategia se considerará operacionalmente demostrada cuando exista evidencia de que:

- el repositorio Git puede recuperarse fuera de GitHub;
- las validaciones deterministas principales pueden ejecutarse localmente;
- el CI puede ejecutarse en runner propio;
- la trazabilidad de cambios permanece intacta;
- existe una plataforma alternativa evaluada;
- no se requiere facturación para continuar el flujo esencial del proyecto.

## Límites

Este documento no afirma:

- que Forgejo o Gitea sean ya equivalentes a GitHub para este repositorio;
- que exista actualmente un mirror operativo;
- que el runner propio ya esté instalado;
- que todas las validaciones actuales sean portables;
- que el costo total de cualquier infraestructura futura sea necesariamente $0.

Esas afirmaciones requieren evidencia específica.
