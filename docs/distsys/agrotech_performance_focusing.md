# AgroTechAI: Optimización de Performance en Sistemas Distribuidos de Borde

**Curso:** Sistemas Distribuidos | **Eje:** Performance

**Equipo:** alfa lobo buena maravilla
- Edward Alejandro Rayo Cortes
- Jonathan Sandoval
- Mauricio Andrés Abril Villadiego

**EAFIT 2026-1**

---

## 1. Introducción: El Tópico de Performance

**Definición Técnica**

Performance en sistemas distribuidos es la capacidad de un sistema para ejecutar tareas dentro de restricciones de tiempo, recursos y costo. No es solo "velocidad" - incluye latencia, throughput, utilización y eficiencia energética.

**Dimensiones Clave**

- **Latencia**: Tiempo de respuesta end-to-end (p50, p99)
- **Throughput**: Operaciones por unidad de tiempo
- **Utilización**: % de recursos efectivamente usados
- **Eficiencia**: Output / Recursos consumidos

**Por qué importa en Edge/Fog**

En arquitecturas Edge/Fog, los recursos del **servidor puente** (gateway local) son escasos:
- Un modelo de ML que funciona en cloud con 32GB RAM debe adaptarse a 4GB
- Los dispositivos de borde (sensores, celulares) envían datos al puente para procesamiento local
- El puente debe procesar sin depender de conectividad a la nube [6]

Performance aquí significa **hacer más con menos**, manteniendo baja latencia hacia los dispositivos de borde.


---

## 2. Estado del Arte: AgriTech con IA

**Microsoft FarmBeats** [8]

- Edge computing para agricultura. 
- Usa TV white spaces para conectividad rural. 
- Requiere Azure IoT Hub, sensores propietarios, y configuración cloud. 
- Orientado a grandes operaciones en EE.UU.

**John Deere Operations Center** [9]

- Agricultura de precisión con ML embebido en maquinaria. 
- Hardware propietario ($$$), requiere tractores John Deere, conectividad satelital. 
- Costo: $15,000+ USD por implementación básica.

**AWS IoT Greengrass + SageMaker** [10]

- ML en el borde con gestión cloud. 
- Requiere cuenta AWS
- Dependencia de internet para deployment/updates
- Modelo pay-per-use. Latencia de gestión: depende de conectividad.

**Climate FieldView (Bayer)** [11]

- Predicción de cultivos SaaS. 
- Datos enviados a cloud para procesamiento. 
- Suscripción anual ~$1,000+ USD. 
- Disponible en 23 países
- Enfocado en maíz/soja en grandes extensiones (220M+ acres).

---

## 2.1 Estado del Arte: AWS IoT, Arquitectura de referencia

Esta es una **arquitectura de referencia** para una granja conectada que integra sensores IoT, visión por computadora e inferencia de machine learning en el borde, utilizando servicios de AWS para escalabilidad, análisis y visualización.

<figure style="text-align:center;">
  <img src="arquitectura_amazon_green.png" alt="Arquitectura de smart farm" />
  <figcaption>Imagen tomada de <a href="https://docs.aws.amazon.com/architecture-diagrams/latest/smart-farm-on-aws/smart-farm-on-aws.html">https://docs.aws.amazon.com/architecture-diagrams/latest/smart-farm-on-aws/smart-farm-on-aws.html</a></figcaption>
</figure>

**Componentes**

1. **Sensores y drones**: Dispositivos sin FreeRTOS envían datos mediante **AWS Lambda** (conversión de protocolos).
2. **Sensores con FreeRTOS**: Se conectan a **AWS IoT Greengrass** para operar con conectividad intermitente.
3. **Ingesta desde borde**: **Greengrass** transmite datos a **Kinesis Data Streams**.
4. **Video en tiempo real**: Streaming y reproducción con **Kinesis Video Streams**.
5. **Procesamiento y notificaciones**: Análisis en tiempo real con **Apache Flink** y alertas vía **Amazon SNS**.
6. **Almacenamiento y análisis**: **Amazon S3** como data lake y **OpenSearch** para consultas.
7. **Integración empresarial**: Conexión segura de datos locales mediante **Direct Connect**.
8. **Acceso seguro externo**: Consumo privado de datos con **PrivateLink**.
9. **Interfaces y visualización**: APIs con **API Gateway** y dashboards con **QuickSight**.
10. **Machine Learning en el borde**: Modelos con **SageMaker** y etiquetado con **Ground Truth**.
11. **Catálogo y consultas**: **Glue** para esquema y catálogo; **Athena** para consultas SQL.
12. **Seguridad centralizada**: Monitoreo con **IoT Device Defender** y **Security Hub**.


