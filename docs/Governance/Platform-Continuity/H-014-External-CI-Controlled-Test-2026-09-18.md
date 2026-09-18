# H-014 — Prueba controlada de CI externo $0 sin infraestructura propia

## Identificación

- Issue rector: #192
- Unidad: H-014
- Fecha: 2026-09-18
- Plataforma actualmente autoritativa: GitHub
- Rama controlada: `issue-192-zero-cost-portability-continuity`
- PR controlado: #193
- Estado: **PRUEBA PREPARADA — EJECUCIÓN EXTERNA PENDIENTE DE ACCIÓN DEL USUARIO**
- Decisión de esta unidad: evaluar primero **Codeberg + Woodpecker CI alojado**.
- No se autoriza migración ni cambio de autoridad.

## Objetivo

Comprobar de forma reversible si una instancia externa de CI alojada puede aportar una capa de continuidad con costo monetario $0, sin:

- comprar o dedicar una PC/servidor;
- instalar un runner propio;
- modificar `main`;
- convertir al proveedor externo en autoridad del proyecto;
- introducir credenciales permanentes en el repositorio;
- activar facturación;
- consumir innecesariamente la cuota de GitHub Actions.

La prueba no pretende demostrar equivalencia funcional entre Codeberg/Woodpecker y GitHub.

## Resultado documental de la investigación

La documentación oficial de Codeberg confirma que ofrece una instancia de Woodpecker CI en `ci.codeberg.org`. El acceso requiere una solicitud manual y revisión por un voluntario; después, el repositorio debe habilitarse específicamente en Woodpecker. Codeberg advierte que el servicio se ofrece bajo disponibilidad limitada, con posibles interrupciones, y que el uso de recursos debe ser razonable. citeturn0search2

La documentación también confirma que Codeberg dispone de Forgejo Actions alojado solamente de forma limitada y recomienda Woodpecker cuando se desea CI alojado. Esto evita asumir que Forgejo Actions sea una sustitución estable o equivalente de GitHub Actions. citeturn0search0

Codeberg se presenta como un servicio gratuito para proyectos compatibles con su misión, pero sus recursos de CI son compartidos y sujetos a condiciones de uso razonable. Por tanto, **$0 no significa capacidad ilimitada ni disponibilidad contractual garantizada**. citeturn0search5

## Por qué se selecciona Codeberg/Woodpecker para H-014

La selección es provisional y responde exclusivamente a los criterios de esta prueba:

1. CI alojado sin exigir infraestructura CI propia al proyecto.
2. No requiere instalar un self-hosted runner para la ruta alojada.
3. El software utilizado es libre/open source.
4. Existe documentación oficial de integración y limitaciones.
5. Permite mantener GitHub como autoridad y realizar una prueba aislada.
6. La activación requiere una acción manual, lo que permite controlar explícitamente cualquier conexión externa.

Esto **no constituye una recomendación general ni una declaración de superioridad** frente a otras plataformas.

## Alcance de la prueba

La prueba debe utilizar una copia o repositorio de prueba, no el repositorio principal como autoridad operativa.

### Fase A — Preparación

- [x] Candidato seleccionado: Codeberg/Woodpecker alojado.
- [x] Documentación oficial revisada.
- [x] Condiciones de acceso y limitaciones registradas.
- [x] GitHub permanece como autoridad.
- [x] No se modifica `main`.
- [x] No se instala runner propio.
- [x] No se añaden credenciales al repositorio.
- [x] No se activa facturación.
- [ ] Crear/usar cuenta externa de Codeberg.
- [ ] Solicitar acceso al CI alojado de Woodpecker.
- [ ] Esperar aprobación del servicio.

### Fase B — Integración controlada

Una vez aprobado el acceso:

1. crear o utilizar un repositorio de prueba en Codeberg;
2. transferir solamente una copia Git controlada;
3. habilitar el repositorio en Woodpecker;
4. ejecutar un pipeline mínimo de validación;
5. comprobar el resultado;
6. registrar duración, límites observados y mensajes relevantes;
7. comprobar que no se requiere infraestructura propia;
8. comprobar que no se genera obligación de pago;
9. retirar/deshabilitar la integración si el resultado no es satisfactorio.

No se debe conectar el repositorio principal de GitHub ni cambiar su autoridad como parte de esta fase.

## Pipeline mínimo previsto

La prueba debe ejecutar solamente controles deterministas y de bajo consumo, priorizando:

- existencia y contenido básico de archivos;
- validación Markdown;
- validación YAML;
- enlaces locales;
- presencia de artefactos críticos.

No se deben ejecutar suites pesadas, despliegues, builds de producto ni procesos que generen consumo innecesario.

## Criterios de aceptación

H-014 podrá marcarse como **VERIFICADO** solamente si existe evidencia de todos estos puntos:

| Criterio | Estado |
|---|---|
| Acceso al servicio alojado obtenido | PENDIENTE |
| Repositorio de prueba habilitado | PENDIENTE |
| Pipeline mínimo ejecutado | PENDIENTE |
| Resultado del pipeline registrado | PENDIENTE |
| Sin PC/servidor/runner propio | PREVISTO |
| Sin credenciales persistentes en GitHub | PREVISTO |
| Sin migración de autoridad | VERIFICADO POR DISEÑO |
| Sin modificación directa de `main` | VERIFICADO POR DISEÑO |
| Costo monetario $0 durante la prueba | PENDIENTE DE EVIDENCIA |
| Límites reales documentados | PENDIENTE |
| Procedimiento de desactivación/remoción probado | PENDIENTE |
| Exportación/recuperación Git independiente preservada | VERIFICADO POR DISEÑO |

## Límite de evidencia actual

La unidad **no declara que la prueba práctica ya fue ejecutada**.

La documentación externa demuestra que la ruta existe y cómo se solicita, pero no demuestra que este proyecto concreto ya tenga acceso, que el pipeline ya haya corrido ni que su disponibilidad futura esté garantizada. La ejecución requiere una acción explícita sobre una cuenta externa y aprobación del servicio. citeturn0search2

Por ello:

**Estado H-014: PREPARADA / PENDIENTE DE EJECUCIÓN EXTERNA.**

## Comparación de control

GitLab.com Free también dispone de CI/CD alojado sin infraestructura propia, pero su nivel Free tiene una cuota base de 400 compute minutes por mes y permite adquirir minutos adicionales. Para el requisito estricto de evitar cualquier ruta de facturación, esto obliga a un control adicional sobre la cuota y los mecanismos de compra. citeturn0search3turn0search6turn0search10

No se selecciona GitLab para la primera prueba; queda como candidato alternativo documentado.

## Seguridad y gobernanza

- GitHub continúa siendo la autoridad.
- El repositorio principal no se migra.
- No se modifica `main`.
- No se registra ningún runner propio.
- No se almacenan tokens externos en el repositorio.
- No se concede al proveedor externo autoridad normativa.
- La prueba debe poder eliminarse sin pérdida del historial Git de GitHub.
- La prueba no modifica Issues, PRs, revisiones, etiquetas ni permisos de GitHub.

## Próximo paso controlado

La ejecución real requiere que el usuario realice la acción externa de alta/solicitud en Codeberg.

Hasta que esa acción ocurra, el repositorio queda en estado **PENDIENTE**, sin fingir una ejecución ni un resultado de CI.

Cualquier integración posterior deberá documentarse en una nueva evidencia dentro de esta unidad o en una unidad posterior, conservando la trazabilidad de Issue → Branch → Commit → Validation → Review → PR → Merge.
