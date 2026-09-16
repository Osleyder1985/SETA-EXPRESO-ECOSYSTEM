# Matriz de controles de Governance, Quality, Security y Evidence Enforcement

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.7.0  
**Estado:** Matriz controlada en evolución  
**Fecha:** 2026-09-15  
**Issues relacionados:** #13, #20, #22, #23, #25, #33, #35

---

## 1. Propósito

Convertir las capas de Governance Enforcement, Decision Governance, Quality Validation, Security Validation y Evidence Validation, junto con los controles de readiness de los Quality Gates y la nueva capacidad de Metrics Governance, en una matriz operacional que permita saber qué se controla, por qué, cómo, qué evidencia se obtiene y cuál es la limitación residual.

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
| GE-012 | Métricas | Falta de visibilidad | Resultados de workflows | M | Run history / dashboard | Métricas iniciales |

## 3. Matriz de Governance Gate Controls

Los controles GC gobiernan la preparación y decisión de un Quality Gate. Son distintos de GE: GE controla la integridad del flujo de cambios; GC controla que exista evidencia suficiente para decidir el avance de una fase.

| ID | Control | Riesgo controlado | Mecanismo | Naturaleza | Evidencia | Limitación |
|---|---|---|---|---|---|---|
| GC-001 | G0 Governance Readiness Assessment | Avanzar de fase sin evaluar objetivamente la baseline de gobernanza | Evaluación formal del Gate G0 | G/D | `15-G0-Governance-Readiness-Assessment.md` | La evaluación requiere revisión de criterios y evidencia |
| GC-002 | G0 Impact Analysis | Introducir el cierre de G0 sin actualizar artefactos dependientes | Análisis formal de impacto | G/D | `16-G0-Impact-Analysis.md` | Puede requerir juicio de ingeniería sobre dependencias |
| GC-003 | G0 Evidence Package | Decisión de gate sin evidencia trazable | Consolidación y revisión de evidencia | G/D | Assessment + Impact Analysis + validaciones + PR | La suficiencia semántica final requiere revisión |
| GC-004 | Residual Risk Acceptance | Ocultar limitaciones técnicas o sobreafirmar controles | Registro explícito de riesgos residuales | G | Governance baseline + Gate decision | La aceptación requiere autoridad responsable |

## 4. Matriz de Decision Governance

Los controles DG gobiernan la creación, contenido, trazabilidad y evolución de los Architecture Decision Records (ADR) y Engineering Decision Records (EDR). Su detalle normativo-operacional se desarrolla en `20-Decision-Governance-Control-Matrix.md`.

| ID | Control | Riesgo controlado | Mecanismo | Naturaleza | Evidencia | Limitación |
|---|---|---|---|---|---|---|
| DG-001 | Decision Record estructurado | Decisiones sin razonamiento verificable | ADR/EDR template | G/D | Decision Record | Revisión semántica humana |
| DG-002 | Identidad estable | Pérdida de trazabilidad histórica | ADR-NNN / EDR-NNN | G/D | Índice + archivo | Integridad automática aún planificada |
| DG-003 | Contexto | Decisión descontextualizada | Campo obligatorio | G | Decision Record | Calidad depende de la información disponible |
| DG-004 | Alternativas | Decisión sin comparación | Campo obligatorio | G | Decision Record | No obliga a una cantidad fija de alternativas |
| DG-005 | Criterios | Selección no justificable | Criterios explícitos | G | Decision Record | Los criterios requieren juicio de ingeniería |
| DG-006 | Trade-offs | Costes y compromisos ocultos | Sección obligatoria | G | Decision Record | Evaluación cualitativa puede requerir revisión |
| DG-007 | Consecuencias | Impactos futuros no registrados | Sección obligatoria | G | Decision Record | No predice todos los efectos |
| DG-008 | Riesgos | Decisión desvinculada de Risk Management | Referencia a Risk Register | G | Decision Record + Risk Register | Correlación automática futura |
| DG-009 | Evidencia | Decisión sin base objetiva | Referencias controladas | G/D | Decision Record | Evidencia externa puede requerir metadatos |
| DG-010 | Status | Estado ambiguo | Estados controlados | G/D | Decision Record | Requiere actualización disciplinada |
| DG-011 | Supersession | Historia de decisiones destruida | `Supersedes` / `Superseded by` | G | Cadena de registros | Validación automática futura |
| DG-012 | Trazabilidad | Decisión aislada | Requisitos/Issues/PR/Gates | G | Enlaces y referencias | No toda relación es automática |
| DG-013 | Approval | Decisión material sin autoridad | Sección de aprobación | G | Decision Record | Autoridad depende del contexto |
| DG-014 | Premature Decision Control | Decisiones técnicas inventadas antes del contexto | Criterio de materialidad + fases | G | Issue/Decision Index | Requiere criterio humano |
| DG-015 | Index Integrity | Índice inconsistente | Validación de índice futura | D | Index + workflow | No implementado |
| DG-016 | Schema Validation | Campos obligatorios ausentes | Linter/schema futuro | P-Compensatorio/D | Check run | No implementado |
| DG-017 | Link Validation | Referencias rotas | Validación futura | P-Compensatorio/D | Check run | No implementado |
| DG-018 | Supersession Consistency | Cadena histórica inconsistente | Validación futura | D | Check run | No implementado |
| DG-019 | Decision Metrics | Falta de visibilidad sobre decisiones | Métricas futuras | M | Dashboard | No implementado |

