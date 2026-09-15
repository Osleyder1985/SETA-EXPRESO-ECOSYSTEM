# Roadmap Maestro de Ingeniería del Ecosistema

**Versión:** 0.4.0  
**Estado:** Vigente como hoja de ruta ejecutable  
**Fuente canónica:** `Docs/Governance/00-Software-Lifecycle-Master.md`  
**Última actualización:** 2026-09-15

## Propósito

El Roadmap es el plan maestro temporal y trazable del Ecosistema. Muestra el camino completo A–O y permite saber qué se ejecutó, cuándo se ejecutó, qué está en curso, qué falta, de qué depende y cuándo se estima completar cada actividad.

Las fechas futuras son estimaciones de planificación. Las fechas reales de cumplimiento se conservan como historia.

## Leyenda

| Estado | Significado |
|---|---|
| 🟢 Completado | Ejecutado, verificado y respaldado por evidencia; tiene fecha real. |
| 🟡 En curso | Trabajo activo; tiene fecha objetivo. |
| 🔵 Recurrente | Actividad continua durante el ciclo de vida. |
| ⚪ Planificado | Aprobado y aún no iniciado; tiene fecha objetivo. |
| 🔴 Bloqueado | Impedido por una dependencia explícita. |
| ⚫ Diferido / No aplica | No requerido ahora o diferido con justificación. |

## Calendario maestro A–O

| Fase | Resultado principal | Estado | Inicio / cumplimiento real | Fecha objetivo | Dependencia | Evidencia de salida |
|---|---|---|---|---|---|---|
| A | Concepción y gobernanza | 🟡 | 2026-09-15 | 2026-09-17 | — | G0 + baseline de gobernanza |
| B | Descubrimiento del sistema y organización | ⚪ | — | 2026-09-24 | A | Current-State Model + G1 |
| C | Necesidades, problema y objetivos | ⚪ | — | 2026-10-01 | B | Problem Statement + Scope + G2 |
| D | Ingeniería de requisitos | ⚪ | — | 2026-10-15 | C | Requirements Baseline + RTM + G3 |
| E | Definición y modelado del sistema | ⚪ | — | 2026-10-29 | D | Target System Model + G4 |
| F | Arquitectura | ⚪ | — | 2026-11-12 | E | Architecture Baseline + G5 |
| G | Diseño | ⚪ | — | 2026-11-26 | F | Design Baseline + G6 |
| H | Implementación / construcción | ⚪ | — | 2026-12-18 | G | Build Baseline + G7 |
| I | Integración y verificación | ⚪ | — | 2027-01-15 | H | Verification Evidence + G8 |
| J | Validación y aceptación | ⚪ | — | 2027-01-29 | I | Acceptance Baseline + G9 |
| K | Transición y despliegue | ⚪ | — | 2027-02-12 | J | Production Release + G10 |
| L | Operación y soporte | ⚪ | — | 2027-03-12 | K | Operational Baseline + G11 |
| M | Mantenimiento y evolución | 🔵 | — | Desde K | K / L | Evolution Releases |
| N | Mejora y optimización | 🔵 | — | Desde L | L + evidencia | Improvement Evidence |
| O | Retirada / migración | ⚪ | — | Según decisión | Evolución | Retirement Record + G12 |

> **A todavía no está completada.** La documentación demuestra preparación, pero la fase requiere evidencia de salida de G0.

## Camino completo del Ecosistema

```text
SETA EXPRESO ECOSYSTEM
        │
        ▼
A ─ Concepción y gobernanza ─────────────── G0
        │
        ▼
B ─ Descubrimiento del sistema ──────────── G1
        │
        ▼
C ─ Necesidades, problema y objetivos ────── G2
        │
        ▼
D ─ Ingeniería de requisitos ────────────── G3
        │
        ▼
E ─ Definición y modelado del sistema ───── G4
        │
        ▼
F ─ Arquitectura ────────────────────────── G5
        │
        ▼
G ─ Diseño ──────────────────────────────── G6
        │
        ▼
H ─ Implementación / construcción ───────── G7
        │
        ▼
I ─ Integración y verificación ──────────── G8
        │
        ▼
J ─ Validación y aceptación ─────────────── G9
        │
        ▼
K ─ Transición y despliegue ────────────── G10
        │
        ▼
L ─ Operación y soporte ───────────────── G11
        │
        ├────────────► M Mantenimiento ───────┐
        │                                      │
        └────────────► N Mejora ──────────────┤
                                               ▼
                                    O Retirada / Migración
                                               │
                                               ▼
                                              G12
```

El macroflujo es el camino de control. Las actividades internas pueden ejecutarse iterativa, incremental, concurrente o recursivamente cuando el contexto lo justifique.

