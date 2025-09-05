## **1) Arquetipo: Agrónomo/a asesor/a independiente**

### Especificación A — Priorización por Umbrales y Severidad (offline)

#### 1. Síntesis de Oportunidades (Extraído de los Mapas)
- **Dolor:** Desorden al decidir qué lote visitar primero tras lluvias, con señal inestable.
  - **Oportunidad:** Ranking local por severidad/urgencia que funcione sin conectividad.
- **Dolor:** Falta de criterios homogéneos entre subregiones/cultivos.
  - **Oportunidad:** Umbrales configurables por subregión/cultivo.
- **Dolor:** Tiempo perdido en traslados por rutas poco eficientes.
  - **Oportunidad:** Orden sugerido que reduzca traslados (lista y ruta básica offline).
- **Dolor:** Ansiedad por tomar decisiones con evidencia incompleta.
  - **Oportunidad:** Score que integre historial, clima reciente y síntomas observados.

#### 2. Borrador de Especificación Funcional
**ID:** AGR-PRIO-001  
**Nombre:** Priorización por Umbrales y Severidad (offline)

**Resumen (User Story):**  
Como agrónomo/a, quiero ver un ranking de lotes por severidad/urgencia, incluso sin señal, para decidir rápidamente a dónde ir primero.

**Trigger:** El/la agrónomo/a abre la vista “Prioridad”.  
**Precondiciones:** Hay lotes registrados con datos mínimos (cultivo, última observación, ubicación).  
**Flujo Principal:**
1. App calcula score local (síntomas, tiempo desde última visita, clima reciente si está cacheado).
2. Muestra lista priorizada (alto/medio/bajo) y tiempo recomendado de atención.
3. Permite filtrar por subregión/cultivo y ver detalles del porqué del score.
4. Opción de “fijar” manualmente prioridades.

**Flujos Alternativos:**
- **A1 (sin datos climáticos cacheados):** se calcula score sin clima, con aviso “clima no disponible”.
- **A2 (lotes sin datos mínimos):** se muestran al final con etiqueta “incompleto”.

**Reglas de Negocio:**
- Score = f(severidad observada, tiempo en cola, historial de eventos) con pesos configurables.
- Cambios de umbral recalculan ranking en el dispositivo.

**Criterios de Aceptación:**
- Dado que no hay señal, cuando abro “Prioridad”, entonces veo ranking sin errores en <2 s para 100 lotes.
- Dado un cambio de umbral, cuando guardo, entonces la lista se recalcula localmente y persiste.

---

### Especificación B — Captura Guiada con Mejora de Imagen (baja luz)

#### 1. Síntesis de Oportunidades
- **Dolor:** Fotos poco útiles por baja iluminación/encuadre.
  - **Oportunidad:** Guías de encuadre y mejora automática offline.
- **Dolor:** Frustración por diagnósticos inciertos por mala evidencia.
  - **Oportunidad:** Check de calidad en tiempo real con feedback inmediato.
- **Dolor:** Pérdida de tiempo repitiendo capturas.
  - **Oportunidad:** Guardado local y sugerencias contextuales (macro, distancia).

#### 2. Borrador de Especificación Funcional
**ID:** AGR-CAM-002  
**Nombre:** Captura Guiada con Mejora de Imagen

**User Story:**  
Como agrónomo/a, quiero ayuda para encuadrar y mejorar fotos en baja luz para generar evidencia útil.

**Trigger:** Se abre la cámara desde un lote/caso.  
**Precondiciones:** Lote seleccionado; almacenamiento suficiente.  
**Flujo Principal:**
1. Superposición de guías (distancia/ángulo/zona de enfoque).
2. Validación de nitidez/iluminación en tiempo real.
3. Captura; mejora local (denoise, sharpen ligero) y guardado.
4. Sugerencia de “foto macro de detalle” y “foto de contexto”.

**Alternativos:**
- **A1 (memoria baja):** modo “lite” (resolución reducida).
- **A2 (cámara fallida):** entrada manual de observaciones + posibilidad de añadir fotos luego.

**Reglas de Negocio:**
- Umbral mínimo de nitidez; si no se alcanza, mostrar aviso y permitir continuar bajo responsabilidad.

