# Flujo de control de cambios y trazabilidad

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.5.0  
**Estado:** Política vigente  
**Idioma documental:** Español  
**Fecha:** 2026-09-15

---

## 1. Propósito

Establecer el mecanismo obligatorio mediante el cual se proponen, analizan, implementan, revisan, integran y trazan los cambios del repositorio del Ecosistema.

La política busca preservar la integridad de la línea base, evitar cambios no controlados y mantener coherencia entre requisitos, arquitectura, diseño, código, pruebas, configuración, datos, documentación y evidencia.

## 2. Regla fundamental

A partir de la adopción de esta política, **ningún cambio de trabajo deberá realizarse directamente sobre `main`**.

`main` constituye la línea base integrada y controlada del proyecto. Los cambios deberán llegar a `main` exclusivamente mediante un Pull Request revisado y aprobado.

La inicialización histórica del repositorio puede contener commits directos a `main`; dichos commits constituyen una excepción de bootstrap y no un precedente para el desarrollo posterior.

## 3. Flujo obligatorio

```text
Issue
  ↓
Análisis del problema / necesidad / oportunidad
  ↓
Definición de alcance y criterios de aceptación
  ↓
Branch de trabajo
  ↓
Implementación
  ↓
Análisis de impacto
  ↓
Actualización de todos los artefactos afectados
  ↓
Decision Record cuando corresponda
  ↓
Pruebas / validación / evidencia
  ↓
Pull Request
  ↓
Governance Validation
  ↓
Quality Validation
  ↓
Security Validation
  ↓
Evidence Validation
  ↓
Revisión
  ↓
Correcciones, si son necesarias
  ↓
Aprobación
  ↓
Merge
  ↓
main
  ↓
Post-Merge Governance Detection
```

La arquitectura automatizada que implementa las capas de Governance, Quality y Security Validation está definida en `10-Governance-Enforcement-Architecture.md`, `12-Quality-Validation-Architecture.md` y `13-Security-Validation-Architecture.md`.

## 4. Issue obligatorio

Todo cambio significativo deberá estar respaldado por un Issue antes de comenzar su implementación.

El Issue deberá explicar, como mínimo:

- problema, necesidad u oportunidad;
- contexto y motivo del cambio;
- alcance;
- exclusiones cuando sean relevantes;
- criterios de aceptación;
- riesgos conocidos;
- artefactos potencialmente afectados cuando puedan identificarse anticipadamente.

Los Issues del proyecto se redactarán en español.

Un Issue podrá ser resuelto mediante uno o varios Pull Requests cuando el cambio requiera dividir la implementación en unidades controlables.

## 5. Branch de trabajo

Toda implementación deberá realizarse en una branch distinta de `main`.

Las branches asociadas a Issues seguirán la convención `issue-<numero>-<slug-corto>` definida en `05-Repository-Naming-Convention.md`.

La branch deberá partir de una línea base conocida y permanecer asociada al Issue que origina el trabajo.

No se utilizará `main` como espacio de trabajo para modificaciones parciales, experimentales o en curso.

## 6. Pull Request obligatorio

Todo cambio destinado a integrarse en `main` deberá presentarse mediante un Pull Request asociado al Issue correspondiente.

El Pull Request deberá describir en español, como mínimo:

1. qué cambió;
2. por qué cambió;
3. alcance del cambio;
4. análisis de impacto;
5. artefactos afectados;
6. pruebas, validaciones y evidencias realizadas;
7. relación explícita con el Issue;
8. trabajo pendiente, si existe;
9. estado explícito de integración: **LISTO PARA FUSIÓN** o **NO FUSIONAR — TRABAJO PENDIENTE**.

El título deberá cumplir la convención `Módulo/Archivo: Acción a realizar.` y el PR deberá tener al menos un label pertinente.

## 7. Análisis de impacto obligatorio

Toda adición, modificación, actualización, movimiento, renombrado o eliminación de un artefacto del repositorio deberá activar un análisis de impacto sobre los demás artefactos relacionados.

La regla formal es:

> Toda adición, modificación, actualización, movimiento, renombrado o eliminación de un artefacto del repositorio debe activar un análisis de impacto sobre los demás artefactos relacionados. Si el cambio afecta a otro artefacto, este deberá actualizarse en la misma unidad de cambio o quedar explícitamente registrado como trabajo pendiente trazable.

Como mínimo deberán considerarse estas relaciones:

| Cambio origen | Posibles artefactos afectados |
|---|---|
| Documento → documento | Referencias, definiciones, versiones, terminología y dependencias documentales |
| Requisito → arquitectura/diseño | Arquitectura, ADR/EDR, diseño, interfaces, pruebas y trazabilidad |
| Arquitectura → código | Componentes, interfaces, configuración, infraestructura y documentación técnica |
| Código → pruebas | Pruebas unitarias, integración, regresión, evidencia y documentación |
| Seguridad → arquitectura/diseño | Controles, amenazas, requisitos, configuración y pruebas de seguridad |
| Pruebas → requisitos | Criterios de aceptación, trazabilidad y estado de verificación/validación |
| Configuración → DevOps | Pipelines, despliegue, infraestructura, secretos y runbooks |
| Datos → documentación | Modelos, contratos, migraciones, calidad y trazabilidad |
| Ingeniería → investigación | Hipótesis, métricas, evidencia, metodología y resultados científicos |
| Movimiento/renombrado → referencias | Enlaces, índices, referencias cruzadas, automatizaciones y documentación |
| Seguridad automatizada → gobernanza/calidad | Matriz de controles, Quality Gates, evidencia, Roadmap y workflows |
| Decisión material → arquitectura/diseño/riesgo | ADR/EDR, requisitos, alternativas, criterios, trade-offs, consecuencias, riesgos y evidencia |

