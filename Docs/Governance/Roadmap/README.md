# 🗺️ Roadmap Dashboard

El Dashboard del Roadmap es la vista visual de presentación y navegación del Roadmap Maestro de Ingeniería del Ecosistema.

## 🎯 Propósito

Permitir que cualquier miembro del proyecto pueda entender rápidamente dónde comenzó el recorrido, qué fases y Gates fueron completados, cuál es la posición actual, qué queda por ejecutar y qué evidencia respalda cada hito.

## 🧭 Fuente de verdad

La fuente canónica continúa siendo:

`Docs/Governance/08-Software-Roadmap.md`

El Dashboard **no sustituye** al Roadmap documental ni a los artefactos de evidencia. Los datos operativos representados son una vista derivada y deben reconciliarse con la fuente canónica.

## 🖥️ Dashboard

Abrir `Roadmap-Dashboard.html` en un navegador moderno.

La versión actual incorpora filtros por estado, detalles desplegables por fase, recorrido A–O, progreso, trazabilidad y diseño responsive, sin dependencias externas obligatorias.

## 🧩 Diseño

El dashboard se organiza en cinco zonas:

1. **🚀 Estado general** — progreso y posición.
2. **🧭 Recorrido A–O** — ciclo completo.
3. **🎛️ Filtros y detalles** — navegación de la información.
4. **🔬 Trazabilidad** — conexión entre planificación y evidencia.
5. **📜 Historia** — hitos ya ejecutados.

## 🔐 Regla de consistencia

Cuando cambien estados, fechas, Gates, Issues, PRs o evidencias, el Roadmap canónico y esta vista deberán revisarse mediante el flujo obligatorio `Issue → Branch → PR → Validaciones → Revisión → Merge`.

No se permite utilizar el Dashboard como mecanismo para cambiar el estado real del proyecto.

## 📐 Evolución técnica

La representación visual debe evolucionar hacia generación reproducible o validación automatizada contra el Roadmap canónico. Mientras exista un snapshot derivado, cualquier divergencia debe considerarse defecto de consistencia y corregirse mediante el flujo controlado.
