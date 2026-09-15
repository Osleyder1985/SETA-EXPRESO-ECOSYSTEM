# Ciclo de Vida Maestro de Ingeniería de Software y del Ecosistema

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.2.0  
**Estado:** Borrador consolidado para aprobación  
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
O.7 Revocación de accesos y dependencias.  
O.8 Validación post-retirada.  
O.9 Auditoría final.  
O.10 Cierre y preservación de evidencia.

## 6. Procesos transversales

Los siguientes procesos atraviesan todas las fases según aplicabilidad:

### 6.1 Stakeholder Management
Identificación, análisis, comunicación, participación y seguimiento de stakeholders.

### 6.2 Requirements Management
Gestión de necesidades, requisitos, baselines, cambios y trazabilidad.

### 6.3 Architecture Management
Gestión de modelos, viewpoints, decisiones, principios, riesgos y baselines arquitectónicas.

### 6.4 Risk Management
Identificación, análisis, respuesta, seguimiento y cierre de riesgos y oportunidades.

### 6.5 Quality Management
Definición de objetivos, métricas, criterios, revisiones, controles y mejora.

### 6.6 Security Engineering
Seguridad de requisitos, threat modeling, secure design, secure coding, supply-chain security, testing, deployment y operación.

### 6.7 Configuration Management
Control de versiones, baselines, configuraciones, artefactos y elementos controlados.

### 6.8 Change Management
Evaluación, autorización, implementación y verificación de cambios.

### 6.9 Data Management
Gobernanza, calidad, seguridad, ciclo de vida, migración y trazabilidad de datos.

### 6.10 Measurement
Definición de métricas, recolección, análisis, interpretación y uso para decisiones.

### 6.11 Decision Management
Registro de decisiones significativas, alternativas consideradas, criterios y consecuencias.

### 6.12 Information and Documentation Management
Creación, revisión, aprobación, versionado, publicación, archivado y preservación de documentación.

### 6.13 Acquisition and Supply
Evaluación y gestión de productos, servicios, proveedores y dependencias externas.

### 6.14 Dependency and Asset Management
Inventario y control de software de terceros, servicios, licencias, activos y dependencias críticas.

### 6.15 Knowledge Management
Conservación y transferencia de conocimiento técnico, operacional y organizacional.

### 6.16 Process Improvement
Evaluación y evolución del propio proceso de ingeniería.

## 7. Calidad del producto

La calidad se gestionará desde la definición de necesidades y requisitos. Los atributos relevantes se convertirán, cuando sea posible, en requisitos medibles, decisiones de diseño, pruebas, métricas y criterios de aceptación.

```text
Necesidad
   ↓
Objetivo de calidad
   ↓
Requisito medible
   ↓
Diseño
   ↓
Implementación
   ↓
Prueba
   ↓
Métrica
   ↓
Aceptación
   ↓
Medición operacional
```

ISO/IEC 25010:2023 será la referencia de modelo de calidad; la selección concreta de atributos y métricas dependerá del contexto del Ecosistema.

## 8. Seguridad

La seguridad se integra durante todo el ciclo y se apoya en NIST SP 800-218 / SSDF 1.1 como referencia de prácticas de desarrollo seguro.

Como mínimo se considerarán, según aplicabilidad:

- seguridad de requisitos;
- threat modeling;
- secure architecture;
- secure design;
- secure coding;
- dependency and supply-chain security;
- secret management;
- static and dynamic analysis;
- vulnerability management;
- security testing;
- secure deployment;
- logging and monitoring;
- incident response;
- security maintenance;
- secure retirement.

## 9. Adquisición y suministro

Todo componente externo relevante deberá evaluarse antes de incorporarse al Ecosistema. La evaluación podrá incluir:

- propósito;
- proveedor;
- dependencia;
- criticidad;
- coste;
- licencia y condiciones de uso;
- seguridad;
- privacidad cuando aplique;
- disponibilidad;
- lock-in;
- soporte;
- riesgo de continuidad;
- alternativa;
- estrategia de sustitución o salida.

## 10. Artefactos y evidencia

Cada actividad relevante debe producir el artefacto o evidencia proporcional a su importancia.

Categorías mínimas:

| Categoría | Ejemplos |
|---|---|
| Gobernanza | Charter, políticas, registros |
| Negocio | Problemas, objetivos, procesos |
| Requisitos | Necesidades, requisitos, aceptación |
| Arquitectura | Descripción, modelos, ADRs |
| Diseño | Diseños detallados, contratos, modelos |
| Construcción | Código, configuración, builds |
| Verificación | Planes, pruebas, resultados |
| Validación | Aceptación, evidencias de uso |
| Seguridad | Threat models, análisis, findings |
| DevOps | Pipelines, releases, deployment evidence |
| Operación | Runbooks, incidentes, métricas |
| Datos | Modelos, migraciones, calidad |
| Investigación | Datasets, protocolos, resultados |

## 11. Trazabilidad

La trazabilidad mínima seguirá el principio:

```text
Business Need
    ↓
Objective
    ↓
System Need
    ↓
Requirement
    ↓
Architecture Decision
    ↓
Design Element
    ↓
Implementation
    ↓
Test
    ↓
Validation
    ↓
Release
    ↓
Operational Evidence
```

La implementación concreta utilizará identificadores estables para elementos que necesiten trazabilidad persistente.

## 12. GitHub como infraestructura de ingeniería

El repositorio será la fuente controlada de código, documentación, decisiones, modelos, pruebas, configuración y evidencia que pueda mantenerse de forma apropiada en Git.

La cadena de evidencia esperada es:

```text
Problema
  ↓
Objetivo
  ↓
Requisito
  ↓
Issue
  ↓
Diseño / ADR
  ↓
Pull Request
  ↓
Commit
  ↓
Test
  ↓
Release
  ↓
Evidencia operacional
```

No todo artefacto físico o confidencial debe almacenarse directamente en GitHub; cuando corresponda, el repositorio conservará su referencia, metadatos, hash, ubicación controlada y evidencia de existencia.

## 13. Convención de estructura y nombres

### 13.1 Estructura

Los directorios y nombres de archivo utilizarán inglés. La documentación será escrita principalmente en español.

```text
SETA-EXPRESO-ECOSYSTEM/
├── README.md
├── Docs/
├── Source/
├── Tests/
├── Infrastructure/
├── Configuration/
├── Scripts/
└── .github/
```

### 13.2 Nombres

Regla: prefijo numérico cuando exista orden documental + palabras en inglés con inicial mayúscula + guiones + extensión en minúscula.

Ejemplo:

`01-Software-Lifecycle-Audit.md`

No se utilizarán formas como `01-CICLO-DE-VIDA-AUDITORIA.md`, `software_lifecycle_audit.md` o `software-lifecycle-audit.md` para los artefactos controlados del proyecto.

### 13.3 Documentación

Toda documentación del proyecto debe residir bajo `Docs/`, organizada por dominio.

## 14. Quality Gates

Los gates representan puntos de control; no necesariamente son únicos ni impiden iteraciones adicionales.

| Gate | Nombre | Propósito |
|---|---|---|
| G0 | Governance Ready | Gobierno y reglas mínimas establecidas |
| G1 | Discovery Ready | Comprensión suficiente del estado actual |
| G2 | Problem and Objectives Ready | Problema, necesidades y objetivos definidos |
| G3 | Requirements Baseline | Requisitos verificables y trazables |
| G4 | System Definition Ready | Sistema objetivo y contexto definidos |
| G5 | Architecture Baseline | Arquitectura evaluada y controlada |
| G6 | Design Ready | Diseño suficientemente detallado |
| G7 | Build Ready | Construcción y controles automatizados establecidos |
| G8 | Verification Ready | Evidencia de verificación aceptable |
| G9 | Validation Accepted | Validación y aceptación logradas |
| G10 | Production Ready | Despliegue y operación preparados |
| G11 | Operationally Stable | Operación estable y observable |
| G12 | Evolution Ready | Cambio/evolución evaluados y controlados |
| G13 | Retirement Complete | Retirada/migración completada y evidencia preservada |

Los criterios concretos de cada gate se definirán en `Docs/Governance/04-Quality-Gates.md`.

## 15. Versionado y configuración

