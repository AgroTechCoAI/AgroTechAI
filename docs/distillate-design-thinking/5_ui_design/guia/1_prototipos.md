### Guía para la Creación de Prototipos con GenAI

### 1\. ¿Qué son los Prototipos?

Imagina que estás construyendo una casa. Antes de poner un solo ladrillo, el arquitecto te muestra planos (wireframes) y luego una maqueta 3D o un recorrido virtual. Esa maqueta es el **prototipo**. No es la casa real, pero te permite caminar por ella, sentir los espacios, ver si la cocina es funcional y si las ventanas están en el lugar correcto, todo antes de gastar una fortuna en la construcción.

En el diseño de productos digitales, un prototipo es exactamente eso: **una simulación interactiva de la aplicación final.** Su propósito principal no es ser funcional, sino:

  * **Validar el Flujo de Usuario:** ¿Es fácil para un mayordomo de finca tomar una foto, subirla y entender el resultado? El prototipo nos permite probarlo.
  * **Probar la Usabilidad:** ¿Los botones son claros? ¿La información está donde el usuario espera encontrarla?
  * **Comunicar la Visión:** Es la mejor herramienta para mostrarle a los inversionistas, a otros departamentos y a los desarrolladores exactamente cómo se debe ver y sentir el producto.
  * **Ahorrar Dinero:** Detectar un error de diseño en un prototipo cuesta casi nada. Corregirlo cuando el producto ya está programado puede costar miles.

Existen diferentes "niveles" de prototipos, desde bocetos en papel (**baja fidelidad**) hasta diseños que parecen la aplicación final (**alta fidelidad**). Con GenAI, apuntaremos a crear prototipos de **alta fidelidad visual**, que son perfectos para validar el diseño y la experiencia general.

-----

### 2\. ¿Cómo se Construyen?

El proceso tradicional implica usar herramientas de diseño como Figma o Sketch para "dibujar" cada pantalla y luego conectar botones y elementos para simular la navegación.

Con la ayuda de GenAI, podemos acelerar drásticamente la parte del "dibujo". La IA no creará un prototipo interactivo directamente, pero puede generar las pantallas visuales de alta fidelidad con una consistencia y calidad asombrosas, basándose en todo el conocimiento que ya hemos recopilado. Estas imágenes luego pueden ser importadas a una herramienta para hacerlas interactivas o usarse directamente para obtener feedback visual.

Ahora, vamos a lo que nos interesa: el prompt para lograrlo.

-----

### 3\. El Prompt Maestro para Generar Prototipos Visuales

Este prompt está diseñado para ser un "todo en uno". Le darás a la IA todo el contexto que ya tienes, y le pedirás que actúe como un diseñador de producto experto para visualizar la interfaz.

**Recomendación:** La salida de este prompt serán descripciones detalladas y, si se usa en una IA generadora de imágenes (como Midjourney o DALL-E 3), las imágenes de las pantallas. La clave es generar una pantalla a la vez para mantener el control.

