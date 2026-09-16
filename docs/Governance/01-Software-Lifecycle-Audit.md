# Auditoría y consolidación del ciclo de vida maestro de Ingeniería de Software

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.3.0  
**Estado actual:** Auditoría consolidada e integrada — Issue #1 cerrado  
**Issue de origen:** #1  
**PR de integración:** #94  
**Fecha de auditoría original:** 2026-09-15  
**Baseline evaluada originalmente:** `main` @ `c2a0e5c3fc91bd959c30623a9783f1888da5d212`  
**Estado histórico de la auditoría v0.2.0:** consolidación propuesta, pendiente de integración controlada  
**Estado posterior a PR #94:** integrada, validada y cerrada

---

## 0. Distinción entre estado histórico y estado actual

Este documento conserva deliberadamente la evidencia de la auditoría realizada el 2026-09-15. La situación descrita en la versión v0.2.0 pertenece a ese momento del ciclo y no debe interpretarse como el estado operativo actual del repositorio.

### 0.1 Estado histórico — auditoría v0.2.0

La auditoría original evaluó `main` en el commit `c2a0e5c3fc91bd959c30623a9783f1888da5d212`. En ese momento, la consolidación de la auditoría estaba pendiente de integración controlada y el cierre del Issue #1 dependía de completar el flujo de Pull Request, ejecutar las validaciones y verificar el resultado final.

Estas condiciones históricas se conservan porque forman parte de la evidencia de ingeniería: permiten demostrar qué se evaluó, qué se propuso y qué faltaba completar en ese punto temporal.

### 0.2 Estado actual — posterior a PR #94

La integración posterior se realizó mediante **PR #94**. El HEAD validado antes de la fusión fue `8bb1517589e4f584e094713da0ea2a663a37be96` y la fusión produjo el commit `e6fab75018ecf14a23c304cf0eba887b24d86781`.

Sobre el HEAD final de PR #94 se obtuvieron:

- Governance Validation — PASS
- Quality Validation — PASS
- Security Validation — PASS
- Evidence Validation — PASS

Posteriormente, el **Issue #1 fue cerrado explícitamente como completado**.

Por tanto, expresiones como **“pendiente de integración controlada”**, **“el cierre del Issue queda condicionado”** o equivalentes son evidencia del estado previo a PR #94 y no representan el estado actual.

> **Regla de interpretación temporal:** la evidencia histórica no se reescribe para aparentar el estado posterior; se conserva y se contextualiza. El estado actual se declara por separado y se respalda mediante la trazabilidad posterior.

---

## 1. Objetivo

Auditar y consolidar el ciclo de vida maestro de Ingeniería de Software y del Ecosistema antes de declararlo baseline oficial. Esta revisión no parte de cero: evalúa los artefactos ya presentes en el repositorio, identifica brechas e inconsistencias y establece la trazabilidad entre los hallazgos del Issue #1 y el ciclo consolidado actualmente documentado.

El resultado debe permitir demostrar, criterio por criterio, que el ciclo distingue adecuadamente el nivel sistema/ecosistema del nivel software, separa fases de procesos transversales, relaciona actividades con artefactos y evidencia y utiliza GitHub como mecanismo de control del cambio.

**Nota temporal:** el objetivo y los criterios anteriores pertenecen a la formulación histórica de la auditoría. El cumplimiento posterior se documenta en las secciones de resultados y trazabilidad.

---

## 2. Evidencia documental evaluada

| ID | Artefacto | Ruta en baseline histórica | Estado histórico observado | Función en la consolidación |
|---|---|---|---|---|
| E-01 | Software Lifecycle Master | `Docs/Governance/00-Software-Lifecycle-Master.md` | v0.3.0, candidato a baseline | Artefacto rector del ciclo A–O |
| E-02 | Software Lifecycle Audit | `Docs/Governance/01-Software-Lifecycle-Audit.md` | v0.1.0 antes de esta revisión | Auditoría y propuesta inicial |
| E-03 | Standards Lifecycle Matrix | `Docs/Governance/02-Standards-Lifecycle-Matrix.md` | v0.4.0 | Alineación metodológica |
| E-04 | Artifacts and Evidence | `Docs/Governance/03-Artifacts-And-Evidence.md` | v1.0.0 | Catálogo de artefactos y evidencia |
| E-05 | Quality Gates | `Docs/Governance/04-Quality-Gates.md` | Controlado | Gates del ciclo |
| E-06 | Change Control Workflow | `Docs/Governance/06-Change-Control-Workflow.md` | Controlado | Flujo Issue → Branch → PR → Merge |
| E-07 | Governance Enforcement Architecture | `Docs/Governance/10-Governance-Enforcement-Architecture.md` | Controlado | Enforcement y validaciones |
| E-08 | Validation workflows | `.github/workflows/*-validation.yml` | Operativo | Governance, Quality, Security y Evidence Validation |

