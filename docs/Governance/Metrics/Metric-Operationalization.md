# Metric Operationalization Record

**Status:** controlled-baseline  
**Scope:** H-003 / Issue #179  
**Catalog:** `docs/Governance/Metrics/Metric-Catalog.yml`  
**Policy:** `docs/Governance/21-Engineering-Metrics-Governance.md`

## Purpose

Convert the metric catalog from a definition-only baseline into an auditable measurement capability without inventing values or treating dashboards as a source of truth.

## Current operational classification

| Class | Meaning | Current rule |
|---|---|---|
| `defined` | Definition exists but reproducible collection is not yet established | No measured value may be claimed |
| `available` | Reproducible source and collection method exist and have produced evidence | Value may be reported with timestamp and source |
| `provisional` | Evidence exists but collection/baseline/coverage still has a controlled limitation | Value must carry limitation |
| `blocked` | Measurement is applicable but a required source/capability is unavailable | No value |
| `deprecated` | Metric no longer governed for new measurement | Historical evidence remains immutable |
| `TBD` | Required semantic field is not yet defined | Cannot be operationalized |

## First operational slice

The first implementation slice targets metrics whose source is the GitHub repository itself and whose evidence can be derived reproducibly from GitHub metadata:

- **EM-020 PR with Issue**
- **EM-021 PR with Impact Analysis**
- **EM-022 PR with Evidence**
- **EM-023 Out-of-Process Changes**
- **EM-024 Gates Pass Rate**
- **EM-025 Artifacts without Owner**

No deployment telemetry is assumed. Therefore EM-001 through EM-004 remain dependent on deployment/incident infrastructure and are not marked available by inference.

Security metrics EM-016 through EM-019 remain dependent on the security-validation implementation and its actual scan evidence.

## Measurement contract

Every operational snapshot MUST contain:

1. measurement timestamp;
2. repository and default branch;
3. metric ID;
4. population/scope;
5. numerator and denominator where applicable;
6. formula/version used;
7. source evidence;
8. collection method;
9. limitations;
10. snapshot identifier.

A dashboard or rendered report is a **derived view**. The measurement evidence and reproducible collection logic remain authoritative for the measured result.

## Historical integrity

Snapshots are append-only records. A later correction creates a new snapshot with an explicit correction relationship; it does not rewrite a prior measured result.

## Automation boundary

The repository workflow may collect GitHub metadata for the first operational slice. It MUST use read-only permissions for repository/PR/issue metadata and Actions evidence. It MUST NOT mutate Issues, PRs, branches, tags, or protected content as part of measurement.

Failures in collection MUST produce a visible failed measurement run rather than a fabricated zero, PASS, or empty dataset.

## Initial applicability decisions

- Deployment metrics: **blocked / not yet operationally applicable** until deployment semantics and environments are established.
- Incident/recovery metrics: **blocked** until controlled incident telemetry exists.
- GitHub governance metrics: **applicable** and suitable for the first automation slice.
- Security metrics: **applicable subject to H-004 applicability review**; no value is asserted here.
- Quality/requirements/architecture metrics: remain **defined** until their required baselines and evidence sources are established.

## Acceptance evidence

H-003 is not considered fully remediated merely because this document exists. Closure requires at least one successful reproducible measurement run for the first operational slice, preserved evidence, and verification that the generated result can be independently recomputed from the declared source.

## Governance constraints

Changes to metric semantics remain subject to the synchronization contract in the Metric Catalog and to the controlled flow:

**Issue → Branch → Commit → Validation → Review → PR → Merge → main**

No metric value in this record is evidence of effectiveness unless the underlying operational evidence establishes effectiveness.
