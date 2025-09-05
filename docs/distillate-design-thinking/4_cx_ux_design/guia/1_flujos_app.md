## Guía de Consultoría: Creación de Flujos de Aplicación (Wireflows)

¡Hola equipo\! Es un placer guiarlos en esta fase crucial del diseño de su producto. Vamos a sentar las bases de una experiencia de usuario intuitiva y lógica que resuelva las necesidades reales de sus usuarios en el campo.

### 1\. ¿Qué son los Flujos de Aplicación (Wireframing / Wireflows)?

Imaginemos que estamos construyendo una casa. Antes de preocuparnos por el color de las paredes o el tipo de muebles (el diseño visual o UI), necesitamos los planos. Estos planos nos dicen dónde estarán las habitaciones, cómo se conectan entre sí, dónde van las puertas y las ventanas. Sin esos planos, la casa sería un caos.

En el mundo digital, los **wireflows** son esos planos.

  * Un **Wireframe** es un esquema básico de una sola pantalla. Es como el plano de una sola habitación. Muestra qué elementos van en esa pantalla (botones, texto, imágenes) y dónde se ubican, pero sin colores ni diseño detallado. Su foco es la **estructura** y la **jerarquía**.

  * Un **Flujo de Usuario (User Flow)** es el camino que un usuario sigue a través de la aplicación para completar una tarea (ej: iniciar sesión, subir una imagen, ver un resultado). Es el camino que conecta las habitaciones.

Un **Wireflow** es la combinación de ambos: una secuencia de wireframes conectados que muestran un flujo de usuario completo, paso a paso. Nos permite visualizar y probar la lógica de la aplicación antes de escribir una sola línea de código o diseñar un solo pixel. 🗺️

**El objetivo principal es responder:** ¿Tiene sentido este camino para el usuario? ¿Es fácil y lógico llegar del punto A al punto B para completar su objetivo?

-----

### 2\. ¿Cómo se Construyen los Wireflows?

Construir un wireflow es un proceso lógico que se apoya directamente en la investigación y la arquitectura que ya han definido.

1.  **Elegir un "Job to be Done" (JTBD) Clave:** Empiecen por un JTBD crítico. Por ejemplo: *"Cuando encuentro una hoja que parece enferma, quiero obtener un diagnóstico rápido y fiable para poder tomar acciones antes de que se propague".*
2.  **Identificar al Actor Principal:** ¿Qué arquetipo realizará esta tarea? ¿El "Mayordomo de Finca" que está en el campo o el "Ingeniero Agrónomo" desde su oficina? Esto define el contexto.
3.  **Listar los Pasos Clave:** Desglosen la tarea en una secuencia de pasos lógicos desde la perspectiva del usuario.
      * *Ejemplo: Abrir la app -\> Ir a la sección de análisis -\> Activar la cámara -\> Tomar la foto -\> Confirmar la foto -\> Ver el diagnóstico -\> Leer las recomendaciones.*
4.  **Dibujar un Wireframe para Cada Paso:** Para cada paso de la lista anterior, creen un wireframe simple. Usen cajas, líneas y texto simple. Pregúntense:
      * ¿Qué necesita ver el usuario en esta pantalla para tomar la siguiente acción? (Ej: un botón grande que diga "Nuevo Análisis").
      * ¿Qué información es indispensable? (Ej: en la pantalla de resultados, el nombre de la plaga y el nivel de certeza son cruciales).
      * ¿Cuáles son las acciones principales que puede realizar? (Ej: "Guardar Reporte", "Compartir").
5.  **Conectar los Wireframes con Flechas:** Unan las pantallas para mostrar el flujo. Una flecha que sale del botón "Tomar Foto" debe apuntar al wireframe de "Confirmar Foto". Esto visualiza el camino.
6.  **Anotar Decisiones y Lógica:** Agreguen pequeñas notas (anotaciones) para explicar interacciones que no son obvias. *Ej: "Si el análisis tarda más de 5 segundos, mostrar una barra de progreso" o "El botón 'Compartir' abre el menú nativo del celular".*

-----

### 3\. La Herramienta Ideal vs. el Canvas de GenAI

Para la creación de wireflows, las herramientas visuales y colaborativas son el estándar de la industria. **Miro**, **Whimsical** o **Figma** (con su herramienta FigJam) son excelentes opciones. Permiten arrastrar y soltar elementos, conectar flechas fácilmente y que todo el equipo colabore en tiempo real.

**Entonces, ¿por qué usar GenAI?**

