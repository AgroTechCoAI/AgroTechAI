## **Resultados: Backlog de Funcionalidades Priorizadas**

### **Arquetipo: Agrónomo/a asesor/a independiente**

---

**Basado en el JTBD #1:**  
> **Cuando** recibo múltiples alertas tras lluvias fuertes y hay baja iluminación y poca señal,  
> **quiero** priorizar rápidamente los lotes críticos con un umbral de acción claro por subregión,  
> **para poder** emitir recomendaciones confiables en 24–48 h y mantener mi reputación.

* **Funcionalidades Propuestas:**

  * **1. Priorización por Umbrales y Severidad (offline)**
    * **User Story:** Como agrónomo, quiero ver un ranking de lotes por severidad/urgencia para poder decidir dónde ir primero incluso sin señal.
    * **Criterio de Aceptación:** Dado que no tengo conectividad, cuando abro la vista de “Prioridad”, entonces veo los lotes ordenados por un score calculado localmente (síntomas, clima reciente, historial).
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Impacta directamente el JTBD (decidir rápido), elimina dolor crítico (tiempo/orden), esencial para el MVP en campo.

  * **2. Captura Guiada con Mejora de Imagen (baja luz)**
    * **User Story:** Como agrónomo, quiero una guía de encuadre y mejora de imagen para poder obtener evidencia útil en condiciones de baja iluminación.
    * **Criterio de Aceptación:** Dado que activo la cámara, cuando enfoco una hoja, entonces la app muestra guías de distancia/ángulo y aplica mejora sin conexión.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Aumenta precisión del diagnóstico y del score; sin buena evidencia, la priorización falla.

  * **3. Mapa Offline y Ruta Óptima por Riesgo**
    * **User Story:** Como agrónomo, quiero una ruta sugerida que minimice traslados y ataque primero los lotes de mayor riesgo.
    * **Criterio de Aceptación:** Dado un conjunto de lotes priorizados, cuando solicito ruta, entonces obtengo un orden recomendado usable sin datos.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Alto valor operativo; no bloquea el MVP si existe la lista priorizada.

  * **4. Reglas de Umbral por Subregión/Cultivo**
    * **User Story:** Como agrónomo, quiero configurar umbrales por subregión y cultivo para adaptar el score a realidades locales.
    * **Criterio de Aceptación:** Dado el panel de configuración, cuando ajusto un umbral, entonces el ranking se recalcula de inmediato.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Aporta precisión y confianza; el MVP puede iniciar con umbrales por defecto.

  * **5. Cola de Sincronización Diferida**
    * **User Story:** Como agrónomo, quiero que evidencias y decisiones se guarden y sincronicen al volver la señal para no perder información.
    * **Criterio de Aceptación:** Dado que estoy offline, cuando registro datos, entonces quedan en cola y se suben automáticamente al recuperar conectividad.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Conveniencia y robustez; el MVP puede operar localmente y exportar manualmente.

---

**Basado en el JTBD #2:**  
> **Cuando** la evidencia de campo es ambigua (pústulas incipientes, daño por granizo parecido a patógeno),  
> **quiero** asistencia en captura/mejora de imagen y pruebas rápidas sugeridas,  
> **para poder** reducir la incertidumbre y evitar gastos innecesarios al productor.

