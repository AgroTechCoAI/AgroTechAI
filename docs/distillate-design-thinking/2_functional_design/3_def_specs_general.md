# Construcción de la "Definición de especificaciones"

## Contexto

El equipo acaba de terminar su fase de investigación y ha priorizado la funcionalidad más importante: "Diagnóstico por Imagen". 
Saben que sus usuarios principales son pragmáticos y algunos desconfían de la tecnología complicada.
El éxito depende de que esta funcionalidad sea increíblemente simple y fiable.

Por tal razon, esta fase se compone de dos prompts:

### Fase 1: La Creación Asistida del Borrador especificaciones funcionales

**Objetivo:** Crear un borrador detallado de la especificación funcional para "Diagnóstico por Imagen" de forma rápida, sin empezar desde una página en blanco.

### Fase 2: La Evaluación Sintética a través de GEN AI

**Objetivo:** "Probar en carretera" la especificación funcional v1.0 desde la perspectiva de sus usuarios clave antes de que David dibuje una sola pantalla.

## Herramientas

Para su construcción se usaron las siguientes herramientas:
- **ChatGPT**
- **Gemini**
- **Claude**

---

## Prompt

### Fase 1: La Creación Asistida del Borrador especificaciones funcionales

Por cada funcionalidad que deseamos generar especificaciones, debemos ejecutar el siguiente prompt.

```markdown
## Analista de Producto IA para Síntesis y Creación de Especificaciones

**ROL Y OBJETIVO:**

Actúa como un Analista de Producto Senior con alta capacidad de síntesis. Tu primer objetivo es analizar en profundidad los artefactos de investigación "As-Is" (Journey Maps, System Maps) para identificar los puntos de dolor, cuellos de botella y oportunidades más relevantes para una funcionalidad específica.

Tu segundo objetivo es, basándote en tu análisis y respetando los "restricciones estratégicos" proporcionados, generar un borrador de "Especificación Funcional" detallado y accionable que apunte a resolver los problemas identificados.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono toda la información necesaria. Debes basar tu respuesta exclusivamente en estos datos.

-----

#### 1. ARQUETIPOS DE USUARIO (Contenido del archivo Markdown de Arquetipos)

Toma como referencia los arquetipos seleccionados en las FASES 3 y 4 de la base de conocimiento que te he suministrado, especificamente en el archivo `1_arquetipos_resultados.md`

-----

#### 2. SYSTEM MAPS AS-IS (Contenido del archivo Markdown de System Maps)

Toma como referencia el systema maps que te he suministrado en la base de tu conocimiento, especificamente en el archivo `2_systemmaps-as-is_resultado.md`

-----

#### 3. JOURNEY MAPS AS-IS (Contenido del archivo Markdown de Journey Maps)

Toma como referencia el journey maps que te he suministrado en la base de tu conocimiento, especificamente en el archivo  `3_journeymaps-as-is_resultado.md`

-----

### 4. JOBS TO BE DONE (JTBD)

Toma como referencia los Jobs to be done que te he suministrado en la base de tu conocimiento, especificamente en el archivo  `1_jtbd_resultado.md`

-----

### **4. FUNCIONALIDAD A DETALLAR Y RESTRICCIONES ESTRATÉGICAS (Aporte Humano)**

Esta sección será recibida como entrada del usuario al momento de solicitar la generación de una especificación, porfa solicitala en caso de que no se te incluya.

* **Nombre de la Funcionalidad a Enfocar:** `[Ej: Diagnóstico por Imagen]`
* **Restricciones Estratégicas:**
    * (Ej: "Enfoque principal: Reducir la incertidumbre y el tiempo de espera identificados en el Journey Map.")
    * (Ej: "La solución debe ser 100% móvil y funcionar en condiciones de baja conectividad.")
    * (Ej: "Presupuesto para esta funcionalidad: Bajo. Evitar soluciones que requieran hardware externo o integraciones complejas con terceros.")
    * (Ej: "Priorizar la simplicidad para el arquetipo 'Carlos, el Mayordomo', incluso si eso significa menos funcionalidades avanzadas.")

-----

**INSTRUCCIONES Y TAREAS:**

Realiza el siguiente proceso en dos pasos:

**Paso 1: Análisis y Síntesis de Oportunidades**
Analiza el Journey Map y el System Map. Identifica y lista en formato de viñetas los 3-5 principales puntos de dolor y oportunidades que la funcionalidad de `[Nombre de la Funcionalidad a Enfocar]` podría resolver, según el contexto proporcionado.

**Paso 2: Generación de la Especificación**
Basándote ESTRICTAMENTE en tu análisis del Paso 1 y respetando TODOS los `restricciones Estratégicos`, genera el borrador de la Especificación Funcional. Utiliza la plantilla proporcionada en el formato de salida. Sé proactivo al sugerir flujos y casos de borde que directamente aborden los problemas que identificaste.

**FORMATO DE SALIDA:**

-----

## **1. Síntesis de Oportunidades (Extraído de los Mapas)**

* **Punto de Dolor Identificado:** [Ej: Larga espera (hasta 48h) para recibir feedback del agrónomo después de enviar una foto por WhatsApp.]
* **Oportunidad:** [Ej: Ofrecer un diagnóstico preliminar instantáneo para permitir una primera acción rápida.]
* **Punto de Dolor Identificado:** [Ej: Incertidumbre al no saber si la foto enviada es de suficiente calidad para el diagnóstico.]
* **Oportunidad:** [Ej: Crear una guía en la cámara para ayudar al usuario a tomar una foto de buena calidad.]
* ... (y así sucesivamente)

-----

## **2. Borrador de Especificación Funcional**

**ID de Funcionalidad:** [Genera un ID]
**Nombre de la Funcionalidad:** [El nombre proporcionado]

**Resumen (User Story):**
[Constrúyela a partir del análisis]

**(Y así sucesivamente, completando el resto de la plantilla: Trigger, Precondiciones, Flujo Principal, Flujos Alternativos, Reglas de Negocio, Criterios de Aceptación).**
```

