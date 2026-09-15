# Gestión de configuración (Configuration Management)

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Baseline propuesta — pendiente de integración  
**Problema:** #45  
**Idioma documental:** Español

## 1. Propósito

Establecer la capacidad formal de Configuration Management (CM) del Ecosistema. Git seguirá siendo el mecanismo principal de control de versiones, pero CM añade identificación formal de Configuration Items (CI), baselines, control de cambios, accounting del estado y verificación/auditoría.

ISO 10007:2017 define estas capacidades como elementos centrales de la gestión de configuración y permanece como versión vigente, aunque existe una revisión de ISO/WD 10007 en desarrollo. citeturn0search2turn0search4

ISO/IEC/IEEE 12207:2026 proporciona el marco vigente del ciclo de vida del software y aplica a todo el ciclo de vida, incluida definición, desarrollo, operación, mantenimiento y retirada. citeturn0search0

## 2. Principio fundamental

```text
Git Version Control
        ≠
Configuration Management
```

Git registra estados y cambios de archivos y commits. Configuration Management determina **qué elementos constituyen configuración controlada**, qué versión es la aprobada, a qué baseline pertenecen, quién responde por ellos y cómo se controla su evolución.

## 3. Objetivos

- identificar Configuration Items de forma estable;
- establecer baselines controladas;
- mantener versiones y estados de configuración;
- relacionar CIs con requisitos, arquitectura, diseño, código, pruebas, seguridad, infraestructura y despliegue;
- controlar cambios mediante Issue → Branch → PR → validaciones → Merge;
- conservar evidencia y aprobaciones;
- detectar desviaciones entre la configuración aprobada y la configuración observada;
- proporcionar información suficiente para auditorías y recuperación.

## 4. Procesos de Configuration Management

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

Un CI es un elemento identificado y controlado cuya modificación puede afectar al sistema, sus requisitos, calidad, seguridad, operación, evidencia o capacidad de evolución.

Un CI puede ser un documento, modelo, contrato, código, configuración, infraestructura, prueba, dato de configuración, artefacto de despliegue o cualquier otro elemento que requiera control formal.

## 6. CIs iniciales

| CI | Nombre | Tipo | Estado inicial | Owner |
|---|---|---|---|---|
| CI-001 | Requirements Baseline | Requirements | Proposed | Requirements Owner |
| CI-002 | Architecture Baseline | Architecture | Proposed | Architecture Owner |
| CI-003 | Database Schema | Data/Design | Proposed | Data Owner |
| CI-004 | API Contract | Interface | Proposed | Architecture Owner |
| CI-005 | Security Baseline | Security | Proposed | Security Owner |
| CI-006 | Infrastructure | Infrastructure | Proposed | DevOps/Operations Owner |
| CI-007 | Source Code | Software | Active | Engineering Owner |
| CI-008 | Test Suite | Verification | Active | Quality Owner |
| CI-009 | Deployment Configuration | Configuration/DevOps | Proposed | Operations Owner |

Los owners son roles de gobernanza y no implican todavía que una persona concreta haya sido asignada.

## 7. Registro canónico

El registro canónico se encuentra en:

`Docs/Governance/Configuration/Configuration-Item-Register.yml`

El registro Markdown derivado se utilizará para lectura humana. El YAML será la fuente estructurada para futuras automatizaciones.

## 8. Atributos obligatorios de un CI

Cada CI deberá registrar, cuando corresponda:

- `ci_id`;
- `name`;
- `type`;
- `description`;
- `owner`;
- `status`;
- `version`;
- `baseline`;
- `source`;
- `dependencies`;
- `change_control`;
- `approval`;
- `evidence`;
- `change_history`;
- `effective_date`;
- `retirement_date`.

## 9. Estados de CI

```text
PROPOSED
   ↓
ACTIVE
   ↓
BASELINED
   ↓
CHANGE_REQUESTED
   ↓
CHANGED
   ↓
REBASELINED
   ↓
RETIRED
```

`BASELINED` no significa que el CI sea inmutable. Significa que su estado forma parte de una baseline aprobada y cualquier cambio posterior debe seguir control de cambios.

