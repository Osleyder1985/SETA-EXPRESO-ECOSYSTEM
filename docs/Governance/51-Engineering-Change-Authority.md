# Engineering Change Authority

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.1  
**Estado:** Baseline vigente  
**Issue:** #66

## 1. Propósito

Definir qué cambios requieren control y aprobación especial sin crear burocracia innecesaria. El rigor depende de riesgo, impacto, materialidad, criticidad e irreversibilidad.

## 2. Clases

| Clase | Ejemplos | Control mínimo |
|---|---|---|
| C0 — Normal | UI, documentación, refactoring local, tests | Issue + branch + PR + validaciones + review |
| C1 — Significativo | cambios funcionales materiales, contratos no críticos, dependencias relevantes | impacto + revisión técnica + validaciones |
| C2 — Arquitectónico | BD, autenticación, arquitectura core, contratos de integración | Change Record + riesgo + Decision Record cuando aplique + autoridad técnica |
| C3 — Crítico | seguridad material, datos personales, financiero, producción crítica, IA crítica, regulación | Change Authority + revisión especializada/independiente + validación independiente cuando aplique |

La clasificación puede elevarse cuando el análisis revele mayor riesgo.

## 3. Engineering Change Authority

ECA es una **función de autoridad**, no necesariamente un comité permanente.

- C0: no requiere ECA formal.
- C1: intervención según impacto.
- C2: autoridad técnica/arquitectónica correspondiente.
- C3: Change Authority y funciones especializadas necesarias.

No se inventan personas u órganos. La asignación de roles se gobierna mediante Decision Authority.

## 4. Flujo

```text
Issue → Change Classification → Impact Analysis → Risk Assessment
→ Decision/Approval Authority → Implementation
→ Governance/Quality/Security/Evidence Validation → Review → Merge
```

## 5. Change Record

```yaml
Change-ID:
Related-Issue:
Requested-Date:
Requester:
Description:
Reason:
Classification: C0|C1|C2|C3
Affected-Components: []
Affected-Artifacts: []
Impact-Analysis:
Risk:
Decision-Record:
Required-Authority:
SoD-Level: I0|I1|I2|I3
Approval:
Implementation-PR:
Validation-Evidence: []
Rollback-or-Recovery:
Residual-Risk:
Urgency: NORMAL|URGENT
Urgent-Justification:
Status: PROPOSED|ASSESSED|APPROVED|IMPLEMENTING|VERIFYING|CLOSED|REJECTED
```

## 6. Urgencias y excepciones

La urgencia puede acelerar el flujo, pero no elimina controles críticos. Deben conservarse motivo, autoridad, riesgo, evidencia disponible, validación posterior y acciones derivadas. Toda excepción registra justificación, riesgo residual, autoridad y control compensatorio.

## 7. Relación con SoD

C2/C3 aplican las restricciones de SoD. Si la independencia no es viable, debe usarse el mecanismo de excepción; no se fabrica una aprobación independiente.

## 8. Regla de main

Ninguna clase de cambio autoriza escritura directa sobre `main`. Toda integración utiliza Pull Request y los controles correspondientes.

## 9. Estado de baseline

Engineering Change Authority está integrado en `main` como **baseline vigente**. La vigencia establece la clasificación, autoridad y flujo de control de cambios; no implica que todas las decisiones de autoridad estén automatizadas. La evidencia y la asignación de autoridad deben conservarse de forma proporcional a la clase C0–C3.