## Trabajo actualmente en curso

| Issue | Actividad | Estado | Fecha inicio | Fecha objetivo | Dependencia | PR |
|---|---|---|---|---|---|---|
| #22 | Automatizar Security Validation inicial | 🟡 | 2026-09-15 | 2026-09-17 | Governance Enforcement (#13) + Quality Validation (#20) | En construcción |

La actividad se considera completada únicamente cuando el PR asociado haya sido validado, integrado y exista evidencia de ejecución satisfactoria de Governance Validation, Quality Validation y Security Validation.

## Controles transversales de ingeniería

| Capacidad | Estado | Evidencia actual | Evolución |
|---|---|---|---|
| Governance Validation | 🟢 | Workflow + PRs validados | Ampliación de controles |
| Quality Validation | 🟢 | Workflow + PR #21 | Incorporación de controles sobre código y pruebas |
| Security Validation | 🟡 | Issue #22 + rama de implementación | SAST, SCA, secrets, IaC, containers, SBOM según aplicabilidad |
| Evidence Validation | ⚪ | Arquitectura prevista | Implementación posterior |

## Seguimiento detallado A–D

### A — Concepción y gobernanza

| ID | Actividad | Estado | Fecha real | Fecha objetivo | Evidencia |
|---|---|---|---|---|---|
| A.1 | Definir propósito y alcance del ciclo de vida | 🟡 | — | 2026-09-15 | Lifecycle Master |
| A.2 | Auditar ciclo de vida contra estándares | 🟢 | 2026-09-15 | — | Lifecycle Audit |
| A.3 | Consolidar ciclo de vida A–O | 🟢 | 2026-09-15 | — | `00-Software-Lifecycle-Master.md` |
| A.4 | Establecer gobernanza documental | 🟢 | 2026-09-15 | — | Governance artifacts |
| A.5 | Establecer control de cambios | 🟢 | 2026-09-15 | — | `06-Change-Control-Workflow.md` |
| A.6 | Establecer estrategia de protección de main | 🟢 | 2026-09-15 | — | `07-Main-Protection-Strategy.md` + workflow |
| A.7 | Establecer Roadmap maestro | 🟢 | 2026-09-15 | — | PR #10 |
| A.8 | Establecer política de labels | 🟢 | 2026-09-15 | — | PR #10 |
| A.9 | Cerrar gobernanza / G0 | 🟡 | 2026-09-15 | 2026-09-17 | Gate G0 |

### B — Descubrimiento

| ID | Actividad | Estado | Fecha objetivo |
|---|---|---|---|
| B.1 | Identificar stakeholders | ⚪ | 2026-09-18 |
| B.2 | Levantar procesos actuales | ⚪ | 2026-09-19 |
| B.3 | Inventariar sistemas y herramientas | ⚪ | 2026-09-20 |
| B.4 | Inventariar datos e información | ⚪ | 2026-09-21 |
| B.5 | Identificar integraciones y dependencias | ⚪ | 2026-09-22 |
| B.6 | Identificar restricciones | ⚪ | 2026-09-23 |
| B.7 | Construir Current-State Model | ⚪ | 2026-09-23 |
| B.8 | Revisar descubrimiento | ⚪ | 2026-09-24 |
| B.9 | Gate G1 | ⚪ | 2026-09-24 |

### C — Necesidades, problema y objetivos

| ID | Actividad | Estado | Fecha objetivo |
|---|---|---|---|
| C.1 | Formular problema | ⚪ | 2026-09-25 |
| C.2 | Identificar necesidades | ⚪ | 2026-09-26 |
| C.3 | Definir objetivos | ⚪ | 2026-09-27 |
| C.4 | Definir alcance y fuera de alcance | ⚪ | 2026-09-28 |
| C.5 | Definir resultados y éxito | ⚪ | 2026-09-29 |
| C.6 | Analizar beneficios y costes | ⚪ | 2026-09-30 |
| C.7 | Revisar con stakeholders | ⚪ | 2026-10-01 |
| C.8 | Consolidar baseline | ⚪ | 2026-10-01 |
| C.9 | Gate G2 | ⚪ | 2026-10-01 |

### D — Ingeniería de requisitos

