# SETA EXPRESO ECOSYSTEM

Repositorio oficial de ingeniería del Ecosistema Digital de Seta Expreso S.U.R.L.

> **No solamente construiremos el Ecosistema; construiremos y conservaremos la evidencia de ingeniería que demuestra cómo y por qué fue construido.**

## Propósito

Este repositorio constituye la fuente controlada de código, documentación, decisiones, modelos, pruebas, configuraciones y evidencias del proyecto.

## Estado actual

El proyecto se encuentra en la consolidación de su **fundación de ingeniería**: ciclo de vida maestro, gobernanza, trazabilidad, control de cambios, Decision Governance, Roadmap, Metrics Governance, AI Governance y mecanismos de evidencia.

La construcción funcional no se inicia por defecto hasta que las fases precedentes del ciclo de vida proporcionen la definición y evidencia necesarias.

## Contribuir

Antes de realizar cualquier cambio consulte:

- `CONTRIBUTING.md`
- `docs/Governance/`
- Pull Request Template

Todos los cambios requieren:

```text
Issue → Branch → PR → Validación → Merge
```

Los cambios no deben realizarse directamente sobre `main`. Todo trabajo debe conservar trazabilidad mediante Issue, Branch, Pull Request, validaciones automáticas y evidencia asociada.

## 🧭 Roadmap de Ingeniería

El trabajo del Ecosistema se gobierna mediante un **Roadmap maestro derivado directamente de las fases A–O** de `docs/Governance/00-Software-Lifecycle-Master.md`.

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

👉 **[Roadmap Maestro completo](docs/Governance/08-Software-Roadmap.md)**  
👉 **[Ciclo de Vida Maestro A–O](docs/Governance/00-Software-Lifecycle-Master.md)**

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
- **Documentation root:** `docs/`.

