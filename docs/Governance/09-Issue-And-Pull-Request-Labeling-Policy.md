# Política de Labels y Títulos para Issues y Pull Requests

**Versión:** 0.3.0  
**Estado:** Vigente  
**Catálogo estructurado:** `docs/Governance/Label-Catalog.yml`  
**Relacionado:** Issue #130

## 1. Propósito

Establecer una clasificación y una convención de títulos consistente para Issues y Pull Requests, facilitando descubrimiento, priorización, filtrado, trazabilidad y lectura del historial de ingeniería.

Los labels son metadatos de gobernanza. **No sustituyen el título, alcance, criterios de aceptación ni documentación del cambio.**

## 2. Regla obligatoria de labels

Todo Issue y todo Pull Request debe tener al menos un label pertinente antes de considerarse correctamente clasificado.

La taxonomía oficial está definida en `docs/Governance/Label-Catalog.yml`. La documentación narrativa de esta política y el catálogo estructurado deben permanecer semánticamente alineados.

Cuando el trabajo atraviese varios dominios, pueden utilizarse varios labels, pero solo los que aporten información real. Un PR hereda normalmente la clasificación principal del Issue que implementa y puede añadir una clasificación secundaria justificada.

## 3. Catálogo oficial vigente

| Label | Uso | Regla de aplicación |
|---|---|---|
| `governance` | Gobierno, políticas, procesos, ciclo de vida, control de cambios, planificación y decisiones. | Obligatorio cuando el trabajo afecte gobernanza, `.github/`, `docs/Governance/` o `docs/Research/`. |
| `documentation` | Documentación, registros, evidencias documentales e índices. | Aplicable cuando el cambio tenga como propósito principal documentación o evidencia documental. |
| `architecture` | Arquitectura de sistema/software, diseño estructural y decisiones arquitectónicas. | Aplicable cuando el cambio afecte arquitectura o decisiones estructurales. |

Los labels estándar adicionales de GitHub no pasan automáticamente a formar parte de la taxonomía oficial del proyecto. Su incorporación requiere una modificación controlada del catálogo y de esta política.

## 4. Reglas de clasificación

1. El **Issue** establece la clasificación primaria del trabajo.
2. El **Pull Request** debe conservar la clasificación primaria del Issue.
3. Un label secundario solo se utiliza cuando el cambio afecta realmente a otro dominio catalogado.
4. No se utilizarán labels para compensar un título ambiguo o una relación de trazabilidad incompleta.
5. No se utilizarán labels fuera del catálogo oficial como clasificación de proyecto.
6. Una clasificación ambigua no debe resolverse mediante una etiqueta arbitraria: debe quedar explícitamente clasificada antes de la integración.
7. La automatización solo podrá crear labels presentes en el catálogo oficial.
8. La automatización no podrá crear, renombrar ni introducir nuevos labels como consecuencia de una inferencia.

## 5. Convención obligatoria de títulos

Toda nueva Issue y todo nuevo Pull Request utilizará exactamente esta estructura conceptual:

> **`Módulo/Archivo: Acción a realizar.`**

### Componentes

| Componente | Regla |
|---|---|
| **Módulo** | Dominio o área del Ecosistema: `Gobernanza`, `Descubrimiento`, `Requisitos`, `Arquitectura`, `Testing`, etc. |
| **Archivo** | Artefacto principal afectado cuando exista. Puede omitirse cuando el trabajo no esté ligado a un archivo concreto. |
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

Estos tres mecanismos tienen funciones distintas:

```text
Título  → ¿Qué acción concreta se realizará?
Label   → ¿De qué naturaleza/dominio es el trabajo?
Fase    → ¿Dónde encaja en el ciclo de vida A–O?
```

**Título ≠ label ≠ fase.** No se utilizará un label para compensar un título ambiguo ni un título para sustituir la trazabilidad de fase.

## 7. Reglas para Issues

Antes de iniciar una unidad de trabajo:

- título conforme a la convención;
- objetivo, contexto, alcance y criterios de aceptación;
- fase/subfase del ciclo de vida cuando corresponda;
- análisis de impacto inicial cuando sea relevante;
- labels pertinentes del catálogo oficial;
- dependencias y evidencia esperada cuando existan.

## 8. Reglas para Pull Requests

Todo PR deberá:

- utilizar la convención de títulos;
- estar vinculado a un Issue;
- conservar el label primario del Issue;
- utilizar únicamente labels oficiales;
- justificar cualquier label secundario;
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
Labels candidatos pertenecientes al catálogo
      ↓
Reglas de precedencia y no solapamiento
      ↓
Clasificación determinista
      ↓
Validación CI
```

Si no existe una clasificación inequívoca dentro del catálogo, el sistema debe detener la integración y exigir clasificación explícita. No debe inventar una nueva categoría.

La automatización de contingencia que añade `governance` cuando un PR nace sin labels tiene como único propósito impedir la ausencia de clasificación mínima. No sustituye la clasificación semántica completa que deberá implementarse conforme a este catálogo.

## 10. Evolución de la taxonomía

Los dominios futuros `requirements`, `testing`, `security`, `data`, `devops` y `operations` permanecen planificados y **no son labels oficiales todavía**.

Su incorporación requerirá:

- necesidad real y estable;
- definición semántica inequívoca;
- ausencia de solapamiento;
- utilidad para métricas y Roadmap;
- reglas de aplicación;
- actualización del catálogo estructurado;
- actualización de esta política;
- cambio mediante Issue → Branch → Commit → PR → Validaciones → Review → Merge.

## 11. Regularización histórica

Los Issues y PRs históricos no se reescribirán artificialmente. Cuando sea útil, podrán regularizarse sus labels o metadatos sin alterar el contenido sustantivo ni romper la trazabilidad histórica.

La nueva convención de títulos se aplica obligatoriamente desde Issue #11 en adelante.

## 12. Relación con el Roadmap

```text
Título
  ↓
Label / dominio
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
