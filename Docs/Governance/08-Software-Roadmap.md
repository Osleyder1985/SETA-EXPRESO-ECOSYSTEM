# Roadmap Maestro de Ingeniería del Ecosistema

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Vigente como hoja de ruta de ingeniería  
**Fuente canónica:** `Docs/Governance/00-Software-Lifecycle-Master.md`  
**Relacionado:** Issue #9

---

## 1. Propósito

Este documento convierte el **Ciclo de Vida Maestro A–O** en una hoja de ruta ejecutable, trazable y visible del Ecosistema.

El Roadmap no es un calendario rígido ni una promesa de fechas. Es un **mapa de evolución de ingeniería** que conecta:

```text
Necesidad / problema
        ↓
Fase del ciclo de vida
        ↓
Entregables
        ↓
Quality Gate
        ↓
Issue(s) / PR(s)
        ↓
Evidencia verificable
        ↓
Baseline / decisión
        ↓
Siguiente evolución
```

La planificación se adapta al riesgo, descubrimiento, evidencia y dependencias reales. Las fases pueden ejecutarse de forma iterativa, incremental, concurrente y recursiva cuando el contexto lo justifique.

---

## 2. North Star de ingeniería

> **Construir un Ecosistema digital útil y sostenible, pero también construir una cadena de evidencia que permita demostrar cómo, por qué y con qué calidad fue construido y evolucionado.**

### Los cinco ejes del Roadmap

| Eje | Pregunta que responde |
|---|---|
| 🎯 **Value** | ¿Qué problema y qué resultado estamos resolviendo? |
| 🧭 **System** | ¿Cómo funciona el Ecosistema como sistema sociotécnico? |
| 🏗️ **Engineering** | ¿Cómo transformamos necesidades en software verificable? |
| 🛡️ **Trust** | ¿Cómo demostramos calidad, seguridad, trazabilidad y operación? |
| 🔬 **Evidence** | ¿Qué evidencia permite reproducir y evaluar nuestras decisiones? |

---

## 3. Estado ejecutivo

### Engineering Flight Plan

```text
FOUNDATION
   │
   ├── A  Concepción y gobernanza          🟡
   ├── B  Descubrimiento del sistema       ⚪
   ├── C  Necesidades y objetivos           ⚪
   ├── D  Ingeniería de requisitos          ⚪
   ├── E  Definición y modelado             ⚪
   ├── F  Arquitectura                      ⚪
   ├── G  Diseño                            ⚪
   ├── H  Implementación                    ⚪
   ├── I  Integración y verificación        ⚪
   ├── J  Validación y aceptación           ⚪
   ├── K  Transición y despliegue           ⚪
   ├── L  Operación y soporte               ⚪
   ├── M  Mantenimiento y evolución         ⚪
   ├── N  Mejora y optimización             ⚪
   └── O  Retirada / migración              ⚪
   │
   └───────────────→ EVOLUTION LOOP
```

**Leyenda:**

- 🟢 **Completado:** ejecutado y respaldado por evidencia suficiente.
- 🟡 **Activo / siguiente foco:** trabajo de ingeniería actualmente prioritario.
- 🔵 **Recurrente:** actividad transversal o ciclo continuo.
- ⚪ **Planificado:** todavía no iniciado como fase ejecutada.
- 🔴 **Bloqueado:** existe una dependencia que impide avanzar.

> **Regla de integridad:** una fase no se marca como 🟢 por la existencia de documentación preliminar. Requiere ejecución, verificación y evidencia conforme a sus criterios de salida.

---

## 4. Horizonte de ejecución

### 🟡 NOW — Fundaciones controladas

**Objetivo:** cerrar la base metodológica y de gobierno antes de transformar el conocimiento del negocio en requisitos y arquitectura.

| Prioridad | Fase | Resultado objetivo | Gate dominante |
|---|---|---|---|
| N1 | **A** | Baseline de gobernanza y estrategia de ciclo de vida | G0 — Governance Baseline |
| N2 | **B** | Modelo confiable del estado actual | G1 — Current-State Understanding |
| N3 | **C** | Problema, necesidades, objetivos, alcance y éxito | G2 — Value & Scope |
| N4 | **D** | Requisitos verificables y trazables | G3 — Requirements Baseline |

