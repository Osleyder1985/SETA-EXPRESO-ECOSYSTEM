# Análisis de impacto — Segregación de funciones

**Issue:** #49  
**Problema:** #11  
**Versión:** 1.0.0

## Cambio
Formalizar la separación de funciones entre definición, ejecución, aprobación, verificación, validación, bloqueo y revisión, con independencia proporcional al riesgo.

## Impactos

- Decision Authority: añade la dimensión de independencia a la autoridad.
- Risk Management: el nivel de riesgo determina la exigencia de independencia.
- Quality Gates: los cambios de mayor riesgo requieren revisión/validación independiente cuando corresponda.
- Change Control: la clasificación SoD forma parte de la evaluación del cambio.
- Configuration Management: modificación, aprobación y baseline quedan sujetos a SoD según riesgo.
- Security, Data y AI Governance: las decisiones materialmente afectadas requieren independencia adecuada.
- Supplier Governance: selección, aprobación y aceptación pueden requerir separación.
- Engineering Metrics: se medirán excepciones y desviaciones cuando haya datos.
- Lifecycle: SoD es transversal al ciclo de vida.

## Personas
No se inventan personas. La acumulación conceptual de roles sigue permitida cuando el riesgo lo permita; las funciones concretas se segregan cuando sea necesario.

## Riesgo de la modificación
El cambio puede alterar criterios de aprobación y validación futuros. Debe pasar las cuatro validaciones y conservar evidencia del HEAD exacto.

## Pendiente
La operacionalización transversal detallada queda registrada en `SoD-Operationalization-Backlog.md` y no se presenta como completada.
