# Política de Labels y Títulos para Issues y Pull Requests

**Versión:** 0.2.0  
**Estado:** Vigente  
**Relacionado:** Issue #11

## 1. Propósito

Establecer una clasificación y una convención de títulos consistente para Issues y Pull Requests, facilitando descubrimiento, priorización, filtrado, trazabilidad y lectura del historial de ingeniería.

Los labels son metadatos de gobernanza. **No sustituyen el título, alcance, criterios de aceptación ni documentación del cambio.**

## 2. Regla obligatoria de labels

Todo Issue y todo Pull Request debe tener al menos un label pertinente antes de considerarse correctamente clasificado.

Cuando el trabajo atraviese varios dominios, pueden utilizarse varios labels, pero solo los que aporten información real. Un PR hereda normalmente la clasificación principal del Issue que implementa y puede añadir una clasificación secundaria justificada.

## 3. Labels actualmente disponibles

| Label | Uso |
|---|---|
| `governance` | Gobierno, políticas, procesos, ciclo de vida, control de cambios, planificación y decisiones. |
| `documentation` | Documentación, registros, evidencias documentales e índices. |
| `architecture` | Arquitectura de sistema/software, diseño estructural y decisiones arquitectónicas. |

Los labels estándar adicionales de GitHub no pasan automáticamente a formar parte de la taxonomía oficial del proyecto. Su incorporación requiere justificación y documentación.

## 4. Convención obligatoria de títulos

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

## 5. Diferencia entre título, label y fase

Estos tres mecanismos tienen funciones distintas:

```text
Título  → ¿Qué acción concreta se realizará?
Label   → ¿De qué naturaleza/dominio es el trabajo?
Fase    → ¿Dónde encaja en el ciclo de vida A–O?
```

**Título ≠ label ≠ fase.** No se utilizará un label para compensar un título ambiguo ni un título para sustituir la trazabilidad de fase.

## 6. Reglas para Issues

Antes de iniciar una unidad de trabajo:

- título conforme a la convención;
- objetivo, contexto, alcance y criterios de aceptación;
- fase/subfase del ciclo de vida cuando corresponda;
- análisis de impacto inicial cuando sea relevante;
- labels pertinentes;
- dependencias y evidencia esperada cuando existan.

## 7. Reglas para Pull Requests

Todo PR deberá:

- utilizar la convención de títulos;
- estar vinculado a un Issue;
- conservar los labels pertinentes;
- documentar cambio y motivo;
- declarar análisis de impacto;
- identificar artefactos afectados;
- registrar pruebas/evidencia;
- declarar explícitamente uno y solo uno de los estados formales de integración del proyecto.

## 8. Regularización histórica

Los Issues y PRs históricos no se reescribirán artificialmente. Cuando sea útil, podrán regularizarse sus labels o metadatos sin alterar el contenido sustantivo ni romper la trazabilidad histórica.

La nueva convención de títulos se aplica obligatoriamente desde Issue #11 en adelante.

## 9. Evolución de la taxonomía

Cuando aparezcan dominios permanentes como requisitos, testing, seguridad, datos, DevOps u operaciones, se evaluará la incorporación de labels específicos antes de utilizarlos como clasificación oficial.

La incorporación deberá considerar necesidad real, ausencia de solapamiento, estabilidad semántica, utilidad para métricas/Roadmap y documentación del significado.

## 10. Relación con el Roadmap

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
