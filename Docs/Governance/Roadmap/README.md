# 🗺️ Roadmap Dashboard

El Dashboard del Roadmap es la vista visual de presentación y navegación del Roadmap Maestro de Ingeniería del Ecosistema.

## 🎯 Propósito

Permitir que cualquier miembro del proyecto pueda entender rápidamente:

- dónde comenzó el recorrido;
- qué fases y Gates ya fueron completados;
- cuál es la posición actual;
- qué queda por ejecutar;
- qué evidencia respalda cada hito.

## 🧭 Fuente de verdad

La fuente canónica continúa siendo:

`Docs/Governance/08-Software-Roadmap.md`

El dashboard **no sustituye** al Roadmap documental ni a los artefactos de evidencia. Es una representación visual derivada y navegable.

## 🖥️ Dashboard

Abrir `Roadmap-Dashboard.html` en un navegador moderno.

## 🧩 Diseño

El dashboard se organiza en cinco zonas:

1. **🚀 Estado general** — progreso y posición.
2. **🧭 Recorrido A–O** — línea temporal visual del ciclo completo.
3. **📍 Estamos aquí** — fase activa o próxima.
4. **🗺️ Camino restante** — fases y Gates pendientes.
5. **🔬 Trazabilidad + 📜 Historia** — conexión entre planificación y evidencia.

## 🔐 Regla de consistencia

Cuando cambien estados, fechas, Gates, Issues, PRs o evidencias, el Roadmap canónico y esta vista deberán revisarse mediante el flujo obligatorio `Issue → Branch → PR → Validaciones → Revisión → Merge`.

## 📌 Evolución prevista

La versión inicial implementa una experiencia visual autónoma, responsive y navegable. Las siguientes evoluciones pueden incorporar generación automática desde datos estructurados, filtros por estado, búsqueda, métricas de ejecución y sincronización automatizada con GitHub Actions, siempre conservando una única fuente de verdad.
