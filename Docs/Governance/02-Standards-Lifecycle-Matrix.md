# Matriz de alineación del ciclo de vida con estándares y referencias

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.4.0  
**Estado:** Matriz controlada en evolución  
**Fecha:** 2026-09-15

---

## 1. Propósito

Esta matriz documenta cómo se utilizan las principales referencias normativas y técnicas para diseñar el ciclo de vida del Ecosistema.

No constituye una declaración de conformidad normativa. La correspondencia se expresa a nivel de propósito y proceso, evitando inventar correspondencias con cláusulas que no hayan sido verificadas contra el texto completo de una norma.

## 2. Referencias

| Referencia | Uso en el proyecto |
|---|---|
| ISO/IEC/IEEE 15288:2023 | Marco principal para el nivel sistema/ecosistema |
| ISO/IEC/IEEE 12207:2026 | Marco principal para el nivel software; adquisición y suministro |
| ISO/IEC/IEEE 29148:2018 | Ingeniería de requisitos |
| ISO/IEC/IEEE 42010:2022 | Descripción y gestión de arquitectura |
| ISO/IEC 25010:2023 | Modelo de calidad del producto |
| NIST SP 800-218 / SSDF 1.1 | Desarrollo seguro y supply-chain security |
| ISO 31000:2018 | Principios, marco y proceso general de gestión de riesgos |
| IEC 31010:2019 | Técnicas de evaluación de riesgos cuando se requieran métodos específicos |
| ISO/IEC 42001:2023 | Sistema de gestión de inteligencia artificial (AIMS) |
| ISO/IEC 23894:2023 | Gestión de riesgos específica de inteligencia artificial |
| NIST AI RMF 1.0 | Gestión de riesgos y confianza en sistemas de IA |
| NIST AI 600-1 | Perfil de gestión de riesgos para IA generativa |
| ISO/IEC 27036-2:2022 | Requisitos de seguridad para relaciones con proveedores |
| ISO/IEC 27036-3:2023 | Seguridad de la cadena de suministro de hardware, software y servicios |
| ISO/IEC 27036-4:2016 | Seguridad en relaciones con proveedores de servicios cloud |

## 3. Matriz de aplicación

| Área / fase | 15288 | 12207 | 29148 | 42010 | 25010 | SSDF | ISO 31000 | IEC 31010 | 27036 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A. Concepción y gobernanza | ✓ | ✓ |  |  |  |  | ✓ | ✓ | ✓ |
| B. Descubrimiento | ✓ | ✓ |  |  |  |  | ✓ | ✓ | ✓ |
| C. Necesidades, problema y objetivos | ✓ | ✓ | ✓ |  | ✓ |  | ✓ | ✓ | ✓ |
| D. Ingeniería de requisitos | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| E. Definición y modelado del sistema | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |
| F. Arquitectura | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| G. Diseño | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| H. Implementación y construcción | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| I. Integración y verificación | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| J. Validación y aceptación | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| K. Transición y despliegue | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| L. Operación y soporte | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| M. Mantenimiento y evolución | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| N. Mejora y optimización | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| O. Retirada y migración | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |

AI Governance añade una capa transversal sobre estas fases: identificación, evaluación, aprobación, operación, monitorización, incident management y retiro de capacidades de IA.

Supplier / Third-Party Governance añade una capa transversal sobre adquisición, suministro, evaluación de proveedores, seguridad de la cadena de suministro, dependencia, contratos, monitorización, continuidad y salida.

## 4. Interpretación

### ISO/IEC/IEEE 15288:2023

Se utiliza para mantener una perspectiva de sistema y ecosistema. Es especialmente relevante para necesidades de stakeholders, definición del sistema, arquitectura, integración, validación, operación, mantenimiento y retirada.

### ISO/IEC/IEEE 12207:2026

Se utiliza para estructurar el ciclo de vida y los procesos específicos de software, incluyendo adquisición, suministro, desarrollo, operación, mantenimiento y disposición.

### ISO/IEC/IEEE 29148:2018

Se utiliza para orientar la ingeniería de requisitos y la gestión de la información asociada. La edición 2018 es la referencia oficial utilizada mientras una futura edición no haya sido publicada como estándar.

### ISO/IEC/IEEE 42010:2022

Se utiliza para estructurar la descripción de arquitectura mediante stakeholders, concerns, viewpoints, modelos y relaciones, sin imponer una metodología concreta.

### ISO/IEC 25010:2023

Se utiliza para seleccionar características de calidad pertinentes y convertirlas, cuando corresponda, en requisitos, objetivos de diseño, pruebas, métricas y criterios de aceptación.

### NIST SP 800-218 / SSDF 1.1

Se utiliza como referencia de prácticas de desarrollo seguro y para incorporar consideraciones de adquisición y riesgo de cadena de suministro de software.

### ISO 31000:2018

Se utiliza como referencia principal para estructurar la gestión de riesgos del Ecosistema: contexto, identificación, análisis, evaluación, tratamiento, comunicación, seguimiento y revisión.

### IEC 31010:2019

Se utiliza como referencia complementaria para seleccionar técnicas de evaluación de riesgos cuando el contexto requiera métodos más específicos que la escala cualitativa 1–5 adoptada inicialmente por el Risk Management System.

### ISO/IEC 42001:2023

Se utiliza como referencia para estructurar la capacidad de gestión de IA: políticas, objetivos, responsabilidades, procesos, evaluación, tratamiento de riesgos y mejora continua. La adopción de sus conceptos no constituye certificación ni declaración de conformidad.

### ISO/IEC 23894:2023

Se utiliza como referencia específica para integrar la gestión de riesgos de IA con las actividades y funciones de la organización que desarrollen, produzcan, desplieguen o utilicen productos, sistemas o servicios con IA.

### NIST AI RMF 1.0

Se utiliza como referencia práctica para gobernar, mapear, medir y gestionar riesgos de IA. Su aplicación se integra con Risk Management, Security, Quality, Evidence y Decision Governance. NIST mantiene el AI RMF como recurso vivo y su revisión futura deberá ser monitorizada.

### NIST AI 600-1

Se utiliza como referencia complementaria para riesgos específicos de IA generativa cuando el Ecosistema utilice capacidades generativas. No se presupone que todo caso de uso futuro sea generativo.

### ISO/IEC 27036-2:2022

Se utiliza para estructurar requisitos de seguridad aplicables a relaciones entre adquirentes y proveedores, incluyendo definición, implementación, operación, monitorización, revisión, mantenimiento y mejora de dichas relaciones.

### ISO/IEC 27036-3:2023

Se utiliza para gestionar riesgos de seguridad derivados de cadenas de suministro de hardware, software y servicios, incluyendo visibilidad de proveedores y niveles inferiores de suministro cuando sean relevantes.

### ISO/IEC 27036-4:2016

Se utiliza como referencia específica para relaciones con proveedores de servicios cloud y los riesgos de seguridad asociados a su adquisición y provisión.

## 5. Regla de actualización

Esta matriz deberá actualizarse cuando:

- se incorpore una nueva referencia relevante;
- cambie una edición normativa aplicable;
- se modifique el ciclo de vida;
- se introduzca un proceso nuevo;
- una auditoría detecte una brecha;
- una decisión de ingeniería cambie la forma de aplicar una referencia;
- aparezca un caso de uso de IA que requiera una referencia adicional;
- aparezca un proveedor, servicio externo o dependencia que requiera una referencia adicional.

Las correspondencias a cláusulas específicas solo deberán añadirse después de verificar el texto oficial de la edición correspondiente.
