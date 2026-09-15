# Estrategia de protección de `main`

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.2.0  
**Estado:** Política vigente  
**Idioma documental:** Español  
**Fecha:** 2026-09-15  
**Issue de origen:** #7  
**Actualización de enforcement:** #13

---

## 1. Propósito

Definir cómo se protege la integridad de `main` mientras el repositorio permanezca privado bajo GitHub Free y no se utilicen planes de pago.

La estrategia distingue explícitamente entre **protección técnica nativa**, **controles compensatorios automatizados**, **detección** y **gobernanza**.

## 2. Restricción conocida

El repositorio es privado y GitHub Free no permite aplicar de forma efectiva las capacidades de branch protection/rulesets requeridas para este nivel de enforcement. Por tanto, no se afirmará que `main` está técnicamente protegida mientras esa capacidad no esté disponible.

La documentación vigente de GitHub establece que branch protection está disponible en repositorios públicos con GitHub Free y en repositorios privados con GitHub Pro, Team o Enterprise; rulesets tienen la misma limitación para repositorios privados. citeturn0search0turn0search1

Esta restricción no modifica la política de ingeniería: los cambios de trabajo deberán continuar siguiendo `Issue → Branch → Pull Request → Review → Merge → main`.

## 3. Objetivos de control

| Objetivo | Control | Naturaleza | Estado |
|---|---|---|---|
| Evitar trabajo en `main` | Política obligatoria de branch de trabajo | G | Vigente |
| Exigir trazabilidad | Issue asociado al cambio | G + D | Automatizado |
| Exigir revisión | Pull Request y revisión | G | Vigente |
| Validar título del PR | Governance Validation | P-Compensatorio + D | Implementado |
| Validar labels | Governance Validation | P-Compensatorio + D | Implementado |
| Validar análisis de impacto | Governance Validation | P-Compensatorio + D | Implementado |
| Validar estado único del PR | Governance Validation | P-Compensatorio + D | Implementado |
| Validar branch distinta de main | Governance Validation | P-Compensatorio + D | Implementado |
| Validar línea base de main | Governance Validation | D | Implementado |
| Validar baseline documental | Governance Validation | D | Implementado |
| Detectar push a main sin PR asociado | Governance Validation | D | Implementado |
| Impedir push directo técnicamente | Branch protection/ruleset | P-Nativo | No disponible bajo restricción actual |
| Impedir force push técnicamente | Branch protection/ruleset | P-Nativo | No disponible bajo restricción actual |
| Exigir approvals técnicamente | Branch protection/ruleset | P-Nativo | No disponible bajo restricción actual |
| Exigir status checks para merge | Branch protection/ruleset | P-Nativo | No disponible bajo restricción actual |

## 4. Governance Enforcement

La arquitectura detallada está definida en `10-Governance-Enforcement-Architecture.md`.

La cadena objetivo es:

```text
Developer
   ↓
Issue
   ↓
Branch
   ↓
Pull Request
   ↓
Governance Validation
   ↓
Quality Validation
   ↓
Security Validation
   ↓
Evidence Validation
   ↓
Review / Approval
   ↓
Merge
   ↓
main
   ↓
Post-Merge Detection
   ↓
Evidence + Metrics
```

La automatización actual cubre la capa de Governance Validation y la detección post-merge. Quality, Security y Evidence Validation se integrarán progresivamente como controles específicos del ciclo de vida.

## 5. Controles compensatorios

### 5.1 Validación de Pull Request

`Governance Validation` comprueba automáticamente:

- branch origen distinta de `main`;
- título conforme a `Módulo/Archivo: Acción a realizar.`;
- al menos un label;
- referencia a Issue;
- análisis de impacto;
- exactamente un estado formal de integración;
- línea base de `main` alcanzable por la branch;
- presencia de la baseline documental de gobernanza.

Estos controles reducen incumplimientos accidentales y producen evidencia. **No sustituyen una regla nativa que impida el merge.**

