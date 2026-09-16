# Ciclo de Vida Maestro de Ingeniería de Software y del Ecosistema

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.3.0  
**Estado:** Baseline controlada vigente  
**Idioma documental:** Español  
**Convención de nombres:** Inglés, Title Case por segmentos y palabras separadas por guiones  
**Fecha:** 2026-09-15

---

## 1. Propósito

Este documento define el marco maestro de ingeniería utilizado para concebir, definir, construir, verificar, validar, desplegar, operar, mantener, evolucionar y retirar el Ecosistema Digital de Seta Expreso S.U.R.L.

El ciclo de vida no es una secuencia rígida de etapas. Es un marco adaptable que permite actividades iterativas, incrementales, concurrentes y recursivas cuando el contexto del sistema, el riesgo, la incertidumbre o la naturaleza del trabajo lo requieran.

El objetivo no es únicamente producir software. El objetivo es producir un sistema útil, seguro, mantenible, verificable, operable y evolutivo, acompañado de evidencia suficiente para explicar qué se decidió, por qué se decidió, cómo se implementó y qué resultados se obtuvieron.

## 2. Alcance

El marco cubre dos niveles relacionados:

```text
SISTEMA / ECOSISTEMA
Organización · Personas · Procesos · Información · Datos
Software · Infraestructura · Integraciones · Servicios externos · Gobernanza

                         ↓

SOFTWARE
Aplicaciones · Servicios · Componentes · APIs · Código
Bases de datos · Configuración · Pipelines · Pruebas
```

La referencia sistémica principal será ISO/IEC/IEEE 15288:2023 y la referencia principal de ciclo de vida de software será ISO/IEC/IEEE 12207:2026. La ingeniería de requisitos, arquitectura, calidad y seguridad se alineará, según corresponda, con ISO/IEC/IEEE 29148:2018, ISO/IEC/IEEE 42010:2022, ISO/IEC 25010:2023 y NIST SP 800-218 / SSDF 1.1.

## 3. Principios

1. **Engineering before implementation:** no se iniciará construcción relevante sin suficiente comprensión del problema y del resultado esperado.
2. **Evidence by default:** toda decisión importante debe dejar evidencia verificable.
3. **Traceability by design:** necesidades, requisitos, decisiones, implementación, pruebas y resultados deben poder relacionarse.
4. **Quality from the beginning:** calidad, seguridad, operabilidad y mantenibilidad se consideran desde requisitos.
5. **Risk-driven execution:** el esfuerzo y la profundidad de ingeniería se ajustan al riesgo.
6. **Automation first:** tareas repetibles y verificables deben automatizarse cuando sea razonable.
7. **Secure by design:** la seguridad se incorpora desde la concepción y durante todo el ciclo.
8. **Observable systems:** lo que se opera debe poder observarse y diagnosticarse.
9. **Controlled change:** cambios relevantes deben tener motivo, impacto, decisión y evidencia.
10. **Reproducibility:** versiones, configuraciones y resultados relevantes deben poder reproducirse cuando sea técnicamente posible.
11. **Standards-informed, context-driven:** las normas orientan; el proyecto decide su adaptación con justificación.
12. **Continuous learning:** operación y resultados retroalimentan la evolución del sistema y del proceso.

## 4. Modelo general

```text
 A  →  B  →  C  →  D  →  E  →  F  →  G  →  H
 │                                                   │
 └──────────────────── Feedback ─────────────────────┘
                                                     ↓
                         I  →  J  →  K  →  L  →  M
                                                     ↓
                                             N  →  O
                                                     │
                                                     └──→ nueva evolución
```

Las flechas representan un flujo lógico, no una restricción de secuencialidad. Un trabajo puede regresar a requisitos, arquitectura o diseño cuando la evidencia lo justifique.

## 5. Fases del ciclo de vida

### A. Concepción y gobernanza

**Objetivo:** establecer propósito, autoridad, contexto inicial y reglas de gobierno.

**Subfases:**