```markdown
### ROL: Diseñador de Producto y Experto en UI Senior

**OBJETIVO PRINCIPAL:**

Actúa como un Diseñador de Producto y Experto en Interfaces de Usuario (UI) de clase mundial, con una especialización galardonada en la creación de aplicaciones B2B robustas, intuitivas y hermosas para industrias complejas como la Agrotecnología (AgriTech).

Tu misión es **transformar** la documentación funcional, la arquitectura de información y los wireframes en un **prototipo visual de alta fidelidad**. Debes diseñar una interfaz que sea extremadamente fácil de usar para personas con poca experiencia tecnológica (como un trabajador de campo) pero que, al mismo tiempo, sea lo suficientemente potente y rica en datos para un experto (como un ingeniero agrónomo). El resultado final debe ser un conjunto de pantallas listas para ser presentadas, que sirvan como la visión definitiva del producto antes del desarrollo.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono el corpus completo de conocimiento sobre el producto, sus usuarios, su estructura y sus funcionalidades. Debes internalizar cada pieza de información antes de comenzar tu labor de diseño.

-----

#### **1. ARQUETIPOS DE USUARIO**
*Pega aquí el contenido del archivo `1_arquetipo_resultado.md`.*

-----

#### **2. SYSTEM MAP AS-IS**
*Pega aquí el contenido del archivo `2_systemmaps-as-is_resultado.md`.*

-----

#### **3. JOURNEY MAP AS-IS**
*Pega aquí el contenido del archivo `3_journeymaps-as-is_resultado.md`.*

-----

#### **4. JOBS TO BE DONE (JTBD)**
*Pega aquí el contenido del archivo `4_jtbd_resultado.md`.*

-----

#### **5. DEFINICIÓN Y SELECCIÓN DE FUNCIONALIDADES**
*Pega aquí el contenido del archivo `5_funcionalidades_resultado.md`.*

-----

#### **6. DEFINICIÓN DE ESPECIFICACIONES**
*Pega aquí el contenido del archivo `6_especificaciones_resultado.md`.*

-----

#### **7. ARQUITECTURA DE LA INFORMACIÓN**
*Pega aquí el contenido del canvas de Arquitectura de Información.*

-----

#### **8. WIREFRAMES**
*Pega aquí la descripción o las imágenes de los wireframes que ya han creado. Sé descriptivo. Ej: "Pantalla de inicio: un header con el logo, debajo una lista de tarjetas, cada tarjeta representa un cultivo. Abajo a la derecha, un botón flotante con un ícono de cámara."*

-----

**INSTRUCCIONES Y TAREAS (EJECÚTALAS EN ORDEN):**

**Paso 1: Síntesis Integral y Definición de Estilo Visual**
Analiza todos los documentos de entrada para comprender profundamente a los usuarios y sus necesidades. Luego, define un **mini sistema de diseño**.
* **Paleta de Colores:** Propón una paleta de colores inspirada en la agricultura moderna y la tecnología. Piensa en verdes (salud del cultivo), ámbar/naranja (alertas), azules (tecnología/IA) y tonos tierra (confiabilidad). Debe ser accesible y con buen contraste.
* **Tipografía:** Elige un par de fuentes (una para títulos, una para cuerpo de texto) que sean altamente legibles en pantallas de móvil, incluso bajo la luz del sol. Google Fonts es una buena fuente de inspiración.
* **Estilo de Iconografía:** Define si los iconos serán de línea, sólidos o a dos tonos. Deben ser universalmente comprensibles.
* **Estilo de Componentes:** Describe el estilo de los elementos clave: botones (redondeados, con sombra suave), tarjetas (bordes, elevación), campos de formulario, etc.

**Paso 2: Transformación de Wireframes a UI de Alta Fidelidad**
Toma los wireframes y la arquitectura de información como el esqueleto. Ahora, vístelos con el sistema de diseño que definiste. Tu tarea no es solo "colorear" los wireframes, sino mejorarlos, asegurando que la jerarquía visual sea perfecta y que la información más importante destaque.

**Paso 3: Creación del Canvas del Prototipo Visual (Pantalla por Pantalla)**
Genera el diseño para cada pantalla principal definida en la arquitectura y los wireframes. Para cada pantalla, proporciona una descripción detallada que permita a otra IA generadora de imágenes crearla visualmente.

**FORMATO DE SALIDA (EL CANVAS DEL PROTOTIPO):**

Utiliza el siguiente formato Markdown para describir cada pantalla. Sé extremadamente detallado en la descripción de los componentes.

-----

### **Canvas: Prototipo Visual para [Nombre del Producto]**

#### **Pantalla 1: Inicio / Dashboard**
* **Arquetipo Principal:** Mayordomo de Finca.
* **JTBD Asociado:** "Cuando empiezo mi día, quiero ver un resumen rápido del estado de mis cultivos y si hay alertas urgentes, para poder priorizar mi trabajo."
* **Descripción para GenAI de Imágenes:** "Una interfaz de app móvil limpia y moderna. En la parte superior, un saludo 'Buenos días, [Nombre Usuario]' y un ícono de notificaciones. Debajo, una sección de 'Alertas Urgentes' con tarjetas rojas o ámbar que muestran el problema (ej: 'Posible hongo en Lote 3'). La sección principal es una lista vertical de 'Mis Cultivos', donde cada cultivo es una tarjeta grande con una foto representativa, su nombre, y un indicador de salud visual (ej: un anillo de color verde, amarillo o rojo). En la esquina inferior derecha, un botón de acción flotante (FAB) de color azul con un ícono de una cámara y un signo de '+', que invita a hacer un nuevo análisis."

#### **Pantalla 2: Nuevo Análisis (Captura de Imagen)**
* **Arquetipo Principal:** Todos.
* **JTBD Asociado:** "Cuando veo algo raro en una planta, quiero capturar una imagen fácilmente y obtener un diagnóstico, para actuar de inmediato."
* **Descripción para GenAI de Imágenes:** "La interfaz de la cámara del móvil. En el centro, un recuadro o guía visual que indica al usuario cómo enfocar la hoja o el área afectada. Hay textos de ayuda como 'Asegura buena iluminación' y 'Enfoca bien la zona afectada'. En la parte inferior, un gran botón obturador para tomar la foto. Opciones para cambiar a la galería y subir una foto existente."

#### **Pantalla 3: Resultados del Análisis**
* **Arquetipo Principal:** Ingeniero Agrónomo, Mayordomo de Finca.
* **JTBD Asociado:** "Cuando recibo un diagnóstico, quiero entender claramente cuál es el problema, qué tan grave es y qué debo hacer al respecto, para poder ejecutar un plan de acción."
* **Descripción para GenAI de Imágenes:** "Una pantalla de resultados clara y fácil de digerir. En la parte superior, la imagen que el usuario subió. Debajo, el diagnóstico principal en letras grandes y con un código de color (ej: 'ALERTA ALTA: Roya del Café'). A continuación, un 'Nivel de Confianza de la IA' (ej: 95%). La pantalla se divide en pestañas: 'Diagnóstico', 'Sugerencias', 'Más Info'. La pestaña 'Diagnóstico' muestra detalles de la plaga/enfermedad. La pestaña 'Sugerencias' muestra una lista numerada de acciones recomendadas (ej: 1. Aplicar fungicida X, 2. Podar hojas afectadas). Cada sugerencia es un componente expandible para ver más detalles. El diseño debe inspirar confianza y claridad, no pánico."

*(Continúa este formato para todas las demás pantallas clave: Historial, Perfil, Configuración, etc.)*
```

