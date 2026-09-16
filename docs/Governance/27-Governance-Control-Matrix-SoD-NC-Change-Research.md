# Governance Control Matrix — SoD, Non-Conformance, Change Authority & Research

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 1.0.0  
**Estado:** Baseline propuesta para revisión  
**Issues:** #52, #62, #66, #71

| ID | Capability | Control | Evidence | Nature | Limitation |
|---|---|---|---|---|---|
| SOD-001 | SoD | Risk-based independence level | SoD policy + change/decision record | G | Requires human risk judgment |
| SOD-002 | SoD | Role-combination restriction | SoD matrix | G | Does not itself enforce GitHub permissions |
| SOD-003 | SoD | Critical change independent review | PR/review/evidence | G/D | Requires suitable reviewer |
| SOD-004 | SoD | Exception + compensating control | Exception record | G | Small teams may need accumulation |
| NC-001 | Non-Conformance | Gate/control failure recorded | NC record | G | Detection source must be reliable |
| NC-002 | Non-Conformance | Classification | NC record | G | Severity requires judgment |
| NC-003 | Non-Conformance | Root cause | RCA evidence | G | Causal analysis is not fully automatable |
| NC-004 | Non-Conformance | Corrective/preventive action | Action + PR/Issue | G/D | Effectiveness needs verification |
| NC-005 | Non-Conformance | Closure verification | Test/check/review evidence | G/D | Evidence sufficiency needs review |
| CHG-001 | Change | Risk-based classification | Change record | G | Classification may change after analysis |
| CHG-002 | Change | Impact analysis | Impact Analysis | G | Semantic dependencies need engineering judgment |
| CHG-003 | Change | Required authority | Approval record | G | Authority assignment depends on context |
| CHG-004 | Change | Urgent change control | Emergency/urgent record | G | Retrospective verification may be necessary |
| CHG-005 | Change | Change traceability | Issue → Risk → Decision → PR → Evidence | G/D | Some links require human review |
| RES-001 | Research | Research question identity | RQ record | G | Not every engineering observation is research |
| RES-002 | Research | Dataset provenance | Dataset register | G/D | Restricted data may limit sharing |
| RES-003 | Research | Experiment specification | Experiment record | G | Method quality requires research review |
| RES-004 | Research | Experimental run traceability | `Runs/Experimental-Run-Template.yml` | G/D | Environment capture may be incomplete |
| RES-005 | Research | Result integrity | Result record + source data | G | Interpretation remains methodological |
| RES-006 | Research | Reproducibility package | `Reproducibility/Reproducibility-Template.yml` | G/D | Legal/privacy constraints may limit reproduction |
| RES-007 | Research | Threats to validity | Validity section | G | Cannot be reduced to a binary pass/fail |
| RES-008 | Research | Publication provenance | Output → Result → Dataset → Evidence | G | Publication review remains human |

## Integrated traceability

```text
Issue
  ↓
Risk / Impact
  ↓
Decision or Change
  ↓
SoD Requirement
  ↓
Implementation
  ↓
Gate / Validation
  ├── PASS → Evidence
  └── FAIL → Non-Conformance → RCA → Actions → Verification → Evidence

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
Reproducibility
  ↓
Research Output
```

## Governance status

These controls are baselineados documentalmente por esta PR. No se deben declarar como controles técnicos totalmente automatizados hasta disponer de implementación ejecutable y evidencia de workflow.