A.1 Iniciación del proyecto.  
A.2 Definición de visión y propósito.  
A.3 Identificación inicial de stakeholders.  
A.4 Contexto y restricciones.  
A.5 Modelo de gobernanza.  
A.6 Viabilidad inicial.  
A.7 Identificación preliminar de riesgos.  
A.8 Estrategia de ciclo de vida.  
A.9 Definición de repositorio, control de versiones y reglas documentales.

**Artefactos principales:** Project Charter, Governance Model, Stakeholder Register, Initial Risk Register, Lifecycle Strategy, Repository Conventions.

**Salida mínima:** autoridad, propósito, alcance inicial, reglas de gobierno y estrategia de ingeniería suficientemente definidos.

---

### B. Descubrimiento del sistema y organización

**Objetivo:** comprender la realidad en la que el Ecosistema debe operar.

**Subfases:**

B.1 Descubrimiento organizacional.  
B.2 Identificación de procesos actuales.  
B.3 Identificación de actores y roles.  
B.4 Inventario de sistemas existentes.  
B.5 Inventario de información y datos.  
B.6 Infraestructura y entorno operativo.  
B.7 Integraciones y dependencias existentes.  
B.8 Capacidades actuales.  
B.9 Problemas, limitaciones y oportunidades observadas.

**Artefactos:** Current-State Model, Process Inventory, System Context, Information Inventory, Capability Map, Discovery Evidence.

**Salida mínima:** modelo suficientemente confiable del estado actual y de sus principales restricciones.

---

### C. Necesidades, problema y objetivos

**Objetivo:** transformar observaciones en problemas, necesidades y resultados esperados.

**Subfases:**

C.1 Formulación del problema.  
C.2 Análisis de causas.  
C.3 Identificación de oportunidades.  
C.4 Identificación y priorización de necesidades.  
C.5 Definición de objetivos.  
C.6 Definición de resultados esperados.  
C.7 Definición de alcance y exclusiones.  
C.8 Hipótesis de valor cuando aplique.  
C.9 Business Case cuando sea necesario.

**Artefactos:** Problem Statement, Needs Catalogue, Objectives, Scope, Business Case, Success Criteria.

**Salida mínima:** problema, necesidades, objetivos, alcance y criterios de éxito definidos y revisables.

---

### D. Ingeniería de requisitos

**Objetivo:** producir y mantener una especificación verificable de lo que el sistema debe proporcionar y de las restricciones que debe satisfacer.

**Subfases:**

D.1 Identificación de fuentes.  
D.2 Elicitación.  
D.3 Análisis y negociación.  
D.4 Modelado de requisitos.  
D.5 Especificación.  
D.6 Priorización.  
D.7 Requisitos funcionales.  
D.8 Requisitos de calidad.  
D.9 Requisitos de seguridad.  
D.10 Requisitos de datos.  
D.11 Restricciones y reglas de negocio.  
D.12 Criterios de aceptación.  
D.13 Trazabilidad.  
D.14 Baseline.  
D.15 Gestión de cambios.

**Artefactos:** Stakeholder Needs, System Requirements, Software Requirements, Quality Requirements, Security Requirements, Acceptance Criteria, Requirements Traceability Matrix.

**Salida mínima:** requisitos suficientemente completos, consistentes, trazables, priorizados y verificables para continuar.

---

### E. Definición y modelado del sistema

**Objetivo:** definir el sistema objetivo y sus relaciones con el entorno.

**Subfases:**

E.1 Modelo de negocio objetivo.  
E.2 Modelo de dominio.  
E.3 Procesos objetivo.  
E.4 Actores y responsabilidades.  
E.5 Capacidades objetivo.  
E.6 Modelo de información.  
E.7 Límites del sistema.  
E.8 Contexto operacional.  
E.9 Escenarios de uso y operación.  
E.10 Interfaces externas.

**Artefactos:** Target Operating Model, Domain Model, Business Process Models, System Context, Operational Scenarios, Information Model.

---

### F. Arquitectura

**Objetivo:** definir la estructura fundamental del Ecosistema, sus elementos, relaciones, principios y decisiones.

**Subfases:**

