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

---

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

***

# **JOURNEY AS-IS 2: Consulta Técnica Pagada con Demoras**

**📋 INFORMACIÓN GENERAL**
* **Arquetipo principal:** Productora Mediana (Diana Cárdenas, productora de Aguacate Hass).
* **Situación que dispara el journey:** Durante una revisión de calidad pre-cosecha, Diana detecta manchas negras sospechosas en varios frutos de aguacate, lo que pone en riesgo el cumplimiento de un contrato de exportación.
* **Método actual principal:** Contacto directo con su agrónoma asesora de confianza para agendar una visita técnica pagada.
* **Frecuencia típica:** Moderada, 2-4 veces por ciclo de cultivo para validaciones críticas o problemas complejos.
* **Duración total actual:** De 4 a 8 días desde la detección hasta la aplicación del tratamiento recomendado.
* **Recursos/herramientas actuales:** Smartphone (WhatsApp Business, llamadas), presupuesto para consultoría ($1.5-3M COP/mes o $200-500K COP por visita), registros en Excel, su propio vehículo para recorrer la finca.

---

## **🗺️ PROCESO ACTUAL (AS-IS)**

### **FASE 1: DETECCIÓN DEL PROBLEMA**
**Cómo actualmente identifica problemas en el cultivo**

**🎬 SITUACIÓN ACTUAL:**
* **Ubicación:** En un lote de aguacates Hass destinado a exportación en el Oriente antioqueño.
* **Momento:** Durante una inspección semanal programada para evaluar el calibre y la sanidad de la fruta.
* **Método de detección:** Visual y metódico. Utiliza su experiencia para diferenciar daños mecánicos de posibles patógenos. Las manchas son circulares y hundidas, un patrón que le preocupa.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Toma varias fotos en alta resolución con su smartphone, asegurándose de capturar el patrón de la lesión, la distribución en el árbol y la ubicación del lote. Marca los árboles afectados con cinta.
* **Pensamientos:** *"Esto parece antracnosis. Si se extiende, la exportadora me va a rechazar el contenedor completo. Necesito que Laura (su agrónoma) lo vea ya mismo. No puedo arriesgarme."*
* **Emociones:** Preocupación financiera, estrés por el cumplimiento del contrato, urgencia profesional.
* **Herramientas:** Smartphone, cintas de marcación, cuaderno de notas o Excel en el celular.

**⏱️ TIEMPO INVERTIDO:** 1 - 2 horas.

**😤 FRUSTRACIONES ACTUALES:**
* Aunque tiene una sospecha informada, no tiene la certeza del 100% para iniciar un tratamiento costoso.
* Sabe que cada hora que pasa es crítica para la calidad de la fruta y el control de la enfermedad.

**💸 COSTOS ACTUALES:**
* El costo de su tiempo y el inicio de la posible pérdida de valor de la cosecha.

---

### **FASE 2: INVESTIGACIÓN Y DIAGNÓSTICO INICIAL**
**Cómo actualmente intenta diagnosticar el problema**

**🎬 SITUACIÓN ACTUAL:**
* **Recursos consultados:** Su agrónoma asesora independiente.
* **Personas contactadas:** Llama o escribe por WhatsApp Business a "Laura Restrepo".
* **Herramientas usadas:** Celular.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Le envía a Laura las fotos por WhatsApp con un mensaje de voz: *"Laurita, buen día. Estoy viendo estas manchas en el lote 7, el de exportación. Parece antracnosis, ¿cuándo podrías venir? Es urgente."*
* **Pensamientos:** *"Ojalá tenga espacio en su agenda esta semana. Sé que está muy ocupada. Mientras tanto, no puedo hacer nada, no voy a aplicar un fungicida caro sin su visto bueno."*
* **Emociones:** Ansiedad por la espera. La respuesta de Laura llega una hora después: *"Diana, qué tal. Sí parece eso. Estoy terminando una visita en Jardín. Lo más pronto que puedo ir es en 3 días."* La frustración aumenta.
* **Criterios de decisión:** Confía plenamente en su asesora, por lo que su única opción es esperar.

