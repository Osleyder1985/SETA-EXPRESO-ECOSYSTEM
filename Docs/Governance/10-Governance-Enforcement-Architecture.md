# Arquitectura de Governance Enforcement

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.5.0  
**Estado:** Arquitectura de enforcement en evolución  
**Idioma documental:** Español  
**Fecha:** 2026-09-15  
**Issues relacionados:** #13, #20, #22, #23, #25

---

## 1. Propósito

Definir una arquitectura de controles que reduzca la dependencia del comportamiento humano para preservar la integridad de `main`, maximice las capacidades gratuitas disponibles y mantenga una separación verificable entre política, enforcement técnico, detección, calidad, seguridad y evidencia.

Mientras el repositorio sea privado bajo GitHub Free, los controles nativos de protección de ramas/rulesets no se consideran disponibles para este propósito. Esta restricción queda registrada como riesgo residual.

## 2. Principio rector

```text
POLÍTICA → CONTROL AUTOMATIZABLE → VALIDACIÓN → EVIDENCIA → MÉTRICA → RESPUESTA
```

La automatización no debe confundirse con protección nativa. Un workflow puede fallar, detectar, registrar o notificar; solo una capacidad de plataforma que impida efectivamente una operación constituye enforcement técnico preventivo.

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
```

Governance, Quality, Security y Evidence Validation son capas independientes. `main` dispone de detección posterior al cambio, pero no de protección nativa bajo las restricciones actuales.

## 4. Niveles de control

| Nivel | Definición | Ejemplo | Estado |
|---|---|---|---|
| P-Nativo | La plataforma impide la operación | Branch protection | No disponible bajo restricción actual |
| P-Compensatorio | Automatización que bloquea el paso lógico del proceso, pero no la capacidad de GitHub de escribir | Validaciones de PR | Parcial |
| D-Detectivo | Detecta incumplimiento después o durante la operación | Push a `main` sin PR asociado | Implementado |
| G-Gobernanza | Política, evidencia y responsabilidad | Issue + PR + revisión | Vigente |
| M-Métrico | Convierte controles en indicadores | % PR conformes | En evolución |

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
13. controles de Evidence Validation aplicables satisfechos.

## 6. Quality, Security y Evidence Validation

Quality Validation comprueba propiedades objetivas de calidad del repositorio. Security Validation comprueba propiedades objetivas de seguridad aplicables. Evidence Validation comprueba que la unidad de cambio conserva evidencia mínima, trazable y verificable.

Ninguna de las tres capas sustituye revisión humana, pruebas específicas, Quality Gates o evaluación integral del producto.

## 7. Evidence Validation

La arquitectura de Evidence Validation se define en `14-Evidence-Validation-Architecture.md`.

Sus controles iniciales EV-001..EV-005 comprueban:

- estructura mínima de evidencia en el PR;
- relación Issue–PR;
- identidad determinista del commit evaluado;
- declaración de Governance, Quality, Security y Evidence Validation;
- presencia de la baseline documental de evidencia.

EV-006..EV-009 quedan planificados o no aplicables hasta disponer de resultados de workflows correlacionables, pruebas, releases, despliegues y necesidades de integridad/procedencia más avanzadas.

## 8. Controles sobre `main`

Ante cada `push` a `main`, la automatización deberá:

1. registrar SHA, actor y mensaje;
2. identificar si el commit está asociado a uno o más Pull Requests mediante la API cuando sea posible;
3. distinguir integración mediante PR de actualización sin PR asociado;
4. marcar como `SUSPICIOUS_DIRECT_UPDATE` cualquier actualización sin PR asociado;
5. conservar el resultado como evidencia detectiva;
6. no afirmar que la automatización revirtió o impidió el cambio.

## 9. Línea base mínima

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
- `.github/workflows/governance-validation.yml`
- `.github/workflows/quality-validation.yml`
- `.github/workflows/security-validation.yml`
- `.github/workflows/evidence-validation.yml`

La ausencia de cualquiera de estos artefactos debe provocar fallo del control de baseline correspondiente.

## 10. Governance Gate Enforcement

Los Quality Gates utilizan controles de readiness específicos definidos en `11-Governance-Control-Matrix.md`. Para G0, los controles `GC-001` a `GC-004` verifican respectivamente la evaluación formal de readiness, el análisis de impacto, la existencia del paquete de evidencia y la explicitación del riesgo residual.

La arquitectura de enforcement no sustituye la decisión del Gate. Su función es garantizar que la decisión se apoye en evidencia localizable y que las limitaciones técnicas no se oculten.

## 11. Residual risk

El riesgo residual principal sigue siendo que un actor con permisos de escritura modifique `main` sin pasar por el mecanismo de Pull Request o fuerce una actualización. La arquitectura reduce la probabilidad de incumplimiento accidental y mejora la detección, pero no convierte GitHub Actions en una barrera de escritura equivalente a branch protection.

La aceptación del riesgo es temporal y está condicionada a repositorio privado, GitHub Free, ausencia de plan de pago, mantenimiento de controles compensatorios y revisión periódica de las capacidades de la plataforma.

## 12. Métricas iniciales

La arquitectura deberá permitir medir progresivamente:

- `% PR con Governance Validation PASS`;
- `% PR con Quality Validation PASS`;
- `% PR con Security Validation PASS`;
- `% PR con Evidence Validation PASS`;
- `% PR con Issue válida`;
- `% PR con análisis de impacto`;
- `% pushes a main asociados a PR`;
- `número de actualizaciones sospechosas de main`;
- `número de fallos por control y capa`.

## 13. Evolución hacia enforcement nativo

Cuando exista capacidad compatible de GitHub, la arquitectura conservará sus validaciones aunque se active branch protection/rulesets.

```text
Compensatorio + Detectivo + Gobernanza
              ↓
       Enforcement nativo
              ↓
Compensatorio + Detectivo + Gobernanza + Preventivo
```

## 14. Criterio de verdad

Nunca se utilizará la expresión `main protegida técnicamente` mientras la plataforma no esté efectivamente impidiendo las operaciones correspondientes.

La afirmación correcta durante la restricción actual es:

> `main` está gobernada mediante controles procedimentales, automatizados y detectivos, con riesgo residual documentado por ausencia de enforcement nativo.

## 15. Evidencia de implementación

La implementación debe conservar Issue, branch, PR, workflow runs, commits, análisis de impacto, resultados de validación, estado final de integración y documentación actualizada.
