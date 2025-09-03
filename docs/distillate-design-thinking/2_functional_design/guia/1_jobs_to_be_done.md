### **Guía de Consultoría: Descubriendo los "Jobs to be Done" para una IA Agrícola**

¡Hola, equipo! Es un placer colaborar con ustedes en este proyecto tan innovador. El objetivo de esta sesión es equiparlos con una de las herramientas más potentes del diseño de productos: el marco **Jobs to be Done (JTBD)**. Al finalizar, no solo entenderán la teoría, sino que sabrán cómo aplicarla para crear los prompts que alimentarán su estudio con IA y descubrirán las verdaderas necesidades de sus usuarios.

Vamos a romper el mercado, y todo empieza por entender el "trabajo" que sus usuarios necesitan resolver.

***

## **1. ¿Qué son los "Jobs to be Done" (JTBD)?** 🤔

En esencia, **Jobs to be Done** es una perspectiva que cambia el foco de atención. En lugar de centrarnos en el usuario (su demografía) o en el producto (sus características), nos enfocamos en el **"trabajo"** que una persona está tratando de realizar en una circunstancia particular.

Piénsenlo de esta manera: los usuarios "contratan" productos o servicios para hacer un trabajo. Nadie compra un taladro de un cuarto de pulgada porque quiera un taladro; lo compran porque quieren un agujero de un cuarto de pulgada. El taladro es la solución que "contratan".

En su caso, un agricultor no quiere necesariamente una "app con IA que analiza imágenes". Lo que realmente quiere es **"mantener su cultivo sano y productivo con el mínimo esfuerzo y riesgo"**. Ese es el trabajo principal. Su app es la solución que él podría contratar para hacer ese trabajo de manera más eficiente que sus métodos actuales.

### **Tipos de Jobs**

Un "job" no es solo funcional, también tiene dimensiones emocionales y sociales que son clave para el diseño:

* **Job Funcional:** Es el núcleo práctico de la tarea.
    * *Ejemplo:* "Determinar si la mancha en una hoja es un hongo o una deficiencia de nitrógeno".
* **Job Emocional:** Cómo quiere sentirse el usuario al realizar el trabajo.
    * *Ejemplo:* "Sentirme seguro y en control de la salud de mi cultivo", o "reducir la ansiedad de perder la cosecha".
* **Job Social:** Cómo quiere ser percibido por otros al realizar el trabajo.
    * *Ejemplo:* "Ser visto como un agricultor moderno y eficiente por mis colegas y empleados".

Ignorar las dimensiones emocionales y sociales es dejar pasar oportunidades de oro para crear un producto que la gente ame y no solo use.



***

## **2. ¿Cómo se construyen los JTBD? ✍️**

Para capturar la esencia de un "job", usamos una estructura simple pero poderosa. Un buen JTBD no describe lo que el usuario está haciendo, sino que describe **el progreso que está intentando alcanzar**.

La sintaxis recomendada es:

**Cuando `[SITUACIÓN]`**, **quiero `[MOTIVACIÓN]`**, **para poder `[RESULTADO ESPERADO]`**.

Desglosemos cada parte:

* **Situación (When...):** Es el contexto, el detonante. ¿Qué está pasando en el mundo del usuario que lo impulsa a actuar? Es el momento en que se da cuenta de que necesita hacer algo.
    * *Ejemplo:* "Cuando estoy recorriendo el lote y veo un amarillamiento irregular en un sector de mis plantas..."
* **Motivación (I want to...):** Es el objetivo, la meta. Es crucial que esta parte esté libre de cualquier solución tecnológica. No es "quiero usar una app", sino "quiero entender la causa del problema".
    * *Ejemplo:* "...quiero diagnosticar la causa raíz de manera inmediata..."
* **Resultado Esperado (So I can...):** Es la visión de un futuro mejor. ¿Cómo mejora la vida del usuario una vez que el trabajo está hecho? Es el verdadero porqué.
    * *Ejemplo:* "...para poder aplicar el tratamiento correcto antes de que afecte el rendimiento de la cosecha y mis ganancias".

### **Ejemplos para su producto agrícola:**

Aquí tienen algunos JTBD construidos que podrían surgir de su investigación:

* **Para un Agrónomo:**
    * **Cuando** estoy asesorando a varios agricultores a la vez, **quiero** priorizar qué fincas necesitan mi atención urgente, **para poder** ofrecer un servicio más eficaz y retener a mis clientes.
* **Para el Dueño de la Finca:**
    * **Cuando** debo decidir si invertir en un nuevo fertilizante, **quiero** tener una predicción fiable del impacto en mi producción, **para poder** tomar decisiones financieras con menos riesgo.
* **Para un Trabajador de Campo (Mayordomo):**
    * **Cuando** encuentro una plaga que no reconozco, **quiero** identificarla y conocer su tratamiento sin tener que esperar al agrónomo, **para poder** actuar rápido y demostrar mi capacidad y responsabilidad.

***

## **3. Prompt para la Investigación Sintética con GenAI 🤖**

Ahora, la parte práctica. Usarán los arquetipos, el system map y el journey map que ya tienen para darle a la IA un contexto profundo y realista. El objetivo es que la IA no invente información, sino que **actúe como su arquetipo** basándose en la realidad que ustedes ya investigaron.

Este prompt está diseñado para ser una plantilla. Deberán copiarlo y pegarlo junto con los archivos de la fase de investigación.

