# Quality Gates del ciclo de vida

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Definición inicial  
**Fecha:** 2026-09-15

---

## 1. Propósito

Definir puntos de control para decidir si existe evidencia suficiente para avanzar, continuar iterando, detener, corregir o cambiar de dirección.

Los gates no convierten el ciclo en cascada. Un gate puede requerir volver a una fase anterior cuando la evidencia sea insuficiente.

## 2. Gates

| ID | Gate | Fase asociada | Resultado esperado |
|---|---|---|---|
| G0 | Governance Ready | A | Gobierno y reglas mínimas establecidos |
| G1 | Discovery Ready | B | Estado actual comprendido |
| G2 | Problem And Objectives Ready | C | Problema, necesidades y objetivos definidos |
| G3 | Requirements Baseline | D | Requisitos verificables, priorizados y trazables |
| G4 | System Definition Ready | E | Sistema objetivo y contexto definidos |
| G5 | Architecture Baseline | F | Arquitectura evaluada y controlada |
| G6 | Design Ready | G | Diseño suficientemente detallado |
| G7 | Build Ready | H | Construcción y controles de ingeniería preparados |
| G8 | Verification Ready | I | Evidencia de verificación aceptable |
| G9 | Validation Accepted | J | Validación y aceptación logradas |
| G10 | Production Ready | K | Producción preparada y rollback definido |
| G11 | Operationally Stable | L | Operación estable y observable |
| G12 | Evolution Ready | M/N | Cambio o evolución evaluados |
| G13 | Retirement Complete | O | Retirada/migración y preservación de evidencia completadas |

## 3. Criterios comunes

Cada gate deberá considerar, según aplicabilidad:

- alcance;
- requisitos;
- calidad;
- seguridad;
- riesgos;
- dependencias;
- configuración y versiones;
- pruebas;
- trazabilidad;
- evidencia;
- responsables y aprobaciones.

## 4. Regla de decisión

Un gate puede resultar:

- **PASS:** criterios satisfechos.
- **PASS WITH CONDITIONS:** puede continuar con condiciones explícitas y fecha/responsable de resolución.
- **REWORK:** debe regresar a actividades anteriores.
- **BLOCKED:** existe impedimento que requiere decisión o información externa.

## 5. Evidencia

La evidencia del gate debe ser localizable desde GitHub mediante documentación, Issues, Pull Requests, commits, resultados de CI/CD, registros de pruebas u otras referencias controladas.

## 6. Evolución

Los criterios específicos de cada gate se detallarán conforme se conozca el contexto real del Ecosistema. No se inventarán criterios operativos antes de disponer de información suficiente.
