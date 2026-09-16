# Impact Analysis — Problems #11–#14

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Branch:** `issue-52-62-66-71-governance-core`  
**Issues:** #52, #62, #66, #71

---

## 1. Objective

Evaluar qué capacidades existentes se relacionan con Segregation of Duties, Non-Conformance Management, Change Authority y Research Governance antes de integrar la baseline.

## 2. Existing governance capabilities reviewed

- `00-Software-Lifecycle-Master.md` — lifecycle transversal.
- `03-Artifacts-And-Evidence.md` — artefactos y evidencia.
- `04-Quality-Gates.md` — gates.
- `06-Change-Control-Workflow.md` — flujo de cambios.
- `07-Main-Protection-Strategy.md` — protección de `main`.
- `10-Governance-Enforcement-Architecture.md` — enforcement.
- `11-Governance-Control-Matrix.md` — matriz transversal.
- `17-Risk-Management-System.md` — riesgo.
- `18-Risk-Management-Control-Matrix.md` — controles de riesgo.
- `19-Decision-Governance.md` — decisiones.
- `20-Decision-Governance-Control-Matrix.md` — controles de decisiones.
- `21-Engineering-Metrics-Governance.md` — métricas.
- `22-Engineering-Metrics-Control-Matrix.md` — controles de métricas.

## 3. Impact by problem

| Problem | Existing capability | Gap closed by this change |
|---|---|---|
| #11 SoD | Decision Authority, Risk, Governance Enforcement | explicit independence levels, role combinations, exceptions and compensating controls |
| #12 NC | Quality Gates, validation workflows, Risk | formal NC lifecycle, RCA, corrective/preventive actions and closure evidence |
| #13 Change Authority | Change Control, Decision Governance, Risk | risk-based change classes and explicit ECA authority |
| #14 Research | Evidence, Metrics, Data/AI governance concepts | governed research questions, datasets, experiments, results and reproducibility |

## 4. Cross-capability effects

### Risk
SoD and Change Authority consume risk classification. NC records residual risk and may create or modify risk records. Research records threats to validity separately from operational risk.

### Decision Governance
Material changes and research-method decisions may require ADR/EDR records. Approval authority must respect SoD.

### Quality Gates
A gate failure can create an NC. A research artifact does not replace a Quality Gate. Gate evidence can become research evidence only after methodological qualification.

### Security and Data
C3 changes and research datasets involving sensitive information require Security/Data controls. Research provenance must not bypass privacy or access controls.

### Evidence
All four capabilities rely on evidence identity and provenance. A claim that a control is automated requires executable workflow evidence.

### Metrics
Engineering metrics may supply research data, but an operational metric is not automatically a scientific result. Definitions, population, collection method and limitations must be preserved.

## 5. No premature implementation claims

This branch establishes documented governance capabilities and templates. It does not claim that GitHub technically enforces every SoD rule, that all NCs are automatically generated, that ECA approvals are automatically enforced, or that scientific results already exist.

## 6. Traceability

```text
Issue #52 ─┐
Issue #62 ─┼→ Branch → Governance Artifacts → Validation → PR → Review → Merge
Issue #66 ─┤
Issue #71 ─┘
```

The implementation must remain associated with the four Issues and their acceptance criteria.
