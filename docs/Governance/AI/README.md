# Registros de gobernanza de inteligencia artificial

Este directorio contiene los registros controlados de AI Governance.

## Principio

El inventario de usos y el inventario de modelos son fuentes estructuradas. Las plantillas sirven para conservar evidencia específica cuando un caso de uso lo requiera.

## Estructura

- `AI-Use-Inventory.yml` — inventario de usos de IA.
- `Model-Inventory.yml` — inventario de modelos cuando corresponda.
- `Data-Provenance-Template.md` — procedencia de datos.
- `Prompt-Record-Template.md` — registro de prompts relevantes.
- `Evaluation-Record-Template.md` — evaluación/TEVV.
- `Incident-Record-Template.md` — incidentes de IA.

## Dominios

Cada uso se clasifica como:

- `build-time`
- `product-runtime`
- `research`

Un caso de uso puede relacionarse con un modelo, pero no todo uso de IA requiere un modelo propio.

## Regla de fuente de verdad

No se deben crear registros ficticios para llenar el inventario. Cuando no existan casos reales, los inventarios permanecen vacíos o expresan explícitamente que no hay usos registrados.
