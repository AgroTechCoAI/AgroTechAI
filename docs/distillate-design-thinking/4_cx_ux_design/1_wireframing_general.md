## Diseño CX/UX: Flujos de  Aplicación (Wireframing)

### Contexto

Con la Arquitectura de la Información ya definida, el equipo ha establecido el "qué" y el "dónde" de la aplicación. Ahora, el reto es diseñar el "cómo": el camino exacto, paso a paso, que seguirán los usuarios para interactuar con el sistema y resolver sus problemas.

El equipo es consciente de que una arquitectura lógica no garantiza una experiencia fluida. Un solo paso innecesario o un botón confuso puede hacer que el "Mayordomo de Finca" abandone la tarea en medio del cultivo. El éxito de la adopción depende de que el flujo para obtener un diagnóstico se sienta como un camino natural y sin obstáculos.

Por esta razón, esta fase de **Diseño de Flujos de Aplicación (Wireframing)** se compone de dos prompts:

#### Fase 1: La Generación Asistida del Wireflow (El Plano)

**Objetivo:** Crear un primer borrador detallado del flujo de usuario principal ("Diagnóstico por Imagen"), describiendo cada pantalla, sus componentes clave y las conexiones lógicas entre ellas. Se busca traducir la estrategia y la arquitectura en un plano estructural tangible.

#### Fase 2: La Simulación de Uso y Evaluación Sintética

**Objetivo:** Validar el wireflow v1.0 simulando cómo un arquetipo de usuario específico (ej. el "Mayordomo") "navegaría" a través de él. El objetivo es identificar puntos de fricción, posibles confusiones o mejoras de usabilidad antes de invertir tiempo y recursos en el diseño visual.

## Herramientas

Para su construcción se usaron las siguientes herramientas:
- **ChatGPT**
- **Gemini**
- **Claude**
- **Mermaid**

## Prompts

```markdown
### ROL: Diseñador de Experiencia de Usuario (UX) Senior y Especialista en Interacción

**OBJETIVO PRINCIPAL:**

Actúa como un Diseñador UX Senior de clase mundial, experto en crear flujos de aplicación intuitivos y eficientes para herramientas de software complejas, especialmente en el sector agrícola.

Tu misión es tomar toda la investigación, la estrategia funcional y la arquitectura de información proporcionada para diseñar un **Wireflow detallado** para una tarea de usuario clave. El resultado debe ser un "canvas" textual que describa, pantalla por pantalla, los componentes, las interacciones y el camino que un usuario seguiría para completar su objetivo. Este canvas será la base para la creación de prototipos y la evaluación sintética.

El diseño debe ser extremadamente amigable, considerando que los usuarios van desde agricultores con poca experiencia tecnológica hasta agrónomos expertos.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono el corpus completo de conocimiento sobre el producto, sus usuarios, sus funcionalidades y su estructura. Debes internalizar cada pieza de información antes de comenzar tu diseño.

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


#### **5. DEFINICIÓN Y SELECCIÓN DE FUNCIONALIDADES**

Toma como referencia las funcionalidades que te he suministrado en la base de tu conocimiento, especificamente en el archivo `2_def_y_select_func_general.md`.

-----

#### **6. DEFINICIÓN DE ESPECIFICACIONES**

Toma como referencia las especificaciones que te he suministrado en la base de tu conocimiento, especificamente en el archivo `3_def_specs_resultado.md`

-----

#### **7. ARQUITECTURA DE LA INFORMACIÓN (AI)**

Toma como referencia las especificaciones que te he suministrado en la base de tu conocimiento, especificamente en el archivo 
`1_arquitectura_informacion_resultado.md`

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