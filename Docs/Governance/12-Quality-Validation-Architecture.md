# Arquitectura de Quality Validation

> Documento controlado de gobernanza y calidad del Ecosistema SETA Expreso.

## 1. Propósito

Definir la primera capa automatizada de **Quality Validation (QV)** para detectar incumplimientos objetivos de calidad en el estado actual del repositorio, separándola de Governance Validation y de la decisión formal de Quality Gate.

Esta capa es deliberadamente incremental: valida propiedades estructurales y de integridad que pueden automatizarse con evidencia reproducible. No sustituye la ingeniería de requisitos, arquitectura, diseño, pruebas funcionales, seguridad, rendimiento ni validación de aceptación.

## 2. Posición en la cadena de control

```text
Issue
  ↓
Branch
  ↓
Pull Request
  ↓
Governance Validation
  ↓
Quality Validation
  ↓
Security Validation
  ↓
Evidence Validation
  ↓
Review
  ↓
Quality Gate Decision
  ↓
Merge
  ↓
main
```

Quality Validation aporta comprobaciones automatizadas. El Quality Gate consume estas y otras evidencias para producir una decisión operacional `PASS`, `CONDITIONAL`, `BLOCKED` o `REOPEN`.

## 3. Principios

1. **Objetividad:** cada control automatizado debe tener una condición verificable.
2. **Reproducibilidad:** la validación se ejecuta automáticamente cuando exista infraestructura para ello.
3. **Separación de responsabilidades:** Governance Validation controla integridad del proceso; Quality Validation controla propiedades de calidad automatizables; Quality Gates deciden sobre evidencia acumulada.
4. **Evidencia:** cada ejecución constituye evidencia técnica del resultado del control.
5. **No sobreafirmación:** un PASS de QV no equivale a certificación integral de calidad ni a PASS de un gate.
6. **Evolución:** los controles se ampliarán cuando aparezcan código fuente, pruebas, infraestructura, datos, requisitos y telemetría verificables.

## 4. Controles actuales

| ID | Control | Riesgo | Mecanismo | Evidencia | Limitación |
|---|---|---|---|---|---|
| QV-001 | Markdown no vacío | Artefactos documentales inválidos o vacíos | Script en GitHub Actions | Run del workflow | No evalúa contenido semántico |
| QV-002 | H1 inicial | Documentos sin encabezado principal | Script en GitHub Actions | Run del workflow | No evalúa estructura completa |
| QV-003 | Sin trailing whitespace fuera de Markdown | Ruido y defectos de formato en archivos técnicos | Script en GitHub Actions | Run del workflow | No es una revisión estilística completa |
| QV-004 | YAML válido | Configuración CI/CD inválida | Parser YAML | Run del workflow | No valida semántica de cada plataforma |
| QV-005 | Enlaces Markdown locales íntegros | Referencias rotas por cambios/movimientos | Resolución de rutas locales | Run del workflow | No verifica enlaces externos ni semántica documental |
| QV-006 | Artefactos críticos presentes | Pérdida accidental de controles base | Lista de artefactos requeridos | Run del workflow | La lista debe evolucionar con el sistema |

## 5. Relación con Quality Gate Operationalization

Los controles QV son una fuente de evidencia para los Quality Gates. No deben confundirse con los criterios completos del gate.

El catálogo operacional de gates se mantiene en:

`Docs/Governance/Quality/Quality-Gate-Catalog.yml`

Cada check del catálogo se clasifica como `AUTOMATED`, `HYBRID` o `HUMAN`. Cuando un check es `AUTOMATED`, Quality Validation podrá implementar el mecanismo técnico correspondiente cuando exista una fuente de datos estructurada y confiable.

Ejemplos de evolución:

```text
Requirements YAML
      ↓
Parser / Rule Engine
      ↓
G3/G4 Checks
      ↓
Machine-readable Result
      ↓
Evidence
      ↓
Quality Gate Decision
```

La automatización no puede convertir por sí sola una evaluación humana en un hecho objetivo.

## 6. Workflow

El workflow `.github/workflows/quality-validation.yml` se ejecuta sobre cambios dirigidos a `main` y valida los controles aplicables al repositorio actual.

El workflow de Governance Validation permanece separado. En particular, la comprobación de labels pertenece a gobernanza y consulta el estado actual del Pull Request mediante la API de GitHub, evitando depender exclusivamente del snapshot del evento.

## 7. Evidencia

La evidencia mínima de una ejecución debe permitir identificar:

- commit validado;
- workflow;
- ejecución;
- controles ejecutados;
- resultado de cada control;
- mensaje de fallo, si existe;
- fecha/hora de ejecución.

La existencia del archivo de workflow, por sí sola, no constituye evidencia de que el control haya sido ejecutado correctamente.

## 8. Evolución prevista

Cuando el Ecosistema incorpore implementación real, Quality Validation deberá crecer progresivamente hacia:

- validación de estructura de requisitos;
- compilación y análisis estático;
- cobertura y pruebas automatizadas;
- validación de contratos e interfaces;
- análisis de complejidad y mantenibilidad;
- validación de arquitectura;
- pruebas de integración;
- rendimiento y resiliencia;
- validaciones de datos;
- controles específicos por riesgo y atributo de calidad ISO/IEC 25010;
- evaluación automatizada de criterios de Quality Gates cuando las fuentes sean estructuradas.

Cada nuevo control deberá registrarse en la matriz de controles, definir su evidencia y documentar sus limitaciones.

## 9. Estado

**Versión:** 0.2.0  
**Estado:** Baseline inicial evolucionada para integración con Quality Gate Operationalization  
**Última actualización:** 2026-09-15
