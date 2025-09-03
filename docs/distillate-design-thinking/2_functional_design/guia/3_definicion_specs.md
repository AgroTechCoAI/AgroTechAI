### Guía para el Equipo de Producto: La Definición de Especificaciones Funcionales

¡Hola, equipo!

Bienvenidos a esta fase crucial del diseño de nuestro producto de IA para la agricultura. Soy su consultor de UI/UX y mi objetivo hoy es equiparlos con el conocimiento para construir la "Definición de Especificaciones Funcionales". Este es el puente que conecta el "qué queremos lograr" (sus JTBD y funcionalidades) con el "cómo lo vamos a diseñar y construir".

Pensemos en esto como si fuéramos a construir un tractor. Ya sabemos *por qué* el agricultor necesita el tractor (los JTBD: "Cuando llega la temporada de siembra, quiero preparar el campo rápidamente para poder maximizar mi ventana de cultivo"). Ya hemos decidido las funcionalidades clave ("Arado automático", "GPS integrado", "Asiento ergonómico").

Ahora, las especificaciones funcionales son el manual detallado que describe exactamente *qué hace* cada una de esas funcionalidades desde la perspectiva del agricultor. No es el plano del motor (eso sería una especificación técnica), sino la descripción de: "Cuando el agricultor presiona el botón verde, el arado baja y avanza a 5 km/h manteniendo una profundidad de 30 cm".

Esta claridad es fundamental para que diseñadores, desarrolladores y testers trabajen alineados, evitando ambigüedades y costosos reprocesos.

-----

### Parte 1: ¿Qué es la "Definición de Especificaciones"?

La **Definición de Especificaciones Funcionales** es un documento que describe en detalle el comportamiento de una funcionalidad del producto. Responde a la pregunta: **"¿Qué debe hacer el sistema?"** desde la perspectiva del usuario, sin entrar en detalles técnicos de implementación.

**Sus características principales son:**

  * **Centradas en el Usuario:** Se escriben en términos de acciones del usuario y respuestas del sistema.
  * **Claras y sin Ambigüedad:** No deben dejar lugar a interpretaciones. Cualquiera en el equipo debe entender lo mismo al leerlas.
  * **Completas:** Deben cubrir no solo el "camino feliz" (cuando todo sale bien), sino también los flujos alternativos, los casos de error y los casos de borde.
  * **Verificables:** Cada especificación debe poder ser probada para confirmar que la funcionalidad se ha construido correctamente.

### Parte 2: ¿Cómo se Construyen las Especificaciones?

Tomaremos el excelente trabajo que ya han realizado (JTBD, funcionalidades) y lo usaremos como materia prima. El proceso es el siguiente:

1.  **Selecciona una Funcionalidad:** Elige una de las funcionalidades que priorizaron. Por ejemplo: **"Análisis de cultivo a partir de una imagen".**
2.  **Conéctala con el JTBD:** Ten siempre a la vista el "Job to be Done" principal al que responde esta funcionalidad. Esto asegura que no perdamos el foco en el valor para el usuario.
3.  **Usa una Plantilla Estructurada:** Para asegurar la consistencia y no olvidar nada, usaremos una plantilla.

#### Plantilla de Especificación Funcional