La tabla anterior conserva las **rutas observadas en la baseline histórica**. Después de la normalización `Docs/` → `docs/`, las rutas activas del repositorio son `docs/Governance/...`.

La existencia de estos artefactos no se interpreta como evidencia automática de que todos los controles estén satisfechos; la auditoría evalúa su coherencia y trazabilidad.

---

## 3. Referentes metodológicos y normativos

La evaluación utiliza las siguientes referencias como marcos de alineación, no como declaración de conformidad o certificación:

- **ISO/IEC/IEEE 15288:2023** — procesos de ciclo de vida de sistemas.
- **ISO/IEC/IEEE 12207:2026** — procesos de ciclo de vida de software.
- **ISO/IEC/IEEE 29148:2018** — ingeniería de requisitos.
- **ISO/IEC/IEEE 42010:2022** — descripción de arquitectura.
- **ISO/IEC 25010:2023** — modelo de calidad de producto.
- **NIST SP 800-218 / SSDF 1.1** — prácticas de desarrollo seguro.

La selección es coherente con el alcance del Ecosistema: 15288 aporta la perspectiva de sistema, 12207 la de software, 29148 requisitos, 42010 arquitectura, 25010 calidad y SSDF seguridad integrada.

### 3.1 Verificación de vigencia realizada durante la auditoría original

A fecha de esta auditoría, ISO registraba **ISO/IEC/IEEE 12207:2026** como edición publicada en abril de 2026 y como reemplazo de 12207:2017. ISO describe su aplicación a adquisición, suministro, desarrollo, operación, mantenimiento y disposición, incluyendo aplicación concurrente, iterativa, recursiva e incremental.  
Fuente oficial: https://www.iso.org/standard/90219.html

ISO registraba **ISO/IEC/IEEE 15288:2023** como edición publicada vigente para procesos de ciclo de vida de sistemas, incluyendo concepción, desarrollo, producción, utilización, soporte, retirada, adquisición y suministro, con aplicación iterativa, concurrente y recursiva.  
Fuente oficial: https://www.iso.org/standard/81702.html

ISO indicaba que **ISO/IEC/IEEE 29148:2018** fue revisada y confirmada en 2024, por lo que permanecía vigente durante la auditoría.  
Fuente oficial: https://www.iso.org/standard/72089.html

ISO registraba **ISO/IEC/IEEE 42010:2022** como edición vigente para requisitos de estructura y expresión de descripciones de arquitectura; no prescribe un método concreto de arquitectura.  
Fuente oficial: https://www.iso.org/standard/74393.html

ISO registraba **ISO/IEC 25010:2023** como modelo de calidad de producto.  
Fuente oficial: https://www.iso.org/standard/78176.html

NIST mantenía **SP 800-218 / SSDF 1.1** como marco de prácticas de desarrollo seguro que puede integrarse en modelos SDLC existentes.  
Fuente oficial: https://csrc.nist.gov/pubs/sp/800/218/final

Estas verificaciones pertenecen al momento de la auditoría original y no constituyen una garantía de vigencia normativa indefinida. Las futuras revisiones normativas deben verificarse mediante el flujo de cambio correspondiente.

---

## 4. Hallazgo principal: doble nivel de ingeniería

El objeto de ingeniería del proyecto no es únicamente software. El Ecosistema es un sistema sociotécnico que puede involucrar organización, personas, procesos, información, datos, software, infraestructura, integraciones, servicios externos y gobernanza.

