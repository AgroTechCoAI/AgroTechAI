# Journey Maps AS-IS

## **FASE 1: INVESTIGACIÓN DE JOURNEYS ACTUALES**

Basado en el System Map AS-IS y los arquetipos, los journeys actuales para el diagnóstico de cultivos en las regiones de Eje Cafetero, Valle del Cauca, Antioquia y Atlántico se pueden agrupar de la siguiente manera:

#### **Journeys por Método Actual de Diagnóstico:**
* **Diagnóstico visual propio + Consulta en WhatsApp:** El usuario (generalmente Pequeño Productor) detecta un problema, toma una foto de baja calidad y la comparte en grupos de WhatsApp de su vereda o de colegas, recibiendo múltiples opiniones contradictorias y no verificadas.
* **Consulta con experto (Técnico de cooperativa/Agrónomo):** El usuario (Productor Mediano o Pequeño Productor con acceso a cooperativa) contacta a un técnico, pero enfrenta demoras significativas (2-7 días de espera) para una visita presencial.
* **Consulta en el punto de venta:** El usuario va directamente al distribuidor de insumos local con una descripción verbal o una muestra física del problema, y recibe una recomendación fuertemente influenciada por el inventario disponible en la tienda.
* **Toma de muestras y envío a laboratorio:** Utilizado por Productores Medianos o en casos muy complejos, este proceso es el más preciso pero también el más lento (7-15 días para resultados) y costoso, lo que lo hace inaccesible para la mayoría.
* **Prueba y error basado en experiencia:** Un productor experimentado aplica un tratamiento que funcionó en el pasado para un problema similar, sin confirmar si la causa raíz es la misma, lo que lleva a un sobreuso de insumos.

#### **Journeys por Urgencia/Contexto:**
* **Emergencia crítica (Ej. Brote de Roya):** Se activa un proceso caótico y acelerado de consulta múltiple (WhatsApp, vecinos, tienda local) bajo alta presión, llevando a decisiones apresuradas y a menudo incorrectas debido a la indisponibilidad inmediata de expertos.
* **Monitoreo rutinario y validación:** Un Administrador de finca o un Productor Mediano realiza revisiones periódicas y, al encontrar una anomalía, busca validar su sospecha inicial con su agrónomo de confianza, iniciando el lento proceso de contacto.
* **Segunda opinión por fracaso de tratamiento:** Tras aplicar una primera solución (a menudo basada en prueba y error) que no funcionó, el usuario inicia un nuevo journey, esta vez buscando una fuente más confiable, duplicando costos y tiempo.

#### **Journeys por Recursos Disponibles:**
* **Con limitaciones económicas (Pequeño Productor):** Se limita exclusivamente a opciones gratuitas como la consulta a vecinos, grupos de WhatsApp y la recomendación del tendero local, aceptando un alto nivel de incertidumbre y baja efectividad (45-70%).
* **Con acceso a expertos (Productor Mediano):** Puede costear una asesoría mensual o visitas técnicas pagadas, pero sufre por la baja disponibilidad y los altos tiempos de espera de los consultores.
* **Aislado geográficamente:** Depende casi por completo de la radio rural y llamadas telefónicas, con el viaje al pueblo (0.5-3 horas) como principal punto de contacto para obtener información o insumos.

---

## **FASE 2: PRIORIZACIÓN DE JOURNEYS AS-IS**

Evaluando los journeys actuales, seleccionamos los 3 más críticos que representan las mayores oportunidades de mejora para una solución de IA.

| Journey AS-IS | Frecuencia Actual (1-10) | Nivel de Frustración (1-10) | Impacto en Resultados (1-10) | Oportunidad de Mejora (1-10) | Representatividad (1-10) | **Puntaje Total (50)** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Diagnóstico de Emergencia vía WhatsApp y Consulta Local** | 9 | 9 | 10 | 10 | 9 | **47** |
| **2. Consulta Técnica Pagada con Demoras** | 7 | 10 | 10 | 9 | 8 | **44** |
| **3. Prueba y Error Basado en Experiencia Previa** | 8 | 7 | 8 | 9 | 8 | **40** |
| **4. Envío de Muestras a Laboratorio** | 4 | 8 | 9 | 8 | 6 | **35** |

