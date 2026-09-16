# Research Governance

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Baseline propuesta para revisión  
**Issue canónico:** #71  
**Relacionado:** #67, #69, #74

---

## 1. Propósito

Integrar investigación científica y evidencia de ingeniería dentro del governance core sin fabricar resultados, datasets, métricas ni conclusiones.

El proyecto debe poder transformar evidencia real de ingeniería en investigación reproducible cuando exista una pregunta investigable.

## 2. Modelo

```text
Engineering Evidence
       ↓
Research Evidence
       ↓
Research Dataset
       ↓
Experiment Specification
       ↓
Experimental Run
       ↓
Result
       ↓
Reproducibility Package
       ↓
Research Output / Publication
```

La relación es trazable pero no automática: datos de ingeniería no se convierten en evidencia científica válida sin pregunta, método, análisis y tratamiento de amenazas a la validez.

## 3. Roles

- **Research Owner:** accountable del rigor del programa de investigación.
- **Researcher:** diseña y ejecuta investigación.
- **Data Steward:** controla procedencia y calidad de datasets cuando corresponda.
- **Reviewer:** revisa metodología y evidencia.
- **Publication Approver:** valida el output antes de publicación cuando el nivel de riesgo o compromiso lo requiera.

No se asignan personas ficticias en esta baseline.

## 4. Research Question

Toda investigación formal debe identificar una pregunta o conjunto de preguntas.

```yaml
RQ-ID:
Question:
Context:
Motivation:
Population:
Scope:
Related-Engineering-Evidence:
Status:
```

## 5. Hypothesis

Cuando el diseño de estudio lo requiera, la hipótesis debe ser explícita y falsable. Si el estudio es exploratorio o descriptivo, debe registrarse esa naturaleza en lugar de inventar una hipótesis.

## 6. Research Dataset

Cada dataset debe conservar:

```yaml
Dataset-ID:
Source:
Source-Artifact:
Collection-Method:
Collection-Period:
Population:
Variables:
Transformations:
Version:
Integrity:
Privacy-Classification:
License-or-Usage-Constraints:
Provenance:
Limitations:
Status:
```

El dataset debe poder rastrearse hasta sus fuentes. Los datos personales o restringidos se tratan conforme a Data Governance y Security/Privacy Governance.

## 7. Experiment Specification

```yaml
Experiment-ID:
RQ-ID:
Hypothesis:
Objective:
Design:
Variables:
Independent-Variables:
Dependent-Variables:
Controls:
Dataset-Version:
Environment:
Procedure:
Analysis-Method:
Reproducibility-Requirements:
Threats-to-Validity:
Expected-Outputs:
Status:
```

## 8. Experimental Run

Cada ejecución debe registrar versión del experimento, dataset, código/artefactos, entorno, parámetros relevantes, fecha y resultados generados.

No se deben sustituir resultados observados por resultados esperados.

## 9. Result

Los resultados deben distinguir:

- observación;
- análisis;
- interpretación;
- limitación;
- conclusión.

No debe afirmarse causalidad a partir de una correlación sin un diseño que permita sostenerla.

## 10. Reproducibilidad

El paquete de reproducibilidad debe contener, según el estudio:

- código o referencia versionada;
- dataset o procedimiento para obtenerlo, sujeto a restricciones;
- configuración;
- entorno;
- parámetros;
- versión de herramientas/modelos;
- procedimiento;
- artefactos generados;
- análisis;
- documentación de limitaciones.

Si un componente no puede compartirse por privacidad, licencia, seguridad o tamaño, debe registrarse la limitación y el mecanismo alternativo de reproducción.

## 11. Threats to Validity

Los estudios deben considerar, según aplicabilidad:

- construct validity;
- internal validity;
- external validity;
- conclusion validity;
- selection bias;
- measurement bias;
- confounding;
- data quality;
- reproducibility limitations.

## 12. Research Outputs

Una publicación, informe técnico, dataset público o artefacto científico debe conservar trazabilidad:

```text
Publication
   ↓
Result
   ↓
Analysis
   ↓
Experiment Run
   ↓
Experiment Specification
   ↓
Dataset
   ↓
Engineering Evidence
```

La publicación no debe presentar como hecho un resultado que no pueda vincularse con evidencia y método registrados.

## 13. Integración con Governance

Research Governance se integra con:

- Decision Governance;
- Risk Management;
- Data Governance;
- AI Governance;
- Security Governance;
- Quality Gates;
- Evidence Governance;
- Engineering Metrics;
- Change Control;
- Configuration Management;
- Lifecycle Master.

## 14. Investigación sobre el propio Ecosistema

Son candidatas a investigación, cuando exista evidencia suficiente, cuestiones relativas a arquitectura, procesos, DevSecOps, IA, calidad, trazabilidad, productividad, evolución y sistemas.

Ejemplo:

```text
RQ
 ↓
Variables
 ↓
Engineering Data
 ↓
Dataset
 ↓
Experiment / Observational Study
 ↓
Analysis
 ↓
Result
 ↓
Reproducibility
```

El hecho de que una métrica exista operacionalmente no implica que su interpretación científica ya esté demostrada.

## 15. Control de cambios

La creación o modificación de una política, dataset controlado, experimento, resultado o publicación debe conservar Issue, versión, evidencia y trazabilidad. Los cambios materiales siguen el Change Control y SoD correspondientes.
