# Catálogo de artefactos y evidencias de ingeniería

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.1.0  
**Estado:** Catálogo controlado  
**Fecha:** 2026-09-17

---

## 1. Propósito

Definir las principales clases de artefactos y evidencias que pueden producirse durante el ciclo de vida. El catálogo evita que la documentación se convierta en un conjunto arbitrario de archivos y permite relacionar cada evidencia con una fase, decisión, requisito o resultado.

## 2. Principio

Un artefacto debe existir porque cumple una función de ingeniería, gobernanza, comunicación, verificación, operación o investigación. Su profundidad debe ser proporcional al riesgo y al impacto.

## 3. Catálogo inicial

| Área | Artefactos principales | Evidencia típica |
|---|---|---|
| Gobernanza | Project Charter, Governance Model, Governance Enforcement Architecture, Governance Control Matrix, Quality Validation Architecture, Security Validation Architecture, Evidence Validation Architecture, G0 Governance Readiness Assessment, G0 Impact Analysis, Risk Register, Decision Governance, Metrics Governance, AI Governance, Issues, Pull Requests | Aprobaciones, decisiones, validaciones automatizadas, revisiones, integración |
| Negocio | Problem Statement, Process Models, Objectives | Entrevistas, observaciones |
| Requisitos | Needs, Requirements, Acceptance Criteria | Revisiones, baselines |
| Arquitectura | Architecture Description, Views, ADRs, Architecture Decision Log | Reviews, decisions |
| Diseño | Detailed Design, API Specs, Data Models, EDRs cuando correspondan | Design reviews |
| Construcción | Source Code, Config, Build Artifacts | Commits, CI results |
| Testing | Test Plans, Cases, Results | Test runs, reports |
| Seguridad | Threat Models, Security Requirements, Findings, Security Validation results | Scans, reviews, remediation |
| DevOps | Pipelines, Releases, Deployment Plans | Pipeline logs, release records |
| Operaciones | Runbooks, Incidents, Problems, Metrics, Metric Snapshots, AI Incidents | Operational records, measurements, incident records |
| Datos | Data Models, Migration Plans, Quality Records, AI Data Provenance Records | Validation and migration evidence, provenance |
| Investigación | Protocols, Datasets, Analysis, Results, AI Evaluation Records | Reproducible study evidence |

## 4. Reglas de identificación

Los artefactos que requieran trazabilidad persistente tendrán identificadores estables. Los nombres de archivos seguirán la convención del repositorio: inglés, iniciales mayúsculas por palabra y guiones.

## 5. Evidencia mínima

Cuando un artefacto sea crítico, su evidencia debería permitir responder:

1. ¿Qué se hizo?
2. ¿Por qué se hizo?
3. ¿Quién lo realizó o aprobó?
4. ¿Cuándo?
5. ¿Con qué versión o configuración?
6. ¿Qué resultado produjo?
7. ¿Qué requisitos, decisiones o riesgos afecta?
8. ¿Qué Issue y Pull Request controlaron el cambio, cuando corresponda?
9. ¿Qué validaciones automatizadas se ejecutaron, cuando correspondan?

## 6. Evidencia de enforcement

Los controles automatizados de gobernanza, calidad, seguridad y evidencia deberán conservar, cuando corresponda:

- nombre del workflow;
- commit validado;
- evento que lo disparó;
- resultado del job;
- regla o control evaluado;
- mensaje de fallo o éxito;
- actor/evento asociado;
- clasificación del control: preventivo compensatorio, detectivo o gobernanza;
- estado global de Governance Validation, Quality Validation, Security Validation y Evidence Validation.

Los workflows no se consideran evidencia suficiente por su mera existencia: debe existir una ejecución verificable o una justificación explícita.

Para MC-001, la evidencia mínima de una actualización de `main` incluye el evento, actor, timestamp del commit y de observación, SHA actual, SHA anterior cuando exista, estado del push, archivos afectados, PRs asociados, clasificación, workflow run y artifact. Cuando se detecta una anomalía, la evidencia debe conservar también la referencia al Issue de incidente generado o actualizado. El control es detectivo y no realiza auto-revert.

