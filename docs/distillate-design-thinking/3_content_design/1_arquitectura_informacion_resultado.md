### **Canvas: Arquitectura de Información para [Nombre del Producto]**

> Estructura pensada para operar en campo con baja conectividad, priorizar acciones en 1–3 toques y generar evidencia trazable. Las etiquetas están en lenguaje de usuario y alineadas a JTBD y arquetipos priorizados.

---

#### **1.0 Tablero (Semáforo por Lote)**
* **Descripción:** Vista inicial con tarjetas de cada lote en rojo/amarillo/verde, mostrando “acción mínima” (mezcla/EPP/observación), última actualización y filtros por prioridad/área/cultivo. Funciona 100% offline con sincronización diferida.  
* **Arquetipo Principal:** Mayordomo/Administrador.  
* **JTBD Asociado:** “Cuando hay alerta fitosanitaria y el clima cierra la ventana, quiero un semáforo por lote con tareas, mezcla y EPP, para reubicar cuadrillas y cumplir metas sin reprocesos.”
  * **1.1 Filtros y búsqueda rápida**  
    * **Descripción:** Filtro por prioridad, cultivo, zona; búsqueda por nombre de lote.  
    * **Arquetipo Principal:** Mayordomo  
    * **JTBD Asociado:** Priorizar sin perder tiempo por desorden.
  * **1.2 Ventanas climáticas y reprogramación**  
    * **Descripción:** Alertas cuando una aspersión programada pierde su ventana; propone nuevo horario.  
    * **Arquetipo Principal:** Mayordomo  
    * **JTBD Asociado:** Reorganizar tareas ante cambio de clima.
  * **1.3 Planificador de cuadrillas**  
    * **Descripción:** Asignar cuadrilla/equipo/hora por lote con validación de EPP mínimo y generación de orden de trabajo.  
    * **Arquetipo Principal:** Mayordomo  
    * **JTBD Asociado:** “Dígame qué lote va primero y con qué mezcla.”
  * **1.4 Integración ligera de inventario (EPP/insumos)**  
    * **Descripción:** Check rápido de disponibilidad de insumos/EPP para no asignar tareas bloqueadas.  
    * **Arquetipo Principal:** Mayordomo  
    * **JTBD Asociado:** Evitar reprocesos por falta de EPP.

---

#### **2.0 Diagnóstico (IA + Guía en Campo)**
* **Descripción:** Captura guiada (modo lite), guía de diferenciación, “Aplicar o Esperar” con umbral y ventana climática; comparador visual antes/después. Opera offline y sugiere escalar a laboratorio cuando aplica.  
* **Arquetipo Principal:** Productor mediano; Todos.  
* **JTBD Asociado:** “Cuando veo síntomas dudosos tras granizada, quiero diferenciar daño mecánico de enfermedad con una guía práctica, para evitar aplicaciones innecesarias.”
  * **2.1 Guía de diferenciación (granizo vs. enfermedad)**  
    * **Descripción:** 3–5 preguntas + 1 foto → veredicto tentativo (mecánico/probable enfermedad) con señales observables.  
    * **Arquetipo Principal:** Productor mediano  
    * **JTBD Asociado:** Evitar gastos inútiles y decidir con confianza.
  * **2.2 Asesor “Aplicar o Esperar”**  
    * **Descripción:** Recomendación simple con umbral de riesgo y ventana climática próxima.  
    * **Arquetipo Principal:** Productor mediano  
    * **JTBD Asociado:** “Aplicar lo justo y a tiempo.”
  * **2.3 Comparador visual (antes/después) offline**  
    * **Descripción:** Galería por lote para contrastar evolución y soportar decisión.  
    * **Arquetipo Principal:** Productor mediano, Agrónomo  
    * **JTBD Asociado:** Ensayo pequeño para reducir incertidumbre.
  * **2.4 Escalar a laboratorio**  
    * **Descripción:** Indicadores de cuándo conviene análisis de laboratorio (criterios y costos/tiempos típicos).  
    * **Arquetipo Principal:** Agrónomo/Productor  
    * **JTBD Asociado:** Elegir gasto de confirmación solo cuando agrega certeza.

---

#### **3.0 Ruta & Mapa (Offline)**
* **Descripción:** Mapa cacheado con pines por riesgo (alto/medio/bajo) y orden sugerido de visitas para minimizar traslados; reglas de prioridad por subregión/cultivo; cola de sincronización cuando regresa la señal.  
* **Arquetipo Principal:** Técnico agrícola (cooperativa/insumos)  
* **JTBD Asociado:** “Ruta con 20 visitas… priorización automática por riesgo + mapa offline.”
  * **3.1 Vista de prioridad**  
    * **Descripción:** Ranking por riesgo/tiempo en cola.  
    * **Arquetipo Principal:** Técnico  
    * **JTBD Asociado:** Atender primero lo crítico.
  * **3.2 Capas y navegación**  
    * **Descripción:** Capas por cultivo, clima y tareas; navegación por sectores aun sin GPS.  
    * **Arquetipo Principal:** Técnico/Mayordomo  
    * **JTBD Asociado:** Reducir tiempos muertos y recorridos.
  * **3.3 Reglas de umbral por zona/cultivo**  
    * **Descripción:** Personalización de límites que alimentan el semáforo y la ruta sugerida.  
    * **Arquetipo Principal:** Agrónomo/Mayordomo  
    * **JTBD Asociado:** Consistencia en decisiones.
  * **3.4 Sincronización diferida**  
    * **Descripción:** Cola de eventos para subir evidencias/reportes cuando haya señal.  
    * **Arquetipo Principal:** Todos  
    * **JTBD Asociado:** No perder datos en campo.

---