---

## 3. Brecha: ¿Por qué no funcionan en Colombia?

**Problema de Conectividad**

- El 60% de zonas rurales colombianas tiene conectividad intermitente o nula [7]. 
- Soluciones cloud-dependent pueden fallar cuando más se necesitan [3]: durante la temporada de cultivo en campo.

**Problema de Costo**

- PIB per cápita agrícola colombiano: ~$3,500 USD/año. 
- Hardware John Deere ($15K+) o suscripciones SaaS ($1K+/año) son inviables para pequeños agricultores (70% del sector).

**Problema de Escala**

- Soluciones diseñadas para farms de 1,000+ hectáreas. 
- Finca promedio colombiana: 5-20 hectáreas. 
- El ROI de soluciones enterprise no aplica.

**Gap Identificado**

Se necesita: 
- IA local 
- Hardware económico (<$500)
- Sin dependencia cloud
- Para pequeña/mediana agricultura tropical.


---

## 4. Caso: AgroTechAI - Nuestra Propuesta

**Qué es AgroTechAI**

Sistema de monitoreo agrícola con IA que analiza imágenes de cultivos en tiempo real. Usa LLMs multimodales locales (Ollama) para diagnóstico. Arquitectura **Fog**: procesa en el servidor puente y sincroniza con la nube cuando hay conectividad. Puede operar en **modo local** sin dependencia de cloud.

**Diferenciadores vs Estado del Arte**

| Aspecto | Soluciones Existentes | AgroTechAI |
|---------|----------------------|------------|
| Conectividad | Requiere internet constante | Fog (intermitente) o 100% offline |
| Costo hardware | $1,000 - $15,000+ | ~$200 (mini PC como servidor puente) |
| Modelo de pago | Suscripción/licencia | Open source |
| Procesamiento | Cloud obligatorio | Servidor puente + nube opcional |
| Dispositivos borde | Sensores propietarios | Celular + sensores estándar |
| Flexibilidad | Una sola configuración | Modo Fog o Modo Local |

**Arquitectura Multi-Agente**

4 agentes coordinados via WebSocket local: 
- ImageVision
- AgriVision
- SoilSense
- CropMaster

---


## 5. El Problema de Performance

**Conflicto Fundamental**

- Los LLMs requieren recursos intensivos (RAM, CPU, GPU).
- La inferencia de un modelo de 4B parámetros puede consumir 8-16GB RAM. 
- En Edge, típicamente tenemos 2-8GB totales.

**Conectividad e infraestructura:**
- Zonas rurales con coberturas inestables e interrumpidas de internet y señal móvil.
- Compatibilidad y sincronización entre los recursos físicos y el software (Heterogeneidad).

**Métricas del Problema**

- Modelos LLM típicos (4B+ params) → ~8GB RAM mínimo
- Raspberry Pi 4 → 4-8GB RAM total
- Mini PC económico → 8-16GB RAM total
- **Solución**: Modelos optimizados para Fog (moondream ~2GB, gemma3:270m ~1GB)

**Trade-off Identificado**

- Calidad del modelo (parámetros) vs. Recursos disponibles vs. Latencia de respuesta. 
  - No podemos maximizar las tres simultáneamente.
- Reducción del impacto ambiental al optimizar recursos y procesos.


---

## 6. Solución: Arquitectura Consolidada

**Decisión 1: Consolidación de Servicios**

En lugar de contenedores aislados (Ollama + API + Frontend + Nginx), consolidamos todo en un solo contenedor gestionado por Supervisord. 
Eliminamos overhead de red virtual entre servicios.