**Journeys Seleccionados:**
1.  **Diagnóstico de Emergencia vía WhatsApp y Consulta Local:** Es el más frecuente, frustrante y con un impacto directo en la pérdida de la cosecha. La oportunidad de mejora es máxima.
2.  **Consulta Técnica Pagada con Demoras:** Representa el "deber ser" para diagnósticos de calidad, pero su principal punto de dolor es el tiempo. Mejorar este journey es clave para usuarios con mayor capacidad de pago.
3.  **Prueba y Error Basado en Experiencia Previa:** Muy común y costoso por el desperdicio de insumos y el riesgo de no resolver el problema de raíz. Hay una gran oportunidad para introducir precisión.

---

## **FASE 3: MAPEO DETALLADO DE JOURNEYS AS-IS**

A continuación, el mapeo detallado del journey más crítico seleccionado.

# **JOURNEY AS-IS 1: Diagnóstico de Emergencia vía WhatsApp y Consulta Local**

**📋 INFORMACIÓN GENERAL**
* **Arquetipo principal:** Pequeño Agricultor Familiar (Carlos, cafetero de 2-5 ha).
* **Situación que dispara el journey:** Detección de síntomas anormales y de rápida propagación en el cultivo después de un cambio climático (ej. manchas naranjas de roya en el café tras varios días de lluvia).
* **Método actual principal:** Autodiagnóstico visual inicial, seguido de una consulta masiva en grupos de WhatsApp y validación en la tienda de insumos local.
* **Frecuencia típica:** Alta, 3-8 episodios críticos por año, especialmente en épocas de lluvia.
* **Duración total actual:** Entre 3 y 10 días desde la detección hasta la aplicación de un tratamiento.
* **Recursos/herramientas actuales:** Smartphone Android de gama media, plan de datos intermitente, grupos de WhatsApp, transporte (moto/bus), y el consejo del dueño de la agropecuaria local.

---

## **🗺️ PROCESO ACTUAL (AS-IS)**

### **FASE 1: DETECCIÓN DEL PROBLEMA**
**Cómo actualmente identifica problemas en el cultivo**

**🎬 SITUACIÓN ACTUAL:**
* **Ubicación:** En medio del lote de café, en una ladera con baja o nula señal de internet.
* **Momento:** Durante su recorrido matutino de rutina por el cultivo.
* **Método de detección:** Puramente visual. Nota que las manchas amarillas que vio ayer hoy son más grandes y de color naranja intenso.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Se acerca, arranca una hoja afectada, la mira a contraluz, la raspa con la uña. Camina a otras partes del lote para ver si el problema está extendido.
* **Pensamientos:** *"Esto se parece a la roya del año pasado, pero las manchas son más agresivas. ¿Será lo mismo? ¿O será algo peor? Tengo que actuar rápido o pierdo la cosecha."*
* **Emociones:** Preocupación, ansiedad, un nudo en el estómago. Urgencia.
* **Herramientas:** Sus propios ojos y su experiencia. Saca su celular para tomar una foto, pero la luz es mala y la foto sale borrosa.

**⏱️ TIEMPO INVERTIDO:** 30 - 60 minutos.

**😤 FRUSTRACIONES ACTUALES:**
* Incertidumbre sobre la gravedad y la identidad exacta del problema.
* La experiencia pasada puede no ser suficiente si es una nueva cepa o un problema diferente con síntomas parecidos.
* La falta de herramientas de magnificación o medición le impide cuantificar el daño.

**💸 COSTOS ACTUALES:**
* Tiempo de inspección que podría usar en otras labores. El costo de oportunidad empieza a correr.

---

### **FASE 2: INVESTIGACIÓN Y DIAGNÓSTICO INICIAL**
**Cómo actualmente intenta diagnosticar el problema**

