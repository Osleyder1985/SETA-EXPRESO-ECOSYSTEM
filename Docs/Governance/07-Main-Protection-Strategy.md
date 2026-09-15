# Estrategia de protección de `main`

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Propuesta para aprobación  
**Idioma documental:** Español  
**Fecha:** 2026-09-15  
**Issue:** #7

---

## 1. Propósito

Definir cómo se protegerá la integridad de `main` mientras el repositorio permanezca privado bajo GitHub Free y no se utilicen planes de pago.

La estrategia distingue explícitamente entre **protección técnica nativa**, que impide una operación mediante una capacidad de la plataforma, y **controles compensatorios**, que reducen el riesgo mediante proceso, automatización, evidencia y detección.

## 2. Restricción conocida

El repositorio es privado y GitHub Free no permite aplicar de forma efectiva Rulesets/branch protection a este repositorio. Por tanto, no se afirmará que `main` está técnicamente protegida mientras esa capacidad no esté disponible.

Esta restricción no modifica la política de ingeniería: los cambios de trabajo deberán continuar siguiendo `Issue → Branch → Pull Request → Review → Merge → main`.

## 3. Objetivos de control

| Objetivo | Control | Naturaleza | Estado |
|---|---|---|---|
| Evitar cambios de trabajo en `main` | Política obligatoria de branch de trabajo | Procedimental | Vigente |
| Exigir trazabilidad | Issue asociado al cambio | Procedimental | Vigente |
| Exigir revisión | Pull Request y revisión | Procedimental | Vigente |
| Verificar documentación mínima del PR | GitHub Actions | Automatizado/detectivo | En implementación |
| Detectar pushes sobre `main` | Workflow sobre `push` a `main` | Detectivo | En implementación |
| Impedir force push | Branch protection nativa | Preventivo técnico | No disponible en GitHub Free privado |
| Impedir push directo | Branch protection nativa | Preventivo técnico | No disponible en GitHub Free privado |
| Exigir approvals técnicamente | Ruleset/branch protection | Preventivo técnico | No disponible en GitHub Free privado |
| Exigir status checks para merge | Ruleset/branch protection | Preventivo técnico | No disponible actualmente |

## 4. Controles compensatorios

### 4.1 Control de proceso

Todo trabajo deberá comenzar con un Issue y desarrollarse en una branch distinta de `main`.

El PR deberá documentar qué cambió, por qué, alcance, impacto, artefactos afectados, pruebas/evidencia, relación con el Issue y estado de integración.

### 4.2 Automatización de validaciones

GitHub Actions validará automáticamente condiciones documentales y de gobernanza que puedan comprobarse sin requerir privilegios administrativos de repositorio.

La automatización no debe presentarse como sustituto de branch protection. Su función es detectar incumplimientos, producir evidencia y preparar Quality Gates para una futura protección técnica.

### 4.3 Detección de cambios sobre `main`

Un workflow se ejecutará cuando exista un `push` a `main`. Esto permite conservar evidencia de cualquier actualización de la línea base y detectar situaciones que requieran análisis.

Este control es **detectivo**, no preventivo: no puede impedir por sí mismo que un usuario con permisos de escritura realice un push directo.

### 4.4 Evidencia

Los resultados de los workflows, commits, Issues y Pull Requests deberán conservarse como evidencia de ingeniería cuando sean relevantes para el cambio.

## 5. Modelo de garantía

La estrategia se clasifica en tres niveles:

- **Nivel P — Preventivo:** la plataforma impide la operación no autorizada.
- **Nivel D — Detectivo:** la plataforma identifica o registra el incumplimiento después de ocurrido.
- **Nivel G — Gobernanza:** el proceso obliga organizacionalmente a seguir una práctica y deja evidencia.

Actualmente `main` dispone principalmente de controles **D + G**. El nivel **P** quedará preparado para activarse cuando la plataforma/plan lo permita.

## 6. Riesgo residual

El principal riesgo residual es que un actor con permisos de escritura pueda modificar `main` directamente o realizar un force push, debido a la ausencia de branch protection efectiva.

Este riesgo se acepta temporalmente bajo la restricción económica/tecnológica definida en el Issue #7 y se mitiga mediante controles de proceso, automatización, detección y evidencia.

La aceptación no debe interpretarse como equivalencia funcional con una rama protegida.

## 7. Evolución prevista

Cuando el proyecto disponga de una capacidad compatible de branch protection/rulesets, se deberán activar progresivamente:

1. Pull Request obligatorio.
2. Aprobación requerida.
3. Resolución de conversaciones.
4. Bloqueo de force push.
5. Restricción de eliminación.
6. Status checks obligatorios.
7. Controles de seguridad y calidad aplicables.

La activación deberá realizarse mediante una unidad de cambio controlada y análisis de impacto.

## 8. Relación con otras políticas

Esta estrategia complementa:

- `00-Software-Lifecycle-Master.md`;
- `03-Artifacts-And-Evidence.md`;
- `04-Quality-Gates.md`;
- `06-Change-Control-Workflow.md`.

No sustituye ninguna de ellas.

## 9. Criterio de verdad operacional

El proyecto no considerará que `main` está protegida técnicamente por el simple hecho de existir una política documental o un workflow.

La afirmación **“`main` está técnicamente protegida”** solo podrá utilizarse cuando una capacidad efectiva de la plataforma haya sido verificada.

## 10. Estado

**Pendiente de aprobación mediante Pull Request asociado al Issue #7.**
