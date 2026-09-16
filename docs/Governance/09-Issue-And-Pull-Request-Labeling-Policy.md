# Política de Labels y Títulos para Issues y Pull Requests

**Versión:** 0.4.0  
**Estado:** Vigente  
**Catálogo estructurado:** `docs/Governance/Label-Catalog.yml`  
**Relacionado:** Issue #130

## 1. Propósito

Establecer una clasificación controlada para Issues y Pull Requests, facilitando descubrimiento, priorización, filtrado, trazabilidad y lectura del historial de ingeniería.

Los labels son metadatos de gobernanza. **No sustituyen el título, alcance, criterios de aceptación ni documentación del cambio.**

La taxonomía oficial se define en `docs/Governance/Label-Catalog.yml`. Esta política explica cómo debe aplicarse; el catálogo es la fuente estructurada de verdad.

## 2. Modelo de clasificación

La clasificación utiliza **dos dimensiones independientes**:

```text
Dominio       → ¿En qué área de ingeniería impacta el trabajo?
Tipo de trabajo → ¿Qué clase de trabajo se está realizando?
```

Todo Issue nuevo debe tener:

1. exactamente **un dominio primario**;
2. exactamente **un tipo de trabajo**.

Por tanto, la clasificación semántica mínima de un Issue/PR son dos labels.

Los dominios secundarios solo se permiten cuando el cambio afecta realmente a más de un dominio. No se permiten tipos de trabajo secundarios.

## 3. Catálogo oficial

### 3.1 Dominios

| Label | Significado |
|---|---|
| `governance` | Gobierno, políticas, procesos de gobernanza, ciclo de vida y control de cambios. |
| `research` | Investigación, revisión de literatura, experimentación científica y evidencia de investigación. |
| `documentation` | Documentación técnica, registros, índices y evidencias documentales. |
| `requirements` | Descubrimiento, especificación, análisis, trazabilidad y validación de requisitos. |
| `architecture` | Arquitectura de sistema/software, diseño estructural y decisiones arquitectónicas. |
| `implementation` | Construcción o modificación del producto, componentes y código ejecutable. |
| `testing` | Verificación, validación, pruebas y estrategia de calidad técnica. |
| `security` | Seguridad, controles, amenazas, vulnerabilidades y protección de activos. |
| `data` | Datos, modelos de datos, esquemas, calidad, gobierno y flujos de información. |
| `devops` | Integración, entrega, automatización de infraestructura y toolchain de ingeniería. |
| `operations` | Operación, observabilidad, despliegue, soporte y continuidad del sistema. |

### 3.2 Tipos de trabajo

| Label | Significado |
|---|---|
| `feature` | Incorporación de capacidad o comportamiento nuevo. |
| `bug` | Corrección de comportamiento incorrecto o fallo existente. |
| `refactor` | Cambio estructural sin alterar el comportamiento funcional esperado. |
| `configuration` | Ajuste de configuración, políticas declarativas o parámetros operativos. |
| `automation` | Automatización de un proceso manual o repetitivo. |
| `decision` | Formalización de una decisión técnica, arquitectónica o de proceso. |
| `baseline` | Creación, actualización o control de una baseline formal. |
| `process` | Definición, mejora o corrección de un proceso de ingeniería. |
| `investigation` | Investigación acotada para reducir incertidumbre antes de decidir o ejecutar. |
| `maintenance` | Mantenimiento preventivo o correctivo sin nueva capacidad ni cambio estructural relevante. |

Los labels estándar adicionales de GitHub no pasan automáticamente a formar parte de la taxonomía oficial del proyecto.

## 4. Reglas obligatorias de clasificación

1. Todo Issue nuevo debe tener un dominio primario y un tipo de trabajo.
2. Todo Pull Request debe conservar el dominio y tipo de trabajo del Issue que implementa.
3. Un dominio secundario solo se utiliza cuando existe afectación real de otro dominio catalogado.
4. No se permiten tipos de trabajo secundarios.
5. No se utilizarán labels para compensar un título ambiguo o una relación de trazabilidad incompleta.
6. No se utilizarán labels fuera del catálogo oficial como clasificación del proyecto.
7. La fase del ciclo de vida no se representa mediante labels.
8. El estado operativo (`open`, `closed`, `merged`) no se representa mediante labels.
9. La prioridad no se representa mediante labels salvo que el proyecto formalice posteriormente una taxonomía específica para ello.
10. Una clasificación ambigua debe resolverse explícitamente antes de la integración.
11. Si cambia materialmente la clasificación del trabajo, primero se actualiza el Issue y después el PR.
12. La automatización solo puede utilizar labels presentes en el catálogo.
13. La automatización no puede ampliar la taxonomía por inferencia.

## 5. Convención obligatoria de títulos

Toda nueva Issue y todo nuevo Pull Request utilizará exactamente esta estructura conceptual:

> **`Módulo/Archivo: Acción a realizar.`**

### Componentes

| Componente | Regla |
|---|---|
| **Módulo** | Dominio o área del Ecosistema. |
| **Archivo** | Artefacto principal afectado cuando exista. Puede omitirse cuando no exista un archivo concreto. |
| **Acción** | Verbo claro que describa qué se realizará. |
| **Puntuación** | El título termina en punto. |

### Ejemplos válidos

- `Gobernanza/08-Software-Roadmap.md: Actualizar seguimiento y fechas.`
- `Descubrimiento/Stakeholders: Identificar y registrar actores.`
- `Requisitos/Requirements-Baseline.md: Definir requisitos verificables.`
- `Arquitectura/Architecture-Baseline.md: Establecer arquitectura objetivo.`
- `Testing/Verification-Plan.md: Definir estrategia de verificación.`

### Ejemplos no válidos

- `Update docs`
- `Fix roadmap`
- `Cambios varios`
- `Implementación`
- `Roadmap`

El número de Issue/PR es identificador de GitHub y no sustituye el título descriptivo.

## 6. Diferencia entre título, label y fase

Estos mecanismos tienen funciones distintas:

```text
Título        → ¿Qué acción concreta se realizará?
Dominio label → ¿En qué área de ingeniería impacta?
Tipo label    → ¿Qué clase de trabajo es?
Fase          → ¿Dónde encaja en el ciclo de vida A–O?
```

**Título ≠ label ≠ fase.** No se utilizará un label para compensar un título ambiguo ni un título para sustituir la trazabilidad de fase.

## 7. Reglas para Issues

Antes de iniciar una unidad de trabajo:

- título conforme a la convención;
- objetivo, contexto, alcance y criterios de aceptación;
- fase/subfase del ciclo de vida cuando corresponda;
- análisis de impacto inicial cuando sea relevante;
- un dominio primario del catálogo;
- un tipo de trabajo del catálogo;
- dominios secundarios únicamente cuando estén justificados;
- dependencias y evidencia esperada cuando existan.

El Issue es la **fuente de clasificación primaria** del trabajo.

## 8. Reglas para Pull Requests

Todo PR deberá:

- utilizar la convención de títulos;
- estar vinculado a un Issue;
- conservar el dominio primario del Issue;
- conservar el tipo de trabajo del Issue;
- utilizar únicamente labels oficiales;
- justificar cualquier dominio secundario;
- no introducir tipos de trabajo secundarios;
- documentar cambio y motivo;
- declarar análisis de impacto;
- identificar artefactos afectados;
- registrar pruebas/evidencia;
- declarar explícitamente uno y solo uno de los estados formales de integración del proyecto.

## 9. Automatización y control

La clasificación automática completa se implementará sobre este catálogo formalizado.

Su contrato será:

```text
Issue clasificado
      ↓
Cambios del PR analizados
      ↓
Labels candidatos del catálogo
      ↓
Reglas de precedencia y no solapamiento
      ↓
Dominio primario + tipo de trabajo
      ↓
Validación CI
```

La automatización debe ser **determinista**: ante las mismas entradas y reglas debe producir la misma clasificación.

Si no existe una clasificación inequívoca dentro del catálogo, el sistema debe detener la integración y exigir clasificación explícita. No debe inventar una nueva categoría.

La contingencia que añade `governance` cuando un PR nace sin labels tiene un propósito limitado: impedir que exista un PR completamente sin clasificación. **No constituye la clasificación semántica completa.**

## 10. Creación y evolución de labels

Un label nuevo no puede aparecer espontáneamente porque una automatización lo considere conveniente.

La creación de una nueva categoría requiere:

1. necesidad real y estable;
2. definición semántica inequívoca;
3. ausencia de solapamiento con categorías existentes;
4. utilidad para trazabilidad, métricas o Roadmap;
5. reglas de aplicación y exclusión;
6. actualización de `Label-Catalog.yml`;
7. actualización de esta política;
8. creación/configuración controlada del label en GitHub;
9. validación mediante Issue → Branch → Commit → PR → Validaciones → Review → Merge.

La automatización podrá crear o aplicar únicamente labels ya autorizados por el catálogo.

## 11. Regularización histórica

Los Issues y PRs históricos no se reescribirán artificialmente. Cuando sea útil, podrán regularizarse sus labels o metadatos sin alterar el contenido sustantivo ni romper la trazabilidad histórica.

La aplicación completa de la taxonomía multidimensional será progresiva; no se debe bloquear el historial existente por exigir retroactivamente una clasificación que no existía cuando fue creado.

## 12. Relación con el Roadmap

```text
Título
  ↓
Dominio + Tipo de trabajo
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

El Roadmap determina el avance temporal y de ejecución; los Issues y PRs son las unidades trazables de trabajo e integración.
