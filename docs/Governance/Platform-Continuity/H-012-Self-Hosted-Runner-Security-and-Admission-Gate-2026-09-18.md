# H-012 — Gate de seguridad para runner propio — alternativa descartada

## Control
- Issue: #192
- Unidad: 6 — seguridad y admisión antes del registro
- Fecha: 2026-09-18
- Autoridad: GitHub
- Estado: **CERRADO POR NO ADOPCIÓN DE LA VARIANTE**

## Propósito histórico

H-012 estableció controles preventivos para impedir el registro prematuro de un self-hosted runner.

La evaluación concluyó que el proyecto no adoptará esa arquitectura porque no se dedicará ni administrará hardware propio para CI.

## Decisión

**No registrar ni habilitar un self-hosted runner.**

Por tanto, el gate de admisión no se convierte en una actividad operativa pendiente.

## Controles conservados como referencia

Se mantienen documentados, para trazabilidad de la decisión:

- separación entre ejecución y autoridad;
- ausencia de credenciales persistentes;
- mínimo privilegio;
- aislamiento frente a código no confiable;
- control de conectividad;
- actualización del runner;
- selección verificable de labels.

Estos controles describen una alternativa evaluada, no requisitos de la arquitectura vigente.

## Arquitectura vigente

La continuidad $0 se basa en:

- validación local;
- Git portable;
- recuperación mediante mirror;
- minimización de consumo de CI alojado;
- evaluación de servicios alternativos gratuitos que no requieran infraestructura propia.

## Criterio de cierre

- [x] Variante de self-hosted runner evaluada.
- [x] Riesgos documentados.
- [x] Coste operativo de infraestructura propia identificado como incompatible con la decisión del proyecto.
- [x] No se registra runner.
- [x] No se modifica ningún workflow para usar `self-hosted`.

## Estado final

**CERRADO / NO APLICABLE.**

GitHub continúa siendo la autoridad del repositorio. Ningún runner propio forma parte de la arquitectura operativa.
