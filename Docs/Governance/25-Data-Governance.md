# Data Governance

**Versión:** 0.1.0  
**Estado:** Baseline documental inicial  
**Fecha:** 2026-09-15  

## 1. Propósito

Establecer la capacidad formal de **Data Governance** del Ecosistema SETA-EXPRESO, definiendo principios, responsabilidades, controles, evidencia y trazabilidad para gobernar los datos durante su ciclo de vida.

Esta baseline no pretende diseñar todavía el modelo físico de datos ni fijar políticas operativas prematuras. Su objetivo es establecer el marco que deberá activarse y profundizarse cuando el descubrimiento del sistema, los requisitos, la arquitectura y el modelo de datos proporcionen evidencia suficiente.

## 2. Alcance

La capacidad deberá gobernar, según aplicabilidad:

- datos maestros;
- datos transaccionales;
- metadatos;
- clasificación de datos;
- calidad de datos;
- ownership y stewardship;
- acceso;
- privacidad;
- retención;
- lineage/procedencia;
- backup;
- recuperación;
- auditoría;
- eliminación/disposición.

## 3. Principios

- **Data as an asset:** los datos relevantes son activos que requieren responsabilidad explícita.
- **Purpose limitation:** los datos deben gestionarse conforme a una finalidad conocida y autorizada.
- **Minimum necessary data:** evitar recopilar, conservar o exponer datos innecesarios.
- **Ownership:** cada dominio de datos relevante debe tener responsable.
- **Stewardship:** las responsabilidades operativas de calidad y definición deben ser explícitas.
- **Traceability:** debe poder reconstruirse origen, transformación, uso y destino cuando resulte necesario.
- **Quality before consumption:** los consumidores críticos no deben asumir calidad sin evidencia.
- **Least privilege:** el acceso se concede según necesidad y autoridad.
- **Privacy by design:** la privacidad se considera desde el diseño y no únicamente después de implementar.
- **Retention by purpose:** la conservación debe tener justificación y reglas explícitas cuando corresponda.
- **Recoverability:** los datos críticos deben tener estrategia de backup y recuperación proporcional al riesgo.
- **Auditable lifecycle:** creación, modificación, acceso, transferencia y disposición deben poder auditarse cuando sean materialmente relevantes.
- **No premature precision:** no se inventan clasificaciones, períodos de retención, RPO/RTO, reglas de calidad o propietarios antes de disponer de evidencia del sistema.

## 4. Dominios de gobierno

### 4.1 Data Domains

Se distinguirán como mínimo:

- **Master Data:** entidades relativamente estables compartidas por múltiples procesos.
- **Transactional Data:** eventos y operaciones generados por los procesos del negocio.
- **Reference Data:** códigos, catálogos y valores controlados utilizados para interpretar datos.
- **Metadata:** información que describe estructura, significado, origen, uso, calidad y gobierno de los datos.

La clasificación concreta de entidades será definida durante las fases B–E con evidencia de negocio y requisitos.

### 4.2 Ownership and Stewardship

Cada dominio crítico deberá identificar, cuando corresponda:

- **Data Owner:** autoridad responsable de finalidad, uso aceptable, calidad esperada, acceso y decisiones de gobierno.
- **Data Steward:** responsable operativo de definición, calidad, metadatos, reglas y coordinación de incidencias.
- **Data Custodian:** responsable técnico de almacenamiento, protección, backup, recuperación y controles de plataforma cuando corresponda.

Estos roles no se asignarán ficticiamente en esta baseline.

### 4.3 Data Classification

La clasificación deberá considerar al menos sensibilidad, criticidad, impacto de divulgación, impacto de modificación y restricciones legales/contractuales.

Las categorías concretas del Ecosistema serán definidas después del inventario real de datos y del análisis de privacidad y seguridad. No se fija todavía una taxonomía operativa definitiva.

### 4.4 Data Quality

La calidad deberá gobernarse mediante reglas verificables y métricas reproducibles. Según el dominio, podrán considerarse dimensiones como:

- exactitud;
- completitud;
- consistencia;
- actualidad;
- unicidad;
- validez;
- integridad;
- trazabilidad.

Las reglas y umbrales deberán derivarse de requisitos, procesos y riesgos, no de valores arbitrarios.

### 4.5 Data Lineage

Cuando sea material para operación, cumplimiento, seguridad, investigación o decisiones críticas, deberá poder trazarse:

```text
Origen
  ↓
Captura
  ↓
Transformación
  ↓
Almacenamiento
  ↓
Integración
  ↓
Consumo
  ↓
Salida / Decisión
  ↓
Retención / Eliminación
```

