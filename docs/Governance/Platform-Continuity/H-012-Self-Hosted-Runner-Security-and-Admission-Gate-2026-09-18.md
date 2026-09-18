# H-012 — Gate de seguridad y admisión para runner propio

## Control
- Issue: #192
- Unidad: 6 — seguridad y admisión antes del registro
- Fecha: 2026-09-18
- Autoridad: GitHub
- Estado: implementado como control preventivo; runner no registrado

## Propósito

Establecer un gate obligatorio antes de registrar o habilitar un self-hosted runner para este repositorio.

GitHub advierte que los self-hosted runners no proporcionan el mismo aislamiento efímero que los GitHub-hosted runners y recomienda especial cautela, particularmente en repositorios públicos, porque código no confiable puede comprometer persistentemente la máquina del runner.

## Decisión provisional

**No registrar todavía el runner.**

Antes del registro deben cumplirse todos estos controles:

| Control | Criterio | Estado |
|---|---|---|
| Hardware | Equipo existente identificado y dedicado/aislado para CI | PENDIENTE |
| SO | Sistema operativo soportado | PENDIENTE |
| Arquitectura | x64/ARM64 compatible | PENDIENTE |
| Usuario | Ejecución sin root | PENDIENTE |
| Red | HTTPS saliente por 443 y conectividad necesaria | PENDIENTE |
| Secretos | Sin credenciales personales ni claves privadas | PENDIENTE |
| Repositorio público | Riesgo de PR no confiable evaluado y controlado | PENDIENTE |
| Etiquetas | Labels reflejan realmente SO/arquitectura/capacidad | PENDIENTE |
| Actualizaciones | Procedimiento definido | PENDIENTE |
| Preflight | H-011 ejecutado y PASS | PENDIENTE |

## Reglas de admisión

1. El runner no debe contener secretos personales o de otros proyectos.
2. No se instalará como root ni se otorgarán privilegios administrativos innecesarios al proceso de jobs.
3. No se habilitará para cargas no confiables hasta definir aislamiento suficiente.
4. El primer workflow candidato será Quality Validation, no workflows con escritura administrativa o secretos.
5. Las labels deben ser verificables; GitHub utiliza labels como `self-hosted`, sistema operativo y arquitectura para seleccionar runners.
6. La conectividad debe limitarse a lo necesario; GitHub requiere HTTPS/443 y endpoints adicionales según los workflows.
7. Debe existir un procedimiento de actualización del runner.
8. La credencial temporal de registro nunca se almacenará en el repositorio ni en documentación versionada.

## Primera prueba

**Local → runner propio → comparación**

- mismo commit;
- mismos controles QV-001..QV-006;
- sin secretos de producción;
- sin escritura en `main`;
- logs conservados;
- resultado PASS/FAIL reproducible.

El runner no será considerado productivo simplemente por aparecer como `Idle` en GitHub. La aceptación requiere reproducibilidad y controles de seguridad.

## Criterio de salida

- [ ] Hardware concreto identificado.
- [ ] H-011 ejecutado con PASS.
- [ ] Riesgo del repositorio público resuelto mediante aislamiento/política apropiada.
- [ ] Runner instalado sin privilegios innecesarios.
- [ ] Runner registrado con credencial temporal no persistida.
- [ ] Labels verificados.
- [ ] Conectividad comprobada.
- [ ] Quality Validation reproducida.
- [ ] Evidencia documentada.
- [ ] Coste monetario $0 verificado para la ruta concreta.

## Conclusión

H-012 convierte la instalación del runner en una decisión condicionada por evidencia. Hasta completar el gate, GitHub continúa siendo la autoridad y no se modifica ningún workflow para enrutar jobs al runner propio.