**Decisión 2: Modelos Optimizados para Fog**

- Producción usa:
  - `moondream` (~1.8B parámetros) para análisis de imágenes (ImageVision)
  - `gemma3:270m` (270M parámetros) para análisis de texto (AgriVision, SoilSense, CropMaster)
- Reducción significativa en RAM: de ~8GB a ~3GB total.

**Configuración de Producción**

```yaml
resources:
  limits:
    memory: 4G    # Total para todo el sistema
    cpus: '2.0'
  reservations:
    memory: 1G
```

---

## 6.1 Modos de Deployment: Fog vs Local

**Modo Fog (Default)** - Servidor puente sincroniza con la nube

```
┌──────────────┐      ┌────────────────┐      ┌──────────────┐
│    BORDE     │      │    PUENTE      │      │    NUBE      │
│              │      │                │      │              │
│  - Sensores  │ ───► │  - Ollama      │ ◄──► │  - Sync      │
│  - Celular   │      │  - FastAPI     │      │  - Updates   │
│  - Cámara    │      │  - Nginx       │      │  - CI/CD     │
│              │      │  (mini PC)     │      │  - Backups   │
└──────────────┘      └────────────────┘      └──────────────┘
     WiFi local            4GB RAM              Conectividad
                                                intermitente
```

**Modo Local** - Cliente/Servidor sin nube (cuando no hay conectividad)

```
┌──────────────┐      ┌────────────────┐
│    BORDE     │      │    PUENTE      │       ✗ Sin nube
│              │      │                │
│  - Sensores  │ ───► │  - Ollama      │       ⚠ Trade-offs:
│  - Celular   │      │  - FastAPI     │       - Updates manuales
│  - Cámara    │      │  - Nginx       │       - Backups locales
│              │      │  (mini PC)     │       - Soporte presencial
└──────────────┘      └────────────────┘
     WiFi local            4GB RAM
```

**Flexibilidad arquitectónica**: El mismo sistema soporta ambos modos según las condiciones de conectividad y recursos disponibles.


---


## 6.2 AgroTechAI: Arquitectura enfocada al rendimiento

| Multi-contenedor (aislado) | Consolidado (producción) |
|---------|----------------------|
| <img src="agrotechai_dev.jpeg" /> | <img src="agrotechai_pdn.png" /> |

---

## 7. Implementación Técnica: Supervisord

**Por qué Supervisord como PID 1**

- Gestión unificada del ciclo de vida de procesos co-ubicados.
- Un solo punto de control para: Nginx, FastAPI, Ollama, Model-Puller.

**Orden de Inicio (Priority) - Configuración Real**

| Programa | Comando | Priority | AutoRestart | Reintentos |
|----------|---------|----------|-------------|------------|
| Ollama | `/usr/bin/ollama serve` | 50 | Sí | 5 |
| Model-Puller | `/usr/local/bin/pull-models.sh` | 200 | No | 3 |
| FastAPI | `python3 main.py` | 300 | Sí | 5 |
| Nginx | `nginx -g "daemon off;"` | - | Sí | 5 |

**Beneficio de Performance**

- Comunicación localhost (`127.0.0.1:5000`) en lugar de red Docker bridge
- Latencia inter-servicio: ~0.1ms vs ~1-2ms (reducción 20x)
- Logs centralizados: `/var/log/supervisor/` con rotación a 10MB


---

## 8. Implementación Técnica: Health Checks

**Problema: Fallos Parciales [2]**

En contenedor consolidado, si un proceso falla, el contenedor sigue "vivo" pero disfuncional. Kubernetes/Docker no detectan el fallo parcial. Como señala Kleppmann, en sistemas distribuidos los fallos parciales son más peligrosos que los totales.

**Solución: Health Check Compuesto (Implementación Real)**

```python
@app.get("/health")
async def health_check():
    ollama_status = check_ollama_connection()  # Timeout: 5s
    status = "healthy" if ollama_status else "error"
    return {"status": status, "ollama": ollama_status, "model": MODEL_NAME}

def check_ollama_connection() -> bool:
    response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
    return response.status_code == 200
```