| ID | Actividad | Estado | Fecha objetivo |
|---|---|---|---|
| D.1 | Estrategia de requisitos | ⚪ | 2026-10-02 |
| D.2 | Elicitación | ⚪ | 2026-10-03 |
| D.3 | Análisis | ⚪ | 2026-10-05 |
| D.4 | Requisitos funcionales | ⚪ | 2026-10-07 |
| D.5 | Requisitos de calidad | ⚪ | 2026-10-09 |
| D.6 | Restricciones | ⚪ | 2026-10-10 |
| D.7 | Interfaces | ⚪ | 2026-10-11 |
| D.8 | Seguridad y privacidad | ⚪ | 2026-10-12 |
| D.9 | Datos | ⚪ | 2026-10-12 |
| D.10 | Criterios de aceptación | ⚪ | 2026-10-13 |
| D.11 | Trazabilidad / RTM | ⚪ | 2026-10-13 |
| D.12 | Verificación de requisitos | ⚪ | 2026-10-14 |
| D.13 | Priorización | ⚪ | 2026-10-14 |
| D.14 | Requirements Baseline | ⚪ | 2026-10-15 |
| D.15 | Gate G3 | ⚪ | 2026-10-15 |

## E–O: planificación inicial

| Fase | Estado | Fecha objetivo inicial | Resultado |
|---|---|---|---|
| E | ⚪ | 2026-10-29 | Target System Model |
| F | ⚪ | 2026-11-12 | Architecture Baseline + ADRs |
| G | ⚪ | 2026-11-26 | Design Baseline |
| H | ⚪ | 2026-12-18 | Build Baseline |
| I | ⚪ | 2027-01-15 | Verification Evidence |
| J | ⚪ | 2027-01-29 | Acceptance Baseline |
| K | ⚪ | 2027-02-12 | Production Release |
| L | ⚪ | 2027-03-12 | Operational Baseline |
| M | 🔵 | Desde K | Evolution Releases |
| N | 🔵 | Desde L | Improvement Evidence |
| O | ⚪ | Según decisión | Retirement Record |

## Quality Gates

| Gate | Control | Estado |
|---|---|---|
| G0 | Governance Baseline | 🟡 |
| G1 | Current-State Understanding | ⚪ |
| G2 | Value & Scope | ⚪ |
| G3 | Requirements Baseline | ⚪ |
| G4 | System Definition | ⚪ |
| G5 | Architecture Baseline | ⚪ |
| G6 | Design Baseline | ⚪ |
| G7 | Build Integrity | ⚪ |
| G8 | Verification | ⚪ |
| G9 | Acceptance | ⚪ |
| G10 | Production Readiness | ⚪ |
| G11 | Operational Readiness | ⚪ |
| G12 | Retirement | ⚪ |

## Registro histórico

| Fecha | Hito | Evidencia |
|---|---|---|
| 2026-09-15 | Auditoría y consolidación del ciclo de vida A–O | `01-Software-Lifecycle-Audit.md`, `00-Software-Lifecycle-Master.md` |
| 2026-09-15 | Control de cambios | `06-Change-Control-Workflow.md` |
| 2026-09-15 | Estrategia compensatoria de main | `07-Main-Protection-Strategy.md` |
| 2026-09-15 | Roadmap y política de labels | PR #10 |
| 2026-09-15 | Quality Validation integrada | Issue #20 + PR #21 |
| 2026-09-15 | Security Validation iniciada | Issue #22 |

## Trazabilidad con GitHub

```text
Roadmap Activity → Issue → Branch → Implementation → Impact Analysis
→ Governance Validation → Quality Validation → Security Validation
→ Evidence / Tests → Pull Request → Review → Merge → main Baseline
```

## Convención de títulos de Issues y Pull Requests

Toda nueva unidad de trabajo utilizará:

> **`Módulo/Archivo: Acción a realizar.`**

Ejemplos:

- `Gobernanza/08-Software-Roadmap.md: Actualizar seguimiento y fechas.`
- `Descubrimiento/Stakeholders: Identificar y registrar actores.`
- `Requisitos/Requirements-Baseline.md: Definir requisitos verificables.`
- `Arquitectura/Architecture-Baseline.md: Establecer arquitectura objetivo.`
- `Testing/Verification-Plan.md: Definir estrategia de verificación.`

**Módulo** identifica el dominio; **Archivo**, el artefacto principal cuando exista; **Acción**, la actividad concreta y comienza con un verbo. El título termina en punto. No se permiten títulos genéricos.

## Reglas de actualización

El Roadmap se actualiza cuando una actividad comienza, termina con evidencia, cambia su fecha objetivo, dependencia, alcance, bloqueo, gate o ruta crítica. Las fechas reales se conservan; las fechas objetivo pueden ajustarse con justificación.

## Fuente de verdad

- `00-Software-Lifecycle-Master.md`: define el ciclo de vida.
- `08-Software-Roadmap.md`: calendariza y registra ejecución.
- `04-Quality-Gates.md`: define criterios de decisión.
- `03-Artifacts-And-Evidence.md`: define evidencia.
- Issues / PRs: unidades trazables de trabajo e integración.
- `main`: baseline integrada.