## 8. Decision Records como parte del cambio controlado

Cuando una unidad de cambio implique una decisión material de arquitectura o ingeniería, deberá crearse, actualizarse o supersederse un `ADR` o `EDR` según corresponda, de acuerdo con `19-Decision-Governance.md`.

Un Decision Record no sustituye al Issue ni al Pull Request. Su función es conservar el razonamiento técnico de la decisión y mantener su trazabilidad histórica.

Una decisión existente que deje de ser válida no deberá eliminarse para ocultar la historia. Se conservará su estado y se utilizará `Supersedes` / `Superseded by` para representar la evolución.

## 9. Criterio de cierre del cambio

Un cambio no se considerará completo únicamente porque el archivo directamente modificado sea correcto.

Antes del Pull Request deberá comprobarse que:

- las dependencias conocidas fueron identificadas;
- los artefactos afectados fueron actualizados;
- las referencias no quedaron rotas;
- los requisitos y decisiones mantienen trazabilidad;
- los Decision Records aplicables están creados o actualizados;
- las pruebas correspondientes fueron ejecutadas o justificadamente planificadas;
- la evidencia relevante quedó registrada;
- Governance Validation, Quality Validation y Security Validation fueron ejecutadas cuando correspondan;
- cualquier pendiente quedó identificado y trazado.

## 10. Revisión e integración

La revisión del Pull Request deberá comprobar tanto la corrección del cambio como su coherencia con el resto del Ecosistema.

La aprobación no deberá limitarse a revisar el archivo modificado. Debe considerar alcance, impacto, trazabilidad, calidad, seguridad, pruebas y evidencia según la naturaleza del cambio.

El merge representa la integración controlada del cambio en la línea base `main`.

Mientras no exista branch protection/rulesets efectivos, los workflows de Governance, Quality y Security Validation son controles compensatorios/detectivos y **no constituyen un mecanismo técnico equivalente a una rama protegida**.

## 11. Evidencia de ingeniería

Cuando corresponda, el cambio deberá conservar la siguiente cadena de evidencia:

```text
Problema
  ↓
Objetivo
  ↓
Requisito
  ↓
Issue
  ↓
ADR / EDR
  ↓
Diseño / Implementación
  ↓
Pull Request
  ↓
Commit
  ↓
Governance Validation
  ↓
Quality Validation
  ↓
Security Validation
  ↓
Test
  ↓
Release
  ↓
Evidencia operacional
```

No todos los cambios requerirán todos los elementos de la cadena, pero la ausencia de un elemento relevante deberá ser justificable.

## 12. Relación con el ciclo de vida

Este flujo es un mecanismo transversal del ciclo de vida maestro. No constituye una fase independiente.

Se aplica durante requisitos, arquitectura, diseño, construcción, pruebas, despliegue, operación, mantenimiento, evolución, mejora y retirada cuando exista un cambio controlado.

La integración explícita del flujo en el ciclo maestro se establece en `Docs/Governance/00-Software-Lifecycle-Master.md`.

## 13. Relación con otras políticas

Esta política debe interpretarse conjuntamente con:

- `00-Software-Lifecycle-Master.md`;
- `03-Artifacts-And-Evidence.md`;
- `04-Quality-Gates.md`;
- `05-Repository-Naming-Convention.md`;
- `07-Main-Protection-Strategy.md`;
- `08-Software-Roadmap.md`;
- `09-Issue-And-Pull-Request-Labeling-Policy.md`;
- `10-Governance-Enforcement-Architecture.md`;
- `11-Governance-Control-Matrix.md`;
- `12-Quality-Validation-Architecture.md`;
- `13-Security-Validation-Architecture.md`;
- `19-Decision-Governance.md`;
- `20-Decision-Governance-Control-Matrix.md`.

Las futuras políticas de configuración, seguridad, calidad, DevOps y documentación deberán mantener compatibilidad con este flujo.

## 14. Regla de decisión

Ante cualquier duda sobre si un cambio requiere Issue, branch, análisis de impacto o Pull Request, se aplicará el criterio más conservador: **el cambio se tratará como controlado y deberá seguir el flujo completo** hasta que exista una política específica que establezca una excepción.

## 15. Protección de `main` bajo restricciones de plataforma

Mientras el repositorio permanezca privado bajo GitHub Free y no disponga de branch protection/rulesets efectivos, la integridad de `main` se gestionará mediante la estrategia de controles compensatorios definida en `07-Main-Protection-Strategy.md` y la arquitectura de enforcement definida en `10-Governance-Enforcement-Architecture.md`.

Los workflows de gobernanza tienen carácter de control automatizado, compensatorio y/o detectivo. **No deben interpretarse como protección técnica equivalente a branch protection.**

La afirmación de que `main` está técnicamente protegida solo podrá utilizarse cuando la capacidad efectiva de la plataforma haya sido verificada.
