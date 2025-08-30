# FASE 1 · Investigación de roles agrícolas (Colombia)

> Notas de contexto: En 2023, los principales cultivos por **extensión** fueron café (14,5%), arroz (11,5%), frutales (10,7%), palma de aceite (10,3%), maíz (9,2%) y plátano (8,4%). Esto orienta dónde la IA por imagen tendría más valor.&#x20;
> En municipios rurales PDET, el **acceso a Internet** alcanzó 44,6% (38,3% en centros poblados y rural disperso, con predominio de conexiones **móviles** 77,7%), por lo que el producto debe funcionar **offline/low-bandwidth** y apoyarse en WhatsApp. ([DANE][1])
> Colombia tiene alta **adopción móvil** (92,5 M de líneas; \~174% de penetración), lo que respalda un enfoque “mobile-first”. ([Mintic][2])

A continuación, los roles/usuarios con atributos clave:

1. **Pequeño agricultor familiar** (tambos, minifundio; “campesino”)

* **Responsabilidades:** manejo diario del lote, monitoreo visual, control básico de plagas.
* **Decisión:** operativo (alto), táctico (medio).
* **Interacción con cultivos:** diaria.
* **Tecnología:** Android gama media; WhatsApp; datos móviles intermitentes.
* **Urgencia:** crítica en brotes/picos climáticos.
* **Influencia de compra:** usuario final; influenciado por técnico, agroinsumo, asociación.

2. **Productor mediano (arroz/papa/maíz/hortalizas)**

* **Responsabilidades:** planificación de siembras, monitoreo fitosanitario y nutricional, coordinación de cuadrillas.
* **Decisión:** táctico/operativo; algunas inversiones estratégicas.
* **Frecuencia:** diaria en campaña, semanal en post-cosecha.
* **Tecnología:** smartphone + Excel/Drive; a veces dron/NDVI tercerizado.
* **Urgencia:** crítica en ventanas de control (ej. añublo/ Pyricularia en arroz). ([Fedearroz][3])
* **Influencia:** decisor de compra en software asequible.

3. **Gran productor/empresa agroindustrial** (palma, banano, caña, flores)

* **Responsabilidades:** SOPs, KPIs, cumplimiento (RSPO/GlobalG.A.P.), control de plagas reguladas (TR4, HLB).
* **Decisión:** estratégico/táctico.
* **Frecuencia:** diaria (equipos de campo).
* **Tecnología:** smartphones corporativos, tablets, conectividad mejor resuelta in-house.
* **Urgencia:** crítica por riesgo fitosanitario y contratos. ([FAOLEX][4], [Comunidad Andina][5])
* **Influencia:** alto (decisor/prescriptor).

4. **Agrónomo asesor independiente/consultor** (café, frutales, arroz, hortalizas)

* **Responsabilidades:** diagnóstico, recomendación, capacitación y reporte.
* **Decisión:** táctico con influencia estratégica en clientes.
* **Frecuencia:** diaria (visitas múltiples).
* **Tecnología:** smartphone; Drive; WhatsApp Business; a veces kit de campo.
* **Urgencia:** crítica — “detectar temprano” = ahorro en control.
* **Influencia:** muy alta (prescriptor multisitio).

5. **Técnico agrícola de campo** (cooperativas, asociaciones, insumos)

* **Responsabilidades:** monitoreo, captura de evidencia, implementación de planes.
* **Decisión:** operativo; ejecuta y retroalimenta.
* **Frecuencia:** diaria.
* **Tecnología:** Android; formularios; fotos; WhatsApp.
* **Urgencia:** crítica en brotes; moderada en seguimiento.
* **Influencia:** media-alta (recomienda herramientas a productores).

6. **Administrador/Mayordomo de finca** (café, banano, palma, frutales)

* **Responsabilidades:** coordinar cuadrillas, aplicar recomendaciones, registrar incidencias.
* **Decisión:** operativo/táctico.
* **Frecuencia:** diaria.
* **Tecnología:** smartphone; radio/WhatsApp; a veces tablet.
* **Urgencia:** crítica (turnos/aspersión/lluvia).
* **Influencia:** influenciador clave hacia dueño/gerencia.

