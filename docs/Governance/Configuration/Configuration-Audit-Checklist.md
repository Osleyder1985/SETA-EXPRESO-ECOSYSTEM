# Checklist de verificación de configuración

**Versión:** 1.0.0  
**Issue:** #45  
**Estado:** Propuesto

## Identificación

- [ ] Cada CI tiene identificador único.
- [ ] Cada CI tiene nombre y tipo.
- [ ] Cada CI tiene owner o rol responsable.
- [ ] Cada CI tiene fuente localizable.

## Estado y versión

- [ ] Cada CI tiene estado controlado.
- [ ] Cada CI tiene versión lógica.
- [ ] Las versiones se relacionan con commits/tags/releases cuando corresponde.
- [ ] Los CI retirados conservan historial.

## Baselines

- [ ] Cada baseline tiene identificador.
- [ ] El propósito de la baseline está definido.
- [ ] Los CIs incluidos están identificados.
- [ ] Las versiones incluidas están registradas.
- [ ] La aprobación es trazable.

## Cambio

- [ ] Cada cambio de CI baselined tiene Issue.
- [ ] Existe análisis de impacto.
- [ ] Existe PR.
- [ ] Las validaciones aplicables fueron ejecutadas.
- [ ] La nueva configuración quedó registrada.

## Reconciliación

- [ ] CI Register coincide con los artefactos existentes.
- [ ] Las dependencias declaradas son razonables.
- [ ] No existen CIs críticos sin owner.
- [ ] No existen baselines sin evidencia de aprobación.
- [ ] No existen cambios aprobados sin accounting.

## Automatización futura

Los checks anteriores se clasificarán progresivamente como `AUTOMATED`, `HYBRID` o `HUMAN`, siguiendo el modelo ya establecido para Quality Gates.
