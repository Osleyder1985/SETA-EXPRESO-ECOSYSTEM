# Arquitectura de Evidence Validation

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Arquitectura inicial controlada  
**Fecha:** 2026-09-15  
**Issue:** #23

---

## 1. Propósito

Definir la cuarta capa automatizada de validación del flujo de cambios: Evidence Validation. Comprueba que una unidad de cambio contiene evidencia mínima, trazable y verificable sobre qué se modificó, por qué, bajo qué Issue y Pull Request, sobre qué commit y con qué resultados declarados.

Evidence Validation no certifica la corrección integral del producto ni la suficiencia científica de una evidencia. Comprueba propiedades objetivas y mínimas de la evidencia disponible.

## 2. Posición en el enforcement

```text
Issue → Branch → Pull Request
             ↓
      Governance Validation
             ↓
       Quality Validation
             ↓
      Security Validation
             ↓
       Evidence Validation
             ↓
       Review / Approval
             ↓
            Merge
```

Evidence Validation es independiente de Governance, Quality y Security. Puede consumir sus resultados como evidencia, pero no los sustituye.

## 3. Principios

1. **Evidencia por defecto:** cada cambio controlado debe dejar evidencia verificable.
2. **Trazabilidad:** Issue, branch, PR y commit deben poder relacionarse.
3. **Reproducibilidad:** los controles deben ejecutarse automáticamente y producir resultados observables.
4. **Proporcionalidad:** la profundidad de evidencia depende del riesgo y alcance.
5. **No sobreafirmación:** PASS significa conformidad con los controles EV aplicables.
6. **Separación de responsabilidades:** EV comprueba evidencia; no sustituye revisión humana ni Quality Gates.
7. **Evolución:** los controles crecerán cuando aparezcan código, pruebas, releases, datos e infraestructura.

## 4. Matriz de controles

| ID | Control | Riesgo | Mecanismo | Naturaleza | Evidencia | Estado |
|---|---|---|---|---|---|---|
| EV-001 | Estructura mínima de evidencia en PR | Cambio sin explicación verificable | Secciones obligatorias | P-Compensatorio/D | Check run + PR | Implementado |
| EV-002 | Relación Issue–PR | Unidad de cambio no trazable | Metadata + cuerpo del PR | P-Compensatorio/D | Check run + PR | Implementado |
| EV-003 | Identidad del commit evaluado | Evidencia asociada a versión incorrecta | SHA del PR | P-Compensatorio/D | Check run | Implementado |
| EV-004 | Declaración de validaciones | Evidencia incompleta de controles previos | Evidencia esperada | P-Compensatorio/D | Check run + PR | Implementado |
| EV-005 | Baseline de evidencia presente | Pérdida de infraestructura documental | Existencia de artefactos críticos | P-Compensatorio/D | Check run | Implementado |
| EV-006 | Resultados de validaciones previas | Evidencia de CI incompleta | Consulta de workflow runs | D | Workflow runs | Planificado |
| EV-007 | Integridad histórica de evidencia | Alteración o pérdida de registros | Hashes/procedencia | D | Evidencia versionada | NOT_IMPLEMENTED |
| EV-008 | Evidencia de pruebas | Cambio sin prueba apropiada | Integración con testing | D | Test reports | NOT_APPLICABLE |
| EV-009 | Evidencia de release/despliegue | Cambio productivo sin trazabilidad | Releases/deployments | D | Registros de despliegue | NOT_APPLICABLE |

## 5. Estados

- **PASS:** control aplicable ejecutado y conforme.
- **FAIL:** control aplicable ejecutado y no conforme.
- **NOT_APPLICABLE:** no aplica al contexto actual y existe justificación.
- **NOT_IMPLEMENTED:** control definido pero todavía no automatizado.

Un `FAIL` no se transforma en `PASS` mediante explicación textual. Una excepción requiere una decisión formal y trazable.

## 6. Evidencia mínima de una unidad de cambio

El Pull Request debe permitir identificar como mínimo:

- objetivo del cambio;
- alcance;
- análisis de impacto;
- Issue relacionado;
- evidencia esperada;
- validaciones aplicables;
- relación con la unidad de cambio;
- commit evaluado mediante el workflow.

La información puede estar distribuida entre metadata, cuerpo del PR, commits y resultados de GitHub Actions siempre que la relación sea verificable.

## 7. Límites

La primera implementación no pretende demostrar corrección semántica, ausencia de manipulación por un actor con permisos de escritura, suficiencia científica, calidad integral, seguridad integral, completitud de pruebas ni integridad criptográfica de evidencias externas.

## 8. Relación con gobernanza y estándares

La capa se alinea conceptualmente con las necesidades de trazabilidad, información de ciclo de vida, configuración, verificación, decisiones y evidencia del marco de ingeniería adoptado por el proyecto. La implementación es contextual y no constituye certificación de conformidad normativa.

Se integra con `00-Software-Lifecycle-Master.md`, `03-Artifacts-And-Evidence.md`, `04-Quality-Gates.md`, `06-Change-Control-Workflow.md`, `10-Governance-Enforcement-Architecture.md` y `11-Governance-Control-Matrix.md`.

## 9. Evolución

Cuando existan requisitos verificables, código, pruebas, infraestructura, releases y datos, se evaluará la activación de EV-006..EV-009 y controles adicionales de procedencia, integridad, reproducibilidad y evidencia científica.
