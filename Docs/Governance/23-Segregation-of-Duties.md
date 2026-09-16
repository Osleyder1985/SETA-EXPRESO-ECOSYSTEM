# Segregation of Duties (SoD)

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Baseline propuesta para revisión  
**Issues:** #52, #47, #66, #33

---

## 1. Propósito

Establecer separación de funciones proporcional al riesgo para evitar que una misma persona concentre, cuando exista conflicto material, la definición, implementación, aprobación y validación de un cambio o decisión.

> **Principio:** la independencia requerida aumenta con el riesgo, impacto, materialidad e irreversibilidad.

SoD es un mecanismo de control. No implica crear puestos ficticios ni una estructura burocrática permanente.

## 2. Roles conceptuales

Las funciones se expresan como roles, no como personas:

- **Requester/Decision Owner:** plantea la necesidad o es accountable de la decisión.
- **Implementer:** ejecuta el cambio.
- **Reviewer:** realiza revisión técnica o de proceso.
- **Approver/Authority:** autoriza cuando el nivel de riesgo lo requiere.
- **Validator:** verifica independientemente el resultado cuando corresponda.
- **Risk Owner:** acepta o gestiona el riesgo residual dentro de su autoridad.

Una persona puede desempeñar varios roles conceptuales. La restricción se aplica a combinaciones concretas cuando el riesgo exige independencia.

## 3. Niveles de independencia

| Nivel | Aplicación | Regla mínima |
|---|---|---|
| I0 — Bajo | documentación, UI, refactoring local | acumulación permitida; PR y validaciones obligatorias |
| I1 — Medio | cambios funcionales o técnicos con impacto limitado | revisión por otra función cuando sea viable |
| I2 — Alto | arquitectura, autenticación, datos sensibles, infraestructura relevante | implementación y aprobación no deben quedar concentradas cuando exista una alternativa razonable |
| I3 — Crítico | seguridad crítica, privacidad material, transacciones financieras, producción crítica, requisitos regulatorios | revisión/aprobación y validación independientes; excepción formal si la independencia no es viable |

El nivel se determina por el análisis de riesgo y no únicamente por el tipo nominal del cambio.

## 4. Combinaciones de funciones

| Combinación en la misma persona | I0 | I1 | I2 | I3 |
|---|---:|---:|---:|---:|
| Requester + Implementer | Permitido | Permitido con revisión | Restringido | Restringido |
| Implementer + Reviewer | Permitido | Restringido | No preferido | Prohibido salvo excepción documentada |
| Implementer + Approver | Permitido mediante PR | Restringido | No permitido | No permitido |
| Implementer + Validator | Permitido como validación inicial | Restringido | No permitido para validación independiente | No permitido |
| Approver + Validator | Permitido | Permitido | Restringido | No permitido si la validación debe ser independiente |

"Prohibido" significa que la combinación no es aceptable para el control normal del cambio. Si el tamaño de la organización impide cumplirla, debe utilizarse el mecanismo de excepción.

## 5. Regla de Pull Request

Ningún cambio de baseline llega directamente a `main`.

```text
Issue
  ↓
Branch
  ↓
Implementation
  ↓
Pull Request
  ↓
Governance / Quality / Security / Evidence validation
  ↓
Review
  ↓
Approval according to risk
  ↓
Merge
  ↓
main
```

Un PR exitoso no sustituye la autoridad requerida por el nivel de riesgo.

## 6. Excepciones y controles compensatorios

Cuando no exista una segunda persona disponible:

1. registrar la excepción;
2. identificar la función acumulada;
3. documentar el riesgo residual;
4. justificar por qué la segregación no es viable;
5. aplicar un control compensatorio, por ejemplo revisión posterior, evidencia reforzada, pruebas automatizadas adicionales o revisión especializada externa;
6. establecer quién acepta el riesgo residual;
7. conservar la evidencia.

No se debe fabricar una aprobación independiente.

## 7. Integración

SoD debe evaluarse conjuntamente con:

- Decision Governance;
- Decision Authority;
- Change Control y Change Authority;
- Risk Management;
- Quality Gates;
- Security Governance;
- Data Governance;
- AI Governance;
- Supplier/Third-Party Governance;
- Configuration Management;
- Evidence Governance;
- Research Governance cuando una decisión afecte evidencia científica.

## 8. Trazabilidad

```text
Issue
  ↓
Risk Assessment
  ↓
Decision / Change
  ↓
Required Independence
  ↓
Implementation
  ↓
Review / Approval
  ↓
Validation
  ↓
Evidence
```

## 9. Límites de madurez

Esta política es un control documental y de proceso. No se debe afirmar que GitHub impide automáticamente toda concentración de funciones hasta disponer de controles técnicos configurados y evidencia de ejecución.