7. **Ingeniero agrónomo de empresa**

* **Responsabilidades:** diseño de programa fitosanitario, análisis de datos, cumplimiento y trazabilidad.
* **Decisión:** estratégico/táctico.
* **Frecuencia:** diaria/semanal.
* **Tecnología:** laptop + móvil; BI básico; GIS.
* **Urgencia:** crítica en alertas; moderada en reporting.
* **Influencia:** alto (decide piloto/compra).

8. **Extensionista rural (UMATA/ATDR, ONG, sector público)**

* **Responsabilidades:** asistencia técnica a pequeños y medianos; transferencia.
* **Decisión:** táctico (en recomendación); operativo (demostraciones).
* **Frecuencia:** diaria/semanal.
* **Tecnología:** móvil; conectividad variable; WhatsApp comunitario.
* **Urgencia:** moderada; crítica en emergencias fitosanitarias.
* **Influencia:** muy alta (escala y confianza local). ([Ministerio de Agricultura][6], [FAOLEX][7])

9. **Investigador (universidad/Agrosavia/Centros)**

* **Responsabilidades:** ensayos, validaciones, fenotipado/imagen, protocolos MIP.
* **Decisión:** estratégico en innovación; no siempre compra directa.
* **Frecuencia:** estacional/intensiva en campañas.
* **Tecnología:** cámaras, apps de captura, R/Excel; buen acceso a Internet.
* **Urgencia:** flexible.
* **Influencia:** media (evidencia y aval técnico).

10. **Estudiante de agronomía**

* **Responsabilidades:** prácticas de campo, monitoreo guiado.
* **Decisión:** bajo (usuario).
* **Frecuencia:** semanal/estacional.
* **Tecnología:** smartphone; redes; aprendizaje activo.
* **Urgencia:** baja.
* **Influencia:** futura (adopción generacional).

> Riesgos fitosanitarios prioritarios que justifican la app: **Fusarium R4T** en musáceas (desde 2019; 20 lugares con presencia a 2024), **HLB** en cítricos; ambos son prioridad sanitaria por Ley 2303 de 2023. **Añublo (Pyricularia)** en arroz es la enfermedad más limitante. ([Comunidad Andina][5], [FAOLEX][4], [Fedearroz][3])

---

# FASE 2 · Priorización y selección

## Matriz (1–10)

| Rol                                         | Adopción | Frecuencia de uso | Impacto | Capacidad de pago | Influencia | **Total** |
| ------------------------------------------- | -------: | ----------------: | ------: | ----------------: | ---------: | --------: |
| Agrónomo asesor independiente               |    **9** |                 9 |       9 |                 7 |     **10** |    **44** |
| Administrador/Mayordomo (café/banano/palma) |        8 |            **10** |   **9** |                 7 |          8 |    **42** |
| Productor mediano (arroz/papa/maíz)         |        8 |                 9 |       8 |                 6 |          7 |    **38** |
| Técnico agrícola (coops/insumos)            |        8 |                 9 |       8 |                 6 |          8 |    **39** |
| Ingeniero agrónomo de empresa               |        7 |                 8 |       9 |             **8** |          8 |        40 |
| Extensionista rural (UMATA/ONG)             |        7 |                 7 |       8 |                 5 |     **10** |        37 |
| Pequeño agricultor familiar                 |        6 |                 8 |       7 |                 4 |          6 |        31 |
| Investigador                                |        6 |                 6 |       7 |                 7 |          6 |        32 |
| Estudiante de agronomía                     |        7 |                 5 |       5 |                 3 |          5 |        25 |
| Gran productor (corporativo)                |        7 |                 8 |   **9** |             **9** |          8 |        41 |

**Selección de 4 arquetipos más prometedores**