Se confirma por tanto el modelo:

```text
Nivel 1 — SISTEMA / ECOSISTEMA
Organización · Personas · Procesos · Información · Datos
Software · Infraestructura · Integraciones · Servicios externos
Gobernanza

                    ↓

Nivel 2 — SOFTWARE
Aplicaciones · Servicios · Componentes · APIs · Código
Bases de datos · Configuración · Pipelines · Pruebas
```

**Decisión consolidada:** 15288:2023 es referencia sistémica y 12207:2026 referencia principal de software. El ciclo propio no copia la estructura normativa; adapta los procesos al contexto del Ecosistema.

---

## 5. Auditoría de los criterios de aceptación del Issue #1

### 5.1 Criterios definidos originalmente

| Criterio | Evidencia | Resultado histórico | Determinación |
|---|---|---|---|
| Identificar procesos/fases/subfases faltantes | E-01, E-02, E-03 | PASS | El ciclo consolidado contiene A–O y subfases; adquisición/suministro y disciplinas transversales quedan explícitos. |
| Identificar duplicidades o responsabilidades mal ubicadas | E-02, E-03 | PASS | Seguridad, calidad, riesgos, configuración, cambios, trazabilidad, observabilidad y DevSecOps se clasifican como transversales/habilitadores, no como fases adicionales. |
| Separar fases y procesos transversales | E-01, E-02 | PASS | Las fases A–O se distinguen de los procesos/controles transversales. |
| Incorporar explícitamente sistema/ecosistema además de software | E-01, E-02 | PASS | El alcance declara ambos niveles y el modelo de doble nivel. |
| Definir relación ciclo–artefactos–evidencia–GitHub | E-01, E-04, E-06, E-07 | PASS | Existe cadena de trazabilidad y control de cambios Issue → Branch → PR → validaciones → revisión → merge → main. |
| Proponer estructura revisada para v0.2 | E-02 | PASS | La auditoría inicial propuso las 15 fases A–O; el artefacto rector evolucionó posteriormente a v0.3.0. |
| Mantener trazabilidad entre hallazgos y modificaciones posteriores | E-01, E-02, esta versión 0.2.0 | PASS CONDICIONADO | La revisión consolidó la relación; la integración controlada, validación y cierre del Issue eran condiciones pendientes en el momento histórico. |

### 5.2 Resultado posterior a PR #94

Los siete criterios quedaron satisfechos mediante la evolución y posterior integración controlada documentada por PR #94.

**Resultado actual: 7/7 criterios con evidencia identificada y cierre completado.**

El séptimo criterio dejó de ser condicional cuando se completaron el PR, las cuatro validaciones, la fusión y el cierre explícito del Issue #1.

---

## 6. Reorganización consolidada

La estructura consolidada del ciclo maestro es de **15 fases principales**, A–O:

A. Concepción y gobernanza  
B. Descubrimiento del sistema y organización  
C. Necesidades, problema y objetivos  
D. Ingeniería de requisitos  
E. Definición y modelado del sistema  
F. Arquitectura  
G. Diseño  
H. Implementación y construcción  
I. Integración y verificación  
J. Validación y aceptación  
K. Transición y despliegue  
L. Operación y soporte  
M. Mantenimiento y evolución  
N. Mejora y optimización  
O. Retirada y migración

La estructura no representa una secuencia rígida. Las actividades pueden ejecutarse iterativamente, incrementalmente, concurrentemente o recursivamente según contexto, riesgo y naturaleza del trabajo.

---

## 7. Procesos y disciplinas transversales

Se confirma que las siguientes capacidades atraviesan las fases y no deben convertirse en fases independientes salvo que una decisión futura justificada lo requiera:

1. Gobernanza y decisiones.
2. Stakeholders.
3. Requisitos y trazabilidad.
4. Arquitectura y decisiones arquitectónicas.
5. Riesgos y oportunidades.
6. Calidad.
7. Seguridad y privacidad cuando corresponda.
8. Configuración y baselines.
9. Cambios.
10. Información y documentación.
11. Datos.
12. Medición.
13. Dependencias, adquisición y suministro.
14. Conocimiento y mejora del proceso.
15. Automatización, CI/CD y DevSecOps.
16. Observabilidad y operación.
17. Defectos y no conformidades.
18. Evidencia y reproducibilidad.
19. Investigación científica cuando corresponda.