**Evidencia mínima:** decisiones, modelos, fuentes, Issues, PRs, revisiones, matrices de trazabilidad y resultados de Quality Gates.

---

### 🔵 NEXT — Diseñar antes de construir

**Objetivo:** transformar necesidades y requisitos en un sistema objetivo y una arquitectura defendible.

| Prioridad | Fase | Resultado objetivo | Gate dominante |
|---|---|---|---|
| X1 | **E** | Modelo objetivo del Ecosistema | G4 — System Definition |
| X2 | **F** | Arquitectura del sistema/ecosistema y software | G5 — Architecture Baseline |
| X3 | **G** | Diseño detallado preparado para construcción y verificación | G6 — Design Baseline |
| X4 | **H** | Incrementos construidos, revisados y reproducibles | G7 — Build Integrity |

**Evidencia mínima:** modelos, Architecture Description, ADRs, decisiones de diseño, threat models, especificaciones, código, pruebas y artefactos reproducibles.

---

### ⚪ LATER — Demostrar, desplegar y operar

| Prioridad | Fase | Resultado objetivo | Gate dominante |
|---|---|---|---|
| L1 | **I** | Integración y verificación objetiva | G8 — Verification |
| L2 | **J** | Validación del uso previsto y aceptación | G9 — Acceptance |
| L3 | **K** | Transición controlada a producción | G10 — Production Readiness |
| L4 | **L** | Operación observable, segura y sostenible | G11 — Operational Readiness |

---

### ♻️ ALWAYS — Evolución permanente

Las fases siguientes no representan un final del producto; representan la capacidad de evolucionarlo de forma controlada.

| Fase | Misión |
|---|---|
| **M** | Corregir, adaptar, refactorizar y ampliar sin perder trazabilidad. |
| **N** | Mejorar calidad, rendimiento, coste, seguridad, experiencia y eficiencia del proceso. |
| **O** | Retirar, sustituir o migrar capacidades de forma controlada, preservando evidencia e información necesaria. |

**Bucle de evolución:**

```text
Operación → Evidencia → Aprendizaje → Cambio → Impacto
     ↑                                      ↓
     └──────── Validación ← Construcción ←──┘
```

---

## 5. Mapa completo A–O

| ID | Fase | Entregable principal | Evidencia de salida |
|---|---|---|---|
| **A** | Concepción y gobernanza | Project Charter + Governance Model + Lifecycle Strategy | Decisiones, reglas, riesgos, baseline |
| **B** | Descubrimiento del sistema y organización | Current-State Model | Procesos, actores, sistemas, datos, restricciones |
| **C** | Necesidades, problema y objetivos | Problem Statement + Objectives + Scope | Causas, necesidades, éxito, business case cuando aplique |
| **D** | Ingeniería de requisitos | Requirements Baseline + RTM | Requisitos verificables, aceptación y trazabilidad |
| **E** | Definición y modelado del sistema | Target System Model | Dominio, procesos, capacidades, información, contexto |
| **F** | Arquitectura | Architecture Baseline + ADRs | Vistas, decisiones, riesgos y evaluaciones |
| **G** | Diseño | Design Baseline | APIs, datos, componentes, seguridad, pruebas |
| **H** | Implementación y construcción | Build Baseline | Código, tests, configuración, artefactos |
| **I** | Integración y verificación | Verification Evidence | Resultados, defectos, compatibilidad, seguridad |
| **J** | Validación y aceptación | Acceptance Baseline | Validación, UAT cuando aplique, aceptación |
| **K** | Transición y despliegue | Production Release | Despliegue, migración, rollback, handover |
| **L** | Operación y soporte | Operational Baseline | Observabilidad, incidentes, continuidad, métricas |
| **M** | Mantenimiento y evolución | Evolution Releases | Cambios, deuda técnica, migraciones, ADRs |
| **N** | Mejora y optimización | Improvement Evidence | Métricas, experimentos, optimizaciones y resultados |
| **O** | Retirada / migración | Retirement Record | Migración, preservación, cierre y lecciones |