* **Funcionalidades Propuestas:**

  * **1. Asistente de Captura + Checklist de Confirmación**
    * **User Story:** Como agrónomo, quiero un checklist guiado por síntoma para confirmar o descartar hipótesis en minutos.
    * **Criterio de Aceptación:** Dado un síntoma seleccionado, cuando completo el checklist, entonces la app muestra probables causas y próximos pasos.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Resuelve el núcleo del JTBD (reducir ambigüedad); esencial en v1.

  * **2. Comparador Visual de Síntomas (galería offline)**
    * **User Story:** Como agrónomo, quiero comparar mis fotos con una galería curada para identificar diferencias clave.
    * **Criterio de Aceptación:** Dado una foto tomada, cuando abro el comparador, entonces veo imágenes de referencia con anotaciones.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Aumenta certeza y velocidad; el MVP puede vivir con el checklist si hay límite de tiempo.

  * **3. Sugeridor de Pruebas Rápidas de Campo**
    * **User Story:** Como agrónomo, quiero recibir sugerencias de micro-pruebas en campo (p.ej., observación adicional, revisión en horas de luz) para confirmar hallazgos.
    * **Criterio de Aceptación:** Dado un caso ambiguo, cuando solicito validación, entonces obtengo 1–3 pruebas simples con tiempos y criterios de éxito/fallo.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Reduce tratamientos innecesarios; alto valor económico para el productor.

  * **4. Umbrales de Escalamiento a Laboratorio**
    * **User Story:** Como agrónomo, quiero reglas claras de cuándo escalar a laboratorio para evitar sobre/infra-tratamiento.
    * **Criterio de Aceptación:** Dado un score de incertidumbre alto, cuando se cumplan condiciones, entonces la app recomienda enviar muestra y documenta motivo.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Estandariza decisiones críticas; no bloquea la v1 si existe el checklist.

  * **5. Registro de Decisión y Riesgo**
    * **User Story:** Como agrónomo, quiero guardar la decisión tomada con el nivel de riesgo para poder revisar casos y aprender.
    * **Criterio de Aceptación:** Dado el cierre de caso, cuando confirmo la decisión, entonces se registra la opción, evidencia y nivel de riesgo.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Útil para mejora continua; puede esperar a v1.1.

---

**Basado en el JTBD #3:**  
> **Cuando** debo entregar evidencia a clientes o cooperativas,  
> **quiero** generar reportes georreferenciados listos para WhatsApp,  
> **para poder** cerrar casos con trazabilidad sin perder horas en escritorio.

* **Funcionalidades Propuestas:**

  * **1. Reporte Georreferenciado Offline (PDF/imagen)**
    * **User Story:** Como agrónomo, quiero generar un reporte con fotos, mapa y fecha para enviarlo por WhatsApp.
    * **Criterio de Aceptación:** Dado un caso con evidencia, cuando toco “Generar reporte”, entonces obtengo un PDF/imagen comprimido listo para compartir.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Es la salida tangible del trabajo y cierra el ciclo; indispensable para el JTBD.

  * **2. Plantillas de Informe + Marca de Cooperativa/Cliente**
    * **User Story:** Como agrónomo, quiero elegir plantillas (cliente/cooperativa) para cumplir requisitos formales.
    * **Criterio de Aceptación:** Dado que selecciono una plantilla, cuando genero el informe, entonces se aplican logos, campos obligatorios y formato requerido.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Facilita auditorías y consistencia; el MVP puede usar una plantilla genérica.

  * **3. Firma Digital en Campo**
    * **User Story:** Como agrónomo, quiero capturar firmas del productor/testigo en el mismo reporte.
    * **Criterio de Aceptación:** Dado el reporte abierto, cuando solicito firma, entonces se añade la firma con fecha y GPS.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Aumenta trazabilidad y evita reprocesos; no bloquea el envío básico.

  * **4. Control de Versiones y Bitácora**
    * **User Story:** Como agrónomo, quiero mantener historial de versiones del reporte para responder observaciones.
    * **Criterio de Aceptación:** Dado un reporte editado, cuando guardo cambios, entonces se crea una nueva versión con dif y sello de tiempo.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Valor en auditorías; puede llegar en una versión posterior.

  * **5. Exportación a CSV para Seguimiento**
    * **User Story:** Como agrónomo, quiero exportar datos clave a CSV para análisis posterior.
    * **Criterio de Aceptación:** Dado la lista de casos, cuando elijo “Exportar CSV”, entonces descargo un archivo con campos estándar.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Útil para analítica, pero no esencial para cerrar casos en v1.

---

### **Arquetipo: Administrador/Mayordomo**

---

**Basado en el JTBD #1:**  
> **Cuando** hay alerta fitosanitaria y el clima cierra la ventana de aspersión,  
> **quiero** un semáforo por lote con tareas, mezcla y EPP,  
> **para poder** reubicar cuadrillas y cumplir metas sin reprocesos.

