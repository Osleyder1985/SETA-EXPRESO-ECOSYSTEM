# Research

Esta carpeta contiene los artefactos de investigación gobernados del Ecosistema.

## Estructura

```text
Docs/Research/
├── README.md
├── Questions/
├── Datasets/
├── Experiments/
├── Runs/
├── Results/
├── Reproducibility/
└── Publications/
```

Las carpetas se poblarán únicamente cuando existan artefactos reales. No se crean datasets, experimentos, ejecuciones, resultados o publicaciones ficticias para satisfacer la estructura.

## Artefactos gobernados

| Etapa | Artefacto | Template |
|---|---|---|
| Research Question | Pregunta de investigación | `Questions/Research-Question-Template.yml` |
| Dataset | Dataset y procedencia | `Datasets/Research-Dataset-Template.yml` |
| Experiment | Especificación experimental | `Experiments/Experiment-Template.yml` |
| Run | Ejecución experimental | `Runs/Experimental-Run-Template.yml` |
| Result | Resultado observado y análisis | `Results/Result-Template.yml` |
| Reproducibility | Paquete/registro de reproducibilidad | `Reproducibility/Reproducibility-Template.yml` |

## Cadena de procedencia

```text
Engineering Evidence
      ↓
Research Evidence
      ↓
Dataset
      ↓
Experiment
      ↓
Run
      ↓
Result
      ↓
Reproducibility Package
      ↓
Publication
```

## Reglas

1. Cada artefacto formal tiene un identificador estable.
2. Cada dataset conserva procedencia y restricciones de uso.
3. Cada experimento registra método, versión de datos y entorno relevante.
4. Cada ejecución registra las versiones y condiciones efectivas de ejecución, además de desviaciones y outputs observados.
5. Los resultados distinguen observación, análisis, interpretación y limitaciones.
6. Las amenazas a la validez se registran explícitamente.
7. La reproducibilidad se evalúa según el estudio y sus restricciones, y conserva evidencia del intento o resultado de reproducción cuando exista.
8. No se fabrican resultados ni se presentan métricas provisionales como resultados científicos.
9. Los cambios materiales siguen Change Control y SoD.