La idea de usar GenAI para generar un "canvas" es muy inteligente para una etapa de evaluación sintética y para **acelerar el proceso**. El prompt que construiremos no le pedirá a la IA que "dibuje" en un sentido literal, sino que genere una **descripción estructural y textual detallada de cada pantalla y sus conexiones**. Este texto es, en esencia, la receta perfecta para que luego un diseñador (o incluso alguien del equipo con una herramienta como Miro) pueda visualizarlo rápidamente.

Además, podemos pedirle a la IA que formatee la salida usando un lenguaje como **Mermaid**, que puede renderizar diagramas simples a partir de texto, dándoles una visualización inmediata y básica.

-----

### 4\. Prompt Detallado para la Creación de Wireflows con GenAI

Aquí está el prompt que tu equipo puede adaptar y usar. Está diseñado para tomar todo su conocimiento previo y transformarlo en flujos de aplicación lógicos y centrados en el usuario.

````markdown
### ROL: Diseñador de Experiencia de Usuario (UX) Senior y Especialista en Interacción

**OBJETIVO PRINCIPAL:**

Actúa como un Diseñador UX Senior de clase mundial, experto en crear flujos de aplicación intuitivos y eficientes para herramientas de software complejas, especialmente en el sector agrícola.

Tu misión es tomar toda la investigación, la estrategia funcional y la arquitectura de información proporcionada para diseñar un **Wireflow detallado** para una tarea de usuario clave. El resultado debe ser un "canvas" textual que describa, pantalla por pantalla, los componentes, las interacciones y el camino que un usuario seguiría para completar su objetivo. Este canvas será la base para la creación de prototipos y la evaluación sintética.

El diseño debe ser extremadamente amigable, considerando que los usuarios van desde agricultores con poca experiencia tecnológica hasta agrónomos expertos.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono el corpus completo de conocimiento sobre el producto, sus usuarios, sus funcionalidades y su estructura. Debes internalizar cada pieza de información antes de comenzar tu diseño.

-----

#### **1. ARQUETIPOS DE USUARIO**
*Contenido del archivo `1_arquetipo_resultado.md` va aquí.*

-----

#### **2. SYSTEM MAP AS-IS**
*Contenido del archivo `2_systemmaps-as-is_resultado.md` va aquí.*

-----

#### **3. JOURNEY MAP AS-IS**
*Contenido del archivo `3_journeymaps-as-is_resultado.md` va aquí.*

-----

#### **4. JOBS TO BE DONE (JTBD)**
*Contenido del archivo `4_jtbd_resultado.md` va aquí.*

-----

#### **5. DEFINICIÓN Y SELECCIÓN DE FUNCIONALIDADES**
*Contenido del archivo `5_funcionalidades_resultado.md` va aquí.*

-----

#### **6. DEFINICIÓN DE ESPECIFICACIONES**
*Contenido del archivo `6_especificaciones_resultado.md` va aquí.*

-----

#### **7. ARQUITECTURA DE LA INFORMACIÓN (AI)**
*Contenido del archivo `canvas_arquitectura_informacion.md` va aquí.*

-----

**INSTRUCCIONES Y TAREAS (EJECÚTALAS EN ORDEN):**

**Paso 1: Selección del Flujo Crítico.**
Analiza los `JTBD` y los puntos de dolor en el `Journey Map`. Selecciona el flujo de usuario más crítico y de mayor impacto para el negocio y el usuario. Comunica cuál flujo elegiste y por qué. Un excelente candidato es: **"Realizar un nuevo diagnóstico de cultivo a partir de una imagen".**

**Paso 2: Identificación del Arquetipo y Contexto.**
Identifica el `Arquetipo` principal para este flujo. Describe brevemente su contexto de uso (ej. "en medio del campo, con una mano, posiblemente con sol directo en la pantalla").

**Paso 3: Desglose Secuencial de Pantallas.**
Basado en la `Arquitectura de la Información` y las `Funcionalidades`, define la secuencia de pantallas (o vistas modales) necesarias para completar el flujo de principio a fin. Nombra cada pantalla de forma clara (ej: "Inicio", "Cámara de Análisis", "Resumen del Diagnóstico").

**Paso 4: Construcción del Canvas de Wireflow.**
Para **cada pantalla** de la secuencia, detalla los siguientes puntos en el formato especificado abajo:
* **Nombre de la Pantalla:** Un título claro.
* **Propósito:** ¿Cuál es el único y principal objetivo de esta pantalla en el flujo?
* **Componentes UI Principales:** Lista los elementos esenciales. No te preocupes por el diseño, solo por la función. Usa elementos genéricos como:
    * `Header (con Título y Botón Atrás)`
    * `Botón Principal (CTA)`
    * `Campo de Texto`
    * `Placeholder de Imagen`
    * `Tarjeta de Información`
    * `Icono de Navegación`
    * `Lista Desplegable`