**Criterios de Aceptación:**
- Dado baja luz, cuando capturo, entonces la app mejora la imagen y advierte si la nitidez es insuficiente.
- Dado “modo lite”, cuando guardo, entonces el tamaño promedio por foto ≤ 300 KB.

---

### Especificación C — Reporte Georreferenciado (PDF/imagen)

#### 1. Síntesis de Oportunidades
- **Dolor:** Armado manual de informes (WhatsApp/Excel) consume horas.
  - **Oportunidad:** Generación 1-click de PDF/imagen comprimido.
- **Dolor:** Clientes/cooperativas exigen trazabilidad (fecha, GPS, fotos).
  - **Oportunidad:** Plantilla con metadatos y evidencia estandarizada.
- **Dolor:** Señal intermitente para envío inmediato.
  - **Oportunidad:** Generar offline y compartir cuando haya conectividad.

#### 2. Borrador de Especificación Funcional
**ID:** AGR-REP-003  
**Nombre:** Reporte Georreferenciado (PDF/imagen)

**User Story:**  
Como agrónomo/a, quiero generar un reporte con fotos, fecha y ubicación para compartir por WhatsApp.

**Trigger:** Botón “Generar reporte” en un caso/lote.  
**Precondiciones:** Caso con al menos 1 foto y ubicación.  
**Flujo Principal:**
1. Selección de plantilla (genérica o cliente).
2. Render local del reporte (portada, mapa, fotos, notas, fecha/hora).
3. Compresión y guardado; opción “Compartir”.

**Alternativos:**
- **A1 (sin GPS):** marcar “ubicación no disponible”; permitir añadir punto manual.
- **A2 (sin fotos):** permitir reporte textual con advertencia.

**Reglas de Negocio:**
- Tamaño final objetivo ≤ 2 MB; fuentes embebidas y numeración de páginas.

**Criterios de Aceptación:**
- Dado un caso completo, cuando genero, entonces obtengo un PDF ≤ 2 MB con metadatos visibles.
- Dado que estoy offline, cuando toco “Compartir”, entonces se encola el envío y se envía al recuperar señal.

## **2) Arquetipo: Administrador/Mayordomo**

### Especificación A — Tablero “Semáforo por Lote” (offline)

#### 1. Síntesis de Oportunidades
- **Dolor:** Dificultad para priorizar lotes en ventanas climáticas cortas.
  - **Oportunidad:** Vista de estado (rojo/amarillo/verde) por lote con acción mínima.
- **Dolor:** Equipos pierden tiempo esperando instrucciones.
  - **Oportunidad:** Acción inmediata (mezcla/EPP) visible por lote.
- **Dolor:** Conectividad limitada en campo.
  - **Oportunidad:** Operación 100% offline con sincronización diferida.

#### 2. Borrador de Especificación Funcional
**ID:** ADM-SEM-001  
**Nombre:** Tablero Semáforo por Lote

**User Story:**  
Como mayordomo, quiero ver el estado de cada lote con la acción sugerida para ejecutar sin demoras.

**Trigger:** Apertura de “Semáforo”.  
**Precondiciones:** Lotes cargados y reglas básicas configuradas.  
**Flujo Principal:**
1. Mostrar tarjetas de lote con color, última actualización y “acción mínima”.
2. Filtros por prioridad/área/cultivo.
3. Tap en un lote → detalle y confirmación de ejecución.

**Alternativos:**
- **A1 (datos incompletos):** lote se marca “incompleto” y se sugiere completar.
- **A2 (conflicto de reglas):** mostrar conflicto y acción por defecto.

**Reglas de Negocio:**
- Rojo: atender <24 h; Amarillo: 48–72 h; Verde: monitoreo.
- Acción mínima siempre visible (mezcla/EPP/observación).

**Criterios de Aceptación:**
- Dado 200 lotes, cuando abro, entonces renderiza en <2 s.
- Dado lote rojo, cuando toco “Marcar en curso”, entonces queda log con fecha/operario.

---

### Especificación B — Planificador de Cuadrillas y Recursos

#### 1. Síntesis de Oportunidades
- **Dolor:** Reprocesos por mala asignación de cuadrillas/equipos.
  - **Oportunidad:** Asignación clara por lote con responsables y tiempos.
