# Research Governance

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Baseline propuesta para revisión  
**Issue canónico:** #71  
**Relacionado:** #67, #69, #74

## 1. Propósito

Integrar investigación científica y evidencia de ingeniería dentro del governance core sin fabricar resultados, datasets, métricas ni conclusiones.

## 2. Cadena gobernada

```text
Engineering Evidence → Research Evidence → Dataset → Experiment Specification
→ Experimental Run → Result → Reproducibility Package → Research Output
```

La evidencia de ingeniería no se convierte automáticamente en evidencia científica: requiere pregunta, método, análisis y tratamiento de amenazas a la validez.

## 3. Roles

- **Research Owner:** accountable del rigor de investigación.
- **Researcher:** diseña/ejecuta investigación.
- **Data Steward:** controla procedencia/calidad de datasets cuando corresponda.
- **Reviewer:** revisa método y evidencia.
- **Publication Approver:** aprueba outputs cuando el contexto lo requiera.

No se asignan personas ficticias.

## 4. Research Question

```yaml
RQ-ID:
Question:
Context:
Motivation:
Population:
Scope:
Related-Engineering-Evidence: []
Related-Datasets: []
Method-Type: EXPLORATORY|DESCRIPTIVE|OBSERVATIONAL|EXPERIMENTAL|OTHER
Hypothesis:
Threats-to-Validity: []
Status: PROPOSED|ACTIVE|ANSWERED|WITHDRAWN
```

## 5. Dataset

Cada dataset conserva fuente, artefacto origen, método de recolección, periodo, población, variables, transformaciones, versión, integridad, clasificación de privacidad, restricciones, procedencia y limitaciones.

## 6. Experiment

Debe conservar RQ, hipótesis cuando aplique, objetivo, diseño, variables, dataset/version, entorno, procedimiento, método de análisis, requisitos de reproducibilidad y amenazas a la validez.

## 7. Experimental Run

Cada ejecución conserva versión del experimento, RQ, dataset, código/artefactos, entorno, parámetros, fecha, procedimiento, outputs observados, desviaciones, evidencia y relación con el registro de reproducibilidad. Los resultados observados nunca se sustituyen por resultados esperados.

El registro formal de ejecución se basa en `Docs/Research/Runs/Experimental-Run-Template.yml`. Un experimento especificado no implica que haya sido ejecutado; cada ejecución debe tener su propio `Run-ID` y estado.

## 8. Results

Los resultados distinguen observación, análisis, interpretación, conclusión y limitaciones. No se afirma causalidad a partir de correlación sin un diseño que la sustente.

## 9. Reproducibility

Según el estudio, el paquete debe conservar código, datos o procedimiento de obtención, configuración, entorno, parámetros, versiones de herramientas/modelos, procedimiento, artefactos, análisis y limitaciones. Restricciones de privacidad/licencia deben quedar registradas.

El registro formal se basa en `Docs/Research/Reproducibility/Reproducibility-Template.yml` y debe enlazar, cuando existan, RQ, experimento, ejecución y resultado. La existencia del registro no implica que la reproducción haya sido exitosa: el estado de reproducción debe reflejar la evidencia disponible.

## 10. Threats to Validity

Se consideran según aplicabilidad: construct, internal, external y conclusion validity, selección, medición, confusión, calidad de datos y limitaciones de reproducibilidad.

## 11. Research Outputs

```text
Publication → Result → Analysis → Run → Experiment → Dataset → Engineering Evidence
```

Un output científico no debe presentar como hecho un resultado sin evidencia fuente y método registrados.

## 12. Investigación sobre el Ecosistema

Cuando exista evidencia suficiente pueden estudiarse arquitectura, procesos, DevSecOps, IA, calidad, trazabilidad, productividad, evolución e ingeniería de sistemas. La existencia de una métrica operacional no implica por sí sola una conclusión científica.

## 13. Integración

Research Governance se integra con Decision, Risk, Data, AI, Security, Quality, Evidence, Metrics, Change, Configuration y Lifecycle Governance. Los cambios materiales siguen Change Control y SoD.