**Probes en Kubernetes (Configuración Real)**

| Probe | Initial Delay | Period | Timeout | Retries | Propósito |
|-------|---------------|--------|---------|---------|-----------|
| Startup | 30s | 10s | 5s | 12 | Espera carga modelo (~2 min) |
| Readiness | 45s | 10s | 5s | 3 | Controla tráfico |
| Liveness | 60s | 30s | 10s | 3 | Reinicia si falla |

**Impacto en MTTR (Mean Time To Recovery)**

- Detección de fallo: máx 30s (liveness period)
- Reinicio contenedor: ~5-10s
- Carga modelo: ~60-90s
- **MTTR total estimado: < 2 minutos**


---

## 9. Resultados: Configuración de Producción

**Recursos del Servidor Puente (Valores Reales)**

| Aspecto | Valor | Notas |
|---------|-------|-------|
| **RAM Total** | **4GB** (reserva: 1GB) | Suficiente para mini PC económico |
| **CPU Total** | **2.0 cores** | CPU-only, sin GPU |
| Modelo Visión | moondream (~1.8B) | Para ImageVision |
| Modelo Texto | gemma3:270m (~270M) | Para AgriVision, SoilSense, CropMaster |
| Contenedores | 1 consolidado | Supervisord como PID 1 |
| Latencia objetivo | < 180s | CTQ para diagnóstico completo |

**Configuración de Pool de Conexiones (Ollama Client)**

```python
# Configuración real para manejo eficiente de requests
pool_connections = 20    # Conexiones en pool
pool_maxsize = 50        # Máximo pool
max_retries = 3          # Reintentos con backoff
timeout = 60             # Timeout por request (segundos)
```

**Implicación**

La consolidación y selección de modelos optimizados permiten deployment en hardware de servidor puente real (mini PC ~$200 USD) con solo **4GB RAM** y **2 CPU cores**, que actúa como gateway entre los dispositivos de borde (sensores, celulares) y procesa la inferencia de IA localmente.


---

## 10. Resultados: Métricas de Rendimiento

**Parámetros de Ollama Optimizados**

```yaml
OLLAMA_NUM_PARALLEL=6      # Requests paralelos
OMP_NUM_THREADS=6          # Threads OpenMP
OLLAMA_FLASH_ATTENTION=1   # Atención optimizada
OLLAMA_MAX_LOADED_MODELS=2 # Modelos en memoria
```

**Variables Predictoras de Performance [1]**

- Tiempo de CPU explica **70% de varianza** en latencia
- Lecturas de disco: predictor secundario clave
- RAM asignada: rendimiento decrece con over-provisioning (>3.24%)

**CTQ (Critical To Quality)**

Latencia p99 < 180s para diagnóstico de imagen en campo.

---

## 10.1 Resultados: Autoescalado y Métricas Operativas

**Horizontal Pod Autoscaler (HPA) - Configuración Real**

```yaml
minReplicas: 1
maxReplicas: 5
metrics:
  - cpu: targetUtilization 70%
  - memory: targetUtilization 80%
behavior:
  scaleDown:
    stabilizationWindowSeconds: 300  # 5 min estabilización
    policies:
      - type: Percent, value: 50, periodSeconds: 60
  scaleUp:
    stabilizationWindowSeconds: 0    # Inmediato
    policies:
      - type: Percent, value: 100, periodSeconds: 30
```

**Parámetros de Generación LLM Optimizados**

| Parámetro | Valor | Propósito |
|-----------|-------|-----------|
| temperature | 0.7 | Balance creatividad/precisión |
| top_p | 0.9 | Diversidad controlada |
| num_predict | 300 | Máx tokens respuesta |
| timeout | 60s | Límite por request |

**Resultados del Benchmark con Imagen (5 requests)**

| Métrica | Valor Medido |
|---------|--------------|
| p50 | 18,675ms (~19s) |
| p90 | 48,517ms (~49s) |
| **p99** | **48,517ms (~49s)** |
| Promedio | 24,904ms (~25s) |
| Tasa éxito | 100% |

