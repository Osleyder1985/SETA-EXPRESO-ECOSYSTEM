# H-009 — Diseño de mirror Git y recuperación

## Estado

**Issue:** #192  
**Unidad:** 3 — Mirror Git y recuperación  
**Fecha:** 2026-09-18  
**Autoridad actual:** GitHub  
**Objetivo económico:** costo monetario $0 siempre que técnicamente sea posible.

## Objetivo

Definir un mecanismo de continuidad basado en Git que permita conservar y recuperar el historial del repositorio fuera de GitHub sin convertir el mirror en autoridad ni alterar la rama principal.

## Alcance

Esta unidad establece el diseño y una herramienta local segura para crear/actualizar un mirror Git. **No crea todavía un mirror externo ni modifica la configuración de GitHub.**

El mirror cubre el estado Git que puede representarse mediante objetos y referencias. No sustituye la exportación de metadatos de la plataforma.

## Diseño aprobado para implementación controlada

### 1. Núcleo portable

Git es el núcleo de continuidad. Un mirror creado con `git clone --mirror` es bare y refleja todas las referencias del repositorio; Git documenta que esto incluye ramas, tags, notas y otras refs, junto con una configuración de actualización remota. citeturn2search0

### 2. Fuente y autoridad

- Fuente actual: repositorio GitHub.
- Autoridad: GitHub continúa siendo la autoridad durante #192.
- Mirror: copia de recuperación, no fuente normativa.
- No se permiten cambios de autoridad por la mera existencia del mirror.

### 3. Operación local $0

La ruta primaria es una copia bare local mantenida con herramientas Git estándar. No requiere minutos de GitHub Actions ni un servicio SaaS adicional.

La herramienta `scripts/continuity/create-git-mirror.sh`:

1. valida parámetros;
2. crea el mirror con `git clone --mirror` cuando el destino no existe;
3. actualiza un mirror existente con `git remote update --prune`;
4. ejecuta `git fsck --full` para detectar problemas de integridad;
5. muestra refs y el HEAD del mirror;
6. no incorpora credenciales en archivos del repositorio;
7. no ejecuta `git push` hacia ningún destino externo.

### 4. Integridad

Una recuperación controlada debe verificar como mínimo:

- existencia de HEAD;
- refs de ramas;
- refs de tags;
- objetos Git íntegros mediante `git fsck --full`;
- comparación del SHA de refs seleccionadas contra la fuente;
- capacidad de clonar el mirror como repositorio operativo.

La validación de recuperación completa queda para la Unidad 6.

## Qué conserva Git y qué no

| Capacidad | Mirror Git | Tratamiento de continuidad |
|---|---|---|
| Commits e historial | Sí | Preservado por objetos Git |
| Ramas | Sí | Preservadas como refs |
| Tags | Sí | Preservados como refs |
| Otras refs Git | Sí | Incluidas por `--mirror` |
| Archivos de configuración versionados | Sí | Preservados en commits |
| Issues | No | Exportación/evidencia separada |
| Pull Requests | No | Exportación/evidencia separada |
| Reviews/comentarios | No | Exportación/evidencia separada |
| Labels | No | Catálogo/exportación separada |
| Workflow runs | No | Evidencia separada |
| Secrets/tokens | No | Nunca deben almacenarse en Git |
| Permisos/configuración SaaS | No | Registro/configuración externa |

## Mirror externo futuro

La existencia de un mirror externo requerirá una unidad posterior y evidencia de control de acceso, dirección de sincronización, frecuencia, integridad y recuperación.

Forgejo documenta tanto pull mirrors como push mirrors y advierte que un push mirror puede sobrescribir el destino; por tanto, cualquier configuración futura deberá tratarse como una operación controlada, no como una acción automática. citeturn1search0

## Portabilidad hacia Forgejo

Forgejo puede utilizar mirrors para conservar ramas, tags y commits entre repositorios. Su documentación también deja claro que Actions no son idénticas a GitHub Actions, por lo que el mirror Git no debe confundirse con equivalencia funcional de la plataforma. citeturn1search0turn1search2

## Seguridad

- No se almacenan PAT, contraseñas, claves SSH privadas ni secretos en el repositorio.
- La URL de origen puede proporcionarse por argumento o remoto previamente configurado.
- El script no imprime variables secretas.
- El mirror local debe almacenarse en una ubicación con controles de acceso apropiados.
- La restauración hacia un servicio remoto no forma parte de esta unidad.

## Criterios de aceptación de la Unidad 3

- [x] Diseño del mirror documentado.
- [x] Separación entre autoridad y copia de recuperación.
- [x] Conservación de refs Git definida.
- [x] Límites frente a Issues/PRs/secrets/configuración SaaS documentados.
- [x] Herramienta local sin credenciales embebidas incorporada.
- [ ] Ejecución real sobre un checkout local del repositorio.
- [ ] Prueba de recuperación completa.
- [ ] Mirror externo operativo.

## Estado

**VERIFICADO:** diseño y herramienta incorporados en la rama de #192.  
**PENDIENTE:** ejecución real y prueba de recuperación.  
**NO VERIFICADO:** equivalencia de plataforma, recuperación de metadatos GitHub y mirror externo.

## Límite de esta unidad

Este documento no autoriza migración, cambio de autoridad, creación de una instancia Forgejo/Gitea ni configuración de un mirror externo. Es una unidad de diseño e implementación local dentro de Issue #192.
