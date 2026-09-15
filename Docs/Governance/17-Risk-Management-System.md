# Sistema de Gestión de Riesgos

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.1  
**Estado:** Baseline en validación  
**Fecha:** 2026-09-15  
**Issue:** #31

---

## 1. Propósito

Establecer un sistema formal, trazable y continuo para identificar, analizar, evaluar, tratar, aceptar, monitorizar, revisar y cerrar riesgos del Ecosistema.

El sistema se aplica al nivel de sistema/ecosistema y al nivel de software cuando corresponda. Debe integrarse con requisitos, arquitectura, diseño, seguridad, proveedores, operaciones, Quality Gates, cambios y evidencia.

Este documento define el proceso y las reglas. El registro operativo se mantiene separado para permitir evolución de los riesgos sin modificar la definición del proceso.

## 2. Referencias

- ISO 31000:2018 — referencia principal para principios, marco y proceso de gestión del riesgo.
- IEC 31010:2019 — referencia complementaria para técnicas de evaluación de riesgos cuando sean necesarias.
- ISO/IEC/IEEE 15288:2023 — contexto de ciclo de vida del sistema/ecosistema.
- ISO/IEC/IEEE 12207:2026 — contexto de ciclo de vida de software.
- NIST SP 800-218 / SSDF 1.1 — riesgos relacionados con desarrollo seguro, cuando sean aplicables.

ISO 31000:2018 permanece como referencia publicada vigente a la fecha de esta baseline; la revisión de una futura edición deberá activar análisis de impacto antes de sustituir esta referencia.

## 3. Principios operativos

1. **Risk-driven engineering:** la profundidad de ingeniería debe ser proporcional al riesgo.
2. **Explicitness:** los riesgos relevantes no deben permanecer únicamente en conocimiento informal.
3. **Traceability:** cada riesgo relevante debe poder relacionarse con su causa, evento, consecuencia, tratamiento y evidencia.
4. **Ownership:** todo riesgo abierto requiere un responsable.
5. **Inherent vs residual:** el riesgo antes y después del tratamiento deben distinguirse.
6. **Treatment before acceptance:** aceptar un riesgo es una decisión explícita, no la ausencia de tratamiento.
7. **Continuous monitoring:** un riesgo no queda congelado por haber sido registrado.
8. **Evidence by default:** decisiones y cambios relevantes deben conservar evidencia.
9. **No false precision:** una puntuación 1–5 es una escala de priorización, no una probabilidad estadística ni una valoración monetaria.
10. **Context-driven:** las escalas y umbrales deben poder adaptarse cuando exista información real suficiente.

## 4. Ciclo de vida del riesgo

```text
Identificar
    ↓
Analizar
    ↓
Evaluar
    ↓
Tratar
    ↓
Aceptar / Escalar
    ↓
Monitorizar
    ↓
Revisar
    ├──→ Mantener abierto
    ├──→ Re-tratar
    └──→ Cerrar
```

Un riesgo puede volver a una actividad anterior cuando cambien el contexto, las causas, la exposición, los controles o la evidencia.

## 5. Estructura del Risk Register

El registro controlado se encuentra en:

`Docs/Governance/Risk/Risk-Register.yml`

La representación humana está en:

`Docs/Governance/Risk/Risk-Register.md`

Cada riesgo utiliza un identificador estable `RISK-NNN`.

### Campos obligatorios

| Campo | Regla |
|---|---|
| `risk_id` | Identificador estable `RISK-NNN` |
| `risk` | Enunciado comprensible del riesgo |
| `category` | Categoría controlada |
| `cause` | Causa o conjunto de causas |
| `event` | Evento incierto que podría ocurrir |
| `consequence` | Consecuencia si ocurre el evento |
| `probability` | Valor inherente 1–5 |
| `impact` | Valor inherente 1–5 |
| `exposure` | `probability × impact` |
| `owner` | Responsable nominal del riesgo |
| `treatment` | Estrategia de tratamiento |
| `mitigation` | Acciones preventivas/reductoras |
| `contingency` | Respuesta si el evento ocurre |
| `trigger` | Condición que activa tratamiento/contingencia |
| `residual_probability` | Probabilidad posterior 1–5 |
| `residual_impact` | Impacto posterior 1–5 |
| `residual_exposure` | `residual_probability × residual_impact` |
| `status` | Estado controlado |
| `review_date` | Próxima revisión |
| `evidence` | Referencias trazables |
| `related_artifacts` | Artefactos afectados o relacionados |

