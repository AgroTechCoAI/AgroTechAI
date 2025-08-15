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
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configuración de Ollama
import os
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_GENERATE_API=f"{OLLAMA_URL}/api/generate"
MODEL_NAME = "gemma3:4b"
VISION_MODEL_NAME = "qwen2.5vl:3b"  # Modelo para análisis de imágenes

# Configure logging
logger = logging.getLogger(__name__)

# Shared session pool for all agents
_shared_session = None

def get_shared_session():
    """Get or create shared session with connection pooling"""
    global _shared_session
    if _shared_session is None:
        _shared_session = requests.Session()
        
        # Retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        # Mount adapter with retry strategy
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=20,
            pool_maxsize=50
        )
        _shared_session.mount("http://", adapter)
        _shared_session.mount("https://", adapter)
    
    return _shared_session

def reset_shared_session():
    """Reset shared session in case of persistent connection issues"""
    global _shared_session
    if _shared_session:
        _shared_session.close()
        _shared_session = None

class OllamaAgent:
    """Base class for all Ollama-powered AI agents"""
    
    def __init__(self, role: str, expertise: str):
        self.role = role
        self.expertise = expertise
        self.session = get_shared_session()
    
    async def generate_response(self, prompt: str) -> Dict[str, Any]:
        """Generate response from Ollama model"""
        start_time = time.time()
        logger.info(f"🤖 [{self.role}] Starting LLM call to {MODEL_NAME}")
        logger.debug(f"🤖 [{self.role}] Prompt length: {len(prompt)} characters")
        
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
            logger.info(f"🌐 [{self.role}] Sending request to Ollama: {OLLAMA_URL}")
            response = self.session.post(OLLAMA_GENERATE_API, json=payload, timeout=60)
            
            elapsed_time = time.time() - start_time
            logger.info(f"✅ [{self.role}] LLM call completed in {elapsed_time:.2f}s")
            logger.debug(f"🌐 [{self.role}] Response status: {response.status_code}")
            if response.status_code != 200:
                return self._get_fallback_response()
            
            result = response.json()
            parsed_result = self._parse_json_response(result.get("response", "{}"))
            
            logger.info(f"📊 [{self.role}] Response parsed successfully")
            logger.debug(f"📊 [{self.role}] Response keys: {list(parsed_result.keys())}")
            
            return parsed_result
        except Exception as e:
            elapsed_time = time.time() - start_time
            logger.error(f"❌ [{self.role}] LLM call failed after {elapsed_time:.2f}s: {e}")
            
            # Reset shared session if connection issues persist
            if "timeout" in str(e).lower() or "connection" in str(e).lower():
                logger.warning(f"🔄 [{self.role}] Resetting shared session due to connection issues")
                reset_shared_session()
                self.session = get_shared_session()
            
            return self._get_fallback_response()
    
    def _parse_json_response(self, response: str) -> Dict[str, Any]:
        """Enhanced JSON parsing with multiple fallback strategies"""
        logger.debug(f"📝 [{self.role}] Raw response length: {len(response)}")
        logger.debug(f"📝 [{self.role}] Raw response preview: {response[:200]}...")
        
        try:
            # Strategy 1: Direct JSON parsing (best case)
            try:
                return json.loads(response.strip())
            except json.JSONDecodeError:
                pass
            
            # Strategy 2: Extract JSON block
            start_idx = response.find('{')
            end_idx = response.rfind('}') + 1
            
            if start_idx != -1 and end_idx > start_idx:
                json_str = response[start_idx:end_idx]
                logger.debug(f"📝 [{self.role}] Extracted JSON: {json_str}")
                
                try:
                    return json.loads(json_str)
                except json.JSONDecodeError as e:
                    logger.warning(f"⚠️ [{self.role}] JSON parsing failed: {e}")
                    
                    # Strategy 3: Try to fix incomplete JSON
                    return self._find_and_fix_json(json_str)
            
            # Strategy 4: No JSON found, return fallback
            logger.warning(f"⚠️ [{self.role}] No valid JSON structure found in response")
            return self._get_fallback_response()
            
        except Exception as e:
            logger.error(f"❌ [{self.role}] JSON parsing exception: {e}")
            return self._get_fallback_response()
        
    def _find_and_fix_json(self, text_blob: str) -> Dict[str, Any]:
        """
        Finds the last, most likely JSON object in a string containing extraneous text
        and then attempts to fix it if it's incomplete.
        """
        logger.info("🕵️‍♂️ Searching for JSON in the text blob...")

        # Find the last occurrence of a JSON-starting character.
        # This is a robust way to isolate the most recent JSON block in logs.
        last_brace_index = text_blob.rfind('{')
        last_bracket_index = text_blob.rfind('[')

        if last_brace_index == -1 and last_bracket_index == -1:
            logger.error("❌ No JSON object/array start found in the text.")
            return self._create_partial_response(text_blob)

        # Slice the string from the start of the last potential JSON object
        start_index = max(last_brace_index, last_bracket_index)
        potential_json = text_blob[start_index:]

        logger.info(f"💡 Found potential JSON fragment to repair: {potential_json[:100]}...")

        # Now, use the existing smarter fixer on this cleaned-up string
        return self._fix_incomplete_json(potential_json)


    # (This is the same trusted repair function from the previous answer)
    def _fix_incomplete_json(self, json_str: str) -> Dict[str, Any]:
        """
        Robustly attempts to fix an incomplete JSON string using a stack-based parser.
        """
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass

        fixed_chars: List[str] = []
        stack: List[str] = []
        in_string = False
        escaped = False

        json_str = re.sub(r',\s*([}\]])', r'\1', json_str.strip())

        for char in json_str:
            fixed_chars.append(char)
            if in_string:
                if char == '"' and not escaped: in_string = False
                elif char == '\\': escaped = not escaped
                else: escaped = False
            else:
                if char == '"': in_string = True; escaped = False
                elif char == '{': stack.append('}')
                elif char == '[': stack.append(']')
                elif char in ('}', ']'):
                    if stack and stack[-1] == char: stack.pop()
        
        if in_string:
            fixed_chars.append('"')
            if stack and stack[-1] == '}':
                temp_str = "".join(fixed_chars).rstrip()
                if not temp_str.endswith(':'): fixed_chars.append(': null')
        
        while stack:
            fixed_chars.append(stack.pop())

        fixed_json_str = "".join(fixed_chars)
        logger.info(f"🔧 Repaired JSON string: {fixed_json_str}")

        try:
            return json.loads(fixed_json_str)
        except json.JSONDecodeError as e:
            logger.error(f"❌ Failed to fix JSON after all attempts: {e}")
            return self._create_partial_response(json_str)
    
    def _create_partial_response(self, partial_json: str) -> Dict[str, Any]:
        """Create a response from partial JSON data"""
        logger.info(f"🔨 [{self.role}] Creating partial response from incomplete data")
        
        # Extract what we can from the partial response
        result = {}
        
        # Try to extract individual fields using regex
        patterns = {
            'image_description': r'"image_description"\s*:\s*"([^"]*)"',
            'soil_visual_indicators': r'"soil_visual_indicators"\s*:\s*"([^"]*)"',
            'environmental_context': r'"environmental_context"\s*:\s*"([^"]*)"',
            'plant_health_indicators': r'"plant_health_indicators"\s*:\s*"([^"]*)"',
            'recommended_focus_areas': r'"recommended_focus_areas"\s*:\s*\[([^\]]*)\]',
            'confidence': r'"confidence"\s*:\s*([0-9.]+)'
        }
        
        for field, pattern in patterns.items():
            match = re.search(pattern, partial_json)
            if match:
                if field == 'confidence':
                    try:
                        result[field] = float(match.group(1))
                    except:
                        result[field] = 0.5
                elif field == 'recommended_focus_areas':
                    try:
                        # Parse array content
                        array_content = match.group(1)
                        items = re.findall(r'"([^"]*)"', array_content)
                        result[field] = items if items else ["análisis visual", "condiciones ambientales"]
                    except:
                        result[field] = ["análisis visual", "condiciones ambientales"]
                else:
                    result[field] = match.group(1)
            else:
                # Provide fallback values
                if field == 'confidence':
                    result[field] = 0.3
                elif field == 'recommended_focus_areas':
                    result[field] = ["análisis visual", "condiciones ambientales"]
                else:
                    result[field] = f"Información parcial - {field}"
        
        result['parsing_status'] = 'partial_recovery'
        logger.info(f"🔨 [{self.role}] Partial response created with {len(result)} fields")
        return result
    
    def _get_fallback_response(self) -> Dict[str, Any]:
        """Respuesta por defecto si falla el parsing"""
        return {"error": "No se pudo procesar la respuesta", "confidence": 0.0}


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

RESPOND ONLY WITH A JSON in this exact format:
{
    "image_description": "Detailed visual description of the crop/plant",
    "soil_visual_indicators": "Visual cues about soil condition visible in image",
    "environmental_context": "Environmental factors visible in the image",
    "plant_health_indicators": "Specific visual signs of plant health/disease",
    "recommended_focus_areas": ["area1", "area2", "area3"],
    "confidence": 0.95
}

DESCRIPTION GUIDELINES:
- image_description: Comprehensive overview of what's visible (plants, leaves, stems, fruits, overall layout)
- soil_visual_indicators: Soil color, moisture appearance, texture, cracking, erosion signs
- environmental_context: Lighting conditions, weather signs, surrounding environment, growth stage
- plant_health_indicators: Leaf color variations, spots, wilting, pest damage, growth patterns
- recommended_focus_areas: Key areas that SoilSense and AgriVision should prioritize
- confidence: Your confidence level in the description accuracy (0.0-1.0)

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
                "num_predict": 300,  # Reduced from 400
                "num_ctx": 4096,     # Context window
                "num_batch": 512,    # Batch size for processing
                "num_gpu": -1,       # Use all available GPUs
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