F.1 Identificación de stakeholders de arquitectura.  
F.2 Identificación de concerns.  
F.3 Selección de viewpoints y técnicas.  
F.4 Arquitectura del Ecosistema.  
F.5 Arquitectura de negocio.  
F.6 Arquitectura de información y datos.  
F.7 Arquitectura de software.  
F.8 Arquitectura de integración.  
F.9 Arquitectura de seguridad.  
F.10 Arquitectura de infraestructura y despliegue.  
F.11 Arquitectura de observabilidad.  
F.12 Evaluación de alternativas.  
F.13 Architecture Decision Records.  
F.14 Evaluación de riesgos arquitectónicos.  
F.15 Baseline arquitectónica.

**Artefactos:** Architecture Description, Architecture Views, Architecture Models, ADRs, Architecture Decision Log, Architecture Risks.

La descripción de arquitectura se gestionará como información controlada y trazable, en línea con el enfoque de ISO/IEC/IEEE 42010:2022.

---

### G. Diseño

**Objetivo:** transformar arquitectura y requisitos en especificaciones suficientemente detalladas para construcción y verificación.

**Subfases:**

G.1 Diseño funcional.  
G.2 Diseño de componentes.  
G.3 Diseño de APIs.  
G.4 Diseño de datos.  
G.5 Diseño de interfaces.  
G.6 Diseño de workflows.  
G.7 Diseño de algoritmos.  
G.8 Diseño de errores y resiliencia.  
G.9 Diseño de seguridad.  
G.10 Diseño de observabilidad.  
G.11 Diseño de configuración.  
G.12 Diseño de pruebas.  
G.13 Revisión y baseline del diseño.

**Artefactos:** Detailed Design, API Specifications, Data Design, Interface Specifications, Threat Models, Test Design, Configuration Design.

---

### H. Implementación y construcción

**Objetivo:** construir los elementos del sistema de manera controlada y reproducible.

**Subfases:**

H.1 Preparación del entorno de desarrollo.  
H.2 Implementación de código.  
H.3 Implementación de datos.  
H.4 Implementación de configuración.  
H.5 Infrastructure as Code cuando aplique.  
H.6 Pruebas unitarias.  
H.7 Automatización de calidad.  
H.8 Análisis estático.  
H.9 Revisión de código.  
H.10 Gestión de dependencias.  
H.11 Documentación técnica.  
H.12 Empaquetado de artefactos.

**Artefactos:** Source Code, Unit Tests, Build Artifacts, Configuration, Infrastructure Code, Technical Documentation.

---

### I. Integración y verificación

**Objetivo:** demostrar mediante evidencia objetiva que los elementos integrados cumplen sus especificaciones y restricciones verificables.

**Subfases:**

I.1 Integración de componentes.  
I.2 Integración de servicios.  
I.3 Integración de sistemas externos.  
I.4 Pruebas de integración.  
I.5 Pruebas de contrato.  
I.6 Verificación funcional.  
I.7 Verificación de calidad.  
I.8 Verificación de seguridad.  
I.9 Compatibilidad e interoperabilidad.  
I.10 Pruebas automatizadas.  
I.11 Gestión de defectos.  
I.12 Registro de resultados y evidencia.

**Artefactos:** Integration Tests, Verification Plan, Test Results, Defect Records, Verification Evidence.

---

### J. Validación y aceptación

**Objetivo:** demostrar que el sistema satisface necesidades, objetivos y uso previsto, y obtener aceptación de los responsables correspondientes.

**Subfases:**

J.1 Validación funcional.  
J.2 Validación de calidad.  
J.3 Validación de seguridad.  
J.4 Validación operacional.  
J.5 Validación con usuarios/stakeholders.  
J.6 Evaluación de objetivos y criterios de éxito.  
J.7 User Acceptance Testing cuando aplique.  
J.8 Registro de no conformidades.  
J.9 Aceptación formal.

**Artefactos:** Validation Plan, Acceptance Test Results, Acceptance Record, Validation Evidence.

---

### K. Transición y despliegue

**Objetivo:** trasladar el sistema a su entorno objetivo de forma controlada.

**Subfases:**

