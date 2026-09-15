# Matriz de controles de Governance, Quality y Security Enforcement

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.3.0  
**Estado:** Matriz controlada en evolución  
**Fecha:** 2026-09-15  
**Issues relacionados:** #13, #20, #22

---

## 1. Propósito

Convertir las capas de Governance Enforcement, Quality Validation y Security Validation en una matriz operacional que permita saber qué se controla, por qué, cómo, qué evidencia se obtiene y cuál es la limitación residual.

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

## 4. Matriz de Security Validation

| ID | Control | Riesgo controlado | Mecanismo | Naturaleza | Evidencia | Limitación |
|---|---|---|---|---|---|---|
| SV-001 | Secret Material Scan | Incorporación accidental de claves privadas o credenciales críticas | Patrones deterministas en archivos versionados | P-Compensatorio/D | Check run | No sustituye secret scanning especializado |
| SV-002 | Workflow Least Privilege | Permisos excesivos del `GITHUB_TOKEN` | Validación de `permissions` | P-Compensatorio/D | Check run | No demuestra seguridad completa del workflow |
| SV-003 | Dangerous Workflow Trigger | Ejecución privilegiada de código no confiable | Detección de `pull_request_target` | P-Compensatorio/D | Check run | Casos legítimos requieren excepción formal |
| SV-004 | Security Workflow Integrity | Degradación silenciosa del control de seguridad | Presencia e integridad básica del workflow | P-Compensatorio/D | Check run | No impide modificación directa de `main` |
| SV-005 | Dependency Security | Vulnerabilidades conocidas en dependencias | SCA / dependency review futuro | D | Decisión de aplicabilidad | No aplicable al baseline actual |
| SV-006 | SAST | Vulnerabilidades en código fuente | Analizador estático futuro | D | Decisión de aplicabilidad | No aplicable al baseline actual |
| SV-007 | IaC Security | Configuración insegura de infraestructura | Scanner IaC futuro | D | Decisión de aplicabilidad | No aplicable al baseline actual |
| SV-008 | Container Security | Vulnerabilidades en imágenes | Scanner de contenedores futuro | D | Decisión de aplicabilidad | No aplicable al baseline actual |
| SV-009 | SBOM | Falta de inventario de componentes | Generación SBOM futura | D | Roadmap / decisión | Aún no implementado |

## 5. Criterios de estado

- **PASS:** control ejecutado y conforme.
- **FAIL:** control ejecutado y no conforme.
- **NOT_APPLICABLE:** control no aplica y existe justificación.
- **NOT_IMPLEMENTED:** control definido pero todavía no automatizado.

## 6. Principio de no sobreafirmación

Ningún control detectivo o compensatorio podrá registrarse como protección nativa. La evidencia debe identificar explícitamente la naturaleza del control.

Un `Quality Validation PASS` demuestra únicamente conformidad con los controles automatizados aplicables de la versión vigente; no certifica la calidad integral del producto.

Un `Security Validation PASS` demuestra únicamente conformidad con los controles de seguridad automatizados aplicables de la versión vigente; no certifica seguridad integral ni ausencia de vulnerabilidades.

## 7. Relación con Quality Gates

Quality Validation y Security Validation aportan evidencia técnica a los Quality Gates, pero no sustituyen su evaluación. Un gate puede requerir evidencia adicional de requisitos, arquitectura, seguridad, validación, operación o aceptación.

## 8. Evolución

La matriz se ampliará cuando se incorporen código, pruebas, infraestructura y requisitos verificables. Podrán añadirse controles de pruebas, análisis estático, SCA, secrets scanning especializado, SBOM, IaC, contenedores, DAST, seguridad de API, supply chain y procedencia.