El proyecto utilizará control de versiones para código y documentación. Los cambios relevantes deberán ser identificables y asociables con su razón de cambio.

Las baselines importantes deberán incluir:

- versión;
- fecha;
- responsable;
- estado;
- alcance;
- elementos incluidos;
- decisiones asociadas;
- evidencia de aprobación.

## 16. Decisiones arquitectónicas y de ingeniería

Las decisiones con impacto significativo deben registrarse como ADRs o en el mecanismo de decisión que el proyecto establezca.

Cada decisión debe incluir, cuando aplique:

- contexto;
- problema;
- opciones;
- criterios;
- decisión;
- consecuencias;
- riesgos;
- alternativas descartadas;
- referencias.

## 17. Métricas

Las métricas se definirán según objetivos y decisiones, evitando recopilar datos sin propósito.

Podrán incluir, según la fase:

- cobertura de requisitos;
- defectos;
- tiempos de ciclo;
- frecuencia de despliegue;
- tasa de cambios fallidos;
- recuperación ante fallos;
- disponibilidad;
- rendimiento;
- vulnerabilidades;
- calidad de datos;
- satisfacción de usuarios;
- coste operacional;
- deuda técnica;
- indicadores de proceso.

No se congelará una taxonomía única de métricas de entrega hasta evaluar el contexto y las fuentes disponibles.

## 18. Integración con investigación científica

El proyecto puede producir posteriormente conocimiento científico, pero ingeniería y ciencia mantendrán objetivos y criterios diferentes.

La cadena prevista es:

```text
Ingeniería de Software
       ↓
Sistema real
       ↓
Datos / observaciones
       ↓
Problema de investigación
       ↓
Pregunta científica
       ↓
Hipótesis
       ↓
Experimento / estudio
       ↓
Análisis
       ↓
Resultados
       ↓
Nuevo conocimiento
       ↓
Publicación
```

Cuando una actividad del proyecto tenga potencial científico, la evidencia deberá conservarse con suficiente trazabilidad para permitir posteriormente un protocolo de investigación reproducible, sin alterar artificialmente la ingeniería para producir una publicación.

## 19. Regla de completitud

Una fase o cambio significativo no se considerará completo únicamente porque el software funcione.

La completitud debe evaluarse respecto de:

```text
Objetivo
+ Requisitos
+ Calidad
+ Seguridad
+ Diseño
+ Implementación
+ Verificación
+ Validación
+ Operación
+ Evidencia
+ Trazabilidad
```

La profundidad exigida será proporcional al riesgo y al impacto.

## 20. Adaptación del ciclo

El ciclo podrá adaptarse por producto, componente, release, iniciativa o cambio. La adaptación deberá quedar documentada cuando modifique controles, artefactos, gates o responsabilidades esperadas.

La adaptación no debe eliminar controles críticos sin una justificación explícita basada en riesgo, contexto y consecuencias.

## 21. Estado de esta versión

La versión **0.2.0** es el borrador consolidado resultante de la auditoría metodológica inicial.

Antes de declararla baseline oficial deberán revisarse y aprobarse como mínimo:

1. este documento;
2. la matriz de estándares;
3. el catálogo de artefactos y evidencias;
4. los quality gates;
5. la convención documental y de repositorio.

Una vez aprobados, el ciclo de vida se convertirá en la referencia normativa interna del proyecto y cualquier modificación posterior deberá seguir control de cambios.

---

## 22. Referencias normativas y técnicas

- ISO/IEC/IEEE 15288:2023 — Systems and software engineering — System life cycle processes.
- ISO/IEC/IEEE 12207:2026 — Systems and software engineering — Software life cycle processes.
- ISO/IEC/IEEE 29148:2018 — Systems and software engineering — Life cycle processes — Requirements engineering.
- ISO/IEC/IEEE 42010:2022 — Software, systems and enterprise — Architecture description.
- ISO/IEC 25010:2023 — Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model.
- NIST SP 800-218 / Secure Software Development Framework (SSDF) Version 1.1.

**Nota:** las referencias se utilizan para alineación y criterio de ingeniería. No se reproducen textos normativos protegidos ni se asume conformidad normativa automática por el simple hecho de utilizar este marco.
