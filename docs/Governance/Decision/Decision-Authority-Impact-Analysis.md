# Análisis de impacto — Decision Authority Governance

**Issue:** #47  
**Estado:** Propuesto

## Alcance

El modelo de autoridad afecta transversalmente a las capacidades de gobernanza existentes.

| Capacidad | Impacto | Acción requerida |
|---|---|---|
| Decision Governance | Alto | Vincular decisiones con autoridad y aprobación |
| Quality Gates | Alto | Identificar autoridad de decisión del gate |
| Configuration Management | Alto | Autorizar cambios y baselines |
| Risk Management | Alto | Asignar owner y autoridad de aceptación/escalamiento |
| Security | Alto | Definir autoridad de bloqueo y aceptación de riesgo |
| Data Governance | Alto | Definir autoridad del Data Owner |
| AI Governance | Medio/Alto | Aplicar autoridad según tipo de uso de IA |
| Supplier Governance | Medio/Alto | Autorizar adquisición, aceptación y salida |
| Engineering Metrics | Medio | Definir ownership y uso de métricas para decisión |
| Lifecycle Master | Alto | Asociar autoridades a fases y gates |
| Requirements | Alto | Requirements Owner y aprobación de baseline |
| Architecture | Alto | System/Software Architect y decisiones arquitectónicas |

## Reglas de impacto

Todo nuevo tipo de decisión que aparezca durante el proyecto debe incorporarse a la matriz de autoridad antes de considerarse gobernado.

Toda modificación de un rol o autoridad debe activar revisión de dependencias y de los Decision Records relacionados.

## Riesgos introducidos

- concentración excesiva de autoridad;
- ausencia de independencia en roles acumulados;
- autoridad no registrada;
- decisiones tomadas fuera del dominio del rol;
- bloqueo sin evidencia;
- aprobación sin autoridad definida.

## Evidencia

- Role Register;
- Decision Authority Matrix;
- Decision Governance;
- Decision Records;
- Risk Register;
- Quality Gate Catalog;
- Configuration Item Register.