* **Funcionalidades Propuestas:**

  * **1. Tablero “Semáforo por Lote” (offline)**
    * **User Story:** Como mayordomo, quiero ver cada lote en rojo/amarillo/verde con mezcla y EPP sugeridos para poder priorizar de inmediato.
    * **Criterio de Aceptación:** Dado que estoy sin señal, cuando abro el tablero, entonces veo el estado por lote con fecha/hora y la recomendación mínima accionable (mezcla, EPP).
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Núcleo del JTBD; sin esto no hay priorización operativa. Impacto directo y esencial en el MVP.

  * **2. Planificador de Cuadrillas y Recursos**
    * **User Story:** Como mayordomo, quiero asignar cuadrillas, equipos y horarios por lote para ejecutar el plan sin confusiones.
    * **Criterio de Aceptación:** Dado el semáforo, cuando asigno cuadrilla y equipo, entonces se generan tareas con responsable y hora objetivo.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Lleva la priorización a ejecución. Elimina reprocesos y pérdida de tiempo; clave para que el MVP produzca resultados reales.

  * **3. Ventanas Climáticas y Alertas de Reprogramación**
    * **User Story:** Como mayordomo, quiero recibir alertas de cambio de clima para reprogramar tareas críticas a tiempo.
    * **Criterio de Aceptación:** Dado un lote con aspersión programada, cuando la ventana climática se invalide, entonces recibo alerta y propuesta de nuevo horario.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Alto valor operativo; el MVP puede iniciar sin predicción avanzada si hay reprogramación manual.

  * **4. Ruta Operativa por Prioridad**
    * **User Story:** Como mayordomo, quiero una secuencia sugerida de atención de lotes para reducir traslados y tiempos muertos.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Optimiza ejecución; no bloquea el lanzamiento si existe tablero + asignación.

  * **5. Integración Ligera de Inventario (EPP/insumos)**
    * **User Story:** Como mayordomo, quiero ver si tengo EPP e insumos mínimos antes de asignar cuadrilla.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Conveniencia y prevención de bloqueos; añade complejidad de datos, no crítica para validar el MVP.

  * **6. Integración con ERP/Bodega**
    * **User Story:** Como mayordomo, quiero sincronizar consumos con el ERP.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Alto costo de integración, no esencial para validar el valor central de la primera versión.

---

**Basado en el JTBD #2:**  
> **Cuando** viene auditoría o cierre de mes,  
> **quiero** generar evidencia ‘antes/después’ en un PDF georreferenciado,  
> **para poder** responder hallazgos sin cazar papeles.

* **Funcionalidades Propuestas:**

  * **1. Generador de Reporte Auditoría (PDF/imagen) con Georreferencia**
    * **User Story:** Como mayordomo, quiero crear un reporte con fotos antes/después, fecha/hora y coordenadas para auditoría.
    * **Criterio de Aceptación:** Dado un conjunto de evidencias, cuando genero el reporte, entonces obtengo un PDF comprimido con metadatos (GPS, sello temporal).
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Salida tangible del trabajo y requisito clave de auditoría; indispensable para el MVP.

  * **2. Plantillas de Cumplimiento (cliente/cooperativa)**
    * **User Story:** Como mayordomo, quiero aplicar plantillas estandarizadas con campos obligatorios para cumplir exigencias formales.
    * **Criterio de Aceptación:** Dado que selecciono una plantilla, cuando exporto, entonces el PDF incluye logos, campos requeridos y numeración.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Garantiza consistencia y reduc e retrabajo; crítica para pasar auditoría desde el día uno.

  * **3. Firma Digital en Campo (Supervisor/Operario)**
    * **User Story:** Como mayordomo, quiero capturar firmas en el reporte para cerrar evidencias en sitio.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Aumenta trazabilidad y evita impresiones; valioso, pero el reporte básico es suficiente para el MVP.

  * **4. Repositorio y Control de Versiones**
    * **User Story:** Como mayordomo, quiero almacenar y versionar reportes para responder observaciones.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Facilita gestión documental; el MVP puede iniciar con guardado local/exportación simple.

  * **5. Código QR/Folio Único por Reporte**
    * **User Story:** Como mayordomo, quiero un QR/folio para rastrear rápidamente el reporte en campo.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Mejora experiencia de auditoría; no esencial en v1.

  * **6. Exportación Masiva y Envío Programado**
    * **User Story:** Como mayordomo, quiero exportar varios reportes y programar su envío.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Útil para escalas grandes; puede esperar tras validar uso del reporte individual.

---

**Basado en el JTBD #3:**  
> **Cuando** ingreso personal o vehículos de proveedores,  
> **quiero** una lista de bioseguridad con registro fotográfico,  
> **para poder** autorizar o negar entrada con respaldo.