### Fase 2: La Evaluación Sintética a través de GEN AI

Con las especificaciones generadas en la Fase 1, ejecutamos el siguiente prompt:

```markdown
# Panel de Evaluación de Experiencia de Usuario Sintética

## ROL Y OBJETIVO

Actúa como un panel de evaluación de experiencia de usuario compuesto por los arquetipos que te proporcionaré. Tu objetivo principal es analizar un conjunto de "Especificaciones Funcionales" para un nuevo producto de software agrícola. No debes evaluar el código ni la tecnología, sino la **experiencia conceptual** que estas especificaciones describen.

Tu tarea es simular cómo cada arquetipo de usuario reaccionaría a estas funcionalidades. Debes identificar puntos de confusión, fricción, preguntas no resueltas y evaluar si la funcionalidad realmente resuelve sus problemas (sus "Jobs to be Done"). Tu feedback debe ser crítico, constructivo y siempre desde la perspectiva del usuario que estás representando.

## CONTEXTO (INFORMACIÓN DE ENTRADA)

A continuación, te proporciono toda la información necesaria. Debes internalizarla por completo antes de proceder.

---

### 1. ARQUETIPOS DE USUARIO

Esta información la podras tomar de la base de conocimiento suministrada en el archivo `1_arquetipo_resultado.md`

---

### 2. JOBS TO BE DONE (JTBD) CLAVE

Esta información la podras tomar de la base de conocimiento suministrada en el archivo `1_jtbd_resultado.md`

---

### 3. ESPECIFICACIONES FUNCIONALES A EVALUAR

Esta información será suministra en un archivo *.md por parte del usuario, porfa solicitala en caso de que no te llegue o no sea claro para vos cómo interpretarlo.

**Ejemplo:**
**ID de Funcionalidad:** DIAG-001
**Nombre de la Funcionalidad:** Análisis de cultivo por imagen.
**(Pegar aquí el resto de la especificación: User Story, Flujo Principal, Flujos Alternativos, etc.)**

---

## INSTRUCCIONES Y TAREAS

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

## Resultados: Evaluación Sintética de Especificaciones

### Funcionalidad Evaluada: `[Nombre de la Funcionalidad, ej: Análisis de cultivo por imagen]`

-----

### Evaluación desde la perspectiva de: `[Nombre del Arquetipo 1]`

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

### Evaluación desde la perspectiva de: `[Nombre del Arquetipo 2]`

**(Repetir toda la estructura anterior para el segundo arquetipo, y así sucesivamente para todos los arquetipos proporcionados).**

```
