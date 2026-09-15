# Política de Labels para Issues y Pull Requests

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Vigente  
**Relacionado:** Issue #9

---

## 1. Propósito

Establecer una clasificación consistente para Issues y Pull Requests que facilite descubrimiento, priorización, filtrado, trazabilidad y lectura del historial de ingeniería.

Los labels son metadatos de gobernanza: **no sustituyen el título, el alcance, los criterios de aceptación ni la documentación del cambio**.

---

## 2. Regla obligatoria

Todo Issue y todo Pull Request del proyecto deberá tener al menos un label pertinente antes de considerarse una unidad de trabajo correctamente clasificada.

Cuando el trabajo atraviese varios dominios, se podrán utilizar varios labels, pero solo los que aporten información real.

Un PR hereda normalmente la clasificación principal del Issue que implementa y puede añadir una clasificación secundaria cuando su contenido lo justifique.

---

## 3. Labels actualmente disponibles y significado

La clasificación debe utilizar los labels realmente disponibles en GitHub. La baseline actual verificada del repositorio incluye:

| Label | Uso |
|---|---|
| `governance` | Gobierno, políticas, procesos, ciclo de vida, control de cambios, planificación y decisiones de gobierno. |
| `documentation` | Documentación, registros, evidencias documentales, índices y mantenimiento documental. |
| `architecture` | Arquitectura de sistema/software, diseño estructural y decisiones arquitectónicas. |

Los labels estándar o adicionales que GitHub pueda ofrecer no se consideran automáticamente parte de la taxonomía del proyecto: su incorporación deberá justificarse y documentarse.

---

## 4. Matriz de clasificación por tipo de trabajo

| Trabajo | Label principal recomendado | Secundarios posibles |
|---|---|---|
| Ciclo de vida, políticas, gobernanza | `governance` | `documentation` |
| Roadmap, planificación de ingeniería | `governance` | `documentation` |
| Documentos, registros, evidencia | `documentation` | `governance` |
| Arquitectura del Ecosistema | `architecture` | `governance`, `documentation` |
| Arquitectura de software | `architecture` | `documentation` |
| Cambio que actualiza política + documentos | `governance` | `documentation` |
| Cambio arquitectónico documentado | `architecture` | `governance`, `documentation` |

---

## 5. Reglas para Issues

Antes de iniciar una unidad de trabajo:

- el Issue debe describir objetivo, contexto, alcance y criterios de aceptación;
- debe identificar la fase/subfase del ciclo de vida cuando corresponda;
- debe incluir análisis de impacto inicial cuando sea relevante;
- debe tener labels pertinentes;
- no se debe usar un label para ocultar una clasificación ambigua.

Al cerrar el Issue, su estado y labels deben continuar describiendo correctamente la naturaleza del trabajo realizado.

---

## 6. Reglas para Pull Requests

Todo PR deberá:

- estar vinculado a un Issue;
- conservar los labels pertinentes del trabajo que integra;
- documentar el cambio y su motivo;
- declarar análisis de impacto;
- identificar artefactos afectados;
- registrar pruebas/evidencia;
- declarar explícitamente uno y solo uno de los estados formales del proyecto:
  - 🟢 `LISTO PARA FUSIÓN`;
  - 🟡 `NO FUSIONAR — TRABAJO PENDIENTE`.

La ausencia de un label no puede interpretarse como aprobación ni como ausencia de impacto.

---

## 7. Regularización histórica

Cuando un Issue o PR histórico carezca de labels, podrá regularizarse sin reabrirlo ni modificar su contenido sustantivo. La regularización es una mejora de metadatos y debe preservar su historial.

La baseline inicial de gobernanza fue regularizada durante la implementación del Issue #9 para los artefactos identificados sin clasificación.

---

## 8. Evolución de la taxonomía

La taxonomía crecerá con el proyecto. Cuando aparezcan dominios permanentes como requisitos, testing, seguridad, datos, DevOps u operaciones, se deberá evaluar la incorporación de labels específicos antes de utilizarlos como clasificación oficial.

La ampliación de la taxonomía debe considerar:

1. necesidad real de filtrado;
2. ausencia de solapamiento semántico;
3. estabilidad del concepto;
4. utilidad para métricas y Roadmap;
5. compatibilidad con el flujo de Issues/PRs;
6. documentación de su significado.

---

## 9. Relación con el Roadmap

Los labels ayudan a clasificar el trabajo; el Roadmap determina dónde encaja ese trabajo en el ciclo de vida.

```text
Label
  ↓
Dominio / naturaleza del trabajo
  ↓
Issue
  ↓
Fase A–O
  ↓
PR
  ↓
Evidence
  ↓
Baseline
```

**Label ≠ fase.** Un mismo label puede aparecer en múltiples fases porque los procesos transversales acompañan todo el ciclo de vida.
