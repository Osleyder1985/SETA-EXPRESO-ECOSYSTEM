# Engineering Governance Dashboard

**Versión:** 0.1.0  
**Estado:** Diseño inicial derivado

## Propósito

Vista ejecutiva y operativa de la salud de la ingeniería. No sustituye al catálogo ni a las evidencias.

## Fuente canónica

`Docs/Governance/Metrics/Metric-Catalog.yml`

## Zonas

1. **Health:** cobertura del sistema métrico, métricas disponibles, métricas TBD/bloqueadas y alertas.
2. **Delivery:** Lead Time, Change Failure Rate, Deployment Frequency, Recovery Time.
3. **Quality:** Defect Density, Escaped Defects, Test Coverage, Requirement Coverage.
4. **Requirements:** trazabilidad, verification, ambigüedad y volatility.
5. **Architecture:** architectural debt, ADR coverage y architecture compliance.
6. **Security:** vulnerabilities, remediation time, dependency risk y secrets exposure.
7. **Governance:** PR con Issue, impact analysis, evidence, cambios fuera de proceso, gates PASS y artifacts sin owner.
8. **Trends:** evolución temporal y comparación contra baseline/target cuando existan.
9. **Evidence:** navegación desde cada indicador hacia su fuente y evidencia.

## Semántica visual

- 🟢 saludable: dentro del objetivo/umbral aprobado.
- 🟡 atención: desviación moderada o dato provisional.
- 🔴 crítico: condición que requiere acción.
- ⚪ TBD/N/A: no existe evidencia suficiente para calcular o interpretar.

Los colores son una ayuda visual y nunca sustituyen la definición de la métrica.

## Regla fundamental

El Dashboard debe poder reconstruirse desde el catálogo, sus fuentes y las evidencias. Si una tarjeta contiene un valor que no puede reproducirse, ese valor no debe presentarse como métrica confiable.

## Evolución

La implementación inicial es documental. La evolución prevista es: extracción reproducible → snapshots → cálculo automático → tendencias → alertas → correlación → acciones de mejora.