## 6. Taxonomía inicial

Las categorías iniciales son deliberadamente generales para evitar inventar una taxonomía de negocio antes de completar el descubrimiento:

- `governance`
- `business`
- `requirements`
- `architecture`
- `technology`
- `security`
- `privacy`
- `data`
- `supplier`
- `operations`
- `continuity`
- `compliance`
- `project`
- `research`
- `other`

La taxonomía podrá ampliarse mediante cambio controlado.

## 7. Escala de Probability

| Valor | Criterio cualitativo |
|---:|---|
| 1 | Raro: no se espera en condiciones normales |
| 2 | Poco probable |
| 3 | Posible |
| 4 | Probable |
| 5 | Casi seguro / altamente probable |

La escala representa juicio estructurado. No implica frecuencias observacionales cuando no existan datos suficientes.

## 8. Escala de Impact

| Valor | Criterio cualitativo |
|---:|---|
| 1 | Insignificante |
| 2 | Menor |
| 3 | Moderado |
| 4 | Mayor |
| 5 | Crítico |

El impacto deberá evaluarse respecto a objetivos relevantes del Ecosistema: negocio, servicio, seguridad, datos, cumplimiento, reputación, operación, coste o continuidad, según aplique.

## 9. Exposure

La exposición inherente se calcula de forma reproducible:

`Exposure = Probability × Impact`

Rango: `1–25`.

| Exposure | Prioridad inicial |
|---:|---|
| 1–4 | Baja |
| 5–9 | Moderada |
| 10–16 | Alta |
| 17–25 | Crítica |

Estos umbrales son una convención inicial de priorización y deberán revisarse cuando el contexto real del negocio permita calibrarlos. No representan riesgo financiero ni probabilidad estadística.

## 10. Tratamiento

El campo `treatment` utilizará inicialmente:

- `avoid` — modificar la situación para eliminar la fuente o exposición cuando sea viable.
- `reduce` — reducir probabilidad y/o impacto.
- `share` — compartir o transferir parte del riesgo mediante contratos, seguros, proveedores u otros mecanismos apropiados.
- `accept` — aceptar explícitamente el riesgo dentro de la autoridad y tolerancia aplicables.
- `exploit` — cuando se gestione una oportunidad y resulte pertinente.
- `enhance` — aumentar la probabilidad o beneficio de una oportunidad.

Un riesgo con tratamiento `accept` debe conservar evidencia de la decisión y del responsable que la acepta cuando corresponda.

## 11. Mitigation, Contingency y Trigger

No son sinónimos:

- **Mitigation:** acciones realizadas antes del evento para reducir probabilidad y/o impacto.
- **Contingency:** acciones previstas para responder cuando el evento ocurre.
- **Trigger:** señal, umbral o condición observable que indica que debe ejecutarse una respuesta o revisión.

Un trigger debe ser observable y, cuando sea posible, medible.

## 12. Residual Risk

El riesgo residual se evalúa después de considerar los tratamientos existentes o comprometidos:

`Residual Exposure = Residual Probability × Residual Impact`

El registro debe conservar tanto la valoración inherente como la residual. Una reducción de la puntuación solo será válida si existe una justificación de por qué el tratamiento modifica realmente la exposición.

## 13. Estados

Estados iniciales controlados:

- `identified`
- `analyzing`
- `treating`
- `accepted`
- `monitoring`
- `escalated`
- `closed`
- `expired`

`closed` requiere evidencia de que el riesgo dejó de ser relevante o fue absorbido/eliminado de forma justificable. `accepted` no significa que el riesgo haya desaparecido.