-----

### 4\. ¿Hay una Herramienta Mejor?

Aquí seré muy directo: **Sí.**

Usar GenAI (como Midjourney, Stable Diffusion, etc.) con el prompt anterior es una forma **fantástica y económica para generar la dirección visual, crear un moodboard o incluso diseñar las pantallas clave de forma estática.** Es perfecto para la fase de ideación visual.

Sin embargo, un prototipo realmente cobra vida cuando es **interactivo**. Los usuarios necesitan poder hacer clic, navegar y sentir el flujo. Las imágenes generadas por IA son estáticas.

**La mejor solución es un enfoque híbrido:**

1.  **Usen el prompt maestro** con una herramienta como **Midjourney** para generar las pantallas visuales clave. Esto les dará un diseño de alta fidelidad increíblemente rápido y barato.
2.  Luego, utilicen esas imágenes como una referencia directa para reconstruir las pantallas en **Figma**.

**Figma** es la herramienta estándar de la industria para el diseño de interfaces y prototipado. Tiene una **generosa capa gratuita** que será más que suficiente para ustedes. Un miembro del equipo puede aprender los conceptos básicos de Figma en pocos días y, usando las imágenes de la IA como guía, podrá crear las pantallas y conectarlas con "hilos" para simular la navegación.

Este enfoque híbrido les da lo mejor de ambos mundos: la velocidad y el bajo costo de la IA para el diseño visual, y el poder de una herramienta profesional como Figma para crear el prototipo interactivo que realmente necesitan para las pruebas de usabilidad.

Espero que esta guía les sea de gran utilidad. ¡Estoy emocionado de ver lo que construirán\!