## 7. Evidencia de Quality Validation

Una ejecución de Quality Validation deberá permitir identificar como mínimo:

- commit evaluado;
- Pull Request, cuando aplique;
- controles QV ejecutados;
- resultado individual y global;
- mensajes de fallo;
- workflow run;
- fecha/hora y contexto de ejecución.

Un `QUALITY_VALIDATION=PASS` solo evidencia la conformidad con los controles automatizados aplicables; no constituye certificación de calidad integral del producto.

## 8. Evidencia de Security Validation

Una ejecución de Security Validation deberá permitir identificar como mínimo:

- commit evaluado;
- Pull Request, cuando aplique;
- controles SV ejecutados;
- resultado individual y global;
- clasificación `NOT_APPLICABLE` o `NOT_IMPLEMENTED` cuando corresponda;
- mensajes de fallo;
- workflow run;
- fecha/hora y contexto de ejecución.

Un `SECURITY_VALIDATION=PASS` solo evidencia la conformidad con los controles de seguridad automatizados aplicables; no constituye certificación de seguridad ni ausencia de vulnerabilidades.

## 9. Evidencia de Evidence Validation

Una ejecución de Evidence Validation deberá permitir identificar como mínimo:

- commit evaluado;
- Pull Request, cuando aplique;
- Issue relacionado;
- controles EV ejecutados;
- resultado individual y global;
- evidencia mínima declarada en el PR;
- mensajes de fallo;
- workflow run;
- fecha/hora y contexto de ejecución.

Un `EVIDENCE_VALIDATION=PASS` solo evidencia la conformidad con los controles de evidencia automatizados aplicables; no certifica suficiencia de evidencia ni la corrección del producto.

## 10. Evidencia de Quality Gate Governance

Un Quality Gate deberá conservar un paquete de evidencia suficiente para justificar la decisión de avance, permanencia o rechazo. Como mínimo, cuando aplique, deberá identificar:

- criterio o criterios del Gate evaluados;
- artefactos y versiones utilizadas como entrada;
- resultado de cada control aplicable;
- validaciones automatizadas ejecutadas;
- análisis de impacto asociado;
- limitaciones y controles no disponibles;
- riesgos residuales relevantes;
- decisión formal del Gate;
- Issue y Pull Request asociados;
- commit integrado cuando la decisión dependa de la integración;
- métricas aplicables, periodo, fuente y limitaciones cuando formen parte de la evidencia del Gate.

Para el Gate G0, el paquete mínimo está compuesto por:

```text
15-G0-Governance-Readiness-Assessment.md
        +
16-G0-Impact-Analysis.md
        +
Governance Validation
        +
Quality Validation
        +
Security Validation
        +
Evidence Validation
        +
PR asociado
        +
resultado de integración
```

Los controles `GC-001` a `GC-004` de `11-Governance-Control-Matrix.md` definen los controles específicos de readiness, impacto, evidencia y riesgo residual del Gate G0.

La existencia del paquete no implica por sí misma que el Gate haya sido aprobado: la decisión debe quedar registrada explícitamente.

## 11. Evidencia de Metrics Governance

Metrics Governance deberá conservar, cuando exista medición operacional suficiente:

- Metric ID y versión de definición;
- periodo de medición;
- fuente y método de colección;
- población, numerador y denominador cuando correspondan;
- cálculo reproducible;
- resultado y unidad;
- baseline, target y thresholds cuando estén formalmente definidos;
- limitaciones y disponibilidad del dato;
- snapshot histórico cuando corresponda;
- interpretación;
- decisión o acción derivada cuando exista;
- relación con riesgos, requisitos, decisiones, gates o cambios afectados.

La definición y el catálogo son evidencia de la semántica controlada de la métrica; no equivalen a evidencia de que la métrica ya tenga datos operacionales. Los valores `TBD`, `N/A` o estados equivalentes deberán conservar la razón de su ausencia cuando aplique.

El Dashboard de Engineering Governance es una representación derivada y no constituye la fuente canónica del dato. La fuente canónica de cada métrica es su entrada en `Docs/Governance/Metrics/Metric-Catalog.yml` junto con la evidencia operacional correspondiente.

