# Arquitectura de Governance Enforcement

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.11.0  
**Estado:** Arquitectura de enforcement en evolución  
**Idioma documental:** Español  
**Fecha:** 2026-09-15  
**Issues relacionados:** #13, #20, #22, #23, #25, #33, #35, #37, #80, #82, #152

---

## 1. Propósito

Definir una arquitectura de controles que reduzca la dependencia del comportamiento humano para preservar la integridad de `main`, maximice las capacidades disponibles y mantenga una separación verificable entre política, enforcement técnico, detección, calidad, seguridad, evidencia, Decision Governance, AI Governance y medición.

Mientras el repositorio permanezca privado y no exista una capacidad nativa compatible y verificable, los controles nativos de protección de ramas/rulesets requeridos para este nivel de enforcement se mantienen como objetivo y riesgo residual.

La auditoría de #82 añade una distinción necesaria: el permiso administrativo de la **cuenta GitHub** no equivale a la capacidad administrativa expuesta por la **integración GitHub**. La cuenta `Osleyder1985` tiene permiso `admin` sobre el repositorio, pero la integración no puede consultar el endpoint de Branch Protection ni Rulesets bajo las condiciones actuales.

Esta restricción queda registrada en `53-Main-Branch-Protection-Enforcement.md`.

## 2. Principio rector

```text
POLÍTICA → CONTROL AUTOMATIZABLE → VALIDACIÓN → EVIDENCIA → MÉTRICA → RESPUESTA
```

La automatización no debe confundirse con protección nativa. Un workflow puede fallar, detectar, registrar o notificar; solo una capacidad de plataforma que impida efectivamente una operación constituye enforcement técnico preventivo.

Asimismo, una cuenta con permiso `admin` no debe considerarse evidencia suficiente de enforcement efectivo si la configuración de la plataforma no puede ser verificada.

## 3. Arquitectura objetivo

```text
Developer
   │
   ▼
Issue → Work Branch → Pull Request
                     │
                     ▼
            Governance Validation
                     │
                     ├── Decision Governance
                     │       │
                     │       └── ADR / EDR
                     │
                     ├── AI Governance (when applicable)
                     │       ├── AI Use / Model Inventory
                     │       ├── Risk / Security / Privacy
                     │       └── Evaluation / Human Oversight
                     ▼
             Quality Validation
                     │
                     ▼
             Security Validation
                     │
                     ▼
             Evidence Validation
                     │
                     ▼
               Review / Approval
                     │
                     ▼
                    Merge
                     │
                     ▼
                   main
                     │
             ┌───────┴────────┐
             ▼                ▼
     Post-Merge Detection   Evidence
             │                │
             └───────┬────────┘
                     ▼
                  Metrics
                     │
                     ▼
             Interpretation / Action
```

Governance, Decision Governance, AI Governance, Quality, Security, Evidence Validation y Metrics Governance son capacidades relacionadas pero distinguibles. `main` dispone de detección posterior al cambio, pero la protección nativa no puede declararse efectiva mientras la capacidad no esté disponible y verificada.

## 4. Niveles de control

| Nivel | Definición | Ejemplo | Estado |
|---|---|---|---|
| P-Nativo | La plataforma impide la operación | Branch protection / ruleset | No disponible o no verificable bajo restricción actual |
| P-Compensatorio | Automatización que bloquea el paso lógico del proceso, pero no la capacidad de GitHub de escribir | Validaciones de PR | Parcial |
| D-Detectivo | Detecta incumplimiento después o durante la operación | Push a `main` sin PR asociado | Implementado |
| G-Gobernanza | Política, evidencia y responsabilidad | Issue + PR + revisión | Vigente |
| DG-Decisión | Conserva y controla decisiones materiales | ADR / EDR | Documental operativo inicial |
| AI-Gobernanza | Controla usos, modelos, datos, evaluación e incidentes de IA | AI Inventory + TEVV + Oversight | Documental operativo inicial |
| M-Métrico | Convierte controles y resultados en indicadores reproducibles | Catálogo + dashboard | Documental operativo inicial |

La etiqueta `P-Compensatorio` nunca debe describirse como equivalente a branch protection nativa.

## 5. Controles obligatorios del cambio

Todo PR nuevo destinado a `main` deberá poder verificarse automáticamente, como mínimo, respecto a:

