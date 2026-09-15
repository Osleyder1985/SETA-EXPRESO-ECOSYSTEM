# Matriz de controles de Governance, Quality, Security y Evidence Enforcement

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.4.0  
**Estado:** Matriz controlada en evolución  
**Fecha:** 2026-09-15  
**Issues relacionados:** #13, #20, #22, #23

---

## 1. Propósito

Convertir las capas de Governance Enforcement, Quality Validation, Security Validation y Evidence Validation en una matriz operacional que permita saber qué se controla, por qué, cómo, qué evidencia se obtiene y cuál es la limitación residual.

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

## 5. Matriz de Evidence Validation

| ID | Control | Riesgo controlado | Mecanismo | Naturaleza | Evidencia | Limitación |
|---|---|---|---|---|---|---|
| EV-001 | Estructura mínima de evidencia en PR | Cambio sin explicación verificable | Secciones obligatorias | P-Compensatorio/D | Check run + PR | No valida semántica |
| EV-002 | Relación Issue–PR | Unidad de cambio no trazable | Metadata + cuerpo del PR | P-Compensatorio/D | Check run + PR | No demuestra legitimidad del actor |
| EV-003 | Identidad del commit evaluado | Evidencia asociada a versión incorrecta | Comparación SHA/HEAD | P-Compensatorio/D | Check run | No garantiza permanencia histórica |
| EV-004 | Declaración de validaciones | Evidencia incompleta | Sección de evidencia esperada | P-Compensatorio/D | Check run + PR | Declaración no sustituye ejecución |
| EV-005 | Baseline de evidencia presente | Pérdida de infraestructura documental | Existencia de artefactos | P-Compensatorio/D | Check run | No valida suficiencia semántica |
| EV-006 | Resultados de validaciones previas | Evidencia CI incompleta | Consulta de workflow runs | D | Workflow runs | Planificado |
| EV-007 | Integridad histórica | Alteración/pérdida de evidencia | Hashes/procedencia | D | Evidencia versionada | NOT_IMPLEMENTED |
| EV-008 | Evidencia de pruebas | Cambio sin prueba apropiada | Integración testing | D | Test reports | NOT_APPLICABLE al baseline actual |
| EV-009 | Evidencia de release/despliegue | Cambio productivo no trazable | Releases/deployments | D | Registros | NOT_APPLICABLE al baseline actual |

## 6. Criterios de estado

- **PASS:** control ejecutado y conforme.
- **FAIL:** control ejecutado y no conforme.
- **NOT_APPLICABLE:** no aplica y existe justificación.
- **NOT_IMPLEMENTED:** definido pero todavía no automatizado.

## 7. Principio de no sobreafirmación

Ningún control detectivo o compensatorio podrá registrarse como protección nativa. PASS demuestra únicamente conformidad con los controles automatizados aplicables de la versión vigente.

## 8. Relación con Quality Gates

Las cuatro capas aportan evidencia técnica a los Quality Gates, pero no sustituyen su evaluación. Un gate puede requerir evidencia adicional de requisitos, arquitectura, seguridad, validación, operación o aceptación.

## 9. Evolución

La matriz se ampliará cuando se incorporen código, pruebas, infraestructura, datos y releases. Podrán añadirse SAST, SCA, DAST, secrets scanning especializado, SBOM, IaC, contenedores, supply chain, procedencia, reproducibilidad y evidencia científica.
