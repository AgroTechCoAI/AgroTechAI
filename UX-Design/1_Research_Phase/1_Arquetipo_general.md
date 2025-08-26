# Construcción de arquetipos

## Contexto

Esta es una propuesta para la creación de una aplicación móvil que ofrezca una solución de inteligencia artificial al sector agrícola. El objetivo del proyecto es que, a partir de una simple imagen, la app pueda diagnosticar la salud de los cultivos y ofrecer sugerencias para su mejoramiento. El desarrollo priorizará una interfaz amigable para todo tipo de usuario (agricultores, agrónomos, etc.) y estará diseñada para operar de forma offline, garantizando su uso en el campo.

## Herramientas

Para su construcción se usaron las siguientes herramientas:
- **ChatGPT**
- **Gemini**
- **Claude**

## Prompts
Para la construcción y selección de arquetipos se uso el siguiente prompt:

```markdown
Actúa como un investigador UX senior especializado en agricultura y tecnología. Tu tarea es realizar una investigación completa para identificar y desarrollar los arquetipos más relevantes para un sistema de IA que analiza cultivos mediante imágenes.
 
## FASE 1: INVESTIGACIÓN DE ROLES AGRÍCOLAS
 
Primero, investiga y analiza todos los posibles roles/usuarios que podrían beneficiarse de un sistema de análisis de cultivos con IA en el contexto de [REGIÓN/PAÍS ESPECÍFICO].
 
Para cada rol identifica:
- **Nombre del rol y variaciones regionales**
- **Responsabilidades principales relacionadas con cultivos**
- **Nivel de toma de decisiones** (estratégico/táctico/operativo)
- **Frecuencia de interacción con cultivos** (diaria/semanal/estacional)
- **Recursos tecnológicos típicos** disponibles
- **Urgencia típica de sus decisiones** (crítica/moderada/flexible)
- **Influencia en compra de tecnología** (decisor/influenciador/usuario final)
 
Roles a considerar (pero no limitarte a):
- Agricultores (pequeños, medianos, grandes)
- Agrónomos (independientes, empleados, consultores)
- Técnicos agrícolas
- Administradores de finca/mayordomos
- Ingenieros agrícolas
- Supervisores de campo
- Estudiantes de agronomía
- Investigadores agrícolas
- Extensionistas rurales
 
## FASE 2: ANÁLISIS Y SELECCIÓN
 
Después de investigar los roles, realiza un análisis de priorización considerando:
 
**Criterios de Selección:**
1. **Potencial de adopción** (1-10): Qué tan probable es que usen tecnología de IA
2. **Frecuencia de uso potencial** (1-10): Qué tan seguido necesitarían el diagnóstico
3. **Impacto en resultados** (1-10): Qué tan críticas son sus decisiones para el éxito del cultivo
4. **Capacidad de pago** (1-10): Recursos para invertir en tecnología
5. **Influencia en otros** (1-10): Capacidad de generar adopción viral
 
Presenta tu análisis en una tabla y selecciona los **3-4 arquetipos más prometedores** justificando tu selección.
 
## FASE 3: DESARROLLO DETALLADO DE ARQUETIPOS
 
Para cada arquetipo seleccionado, desarrolla un perfil completo:
 
### ARQUETIPO [NÚMERO]: [NOMBRE DEL ROL]
 
**👤 PERFIL PERSONAL**
- **Nombre ficticio:** [Nombre realista para la región]
- **Edad:** [Rango específico]
- **Ubicación:** [Zona rural/urbana específica]
- **Educación:** [Nivel y tipo]
- **Años de experiencia:** [En agricultura]
- **Situación familiar:** [Relevante para decisiones laborales]
 
**🏢 CONTEXTO PROFESIONAL**
- **Título/Rol exacto:**
- **Responsabilidades principales:**
- **Tamaño de operación:** [Hectáreas, número de empleados]
- **Tipos de cultivos principales:** [Específicos para la región]
- **Cultivos secundarios:**
- **Estacionalidad:** [Cómo varía su trabajo por temporadas]
- **Estructura organizacional:** [A quién reporta, quién le reporta]
- **Presupuesto típico para tecnología:**
 
**📱 RELACIÓN CON TECNOLOGÍA**
- **Dispositivos principales:** [Smartphone, tablet, laptop]
- **Apps agrícolas actuales:** [Específicas que usa]
- **Nivel de confianza tecnológica:** [1-10 con explicación]
- **Canales de información preferidos:** [WhatsApp, YouTube, etc.]
- **Barreras tecnológicas principales:**
- **Persona de soporte técnico:** [A quién acude cuando tiene problemas]
 
**🎯 OBJETIVOS Y MOTIVACIONES**
- **Objetivo principal en su rol:**
- **Definición de éxito:**
- **Métricas que sigue:**
- **Motivadores para adoptar nueva tecnología:**
- **Presiones externas que enfrenta:**
 
**😤 FRUSTRACIONES Y DESAFÍOS**
- **3 problemas principales actuales:**
- **Limitaciones de recursos más críticas:**
- **Temores específicos sobre IA/tecnología:**
- **Experiencias negativas previas con tecnología:**
 
**🔄 ESCENARIOS DE USO ESPECÍFICOS**
 
**Escenario 1: [Nombre del escenario]**
- **Situación:** [Descripción detallada]
- **Frecuencia:** [Cuándo ocurre]
- **Ubicación:** [Dónde estaría]
- **Urgencia:** [Nivel de prisa]
- **Información que necesita:**
- **Decisiones que debe tomar:**
- **Consecuencias de error:**
 
**Escenario 2: [Nombre del escenario]**
[Misma estructura]
 
**Escenario 3: [Nombre del escenario]**
[Misma estructura]
 
**💬 CITAS REPRESENTATIVAS**
Incluye 2-3 frases que este arquetipo diría sobre:
- Su trabajo actual
- Tecnología
- El problema que resuelve nuestro producto
 
**🎨 CONTEXTO VISUAL**
- **Entorno de trabajo típico:**
- **Vestimenta característica:**
- **Herramientas que porta:**
- **Vehículo que usa:**
 
## ESPECIFICACIONES ADICIONALES:
 
- Basa todo en investigación real del sector agrícola de [REGIÓN]
- Incluye variaciones culturales y socioeconómicas relevantes
- Considera factores climáticos y geográficos específicos
- Usa terminología agrícola precisa y regional
- Incluye desafíos reales como conectividad rural, estacionalidad, etc.
- Considera diferentes escalas de operación (pequeña/mediana/grande)
- Incluye aspectos generacionales (adopción tecnológica por edad)
 
**Contexto del producto recordar:**
- Sistema que analiza fotos de cultivos con IA
- Proporciona diagnóstico del estado de la planta  
- Ofrece recomendaciones específicas de mejora
- Funciona mediante smartphone/tablet
- Dirigido a mercado agrícola de [ESPECIFICAR REGIÓN]
```

Una vez obtenido los arquetipos, se usaron lo siguientes prompts para obtener mas detalles de cada uno de ellos:

### Para enriquecer escenarios:
```markdown
Toma el Arquetipo [NOMBRE] y crea 5 escenarios adicionales de uso del sistema de IA, incluyendo situaciones de emergencia, uso estacional específico, y casos edge que podrían presentarse en [REGIÓN].
```
### Para validar realismo:
```markdown
Revisa el Arquetipo [NOMBRE] y identifica:1. Qué aspectos podrían no ser realistas para [REGIÓN]2. Qué detalles culturales o socioeconómicos faltan3. Cómo ajustarías el perfil para que sea más auténtico
```
### Para explorar motivaciones:
```markdown
Profundiza en las motivaciones del Arquetipo [NOMBRE]:- ¿Qué lo mantiene despierto por las noches?- ¿Cuál sería su mayor preocupación al adoptar IA?- ¿Qué historia de éxito lo convencería de usarlo?
```