## 14. Review Date y revisión continua

Todo riesgo abierto debe tener `review_date`.

La revisión debe ocurrir como mínimo:

- en la fecha indicada;
- cuando ocurra su trigger;
- cuando cambie una causa o dependencia relevante;
- cuando cambie arquitectura, requisitos, proveedor o entorno operativo relacionado;
- cuando un incidente demuestre que la valoración ya no representa la realidad;
- durante Quality Gates cuando el riesgo sea material para la decisión.

## 15. Criterios de escalamiento

Un riesgo debe escalarse cuando:

- su exposición entra en categoría crítica;
- supera la tolerancia o autoridad del owner;
- requiere una decisión de arquitectura, negocio o dirección;
- puede comprometer un Quality Gate;
- el tratamiento no puede ejecutarse con los recursos o autoridad disponibles;
- el riesgo residual permanece material después del tratamiento.

## 16. Trazabilidad y evidencia

Cada riesgo relevante deberá relacionarse, cuando corresponda, con:

```text
Risk
 ↓
Cause / Event / Consequence
 ↓
Issue / Requirement / Architecture / ADR / Control
 ↓
Treatment
 ↓
Evidence / Test / Workflow / Operational Record
 ↓
Residual Risk
 ↓
Decision / Acceptance / Closure
```

La evidencia puede ser un archivo, Issue, Pull Request, commit, workflow run, prueba, registro operacional, decisión o referencia externa controlada.

## 17. Integración con Quality Gates

Cada Gate deberá considerar los riesgos materiales para su decisión. Como mínimo:

- G0: riesgos de gobernanza y riesgos residuales conocidos.
- G1: riesgos derivados del estado actual, dependencias y restricciones descubiertas.
- G2: riesgos asociados a valor, alcance y objetivos.
- G3: riesgos de requisitos, incertidumbre y trazabilidad.
- G4–G6: riesgos de sistema, arquitectura y diseño.
- G7–G8: riesgos de construcción, integración, seguridad y verificación.
- G9–G11: riesgos de aceptación, despliegue, operación, continuidad y soporte.
- G12–G13: riesgos de evolución, mejora, migración y retirada.

La existencia de un Risk Register no sustituye la decisión del Gate.

## 18. Automatización futura

La primera baseline es documental y basada en datos versionados. La automatización podrá evolucionar hacia:

- validación de esquema YAML;
- detección de IDs duplicados;
- validación de escalas y fórmulas;
- detección de riesgos sin owner/review date;
- detección de riesgos vencidos;
- cálculo automático de Exposure y Residual Exposure;
- métricas de riesgos por categoría/estado/prioridad;
- correlación con Issues, PRs y Quality Gates.

Estas automatizaciones deberán añadirse como controles explícitos y no deben presentarse como implementadas antes de existir evidencia ejecutable.

## 19. Limitaciones conocidas

- Las valoraciones iniciales pueden depender de juicio experto mientras no existan datos históricos suficientes.
- El Risk Register no constituye por sí mismo una garantía de que todos los riesgos hayan sido identificados.
- La ausencia de un riesgo en el registro no demuestra ausencia de riesgo.
- Los owners y fechas deben revisarse a medida que el contexto real del Ecosistema sea descubierto.

## 20. Criterio de madurez de esta baseline

El Problema #2 no se considerará completamente resuelto por la mera creación de documentos. La capacidad se considerará **implementada como sistema documental operativo** cuando el proceso, registro, criterios, trazabilidad y revisión estén integrados y exista evidencia de uso real. La automatización avanzada podrá evolucionar posteriormente.

## 21. Evidencia esperada para la validación de esta baseline

- Issue #31.
- PR #32.
- Resultados de Governance Validation, Quality Validation, Security Validation y Evidence Validation sobre el HEAD final.
- `Docs/Governance/Risk/Risk-Register.yml` y su representación legible.
- Revisión de coherencia con Quality Gates y catálogo de artefactos.
