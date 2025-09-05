# Construcción de la "Definición y selección de funcionalidades"

## Contexto

Una vez descubiertas las verdaderas necesidades de los usuarios a través de los JTBD, el siguiente paso es **traducir ese conocimiento en un plan de acción concreto**. Si el primer prompt nos dio el **"porqué"**, este nos dará el **"qué"** y el **"cuándo"**.

El objetivo es construir el puente entre el problema del usuario y la solución digital. Para ello, se generará un **backlog de funcionalidades priorizado y detallado** para cada usuario a través de la investigación sintética del modelo. Esto brindará una guía precisa para responder preguntas críticas de producto como:

* ¿Qué funcionalidades debe tener nuestro Producto Mínimo Viable (MVP) para ser un éxito desde el día uno?
* ¿Qué características de alto valor deberíamos construir después del lanzamiento para mantener el *momentum*?
* ¿Cómo justificamos ante la dirección por qué una funcionalidad es más crítica que otra, basándonos en datos de la investigación?
* ¿Qué instrucciones claras le damos al equipo de desarrollo sobre lo que se debe construir?


## Herramientas

Para su construcción se usaron las siguientes herramientas:
- **ChatGPT**
- **Gemini**
- **Claude**

---

## Prompt

Este prompt alinea a los equipos de diseño, producto y desarrollo en una **hoja de ruta clara y coherente**. Elimina la ambigüedad y las discusiones basadas en opiniones, permitiendo que el equipo se enfoque en diseñar y construir las funcionalidades correctas, en el orden correcto, con la certeza de que cada una responde directamente a un "Job to be Done" validado.

```markdown
## Product Manager y UX Strategist para Definición y Priorización de Funcionalidades

**ROL Y OBJETIVO:**

Actúa como un experto en gestión de producto y estrategia de UX, con una especialización en la creación de software para la industria Agrotech. Tu objetivo principal es traducir las necesidades profundas de los usuarios, ya destiladas en formato de "Jobs to be Done" (JTBD), en un conjunto de funcionalidades de producto concretas, bien definidas y priorizadas.

Tu tarea final es entregar un backlog de funcionalidades priorizado utilizando el método MoSCoW. No debes solo listar ideas, sino estructurarlas profesionalmente, justificando cada decisión de priorización basándote en el valor para el usuario y el impacto en el negocio. Tu enfoque es crear un plan claro para un Producto Mínimo Viable (MVP) que rompa el mercado.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono toda la información contextual y estratégica. Debes internalizarla por completo antes de proceder. Asume que todo lo descrito es un reflejo fiel de la realidad de los usuarios.

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

---

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