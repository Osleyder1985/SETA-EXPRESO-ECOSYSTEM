# Supplier / Third-Party Governance

**Versión:** 0.1.0  
**Estado:** Baseline documental inicial  
**Issue:** #41  
**Fecha:** 2026-09-15  

## 1. Propósito

Establecer una capacidad formal, trazable y proporcional al riesgo para gobernar proveedores, terceros, servicios externos, componentes adquiridos y dependencias que participen en el ciclo de vida del Ecosistema SETA-EXPRESO.

La capacidad cubre adquisición y suministro durante el ciclo de vida y evita tratar los servicios externos como elementos fuera del alcance de la ingeniería.

Esta baseline no selecciona proveedores ni fija valores contractuales ficticios. Su finalidad es establecer el marco de control que deberá activarse cuando B–F proporcionen evidencia suficiente sobre servicios, productos, componentes y dependencias reales.

## 2. Alcance

Aplica, según corresponda, a:

- cloud e infraestructura gestionada;
- APIs y servicios externos;
- SaaS;
- servicios de IA;
- bibliotecas y componentes de software;
- correo electrónico y mensajería;
- pagos;
- mapas y geolocalización;
- autenticación e identidad;
- observabilidad;
- consultores y proveedores profesionales;
- otros terceros con acceso, dependencia o impacto material sobre el Ecosistema.

## 3. Principios

- **Lifecycle integration:** la adquisición y el suministro forman parte del ciclo de vida.
- **Risk proportionality:** la profundidad de evaluación depende de criticidad, exposición y riesgo.
- **Security by design:** seguridad y supply-chain security se consideran antes del uso material del tercero.
- **Data accountability:** el acceso a datos, finalidad, tratamiento, retención y eliminación deben quedar identificados.
- **Contractual clarity:** obligaciones relevantes deben ser verificables contractualmente cuando corresponda.
- **License compliance:** las licencias y obligaciones de componentes deben ser identificables y controlables.
- **Dependency transparency:** las dependencias directas y, cuando sea material, transitorias deben poder rastrearse.
- **Operational resilience:** deben considerarse sustitución, fallos, concentración y continuidad.
- **Exit readiness:** los servicios críticos deben tener una estrategia de salida proporcional a su riesgo.
- **Evidence first:** una afirmación de seguridad, disponibilidad, licencia o cumplimiento requiere evidencia apropiada.
- **No premature precision:** no se inventan proveedores, SLA, certificaciones, riesgos, licencias ni estrategias de salida antes de identificar los activos reales.

## 4. Ciclo de gobierno de terceros

```text
Identificar
    ↓
Clasificar
    ↓
Evaluar Riesgo
    ↓
Evaluar Seguridad / Datos / Legal / Licencia
    ↓
Aprobar
    ↓
Contratar
    ↓
Onboard
    ↓
Monitorizar
    ↓
Reevaluar
    ↓
Cambiar / Suspender / Terminar
    ↓
Ejecutar Exit Strategy
    ↓
Cerrar y Conservar Evidencia
```

## 5. Third-Party Register

Cada tercero material deberá disponer, como mínimo, de:

- `third_party_id`;
- nombre e identificación del proveedor;
- categoría;
- producto, servicio o componente;
- función dentro del Ecosistema;
- criticidad;
- lifecycle role;
- owner interno;
- sistemas afectados;
- datos accedidos o procesados;
- regiones relevantes cuando aplique;
- contrato y documentos asociados;
- estado;
- fecha de incorporación;
- próxima revisión;
- dependencias relacionadas;
- riesgos relacionados;
- evidencias.

## 6. Vendor Risk

La evaluación deberá considerar, según aplicabilidad:

- disponibilidad;
- continuidad;
- seguridad;
- privacidad;
- protección de datos;
- dependencia técnica;
- concentración/vendor lock-in;
- cambios de servicio;
- dependencia de subprocesadores o sub-tier suppliers;
- riesgo legal/contractual;
- riesgo financiero u operacional cuando sea material;
- capacidad de sustitución;
- impacto de interrupción o terminación.

Los riesgos relevantes deberán integrarse con **Risk Management** y conservar su trazabilidad hasta el tratamiento y riesgo residual.

## 7. SLA y controles contractuales

Cuando el servicio lo requiera, el control contractual deberá contemplar, según aplicabilidad:

- niveles de servicio;
- disponibilidad;
- soporte;
- tiempos de respuesta;
- gestión de incidentes;
- notificación de incidentes de seguridad;
- confidencialidad;
- propiedad y uso de datos;
- subcontratación/subprocesadores;
- auditoría o evidencia de controles;
- cambios materiales;
- continuidad;
- terminación;
- exportación/portabilidad;
- eliminación o devolución de datos;
- obligaciones posteriores a la terminación.

No se fijan SLA numéricos hasta disponer de requisitos de negocio, arquitectura, riesgos y contexto contractual.

## 8. Security Assessment

Antes del uso material de un tercero crítico o de alta exposición deberá existir una evaluación proporcional a su riesgo. Puede considerar:

- controles de identidad y acceso;
- cifrado;
- gestión de vulnerabilidades;
- seguridad de la cadena de suministro;
- aislamiento y arquitectura;
- registro y monitorización;
- gestión de incidentes;
- continuidad y recuperación;
- certificaciones/atestaciones cuando sean relevantes;
- subproveedores;
- evidencia técnica y contractual.

La existencia de una certificación externa no se interpretará automáticamente como evidencia suficiente para todos los riesgos del Ecosistema.

## 9. License Governance

Las licencias de software y componentes adquiridos deberán poder registrarse con:

- componente;
- versión;
- licencia;
- fuente;
- obligaciones;
- restricciones;
- compatibilidad;
- avisos/atribuciones;
- excepciones aprobadas;
- evidencia.

Las obligaciones deberán analizarse también en relación con distribución, modificación, integración y uso comercial cuando sean aplicables.

## 10. Dependency Governance

Las dependencias deberán poder clasificarse como:

- servicio externo;
- dependencia directa;
- dependencia transitoria;
- componente adquirido;
- componente interno reutilizado.

Para dependencias materialmente relevantes se deberá conservar, según contexto:

- identidad y versión;
- propietario;
- criticidad;
- procedencia;
- vulnerabilidades conocidas;
- ciclo de actualización;
- compatibilidad;
- evidencia de integridad/provenance;
- relación con SBOM cuando exista.

## 11. Exit Strategy

Para terceros críticos deberá existir una estrategia proporcional de salida que considere:

- condiciones de terminación;
- exportación de datos;
- portabilidad;
- formato y disponibilidad de datos;
- sustitutos plausibles;
- migración;
- revocación de credenciales y accesos;
- eliminación/devolución de datos;
- desmantelamiento de integraciones;
- continuidad durante transición;
- evidencia de cierre.

Los valores RTO/RPO y planes de migración detallados se definirán cuando arquitectura, operación y criticidad real los justifiquen.

## 12. Integración transversal

### Risk Management

`Third Party → Vendor Risk → Risk Register → Treatment → Residual Risk → Decision/Acceptance`.

### Security Governance

Los proveedores y dependencias externas deben integrarse con Security Validation, supply-chain security, gestión de vulnerabilidades y control de accesos.

### Data Governance

Debe identificarse qué terceros acceden, procesan, almacenan, transfieren o eliminan datos y bajo qué finalidad, autoridad y condiciones.

### AI Governance

Los proveedores de IA, APIs de modelos y servicios generativos deberán integrarse con Model Inventory, AI Risk, Data Provenance, Evaluation, incident management y condiciones de uso.

### Architecture

Los terceros materialmente relevantes deberán reflejarse como límites externos, dependencias, flujos de datos, puntos de fallo y alternativas cuando corresponda.

### Quality

Disponibilidad, rendimiento, soporte y comportamiento contractual relevante deberán poder convertirse en criterios verificables cuando sean requisitos de calidad.

### Evidence

Contratos, anexos, DPA, certificaciones, atestaciones, cuestionarios, SBOM, licencias, evaluaciones, incidentes, revisiones y evidencias de salida deberán conservarse según aplicabilidad.

### Metrics

La capacidad podrá alimentar métricas como cobertura de evaluación, terceros críticos con revisión vigente, exposición de dependencias, incumplimientos SLA, excepciones de licencia y preparación de salida.

### Decision Governance

Las selecciones, excepciones, aceptaciones de riesgo y decisiones de sustitución material deberán registrarse mediante Decision Records cuando corresponda.

## 13. Artefactos controlados

La capacidad evolucionará mediante:

- `Third-Party Register`;
- `Vendor Risk Register`;
- `SLA / Contractual Control Register`;
- `Security Assessment Register`;
- `License Register`;
- `Dependency Register`;
- `Exit Strategy Register`;
- evaluaciones y evidencias asociadas;
- `Supplier / Third-Party Control Matrix`.

Los registros deberán evitar activos ficticios: un registro vacío controlado es preferible a información inventada.

## 14. Integración con el ciclo de vida

- **A:** establecer gobierno y criterios.
- **B:** identificar proveedores, terceros y dependencias existentes.
- **C:** determinar necesidades, criticidad y restricciones.
- **D:** convertir necesidades contractuales, de seguridad, datos y continuidad en requisitos verificables.
- **E:** modelar límites, dependencias y flujos con terceros.
- **F:** decidir arquitectura, alternativas, fallback y controles.
- **G/H:** integrar y configurar servicios/componentes.
- **I/J:** verificar integración, seguridad, calidad y condiciones relevantes.
- **K/L:** operar, monitorizar y reevaluar.
- **M/N:** gestionar cambios, vulnerabilidades, nuevas versiones y sustitución.
- **O:** ejecutar migración, terminación, devolución/eliminación y cierre de evidencia.

## 15. Madurez y límites

**Problema #7 no se considera completamente resuelto por esta baseline.**

Esta entrega establece una capacidad documental inicial. La madurez operacional requerirá proveedores reales, evaluaciones de riesgo, condiciones contractuales, evidencias de seguridad, inventarios de licencias/dependencias, monitorización y estrategias de salida verificables.

No se declara certificación, conformidad normativa ni control técnico implementado únicamente por la existencia de esta documentación.
