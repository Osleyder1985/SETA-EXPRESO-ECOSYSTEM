# Arquitectura de Security Validation

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Baseline inicial de Security Validation  
**Idioma documental:** Español  
**Fecha:** 2026-09-15  
**Issue:** #22

---

## 1. Propósito

Definir la primera capa automatizada de **Security Validation (SV)** para detectar condiciones objetivas de riesgo de seguridad antes de integrar cambios en `main`.

Security Validation es una capa transversal del ciclo de vida. No sustituye threat modeling, arquitectura de seguridad, análisis de riesgos, pruebas de penetración, revisión humana, gestión de vulnerabilidades ni aceptación de seguridad.

NIST SP 800-218 (SSDF 1.1) recomienda integrar prácticas de desarrollo seguro dentro del ciclo de desarrollo existente, mientras que NIST CSF 2.0 organiza la gestión del riesgo mediante las funciones Govern, Identify, Protect, Detect, Respond y Recover. En este repositorio se utilizan como marcos de referencia y vocabulario; su adopción no implica conformidad automática. citeturn0search0turn0search12

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
Review / Approval
  ↓
Merge
  ↓
main
```

## 3. Principios

1. **Security by design:** la seguridad se considera desde el inicio y no únicamente antes del despliegue.
2. **Risk-based:** cada control debe justificar qué riesgo reduce.
3. **Objetividad:** un control automatizado debe tener una condición verificable.
4. **Least privilege:** los workflows deben solicitar únicamente permisos necesarios.
5. **Secrets hygiene:** credenciales y material secreto no deben formar parte del repositorio.
6. **Evidence by default:** cada resultado debe ser reproducible y localizable.
7. **No sobreafirmación:** pasar SV no equivale a certificación de seguridad.
8. **Aplicabilidad explícita:** cuando un control depende de artefactos todavía inexistentes, se registra como `NOT_APPLICABLE` o `NOT_IMPLEMENTED`, no como PASS artificial.
9. **Evolución:** los controles aumentarán conforme aparezcan código, dependencias, infraestructura, datos y servicios reales.

## 4. Matriz de controles inicial

| ID | Control | Objetivo / riesgo | Mecanismo | Estado actual | Evidencia | Limitación |
|---|---|---|---|---|---|---|
| SV-001 | Secret Material Scan | Evitar incorporación accidental de claves privadas y patrones de credenciales críticas | Detección determinista de patrones de alto riesgo | Implementado | Workflow run | No sustituye secret scanning especializado |
| SV-002 | Workflow Least Privilege | Reducir abuso del `GITHUB_TOKEN` y permisos excesivos | Validación de `permissions` en workflows | Implementado | Workflow run | No demuestra seguridad completa del workflow |
| SV-003 | Dangerous Workflow Trigger | Detectar `pull_request_target` y otros vectores de ejecución privilegiada no justificados | Validación de triggers | Implementado | Workflow run | Requiere excepción formal si aparece un caso legítimo |
| SV-004 | Security Workflow Integrity | Evitar que el propio control de seguridad elimine su barrera sin trazabilidad | Presencia y validación de workflow crítico | Implementado | Workflow run | Sin protección nativa no impide escritura directa |
| SV-005 | Dependency Security | Identificar vulnerabilidades conocidas en dependencias | SCA/dependency review | `NOT_APPLICABLE` inicial | Decisión documentada | No existen todavía manifiestos de dependencias de aplicación que justifiquen el control |
| SV-006 | SAST | Detectar vulnerabilidades en código fuente | Analizador estático | `NOT_APPLICABLE` inicial | Decisión documentada | No existe todavía código de aplicación |
| SV-007 | IaC Security | Detectar configuraciones inseguras de infraestructura | Scanner IaC | `NOT_APPLICABLE` inicial | Decisión documentada | No existe infraestructura declarativa del producto |
| SV-008 | Container Security | Detectar vulnerabilidades en imágenes/configuración de contenedores | Scanner de imágenes | `NOT_APPLICABLE` inicial | Decisión documentada | No existen imágenes del producto |
| SV-009 | SBOM | Mantener inventario de componentes de software | Generación SBOM | `NOT_IMPLEMENTED` inicial | Registro de roadmap | Se implementará cuando exista software/dependencias reales |

## 5. Relación con marcos de referencia

### NIST SSDF 1.1

La implementación inicial se alinea conceptualmente con prácticas de preparación del entorno de desarrollo seguro, protección de componentes y reducción/detección de vulnerabilidades. SSDF proporciona prácticas y tareas de alto nivel que deben integrarse al SDLC, no un checklist universal que pueda declararse satisfecho únicamente por CI. citeturn0search0turn0search9

### NIST CSF 2.0

La arquitectura utiliza principalmente los resultados conceptuales de **Govern, Identify, Protect y Detect** para estructurar gobernanza, identificación de activos/riesgos, controles preventivos y detección. CSF 2.0 es orientado a resultados y no prescribe una implementación tecnológica única. citeturn0search12turn0search5

### ISO/IEC/IEEE 12207:2026 y 15288:2023

Security Validation se trata como capacidad transversal del ciclo de vida y no como una fase aislada. Los controles deben evolucionar con adquisición, desarrollo, operación, mantenimiento, evolución y retirada.

### ISO/IEC 25010:2023

La seguridad se relacionará posteriormente con los atributos de calidad y sus medidas verificables cuando existan requisitos y contexto del producto suficientes. No se inventan métricas de seguridad antes de disponer de objetivos verificables.

## 6. Workflow y evidencia

El workflow `.github/workflows/security-validation.yml` se ejecuta sobre Pull Requests hacia `main` y sobre cambios a `main` cuando corresponda para mantener visibilidad posterior.

La ejecución debe identificar:

- commit validado;
- workflow y versión del control;
- controles ejecutados;
- resultado individual;
- fallo y ubicación cuando corresponda;
- fecha/hora;
- estado final.

Un `SECURITY_VALIDATION=PASS` significa únicamente que los controles automatizados aplicables fueron satisfechos.

## 7. Política de fallo

Los controles `SV-001` a `SV-004` son barreras activas para el estado actual del repositorio. Un fallo debe terminar la ejecución con resultado distinto de PASS.

Los controles declarados `NOT_APPLICABLE` o `NOT_IMPLEMENTED` no deben maquillarse como PASS. Su condición debe quedar registrada y revisarse cuando cambie el contexto técnico.

## 8. Evolución

Cuando aparezca código e infraestructura reales, se incorporarán progresivamente, según riesgo y aplicabilidad:

- SAST;
- SCA y revisión de dependencias;
- secret scanning especializado;
- SBOM;
- análisis de IaC;
- análisis de contenedores;
- validación de configuración cloud;
- DAST;
- pruebas de seguridad de API;
- threat modeling automatizable y asistido;
- controles de supply-chain y procedencia;
- firma/proveniencia de artefactos.

Cada incorporación deberá activar análisis de impacto, actualizar la matriz y definir evidencia y limitaciones.

## 9. Riesgo residual

La capa inicial no garantiza ausencia de vulnerabilidades. Persisten, entre otros, riesgos de:

- vulnerabilidades lógicas o de diseño;
- errores de autorización/autenticación;
- dependencias futuras vulnerables;
- secretos no capturados por patrones deterministas;
- vulnerabilidades de infraestructura o proveedores;
- configuración operacional insegura;
- ataques de cadena de suministro;
- modificaciones directas de `main` mientras no exista enforcement nativo.

La ausencia de un control aplicable no debe confundirse con ausencia de riesgo.

## 10. Criterio de verdad

Nunca se afirmará que el Ecosistema está «seguro» únicamente porque Security Validation haya pasado. La afirmación permitida es que **los controles automatizados aplicables ejecutados en esa revisión fueron satisfechos**.

## 11. Evidencia de implementación

La unidad mínima de evidencia será:

`Issue → Branch → Commit → Workflow Run → Resultado → PR → Review → Merge → main`

Cuando un control sea `NOT_APPLICABLE` o `NOT_IMPLEMENTED`, debe existir una justificación documental y una condición que indique cuándo debe reevaluarse.
