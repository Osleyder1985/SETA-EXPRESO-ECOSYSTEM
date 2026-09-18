# H-013 — Evaluación de CI externo $0 sin infraestructura propia

**Issue:** #192  
**Unidad:** H-013  
**Fecha:** 2026-09-18  
**Autoridad:** GitHub  
**Estado:** EVALUACIÓN DOCUMENTAL CONTROLADA

## 1. Objetivo

Evaluar opciones de CI alojado por terceros que permitan mantener una capacidad de validación remota con costo monetario objetivo **$0**, sin comprar, dedicar ni administrar una PC, servidor o runner propio.

Esta unidad no autoriza migración, cambio de autoridad, conexión de cuentas externas ni activación de facturación.

## 2. Restricciones

- GitHub continúa siendo la plataforma principal y autoridad del proyecto.
- No se utilizará infraestructura propia para CI.
- No se habilitarán servicios de pago ni consumo con facturación implícita.
- Una cuota gratuita no se considera equivalente a disponibilidad ilimitada.
- La existencia de compatibilidad con GitHub Actions no implica equivalencia funcional.
- No se realizará migración de repositorio bajo esta unidad.
- Cualquier integración real con un proveedor externo requiere una unidad posterior con evidencia y control explícito.

## 3. Evidencia documental consultada

### GitLab.com

La documentación vigente de GitLab.com establece una cuota base de **400 minutos de cómputo por mes** para namespaces del nivel Free. La cuota se aplica a runners de instancia y se reinicia mensualmente. GitLab también documenta la posibilidad de comprar minutos adicionales una vez consumida la cuota. Por tanto, la ruta Free tiene una cuota finita y no debe tratarse como CI ilimitado ni como garantía permanente de $0.

**Resultado:** candidato de contingencia condicionada; requiere control estricto de cuota y facturación.

### Codeberg / Woodpecker CI

Codeberg documenta una instancia alojada de Woodpecker CI (`ci.codeberg.org`) y señala que el servicio alojado de Woodpecker es su opción recomendada para CI/CD. Su documentación también indica que Forgejo Actions alojado se ofrece de forma limitada, mientras que el runner propio requeriría infraestructura del usuario.

Codeberg ha documentado además que su servicio alojado de Woodpecker requiere una solicitud previa y que no mantiene actualmente límites estrictos de uso publicados en esa referencia histórica. Esto no constituye una garantía de disponibilidad futura ni un contrato de CI ilimitado.

**Resultado:** candidato relevante para evaluación práctica; no se declara adoptado hasta verificar acceso, límites actuales y condiciones de uso.

### SourceHut

SourceHut publica actualmente planes de pago para alojar proyectos y especifica que `builds.sr.ht` requiere pago. Existe asistencia financiera para quienes no pueden pagar, pero esto requiere una solicitud y no debe confundirse con una oferta universal de CI gratuito.

**Resultado:** descartado como ruta base de continuidad $0.

### Woodpecker autohospedado

Woodpecker es software libre y gratuito, pero una instancia propia requiere infraestructura. Como el proyecto descartó explícitamente dedicar hardware para CI, esta variante queda fuera de la arquitectura adoptada.

**Resultado:** descartado para la arquitectura actual.

## 4. Matriz de decisión factual

| Opción | CI alojado | Ruta $0 documentada | Cuota/límite relevante | Infraestructura propia | Estado |
|---|---|---|---|---|---|
| GitHub Actions | Sí | Sí, pero cuota actual agotada | Cuota mensual del plan | No | Contingencia limitada |
| GitLab.com Free | Sí | Sí | 400 compute minutes/mes | No | Candidato condicionado |
| Codeberg + Woodpecker alojado | Sí | Servicio alojado disponible según documentación | Condiciones de servicio a verificar | No | Candidato a prueba |
| Codeberg Forgejo Actions | Limitado | No debe asumirse ilimitado | Servicio alojado limitado | No, si se usa hosted | No adoptar aún |
| SourceHut Builds | Sí | No como oferta estándar | Servicio requiere pago | No | Descartado para $0 |
| Woodpecker autohospedado | Depende de infraestructura | Software $0 | Depende de recursos propios | Sí | Descartado |

## 5. Decisión arquitectónica de esta unidad

No se selecciona todavía un proveedor externo como sustituto de GitHub.

La arquitectura de continuidad queda temporalmente separada en tres capas:

1. **Validación local reproducible:** capacidad primaria para controles deterministas y para continuar trabajando sin consumir minutos alojados.
2. **Git portable + mirror/recovery:** preservación de la historia y referencias Git fuera de la ejecución CI.
3. **CI alojado externo $0:** contingencia opcional, pendiente de una prueba controlada sobre un proveedor que confirme condiciones reales de uso sin infraestructura propia y sin facturación inesperada.

La alternativa externa no debe convertirse en una nueva dependencia crítica antes de demostrar portabilidad, límites, seguridad y continuidad.

## 6. Próxima unidad requerida

H-014 deberá, si se mantiene la necesidad, realizar una **prueba documental/técnica controlada de un único proveedor candidato**, empezando por Codeberg/Woodpecker alojado o GitLab.com Free, sin migrar el repositorio principal y sin modificar `main`.

La prueba deberá verificar:

- registro/acceso disponible;
- integración con el repositorio sin modificar autoridad;
- ejecución de un control mínimo;
- límites reales observables;
- ausencia de facturación obligatoria;
- mecanismo de desactivación;
- exportación o eliminación limpia;
- separación entre CI externo y autoridad GitHub.

## 7. Límites de la evidencia

Esta unidad registra condiciones documentadas al **2026-09-18**. Las cuotas, políticas, disponibilidad y condiciones de servicios alojados pueden cambiar. Ningún proveedor externo queda declarado como equivalente a GitHub ni como garantía permanente de costo $0.

## 8. Estado

**VERIFICADO:** existencia documental de las opciones y sus principales restricciones.

**PENDIENTE:** prueba práctica de acceso y ejecución de CI externo bajo condiciones reales $0.

**NO VERIFICADO:** continuidad indefinida, ausencia absoluta de cambios futuros de cuota/política y equivalencia funcional con GitHub Actions.

**No se autoriza migración ni cambio de autoridad.**