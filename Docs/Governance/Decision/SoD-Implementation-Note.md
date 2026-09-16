# Nota de implementación de SoD

**Issue:** #49  
**Estado:** En preparación controlada

## Desviación de proceso registrada
Durante la preparación inicial de Issue #49 se realizaron accidentalmente escrituras sobre `main` antes de crear la rama dedicada. Esto contradice el flujo establecido Issue → Branch → PR.

Los commits afectados se conservan deliberadamente para mantener trazabilidad histórica. La corrección operativa consiste en continuar desde el estado actual, crear la rama de trabajo y retirar de `main` los artefactos de preparación mediante commits trazables, sin reescribir historia.

## Principio
La desviación no se considera una justificación para eliminar evidencia histórica. Debe quedar registrada y servir como entrada para la mejora del enforcement del flujo de cambios.