## 10. Baselines

Una baseline es un conjunto identificado y coherente de CIs aprobado para un propósito determinado.

Una baseline deberá identificar como mínimo:

- `baseline_id`;
- propósito;
- fecha efectiva;
- estado;
- CIs incluidos;
- versiones incluidas;
- aprobación;
- evidencia;
- relación con Issue/PR/commit cuando corresponda.

## 11. Versionado

La versión del CI no sustituye al SHA de Git.

```text
CI Version
   ↓
Baseline Version
   ↓
Git Commit / Tag / Release
```

Cuando exista una relación inequívoca, el registro deberá conservarla. Cuando un CI no sea directamente representable por un commit, deberá registrarse su fuente documental o técnica y su evidencia correspondiente.

## 12. Change Control

Todo cambio a un CI baselined seguirá el flujo general del proyecto:

```text
Issue
 ↓
Impact Analysis
 ↓
Branch
 ↓
Change
 ↓
Validation
 ↓
PR
 ↓
Approval
 ↓
Merge
 ↓
New CI State
 ↓
Baseline Update cuando corresponda
```

La modificación directa de un CI baselined fuera de este flujo se considera una desviación de configuración.

## 13. Configuration Status Accounting

El accounting deberá permitir responder en cualquier momento:

- qué CIs existen;
- cuál es su versión vigente;
- cuál es su baseline;
- qué cambios están pendientes;
- qué cambios fueron aprobados;
- qué cambios fueron rechazados;
- qué CIs están retirados;
- qué dependencias existen;
- qué evidencia respalda cada estado.

El registro inicial se documenta en:

`Docs/Governance/Configuration/Configuration-Status-Accounting.md`

## 14. Configuration Verification / Audit

Las verificaciones deberán comprobar progresivamente:

1. CI identificado;
2. owner definido;
3. versión registrada;
4. baseline válida;
5. fuente localizable;
6. dependencias registradas;
7. cambios trazables;
8. aprobación disponible;
9. evidencia disponible;
10. correspondencia entre configuración aprobada y configuración observada.

Inicialmente estas comprobaciones serán mayoritariamente documentales/híbridas. No se declarará automatización donde todavía no exista implementación.

## 15. Integración con Quality Gates

Configuration Management será una fuente de evidencia para Quality Gates.

En particular, los Gates deberán poder verificar progresivamente que los artefactos críticos que forman parte de una baseline están identificados, versionados y aprobados.

## 16. Integración con Risk Management

Un riesgo de configuración podrá registrarse cuando exista:

- pérdida de trazabilidad;
- configuración no identificada;
- baseline inconsistente;
- divergencia entre configuración aprobada y desplegada;
- dependencia no registrada;
- cambio no autorizado;
- imposibilidad de reconstrucción.

## 17. Integración con Decision Governance

Cuando la selección o modificación de una configuración constituya una decisión material de arquitectura o ingeniería, deberá relacionarse con el ADR/EDR correspondiente.

## 18. Integración con Evidence Governance

Cada CI crítico deberá poder apuntar a evidencia que permita reconstruir su estado y evolución.

## 19. Desviación histórica de preparación

Durante la preparación de este problema se produjeron commits directos accidentales sobre `main`. La desviación queda registrada en el Issue #45 y los artefactos temporales creados durante la preparación son eliminados mediante el PR de este mismo Issue.

La desviación no se considera una excepción válida de la política de cambio. La existencia histórica de los commits no será ocultada ni reescrita.

## 20. Limitaciones actuales

La primera implementación proporciona una capacidad documental y estructurada de CM. La automatización completa de reconciliación entre CI Register, Git, CI/CD, infraestructura y entornos operativos queda como evolución posterior y deberá ser implementada mediante cambios controlados.

## 21. Evidencia esperada

- Configuration Management Plan/Policy;
- Configuration Item Register;
- Baseline Register;
- Configuration Status Accounting;
- Configuration Audit Checklist;
- Impact Analysis;
- Issue #45;
- Pull Request asociado;
- resultados Governance/Quality/Security/Evidence Validation;
- commit de integración.
