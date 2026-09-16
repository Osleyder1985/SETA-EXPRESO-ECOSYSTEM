# Supplier / Third-Party Governance

Esta carpeta contiene los registros controlados de proveedores, terceros, servicios externos, componentes adquiridos y dependencias del Ecosistema.

## Registros

- `Third-Party-Register.yml`
- `Vendor-Risk-Register.yml`
- `SLA-Contractual-Control-Register.yml`
- `Security-Assessment-Register.yml`
- `License-Register.yml`
- `Dependency-Register.yml`
- `Exit-Strategy-Register.yml`

## Regla fundamental

Los registros pueden permanecer vacíos mientras no existan proveedores o componentes reales identificados. No se deben crear entradas ficticias para aparentar madurez.

## Trazabilidad

```text
Third Party
   ↓
Classification
   ↓
Risk / Security / Data / Legal / License / Dependency
   ↓
Decision
   ↓
Contract / Onboarding
   ↓
Monitoring / Reassessment
   ↓
Exit / Closure
   ↓
Evidence
```