K.1 Preparación del entorno.  
K.2 Preparación de configuración.  
K.3 Migración y carga inicial de datos.  
K.4 Gestión de versiones.  
K.5 Despliegue.  
K.6 Capacitación.  
K.7 Preparación del soporte.  
K.8 Verificación post-despliegue.  
K.9 Rollback/contingencia.  
K.10 Aceptación de producción.  
K.11 Handover operacional.

**Artefactos:** Deployment Plan, Migration Plan, Release Notes, Runbooks, Training Materials, Rollback Plan, Production Acceptance.

---

### L. Operación y soporte

**Objetivo:** mantener el sistema disponible, seguro, observable y útil en su entorno operativo.

**Subfases:**

L.1 Operación rutinaria.  
L.2 Monitorización y observabilidad.  
L.3 Gestión de incidentes.  
L.4 Gestión de problemas.  
L.5 Gestión de capacidad.  
L.6 Gestión de disponibilidad.  
L.7 Continuidad.  
L.8 Backup y recuperación.  
L.9 Seguridad operacional.  
L.10 Gestión de accesos.  
L.11 Soporte a usuarios.  
L.12 Métricas operacionales.

**Artefactos:** Runbooks, Monitoring Definitions, Incident Records, Problem Records, Backup Evidence, Operational Metrics.

---

### M. Mantenimiento y evolución

**Objetivo:** corregir, adaptar, mejorar y ampliar el sistema manteniendo control de impacto y trazabilidad.

**Subfases:**

M.1 Mantenimiento correctivo.  
M.2 Mantenimiento adaptativo.  
M.3 Mantenimiento perfectivo.  
M.4 Mantenimiento preventivo.  
M.5 Gestión de deuda técnica.  
M.6 Refactorización.  
M.7 Nuevas capacidades.  
M.8 Evolución arquitectónica.  
M.9 Actualización de dependencias.  
M.10 Migraciones tecnológicas.

Cada cambio significativo vuelve a activar los procesos de requisitos, arquitectura, diseño, construcción, verificación y validación que resulten necesarios.

---

### N. Mejora y optimización

**Objetivo:** utilizar evidencia del sistema y del proceso para mejorar resultados.

**Subfases:**

N.1 Recolección de métricas.  
N.2 Análisis de tendencias.  
N.3 Identificación de oportunidades.  
N.4 Mejora de procesos.  
N.5 Optimización técnica.  
N.6 Optimización operacional.  
N.7 Feedback de usuarios.  
N.8 Experimentación controlada.  
N.9 Evaluación de resultados.  
N.10 Incorporación de aprendizajes.

---

### O. Retirada y migración

**Objetivo:** retirar o sustituir capacidades de forma segura, controlada y trazable.

**Subfases:**

O.1 Evaluación de retirada.  
O.2 Análisis de impacto.  
O.3 Estrategia de migración.  
O.4 Migración de datos.  
O.5 Retención y archivado.  
O.6 Desmantelamiento.

---

## 6. Procesos y controles transversales

Las fases A–O constituyen una organización del trabajo, pero no representan la totalidad de la ingeniería. Los siguientes procesos y disciplinas atraviesan el ciclo completo y se activan según contexto, riesgo y naturaleza del cambio:

- Gobernanza y toma de decisiones.
- Gestión de cambios.
- Gestión de configuración y baselines.
- Gestión de riesgos y oportunidades.
- Gestión de calidad.
- Ingeniería de seguridad y privacidad cuando corresponda.
- Gestión de requisitos y trazabilidad.
- Gestión de datos e información.
- Gestión de dependencias y suministro/adquisición.
- Gestión de documentación y conocimiento.
- Medición y análisis.
- Automatización y DevSecOps.
- Observabilidad y operación.
- Gestión de defectos y no conformidades.
- Gestión de decisiones y Architecture Decision Records.
- Gestión de evidencia y reproducibilidad.
- Integración con actividades de investigación científica.

Estos controles no deben interpretarse como fases adicionales. Su aplicación puede ser concurrente, iterativa, incremental o recursiva.

---

## 7. Control obligatorio de cambios del repositorio

El control de cambios del repositorio constituye un mecanismo transversal obligatorio del ciclo de vida.

### 7.1 Flujo operativo

Todo cambio controlado seguirá, como mínimo, esta cadena:

```text
Issue
  ↓
Análisis del problema / necesidad / oportunidad
  ↓
Definición de alcance y criterios de aceptación
  ↓
Branch de trabajo
  ↓
Implementación
  ↓
Análisis de impacto
  ↓
Actualización de artefactos afectados
  ↓
Pruebas / validación / evidencia
  ↓
Pull Request
  ↓
Revisión
  ↓
Correcciones, si son necesarias
  ↓
Aprobación
  ↓
Merge
  ↓
main
```

### 7.2 Reglas obligatorias

1. `main` es la línea base integrada y controlada; no es espacio de trabajo.
2. Ningún cambio de trabajo deberá realizarse directamente sobre `main`.
3. Todo cambio significativo deberá estar respaldado por un Issue antes de su implementación.
4. La implementación se realizará en una branch asociada al Issue.
5. Un Issue puede resolverse mediante uno o varios Pull Requests.
6. Todo Pull Request destinado a `main` deberá estar vinculado al Issue correspondiente.
7. Issues y Pull Requests del proyecto se redactarán en español.
8. Todo cambio deberá incluir análisis de impacto sobre los artefactos relacionados.
9. Los artefactos afectados deberán actualizarse en la misma unidad de cambio cuando sea razonable; de lo contrario, el pendiente deberá quedar explícitamente trazado.
10. Ningún Pull Request deberá considerarse listo para integración mientras tenga trabajo pendiente no resuelto que afecte sus criterios de aceptación.
11. Antes de solicitar la revisión/fusión de un Pull Request se deberá declarar explícitamente su estado: **LISTO PARA FUSIÓN** o **NO FUSIONAR — TRABAJO PENDIENTE**.

La política operativa detallada se encuentra en `Docs/Governance/06-Change-Control-Workflow.md`.

### 7.3 Análisis de impacto mínimo

Como mínimo deberán considerarse estas relaciones:

| Cambio origen | Posibles artefactos afectados |
|---|---|
| Documento → documento | Referencias, definiciones, versiones, terminología y dependencias documentales |
| Requisito → arquitectura/diseño | Arquitectura, ADR, diseño, interfaces, pruebas y trazabilidad |
| Arquitectura → código | Componentes, interfaces, configuración, infraestructura y documentación técnica |
| Código → pruebas | Pruebas unitarias, integración, regresión, evidencia y documentación |
| Seguridad → arquitectura/diseño | Controles, amenazas, requisitos, configuración y pruebas de seguridad |
| Pruebas → requisitos | Criterios de aceptación, trazabilidad y estado de verificación/validación |
| Configuración → DevOps | Pipelines, despliegue, infraestructura, secretos y runbooks |
| Datos → documentación | Modelos, contratos, migraciones, calidad y trazabilidad |
| Ingeniería → investigación | Hipótesis, métricas, evidencia, metodología y resultados científicos |
| Movimiento/renombrado → referencias | Enlaces, índices, referencias cruzadas, automatizaciones y documentación |

---

## 8. Artefactos, evidencia y trazabilidad

Cada unidad de ingeniería deberá conservar evidencia proporcional a su importancia y riesgo.

La cadena de trazabilidad objetivo es:

```text
Problema / Necesidad
        ↓
Objetivo
        ↓
Requisito
        ↓
Decisión / Diseño / ADR
        ↓
Issue
        ↓
Branch
        ↓
Pull Request
        ↓
Commit
        ↓
Prueba / Verificación / Validación
        ↓
Release
        ↓
Evidencia operacional
        ↓
Resultado / Aprendizaje
```

No todos los cambios requerirán todos los elementos de la cadena. La ausencia de un elemento relevante deberá ser justificable.

La documentación, código, pruebas, configuraciones, modelos, decisiones y evidencias deberán permanecer coherentes entre sí. Un archivo correcto de forma aislada no constituye evidencia suficiente de coherencia del Ecosistema.

---

## 9. Quality Gates

Los Quality Gates son puntos de decisión basados en evidencia. No convierten el ciclo en cascada.

Los gates principales son:

