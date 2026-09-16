# Label Automation Contract

## Objetivo
Definir el contrato mínimo para que la clasificación automática de Pull Requests utilice únicamente etiquetas autorizadas por `Label-Catalog.yml`.

## Fuente de verdad
`docs/Governance/Label-Catalog.yml` es la fuente de verdad del catálogo.

## Clasificación obligatoria
La metadata de gobernanza declara exactamente un valor para cada dimensión activa:
- `domain`
- `work_type`
- `priority`

## Regla de autorización
La automatización solo puede aplicar etiquetas presentes en la categoría correspondiente del catálogo.

## Seguridad
El workflow de clasificación requiere `pull-requests: write` exclusivamente para aplicar las etiquetas del catálogo. No requiere permisos de escritura sobre contenidos.

## Trazabilidad
La clasificación es declarativa en el PR y verificable mediante CI.