La definición detallada de cada fase y sus subfases reside exclusivamente en `00-Software-Lifecycle-Master.md`.

---

## 6. Quality Gates como puertas de decisión

El Roadmap utiliza gates para evitar que el proyecto avance únicamente porque "hay trabajo hecho".

```text
G0 Governance
   ↓
G1 Current State
   ↓
G2 Value & Scope
   ↓
G3 Requirements
   ↓
G4 System Definition
   ↓
G5 Architecture
   ↓
G6 Design
   ↓
G7 Build
   ↓
G8 Verification
   ↓
G9 Acceptance
   ↓
G10 Production
   ↓
G11 Operations
   ↺ M / N
   ↓
G12 Retirement
```

Un gate puede producir una de estas decisiones:

- 🟢 **PASS** — se cumplen criterios de salida.
- 🟡 **CONDITIONAL** — puede continuar con riesgos/pedientes explícitos y trazables.
- 🔴 **BLOCKED** — no se autoriza el avance.
- 🔵 **REOPEN** — nueva evidencia obliga a revisar una decisión anterior.

---

## 7. Sistema de trazabilidad del Roadmap

Cada incremento de ingeniería debe poder navegarse en ambos sentidos:

```text
Business Need
    ↕
Objective
    ↕
Requirement
    ↕
Architecture / Design Decision
    ↕
Implementation
    ↕
Test / Verification
    ↕
Validation / Acceptance
    ↕
Operational Metric
    ↕
Change / Improvement
```

Y, desde GitHub:

```text
Roadmap Item
     ↓
Issue
     ↓
Branch
     ↓
Pull Request
     ↓
Review + Checks
     ↓
Merge
     ↓
main Baseline
     ↓
Evidence
```

---

## 8. Regla de planificación

El Roadmap no se ejecuta por "fase completa" de manera artificial. Una fase puede generar múltiples unidades de cambio y un Issue puede requerir varios Pull Requests.

La unidad operativa sigue siendo:

**Issue → Branch → Implementación → Impact Analysis → Evidence → Pull Request → Review → Merge → main**

Antes de abrir una nueva unidad se debe identificar:

1. objetivo y necesidad;
2. fase/subfase del ciclo de vida;
3. dependencias;
4. artefactos afectados;
5. criterios de aceptación;
6. Quality Gate aplicable;
7. evidencia esperada;
8. riesgos y decisiones pendientes.

---

## 9. Métrica de madurez del Roadmap

No se utilizará solamente porcentaje de código construido. La madurez del Ecosistema se observará mediante cinco dimensiones:

| Dimensión | Señal de madurez |
|---|---|
| **Value** | objetivos y resultados verificables |
| **Definition** | requisitos y modelos coherentes |
| **Architecture** | decisiones explícitas y evaluadas |
| **Quality** | verificación, validación y métricas |
| **Evidence** | trazabilidad y reproducibilidad |

Esto evita confundir **cantidad de implementación** con **avance real de ingeniería**.

---

## 10. Regla de actualización

Este Roadmap se actualiza cuando exista evidencia que cambie de manera material:

- el estado de una fase;
- la prioridad del trabajo;
- una dependencia;
- un Quality Gate;
- una decisión arquitectónica o de negocio;
- el alcance;
- un riesgo relevante;
- una baseline;
- una condición de operación o evolución.

Las actualizaciones del Roadmap siguen el mismo flujo de control de cambios del repositorio.

---

## 11. Fuente de verdad

| Artefacto | Función |
|---|---|
| `00-Software-Lifecycle-Master.md` | **Define el ciclo de vida.** |
| `08-Software-Roadmap.md` | **Planifica y visualiza su ejecución.** |
| `04-Quality-Gates.md` | Define criterios de decisión y salida. |
| `03-Artifacts-And-Evidence.md` | Define artefactos y evidencia. |
| Issues | Capturan unidades de necesidad/trabajo. |
| Pull Requests | Capturan unidades controladas de integración. |
| `main` | Baseline integrada del repositorio. |

**El Roadmap nunca sustituye al ciclo de vida maestro; lo operacionaliza.**