1. **Agrónomo asesor independiente** — Máxima **influencia** y uso transversal (multiplica adopción).
2. **Administrador/Mayordomo** — **Uso diario** y alto impacto operativo en cultivos perennes críticos (café/banano/palma).
3. **Productor mediano (arroz/papa/maíz)** — Alta **frecuencia** y sensibilidad a decisiones de ventana (ej. fungicidas).
4. **Técnico agrícola (cooperativa/insumos)** — Cubre **muchas fincas**, necesita evidencia visual y reportes rápidos (WhatsApp).

---

# FASE 3 · Desarrollo detallado de arquetipos

## ARQUETIPO 1: Agrónomo asesor independiente

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

---

## Implicaciones de diseño para el producto

* **Mobile-first, offline-first y “WhatsApp-ready”** (exportar diagnóstico+foto+plan en 1 toque). Conectividad rural sigue siendo el cuello de botella; en PDET predominan accesos móviles. ([DANE][1])
* **Guías de captura asistida** (encuadre, iluminación, escala) para mejorar precisión del modelo.
* **Clasificación por cultivos prioritarios de Colombia** (café, arroz, banano/plátano, palma, maíz) con **rutas rápidas** para enfermedades clave (Roya, Sigatoka/TR4, HLB, Pyricularia). ([Instituto Geográfico Agustín Codazzi][8], [FAOLEX][4], [Fedearroz][3])
* **Semáforo de severidad + umbrales de acción** y **checklists por lote**.
* **Modo auditoría** (antes/después + geolocalización + metadatos) para empresas y certificaciones.
* **Métricas**: tiempo a primer diagnóstico, reducción de aplicaciones innecesarias, % casos con recomendación implementada, severidad promedio, ahorro estimado/ha.
* **Precios**: planes por rol (asesor/técnico multi-finca vs. productor individual), con bundle de SMS/WhatsApp si aplica.

---

### Fuentes citadas (selección)

* MinAgricultura, *Memorias al Congreso 2023–2024* (cultivos por extensión; contexto HLB).&#x20;
* DANE, *Encuesta Nacional Agropecuaria / PDET* (acceso a Internet rural; predominio móvil). ([DANE][1])
* MinTIC, *Boletín sector TIC 2025-Q1* (líneas móviles y penetración). ([Mintic][2])
* **Ley 2303 de 2023** (prioridad sanitaria: TR4, HLB, palma). ([FAOLEX][4])
* ICA / CAN (TR4 presente desde 2019; situación 2024). ([Comunidad Andina][5])
* Fedearroz (Pyricularia/añublo: enfermedad limitante en arroz). ([Fedearroz][3])

---
# Fase 4 - Información adicional para cada arquetipo seleccionado

A continuación se complementa **cada arquetipo seleccionado** con: 
-  **5 escenarios adicionales** (incluyen emergencias, estacionalidad y edge cases propios de Antioquia). 
-  **validación de realismo** (qué ajustar para Antioquia)  
-  **motivaciones** (qué les preocupa y qué historia de éxito los convence).

---

## 1) Agrónomo/a asesor/a independiente (Eje cafetero, Oriente, Urabá)

### 5 escenarios adicionales

1. **“Roya tras invierno súbito en Suroeste” (emergencia/estacional)**

   * *Situación:* 5–7 días de lluvia continua en Andes/Jardín; hojas con pústulas incipientes.
   * *Uso IA:* Clasifica severidad por imagen y genera umbral de acción por lote.
   * *Decisión:* Priorizar lotes >“amarillo” en 48 h.

2. **“Granizada en Oriente (Rionegro/La Ceja) sobre aguacate Hass” (emergencia/edge)**

   * *Situación:* Frutos con necrosis por golpe vs. antracnosis.
   * *Uso IA:* Diferencia daño mecánico de lesión patológica; sugiere descarte/curativo.
   * *Decisión:* Definir % de cosecha salvable y tratamientos post-evento.

