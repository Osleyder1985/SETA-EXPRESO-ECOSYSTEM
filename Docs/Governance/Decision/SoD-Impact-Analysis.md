# Análisis de impacto — Segregación de funciones

**Issue:** #49  
**Problema:** #11  
**Versión:** 1.0.0  

## 1. Cambio

Formalizar la separación de funciones (SoD) entre definición, ejecución, aprobación, verificación, validación, bloqueo y revisión, aplicando independencia proporcional al riesgo.

## 2. Impacto directo

| Artefacto | Impacto | Acción |
|---|---|---|
| `48-Decision-Authority-Governance.md` | Alto | Integrar SoD como condición de autoridad |
| `Decision-Authority-Matrix.yml` | Alto | Incorporar referencia a independencia requerida |
| `Role-Assignment-Policy.md` | Alto | Vincular acumulación de roles con SoD |
| `17-Risk-Management-System.md` | Alto | Usar nivel de riesgo como entrada de independencia |
| `18-Risk-Management-Control-Matrix.md` | Medio | Añadir control SoD |
| `04-Quality-Gates.md` | Alto | Considerar independencia en gates de alto riesgo |
| `12-Quality-Validation-Architecture.md` | Medio | Distinguir independencia de validación |
| `06-Change-Control-Workflow.md` | Alto | Introducir clasificación SoD en cambios |
| `35-Configuration-Management.md` | Medio | Separar modificación, aprobación y baseline según riesgo |
| `41-Configuration-Management-Control-Matrix.md` | Medio | Añadir referencia de control |
| `13-Security-Validation-Architecture.md` | Alto | Preservar independencia en seguridad |
| `25-Data-Governance.md` | Alto | Aplicar independencia a decisiones de datos |
| `23-AI-Governance.md` | Alto | Aplicar independencia a decisiones de IA |
| Supplier/Third-Party Governance | Medio | Considerar separación selección/aprobación/aceptación |
| Engineering Metrics | Medio | Medir desviaciones y excepciones SoD |
| `00-Software-Lifecycle-Master.md` | Medio | SoD transversal al ciclo de vida |

## 3. Impacto de implementación

No se modifica código de aplicación. El cambio establece una capacidad de gobernanza que posteriormente podrá habilitar automatizaciones verificables.

## 4. Impacto sobre personas

No se asignan personas ficticias. La acumulación conceptual existente permanece posible en R1 y, bajo condiciones, en otros niveles. La segregación se aplica a funciones concretas cuando el riesgo lo exige.

## 5. Riesgo de la modificación

La modificación de gobernanza puede alterar criterios de aprobación y validación de futuros cambios. Por ello debe pasar por las cuatro validaciones establecidas y conservar evidencia del HEAD exacto validado.

## 6. Dependencias

```text
Decision Authority
        ↓
Risk Management
        ↓
SoD Classification
        ↓
Quality / Security / Data / AI / Supplier controls
        ↓
Evidence
```

## 7. Trabajo pendiente trazable

La integración normativa completa con todos los artefactos impactados se ejecutará como parte de esta unidad de cambio o se registrará explícitamente como continuación trazable antes de considerar la capacidad completamente baselineada.
