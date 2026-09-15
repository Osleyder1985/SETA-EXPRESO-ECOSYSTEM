# Matriz de controles de Governance y Quality Enforcement

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.2.0  
**Estado:** Propuesta para aprobación mediante PR asociado al Issue #20  
**Fecha:** 2026-09-15  
**Issues relacionados:** #13, #20

---

## 1. Propósito

Convertir las capas de Governance Enforcement y Quality Validation en una matriz operacional que permita saber qué se controla, por qué, cómo, qué evidencia se obtiene y cuál es la limitación residual.

## 2. Matriz de Governance Enforcement

| ID | Control | Riesgo controlado | Mecanismo | Naturaleza | Evidencia | Limitación |
|---|---|---|---|---|---|---|
| GE-001 | Issue asociado | Cambio no trazable | Referencia en PR + validación | G/D | PR + workflow | No impide push directo |
| GE-002 | Branch no-main | Trabajo accidental en baseline | Validación de PR | P-Compensatorio/D | Check run | No bloquea escritura directa |
| GE-003 | Branch Issue-based | Branch sin unidad de trabajo | Regex + Issue reference | P-Compensatorio/D | Check run | Excepciones requieren control manual |
| GE-004 | Título normalizado | Ambigüedad operacional | Regex | P-Compensatorio/D | Check run | No valida calidad semántica completa |
| GE-005 | Label pertinente | Clasificación deficiente | Metadata validation | P-Compensatorio/D | Check run | No garantiza clasificación correcta |
| GE-006 | Impact analysis | Dependencias omitidas | Texto obligatorio + revisión | P-Compensatorio/G | PR + review | Puede requerir juicio humano |
| GE-007 | Estado único | Ambigüedad de integración | Exact-one validation | P-Compensatorio/D | Check run | No impide merge sin protection |
| GE-008 | Baseline documental | Gobernanza incompleta | File existence validation | D | Check run | No valida todo el contenido |
| GE-009 | Línea base actual | Branch desactualizada | Git ancestry validation | P-Compensatorio/D | Check run | No sustituye política de actualización |
| GE-010 | PR asociado a push | Cambio fuera del flujo | GitHub API | D | Push workflow | No revierte el cambio |
| GE-011 | Residual risk | Falsa sensación de protección | Política explícita | G | Documento controlado | Depende de lectura/revisión |
| GE-012 | Métricas | Falta de visibilidad | Resultados de workflows | M | Run history / dashboard futuro | Métricas iniciales |

## 3. Matriz de Quality Validation

| ID | Control | Riesgo controlado | Mecanismo | Naturaleza | Evidencia | Limitación |
|---|---|---|---|---|---|---|
| QV-001 | Markdown no vacío | Artefacto documental vacío | Shell | P-Compensatorio/D | Check run | No evalúa semántica |
| QV-002 | H1 inicial | Estructura documental inconsistente | Shell | P-Compensatorio/D | Check run | No sustituye revisión editorial |
| QV-003 | Sin trailing whitespace fuera de Markdown | Ruido técnico en artefactos de configuración/código | Shell | P-Compensatorio/D | Check run | Markdown puede usar espacios intencionales |
| QV-004 | YAML sintácticamente válido | Configuración inválida | Ruby/Psych | P-Compensatorio/D | Check run | Sintaxis válida no implica semántica correcta |
| QV-005 | Enlaces locales íntegros | Referencias documentales rotas | Python estándar | P-Compensatorio/D | Check run | No valida enlaces externos |
| QV-006 | Artefactos críticos presentes | Pérdida accidental de baseline | Shell | P-Compensatorio/D | Check run | Inventario debe evolucionar con el sistema |

## 4. Criterios de estado

- **PASS:** control ejecutado y conforme.
- **FAIL:** control ejecutado y no conforme.
- **NOT_APPLICABLE:** control no aplica y existe justificación.
- **NOT_IMPLEMENTED:** control definido pero todavía no automatizado.

## 5. Principio de no sobreafirmación

Ningún control detectivo o compensatorio podrá registrarse como protección nativa. La evidencia debe identificar explícitamente la naturaleza del control.

Un `Quality Validation PASS` demuestra únicamente conformidad con los controles automatizados aplicables de la versión vigente; no certifica la calidad integral del producto.

## 6. Relación con Quality Gates

Quality Validation aporta evidencia técnica a los Quality Gates, pero no sustituye su evaluación. Un gate puede requerir evidencia adicional de requisitos, arquitectura, seguridad, validación, operación o aceptación.

## 7. Evolución

La matriz se ampliará cuando se incorporen código, pruebas, infraestructura y requisitos verificables. Podrán añadirse controles de pruebas, análisis estático, cobertura justificada, complejidad, rendimiento, resiliencia, contratos e integridad de interfaces.

Security Validation, Evidence Validation, Requirements Governance, Architecture Governance, Data Governance y AI Governance permanecerán como capacidades diferenciadas y se integrarán mediante cambios controlados.