3. **“Sospecha de TR4 en plátano de Urabá” (emergencia)**

   * *Situación:* Marchitez localizada, vetas en pecíolo; finca cerca de corredor bananero.
   * *Uso IA:* Check de señales visuales + protocolo de bioseguridad y derivación inmediata.
   * *Decisión:* Aislar zona, activar ruta con técnico e ICA; registro georreferenciado.

4. **“Sombrío denso en café (café-plátano)” (edge Antioquia)**

   * *Situación:* Fotos con baja iluminación y sombras duras.
   * *Uso IA:* Asistente de captura (flash/ángulo/escala); mejora imagen y repite análisis offline.
   * *Decisión:* Validar diagnóstico sin conectividad.

5. **“Confusión nutricional en ladera” (estacional/edge topográfico)**

   * *Situación:* Clorosis por lavado de N/Mg vs. enfermedad foliar.
   * *Uso IA:* Probabilidad + “pruebas de campo” (tirilla suelo/agua) sugeridas.
   * *Decisión:* Corregir fertilización o aplicar fungicida (evitar gasto innecesario).

### Validación de realismo (Antioquia)

1. **Potencialmente no realista:** dependencia de drones propios; en Antioquia suelen tercerizar.
2. **Faltan detalles:** *dialecto y canales* (notas de voz por WhatsApp, “vos”), alianzas con cooperativas cafeteras, tiempos de viaje por vías terciarias.
3. **Ajustes:** reforzar **modo offline**, plantillas “listas para WhatsApp”, y rutas por subregión (Suroeste, Oriente, Urabá) con packs de enfermedades locales.

### Motivaciones

* **Qué lo desvela:** fallar en detectar un brote temprano y perder la confianza del cliente.
* **Mayor preocupación con IA:** falsos negativos/positivos que lleven a recomendar mal; dependencia de Internet.
* **Historia de éxito que convence:** “En Jardín, la app detectó roya temprana; el plan oportuno redujo severidad 30% y ahorró una aplicación por ciclo, con informe listo para WhatsApp.”

---

## 2) Administrador/Mayordomo (café Suroeste, plátano/banano Urabá)

### 5 escenarios adicionales

1. **“Alerta de Sigatoka en Urabá” (emergencia/estacional)**

   * *Situación:* Incremento de mancha; ventana corta por pronóstico de lluvia.
   * *Uso IA:* Semáforo por lote + checklist de aspersión y EPP.
   * *Decisión:* Reubicar cuadrillas y planificar mezcla del día.

2. **“Bioseguridad en portería” (edge operativo)**

   * *Situación:* Ingreso de proveedor tras visitar otra finca.
   * *Uso IA:* Lista guiada con fotos (pisos/botas/rodachines) y registro de cumplimiento.
   * *Decisión:* Autorizar o no ingreso; activar lavado/desinfección.

3. **“Café en ladera tras aguacero” (emergencia topográfica)**

   * *Situación:* Deslizamientos menores; plantas con daño radicular/defoliación.
   * *Uso IA:* Clasifica daño visible y sugiere priorización de tutorado y drenajes.
   * *Decisión:* Orden de cuadrillas por severidad y accesibilidad.

4. **“Selección de racimos (banano) para exportación” (estacional)**

   * *Situación:* Duda entre daño mecánico vs. defecto fisiológico.
   * *Uso IA:* Etiqueta defectos por imagen y crea reporte “apto/no apto”.
   * *Decisión:* Reducir rechazos en planta de empaque.

5. **“Auditoría interna a fin de mes” (edge documental)**

   * *Situación:* Piden evidencia antes/después de controles.
   * *Uso IA:* Genera PDF georreferenciado con fotos, fechas y lotes.
   * *Decisión:* Entregar soporte sin buscar papeles.

### Validación de realismo (Antioquia)

1. **Potencialmente no realista:** hablar de palma de aceite como cultivo principal en Antioquia; aquí pesa más **plátano/banano** (Urabá) y **café**.
2. **Faltan detalles:** uso de **radio** en campo, cuadrillas mixtas por jornal, cambios de turno por clima, alfabetización digital variada.
3. **Ajustes:** reemplazar “palma” por **Hass** (Oriente) o **banano** (Urabá) según zona; reforzar flujos **sin señal** y con evidencia fotográfica simple.