**Latencia por Agente - Con Imagen (promedios)**

| Agente | Latencia | Función |
|--------|----------|---------|
| ImageVision | 13,231ms | Análisis de imagen (moondream) |
| AgriVision | 6,944ms | Salud del cultivo (gemma3:270m) |
| SoilSense | 6,944ms | Condiciones ambientales (gemma3:270m) |
| CropMaster | 0.1ms | Decisión final (gemma3:270m) |

---

**Resultados del Benchmark Solo Sensores (5 requests, sin imagen)**

Escenario alternativo: análisis basado únicamente en datos de sensores (texto), sin procesamiento de imagen. Usa solo AgriVision, SoilSense y CropMaster.

| Métrica | Valor Medido |
|---------|--------------|
| p50 | 8,653ms (~9s) |
| p90 | 9,299ms (~9s) |
| **p99** | **9,299ms (~9s)** |
| Promedio | 8,854ms (~9s) |
| Tasa éxito | 100% |

**Latencia por Agente - Solo Sensores (promedios)**

| Agente | Latencia | Función |
|--------|----------|---------|
| AgriVision | 4,367ms | Salud del cultivo (gemma3:270m) |
| SoilSense | 4,367ms | Condiciones ambientales (gemma3:270m) |
| CropMaster | 0.11ms | Decisión final (gemma3:270m) |

**Comparación: Con Imagen vs Solo Sensores**

| Escenario | p99 Latencia | Throughput | Uso Principal |
|-----------|--------------|------------|---------------|
| Con Imagen | 49s | 2.4/min | Diagnóstico visual de cultivos |
| Solo Sensores | **9s** | **6.8/min** | Monitoreo continuo, alertas rápidas |

> **Insight**: El análisis de solo sensores es **5.3x más rápido** que el análisis con imagen, ideal para monitoreo continuo donde no se requiere diagnóstico visual.

---

**Validación del CTQ**

| Métrica | Objetivo | Con Imagen | Solo Sensores | Estado |
|---------|----------|------------|---------------|--------|
| Latencia diagnóstico | < 180s | p99 = 49s | p99 = 9s | **CUMPLE** |
| Disponibilidad | > 99% | 100% (5/5) | 100% (5/5) | **CUMPLE** |
| Memoria pico | < 4GB | ~3GB | ~2GB | **CUMPLE** |
| MTTR | < 5 min | Estimado ~2 min | Estimado ~2 min | Diseñado |

---

## 11. Sustentación: Por qué responde a Performance

**Tesis Central**

Performance no es solo hacer cosas rápido, es hacer cosas eficientemente dentro de restricciones. AgroTechAI demuestra optimización de performance bajo restricciones severas de recursos, priorizando **MTTR sobre MTBF** [12].

**Técnicas Aplicadas y su Conexión Teórica**

| Técnica | Impacto | Referencia |
|---------|---------|------------|
| Consolidación de servicios | Elimina overhead virtualización (1-2.4%) | Lloyd et al. [1] |
| Modelos optimizados para Fog | moondream + gemma3:270m → ~3GB RAM, p99 ~49s | - |
| Comunicación localhost | Reduce latencia inter-servicio 20x | Aldossary [5] |
| Health checks compuestos | Detecta fallos parciales | Kleppmann [2] |
| Priorización MTTR | Recuperación < 2 min vs. infalibilidad | [12] |

**Conexión con Teoría de Sistemas Distribuidos**

1. **Fallos Parciales [2]**: En sistemas consolidados, un componente puede fallar mientras el contenedor reporta "healthy". Los health checks compuestos (FastAPI → Ollama) detectan esta condición.

2. **Estabilidad como Filtro de Eficiencia [5]**: Al priorizar nodos estables (alto uptime), los costos de migración de VMs se vuelven irrelevantes. El servidor puente mantiene alta permanencia.

3. **El "Depende" como Axioma [3]**: No existen soluciones universales. Para Edge con recursos limitados, consolidación gana. Para Cloud con recursos abundantes, aislamiento gana.

