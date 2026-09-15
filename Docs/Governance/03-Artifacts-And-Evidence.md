# Catálogo de artefactos y evidencias de ingeniería

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Catálogo inicial  
**Fecha:** 2026-09-15

---

## 1. Propósito

Definir las principales clases de artefactos y evidencias que pueden producirse durante el ciclo de vida. El catálogo evita que la documentación se convierta en un conjunto arbitrario de archivos y permite relacionar cada evidencia con una fase, decisión, requisito o resultado.

## 2. Principio

Un artefacto debe existir porque cumple una función de ingeniería, gobernanza, comunicación, verificación, operación o investigación. Su profundidad debe ser proporcional al riesgo y al impacto.

## 3. Catálogo inicial

| Área | Artefactos principales | Evidencia típica |
|---|---|---|
| Gobernanza | Project Charter, Governance Model, Risk Register | Aprobaciones, decisiones |
| Negocio | Problem Statement, Process Models, Objectives | Entrevistas, observaciones |
| Requisitos | Needs, Requirements, Acceptance Criteria | Revisiones, baselines |
| Arquitectura | Architecture Description, Views, ADRs | Reviews, decisions |
| Diseño | Detailed Design, API Specs, Data Models | Design reviews |
| Construcción | Source Code, Config, Build Artifacts | Commits, CI results |
| Testing | Test Plans, Cases, Results | Test runs, reports |
| Seguridad | Threat Models, Security Requirements, Findings | Scans, reviews, remediation |
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

## 6. Evidencia externa

Si la evidencia no puede almacenarse directamente en GitHub por tamaño, confidencialidad, regulación o naturaleza del medio, el repositorio conservará metadatos suficientes para localizarla y verificar su integridad cuando sea apropiado.

## 7. Control de cambios

El catálogo evolucionará junto con el proyecto. Los nuevos artefactos deberán justificar su propósito y ubicación.
