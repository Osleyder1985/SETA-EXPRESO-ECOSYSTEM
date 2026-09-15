# Gobernanza de inteligencia artificial

**Proyecto:** SETA EXPRESO ECOSYSTEM  
**Versión:** 0.1.0  
**Estado:** Baseline documental inicial  
**Fecha:** 2026-09-15  
**Issue:** #37

---

## 1. Propósito

Establecer una capacidad transversal para gobernar el diseño, adquisición, uso, evaluación, despliegue, operación, evolución y retiro de capacidades de inteligencia artificial (IA), manteniendo responsabilidad humana, trazabilidad y evidencia.

Esta política distingue tres dominios:

| Dominio | Descripción | Riesgo dominante |
|---|---|---|
| `build-time` | IA utilizada para desarrollar, analizar, documentar o automatizar la ingeniería | confidencialidad, errores introducidos, dependencia, propiedad intelectual, pérdida de trazabilidad |
| `product-runtime` | IA incorporada al producto o a procesos operativos | seguridad, privacidad, calidad, impacto sobre usuarios, disponibilidad, decisiones automatizadas |
| `research` | IA utilizada para investigación y experimentación | reproducibilidad, validez, sesgo, procedencia de datos, integridad científica |

Un mismo proveedor o modelo puede aparecer en más de un dominio y deberá registrarse por caso de uso.

## 2. Referencias

La capacidad se alinea conceptualmente con ISO/IEC 42001:2023, ISO/IEC 23894:2023, NIST AI RMF 1.0 y NIST AI 600-1 para GenAI, integrándolas con 15288, 12207, 42010, 25010 y SSDF. Esta adopción no constituye certificación ni declaración de conformidad.

## 3. Principios

1. **Human accountability:** una persona o rol responsable responde por el uso de IA.
2. **Risk proportionality:** los controles aumentan con impacto, autonomía, sensibilidad de datos y reversibilidad.
3. **Evidence before trust:** una salida generada por IA no es evidencia suficiente por sí misma.
4. **Traceability:** caso de uso → modelo/servicio → datos → configuración → evaluación → resultado → decisión.
5. **Data minimization:** solo se introducen datos necesarios y autorizados.
6. **Least privilege:** herramientas, modelos y agentes reciben únicamente capacidades necesarias.
7. **Reproducibility:** los resultados relevantes deben poder reconstruirse dentro de límites razonables.
8. **No premature approval:** no se aprueba una tecnología por preferencia o popularidad.
9. **Historical integrity:** evaluaciones, incidentes y decisiones relevantes conservan historial.
10. **No false assurance:** ningún control aislado demuestra que una IA sea segura, justa o correcta en todos los contextos.

## 4. Ciclo de vida AI Governance

```text
Identificar uso
   ↓
Clasificar dominio y criticidad
   ↓
Registrar IA / modelo / datos
   ↓
Analizar riesgos e impactos
   ↓
Definir controles y supervisión humana
   ↓
Evaluar / TEVV
   ↓
Aprobar / restringir / rechazar
   ↓
Usar / desplegar
   ↓
Monitorizar
   ↓
Gestionar incidentes y cambios
   ↓
Reevaluar / retirar
```

La gobernanza se aplica de forma continua durante el ciclo de vida; no es un gate único.

## 5. Clasificación de criticidad

La criticidad deberá determinarse por contexto y evidencia. Como guía inicial:

- `low`: apoyo interno, reversible y sin datos sensibles relevantes.
- `moderate`: impacto material en ingeniería, procesos o información.
- `high`: impacto significativo sobre usuarios, seguridad, privacidad, operaciones o decisiones.
- `critical`: consecuencias potencialmente graves, alta autonomía o fuerte irreversibilidad.

La clasificación no debe sustituir el análisis de riesgos formal.

## 6. AI Inventory

Todo uso material de IA deberá registrarse con identificador estable, dominio, finalidad, owner, proveedor, modelo/servicio, datos, criticidad, estado, evidencia y relaciones con riesgos, decisiones y artefactos.

El inventario de usos es distinto del inventario de modelos: un mismo modelo puede soportar múltiples casos de uso con riesgos diferentes.

## 7. Model Inventory

Cuando exista un modelo identificable deberán conservarse, según aplicabilidad, versión, origen/proveedor, modalidad, capacidades, limitaciones, licencia/condiciones, evaluación, entorno, dependencias y estrategia de sustitución.

Los modelos externos no se consideran confiables por defecto.

## 8. Data Provenance

Los datos usados por una capacidad de IA deberán conservar procedencia, propietario, finalidad, transformaciones, versión, restricciones de licencia/privacidad, retención y evidencia de autorización cuando corresponda.