4. **Renovabilidad de Métricas [12]**: En entornos rurales con reparaciones precarias, el MTBF histórico pierde validez. Por eso priorizamos CTQ basado en comportamiento (latencia, consumo) sobre predicciones estadísticas.


---

## 12. Ventajas de la Arquitectura

**Operacionales**

- Deployment simplificado: una imagen, un contenedor
- Menor superficie de ataque: menos puntos de entrada
- Recuperación automática: Supervisord + health checks

**De Performance**

- Latencia predecible: sin variabilidad de red virtual
- Utilización eficiente: recursos compartidos sin overhead
- Escalamiento vertical simple: aumentar límites del contenedor

**De Costo**

- Hardware más económico: funciona en mini PC de ~$200 USD
- Menor consumo energético: menos procesos de orquestación
- Sin licencias: stack completamente open source


---

## 13. Riesgos y Limitaciones

**Riesgo 1: Punto Único de Fallo**

Consolidación = si el contenedor cae, todo cae. Mitigación: health checks agresivos + restart policies + réplicas en Kubernetes.

**Riesgo 2: Escalamiento Horizontal Limitado**

No puedes escalar solo el LLM o solo la API. Mitigación: en modo Fog, la nube puede absorber picos de demanda.

**Riesgo 3: Calidad del Modelo**

Modelos pequeños (moondream, gemma3:270m) son menos capaces que modelos grandes. Mitigación: prompts optimizados + validación humana para casos críticos.

**Riesgo 4: Costos Operativos en Modo Local**

Cuando se despliega **sin conexión a la nube** (modo cliente/servidor local), se transfieren responsabilidades al operador:
- Actualización manual de modelos (sin CI/CD automatizado)
- Mantenimiento físico del servidor puente
- Gestión de backups y recuperación ante desastres
- Soporte técnico debe ser presencial

> En **modo Fog**, estos costos se mitigan mediante sincronización y gestión remota.

Mitigación modo local: Capacitación a cooperativas + documentación + scripts simplificados.

**Limitación Honesta**

Esta arquitectura optimiza para recursos limitados, no para throughput máximo. No es la solución para 10,000 requests/segundo.


---

## 14. Trade-offs Explícitos

**Trade-off 1: Recursos (Consolidación vs Aislamiento)**

| Lo que Ganamos | Lo que Perdemos |
|----------------|-----------------|
| Funcionamiento en 4GB RAM | Flexibilidad de escalar componentes independientes |
| Latencia inter-servicio ~0.1ms | Capacidad de modelos más grandes |
| Deployment de una sola imagen | Facilidad de debugging (procesos co-ubicados) |
| Solo 2 CPU cores requeridos | Aislamiento entre servicios |

**Trade-off 2: Modo Fog vs Modo Local**

| Aspecto | Modo Fog (Default) | Modo Local |
|---------|-------------------|------------|
| Conectividad | Requiere intermitente | No requiere |
| Actualización modelos | Automática (CI/CD) | Manual |
| Backups | Sincronizados a nube | Responsabilidad local |
| Soporte técnico | Remoto posible | Presencial requerido |
| Costos cloud | Suscripción/uso | $0 |
| Datos | Pueden sincronizarse | Nunca salen de la finca |

**¿Quién asume el costo operativo?**

| Modo | Responsable |
|------|-------------|
| **Fog** | Compartido: nube absorbe sincronización, CI/CD, backups |
| **Local** | Operador local: cooperativa, técnico agrícola, agricultor |

**El "Depende"**

La elección del modo depende del contexto:
- **Conectividad disponible** → Modo Fog aprovecha sincronización
- **Sin conectividad / datos sensibles** → Modo Local es viable
- **Capacidad técnica local** → Factor decisivo para modo Local

---

## 15. Conclusiones

**Hallazgo Principal**

La consolidación de servicios con modelos optimizados (moondream + gemma3:270m) permite ejecutar sistemas de IA en servidores puente con **4GB RAM** y **2 CPU cores**, cumpliendo el CTQ de latencia **p99 < 180s**:
- **Con imagen**: p99 = 49s (diagnóstico visual completo)
- **Solo sensores**: p99 = 9s (monitoreo continuo, **5.3x más rápido**)

