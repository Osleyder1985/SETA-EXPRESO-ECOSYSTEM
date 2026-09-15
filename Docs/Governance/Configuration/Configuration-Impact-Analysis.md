# Análisis de impacto — Configuration Management

**Issue:** #45  
**Estado:** Propuesto

## Cambio

Introducción formal de Configuration Item Management.

## Artefactos afectados

| Área | Impacto |
|---|---|
| Change Control | CM pasa a formar parte explícita del control de cambios. |
| Artifacts & Evidence | Los CIs requieren identificación, versión y evidencia. |
| Quality Gates | Los Gates podrán usar estado de configuración como entrada. |
| Risk Management | La pérdida de control de configuración se convierte en riesgo gestionable. |
| Decision Governance | Cambios materiales de configuración pueden requerir ADR/EDR. |
| Metrics Governance | Podrán derivarse métricas de cobertura de CIs, baselines y trazabilidad. |
| Security Governance | Security Baseline se convierte en CI controlado. |
| DevOps | Infraestructura y deployment configuration podrán ser CIs. |
| Roadmap | CM queda como capacidad transversal antes de la expansión técnica significativa. |
| Supplier Governance | Dependencias externas podrán relacionarse posteriormente con CIs. |

## Regla de impacto

Un CI no deberá convertirse en baseline simplemente porque exista el archivo. La baseline requiere coherencia, identificación, versiones y evidencia de aprobación.

## Riesgo residual

La primera implementación es principalmente documental. La reconciliación automática con runtime, infraestructura y despliegues será una evolución posterior.
