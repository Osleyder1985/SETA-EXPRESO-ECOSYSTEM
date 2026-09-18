# H-011 — Preflight de hardware para runner propio — alternativa descartada

## Control
- Issue: #192
- Unidad: 5 — evaluación de hardware para runner propio
- Fecha: 2026-09-18
- Autoridad del repositorio: GitHub
- Estado: **CERRADO POR DECISIÓN ARQUITECTÓNICA**

## Propósito histórico

H-011 definió un preflight de solo lectura para evaluar una máquina existente como self-hosted runner.

La alternativa fue posteriormente descartada: el proyecto **no dedicará ni administrará una PC para CI**.

## Decisión

No se ejecutará este preflight sobre hardware del proyecto y no se continuará con:

- selección de hardware;
- instalación de runner;
- registro de runner;
- configuración de servicios;
- pruebas de Quality Validation mediante self-hosted runner.

## Artefacto operativo

El script `scripts/continuity/self-hosted-runner-preflight.sh` queda retirado del árbol operativo del proyecto porque ya no existe una unidad activa que lo utilice.

El documento H-011 se conserva para trazabilidad histórica de la evaluación realizada bajo Issue #192.

## Criterios que quedan sin aplicar

Los criterios de SO, arquitectura, CPU/RAM, disco, red, privilegios, contenedores y seguridad del runner no constituyen requisitos de la arquitectura adoptada.

## Alternativa vigente

La validación reproducible se realizará localmente, sin self-hosted runner y sin hardware de CI administrado por el proyecto.

## Estado final

**CERRADO / NO APLICABLE.**

La conservación de este documento no implica que exista un runner ni que se planee instalar uno.
