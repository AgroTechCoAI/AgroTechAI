"""
AI Agents for Agricultural Monitoring System
"""
import requests
import json
import base64
from typing import Dict, Any
from PIL import Image
import io
import asyncio
import logging
import time
from ollama_client import OllamaAgent

# Configuración de Ollama
import os
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_GENERATE_API=f"{OLLAMA_URL}/api/generate"
MODEL_NAME = "gemma3:4b"
VISION_MODEL_NAME = "qwen2.5vl:3b"  # Modelo para análisis de imágenes

# Configure logging
logger = logging.getLogger(__name__)

class ImageVisionAgent(OllamaAgent):
    """Agent specialized in analyzing agricultural images and providing detailed descriptions"""
    
    def __init__(self):
        super().__init__("ImageVision", "análisis visual de imágenes agrícolas")
    
    def _optimize_image(self, image_base64: str) -> str:
        """Optimize image size and quality for faster processing"""
        start_time = time.time()
        logger.info(f"🖼️  [{self.role}] Starting image optimization")
        
        try:
            # Decode base64 image
            image_data = base64.b64decode(image_base64)
            original_size = len(image_data)
            image = Image.open(io.BytesIO(image_data))
            
            logger.debug(f"🖼️  [{self.role}] Original image: {image.size}, format: {image.format}, size: {original_size/1024:.1f}KB")
            
            # Resize if too large (max 1024px on longest side)
            max_size = 1024
            if max(image.size) > max_size:
                ratio = max_size / max(image.size)
                new_size = tuple(int(dim * ratio) for dim in image.size)
                image = image.resize(new_size, Image.Resampling.LANCZOS)
                logger.info(f"🖼️  [{self.role}] Image resized from {image.size} to {new_size}")
            
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
                logger.debug(f"🖼️  [{self.role}] Image converted to RGB")
            
            # Save optimized image
            buffer = io.BytesIO()
            image.save(buffer, format='JPEG', quality=85, optimize=True)
            optimized_data = buffer.getvalue()
            optimized_size = len(optimized_data)
            
            elapsed_time = time.time() - start_time
            compression_ratio = (1 - optimized_size/original_size) * 100
            
            logger.info(f"✅ [{self.role}] Image optimized in {elapsed_time:.2f}s: {original_size/1024:.1f}KB → {optimized_size/1024:.1f}KB ({compression_ratio:.1f}% reduction)")
            
            return base64.b64encode(optimized_data).decode('utf-8')
        except Exception as e:
            elapsed_time = time.time() - start_time
            logger.error(f"❌ [{self.role}] Image optimization failed after {elapsed_time:.2f}s: {e}")
            return image_base64  # Return original if optimization fails

    async def analyze_image(self, image_base64: str) -> Dict[str, Any]:
        """Analyze agricultural image and provide detailed description for other agents"""
        start_time = time.time()
        logger.info(f"🔍 [{self.role}] Starting image analysis with {VISION_MODEL_NAME}")
        
        # Optimize image first
        optimized_image = self._optimize_image(image_base64)
        prompt = """You are ImageVision, a specialized AI agent that provides detailed visual descriptions of agricultural images for other AI systems to analyze.

IMPORTANT: ALWAYS respond in SPANISH. All descriptions, recommendations, and text must be in Spanish.
TASK: Analyze this agricultural image and provide a comprehensive description.

IF THE IMAGE IS NOT RELATED TO AGRICULTURE, use this specific format:
{
"is_agricultural_image": false,
"reason": "Brief explanation in Spanish why the image is not relevant.",
"confidence": 0.98,
"image_description": null,
"soil_visual_indicators": null,
"environmental_context": null,
"plant_health_indicators": null,
"recommended_focus_areas": null
}

IF THE IMAGE IS RELATED TO AGRICULTURE, RESPOND ONLY WITH A JSON in this exact format:
{
"image_description": "Detailed visual description of the crop/plant",
"soil_visual_indicators": "Visual cues about soil condition visible in image",
"environmental_context": "Environmental factors visible in the image",
"plant_health_indicators": "Specific visual signs of plant health/disease",
"recommended_focus_areas": ["area1", "area2", "area3"],
"confidence": 0.95
}

DESCRIPTION GUIDELINES:

image_description: Comprehensive overview of what's visible (plants, leaves, stems, fruits, overall layout)

soil_visual_indicators: Soil color, moisture appearance, texture, cracking, erosion signs

environmental_context: Lighting conditions, weather signs, surrounding environment, growth stage

plant_health_indicators: Leaf color variations, spots, wilting, pest damage, growth patterns

recommended_focus_areas: Key areas that SoilSense and AgriVision should prioritize

confidence: Your confidence level in the description accuracy (0.0-1.0)

Focus on quantifiable visual elements (percentages, sizes, distributions) and use agricultural terminology.
Also focus on spanish answer for the description.

JSON:"""

        payload = {
            "model": VISION_MODEL_NAME,
            "prompt": prompt,
            "images": [optimized_image],
            "stream": False,
            "options": {
                "temperature": 0.3,
                "top_p": 0.9,
                "num_predict": 400,  # Reduced from 400
                "num_ctx": 4096,     # Context window
                "num_batch": 512,    # Batch size for processing
                "num_gpu": 0,        # Run via CPU
                "low_vram": False    # Set to True if running out of VRAM
            }
        }
        timeoutReq = 180
        
        logger.debug(f"🔧 [{self.role}] Vision payload created - Model: {payload['model']}, Options: {payload['options']}, Image data length: {len(optimized_image)}, Stream: {payload['stream']}")
        
        try:
            logger.info(f"🌐 [{self.role}] Sending vision request to Ollama (timeout: {timeoutReq}s)")
            logger.debug(f"🌐 [{self.role}] Prompt length: {len(prompt)} chars, Image size: {len(optimized_image)} chars")
            
            # Use asyncio to run in thread pool for better async handling
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                lambda: self.session.post(OLLAMA_GENERATE_API, json=payload, timeout=timeoutReq)
            )
            
            elapsed_time = time.time() - start_time
            logger.info(f"✅ [{self.role}] Vision analysis completed in {elapsed_time:.2f}s")
            logger.debug(f"🌐 [{self.role}] Response status: {response.status_code}")
            
            result = response.json()
            resp = result.get("response", "{}")
            logger.debug(f"📊 [{self.role}] Actual Response: {resp}")
            parsed_result = self._parse_json_response(resp)
            
            logger.info(f"📊 [{self.role}] Vision response parsed successfully")
            logger.debug(f"📊 [{self.role}] Response: {parsed_result}")
            
            return parsed_result
        except Exception as e:
            elapsed_time = time.time() - start_time
            logger.error(f"❌ [{self.role}] Vision analysis failed after {elapsed_time:.2f}s: {e}")
            
            # Reset shared session if connection issues persist
            if "timeout" in str(e).lower() or "connection" in str(e).lower():
                logger.warning(f"🔄 [{self.role}] Resetting shared session due to connection issues")
                reset_shared_session()
                self.session = get_shared_session()
            
            return self._get_fallback_response()
    
    def _get_fallback_response(self) -> Dict[str, Any]:
        return {
            "image_description": "Error en análisis de imagen",
            "soil_visual_indicators": "No disponible",
            "environmental_context": "No disponible", 
            "plant_health_indicators": "No disponible",
            "recommended_focus_areas": ["Error en análisis"],
            "confidence": 0.0
        }


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
        logger.info(f"✅ checking OLLAMA_HEALTH {OLLAMA_URL}/api/tags")
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