**🎬 SITUACIÓN ACTUAL:**
* **Recursos consultados:** Tiene que caminar hasta un punto más alto de la finca o volver a la casa para tener algo de señal de datos.
* **Personas contactadas:** El grupo de WhatsApp "Cafeteros de la Vereda".
* **Herramientas usadas:** WhatsApp.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Sube la foto borrosa al grupo con el mensaje: *"Buenos días vecinos, ¿alguien sabe qué es esto? Me apareció de un día para otro."*
* **Pensamientos:** *"Espero que alguien que sepa responda rápido. A ver qué dicen... Ojalá no sea grave."*
* **Emociones:** Impaciencia, confusión. En las siguientes 2 a 6 horas, recibe 10 respuestas:
    * Uno dice que es roya.
    * Otro dice que es deficiencia de nutrientes.
    * Un tercero comparte una foto de un problema que no se parece en nada.
    * Alguien recomienda un producto carísimo.
    * Otro recomienda un remedio casero.
* **Criterios de decisión:** Tiende a confiar en la opinión del vecino que considera más experimentado, aunque no tenga una base técnica.

**⏱️ TIEMPO INVERTIDO:** 2 - 24 horas esperando respuestas y tratando de descifrarlas.

**🔧 TOUCHPOINTS ACTUALES:**
* Grupo de WhatsApp de la vereda.
* Llamada a un familiar o compadre que también cultiva.

**😤 FRUSTRACIONES ACTUALES:**
* **Información contradictoria y no verificada:** La principal frustración. El 30% es útil, el 40% irrelevante y el 30% contradictorio.
* La baja calidad de la foto dificulta cualquier diagnóstico remoto.
* La urgencia choca con la velocidad de respuesta asíncrona del chat.

**💸 COSTOS ACTUALES:**
* Costo del plan de datos móviles.
* **Costo de oportunidad:** Tiempo valioso perdido donde la enfermedad se sigue propagando.

---

### **FASE 3: BÚSQUEDA DE SEGUNDA OPINIÓN**
**Cómo valida su diagnóstico inicial**

**🎬 SITUACIÓN ACTUAL:**
* **Fuentes de validación:** Confundido por WhatsApp, decide ir al pueblo a la agropecuaria de confianza.
* **Métodos de comunicación:** Visita presencial. Lleva una hoja afectada en una bolsa.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Toma la moto o el bus, un viaje que le toma entre 30 minutos y 2 horas. Le muestra la hoja al dueño de la tienda.
* **Pensamientos:** *"Don Miguel sabe de esto, él me va a decir qué es de verdad. Él no me va a dejar colgado."*
* **Emociones:** Esperanza, pero también ansiedad por el costo del viaje y del posible tratamiento.

**⏱️ TIEMPO INVERTIDO:** 2 - 4 horas (viaje + espera + consulta).

**😤 FRUSTRACIONES ACTUALES:**
* El diagnóstico del tendero está sesgado por el inventario que tiene disponible. Su recomendación casi siempre coincide con los productos que más margen le dejan.
* El conocimiento del tendero es empírico, no necesariamente técnico o actualizado.
* Disponibilidad limitada: la tienda puede estar cerrada o el dueño ocupado.

**💸 COSTOS ACTUALES:**
* Costo del transporte ($10-20K COP).
* Tiempo de trabajo perdido durante media jornada.

---

### **FASE 4: TOMA DE DECISIÓN**
**Cómo decide qué tratamiento aplicar**

**🎬 SITUACIÓN ACTUAL:**
* **Proceso de decisión:** En el mostrador de la tienda, con la recomendación de Don Miguel y las opiniones de WhatsApp en la cabeza.
* **Factores considerados:** **Costo** (lo más importante), **disponibilidad inmediata**, confianza en el tendero y la experiencia previa ("*el año pasado usé este y como que funcionó*").

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Pregunta precios, pregunta si hay una opción más barata, evalúa si le alcanza el dinero que tiene.
* **Pensamientos:** *"Este fungicida es caro, ¿y si no funciona? El vecino me dijo que usara otro más barato. Pero Don Miguel dice que este es el bueno. Mejor le hago caso a él, que para eso vine hasta acá."*
* **Emociones:** Presión, incertidumbre, resignación ante el gasto.

**⏱️ TIEMPO INVERTIDO:** 15 - 30 minutos.

**😤 FRUSTRACIONES ACTUALES:**
* Decidir con información incompleta y sesgada.
* La presión de tener que comprar algo después de haber hecho el viaje y la consulta.
* Falta de alternativas y opciones de pago.

