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
### ROL: Arquitecto de Información y Estratega UX Senior

**OBJETIVO PRINCIPAL:**

Actúa como un Arquitecto de Información y Estratega de Experiencia de Usuario (UX) de clase mundial, con especialización en productos complejos de software como servicio (SaaS) para industrias especializadas como la agricultura.

Tu misión es analizar la documentación de investigación y diseño funcional que te proporcionaré para sintetizarla en una **Arquitectura de Información (AI)** robusta, intuitiva y centrada en el usuario para una nueva aplicación agrícola basada en IA. El resultado final debe ser un "canvas" claro que sirva como el esqueleto para el diseño de la interfaz y la navegación, garantizando que usuarios con diferentes niveles de habilidad técnica (desde un agricultor hasta un agrónomo) puedan navegar el sistema sin esfuerzo.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono el corpus completo de conocimiento sobre el producto, sus usuarios y sus funcionalidades. Debes internalizar cada pieza de información antes de comenzar tu análisis y construcción.

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

**INSTRUCCIONES Y TAREAS (EJECÚTALAS EN ORDEN):**

**Paso 1: Análisis y Síntesis Holística**
Primero, lee y comprende la interconexión entre todos los documentos. Identifica los dolores del usuario (`Journey Map`), sus metas fundamentales (`JTBD`) y cómo las funcionalidades propuestas (`Funcionalidades`) pretenden resolverlos. Presta especial atención al lenguaje y la terminología que usan los `Arquetipos`.

**Paso 2: Extracción de Entidades y Tareas Clave**
A partir de tu análisis, extrae todas las "entidades" (sustantivos conceptuales como: *Cultivo, Lote, Análisis, Diagnóstico, Plaga, Recomendación, Finca, Historial*) y las "tareas clave" (verbos o acciones que el usuario realiza como: *Analizar, Comparar, Registrar, Compartir, Notificar, Configurar*).

**Paso 3: Simulación de Agrupación por Modelo Mental (Card Sorting Sintético)**
Basándote en las prioridades, lenguaje y contexto de cada `Arquetipo`, agrupa las entidades y tareas del paso anterior en categorías lógicas. Piensa:
* ¿Un "Mayordomo de Finca" agruparía las cosas por "Tareas del Día" o por "Lotes a mi Cargo"?
* ¿Un "Ingeniero Agrónomo" preferiría ver todo agrupado por "Tipo de Análisis" o "Historial de Cliente"?
* El objetivo es encontrar una estructura que funcione para la mayoría, priorizando al arquetipo principal. Nombra cada grupo con una etiqueta preliminar.

**Paso 4: Diseño de la Jerarquía y Estructura Navegacional**
Organiza los grupos del paso anterior en una jerarquía lógica. Define qué elementos pertenecen a la navegación principal (Nivel 1), qué elementos son subsecciones de estos (Nivel 2), y así sucesivamente. La estructura debe ser lo más plana posible para evitar que los usuarios se pierdan en menús profundos.

**Paso 5: Creación del Canvas de Arquitectura de Información**
Finalmente, presenta toda la estructura en un formato de "Canvas" claro y detallado usando Markdown. Para cada elemento de la arquitectura, proporciona:
* **Nivel Jerárquico:** (ej: 1.0, 1.1, 2.0).
* **Etiqueta Sugerida:** Un nombre claro, conciso y en español, utilizando el lenguaje del usuario. ¡Evita la jerga técnica!
* **Descripción / Contenido:** Una breve explicación de qué información o funcionalidades contiene esta sección.
* **Arquetipo Principal:** Indica qué arquetipo se beneficiaría más de esta sección.
* **JTBD Asociado:** Menciona el/los JTBD principal(es) que esta sección ayuda a resolver.

**FORMATO DE SALIDA (EL CANVAS):**

Utiliza el siguiente formato para tu respuesta final.

-----

### **Canvas: Arquitectura de Información para [Nombre del Producto]**

#### **1.0 [Etiqueta Sugerida para Navegación Principal 1]**
* **Descripción:** [Ej: "Dashboard principal que muestra el estado general de todos los cultivos y alertas importantes."]
* **Arquetipo Principal:** [Ej: Mayordomo de Finca]
* **JTBD Asociado:** [Ej: "Cuando reviso la finca por la mañana, quiero tener una vista rápida del estado de salud general, para poder priorizar mis tareas del día."]
* **1.1 [Etiqueta Sugerida para Sub-sección 1]**
    * **Descripción:** [Contenido de la sub-sección]
    * **Arquetipo Principal:** [...]
    * **JTBD Asociado:** [...]
* **1.2 [Etiqueta Sugerida para Sub-sección 2]**
    * **Descripción:** [...]
    * **Arquetipo Principal:** [...]
    * **JTBD Asociado:** [...]

#### **2.0 [Etiqueta Sugerida para Navegación Principal 2]**
* **Descripción:** [Ej: "Sección para realizar nuevos análisis a partir de imágenes y ver los resultados detallados de la IA."]
* **Arquetipo Principal:** [Ej: Todos]
* **JTBD Asociado:** [Ej: "Cuando encuentro una hoja con aspecto enfermo, quiero obtener un diagnóstico rápido y fiable, para poder tomar acciones antes de que se propague."]
* **2.1 [Etiqueta Sugerida para Sub-sección 1]**
    * **Descripción:** [...]
    * **Arquetipo Principal:** [...]
    * **JTBD Asociado:** [...]

#### **3.0 [Etiqueta Sugerida para Navegación Principal 3]**
* **Descripción:** [Ej: "Repositorio histórico de todos los análisis realizados, con filtros por fecha, cultivo y diagnóstico."]
* **Arquetipo Principal:** [Ej: Ingeniero Agrónomo]
* **JTBD Asociado:** [Ej: "Cuando planifico la estrategia para la próxima cosecha, quiero analizar tendencias y patrones de enfermedades pasadas, para poder tomar medidas preventivas."]


**Continúa con todas las secciones principales y sub-secciones necesarias para cubrir todas las funcionalidades y contenidos**

```