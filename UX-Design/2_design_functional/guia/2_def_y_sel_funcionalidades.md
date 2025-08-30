## **Guía Completa: Definición y Selección de Funcionalidades**

Esta fase es el puente entre la estrategia (entender el problema del usuario) y el diseño (crear la solución). Si los JTBD nos dicen qué "trabajo" quiere resolver el usuario, las funcionalidades son las herramientas que le damos dentro de nuestro producto para que pueda hacerlo de manera eficiente y satisfactoria.

### **1. ¿Qué es la "Definición y Selección de Funcionalidades"?**

Es el proceso de traducir las necesidades, motivaciones y resultados esperados del usuario (identificados en los JTBD) en características y capacidades concretas que el producto debe tener. Este proceso no se trata solo de hacer una lista de ideas; se trata de:

  * **Definir:** Describir cada funcionalidad de manera clara y concisa. ¿Qué hace? ¿Para quién es? ¿Qué valor aporta?
  * **Priorizar:** No todas las funcionalidades son iguales. Algunas son esenciales para que el producto funcione, mientras que otras son "agradables de tener". Debemos ordenarlas para enfocar los esfuerzos de desarrollo en lo que genera más impacto.
  * **Seleccionar:** Tomar decisiones informadas sobre qué se construirá en la primera versión del producto (MVP - Producto Mínimo Viable) y qué se dejará para futuras iteraciones.

El error más común es saltar directamente a la creación de funcionalidades sin una conexión clara con los JTBD. Esto lleva a productos inflados, con características que nadie usa, porque no resuelven un "trabajo" real.

### **2. ¿Cómo se Construyen y Priorizan las Funcionalidades?**

Seguiremos un proceso de 3 pasos para pasar de la necesidad a la funcionalidad priorizada.

**Paso A: Ideación a partir de los JTBD (Brainstorming)**

Por cada JTBD que han definido, reúnan al equipo y hagan una lluvia de ideas respondiendo a la pregunta:

> **"¿Cómo podríamos ayudar al `[Arquetipo]` a `[Motivación / Necesidad]` para que pueda `[Resultado Esperado]`?"**

Dejen que las ideas fluyan sin filtro. En esta etapa, no hay ideas malas.

  * **Ejemplo:**
      * **JTBD:** *Cuando veo una mancha extraña en una hoja, quiero identificar rápidamente si es una plaga o una deficiencia nutricional, para poder aplicar el tratamiento correcto antes de que se extienda y afecte mi producción.*
      * **Ideas de Funcionalidades:**
          * Un botón para tomar una foto.
          * Análisis de imagen con IA.
          * Un reporte con el porcentaje de confianza del diagnóstico.
          * Sugerencia de 2-3 posibles tratamientos.
          * Comparación con imágenes de una base de datos.
          * Un historial de análisis por lote/parcela.
          * Alerta si la plaga es muy peligrosa.

**Paso B: Estructuración de las Funcionalidades (User Stories)**

Ahora, tomamos las ideas en bruto y las estructuramos en un formato claro llamado "User Story" (Historia de Usuario). Esto nos obliga a mantener la perspectiva del usuario.

  * **Formato:** *Como `[tipo de usuario]`, quiero `[realizar una acción]` para poder \`[obtener un beneficio]'.*

  * **Ejemplo:**

      * **Idea:** Análisis de imagen con IA.
      * **User Story:** *Como **Agrónomo**, quiero **analizar una foto de una hoja afectada usando IA** para poder **obtener un diagnóstico diferencial entre plaga y deficiencia en menos de un minuto.***

**Paso C: Priorización con el Método MoSCoW**

Con una lista de funcionalidades bien definidas, necesitamos priorizarlas. El método MoSCoW es simple y efectivo para esto. Clasificamos cada funcionalidad en una de cuatro categorías:

1.  **M - Must-have (Debe tener):** **Indispensable.** Sin esta funcionalidad, el producto no funciona, no tiene sentido o no cumple su promesa de valor principal. Es innegociable para el lanzamiento.

      * *Ejemplo:* La capacidad de tomar o subir una foto de un cultivo y recibir un diagnóstico básico.

2.  **S - Should-have (Debería tener):** **Importante, pero no vital.** Estas funcionalidades añaden un valor significativo, pero el producto puede ser lanzado sin ellas. Son las primeras candidatas para la siguiente versión.

      * *Ejemplo:* Un historial de diagnósticos para ver la evolución del cultivo a lo largo del tiempo.

3.  **C - Could-have (Podría tener):** **Deseable, pero no necesaria.** Son funcionalidades "agradables de tener" que tienen un impacto menor. Se pueden incluir si hay tiempo y recursos de sobra.

      * *Ejemplo:* Integración con datos meteorológicos para predecir posibles brotes de plagas.

4.  **W - Won't-have (No tendrá):** **Fuera de alcance.** Funcionalidades que explícitamente se decide no construir en esta etapa (o quizás nunca). Ayuda a gestionar las expectativas y a no desviarse del foco.

      * *Ejemplo:* Un módulo de contabilidad para llevar los costos de los insumos.

Al finalizar este proceso, tendrán una lista clara y priorizada de qué construir, asegurando que su MVP sea potente y esté 100% enfocado en resolver los problemas reales de sus usuarios.

-----

## **Prompt para Investigación Sintética con GenAI: Definición y Selección de Funcionalidades**

Ahora, la herramienta que les permitirá hacer esto de forma sintética. Este prompt está diseñado para que la GenAI actúe como un estratega de producto experto, tomando toda su investigación previa y convirtiéndola en un plan de funcionalidades accionable.

Simplemente deben reemplazar el contenido entre `[ ]` con la información que ya tienen.

```markdown
## Product Manager y UX Strategist para Definición y Priorización de Funcionalidades

