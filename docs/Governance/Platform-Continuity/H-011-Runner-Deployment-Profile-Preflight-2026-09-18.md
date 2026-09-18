# H-011 — Perfil de despliegue y preflight para runner propio

## Control
- Issue: #192
- Unidad: 5 — preparación controlada del runner
- Fecha: 2026-09-18
- Autoridad del repositorio: GitHub
- Estado: diseño y preflight implementados; selección de hardware y registro del runner pendientes

## Objetivo

Establecer un perfil mínimo y reproducible para evaluar un equipo existente como runner propio, sin comprar hardware, instalar servicios ni registrar credenciales como parte de esta unidad.

La ruta de coste monetario objetivo es **$0** mediante hardware ya disponible y software libre/abierto. Este documento no declara que esa ruta esté verificada hasta ejecutar el preflight y completar una prueba controlada.

## Criterios de selección

| Criterio | Requisito de evaluación | Estado |
|---|---|---|
| Sistema operativo | Linux soportado por el runner seleccionado | PENDIENTE |
| Arquitectura | x86_64 o ARM64, según runner y workflow | PENDIENTE |
| Usuario | ejecución sin privilegios de root | PENDIENTE |
| Git | versión suficiente para el runner | PENDIENTE |
| CPU/RAM | suficientes para Quality Validation y aislamiento elegido | PENDIENTE |
| Disco | espacio suficiente para checkout, dependencias, logs y limpieza | PENDIENTE |
| Red | conectividad saliente necesaria para el proveedor elegido | PENDIENTE |
| Contenedores | Docker o Podman solo si el modo de ejecución elegido lo requiere | PENDIENTE |
| Seguridad | no compartir credenciales administrativas ni secretos del repositorio | PENDIENTE |
| Coste | hardware existente + software libre/abierto | NO VERIFICADO |

## Preflight

Herramienta:

`scripts/continuity/self-hosted-runner-preflight.sh`

El script es deliberadamente **read-only**. Comprueba:
- ejecución no-root;
- presencia y versión de Git;
- sistema/arquitectura;
- CPU, memoria y espacio disponible cuando las utilidades están presentes;
- disponibilidad de Docker, sin exigirlo;
- ausencia de nombres de archivos que indiquen secretos/token/credenciales en el workspace inmediato.

El preflight **no**:
- instala paquetes;
- descarga runners;
- registra runners;
- crea tokens;
- modifica servicios;
- cambia GitHub;
- cambia Forgejo/Gitea;
- ejecuta workflows remotos.

## Secuencia controlada

1. Identificar un equipo ya disponible.
2. Ejecutar el preflight localmente.
3. Registrar evidencia del resultado.
4. Seleccionar un modo de ejecución y aislar el runner.
5. Instalar el runner solo mediante una unidad controlada posterior.
6. Ejecutar primero una prueba equivalente a Quality Validation.
7. Comparar resultado con la validación local sobre el mismo commit.
8. Evaluar consumo de Actions y reproducibilidad.
9. Solo después estudiar integración con Forgejo/Gitea.

## Restricciones

- GitHub continúa siendo la autoridad del repositorio.
- No se cambia el remoto oficial por este artefacto.
- No se registra ningún runner con credenciales dentro del repositorio.
- No se declara ahorro monetario real hasta medir la ruta elegida.
- No se asume compatibilidad completa entre GitHub Actions y Forgejo Actions; la documentación de Forgejo indica expresamente que no son idénticos. citeturn0search2
- El runner propio elimina el consumo de minutos de runners alojados de GitHub, pero no convierte por sí mismo la infraestructura en coste cero: el hardware, electricidad, red, almacenamiento y mantenimiento siguen siendo recursos. GitHub documenta que los self-hosted runners no consumen minutos facturables de Actions. citeturn0search0

## Aceptación de la unidad

- [x] Criterios de selección documentados.
- [x] Preflight reproducible creado.
- [x] Preflight no instala ni registra nada.
- [x] Separación entre runner y autoridad del repositorio.
- [ ] Hardware existente identificado.
- [ ] Preflight ejecutado sobre el hardware seleccionado.
- [ ] Runner instalado.
- [ ] Runner registrado.
- [ ] Quality Validation reproducida.
- [ ] Ruta $0 verificada con evidencia.

## Conclusión

Esta unidad reduce el riesgo de instalar o registrar un runner sin conocer previamente la capacidad del equipo. El siguiente cambio operativo requiere un equipo concreto; hasta entonces, la implementación permanece limitada a documentación y preflight.