* **Funcionalidades Propuestas:**

  * **1. Checklist de Bioseguridad con Evidencia Fotográfica**
    * **User Story:** Como mayordomo, quiero un checklist simple con fotos para validar requisitos de ingreso.
    * **Criterio de Aceptación:** Dado un visitante, cuando completo el checklist, entonces la app registra estado (cumple/no cumple), fotos y sello temporal.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Cubre el núcleo del JTBD (decidir con respaldo); fundamental para el MVP.

  * **2. Registro de Proveedores/Vehículos (placa, empresa, responsable)**
    * **User Story:** Como mayordomo, quiero registrar datos básicos de proveedor y vehículo para trazabilidad.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Mejora la auditoría y seguridad; el MVP puede operar con checklist + foto aun sin base maestra.

  * **3. Semáforo de Acceso (Aprobado/Pendiente/Denegado) y Motivos**
    * **User Story:** Como mayordomo, quiero ver un estado claro de acceso con razones documentadas.
    * **Criterio de Aceptación:** Dado un control efectuado, cuando finalizo, entonces se asigna estado y se guarda el motivo.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Estándar operativo y claridad para portería; eleva profesionalismo.

  * **4. Bitácora de Eventos y Exportación CSV**
    * **User Story:** Como mayordomo, quiero revisar un historial de ingresos y exportarlo cuando lo soliciten.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Útil en investigaciones/auditorías; no bloquea el uso diario.

  * **5. Pases con QR e Integración con Cámaras/Torniquetes**
    * **User Story:** Como mayordomo, quiero emitir pases QR y vincular cámaras para automatizar el control.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Requiere hardware e integraciones; posponer hasta validar el flujo manual con checklist.

## **Resultados: Backlog de Funcionalidades Priorizadas**

### **Arquetipo: Productor mediano (papa / maíz / aguacate Hass)**

---

**Basado en el JTBD #1:**  
> **Cuando** veo síntomas dudosos después de una granizada o lluvias,  
> **quiero** diferenciar daño mecánico de enfermedad con una guía práctica,  
> **para poder** evitar aplicaciones innecesarias y cuidar el flujo de caja.

* **Funcionalidades Propuestas:**

  * **1. Guía de Diferenciación Rápida (daño mecánico vs. enfermedad)**
    * **User Story:** Como productor, quiero una guía paso a paso que me muestre señales clave para distinguir daño por clima de patógeno, para decidir con confianza.
    * **Criterio de Aceptación:** Dado que selecciono “granizada/lluvia”, cuando sigo 3–5 preguntas y subo 1 foto, entonces recibo un veredicto tentativo (mecánico/probable enfermedad) con señales observables.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Ataca el dolor principal (gasto inútil). Esencial para el valor del MVP en campo.

  * **2. Asesor “Aplicar o Esperar” (con umbral y clima cercano)**
    * **User Story:** Como productor, quiero una recomendación simple “aplicar/esperar” con umbral de riesgo y ventana climática para no desperdiciar insumo.
    * **Criterio de Aceptación:** Dado el diagnóstico tentativo, cuando consulto la recomendación, entonces obtengo acción sugerida, ventana de tiempo y breve razonamiento.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Conecta el diagnóstico con la decisión que ahorra dinero. Núcleo del JTBD.

  * **3. Comparador Visual Offline con Anotaciones**
    * **User Story:** Como productor, quiero comparar mi foto con ejemplos de referencia anotados para ver diferencias críticas.
    * **Criterio de Aceptación:** Dado una foto, cuando abro el comparador, entonces veo 3–5 imágenes de referencia con anotaciones y checklist corto.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Aumenta certeza y reduce errores; el MVP puede vivir con guía + asesor si hay límite.

  * **4. Simulador de Costo–Beneficio (aplicar vs. esperar)**
    * **User Story:** Como productor, quiero estimar el costo de aplicar ahora vs. esperar X días para decidir financieramente.
    * **Criterio de Aceptación:** Dado precio del insumo y área, cuando simulo, entonces veo costo estimado y riesgo asociado.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Potencia la decisión económica, pero no es indispensable en v1.

  * **5. Escalamiento a Laboratorio / Toma de Muestra**
    * **User Story:** Como productor, quiero instrucciones para toma de muestra y envío a laboratorio cuando la incertidumbre sea alta.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Requiere red externa e integración; posponer hasta validar flujo básico.

