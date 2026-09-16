# Reglas de Precedencia para Clasificación Automática de Labels

**Versión:** 1.0.0  
**Estado:** Diseño aprobado para automatización futura  
**Relacionado:** Política de Labels y `Label-Catalog.yml`

## Propósito

Definir cómo debe decidir una futura automatización la clasificación de Issues y Pull Requests sin crear ambigüedad ni categorías nuevas.

La automatización debe ser determinista:

> Mismo contexto + mismas reglas = misma clasificación.

## Orden de decisión

La clasificación seguirá este orden obligatorio:

```
1. Fuente declarada por el usuario
          ↓
2. Tipo de cambio identificado
          ↓
3. Artefactos afectados
          ↓
4. Dominio primario
          ↓
5. Tipo de trabajo
          ↓
6. Validación contra catálogo
```

## Regla 1 — La intención declarada tiene prioridad

Si el Issue declara explícitamente el dominio y tipo de trabajo mediante metadata válida, la automatización debe respetar esa clasificación.

La automatización valida; no reemplaza la decisión humana inicial.

## Regla 2 — El artefacto afectado orienta el dominio

Ejemplos:

| Artefacto | Dominio probable |
|---|---|
| `.github/`, workflows, políticas | governance/devops |
| `docs/Governance/` | governance/documentation |
| `docs/Architecture/` | architecture |
| `src/` | implementation |
| `tests/` | testing |
| modelos y esquemas de datos | data |

La coincidencia de artefacto nunca debe sustituir la revisión de contexto.

## Regla 3 — Dominio antes que tipo

Primero se determina:

```
¿Dónde impacta el cambio?
```

Después:

```
¿Qué clase de trabajo es?
```

Ejemplo:

```
docs/Architecture/ADR-001.md
+
crear una decisión

Resultado:
architecture + decision
```

## Regla 4 — Prioridad ante múltiples dominios

Si aparecen varios dominios posibles:

1. Usar el dominio declarado en el Issue.
2. Si no existe declaración, usar el artefacto principal modificado.
3. Si continúa la ambigüedad, detener automatización y solicitar clasificación humana.

Nunca elegir arbitrariamente.

## Regla 5 — Tipos de trabajo

La prioridad será:

```
bug
  ↓
feature
  ↓
refactor
  ↓
automation
  ↓
configuration
  ↓
decision
  ↓
baseline
  ↓
process
  ↓
investigation
  ↓
maintenance
```

Esta prioridad evita que un cambio correctivo sea clasificado erróneamente como mantenimiento.

## Regla 6 — Prohibiciones

La automatización NO puede:

- crear nuevos labels;
- cambiar el significado de un label existente;
- inferir fases del proyecto mediante labels;
- usar labels como prioridad;
- reemplazar la revisión humana en casos ambiguos.

## Casos ambiguos

Ejemplo:

```
Cambios en documentación de arquitectura
```

Puede ser:

- architecture + documentation
- documentation + process

Resultado:

```
requiere clasificación explícita
```

## Futuro motor automático

La implementación futura deberá consumir únicamente:

```
docs/Governance/Label-Catalog.yml
        +
LABEL-CLASSIFICATION-PRECEDENCE.md
        +
metadata del Issue
```

La automatización será una capa de validación y asistencia, no una fuente autónoma de decisiones del ecosistema.
