# Convención de estructura y nomenclatura del repositorio

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.2.0  
**Estado:** Política propuesta para aprobación  
**Fecha:** 2026-09-15

---

## 1. Objetivo

Establecer una convención única para directorios y archivos del repositorio, reduciendo ambigüedad y evitando renombrados inconsistentes durante la evolución del proyecto.

## 2. Idioma

Los nombres de directorios y archivos utilizan **inglés**.

El contenido de la documentación utiliza **español** como idioma principal.

El código y los identificadores técnicos utilizarán inglés, salvo excepciones justificadas por una tecnología, estándar o integración externa.

## 3. Formato de nombres

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