No se incorporarán datos personales, confidenciales, secretos o restringidos a servicios de IA sin autorización y controles adecuados.

## 9. Prompt Governance

Para usos generativos relevantes se deberán conservar, cuando sean necesarios para trazabilidad o reproducibilidad, versiones de prompts/familias de prompts, propósito, contexto, variables, restricciones, datos sensibles potenciales y resultados de evaluación.

Los prompts no deben contener secretos, credenciales ni información restringida innecesaria.

## 10. Evaluation / TEVV

La evaluación deberá ser proporcional al riesgo. Puede incluir funcionalidad, exactitud, robustez, seguridad, privacidad, fairness, factualidad/alucinaciones, resistencia adversarial, reproducibilidad, regresión y límites de uso.

Los criterios de aceptación deberán ser explícitos cuando una IA forme parte del producto o genere evidencia crítica.

## 11. Human Oversight

Debe definirse para cada caso de uso si la salida:

- puede consumirse automáticamente;
- requiere revisión humana;
- requiere revisión especializada o doble revisión;
- no puede constituir por sí sola la base de una decisión material.

La responsabilidad no se transfiere al modelo, proveedor o herramienta.

## 12. Seguridad y privacidad

La evaluación deberá considerar, según aplicabilidad, prompt injection, data leakage, insecure output handling, abuso de herramientas/agentes, exposición de secretos, dependencia de modelos/proveedores, acceso no autorizado, supply-chain risk y tratamiento indebido de información personal o confidencial.

## 13. Sesgo, fairness y daño

Cuando el caso de uso pueda afectar personas o grupos, deberán identificarse posibles impactos diferenciados y definir métodos de evaluación apropiados al contexto. No se declarará ausencia de sesgo únicamente porque una prueba aislada sea satisfactoria.

## 14. AI Incident Management

Los incidentes relacionados con IA deberán registrar al menos: Incident ID, fecha, caso de uso, modelo/versión, descripción, impacto, severidad, contención, causa conocida o hipótesis, evidencia, acciones correctivas, owner, estado y cierre.

## 15. Investigación y reproducibilidad

Los usos de IA en investigación deberán conservar, según pertinencia, modelo/versiones, prompts relevantes, datasets/versiones, parámetros, código, entorno, semillas, artefactos, resultados, limitaciones y amenazas a la validez.

La IA generativa no sustituye la evaluación científica ni la revisión crítica de resultados.

## 16. Relación con otras capacidades

```text
AI Governance
 ├──→ Risk Management
 ├──→ Decision Governance
 ├──→ Security Validation
 ├──→ Quality Validation
 ├──→ Evidence Validation
 ├──→ Engineering Metrics
 ├──→ Data Governance
 └──→ Research Reproducibility
```

Una decisión material de IA deberá utilizar ADR/EDR cuando corresponda. Los riesgos de IA deberán relacionarse con el Risk Register. Las métricas de IA se incorporarán al sistema métrico cuando existan fuentes reales.

## 17. Cambios y reevaluación

Un cambio material de modelo, proveedor, versión, datos, prompt, arquitectura, permisos, finalidad, población afectada o nivel de autonomía deberá activar análisis de impacto y reevaluación proporcional al riesgo.

## 18. Automatización futura

Quedan preparados como evolución: validación de esquemas, detección de inventarios incompletos, controles de secretos, evaluación automatizada, snapshots, métricas, alertas, enlaces de trazabilidad, detección de modelos obsoletos e integración con incident management.

No se declara implementada ninguna automatización que todavía no tenga código y evidencia ejecutable.

## 19. Madurez

Esta baseline establece una **capacidad documental operativa inicial**. No implica que existan ya modelos aprobados, casos de uso productivos, evaluaciones completas o certificación. La madurez aumentará con casos reales, evidencia, revisiones, automatización y aprendizaje de incidentes.

## 20. Artefactos controlados

- `Docs/Governance/23-AI-Governance.md`
- `Docs/Governance/24-AI-Governance-Control-Matrix.md`
- `Docs/Governance/AI/README.md`
- `Docs/Governance/AI/AI-Use-Inventory.yml`
- `Docs/Governance/AI/Model-Inventory.yml`
- `Docs/Governance/AI/Data-Provenance-Template.md`
- `Docs/Governance/AI/Prompt-Record-Template.md`
- `Docs/Governance/AI/Evaluation-Record-Template.md`
- `Docs/Governance/AI/Incident-Record-Template.md`

## 21. Evidencia de esta baseline

- Issue #37.
- PR asociado.
- Cuatro validaciones obligatorias sobre el commit final.
- Análisis de impacto.
- Referencias normativas revisadas.
- Inventarios sin datos inventados.