El nivel de lineage requerido será proporcional al riesgo y a la criticidad.

### 4.6 Retention and Disposal

La retención deberá relacionarse con finalidad, requisitos legales/contractuales, necesidades operativas, riesgos y capacidad de recuperación. La eliminación deberá ser controlada y, cuando sea necesario, evidenciada.

No se establecerán períodos de retención concretos hasta disponer de los requisitos aplicables y de los datos reales.

### 4.7 Access and Privacy

El gobierno de datos deberá integrarse con Security Governance y Privacy. El acceso deberá basarse en necesidad, rol, finalidad y mínimo privilegio.

Los datos personales, confidenciales o regulados requerirán controles específicos de acuerdo con su contexto.

### 4.8 Backup and Recovery

Los datos críticos deberán disponer de estrategia de backup y recuperación proporcional a su impacto y riesgo. Los valores concretos de frecuencia, RPO, RTO, retención de copias y pruebas de restauración se determinarán durante arquitectura y operación con evidencia.

### 4.9 Audit

Los eventos de gobierno materialmente relevantes deberán dejar evidencia suficiente para reconstruir quién, qué, cuándo, por qué y con qué autorización se realizó una acción sobre los datos.

## 5. Ciclo de gobierno de datos

```text
Identificar
    ↓
Clasificar
    ↓
Asignar Ownership / Stewardship
    ↓
Definir Calidad y Metadatos
    ↓
Controlar Acceso / Privacidad
    ↓
Gestionar Lineage
    ↓
Retener / Proteger / Recuperar
    ↓
Auditar
    ↓
Eliminar / Disponer
    ↓
Revisar y Mejorar
```

## 6. Integración transversal

Data Governance se integra con:

- **Risk Management:** riesgos de pérdida, corrupción, divulgación, dependencia, calidad y disponibilidad.
- **Decision Governance:** decisiones arquitectónicas o de negocio que dependan de datos.
- **AI Governance:** procedencia, datasets, privacidad, evaluación y reproducibilidad de IA.
- **Security Validation:** acceso, secretos, exposición, integridad y protección.
- **Quality Governance:** calidad de datos como atributo verificable.
- **Evidence Governance:** evidencia de reglas, accesos, transformaciones, backups, restauraciones y disposición.
- **Metrics Governance:** métricas de calidad, cobertura, incidentes, acceso, retención y recuperación.
- **Architecture:** almacenamiento, integración, ownership técnico y flujos de datos.

## 7. Artefactos controlados

La capacidad evolucionará hacia artefactos como:

- Data Inventory;
- Data Domain Catalog;
- Data Classification Matrix;
- Data Ownership Register;
- Data Stewardship Register;
- Data Quality Rule Catalog;
- Data Lineage Register;
- Retention Schedule;
- Access Policy/Matrix;
- Privacy Data Register;
- Backup and Recovery Policy;
- Data Disposal Records;
- Data Governance Control Matrix.

En esta baseline se evita crear registros operativos ficticios. Los registros concretos se poblarán cuando exista evidencia del sistema.

## 8. Integración con el ciclo de vida

- **A — Concepción y gobernanza:** establecer capacidad y criterios.
- **B — Descubrimiento:** identificar dominios, fuentes, actores y responsabilidades.
- **C — Necesidades y objetivos:** determinar finalidades, criticidad y restricciones.
- **D — Requisitos:** convertir necesidades de datos en requisitos verificables.
- **E — Modelado:** definir entidades, dominios, metadatos y reglas.
- **F — Arquitectura:** decidir almacenamiento, integración, acceso, protección, backup y recuperación.
- **G/H — Diseño e implementación:** materializar controles y evidencia.
- **I/J — Integración y validación:** verificar calidad, seguridad, privacidad y recuperación.
- **K/L — Transición y operación:** activar ownership, monitoring, backups, auditoría y gestión de incidencias.
- **M/N — Evolución:** revisar calidad, retención, lineage, acceso y controles.
- **O — Retirada:** migrar, conservar o eliminar de forma controlada.

## 9. Madurez y límites de esta baseline

**Problema #6 no se considera completamente resuelto por este documento.**

Esta entrega establece una **capacidad documental operativa inicial**. La madurez aumentará cuando existan datos reales, dominios identificados, propietarios asignados, reglas de calidad verificadas, clasificación aprobada, lineage observable, políticas de retención, controles de acceso, backups probados y evidencia operacional.

No se declaran certificaciones, conformidad normativa ni controles técnicos implementados únicamente por la existencia de esta documentación.
