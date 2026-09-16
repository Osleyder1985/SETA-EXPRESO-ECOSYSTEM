# Label Automation Contract

## Propósito

Definir las reglas formales para la clasificación y asignación automática de etiquetas en Pull Requests del ecosistema.

Este contrato separa la declaración humana de la aplicación automática de etiquetas, manteniendo trazabilidad y validación.

## Principios

1. Toda etiqueta automática debe existir en `Label-Catalog.yml`.
2. La clasificación debe provenir de metadata estructurada del Pull Request.
3. Ninguna etiqueta desconocida puede ser aplicada automáticamente.
4. La automatización no sustituye la evidencia; la complementa.

## Flujo de resolución

```
Pull Request
    ↓
Governance Metadata YAML
    ↓
Classification Resolver
    ↓
Label Catalog Validation
    ↓
GitHub Labels
    ↓
Governance Validation
```

## Fuente de clasificación

Ejemplo:

```yaml
governance:
  classification:
    domain: governance
    work_type: automation
    priority: medium
```

## Reglas

### Domain

Obligatorio.

Representa el área principal del cambio.

### Work Type

Obligatorio.

Representa la naturaleza del trabajo realizado.

### Priority

Opcional.

Representa la prioridad declarada cuando aplique.

## Validación

La automatización debe fallar si:

- La metadata no existe.
- La clasificación no está definida.
- El label no pertenece al catálogo oficial.
- Existen etiquetas fuera de política.

## Trazabilidad

El ciclo completo debe mantenerse:

```
Issue → Branch → PR → Classification → Validation → Merge
```