* **Interacciones y Conexiones:** Describe qué sucede cuando el usuario interactúa con los componentes principales. Especifica a qué pantalla lleva cada acción. (Ej: "Al hacer clic en el `Botón Principal 'Tomar Foto'`, se avanza a la pantalla `P3: Confirmación de Imagen`").
* **Anotaciones Clave:** Añade notas importantes sobre el comportamiento, la lógica o el contenido que debe mostrarse, basándote en las `Especificaciones`.

**Paso 5: Generación de Diagrama Visual (Opcional pero Recomendado).**
Al final del canvas textual, genera un diagrama de flujo simple usando la sintaxis de **Mermaid (graph TD)**. Esto proporcionará una vista rápida y visual del flujo completo que has diseñado.

**FORMATO DE SALIDA (EL CANVAS):**

Utiliza estrictamente el siguiente formato Markdown para tu respuesta.

-----

### **Canvas de Wireflow: [Nombre del Flujo de Usuario Seleccionado]**

**Arquetipo Principal:** [Ej: Mayordomo de Finca]
**Job to be Done (JTBD):** [Ej: "Cuando encuentro una hoja con aspecto enfermo, quiero obtener un diagnóstico rápido y fiable, para poder tomar acciones antes de que se propague."]
**Contexto de Uso:** [Ej: De pie en el cultivo, necesita un proceso rápido con pocos pasos y elementos grandes y claros.]

---

#### **P1: Dashboard Principal**
* **Propósito:** Dar una vista general del estado de los cultivos y ofrecer un acceso rápido a la función principal de análisis.
* **Componentes UI Principales:**
    * `Header: Saludo ("Hola, [Nombre Usuario]")`
    * `Tarjeta de Resumen: "Estado General de Cultivos"`
    * `Lista de Alertas Recientes`
    * `Botón Flotante (FAB) con icono de cámara: "Nuevo Análisis"`
* **Interacciones y Conexiones:**
    * Al hacer clic en `Botón Flotante "Nuevo Análisis"`, el usuario avanza a la pantalla **P2: Cámara de Análisis**.
* **Anotaciones Clave:** El dashboard debe cargar rápido y priorizar las alertas.

---

#### **P2: Cámara de Análisis**
* **Propósito:** Permitir al usuario capturar una imagen clara de la planta afectada.
* **Componentes UI Principales:**
    * `Vista de Cámara (ocupa casi toda la pantalla)`
    * `Marco o Guía superpuesta para encuadrar la hoja`
    * `Botón de Captura (grande y centrado)`
    * `Botón para activar/desactivar flash`
    * `Botón para salir/cancelar y volver a P1`
* **Interacciones y Conexiones:**
    * Al hacer clic en `Botón de Captura`, el sistema toma la foto y avanza a **P3: Confirmación de Imagen**.
* **Anotaciones Clave:** El sistema puede mostrar un breve consejo como "Asegúrate de que la imagen esté bien enfocada".

---

#### **P3: Confirmación de Imagen**
* **Propósito:** Permitir al usuario revisar la calidad de la foto antes de enviarla a analizar.
* **Componentes UI Principales:**
    * `Header: Título "¿Usar esta imagen?"`
    * `Placeholder de Imagen: Muestra la foto recién tomada`
    * `Botón Principal: "Analizar"`
    * `Botón Secundario: "Tomar Otra"`
* **Interacciones y Conexiones:**
    * Al hacer clic en `"Analizar"`, se muestra un indicador de carga y se avanza a **P4: Resultados del Diagnóstico**.
    * Al hacer clic en `"Tomar Otra"`, se regresa a **P2: Cámara de Análisis**.
* **Anotaciones Clave:** La pantalla de carga debe indicar que la IA está procesando la imagen.

---

**Continúa con las demás pantallas del flujo, como "Resultados del Diagnóstico", "Detalle de Recomendaciones", etc.**

---

### **Diagrama de Flujo (Mermaid)**

    ```mermaid
    graph BT
        subgraph "Flujo de Diagnóstico y Gestión"
            A[P1: Dashboard Principal] -->|Click en 'Nuevo Análisis'| B[P2: Cámara de Análisis];
            B -->|Click en 'Capturar'| C{P3: Confirmación de Imagen};
            C -->|Click en 'Tomar Otra'| B;
            C -->|Click en 'Analizar'| D[P4: Resultados del Diagnóstico];
            
            D -->|Click en 'Ver Recomendaciones'| E[P5: Detalle de Recomendaciones];
            D -->|Click en 'Guardar Reporte'| G[P7: Historial de Reportes];

            E -->|Click en 'Marcar Tareas'| F[P6: Plan de Trabajo];
            
            F -->|Navegación: Ir a Inicio| A;
            G -->|Navegación: Volver| A;
        end
    ```
```