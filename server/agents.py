"""
AI Agents for Agricultural Monitoring System
"""
import requests
import json
from typing import Dict, Any

# Configuración de Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3"  # Cambia por llama2 o codellama si prefieres

class OllamaAgent:
    """Base class for all Ollama-powered AI agents"""
    
    def __init__(self, role: str, expertise: str):
        self.role = role
        self.expertise = expertise
    
    async def generate_response(self, prompt: str) -> Dict[str, Any]:
        """Generate response from Ollama model"""
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "num_predict": 300
            }
        }
        
        try:
            response = requests.post(OLLAMA_URL, json=payload, timeout=30)
            result = response.json()
            return self._parse_json_response(result.get("response", "{}"))
        except Exception as e:
            print(f"Error en {self.role}: {e}")
            return self._get_fallback_response()
    
    def _parse_json_response(self, response: str) -> Dict[str, Any]:
        """Intenta extraer JSON de la respuesta de Ollama"""
        try:
            # Buscar JSON en la respuesta
            start_idx = response.find('{')
            end_idx = response.rfind('}') + 1
            
            if start_idx != -1 and end_idx > start_idx:
                json_str = response[start_idx:end_idx]
                return json.loads(json_str)
            else:
                return self._get_fallback_response()
        except:
            return self._get_fallback_response()
    
    def _get_fallback_response(self) -> Dict[str, Any]:
        """Respuesta por defecto si falla el parsing"""
        return {"error": "No se pudo procesar la respuesta", "confidence": 0.0}


class AgriVisionAgent(OllamaAgent):
    """Agent specialized in visual analysis of crop conditions"""
    
    def __init__(self):
        super().__init__("AgriVision", "análisis visual de cultivos")
    
    async def analyze_image(self, image_description: str) -> Dict[str, Any]:
        """Analyze crop image description and provide health assessment"""
        prompt = f"""Eres AgriVision, un experto en análisis visual de cultivos agrícolas.

TAREA: Analiza esta descripción de imagen del cultivo: "{image_description}"

RESPONDE ÚNICAMENTE CON UN JSON VÁLIDO en este formato exacto:
{{
    "crop_health": "healthy",
    "pest_detected": false,
    "leaf_condition": "good",
    "disease_probability": 0.2,
    "visual_symptoms": ["hojas verdes", "sin manchas"],
    "recommendations": ["continuar monitoreo", "revisar en 2 días"],
    "confidence": 0.85
}}

REGLAS IMPORTANTES:
- crop_health debe ser: "healthy", "stressed", "diseased"
- pest_detected debe ser: true o false
- leaf_condition debe ser: "excellent", "good", "fair", "poor"
- disease_probability debe ser un número entre 0.0 y 1.0
- NO agregues texto antes o después del JSON
- El JSON debe ser válido y parseable

JSON:"""

        return await self.generate_response(prompt)
    
    def _get_fallback_response(self) -> Dict[str, Any]:
        return {
            "crop_health": "unknown",
            "pest_detected": False,
            "leaf_condition": "unknown",
            "disease_probability": 0.0,
            "visual_symptoms": ["Error en análisis"],
            "recommendations": ["Reintentar análisis"],
            "confidence": 0.0
        }


class SoilSenseAgent(OllamaAgent):
    """Agent specialized in environmental conditions and soil analysis"""
    
    def __init__(self):
        super().__init__("SoilSense", "condiciones ambientales y del suelo")
    
    async def analyze_environment(self, conditions: str) -> Dict[str, Any]:
        """Analyze environmental conditions and soil parameters"""
        prompt = f"""Eres SoilSense, especialista en condiciones ambientales y del suelo para agricultura.

TAREA: Analiza estas condiciones ambientales: "{conditions}"

RESPONDE ÚNICAMENTE CON UN JSON VÁLIDO en este formato exacto:
{{
    "soil_moisture": 45,
    "ph_level": 6.5,
    "temperature": 24,
    "humidity": 60,
    "irrigation_needed": true,
    "fertilizer_status": "adequate",
    "environmental_stress": "low",
    "alerts": ["humedad baja detectada"],
    "confidence": 0.88
}}

REGLAS IMPORTANTES:
- soil_moisture: número entre 0-100 (porcentaje)
- ph_level: número entre 4.0-9.0
- temperature: número entre -10 y 50 (celsius)
- humidity: número entre 0-100 (porcentaje)
- irrigation_needed: true o false
- fertilizer_status: "deficient", "adequate", "excess"
- environmental_stress: "low", "medium", "high"
- NO agregues texto antes o después del JSON

JSON:"""

        return await self.generate_response(prompt)
    
    def _get_fallback_response(self) -> Dict[str, Any]:
        return {
            "soil_moisture": 50,
            "ph_level": 7.0,
            "temperature": 25,
            "humidity": 50,
            "irrigation_needed": False,
            "fertilizer_status": "adequate",
            "environmental_stress": "unknown",
            "alerts": [],
            "confidence": 0.0
        }


class CropMasterAgent(OllamaAgent):
    """Agent for integrated agricultural decision-making"""
    
    def __init__(self):
        super().__init__("CropMaster", "toma de decisiones agrícolas integrales")
    
    async def make_decision(self, vision_data: Dict, soil_data: Dict) -> Dict[str, Any]:
        """Make integrated decisions based on data from multiple agents"""
        prompt = f"""Eres CropMaster, el sistema inteligente que toma decisiones agrícolas basado en datos de múltiples sensores.

DATOS DE ENTRADA:
- AgriVision: {json.dumps(vision_data, indent=2)}
- SoilSense: {json.dumps(soil_data, indent=2)}

TAREA: Fusiona toda esta información y toma una decisión integral sobre el manejo del cultivo.

RESPONDE ÚNICAMENTE CON UN JSON VÁLIDO en este formato exacto:
{{
    "overall_status": "good",
    "priority_actions": ["regar por 10 minutos", "aplicar fungicida preventivo"],
    "estimated_yield": "high",
    "risk_assessment": "low",
    "next_inspection_hours": 24,
    "economic_impact": "positive",
    "urgent_alerts": [],
    "confidence": 0.92
}}

REGLAS IMPORTANTES:
- overall_status: "excellent", "good", "warning", "critical"
- estimated_yield: "high", "medium", "low"
- risk_assessment: "low", "medium", "high", "critical"
- economic_impact: "positive", "neutral", "negative"
- next_inspection_hours: número entre 1 y 168 (1 semana máximo)
- priority_actions: lista de máximo 4 acciones concretas
- NO agregues texto antes o después del JSON

JSON:"""

        return await self.generate_response(prompt)
    
    def _get_fallback_response(self) -> Dict[str, Any]:
        return {
            "overall_status": "unknown",
            "priority_actions": ["Error en análisis"],
            "estimated_yield": "unknown",
            "risk_assessment": "unknown",
            "next_inspection_hours": 24,
            "economic_impact": "neutral",
            "urgent_alerts": [],
            "confidence": 0.0
        }


def check_ollama_connection() -> bool:
    """Check if Ollama is running and accessible"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
