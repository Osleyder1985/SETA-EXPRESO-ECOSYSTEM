# Arquitectura de Governance Enforcement

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Propuesta para aprobación mediante PR asociado al Issue #13  
**Idioma documental:** Español  
**Fecha:** 2026-09-15  
**Issue:** #13

---

## 1. Propósito

Definir una arquitectura de controles que reduzca la dependencia del comportamiento humano para preservar la integridad de `main`, maximice las capacidades gratuitas disponibles y mantenga una separación verificable entre política, enforcement técnico, detección y evidencia.

La arquitectura no afirma capacidades de GitHub que no estén realmente disponibles. Mientras el repositorio sea privado bajo GitHub Free, los controles nativos de protección de ramas/rulesets no se consideran disponibles para este propósito. GitHub documenta que branch protection está disponible en repositorios públicos con Free y en repositorios privados con Pro/Team/Enterprise; rulesets siguen una disponibilidad equivalente para repositorios privados. Esta restricción queda registrada como riesgo residual, no como una razón para abandonar el control de ingeniería.

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
Issue
   │
   ▼
Work Branch
   │
   ├── branch identity
   ├── Issue traceability
   └── controlled scope
   │
   ▼
Pull Request
   │
   ├── title validation
   ├── label validation
   ├── Issue reference validation
   ├── impact analysis validation
   ├── integration-status validation
   ├── source-branch validation
   ├── baseline validation
   └── changed-artifact checks
   │
   ▼
Governance Validation
   │
   ├── PASS → continue
   └── FAIL → merge must not be considered compliant
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
   ├── push detection
   ├── PR association verification
   ├── baseline integrity detection
   └── evidence
   │
   ▼
Governance Metrics
```

En el estado actual, `Governance Validation` es ejecutable y `main` dispone de detección posterior al cambio. La capacidad de impedir técnicamente el merge o push sin branch protection/rulesets sigue siendo una limitación de plataforma.

## 4. Niveles de control

| Nivel | Definición | Ejemplo | Estado |
|---|---|---|---|
| P-Nativo | La plataforma impide la operación | Branch protection | No disponible bajo restricción actual |
| P-Compensatorio | Automatización que bloquea el paso lógico del proceso, pero no la capacidad de GitHub de escribir | Validación obligatoria del pipeline/proceso | Parcial |
| D-Detectivo | Detecta incumplimiento después o durante la operación | Push a `main` sin PR asociado | Implementable |
| G-Gobernanza | Política, evidencia y responsabilidad | Issue + PR + revisión | Vigente |
| M-Métrico | Convierte controles en indicadores | % PR conformes | Implementable |

La etiqueta `P-Compensatorio` nunca debe describirse como equivalente a branch protection nativa.

## 5. Controles obligatorios de Pull Request

Todo PR nuevo destinado a `main` deberá poder verificarse automáticamente, como mínimo, respecto a:

1. branch origen distinta de `main`;
2. título conforme a `Módulo/Archivo: Acción a realizar.`;
3. al menos un label pertinente;
4. referencia a Issue (`Issue #`, `Closes #`, `Fixes #` o `Resolves #`);
5. sección `Análisis de impacto`;
6. exactamente un estado formal de integración;
7. branch de trabajo identificable y asociada al Issue;
8. línea base documental mínima presente;
9. branch de trabajo basada en una línea base alcanzable de `main`, salvo excepción explícita documentada;
10. ausencia de artefactos de gobernanza críticos eliminados sin justificación trazable.

El workflow deberá producir mensajes de error específicos y accionables.

## 6. Controles sobre `main`

Ante cada `push` a `main`, la automatización deberá:

1. registrar SHA, actor y mensaje;
2. identificar si el commit está asociado a uno o más Pull Requests mediante la API de GitHub cuando sea posible;
3. distinguir entre evidencia de integración mediante PR y una actualización sin PR asociado;
4. marcar como `SUSPICIOUS_DIRECT_UPDATE` cualquier actualización de `main` que no pueda asociarse a un PR integrado;
5. conservar el resultado como evidencia detectiva;
6. no afirmar que la automatización revirtió o impidió el cambio.

Un resultado `SUSPICIOUS_DIRECT_UPDATE` no significa automáticamente que exista una violación: debe permitir analizar casos como commits de bootstrap, automatizaciones legítimas o eventos de plataforma. La clasificación final será trazable.

## 7. Integridad de la gobernanza

