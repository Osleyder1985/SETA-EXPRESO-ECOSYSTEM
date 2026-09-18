# H-010 — Evaluación de runner propio y decisión de no adopción

## Control
- Issue: #192
- Unidad: 4 — evaluación de ejecución CI alternativa
- Fecha: 2026-09-18
- Autoridad del repositorio: GitHub
- Estado: **EVALUADO Y DESCARTADO**

## Objetivo

Evaluar si un self-hosted runner puede reducir el consumo de GitHub Actions manteniendo el objetivo económico de $0.

## Decisión

La variante de **runner propio queda descartada para este proyecto**.

La razón es de arquitectura y coste operativo: requiere disponer, dedicar o mantener hardware, además de asumir red, almacenamiento, actualizaciones, seguridad y administración. El proyecto no incorporará una PC ni otro equipo dedicado o administrado para ejecutar CI.

Esta decisión no invalida la utilidad técnica del concepto; únicamente establece que **no forma parte de la arquitectura operativa adoptada**.

## Consecuencias

- No se instalará un self-hosted runner.
- No se registrará ningún runner en GitHub.
- No se reservará hardware para CI.
- No se modificarán workflows para utilizar `self-hosted`.
- No se crearán credenciales de registro.
- H-011 deja de ser un procedimiento operativo y se conserva únicamente como registro histórico de la evaluación.
- H-012 se conserva como evidencia del gate de seguridad aplicado antes de cualquier posible registro.

## Alternativa adoptada

La continuidad a $0 se concentra en:

1. validación local reproducible;
2. Git como núcleo portable;
3. mirror/recuperación Git sin cambio de autoridad;
4. reducción de ejecuciones innecesarias de Actions;
5. evaluación de plataformas alternativas que no exijan infraestructura propia;
6. separación estricta entre capacidades esenciales y servicios sujetos a cuota.

## Límites

Esta unidad no autoriza migración de plataforma ni cambio de autoridad. GitHub continúa siendo la autoridad actual.

## Estado final

**VERIFICADO:** la alternativa fue evaluada y la decisión de no adoptar infraestructura propia quedó establecida.

**NO APLICABLE:** instalación, registro, pruebas de runner y preflight sobre hardware.

**CONSERVAR:** este documento permanece como registro de decisión y trazabilidad de la alternativa descartada.
