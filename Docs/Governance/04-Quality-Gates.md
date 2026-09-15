# Quality Gates del ciclo de vida

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Definición controlada y operacional  
**Fecha:** 2026-09-15

---

## 1. Propósito

Definir puntos de control para decidir si existe evidencia suficiente para avanzar, continuar iterando, detener, corregir o cambiar de dirección.

Los gates no convierten el ciclo en cascada. Un gate puede requerir volver a una fase anterior cuando la evidencia sea insuficiente.

Un Quality Gate representa una decisión basada en evidencia; no es únicamente la ejecución exitosa de workflows automatizados.

A partir de esta versión, cada gate dispone además de una especificación operacional con criterios de entrada, entradas requeridas, comprobaciones, métricas, evidencia, autoridad de decisión y criterios de salida.

## 2. Gates

| ID | Gate | Fase asociada | Resultado esperado |
|---|---|---|---|
| G0 | Governance Ready | A | Gobierno, controles mínimos y evidencia base establecidos |
| G1 | Discovery Ready | B | Estado actual comprendido |
| G2 | Problem And Objectives Ready | C | Problema, necesidades y objetivos definidos |
| G3 | Requirements Baseline | D | Requisitos verificables, priorizados y trazables |
| G4 | System Definition Ready | E | Sistema objetivo y contexto definidos |
| G5 | Architecture Baseline | F | Arquitectura evaluada y controlada |
| G6 | Design Ready | G | Diseño suficientemente detallado |
| G7 | Build Ready | H | Construcción y controles de ingeniería preparados |
| G8 | Verification Ready | I | Evidencia de verificación aceptable |
| G9 | Validation Accepted | J | Validación y aceptación logradas |
| G10 | Production Ready | K | Producción preparada y rollback definido |
| G11 | Operationally Stable | L | Operación estable y observable |
| G12 | Evolution Ready | M/N | Cambio o evolución evaluados |
| G13 | Retirement Complete | O | Retirada/migración y preservación de evidencia completadas |

## 3. G0 — Governance Ready

El Gate G0 confirma que existe una base mínima de gobernanza antes de avanzar a fases posteriores.

### Evidencia mínima requerida

```text
15-G0-Governance-Readiness-Assessment.md
        +
16-G0-Impact-Analysis.md
        +
Governance Control Matrix
        +
Governance Validation
        +
Quality Validation
        +
Security Validation
        +
Evidence Validation
        +
Pull Request asociado
```

### Controles relacionados

```text
GC-001  G0 Governance Readiness Assessment
GC-002  G0 Impact Analysis
GC-003  G0 Evidence Package
GC-004  Residual Risk Acceptance
```

El resultado del Gate G0 debe considerar también las limitaciones técnicas conocidas y sus controles compensatorios.

## 4. Validaciones transversales de cambios

Las validaciones automatizadas para una unidad de cambio siguen esta cadena:

```text
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
```

Un resultado `PASS` de una validación automatizada es evidencia técnica de los controles aplicables de esa capa; no equivale por sí mismo al resultado de un Quality Gate.

### Governance Validation

Comprueba las reglas de trazabilidad, nomenclatura, labels, análisis de impacto y baseline de gobernanza definidas para los cambios.

### Quality Validation

Aporta comprobaciones técnicas objetivas. Un `QUALITY_VALIDATION=PASS` no certifica la calidad integral del producto.

### Security Validation

Aporta comprobaciones de seguridad objetivas. Un `SECURITY_VALIDATION=PASS` no certifica seguridad integral ni ausencia de vulnerabilidades.

### Evidence Validation

Comprueba que el cambio contiene evidencia mínima, trazable y verificable. Un `EVIDENCE_VALIDATION=PASS` no certifica suficiencia de evidencia ni corrección integral del producto.

Para una unidad de cambio, un fallo objetivo de Governance, Quality, Security o Evidence Validation implica que el cambio no debe considerarse conforme hasta que el defecto sea corregido o exista una decisión formal y trazable de excepción.