### Motivaciones

* **Qué lo desvela:** que el jefe le pida resultados “para ya” y no tenga evidencia clara.
* **Mayor preocupación con IA:** que sea complicada para el personal y se pierda tiempo en la jornada.
* **Historia de éxito que convence:** “En Apartadó, con el semáforo de Sigatoka, bajamos rechazos 15% y cumplimos ventanas a tiempo; auditoría pasó sin hallazgos usando los PDFs de la app.”

---

## 3) Productor mediano (ajustado a Antioquia: **papa/maíz/aguacate Hass**)

### 5 escenarios adicionales

1. **“Tizón tardío vs. daño por granizo (papa, Altiplano Norte)” (emergencia/edge)**

   * *Situación:* Lesiones tras granizada en Santa Rosa/Sonsón.
   * *Uso IA:* Diferencia patrón foliar; sugiere curativo preventivo o esperar.
   * *Decisión:* Evitar aplicación inútil.

2. **“Cogollero en maíz (Urabá/Norte)” (emergencia/estacional)**

   * *Situación:* Daño en cogollo en V4–V6.
   * *Uso IA:* Estimación rápida de severidad por imagen; umbral de intervención.
   * *Decisión:* Aplicar o monitorear 48 h.

3. **“Clorosis por lavado de nutrientes” (estacional lluvias)**

   * *Situación:* Suelos en pendiente con lixiviación.
   * *Uso IA:* Señales de deficiencia vs. patógeno; sugiere análisis de suelo simple.
   * *Decisión:* Ajuste de fertilización fraccionada.

4. **“Antracnosis en Hass pre-cosecha (Oriente)” (estacional)**

   * *Situación:* Mancha en fruto; dudas de severidad y manejo poscosecha.
   * *Uso IA:* Clasifica y sugiere cosecha selectiva y tratamiento.
   * *Decisión:* Reducir pérdidas en empaque.

5. **“Comparación entre lotes con y sin cobertura” (edge práctico)**

   * *Situación:* Ensayo casero de manejo.
   * *Uso IA:* Galería comparativa (antes/después) y score de daño.
   * *Decisión:* Elegir práctica que realmente funciona.

### Validación de realismo (Antioquia)

1. **Potencialmente no realista:** enfocar en arroz (poco representativo en Antioquia).
2. **Faltan detalles:** compras en agroinsumos locales, pagos en efectivo, familia involucrada en labores, conectividad intermitente.
3. **Ajustes:** centrar cultivos en **papa/maíz/Hass**, añadir **modo ligero** (fotos comprimidas) y tutoriales visuales sin texto largo.

### Motivaciones

* **Qué lo desvela:** gastar en insumos sin certeza y que “no pegue” la aplicación por clima.
* **Mayor preocupación con IA:** costos/mes y que la app “no sirva sin datos”.
* **Historia de éxito que convence:** “En Sonsón, la app evitó 1 aplicación por confundir granizo con tizón; ahorré insumo y jornales y aún así mantuve rendimiento.”

---

## 4) Técnico agrícola (cooperativa/insumos) — Huila/Tolima/Antioquia, rutas en **Eje cafetero y Oriente**

### 5 escenarios adicionales

1. **“Ruta con 20 visitas en Oriente” (estacional pico lluvias)**

   * *Situación:* Múltiples consultas por enfermedades foliares.
   * *Uso IA:* Priorización automática por riesgo + mapa offline.
   * *Decisión:* Orden de visitas que maximiza impacto.

2. **“Capacitación en vereda con comunidad Embera en Urabá” (edge cultural)**

   * *Situación:* Barrera de idioma/alfabetización.
   * *Uso IA:* Modo **pictogramas** y audio en voz para explicar manejo.
   * *Decisión:* Aumentar comprensión sin texto técnico.

