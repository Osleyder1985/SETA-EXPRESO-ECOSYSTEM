# Matriz de alineación del ciclo de vida con estándares y referencias

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Matriz inicial  
**Fecha:** 2026-09-15

---

## 1. Propósito

Esta matriz documenta cómo se utilizan las principales referencias normativas y técnicas para diseñar el ciclo de vida del Ecosistema.

No constituye una declaración de conformidad normativa. La correspondencia se expresa a nivel de propósito y proceso, evitando inventar correspondencias con cláusulas que no hayan sido verificadas contra el texto completo de una norma.

## 2. Referencias

| Referencia | Uso en el proyecto |
|---|---|
| ISO/IEC/IEEE 15288:2023 | Marco principal para el nivel sistema/ecosistema |
| ISO/IEC/IEEE 12207:2026 | Marco principal para el nivel software |
| ISO/IEC/IEEE 29148:2018 | Ingeniería de requisitos |
| ISO/IEC/IEEE 42010:2022 | Descripción y gestión de arquitectura |
| ISO/IEC 25010:2023 | Modelo de calidad del producto |
| NIST SP 800-218 / SSDF 1.1 | Desarrollo seguro |

## 3. Matriz de aplicación

| Área / fase | 15288 | 12207 | 29148 | 42010 | 25010 | SSDF |
|---|---:|---:|---:|---:|---:|---:|
| A. Concepción y gobernanza | ✓ | ✓ |  |  |  |  |
| B. Descubrimiento | ✓ | ✓ |  |  |  |  |
| C. Necesidades, problema y objetivos | ✓ | ✓ | ✓ |  | ✓ |  |
| D. Ingeniería de requisitos | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| E. Definición y modelado del sistema | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| F. Arquitectura | ✓ | ✓ |  | ✓ | ✓ | ✓ |
| G. Diseño | ✓ | ✓ |  | ✓ | ✓ | ✓ |
| H. Implementación y construcción | ✓ | ✓ |  |  | ✓ | ✓ |
| I. Integración y verificación | ✓ | ✓ |  |  | ✓ | ✓ |
| J. Validación y aceptación | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| K. Transición y despliegue | ✓ | ✓ |  |  | ✓ | ✓ |
| L. Operación y soporte | ✓ | ✓ |  |  | ✓ | ✓ |
| M. Mantenimiento y evolución | ✓ | ✓ |  |  | ✓ | ✓ |
| N. Mejora y optimización | ✓ | ✓ |  |  | ✓ | ✓ |
| O. Retirada y migración | ✓ | ✓ |  |  | ✓ | ✓ |

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

Se utiliza como referencia de prácticas de desarrollo seguro integradas en las fases y controles del ciclo de vida.

## 5. Regla de actualización

Esta matriz deberá actualizarse cuando:

- se incorpore una nueva referencia relevante;
- cambie una edición normativa aplicable;
- se modifique el ciclo de vida;
- se introduzca un proceso nuevo;
- una auditoría detecte una brecha;
- una decisión de ingeniería cambie la forma de aplicar una referencia.

Las correspondencias a cláusulas específicas solo deberán añadirse después de verificar el texto oficial de la edición correspondiente.
