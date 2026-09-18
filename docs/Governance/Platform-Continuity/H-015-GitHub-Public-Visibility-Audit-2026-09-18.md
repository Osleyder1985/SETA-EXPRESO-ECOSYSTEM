# Auditoría de exposición pública — Issue #194

## Estado

**PREPARADA — CAMBIO DE VISIBILIDAD PENDIENTE DE REVIEW Y EJECUCIÓN CONTROLADA**

- Issue: #194
- Rama: `issue-194-public-repository-ci-zero-cost`
- Autoridad: GitHub
- Plataforma objetivo: GitHub exclusivamente
- CI objetivo: GitHub Actions con runners estándar hospedados por GitHub
- Costo objetivo: $0
- Codeberg/Woodpecker: fuera del alcance de la arquitectura adoptada

## Objetivo

Determinar si el contenido versionado actualmente en `main` presenta hallazgos evidentes que deban resolverse antes de convertir el repositorio en público.

Esta auditoría es una revisión de exposición del contenido versionado; no constituye una certificación criptográfica, un pentest ni una garantía de ausencia absoluta de secretos.

## Evidencia revisada

La revisión se realizó sobre `main` y sobre los workflows activos de GitHub Actions.

### 1. Documentación pública

- `README.md` existe y describe el propósito, estado y reglas de contribución del repositorio.
- La documentación de gobernanza está organizada bajo `docs/Governance/`.
- No se encontró una política de licencia explícita mediante búsquedas de términos `license`, `licencia`, `copyright` o `proprietary`.

### 2. Licencia

**Hallazgo H-194-01: no existe archivo `LICENSE` en el repositorio auditado.**

Esto no impide técnicamente que GitHub permita que el repositorio sea público. Sin embargo, significa que la intención jurídica de reutilización del contenido no está formalizada mediante una licencia de software en el árbol auditado.

**Decisión:** no se inventa ni selecciona una licencia sin una decisión explícita del proyecto. Si se requiere publicar el código/documentación bajo una licencia concreta, deberá resolverse mediante una Issue específica antes o después del cambio de visibilidad, según la decisión de gobernanza.

### 3. Patrones evidentes de material sensible

Las búsquedas realizadas no encontraron coincidencias para:

- contraseñas;
- API keys;
- credenciales;
- tokens explícitos;
- claves privadas PEM/RSA/OpenSSH;
- `GITHUB_TOKEN`;
- `github.token`;
- referencias textuales genéricas a `secrets.`.

Tampoco se identificaron, en la auditoría inicial, rutas de archivo con nombres típicamente asociados a secretos como `.env`, `id_rsa`, `.pem`, `.p12`, `.pfx` o archivos de credenciales.

**Limitación:** estas comprobaciones son búsquedas estáticas de patrones y nombres; no sustituyen un escaneo especializado de secretos ni garantizan que ningún dato sensible exista en la historia Git.

### 4. GitHub Actions

Los workflows actuales utilizan runners hospedados estándar y permisos explícitos. La revisión identificó:

- `actions/checkout@v4`;
- `actions/upload-artifact@v4`;
- uso de `github.token` dentro de los propios workflows para consultas a la API de GitHub;
- permisos declarados de lectura en los workflows revisados.

No se detectó una credencial estática incrustada en los archivos revisados.

El hecho de que el repositorio pase a público no requiere incorporar un proveedor CI externo.

### 5. Arquitectura de continuidad

La arquitectura adoptada para este cambio queda limitada a:

1. GitHub como autoridad;
2. GitHub Actions como CI hospedado;
3. validación local reproducible como mecanismo de contingencia;
4. Git/mirror como recuperación y portabilidad de los objetos Git;
5. sin runner propio;
6. sin Codeberg, Woodpecker, Gitea o Forgejo como plataforma operativa.

## Resultado de auditoría

**RESULTADO: CONDICIONADO — APTO PARA CONTINUAR LA PREPARACIÓN, PERO NO SE DEBE PRESENTAR COMO AUDITORÍA DE SECRETOS COMPLETA.**

No se encontró evidencia textual evidente que obligue a bloquear técnicamente la preparación del cambio de visibilidad.

Permanece abierto el punto de gobernanza sobre licencia.

## Regla de ejecución

El cambio de visibilidad no se ejecuta directamente sobre `main` mediante un commit.

La secuencia controlada es:

`Issue #194 → auditoría → correcciones necesarias → validación → PR → Review → Merge → cambio de visibilidad en GitHub → verificación posterior`

La modificación de la visibilidad es una operación de configuración de GitHub y no un cambio de contenido Git; por ello debe quedar registrada como evidencia posterior al merge.

## Criterios posteriores al cambio

Después de hacer público el repositorio se verificará:

- visibilidad pública efectiva;
- acceso anónimo al contenido;
- ausencia de exposición de credenciales conocidas;
- disponibilidad de GitHub Actions;
- ejecución de los workflows con runners estándar;
- ausencia de uso de runners grandes o facturables;
- estado de los controles de gobernanza;
- actualización de la documentación de continuidad $0.

## Fuentes externas de referencia

La documentación oficial de GitHub establece que los runners estándar hospedados por GitHub son gratuitos e ilimitados para repositorios públicos, mientras que los runners grandes tienen facturación incluso en repositorios públicos. Por tanto, la arquitectura deberá continuar utilizando únicamente runners estándar.


## Control de licencia

La ausencia de LICENSE se conserva como hallazgo de gobernanza y no se resuelve unilateralmente en este Issue. El cambio de visibilidad pública de GitHub y la decisión jurídica sobre licencia son controles distintos.