#### **4.0 Casos & Historial**
* **Descripción:** Repositorio histórico por lote/cultivo/diagnóstico con búsqueda y versiones; exportación básica a CSV cuando aplique.  
* **Arquetipo Principal:** Agrónomo  
* **JTBD Asociado:** Analizar tendencias y responder observaciones.
  * **4.1 Línea de tiempo por lote**  
    * **Descripción:** Eventos (detección, recomendación, aplicación, verificación) con fotos y sellos de tiempo.  
    * **Arquetipo Principal:** Agrónomo/Mayordomo  
    * **JTBD Asociado:** Trazabilidad de punta a punta.
  * **4.2 Reporte Auditoría (PDF georreferenciado)**  
    * **Descripción:** Generar PDF comprimido “antes/después” con metadatos (GPS, sello temporal) y firmas en sitio.  
    * **Arquetipo Principal:** Mayordomo  
    * **JTBD Asociado:** “Cuando viene auditoría, quiero evidencia antes/después en PDF georreferenciado…”
  * **4.3 Bitácora y exportación**  
    * **Descripción:** Listado de eventos con exportación ad-hoc a CSV (cuando esté habilitado).  
    * **Arquetipo Principal:** Mayordomo/Agrónomo  
    * **JTBD Asociado:** Responder requerimientos con datos consolidados.

---

#### **5.0 Operación de Campo (Ejecución Guiada)**
* **Descripción:** Componentes para ejecutar y enseñar en campo con baja conectividad: Cámara “modo lite”, plantillas con pictogramas y audio, y ensayos A/B rápidos.  
* **Arquetipo Principal:** Técnico agrícola  
* **JTBD Asociado:** “Explicar manejo sin depender de lectura ni señal.”
  * **5.1 Cámara modo lite**  
    * **Descripción:** Captura optimizada (compresión/guardado diferido) para teléfonos de gama baja.  
    * **Arquetipo Principal:** Técnico/Productor  
    * **JTBD Asociado:** “La app debe servir sin datos.”
  * **5.2 Plantillas con pictogramas y audio (offline)**  
    * **Descripción:** Demos paso a paso por cultivo/tema; registra finalización y feedback.  
    * **Arquetipo Principal:** Técnico/Cooperativa  
    * **JTBD Asociado:** Capacitar en vereda con barreras de idioma/alfabetización.
  * **5.3 Ensayos A/B rápidos**  
    * **Descripción:** Definir práctica A/B, capturar datos + fotos, calcular score y generar conclusión/reporte corto.  
    * **Arquetipo Principal:** Agrónomo/Técnico  
    * **JTBD Asociado:** “Elegir práctica que realmente funciona.”

---

#### **6.0 Control de Acceso & Bioseguridad**
* **Descripción:** Checklist con registro fotográfico, estado de acceso (Aprobado/Pendiente/Denegado), registro básico de proveedor/vehículo; bitácora y exportación.  
* **Arquetipo Principal:** Mayordomo/Portería  
* **JTBD Asociado:** “Cuando ingreso personal o vehículos, quiero lista de bioseguridad con registro fotográfico para autorizar o negar con respaldo.”
  * **6.1 Semáforo de acceso y motivos**  
    * **Descripción:** Estado claro y motivo documentado al finalizar control.  
    * **Arquetipo Principal:** Mayordomo  
    * **JTBD Asociado:** “La portería no puede ser cuello de botella ni coladero.”

---

#### **7.0 Conocimiento & Capacitación**
* **Descripción:** Módulo de aprendizaje situacional: referencias curadas, demos descargables y notas prácticas orientadas a condiciones locales; aborda barreras de tiempo, idioma y aplicabilidad.  
* **Arquetipo Principal:** Técnico/Productor  
* **JTBD Asociado:** Aprender lo justo, aplicable a mi región, sin depender de internet.

---

#### **8.0 Configuración**
* **Descripción:** Reglas de umbral por cultivo/zona (alimentan Semáforo y Ruta), perfiles y permisos, plantillas de reporte y preferencias offline (paquetes descargables).  
* **Arquetipo Principal:** Agrónomo/Administrador  
* **JTBD Asociado:** Consistencia y personalización local.
  * **8.1 Reglas y umbrales**  
    * **Descripción:** Límites de riesgo/tiempo (rojo <24 h; amarillo 48–72 h; verde monitoreo).  
    * **Arquetipo Principal:** Agrónomo  
    * **JTBD Asociado:** Diagnóstico más consistente.
  * **8.2 Plantillas y formatos**  
    * **Descripción:** Definir campos obligatorios, logos, numeración para auditorías.  
    * **Arquetipo Principal:** Mayordomo/Auditoría  
    * **JTBD Asociado:** “El cierre debe armarse solo.”

---

#### **9.0 Integraciones & Datos**
* **Descripción:** Exportaciones básicas (CSV) y conectores futuros (ERP/Bodega) priorizados por impacto; se pospone integración compleja en MVP.  
* **Arquetipo Principal:** Agrónomo/Administrador  
* **JTBD Asociado:** Analítica y compliance sin fricción.

---

### **Notas de diseño transversales**
- **Evidencia primero:** toda acción crítica deja huella (foto/fecha/usuario/ubicación).  
- **Offline by design:** tablero, ruta, cámara “lite” y plantillas funcionan sin señal; sincronización diferida y paquetes descargables.  
- **2–3 toques máximo:** jerarquía plana (Inicio → Lote → Acción/Reporte) para evitar menús profundos.  
- **Lenguaje del usuario:** etiquetas y decisiones simples (“Aplicar/Esperar”), evitando jerga.  

> Este canvas consolida arquetipos, JTBD y funcionalidades priorizadas (MoSCoW) para un MVP operable en campo, y traza la base para wireframes de navegación superficial (N1–N2) sin menús profundos.
