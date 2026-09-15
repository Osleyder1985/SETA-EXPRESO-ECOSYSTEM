# Supplier / Third-Party Governance — Análisis De Impacto

**Versión:** 0.1.1  
**Issue:** #41  
**Estado:** Análisis inicial controlado  
**Fecha:** 2026-09-15

## 1. Objetivo

Determinar qué artefactos existentes se relacionan con la nueva capacidad de Supplier / Third-Party Governance y cuáles deben actualizarse ahora o quedar como evolución trazable.

## 2. Artefactos afectados

| Área | Relación | Acción |
|---|---|---|
| Lifecycle | 12207 incluye adquisición y suministro | Actualización de `02-Standards-Lifecycle-Matrix.md` |
| Governance Control | Nuevo dominio de control transversal | Integración documentada en `32-Supplier-Third-Party-Integration-Map.md` |
| Risk Management | Vendor Risk alimenta riesgos | Integración documentada |
| Decision Governance | Selección, excepción y aceptación requieren decisiones | Integración documentada |
| Security Governance | Evaluación de proveedores y supply chain security | Integración documentada |
| Data Governance | Terceros pueden acceder/procesar datos | Integración documentada |
| AI Governance | Servicios/proveedores de IA requieren controles específicos | Integración documentada |
| Quality Governance | SLA, disponibilidad y soporte pueden convertirse en requisitos | Integración documentada |
| Evidence Governance | Contratos, atestaciones, licencias y evaluaciones son evidencia | Integración documentada |
| Metrics Governance | Cobertura y estado de proveedores pueden medirse | Integración documentada |
| Architecture | Dependencias externas y límites del sistema | Integración documentada; detalle futuro con arquitectura real |
| Operations | Onboarding, monitorización, incidentes y salida | Integración documentada; ejecución futura |

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
- Mapa explícito de integración transversal.
- Registro de estado de la capacidad.

## 4. Trabajo deliberadamente pendiente

No se inventan proveedores, contratos, SLA, certificaciones, licencias, dependencias ni valores de riesgo. Su incorporación queda trazada para B–F y, cuando corresponda, para G–O.

También queda pendiente la automatización especializada de SCA/SBOM, seguimiento contractual, monitorización de SLA, evaluación periódica y evidencias de exit readiness, porque requieren contexto y activos reales.

## 5. Criterio de cierre

El impacto se considera cubierto documentalmente cuando las relaciones con Governance, Risk, Security, Data, AI, Quality, Evidence, Metrics, Decision Governance, Architecture y Operations están explícitamente identificadas y los cambios necesarios de esta unidad están trazados.
