# Catálogo de artefactos y evidencias de ingeniería

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.6.0  
**Estado:** Catálogo controlado  
**Fecha:** 2026-09-15

---

## 1. Propósito

Definir las principales clases de artefactos y evidencias que pueden producirse durante el ciclo de vida. El catálogo evita que la documentación se convierta en un conjunto arbitrario de archivos y permite relacionar cada evidencia con una fase, decisión, requisito o resultado.

## 2. Principio

Un artefacto debe existir porque cumple una función de ingeniería, gobernanza, comunicación, verificación, operación o investigación. Su profundidad debe ser proporcional al riesgo y al impacto.

## 3. Catálogo inicial

| Área | Artefactos principales | Evidencia típica |
|---|---|---|
| Gobernanza | Project Charter, Governance Model, Governance Enforcement Architecture, Quality Validation Architecture, Security Validation Architecture, Evidence Validation Architecture, Risk Register, Issues, Pull Requests | Aprobaciones, decisiones, validaciones automatizadas, revisiones, integración |
| Negocio | Problem Statement, Process Models, Objectives | Entrevistas, observaciones |
| Requisitos | Needs, Requirements, Acceptance Criteria | Revisiones, baselines |
| Arquitectura | Architecture Description, Views, ADRs | Reviews, decisions |
| Diseño | Detailed Design, API Specs, Data Models | Design reviews |
| Construcción | Source Code, Config, Build Artifacts | Commits, CI results |
| Testing | Test Plans, Cases, Results | Test runs, reports |
| Seguridad | Threat Models, Security Requirements, Findings, Security Validation results | Scans, reviews, remediation |
| DevOps | Pipelines, Releases, Deployment Plans | Pipeline logs, release records |
| Operaciones | Runbooks, Incidents, Problems, Metrics | Operational records |
| Datos | Data Models, Migration Plans, Quality Records | Validation and migration evidence |
| Investigación | Protocols, Datasets, Analysis, Results | Reproducible study evidence |

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

## 10. Evidencia externa

Si la evidencia no puede almacenarse directamente en GitHub por tamaño, confidencialidad, regulación o naturaleza del medio, el repositorio conservará metadatos suficientes para localizarla y verificar su integridad cuando sea apropiado.

## 11. Control de cambios

El catálogo evolucionará junto con el proyecto. Los nuevos artefactos deberán justificar su propósito y ubicación.

Toda adición, modificación, actualización, movimiento, renombrado o eliminación de un artefacto deberá activar un análisis de impacto sobre los artefactos relacionados. Si otro artefacto resulta afectado, deberá actualizarse en la misma unidad de cambio cuando sea razonable o quedar registrado como trabajo pendiente trazable.

La cadena de evidencia deberá conservar, cuando aplique:

```text
Necesidad / Problema → Issue → Branch → Cambio → Impacto → Governance Validation → Quality Validation → Security Validation → Evidence Validation → Evidencia → Pull Request → Revisión → Merge → main
```

Este catálogo se interpreta conjuntamente con `Docs/Governance/00-Software-Lifecycle-Master.md`, `Docs/Governance/06-Change-Control-Workflow.md`, `Docs/Governance/10-Governance-Enforcement-Architecture.md`, `Docs/Governance/12-Quality-Validation-Architecture.md`, `Docs/Governance/13-Security-Validation-Architecture.md` y `Docs/Governance/14-Evidence-Validation-Architecture.md`.