**⏱️ TIEMPO INVERTIDO:** **2 a 7 días de espera** para la visita técnica.

**🔧 TOUCHPOINTS ACTUALES:**
* Llamada directa y WhatsApp Business con la agrónoma.

**😤 FRUSTRACIONES ACTUALES:**
* **La disponibilidad limitada del experto es el mayor pain point.** La enfermedad avanza mientras ella espera.
* El diagnóstico preliminar por foto es útil pero no definitivo, lo que le impide tomar acciones inmediatas.
* El costo de la inacción durante la espera es alto y se acumula día a día.

**💸 COSTOS ACTUALES:**
* **Costo de oportunidad:** Pérdidas estimadas del 15-30% de daño adicional por el retraso en el diagnóstico y tratamiento.

---

### **FASE 3: BÚSQUEDA DE SEGUNDA OPINIÓN (Visita del Experto)**
**Cómo valida su diagnóstico inicial**

**🎬 SITUACIÓN ACTUAL:**
* **Fuentes de validación:** La visita presencial de la agrónoma.
* **Métodos de comunicación:** Interacción cara a cara en la finca.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Recorre el lote con Laura. Le muestra los árboles marcados y los registros que ha tomado. Laura usa una lupa de campo, toma sus propias notas y posiblemente muestras para el laboratorio si el caso es complejo.
* **Pensamientos:** *"Finalmente. Ahora sí vamos a saber qué hacer. Vale la pena pagar la visita para tener esta tranquilidad y un plan de acción claro."*
* **Emociones:** Alivio, confianza. Se siente empoderada al recibir información experta.

**⏱️ TIEMPO INVERTIDO:** 2 - 4 horas de la visita técnica.

**😤 FRUSTRACIONES ACTUALES:**
* El alto costo de la visita ($200K - $500K COP), que se suma a los costos del tratamiento.
* A veces, incluso el experto puede necesitar una confirmación de laboratorio, lo que añade otra semana de espera y más costos.

**💸 COSTOS ACTUALES:**
* Honorarios de la agrónoma: **$200,000 - $500,000 COP**.

---

### **FASE 4: TOMA DE DECISIÓN**
**Cómo decide qué tratamiento aplicar**

**🎬 SITUACIÓN ACTUAL:**
* **Proceso de decisión:** Al final de la visita, Laura le presenta un diagnóstico confirmado y 2-3 opciones de tratamiento, explicando los pros y contras de cada uno (costo, efectividad, residualidad).
* **Factores considerados:** Efectividad del tratamiento, costo/beneficio, período de carencia (importante para la exportación), y la recomendación específica de la experta.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Discute el plan con Laura. Toman una decisión conjunta basada en los datos. Laura le envía el plan de acción detallado por correo electrónico o WhatsApp Business.
* **Pensamientos:** *"La opción A es la más efectiva pero también la más cara. La B es más barata pero podría necesitar una segunda aplicación. Con el contrato en juego, no puedo arriesgar. Vamos con la A."*
* **Emociones:** Determinación, claridad. La incertidumbre ha sido reemplazada por un plan de acción.

**⏱️ TIEMPO INVERTIDO:** 30 minutos de análisis y decisión.

**😤 FRUSTRACIONES ACTUALES:**
* Las soluciones más efectivas suelen ser las más costosas, presionando su presupuesto.
* Debe confiar en que la recomendación es la mejor y no está influenciada por relaciones comerciales del agrónomo.

**💸 COSTOS ACTUALES:**
* El costo mental de aprobar un gasto significativo.

---

### **FASE 5, 6, 7 y 8: ADQUISICIÓN, APLICACIÓN, MONITOREO Y EVALUACIÓN**
Estas fases son similares al journey anterior, pero con un mayor nivel de profesionalismo:

* **Adquisición:** Compra insumos específicos en distribuidores regionales, no solo en la tienda local, buscando calidad y disponibilidad garantizada.
* **Aplicación:** Supervisa a su equipo o a su mayordomo para asegurar que la aplicación se haga siguiendo el protocolo exacto de la agrónoma (dosis, calibración de equipos, EPP).
* **Monitoreo:** Es sistemático. Toma fotos de seguimiento y se las envía a la agrónoma para una evaluación remota. Documenta el progreso en sus registros.
* **Evaluación:** El éxito se mide con KPIs claros: reducción del % de fruta rechazada, control efectivo de la enfermedad. El aprendizaje se documenta formalmente para ajustar el plan de manejo del próximo ciclo. La efectividad del tratamiento es alta (75-90%).

---

## **📊 ANÁLISis DEL JOURNEY AS-IS**

**⏱️ TIEMPOS TOTALES:**
* Desde detección hasta inicio de tratamiento: **4 - 8 días**.
* Proceso completo hasta evaluación: **3 - 5 semanas**.

**💰 COSTOS TOTALES:**
* **Monetarios:** **$500,000 - $2,000,000 COP** (visita técnica + insumos de alta gama + pérdida de fruta durante la espera).
* **Tiempo:** 6 - 10 horas de su propio tiempo directivo.
* **Oportunidad:** La pérdida de valor de la cosecha por el avance de la enfermedad durante los días de espera.

**😤 PAIN POINTS CRÍTICOS:**
1.  **El Tiempo de Espera del Experto:** Es el cuello de botella más costoso y frustrante. El sistema depende de la disponibilidad de un recurso humano escaso, lo que crea un retraso inaceptable en situaciones críticas.
2.  **Alto Costo Acumulado:** El costo de la visita experta, sumado a los tratamientos recomendados (que suelen ser caros), representa una inversión significativa y un riesgo financiero.
3.  **Dependencia de una Sola Persona:** Todo el proceso se detiene si su agrónomo de confianza no está disponible, creando un punto único de fallo.

**🎯 OPORTUNIDADES DE MEJORA:**
1.  **Triaje y Diagnóstico Preliminar Inmediato:** Ofrecer una herramienta de IA que le dé a Diana un diagnóstico preliminar con un alto grado de confianza (>85%) en minutos, no en días. Esto le permitiría tomar acciones de contención inmediatas mientras espera al experto.
2.  **Empoderar al Experto Remotamente:** Crear un canal donde la agrónoma pueda recibir datos estructurados y de alta calidad (fotos guiadas, historial del lote, clima) para dar una recomendación remota más rápida y precisa, quizás convirtiendo la visita física en una excepción y no en la regla.
3.  **Optimización de Decisiones:** Utilizar datos para comparar la efectividad y el costo de diferentes tratamientos, ayudando a Diana a tomar la decisión más rentable sin sacrificar la calidad de exportación.

***

# **JOURNEY AS-IS 3: Diagnóstico por Experiencia y Prueba y Error**

**📋 INFORMACIÓN GENERAL**
* **Arquetipo principal:** Administrador/Mayordomo de Finca (Luis Alberto Mosquera, en una finca de banano en Urabá).
* **Situación que dispara el journey:** Durante una ronda de supervisión, Luis identifica síntomas que él reconoce como un problema recurrente y bien conocido en la finca, como un brote inicial de Sigatoka Negra.
* **Método actual principal:** Autodiagnóstico basado en su amplia experiencia de campo y aplicación inmediata del protocolo o tratamiento estándar de la finca, sin buscar una segunda opinión externa.
* **Frecuencia típica:** Muy alta. Es el mecanismo por defecto para el 80% de los problemas "conocidos".
* **Duración total actual:** Muy rápido para iniciar (2-4 horas), pero el ciclo completo puede ser largo y fallido si el diagnóstico fue incorrecto.
* **Recursos/herramientas actuales:** Su experiencia, protocolos de la finca (a veces solo mentales), equipo de aplicación, y el inventario de insumos en la bodega de la finca.

---

## **🗺️ PROCESO ACTUAL (AS-IS)**

