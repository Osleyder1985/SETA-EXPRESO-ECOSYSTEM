# Gobernanza de decisiones de arquitectura e ingeniería

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.1  
**Estado:** Baseline propuesta para revisión  
**Fecha:** 2026-09-15  
**Issue:** #33

---

## 1. Propósito

Establecer un sistema formal de **Decision Governance** para registrar, evaluar, aprobar, revisar, superseder y conservar las decisiones arquitectónicas y de ingeniería que puedan condicionar el Ecosistema.

El objetivo no es documentar únicamente el resultado de una decisión. El registro debe conservar el razonamiento suficiente para que una tercera persona pueda reconstruir posteriormente:

- qué problema o contexto originó la decisión;
- qué se decidió;
- qué alternativas fueron consideradas;
- con qué criterios se compararon;
- qué trade-offs fueron aceptados;
- qué consecuencias se esperan;
- qué riesgos se introducen, reducen o aceptan;
- qué evidencia respalda la decisión;
- quién y cuándo la decidió, cuando corresponda;
- cuál es su estado actual y qué decisión la reemplaza, si alguna.

## 2. Alcance

La gobernanza se aplica a decisiones relevantes de arquitectura del Ecosistema, arquitectura de software, datos e información, integración e interfaces, seguridad e identidad, infraestructura y despliegue, observabilidad y operación, proveedores y servicios externos, tecnología y dependencias estratégicas, inteligencia artificial y modelos cuando corresponda, diseño técnico e investigación metodológica.

No toda decisión cotidiana requiere un Decision Record. El criterio es la **materialidad de sus consecuencias, irreversibilidad, riesgo, coste, alcance o impacto futuro**.

## 3. Tipos de Decision Record

### 3.1 Architecture Decision Record — ADR

Se utilizará para decisiones que definan o modifiquen aspectos estructurales de la arquitectura del sistema o del software. Identificador: `ADR-NNN`.

### 3.2 Engineering Decision Record — EDR

Se utilizará para decisiones técnicas relevantes que no constituyan necesariamente una decisión arquitectónica, pero cuyo razonamiento deba conservarse como evidencia de ingeniería. Identificador: `EDR-NNN`.

Los dos tipos utilizan la misma estructura mínima y reglas de gobernanza.

## 4. Principio fundamental

> **Una decisión de ingeniería no queda justificada por haber elegido una opción; queda justificada por el contexto, los criterios, las alternativas, los trade-offs, la evidencia y las consecuencias que explican por qué la opción era razonable.**

Una afirmación como `Elegimos PostgreSQL` no constituye por sí misma un Decision Record suficiente.

## 5. Cuándo requiere un Decision Record

Debe considerarse obligatorio cuando una decisión:

1. afecta una característica estructural de la arquitectura;
2. introduce una tecnología o proveedor con impacto significativo;
3. crea una dependencia difícil de sustituir;
4. afecta seguridad, identidad, privacidad o datos de manera relevante;
5. establece un patrón de integración o interfaz importante;
6. afecta disponibilidad, continuidad, rendimiento o escalabilidad de forma material;
7. compromete coste, licencia o capacidad operativa significativa;
8. condiciona múltiples componentes o fases posteriores;
9. presenta trade-offs relevantes entre calidad, coste, riesgo, tiempo o complejidad;
10. es difícil o costosa de revertir;
11. modifica una decisión previa;
12. puede ser relevante para auditoría, aceptación, investigación o explicación futura.

Las decisiones reversibles y de bajo impacto pueden quedar registradas en otros mecanismos cuando exista una justificación para no generar un record formal.

## 6. Estructura obligatoria

Todo Decision Record formal debe contener como mínimo:

| Campo | Propósito |
|---|---|
| `ID` | Identificador estable `ADR-NNN` o `EDR-NNN` |
| `Title` | Enunciado breve de la decisión |
| `Date` | Fecha de registro/decisión |
| `Status` | Estado controlado |
| `Context` | Situación, problema, restricciones y drivers |
| `Decision` | Decisión adoptada, expresada claramente |
| `Alternatives` | Opciones relevantes consideradas |
| `Criteria` | Criterios utilizados para comparar alternativas |
| `Trade-offs` | Compromisos, ventajas y desventajas aceptadas |
| `Consequences` | Efectos esperados, positivos y negativos |
| `Risks` | Riesgos creados, modificados o aceptados |
| `Evidence` | Evidencia que respalda el razonamiento |
| `Supersedes` | Decisión previa reemplazada, si aplica |
| `Superseded by` | Decisión posterior que la reemplaza, si aplica |

Cuando corresponda también deberán registrarse `Owner`, `Review Date`, `Related Requirements`, `Related Architecture`, `Related Risks`, `Related Issues`, `Related PRs` y `Approvals`.

## 7. Criterios de decisión

Los criterios deberán derivarse del contexto real. Pueden incluir adecuación funcional, seguridad, privacidad, mantenibilidad, disponibilidad, rendimiento, escalabilidad, interoperabilidad, observabilidad, resiliencia, coste total de propiedad, complejidad operacional, madurez tecnológica, soporte y ciclo de vida, dependencia de proveedor, portabilidad, licencia, esfuerzo de implementación, reversibilidad, riesgo técnico, impacto sobre requisitos y reproducibilidad.

No deberán inventarse pesos, métricas o datos cuantitativos cuando todavía no exista evidencia suficiente. Cuando se utilicen puntuaciones, debe explicarse la escala y su significado.

## 8. Alternativas

El record debe conservar las alternativas materialmente relevantes que hayan sido consideradas. No es necesario listar opciones irrelevantes únicamente para aparentar exhaustividad. Cuando solo exista una opción técnicamente viable, el record debe indicar por qué las demás alternativas no son viables o no resultan aplicables.

## 9. Trade-offs

El análisis debe hacer visibles los compromisos aceptados. Un Decision Record no debe presentar una alternativa como superior en todos los criterios si existe evidencia de compromisos reales.

## 10. Riesgos

Cada decisión deberá revisar si crea nuevos riesgos, modifica la probabilidad o impacto de riesgos existentes, reduce riesgos, introduce dependencia de proveedor, crea deuda técnica, afecta controles de seguridad o afecta continuidad u operación.

Los riesgos relevantes deberán relacionarse con `Docs/Governance/Risk/Risk-Register.yml` cuando corresponda.

## 11. Evidence

La evidencia puede incluir requisitos, análisis comparativos, pruebas de concepto, benchmarks, prototipos, documentación técnica de proveedores, resultados de pruebas, análisis de seguridad, análisis de costes, experimentos, datos operacionales, evidencia científica, Issues, Pull Requests y referencias normativas o técnicas controladas.

## 12. Estados

Estados controlados: `proposed`, `accepted`, `rejected`, `superseded`, `deprecated`, `withdrawn`.

Un Decision Record histórico no debe eliminarse para ocultar una decisión anterior. Cuando una decisión cambia, se crea o registra la nueva decisión y se establece la relación de supersession.

## 13. Supersession

La sustitución debe mantener una cadena histórica explícita:

```text
ADR-001
   │
   └── superseded by → ADR-014
                         │
                         └── superseded by → ADR-027
```

La nueva decisión deberá indicar qué decisión sustituye mediante `Supersedes`. La decisión anterior deberá actualizar su `Superseded by` mediante un cambio controlado.

La historia no se reescribe: se extiende.

## 14. Relación con el ciclo de vida

El Decision Governance es transversal al ciclo de vida y tiene especial relevancia en E — Definición y modelado del sistema; F — Arquitectura; G — Diseño; H — Implementación y construcción; I–J cuando resultados provoquen cambios de dirección; K–L en decisiones de despliegue y operación; M–N en evolución y mejora; y O en migración o retirada.

La Fase F incluye explícitamente **Architecture Decision Records** como artefacto y actividad arquitectónica.

## 15. Relación con requisitos, riesgos y evidencia

La cadena esperada es:

```text
Need / Problem
      ↓
Requirement / Constraint
      ↓
Decision Record
      ↓
Architecture / Design
      ↓
Implementation
      ↓
Verification / Validation
      ↓
Evidence
```