### 5.2 Detección de actualizaciones de `main`

Ante cada `push` a `main`, el workflow consulta la API de GitHub para comprobar si el commit tiene Pull Request asociado.

Si no encuentra asociación, registra `SUSPICIOUS_DIRECT_UPDATE` y falla la ejecución como control detectivo.

El fallo no revierte ni impide el cambio ya ocurrido. El evento requiere análisis posterior y clasificación.

### 5.3 Baseline de gobernanza

El workflow comprueba la presencia de los artefactos críticos definidos en `10-Governance-Enforcement-Architecture.md`.

Una desaparición accidental o modificación estructural no acompañada por la evidencia correspondiente deberá ser investigada como incumplimiento de gobernanza.

## 6. Modelo de garantía

- **P-Nativo:** la plataforma impide la operación.
- **P-Compensatorio:** la automatización bloquea el paso lógico de validación, pero no puede impedir una escritura que GitHub permita.
- **D-Detectivo:** identifica o registra incumplimientos.
- **G-Gobernanza:** política, responsabilidades, revisión y evidencia.
- **M-Métrico:** convierte el cumplimiento en indicadores.

Actualmente `main` dispone de **G + P-Compensatorio + D + M en construcción**. El nivel P-Nativo permanece no disponible bajo la restricción actual.

## 7. Riesgo residual

El principal riesgo residual sigue siendo que un actor con permisos de escritura pueda modificar `main` directamente o realizar un force push.

La estrategia reduce la probabilidad de incumplimiento accidental y mejora su detección, pero **no proporciona equivalencia funcional con branch protection nativa**.

El riesgo se acepta temporalmente bajo estas condiciones:

- repositorio privado;
- GitHub Free;
- ausencia de plan de pago;
- mantenimiento de controles compensatorios;
- revisión periódica de capacidades de GitHub;
- conservación de evidencia de los eventos sobre `main`.

## 8. Métricas de enforcement

Se comenzarán a medir progresivamente:

- `% PR con Issue válida`;
- `% PR con título conforme`;
- `% PR con labels`;
- `% PR con análisis de impacto`;
- `% PR con estado formal único`;
- `% PR con baseline válida`;
- `% actualizaciones de main asociadas a PR`;
- `número de SUSPICIOUS_DIRECT_UPDATE`;
- `% ejecuciones Governance Validation PASS`;
- `número de fallos por regla`.

## 9. Evolución prevista

Cuando exista capacidad compatible de branch protection/rulesets, se deberán activar progresivamente:

1. Pull Request obligatorio.
2. Aprobación requerida.
3. Resolución de conversaciones.
4. Status checks obligatorios.
5. Bloqueo de force push.
6. Restricción de eliminación.
7. Reglas de seguridad y calidad apropiadas al riesgo.
8. Aplicación de las reglas también a administradores cuando sea compatible.

La activación deberá realizarse mediante una unidad de cambio controlada y análisis de impacto.

## 10. Relación con otras políticas

Esta estrategia complementa:

- `00-Software-Lifecycle-Master.md`;
- `03-Artifacts-And-Evidence.md`;
- `04-Quality-Gates.md`;
- `06-Change-Control-Workflow.md`;
- `08-Software-Roadmap.md`;
- `09-Issue-And-Pull-Request-Labeling-Policy.md`;
- `10-Governance-Enforcement-Architecture.md`.

## 11. Criterio de verdad operacional

El proyecto no considerará que `main` está protegida técnicamente por el simple hecho de existir una política, un workflow o un check.

La afirmación **“`main` está técnicamente protegida”** solo podrá utilizarse cuando una capacidad efectiva de la plataforma haya sido verificada.

La afirmación operacional válida mientras dure la restricción es:

> `main` está gobernada mediante controles procedimentales, automatizados y detectivos, con riesgo residual documentado por ausencia de enforcement nativo.