## 5. Matriz de Metrics Governance

Los controles EM gobiernan la definición, medición, interpretación y evolución de las métricas de ingeniería. Su detalle se desarrolla en `22-Engineering-Metrics-Control-Matrix.md`.

| ID | Control | Riesgo controlado | Mecanismo | Naturaleza | Evidencia | Limitación |
|---|---|---|---|---|---|---|
| EM-001 | Política de métricas | Medición sin gobierno | `21-Engineering-Metrics-Governance.md` | G | Política controlada | Capacidad documental inicial |
| EM-002 | Identidad estable | Métricas no trazables | Metric ID | G/D | Catálogo | Validación automática futura |
| EM-003 | Definición operacional | Ambigüedad semántica | Definición controlada | G | Catálogo | Requiere contexto operacional |
| EM-004 | Fórmula | Resultados no reproducibles | Fórmula explícita | G/D | Catálogo/cálculo | Algunas métricas requieren método específico |
| EM-005 | Población de cálculo | Denominadores inconsistentes | Numerador/denominador/población | G | Catálogo | Datos reales aún no disponibles |
| EM-006 | Fuente | Métrica sin origen verificable | Source | G/D | Catálogo/evidencia | Fuentes operacionales futuras |
| EM-007 | Recolección | Datos no reproducibles | Collection Method | G/D | Catálogo/registros | Automatización futura |
| EM-008 | Frecuencia | Falta de frescura conocida | Frequency | G | Catálogo/snapshots | Sin snapshots operacionales todavía |
| EM-009 | Owner | Métrica sin responsable | Owner | G | Catálogo | Requiere asignación operacional futura |
| EM-010 | Baseline | Interpretación sin punto de referencia | Baseline | M | Snapshot | TBD hasta disponer de datos |
| EM-011 | Target | Objetivo inventado o no aprobado | Target | G/M | Política/catálogo | TBD cuando no exista decisión formal |
| EM-012 | Thresholds | Alarmas sin contexto | Thresholds | G/M | Política/catálogo | No deben inventarse |
| EM-013 | Availability Status | Datos ausentes interpretados como cero | Estado definido/provisional/bloqueado | M | Catálogo/dashboard | Requiere fuentes reales |
| EM-014 | Limitations | Falsa precisión | Limitations | G | Catálogo/dashboard | Revisión humana |
| EM-015 | Traceability | Métrica aislada | Metric → Source → Calculation → Evidence | G/M | Catálogo/evidencia | Correlación automática futura |
| EM-016 | Risk Relation | Métricas desconectadas del riesgo | Risk linkage | G/M | Risk Register | Automatización futura |
| EM-017 | Decision Relation | Métricas sin uso decisional | Decision linkage | G/M | Decision Records | Automatización futura |
| EM-018 | Dashboard Derivation | Vista tomada como fuente de verdad | Dashboard derivado | G/D | Catalog + dashboard | Generación reproducible futura |
| EM-019 | Historical Integrity | Cambios semánticos que reescriben historia | Snapshots/versionado | D/M | Historial | Automatización futura |
| EM-020 | Automatic Extraction | Datos manuales no sostenibles | Integración de fuentes | D | Workflow/collector futuro | No implementado |
| EM-021 | Automatic Calculation | Error manual de cálculo | Motor reproducible | D | Workflow/artifact futuro | No implementado |
| EM-022 | Catalog Validation | Catálogo inconsistente | Schema/linter | P-Compensatorio/D | Check run futuro | No implementado |
| EM-023 | Trend Detection | Cambios relevantes no detectados | Series temporales | D/M | Snapshot history futuro | No implementado |
| EM-024 | Actionable Alerts | Indicador sin respuesta | Alertas + owner/action | D/M | Alert record futuro | No implementado |
| EM-025 | Correlation | Métricas interpretadas aisladamente | Correlación multidimensional | M | Analysis future | No implementado |
| EM-026 | Governance Health | Falta de visión global | Health indicators | M | Dashboard futuro | No implementado |
| EM-027 | Periodic Review | Métricas obsoletas | Revisión controlada | G/M | Review record | Periodicidad operacional futura |
| EM-028 | Metric Change Control | Deriva semántica no controlada | Change Control + Impact Analysis | G/D | Issue/PR | Depende de disciplina y validación |

