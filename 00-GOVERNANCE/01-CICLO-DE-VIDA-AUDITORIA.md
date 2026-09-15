# Auditoría del ciclo de vida maestro de Ingeniería de Software

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión del documento:** 0.1.0  
**Estado:** Auditoría metodológica inicial  
**Issue:** #1  
**Fecha:** 2026-09-15

---

## 1. Objetivo

Auditar el ciclo de vida maestro inicial definido para el Ecosistema Seta Expreso antes de convertirlo en el marco oficial del proyecto.

La auditoría no pretende copiar una norma. Pretende construir un ciclo de vida propio, justificable y trazable, utilizando las normas y prácticas pertinentes como referencias.

---

## 2. Referentes evaluados

### 2.1 ISO/IEC/IEEE 12207:2026

Se utilizará como referencia principal para el ciclo de vida de software. La edición 2026 establece un marco común de procesos, actividades y tareas para adquisición, suministro, desarrollo, operación, mantenimiento y disposición, y permite su aplicación de forma concurrente, iterativa, recursiva e incremental. Esto confirma que nuestro modelo no debe interpretarse como una cascada rígida. [ISO 12207:2026](https://www.iso.org/standard/90219.html)

### 2.2 ISO/IEC/IEEE 15288:2023

Debe incorporarse porque el objeto del proyecto no es únicamente software: estamos construyendo un **Ecosistema**, es decir, un sistema sociotécnico compuesto por personas, procesos, información, software, infraestructura, integraciones y otros elementos. ISO/IEC/IEEE 15288 proporciona el marco de ciclo de vida para sistemas y sistemas de sistemas. [ISO 15288:2023](https://www.iso.org/standard/81702.html)

### 2.3 ISO/IEC/IEEE 29148:2018

Referencia para ingeniería de requisitos. La edición 2018 continúa vigente tras su revisión de 2024. Además, existe actualmente un borrador DIS de una futura tercera edición; por tanto, la versión oficial aplicable al proyecto seguirá siendo 2018 hasta que la nueva edición sea publicada. [ISO 29148:2018](https://www.iso.org/standard/72089.html)

### 2.4 ISO/IEC/IEEE 42010:2022

Referencia para la estructura y expresión de las descripciones de arquitectura. No prescribe una metodología concreta de arquitectura, por lo que C4, UML, BPMN, ArchiMate u otras técnicas serán decisiones del proyecto y no requisitos automáticos de la norma. [ISO 42010:2022](https://www.iso.org/standard/74393.html)

### 2.5 ISO/IEC 25010:2023

Referencia para el modelo de calidad del producto. Sus características y subcaracterísticas pueden utilizarse para derivar requisitos de calidad, criterios de aceptación, objetivos de diseño y pruebas. [ISO 25010:2023](https://www.iso.org/standard/78176.html)

### 2.6 NIST SP 800-218 / SSDF

El SSDF se utilizará como referencia de desarrollo seguro integrada al ciclo de vida. La versión final actualmente disponible es SSDF 1.1; la versión 1.2 continúa siendo un borrador público y no se tratará como norma final. [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)

---

# 3. Hallazgo principal: el objeto de ingeniería debe definirse como sistema/ecosistema

El ciclo de vida inicial estaba expresado principalmente como un ciclo de vida de software. Eso es insuficiente para el proyecto.

El Ecosistema debe analizarse en dos niveles relacionados:

```text
NIVEL 1 — SISTEMA / ECOSISTEMA

Organización
Procesos
Personas
Información
Software
Infraestructura
Servicios externos
Integraciones
Reglas
Datos
Gobernanza

              ↓

NIVEL 2 — SOFTWARE

Aplicaciones
Servicios
Módulos
APIs
Código
Bases de datos
Pipelines
Tests
Configuración
```

**Decisión propuesta:** utilizar ISO/IEC/IEEE 15288:2023 como referencia para el nivel de sistema/ecosistema y ISO/IEC/IEEE 12207:2026 para el nivel de software.

Esto evita intentar resolver con un único ciclo de software problemas que pertenecen al nivel organizacional o sistémico.

---

# 4. Hallazgo: las 18 fases iniciales son útiles, pero mezclan niveles diferentes

El modelo inicial contenía:

1. Gobernanza e inicio
2. Descubrimiento organizacional
3. Problema y oportunidad
4. Requisitos
5. Negocio y dominio
6. Arquitectura
7. Diseño
8. Construcción
9. Verificación y validación
10. Seguridad
11. Integración
12. CI/CD y DevSecOps
13. Despliegue
14. Operación
15. Mantenimiento
16. Evolución
17. Mejora continua
18. Retirada/migración

El contenido es sólido como mapa de trabajo, pero hay una mezcla entre:

- fases del ciclo de vida;
- procesos técnicos;
- prácticas de ingeniería;
- capacidades transversales;
- mecanismos de automatización.

### Consecuencia

Si se mantiene esta clasificación sin cambios, aparecerán duplicidades. Por ejemplo, seguridad, calidad, configuración y gestión de cambios deberían actuar durante todo el ciclo, no únicamente en una fase aislada.

---

# 5. Reorganización propuesta

El ciclo de vida consolidado deberá distinguir tres categorías.

## 5.1 Fases del ciclo de vida

Representan estados o grandes conjuntos de actividades del sistema y del software.

## 5.2 Subfases / procesos de ingeniería

Describen cómo se realiza la ingeniería dentro de cada fase.

## 5.3 Procesos transversales

Atraviesan todas las fases.

```text
                 CICLO DE VIDA
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ↓               ↓                ↓
   REQUISITOS      ARQUITECTURA      CALIDAD
       │               │                │
       ├───────────────┼────────────────┤
       ↓               ↓                ↓
   SEGURIDAD         DATOS          CONFIGURACIÓN
       │               │                │
       └───────────────┼────────────────┘
                       ↓
                  TRAZABILIDAD
```

---

# 6. Fases que deberán mantenerse como núcleo

Se propone que la versión 0.2 conserve el contenido de las 18 fases, pero lo reorganice en una arquitectura metodológica más limpia.

## 6.1 Fase A — Concepción y gobernanza

Incluye:

- gobernanza;
- visión;
- contexto;
- stakeholders;
- restricciones;
- riesgos iniciales;
- viabilidad;
- estrategia de ciclo de vida.

## 6.2 Fase B — Descubrimiento del sistema y organización

Incluye:

- organización;
- procesos actuales;
- actores;
- sistemas existentes;
- información;
- infraestructura;
- problemas;
- capacidades.

## 6.3 Fase C — Necesidades, problema y objetivos

Incluye:

- problemas;
- causas;
- oportunidades;
- necesidades;
- objetivos;
- alcance;
- resultados esperados;
- business case cuando sea aplicable.

## 6.4 Fase D — Ingeniería de requisitos

Incluye:

- elicitación;
- análisis;
- especificación;
- priorización;
- reglas;
- requisitos funcionales;
- requisitos de calidad;
- restricciones;
- aceptación;
- trazabilidad;
- baseline;
- gestión de cambios.

## 6.5 Fase E — Definición y modelado del sistema

Incluye:

- modelo de negocio;
- dominio;
- procesos objetivo;
- capacidades;
- actores;
- información;
- límites del sistema;
- contexto operacional.

## 6.6 Fase F — Arquitectura

Incluye:

- arquitectura del ecosistema;
- arquitectura de negocio;
- arquitectura de información/datos;
- arquitectura de aplicaciones/software;
- integración;
- seguridad;
- infraestructura;
- despliegue;
- observabilidad;
- decisiones arquitectónicas.

## 6.7 Fase G — Diseño

Incluye:

- diseño funcional;
- diseño técnico;
- componentes;
- APIs;
- datos;
- algoritmos;
- interfaces;
- workflows;
- errores;
- configuración;
- observabilidad.

## 6.8 Fase H — Implementación / construcción

Incluye:

- código;
- configuración;
- infraestructura como código cuando proceda;
- pruebas automatizadas;
- documentación técnica;
- revisión de código;
- artefactos.

## 6.9 Fase I — Integración y verificación

Se consolidan aquí integración y parte de las actividades que antes estaban separadas.

Incluye:

- integración de componentes;
- integración de sistemas;
- pruebas de integración;
- verificación;
- pruebas automatizadas;
- análisis estático;
- compatibilidad;
- contratos.

## 6.10 Fase J — Validación y aceptación

Incluye:

- validación funcional;
- validación de calidad;
- aceptación del usuario;
- aceptación operacional;
- validación de objetivos;
- evidencia de cumplimiento.

## 6.11 Fase K — Transición y despliegue

Incluye:

- preparación del entorno;
- migraciones;
- despliegue;
- configuración;
- capacitación;
- transición operacional;
- rollback;
- aceptación de producción.

## 6.12 Fase L — Operación y soporte

Incluye:

- operación;
- observabilidad;
- incidentes;
- problemas;
- capacidad;
- disponibilidad;
- continuidad;
- backups;
- recuperación.

## 6.13 Fase M — Mantenimiento y evolución

Incluye:

- correctivo;
- adaptativo;
- perfectivo;
- preventivo;
- refactorización;
- deuda técnica;
- nuevas capacidades;
- migraciones;
- evolución arquitectónica.

## 6.14 Fase N — Mejora y optimización

Incluye:

- métricas;
- análisis;
- mejora de procesos;
- optimización técnica;
- optimización operacional;
- feedback de usuarios;
- experimentación.

## 6.15 Fase O — Retirada / migración

Incluye:

- análisis de impacto;
- estrategia de retirada;
- migración;
- archivado;
- retención de datos;
- desmantelamiento;
- auditoría final.

---

# 7. Qué ocurre con seguridad, CI/CD y DevSecOps

## 7.1 Seguridad

No debe considerarse exclusivamente una fase.

Se mantendrá como **disciplina transversal**, con actividades específicas en:

- requisitos;
- arquitectura;
- diseño;
- implementación;
- integración;
- pruebas;
- CI/CD;
- despliegue;
- operación;
- mantenimiento;
- retirada.

Puede existir además un **Security Engineering Plan** y gates específicos de seguridad.

## 7.2 CI/CD

CI/CD no constituye por sí mismo una etapa temporal del ciclo de vida.

Es un mecanismo de automatización que habilita múltiples fases, especialmente:

- construcción;
- integración;
- verificación;
- validación;
- despliegue;
- operación.

## 7.3 DevSecOps

Se tratará como un enfoque operativo transversal que integra:

```text
Development
     +
Security
     +
Operations
     +
Automation
     +
Feedback
```

---

# 8. Procesos transversales obligatorios

La versión consolidada deberá incluir explícitamente, como mínimo:

1. Gestión de proyecto.
2. Gestión de stakeholders.
3. Gestión de requisitos.
4. Gestión de arquitectura.
5. Gestión de riesgos.
6. Gestión de calidad.
7. Gestión de seguridad.
8. Gestión de configuración.
9. Gestión de cambios.
10. Gestión de información y documentación.
11. Gestión de datos.
12. Gestión de medición.
13. Gestión de decisiones.
14. Gestión de proveedores/adquisición cuando corresponda.
15. Gestión de conocimiento.
16. Gestión de trazabilidad.
17. Gestión de activos y dependencias.
18. Mejora del proceso.

---

# 9. Nuevo requisito: adquisición y suministro

ISO/IEC/IEEE 12207:2026 contempla también adquisición y suministro. Por tanto, el proyecto deberá disponer de un proceso para componentes externos cuando existan:

- proveedores SaaS;
- APIs externas;
- servicios cloud;
- librerías críticas;
- servicios de IA;
- infraestructura administrada;
- consultores;
- software de terceros.

Deberá quedar registrado:

- qué se adquiere;
- por qué;
- proveedor;
- dependencia;
- licencia/condiciones;
- riesgo;
- coste;
- criticidad;
- alternativa;
- estrategia de sustitución.

---

# 10. Nuevo requisito: ingeniería de calidad desde requisitos

La calidad no se limitará a una etapa de pruebas.

A partir de ISO/IEC 25010:2023, los atributos de calidad deberán convertirse en objetivos y requisitos medibles cuando sean relevantes.

```text
Necesidad de negocio
        ↓
Atributo de calidad
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
```

---

# 11. Nuevo requisito: arquitectura como descripción controlada

La arquitectura deberá gestionarse como un conjunto de modelos y decisiones, no como un único diagrama.

Se deberán controlar:

- stakeholders de arquitectura;
- preocupaciones;
- viewpoints;
- modelos;
- relaciones entre modelos;
- decisiones;
- versiones;
- correspondencia con requisitos.

Esto se alinea con el propósito de ISO/IEC/IEEE 42010:2022.

---

# 12. Nuevo requisito: seguridad integrada

El proyecto adoptará SSDF como referencia para prácticas de desarrollo seguro.

No se tratará SSDF como una fase aislada.

Las prácticas se asignarán a las fases y artefactos correspondientes.

La versión final del ciclo de vida deberá contener una matriz:

| Práctica de seguridad | Fase | Artefacto | Evidencia | Gate |
|---|---|---|---|---|
| Seguridad de requisitos | Requisitos | Security Requirements | Revisión | G3 |
| Threat modeling | Arquitectura/Diseño | Threat Model | Modelo validado | G4 |
| Dependency security | Construcción/CI | SBOM/Scan | Reporte | G5 |
| Security testing | Verificación | Security Test Report | Resultados | G7 |
| Runtime security | Operación | Monitoring/Alerts | Evidencia | G8 |

La tabla anterior es una estructura inicial; los controles concretos se definirán posteriormente.

---

# 13. Artefactos: de lista a sistema documental

No basta con enumerar documentos. Cada artefacto deberá tener:

- identificador;
- propósito;
- propietario;
- entradas;
- contenido mínimo;
- formato;
- versión;
- estado;
- relaciones;
- criterios de aprobación;
- ubicación en GitHub;
- evidencia asociada.

Esto permitirá construir posteriormente un **Architecture/Engineering Information Model** del proyecto.

---

# 14. GitHub como sistema de evidencia

El repositorio será tratado como parte de la infraestructura de ingeniería.

La trazabilidad objetivo será:

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

No todos los artefactos deberán reducirse a commits, pero todos los artefactos controlados deberán tener una ubicación y una relación documental definida.

---

# 15. Criterios para la versión 0.2

La siguiente versión del ciclo de vida deberá:

- incorporar explícitamente el nivel de sistema/ecosistema;
- mantener el nivel de software;
- reorganizar las 18 fases iniciales en una estructura coherente;
- mover seguridad a transversal;
- mover CI/CD/DevSecOps a transversal/enabling process;
- consolidar integración y verificación donde resulte coherente;
- separar verificación de validación;
- incorporar adquisición/suministro;
- incorporar calidad como disciplina desde requisitos;
- formalizar arquitectura como descripción controlada;
- definir artefactos y evidencias;
- definir gates;
- definir trazabilidad;
- mantener iteración, concurrencia, recursividad e incrementalidad;
- conservar capacidad de evolución y retirada.

---

# 16. Decisiones todavía NO tomadas

Esta auditoría no autoriza todavía decisiones sobre:

- lenguaje de programación;
- framework backend;
- framework frontend;
- motor de base de datos;
- cloud provider;
- Kubernetes;
- Docker como tecnología obligatoria;
- proveedor de IA;
- estrategia de microservicios;
- arquitectura monolítica/modular/distribuida;
- herramientas concretas de CI/CD.

Estas decisiones deberán derivarse de requisitos, restricciones, atributos de calidad, riesgos y coste.

---

# 17. Resultado de la auditoría

### Estado: APROBACIÓN CONDICIONADA

El ciclo de vida inicial es suficientemente completo como **mapa conceptual**, pero no debe congelarse todavía como versión oficial.

La principal modificación requerida es pasar de un modelo predominantemente orientado a software a un **modelo de ingeniería de sistemas/ecosistemas con una capa explícita de ingeniería de software**.

La siguiente versión deberá ser `v0.2.0` y constituirá la primera versión consolidada del ciclo de vida.

---

# 18. Fuentes normativas y técnicas

- ISO/IEC/IEEE 12207:2026 — Software life cycle processes.
- ISO/IEC/IEEE 15288:2023 — System life cycle processes.
- ISO/IEC/IEEE 29148:2018 — Requirements engineering.
- ISO/IEC/IEEE 42010:2022 — Architecture description.
- ISO/IEC 25010:2023 — Product quality model.
- NIST SP 800-218 — Secure Software Development Framework.
- DORA — Software delivery performance metrics.

---

# 19. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-09-15 | Auditoría metodológica inicial y propuesta de consolidación |
