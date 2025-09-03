## Guía Completa: Arquitectura de Información (AI) para su Producto Agrícola

### 1. ¿Qué es la Arquitectura de Información? 🏛️

La **Arquitectura de Información** es el arte y la ciencia de organizar, estructurar y etiquetar el contenido de un producto digital (como su app) de manera que los usuarios puedan encontrar la información y completar tareas de forma fácil y directa. Se enfoca en responder tres preguntas clave desde la perspectiva del usuario:

  * **¿Dónde estoy?** (Orientación)
  * **¿Qué puedo encontrar aquí?** (Comprensión)
  * **¿A dónde puedo ir desde aquí?** (Navegación)

Para lograrlo, nos basamos en cuatro sistemas fundamentales:

1.  **Sistemas de Organización:** ¿Cómo agrupamos el contenido?
      * **Jerárquico:** De lo más general a lo más específico (Ej: Cultivos -\> Tomate -\> Lote 3 -\> Último Diagnóstico).
      * **Secuencial:** En un orden lógico o de pasos (Ej: Paso 1: Tomar Foto, Paso 2: Ver Análisis, Paso 3: Aplicar Sugerencia).
      * **Por Tópicos:** Agrupado por tema (Ej: Plagas, Enfermedades, Deficiencias Nutricionales).
2.  **Sistemas de Etiquetado (Labeling):** ¿Cómo llamamos a las cosas? Las etiquetas deben ser claras y usar el lenguaje de sus usuarios. ¿Lo llamamos "Análisis de Fitopatología" o "Diagnóstico de la Planta"? El segundo es probablemente más efectivo para un público amplio.
3.  **Sistemas de Navegación:** ¿Cómo se mueven los usuarios por la información? Esto incluye el menú principal, los filtros, los enlaces internos y las migas de pan (breadcrumbs).
4.  **Sistemas de Búsqueda:** ¿Cómo buscan los usuarios algo específico? Esto se refiere a la funcionalidad de búsqueda y cómo presenta los resultados.

### 2. ¿Cómo se Construye la Arquitectura de Información? 🗺️

El proceso tradicional implica varios pasos que vamos a simular con la ayuda de la GenAI.

1.  **Inventario de Contenido y Funcionalidades:** El primer paso es hacer una lista de *todo* lo que vivirá en la aplicación. Cada pieza de información (como un diagnóstico, un historial de lote, un artículo de ayuda) y cada funcionalidad (tomar una foto, generar un reporte, contactar a un agrónomo) es un elemento que debemos organizar. Afortunadamente, ustedes ya tienen esto en sus documentos de funcionalidades y especificaciones.

2.  **Agrupación de Contenido (Card Sorting):** Esta es la técnica central. Imaginen que escribimos cada elemento del inventario en una tarjeta. Luego, le pedimos a los usuarios (en nuestro caso, la GenAI actuando como sus arquetipos) que agrupen esas tarjetas de la manera que les parezca más lógica y que le pongan un nombre a cada grupo. Esto nos revela el modelo mental del usuario, no el nuestro.

3.  **Creación del Mapa del Sitio (Sitemap):** Una vez que tenemos los grupos, los organizamos en una estructura jerárquica. El sitemap es un diagrama que muestra la estructura de las páginas y secciones de la app y cómo se conectan entre sí. Será el plano final de nuestro producto.

Ahora, traduzcamos todo esto en un prompt que puedan usar.

-----

## Construyendo el Prompt para la Evaluación Sintética con GenAI

Aquí tienen el prompt detallado. La idea es que copien y peguen este texto en la herramienta de GenAI y luego inserten el contenido de sus documentos donde se indica.

