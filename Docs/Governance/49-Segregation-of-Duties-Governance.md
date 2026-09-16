# Gobernanza de separación de funciones

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Propuesta para baseline mediante Issue #49  
**Problema:** #11  

## 1. Propósito

Establecer cómo se separan, restringen o acumulan las funciones de definición, ejecución, aprobación y validación cuando una decisión o cambio pueda generar un riesgo material.

> **La independencia requerida debe ser proporcional al riesgo.**

La segregación de funciones (Segregation of Duties, SoD) es un control de gobernanza. No presupone que cada rol conceptual deba ser desempeñado por una persona distinta.

## 2. Relación con Decision Authority

`48-Decision-Authority-Governance.md` define quién posee autoridad en cada dominio. SoD añade la pregunta de qué combinaciones de funciones son aceptables para una decisión o cambio concreto.

```text
Decision Authority → ¿quién tiene autoridad?
        ↓
Segregation of Duties → ¿puede coincidir con ejecución/validación?
        ↓
Risk-Based Independence
```

## 3. Funciones sujetas a segregación

- **DEFINE:** define necesidad, decisión, requisito o cambio.
- **EXECUTE:** implementa, configura o aplica la decisión/cambio.
- **APPROVE:** autoriza formalmente la decisión/cambio.
- **VERIFY:** verifica técnicamente o mediante pruebas.
- **VALIDATE:** determina si el resultado satisface el propósito y criterios de aceptación.
- **BLOCK:** puede impedir o escalar una decisión por un criterio formal.
- **REVIEW:** realiza revisión independiente cuando el nivel de riesgo lo exige.

Una misma persona puede acumular varias funciones cuando la matriz de riesgo lo permita.

## 4. Independencia proporcional al riesgo

| Nivel | Condición orientativa | Independencia mínima |
|---|---|---|
| R1 Bajo | Impacto limitado, reversible y sin activos críticos | Acumulación permitida; autocontrol documentado |
| R2 Moderado | Impacto relevante o dependencia de varios componentes | Revisión independiente según criterio del cambio |
| R3 Alto | Impacto significativo, seguridad/datos/operación crítica | Separación entre aprobación y ejecución cuando sea viable |
| R4 Crítico | Riesgo crítico para seguridad, datos, continuidad o activos esenciales | Independencia reforzada entre definición/aprobación/ejecución/validación; bloqueo independiente cuando corresponda |

Estos niveles orientan el control y deben aplicarse junto con el registro de riesgos. No sustituyen el análisis específico.

## 5. Reglas de segregación

### R1 — Bajo

Puede permitirse `DEFINE → EXECUTE → VERIFY` cuando exista autorización, evidencia mínima, ausencia de conflicto material y reversibilidad razonable.

### R2 — Moderado

Debe incorporarse revisión adicional cuando el cambio afecte múltiples dominios, activos relevantes o decisiones difíciles de detectar mediante autocontrol. La persona ejecutora no debe ser la única fuente de evidencia de corrección.

### R3 — Alto

Debe evitarse, cuando sea viable, `DEFINE + EXECUTE + APPROVE`. La persona ejecutora tampoco debe ser la única que valide el resultado. Los owners de seguridad, calidad, datos u operaciones intervienen cuando su dominio sea materialmente afectado.

### R4 — Crítico

Se requiere independencia reforzada:

```text
DEFINE ───────→ APPROVE
                  │
EXECUTE ───────→ VERIFY ───────→ VALIDATE
                  │
               BLOCK
```

La aprobación y validación no deben depender exclusivamente de quien ejecutó el cambio cuando exista una alternativa viable.

## 6. Matrices normativas

- `Docs/Governance/Decision/SoD-Decision-Function-Matrix.yml` define las funciones controladas.
- `Docs/Governance/Decision/SoD-Risk-Independence-Matrix.yml` relaciona riesgo con independencia.
- `Docs/Governance/Decision/SoD-Role-Combination-Matrix.yml` clasifica combinaciones como ALLOWED, RESTRICTED o PROHIBITED.

## 7. Excepciones y controles compensatorios

Cuando no existan suficientes personas para separar funciones:

1. registrar la excepción;
2. identificar el riesgo afectado;
3. justificar por qué la independencia no es viable;
4. aplicar un control compensatorio razonable;
5. conservar evidencia de revisión;
6. registrar el riesgo residual;
7. definir una condición de reevaluación.

Una excepción no convierte automáticamente una combinación prohibida en aceptable.

## 8. Aplicación a cambios controlados

```text
Necesidad → Impact Analysis → Risk Classification → DEFINE
→ APPROVE según SoD → EXECUTE → VERIFY → VALIDATE → Evidence → Cierre
```

El flujo del repositorio continúa siendo:

```text
Issue → Branch → PR → Governance → Quality → Security → Evidence → Review → Merge
```

## 9. Aplicación por dominio

| Dominio | Independencia especialmente relevante |
|---|---|
| Requisitos | definición/aprobación/validación |
| Arquitectura | decisión/implementación/revisión |
| Seguridad | implementación/aprobación/evaluación |
| Datos | definición/autorización/uso/validación |
| IA | definición/implementación/evaluación |
| Calidad | ejecución/evidencia/decisión de gate |
| Configuración | modificación/aprobación/baseline |
| Plataforma | cambio/aprobación/verificación |
| Operaciones | ejecución/autorización/validación |
| Proveedores | selección/aprobación/aceptación |

## 10. Trazabilidad

```text
Risk ID → Risk Level → Independence Requirement
       → Role Combination → Decision / Change → Evidence
```

## 11. Métricas

Cuando existan datos suficientes se medirán cambios clasificados por riesgo, aplicación correcta de SoD, excepciones, controles compensatorios, conflictos detectados, cambios de alto/crítico riesgo con revisión independiente y desviaciones detectadas después del cambio.

No se inventarán valores históricos.

## 12. Limitaciones

La primera implementación es documental y estructural. GitHub Free no se considera por sí mismo enforcement empresarial de segregación de funciones. La automatización solo se afirmará cuando exista un control técnico verificable.

La política evolucionará conforme aumenten participantes, criticidad, activos, proveedores y automatización del Ecosistema.