- **Dolor:** Falta de visibilidad de EPP/insumos mínimos.
  - **Oportunidad:** Chequeo de disponibilidad antes de asignar.

#### 2. Borrador de Especificación Funcional
**ID:** ADM-PLAN-002  
**Nombre:** Planificador de Cuadrillas y Recursos

**User Story:**  
Como mayordomo, quiero asignar cuadrillas/equipos a lotes priorizados para ejecutar el plan del día.

**Trigger:** Botón “Planificar” en Semáforo.  
**Precondiciones:** Lotes priorizados; cuadrillas registradas.  
**Flujo Principal:**
1. Selección de lote(s) → asignar cuadrilla/equipo/hora.
2. Validación de EPP/insumos mínimos.
3. Confirmar y generar orden de trabajo.

**Alternativos:**
- **A1 (EPP insuficiente):** mostrar alerta y alternativas.
- **A2 (solapamiento de horarios):** sugerir reacomodo automático.

**Reglas de Negocio:**
- Cada cuadrilla no puede estar en dos lotes simultáneamente.
- Log de asignaciones con sello de tiempo.

**Criterios de Aceptación:**
- Dado una cuadrilla, cuando asigno a 3 lotes, entonces se generan 3 órdenes sin solapamientos.
- Dado falta de EPP, cuando confirmo, entonces recibo alerta bloqueante.

---

### Especificación C — Generador de Reporte de Auditoría (antes/después)

#### 1. Síntesis de Oportunidades
- **Dolor:** Consolidar evidencia para auditoría consume tiempo.
  - **Oportunidad:** Reporte “antes/después” con georreferencia y firmas.
- **Dolor:** Formatos distintos por cliente/cooperativa.
  - **Oportunidad:** Plantillas estandarizadas.

#### 2. Borrador de Especificación Funcional
**ID:** ADM-AUD-003  
**Nombre:** Generador de Reporte de Auditoría

**User Story:**  
Como mayordomo, quiero generar un PDF con fotos antes/después y metadatos para auditoría.

**Trigger:** Botón “Reporte auditoría” en lote/orden.  
**Precondiciones:** Evidencias capturadas.  
**Flujo Principal:**
1. Selección de rango (antes/después).
2. Compilación automática (fotos, fecha/hora, GPS).
3. Firma digital (supervisor/operario) y exportar.

**Alternativos:**
- **A1 (sin fotos ‘antes’):** permitir generar con nota de ausencia.
- **A2 (sin GPS):** permitir ubicación manual.

**Reglas de Negocio:**
- Campos obligatorios por plantilla; folio único y QR opcional.

**Criterios de Aceptación:**
- Dado evidencias completas, cuando genero, entonces obtengo PDF ≤ 3 MB con firmas embebidas.
- Dado que no hay señal, cuando guardo, entonces queda en almacenamiento local para envío posterior.

## **3) Arquetipo: Productor mediano (papa / maíz / aguacate Hass)**

### Especificación A — Guía de Diferenciación Rápida (daño mecánico vs. enfermedad)

#### 1. Síntesis de Oportunidades
- **Dolor:** Confusión entre síntomas similares (granizada vs. patógeno).
  - **Oportunidad:** Árbol simple de preguntas + referencia visual.
- **Dolor:** Gastos innecesarios por aplicar sin certeza.
  - **Oportunidad:** Veredicto tentativo con señales observables.

#### 2. Borrador de Especificación Funcional
**ID:** PROD-GUIA-001  
**Nombre:** Guía de Diferenciación Rápida

**User Story:**  
Como productor, quiero distinguir si el daño es mecánico o enfermedad para evitar aplicaciones inútiles.

**Trigger:** Botón “¿Qué es esto?” en un lote.  
**Precondiciones:** Mínimo 1 foto o descripción textual.  
**Flujo Principal:**
1. Preguntas guiadas (3–5) + mini comparativas visuales.
2. Veredicto tentativo (mecánico / probable enfermedad).
3. Próximo paso recomendado (observar X horas, foto de control, etc.).

**Alternativos:**
- **A1 (sin foto):** flujo solo texto con ejemplos.
- **A2 (ambigüedad alta):** sugerir “Tomar muestra/consultar técnico”.

