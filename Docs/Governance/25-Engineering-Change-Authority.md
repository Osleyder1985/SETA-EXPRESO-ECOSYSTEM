# Engineering Change Authority

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Baseline propuesta para revisión  
**Issue:** #66

---

## 1. Propósito

Definir qué cambios requieren control y aprobación especial sin convertir el proyecto en un proceso burocrático. El rigor se determina por riesgo, impacto, materialidad, criticidad e irreversibilidad.

## 2. Clases de cambio

| Clase | Ejemplos | Control mínimo |
|---|---|---|
| C0 — Normal | UI, documentación, refactoring local, tests | Issue + branch + PR + validaciones + review |
| C1 — Significativo | comportamiento funcional material, contratos no críticos, dependencias relevantes | análisis de impacto + revisión técnica + validaciones |
| C2 — Arquitectónico | tecnología de BD, autenticación, arquitectura core, contrato de integración | Change Request + Risk Assessment + Decision Record cuando aplique + autoridad técnica |
| C3 — Crítico | seguridad material, datos personales, transacciones financieras, infraestructura productiva crítica, IA crítica, requisito regulatorio | autoridad de cambio + revisión especializada/independiente + validación independiente cuando aplique |

La clasificación nominal no sustituye el análisis de riesgo. Un cambio inicialmente C0 puede elevarse a C1/C2/C3.

## 3. Engineering Change Authority (ECA)

La ECA es una **función de autoridad**, no necesariamente un comité permanente.

- C0: no requiere ECA formal.
- C1: intervención según impacto.
- C2: aprobación por autoridad técnica/arquitectónica correspondiente.
- C3: aprobación de Change Authority y participación de las funciones especializadas necesarias.

No se deben inventar personas ni órganos organizativos. La asignación concreta de roles se mantiene en el modelo de Decision Authority.

## 4. Flujo

```text
Issue
  ↓
Change Classification
  ↓
Impact Analysis
  ↓
Risk Assessment
  ↓
Decision / Approval Authority
  ↓
Implementation
  ↓
Governance / Quality / Security / Evidence Validation
  ↓
Review
  ↓
Merge
```

Para C2/C3 debe existir Change Record con evidencia de autoridad y decisión.

## 5. Change Record mínimo

```yaml
Change-ID:
Related-Issue:
Requested-Date:
Requester:
Description:
Reason:
Classification:
Affected-Components:
Affected-Artifacts:
Risk:
Impact-Analysis:
Decision-Record:
Required-Authority:
Approval:
Implementation-PR:
Validation-Evidence:
Rollback-or-Recovery:
Residual-Risk:
Closure:
```

## 6. Cambios urgentes

Un cambio urgente puede utilizar un flujo acelerado únicamente cuando exista necesidad operacional real. La urgencia no elimina los controles críticos.

Debe conservarse:

1. motivo de urgencia;
2. autoridad que autorizó;
3. riesgo aceptado;
4. evidencia disponible antes del cambio;
5. validación posterior;
6. acciones correctivas/preventivas si la vía acelerada produjo una desviación.

## 7. Excepciones

Toda excepción debe registrar justificación, riesgo residual, autoridad y control compensatorio. Una excepción no debe ocultar que un control fue omitido.

## 8. Relación con SoD

C2 y C3 deben aplicar las restricciones de Segregation of Duties. Cuando la independencia requerida no sea viable, se utiliza el mecanismo formal de excepción y control compensatorio.

## 9. Trazabilidad

```text
Change
  ↕
Issue
  ↕
Risk
  ↕
Decision
  ↕
Approval
  ↕
Implementation
  ↕
Verification
  ↕
Evidence
```

## 10. Regla de main

Ninguna clase de cambio autoriza escritura directa sobre `main`. La integración debe realizarse mediante Pull Request y los controles correspondientes.
