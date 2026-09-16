# Governance Entry Point

## Propósito

Este documento es el punto de entrada al modelo de gobernanza del repositorio SETA-EXPRESO-ECOSYSTEM.

Su objetivo es indicar cómo iniciar, ejecutar, validar y cerrar cualquier cambio dentro del ecosistema de ingeniería de software.

---

# Flujo obligatorio de cambios

```text
¿Quiero cambiar código?
        |
        v
Crear Issue
        |
        v
¿Quiero cambiar documentación?
        |
        v
Crear Documentation Issue
        |
        v
¿Existe aprobación y alcance definido?
        |
        v
Crear Branch gobernada
        |
        v
¿Terminé el cambio?
        |
        v
Crear Pull Request con plantilla
        |
        v
¿Pasan validaciones automáticas?
        |
        v
Merge protegido a main
```

---

# Reglas fundamentales

## 1. Todo cambio inicia con un Issue

Ningún cambio debe realizarse directamente sobre `main`.

El Issue debe definir:

- objetivo del cambio;
- alcance;
- impacto esperado;
- criterios de aceptación.

---

## 2. Branch obligatoria

La rama debe estar relacionada con el Issue:

```text
issue-<numero>-<descripcion>
```

Ejemplo:

```text
issue-116-create-governance-entry-document
```

---

## 3. Pull Request obligatorio

Toda integración hacia `main` debe realizarse mediante Pull Request.

El PR debe incluir:

- relación explícita con Issue;
- análisis de impacto;
- evidencia esperada;
- estado formal de integración;
- etiquetas correspondientes.

---

# Validaciones automáticas

Antes del merge se ejecutan controles de:

- Validate engineering evidence.
- Validate governance controls.
- Validate repository quality.
- Validate security controls.

---

# Principio de trazabilidad

El ciclo completo debe ser auditable:

```text
Issue
  ↓
Branch
  ↓
Commit
  ↓
Pull Request
  ↓
Validaciones
  ↓
Merge
```

---

# Protección de main

La rama principal representa una versión integrada y validada del sistema.

Por ello:

- no recibe cambios directos;
- requiere Pull Request;
- requiere validaciones exitosas;
- conserva evidencia del proceso.

---

Este documento debe mantenerse actualizado como mapa principal de entrada al proceso de ingeniería del ecosistema.
