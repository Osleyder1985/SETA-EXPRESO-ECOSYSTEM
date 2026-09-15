# Arquitectura de Quality Validation

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Propuesta para aprobación mediante PR asociado al Issue #20  
**Idioma documental:** Español  
**Fecha:** 2026-09-15  
**Issue:** #20

---

## 1. Propósito

Definir una capa de **Quality Validation** que transforme criterios objetivos de calidad en controles ejecutables y evidencia reproducible antes de integrar cambios en `main`.

Quality Validation no constituye una certificación de calidad del producto. Un resultado `PASS` significa únicamente que los controles definidos para la unidad de cambio y el contexto actual fueron satisfechos.

## 2. Principios

1. **Objetividad:** cada control debe tener una condición verificable.
2. **Evidencia:** cada ejecución debe dejar un resultado observable en CI.
3. **Aplicabilidad:** un control no aplicable debe identificarse como `NOT_APPLICABLE`, no disfrazarse como `PASS`.
4. **Proporcionalidad:** los controles evolucionan con el riesgo y la naturaleza del sistema.
5. **Independencia lógica:** Governance Validation, Quality Validation y Security Validation son capas diferenciadas.
6. **No sobreafirmación:** pasar los checks no demuestra por sí solo ausencia de defectos.
7. **Reproducibilidad:** las validaciones deben ejecutarse de forma determinista siempre que sea razonablemente posible.
8. **Costo controlado:** en la fase actual se priorizan mecanismos gratuitos y mantenibles.

## 3. Posición en el flujo

```text
Issue
  ↓
Branch
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
Review / Approval
  ↓
Merge
  ↓
main
```

Quality Validation es una capa previa a la integración. No sustituye la revisión humana ni los gates del ciclo de vida.

## 4. Controles iniciales

| ID | Control | Objetivo | Mecanismo | Evidencia | Limitación |
|---|---|---|---|---|---|
| QV-001 | Archivos Markdown no vacíos | Evitar artefactos documentales vacíos | Shell | Check run | No evalúa calidad semántica |
| QV-002 | Encabezado Markdown válido | Mantener estructura mínima de documentos | Shell | Check run | No sustituye revisión editorial |
| QV-003 | Sin trailing whitespace fuera de Markdown | Reducir ruido y variaciones innecesarias | Shell | Check run | Markdown puede usar espacios intencionales |
| QV-004 | YAML válido | Detectar errores sintácticos en configuración YAML | Ruby/Psych | Check run | Sintaxis válida no implica configuración correcta |
| QV-005 | Integridad de enlaces locales Markdown | Detectar referencias locales rotas | Python estándar | Check run | No valida enlaces externos ni semántica |
| QV-006 | Archivos críticos presentes | Evitar pérdida accidental de artefactos esenciales | Shell | Check run | El inventario evolucionará con el proyecto |

Los controles QV-001–QV-006 constituyen la línea base de calidad técnica del repositorio en su estado actual. No se establecen métricas de cobertura, complejidad o rendimiento porque todavía no existe código de aplicación suficiente para justificar umbrales.

## 5. Estados

- **PASS:** control ejecutado y satisfecho.
- **FAIL:** control ejecutado y no satisfecho; la validación de la unidad de cambio falla.
- **NOT_APPLICABLE:** el control no corresponde al cambio/contexto y la razón queda registrada.

El workflow debe preferir `FAIL` ante defectos objetivos y no utilizar `PASS` como sustituto de una evaluación no realizada.

## 6. Relación con ISO/IEC 25010:2023

La calidad del producto se evaluará progresivamente mediante las características y subcaracterísticas pertinentes del modelo de calidad adoptado. En esta etapa, los controles QV iniciales se consideran principalmente mecanismos de **mantenibilidad**, **fiabilidad del artefacto de ingeniería** y calidad del proceso/documentación; no se asignan equivalencias uno-a-uno cuando la evidencia disponible no las justifica.

La selección futura de métricas y pruebas deberá derivarse de requisitos de calidad verificables, contexto operativo y riesgos del Ecosistema.

## 7. Relación con Quality Gates

Quality Validation proporciona evidencia técnica para los gates, pero no decide por sí sola el resultado de todos ellos.

Ejemplo:

```text
QV PASS
  ↓
Evidencia técnica disponible
  ↓
Evaluación del Gate correspondiente
  ↓
PASS / PASS WITH CONDITIONS / REWORK / BLOCKED
```

Un `PASS` de Quality Validation no equivale a `PASS` de un Quality Gate.

## 8. Evolución prevista

A medida que aparezcan código, pruebas, infraestructura y requisitos verificables, podrán incorporarse, con justificación y análisis de impacto:

- pruebas unitarias;
- pruebas de integración;
- análisis estático;
- cobertura de pruebas cuando exista base estadística y riesgo que justifique el umbral;
- complejidad y mantenibilidad;
- validaciones de contratos e interfaces;
- pruebas de rendimiento;
- pruebas de resiliencia;
- controles de documentación técnica;
- validaciones específicas por tecnología.

Los controles de seguridad se mantendrán en una capa independiente para evitar mezclar objetivos y responsabilidades.

## 9. Limitaciones y riesgo residual

La validación automatizada puede producir falsos positivos y falsos negativos. Los checks iniciales son deliberadamente modestos porque el repositorio todavía se encuentra en una etapa documental y de definición del sistema.

El riesgo residual incluye defectos semánticos, errores de diseño, requisitos incorrectos y problemas no detectables mediante las comprobaciones automatizadas. Estos riesgos requieren revisión de ingeniería, pruebas apropiadas y validación del sistema conforme avance el ciclo de vida.

## 10. Evidencia requerida

Cada ejecución de Quality Validation debe permitir identificar:

- commit evaluado;
- Pull Request, cuando aplique;
- controles ejecutados;
- resultado por control;
- mensajes de fallo;
- contexto de ejecución;
- fecha/hora de ejecución;
- workflow run asociado.

## 11. Criterio de verdad

La afirmación permitida es:

> `Quality Validation PASS` significa que los controles automatizados aplicables definidos para la versión actual del repositorio fueron satisfechos.

No se utilizará como sinónimo de:

> "el software es de alta calidad".