---

**Basado en el JTBD #2:**  
> **Cuando** dudo si cosechar Hass con antracnosis leve,  
> **quiero** una recomendación de cosecha selectiva y manejo poscosecha,  
> **para poder** reducir pérdidas y rechazos en empaque.

* **Funcionalidades Propuestas:**

  * **1. Asesor de Cosecha Selectiva (severidad de antracnosis)**
    * **User Story:** Como productor de Hass, quiero clasificar frutos por severidad para decidir cuáles cosechar ya y cuáles dejar.
    * **Criterio de Aceptación:** Dado un muestreo de frutos, cuando clasifico con la guía visual, entonces obtengo recomendación por categoría (cosechar/esperar/descartar).
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Resuelve directamente el JTBD y evita rechazos en planta.

  * **2. Guía Pos-cosecha Adaptativa (lavado, fungicida, curado, temperatura)**
    * **User Story:** Como productor, quiero pasos poscosecha según severidad y recursos disponibles para minimizar daños.
    * **Criterio de Aceptación:** Dado el nivel de severidad, cuando selecciono “poscosecha”, entonces recibo protocolo breve con tiempos/condiciones.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Complementa la decisión de corte con acción concreta; muy valiosa, posterior al asesor de cosecha.

  * **3. Semáforo de Rechazo en Empaque (apto / riesgo / no apto)**
    * **User Story:** Como productor, quiero un semáforo que me anticipe probabilidad de rechazo según defectos.
    * **Criterio de Aceptación:** Dado el muestreo, cuando genero el semáforo, entonces veo el porcentaje por categoría con recomendación.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Facilita decisiones rápidas antes de enviar a planta.

  * **4. Especificaciones de Comprador (calibres, tolerancias)**
    * **User Story:** Como productor, quiero ver requisitos del comprador (cuando estén disponibles) para alinear corte y selección.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Alto valor, pero requiere mantener catálogos/variantes; posponer a v1.1.

  * **5. Integración con Báscula / Etiquetado QR en Empaque**
    * **User Story:** Como productor, quiero vincular peso y etiquetas para trazabilidad en planta.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Demanda hardware e integración; no crítico para validar el proceso de decisión.

---

**Basado en el JTBD #3:**  
> **Cuando** evalúo prácticas (con/sin cobertura, fertilización fraccionada),  
> **quiero** comparar ‘antes/después’ por lote con un score simple,  
> **para poder** quedarme con lo que realmente funciona y descartar lo que no.

* **Funcionalidades Propuestas:**

  * **1. Ensayos A/B por Lote (plantilla rápida)**
    * **User Story:** Como productor, quiero crear ensayos sencillos A/B por lote para medir el efecto real de una práctica.
    * **Criterio de Aceptación:** Dado un lote, cuando defino A/B y registro 3–5 datos, entonces obtengo una comparación básica con conclusión sugerida.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Núcleo del JTBD: evidenciar qué funciona de forma simple.

  * **2. Score Simple de Práctica + Panel “Lo que Funciona”**
    * **User Story:** Como productor, quiero un score (↑/→/↓) por práctica y un panel que resuma lo que conviene mantener o descartar.
    * **Criterio de Aceptación:** Dado varios ensayos, cuando abro el panel, entonces veo el ranking y una recomendación por práctica.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Traduce resultados en decisiones accionables; esencial para el MVP.

  * **3. Galería Antes/Después y Línea de Tiempo**
    * **User Story:** Como productor, quiero ver fotos antes/después y la evolución en el tiempo para comunicar resultados.
    * **Criterio de Aceptación:** Dado un ensayo, cuando abro la galería, entonces visualizo pares de fotos y fechas clave.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Refuerza adopción y aprendizaje; puede llegar tras el score inicial.

  * **4. Exportación y Compartir con Técnico (PDF/imagen)**
    * **User Story:** Como productor, quiero exportar resultados y enviarlos por WhatsApp al técnico.
    * **Criterio de Aceptación:** Dado un ensayo, cuando toco “Exportar”, entonces genero PDF/imagen comprimida lista para compartir.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Útil para soporte y validación externa; no bloquea el MVP.

  * **5. Integración con Sensores IoT / Imágenes NDVI**
    * **User Story:** Como productor, quiero combinar mis ensayos con datos de sensores o NDVI para mayor precisión.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Alto esfuerzo y dependencias; posponer hasta validar uso del módulo A/B.