La clasificación es consistente con la naturaleza de 12207:2026, 15288:2023 y SSDF 1.1: seguridad y otras capacidades pueden integrarse en el SDLC y no requieren convertirse en una fase temporal aislada.

---

## 8. Relación ciclo de vida → artefactos → evidencia → GitHub

La cadena canónica queda definida como:

```text
Problema / Necesidad
        ↓
Objetivo
        ↓
Requisito
        ↓
Decisión / Arquitectura / Diseño
        ↓
Issue
        ↓
Branch
        ↓
Commit
        ↓
Pull Request
        ↓
Governance Validation
Quality Validation
Security Validation
Evidence Validation
        ↓
Revisión / SoD
        ↓
Merge
        ↓
main
        ↓
Release / Operación
        ↓
Evidencia operacional / Resultado / Aprendizaje
```

No todos los cambios necesitan todos los artefactos. La ausencia de un elemento que no aplique debe ser justificable. La regla de control del repositorio permanece: **ningún trabajo pasa directamente a `main`**.

---

## 9. Quality Gates y criterios de transición

Los gates se mantienen como puntos de decisión basados en evidencia, no como una conversión del ciclo a cascada.

| Gate | Resultado esperado |
|---|---|
| G0 | Gobernanza y contexto listos |
| G1 | Descubrimiento suficientemente confiable |
| G2 | Problema, objetivos y alcance definidos |
| G3 | Requisitos baselined y trazables |
| G4 | Definición del sistema preparada |
| G5 | Arquitectura baselined |
| G6 | Diseño preparado |
| G7 | Construcción preparada/controlada |
| G8 | Verificación preparada y ejecutable |
| G9 | Validación y aceptación satisfechas |
| G10 | Preparación de producción satisfecha |
| G11 | Operación estable |
| G12 | Evolución/mejora preparada |
| G13 | Retirada/migración completada |

Un gate puede producir PASS, PASS WITH CONDITIONS, REWORK o BLOCKED, siempre con evidencia y decisión trazable.

---

## 10. Hallazgos residuales

La auditoría no identifica una brecha conceptual que obligue a rediseñar las 15 fases A–O. Sí identifica controles de mantenimiento documental que deben permanecer activos:

- sincronizar versiones de documentos rectores;
- mantener la matriz de estándares actualizada cuando cambie una edición normativa;
- evitar declarar conformidad normativa sin revisión del texto oficial completo;
- conservar trazabilidad de cambios del ciclo mediante Issue/PR;
- actualizar artefactos relacionados cuando cambie el ciclo maestro;
- distinguir evidencia de ingeniería de evidencia científica;
- mantener seguridad, calidad, riesgo, configuración y evidencia como capacidades transversales.

Estos puntos son **controles de mantenimiento**, no bloqueadores conceptuales del modelo A–O.

---

## 11. Decisión de consolidación

La auditoría inicial produjo una propuesta de ciclo de 15 fases. El repositorio posteriormente evolucionó el artefacto rector a `docs/Governance/00-Software-Lifecycle-Master.md` **v0.3.0**, por lo que la referencia a una futura v0.2.0 en la auditoría histórica queda interpretada como una etapa intermedia de evolución, no como una versión que deba crearse retroactivamente.

La auditoría v0.2.0 fue integrada mediante **PR #94** y dejó de ser un cambio pendiente. La presente v0.3.0 no altera retroactivamente la evidencia histórica; añade el contexto necesario para distinguir la situación observada durante la auditoría de la situación posterior a la integración.

**Estado actual de la consolidación:** integrada y cerrada.

No se utiliza esta auditoría para declarar certificación o conformidad normativa. Su función es conservar la evidencia de evaluación, las decisiones de ingeniería y la trazabilidad de la consolidación.

---

## 12. Trazabilidad de resolución del Issue #1