```markdown
### Experto en Arquitectura de Información para una App de Agri-Tech

**ROL Y OBJETIVO:**

Actúa como un experto de clase mundial en Arquitectura de Información (AI) y Experiencia de Usuario (UX), con especialización en productos digitales para la industria agrícola. Tu objetivo es analizar de forma exhaustiva todos los documentos de investigación y diseño funcional que te proporcionaré para construir una Arquitectura de Información sólida, intuitiva y centrada en el usuario para una nueva aplicación de agricultura de precisión.

Tu tarea final es organizar todo el contenido y las funcionalidades de la aplicación en una estructura lógica que responda directamente a las necesidades, modelos mentales y "Jobs to be Done" de los usuarios finales (agricultores, mayordomos, agrónomos). Debes priorizar la claridad, la facilidad de búsqueda y la eficiencia.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono toda la información necesaria. Debes internalizarla por completo antes de proceder. Asume que todo lo descrito a continuación es un reflejo fiel de la realidad de los usuarios.

-----

#### **1. ARQUETIPOS DE USUARIO**
*(Aquí deben pegar el contenido completo del archivo `1_arquetipo_resultado.md`)*

-----

#### **2. SYSTEM MAPS AS-IS**
*(Aquí deben pegar el contenido completo del archivo `2_systemmaps-as-is_resultado.md`)*

-----

#### **3. JOURNEY MAPS AS-IS**
*(Aquí deben pegar el contenido completo del archivo `3_journeymaps-as-is_resultado.md`)*

-----

#### **4. JOBS TO BE DONE (JTBD)**
*(Aquí deben pegar el contenido completo del archivo con los JTBD que generaron previamente)*

-----

#### **5. DEFINICIÓN Y SELECCIÓN DE FUNCIONALIDADES**
*(Aquí deben pegar el listado y descripción de todas las funcionalidades que tendrá la aplicación)*

-----

#### **6. DEFINICIÓN DE ESPECIFICACIONES**
*(Aquí deben pegar cualquier detalle técnico o de contenido relevante, como tipos de datos a mostrar, reportes, etc.)*

-----

**INSTRUCCIONES Y TAREAS:**

Ahora que has procesado toda la información, sigue estos pasos de forma rigurosa y estructurada.

**Paso 1: Inventario y Abstracción de Contenido y Funcionalidades**

Primero, revisa los documentos de "Funcionalidades" y "Especificaciones". Crea una lista plana (un inventario) de cada pieza de contenido individual y cada función que debe ser organizada. Por ejemplo:
* Función: Tomar/subir foto del cultivo.
* Contenido: Diagnóstico de plaga (resultado).
* Contenido: Sugerencia de tratamiento (resultado).
* Contenido: Nivel de confianza del diagnóstico AI.
* Función: Ver historial de diagnósticos por lote.
* Contenido: Reporte de salud del cultivo (PDF).
* Función: Contactar a un agrónomo.
* Contenido: Perfil del usuario/finca.
* etc.

**Paso 2: Simulación de "Card Sorting" Sintético**

Este es el paso más crítico. Adoptando la mentalidad, el lenguaje y las prioridades de los **Arquetipos** que te he proporcionado, agrupa los elementos del inventario del Paso 1 en categorías lógicas.

Para cada grupo que crees, debes:
1.  **Darle un nombre (etiqueta):** Usa un lenguaje claro, simple y directo que resuene con los usuarios. Evita la jerga técnica.
2.  **Listar los elementos que contiene:** Enumera qué funcionalidades y piezas de contenido pertenecen a este grupo.
3.  **Justificar la agrupación:** Explica *por qué* un arquetipo específico agruparía estas cosas juntas. Basa tu justificación directamente en sus **JTBD**, dolores y motivaciones. (Ej: "El Mayordomo agruparía 'Historial de Lotes' y 'Reportes Anteriores' bajo una sección llamada 'Mis Registros' porque su JTBD es 'Cuando planifico la siembra, quiero revisar el rendimiento pasado para poder optimizar la inversión'").

Realiza este ejercicio para todos los elementos del inventario.

**Paso 3: Creación de la Arquitectura de Información (Sitemap Jerárquico)**

Usando los grupos que creaste en el Paso 2, organiza todo en un mapa del sitio jerárquico y coherente. Este mapa representará la navegación principal y la estructura de la aplicación.

* Define las 4 o 5 secciones principales que conformarían el menú de navegación principal (Ej: Inicio, Diagnosticar, Mis Cultivos, Ayuda).
* Debajo de cada sección principal, anida las sub-secciones, funcionalidades y páginas de contenido correspondientes.
* Utiliza una lista anidada (markdown) para representar la jerarquía visualmente.
* Para cada elemento del sitemap, añade un breve comentario explicando su propósito y el arquetipo principal al que sirve.

**FORMATO DE SALIDA:**

Presenta tu respuesta final utilizando la siguiente estructura de Markdown. No incluyas explicaciones previas, solo el resultado final estructurado como se pide a continuación.

-----

## **Arquitectura de Información Propuesta**

### **1. Grupos de Contenido Clave (Resultado del Card Sorting Sintético)**

#### **Grupo A: [Nombre del Grupo 1]**
* **Justificación:** [Explicación basada en los arquetipos y JTBD]
* **Contenido:**
    * [Elemento 1]
    * [Elemento 2]
    * ...

#### **Grupo B: [Nombre del Grupo 2]**
* **Justificación:** [Explicación basada en los arquetipos y JTBD]
* **Contenido:**
    * [Elemento 3]
    * [Elemento 4]
    * ...

*(Repetir para todos los grupos identificados)*

-----

### **2. Mapa del Sitio Jerárquico (Sitemap)**

* **1.0 Inicio / Dashboard** *(Propósito: Vista rápida del estado general de los cultivos, alertas y accesos directos. Primario para Mayordomo y Agrónomo)*
    * 1.1 Resumen de Alertas Recientes
    * 1.2 Estado General de los Lotes
    * 1.3 Acceso Rápido a "Nuevo Diagnóstico"

* **2.0 Diagnosticar** *(Propósito: El core de la app, donde el usuario inicia el análisis. Primario para todos los arquetipos)*
    * 2.1 Tomar o Subir Fotografía del Cultivo
    * 2.2 Pantalla de Análisis en Progreso
    * 2.3 Página de Resultado del Diagnóstico
        * 2.3.1 Identificación del Problema (Plaga, enfermedad, etc.)
        * 2.3.2 Nivel de Confianza de la IA
        * 2.3.3 Sugerencias y Plan de Acción
        * 2.3.4 Opción de Guardar o Descartar Reporte

* **3.0 Mis Cultivos / Finca** *(Propósito: Centro de gestión de la información histórica y por lotes. Primario para Mayordomo y Agrónomo)*
    * 3.1 Vista de Lotes/Sectores
        * 3.1.1 Historial de Diagnósticos del Lote
        * 3.1.2 Reportes Históricos (PDFs)
        * 3.1.3 Notas y Observaciones del Lote
    * 3.2 Vista por Tipo de Cultivo

*(Continúa estructurando el resto de las secciones como "Recursos/Ayuda", "Perfil/Configuración", etc., basándote en los grupos del card sorting)*

```