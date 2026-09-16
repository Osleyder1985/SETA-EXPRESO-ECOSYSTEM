# Enforcement técnico de protección de `main`

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Issue de origen:** #80  
**Actualización de auditoría de integración:** #82  
**Estado:** Especificación, evaluación de capacidad y limitación de integración documentada  
**Fecha:** 2026-09-15  

---

## 1. Propósito

Definir el perfil técnico que deberá aplicarse a `main` cuando la capacidad de protección nativa de GitHub sea compatible con la configuración del repositorio, y dejar evidencia explícita de qué controles están actualmente disponibles, cuáles están configurados y cuáles permanecen pendientes por una restricción de plataforma o de acceso de la integración.

La política operativa no cambia:

```text
Issue → Branch → Commits → Pull Request →
Governance / Quality / Security / Evidence →
Review → Merge → main
```

Ningún workflow, documento o excepción autoriza una modificación directa de `main`.

## 2. Estado verificado de la plataforma y de la integración

El repositorio `Osleyder1985/SETA-EXPRESO-ECOSYSTEM` es actualmente **privado** y tiene `main` como rama por defecto.

La auditoría de permisos realizada sobre la integración GitHub demostró dos hechos que deben mantenerse separados:

1. La cuenta GitHub `Osleyder1985` posee permiso **`admin`** sobre el repositorio.
2. La integración GitHub utilizada en este entorno **no puede acceder al endpoint administrativo de Branch Protection** ni consultar Rulesets para este repositorio bajo las condiciones actuales de acceso.

Evidencia de integración:

```text
Repository permissions:
admin = true
maintain = true
push = true
triage = true
pull = true

Collaborator permission:
Osleyder1985 = admin

GET /repos/Osleyder1985/SETA-EXPRESO-ECOSYSTEM/branches/main/protection
→ HTTP 403: Resource not accessible by integration

GET /repos/Osleyder1985/SETA-EXPRESO-ECOSYSTEM/rulesets
→ HTTP 403 bajo las condiciones actuales de acceso al repositorio privado
```

La conclusión **no** es que la cuenta carezca de privilegios administrativos. La conclusión es que la autorización/capacidad efectiva expuesta por la integración no permite utilizar esos endpoints administrativos desde este entorno.

Además, la documentación oficial vigente de GitHub indica que la disponibilidad de protected branches y rulesets depende del plan y de la visibilidad del repositorio. Mientras el repositorio privado permanezca bajo una configuración sin capacidad compatible de enforcement nativo, no se considerará disponible el enforcement requerido.

Fuentes normativas externas:

- GitHub Docs — Managing protected branches: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches
- GitHub Docs — About rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets

## 3. Perfil objetivo de protección

Cuando la capacidad esté disponible, el objetivo mínimo para `main` será:

| Control | Requisito objetivo | Razón |
|---|---|---|
| Pull Request | Obligatorio | Evitar integración sin trazabilidad de PR |
| Reviews | Obligatoria al menos 1 aprobación independiente cuando sea viable | SoD y revisión humana |
| Último push revisable | Requerir aprobación posterior al último cambio cuando la configuración lo permita | Evitar aprobar una versión distinta de la revisada |
| Status checks | Governance, Quality, Security y Evidence requeridos | Gates verificables antes de merge |
| Branch up-to-date | Preferente cuando el costo operativo sea aceptable | Evitar integrar contra una base obsoleta |
| Conversation resolution | Obligatoria | Cerrar observaciones de revisión |
| Force push | Bloqueado | Preservar integridad e historial |
| Deletion | Bloqueada | Preservar la rama protegida |
| Bypass | Mínimo y explícito | Reducir excepciones silenciosas |
| Administradores | No bypass cuando la plataforma y el modelo de operación lo permitan | Fortalecer enforcement |
| Merge queue | Evaluar posteriormente | Útil cuando aumente la concurrencia |
| Signed commits | Evaluar según riesgo y capacidad operativa | Integridad/autenticidad adicional |

La configuración final deberá respetar el modelo SoD I0–I3 y no podrá utilizar una regla técnica para simular una aprobación independiente que no exista.

## 4. Status checks candidatos

Los workflows existentes en el repositorio son:

- `Governance Validation`
- `Quality Validation`
- `Security Validation`
- `Evidence Validation`

