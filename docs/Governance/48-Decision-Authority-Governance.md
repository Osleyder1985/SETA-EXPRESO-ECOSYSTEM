# Gobernanza de autoridad de decisiones

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Propuesta para baseline mediante Issue #47  
**Problema:** #10  

## 1. Propósito

Definir formalmente quién es responsable, quién tiene autoridad y qué evidencia se requiere para las decisiones relevantes del Ecosistema.

La existencia de roles conceptuales es independiente de la asignación de personas. Una misma persona puede desempeñar varios roles inicialmente, pero la autoridad de cada dominio permanece diferenciada.

## 2. Principios

1. La responsabilidad no implica automáticamente autoridad de aprobación.
2. Toda decisión material debe ser trazable a su contexto, evidencia y decisión registrada.
3. Los roles representan responsabilidades estables; las personas pueden cambiar.
4. Cuando una persona acumule roles, esa acumulación debe quedar visible.
5. Las decisiones que requieran independencia deben tener revisión separada cuando sea posible.
6. La política de autoridad no se considera por sí sola un control técnico.
7. La automatización se clasifica como AUTOMATED, HYBRID o HUMAN según capacidad real.

## 3. Registro conceptual de roles

| ID | Rol | Responsabilidad principal | Autoridad principal |
|---|---|---|---|
| ROLE-001 | Product Owner | Valor, prioridades y outcomes | Priorizar producto |
| ROLE-002 | System Owner | Objetivos, alcance y desempeño sistémico | Decisiones sistémicas |
| ROLE-003 | Requirements Owner | Calidad, baseline y trazabilidad de requisitos | Aprobar baseline de requisitos |
| ROLE-004 | System Architect | Arquitectura del sistema | Aprobar decisiones arquitectónicas sistémicas |
| ROLE-005 | Software Architect | Arquitectura y diseño del software | Aprobar decisiones de arquitectura software |
| ROLE-006 | Security Owner | Seguridad y riesgos de seguridad | Bloquear/elevar cambios por riesgo de seguridad |
| ROLE-007 | Data Owner | Gobierno, uso y calidad de datos | Autorizar decisiones sobre datos bajo su dominio |
| ROLE-008 | QA Owner | Calidad, verificación y evidencia | Autoridad sobre evidencia y resultados de calidad |
| ROLE-009 | DevOps/Platform Owner | Plataforma, CI/CD e infraestructura técnica | Decisiones de plataforma |
| ROLE-010 | Operations Owner | Operación, soporte y continuidad | Decisiones operativas |
| ROLE-011 | Research Owner | Investigación, rigor y reproducibilidad | Decisiones metodológicas de investigación |
| ROLE-012 | Change Authority | Control y autorización de cambios | Aprobar/rechazar cambios controlados |

## 4. Tipos de decisión

| Tipo | Autoridad accountable | Consultados principales | Evidencia mínima |
|---|---|---|---|
| DEC-001 Valor/prioridad | Product Owner | System Owner, Requirements Owner | Objetivos, necesidades, impacto |
| DEC-002 Alcance sistémico | System Owner | Product Owner, Architect | Objetivos, requisitos, riesgos |
| DEC-003 Baseline de requisitos | Requirements Owner | Product Owner, QA | Requisitos, trazabilidad, aceptación |
| DEC-004 Arquitectura de sistema | System Architect | System Owner, Security, Data | Architecture Decision Record, riesgos |
| DEC-005 Arquitectura software | Software Architect | System Architect, QA, Security | ADR, diseño, verificación |
| DEC-006 Seguridad | Security Owner | Architect, Data, Operations | Security evidence, risk assessment |
| DEC-007 Datos | Data Owner | Security, Requirements, Architecture | Clasificación, calidad, lineage |
| DEC-008 Calidad/gate | QA Owner | Owners afectados | Resultados, métricas, evidencia |
| DEC-009 Plataforma | DevOps/Platform Owner | Security, Operations | Configuración, riesgos, evidencia |
| DEC-010 Operación | Operations Owner | Security, Platform | Runbook, readiness, métricas |
| DEC-011 Investigación | Research Owner | Owners afectados | Método, datos, evidencia, reproducibilidad |
| DEC-012 Cambio controlado | Change Authority | Owner del CI, QA, Security | Impact analysis, validaciones, evidencia |

## 5. RACI conceptual

Se utilizará RACI como lenguaje auxiliar, no como sustituto de la autoridad explícita:

- **R — Responsible:** ejecuta o prepara el trabajo.
- **A — Accountable:** responde por la decisión o resultado.
- **C — Consulted:** debe ser consultado cuando corresponda.
- **I — Informed:** debe ser informado.

La matriz completa y estructurada se mantiene en `Docs/Governance/Decision/Decision-Authority-Matrix.yml`.

## 6. Acumulación inicial de roles

No se asignan personas ficticias. La asignación inicial se registra conceptualmente:

```text
Persona inicial / liderazgo del proyecto
├── Product Owner
├── System Owner
├── Requirements Owner
├── System Architect
├── Software Architect
├── Security Owner
├── Data Owner
├── QA Owner
├── DevOps/Platform Owner
├── Operations Owner
├── Research Owner
└── Change Authority
```

Esta acumulación constituye una condición de gobernanza y un riesgo potencial de independencia. A medida que el Ecosistema incorpore participantes, las funciones podrán segregarse.

## 7. Autoridad de bloqueo

Security Owner, QA Owner y Change Authority pueden disponer de autoridad de bloqueo dentro de sus dominios cuando existan criterios formales de bloqueo. El bloqueo debe estar sustentado por evidencia, criterio aplicable y registro trazable; no es una autoridad arbitraria.

## 8. Escalamiento

```text
Decisión local
    ↓
Owner del dominio
    ↓
System Owner / Product Owner según dominio
    ↓
Change Authority cuando exista cambio controlado
    ↓
Escalamiento extraordinario registrado
```

Un conflicto entre dominios se resuelve mediante decisión registrada y evidencia, no mediante autoridad implícita del asistente.

## 9. Integración con gobernanza existente

Esta capacidad se integra con:

- `19-Decision-Governance.md` y sus Decision Records;
- `43-Quality-Gates-Operationalization.md`;
- `35-Configuration-Management.md`;
- `17-Risk-Management-System.md`;
- `13-Security-Validation-Architecture.md`;
- `25-Data-Governance.md`;
- `23-AI-Governance.md`;
- Supplier/Third-Party Governance;
- Engineering Metrics;
- Lifecycle Master.

## 10. Criterios de decisión

Una decisión material debe poder responder:

```text
¿Qué se decide?
¿Quién es accountable?
¿Quién puede aprobar?
¿Quién puede bloquear?
¿Quién debe ser consultado?
¿Qué evidencia se necesita?
¿Qué riesgos existen?
¿Dónde queda registrada?
¿Qué artefactos cambia?
¿Cómo se verifica la decisión?
```

## 11. Estados

`PROPOSED → REVIEWED → ACCEPTED → REJECTED → SUPERSEDED → DEPRECATED`

El estado `ACCEPTED` requiere evidencia de autoridad y trazabilidad. Una decisión puede ser reemplazada sin borrar su historial.

## 12. Limitaciones actuales

La primera implementación es principalmente documental y estructural. La automatización de autoridad, separación de funciones, enforcement de aprobaciones y detección de conflictos se desarrollará progresivamente.

No se afirma que GitHub Free proporcione enforcement empresarial nativo donde no exista.
