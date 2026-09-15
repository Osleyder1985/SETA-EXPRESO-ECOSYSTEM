# SETA EXPRESO ECOSYSTEM

Repositorio oficial de ingeniería del Ecosistema Digital de Seta Expreso S.U.R.L.

> **No solamente construiremos el Ecosistema; construiremos y conservaremos la evidencia de ingeniería que demuestra cómo y por qué fue construido.**

## Propósito

Este repositorio constituye la fuente controlada de código, documentación, decisiones, modelos, pruebas, configuraciones y evidencias del proyecto.

## Estado actual

El proyecto se encuentra en la consolidación de su **fundación de ingeniería**: ciclo de vida maestro, gobernanza, trazabilidad, control de cambios, Decision Governance, Roadmap, Metrics Governance y mecanismos de evidencia.

La construcción funcional no se inicia por defecto hasta que las fases precedentes del ciclo de vida proporcionen la definición y evidencia necesarias.

## 🧭 Roadmap de Ingeniería

El trabajo del Ecosistema se gobierna mediante un **Roadmap maestro derivado directamente de las fases A–O** de `Docs/Governance/00-Software-Lifecycle-Master.md`.

### Engineering Flight Plan

```text
                 SETA EXPRESO ECOSYSTEM
                         │
        ┌────────────────┴────────────────┐
        │                                 │
   🟡 NOW                            🔵 NEXT
   Fundaciones                       Diseño antes
   de ingeniería                     de construir
        │                                 │
   A → B → C → D                    E → F → G → H
        │                                 │
        └──────────────┬──────────────────┘
                       ↓
                  ⚪ LATER
              Demostrar y operar
                  I → J → K → L
                       │
                       ↓
                 ♻️ ALWAYS
                   M → N → O
                       │
                       └────→ evolución
```

| Horizonte | Fases | Propósito |
|---|---|---|
| 🟡 **NOW** | **A–D** | Gobernanza, descubrimiento, valor y requisitos verificables |
| 🔵 **NEXT** | **E–H** | Definición del sistema, arquitectura, diseño y construcción |
| ⚪ **LATER** | **I–L** | Verificación, aceptación, despliegue y operación |
| ♻️ **ALWAYS** | **M–O** | Evolución, mejora, optimización y retirada/migración |

**Regla:** el estado del Roadmap se actualiza con evidencia. Tener documentos preliminares no equivale a completar una fase.

👉 **[Roadmap Maestro completo](Docs/Governance/08-Software-Roadmap.md)**  
👉 **[Ciclo de Vida Maestro A–O](Docs/Governance/00-Software-Lifecycle-Master.md)**

### Quality Gates

```text
G0 Governance → G1 Current State → G2 Value & Scope
      → G3 Requirements → G4 System → G5 Architecture
      → G6 Design → G7 Build → G8 Verification
      → G9 Acceptance → G10 Production → G11 Operations
      → ↺ M/N → G12 Retirement
```

El Roadmap conecta cada tramo con **entregables, Quality Gates, Issues, Pull Requests y evidencia verificable**.

## Repository Conventions

- **Repository structure:** English.
- **Directory names:** English, Title Case by word, separated with `-` when multi-word.
- **File names:** English, Title Case by word, separated with `-` when multi-word.
- **Documentation content:** Spanish.
- **Code and technical identifiers:** English by default, with justified exceptions when required by an external technology or integration.
- **Documentation root:** `Docs/`.

Example:

```text
01-Software-Lifecycle-Audit.md
02-Standards-Lifecycle-Matrix.md
03-Artifacts-And-Evidence.md
```

## Repository Structure

```text
SETA-EXPRESO-ECOSYSTEM/
├── README.md
├── Docs/
│   ├── Governance/
│   │   ├── Metrics/
│   │   └── Risk/
│   ├── Business/
│   ├── Requirements/
│   ├── Architecture/
│   │   └── Decision-Records/
│   ├── Design/
│   ├── Testing/
│   ├── Security/
│   ├── DevOps/
│   ├── Operations/
│   ├── Data/
│   ├── Research/
│   └── Standards/
├── Source/
├── Tests/
├── Infrastructure/
├── Configuration/
├── Scripts/
└── .github/
```

Git no almacena directorios vacíos; las carpetas se crearán conforme existan artefactos que deban gestionarse en ellas.

## Governance Documents