**Reglas de Negocio:**
- Guardar resultado y recomendaciones para seguimiento.

**Criterios de Aceptación:**
- Dado caso típico, cuando completo el flujo, entonces recibo veredicto en <60 s.
- Dado ambigüedad alta, cuando finalizo, entonces se muestra claramente “se requiere verificación”.

---

### Especificación B — Asesor “Aplicar o Esperar”

#### 1. Síntesis de Oportunidades
- **Dolor:** Decidir momento de aplicación con clima incierto.
  - **Oportunidad:** Sugerencia simple aplicar/esperar con breve razón.
- **Dolor:** Miedo a “que no pegue” y perder dinero.
  - **Oportunidad:** Ventana sugerida y recordatorio.

#### 2. Borrador de Especificación Funcional
**ID:** PROD-APES-002  
**Nombre:** Asesor “Aplicar o Esperar”

**User Story:**  
Como productor, quiero una recomendación simple de cuándo aplicar para cuidar el flujo de caja.

**Trigger:** Tras un veredicto de la Guía o desde el lote.  
**Precondiciones:** Diagnóstico tentativo o síntomas declarados.  
**Flujo Principal:**
1. Mostrar “Aplicar/Esperar” con ventana de tiempo y nota breve.
2. Crear recordatorio si se elige “Esperar”.

**Alternativos:**
- **A1 (sin clima cacheado):** mostrar recomendación basada solo en síntomas.
- **A2 (insumos no disponibles):** sugerir alternativa o esperar.

**Reglas de Negocio:**
- Reglas por cultivo/severidad; registro de decisión.

**Criterios de Aceptación:**
- Dado una recomendación “Esperar 24 h”, cuando llega el tiempo, entonces recibo notificación.
- Dado “Aplicar”, cuando confirmo, entonces se registra la decisión y fecha.

---

### Especificación C — Ensayos A/B por Lote + Score Simple

#### 1. Síntesis de Oportunidades
- **Dolor:** “Ensayos caseros” sin método; decisiones por memoria.
  - **Oportunidad:** Plantilla A/B con métricas mínimas y fotos.
- **Dolor:** Dificultad para comunicar resultados.
  - **Oportunidad:** Score simple (↑/→/↓) y panel “Lo que Funciona”.

#### 2. Borrador de Especificación Funcional
**ID:** PROD-ENS-003  
**Nombre:** Ensayos A/B + Score Simple

**User Story:**  
Como productor, quiero comparar prácticas A/B y obtener un score claro para decidir qué mantener## **4) Arquetipo: Técnico agrícola (cooperativa / insumos)**

### Especificación A — Mapa Offline + Score de Riesgo por Caso

#### 1. Síntesis de Oportunidades
- **Dolor:** Pérdida de tiempo por mala planificación de ruta sin señal.
  - **Oportunidad:** Mapa offline con score y orden sugerido.
- **Dolor:** Casos críticos quedan atrás por falta de visibilidad.
  - **Oportunidad:** Ranking por riesgo/tiempo en cola.

#### 2. Borrador de Especificación Funcional
**ID:** TEC-MAPA-001  
**Nombre:** Mapa Offline + Score de Riesgo

**User Story:**  
Como técnico, quiero ver casos en un mapa offline con score para decidir a dónde ir primero.

**Trigger:** Apertura del módulo “Ruta”.  
**Precondiciones:** Casos con ubicación; mapa cacheado.  
**Flujo Principal:**
1. Cargar pines con color por riesgo (alto/medio/bajo).
2. Lista ordenada por score; botón “Orden sugerido”.
3. Guardar ruta del día.

**Alternativos:**
- **A1 (sin mapa cacheado):** vista lista con distancias aproximadas.
- **A2 (caso sin ubicación):** permitir geolocalizar manualmente.

**Reglas de Negocio:**
- Score incluye tiempo en cola, severidad, compromisos (SLAs).

**Criterios de Aceptación:**
- Dado 50 casos, cuando abro, entonces el mapa carga en <2 s offline.
- Dado “Orden sugerido”, cuando confirmo, entonces la ruta queda guardada.

---

### Especificación B — Cámara Modo Lite (compresión + guardado en segundo plano)