### **FASE 1: DETECCIÓN DEL PROBLEMA**
**🎬 SITUACIÓN ACTUAL:**
* **Ubicación:** Un sector de una finca bananera grande en Urabá.
* **Momento:** Supervisando a la cuadrilla de trabajo a media mañana.
* **Método de detección:** Ojo entrenado. Reconoce el patrón de las manchas de Sigatoka casi instantáneamente.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Se acerca, evalúa visualmente la severidad y la extensión del brote. No duda.
* **Pensamientos:** *"Esto es Sigatoka, etapa 2. Ya sabemos cómo manejarla. Si no actuamos hoy, para el fin de semana se nos contamina todo el lote. Hay que aplicar el fungicida de rotación que toca esta semana."*
* **Emociones:** Confianza, proactividad, sentido del deber. No hay pánico, es "business as usual".
* **Herramientas:** Su vista y su memoria.

**⏱️ TIEMPO INVERTIDO:** 5 - 10 minutos.

### **FASE 2 Y 3: INVESTIGACIÓN Y SEGUNDA OPINIÓN (Omitidas)**
**Cómo actualmente intenta diagnosticar el problema**

**🎬 SITUACIÓN ACTUAL:**
* Luis **no investiga ni busca una segunda opinión** para problemas que considera rutinarios. Su rol es ejecutar rápidamente, y consultar al ingeniero de la empresa (que puede estar en otra finca o en la oficina) por cada brote de Sigatoka sería visto como ineficiente y una falta de autonomía.
* Su "base de conocimiento" es la experiencia acumulada y los protocolos establecidos.

**😤 FRUSTRACIONES ACTUALES (Latentes):**
* El riesgo oculto: ¿Y si no es la cepa habitual de Sigatoka? ¿Y si los síntomas son similares pero la causa es otra (ej. una deficiencia nutricional o un nuevo patógeno)?
* La experiencia puede generar un "sesgo de confirmación", viendo lo que espera ver.

---

### **FASE 4: TOMA DE DECISIÓN**
**Cómo decide qué tratamiento aplicar**

**🎬 SITUACIÓN ACTUAL:**
* **Proceso de decisión:** Instantáneo y basado en el protocolo.
* **Factores considerados:** El calendario de rotación de fungicidas de la finca (para evitar resistencia), la disponibilidad de personal y equipos, y el pronóstico del tiempo.

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Llama por radio o WhatsApp al jefe de cuadrilla. *"Preparen la mezcla del fungicida X para el lote 12. Aplicación inmediata."*
* **Pensamientos:** *"Listo. Problema visto, problema siendo solucionado. Puedo pasar al siguiente tema."*
* **Emociones:** Eficiencia, control.

**⏱️ TIEMPO INVERTIDO:** 2 minutos.

---

### **FASE 5 Y 6: ADQUISICIÓN Y APLICACIÓN**
**Cómo obtiene y aplica la solución**

* **Adquisición:** No hay compra. Luis va a la bodega de la finca y solicita los insumos del inventario.
* **Aplicación:** Dirige y supervisa a su equipo para que realice la aspersión según los estándares de la finca. Se enfoca en la eficiencia operativa: hectáreas cubiertas por hora.

**⏱️ TIEMPO INVERTIDO:** 4 - 6 horas para la aplicación en el lote afectado.

---

### **FASE 7: MONITOREO DE RESULTADOS (EL MOMENTO DE LA VERDAD)**
**Cómo evalúa si el tratamiento está funcionando**

**🎬 SITUACIÓN ACTUAL:**
* **Frecuencia de revisión:** En sus rondas diarias durante la siguiente semana.
* **Método de evaluación:** Visual.

**👤 COMPORTAMIENTO ACTUAL:**
* **Escenario A (Éxito):** Las lesiones se secan y la propagación se detiene. **Pensamientos:** *"Perfecto, el protocolo funcionó como siempre."* **Emociones:** Satisfacción. El ciclo termina aquí.
* **Escenario B (Fracaso):** Las lesiones continúan expandiéndose. El tratamiento no tuvo efecto. **Pensamientos:** *"Carajo. Esto no está funcionando. ¿Por qué? ¿Usamos la dosis incorrecta? ¿El producto está malo? ¿O no es Sigatoka...?"* **Emociones:** Duda, frustración, preocupación por tener que reportar el fallo a su jefe.