## 12. Evidencia externa

Si la evidencia no puede almacenarse directamente en GitHub por tamaño, confidencialidad, regulación o naturaleza del medio, el repositorio conservará metadatos suficientes para localizarla y verificar su integridad cuando sea apropiado.

## 13. Control de cambios

El catálogo evolucionará junto con el proyecto. Los nuevos artefactos deberán justificar su propósito y ubicación.

Toda adición, modificación, actualización, movimiento, renombrado o eliminación de un artefacto deberá activar un análisis de impacto sobre los artefactos relacionados. Si otro artefacto resulta afectado, deberá actualizarse en la misma unidad de cambio cuando sea razonable o quedar registrado como trabajo pendiente trazable.

La cadena de evidencia deberá conservar, cuando aplique:

```text
Necesidad / Problema → Issue → Branch → Cambio → Impacto → Governance Validation → Quality Validation → Security Validation → Evidence Validation → Evidencia → Pull Request → Revisión → Merge → main
```

## 14. Decision Governance y Decision Records

Decision Governance constituye una capacidad transversal para conservar el razonamiento de decisiones materiales de arquitectura e ingeniería. Los `Architecture Decision Records (ADR)` y `Engineering Decision Records (EDR)` son artefactos controlados cuando una decisión tenga impacto material, incertidumbre relevante, consecuencias duraderas, alternativas significativas, riesgo apreciable o necesidad de trazabilidad futura.

Los Decision Records deberán conservar, como mínimo cuando correspondan:

- Context;
- Decision;
- Alternatives;
- Criteria;
- Trade-offs;
- Consequences;
- Risks;
- Evidence;
- Status;
- Supersedes;
- Superseded by;
- Traceability y Approval según aplicabilidad.

La existencia de un Decision Record no implica que una alternativa haya sido seleccionada por anticipado. Las decisiones se registrarán cuando exista contexto y evidencia suficientes, evitando decisiones prematuras durante las fases de descubrimiento y definición.

Los registros se gestionarán bajo `Docs/Architecture/Decision-Records/` y se relacionarán con requisitos, arquitectura, diseño, riesgos, Issues, Pull Requests, Quality Gates y evidencia cuando corresponda.

## 15. AI Governance y AI Evidence

AI Governance añade artefactos específicos para registrar usos de IA, modelos, procedencia de datos, prompts relevantes, evaluaciones e incidentes. La estructura canónica está bajo `Docs/Governance/AI/` y la política en `Docs/Governance/23-AI-Governance.md`.

La evidencia de IA deberá permitir, cuando corresponda, reconstruir:

```text
AI Use
  ↓
Model / Service
  ↓
Data Provenance
  ↓
Prompt / Configuration
  ↓
Evaluation / TEVV
  ↓
Human Oversight
  ↓
Output / Decision
  ↓
Evidence / Incident / Outcome
```

No se deberán crear inventarios ficticios ni presentar modelos, evaluaciones o usos como existentes cuando no haya evidencia operacional. Los inventarios iniciales pueden permanecer vacíos.

## 16. Referencias de gobernanza

Este catálogo se interpreta conjuntamente con `Docs/Governance/00-Software-Lifecycle-Master.md`, `Docs/Governance/04-Quality-Gates.md`, `Docs/Governance/06-Change-Control-Workflow.md`, `Docs/Governance/10-Governance-Enforcement-Architecture.md`, `Docs/Governance/11-Governance-Control-Matrix.md`, `Docs/Governance/12-Quality-Validation-Architecture.md`, `Docs/Governance/13-Security-Validation-Architecture.md`, `Docs/Governance/14-Evidence-Validation-Architecture.md`, `Docs/Governance/19-Decision-Governance.md`, `Docs/Governance/20-Decision-Governance-Control-Matrix.md`, `Docs/Governance/21-Engineering-Metrics-Governance.md`, `Docs/Governance/22-Engineering-Metrics-Control-Matrix.md` y `Docs/Governance/23-AI-Governance.md`.