**ROL Y OBJETIVO:**

Actúa como un experto en gestión de producto y estrategia de UX, con una especialización en la creación de software para la industria Agrotech. Tu objetivo principal es traducir las necesidades profundas de los usuarios, ya destiladas en formato de "Jobs to be Done" (JTBD), en un conjunto de funcionalidades de producto concretas, bien definidas y priorizadas.

Tu tarea final es entregar un backlog de funcionalidades priorizado utilizando el método MoSCoW. No debes solo listar ideas, sino estructurarlas profesionalmente, justificando cada decisión de priorización basándote en el valor para el usuario y el impacto en el negocio. Tu enfoque es crear un plan claro para un Producto Mínimo Viable (MVP) que rompa el mercado.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono toda la información contextual y estratégica. Debes internalizarla por completo antes de proceder. Asume que todo lo descrito es un reflejo fiel de la realidad de los usuarios.

-----

### **1. ARQUETIPOS DE USUARIO**

[Aquí pegas el contenido completo del archivo Markdown de Arquetipos. Ejemplo: `1_arquetipo_resultado.md`]

-----

### **2. SYSTEM MAPS AS-IS**

[Aquí pegas el contenido completo del archivo Markdown de System Maps. Ejemplo: `2_systemmaps-as-is_resultado.md`]

-----

### **3. JOURNEY MAPS AS-IS**

[Aquí pegas el contenido completo del archivo Markdown de Journey Maps. Ejemplo: `3_journeymaps-as-is_resultado.md`]

-----

### **4. JOBS TO BE DONE (JTBD)**

[Aquí pegas el resultado completo del análisis de JTBD, el cual es el input más CRÍTICO para esta tarea. Ejemplo: `4_jtbd_resultado.md`]

-----


**INSTRUCCIONES Y TAREAS:**

Ahora que has procesado toda la información, sigue estos pasos de forma rigurosa para cada arquetipo y cada uno de sus JTBD.

**Paso 1: Sesión de Ideación "How Might We..." (Proceso Mental)**

Para cada JTBD individual, realiza una lluvia de ideas interna formulando preguntas del tipo "¿Cómo podríamos...?". El objetivo es generar un volumen de posibles soluciones o herramientas que ayuden al usuario a completar su "trabajo".

* Ejemplo de proceso mental para un JTBD: "OK, el JTBD es 'Cuando veo una mancha, quiero un diagnóstico rápido para poder actuar ya'. ¿Cómo podríamos ayudarlo? Podríamos permitirle usar la cámara. Podríamos darle un porcentaje de certeza. Podríamos mostrarle fotos para comparar. Podríamos conectarlo con un experto si la IA no está segura..."

**Paso 2: Definición y Estructuración de Funcionalidades**

Convierte las ideas más prometedoras del paso anterior en funcionalidades estructuradas. Por cada funcionalidad, debes definir:

