# Estrategia de portabilidad y continuidad tecnológica a costo $0

## Estado

**Issue:** #192  
**Estado:** implementación inicial controlada  
**Autoridad actual:** GitHub continúa siendo la plataforma principal.  
**Objetivo económico:** costo monetario $0 siempre que técnicamente sea posible.

## Propósito

El proyecto debe conservar capacidad de ingeniería sin quedar bloqueado por una cuota mensual de CI ni por infraestructura propia.

La estrategia desacopla progresivamente:

- repositorio Git;
- gestión de Issues y Pull Requests;
- validación;
- ejecución CI/CD;
- almacenamiento de evidencia;
- plataforma de colaboración.

La migración de plataforma **no está autorizada por este artefacto**. Cualquier cambio de autoridad deberá tramitarse mediante un Issue específico.

## Principios

1. **Git como núcleo portable.** El historial y las ramas deben permanecer recuperables fuera del proveedor.
2. **Validación local primero.** Los defectos deterministas deben detectarse sin consumir GitHub Actions.
3. **Sin infraestructura propia para CI.** No se dedicará ni administrará una PC, servidor o runner propio para el proyecto.
4. **Costo controlado.** No se activarán servicios potencialmente facturables sin autorización explícita.
5. **Gobernanza preservada.** Issue → Branch → Commit → Validation → Review → PR → Merge continúa siendo obligatorio.
6. **No migración prematura.** GitHub sigue siendo la autoridad mientras se verifica la portabilidad.
7. **Evidencia reproducible.** Cada capacidad se clasifica como VERIFICADA, PENDIENTE o NO VERIFICADA.
8. **Continuidad sin cuota obligatoria.** Las validaciones esenciales deben disponer de una ruta local reproducible.

## Primera implementación

Se incorpora:

- `scripts/validation/local-quality-validation.py`;
- reproducción local de QV-001..QV-006;
- inventario explícito de los artefactos críticos;
- salida de máquina `QUALITY_VALIDATION_LOCAL=PASS|FAIL`.

El validador local **no sustituye** la Quality Validation oficial. Detecta previamente fallos deterministas y permite continuar trabajando sin depender de una ejecución remota.

### Dependencia local

Para QV-004 se recomienda Python 3 y PyYAML. Si PyYAML no está disponible, el validador falla explícitamente y no inventa un PASS.

## Arquitectura vigente

```text
                    Git / historial portable
                             |
               +-------------+-------------+
               |                           |
        GitHub principal            Plataforma alternativa
               |                    evaluada posteriormente
               |                           |
       CI/CD sujeto a cuota          CI/CD del proveedor
               |
      Validación local primero
               |
           Evidencia
```

No se incorpora self-hosted runner a esta arquitectura.

## Plataforma alternativa

Forgejo y Gitea permanecen como candidatos de evaluación técnica. La evaluación futura debe verificar sus condiciones reales de uso gratuito, mantenimiento requerido y compatibilidad con las necesidades del proyecto.

No se declara equivalencia con GitHub Actions ni se asume que una alternativa gratuita sea sostenible hasta contar con evidencia.

## Continuidad operativa a $0

La ruta prioritaria es:

1. checkout Git local;
2. validación local reproducible;
3. desarrollo y revisión mediante el flujo gobernado;
4. mirror Git para recuperación;
5. uso prudente de CI alojado cuando sea necesario y esté disponible sin coste;
6. evaluación posterior de una plataforma alternativa que no requiera hardware administrado por el proyecto.

## Variantes descartadas

La opción **self-hosted runner sobre hardware propio o dedicado** fue evaluada bajo H-010, H-011 y H-012 y queda descartada.

No se comprarán ni dedicarán equipos para ejecutar CI como parte de esta estrategia.

## Criterios de éxito

La estrategia se considerará operacionalmente demostrada cuando exista evidencia de que:

- el repositorio Git puede recuperarse fuera de GitHub;
- las validaciones deterministas principales pueden ejecutarse localmente;
- el flujo esencial puede continuar sin depender exclusivamente de una cuota mensual de Actions;
- la trazabilidad de cambios permanece intacta;
- existe una plataforma alternativa evaluada bajo condiciones reales de costo $0, si resulta necesaria;
- no se requiere facturación para continuar el flujo esencial del proyecto.

## Límites

Este documento no afirma:

- que Forgejo o Gitea sean ya equivalentes a GitHub;
- que exista actualmente un mirror operativo si aún no se ha probado;
- que todas las validaciones sean portables;
- que una plataforma alternativa futura sea necesariamente $0;
- que GitHub Actions esté disponible ilimitadamente sin coste.

Las afirmaciones de capacidad y costo requieren evidencia específica.
