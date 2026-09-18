# H-007 — Auditoría de versiones normativas de estándares — 2026-09-18

**Issue:** #188  
**Rama:** `issue-188-h007-standards-version-audit`  
**Estado:** Auditoría inicial completada; remediación pendiente  
**Naturaleza:** Evidencia de gobernanza; no constituye declaración de conformidad.

## 1. Objetivo

Verificar las referencias normativas explícitas utilizadas por el Governance Core y establecer una regla controlada para distinguir:

- edición vigente;
- edición histórica/reemplazada;
- borrador en desarrollo;
- referencia pendiente de verificación.

La auditoría separa el estado documental del repositorio de cualquier afirmación de conformidad o efectividad.

## 2. Fuentes canónicas del repositorio examinadas

- `docs/Governance/02-Standards-Lifecycle-Matrix.md`
- `docs/Governance/00-Software-Lifecycle-Master.md`
- `docs/Governance/GOVERNANCE-FOUNDATION.md`
- `docs/Governance/README-Governance.md`
- `docs/Governance/Artifact-Authority-Register.yml`

## 3. Referencias normativas explícitas encontradas en los artefactos canónicos

| Referencia | Estado externo verificado | Uso documental actual | Tratamiento H-007 |
|---|---|---|---|
| ISO/IEC/IEEE 15288:2023 | Publicada, edición 2 | Marco principal de sistema/ecosistema | VIGENTE |
| ISO/IEC/IEEE 12207:2026 | Publicada, edición 2 | Marco principal de ciclo de vida de software | VIGENTE |
| ISO/IEC/IEEE 29148:2018 | Publicada; confirmada en 2024; nueva DIS en desarrollo | Ingeniería de requisitos | VIGENTE; monitorizar sucesora |
| ISO/IEC/IEEE 42010:2022 | Publicada, edición 2 | Descripción de arquitectura | VIGENTE |
| ISO/IEC 25010:2023 | Referencia declarada por el repositorio | Modelo de calidad de producto | REQUIERE VERIFICACIÓN EXTERNA COMPLEMENTARIA |
| NIST SP 800-218 / SSDF 1.1 | Referencia NIST declarada | Desarrollo seguro | VIGENTE COMO MARCO NIST DECLARADO |
| ISO 31000:2018 | Referencia declarada | Gestión general de riesgos | REQUIERE VERIFICACIÓN EXTERNA COMPLEMENTARIA |
| IEC 31010:2019 | Referencia declarada | Técnicas de evaluación de riesgos | REQUIERE VERIFICACIÓN EXTERNA COMPLEMENTARIA |
| ISO/IEC 42001:2023 | Referencia declarada | Sistema de gestión de IA | REQUIERE VERIFICACIÓN EXTERNA COMPLEMENTARIA |
| ISO/IEC 23894:2023 | Referencia declarada | Riesgos de IA | REQUIERE VERIFICACIÓN EXTERNA COMPLEMENTARIA |
| NIST AI RMF 1.0 | Referencia declarada | Gestión de riesgos de IA | VIGENTE COMO MARCO NIST DECLARADO |
| NIST AI 600-1 | Referencia declarada | Riesgos de IA generativa | VIGENTE COMO REFERENCIA COMPLEMENTARIA |
| ISO/IEC 27036-2:2022 | Referencia declarada | Seguridad de relaciones con proveedores | REQUIERE VERIFICACIÓN EXTERNA COMPLEMENTARIA |
| ISO/IEC 27036-3:2023 | Referencia declarada | Seguridad de supply chain | REQUIERE VERIFICACIÓN EXTERNA COMPLEMENTARIA |
| ISO/IEC 27036-4:2016 | Referencia declarada | Relaciones con proveedores cloud | REQUIERE VERIFICACIÓN EXTERNA COMPLEMENTARIA |

## 4. Hallazgo crítico: ISO/IEC/IEEE 12207

