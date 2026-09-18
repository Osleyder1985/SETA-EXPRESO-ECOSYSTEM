# H-001 — Verificación live-tree ↔ Artifact Authority Register

**Issue:** #187  
**Fecha:** 2026-09-18  
**Branch:** `issue-187-h001-register-tree-verification`  
**Baseline inicial verificada:** `main` @ `78286b408521f8d11c635de31c2ac313dfd60311`  
**Método:** Git Trees API recursiva + lectura directa del Artifact Authority Register.

## 1. Resultado de la comparación

La primera comparación reproducible del árbol vivo contra el registro encontró:

| Control | Resultado inicial |
|---|---:|
| Blobs bajo `docs/Governance/` | 188 |
| Artefactos registrados | 182 |
| IDs registrados | 182 |
| IDs únicos | 182 |
| Paths registrados únicos | 182 |
| Paths en árbol no registrados | 6 |
| Paths registrados inexistentes | 0 |
| IDs duplicados | 0 |
| Paths duplicados | 0 |
| IDs fuera del patrón `GOV-A####` | 0 |

Los seis artefactos detectados después de la auditoría #183 eran:

1. `171-Governance-Core-Final-Revalidation-2026-09-18.md`
2. `Artifact-Authority-Register-H001-Audit-2026-09-18.md`
3. `Decision/Decision-SoD-H002-H005-Audit-2026-09-18.md`
4. `Decision/SoD-Transversal-Operationalization-Matrix-H005-2026-09-18.md`
5. `Metrics/Metric-Operationalization.md`
6. `Security/H-004-Security-Applicability-Matrix.md`

## 2. Remediación

Se incorporaron esos seis paths al register con IDs estables:

- `GOV-A0183` → revalidación integral #171.
- `GOV-A0184` → auditoría H-001 #183.
- `GOV-A0185` → auditoría Decision/SoD #184.
- `GOV-A0186` → matriz de operacionalización transversal SoD #185.
- `GOV-A0187` → operacionalización de métricas #179.
- `GOV-A0188` → matriz de aplicabilidad/evidencia Security #180.

El commit de actualización del register es `2436185f9af323922b2a776309aec12dab819c68`.

## 3. Regla de autoridad

Estos artefactos no adquieren autoridad normativa por haber sido registrados.

Los informes de auditoría/revalidación son registros derivados. Las matrices de operacionalización son artefactos de apoyo. El register sigue siendo el mecanismo de identidad y clasificación, no una evidencia automática de implementación o efectividad.

## 4. Cierre de la comparación

La verificación debe repetirse después de registrar este propio informe, porque el informe constituye un nuevo blob bajo `docs/Governance/`. La comprobación final de cierre debe demostrar nuevamente igualdad 1:1 y registrar el ID de este informe.

## 5. Conclusión

La limitación de observabilidad documentada en #183 quedó superada técnicamente para el árbol consultado: la Git Trees API permitió obtener el inventario recursivo completo y reproducible. La primera pasada encontró seis artefactos legítimamente existentes pero todavía ausentes del register; fueron incorporados sin reasignar IDs existentes.

**No se infiere implementación, efectividad, conformidad normativa ni ausencia de deuda operacional a partir de esta verificación registral.**
