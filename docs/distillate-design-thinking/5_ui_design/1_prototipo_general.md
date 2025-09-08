# Diseño de Prototipos de Alta Fidelidad

## Contexto

Con los flujos de la aplicación y los wireframes ya definidos, el equipo tiene el esqueleto funcional del producto. Se ha trazado el camino lógico que un usuario seguirá para obtener un diagnóstico.

Sin embargo, un esqueleto no es suficiente para generar confianza y adopción. Para que un agricultor o un agrónomo confíe en un diagnóstico de IA, la interfaz debe sentirse tan profesional y precisa como la tecnología que la impulsa. Los wireframes muestran el camino, pero no transmiten la emoción, la claridad visual ni la facilidad de uso que el producto final necesita para tener éxito en el campo. Un diseño poco profesional puede generar desconfianza en los resultados, sin importar cuán avanzada sea la IA.

Por esta razón, esta fase de **Diseño de Prototipos de Alta Fidelidad** se enfoca en dar vida a esos planos estructurales, transformándolos en una simulación visualmente rica y realista de la experiencia final.

### **El Prompt: La Generación Asistida de la Interfaz Visual**

**Objetivo:** Utilizar la inteligencia artificial generativa como un co-diseñador experto para acelerar drásticamente la creación de la interfaz de usuario (UI). Se busca traducir los wireframes y toda la investigación previa en pantallas pulidas y listas para ser ensambladas en un prototipo interactivo, asegurando que el diseño sea intuitivo, estéticamente agradable y que refuerce la credibilidad del producto.

### Herramientas

Para la construcción de este artefacto y el flujo de trabajo asociado se utilizaron las siguientes herramientas:

* **Stitch:** Para la generación de la interfaz de usuario (UI) de alta fidelidad a partir de prompts y wireframes.
* **Gemini:** Como modelo de lenguaje que potencia a Stitch y ayuda en la refinación de los prompts.