```
// --- Inicio de la Especificación ---

**ID de Funcionalidad:** [Un identificador único, ej: DIAG-001]
**Nombre de la Funcionalidad:** Análisis de cultivo por imagen.

**Resumen (User Story):**
Como un [Arquetipo de usuario, ej: Agrónomo Junior], quiero tomar o subir una foto de una hoja de mi cultivo y recibir un diagnóstico claro, para poder tomar decisiones rápidas y precisas sobre el tratamiento a aplicar.

**Disparador (Trigger):**
El usuario presiona el botón "Realizar nuevo diagnóstico" desde la pantalla principal.

**Precondiciones:**
1. El usuario debe haber iniciado sesión en la aplicación.
2. La aplicación debe tener permisos para acceder a la cámara y/o a la galería de fotos del dispositivo.

**Flujo Principal (El "Camino Feliz"):**
1.  **Sistema:** Muestra al usuario dos opciones: "Tomar foto" y "Elegir de la galería".
2.  **Usuario:** Selecciona "Tomar foto".
3.  **Sistema:** Abre la interfaz de la cámara del dispositivo, mostrando una superposición con guías (ej: "Asegúrate de que la hoja esté bien enfocada y ocupe el centro del recuadro").
4.  **Usuario:** Captura una imagen y confirma que desea usarla.
5.  **Sistema:** Muestra una vista previa de la imagen y un campo de texto opcional para "Añadir notas". Presenta el botón "Analizar".
6.  **Usuario:** Presiona "Analizar".
7.  **Sistema:** Muestra un indicador de carga con el texto "Analizando con IA... Esto puede tardar unos segundos".
8.  **Sistema:** Al finalizar, muestra la pantalla de resultados con:
    * La imagen analizada.
    * Un título claro con el diagnóstico principal (ej: "Diagnóstico: Roya del Café").
    * Un porcentaje de confianza (ej: "Confianza del 92%").
    * Una sección de "Sugerencias" con acciones recomendadas.
    * Un botón para "Guardar en mi historial".

**Flujos Alternativos y Casos de Borde:**
* **Si el usuario elige "Elegir de la galería":** El sistema abre la galería de fotos del dispositivo para que el usuario seleccione una imagen existente.
* **Si la imagen es de baja calidad (borrosa, muy oscura):** Antes del paso 7, el sistema muestra un aviso: "La calidad de la imagen es baja. Los resultados pueden no ser precisos. ¿Deseas continuar o tomar otra foto?".
* **Si el usuario no tiene conexión a internet al presionar "Analizar":** El sistema muestra un mensaje de error: "Necesitas conexión a internet para analizar la imagen. La foto se ha guardado como borrador para que puedas intentarlo más tarde".
* **Si la IA no puede identificar nada en la imagen:** El sistema muestra un mensaje amigable: "No hemos podido identificar un cultivo o una posible afección en esta imagen. Por favor, intenta con una foto más clara y cercana a la planta".

**Reglas de Negocio:**
* El análisis no debe tardar más de 45 segundos.
* Las imágenes subidas deben estar en formato .JPG, .JPEG o .PNG.
* El tamaño máximo de la imagen es de 15 MB.

**Criterios de Aceptación:**
(Son afirmaciones verificables, ideales para el equipo de QA)
* **Dado** que estoy en la pantalla de diagnóstico, **cuando** selecciono "Tomar foto", **entonces** la cámara se abre correctamente.
* **Dado** que he subido una imagen clara de una hoja con Roya, **cuando** presiono "Analizar", **entonces** el resultado muestra "Roya" con una confianza superior al 85%.
* **Dado** que intento analizar una imagen sin conexión a internet, **cuando** presiono "Analizar", **entonces** veo el mensaje de error de conectividad.

// --- Fin de la Especificación ---
```

-----

### Parte 3: Prompts

#### Creación borrador "Plantilla de Especificación Funcional"
Nuestro enfoque será colaborativo. Tú, como experto humano, proporcionarás las "semillas" de la especificación (las decisiones clave y el contexto), y la IA las hará germinar, construyendo un primer borrador estructurado que luego tu equipo revisará, corregirá y enriquecerá.

Este método les ahorrará entre el 60% y el 80% del tiempo de redacción.

**Prompt para Generar un Borrador de Especificación Funcional**

