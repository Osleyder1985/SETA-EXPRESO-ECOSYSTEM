# Gestión de configuración (Configuration Management)

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Baseline propuesta — pendiente de integración  
**Problema:** #45  
**Idioma documental:** Español

## 1. Propósito

Establecer la capacidad formal de Configuration Management (CM) del Ecosistema. Git seguirá siendo el mecanismo principal de control de versiones, pero CM añade identificación formal de Configuration Items (CI), baselines, control de cambios, accounting del estado y verificación/auditoría.

ISO 10007:2017 permanece como referencia vigente para configuration management. ISO/WD 10007 se encuentra en desarrollo y no se utiliza como estándar vigente.

ISO/IEC/IEEE 12207:2026 proporciona el marco vigente del ciclo de vida del software.

## 2. Principio fundamental

```text
Git Version Control
        ≠
Configuration Management
```

Git registra estados y cambios de archivos y commits. Configuration Management determina qué elementos constituyen configuración controlada, qué versión es la aprobada, a qué baseline pertenecen, quién responde por ellos y cómo se controla su evolución.

## 3. Objetivos

- identificar Configuration Items de forma estable;
- establecer baselines controladas;
- mantener versiones y estados de configuración;
- relacionar CIs con requisitos, arquitectura, diseño, código, pruebas, seguridad, infraestructura y despliegue;
- controlar cambios mediante Issue → Branch → PR → validaciones → Merge;
- conservar evidencia y aprobaciones;
- detectar desviaciones entre configuración aprobada y observada;
- proporcionar información suficiente para auditorías y recuperación.

## 4. Procesos

```text
CM Planning
    ↓
Configuration Identification
    ↓
Baseline Establishment
    ↓
Change Control
    ↓
Configuration Status Accounting
    ↓
Configuration Verification / Audit
    ↓
Continuous Reconciliation
```

## 5. Configuration Item

Un CI es un elemento identificado y controlado cuya modificación puede afectar al sistema, sus requisitos, calidad, seguridad, operación, evidencia o evolución.

## 6. CIs iniciales

| CI | Nombre | Tipo | Estado inicial | Owner |
|---|---|---|---|---|
| CI-001 | Requirements Baseline | Requirements | PROPOSED | Requirements Owner |
| CI-002 | Architecture Baseline | Architecture | PROPOSED | Architecture Owner |
| CI-003 | Database Schema | Data/Design | PROPOSED | Data Owner |
| CI-004 | API Contract | Interface | PROPOSED | Architecture Owner |
| CI-005 | Security Baseline | Security | PROPOSED | Security Owner |
| CI-006 | Infrastructure | Infrastructure | PROPOSED | DevOps/Operations Owner |
| CI-007 | Source Code | Software | ACTIVE | Engineering Owner |
| CI-008 | Test Suite | Verification | ACTIVE | Quality Owner |
| CI-009 | Deployment Configuration | Deployment | PROPOSED | Operations Owner |

Los owners representan roles de gobernanza y no implican asignación personal todavía.

## 7. Registro canónico

`Docs/Governance/Configuration/Configuration-Item-Register.yml`

El YAML es la fuente estructurada para futuras automatizaciones.

## 8. Atributos obligatorios

- `ci_id`
- `name`
- `type`
- `description`
- `owner`
- `status`
- `version`
- `baseline`
- `source`
- `dependencies`
- `change_control`
- `approval`
- `evidence`
- `change_history`
- `effective_date`
- `retirement_date`

## 9. Estados

```text
PROPOSED → ACTIVE → BASELINED → CHANGE_REQUESTED → CHANGED → REBASELINED → RETIRED
```

`BASELINED` significa que el estado forma parte de una baseline aprobada; no significa inmutabilidad.

## 10. Baselines

Una baseline es un conjunto identificado y coherente de CIs aprobado para un propósito determinado.

Debe identificar propósito, fecha efectiva, estado, CIs incluidos, versiones, aprobación y evidencia.

## 11. Versionado

La versión lógica del CI no sustituye al SHA de Git.

```text
CI Version → Baseline Version → Git Commit / Tag / Release
```

## 12. Change Control

Todo cambio a un CI baselined seguirá:

```text
Issue → Impact Analysis → Branch → Change → Validation → PR → Approval → Merge → New CI State → Baseline Update
```

## 13. Configuration Status Accounting

Debe permitir conocer CIs existentes, versiones vigentes, baselines, cambios pendientes/aprobados/rechazados, estados retirados, dependencias y evidencias.

Registro: `Docs/Governance/Configuration/Configuration-Status-Accounting.md`

## 14. Configuration Verification / Audit

Se verificará progresivamente:

1. CI identificado;
2. owner definido;
3. versión registrada;
4. baseline válida;
5. fuente localizable;
6. dependencias registradas;
7. cambios trazables;
8. aprobación disponible;
9. evidencia disponible;
10. correspondencia entre configuración aprobada y observada.

Las comprobaciones se clasificarán progresivamente como AUTOMATED, HYBRID o HUMAN. No se declara automatización inexistente.

## 15. Quality Gates

CM proporciona evidencia para Quality Gates. Los gates podrán verificar progresivamente identificación, versión, baseline y aprobación de CIs críticos.

## 16. Risk Management

Los riesgos de configuración incluyen pérdida de trazabilidad, CI no identificado, baseline inconsistente, divergencia entre configuración aprobada y desplegada, dependencia no registrada, cambio no autorizado o imposibilidad de reconstrucción.

## 17. Decision Governance

Los cambios materiales de configuración que constituyan decisiones de arquitectura o ingeniería deberán relacionarse con ADR/EDR cuando corresponda.

## 18. Evidence Governance

Los CIs críticos deberán apuntar a evidencia suficiente para reconstruir su estado y evolución.

## 19. Desviación histórica

Durante la preparación se produjeron commits directos accidentales sobre `main`. La desviación queda registrada en Issue #45. Los artefactos temporales se eliminan mediante este PR. La historia no se reescribe.

## 20. Limitaciones

Esta primera implementación proporciona una capacidad documental y estructurada. La reconciliación automática con CI/CD, infraestructura, despliegues y runtime queda como evolución posterior.

## 21. Evidencia esperada

- Configuration Management Policy/Process;
- Configuration Item Register;
- Baseline Register;
- Configuration Status Accounting;
- Configuration Audit Checklist;
- Control Matrix;
- Impact Analysis;
- Issue #45;
- PR asociado;
- resultados de Governance, Quality, Security y Evidence Validation.

## 22. Criterio de no-invención

La baseline inicial es propuesta. Los CIs no se consideran aprobados o implementados simplemente por existir en el registro. Los campos sin evidencia permanecen explícitamente vacíos/null.
