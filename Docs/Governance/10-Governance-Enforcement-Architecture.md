# Arquitectura de Governance Enforcement

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.2.0  
**Estado:** Arquitectura de enforcement en evolución  
**Idioma documental:** Español  
**Fecha:** 2026-09-15  
**Issues relacionados:** #13, #20

---

## 1. Propósito

Definir una arquitectura de controles que reduzca la dependencia del comportamiento humano para preservar la integridad de `main`, maximice las capacidades gratuitas disponibles y mantenga una separación verificable entre política, enforcement técnico, detección, calidad, seguridad y evidencia.

La arquitectura no afirma capacidades de GitHub que no estén realmente disponibles. Mientras el repositorio sea privado bajo GitHub Free, los controles nativos de protección de ramas/rulesets no se consideran disponibles para este propósito. Esta restricción queda registrada como riesgo residual.

## 2. Principio rector

```text
POLÍTICA
   ↓
CONTROL AUTOMATIZABLE
   ↓
VALIDACIÓN
   ↓
EVIDENCIA
   ↓
MÉTRICA
   ↓
RESPUESTA
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

En el estado actual, Governance Validation y Quality Validation son ejecutables. Security Validation y Evidence Validation quedan como capas evolutivas. `main` dispone de detección posterior al cambio, pero no de protección nativa bajo las restricciones actuales.

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
9. branch basada en una línea base alcanzable de `main`, salvo excepción explícita;
10. ausencia de artefactos críticos eliminados sin justificación trazable;
11. controles de Quality Validation aplicables satisfechos.

El workflow deberá producir mensajes de error específicos y accionables.

## 6. Quality Validation

Quality Validation es una capa independiente que comprueba propiedades objetivas del repositorio. Su arquitectura, controles y limitaciones se definen en `12-Quality-Validation-Architecture.md`.

Los controles iniciales QV-001..QV-006 cubren Markdown, estructura mínima, whitespace fuera de Markdown, sintaxis YAML, enlaces locales y presencia de artefactos críticos.

Un `QUALITY_VALIDATION=PASS` significa exclusivamente que los controles automatizados aplicables fueron satisfechos. No constituye certificación de calidad integral del producto ni sustituye revisión, pruebas específicas o Quality Gates.

## 7. Controles sobre `main`

Ante cada `push` a `main`, la automatización deberá:

1. registrar SHA, actor y mensaje;
2. identificar si el commit está asociado a uno o más Pull Requests mediante la API de GitHub cuando sea posible;
3. distinguir evidencia de integración mediante PR de una actualización sin PR asociado;
4. marcar como `SUSPICIOUS_DIRECT_UPDATE` cualquier actualización sin PR asociado;
5. conservar el resultado como evidencia detectiva;
6. no afirmar que la automatización revirtió o impidió el cambio.

## 8. Integridad de la gobernanza y calidad

Los siguientes artefactos constituyen la línea base mínima:

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
- `.github/workflows/governance-validation.yml`
- `.github/workflows/quality-validation.yml`

La ausencia de cualquiera de estos artefactos debe provocar fallo del control de baseline correspondiente.

## 9. Matriz resumida

| Control | Riesgo | Mecanismo | Evidencia | Limitación |
|---|---|---|---|---|
| PR con Issue | Cambio no trazable | Workflow | Check run + PR | No impide push directo |
| Impact analysis | Dependencias omitidas | Workflow + revisión | PR | Puede requerir juicio humano |
| Governance baseline | Gobierno degradado | Workflow | Check run | No valida semántica |
| Quality baseline | Degradación técnica básica | Quality workflow | Check run | Cobertura limitada al contexto actual |
| Push asociado a PR | Cambio fuera del flujo | API + workflow | Push run | Detectivo |
| Residual risk | Falsa sensación de seguridad | Documentación | Estrategia | Requiere revisión |

## 10. Residual risk

El riesgo residual principal sigue siendo que un actor con permisos de escritura modifique `main` sin pasar por el mecanismo de Pull Request o fuerce una actualización. La arquitectura reduce la probabilidad de incumplimiento accidental y mejora la detección, pero no puede convertir GitHub Actions en una barrera de escritura equivalente a branch protection.

La aceptación del riesgo es temporal y está condicionada a repositorio privado, GitHub Free, ausencia de plan de pago, mantenimiento de controles compensatorios y revisión periódica de las capacidades de la plataforma.

## 11. Métricas iniciales

La arquitectura deberá permitir medir progresivamente:

- `% PR con Governance Validation PASS`;
- `% PR con Quality Validation PASS`;
- `% PR con Issue válida`;
- `% PR con análisis de impacto`;
- `% pushes a main asociados a PR`;
- `número de actualizaciones sospechosas de main`;
- `número de fallos de calidad por control`.

## 12. Evolución hacia enforcement nativo

Cuando exista capacidad compatible de GitHub, la arquitectura deberá conservar sus validaciones aunque se active branch protection/rulesets.

```text
Compensatorio + Detectivo + Gobernanza
              ↓
       Enforcement nativo
              ↓
Compensatorio + Detectivo + Gobernanza + Preventivo
```

## 13. Criterio de verdad

Nunca se utilizará la expresión `main protegida técnicamente` para describir esta arquitectura mientras la plataforma no esté efectivamente impidiendo las operaciones correspondientes.

La afirmación correcta durante la restricción actual es:

> `main` está gobernada mediante controles procedimentales, automatizados y detectivos, con riesgo residual documentado por ausencia de enforcement nativo.

## 14. Evidencia de implementación

La implementación debe conservar Issue, branch, PR, workflow runs, commits, análisis de impacto, resultados de validación, estado final de integración y documentación actualizada.
