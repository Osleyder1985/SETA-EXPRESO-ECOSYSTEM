# Supplier / Third-Party Governance — Análisis De Impacto

**Versión:** 0.1.0  
**Issue:** #41  
**Estado:** Análisis inicial controlado  
**Fecha:** 2026-09-15

## 1. Objetivo

Determinar qué artefactos existentes se relacionan con la nueva capacidad de Supplier / Third-Party Governance y cuáles deben actualizarse ahora o quedar como evolución trazable.

## 2. Artefactos afectados

| Área | Relación | Acción |
|---|---|---|
| Lifecycle | 12207 incluye adquisición y suministro | Integrar en matriz de estándares |
| Governance Control | Nuevo dominio de control transversal | Actualizar matriz de governance |
| Risk Management | Vendor Risk alimenta riesgos | Integración documental |
| Decision Governance | Selección, excepción y aceptación requieren decisiones | Integración documental |
| Security Governance | Evaluación de proveedores y supply chain security | Integración documental |
| Data Governance | Terceros pueden acceder/procesar datos | Integración documental |
| AI Governance | Servicios/proveedores de IA requieren controles específicos | Integración documental |
| Quality Governance | SLA, disponibilidad y soporte pueden convertirse en requisitos | Integración conceptual |
| Evidence Governance | Contratos, atestaciones, licencias y evaluaciones son evidencia | Integración conceptual |
| Metrics Governance | Cobertura y estado de proveedores pueden medirse | Integración conceptual |
| Architecture | Dependencias externas y límites del sistema | Integración futura con arquitectura real |
| Operations | Onboarding, monitorización, incidentes y salida | Evolución durante K–O |

## 3. Cambios realizados en esta unidad

- Baseline formal de Supplier / Third-Party Governance.
- Matriz de controles SP-001..SP-030.
- Registro controlado de terceros.
- Registro de riesgos de proveedores.
- Registro de SLA y controles contractuales.
- Registro de evaluaciones de seguridad.
- Registro de licencias.
- Registro de dependencias.
- Registro de estrategias de salida.
- Actualización de la matriz de estándares.
- Actualización de la matriz general de Governance.

## 4. Trabajo deliberadamente pendiente

No se inventan proveedores, contratos, SLA, certificaciones, licencias, dependencias ni valores de riesgo. Su incorporación queda trazada para B–F y, cuando corresponda, para G–O.

También queda pendiente la automatización especializada de SCA/SBOM, seguimiento contractual, monitorización de SLA, evaluación periódica y evidencias de exit readiness, porque requieren contexto y activos reales.

## 5. Criterio de cierre

El impacto se considera cubierto documentalmente cuando las relaciones con Governance, Risk, Security, Data, AI, Quality, Evidence, Metrics, Decision Governance, Architecture y Operations están explícitamente identificadas y los cambios necesarios de esta unidad están trazados.
