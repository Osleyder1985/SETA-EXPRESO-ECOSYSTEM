# Auditoría Decision / SoD — H-002/H-005

**Issue:** #184  
**Fecha:** 2026-09-18  
**Baseline:** `main` / `77500f090876d4b19c02fa56a3534f88f6629913`

## Resultado

La auditoría confirma que las fronteras de autoridad ya formalizadas en #173, #174 y #175 son coherentes y que no existe evidencia suficiente para declarar un duplicado adicional ni un verdadero huérfano.

### Capas verificadas

```
Decision Authority
 ├─ Role-Register.yml
 ├─ Decision-Authority-Matrix.yml  [SoT estructurado]
 │        ↓ mirror
 └─ Decision-Authority-Register.md [derivado]

SoD
 ├─ Risk-Independence-Matrix       [semántica riesgo/independencia]
 ├─ Decision-Function-Matrix       [vocabulario + R1-R4]
 │        ↓
 ├─ Role-Combination-Matrix        [clasificación de pares]
 │        ↓
 ├─ Control-Matrix                 [controles/excepciones]
 ├─ Exception-Register             [registro; actualmente vacío]
 ├─ Templates / Checklist / Impact
 └─ Integration-Register           [SoT de alcance/estado de integración]
        ↓
 Integration-Register-2             [derivado/trazabilidad]
```

## H-002 — Decision fragmentation

**Estado: PARCIALMENTE RESUELTO.**

Se verifican 12 decisiones DEC-001..DEC-012 y su espejo Markdown. El contrato de espejo establece YAML como fuente canónica y MD como vista derivada.

No se observa una segunda fuente de autoridad equivalente dentro de los artefactos revisados. Los controles DA-001..DA-015 son controles de gobernanza y no sustituyen la matriz de autoridad.

La deuda residual es operacional: demostrar que Decision Records reales consumen estas autoridades y que nuevos tipos de decisión se incorporan antes de considerarse gobernados.

## H-005 — SoD

**Estado: PARCIALMENTE RESUELTO.**

Las matrices mantienen fronteras no equivalentes:

- Function Matrix: vocabulario y semántica R1-R4.
- Role Combination Matrix: clasificación ALLOWED/RESTRICTED/PROHIBITED.
- Control Matrix: controles y respuesta a excepciones.
- Risk-Independence Matrix: criterios de independencia.
- Exception Register: registros de excepción; actualmente vacío.
- Integration Register: alcance/estado registral de integración.

No hay base suficiente para consolidarlas.

## Integración transversal

El SoD Impact Analysis identifica explícitamente Decision Authority, Risk, Quality Gates, Change, Configuration, Security, Data, AI, Supplier y Metrics. Sin embargo, esa identificación documental **no prueba integración operacional continua**.

Los estados del Integration Register muestran:

- Decision Authority: INTEGRATED.
- Risk Management: INTEGRATED.
- Quality Gates: PENDING OPERATIONALIZATION.
- Change Control: PENDING OPERATIONALIZATION.
- Configuration Management: PENDING OPERATIONALIZATION.
- Security: PENDING OPERATIONALIZATION.
- Data: PENDING OPERATIONALIZATION.
- AI: PENDING OPERATIONALIZATION.
- Supplier: PENDING OPERATIONALIZATION.
- Metrics: PENDING OPERATIONALIZATION.

## Orfandad

No se confirma ningún verdadero huérfano.

Templates, checklists, status records e impact analyses tienen función de apoyo/operación documental. Su ausencia de referencias directas no basta para declararlos huérfanos.

## Deuda residual

1. Registrar Decision Records reales y verificar consumo de DEC-*.
2. Demostrar SoD en Change/Quality/Configuration/Security/Data/AI/Supplier/Metrics.
3. Probar enforcement o evidencia operacional donde corresponda.
4. Medir excepciones y desviaciones cuando existan datos.
5. Mantener revisión de nuevos tipos de decisión.

## Conclusión

La arquitectura Decision/SoD presenta fronteras semánticas explícitas y no requiere consolidación adicional con la evidencia disponible.

**H-002:** parcialmente resuelto; falta evidencia operacional de consumo y cobertura exhaustiva de nuevos tipos de decisión.

**H-005:** parcialmente resuelto; falta operacionalización transversal continua.

Esta auditoría no declara implementación, efectividad, cumplimiento normativo ni certificación.

## Metadata

```yaml
governance:
  schema_version: "1"
  classification:
    domain: governance
    work_type: process
  validation:
    evidence: required
    governance: required
    quality: required
    security: required
```