```text
Issue #1
  ↓
01-Software-Lifecycle-Audit.md v0.1.0
  ↓
Propuesta de 15 fases + disciplinas transversales
  ↓
00-Software-Lifecycle-Master.md v0.3.0
  ↓
02-Standards-Lifecycle-Matrix.md v0.4.0
  ↓
03-Artifacts-And-Evidence.md v1.0.0
  ↓
01-Software-Lifecycle-Audit.md v0.2.0
  ↓
PR #94
  ↓
HEAD validado: 8bb1517589e4f584e094713da0ea2a663a37be96
  ↓
Governance Validation — PASS
Quality Validation — PASS
Security Validation — PASS
Evidence Validation — PASS
  ↓
Revisión / SoD
  ↓
Merge commit e6fab75018ecf14a23c304cf0eba887b24d86781
  ↓
Verificación final
  ↓
Cierre del Issue #1
```

### 12.1 Interpretación temporal de la trazabilidad

La secuencia anterior debe leerse como una cadena histórica de ingeniería. Los elementos anteriores a PR #94 representan el estado y las decisiones durante la resolución del Issue. Los elementos posteriores representan la evidencia de integración y cierre.

La existencia de una frase histórica como “pendiente de integración controlada” no contradice el cierre posterior del Issue: pertenece a un punto temporal anterior de la misma cadena de trazabilidad.

La referencia a `Docs/Governance/...` en artefactos históricos no contradice la estructura actual `docs/Governance/...`: representa la ruta observada antes de la normalización del directorio.

---

## 13. Criterio de cierre — estado histórico y resultado final

### 13.1 Criterio definido originalmente

En la versión v0.2.0, el Issue #1 podía cerrarse únicamente cuando el Pull Request asociado demostrara:

- esta auditoría consolidada integrada;
- coherencia entre el ciclo maestro, la matriz de estándares y el catálogo de artefactos/evidencias;
- los cuatro workflows de validación en PASS sobre el HEAD final;
- revisión/SoD conforme al nivel de riesgo o excepción formal cuando corresponda;
- trazabilidad explícita Issue → Branch → Commits → PR → Validaciones → Revisión → Merge;
- ausencia de afirmaciones de conformidad normativa no sustentadas;
- verificación post-merge de los artefactos resultantes.

Este texto representa el **criterio histórico de cierre**, no una condición actualmente pendiente.

### 13.2 Resultado posterior a PR #94

El criterio histórico fue satisfecho mediante el flujo controlado de integración. El cambio fue validado sobre el HEAD final, fusionado mediante PR #94 y el Issue #1 fue cerrado explícitamente como completado.

**Resultado actual: CERRADO / COMPLETADO.**

---

## 14. Regla de mantenimiento futuro

Cualquier modificación futura del ciclo maestro, de esta auditoría o de sus artefactos relacionados debe conservar la separación entre:

1. **evidencia histórica**, que no debe falsificarse ni reescribirse para aparentar un estado que no existía;
2. **estado actual**, que debe reflejar el repositorio y los controles vigentes;
3. **cambio propuesto**, que debe pasar por Issue → Branch → Commits → Pull Request → Validaciones → Revisión/SoD → Merge.

Cuando un estado histórico deje de ser actual, debe contextualizarse mediante una sección temporal, versión o registro de cambio; no debe eliminarse silenciosamente.

La documentación debe utilizar las rutas vigentes del repositorio, actualmente bajo `docs/`, salvo cuando una referencia histórica deba conservar explícitamente la ruta anterior como evidencia de contexto.

---

## 15. Conclusión

La auditoría conserva su valor como evidencia de la consolidación del ciclo de vida, pero su interpretación queda ahora temporalmente delimitada.

**Estado histórico:** auditoría v0.2.0 pendiente de integración controlada.  
**Evento de transición:** PR #94.  
**Resultado de integración:** cuatro validaciones PASS y merge controlado.  
**Estado posterior:** Issue #1 cerrado/completado.  
**Estado documental actual:** auditoría consolidada e integrada, con distinción explícita entre evidencia histórica y estado actual.

La estructura A–O, la separación entre sistema/ecosistema y software, las disciplinas transversales, los Quality Gates y la cadena Issue → Branch → Commit → PR → Validación → Revisión/SoD → Merge permanecen como decisiones documentadas del ciclo consolidado.