Los nombres de los jobs deberán permanecer inequívocos para poder seleccionarlos como required status checks. GitHub advierte que nombres de jobs duplicados entre workflows pueden producir resultados ambiguos al requerir status checks.

La selección definitiva de checks deberá hacerse sobre ejecuciones reales del PR de implementación y conservar sus nombres exactos como evidencia.

## 5. Enforcement actual

Mientras la protección nativa no esté disponible o no pueda ser verificada mediante la integración:

### Preventivo/compensatorio

Los workflows validan propiedades del PR, incluyendo:

- branch de origen distinta de `main`;
- convención de nombre de branch;
- Issue asociado;
- análisis de impacto;
- labels;
- estado formal de integración;
- baseline documental.

### Detectivo

El workflow de Governance Validation inspecciona las actualizaciones de `main` y falla cuando no encuentra un Pull Request asociado al commit, marcando el evento como `SUSPICIOUS_DIRECT_UPDATE`.

Este control **no bloquea físicamente** una escritura permitida por GitHub y no debe describirse como equivalente a branch protection.

## 6. Protocolo de activación futura

Cuando cambie la capacidad de la plataforma o el plan del repositorio, o cuando exista una integración con acceso administrativo verificable:

1. Abrir una Issue específica para la activación.
2. Crear branch desde el `main` vigente.
3. Registrar análisis de impacto y riesgo.
4. Verificar los status checks exactos mediante un PR real.
5. Configurar protección/ruleset para `main`.
6. Deshabilitar bypasses innecesarios.
7. Verificar force push y deletion bloqueados.
8. Verificar requisito de PR y reviews.
9. Verificar required status checks.
10. Ejecutar un PR de prueba que demuestre el comportamiento esperado.
11. Registrar evidencia de configuración efectiva.
12. Actualizar este documento y `07-Main-Protection-Strategy.md`.
13. Cerrar la Issue únicamente con evidencia verificable.

## 7. Criterio de verdad

Se considerará que `main` está **técnicamente protegida** solamente si una prueba verificable demuestra que GitHub impide efectivamente las operaciones configuradas.

No constituyen evidencia suficiente:

- la existencia de una política;
- la existencia de un workflow;
- un check verde;
- una promesa de configuración;
- una captura sin contexto verificable;
- la ausencia de incidentes;
- que la cuenta GitHub tenga permiso `admin` si la integración no puede verificar la configuración efectiva.

## 8. Limitación de Issue #80 y auditoría #82

Issue #80 completó el perfil documental de enforcement, los checks candidatos, el protocolo de activación y los controles compensatorios, pero no puede declarar completada la protección técnica nativa sin evidencia verificable.

La auditoría #82 añade una precisión de arquitectura de integración: **la cuenta `Osleyder1985` sí tiene permiso `admin`, pero la integración utilizada por ChatGPT no puede consultar el endpoint administrativo de Branch Protection ni Rulesets bajo las condiciones actuales**.

Por ello, la ausencia de una lectura exitosa del endpoint no debe interpretarse como evidencia de que `main` está desprotegida. Debe registrarse como **limitación de observabilidad administrativa de la integración** hasta disponer de una vía de verificación compatible.

## 9. Evidencia requerida para cierre técnico

El cierre completo de la capacidad deberá conservar como mínimo:

- Issue de activación;
- branch y commits;
- PR de configuración/documentación;
- estado de ruleset o branch protection;
- configuración efectiva de required reviews;
- configuración efectiva de required status checks;
- evidencia de bloqueo de force push;
- evidencia de bloqueo de deletion;
- evidencia de bypasses autorizados, si existen;
- resultado de PR de prueba;
- workflow runs correspondientes;
- análisis de impacto;
- riesgo residual actualizado;
- evidencia de la vía administrativa utilizada para verificar la configuración cuando la integración estándar no pueda leerla.

## 10. Relación con Governance Core

Este control se integra con:

- `07-Main-Protection-Strategy.md`;
- `10-Governance-Enforcement-Architecture.md`;
- `49-Segregation-of-Duties.md`;
- `50-Non-Conformance-Management.md`;
- `51-Engineering-Change-Authority.md`;
- `52-Research-Governance.md`;
- `27-Governance-Control-Matrix-SoD-NC-Change-Research.md`.
