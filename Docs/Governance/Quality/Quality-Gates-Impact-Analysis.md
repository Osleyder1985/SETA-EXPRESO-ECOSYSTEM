# Quality Gates — Análisis de impacto

**Issue:** #43  
**Estado:** En elaboración dentro de branch controlada  

## 1. Objetivo

Evaluar el impacto de operacionalizar G0–G13 antes de integrar el cambio.

## 2. Artefactos impactados

| Área | Artefacto | Impacto |
|---|---|---|
| Governance | `04-Quality-Gates.md` | Alto: pasa de definición conceptual a definición operacional |
| Quality | `12-Quality-Validation-Architecture.md` | Alto: QV pasa a ser fuente explícita de evidencia para gates |
| Quality | `Quality/Quality-Gate-Catalog.yml` | Nuevo: catálogo machine-readable |
| Requirements | Requisitos futuros | Alto: G3/G4 necesitarán fuentes estructuradas |
| Architecture | Arquitectura futura | Medio/alto: G5 debe evaluar trazabilidad y decisiones |
| Design | Diseño futuro | Medio: G6 requiere trazabilidad |
| Testing | Pruebas futuras | Alto: G8 dependerá de evidencia de verificación |
| Risk | Risk Register | Medio/alto: riesgos condicionan decisiones de gates |
| Decision | ADR/EDR | Medio/alto: autoridades y decisiones materiales deben quedar trazables |
| Security | Security Validation | Medio: evidencia de seguridad alimenta gates aplicables |
| Evidence | Evidence Validation | Alto: evidencia pasa a ser insumo formal del gate |
| Metrics | Metric Catalog | Alto: métricas de gate necesitan definiciones y fuentes |
| AI | AI Governance | Medio: controles AI aplican cuando el alcance lo requiera |
| Supplier | Third-Party Governance | Medio: dependencias externas pueden bloquear gates críticos |
| Lifecycle | `00-Software-Lifecycle-Master.md` | Medio: gates formalizan decisiones de transición |

## 3. Principio de integración

No se pretende automatizar todo el juicio de ingeniería. La operacionalización separa:

- hechos comprobables por máquina;
- comprobaciones híbridas;
- decisiones que requieren autoridad humana.

## 4. Riesgos del cambio

- Falsos PASS por fuentes incompletas.
- Falsos BLOCKED por datos todavía no disponibles.
- Umbrales arbitrarios sin baseline.
- Automatización de criterios que en realidad requieren juicio.
- Duplicación entre Quality Validation y Quality Gate.
- Desalineación entre métricas y fuentes operacionales.

## 5. Mitigaciones

- catálogo con clasificación de automatización;
- evidencia obligatoria;
- fuente y limitaciones para métricas;
- separación QV vs Gate Decision;
- autoridad explícita;
- REOPEN ante cambios que invaliden evidencia;
- prohibición de inventar datos o aceptación.

## 6. Criterio de cierre

El impacto se considera controlado cuando los artefactos afectados quedan actualizados o la dependencia futura queda registrada explícitamente, sin introducir afirmaciones no verificadas.