### **Arquetipo: Técnico agrícola (cooperativa / insumos)**

---

**Basado en el JTBD #1:**  
> **Cuando** tengo una ruta con muchas visitas y la señal es irregular,  
> **quiero** priorizar casos en un mapa offline con riesgo y distancia,  
> **para poder** maximizar el impacto de la jornada y cumplir metas sin devoluciones innecesarias.

* **Funcionalidades Propuestas:**

  * **1. Mapa Offline + Score de Riesgo por Caso**
    * **User Story:** Como técnico, quiero visualizar los casos en un mapa sin conexión con un score de riesgo para decidir a dónde ir primero.
    * **Criterio de Aceptación:** Dado que no tengo señal, cuando abro el mapa, entonces veo pines de casos con color/score (alto/medio/bajo) calculado localmente (síntomas, tiempo en cola, historial).
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Es el núcleo del JTBD (priorizar sin señal); sin esto no hay planificación efectiva en campo.

  * **2. Planificador de Ruta por Riesgo y Distancia (offline)**
    * **User Story:** Como técnico, quiero una secuencia sugerida que minimice traslados y atienda primero lo crítico.
    * **Criterio de Aceptación:** Dado un conjunto de casos, cuando solicito ruta, entonces obtengo un orden recomendado (heurística TSP) usable sin datos.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Optimiza la jornada y reduce tiempo muerto; no bloquea el MVP si existe la lista priorizada.

  * **3. Alta Rápida de Casos (1-min) con GPS y Fotos**
    * **User Story:** Como técnico, quiero registrar un caso en menos de 1 minuto con datos clave (cultivo, síntoma, 1–3 fotos, GPS) para no perder evidencia.
    * **Criterio de Aceptación:** Dado el formulario rápido, cuando guardo, entonces el caso queda disponible offline y aparece en el mapa con su score inicial.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Sin captura ágil no hay datos para priorizar ni cerrar visitas; esencial.

  * **4. Repriorización Dinámica por Tiempo y Compromisos**
    * **User Story:** Como técnico, quiero que los casos aumenten de prioridad si están cerca de vencer SLAs o si el productor reporta empeoramiento.
    * **Criterio de Aceptación:** Dado un SLA, cuando el tiempo restante baje del umbral, entonces el score sube y el caso asciende en el ranking.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Alinea metas comerciales/técnicas con la agenda; agrega valor sin ser bloqueante.

  * **5. Cola de Sincronización y Resolución de Conflictos**
    * **User Story:** Como técnico, quiero que mis cambios se sincronicen al recuperar señal y que la app me ayude a resolver conflictos (último cambio vs. servidor).
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Mejora robustez post-MVP; el flujo base puede operar con exportación manual si es necesario.

  * **6. Geofencing de Llegada/Salida (auto check-in)**
    * **User Story:** Como técnico, quiero que la app registre automáticamente llegada/salida a un predio.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Requiere calibración y puede drenar batería; posponer hasta validar uso con check-ins manuales.

---

**Basado en el JTBD #2:**  
> **Cuando** mi teléfono es de baja gama y la memoria se llena,  
> **quiero** un modo ‘lite’ que comprima, guarde y permita subir luego,  
> **para poder** capturar evidencia sin que la app se caiga ni perder información.

