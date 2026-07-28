# Prueba Técnica — Data Platform Engineer · Habi

Lea primero **Prueba_Data_Platform_Engineer_Habi.docx** y
**fuentes/CATALOGO_DE_FUENTES.md**.

Esta prueba es abierta: **usted elige las fuentes, define el problema y construye la solución.**
Puede usar pocas fuentes o todas: lo importante es que **sustente y documente cada decisión,
proceso y resultado.**

## Estructura sugerida (reorganícela si lo justifica — y explique por qué la organizó así)
```
fuentes/            abanico de fuentes crudas (incluidas) + catálogo de remotas
ingesta/            su código de extracción (a zona raw local)
transformacion/     capas raw -> staging -> consumo (dbt O python/sql, su elección)
contratos/          data contract as code (ejemplo a completar)
arquitectura/       DISEÑO cloud (AWS/GCP) — obligatorio; implementarlo es un plus
analisis/           su hallazgo de negocio (formato libre: reporte/dashboard/notebook/modelo/slides)
```
> **Documente en el README cómo organizó el repositorio y por qué** (convenciones,
> separación de responsabilidades). La organización también se evalúa.

## Definición de capas (explíquela usted)
Debe **definir explícitamente qué significa raw, staging y consumo** en su solución.
No asumimos una definición única; queremos ver su criterio.

## Modelo de consumo: usted elige el paradigma
No es obligatorio un modelo relacional. Puede usar SQL, o NoSQL (clave-valor, documentos,
columnar, grafos) si encaja mejor. **Justifique la elección** según el patrón de consumo.

## Sobre la transformación: dbt es opcional
- Si conoce **dbt**, úselo (plus). Esqueleto en `transformacion/dbt_opcional/`.
- Si no, resuelva por capas en **Python/SQL** (`transformacion/python_alternativa/`).
- Evaluamos estructura por capas + **pruebas** + decisiones documentadas, no la herramienta.

## Cómo se espera que corra (ejemplo)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ingesta/extraer.py       # ingiere fuentes elegidas (incl. al menos 1 remota)
# luego su transformación (dbt build  Ó  python transformacion/python_alternativa/run.py)
```

## Entregables
1. Este repositorio ejecutable + README explicando su organización.
2. Documentación del caso (fuentes, problema, pipeline, definición de capas, arquitectura cloud, trade-offs).
3. Análisis a negocio (formato libre).
4. Sustentación (~30 min) ante el panel.

3 días. Sustente y documente **cada** decisión, proceso y resultado.