- `Docs/Governance/00-Software-Lifecycle-Master.md` — marco maestro consolidado v0.3.0.
- `Docs/Governance/01-Software-Lifecycle-Audit.md` — auditoría metodológica inicial.
- `Docs/Governance/02-Standards-Lifecycle-Matrix.md` — alineación del ciclo con referencias normativas y técnicas.
- `Docs/Governance/03-Artifacts-And-Evidence.md` — catálogo de artefactos y evidencias.
- `Docs/Governance/04-Quality-Gates.md` — gates del ciclo de vida.
- `Docs/Governance/05-Repository-Naming-Convention.md` — política de nomenclatura y estructura.
- `Docs/Governance/06-Change-Control-Workflow.md` — flujo obligatorio de Issue → Branch → Pull Request → `main` y control de impacto.
- `Docs/Governance/07-Main-Protection-Strategy.md` — estrategia de protección compensatoria de `main` bajo GitHub Free + repositorio privado.
- `Docs/Governance/08-Software-Roadmap.md` — Roadmap maestro de ejecución del ciclo de vida A–O.
- `Docs/Governance/09-Issue-And-Pull-Request-Labeling-Policy.md` — política de clasificación de Issues y Pull Requests.
- `Docs/Governance/19-Decision-Governance.md` — política formal de Architecture y Engineering Decision Records.
- `Docs/Governance/20-Decision-Governance-Control-Matrix.md` — matriz de controles de Decision Governance.
- `Docs/Governance/21-Engineering-Metrics-Governance.md` — política formal de métricas de ingeniería.
- `Docs/Governance/22-Engineering-Metrics-Control-Matrix.md` — matriz de controles de Metrics Governance.
- `Docs/Governance/Metrics/Metric-Catalog.yml` — catálogo canónico de métricas.
- `Docs/Governance/Metrics/Engineering-Governance-Dashboard.md` — vista documental derivada del catálogo métrico.
- `Docs/Governance/Metrics/Engineering-Governance-Dashboard.html` — Dashboard visual derivado del catálogo.

## Decision Governance

Las decisiones materiales de arquitectura e ingeniería se gestionarán mediante **Architecture Decision Records (ADR)** y **Engineering Decision Records (EDR)** cuando corresponda. Un Decision Record debe conservar el contexto, decisión, alternativas, criterios, trade-offs, consecuencias, riesgos, evidencia, estado y relaciones de supersession, además de trazabilidad y aprobación según aplicabilidad.

Los registros controlados se almacenan en:

```text
Docs/Architecture/Decision-Records/
├── README.md
├── ADR-Template.md
├── EDR-Template.md
└── Decision-Record-Index.md
```

Los ejemplos de decisiones futuras —como PostgreSQL, arquitectura modular, REST/GraphQL, Kubernetes, proveedor, identidad o arquitectura de IA— son **temas potenciales**, no decisiones aprobadas. No se registrarán como decisiones hasta disponer del contexto y la evidencia necesarios.

## Engineering Metrics Governance

El Ecosistema mantiene un sistema formal para definir, medir, interpretar y evolucionar indicadores de ingeniería. La capacidad cubre **Delivery, Quality, Requirements, Architecture, Security y Governance**.

La fuente canónica es `Docs/Governance/Metrics/Metric-Catalog.yml`. El Dashboard es una representación derivada y no reemplaza al catálogo ni a la evidencia operacional.

Cada métrica debe conservar, según aplicabilidad, definición, fórmula, población, unidad, fuente, método de colección, frecuencia, owner, baseline, target, thresholds, disponibilidad, evidencia y limitaciones. Cuando todavía no existe evidencia operacional suficiente, el estado permanece explícitamente `defined`, `provisional` o `blocked`; no se inventan valores.

La trazabilidad métrica es:

```text
Metric Definition
  ↓
Source
  ↓
Collection
  ↓
Calculation
  ↓
Snapshot / Evidence
  ↓
Interpretation
  ↓
Decision / Action
  ↓
Outcome
```

👉 **[Engineering Governance Dashboard](Docs/Governance/Metrics/Engineering-Governance-Dashboard.html)**  
👉 **[Metric Catalog](Docs/Governance/Metrics/Metric-Catalog.yml)**

## Change Control

Los cambios del repositorio siguen un flujo obligatorio:

```text
Issue
  ↓
Análisis y alcance
  ↓
Branch
  ↓
Implementación
  ↓
Análisis de impacto
  ↓
Actualización de artefactos afectados
  ↓
Decision Record cuando corresponda
  ↓
Pruebas / evidencia
  ↓
Pull Request
  ↓
Revisión y aprobación
  ↓
Merge
  ↓
main
```

**No se realizan cambios de trabajo directamente sobre `main`.** Un Issue puede resolverse mediante uno o varios Pull Requests. Todo Pull Request deberá documentar en español el cambio, su motivo, alcance, impacto, artefactos afectados, pruebas/evidencias y relación con el Issue.

Los cambios en definiciones, fórmulas, fuentes, alcance, targets o thresholds de métricas también requieren control de cambios y análisis de impacto.

## 🏷️ Labels

Todo **Issue** y **Pull Request** debe tener al menos un label pertinente.

Baseline de clasificación actual:

- `governance` — gobierno, ciclo de vida, políticas, control y planificación.
- `documentation` — documentación, registros y evidencia documental.
- `architecture` — arquitectura de sistema/software y decisiones estructurales.

La taxonomía crecerá cuando el proyecto necesite dominios estables adicionales. Los nuevos labels deberán justificarse y documentarse antes de convertirse en clasificación oficial.

👉 **[Política de Labels](Docs/Governance/09-Issue-And-Pull-Request-Labeling-Policy.md)**

La regla completa de control de cambios está definida en `Docs/Governance/06-Change-Control-Workflow.md`.

## Engineering Principle

> **No solamente construiremos el Ecosistema; construiremos y conservaremos la evidencia de ingeniería que demuestra cómo y por qué fue construido.**