1.  **Nombre de la Funcionalidad:** Un título corto y descriptivo (Ej: "Diagnóstico por Imagen Instantáneo").
2.  **Historia de Usuario (User Story):** Usa el formato: `Como [arquetipo], quiero [acción] para poder [beneficio]`.
3.  **Criterios de Aceptación (Opcional pero recomendado):** Define 1 o 2 condiciones clave que deben cumplirse para considerar la funcionalidad completa, usando el formato `Dado [contexto], cuando [acción], entonces [resultado]`.

**Paso 3: Priorización MoSCoW y Justificación**

Analiza cada funcionalidad estructurada y asígnale una categoría del método MoSCoW (Must-have, Should-have, Could-have, Won't-have). Lo más importante es que justifiques tu elección. La justificación debe basarse en:

* **Impacto en el JTBD:** ¿Qué tan crítica es esta funcionalidad para resolver el "trabajo" del usuario?
* **Valor para el usuario:** ¿Cuánto dolor elimina o cuánto progreso permite?
* **Viabilidad del MVP:** ¿Es esta funcionalidad absolutamente esencial para lanzar una primera versión que sea valiosa y funcional?

**FORMATO DE SALIDA:**

Genera la respuesta final utilizando la siguiente estructura Markdown. Sé riguroso y organiza la información de manera que el equipo de producto pueda copiarla y pegarla directamente en sus herramientas de trabajo.

-----

## **Resultados: Backlog de Funcionalidades Priorizadas**

### **Arquetipo: `[Nombre del Arquetipo]`**

-----

**Basado en el JTBD #1:** `[Pega aquí el JTBD completo: Cuando..., quiero..., para poder...]`

* **Funcionalidades Propuestas:**

    * **1. Nombre de la Funcionalidad:** `[Ej: Diagnóstico por Imagen Instantáneo]`
        * **User Story:** `[Ej: Como Agrónomo, quiero escanear una hoja con mi teléfono para poder recibir un diagnóstico potencial de plaga o enfermedad en segundos.]`
        * **Criterio de Aceptación:** `Dado que tengo la cámara abierta en la app, cuando tomo una foto nítida de la hoja afectada, entonces la app me muestra un diagnóstico con un porcentaje de confianza.`
        * **Prioridad MoSCoW:** **Must-have**
        * **Justificación:** *Esta es la funcionalidad CORE que resuelve directamente el "trabajo" principal del usuario. Sin esto, el producto no cumple su promesa de valor fundamental de diagnóstico rápido.*

    * **2. Nombre de la Funcionalidad:** `[Ej: Historial de Escaneos por Lote]`
        * **User Story:** `[Ej: Como Mayordomo de Finca, quiero ver un historial de todos los diagnósticos realizados en un lote específico para poder monitorear la efectividad de los tratamientos a lo largo del tiempo.]`
        * **Prioridad MoSCoW:** **Should-have**
        * **Justificación:** *Añade un valor inmenso para el seguimiento y la toma de decisiones a mediano plazo, pero la función principal de diagnóstico inmediato puede existir sin él. Es un candidato perfecto para la v1.1 o v2.*

    * **3. Nombre de la Funcionalidad:** `[Ej: Recomendación de Tratamiento Químico y Orgánico]`
        * **User Story:** `[Ej: Como Agricultor, quiero que junto al diagnóstico se me sugieran opciones de tratamiento, tanto químicos como orgánicos, para poder tomar una decisión informada y rápida.]`
        * **Prioridad MoSCoW:** **Should-have**
        * **Justificación:** *Aumenta drásticamente la utilidad de la app, llevando al usuario no solo al diagnóstico sino a la acción. Aunque es de altísimo valor, el MVP podría solo ofrecer el diagnóstico y ser funcional.*

    * **4. Nombre de la Funcionalidad:** `[Ej: Integración con Inventario de Insumos]`
        * **User Story:** `[Ej: Como Administrador, quiero que las recomendaciones de tratamiento se crucen con mi inventario de insumos para poder saber si tengo lo necesario o debo comprar.]`
        * **Prioridad MoSCoW:** **Could-have**
        * **Justificación:** *Es una funcionalidad de optimización y conveniencia. Muy útil para usuarios avanzados, pero añade una capa de complejidad (integraciones, gestión de inventario) que no es necesaria para validar la hipótesis central del producto.*

-----

**(Repetir la estructura para el JTBD #2, #3, etc., de este arquetipo)**

-----

### **Arquetipo: `[Nombre del Segundo Arquetipo]`**

-----

**(Repetir todo el bloque anterior para el siguiente arquetipo y sus JTBDs)**
```