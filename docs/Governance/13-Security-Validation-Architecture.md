# Arquitectura de Security Validation

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Baseline inicial de Security Validation  
**Fecha:** 2026-09-15  
**Issue:** #22

Security Validation es una capa transversal para detectar condiciones objetivas de riesgo antes de integrar cambios en `main`. No sustituye threat modeling, arquitectura de seguridad, análisis de riesgos, pruebas de penetración, revisión humana ni gestión de vulnerabilidades.

## Cadena de control

```text
Issue → Branch → Pull Request → Validate governance controls → Validate repository quality → Validate security controls → Validate engineering evidence → Review → Merge → main
```

## Controles iniciales

| ID | Control | Objetivo / riesgo | Mecanismo | Estado | Evidencia | Limitación |
|---|---|---|---|---|---|---|
| SV-001 | Secret Material Scan | Evitar claves privadas y credenciales críticas conocidas | Patrones deterministas | Implementado | Workflow run | No sustituye secret scanning especializado |
| SV-002 | Workflow Least Privilege | Reducir permisos excesivos del `GITHUB_TOKEN` | Validación de `permissions` | Implementado | Workflow run | No demuestra seguridad completa |
| SV-003 | Dangerous Workflow Trigger | Detectar `pull_request_target` no justificado | Validación de triggers | Implementado | Workflow run | Casos legítimos requieren excepción |
| SV-004 | Security Workflow Integrity | Evitar degradación silenciosa del control | Presencia e integridad básica | Implementado | Workflow run | No impide escritura directa |
| SV-005 | Dependency Security | Vulnerabilidades conocidas | SCA futuro | `NOT_APPLICABLE` inicial | Decisión documentada | No hay manifiestos de aplicación aún |
| SV-006 | SAST | Vulnerabilidades en código | SAST futuro | `NOT_APPLICABLE` inicial | Decisión documentada | No hay código de aplicación aún |
| SV-007 | IaC Security | Configuración insegura | Scanner IaC futuro | `NOT_APPLICABLE` inicial | Decisión documentada | No hay IaC del producto aún |
| SV-008 | Container Security | Vulnerabilidades en imágenes | Scanner futuro | `NOT_APPLICABLE` inicial | Decisión documentada | No hay imágenes del producto |
| SV-009 | SBOM | Inventario de componentes | Generación SBOM futura | `NOT_IMPLEMENTED` inicial | Roadmap | Se implementará con software/dependencias reales |

## Marcos de referencia

NIST SP 800-218 (SSDF 1.1) recomienda integrar prácticas de desarrollo seguro dentro del SDLC. NIST CSF 2.0 organiza la gestión del riesgo mediante Govern, Identify, Protect, Detect, Respond y Recover. Se utilizan como referencias y su uso no implica conformidad automática.

Security Validation es transversal al ciclo de vida y se relacionará con ISO/IEC/IEEE 12207:2026, 15288:2023 e ISO/IEC 25010:2023 mediante requisitos y medidas verificables cuando exista contexto suficiente.

## Política de fallo

SV-001..SV-004 son controles activos para el estado actual. Un fallo termina la ejecución con resultado distinto de PASS. `NOT_APPLICABLE` y `NOT_IMPLEMENTED` se conservan explícitamente y no se convierten artificialmente en PASS.

## Evolución

Cuando exista código e infraestructura reales se incorporarán, según riesgo y aplicabilidad, SAST, SCA, secret scanning especializado, SBOM, IaC, contenedores, configuración cloud, DAST, seguridad de API, threat modeling, supply chain y procedencia.

## Riesgo residual

La capa inicial no garantiza ausencia de vulnerabilidades. Persisten riesgos de vulnerabilidades lógicas, errores de autorización/autenticación, dependencias futuras vulnerables, secretos no capturados, infraestructura insegura, proveedores vulnerables, ataques de cadena de suministro y modificaciones directas de `main` mientras no exista enforcement nativo.

## Criterio de verdad

Nunca se afirmará que el Ecosistema está «seguro» únicamente porque Security Validation haya pasado. La afirmación permitida es que los controles automatizados aplicables ejecutados en esa revisión fueron satisfechos.

## Evidencia mínima

`Issue → Branch → Commit → Workflow Run → Resultado → PR → Review → Merge → main`