**💸 COSTOS ACTUALES:**
* El costo mental de tomar una decisión de alto riesgo con poca información.

---

### **FASE 5: ADQUISICIÓN DE TRATAMIENTO**
**Cómo obtiene los productos/servicios necesarios**

**🎬 SITUACIÓN ACTUAL:**
* **Proveedores:** La agropecuaria local en la cabecera municipal.
* **Proceso de compra:** Pago en efectivo o, si tiene suerte, crédito informal ("fíemelo hasta la cosecha").

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Compra el fungicida recomendado (costo: $80-300K COP/ha), junto con un adherente. Se asegura de que le den las instrucciones de mezcla.
* **Pensamientos:** *"Espero que esto sea suficiente. ¿Cómo lo voy a transportar en la moto sin que se riegue?"*
* **Emociones:** Alivio temporal por tener una solución en la mano, pero preocupación por el desembolso económico.

**⏱️ TIEMPO INVERTIDO:** 10 minutos para la transacción, más el viaje de regreso (0.5 - 2 horas).

**😤 FRUSTRACIONES ACTUALES:**
* **Disponibilidad limitada:** A veces el producto recomendado no está en stock y tiene que aceptar un sustituto "parecido".
* **Precios elevados:** Sabe que podría haber una variación de hasta el 60% con otras tiendas, pero no tiene tiempo ni recursos para comparar.
* Transporte de insumos químicos de forma insegura.

**💸 COSTOS ACTUALES:**
* Costo directo del producto: $80-300K COP/ha.
* Costo del transporte de regreso.

---

### **FASE 6: APLICACIÓN DEL TRATAMIENTO**
**Cómo implementa la solución**

**🎬 SITUACIÓN ACTUAL:**
* **Método de aplicación:** Manual, usando una bomba de espalda de 20 litros.
* **Seguimiento de protocolo:** Intenta seguir las instrucciones del empaque o lo que le dijo el tendero, pero a menudo lo hace "al ojo".

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Mezcla el producto con agua del aljibe, calibra la boquilla de la bomba "más o menos". Aplica el producto por todo el lote, tardando varias horas o incluso un día completo.
* **Pensamientos:** *"Ojalá esté mezclando bien la dosis. Tengo que apurarme antes de que llueva. ¿Debo ponerme guantes? Nah, así está bien."*
* **Emociones:** Cansancio físico, esperanza de que el esfuerzo valga la pena.

**⏱️ TIEMPO INVERTIDO:** 4 - 8 horas de trabajo físico intenso.

**😤 FRUSTRACIONES ACTUALES:**
* Dificultad para calcular la dosis correcta para su área específica.
* Condiciones climáticas (lluvia, viento) que pueden lavar el producto y anular su efecto.
* Falta de equipo de protección personal adecuado y el riesgo para su salud.

**💸 COSTOS ACTUALES:**
* Un día completo de trabajo.
* Posible costo de mano de obra si necesita contratar a un jornalero.

---

### **FASE 7: MONITOREO DE RESULTADOS**
**Cómo evalúa si el tratamiento está funcionando**

**🎬 SITUACIÓN ACTUAL:**
* **Frecuencia de revisión:** Diaria. Va al mismo punto todos los días a ver si hay cambios.
* **Método de evaluación:** Puramente visual y subjetivo. Compara el recuerdo de cómo se veía ayer con lo que ve hoy.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Inspecciona las hojas tratadas, busca nuevas manchas, toca las hojas para sentir su textura.
* **Pensamientos:** *"¿Las manchas están más secas? ¿O es idea mía? Parece que no hay nuevas, eso es bueno. Pero las hojas viejas se ven igual de mal. ¿Estará funcionando?"*
* **Emociones:** Impaciencia, ansiedad, duda. La retroalimentación es lenta y ambigua.

**⏱️ TIEMPO INVERTIDO:** 15-30 minutos diarios durante 1-2 semanas.

**😤 FRUSTRACIONES ACTUALES:**
* No saber qué indicadores de mejora buscar ni cuándo esperarlos.
* La lenta respuesta del cultivo hace difícil evaluar la efectividad del tratamiento.
* Duda constante sobre si necesita volver a aplicar, lo que podría llevar a un gasto innecesario.