#### 1. Síntesis de Oportunidades
- **Dolor:** Cierres de app por memoria baja; pérdida de evidencia.
  - **Oportunidad:** Compresión y guardado en background con reintentos.
- **Dolor:** Subidas fallidas por señal inestable.
  - **Oportunidad:** Cola de subida con resume y modo datos bajos.

#### 2. Borrador de Especificación Funcional
**ID:** TEC-LITE-002  
**Nombre:** Cámara Modo Lite

**User Story:**  
Como técnico, quiero capturar evidencia en modo liviano para que la app no se caiga ni pierda fotos.

**Trigger:** Apertura de cámara desde un caso.  
**Precondiciones:** Caso activo; almacenamiento mínimo disponible.  
**Flujo Principal:**
1. Captura en resolución controlada.
2. Compresión inmediata y guardado local.
3. Encolar subida (si hay señal) o diferir (si no hay).

**Alternativos:**
- **A1 (almacenamiento crítico):** degradar a solo texto/checkbox y 1 foto.
- **A2 (fallo de cámara):** adjuntar fotos desde galería.

**Reglas de Negocio:**
- Tamaño objetivo ≤ 300 KB por imagen; reintentos exponenciales en subida.

**Criterios de Aceptación:**
- Dado 3 fotos seguidas, cuando regreso al caso, entonces están guardadas y visibles.
- Dado que recupero 3G, cuando inicia la cola, entonces las imágenes suben sin intervención.

---

### Especificación C — Motor de Plantillas con Pictogramas y Audio (offline)

#### 1. Síntesis de Oportunidades
- **Dolor:** Barreras de lectura/jerga técnica en capacitaciones.
  - **Oportunidad:** Pasos con pictogramas y audio.
- **Dolor:** Conectividad limitada durante demos en campo.
  - **Oportunidad:** Paquetes descargables y reproducción offline.

#### 2. Borrador de Especificación Funcional
**ID:** TEC-TPL-003  
**Nombre:** Motor de Plantillas con Pictogramas y Audio

**User Story:**  
Como técnico, quiero demos paso a paso con iconografía y audio para enseñar sin depender de lectura ni señal.

**Trigger:** Botón “Demo” → seleccionar plantilla.  
**Precondiciones:** Paquete descargado.  
**Flujo Principal:**
1. Seleccionar cultivo/tema.
2. Reproducir pasos con pictogramas y audio; avanzar “Siguiente”.
3. Registrar finalización y (opcional) feedback rápido.

**Alternativos:**
- **A1 (sin paquete):** sugerir descarga cuando haya señal.
- **A2 (idioma alterno):** cambiar perfil de idioma si está disponible.

**Reglas de Negocio:**
- Plantillas versionadas; compatibilidad hacia atrás.

**Criterios de Aceptación:**
- Dado paquete descargado, cuando inicio, entonces la demo corre fluida sin internet.
- Dado feedback, cuando guardo, entonces queda asociado a la plantilla y fecha.


**Trigger:** Botón “Nuevo ensayo” en lote.  
**Precondiciones:** Definir práctica A y B.  
**Flujo Principal:**
1. Definir A/B (práctica, área, fecha inicio).
2. Capturar 3–5 datos básicos + fotos antes/después.
3. Calcular score y mostrar conclusión sugerida.

**Alternativos:**
- **A1 (datos incompletos):** permitir guardar en borrador.
- **A2 (sin fotos):** score solo con datos numéricos.

**Reglas de Negocio:**
- Score basado en delta entre A y B (rendimiento/daño/costo).

**Criterios de Aceptación:**
- Dado un ensayo con datos, cuando finalizo, entonces obtengo score y recomendación en una pantalla.
- Dado exportación, cuando toco “Compartir”, entonces genero PDF/imagen comprimida.

## **4) Arquetipo: Técnico agrícola (cooperativa / insumos)**

### Especificación A — Mapa Offline + Score de Riesgo por Caso

#### 1. Síntesis de Oportunidades
- **Dolor:** Pérdida de tiempo por mala planificación de ruta sin señal.
  - **Oportunidad:** Mapa offline con score y orden sugerido.
