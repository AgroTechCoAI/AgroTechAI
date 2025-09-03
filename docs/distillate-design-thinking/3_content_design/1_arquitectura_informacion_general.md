## Diseño de Contenido: Arquitectura de Información

### Contexto

Con las funcionalidades clave ya definidas y sus especificaciones detalladas en la fase de "diseño funcional", el equipo tiene todas las "piezas del rompecabezas" sobre la mesa. Ahora enfrentamos una pregunta crítica: ¿cómo organizamos estas piezas para que formen una herramienta coherente y no un laberinto confuso?

Sabemos por la investigación que un agrónomo en campo o un mayordomo supervisando un lote no tiene tiempo para descifrar menús complejos. Si la información correcta —un diagnóstico, un historial, una sugerencia— no está a dos o tres toques de distancia, la herramienta será abandonada, sin importar cuán potente sea su tecnología de IA.

El éxito del producto no solo radica en la precisión de su análisis, sino en la **claridad de su estructura**. La Arquitectura de Información debe ser tan intuitiva que se sienta como una extensión del propio proceso mental del usuario, no como un software que deben "aprender a usar".

Por tal razón, esta fase se compone de un único y potente prompt, diseñado como una simulación estratégica:

#### Fase Única: La Construcción del Plano Digital mediante Simulación Sintética

**Objetivo:** Crear un **plano de navegación y contenido (Sitemap)** completo y validado sintéticamente. El objetivo es definir "el lugar correcto para cada cosa" basándose en los modelos mentales de los usuarios (extraídos de los arquetipos y JTBD), no en suposiciones internas del equipo, antes de diseñar una sola interfaz.


## Herramientas

Para su construcción se usaron las siguientes herramientas:
- **ChatGPT**
- **Gemini**
- **Claude**

---

## Prompt
```markdown
### Experto en Arquitectura de Información para una App de Agro-Tech

**ROL Y OBJETIVO:**

Actúa como un experto de clase mundial en Arquitectura de Información (AI) y Experiencia de Usuario (UX), con especialización en productos digitales para la industria agrícola. Tu objetivo es analizar de forma exhaustiva todos los documentos de investigación y diseño funcional que te proporcionaré para construir una Arquitectura de Información sólida, intuitiva y centrada en el usuario para una nueva aplicación de agricultura de precisión.

Tu tarea final es organizar todo el contenido y las funcionalidades de la aplicación en una estructura lógica que responda directamente a las necesidades, modelos mentales y "Jobs to be Done" de los usuarios finales (agricultores, mayordomos, agrónomos). Debes priorizar la claridad, la facilidad de búsqueda y la eficiencia.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono toda la información necesaria. Debes internalizarla por completo antes de proceder. Asume que todo lo descrito a continuación es un reflejo fiel de la realidad de los usuarios.

-----

#### **1. ARQUETIPOS DE USUARIO**
Esta información la podras tomar de la base de conocimiento suministrada en el archivo `1_arquetipo_resultado.md`, ten cuenta que los arquetipos seleccionados son aquellos que se encuentran en la fases No 3 y 4.

-----

#### **2. SYSTEM MAPS AS-IS**
Esta información la podras tomar de la base de conocimiento suministrada en el archivo `2_systemmaps-as-is_resultado.md`

-----

#### **3. JOURNEY MAPS AS-IS**
Esta información la podras tomar de la base de conocimiento suministrada en el archivo `3_journeymaps-as-is_resultado.md`

-----

#### **4. JOBS TO BE DONE (JTBD)**
Esta información la podras tomar de la base de conocimiento suministrada en el archivo `1_jtbd_resultado.md`

-----

#### **5. DEFINICIÓN Y SELECCIÓN DE FUNCIONALIDADES**
Esta información la podras tomar de la base de conocimiento suministrada en el archivo `2_def_y_select_func_resultado.md`

-----

#### **6. DEFINICIÓN DE ESPECIFICACIONES**
Esta información la podras tomar de la base de conocimiento suministrada en el archivo `2_def_y_select_func_resultado.md`

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