# Quality Gates del ciclo de vida

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.4.0  
**Estado:** Definición controlada en evolución  
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

## 3. Validaciones transversales de cambios

Las validaciones automatizadas para una unidad de cambio siguen esta cadena:

```text
Issue
  ↓
Branch
  ↓
Pull Request
  ↓
Governance Validation
  ↓
Quality Validation
  ↓
Security Validation
  ↓
Evidence Validation
  ↓
Review / Approval
  ↓
Merge
```

Un resultado `PASS` de una validación automatizada es evidencia técnica de los controles aplicables de esa capa; no equivale por sí mismo al resultado de un Quality Gate.

### Quality Validation

Quality Validation aporta comprobaciones técnicas objetivas. Un `QUALITY_VALIDATION=PASS` no certifica la calidad integral del producto.

### Security Validation

Security Validation aporta comprobaciones de seguridad objetivas. Un `SECURITY_VALIDATION=PASS` no certifica seguridad integral ni ausencia de vulnerabilidades.

Para una unidad de cambio, un fallo objetivo de Quality o Security Validation implica que el cambio **no debe considerarse conforme** hasta que el defecto sea corregido o exista una decisión formal y trazable de excepción.

## 4. Criterios comunes

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
- responsables y aprobaciones;
- control de cambios y estado del Pull Request cuando el gate implique una modificación controlada;
- resultados de Governance Validation, Quality Validation y Security Validation cuando correspondan.

## 5. Regla de decisión

Un gate puede resultar:

- **PASS:** criterios satisfechos.
- **PASS WITH CONDITIONS:** puede continuar con condiciones explícitas y fecha/responsable de resolución.
- **REWORK:** debe regresar a actividades anteriores.
- **BLOCKED:** existe impedimento que requiere decisión o información externa.

Una excepción no debe ocultarse convirtiendo un `FAIL` automatizado en `PASS`. Debe registrarse como condición, excepción o decisión controlada según corresponda.

## 6. Evidencia

La evidencia del gate debe ser localizable desde GitHub mediante documentación, Issues, Pull Requests, commits, resultados de CI/CD, registros de pruebas u otras referencias controladas.

Cuando el gate corresponda a una unidad de cambio, la evidencia deberá permitir comprobar que el cambio fue propuesto mediante Issue, implementado en branch, sometido a análisis de impacto y presentado mediante Pull Request antes de su integración.

Cuando aplique Quality Validation o Security Validation, la evidencia deberá identificar el workflow run y los controles ejecutados.

## 7. Evolución

Los criterios específicos de cada gate se detallarán conforme se conozca el contexto real del Ecosistema. No se inventarán criterios operativos antes de disponer de información suficiente.

Los criterios de los gates evolucionarán mediante cambios controlados y análisis de impacto sobre el ciclo maestro, el catálogo de artefactos y las políticas relacionadas.