1. branch origen distinta de `main`;
2. título conforme a `Módulo/Archivo: Acción a realizar.`;
3. al menos un label pertinente;
4. referencia a Issue;
5. sección `Análisis de impacto`;
6. exactamente un estado formal de integración;
7. branch de trabajo identificable y asociada al Issue;
8. línea base documental mínima presente;
9. branch basada en una línea base alcanzable de `main`;
10. ausencia de artefactos críticos eliminados sin justificación trazable;
11. controles de Quality Validation aplicables satisfechos;
12. controles de Security Validation aplicables satisfechos;
13. controles de Evidence Validation aplicables satisfechos;
14. Decision Records aplicables identificados y trazables cuando el cambio implique una decisión material;
15. AI Governance aplicable identificada cuando el cambio introduzca o modifique un uso material de IA.

## 6. Quality, Security y Evidence Validation

Quality Validation comprueba propiedades objetivas de calidad del repositorio. Security Validation comprueba propiedades objetivas de seguridad aplicables. Evidence Validation comprueba que la unidad de cambio conserva evidencia mínima, trazable y verificable.

Ninguna de las tres capas sustituye revisión humana, pruebas específicas, Quality Gates, Decision Governance, AI Governance o evaluación integral del producto.

## 7. Decision Governance

Decision Governance constituye una capacidad transversal de control del razonamiento técnico. Su política y matriz de controles se definen en `19-Decision-Governance.md` y `20-Decision-Governance-Control-Matrix.md`.

Los Decision Records no son un sustituto del control de cambios: complementan Issue, análisis de impacto, PR y evidencia, conservando el contexto, las alternativas, los criterios, los trade-offs, las consecuencias, los riesgos y la evidencia que justifican una decisión material.

## 8. AI Governance

AI Governance se define en `23-AI-Governance.md` y `24-AI-Governance-Control-Matrix.md`. Se activa cuando exista uso material de IA y distingue tres dominios:

- `build-time`;
- `product-runtime`;
- `research`.

Los controles incluyen inventario de usos/modelos, procedencia de datos, gobernanza de prompts, evaluación/TEVV, seguridad, privacidad, fairness, factualidad/alucinaciones, human oversight, reproducibilidad e incident management.

La automatización futura de inventarios, evaluación, seguridad, drift y dashboard no se considera implementada hasta disponer de código y evidencia ejecutable.

## 9. Evidence Validation

La arquitectura de Evidence Validation se define en `14-Evidence-Validation-Architecture.md`.

Sus controles iniciales EV-001..EV-005 comprueban estructura mínima de evidencia, relación Issue–PR, identidad determinista del commit evaluado, declaración de validaciones y baseline documental.

## 10. Controles sobre `main`

Ante cada `push` a `main`, el control MC-001 ejecuta un monitor dedicado que registra el evento, actor, fecha/hora del commit y de observación, SHA actual, SHA anterior cuando está disponible, mensaje, estado del push, archivos afectados y Pull Requests asociados mediante GitHub API. La actualización se clasifica como integración esperada únicamente cuando existe al menos un PR fusionado hacia `main`; en caso contrario se clasifica como anomalía y se genera o actualiza un Issue de incidente.

MC-001 conserva evidencia reproducible como artifact del workflow. El artifact contiene un registro JSON estructurado con el contexto del evento, procedencia de la ejecución, clasificación, PRs asociados e Issue de incidente cuando corresponda, además de la relación de archivos afectados. El control no realiza auto-revert. El workflow utiliza `contents: read`, `pull-requests: read` e `issues: write`, limitando los permisos al mínimo necesario para observación, correlación y registro del incidente.

La protección nativa futura deberá complementar, no sustituir, esta detección.

## 11. Perfil de enforcement nativo futuro

Cuando la plataforma lo permita y exista una vía de verificación administrativa compatible, `main` deberá adoptar el perfil definido en `53-Main-Branch-Protection-Enforcement.md`, incluyendo como mínimo:

- Pull Request obligatorio;
- reviews requeridas según SoD/riesgo;
- required status checks de Governance, Quality, Security y Evidence;
- resolución de conversaciones;
- bloqueo de force push;
- bloqueo de eliminación;
- bypasses mínimos, explícitos y documentados;
- protección administrativa cuando sea compatible.

La configuración deberá probarse mediante un PR real y no se considerará efectiva por mera declaración documental ni por el simple hecho de que la cuenta administradora tenga permiso `admin`.

## 12. Línea base mínima

Los siguientes artefactos forman parte de la baseline de enforcement:

