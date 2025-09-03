# Construcción de Journey Maps As-Is

## Contexto

Con el siguiente prompt para **Journey Maps As-Is**, la visualización completa del proceso que **ACTUALMENTE** sigue un usuario desde que identifica un problema en el cultivo hasta que evalúa los resultados **SIN nuestro sistema de IA** en el sector agricola colombiano, especificamente para los departamentos de Antioquia, Valle del Cauca y Cundinamarca. Para ello, el prompt tomará como base de conocimiento el resultado generado en [1_arquetipo_resultdado.md](1_arquetipo_resultado.md), [2_systemmaps-as-is_general.md](2_systemmaps-as-is_general.md) para:

- ✅ **Contexto progresivo:** Cada fase construye sobre la base anterior, en este caso arquetipos y system maps as-is.
- ✅ **Journeys más precisos:** Ya conoces todo el ecosistema cuando mapeas comportamientos
- ✅ **Insights más profundos:** Los journey maps pueden referenciar específicamente actores y recursos del system map
- ✅ **Validación cruzada:** Puedes verificar que los journeys son consistentes con el ecosistema mapeado

### 🗺️ Fases del Journey Maps AS-IS

#### FASE 1: DETECCIÓN DEL PROBLEMA
Cómo actualmente identifica problemas en el cultivo

#### FASE 2: INVESTIGACIÓN Y DIAGNÓSTICO INICIAL
Cómo actualmente intenta diagnosticar el problema

#### FASE 3: BÚSQUEDA DE SEGUNDA OPINIÓN
Cómo valida su diagnóstico inicial

#### FASE 4: TOMA DE DECISIÓN
Cómo decide qué tratamiento aplicar

#### FASE 5: ADQUISICIÓN DE TRATAMIENTO
Cómo obtiene los productos/servicios necesarios

#### FASE 6: APLICACIÓN DEL TRATAMIENTO
Cómo implementa la solución

#### FASE 7: MONITOREO DE RESULTADOS
Cómo evalúa si el tratamiento está funcionando

#### FASE 8: EVALUACIÓN FINAL Y APRENDIZAJE
Cómo determina si fue exitoso y qué aprendió

## Herramientas

Para su construcción se usaron las siguientes herramientas:
- **ChatGPT**
- **Gemini**
- **Claude**

## Prompts