Los siguientes artefactos constituyen una línea base mínima:

- `00-Software-Lifecycle-Master.md`
- `03-Artifacts-And-Evidence.md`
- `04-Quality-Gates.md`
- `05-Repository-Naming-Convention.md`
- `06-Change-Control-Workflow.md`
- `07-Main-Protection-Strategy.md`
- `08-Software-Roadmap.md`
- `09-Issue-And-Pull-Request-Labeling-Policy.md`
- `10-Governance-Enforcement-Architecture.md`
- `.github/workflows/governance-validation.yml`

La ausencia de cualquiera de estos artefactos en una ejecución de gobernanza debe provocar fallo del control de baseline.

## 8. Matriz de control

| Control | Riesgo | Mecanismo | Evidencia | Limitación |
|---|---|---|---|---|
| PR con Issue | Cambio no trazable | Workflow | Check run + PR | No impide push directo |
| Título normalizado | Ambigüedad | Workflow | Check run | No impide modificación manual |
| Label obligatorio | Clasificación deficiente | Workflow | Check run | Label puede ser semánticamente incorrecto |
| Impact analysis | Dependencias olvidadas | Workflow + revisión | PR | Texto puede ser insuficiente |
| Estado único | Merge ambiguo | Workflow | Check run | No obliga técnicamente el merge |
| Branch distinta de main | Trabajo en baseline | Workflow | Check run | No bloquea push directo |
| Baseline presente | Gobierno degradado | Workflow | Check run | No protege configuración fuera del repo |
| Push asociado a PR | Cambio fuera del flujo | API + workflow | Run de `push` | Detectivo |
| Residual risk documentado | Falsa sensación de seguridad | Documentación | Estrategia | Depende de revisión |

## 9. Residual risk

El riesgo residual principal sigue siendo que un actor con permisos de escritura modifique `main` sin pasar por el mecanismo de Pull Request o fuerce una actualización. La arquitectura reduce la probabilidad de incumplimiento accidental y mejora la detección, pero no puede convertir GitHub Actions en una barrera de escritura equivalente a branch protection.

La aceptación del riesgo es temporal y está condicionada a:

- repositorio privado;
- GitHub Free;
- ausencia de plan de pago;
- mantenimiento de controles compensatorios;
- revisión periódica de la capacidad de la plataforma.

## 10. Métricas iniciales

La arquitectura deberá permitir medir progresivamente:

- `% PR con Issue válida`;
- `% PR con análisis de impacto`;
- `% PR con labels`;
- `% PR con título conforme`;
- `% PR con estado formal único`;
- `% pushes a main asociados a PR`;
- `número de actualizaciones sospechosas de main`;
- `% ejecuciones de Governance Validation PASS`;
- `número de fallos de gobernanza por causa`.

Estas métricas serán precursoras del futuro Governance Dashboard.

## 11. Evolución hacia enforcement nativo

Cuando exista capacidad compatible de GitHub, la arquitectura deberá conservar sus validaciones aunque se active branch protection/rulesets. La evolución será:

```text
Compensatorio + Detectivo + Gobernanza
              ↓
       Enforcement nativo
              ↓
Compensatorio + Detectivo + Gobernanza + Preventivo
```

Los controles nativos previstos incluyen Pull Request obligatorio, approvals, status checks, resolución de conversaciones, bloqueo de force push, restricciones de eliminación y otras reglas apropiadas al riesgo.

## 12. Criterio de verdad

Nunca se utilizará la expresión `main protegida técnicamente` para describir esta arquitectura mientras la plataforma no esté efectivamente impidiendo las operaciones correspondientes.

La afirmación correcta durante la restricción actual es:

> `main` está gobernada mediante controles procedimentales, automatizados y detectivos, con riesgo residual documentado por ausencia de enforcement nativo.

## 13. Evidencia de implementación

La implementación de esta arquitectura deberá conservar:

- Issue que origina el cambio;
- branch de trabajo;
- PR asociado;
- workflow runs;
- commits;
- análisis de impacto;
- resultado de validaciones;
- estado final de integración;
- documentación actualizada.

## 14. Relación con la gobernanza existente

Esta arquitectura complementa:

- `06-Change-Control-Workflow.md`;
- `07-Main-Protection-Strategy.md`;
- `08-Software-Roadmap.md`;
- `09-Issue-And-Pull-Request-Labeling-Policy.md`.

No sustituye el ciclo de vida maestro ni los Quality Gates.