El repositorio ya utiliza **ISO/IEC/IEEE 12207:2026** en `02-Standards-Lifecycle-Matrix.md` y `00-Software-Lifecycle-Master.md`.

La fuente oficial ISO confirma que:

- ISO/IEC/IEEE 12207:2026 fue publicada en abril de 2026 como edición 2.
- La edición anterior ISO/IEC/IEEE 12207:2017 figura como retirada.
- ISO identifica explícitamente a 12207:2026 como la nueva versión.

Por tanto, **12207:2017 no debe mantenerse como referencia normativa vigente del proyecto**.

Si una referencia histórica a 12207:2017 aparece posteriormente en evidencia, auditoría, documentación histórica o contexto de transición, deberá etiquetarse como **HISTÓRICA/REEMPLAZADA** y no como fuente normativa vigente.

## 5. Hallazgo de ciclo de vida de 29148

ISO indica que ISO/IEC/IEEE 29148:2018 continúa siendo la versión publicada vigente, aunque está siendo revisada y existe un DIS en desarrollo.

Por tanto:

- 29148:2018 permanece como referencia normativa publicada utilizada por el repositorio.
- El DIS no debe sustituir a 29148:2018 antes de su publicación oficial.
- La matriz debe conservar una condición de monitorización para la futura edición.

## 6. Regla normativa H-007 propuesta

Toda referencia normativa controlada deberá tener:

```yaml
standard:
  identifier: "ISO/IEC/IEEE 12207"
  edition: "2026"
  status: "current"
  authority: "ISO"
  adopted_by_project: true
  historical_predecessors:
    - "ISO/IEC/IEEE 12207:2017"
  monitoring_required: false
```

Para referencias en transición:

```yaml
status: "current-with-successor-under-development"
```

Para referencias históricas:

```yaml
status: "historical-replaced"
adopted_by_project: false
```

## 7. Regla de actualización

No se cambiará una edición normativa únicamente porque exista un borrador, DIS, CD o proyecto en desarrollo.

La actualización requiere:

1. identificación de la nueva edición oficial;
2. verificación de estado en la fuente del organismo emisor;
3. análisis de impacto sobre procesos y artefactos;
4. decisión documentada;
5. actualización coordinada de la matriz y consumidores;
6. validación;
7. PR y merge controlado.

## 8. Limitación de la auditoría inicial

La búsqueda indexada de código de GitHub no devolvió resultados para términos normativos en este repositorio. Por ello, **no se declara todavía una búsqueda exhaustiva de los 189 artefactos del árbol como completada**.

La evidencia disponible permite verificar los principales artefactos canónicos y las referencias normativas explícitas de ellos, pero queda pendiente un inventario completo de consumidores y referencias distribuidas por todos los artefactos.

Esto se registra como deuda de H-007 y no se resuelve por inferencia.

## 9. Resultado

**H-007 — primera capa: PARCIALMENTE RESUELTO.**

Se confirma que las referencias principales del Governance Core ya están alineadas con 12207:2026 y 15288:2023, y que 29148:2018 debe mantenerse mientras su sucesora continúe en desarrollo.

Permanece abierta la verificación exhaustiva de referencias distribuidas y la formalización de un registro normativo único.

## 10. Fuentes externas de verificación

- ISO/IEC/IEEE 12207:2026 — https://www.iso.org/standard/90219.html
- ISO/IEC/IEEE 12207:2017 — https://www.iso.org/standard/63712.html
- ISO/IEC/IEEE 15288:2023 — https://www.iso.org/standard/81702.html
- ISO/IEC/IEEE 29148:2018 — https://www.iso.org/standard/72089.html
- ISO/IEC/IEEE DIS 29148 — https://www.iso.org/standard/94091.html
- ISO/IEC/IEEE 42010:2022 — https://www.iso.org/standard/74393.html

## 11. Próximo cambio controlado

El siguiente commit de esta rama deberá convertir esta auditoría en un mecanismo persistente de control de versiones normativas, sin afirmar conformidad normativa por el mero hecho de mantener referencias actualizadas.