## 5. Criterios comunes

Cada gate deberá considerar, según aplicabilidad:

- alcance;
- requisitos;
- calidad;
- seguridad;
- riesgos;
- dependencias;
- configuración y versiones;
- pruebas;
- trazabilidad;
- evidencia;
- responsables y aprobaciones;
- control de cambios y estado del Pull Request cuando el gate implique una modificación controlada;
- resultados de Governance Validation, Quality Validation, Security Validation y Evidence Validation cuando correspondan;
- decisiones materiales de arquitectura e ingeniería y sus Decision Records cuando sean aplicables;
- controles de AI Governance cuando exista un caso de uso de IA dentro del alcance del gate.

## 6. Decision Governance en Quality Gates

Las decisiones materiales que condicionen la aceptación de arquitectura, diseño, tecnología, integraciones, seguridad, datos, operación o evolución deberán estar respaldadas por un `ADR` o `EDR` cuando corresponda a los criterios de materialidad definidos en `19-Decision-Governance.md`.

En particular:

- **G5 Architecture Baseline:** deberá comprobarse la existencia y estado de los ADR relevantes para las decisiones arquitectónicas materiales.
- **G6 Design Ready:** deberá comprobarse la trazabilidad de las decisiones de diseño materiales hacia sus requisitos, alternativas, riesgos y evidencia.
- **G12 Evolution Ready:** los cambios que alteren decisiones previamente registradas deberán actualizar, superseder o complementar el Decision Record correspondiente.

La ausencia de un Decision Record aplicable no se corregirá inventando una decisión histórica. Deberá registrarse la decisión cuando exista contexto y evidencia suficientes, o quedar como condición/pending work trazable.

## 7. AI Governance en Quality Gates

Cuando un cambio, producto, proceso o investigación utilice IA de manera material, el gate deberá considerar la aplicabilidad de `Docs/Governance/23-AI-Governance.md`.

Como mínimo, según criticidad y dominio, deberá comprobarse:

- AI Use Inventory actualizado;
- Model Inventory cuando corresponda;
- clasificación `build-time`, `product-runtime` o `research`;
- riesgos de IA relacionados con el Risk Register;
- Decision Record cuando la IA implique una decisión material;
- evaluación/TEVV proporcional al riesgo;
- controles de seguridad y privacidad;
- Human Oversight;
- Data Provenance cuando se utilicen datasets relevantes;
- evidencia de reproducibilidad para investigación;
- incidentes abiertos o restricciones de uso;
- criterios de aceptación y límites de uso.

No se deberá aprobar una capacidad de IA únicamente porque el modelo produzca resultados plausibles o porque un proveedor la declare segura.

## 8. Métricas de ingeniería como evidencia de Gate

Las métricas definidas en `Docs/Governance/21-Engineering-Metrics-Governance.md` y `Docs/Governance/Metrics/Metric-Catalog.yml` constituyen una fuente formal de evidencia para evaluar la salud y evolución del proceso cuando exista una fuente operacional suficiente.

Los Quality Gates no deberán convertir métricas sin baseline en criterios numéricos artificiales. Cuando una métrica esté en estado `defined`, `provisional` o `blocked`, el gate deberá registrar la limitación y no interpretarla como cero, cumplimiento o incumplimiento.

Cuando aplique, el paquete de evidencia del gate podrá incluir:

- métricas aplicables y su periodo de medición;
- fuente y método de cálculo;
- baseline y target si existen;
- tendencia histórica cuando exista;
- desviaciones respecto de thresholds formalmente definidos;
- limitaciones de cobertura o calidad de datos;
- acciones o decisiones derivadas.

Las métricas sirven como evidencia para decidir; no sustituyen la evaluación de requisitos, arquitectura, riesgos, pruebas, aceptación ni juicio de ingeniería.

## 9. Modelo formal de decisión

Un gate puede resultar:

- **PASS:** todos los criterios obligatorios satisfechos y exit criteria cumplidos.
- **CONDITIONAL:** los criterios obligatorios están satisfechos, pero existen condiciones explícitas, acotadas, con responsable y fecha de resolución, aprobadas por la autoridad correspondiente.
- **BLOCKED:** falta una entrada, dependencia, evidencia o decisión de autoridad necesaria para evaluar o continuar.
- **REOPEN:** un evento posterior invalida parcial o totalmente la evidencia o decisión previa y obliga a reevaluar el gate.

Los estados históricos `PASS WITH KNOWN LIMITATIONS`, `PASS WITH CONDITIONS`, `REWORK` y `FAIL` quedan interpretados dentro del modelo operacional mediante la especificación de cada gate y las reglas de disposición correspondientes. No se permite convertir automáticamente un `FAIL` en `PASS`.

Una excepción debe quedar registrada como condición, excepción o decisión controlada.

## 10. Especificación operacional obligatoria

Cada gate G0–G13 deberá disponer de los siguientes elementos:

```text
Entry Criteria
Required Inputs
Checks
Metrics
Evidence
Decision Authority
PASS
CONDITIONAL
BLOCKED
REOPEN
Exit Criteria
```

La especificación operacional completa y machine-readable se mantiene en:

`Docs/Governance/Quality/Quality-Gate-Catalog.yml`

La clasificación de cada comprobación es:

- `AUTOMATED`: puede comprobarse objetivamente por máquina.
- `HYBRID`: la máquina prepara/verifica evidencia y una autoridad humana completa el juicio.
- `HUMAN`: requiere juicio o aprobación humana.

La máquina no deberá inventar evidencia, valores de métricas, aceptación ni decisiones.

## 11. G4 — Requirements Baseline: ejemplo de criterio operacional

G4 constituye el primer ejemplo explícito de cómo una decisión de gate debe transformarse en condiciones verificables:

```text
PASS solamente si:

100% requirements tienen ID
100% tienen owner
100% tienen acceptance criteria
≥95% tienen trazabilidad
0 requirements críticos ambiguos
100% requirements críticos verificables
```

Estos criterios deben tener una fuente de datos, una definición operacional y evidencia reproducible. Los umbrales son criterios de ejemplo hasta que sean justificados y aprobados dentro del contexto real de requisitos del Ecosistema.

## 12. Evidencia y automatización progresiva

La evidencia del gate debe ser localizable desde GitHub mediante documentación, Issues, Pull Requests, commits, resultados de CI/CD, registros de pruebas u otras referencias controladas.

Cada resultado de gate deberá poder responder, como mínimo:

```text
¿Qué gate?
¿Qué versión de criterios?
¿Qué entrada se evaluó?
¿Qué checks se ejecutaron?
¿Qué métricas se calcularon?
¿Qué evidencia las sustenta?
¿Qué autoridad decidió?
¿Qué resultado produjo?
¿Qué condiciones quedaron abiertas?
¿Qué puede provocar REOPEN?
```

La automatización se ampliará progresivamente a medida que Requirements, Architecture, Tests, Data, Infrastructure y Operational telemetry dispongan de fuentes estructuradas. Los controles automatizados deberán producir evidencia reproducible y no deberán confundirse con la decisión final cuando esta requiera juicio humano.

## 13. Evolución

Los criterios específicos de cada gate evolucionarán mediante cambios controlados y análisis de impacto sobre:

- ciclo maestro;
- catálogo de artefactos;
- Quality Validation;
- Risk Management;
- Decision Governance;
- Security Validation;
- Evidence Validation;
- Engineering Metrics;
- Requirements;
- Architecture;
- Data Governance;
- AI Governance;
- Supplier/Third-Party Governance.

Cualquier modificación de criterios, thresholds, autoridad o semántica de resultados deberá quedar trazada mediante Issue → Branch → PR → Validaciones → Review → Merge.