**⏱️ TIEMPO INVERTIDO:** 10 minutos diarios durante una semana.

### **FASE 8: EVALUACIÓN FINAL Y APRENDIZAJE (EN CASO DE FRACASO)**
**Cómo determina si fue exitoso y qué aprendió**

**🎬 SITUACIÓN ACTUAL:**
* El tratamiento estándar falló. El problema se ha agravado.
* Ahora la situación pasó de "rutinaria" a "crítica".

**👤 COMPORTAMIENTO ACTUAL:**
* **Acciones:** Ahora sí, contacta al ingeniero agrónomo de la empresa. Le explica la situación: "Ingeniero, aplicamos el protocolo para Sigatoka hace una semana en el lote 12, pero el problema empeoró." Inicia un nuevo journey (el **Journey 2: Consulta Técnica**), pero desde una posición mucho peor.
* **Pensamientos:** *"Perdimos tiempo valioso y gastamos insumos para nada. Ahora el daño es mayor y la solución será más cara. El jefe no va a estar contento."*
* **Emociones:** Decepción, estrés, sensación de haber fallado.

---

## **📊 ANÁLISis DEL JOURNEY AS-IS**

**⏱️ TIEMPOS TOTALES:**
* **En caso de éxito:** 1 semana.
* **En caso de fracaso:** 1 semana perdida + el tiempo del nuevo journey (4-8 días), totalizando **11-15 días** para una solución real.

**💰 COSTOS TOTALES (EN CASO DE FRACASO):**
* **Monetarios:** El costo de la aplicación fallida ($150-500K/ha en insumos) + el costo del nuevo tratamiento correcto + las pérdidas agravadas por la demora. Un error puede costar **$800K - $2M COP por hectárea**.
* **Tiempo:** Horas de trabajo del equipo desperdiciadas en la primera aplicación.
* **Oportunidad:** La ventana crítica para un control efectivo se perdió.

**😤 PAIN POINTS CRÍTICOS:**
1.  **El Alto Costo del Falso Positivo:** El mayor riesgo de este journey es la confianza ciega en la experiencia. Cuando la experiencia falla, los costos (tiempo, dinero, rendimiento) se disparan exponencialmente.
2.  **Falta de un Bucle de Retroalimentación:** El sistema no tiene un mecanismo para cuestionar el protocolo. Si un tratamiento empieza a perder efectividad (ej. por resistencia), el modelo de "prueba y error" no lo detecta hasta que el fracaso es evidente y costoso.
3.  **Invisibilidad de Problemas Nuevos:** Este journey es incapaz de identificar correctamente problemas nuevos o emergentes que se disfrazan con síntomas de problemas conocidos.

**🎯 OPORTUNIDADES DE MEJORA:**
1.  **Herramienta de Verificación Rápida:** Proporcionar a Luis una herramienta de IA que le permita, en 30 segundos, verificar su diagnóstico visual antes de movilizar a su equipo. Un "segundo ojo digital" que confirme: "Sí, 95% de probabilidad de Sigatoka Negra" o que alerte: "Alerta: se detectan patrones atípicos, podría ser una deficiencia de X. Se recomienda verificar antes de aplicar fungicida".
2.  **Sistema de Alerta Temprana de Resistencia:** Si la IA empieza a detectar que tratamientos estándar están fallando en múltiples fincas de la región para un problema específico, puede generar una alerta regional sobre posible resistencia, ayudando a ajustar los protocolos de forma proactiva.
3.  **Documentación Automática de Aplicaciones:** Permitir que Luis registre cada aplicación con una foto y geolocalización. Esto crea un historial invaluable para la finca, permitiendo correlacionar tratamientos con resultados y optimizar protocolos basándose en datos reales, no solo en la memoria.