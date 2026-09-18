# H-004 — Security Applicability and Evidence Matrix

**Issue:** #180  
**Baseline de referencia:** main @ 630af2096e2873a84517d1211c9c4ab8bfce7e35  
**Fecha de evaluación:** 2026-09-18

## Resultado

La inspección reproducible del árbol del repositorio no encontró código de aplicación ni manifests/lockfiles de dependencias de producto, Dockerfiles, imágenes o IaC del producto. Sí encontró GitHub Actions y configuración de automatización.

Por tanto, SV-005, SV-006 de producto, SV-007, SV-008 y SV-009 quedan justificados como `NOT_APPLICABLE` en la baseline actual. El código de workflows sí es analizable. Se intentó CodeQL para GitHub Actions, pero el run #2 terminó con `configuration error`; por tanto SV-006A queda `NOT_VERIFIED`, no `IMPLEMENTED`.

| Control | Objeto | Estado | Mecanismo | Evidencia requerida | Reevaluación |
|---|---|---|---|---|---|
| SV-001 | Secretos conocidos en contenido versionado | PASS | Scan determinista | Security Validation run | Nuevos formatos/secretos |
| SV-001A | Secret scanning especializado | NOT_VERIFIED | Capacidad administrativa no observable | Evidencia de configuración/ejecución de plataforma | Acceso verificable a Security settings |
| SV-002 | Permisos de workflows | PASS | Validación YAML | Security Validation run | Nuevo workflow |
| SV-003 | Triggers peligrosos | PASS | grep controlado | Security Validation run | Nuevo trigger |
| SV-004 | Integridad del workflow de seguridad | PASS | Autocomprobación | Security Validation run | Cambios del workflow/arquitectura |
| SV-005 | Dependencias de aplicación | NOT_APPLICABLE | No manifests/lockfiles de producto | Inventario de árbol | Primer manifest/lockfile |
| SV-006 | Código de aplicación | NOT_APPLICABLE | No source code de producto | Inventario de árbol | Primer source file de producto |
| SV-006A | GitHub Actions workflows | NOT_VERIFIED | CodeQL intentado | Run #2: analizó 10/10 workflows pero terminó `configuration error`; Code Scanning no está habilitado / endpoint requerido no accesible | Cuando Code Scanning/CodeQL sea habilitable y verificable |
| SV-007 | IaC de producto | NOT_APPLICABLE | No Terraform/cloud/IaC | Inventario de árbol | Primera IaC |
| SV-008 | Contenedores | NOT_APPLICABLE | No Dockerfile/imagen | Inventario de árbol | Primer Dockerfile/imagen |
| SV-009 | SBOM de producto | NOT_APPLICABLE | No composición de producto | Inventario de árbol | Primer componente/dependencia de producto |

## Limitaciones

- No se pudo verificar desde la integración actual la activación de GitHub Secret Scanning especializado.
- No se pudo convertir la ausencia de manifests en evidencia de ausencia futura: la condición debe reevaluarse cuando aparezca un artefacto de composición.
- Las referencias de GitHub Actions se consideran superficie de supply chain y deben mantenerse bajo revisión de cambios; no se declaran como SBOM.

## Regla de no sobreafirmación

`NOT_APPLICABLE` significa ausencia verificable del objeto técnico del control en la baseline evaluada; no significa «seguro». `NOT_VERIFIED` significa que la capacidad no fue demostrada; no significa «no existe».
