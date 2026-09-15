# Auditoría del ciclo de vida maestro de Ingeniería de Software

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Auditoría metodológica inicial  
**Issue:** #1  
**Fecha:** 2026-09-15

---

## 1. Objetivo

Auditar el ciclo de vida maestro inicial del Ecosistema antes de convertirlo en el marco oficial del proyecto. La auditoría busca construir un ciclo de vida propio, justificable y trazable, utilizando normas y prácticas reconocidas como referencias, sin copiar mecánicamente ninguna norma.

## 2. Referentes evaluados

- **ISO/IEC/IEEE 15288:2023:** referencia para el nivel sistema/ecosistema y sistemas de sistemas.
- **ISO/IEC/IEEE 12207:2026:** referencia para el nivel software y sus procesos de ciclo de vida.
- **ISO/IEC/IEEE 29148:2018:** referencia para ingeniería de requisitos.
- **ISO/IEC/IEEE 42010:2022:** referencia para descripción de arquitectura.
- **ISO/IEC 25010:2023:** referencia para calidad del producto.
- **NIST SP 800-218 / SSDF 1.1:** referencia para desarrollo seguro.

Las referencias normativas se utilizan como marco de alineación; el proyecto mantiene la responsabilidad de definir su método, artefactos, evidencias y criterios de adaptación.

## 3. Hallazgo principal: doble nivel de ingeniería

El proyecto no es únicamente una aplicación. El objeto de ingeniería es un ecosistema sociotécnico compuesto, según corresponda, por organización, personas, procesos, información, software, infraestructura, datos, integraciones y servicios externos.

Por ello se adopta un modelo de dos niveles:

```text
Nivel 1 — Sistema / Ecosistema
Organización · Personas · Procesos · Información · Software · Infraestructura
Servicios externos · Integraciones · Datos · Gobernanza

                    ↓

Nivel 2 — Software
Aplicaciones · Servicios · Módulos · APIs · Código · Bases de datos
Pipelines · Pruebas · Configuración
```

**Decisión:** ISO/IEC/IEEE 15288:2023 será la referencia sistémica y ISO/IEC/IEEE 12207:2026 la referencia principal de software.

## 4. Hallazgo sobre las 18 fases iniciales

El modelo inicial era sólido como mapa de trabajo, pero mezclaba fases de ciclo de vida, procesos técnicos, disciplinas transversales y mecanismos de automatización.

Esto generaba riesgos de duplicidad. Seguridad, calidad, configuración, cambios, riesgos y trazabilidad deben atravesar el ciclo; CI/CD y DevSecOps son mecanismos/enfoques habilitadores, no etapas temporales independientes.

## 5. Reorganización aprobada para el borrador consolidado

Se establece una estructura de **15 fases principales**, identificadas de A a O:

A. Concepción y gobernanza  
B. Descubrimiento del sistema y organización  
C. Necesidades, problema y objetivos  
D. Ingeniería de requisitos  
E. Definición y modelado del sistema  
F. Arquitectura  
G. Diseño  
H. Implementación y construcción  
I. Integración y verificación  
J. Validación y aceptación  
K. Transición y despliegue  
L. Operación y soporte  
M. Mantenimiento y evolución  
N. Mejora y optimización  
O. Retirada y migración

## 6. Disciplinas transversales

Como mínimo se gestionarán transversalmente:

1. Gobernanza y gestión del proyecto.
2. Stakeholders.
3. Requisitos y trazabilidad.
4. Arquitectura y decisiones.
5. Riesgos y oportunidades.
6. Calidad.
7. Seguridad.
8. Configuración.
9. Cambios.
10. Información y documentación.
11. Datos.
12. Medición.
13. Decisiones.
14. Adquisición y suministro.
15. Dependencias y activos.
16. Conocimiento.
17. Mejora del proceso.

## 7. Decisiones metodológicas derivadas de la auditoría

### 7.1 Seguridad transversal

La seguridad no será una fase aislada. Existirán actividades y gates de seguridad en requisitos, arquitectura, diseño, construcción, integración, validación, despliegue, operación, mantenimiento y retirada.

### 7.2 CI/CD y DevSecOps como habilitadores

CI/CD se tratará como automatización del flujo de ingeniería. DevSecOps se tratará como enfoque integrado de desarrollo, seguridad, operaciones, automatización y feedback.

### 7.3 Verificación separada de validación

La verificación responderá principalmente a si el producto fue construido correctamente respecto de sus especificaciones. La validación responderá a si el sistema satisface necesidades, objetivos y uso previsto.

### 7.4 Calidad desde requisitos

Los objetivos de calidad se derivarán de necesidades y se convertirán, cuando corresponda, en requisitos medibles, decisiones de diseño, pruebas, métricas y criterios de aceptación.

### 7.5 Arquitectura como descripción controlada

La arquitectura se gestionará mediante stakeholders, concerns, viewpoints, modelos, relaciones, decisiones, versiones y trazabilidad; no como un conjunto informal de diagramas.

### 7.6 Adquisición y suministro

Las dependencias externas relevantes —SaaS, cloud, APIs, IA, librerías, infraestructura administrada, consultoría y otros proveedores— deberán tener justificación, criticidad, riesgo, condiciones, coste y estrategia de sustitución o salida cuando aplique.

### 7.7 Naturaleza iterativa del ciclo

El ciclo no se interpretará como cascada rígida. Las actividades podrán ejecutarse de forma iterativa, incremental, concurrente y recursiva según el contexto, riesgo y naturaleza del trabajo.

## 8. Cadena de evidencia

El repositorio GitHub será parte de la infraestructura de ingeniería y de la evidencia del proyecto:

```text
Problema
  ↓
Objetivo
  ↓
Necesidad / Requisito
  ↓
Issue
  ↓
Diseño / Decisión
  ↓
Pull Request
  ↓
Commit
  ↓
Prueba / Evidencia
  ↓
Release
  ↓
Evidencia operacional
```

## 9. Resultado de la auditoría

**APROBACIÓN CONDICIONADA.** El ciclo de vida inicial es conceptualmente válido, pero no debe congelarse como versión oficial hasta incorporar el modelo sistema + software, las 15 fases consolidadas, las disciplinas transversales, adquisición/suministro, calidad desde requisitos, arquitectura controlada, gates y trazabilidad.

El siguiente artefacto rector es `Docs/Governance/00-Software-Lifecycle-Master.md`, versión 0.2.0.