- **Dolor:** Casos críticos quedan atrás por falta de visibilidad.
  - **Oportunidad:** Ranking por riesgo/tiempo en cola.

#### 2. Borrador de Especificación Funcional
**ID:** TEC-MAPA-001  
**Nombre:** Mapa Offline + Score de Riesgo

**User Story:**  
Como técnico, quiero ver casos en un mapa offline con score para decidir a dónde ir primero.

**Trigger:** Apertura del módulo “Ruta”.  
**Precondiciones:** Casos con ubicación; mapa cacheado.  
**Flujo Principal:**
1. Cargar pines con color por riesgo (alto/medio/bajo).
2. Lista ordenada por score; botón “Orden sugerido”.
3. Guardar ruta del día.

**Alternativos:**
- **A1 (sin mapa cacheado):** vista lista con distancias aproximadas.
- **A2 (caso sin ubicación):** permitir geolocalizar manualmente.

**Reglas de Negocio:**
- Score incluye tiempo en cola, severidad, compromisos (SLAs).

**Criterios de Aceptación:**
- Dado 50 casos, cuando abro, entonces el mapa carga en <2 s offline.
- Dado “Orden sugerido”, cuando confirmo, entonces la ruta queda guardada.

---

### Especificación B — Cámara Modo Lite (compresión + guardado en segundo plano)

#### 1. Síntesis de Oportunidades
- **Dolor:** Cierres de app por memoria baja; pérdida de evidencia.
  - **Oportunidad:** Compresión y guardado en background con reintentos.
- **Dolor:** Subidas fallidas por señal inestable.
  - **Oportunidad:** Cola de subida con resume y modo datos bajos.

#### 2. Borrador de Especificación Funcional
**ID:** TEC-LITE-002  
**Nombre:** Cámara Modo Lite

**User Story:**  
Como técnico, quiero capturar evidencia en modo liviano para que la app no se caiga ni pierda fotos.

**Trigger:** Apertura de cámara desde un caso.  
**Precondiciones:** Caso activo; almacenamiento mínimo disponible.  
**Flujo Principal:**
1. Captura en resolución controlada.
2. Compresión inmediata y guardado local.
3. Encolar subida (si hay señal) o diferir (si no hay).

**Alternativos:**
- **A1 (almacenamiento crítico):** degradar a solo texto/checkbox y 1 foto.
- **A2 (fallo de cámara):** adjuntar fotos desde galería.

**Reglas de Negocio:**
- Tamaño objetivo ≤ 300 KB por imagen; reintentos exponenciales en subida.

**Criterios de Aceptación:**
- Dado 3 fotos seguidas, cuando regreso al caso, entonces están guardadas y visibles.
- Dado que recupero 3G, cuando inicia la cola, entonces las imágenes suben sin intervención.

---

### Especificación C — Motor de Plantillas con Pictogramas y Audio (offline)

#### 1. Síntesis de Oportunidades
- **Dolor:** Barreras de lectura/jerga técnica en capacitaciones.
  - **Oportunidad:** Pasos con pictogramas y audio.
- **Dolor:** Conectividad limitada durante demos en campo.
  - **Oportunidad:** Paquetes descargables y reproducción offline.

#### 2. Borrador de Especificación Funcional
**ID:** TEC-TPL-003  
**Nombre:** Motor de Plantillas con Pictogramas y Audio

**User Story:**  
Como técnico, quiero demos paso a paso con iconografía y audio para enseñar sin depender de lectura ni señal.

**Trigger:** Botón “Demo” → seleccionar plantilla.  
**Precondiciones:** Paquete descargado.  
**Flujo Principal:**
1. Seleccionar cultivo/tema.
2. Reproducir pasos con pictogramas y audio; avanzar “Siguiente”.
3. Registrar finalización y (opcional) feedback rápido.

**Alternativos:**
- **A1 (sin paquete):** sugerir descarga cuando haya señal.
- **A2 (idioma alterno):** cambiar perfil de idioma si está disponible.

**Reglas de Negocio:**
- Plantillas versionadas; compatibilidad hacia atrás.

**Criterios de Aceptación:**
- Dado paquete descargado, cuando inicio, entonces la demo corre fluida sin internet.
- Dado feedback, cuando guardo, entonces queda asociado a la plantilla y fecha.
