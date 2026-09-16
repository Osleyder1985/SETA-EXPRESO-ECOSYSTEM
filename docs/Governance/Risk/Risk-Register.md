# Registro de Riesgos

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Fuente estructurada:** `Risk-Register.yml`  
**Última actualización:** 2026-09-15

---

## Resumen

| ID | Categoría | Riesgo | P | I | Exposición | Residual | Estado | Owner | Revisión |
|---|---|---|---:|---:|---:|---:|---|---|---|
| RISK-001 | Governance | Ausencia de enforcement nativo de branch protection/rulesets | 3 | 4 | 12 | 8 | Monitoring | Governance | 2026-10-15 |

## RISK-001

**Riesgo:** Ausencia de enforcement nativo de branch protection/rulesets bajo repositorio privado y GitHub Free.

**Causa:** Limitación de capacidades de la plataforma bajo las condiciones actuales del proyecto.

**Evento:** Un actor con permisos de escritura modifica `main` sin pasar por el flujo Issue → Branch → PR → Merge.

**Consecuencia:** La línea base puede recibir cambios no controlados y perder parte de la trazabilidad procedimental esperada.

**Valoración inherente:**

- Probability: **3/5**
- Impact: **4/5**
- Exposure: **12/25 — Alta**

**Owner:** Governance

**Tratamiento:** Reduce

**Mitigación:** Controles compensatorios de Governance, Quality, Security y Evidence Validation; detección post-merge; política explícita de cambio controlado; evidencia trazable.

**Contingencia:** Analizar el cambio detectado, determinar impacto, registrar la desviación y ejecutar corrección controlada mediante Issue → Branch → PR.

**Trigger:** Push a `main` sin Pull Request asociado o evidencia de actualización fuera del flujo controlado.

**Riesgo residual:**

- Probability: **2/5**
- Impact: **4/5**
- Residual Exposure: **8/25 — Moderada**

**Estado:** `monitoring`

**Review Date:** `2026-10-15`

**Evidencia:**

- `Docs/Governance/07-Main-Protection-Strategy.md`
- `Docs/Governance/10-Governance-Enforcement-Architecture.md`
- `Docs/Governance/11-Governance-Control-Matrix.md`
- `Docs/Governance/15-G0-Governance-Readiness-Assessment.md`

> Esta valoración es una priorización cualitativa estructurada. No representa una probabilidad estadística ni una valoración monetaria.