* **Funcionalidades Propuestas:**

  * **1. Cámara Modo Lite (compresión + guardado en segundo plano)**
    * **User Story:** Como técnico, quiero sacar fotos evidenciales en modo comprimido que no cierre la app ni consuma demasiada memoria.
    * **Criterio de Aceptación:** Dado que capturo 3 fotos seguidas, cuando vuelvo al caso, entonces las imágenes están guardadas (≤300 KB c/u) y la app sigue operativa.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Elimina el dolor central (crashes/pérdida de evidencia); imprescindible en dispositivos de gama baja.

  * **2. Gestor de Almacenamiento con Alertas y Limpieza Segura**
    * **User Story:** Como técnico, quiero ver cuánto espacio queda y poder limpiar caché de miniaturas sin perder evidencias.
    * **Criterio de Aceptación:** Dado espacio bajo, cuando ejecuto “Limpiar caché”, entonces se liberan MB y las fotos originales permanecen.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Previene caídas por almacenamiento; crítico para continuidad de uso.

  * **3. Cola de Subida con Reintentos/Resume y Modo Datos Bajos**
    * **User Story:** Como técnico, quiero que las evidencias se suban automáticamente cuando haya señal, con reintentos y límite de datos.
    * **Criterio de Aceptación:** Dado que recupero 3G, cuando se inicia la cola, entonces los archivos suben por prioridad y se reanudan si falla la conexión.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Asegura flujo sin intervención manual; agrega resiliencia post-MVP.

  * **4. Paquetes de Evidencia (foto+nota+coordenada)**
    * **User Story:** Como técnico, quiero agrupar varias fotos y notas en un “paquete” comprimido por caso para enviar/guardar de forma liviana.
    * **Criterio de Aceptación:** Dado un caso, cuando genero paquete, entonces obtengo un archivo ≤2 MB con metadatos básicos.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Facilita compartir/transferir en conectividad limitada.

  * **5. Modo Texto-Primero (degradación elegante)**
    * **User Story:** Como técnico, quiero poder registrar solo texto/checkbox y añadir fotos después para no detenerme por memoria.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Alternativa útil en casos extremos; no crítica si el Modo Lite funciona bien.

  * **6. Soporte SD/Disco Externo**
    * **User Story:** Como técnico, quiero guardar en SD/USB-OTG.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Fragmentación de dispositivos/permiso; posponer hasta validar adopción del Modo Lite.

---

**Basado en el JTBD #3:**  
> **Cuando** hago demos o capacitaciones con comunidades diversas,  
> **quiero** plantillas estándar con pictogramas y audio,  
> **para poder** enseñar sin barreras de lectura o jerga técnica y generar adopción real.

* **Funcionalidades Propuestas:**

  * **1. Motor de Plantillas con Pictogramas y Audio (offline)**
    * **User Story:** Como técnico, quiero reproducir pasos con iconografía y audio para explicar procedimientos sin depender de lectura.
    * **Criterio de Aceptación:** Dado que selecciono una plantilla, cuando inicio “Demo”, entonces la app muestra pantallas con pictogramas y reproduce indicaciones de voz sin conexión.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Ataca directamente la barrera de alfabetización/jerga; esencial para lograr adopción en campo.

  * **2. Modo Presentador (botones grandes + avance paso a paso)**
    * **User Story:** Como técnico, quiero un modo con controles grandes y avance secuencial para dictar la capacitación desde el teléfono.
    * **Criterio de Aceptación:** Dado el modo presentador, cuando toco “Siguiente”, entonces el paso avanza y se registra el tiempo por paso.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Mejora la dinámica de formación; el MVP puede operar con el motor de plantillas básico.

  * **3. Perfiles Comunitarios (idioma, nivel de detalle)**
    * **User Story:** Como técnico, quiero configurar idioma y nivel (básico/avanzado) para adaptar la explicación a cada comunidad.
    * **Criterio de Aceptación:** Dado un perfil seleccionado, cuando inicio la plantilla, entonces los textos/audio y la cantidad de pasos se ajustan al perfil.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Eleva la relevancia cultural/lingüística; no bloqueante para la primera entrega.

  * **4. Paquetes de Contenido por Cultivo/Región (descarga)**
    * **User Story:** Como técnico, quiero descargar paquetes temáticos (café, plátano, papa, Hass) para tener demos listos sin internet.
    * **Criterio de Aceptación:** Dado conectividad puntual, cuando descargo un paquete, entonces queda disponible offline con imágenes/audio.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Aporta amplitud de uso; puede llegar tras validar el motor de plantillas.

  * **5. Registro de Sesiones y Feedback Rápido**
    * **User Story:** Como técnico, quiero registrar cuántas personas asistieron y su feedback (pulgar arriba/abajo) por plantilla.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Útil para medir adopción/impacto, pero no esencial para enseñar.

  * **6. Proyección a Pantalla (Chromecast/Miracast)**
    * **User Story:** Como técnico, quiero proyectar la demo a una TV o proyector.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Requiere hardware adicional; posponer hasta validar el uso móvil 1:1/pequeños grupos.