**💸 COSTOS ACTUALES:**
* Tiempo continuo de monitoreo.
* El costo emocional de la incertidumbre.

---

### **FASE 8: EVALUACIÓN FINAL Y APRENDIZAJE**
**Cómo determina si fue exitoso y qué aprendió**

**🎬 SITUACIÓN ACTUAL:**
* **Criterios de éxito:** Si la propagación de la enfermedad se detuvo y no perdió una parte significativa de la cosecha.
* **Documentación:** Ninguna. Todo el aprendizaje es mental, basado en la memoria.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Después de 2-3 semanas, hace una evaluación final. Si el problema se controló, se siente aliviado. Si no, se siente frustrado y piensa en qué falló.
* **Pensamientos:** *"Bueno, parece que funcionó. Para la próxima ya sé que ese producto de Don Miguel sirve para estas manchas. Pero perdí como el 15% de las hojas en ese lote."*
* **Emociones:** Satisfacción si funcionó, o decepción y resignación si no.

**⏱️ TIEMPO INVERTIDO:** Proceso total de 2 a 4 semanas.

**😤 FRUSTRACIONES ACTUALES:**
* **Falta de documentación sistemática:** El conocimiento adquirido es volátil y se basa en la memoria. Si el mismo problema ocurre en dos años, puede que no recuerde exactamente qué hizo.
* Dificultad para medir el ROI real: no puede cuantificar con precisión cuánto perdió y cuánto se salvó.
* El aprendizaje es anecdótico y no se comparte de forma estructurada con otros.

**💸 COSTOS TOTALES:**
* La suma de todos los costos del proceso, incluyendo la pérdida de producción.

---

## **📊 ANÁLISIS DEL JOURNEY AS-IS**

**⏱️ TIEMPOS TOTALES:**
* Desde detección hasta inicio de tratamiento: **3 - 10 días**.
* Proceso completo hasta evaluación: **2 - 4 semanas**.

**💰 COSTOS TOTALES:**
* **Monetarios:** Entre **$150,000 y $800,000 COP** (transporte, insumos, pérdida de producción inicial).
* **Tiempo:** Entre **15 y 30 horas** de trabajo y espera invertidas.
* **Oportunidad:** Pérdidas por demora estimadas en un **15-30% de daño adicional** al cultivo.

**😤 PAIN POINTS CRÍTICOS:**
1.  **Información Contradictoria y Poco Fiable:** La consulta en WhatsApp genera más confusión que claridad, paralizando la toma de decisiones.
2.  **Lentitud en el Acceso a Conocimiento Confiable:** La brecha entre detectar un problema y obtener una recomendación fiable (incluso la sesgada de la tienda) es de días, una eternidad en una emergencia fitosanitaria.
3.  **Incertidumbre en Cada Etapa:** Desde la identificación inicial hasta la evaluación de resultados, el productor opera con un altísimo grado de duda, lo que genera estrés y decisiones subóptimas.

**⚡ MOMENTOS DE MAYOR FRICCIÓN:**
1.  **Post-Consulta en WhatsApp:** El momento en que el productor tiene 5-10 opiniones diferentes y no sabe a quién creer. Aquí es donde muchos se paralizan o toman el peor consejo.
2.  **Decisión de Compra en la Tienda:** La presión de tener que gastar una suma importante de dinero basándose en una sola recomendación comercial.
3.  **Monitoreo Post-Aplicación:** La espera ansiosa sin saber si el tratamiento caro y el trabajo duro están dando resultados.

**🎯 OPORTUNIDADES DE MEJORA:**
1.  **Diagnóstico Inmediato y Confiable:** La mayor oportunidad es reemplazar la incertidumbre de WhatsApp con un diagnóstico instantáneo, visual y basado en datos, directamente en el campo.
2.  **Recomendaciones Específicas y No Sesgadas:** Proporcionar una recomendación de tratamiento basada en la efectividad y no en el inventario de una tienda, incluyendo opciones de manejo integrado y diferentes rangos de precios.
3.  **Monitoreo Guiado y Cuantificación de Resultados:** Ayudar al usuario a seguir el progreso del tratamiento con indicadores claros y a documentar el proceso para futuros aprendizajes, cerrando el ciclo de manera efectiva.