```markdown
# UX AgroTech Research - Journey Maps As-Is

Actúa como un investigador UX senior especializado en agricultura. Tu tarea es investigar y mapear cómo los usuarios ACTUALMENTE diagnostican y manejan problemas en sus cultivos, SIN nuestro sistema de IA.

## CONTEXTO DE LA INVESTIGACIÓN
- Objetivo: Entender el proceso actual de diagnóstico de cultivos
- Enfoque: AS-IS (estado actual, sin tecnología de IA)
- Región objetivo: [ESPECIFICAR REGIÓN]
- Arquetipos base: Toma como referencia los arquetipos seleccionados en las FASES 3 y 4 de la base de conocimiento que te he suministrado, especificamente en el archivo `1_arquetipos_resultados.md`
- System Map AS-IS: Toma como referencia el systema maps que te he suministrado en la base de tu conocimiento, especificamente en el archivo `2_systemmaps-as-is_resultado.md`
- Consulta información de páginas como https://mintic.gov.co/portal/inicio/Sala-de-prensa/Noticias/276923:Con-AgroTECH-el-MinTIC-potenciara-el-campo-con-Inteligencia-Artificial, https://agroexpo.com/es para ayudar a determinar el estado actual del agro en Colombia.

## FASE 1: INVESTIGACIÓN DE JOURNEYS ACTUALES

Basándote en el System Map AS-IS y los arquetipos desarrollados, investiga cómo los usuarios actualmente manejan situaciones de diagnóstico de cultivos:

### Journeys por Método Actual de Diagnóstico:
- **Diagnóstico visual propio**: Usuario inspecciona y decide basado en experiencia
- **Consulta con expertos**: Agrónomo, extensionista, colega experimentado
- **Búsqueda en recursos**: Internet, libros, manuales, grupos de WhatsApp
- **Toma de muestras**: Lleva muestra a laboratorio o centro de diagnóstico
- **Prueba y error**: Aplica tratamientos basados en intuición/experiencia previa
- **Consulta múltiple**: Combina varias fuentes antes de decidir
- **Monitoreo y espera**: Observa evolución sin intervenir inmediatamente

### Journeys por Urgencia/Contexto:
- **Emergencia crítica**: Problema que requiere acción inmediata
- **Monitoreo rutinario**: Revisión preventiva programada
- **Validación de sospecha**: Confirmar hipótesis propia
- **Segunda opinión**: Ya tiene diagnóstico pero busca confirmación
- **Capacitación activa**: Aprovecha problema para aprender

### Journeys por Recursos Disponibles:
- **Con limitaciones económicas**: Opciones gratuitas/baratas solamente
- **Con acceso a expertos**: Puede pagar consultoría
- **Con red de apoyo**: Tiene comunidad de productores
- **Aislado geográficamente**: Acceso limitado a expertos presenciales
- **Con experiencia limitada**: Usuario novato que necesita mucha guía

## FASE 2: PRIORIZACIÓN DE JOURNEYS AS-IS

Evalúa cada journey actual usando estos criterios:

**Criterios de Evaluación:**
1. **Frecuencia actual** (1-10): Qué tan común es este journey
2. **Nivel de frustración** (1-10): Qué tan problemático es el proceso actual
3. **Impacto en resultados** (1-10): Qué tan crítico es para el éxito del cultivo
4. **Oportunidad de mejora** (1-10): Qué tanto podría mejorar nuestro sistema este proceso
5. **Representatividad** (1-10): Qué tan típico es entre nuestros arquetipos

Selecciona los **3-4 journeys AS-IS más críticos** que representan las mayores oportunidades de mejora.

## FASE 3: MAPEO DETALLADO DE JOURNEYS AS-IS

Para cada journey actual seleccionado, mapea el proceso existente:

---

# JOURNEY AS-IS [NÚMERO]: [NOMBRE DEL JOURNEY ACTUAL]

**📋 INFORMACIÓN GENERAL**
- **Arquetipo principal:** [De los desarrollados previamente]
- **Situación que dispara el journey:** [Qué problema/necesidad inicia el proceso]
- **Método actual principal:** [Cómo resuelve actualmente]
- **Frecuencia típica:** [Qué tan seguido ocurre este proceso]
- **Duración total actual:** [Tiempo desde detección hasta resolución]
- **Recursos/herramientas actuales:** [Qué usa para diagnosticar]

---

## 🗺️ PROCESO ACTUAL (AS-IS)

### FASE 1: DETECCIÓN DEL PROBLEMA
**Cómo actualmente identifica problemas en el cultivo**

**🎬 SITUACIÓN ACTUAL:**
- **Ubicación:** [Donde típicamente nota el problema]
- **Momento:** [Cuándo en su rutina lo detecta]
- **Método de detección:** [Visual, táctil, por síntomas generales]

**👤 COMPORTAMIENTO ACTUAL:**
- **Acciones:** [Qué hace específicamente para examinar]
- **Pensamientos:** [Primera hipótesis, preocupaciones]
- **Emociones:** [Cómo se siente al detectar el problema]
- **Herramientas:** [Qué instrumentos usa para examinar mejor]

**⏱️ TIEMPO INVERTIDO:** [Duración de esta fase]

**😤 FRUSTRACIONES ACTUALES:**
- [Problemas específicos con el método actual de detección]
- [Limitaciones de su capacidad de diagnóstico]
- [Incertidumbre sobre gravedad del problema]

**💸 COSTOS ACTUALES:**
- [Tiempo, recursos, dinero que invierte]

---

### FASE 2: INVESTIGACIÓN Y DIAGNÓSTICO INICIAL
**Cómo actualmente intenta diagnosticar el problema**

**🎬 SITUACIÓN ACTUAL:**
- **Recursos consultados:** [A dónde va para buscar información]
- **Personas contactadas:** [Expertos, colegas, familiares]
- **Herramientas usadas:** [Internet, libros, apps existentes]

**👤 COMPORTAMIENTO ACTUAL:**
- **Acciones:** [Proceso específico de investigación]
- **Pensamientos:** [Cómo evalúa diferentes fuentes]
- **Emociones:** [Frustración, confianza, confusión]
- **Criterios de decisión:** [Cómo decide en qué información confiar]

**⏱️ TIEMPO INVERTIDO:** [Duración típica de investigación]

**🔧 TOUCHPOINTS ACTUALES:**
- [WhatsApp con colegas, Google, técnicos locales, etc.]

**😤 FRUSTRACIONES ACTUALES:**
- [Información contradictoria, falta de especificidad local]
- [Dificultad para contactar expertos]
- [Costo de consultas profesionales]

**💸 COSTOS ACTUALES:**
- [Tiempo de investigación, consultas pagadas]

---

### FASE 3: BÚSQUEDA DE SEGUNDA OPINIÓN
**Cómo valida su diagnóstico inicial**

**🎬 SITUACIÓN ACTUAL:**
- **Fuentes de validación:** [A quién recurre para confirmar]
- **Métodos de comunicación:** [Llamadas, visitas, fotos por WhatsApp]

**👤 COMPORTAMIENTO ACTUAL:**
- **Acciones:** [Cómo presenta el problema a otros]
- **Pensamientos:** [Nivel de confianza en su diagnóstico]
- **Emociones:** [Ansiedad por confirmación]

**⏱️ TIEMPO INVERTIDO:** [Tiempo para obtener segunda opinión]

**😤 FRUSTRACIONES ACTUALES:**
- [Disponibilidad limitada de expertos]
- [Costo de visitas técnicas]
- [Tiempo perdido esperando confirmación]

**💸 COSTOS ACTUALES:**
- [Honorarios de agrónomos, tiempo de espera]

---

### FASE 4: TOMA DE DECISIÓN
**Cómo decide qué tratamiento aplicar**

**🎬 SITUACIÓN ACTUAL:**
- **Proceso de decisión:** [Cómo evalúa opciones de tratamiento]
- **Factores considerados:** [Costo, disponibilidad, experiencia previa]

**👤 COMPORTAMIENTO ACTUAL:**
- **Acciones:** [Investigación de tratamientos, evaluación de opciones]
- **Pensamientos:** [Análisis costo-beneficio, riesgos]
- **Emociones:** [Presión por decidir, incertidumbre]

**⏱️ TIEMPO INVERTIDO:** [Tiempo de análisis y decisión]

**😤 FRUSTRACIONES ACTUALES:**
- [Opciones limitadas por presupuesto]
- [Incertidumbre sobre efectividad]
- [Presión temporal para actuar]

**💸 COSTOS ACTUALES:**
- [Tiempo de análisis, posibles consultorías adicionales]

---

### FASE 5: ADQUISICIÓN DE TRATAMIENTO
**Cómo obtiene los productos/servicios necesarios**

**🎬 SITUACIÓN ACTUAL:**
- **Proveedores:** [Dónde compra insumos, servicios]
- **Proceso de compra:** [Cómo adquiere lo necesario]

**👤 COMPORTAMIENTO ACTUAL:**
- **Acciones:** [Visita a distribuidores, negociación, transporte]
- **Pensamientos:** [Sobre disponibilidad, precios, calidad]
- **Emociones:** [Prisa por resolver, preocupación por costos]

**⏱️ TIEMPO INVERTIDO:** [Tiempo para adquirir insumos]

**😤 FRUSTRACIONES ACTUALES:**
- [Disponibilidad limitada de productos]
- [Precios elevados]
- [Calidad inconsistente]

**💸 COSTOS ACTUALES:**
- [Costo de productos, transporte, tiempo]

---

### FASE 6: APLICACIÓN DEL TRATAMIENTO
**Cómo implementa la solución**

**🎬 SITUACIÓN ACTUAL:**
- **Método de aplicación:** [Manual, con equipos, contratado]
- **Seguimiento de protocolo:** [Qué tan estrictamente sigue instrucciones]

**👤 COMPORTAMIENTO ACTUAL:**
- **Acciones:** [Preparación, aplicación, limpieza]
- **Pensamientos:** [Sobre técnica correcta, efectividad]
- **Emociones:** [Esperanza, ansiedad por resultados]

**⏱️ TIEMPO INVERTIDO:** [Tiempo total de aplicación]

**😤 FRUSTRACIONES ACTUALES:**
- [Dificultad técnica de aplicación]
- [Condiciones climáticas adversas]
- [Falta de equipo adecuado]

**💸 COSTOS ACTUALES:**
- [Tiempo de aplicación, posible mano de obra adicional]

---

### FASE 7: MONITOREO DE RESULTADOS
**Cómo evalúa si el tratamiento está funcionando**

**🎬 SITUACIÓN ACTUAL:**
- **Frecuencia de revisión:** [Cada cuánto monitorea progreso]
- **Método de evaluación:** [Visual, comparación con fotos, mediciones]

**👤 COMPORTAMIENTO ACTUAL:**
- **Acciones:** [Inspecciones regulares, documentación]
- **Pensamientos:** [Sobre progreso, necesidad de ajustes]
- **Emociones:** [Esperanza, impaciencia, preocupación]

**⏱️ TIEMPO INVERTIDO:** [Tiempo de monitoreo continuo]

**😤 FRUSTRACIONES ACTUALES:**
- [Dificultad para evaluar progreso]
- [Resultados lentos o ambiguos]
- [No saber cuándo esperar cambios]

**💸 COSTOS ACTUALES:**
- [Tiempo de monitoreo, posibles tratamientos adicionales]

---

### FASE 8: EVALUACIÓN FINAL Y APRENDIZAJE
**Cómo determina si fue exitoso y qué aprendió**

**🎬 SITUACIÓN ACTUAL:**
- **Criterios de éxito:** [Cómo define si funcionó]
- **Documentación:** [Cómo registra lo aprendido]

**👤 COMPORTAMIENTO ACTUAL:**
- **Acciones:** [Evaluación final, documentación mental/física]
- **Pensamientos:** [Sobre efectividad, costo-beneficio]
- **Emociones:** [Satisfacción, decepción, aprendizaje]

**⏱️ TIEMPO INVERTIDO:** [Tiempo total del proceso completo]

**😤 FRUSTRACIONES ACTUALES:**
- [Dificultad para medir ROI real]
- [Falta de documentación sistemática]
- [Pérdida de conocimiento para situaciones futuras]

**💸 COSTOS TOTALES:**
- [Suma de todos los costos del proceso]

---

## 📊 ANÁLISIS DEL JOURNEY AS-IS

**⏱️ TIEMPOS TOTALES:**
- Desde detección hasta inicio de tratamiento: [X días/horas]
- Proceso completo hasta evaluación: [X días/semanas]

**💰 COSTOS TOTALES:**
- Monetarios: [Suma de todos los gastos]
- Tiempo: [Horas invertidas total]
- Oportunidad: [Pérdidas por demora]

**😤 PAIN POINTS CRÍTICOS:**
1. [Mayor frustración del proceso actual]
2. [Segunda mayor frustración]
3. [Tercera mayor frustración]

**⚡ MOMENTOS DE MAYOR FRICCIÓN:**
1. [Punto donde más usuarios se atascan/abandonan]
2. [Segundo punto crítico]
3. [Tercer punto crítico]

**🎯 OPORTUNIDADES DE MEJORA:**
1. [Mayor oportunidad para nuestro sistema de IA]
2. [Segunda oportunidad]
3. [Tercera oportunidad]

**📈 VARIACIONES POR CONTEXTO:**
- **Por experiencia:** [Cómo cambia el proceso para novatos vs expertos]
- **Por recursos:** [Diferencias según presupuesto disponible]
- **Por urgencia:** [Cómo se acelera/modifica en emergencias]
- **Por temporada:** [Variaciones estacionales del proceso]

---

## FASE 4: ANÁLISIS PROFUNDO Y VALIDACIÓN

Ahora que has mapeado el journey AS-IS básico, profundiza con estos análisis adicionales:

### 4.1 EXPLORACIÓN DE VARIACIONES CONTEXTUALES

**Analiza cómo cambia significativamente este journey AS-IS en estos contextos:**

**4.1.1 Variación por Experiencia del Usuario:**
- **Primera vez enfrentando este problema:** 
  - ¿Cómo cambia el proceso de investigación?
  - ¿Qué recursos adicionales consulta?
  - ¿Cuánto más tiempo invierte?
  - ¿Qué errores adicionales comete?

- **Usuario experimentado con historial del problema:**
  - ¿Qué pasos omite del proceso estándar?
  - ¿Cómo usa su experiencia previa?
  - ¿En qué casos su experiencia lo perjudica?
  - ¿Cuándo decide saltarse su protocolo habitual?

**4.1.2 Variación por Época del Año:**
- **Época de siembra vs época de cosecha:**
  - ¿Cómo cambia la urgencia del proceso?
  - ¿Qué recursos están disponibles/ocupados?
  - ¿Cómo afecta esto la toma de decisiones?
  - ¿Qué tratamientos son viables en cada época?

**4.1.3 Variación por Conectividad:**
- **Conectividad excelente vs limitada:**
  - ¿Qué recursos digitales puede/no puede usar?
  - ¿Cómo cambian sus fuentes de información?
  - ¿Qué alternativas desarrolla para información?
  - ¿Cómo afecta esto sus tiempos de respuesta?

**4.1.4 Variación por Contexto Social:**
- **Usuario individual vs equipo de trabajo:**
  - ¿Cómo cambia el proceso de consulta?
  - ¿Quién toma las decisiones finales?
  - ¿Cómo se validan las opiniones múltiples?
  - ¿Qué conflictos surgen en el proceso?

**4.1.5 Variación por Nivel de Crisis:**
- **Situación rutinaria vs emergencia crítica:**
  - ¿Qué pasos se aceleran o eliminan?
  - ¿Cómo cambia la tolerancia al riesgo?
  - ¿Qué recursos adicionales se movilizan?
  - ¿Cuándo acepta soluciones subóptimas por velocidad?

### 4.2 IDENTIFICACIÓN DE MOMENTOS CRÍTICOS

**Analiza específicamente estos aspectos del journey AS-IS:**

**4.2.1 Puntos de Abandono:**
- **Identifica los 3 momentos donde es más probable que el usuario abandone el proceso:**
  1. [Momento específico + razón + % estimado de abandono]
  2. [Momento específico + razón + % estimado de abandono]
  3. [Momento específico + razón + % estimado de abandono]

- **Para cada punto de abandono, describe:**
  - ¿Qué consecuencias tiene abandonar en ese momento?
  - ¿Qué alternativas busca el usuario?
  - ¿Bajo qué condiciones retoma el proceso?

**4.2.2 Momentos de Máxima Lealtad:**
- **Identifica los 2 momentos donde una experiencia excelente crearía mayor lealtad:**
  1. [Momento específico + por qué genera lealtad + impacto esperado]
  2. [Momento específico + por qué genera lealtad + impacto esperado]

- **Para cada momento de lealtad, describe:**
  - ¿Qué expectativas específicas tiene el usuario?
  - ¿Qué haría que calificara la experiencia como "excelente"?
  - ¿Cómo se manifestaría esa lealtad en comportamientos futuros?

**4.2.3 Oportunidades de Diferenciación:**
- **Identifica las 3 oportunidades más grandes para diferenciarse de la competencia:**
  1. [Oportunidad + competencia actual + diferenciación posible]
  2. [Oportunidad + competencia actual + diferenciación posible]
  3. [Oportunidad + competencia actual + diferenciación posible]

**4.2.4 Puntos de Integración Valiosos:**
- **Identifica momentos donde integraciones con otros sistemas agregarían más valor:**
  - Con proveedores de insumos: [Momento + valor agregado]
  - Con sistemas de gestión agrícola: [Momento + valor agregado]
  - Con servicios financieros: [Momento + valor agregado]
  - Con redes sociales/profesionales: [Momento + valor agregado]

### 4.3 ANÁLISIS PROFUNDO DE PAIN POINTS

**Para cada pain point crítico identificado, profundiza:**

**4.3.1 Anatomía del Pain Point:**
- **Pain Point #1:** [Nombre del problema principal]
  - **Momento exacto:** [Cuándo en el journey ocurre]
  - **Manifestación:** [Cómo se expresa la frustración]
  - **Frecuencia:** [Qué tan seguido ocurre]
  - **Intensidad:** [Nivel de frustración del 1-10]
  - **Causas raíz:** [Por qué ocurre realmente]
  - **Intentos de solución actuales:** [Cómo trata de resolverlo]
  - **Costo real:** [Tiempo, dinero, oportunidad perdida]

**4.3.2 Errores Comunes:**
- **Identifica los 3 errores más comunes que comete en el proceso actual:**
  1. [Error + por qué ocurre + consecuencias]
  2. [Error + por qué ocurre + consecuencias]
  3. [Error + por qué ocurre + consecuencias]

**4.3.3 Información Faltante Crítica:**
- **Qué información le falta más crítica para tomar mejores decisiones:**
  - En el momento de detección: [Información específica necesaria]
  - Durante investigación: [Información específica necesaria]
  - Al decidir tratamiento: [Información específica necesaria]
  - Durante implementación: [Información específica necesaria]

**4.3.4 Momentos de Soledad/Desamparo:**
- **Identifica cuándo se siente más solo/sin soporte en el proceso:**
  - Situación específica: [Descripción del momento]
  - Por qué se siente desaparado: [Causas]
  - Qué tipo de soporte buscaría: [Soporte ideal]
  - Cómo afecta sus decisiones: [Impacto en el proceso]

### 4.4 VALIDACIÓN DEL JOURNEY AS-IS

**Valida la precisión y completitud del journey mapeado:**

**4.4.1 Validación de Realismo Regional:**
- **¿Qué tan realista es este proceso para [región específica]?**
  - Aspectos que suenan auténticos: [Lista]
  - Aspectos que podrían no ser precisos: [Lista + correcciones]
  - Variaciones regionales importantes: [Diferencias por zona]

**4.4.2 Validación por Tipo de Cultivo:**
- **¿Qué variaciones tendría según el tipo de cultivo?**
  - Cultivos de ciclo corto vs largo: [Diferencias principales]
  - Cultivos de alto vs bajo valor: [Diferencias en recursos disponibles]
  - Cultivos tradicionales vs tecnificados: [Diferencias en procesos]

**4.4.3 Validación Temporal:**
- **¿Cómo cambiaría este proceso en diferentes épocas del año?**
  - Estación seca vs lluviosa: [Variaciones específicas]
  - Época de siembra: [Modificaciones al proceso]
  - Época de cosecha: [Modificaciones al proceso]
  - Periodos de alta demanda técnica: [Cómo se adapta]

**4.4.4 Validación Socioeconómica:**
- **¿Qué aspectos culturales o socioeconómicos podrían estar faltando?**
  - Factores culturales: [Creencias, tradiciones que influyen]
  - Dinámicas familiares: [Quién decide qué en la familia]
  - Aspectos generacionales: [Diferencias por edad]
  - Factores de género: [Si hay diferencias de género relevantes]

### 4.5 CUANTIFICACIÓN DEL IMPACTO ACTUAL

**Estima específicamente los costos del proceso AS-IS:**

**4.5.1 Cuantificación Temporal:**
- **Tiempo promedio perdido por demoras en diagnóstico:** [X horas/días]
  - Tiempo directo invertido: [Horas de trabajo]
  - Tiempo de espera: [Horas/días perdidos]
  - Tiempo de oportunidad: [Qué no puede hacer mientras tanto]

**4.5.2 Cuantificación Monetaria:**
- **Costo monetario típico del proceso actual completo:** [$X USD total]
  - Costos directos: [Consultas, análisis, transporte]
  - Costos de insumos: [Productos para tratamiento]
  - Costos de oportunidad: [Ingresos perdidos por demora]
  - Costos de error: [Pérdidas por diagnósticos incorrectos]

**4.5.3 Tasa de Éxito/Fracaso:**
- **% de veces que el usuario NO logra resolver el problema satisfactoriamente:** [X%]
  - Casos donde abandona el proceso: [X%]
  - Casos donde el tratamiento no funciona: [X%]
  - Casos donde el problema se agrava durante el proceso: [X%]

**4.5.4 Impacto Económico de Errores:**
- **Impacto económico de diagnósticos incorrectos o tardíos:** [$X USD promedio]
  - Pérdida de cosecha: [% de producción perdida]
  - Costos de tratamientos innecesarios: [Dinero gastado en vano]
  - Daño a largo plazo: [Impacto en futuras cosechas]

### 4.6 BENCHMARKING CON ALTERNATIVAS

**Compara este journey AS-IS con métodos alternativos disponibles:**

**4.6.1 Comparación con Otros Métodos:**
- **Método tradicional vs consulta digital vs laboratorio:**
  - Tiempo requerido: [Comparación]
  - Costo total: [Comparación]
  - Precisión esperada: [Comparación]
  - Accesibilidad: [Comparación]

**4.6.2 Identificación de Best Practices:**
- **¿Qué hacen los usuarios más exitosos diferente?**
  - Estrategias únicas que usan: [Mejores prácticas]
  - Recursos que aprovechan mejor: [Optimizaciones]
  - Errores que evitan: [Lecciones aprendidas]
```