Aquí tienes un prompt diseñado para esta tarea. Fíjate bien en cómo le pedimos al humano que proporcione los ingredientes clave en la sección de CONTEXTO.
```markdown
### Asistente de Producto para la Creación de Especificaciones Funcionales

**ROL Y OBJETIVO:**

Actúa como un experimentado Product Manager y Analista Funcional especializado en software. Tu objetivo es tomar una descripción de alto nivel de una funcionalidad y, basándote en el contexto de usuario proporcionado, expandirla en un borrador de "Especificación Funcional" completo y detallado.

Tu tarea es ser metódico y proactivo. No solo debes describir el flujo ideal ("happy path"), sino también anticipar y proponer flujos alternativos, posibles casos de error y casos de borde relevantes. El resultado debe ser un documento claro que un equipo de diseño y desarrollo pueda usar como punto de partida.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono toda la información necesaria. Debes basar tu respuesta exclusivamente en estos datos.

-----

#### **1. ARQUETIPOS DE USUARIO Y JOBS TO BE DONE (JTBD)**

*(Aquí, pega el contenido de tus archivos de arquetipos y JTBD. Esto le da a la IA el "porqué" y el "para quién".)*

-----

#### **2. INFORMACIÓN CLAVE DE LA FUNCIONALIDAD A DETALLAR**

*(Esta es la sección más importante. Aquí, tú y tu equipo proporcionan las "semillas" o las decisiones de producto que la IA debe respetar. Sé breve pero claro.)*

* **Nombre de la Funcionalidad:** `[Ej: Registro de Actividades en el Cultivo]`
* **Arquetipo Principal al que se dirige:** `[Ej: Carlos, el Mayordomo Experimentado]`
* **JTBD Principal que Resuelve:** `[Ej: "Cuando aplico un producto o realizo una tarea importante en un lote, quiero dejar un registro fácil y rápido, para poder llevar un control preciso y justificar mis decisiones ante el dueño de la finca."]`
* **Descripción de Alto Nivel:** `[Ej: "Una función que permite al usuario registrar rápidamente qué actividad hizo (ej: fumigar, regar), en qué fecha y en qué lote de la finca."]`
* **Requisitos Indispensables / Decisiones Clave (¡Tu aporte humano!):**
    * (Ej: "Debe funcionar sin conexión a internet y sincronizarse después.")
    * (Ej: "El registro debe poder hacerse en menos de 30 segundos.")
    * (Ej: "Debe permitir adjuntar una foto opcional.")
    * (Ej: "Las actividades (fumigar, regar, abonar) deben estar en una lista predefinida para evitar errores de escritura.")
    * (Ej: "No debe pedir más de 5 datos para completar un registro.")

-----

**INSTRUCCIONES Y TAREAS:**

Ahora que has procesado el contexto, realiza las siguientes acciones:

1.  **Internaliza el Contexto:** Comprende profundamente al arquetipo, su necesidad (JTBD) y los requisitos indispensables que te he proporcionado.
2.  **Genera la Especificación:** Utilizando la información anterior, completa de la forma más detallada posible la "Plantilla de Especificación Funcional" que se encuentra en el formato de salida.
3.  **Sé Proactivo:**
    * Para el **Flujo Principal**, describe la secuencia de pasos más lógica y sencilla para el usuario.
    * Para los **Flujos Alternativos y Casos de Borde**, piensa en qué podría salir mal o qué otras rutas podría tomar el usuario (ej: ¿qué pasa si empieza un registro y lo cancela? ¿qué pasa si la foto es muy pesada? ¿cómo funciona la sincronización offline?).
    * Para las **Reglas de Negocio**, define las restricciones lógicas del sistema (ej: "La fecha de la actividad no puede ser en el futuro").
    * Para los **Criterios de Aceptación**, escribe afirmaciones claras y verificables en el formato "Dado... Cuando... Entonces...".

**FORMATO DE SALIDA (Usa esta plantilla exacta):**

-----

### **Borrador de Especificación Funcional**

**ID de Funcionalidad:** [Genera un ID, ej: REG-001]
**Nombre de la Funcionalidad:** [El nombre que te proporcioné]

**Resumen (User Story):**
[Constrúyela usando el arquetipo y el JTBD]

**Disparador (Trigger):**
[Describe cómo se inicia la funcionalidad]

**Precondiciones:**
[¿Qué debe ser verdad para que esto funcione?]

**Flujo Principal (El "Camino Feliz"):**
[Describe los pasos detallados de la interacción ideal]

**Flujos Alternativos y Casos de Borde:**
[Describe las variaciones, errores y casos especiales que anticipaste]

**Reglas de Negocio:**
[Define las reglas y restricciones que dedujiste]

**Criterios de Aceptación:**
[Escribe al menos 3 criterios de aceptación claros y verificables]
```