**Resultados Validados**

| Métrica | Objetivo | Con Imagen | Solo Sensores |
|---------|----------|------------|---------------|
| Latencia p99 | < 180s | 49s | 9s |
| Tasa de éxito | > 99% | 100% | 100% |
| RAM | < 4GB | ~3GB | ~2GB |
| Throughput | - | 2.4/min | 6.8/min |

**Lecciones de Performance**

1. **Modelo pequeño + hardware disponible > modelo grande + hardware inexistente**
2. **Latencia de red virtual es costo oculto**: Docker bridge añade ~2ms vs ~0.1ms localhost
3. **Health checks compuestos son críticos**: Detectan fallos parciales que Kubernetes no ve
4. **MTTR sobre MTBF** [12]: En entornos rurales, priorizar recuperación rápida sobre infalibilidad
5. **Selección de modelos importa**: moondream + gemma3:270m logran balance calidad/velocidad
6. **Dos modos de operación**: Análisis con imagen para diagnóstico visual, solo sensores para monitoreo continuo (5.3x más rápido)

**El Axioma del "Depende"**

La arquitectura óptima depende del contexto [3]:
- **Recursos limitados**: Consolidación en servidor puente gana
- **Conectividad disponible**: Modo Fog aprovecha sincronización con nube
- **Sin conectividad**: Modo Local viable con trade-offs operativos
- **Capacidad técnica local**: Factor decisivo para viabilidad del modo Local

**Aplicabilidad**

Patrón replicable para cualquier aplicación de ML en arquitectura Fog:
- IoT industrial con gateway local + sincronización cloud
- Visión por computador en campo con backup a nube
- NLP (Procesamiento de Lenguaje Natural) embebido con actualizaciones remotas
- Sistemas que requieren operar offline pero beneficiarse de conectividad cuando existe


---

## 16. Bibliografía (Formato IEEE)

[1] W. Lloyd, S. Pallickara, O. David, J. Lyon, M. Arabi, and K. Rojas, "Performance implications of multi-tier application deployments on Infrastructure-as-a-Service clouds," *Future Generation Computer Systems*, vol. 29, no. 5, pp. 1254-1264, 2013.

[2] M. Kleppmann, *Designing Data-Intensive Applications*. O'Reilly Media, 2017.

[3] K. Kingsbury (Aphyr), "Distributed Systems Class," 2021. [Online]. Available: https://github.com/aphyr/distsys-class

[4] AgroTechAI Team, "AgroTechAI: AI-driven crop care suggestions," 2024. [Online]. Available: https://github.com/AgroTechCoAI/AgroTechAI

[5] M. Aldossary, "A Review of Dynamic Resource Management in Cloud Computing," *SN Computer Science*, vol. 2, no. 4, 2021.

[6] A. Luntovskyy, M. Klymash, *Fog Computing and Cloud Computing*, 2019.

[7] MinTIC Colombia, "Informe de Conectividad Rural," 2023. [Online]. Available: https://mintic.gov.co/

[8] Microsoft Research, "FarmBeats: An IoT Platform for Data-Driven Agriculture" 2019. [Online]. Available: https://www.microsoft.com/en-us/research/wp-content/uploads/2017/03/FarmBeats-webpage-1.pdf

[9] John Deere, "Operations Center: Precision Agriculture," 2024. [Online]. Available: https://www.deere.com/

[10] Amazon Web Services, "Smart Farm on AWS: Architecture for Agricultural IoT," 2024. [Online]. Available: https://docs.aws.amazon.com/architecture-diagrams/latest/smart-farm-on-aws/smart-farm-on-aws.html

[11] Bayer Crop Science, "Climate FieldView: Digital Farming Platform," 2024. [Online]. Available: https://www.bayer.com/en/agriculture/digital-farming

[12] E. A. Rayo Cortés, "Análisis de Disponibilidad y Resiliencia en Sistemas de Monitoreo Agrícola," EAFIT, 2026. Análisis interno del proyecto AgroTechAI sobre MTBF, MTTR y renovabilidad de métricas en contexto rural colombiano.

---