## 6. Matriz de Quality Validation

| ID | Control | Riesgo controlado | Mecanismo | Naturaleza | Evidencia | Limitación |
|---|---|---|---|---|---|---|
| QV-001 | Markdown no vacío | Artefacto documental vacío | Shell | P-Compensatorio/D | Check run | No evalúa semántica |
| QV-002 | H1 inicial | Estructura documental inconsistente | Shell | P-Compensatorio/D | Check run | No sustituye revisión editorial |
| QV-003 | Sin trailing whitespace fuera de Markdown | Ruido técnico en artefactos de configuración/código | Shell | P-Compensatorio/D | Check run | Markdown puede usar espacios intencionales |
| QV-004 | YAML sintácticamente válido | Configuración inválida | Ruby/Psych | P-Compensatorio/D | Check run | Sintaxis válida no implica semántica correcta |
| QV-005 | Enlaces locales íntegros | Referencias documentales rotas | Python estándar | P-Compensatorio/D | Check run | No valida enlaces externos |
| QV-006 | Artefactos críticos presentes | Pérdida accidental de baseline | Shell | P-Compensatorio/D | Check run | Inventario debe evolucionar con el sistema |

## 7. Matriz de Security Validation

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

## 8. Matriz de Evidence Validation

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

## 9. Criterios de estado

- **PASS:** control ejecutado y conforme.
- **FAIL:** control ejecutado y no conforme.
- **NOT_APPLICABLE:** no aplica y existe justificación.
- **NOT_IMPLEMENTED:** definido pero todavía no automatizado.

## 10. Principio de no sobreafirmación

Ningún control detectivo o compensatorio podrá registrarse como protección nativa. PASS demuestra únicamente conformidad con los controles automatizados aplicables de la versión vigente.

## 11. Relación con Quality Gates

Las capas aportan evidencia técnica a los Quality Gates, mientras que los controles GC aportan evidencia específica para la decisión de readiness. Decision Governance aporta evidencia del razonamiento de decisiones materiales cuando corresponda. Metrics Governance aporta indicadores y evidencia cuantitativa cuando existen fuentes operacionales suficientes. Ninguna capa sustituye la evaluación del gate. Un gate puede requerir evidencia adicional de requisitos, arquitectura, seguridad, validación, operación o aceptación.

## 12. Evolución

La matriz se ampliará cuando se incorporen código, pruebas, infraestructura, datos y releases. Podrán añadirse SAST, SCA, DAST, secrets scanning especializado, SBOM, IaC, contenedores, supply chain, procedencia, reproducibilidad, validación automatizada de Decision Records, extracción/cálculo de métricas y métricas de decisión.
