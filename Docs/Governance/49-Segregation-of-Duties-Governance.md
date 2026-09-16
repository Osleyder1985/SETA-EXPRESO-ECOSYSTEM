# Gobernanza de separación de funciones

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Propuesta para baseline mediante Issue #49  
**Problema:** #11  

## 1. Propósito

Establecer cómo se separan, restringen o acumulan las funciones de definición, ejecución, aprobación y validación cuando una decisión o cambio pueda generar un riesgo material.

El principio rector es:

> **La independencia requerida debe ser proporcional al riesgo.**

La segregación de funciones (Segregation of Duties, SoD) es un control de gobernanza. No presupone que cada rol conceptual deba ser desempeñado por una persona distinta.

## 2. Relación con Decision Authority

`48-Decision-Authority-Governance.md` define quién posee autoridad en cada dominio. Esta política añade una dimensión distinta: **qué combinaciones de funciones son aceptables para una decisión o cambio concreto**.

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

Estos niveles son una clasificación de control y deben aplicarse junto con el registro de riesgos. No sustituyen el análisis específico del riesgo.

## 5. Reglas de segregación

### 5.1 Bajo riesgo

Puede permitirse:

```text
DEFINE → EXECUTE → VERIFY
```

siempre que exista autorización, evidencia mínima, ausencia de conflicto material y reversibilidad razonable.

### 5.2 Riesgo moderado

Debe incorporarse revisión adicional cuando el cambio afecte múltiples dominios, activos relevantes o decisiones con consecuencias difíciles de detectar mediante autocontrol. La persona ejecutora no debe ser la única fuente de evidencia de corrección.

### 5.3 Riesgo alto

Debe evitarse, cuando sea viable:

```text
DEFINE + EXECUTE + APPROVE
```

La persona ejecutora tampoco debe ser la única que valide el resultado. Security Owner, QA Owner, Data Owner u Operations Owner intervienen cuando su dominio sea materialmente afectado.

### 5.4 Riesgo crítico

Se requiere independencia reforzada:

```text
DEFINE ───────→ APPROVE
                  │
EXECUTE ───────→ VERIFY ───────→ VALIDATE
                  │
               BLOCK
```

La aprobación y validación no deben depender exclusivamente de quien ejecutó el cambio cuando exista una alternativa viable.

## 6. Combinaciones de funciones

La matriz `Docs/Governance/Decision/SoD-Role-Combination-Matrix.yml` clasifica combinaciones como **ALLOWED**, **RESTRICTED** o **PROHIBITED** según el nivel de riesgo.

La clasificación se aplica a funciones en una decisión/cambio, no a la existencia conceptual de roles.

## 7. Autoridad de bloqueo

Una función de bloqueo no equivale a aprobación. Security Owner y QA Owner mantienen la autoridad de bloqueo definida por Decision Authority dentro de sus dominios. Otros owners podrán bloquear o escalar únicamente cuando exista un criterio formal de su dominio.

## 8. Excepciones y controles compensatorios

Cuando no existan suficientes personas para separar funciones:

1. registrar la excepción;
2. identificar el riesgo afectado;
3. justificar por qué la independencia no es viable;
4. aplicar un control compensatorio razonable;
5. conservar evidencia de revisión;
6. registrar el riesgo residual;
7. definir fecha o condición de reevaluación.

Una excepción no convierte automáticamente una combinación prohibida en aceptable; requiere justificación y tratamiento explícito del riesgo.

## 9. Aplicación a cambios controlados

```text
Necesidad → Impact Analysis → Risk Classification → DEFINE
→ APPROVE según SoD → EXECUTE → VERIFY → VALIDATE → Evidence → Cierre
```

El flujo de repositorio continúa siendo:

```text
Issue → Branch → PR → Governance → Quality → Security → Evidence → Review → Merge
```

## 10. Aplicación por dominio

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

## 11. Trazabilidad con riesgos

```text
Risk ID → Risk Level → Independence Requirement
       → Role Combination → Decision / Change → Evidence
```

La política no sustituye el sistema de gestión de riesgos.

## 12. Métricas

Cuando existan datos suficientes se medirán: cambios clasificados por riesgo, aplicación correcta de SoD, excepciones, excepciones con controles compensatorios, conflictos detectados, cambios de alto/crítico riesgo con revisión independiente y desviaciones detectadas después del cambio.

No se deben inventar valores históricos.

## 13. Estados de control

`NOT_APPLICABLE → ALLOWED → RESTRICTED → SEGREGATED → EXCEPTION → BLOCKED → RESOLVED`

Cada estado debe estar respaldado por evidencia suficiente para el nivel de riesgo.

## 14. Responsabilidad y autoridad

Decision Authority determina el owner/accountable de cada decisión. SoD determina las condiciones de independencia que deben acompañar a esa autoridad.

Cuando exista conflicto entre autoridad y requisito de independencia, el conflicto debe escalarse y registrarse; no debe resolverse mediante autoridad implícita.

## 15. Limitaciones actuales

La primera implementación es principalmente documental y estructural. GitHub Free no se considera por sí mismo un enforcement empresarial de segregación de funciones. La automatización solo debe afirmarse cuando exista un control técnico verificable.

La política debe evolucionar conforme aumenten participantes, criticidad, activos, proveedores y automatización del Ecosistema.
