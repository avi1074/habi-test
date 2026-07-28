# Diseño de arquitectura en la nube (OBLIGATORIO)

Diseñe cómo montaría esta solución en producción sobre **AWS o GCP**.
Implementarla (aunque sea parcial, p. ej. con Terraform o un servicio real) es un **plus**.

Cubra al menos:

## 1. Diagrama de arquitectura
(Incruste una imagen o descríbalo. Flujo del dato de extremo a extremo.)

## 2. Servicios y herramientas — con nombre y justificación
Para cada etapa, qué servicio usaría y **por qué ese y no otro**:
| Etapa | Servicio elegido | Alternativa descartada | Por qué |
|---|---|---|---|
| Almacenamiento raw | | | |
| Procesamiento / transformación | | | |
| Orquestación | | | |
| Almacén de consumo | | | |
| Exposición / API (si aplica) | | | |
| Observabilidad / alertas | | | |

## 3. Actualización de datos y procesos
- **Datos**: ¿batch o streaming? ¿cada cuánto? ¿cómo maneja incrementalidad y reprocesos?
- **Procesos**: versionado, CI/CD, estrategia de despliegue, observabilidad, alertas.

## 4. Trade-offs
Costo, latencia, mantenibilidad y escalabilidad de su diseño.