```markdown
### **Prompt Maestro para Descubrir y Formatear Jobs to be Done (JTBD)**

**ROL Y OBJETIVO:**

Actúa como un experto en investigación de experiencia de usuario y estrategia de producto, especializado en la metodología "Jobs to be Done" (JTBD). Tu objetivo principal es analizar en profundidad la información contextual que te proporcionaré (arquetipos, system maps, journey maps) para identificar las luchas, motivaciones y resultados deseados de los usuarios.

Tu tarea final será destilar esta información en una serie de "Jobs to be Done" claros y accionables, presentados con un formato profesional y fácil de entender para un equipo de diseño y producto. No debes inventar soluciones ni funcionalidades; tu foco absoluto está en definir el problema desde la perspectiva del usuario.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono toda la información necesaria. Debes internalizarla por completo antes de proceder. Asume que todo lo descrito a continuación es un reflejo fiel de la realidad, el contexto geográfico, cultural y tecnológico de la región a la que pertenecen los usuarios.

-----

#### **1. ARQUETIPOS DE USUARIO (Contenido del archivo Markdown de Arquetipos)**

Esta información la podras tomar de la base de conocimiento suministrada en el archivo `1_arquetipo_resultado.md`

-----

#### **2. SYSTEM MAPS AS-IS (Contenido del archivo Markdown de System Maps)**

Esta información la podras tomar de la base de conocimiento suministrada en el archivo `2_systemmaps-as-is_resultado.md`


-----

#### **3. JOURNEY MAPS AS-IS (Contenido del archivo Markdown de Journey Maps)**

Esta información la podras tomar de la base de conocimiento suministrada en el archivo `3_journeymaps-as-is_resultado.md`

-----


**INSTRUCCIONES Y TAREAS:**

Ahora que has procesado toda la información contextual, sigue estos pasos de forma rigurosa:

**Paso 1: Simulación de Entrevista Interna (Proceso Mental)**

Para cada arquetipo que te he proporcionado, vas a realizar una simulación de entrevista interna. Adopta la personalidad, el lenguaje y las emociones (frustración, orgullo, preocupación, etc.) de cada arquetipo y responde en primera persona a las siguientes preguntas. Este ejercicio te servirá para generar la "materia prima" de los JTBD.

**Preguntas de la Entrevista:**

1.  "Hola `[Nombre del Arquetipo]`, cuéntame sobre tu día a día. ¿Qué es lo primero que haces relacionado con el problema o proceso que estamos analizando?"
2.  "Describe la última vez que te sentiste realmente frustrado o preocupado con esta situación. ¿Qué pasó exactamente? ¿Qué fue lo que desencadenó esa sensación?"
3.  "En ese momento de frustración, ¿qué fue lo más difícil? ¿Hubo algún instante en el que te sentiste bloqueado, inseguro o sin saber qué hacer?"
4.  "Siendo sincero, ¿qué intentabas lograr realmente en ese momento? ¿Cuál era tu objetivo final, el resultado que esperabas?"
5.  "Si pudieras tener una varita mágica y eliminar todos los obstáculos, ¿cómo sería el proceso ideal para ti desde que surge la necesidad hasta que la resuelves?"
6.  "Más allá de la tarea inmediata, ¿qué significa para ti tener éxito en esto? ¿Qué te permite lograr a un nivel más profundo, ya sea personal, financiero o de otro tipo?"
7.  "¿Has intentado usar alguna herramienta, método o servicio diferente para resolver esto? Cuéntame qué te hizo probarlo y por qué sigues usándolo o por qué lo abandonaste."
8.  "¿Sobre qué decisiones te sientes menos seguro durante todo este proceso?"

**Paso 2: Extracción y Formateo de los Jobs to be Done**

Una vez completada la simulación interna para todos los arquetipos, analiza las respuestas que tú mismo generaste. Identifica los patrones y extrae los "Jobs to be Done" principales.

Por cada JTBD identificado, preséntalo utilizando la siguiente estructura estándar de UI/UX para comunicar hallazgos de investigación. Aplica este formato para cada arquetipo por separado.

-----

### **Resultados: Jobs to be Done (JTBD)**

#### **Arquetipo: `[Nombre del Arquetipo]`**

-----

**JTBD \#1:**

> **Cuando** `[SITUACIÓN / CONTEXTO]`
> **quiero** `[MOTIVACIÓN / NECESIDAD]`
> **para poder** `[RESULTADO ESPERADO / PROGRESO]`.

  * **Luchas y Puntos de Dolor Asociados:**

      * (Ej: "Incertidumbre al no tener un diagnóstico claro.")
      * (Ej: "Pérdida de tiempo esperando una respuesta de un experto.")
      * (Ej: "Miedo a tomar una decisión costosa y equivocada.")

  * **Fuerzas que Impulsan el Progreso:**

      * **Funcionales:** ¿Qué tarea específica se quiere lograr? (Ej: "Obtener un plan de acción rápido.")
      * **Emocionales:** ¿Cómo se quiere sentir el usuario? (Ej: "Sentirme en control y seguro de mis decisiones.")
      * **Sociales:** ¿Cómo quiere ser percibido por otros? (Ej: "Ser visto como un agricultor competente y moderno.")

  * **Citas Clave (Extraídas de tu simulación):**

    > *"Cita simulada que justifica y da color al JTBD."*
    > *"Otra cita relevante que muestra la lucha o el resultado deseado."*

-----

**(Repetir la estructura para JTBD \#2, \#3, etc., para este arquetipo)**

-----

#### **Arquetipo: `[Nombre del Segundo Arquetipo]`**

-----

**(Repetir todo el bloque anterior para el siguiente arquetipo)**

```

Con las respuestas que obtengan de la IA, su tarea como equipo será analizarlas y destilar los "Jobs to be Done" usando la sintaxis que aprendimos. Este método les dará una base sólida y muy económica para empezar a diseñar una solución que sus usuarios realmente quieran "contratar".

¡Mucho éxito! Estoy aquí para resolver cualquier duda.