# Escalamiento de decisiones

## Ruta estándar

```text
Decision Owner
   ↓
Domain Owner
   ↓
System Owner / Product Owner
   ↓
Change Authority cuando implique cambio controlado
   ↓
Escalamiento extraordinario registrado
```

## Reglas

- Los conflictos entre dominios deben quedar registrados en un Decision Record.
- Una autoridad no puede aprobar fuera de su dominio salvo que exista una autoridad superior explícita.
- Security y QA pueden bloquear cuando los criterios formales de su dominio lo permitan.
- Change Authority controla la autorización de cambios; no sustituye la responsabilidad técnica del owner del CI.
- Las decisiones urgentes deben registrarse retrospectivamente con evidencia y justificación.
- La acumulación de roles debe considerarse en el análisis de riesgo cuando reduzca independencia.