3. **“Teléfono de baja gama con memoria llena” (edge técnico)**

   * *Situación:* App se cierra al sacar fotos.
   * *Uso IA:* Modo *lite* (cámara integrada, compresión, guardado diferido).
   * *Decisión:* Cerrar caso y subir cuando haya Wi-Fi.

4. **“Evento demo en feria de La Ceja” (estacional comercial)**

   * *Situación:* Demostración a 30 productores.
   * *Uso IA:* Modo “demo” con casos locales etiquetados y reportes instantáneos.
   * *Decisión:* Generar leads y seguimiento por WhatsApp.

5. **“Diagnóstico nocturno en emergencia” (edge operativo)**

   * *Situación:* Llaman tarde por brote.
   * *Uso IA:* Guía de captura con linterna/ángulo + advertencia de fiabilidad.
   * *Decisión:* Dar primera recomendación y programar verificación diurna.

### Validación de realismo (Antioquia)

1. **Potencialmente no realista:** asumir cobertura 4G estable; muchas veredas tienen 2G/intermitente.
2. **Faltan detalles:** trabajo por metas mensuales, mezcla de rol técnico-comercial, presión de temporada y vías terciarias en mal estado.
3. **Ajustes:** dashboards de **casos cerrados/mes**, **plantillas estándar** por cultivo local y sincronización diferida.

### Motivaciones

* **Qué lo desvela:** perder credibilidad por recomendaciones inconsistentes entre visitas.
* **Mayor preocupación con IA:** que contradiga protocolos de la empresa o que el productor la malinterprete.
* **Historia de éxito que convence:** “Con la app estandarizamos captura y reporte; el índice de repetición de visitas bajó 20% y las quejas se redujeron a la mitad.”

---

### Notas transversales para producto (al hilo de estos hallazgos)

* **Antioquia-first:** bibliotecas de casos para **Suroeste cafetero**, **Urabá platanero/bananero** y **Oriente Hass/flores**.
* **Operar sin señal:** captura guiada, compresión automática, cola de sincronización y **PDF/WhatsApp en un toque**.
* **Confianza y control:** semáforo + umbrales + “pruebas de campo sugeridas” para reducir falso positivo/negativo.
* **Cultura local:** interfaz con **pictogramas** y soporte a **notas de voz**; lenguaje claro, opción “vos”.

---


[1]: https://www.dane.gov.co/files/operaciones/ECV/bol-PDET-ECV-2023.pdf?utm_source=chatgpt.com "Boletín PDET 2023"
[2]: https://www.mintic.gov.co/portal/715/w3-article-404518.html?utm_source=chatgpt.com "Colombia cerró el primer trimestre de 2025 con más de 49 ..."
[3]: https://fedearroz.com.co/es/servicios-al-arrocero/eventos-tecnicos-fedearroz-fna/manejo-integrado-de-pyricularia-oryzae-en-el-cultivo-del-arroz/manejo-integrado-de-pyricularia-oryzae-en-el-cultivo-del-arroz/?utm_source=chatgpt.com "Manejo Integrado de Pyricularia oryzae en el cultivo del arroz"
[4]: https://faolex.fao.org/docs/pdf/col221478.pdf?utm_source=chatgpt.com "LEY 2303 DE 2023"
[5]: https://www.comunidadandina.org/documents/temas/dg-com/sanidad-vegetal/vigilancia_focr4t_colombia_IV_trimestre_2024.pdf?utm_source=chatgpt.com "1 BOLETÍN EPIDEMIOLÓGICO RESULTADOS DE LA ..."
[6]: https://www.minagricultura.gov.co/normatividad/leyes/ley%20607%20de%202000.pdf?utm_source=chatgpt.com "LEY 607 DE 2000"
[7]: https://faolex.fao.org/docs/pdf/col35053.pdf?utm_source=chatgpt.com "LEY NÚMERO 607 DE 2000"
[8]: https://www.ica.gov.co/icacomunica/pyp/fusarium-r4t?utm_source=chatgpt.com "Marchitez por Fusarium Raza 4 Tropical – Foc R4T"
