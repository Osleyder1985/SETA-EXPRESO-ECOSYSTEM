# Registro de integración — SoD

**Issue:** #49  
**Autoridad:** registro canónico de integraciones SoD y de su estado de operacionalización.  
**Fuente de verdad:** este documento es la referencia normativa/registral para el alcance de integración; no constituye evidencia de que un control esté automatizado o sea efectivo.

## Regla de autoridad

Este registro mantiene **una sola fila por capacidad de integración SoD** y es la fuente canónica para el estado de integración/operacionalización. Los artefactos de dominio, matrices y controles pueden consumir esta información, pero no deben crear una segunda lista competidora del mismo alcance.

SoD-Integration-Register-2.md no es una fuente de verdad paralela. Su función queda limitada a trazabilidad complementaria y debe apuntar a este registro cuando necesite contextualizar una integración.

| Capacidad | Integración requerida | Estado |
|---|---|---|
| Decision Authority | SoD determina independencia asociada a autoridad | INTEGRATED |
| Risk Management | Risk Level alimenta la exigencia de independencia | INTEGRATED |
| Quality Gates | Gates de mayor riesgo consideran revisión/independencia | PENDING OPERATIONALIZATION |
| Change Control | Cambios controlados requieren clasificación SoD | PENDING OPERATIONALIZATION |
| Configuration Management | Modificación/aprobación/baseline se evalúan por riesgo | PENDING OPERATIONALIZATION |
| Security | Cambios con impacto de seguridad requieren independencia adecuada | PENDING OPERATIONALIZATION |
| Data | Decisiones de datos se someten a SoD según riesgo | PENDING OPERATIONALIZATION |
| AI | Decisiones de IA se someten a SoD según riesgo | PENDING OPERATIONALIZATION |
| Supplier | Selección/aprobación/aceptación se evalúan por riesgo | PENDING OPERATIONALIZATION |
| Metrics | Excepciones y desviaciones SoD serán medibles | PENDING OPERATIONALIZATION |

Los estados **PENDING OPERATIONALIZATION** representan trabajo futuro trazable; no se presentan como controles ya automatizados ni como evidencia de efectividad.

## Límite de autoridad

Este registro no sustituye:
- la política principal de SoD;
- las matrices de funciones, riesgo, combinaciones o controles;
- los registros de excepciones;
- la evidencia de ejecución o efectividad.

Cuando exista conflicto entre una lista de integraciones derivada y este registro, prevalece este registro para el **alcance y estado registral de la integración SoD**, sujeto a revisión mediante cambio controlado.
