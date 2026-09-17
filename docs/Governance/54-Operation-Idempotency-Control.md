# Control de Idempotencia Operativa

## Propósito

Establecer un control explícito para evitar la creación duplicada de recursos durante operaciones automatizadas sobre GitHub, especialmente Issues, branches, commits y Pull Requests.

Este control complementa los controles de gobernanza del repositorio. No sustituye la protección nativa de GitHub ni pretende bloquear por sí mismo operaciones permitidas por la plataforma.

## Incidente de referencia

Durante la implementación de MC-001 se produjeron intentos repetidos de creación de recursos después de que una operación anterior ya había tenido éxito. El problema se identificó como una falta de idempotencia en la orquestación de herramientas: una operación de escritura confirmada no fue tratada como una operación terminal y se volvió a ejecutar.

El resultado fue la aparición de recursos duplicados que posteriormente tuvieron que ser identificados y cerrados como duplicados u obsoletos.

La causa no fue una deficiencia del modelo de gobernanza del repositorio, sino un fallo del procedimiento de ejecución de operaciones de escritura.

## Regla normativa

> **Una operación de escritura confirmada es terminal: nunca debe repetirse automáticamente.**

Después de recibir una respuesta de éxito de GitHub, el identificador del recurso creado o modificado debe conservarse y reutilizarse en las operaciones posteriores.

Si una operación de creación devuelve un error del tipo `already exists`, `Reference already exists` o equivalente, el procedimiento debe localizar y reutilizar el recurso existente. Nunca debe crearse otro recurso como respuesta al error.

## Protocolo obligatorio

Toda operación que pueda crear o modificar recursos de GitHub debe seguir esta secuencia:

```text
1. IDENTIFICAR
   Determinar el recurso esperado y su propósito.
        ↓
2. BUSCAR
   Verificar si el recurso ya existe.
        ↓
3. DECIDIR
   ├── Existe → REUTILIZAR
   └── No existe → CREAR UNA SOLA VEZ
                         ↓
                   CONFIRMAR RESULTADO
                         ↓
                   CONSERVAR IDENTIFICADOR
                         ↓
                   CONTINUAR CON EL MISMO RECURSO
```

### Reglas de ejecución

1. **Buscar antes de crear.**
2. **Crear una sola vez.**
3. **Persistir inmediatamente el identificador devuelto.**
4. **No repetir una escritura después de una respuesta de éxito.**
5. **Ante una respuesta ambigua, consultar el estado real antes de reintentar.**
6. **Ante `already exists`, localizar y reutilizar; no crear otro recurso.**
7. **Una misma necesidad debe conservar un único Issue canónico.**
8. **Una misma línea de cambio debe conservar una única branch canónica.**
9. **Una misma implementación debe conservar un único PR canónico.**
10. **Los recursos duplicados deben marcarse como duplicados/obsoletos y cerrarse mediante el flujo de gobernanza correspondiente.**

## Aplicación al flujo del proyecto

La unidad de cambio continúa siendo:

```text
Issue → Branch → Commit → Pull Request → Validaciones → Review → Merge
```

La idempotencia se aplica a cada transición. Antes de crear un recurso, debe comprobarse el recurso esperado; después de crearlo, debe conservarse su identificador y continuar sobre él.

### Ejemplo

Si ya existe:

```text
Issue #146
branch: issue-146-operation-idempotency-v2
```

una nueva ejecución no debe crear otro Issue ni otra branch para la misma necesidad. Debe reutilizar esos recursos.

## Relación con MC-001

MC-001 ya se encuentra implementado como control de integridad de `main` dentro de los mecanismos de validación existentes. Su función es detectar actualizaciones sospechosas o incompatibles con el flujo de integración y generar evidencia de la anomalía.

Este documento no crea un segundo MC-001. Formaliza el **control de idempotencia de la orquestación** que evita que la propia automatización genere duplicados durante la ejecución de cambios.

Por tanto:

```text
MC-001
  ↓
Detecta anomalías de integridad de main

Control de Idempotencia Operativa
  ↓
Evita duplicación de operaciones y recursos
```

Son controles distintos y complementarios.

## Evidencia mínima

Cuando ocurra una operación de escritura, la evidencia debe permitir reconstruir:

- recurso afectado;
- identificador del recurso;
- operación ejecutada;
- resultado de la operación;
- timestamp o contexto de ejecución disponible;
- branch/PR/Issue relacionados, cuando existan;
- resultado de validación posterior.

En caso de incidente de duplicación, debe conservarse además:

- recurso original;
- recurso duplicado;
- causa identificada;
- acción correctiva;
- estado final de ambos recursos.

## Criterio de cumplimiento

El control se considera cumplido cuando:

- no se crean recursos duplicados por reintentos automáticos;
- una operación confirmada no se ejecuta nuevamente;
- los errores de recurso existente provocan reutilización y no recreación;
- los recursos canónicos son identificables de forma inequívoca;
- las anomalías quedan registradas y son trazables;
- la documentación distingue entre controles preventivos nativos de GitHub y controles compensatorios/detectivos del repositorio y de la orquestación.

## Regla de auditoría

Durante cualquier auditoría futura, la existencia de un recurso duplicado debe investigarse como una posible violación de idempotencia antes de asumir una deficiencia del modelo de gobernanza.

La evidencia de ejecución prevalece sobre la intención declarada.