Y, de forma transversal:

```text
Decision
   ├──→ Risks
   ├──→ Requirements
   ├──→ Architecture
   ├──→ Issues / PRs
   ├──→ Quality Gates
   └──→ Evidence
```

## 16. Relación con Quality Gates

Los gates deberán considerar Decision Records cuando una decisión relevante sea necesaria para demostrar la preparación o aceptación de una fase. G5 requiere decisiones arquitectónicas relevantes y su evaluación; G6 puede requerir decisiones de diseño materialmente significativas; G12 requiere decisiones de evolución cuando cambie la baseline.

Un `PASS` de validaciones automatizadas no constituye aprobación de una decisión. La decisión debe ser evaluada según su autoridad, evidencia y contexto.

## 17. Gobernanza de aprobación

La autoridad para aceptar una decisión dependerá de su alcance e impacto. Como regla inicial: decisiones técnicas locales requieren revisión de ingeniería correspondiente; decisiones de arquitectura, revisión arquitectónica; decisiones con impacto de negocio, participación del stakeholder correspondiente; decisiones con riesgos materiales, participación del Risk Owner y autoridad pertinente; decisiones con impacto significativo de seguridad, revisión de seguridad cuando corresponda.

La gobernanza no inventará una jerarquía organizativa que todavía no haya sido descubierta. Los roles concretos se precisarán durante B y C.

## 18. Decisiones durante descubrimiento

Durante la Fase B se evitará convertir preferencias tecnológicas en decisiones arquitectónicas prematuras.

Ejemplos como PostgreSQL, Kubernetes, REST, GraphQL, un proveedor concreto o una arquitectura de IA son **hipótesis de decisión**, no decisiones aprobadas, hasta disponer de contexto, necesidades, restricciones, criterios y evidencia suficientes.

## 19. Automatización futura

La capacidad podrá evolucionar hacia validación de estructura, identificadores únicos, referencias rotas, estados válidos, relaciones de supersession, links hacia Issues/requisitos/riesgos, Decision Records sin evidencia, métricas, detección de obsolescencia y generación de índices/grafos de trazabilidad.

Ninguna automatización futura deberá declararse implementada antes de disponer de código/workflow y evidencia ejecutable.

## 20. Criterio de madurez

Esta baseline establece la **capacidad documental inicial de Decision Governance**. No implica que las decisiones futuras del Ecosistema ya estén tomadas ni que los ADR/EDR estén automatizados.

La madurez aumentará mediante uso real, decisiones efectivamente registradas, revisiones y aprobaciones trazables, relaciones con requisitos y riesgos, evidencia objetiva, supersession correctamente gestionada y automatización progresiva.

## 21. Artefactos controlados

- `Docs/Governance/19-Decision-Governance.md` — política y proceso.
- `Docs/Architecture/Decision-Records/README.md` — reglas de almacenamiento.
- `Docs/Architecture/Decision-Records/ADR-Template.md` — plantilla ADR.
- `Docs/Architecture/Decision-Records/EDR-Template.md` — plantilla EDR.
- `Docs/Architecture/Decision-Records/Decision-Record-Index.md` — índice de decisiones.

## 22. Regla de cambio

La creación, modificación, supersession o retiro de un Decision Record constituye un cambio controlado y debe seguir el flujo Issue → Branch → Impact Analysis → PR → validaciones → revisión → merge.

Cuando una decisión modifique arquitectura, requisitos, riesgos, diseño, configuración, código o pruebas, el análisis de impacto deberá determinar qué artefactos deben actualizarse en la misma unidad de cambio.

## 23. Evidencia esperada para esta baseline

- Issue #33.
- PR asociado.
- Política de Decision Governance.
- Estructura de Decision Records.
- Plantillas ADR y EDR.
- Índice controlado.
- Sin decisiones técnicas prematuras inventadas.
- Coherencia con lifecycle, change control, artifact catalog, Risk Management y Quality Gates.
- Governance Validation, Quality Validation, Security Validation y Evidence Validation sobre el commit final.
