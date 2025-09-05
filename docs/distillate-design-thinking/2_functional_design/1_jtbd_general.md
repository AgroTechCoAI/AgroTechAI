# Construcción de JOBS TO BE DONE (JTBD)

## Contexto

El objetivo descubrir las verdaderas necesidades de sus usuarios. Para ello, se generará una lista clara y jerarquizada de los "Jobs to be Done" para cada usuario a través de la investigación realizada de forma sintética por el modelo, que brindará una guía precisa para responder preguntas como:

- ¿Qué botón es más importante en la pantalla principal?
- ¿Cómo debería ser el flujo para reportar un problema?
- ¿Qué información necesita ver la agrónoma que es diferente a la que necesita el agricultor?

El prompt se alineó a todo el equipo en una comprensión profunda y compartida del problema a resolver, permitiéndoles pasar a la fase de diseño con una confianza y una claridad inmensamente mayores.

## Herramientas

Para su construcción se usaron las siguientes herramientas:
- **ChatGPT**
- **Gemini**
- **Claude**

## Prompt

```markdown
### UX Engineer para Descubrir y Formatear Jobs to be Done (JTBD)

**ROL Y OBJETIVO:**

Actúa como un experto en investigación de experiencia de usuario y estrategia de producto, especializado en la metodología "Jobs to be Done" (JTBD). Tu objetivo principal es analizar en profundidad la información contextual que te proporcionaré (arquetipos, system maps, journey maps) para identificar las luchas, motivaciones y resultados deseados de los usuarios.

Tu tarea final será destilar esta información en una serie de "Jobs to be Done" claros y accionables, presentados con un formato profesional y fácil de entender para un equipo de diseño y producto. No debes inventar soluciones ni funcionalidades; tu foco absoluto está en definir el problema desde la perspectiva del usuario.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono toda la información necesaria. Debes internalizarla por completo antes de proceder. Asume que todo lo descrito a continuación es un reflejo fiel de la realidad, el contexto geográfico, cultural y tecnológico de la región a la que pertenecen los usuarios.

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