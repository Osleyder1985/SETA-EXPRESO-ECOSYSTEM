# Convención de estructura y nomenclatura del repositorio

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.3.0  
**Estado:** Política vigente  
**Fecha:** 2026-09-15

---

## 1. Objetivo

Establecer una convención única para directorios, archivos y branches del repositorio, reduciendo ambigüedad y evitando renombrados inconsistentes durante la evolución del proyecto.

## 2. Idioma

Los nombres de directorios y archivos utilizan **inglés**.

El contenido de la documentación utiliza **español** como idioma principal.

El código y los identificadores técnicos utilizarán inglés, salvo excepciones justificadas por una tecnología, estándar o integración externa.

## 3. Formato de nombres de archivos

La convención general es:

```text
[Prefix-]Word-Word-Word.extension
```

Reglas:

1. Cada palabra comienza con mayúscula.
2. El resto de la palabra se escribe en minúscula.
3. Las palabras se separan con `-`.
4. Los prefijos numéricos utilizan dos dígitos cuando forman una secuencia.
5. Las extensiones se escriben en minúscula.
6. No se utilizará `snake_case` para nombres controlados del repositorio.
7. No se utilizará `kebab-case` completamente en minúsculas para documentos controlados.

## 4. Ejemplos correctos

```text
01-Software-Lifecycle-Audit.md
02-Standards-Lifecycle-Matrix.md
03-Artifacts-And-Evidence.md
04-Quality-Gates.md
05-Repository-Naming-Convention.md
06-Change-Control-Workflow.md
```

## 5. Ejemplos incorrectos

```text
01-CICLO-DE-VIDA-AUDITORIA.md
software-lifecycle-audit.md
software_lifecycle_audit.md
01_software_lifecycle_audit.md
01-Software_lifecycle-Audit.md
```

## 6. Directorios

Los directorios seguirán la misma convención de palabras, sin extensión:

```text
Docs/
Governance/
Requirements/
Architecture/
Testing/
Infrastructure/
```

## 7. Excepciones

`README.md`, `.github/` y otros nombres impuestos por convenciones de herramientas podrán conservar su forma estándar. Las excepciones deliberadas deben documentarse cuando sea necesario.

## 8. Aplicación

Esta política aplica a nuevos artefactos y modificaciones estructurales. Cuando un archivo existente contradiga la política, se renombrará mediante un cambio controlado y se actualizarán todas las referencias afectadas.

## 9. Control de cambios e impacto

Los cambios de nombres, movimientos, adiciones, modificaciones o eliminaciones de artefactos están sujetos al flujo definido en `06-Change-Control-Workflow.md`.

En particular, cualquier cambio estructural deberá incluir un análisis de impacto sobre referencias, índices, enlaces, automatizaciones, trazabilidad y demás artefactos dependientes. Cuando el impacto requiera actualizar otros artefactos, estos deberán actualizarse en la misma unidad de cambio o quedar registrados como trabajo pendiente trazable.

## 10. Convención de branches

Las branches de trabajo asociadas a Issues utilizarán:

```text
issue-<numero>-<slug-corto>
```

Ejemplos:

```text
issue-13-governance-enforcement
issue-14-requirements-baseline
issue-15-system-discovery
```

Reglas:

1. `main` no se utilizará como branch de trabajo.
2. Toda branch de trabajo deberá corresponder a un Issue existente.
3. El número del Issue deberá aparecer en la branch.
4. El slug será corto, descriptivo y en minúsculas.
5. Las palabras del slug se separarán con `-`.
6. No se utilizarán espacios ni caracteres especiales.
7. La branch deberá partir de una línea base conocida.

Esta convención permite que Governance Validation compruebe automáticamente una relación mínima entre `Issue` y `Branch`.

Las excepciones deberán estar justificadas en el Issue/PR y no deberán utilizarse para trabajar directamente sobre `main`.