## Prompts
```markdown
# Generación de Prototipos a partir de un Flujo Textual

# ROL: Diseñador de Producto y Experto en UI Senior

**OBJETIVO PRINCIPAL:**

Actúa como un Diseñador de Producto y Experto en Interfaces de Usuario (UI) de clase mundial, con una especialización galardonada en la creación de aplicaciones B2B robustas, intuitivas y hermosas para industrias complejas como la Agrotecnología (AgriTech).

Tu misión es **transformar** la documentación de investigación y un **flujo de aplicación descrito textualmente** en un **prototipo visual de alta fidelidad.** Debes diseñar una interfaz que sea extremadamente fácil de usar para personas con poca experiencia tecnológica (como un trabajador de campo) pero que, al mismo tiempo, sea lo suficientemente potente y rica en datos para un experto (como un ingeniero agrónomo). El resultado final debe ser un conjunto de descripciones detalladas de pantallas listas para ser generadas, que sirvan como la visión definitiva del producto antes del desarrollo.

**CONTEXTO (INFORMACIÓN DE ENTRADA):**

A continuación, te proporciono el corpus completo de conocimiento sobre el producto, sus usuarios y, más importante, el flujo de pantallas y acciones. Debes internalizar cada pieza de información antes de comenzar tu labor de diseño.

-----

## **1. ARQUETIPOS DE USUARIO**

### ARQUETIPO 1: Agrónomo asesor independiente

**👤 PERFIL PERSONAL**

* **Nombre:** *Laura Restrepo*
* **Edad:** 32–45
* **Ubicación:** Eje Cafetero – municipios rurales con conectividad irregular
* **Educación:** Ing. Agrónoma (pregrado), diplomados en fitopatología
* **Experiencia:** 8–15 años
* **Familia:** Hijos en edad escolar; organiza rutas para compatibilizar familia/visitas

**🏢 CONTEXTO PROFESIONAL**

* **Rol:** Consultora agronómica multicliente (café/frutales/arroz de rotación)
* **Responsabilidades:** Diagnóstico, prescripción, capacitación y seguimiento; reportes a clientes
* **Tamaño de operación:** 40–80 lotes/mes (varios clientes); sin empleados directos
* **Cultivos principales:** Café, cítricos, plátano, arroz de riego
* **Estacionalidad:** Picos en lluvias (enfermedades foliares) y cosecha
* **Estructura:** Reporta a dueños/gerentes de finca; coordina con mayordomos/técnicos
* **Presupuesto tecnología:** 2–5 M COP/año (licencias, datos, equipo)

**📱 RELACIÓN CON TECNOLOGÍA**

* **Dispositivos:** Smartphone Android + laptop liviana
* **Apps actuales:** Cámara, WhatsApp/WhatsApp Business, Drive/Sheets, IDEAM (clima)
* **Confianza tecnológica:** 8/10 (si ve ROI y ahorra tiempo)
* **Canales de info:** WhatsApp, YouTube técnico, boletines gremiales
* **Barreras:** Señal móvil irregular; carga de fotos/pesos; heterogeneidad de clientes
* **Soporte:** Colegas y proveedores de insumos

**🎯 OBJETIVOS Y MOTIVACIONES**

* **Principal:** **Detectar temprano** y recomendar con evidencia para reducir pérdidas
* **Éxito:** Menos incidencias y menor costo/ha; clientes renovando contrato
* **Métricas:** % lotes con control oportuno; severidad promedio; días a respuesta
* **Motivadores:** Diferenciarse con analítica/imagen; generar reportes “listos para WhatsApp”
* **Presiones:** Brotes cuarentenarios (TR4/HLB), clima (El Niño/La Niña), tiempos de viaje ([FAOLEX][4])

**😤 FRUSTRACIONES**

* Diagnósticos tardíos por “ojímetro” del operario
* Subir fotos con mala señal
* Que el cliente no siga la recomendación y culpe al diagnóstico

**🔄 ESCENARIOS DE USO**

* **Escenario 1: “Roya en banda”**

  * **Situación:** Café con manchas anaranjadas tras semana húmeda
  * **Frecuencia:** Estacional lluvias
  * **Ubicación:** Lote en ladera, señal baja
  * **Urgencia:** Alta (48 h para decisión)
  * **Info requerida:** Severidad/índice foliar, focos, recomendación de mezcla y calendario
  * **Decisiones:** Aplicar vs. esperar; dosis; priorización de lotes
  * **Error:** Pérdida de hojas, mermas en cosecha
* **Escenario 2: “HLB sospechoso”**

  * **Situación:** Cítrico con moteado asimétrico; se requiere descarte temprano
  * **Frecuencia:** Ad-hoc
  * **Urgencia:** Alta por norma sanitaria (trazabilidad/aislamiento) ([FAOLEX][4])
* **Escenario 3: “Reporte al cliente ya”**

  * **Situación:** En el campo necesita un PDF/WhatsApp con fotos, diagnóstico y plan
  * **Urgencia:** Alta; en la ruta entre fincas

**💬 CITAS**

* “Si puedo **detectar antes**, ahorro plata al productor.”
* “Dame un **score objetivo** y listo, yo traduzco a manejo.”
* “Si el informe sale directo a **WhatsApp**, lo implementan mañana.”

**🎨 CONTEXTO VISUAL**

* **Entorno:** Fincas en ladera; invernaderos pequeños; arrozales en planicie
* **Vestimenta:** Botas, jean, camisa manga larga
* **Herramientas:** Smartphone, cintas de marcación, cuaderno impermeable
* **Vehículo:** Motocicleta o pick-up compartida

---

## ARQUETIPO 2: Administrador/Mayordomo (café/banano/palma)

**👤 PERFIL PERSONAL**

* **Nombre:** *Luis Alberto Mosquera*
* **Edad:** 28–50 | **Ubicación:** Antioquia/Urabá/Meta (perennes)
* **Educación:** Media técnica o SENA; cursos MIP
* **Experiencia:** 6–20 años | **Familia:** Vive en finca o vereda cercana

**🏢 CONTEXTO PROFESIONAL**

* **Rol:** Coordina jornales, aplica insumos, levanta alertas
* **Tamaño:** 20–100 ha; 10–60 trabajadores temporales
* **Cultivos:** Banano/plátano, palma, café
* **Estacionalidad:** Trabajo continuo; picos por lluvia/vendavales
* **Organización:** Reporta a dueño/gerente; recibe guía de ingeniero
* **Presupuesto tecnología:** 3–8 M COP/año (dispositivos/planes de datos)

**📱 TECNOLOGÍA**

* **Dispositivos:** Smartphone robusto; radio VHF en banano
* **Apps:** WhatsApp, cámara, notas; a veces app corporativa
* **Confianza:** 7/10 (si es simple)
* **Canales:** WhatsApp, proveedor de insumos, compañeros
* **Barreras:** Señal inestable; rotación de personal
* **Soporte:** Ingeniero de empresa / proveedor

**🎯 OBJETIVOS**

* **Principal:** Ejecutar **rápido y bien** (coberturas, dosis, ventanas)
* **Éxito:** Menos re-trabajos; cero sanciones fitosanitarias (TR4, HLB) ([Comunidad Andina][5], [FAOLEX][4])
* **Métricas:** % lotes a tiempo, rechazos, mermas

**😤 FRUSTRACIONES**

* “Me mandan fotos borrosas y deciden tarde.”
* Conectividad mala al subir evidencias
* Checklists en papel que se pierden

**🔄 ESCENARIOS**

* **1: “Sospecha de Sigatoka/TR4” (banano/plátano)**

  * **Urgencia:** Crítica (bioseguridad y contención) ([Instituto Geográfico Agustín Codazzi][8])
  * **Necesita:** Marco de fotos guiadas, geocerca, protocolo y ‘qué hacer ahora’
* **2: “Raleo/fertilización priorizada” (palma/café)**

  * **Urgencia:** Alta por clima (ventana corta)
  * **Necesita:** Mapa de focos y listas accionables por lote
* **3: “Auditoría interna”**

  * **Urgencia:** Media
  * **Necesita:** PDF con evidencias (antes/después) y registro del equipo

**💬 CITAS**

* “Si la app me dice **a quién mando y con qué**, yo corro.”
* “Quiero que el jefe vea el **antes-después** sin buscarme.”
* “Offline y que **sin señal** guarde todo.”

**🎨 VISUAL**

* **Entorno:** Lotes planos (banano/palma) o ladera (café)
* **Vestimenta:** Pantalón resistente, camisa, EPP
* **Herramientas:** Mochila de campo, marcador de árboles, smartphone con carcasa
* **Vehículo:** Moto/enduro, cuatrimoto o campero

---

## ARQUETIPO 3: Productor mediano (arroz/papa/maíz)

**👤 PERFIL**

* **Nombre:** *Diana Cárdenas*
* **Edad:** 30–48 | **Ubicación:** Llanos, Tolima, Nariño, Boyacá
* **Educación:** Técnica/tecnológica; cursos gremiales (Fedearroz, Fedepapa)
* **Experiencia:** 7–15 años | **Familia:** Negocio familiar con 2–5 trabajadores

**🏢 CONTEXTO**

* **Tamaño:** 15–80 ha; contrataciones por campaña
* **Cultivos:** Arroz (riego/sequía), papa, maíz
* **Estacionalidad:** Ventanas de siembra y control ajustadas a clima
* **Estructura:** Decide con asesor externo y agroinsumo
* **Presupuesto tech:** 1–3 M COP/año

**📱 TECNOLOGÍA**

* **Dispositivos:** Android gama media; a veces tablet barata
* **Apps:** WhatsApp, cámara, Excel/Drive; pronóstico local
* **Confianza:** 7/10 (si es práctica y barata)
* **Barreras:** Datos caros; cobertura irregular; curva de aprendizaje
* **Soporte:** Técnico de agroinsumo / asesor

**🎯 OBJETIVOS**

* **Principal:** Reducir **pérdidas por enfermedades** (p. ej., **añublo/Pyricularia** en arroz) y optimizar costos. ([Fedearroz][3])
* **Éxito:** Rendimiento/ha y costo/ha bajo control; menos aplicaciones “a ciegas”
* **Métricas:** Rendimiento, IAF/NDVI (si contrata), nº aplicaciones

**😤 FRUSTRACIONES**

* Diagnóstico tardío (cuando ya llovió 3 días)
* Recomendaciones contradictorias
* Compras de insumo sin certeza de necesidad

**🔄 ESCENARIOS**

* **1: “¿Es Pyricularia o mancha foliar?”**

  * **Urgencia:** Alta en picos de humedad/temperatura
  * **Necesita:** Probabilidad por imagen + severidad + umbral sugerido
* **2: “Deficiencia nutricional vs. estrés hídrico”**

  * **Urgencia:** Media-alta
  * **Necesita:** Pistas visuales + recomendación de verificación (conductímetro/suelo)
* **3: “Comparar lotes”**

  * **Urgencia:** Media
  * **Necesita:** Informe simple por WhatsApp para decidir inversión del día

**💬 CITAS**

* “Si me ahorra **una aplicación**, ya se pagó.”
* “Quiero que la foto me diga **qué tan grave** y **qué hago hoy**.”
* “Necesito algo que funcione con **señal floja**.”

**🎨 VISUAL**

* **Entorno:** Parcelas planas de riego o ladera fría (papa)
* **Vestimenta:** Gorra, botas, impermeable
* **Herramientas:** Smartphone, cuaderno, medidor simple
* **Vehículo:** Camioneta doble cabina o moto

---

## ARQUETIPO 4: Técnico agrícola (cooperativa/insumos)

**👤 PERFIL**

* **Nombre:** *Jhonatan Pacheco* | **Edad:** 24–35
* **Ubicación:** Huila, Tolima, Eje Cafetero, Caribe bananero
* **Educación:** Tecnólogo agropecuario
* **Experiencia:** 3–8 años | **Familia:** Vive en cabecera municipal

**🏢 CONTEXTO**

* **Rol:** Atiende 60–120 productores/mes; levanta casos y da seguimiento
* **Cultivos:** Café, arroz, plátano, frutales
* **Estructura:** Reporta a coordinador técnico/comercial
* **Presupuesto tech:** 1–2 M COP/año (empresa aporta plan de datos)

**📱 TECNOLOGÍA**

* **Dispositivos:** Smartphone corporativo; a veces tablet
* **Apps:** WhatsApp, cámara, formularios propios
* **Confianza:** 8/10 (si acelera visitas)
* **Barreras:** Subir evidencias con poca señal; estandarizar fotos
* **Soporte:** Área de TI/coordinación

**🎯 OBJETIVOS**

* Estandarizar **captura de evidencia** y dar **recomendación consistente**
* Medir impacto (antes/después) para justificar ventas/servicio

**🔄 ESCENARIOS**

* **1: “Ruta de visitas con alertas”** — priorizar fincas por riesgo (clima/fenología)
* **2: “Capacitación con ejemplos locales”** — usar galería de casos etiquetados
* **3: “Cierre de caso”** — enviar reporte corto (PDF/WhatsApp) con plan de acción

**💬 CITAS**

* “Quiero **estandarizar** cómo tomo fotos.”
* “Un **semáforo** (verde-amarillo-rojo) me ahorra discusiones.”
* “PDF corto y **compartible** o no lo leen.”

## **1. JOBS TO BE DONE**

# **Arquetipo: Agrónomo/a asesor/a independiente**  
(Eje Cafetero, Oriente antioqueño, Urabá)

---

## **Paso 1: Simulación de Entrevista Interna**

1. **Día a día**  
   Lo primero es revisar WhatsApp y llamadas de fincas en Jardín, Andes, Rionegro o Urabá. Organizo la ruta según urgencia (roya, Sigatoka, sospecha de TR4) y clima. Como a veces no hay señal, dejo listos formatos y plantillas para evidencias y priorizo lotes por riesgo.

2. **Última gran frustración**  
   Tras un aguacero, encontré un lote de café con pústulas incipientes. Me exigían respuesta “ya”, pero el camino estaba intransitable y la luz pésima para fotos. Sentí que, si me equivocaba por apuro, perdía la confianza del cliente.

3. **Lo más difícil**  
   Decidir sin imágenes claras ni conectividad. Me bloqueé por el riesgo de un falso negativo/positivo que implicara gasto innecesario.

4. **Objetivo real**  
   Priorizar los lotes de mayor riesgo y entregar un plan de acción en 24–48 horas, con recomendaciones ejecutables de inmediato.

5. **Proceso ideal (varita mágica)**  
   Captura guiada “offline” con mejora de imagen, umbrales de acción por lote/subregión y reporte listo “para WhatsApp” (mapa + evidencia) sin depender de la señal.

6. **Qué significa el éxito**  
   Reputación sólida: diagnósticos consistentes, intervenciones oportunas y ahorro real para el productor (insumos/jornales).

7. **Herramientas probadas**  
   Grupos de WhatsApp, guías impresas, apps básicas de cámara/notas. Sigo con lo práctico; abandono lo que exija datos móviles estables o mucho tiempo de escritorio.

8. **Decisiones con más incertidumbre**  
   Cuándo escalar a laboratorio vs. tratamiento preventivo; y el umbral exacto para recomendar aspersión.

---

## **Paso 2: Resultados — Jobs to be Done (JTBD)**

### **JTBD #1**

> **Cuando** recibo múltiples alertas tras lluvias fuertes y hay baja iluminación y poca señal,  
> **quiero** priorizar rápidamente los lotes críticos con un umbral de acción claro por subregión,  
> **para poder** emitir recomendaciones confiables en 24–48 h y mantener mi reputación.

- **Luchas / Puntos de dolor**
  - Imágenes deficientes y sin conectividad.  
  - Riesgo de falsos negativos/positivos que erosionan la confianza.  
  - Vías terciarias que retrasan la verificación en campo.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Priorización por severidad y lote; reporte listo para envío.  
  - **Emocionales:** Sentirme seguro y consistente.  
  - **Sociales:** Ser visto como referente serio en la zona.

- **Citas clave**
  > “Si me equivoco por afán, pierdo al cliente para siempre.”  
  > “Necesito umbrales accionables aunque esté sin señal.”

---

### **JTBD #2**

> **Cuando** la evidencia de campo es ambigua (pústulas incipientes, daño por granizo parecido a patógeno),  
> **quiero** asistencia en captura/mejora de imagen y pruebas rápidas sugeridas,  
> **para poder** reducir la incertidumbre y evitar gastos innecesarios al productor.

- **Luchas / Puntos de dolor**
  - Calidad de imagen y sintomatología similar.  
  - Presión de tiempo y temor a sobretratar.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Guía de captura + checklist de confirmación.  
  - **Emocionales:** Bajar la ansiedad de “errar por falta de datos”.  
  - **Sociales:** Mantener autoridad técnica frente al cliente.

- **Citas clave**
  > “Con luz mala, todo parece lo mismo.”  
  > “Prefiero una prueba de campo antes que recetar a ciegas.”

---

### **JTBD #3**

> **Cuando** debo entregar evidencia a clientes o cooperativas,  
> **quiero** generar reportes georreferenciados listos para WhatsApp,  
> **para poder** cerrar casos con trazabilidad sin perder horas en escritorio.

- **Luchas / Puntos de dolor**
  - Armado manual de informes; señal intermitente.  
  - Estandarización de fotos, fechas y firmas.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** PDF/imagen comprimida offline con subida diferida.  
  - **Emocionales:** Tranquilidad de “caso bien cerrado”.  
  - **Sociales:** Transparencia que refuerza la confianza.

- **Citas clave**
  > “Si no queda por escrito y con fotos, no existió.”  
  > “Quiero que el informe salga de una, no en la noche.”


# **Arquetipo: Administrador/Mayordomo**  
_(Café Suroeste antioqueño; plátano/banano Urabá)_

---

## **Paso 1: Simulación de Entrevista Interna**

1. **Día a día**  
   Empiezo revisando clima, cuadrillas disponibles y estado de lotes. Ajusto tareas según ventanas de aspersión, disponibilidad de equipos/EPP y prioridades fitosanitarias. Coordino insumos, transporte y permisos de ingreso.

2. **Última gran frustración**  
   Recibí alerta de Sigatoka con lluvia en puerta: la mezcla estaba lista, pero no tenía certeza de qué lote priorizar ni evidencia suficiente para justificar el cambio de plan. La presión era “resultados para ya”.

3. **Lo más difícil**  
   Coordinar gente, insumos y clima con información incompleta. Temí aplicar tarde o en el lote equivocado y perder dinero y tiempo.

4. **Objetivo real**  
   Reducir rechazos y cumplir la ventana ideal de aspersión con respaldo documental para auditoría y para mi jefe.

5. **Proceso ideal (varita mágica)**  
   Un semáforo por lote (rojo/amarillo/verde) que me indique prioridad, mezcla y EPP; checklist guiado con fotos georreferenciadas y generación automática de un PDF de evidencia.

6. **Qué significa el éxito**  
   Orden operativo, menos reprocesos y cuadrillas enfocadas. Que el jefe vea consistencia y que las auditorías pasen sin observaciones.

7. **Herramientas probadas**  
   Radios, hojas impresas, Excel, fotos con el celular. Abandono apps complejas o que el personal no entiende en campo.

8. **Decisiones con más incertidumbre**  
   Cambiar mezcla o reprogramar aspersión por clima; autorizar ingreso según bioseguridad y protocolos.

---

## **Paso 2: Resultados — Jobs to be Done (JTBD)**

### **JTBD #1**

> **Cuando** hay alerta fitosanitaria y el clima cierra la ventana de aspersión,  
> **quiero** un semáforo por lote con tareas, mezcla y EPP,  
> **para poder** reubicar cuadrillas y cumplir metas sin reprocesos.

- **Luchas / Puntos de dolor**
  - Ventanas climáticas estrechas y cambiantes.  
  - Coordinación simultánea de personal, equipos y rutas.  
  - Presión de la gerencia por resultados inmediatos.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Priorización operativa y checklist accionable.  
  - **Emocionales:** Sentirme en control del día.  
  - **Sociales:** Demostrar liderazgo y fiabilidad ante el equipo y el jefe.

- **Citas clave**
  > “No puedo fallar por desorden, no por técnica.”  
  > “Dígame qué lote va primero y con qué mezcla.”

---

### **JTBD #2**

> **Cuando** viene auditoría o cierre de mes,  
> **quiero** generar evidencia ‘antes/después’ en un PDF georreferenciado,  
> **para poder** responder hallazgos sin cazar papeles.

- **Luchas / Puntos de dolor**
  - Pruebas dispersas en celulares/hojas sueltas.  
  - Formatos distintos y pérdida de tiempo consolidando.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Estandarizar fotos, fechas, firmas y ubicación.  
  - **Emocionales:** Alivio al pasar auditoría sin observaciones.  
  - **Sociales:** Mostrar gestión ordenada y profesional.

- **Citas clave**
  > “Sin fotos y fechas, todo se cuestiona.”  
  > “El cierre debe armarse solo.”

---

### **JTBD #3**

> **Cuando** ingreso personal o vehículos de proveedores,  
> **quiero** una lista de bioseguridad con registro fotográfico,  
> **para poder** autorizar o negar entrada con respaldo.

- **Luchas / Puntos de dolor**
  - Ambigüedad de cumplimiento y trazabilidad en portería.  
  - Responsabilidad personal ante incidentes.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Checklist simple, sellos/firmas y evidencia visual.  
  - **Emocionales:** Seguridad y tranquilidad al decidir.  
  - **Sociales:** Resguardar la reputación de la finca.

- **Citas clave**
  > “La portería no puede ser un cuello de botella ni un coladero.”  
  > “Prefiero negar con evidencia que asumir el riesgo.”

# **Arquetipo: Productor mediano (papa / maíz / aguacate Hass)**  
_(Antioquia, Eje Cafetero y zonas aledañas)_

---

## **Paso 1: Simulación de Entrevista Interna**

1. **Día a día**  
   Reviso los lotes temprano; si veo manchas, clorosis o daños, tomo fotos y consulto a mi círculo (vecinos, técnico de confianza). Compro insumos en la agropecuaria local según consejo y presupuesto. Ajusto labores según clima y disponibilidad de mano de obra.

2. **Última gran frustración**  
   Tras una granizada en papa, no sabía si era solo daño mecánico o si ya había tizón. Estuve a punto de gastar en fungicida que quizá no hacía falta. Me preocupó perder plata y tiempo.

3. **Lo más difícil**  
   Distinguir síntomas parecidos y decidir si aplicar o esperar. El miedo es “que no pegue” por clima o que sea tarde cuando actúe.

4. **Objetivo real**  
   Evitar gastos inútiles y proteger rendimiento, aplicando lo justo y a tiempo.

5. **Proceso ideal (varita mágica)**  
   Comparación guiada “antes/después” por lote, con una recomendación clara (aplicar/no aplicar) que funcione incluso sin señal. Si hace falta, un paso simple de verificación en campo.

6. **Qué significa el éxito**  
   Flujo de caja sano, menos pérdidas en empaque (Hass) y decisiones más seguras sin sobretratar.

7. **Herramientas probadas**  
   YouTube, Google, grupos de WhatsApp, visitas del técnico cuando se puede. Me quedo con lo rápido y práctico; abandono lo caro o lo que dependa de internet estable.

8. **Decisiones con más incertidumbre**  
   Cuándo enviar muestra a laboratorio vs. hacer un ensayo pequeño; momento de cosecha selectiva en Hass para reducir rechazo.

---

## **Paso 2: Resultados — Jobs to be Done (JTBD)**

### **JTBD #1**

> **Cuando** veo síntomas dudosos después de una granizada o lluvias,  
> **quiero** diferenciar daño mecánico de enfermedad con una guía práctica,  
> **para poder** evitar aplicaciones innecesarias y cuidar el flujo de caja.

- **Luchas / Puntos de dolor**
  - Síntomas similares que confunden.  
  - Temor a perder rendimiento por decidir mal.  

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Comparativa visual y pasos claros de verificación.  
  - **Emocionales:** Calma de no gastar por gastar.  
  - **Sociales:** Ser visto como productor que administra bien.

- **Citas clave**
  > “Cada tanque mal aplicado duele en el bolsillo.”  
  > “Necesito una pista clara antes de comprar.”

---

### **JTBD #2**

> **Cuando** dudo si cosechar Hass con antracnosis leve,  
> **quiero** una recomendación de cosecha selectiva y manejo poscosecha,  
> **para poder** reducir pérdidas y rechazos en empaque.

- **Luchas / Puntos de dolor**
  - Mermas por decisiones tardías o mal calibradas.  
  - Exigencias del comprador y variabilidad del clima.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Etiquetado de severidad y guías poscosecha.  
  - **Emocionales:** Confianza al decidir.  
  - **Sociales:** Cumplir estándares del comprador.

- **Citas clave**
  > “El fruto que rechazo es plata que se fue.”  
  > “Si me dicen ‘apto/no apto’, actúo rápido.”

---

### **JTBD #3**

> **Cuando** evalúo prácticas (con/sin cobertura, fertilización fraccionada),  
> **quiero** comparar ‘antes/después’ por lote con un score simple,  
> **para poder** quedarme con lo que realmente funciona y descartar lo que no.

- **Luchas / Puntos de dolor**
  - Ensayos caseros sin método y memoria sesgada.  
  - Dificultad para cuantificar mejoras.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Evidencia visual y métrica básica por lote.  
  - **Emocionales:** Satisfacción de elegir con datos.  
  - **Sociales:** Mostrar decisiones “con prueba” frente a la familia o socios.

- **Citas clave**
  > “Quiero ver la diferencia, no imaginarla.”  
  > “Lo que se mide, mejora.”

# **Arquetipo: Técnico agrícola (cooperativa / insumos)**  
_(Antioquia, Eje Cafetero, Urabá)_

---

## **Paso 1: Simulación de Entrevista Interna**

1. **Día a día**  
   Tengo una ruta con 15–20 visitas. Priorizo por urgencia y ubicación, mezclo el rol técnico con metas comerciales mensuales. La señal es irregular, así que planifico mapas y contactos offline. Documentar bien cada caso es clave para no repetir visitas.

2. **Última gran frustración**  
   En mitad de una captura, mi teléfono de baja gama se quedó sin memoria y la app se cerró. Perdí fotos y notas. Tuve que volver a la finca al día siguiente y el productor quedó molesto.

3. **Lo más difícil**  
   Mantener consistencia entre recomendaciones y no contradecir protocolos de la empresa, especialmente cuando las condiciones de campo cambian y hay presión por cerrar la venta.

4. **Objetivo real**  
   Cerrar casos con un reporte estándar y claro, disminuyendo visitas repetidas por el mismo problema y fortaleciendo la confianza del productor.

5. **Proceso ideal (varita mágica)**  
   Un mapa offline que ordene los casos por riesgo y distancia, un “modo lite” para fotos comprimidas que no se caiga, y una plantilla de informe instantáneo que pueda compartir al terminar la visita.

6. **Qué significa el éxito**  
   Menos quejas, más confianza, y cumplir metas de cierre sin sacrificar criterio técnico. Ser reconocido por soluciones eficaces y trazables.

7. **Herramientas probadas**  
   Plantillas en Excel/Drive, folletos impresos, demos en ferias. Mantengo lo que estandariza y funciona sin señal. Abandono apps pesadas o confusas para el campo.

8. **Decisiones con más incertidumbre**  
   Cuándo dar una recomendación provisional (noche/foto) y cuándo exigir verificación diurna; y cuándo escalar a laboratorio antes de proponer mezcla.

---

## **Paso 2: Resultados — Jobs to be Done (JTBD)**

### **JTBD #1**

> **Cuando** tengo una ruta con muchas visitas y la señal es irregular,  
> **quiero** priorizar casos en un mapa offline con riesgo y distancia,  
> **para poder** maximizar el impacto de la jornada y cumplir metas sin devoluciones innecesarias.

- **Luchas / Puntos de dolor**
  - Logística en veredas, tiempo muerto por navegación.  
  - Reprogramaciones por clima/señal.  
  - Expectativas comerciales y técnicas en tensión.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Orden de visitas por criticidad y cercanía; notas estandarizadas.  
  - **Emocionales:** Sensación de jornada fluida y productiva.  
  - **Sociales:** Ser percibido como eficiente por la empresa y por los productores.

- **Citas clave**
  > “La mitad del día se va en moverse mal.”  
  > “Quiero empezar donde más duele.”

---

### **JTBD #2**

> **Cuando** mi teléfono es de baja gama y la memoria se llena,  
> **quiero** un modo ‘lite’ que comprima, guarde y permita subir luego,  
> **para poder** capturar evidencia sin que la app se caiga ni perder información.

- **Luchas / Puntos de dolor**
  - Cierres forzados, pérdida de fotos y notas.  
  - Retrabajo y visitas repetidas por falta de evidencia.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Cámara integrada, compresión automática y subida diferida.  
  - **Emocionales:** Tranquilidad de que nada se pierda.  
  - **Sociales:** Reportes consistentes que respalden mis recomendaciones.

- **Citas clave**
  > “Sin evidencia, me toca volver y quedo mal.”  
  > “Prefiero subir luego, pero no perder nada.”

---

### **JTBD #3**

> **Cuando** hago demos o capacitaciones con comunidades diversas,  
> **quiero** plantillas estándar con pictogramas y audio,  
> **para poder** enseñar sin barreras de lectura o jerga técnica y generar adopción real.

- **Luchas / Puntos de dolor**
  - Diferentes niveles de alfabetización y términos técnicos confusos.  
  - Saturación de texto en materiales tradicionales.

- **Fuerzas que impulsan el progreso**
  - **Funcionales:** Modo demo con casos locales y pasos visuales.  
  - **Emocionales:** Orgullo de que todos entiendan y puedan aplicar.  
  - **Sociales:** Dejar buena imagen y crear relaciones a largo plazo.

- **Citas clave**
  > “Si no lo entienden, no lo aplican.”  
  > “Con dibujos y voz, avanzamos más.”

---

## 3. FUNCIONALIDADES  

### **Arquetipo: Agrónomo/a asesor/a independiente**

---

**Basado en el JTBD #1:**  
> **Cuando** recibo múltiples alertas tras lluvias fuertes y hay baja iluminación y poca señal,  
> **quiero** priorizar rápidamente los lotes críticos con un umbral de acción claro por subregión,  
> **para poder** emitir recomendaciones confiables en 24–48 h y mantener mi reputación.

* **Funcionalidades Propuestas:**

  * **1. Priorización por Umbrales y Severidad (offline)**
    * **User Story:** Como agrónomo, quiero ver un ranking de lotes por severidad/urgencia para poder decidir dónde ir primero incluso sin señal.
    * **Criterio de Aceptación:** Dado que no tengo conectividad, cuando abro la vista de “Prioridad”, entonces veo los lotes ordenados por un score calculado localmente (síntomas, clima reciente, historial).
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Impacta directamente el JTBD (decidir rápido), elimina dolor crítico (tiempo/orden), esencial para el MVP en campo.

  * **2. Captura Guiada con Mejora de Imagen (baja luz)**
    * **User Story:** Como agrónomo, quiero una guía de encuadre y mejora de imagen para poder obtener evidencia útil en condiciones de baja iluminación.
    * **Criterio de Aceptación:** Dado que activo la cámara, cuando enfoco una hoja, entonces la app muestra guías de distancia/ángulo y aplica mejora sin conexión.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Aumenta precisión del diagnóstico y del score; sin buena evidencia, la priorización falla.

  * **3. Mapa Offline y Ruta Óptima por Riesgo**
    * **User Story:** Como agrónomo, quiero una ruta sugerida que minimice traslados y ataque primero los lotes de mayor riesgo.
    * **Criterio de Aceptación:** Dado un conjunto de lotes priorizados, cuando solicito ruta, entonces obtengo un orden recomendado usable sin datos.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Alto valor operativo; no bloquea el MVP si existe la lista priorizada.

  * **4. Reglas de Umbral por Subregión/Cultivo**
    * **User Story:** Como agrónomo, quiero configurar umbrales por subregión y cultivo para adaptar el score a realidades locales.
    * **Criterio de Aceptación:** Dado el panel de configuración, cuando ajusto un umbral, entonces el ranking se recalcula de inmediato.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Aporta precisión y confianza; el MVP puede iniciar con umbrales por defecto.

  * **5. Cola de Sincronización Diferida**
    * **User Story:** Como agrónomo, quiero que evidencias y decisiones se guarden y sincronicen al volver la señal para no perder información.
    * **Criterio de Aceptación:** Dado que estoy offline, cuando registro datos, entonces quedan en cola y se suben automáticamente al recuperar conectividad.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Conveniencia y robustez; el MVP puede operar localmente y exportar manualmente.

---

**Basado en el JTBD #2:**  
> **Cuando** la evidencia de campo es ambigua (pústulas incipientes, daño por granizo parecido a patógeno),  
> **quiero** asistencia en captura/mejora de imagen y pruebas rápidas sugeridas,  
> **para poder** reducir la incertidumbre y evitar gastos innecesarios al productor.

* **Funcionalidades Propuestas:**

  * **1. Asistente de Captura + Checklist de Confirmación**
    * **User Story:** Como agrónomo, quiero un checklist guiado por síntoma para confirmar o descartar hipótesis en minutos.
    * **Criterio de Aceptación:** Dado un síntoma seleccionado, cuando completo el checklist, entonces la app muestra probables causas y próximos pasos.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Resuelve el núcleo del JTBD (reducir ambigüedad); esencial en v1.

  * **2. Comparador Visual de Síntomas (galería offline)**
    * **User Story:** Como agrónomo, quiero comparar mis fotos con una galería curada para identificar diferencias clave.
    * **Criterio de Aceptación:** Dado una foto tomada, cuando abro el comparador, entonces veo imágenes de referencia con anotaciones.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Aumenta certeza y velocidad; el MVP puede vivir con el checklist si hay límite de tiempo.

  * **3. Sugeridor de Pruebas Rápidas de Campo**
    * **User Story:** Como agrónomo, quiero recibir sugerencias de micro-pruebas en campo (p.ej., observación adicional, revisión en horas de luz) para confirmar hallazgos.
    * **Criterio de Aceptación:** Dado un caso ambiguo, cuando solicito validación, entonces obtengo 1–3 pruebas simples con tiempos y criterios de éxito/fallo.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Reduce tratamientos innecesarios; alto valor económico para el productor.

  * **4. Umbrales de Escalamiento a Laboratorio**
    * **User Story:** Como agrónomo, quiero reglas claras de cuándo escalar a laboratorio para evitar sobre/infra-tratamiento.
    * **Criterio de Aceptación:** Dado un score de incertidumbre alto, cuando se cumplan condiciones, entonces la app recomienda enviar muestra y documenta motivo.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Estandariza decisiones críticas; no bloquea la v1 si existe el checklist.

  * **5. Registro de Decisión y Riesgo**
    * **User Story:** Como agrónomo, quiero guardar la decisión tomada con el nivel de riesgo para poder revisar casos y aprender.
    * **Criterio de Aceptación:** Dado el cierre de caso, cuando confirmo la decisión, entonces se registra la opción, evidencia y nivel de riesgo.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Útil para mejora continua; puede esperar a v1.1.

---

**Basado en el JTBD #3:**  
> **Cuando** debo entregar evidencia a clientes o cooperativas,  
> **quiero** generar reportes georreferenciados listos para WhatsApp,  
> **para poder** cerrar casos con trazabilidad sin perder horas en escritorio.

* **Funcionalidades Propuestas:**

  * **1. Reporte Georreferenciado Offline (PDF/imagen)**
    * **User Story:** Como agrónomo, quiero generar un reporte con fotos, mapa y fecha para enviarlo por WhatsApp.
    * **Criterio de Aceptación:** Dado un caso con evidencia, cuando toco “Generar reporte”, entonces obtengo un PDF/imagen comprimido listo para compartir.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Es la salida tangible del trabajo y cierra el ciclo; indispensable para el JTBD.

  * **2. Plantillas de Informe + Marca de Cooperativa/Cliente**
    * **User Story:** Como agrónomo, quiero elegir plantillas (cliente/cooperativa) para cumplir requisitos formales.
    * **Criterio de Aceptación:** Dado que selecciono una plantilla, cuando genero el informe, entonces se aplican logos, campos obligatorios y formato requerido.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Facilita auditorías y consistencia; el MVP puede usar una plantilla genérica.

  * **3. Firma Digital en Campo**
    * **User Story:** Como agrónomo, quiero capturar firmas del productor/testigo en el mismo reporte.
    * **Criterio de Aceptación:** Dado el reporte abierto, cuando solicito firma, entonces se añade la firma con fecha y GPS.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Aumenta trazabilidad y evita reprocesos; no bloquea el envío básico.

  * **4. Control de Versiones y Bitácora**
    * **User Story:** Como agrónomo, quiero mantener historial de versiones del reporte para responder observaciones.
    * **Criterio de Aceptación:** Dado un reporte editado, cuando guardo cambios, entonces se crea una nueva versión con dif y sello de tiempo.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Valor en auditorías; puede llegar en una versión posterior.

  * **5. Exportación a CSV para Seguimiento**
    * **User Story:** Como agrónomo, quiero exportar datos clave a CSV para análisis posterior.
    * **Criterio de Aceptación:** Dado la lista de casos, cuando elijo “Exportar CSV”, entonces descargo un archivo con campos estándar.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Útil para analítica, pero no esencial para cerrar casos en v1.

---

### **Arquetipo: Administrador/Mayordomo**

---

**Basado en el JTBD #1:**  
> **Cuando** hay alerta fitosanitaria y el clima cierra la ventana de aspersión,  
> **quiero** un semáforo por lote con tareas, mezcla y EPP,  
> **para poder** reubicar cuadrillas y cumplir metas sin reprocesos.

* **Funcionalidades Propuestas:**

  * **1. Tablero “Semáforo por Lote” (offline)**
    * **User Story:** Como mayordomo, quiero ver cada lote en rojo/amarillo/verde con mezcla y EPP sugeridos para poder priorizar de inmediato.
    * **Criterio de Aceptación:** Dado que estoy sin señal, cuando abro el tablero, entonces veo el estado por lote con fecha/hora y la recomendación mínima accionable (mezcla, EPP).
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Núcleo del JTBD; sin esto no hay priorización operativa. Impacto directo y esencial en el MVP.

  * **2. Planificador de Cuadrillas y Recursos**
    * **User Story:** Como mayordomo, quiero asignar cuadrillas, equipos y horarios por lote para ejecutar el plan sin confusiones.
    * **Criterio de Aceptación:** Dado el semáforo, cuando asigno cuadrilla y equipo, entonces se generan tareas con responsable y hora objetivo.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Lleva la priorización a ejecución. Elimina reprocesos y pérdida de tiempo; clave para que el MVP produzca resultados reales.

  * **3. Ventanas Climáticas y Alertas de Reprogramación**
    * **User Story:** Como mayordomo, quiero recibir alertas de cambio de clima para reprogramar tareas críticas a tiempo.
    * **Criterio de Aceptación:** Dado un lote con aspersión programada, cuando la ventana climática se invalide, entonces recibo alerta y propuesta de nuevo horario.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Alto valor operativo; el MVP puede iniciar sin predicción avanzada si hay reprogramación manual.

  * **4. Ruta Operativa por Prioridad**
    * **User Story:** Como mayordomo, quiero una secuencia sugerida de atención de lotes para reducir traslados y tiempos muertos.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Optimiza ejecución; no bloquea el lanzamiento si existe tablero + asignación.

  * **5. Integración Ligera de Inventario (EPP/insumos)**
    * **User Story:** Como mayordomo, quiero ver si tengo EPP e insumos mínimos antes de asignar cuadrilla.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Conveniencia y prevención de bloqueos; añade complejidad de datos, no crítica para validar el MVP.

  * **6. Integración con ERP/Bodega**
    * **User Story:** Como mayordomo, quiero sincronizar consumos con el ERP.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Alto costo de integración, no esencial para validar el valor central de la primera versión.

---

**Basado en el JTBD #2:**  
> **Cuando** viene auditoría o cierre de mes,  
> **quiero** generar evidencia ‘antes/después’ en un PDF georreferenciado,  
> **para poder** responder hallazgos sin cazar papeles.

* **Funcionalidades Propuestas:**

  * **1. Generador de Reporte Auditoría (PDF/imagen) con Georreferencia**
    * **User Story:** Como mayordomo, quiero crear un reporte con fotos antes/después, fecha/hora y coordenadas para auditoría.
    * **Criterio de Aceptación:** Dado un conjunto de evidencias, cuando genero el reporte, entonces obtengo un PDF comprimido con metadatos (GPS, sello temporal).
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Salida tangible del trabajo y requisito clave de auditoría; indispensable para el MVP.

  * **2. Plantillas de Cumplimiento (cliente/cooperativa)**
    * **User Story:** Como mayordomo, quiero aplicar plantillas estandarizadas con campos obligatorios para cumplir exigencias formales.
    * **Criterio de Aceptación:** Dado que selecciono una plantilla, cuando exporto, entonces el PDF incluye logos, campos requeridos y numeración.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Garantiza consistencia y reduc e retrabajo; crítica para pasar auditoría desde el día uno.

  * **3. Firma Digital en Campo (Supervisor/Operario)**
    * **User Story:** Como mayordomo, quiero capturar firmas en el reporte para cerrar evidencias en sitio.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Aumenta trazabilidad y evita impresiones; valioso, pero el reporte básico es suficiente para el MVP.

  * **4. Repositorio y Control de Versiones**
    * **User Story:** Como mayordomo, quiero almacenar y versionar reportes para responder observaciones.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Facilita gestión documental; el MVP puede iniciar con guardado local/exportación simple.

  * **5. Código QR/Folio Único por Reporte**
    * **User Story:** Como mayordomo, quiero un QR/folio para rastrear rápidamente el reporte en campo.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Mejora experiencia de auditoría; no esencial en v1.

  * **6. Exportación Masiva y Envío Programado**
    * **User Story:** Como mayordomo, quiero exportar varios reportes y programar su envío.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Útil para escalas grandes; puede esperar tras validar uso del reporte individual.

---

**Basado en el JTBD #3:**  
> **Cuando** ingreso personal o vehículos de proveedores,  
> **quiero** una lista de bioseguridad con registro fotográfico,  
> **para poder** autorizar o negar entrada con respaldo.

* **Funcionalidades Propuestas:**

  * **1. Checklist de Bioseguridad con Evidencia Fotográfica**
    * **User Story:** Como mayordomo, quiero un checklist simple con fotos para validar requisitos de ingreso.
    * **Criterio de Aceptación:** Dado un visitante, cuando completo el checklist, entonces la app registra estado (cumple/no cumple), fotos y sello temporal.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Cubre el núcleo del JTBD (decidir con respaldo); fundamental para el MVP.

  * **2. Registro de Proveedores/Vehículos (placa, empresa, responsable)**
    * **User Story:** Como mayordomo, quiero registrar datos básicos de proveedor y vehículo para trazabilidad.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Mejora la auditoría y seguridad; el MVP puede operar con checklist + foto aun sin base maestra.

  * **3. Semáforo de Acceso (Aprobado/Pendiente/Denegado) y Motivos**
    * **User Story:** Como mayordomo, quiero ver un estado claro de acceso con razones documentadas.
    * **Criterio de Aceptación:** Dado un control efectuado, cuando finalizo, entonces se asigna estado y se guarda el motivo.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Estándar operativo y claridad para portería; eleva profesionalismo.

  * **4. Bitácora de Eventos y Exportación CSV**
    * **User Story:** Como mayordomo, quiero revisar un historial de ingresos y exportarlo cuando lo soliciten.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Útil en investigaciones/auditorías; no bloquea el uso diario.

  * **5. Pases con QR e Integración con Cámaras/Torniquetes**
    * **User Story:** Como mayordomo, quiero emitir pases QR y vincular cámaras para automatizar el control.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Requiere hardware e integraciones; posponer hasta validar el flujo manual con checklist.

## **Resultados: Backlog de Funcionalidades Priorizadas**

### **Arquetipo: Productor mediano (papa / maíz / aguacate Hass)**

---

**Basado en el JTBD #1:**  
> **Cuando** veo síntomas dudosos después de una granizada o lluvias,  
> **quiero** diferenciar daño mecánico de enfermedad con una guía práctica,  
> **para poder** evitar aplicaciones innecesarias y cuidar el flujo de caja.

* **Funcionalidades Propuestas:**

  * **1. Guía de Diferenciación Rápida (daño mecánico vs. enfermedad)**
    * **User Story:** Como productor, quiero una guía paso a paso que me muestre señales clave para distinguir daño por clima de patógeno, para decidir con confianza.
    * **Criterio de Aceptación:** Dado que selecciono “granizada/lluvia”, cuando sigo 3–5 preguntas y subo 1 foto, entonces recibo un veredicto tentativo (mecánico/probable enfermedad) con señales observables.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Ataca el dolor principal (gasto inútil). Esencial para el valor del MVP en campo.

  * **2. Asesor “Aplicar o Esperar” (con umbral y clima cercano)**
    * **User Story:** Como productor, quiero una recomendación simple “aplicar/esperar” con umbral de riesgo y ventana climática para no desperdiciar insumo.
    * **Criterio de Aceptación:** Dado el diagnóstico tentativo, cuando consulto la recomendación, entonces obtengo acción sugerida, ventana de tiempo y breve razonamiento.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Conecta el diagnóstico con la decisión que ahorra dinero. Núcleo del JTBD.

  * **3. Comparador Visual Offline con Anotaciones**
    * **User Story:** Como productor, quiero comparar mi foto con ejemplos de referencia anotados para ver diferencias críticas.
    * **Criterio de Aceptación:** Dado una foto, cuando abro el comparador, entonces veo 3–5 imágenes de referencia con anotaciones y checklist corto.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Aumenta certeza y reduce errores; el MVP puede vivir con guía + asesor si hay límite.

  * **4. Simulador de Costo–Beneficio (aplicar vs. esperar)**
    * **User Story:** Como productor, quiero estimar el costo de aplicar ahora vs. esperar X días para decidir financieramente.
    * **Criterio de Aceptación:** Dado precio del insumo y área, cuando simulo, entonces veo costo estimado y riesgo asociado.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Potencia la decisión económica, pero no es indispensable en v1.

  * **5. Escalamiento a Laboratorio / Toma de Muestra**
    * **User Story:** Como productor, quiero instrucciones para toma de muestra y envío a laboratorio cuando la incertidumbre sea alta.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Requiere red externa e integración; posponer hasta validar flujo básico.

---

**Basado en el JTBD #2:**  
> **Cuando** dudo si cosechar Hass con antracnosis leve,  
> **quiero** una recomendación de cosecha selectiva y manejo poscosecha,  
> **para poder** reducir pérdidas y rechazos en empaque.

* **Funcionalidades Propuestas:**

  * **1. Asesor de Cosecha Selectiva (severidad de antracnosis)**
    * **User Story:** Como productor de Hass, quiero clasificar frutos por severidad para decidir cuáles cosechar ya y cuáles dejar.
    * **Criterio de Aceptación:** Dado un muestreo de frutos, cuando clasifico con la guía visual, entonces obtengo recomendación por categoría (cosechar/esperar/descartar).
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Resuelve directamente el JTBD y evita rechazos en planta.

  * **2. Guía Pos-cosecha Adaptativa (lavado, fungicida, curado, temperatura)**
    * **User Story:** Como productor, quiero pasos poscosecha según severidad y recursos disponibles para minimizar daños.
    * **Criterio de Aceptación:** Dado el nivel de severidad, cuando selecciono “poscosecha”, entonces recibo protocolo breve con tiempos/condiciones.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Complementa la decisión de corte con acción concreta; muy valiosa, posterior al asesor de cosecha.

  * **3. Semáforo de Rechazo en Empaque (apto / riesgo / no apto)**
    * **User Story:** Como productor, quiero un semáforo que me anticipe probabilidad de rechazo según defectos.
    * **Criterio de Aceptación:** Dado el muestreo, cuando genero el semáforo, entonces veo el porcentaje por categoría con recomendación.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Facilita decisiones rápidas antes de enviar a planta.

  * **4. Especificaciones de Comprador (calibres, tolerancias)**
    * **User Story:** Como productor, quiero ver requisitos del comprador (cuando estén disponibles) para alinear corte y selección.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Alto valor, pero requiere mantener catálogos/variantes; posponer a v1.1.

  * **5. Integración con Báscula / Etiquetado QR en Empaque**
    * **User Story:** Como productor, quiero vincular peso y etiquetas para trazabilidad en planta.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Demanda hardware e integración; no crítico para validar el proceso de decisión.

---

**Basado en el JTBD #3:**  
> **Cuando** evalúo prácticas (con/sin cobertura, fertilización fraccionada),  
> **quiero** comparar ‘antes/después’ por lote con un score simple,  
> **para poder** quedarme con lo que realmente funciona y descartar lo que no.

* **Funcionalidades Propuestas:**

  * **1. Ensayos A/B por Lote (plantilla rápida)**
    * **User Story:** Como productor, quiero crear ensayos sencillos A/B por lote para medir el efecto real de una práctica.
    * **Criterio de Aceptación:** Dado un lote, cuando defino A/B y registro 3–5 datos, entonces obtengo una comparación básica con conclusión sugerida.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Núcleo del JTBD: evidenciar qué funciona de forma simple.

  * **2. Score Simple de Práctica + Panel “Lo que Funciona”**
    * **User Story:** Como productor, quiero un score (↑/→/↓) por práctica y un panel que resuma lo que conviene mantener o descartar.
    * **Criterio de Aceptación:** Dado varios ensayos, cuando abro el panel, entonces veo el ranking y una recomendación por práctica.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Traduce resultados en decisiones accionables; esencial para el MVP.

  * **3. Galería Antes/Después y Línea de Tiempo**
    * **User Story:** Como productor, quiero ver fotos antes/después y la evolución en el tiempo para comunicar resultados.
    * **Criterio de Aceptación:** Dado un ensayo, cuando abro la galería, entonces visualizo pares de fotos y fechas clave.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Refuerza adopción y aprendizaje; puede llegar tras el score inicial.

  * **4. Exportación y Compartir con Técnico (PDF/imagen)**
    * **User Story:** Como productor, quiero exportar resultados y enviarlos por WhatsApp al técnico.
    * **Criterio de Aceptación:** Dado un ensayo, cuando toco “Exportar”, entonces genero PDF/imagen comprimida lista para compartir.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Útil para soporte y validación externa; no bloquea el MVP.

  * **5. Integración con Sensores IoT / Imágenes NDVI**
    * **User Story:** Como productor, quiero combinar mis ensayos con datos de sensores o NDVI para mayor precisión.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Alto esfuerzo y dependencias; posponer hasta validar uso del módulo A/B.


### **Arquetipo: Técnico agrícola (cooperativa / insumos)**

---

**Basado en el JTBD #1:**  
> **Cuando** tengo una ruta con muchas visitas y la señal es irregular,  
> **quiero** priorizar casos en un mapa offline con riesgo y distancia,  
> **para poder** maximizar el impacto de la jornada y cumplir metas sin devoluciones innecesarias.

* **Funcionalidades Propuestas:**

  * **1. Mapa Offline + Score de Riesgo por Caso**
    * **User Story:** Como técnico, quiero visualizar los casos en un mapa sin conexión con un score de riesgo para decidir a dónde ir primero.
    * **Criterio de Aceptación:** Dado que no tengo señal, cuando abro el mapa, entonces veo pines de casos con color/score (alto/medio/bajo) calculado localmente (síntomas, tiempo en cola, historial).
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Es el núcleo del JTBD (priorizar sin señal); sin esto no hay planificación efectiva en campo.

  * **2. Planificador de Ruta por Riesgo y Distancia (offline)**
    * **User Story:** Como técnico, quiero una secuencia sugerida que minimice traslados y atienda primero lo crítico.
    * **Criterio de Aceptación:** Dado un conjunto de casos, cuando solicito ruta, entonces obtengo un orden recomendado (heurística TSP) usable sin datos.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Optimiza la jornada y reduce tiempo muerto; no bloquea el MVP si existe la lista priorizada.

  * **3. Alta Rápida de Casos (1-min) con GPS y Fotos**
    * **User Story:** Como técnico, quiero registrar un caso en menos de 1 minuto con datos clave (cultivo, síntoma, 1–3 fotos, GPS) para no perder evidencia.
    * **Criterio de Aceptación:** Dado el formulario rápido, cuando guardo, entonces el caso queda disponible offline y aparece en el mapa con su score inicial.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Sin captura ágil no hay datos para priorizar ni cerrar visitas; esencial.

  * **4. Repriorización Dinámica por Tiempo y Compromisos**
    * **User Story:** Como técnico, quiero que los casos aumenten de prioridad si están cerca de vencer SLAs o si el productor reporta empeoramiento.
    * **Criterio de Aceptación:** Dado un SLA, cuando el tiempo restante baje del umbral, entonces el score sube y el caso asciende en el ranking.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Alinea metas comerciales/técnicas con la agenda; agrega valor sin ser bloqueante.

  * **5. Cola de Sincronización y Resolución de Conflictos**
    * **User Story:** Como técnico, quiero que mis cambios se sincronicen al recuperar señal y que la app me ayude a resolver conflictos (último cambio vs. servidor).
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Mejora robustez post-MVP; el flujo base puede operar con exportación manual si es necesario.

  * **6. Geofencing de Llegada/Salida (auto check-in)**
    * **User Story:** Como técnico, quiero que la app registre automáticamente llegada/salida a un predio.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Requiere calibración y puede drenar batería; posponer hasta validar uso con check-ins manuales.

---

**Basado en el JTBD #2:**  
> **Cuando** mi teléfono es de baja gama y la memoria se llena,  
> **quiero** un modo ‘lite’ que comprima, guarde y permita subir luego,  
> **para poder** capturar evidencia sin que la app se caiga ni perder información.

* **Funcionalidades Propuestas:**

  * **1. Cámara Modo Lite (compresión + guardado en segundo plano)**
    * **User Story:** Como técnico, quiero sacar fotos evidenciales en modo comprimido que no cierre la app ni consuma demasiada memoria.
    * **Criterio de Aceptación:** Dado que capturo 3 fotos seguidas, cuando vuelvo al caso, entonces las imágenes están guardadas (≤300 KB c/u) y la app sigue operativa.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Elimina el dolor central (crashes/pérdida de evidencia); imprescindible en dispositivos de gama baja.

  * **2. Gestor de Almacenamiento con Alertas y Limpieza Segura**
    * **User Story:** Como técnico, quiero ver cuánto espacio queda y poder limpiar caché de miniaturas sin perder evidencias.
    * **Criterio de Aceptación:** Dado espacio bajo, cuando ejecuto “Limpiar caché”, entonces se liberan MB y las fotos originales permanecen.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Previene caídas por almacenamiento; crítico para continuidad de uso.

  * **3. Cola de Subida con Reintentos/Resume y Modo Datos Bajos**
    * **User Story:** Como técnico, quiero que las evidencias se suban automáticamente cuando haya señal, con reintentos y límite de datos.
    * **Criterio de Aceptación:** Dado que recupero 3G, cuando se inicia la cola, entonces los archivos suben por prioridad y se reanudan si falla la conexión.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Asegura flujo sin intervención manual; agrega resiliencia post-MVP.

  * **4. Paquetes de Evidencia (foto+nota+coordenada)**
    * **User Story:** Como técnico, quiero agrupar varias fotos y notas en un “paquete” comprimido por caso para enviar/guardar de forma liviana.
    * **Criterio de Aceptación:** Dado un caso, cuando genero paquete, entonces obtengo un archivo ≤2 MB con metadatos básicos.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Facilita compartir/transferir en conectividad limitada.

  * **5. Modo Texto-Primero (degradación elegante)**
    * **User Story:** Como técnico, quiero poder registrar solo texto/checkbox y añadir fotos después para no detenerme por memoria.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Alternativa útil en casos extremos; no crítica si el Modo Lite funciona bien.

  * **6. Soporte SD/Disco Externo**
    * **User Story:** Como técnico, quiero guardar en SD/USB-OTG.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Fragmentación de dispositivos/permiso; posponer hasta validar adopción del Modo Lite.

---

**Basado en el JTBD #3:**  
> **Cuando** hago demos o capacitaciones con comunidades diversas,  
> **quiero** plantillas estándar con pictogramas y audio,  
> **para poder** enseñar sin barreras de lectura o jerga técnica y generar adopción real.

* **Funcionalidades Propuestas:**

  * **1. Motor de Plantillas con Pictogramas y Audio (offline)**
    * **User Story:** Como técnico, quiero reproducir pasos con iconografía y audio para explicar procedimientos sin depender de lectura.
    * **Criterio de Aceptación:** Dado que selecciono una plantilla, cuando inicio “Demo”, entonces la app muestra pantallas con pictogramas y reproduce indicaciones de voz sin conexión.
    * **Prioridad MoSCoW:** **Must-have**
    * **Justificación:** Ataca directamente la barrera de alfabetización/jerga; esencial para lograr adopción en campo.

  * **2. Modo Presentador (botones grandes + avance paso a paso)**
    * **User Story:** Como técnico, quiero un modo con controles grandes y avance secuencial para dictar la capacitación desde el teléfono.
    * **Criterio de Aceptación:** Dado el modo presentador, cuando toco “Siguiente”, entonces el paso avanza y se registra el tiempo por paso.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Mejora la dinámica de formación; el MVP puede operar con el motor de plantillas básico.

  * **3. Perfiles Comunitarios (idioma, nivel de detalle)**
    * **User Story:** Como técnico, quiero configurar idioma y nivel (básico/avanzado) para adaptar la explicación a cada comunidad.
    * **Criterio de Aceptación:** Dado un perfil seleccionado, cuando inicio la plantilla, entonces los textos/audio y la cantidad de pasos se ajustan al perfil.
    * **Prioridad MoSCoW:** **Should-have**
    * **Justificación:** Eleva la relevancia cultural/lingüística; no bloqueante para la primera entrega.

  * **4. Paquetes de Contenido por Cultivo/Región (descarga)**
    * **User Story:** Como técnico, quiero descargar paquetes temáticos (café, plátano, papa, Hass) para tener demos listos sin internet.
    * **Criterio de Aceptación:** Dado conectividad puntual, cuando descargo un paquete, entonces queda disponible offline con imágenes/audio.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Aporta amplitud de uso; puede llegar tras validar el motor de plantillas.

  * **5. Registro de Sesiones y Feedback Rápido**
    * **User Story:** Como técnico, quiero registrar cuántas personas asistieron y su feedback (pulgar arriba/abajo) por plantilla.
    * **Prioridad MoSCoW:** **Could-have**
    * **Justificación:** Útil para medir adopción/impacto, pero no esencial para enseñar.

  * **6. Proyección a Pantalla (Chromecast/Miracast)**
    * **User Story:** Como técnico, quiero proyectar la demo a una TV o proyector.
    * **Prioridad MoSCoW:** **Won’t-have (por ahora)**
    * **Justificación:** Requiere hardware adicional; posponer hasta validar el uso móvil 1:1/pequeños grupos.


*****

## **2. FLUJO DE APLICACIÓN (DESCRIPCIÓN TEXTUAL)**
*Aquí se describe, pantalla por pantalla, el flujo lógico de la aplicación, las acciones clave y las conexiones entre ellas. Este es el esqueleto de la experiencia del usuario.*

**Flujo Principal: Diagnóstico por Imagen**

* **P1: Dashboard / Tablero:**
    * **Propósito:** Pantalla de inicio. Muestra un resumen del estado de los cultivos y alertas.
    * **Acciones Principales:**
        * Tocar **"Nuevo Análisis"** lleva a **P2**.

* **P2: Cámara de Análisis:**
    * **Propósito:** Interfaz de cámara para capturar una imagen del cultivo afectado.
    * **Acciones Principales:**
        * Tocar **"Capturar"** lleva a **P3**.

* **P3: Confirmación de Imagen:**
    * **Propósito:** Muestra la foto recién tomada para que el usuario la confirme.
    * **Acciones Principales:**
        * Tocar **"Analizar"** lleva a **P4**.
        * Tocar **"Tomar Otra"** regresa a **P2**.

* **P4: Pre-análisis & Estado:**
    * **Propósito:** Pantalla de carga o procesamiento. Muestra al usuario que la IA está trabajando.
    * **Flujo:**
        * Al completarse con éxito (**"OK / Resultado listo"**), lleva a **P5**.
        * Si no hay conexión (**"Sin red"**), la tarea se pone en cola y regresa a **P1**, mostrando una notificación.

* **P5: Resultados del Diagnóstico:**
    * **Propósito:** Muestra el resultado detallado del análisis de la IA. Es una pantalla rica en información.
    * **Acciones Principales:**
        * Tocar **"Ver Recomendaciones"** lleva a **P6**.
        * Tocar **"Comparar"** lleva a **P8**.
        * Tocar **"Escalar a Laboratorio"** lleva a **P9**.
        * Tocar **"Volver al Tablero"** regresa a **P1**.

* **P6: Recomendaciones & EPP:**
    * **Propósito:** Detalla las acciones sugeridas y el equipo de protección personal (EPP) necesario.
    * **Acciones Principales:**
        * Tocar **"Crear Plan de Trabajo"** lleva a **P7**.

* **P7: Plan de Trabajo:**
    * **Propósito:** Permite al usuario organizar las recomendaciones en tareas asignables.
    * **Acciones Principales:**
        * Tocar **"Asignar y Generar"** lleva a **P10**.

* **P8: Comparador Antes/Después:**
    * **Propósito:** Herramienta para comparar la imagen actual con una anterior del mismo cultivo.
    * **Acciones Principales:**
        * Tocar **"Volver a Resultados"** regresa a **P5**.

* **P9: Derivar a Laboratorio:**
    * **Propósito:** Formulario para escalar el caso a un análisis de laboratorio humano.
    * **Acciones Principales:**
        * Tocar **"Crear Solicitud"** lleva a **P10**.

* **P10: Confirmación & Evidencia:**
    * **Propósito:** Pantalla que confirma que la acción (Plan de Trabajo o Solicitud de Laboratorio) se ha creado con éxito.
    * **Acciones Principales:**
        * Tocar **"Ver en Historial"** lleva a **H1**.

* **H1: Historial de Casos:**
    * **Propósito:** Un registro de todos los análisis y acciones pasadas.
    * **Acciones Principales:**
        * Tocar un caso podría llevar a **P5** (para ver detalles).
        * Un botón para **"Volver al Tablero"** regresa a **P1**.

-----

**INSTRUCCIONES Y TAREAS (EJECÚTALAS EN ORDEN):**

**Paso 1: Síntesis Integral y Definición de Estilo Visual**
Analiza todos los documentos de contexto y, fundamentalmente, el **Flujo de Aplicación Textual** para comprender la estructura y las transiciones. Luego, define un mini sistema de diseño (paleta de colores, tipografía, estilo de componentes) que sea apropiado para la industria agrícola: confiable, claro y moderno.

**Paso 2: Diseño de Pantallas basado en el Flujo**
Para cada punto del flujo textual (P1, P2, P3, etc.), diseña la pantalla correspondiente. Presta especial atención a las **"Acciones Principales"** descritas; estas deben traducirse en los botones y elementos interactivos más prominentes de cada pantalla. Asegúrate de que la transición entre pantallas se sienta lógica y fluida.

**Paso 3: Creación del Canvas del Prototipo Visual (Pantalla por Pantalla)**
Genera el diseño para cada pantalla principal. Para cada una, proporciona una descripción detallada que permita a otra IA generadora de imágenes (o a un diseñador) crearla visualmente. Usa el formato de salida especificado a continuación.

**FORMATO DE SALIDA (EL CANVAS DEL PROTOTIPO):**

Utiliza el siguiente formato Markdown para describir cada pantalla, asegurándote de que el diseño refleje el propósito y las acciones definidas en el flujo textual.

-----

# **Canvas: Prototipo Visual para [Nombre del Producto]**

## **P1: Dashboard / Tablero**
* **Propósito (del Flujo):** Pantalla de inicio. Muestra un resumen del estado de los cultivos y alertas.
* **Arquetipo Principal:** Mayordomo de Finca.
* **Descripción para GenAI:** "Interfaz de app móvil limpia y moderna para agricultura. Header con 'Bienvenido, [Nombre]'. Sección principal con tarjetas horizontales para 'Cultivos Monitoreados', cada una con nombre, foto y un indicador de salud visual (anillo verde/amarillo/rojo). Una sección de 'Alertas Recientes' en la parte superior. El elemento más prominente es un **botón de acción flotante (FAB) azul en la esquina inferior derecha con el texto 'Nuevo Análisis'** y un ícono de cámara, que inicia el flujo principal."

## **P2: Cámara de Análisis**
* **Propósito (del Flujo):** Interfaz de cámara para capturar una imagen del cultivo afectado.
* **Arquetipo Principal:** Todos.
* **Descripción para GenAI:** "La interfaz de la cámara nativa del móvil. Superpuesto, hay un marco guía translúcido y texto de ayuda como 'Enfoque la hoja o fruto afectado'. En la parte inferior, un gran botón de obturador circular para **'Capturar'** la imagen. Un icono de galería permite subir una foto existente."

*(...y así sucesivamente para cada una de las pantallas P3, P4, P5, etc., hasta H1, siempre asegurando que la descripción visual incorpore los elementos de acción que conectan el flujo.)*

```