#### Evaluación Sintética con GenAI

Ahora, la parte más innovadora. Una vez que su equipo haya escrito las especificaciones para las funcionalidades clave usando la plantilla anterior, utilizaremos este prompt para que GenAI actúe como un panel de usuarios virtuales y nos dé retroalimentación temprana.

**Instrucción para el equipo:** Copien y peguen el siguiente prompt en la herramienta de GenAI y luego rellenen las secciones de `[CONTEXTO]` con la información que ya han generado.

```markdown
### Panel de Evaluación de Experiencia de Usuario Sintética

**ROL Y OBJETIVO:**

Actúa como un panel de evaluación de experiencia de usuario compuesto por los arquetipos que te proporcionaré. Tu objetivo principal es analizar un conjunto de "Especificaciones Funcionales" para un nuevo producto de software agrícola. No debes evaluar el código ni la tecnología, sino la **experiencia conceptual** que estas especificaciones describen.

Tu tarea es simular cómo cada arquetipo de usuario reaccionaría a estas funcionalidades. Debes identificar puntos de confusión, fricción, preguntas no resueltas y evaluar si la funcionalidad realmente resuelve sus problemas (sus "Jobs to be Done"). Tu feedback debe ser crítico, constructivo y siempre desde la perspectiva del usuario que estás representando.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono toda la información necesaria. Debes internalizarla por completo antes de proceder.

-----

#### 1. ARQUETIPOS DE USUARIO

*(Aquí, el equipo debe pegar el contenido completo de su archivo de arquetipos. Por ejemplo: `1_arquetipo_resultado.md`)*

**Ejemplo:**
* **Carlos, el Mayordomo Experimentado (55 años):** Pragmatico, poca paciencia con la tecnología complicada. Valora la rapidez y la confianza. Su mayor miedo es fallarle al dueño de la finca.
* **Laura, la Agrónoma Junior (28 años):** Digitalmente hábil, busca precisión y datos para respaldar sus recomendaciones. Quiere demostrar su valía y usar herramientas modernas.
* **... (y otros arquetipos)**

-----

#### 2. JOBS TO BE DONE (JTBD) CLAVE

*(Aquí, el equipo debe pegar los JTBD más importantes que el producto busca resolver, para que la IA tenga claro el "porqué" de cada funcionalidad.)*

**Ejemplo:**
* **JTBD Agrónoma:** "Cuando visito un cultivo y encuentro una plaga desconocida, quiero identificarla rápidamente y conocer su tratamiento, para poder dar una recomendación fiable en el momento y ser percibida como una profesional eficiente."
* **JTBD Mayordomo:** "Cuando uno de mis trabajadores me muestra una hoja enferma, quiero saber qué tan grave es el problema de inmediato, para poder decidir si debo llamar al agrónomo o si puedo solucionarlo yo mismo y así no perder tiempo ni dinero."

-----

#### 3. ESPECIFICACIONES FUNCIONALES A EVALUAR

*(Aquí, el equipo debe pegar las especificaciones funcionales que han creado usando la plantilla que les proporcioné. Pueden pegar una o varias.)*

**Ejemplo:**
**ID de Funcionalidad:** DIAG-001
**Nombre de la Funcionalidad:** Análisis de cultivo por imagen.
**(Pegar aquí el resto de la especificación: User Story, Flujo Principal, Flujos Alternativos, etc.)**

-----

**INSTRUCCIONES Y TAREAS:**

Ahora que has procesado todo el contexto, sigue estos pasos de forma rigurosa:

**Paso 1: Internalización Profunda**
Lee y comprende a fondo cada arquetipo, sus motivaciones, sus miedos y sus JTBD. Asimila completamente las especificaciones funcionales que se van a evaluar.

**Paso 2: Simulación de "Lectura Crítica" por Arquetipo**
Para CADA especificación funcional proporcionada, vas a realizar el siguiente análisis desde la perspectiva de CADA uno de los arquetipos. No mezcles sus personalidades.

Adopta la personalidad del arquetipo y, mientras "lees mentalmente" el flujo de la funcionalidad, responde a estas preguntas en primera persona:

1.  **Reacción Inicial:** "Al leer lo que esta función hace, ¿mi primera impresión es de interés, confusión, escepticismo o entusiasmo? ¿Por qué?"
2.  **Claridad del Proceso:** "Siguiendo el 'Flujo Principal', ¿hay algún paso que no entiendo o que me parece complicado? ¿El lenguaje usado tiene sentido para alguien como yo?"
3.  **Resolución del Problema (JTBD):** "¿Esto realmente me ayuda a lograr lo que quiero (mi JTBD)? ¿Siento que me da el control, la seguridad o la rapidez que necesito?"
4.  **Preguntas y Dudas:** "¿Qué preguntas me surgen inmediatamente? Por ejemplo: '¿Y qué pasa si no tengo buena señal?', '¿Cuánto cuesta cada análisis?', '¿Puedo confiar en la IA más que en mi propia experiencia?'"
5.  **Puntos de Fricción:** "¿En qué parte del proceso creo que podría frustrarme, rendirme o cometer un error? ¿Quizás al tomar la foto, al interpretar los resultados?"
6.  **Funcionalidad Faltante:** "Leyendo esto, ¿siento que falta algo? ¿Hay alguna pequeña cosa que, si la tuviera, haría que todo fuera mucho más útil para mí?"

**Paso 3: Formateo de la Salida**
Presenta tus hallazgos de forma organizada y clara. Utiliza el siguiente formato para estructurar tu respuesta.

-----

### Resultados: Evaluación Sintética de Especificaciones

#### Funcionalidad Evaluada: `[Nombre de la Funcionalidad, ej: Análisis de cultivo por imagen]`

-----

#### Evaluación desde la perspectiva de: `[Nombre del Arquetipo 1]`

* **Resumen de la Reacción:** `[1-2 frases que resuman la opinión general del arquetipo sobre la funcionalidad.]`
* **Claridad y Facilidad de Uso (Puntuación: X/5):** `[Una puntuación y una breve justificación.]`
* **Relevancia para su JTBD (Puntuación: X/5):** `[Una puntuación y justificación sobre si resuelve su problema.]`

* **Feedback Detallado:**
    * **Puntos de Confusión y Preguntas:**
        * (Ej: "¿Qué significa 'confianza del 92%'? ¿Significa que hay un 8% de probabilidad de que esté equivocado? Eso me pone nervioso.")
        * (Ej: "No entiendo por qué necesito 'Añadir notas'. Yo solo quiero la respuesta.")
    * **Posibles Fricciones y Frustraciones:**
        * (Ej: "Me frustraría mucho si después de tomar la foto perfecta, la app me dice que la calidad es baja. Debería ayudarme a tomarla bien desde el principio.")
        * (Ej: "Si el análisis tarda más de 15 segundos, probablemente cierre la app y me olvide.")
    * **Sugerencias y Funcionalidades Faltantes:**
        * (Ej: "Me gustaría que, junto al diagnóstico, me mostrara fotos de referencia de otros casos para comparar.")
        * (Ej: "Debería haber un botón para llamar directamente al agrónomo desde la pantalla de resultados si el problema es muy grave.")

* **Cita Clave Simulada:**
    > *"Suena útil, pero si no me da una respuesta directa y en la que pueda confiar al 100%, seguiré llamando a Don Manuel, que lleva 40 años en esto."*

-----

#### Evaluación desde la perspectiva de: `[Nombre del Arquetipo 2]`

**(Repetir toda la estructura anterior para el segundo arquetipo, y así sucesivamente para todos los arquetipos proporcionados).**

```