- `00-Software-Lifecycle-Master.md`
- `03-Artifacts-And-Evidence.md`
- `04-Quality-Gates.md`
- `05-Repository-Naming-Convention.md`
- `06-Change-Control-Workflow.md`
- `07-Main-Protection-Strategy.md`
- `08-Software-Roadmap.md`
- `09-Issue-And-Pull-Request-Labeling-Policy.md`
- `10-Governance-Enforcement-Architecture.md`
- `11-Governance-Control-Matrix.md`
- `12-Quality-Validation-Architecture.md`
- `13-Security-Validation-Architecture.md`
- `14-Evidence-Validation-Architecture.md`
- `15-G0-Governance-Readiness-Assessment.md`
- `16-G0-Impact-Analysis.md`
- `17-Risk-Management-System.md`
- `18-Risk-Management-Control-Matrix.md`
- `19-Decision-Governance.md`
- `20-Decision-Governance-Control-Matrix.md`
- `21-Engineering-Metrics-Governance.md`
- `22-Engineering-Metrics-Control-Matrix.md`
- `23-AI-Governance.md`
- `24-AI-Governance-Control-Matrix.md`
- `Docs/Architecture/Decision-Records/README.md`
- `Docs/Architecture/Decision-Records/ADR-Template.md`
- `Docs/Architecture/Decision-Records/EDR-Template.md`
- `Docs/Architecture/Decision-Records/Decision-Record-Index.md`
- `.github/workflows/governance-validation.yml`
- `.github/workflows/quality-validation.yml`
- `.github/workflows/security-validation.yml`
- `.github/workflows/evidence-validation.yml`

La ausencia de cualquiera de estos artefactos debe provocar fallo del control de baseline correspondiente cuando el control sea aplicable.

## 13. Governance Gate Enforcement

Los Quality Gates utilizan controles de readiness específicos definidos en `11-Governance-Control-Matrix.md`. Para G0, los controles `GC-001` a `GC-004` verifican respectivamente la evaluación formal de readiness, el análisis de impacto, la existencia del paquete de evidencia y la explicitación del riesgo residual.

## 14. Metrics Governance

Metrics Governance convierte los resultados observables del proceso de ingeniería en indicadores definidos y reproducibles. Su política, catálogo y matriz de controles se encuentran en `21-Engineering-Metrics-Governance.md` y `22-Engineering-Metrics-Control-Matrix.md`.

## 15. Residual risk

El riesgo residual principal sigue siendo que un actor con permisos de escritura modifique `main` sin pasar por el mecanismo de Pull Request o fuerce una actualización. La arquitectura reduce la probabilidad de incumplimiento accidental y mejora la detección, pero no convierte GitHub Actions en una barrera de escritura equivalente a branch protection.

Existe además un riesgo de observabilidad: la integración GitHub actual no puede consultar los endpoints administrativos necesarios para verificar Branch Protection/Rulesets. Este riesgo es distinto de los permisos de la cuenta GitHub y debe mantenerse explícitamente separado en la evidencia.

La aceptación del riesgo es temporal y está condicionada a repositorio privado, configuración/plataforma actual sin enforcement nativo verificable, mantenimiento de controles compensatorios y revisión periódica de las capacidades de la plataforma y de la integración.

## 16. Métricas iniciales

La arquitectura deberá permitir medir progresivamente el cumplimiento de Governance, Quality, Security, Evidence, Decision Governance y AI Governance, además de actualizaciones sospechosas de `main` y disponibilidad/frescura de evidencia.

## 17. Evolución hacia enforcement nativo

Cuando exista capacidad compatible de GitHub y una vía de verificación administrativa, la arquitectura conservará sus validaciones aunque se active branch protection/rulesets.

La activación será una unidad de cambio controlada y deberá conservar Issue, branch, commits, PR, configuración efectiva, pruebas y evidencia de los controles.

## 18. Criterio de verdad

Nunca se utilizará la expresión `main protegida técnicamente` mientras la plataforma no esté efectivamente impidiendo las operaciones correspondientes y esa condición pueda ser verificada.

## 19. Evidencia de implementación

La implementación debe conservar Issue, branch, PR, workflow runs, commits, análisis de impacto, Decision Records cuando correspondan, registros de AI Governance cuando existan usos reales, resultados de validación, métricas y snapshots cuando existan, estado final de integración y documentación actualizada.

Para cambios relacionados con enforcement administrativo deberá conservarse adicionalmente:

- permiso de la cuenta GitHub sobre el repositorio;
- capacidad administrativa efectivamente expuesta por la integración;
- endpoint o mecanismo utilizado para verificar Branch Protection/Rulesets;
- resultado de cualquier intento de lectura que sea rechazado por la integración;
- separación explícita entre **permiso de cuenta** y **capacidad de integración**.