| ID | Gate | Fase asociada |
|---|---|---|
| G0 | Governance Ready | A |
| G1 | Discovery Ready | B |
| G2 | Problem And Objectives Ready | C |
| G3 | Requirements Baseline | D |
| G4 | System Definition Ready | E |
| G5 | Architecture Baseline | F |
| G6 | Design Ready | G |
| G7 | Build Ready | H |
| G8 | Verification Ready | I |
| G9 | Validation Accepted | J |
| G10 | Production Ready | K |
| G11 | Operationally Stable | L |
| G12 | Evolution Ready | M/N |
| G13 | Retirement Complete | O |

Todo gate deberá considerar, según aplicabilidad, alcance, requisitos, calidad, seguridad, riesgos, dependencias, configuración, pruebas, trazabilidad, evidencia y responsables.

Para cualquier cambio controlado que atraviese un gate, la evidencia deberá demostrar que el cambio siguió el flujo de control establecido y que su impacto fue evaluado.

Los resultados posibles de un gate son:

- **PASS:** criterios satisfechos.
- **PASS WITH CONDITIONS:** puede continuar con condiciones explícitas y trazables.
- **REWORK:** debe regresar a actividades anteriores.
- **BLOCKED:** existe un impedimento que requiere decisión o información externa.

---

## 10. Investigación científica y generación de conocimiento

El proyecto se gestionará de forma que determinados resultados puedan convertirse, cuando exista mérito científico, en evidencia para investigación, publicaciones, tesis, informes técnicos o estudios reproducibles.

Las actividades de investigación no sustituyen la ingeniería del producto. Deben mantener separación conceptual entre:

- evidencia necesaria para construir y operar el Ecosistema;
- evidencia utilizada para evaluar hipótesis o preguntas de investigación;
- resultados científicos derivados del proyecto.

Cuando una actividad de ingeniería pueda producir evidencia científica, deberá preservarse información suficiente sobre contexto, método, versión, datos, configuración, métricas, amenazas a la validez y resultados.

---

## 11. Aplicación de estándares

El ciclo se apoya en estándares y marcos reconocidos, pero no se aplicará ninguna práctica únicamente por conformidad nominal.

La adaptación deberá justificarse por contexto, riesgo, tamaño, criticidad, restricciones, recursos y objetivos del Ecosistema.

Referencias principales:

- ISO/IEC/IEEE 15288:2023 — ciclo de vida de sistemas.
- ISO/IEC/IEEE 12207:2026 — ciclo de vida de software.
- ISO/IEC/IEEE 29148:2018 — ingeniería de requisitos.
- ISO/IEC/IEEE 42010:2022 — descripción de arquitectura.
- ISO/IEC 25010:2023 — modelo de calidad de producto.
- NIST SP 800-218 / SSDF 1.1 — prácticas de desarrollo seguro de software.

La matriz de relación entre estándares y ciclo de vida se mantendrá en `Docs/Governance/02-Standards-Lifecycle-Matrix.md`.

---

## 12. Criterio de suficiencia de ingeniería

No existe un nivel universal de documentación o control que deba aplicarse con igual profundidad a todos los cambios.

La profundidad de ingeniería se determinará considerando, como mínimo:

- impacto para el negocio;
- criticidad del sistema;
- riesgo técnico y operacional;
- seguridad y privacidad;
- complejidad;
- incertidumbre;
- dependencia de terceros;
- impacto de datos;
- reversibilidad del cambio;
- requisitos regulatorios o contractuales;
- potencial valor científico.

La reducción de rigor deberá ser una decisión explícita y justificable, nunca una omisión accidental.

---

## 13. Gobernanza del propio ciclo de vida

Este documento es un artefacto controlado. Sus modificaciones deberán seguir el flujo establecido en la sección 7 y activar análisis de impacto sobre las políticas, matrices, catálogos, gates, README, nomenclatura y demás artefactos relacionados.

Las versiones del documento representan estados controlados del marco de ingeniería. La aprobación de una versión no impide su evolución posterior cuando nueva evidencia o cambios del contexto lo justifiquen.

**Estado de esta versión:** Baseline controlada vigente; aprobada mediante cambio controlado asociado al Issue #100.
