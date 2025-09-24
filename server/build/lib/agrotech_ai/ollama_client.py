"""
AI Agents for Agricultural Monitoring System
"""

import json
import logging

# Configuración de Ollama
import os
import re
import time
from typing import Any, Dict, List

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_GENERATE_API = f"{OLLAMA_URL}/api/generate"
MODEL_NAME = "gemma3:4b"
VISION_MODEL_NAME = "qwen2.5vl:3b"  # Modelo para análisis de imágenes

# Configure logging
logger = logging.getLogger(__name__)

# Shared session pool for all agents
_SHARED_SESSION = None


def get_shared_session():
    """Get or create shared session with connection pooling"""
    global _SHARED_SESSION  # pylint: disable=global-statement
    if _SHARED_SESSION is None:
        _SHARED_SESSION = requests.Session()

        # Retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )

        # Mount adapter with retry strategy
        adapter = HTTPAdapter(
            max_retries=retry_strategy, pool_connections=20, pool_maxsize=50
        )
        _SHARED_SESSION.mount("http://", adapter)
        _SHARED_SESSION.mount("https://", adapter)

    return _SHARED_SESSION


def reset_shared_session():
    """Reset shared session in case of persistent connection issues"""
    global _SHARED_SESSION  # pylint: disable=global-statement
    if _SHARED_SESSION:
        _SHARED_SESSION.close()
        _SHARED_SESSION = None


def check_ollama_connection() -> bool:
    """Check if Ollama is running and accessible"""
    try:
        logger.info("✅ checking OLLAMA_HEALTH %s/api/tags", OLLAMA_URL)
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


class OllamaAgent:  # pylint: disable=too-few-public-methods
    """Base class for all Ollama-powered AI agents"""

    def __init__(self, role: str, expertise: str):
        self.role = role
        self.expertise = expertise
        self.session = get_shared_session()

    async def generate_response(self, prompt: str) -> Dict[str, Any]:
        """Generate response from Ollama model"""
        start_time = time.time()
        logger.info("🤖 [%s] Starting LLM call to %s", self.role, MODEL_NAME)
        logger.debug("🤖 [%s] Prompt length: %s characters", self.role, len(prompt))

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "num_predict": 300,
            },
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
            logger.debug(
                f"📊 [{self.role}] Response keys: {list(parsed_result.keys())}"
            )

            return parsed_result
        except Exception as e:
            elapsed_time = time.time() - start_time
            logger.error(
                f"❌ [{self.role}] LLM call failed after " f"{elapsed_time:.2f}s: {e}"
            )

            # Reset shared session if connection issues persist
            if "timeout" in str(e).lower() or "connection" in str(e).lower():
                logger.warning(
                    f"🔄 [{self.role}] Resetting shared session due to "
                    f"connection issues"
                )
                reset_shared_session()
                self.session = get_shared_session()

            return self._get_fallback_response()

    def _find_and_fix_json(self, text_blob: str) -> Dict[str, Any]:
        """
        Encuentra el JSON más probable en un bloque de texto y luego intenta
        repararlo si está incompleto.
        """
        logger.info("🕵️‍♂️ Buscando JSON en el bloque de texto...")

        # Find the first occurrence of JSON structures to get complete objects
        first_brace_index = text_blob.find("{")
        first_bracket_index = text_blob.find("[")

        if first_brace_index == -1 and first_bracket_index == -1:
            logger.error(
                "❌ No se encontró un inicio de objeto/array JSON en el texto."
            )
            return self._create_partial_response(text_blob)

        # Choose the first JSON structure that appears
        if first_brace_index == -1:
            start_index = first_bracket_index
            start_char = "["
            end_char = "]"
        elif first_bracket_index == -1:
            start_index = first_brace_index
            start_char = "{"
            end_char = "}"
        else:
            if first_brace_index < first_bracket_index:
                start_index = first_brace_index
                start_char = "{"
                end_char = "}"
            else:
                start_index = first_bracket_index
                start_char = "["
                end_char = "]"

        # Extract only the JSON part by finding the matching closing
        # brace/bracket
        potential_json = self._extract_json_structure(
            text_blob, start_index, start_char, end_char
        )

        logger.info(
            "💡 Fragmento de JSON potencial encontrado para reparar: %s...",
            potential_json[:100],
        )

        # Llama a la función reparadora con el fragmento aislado
        return self._fix_incomplete_json(potential_json)

    def _extract_json_structure(
        self, text: str, start_index: int, start_char: str, end_char: str
    ) -> str:
        """Extract a complete JSON structure from text starting at
        start_index."""
        if start_index >= len(text):
            return ""

        brace_count = 0
        i = start_index

        while i < len(text):
            char = text[i]
            if char == start_char:
                brace_count += 1
            elif char == end_char:
                brace_count -= 1
                if brace_count == 0:
                    # Found the matching closing brace/bracket
                    return text[start_index : i + 1]
            i += 1

        # If we reach here, the JSON is incomplete (no matching closing
        # brace/bracket)
        return text[start_index:]

    def _fix_incomplete_json(self, json_str: str) -> Dict[str, Any]:
        """
        La función definitiva y robusta para reparar JSON incompleto. Maneja
        claves, valores y estructuras truncadas, y distingue correctamente
        entre ellos.
        """
        logger.info("🔧 Intentando reparar JSON incompleto con lógica definitiva...")

        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            # Se confirma que la cadena está incompleta, se procede a reparar.
            pass

        json_str, fixed_chars, stack, in_string = self._repair_json_string(json_str)

        # --- LÓGICA DE RECONSTRUCCIÓN ROBUSTA Y COMBINADA ---
        if in_string:
            # Caso 1: La cadena se cortó a mitad de un string.
            temp_str = "".join(fixed_chars).rstrip()
            last_quote_index = temp_str.rfind('"')
            if last_quote_index > 0:
                preceding_content = temp_str[:last_quote_index].rstrip()
                if preceding_content.endswith(":"):
                    fixed_chars.append('"')  # Es un valor, solo ciérralo.
                else:
                    fixed_chars.append(
                        '": null'
                    )  # Es una clave, ciérrala y añade un valor.
            else:
                fixed_chars.append('": null')  # Debe ser una clave al inicio.
        else:
            # Caso 2: La cadena se cortó después de dos puntos,
            # esperando un valor.
            temp_str = "".join(fixed_chars).rstrip()
            if temp_str.endswith(":"):
                fixed_chars.append(" null")  # Añade un valor nulo por defecto.

        # Finalmente, cierra todas las estructuras abiertas.
        while stack:
            fixed_chars.append(stack.pop())

        fixed_json_str = "".join(fixed_chars)
        logger.info("🔧 Cadena JSON reparada: %s", fixed_json_str)

        try:
            return json.loads(fixed_json_str)
        except json.JSONDecodeError as e:
            logger.error(
                "❌ Fallo al reparar el JSON después de todos los intentos: %s", e
            )
            return {
                "error": "Fallo al parsear el JSON",
                "original_string": json_str,
            }

    def _repair_json_string(self, json_str):
        fixed_chars: List[str] = []
        stack: List[str] = []
        in_string = False
        escaped = False

        json_str = re.sub(r",\s*([}\]])", r"\1", json_str.strip())

        for char in json_str:
            fixed_chars.append(char)
            if in_string:
                if char == '"' and not escaped:
                    in_string = False
                elif char == "\\":
                    escaped = not escaped
                else:
                    escaped = False
            else:
                if char == '"':
                    in_string = True
                    escaped = False
                elif char == "{":
                    stack.append("}")
                elif char == "[":
                    stack.append("]")
                elif char in ("}", "]"):
                    if stack and stack[-1] == char:
                        stack.pop()

        return json_str, fixed_chars, stack, in_string

    def _parse_json_response(self, response: str) -> Dict[str, Any]:
        """Enhanced JSON parsing with multiple fallback strategies"""
        logger.debug("📝 [%s] Raw response length: %s", self.role, len(response))
        logger.debug("📝 [%s] Raw response preview: %s...", self.role, response[:200])

        try:
            # Strategy 1: Direct JSON parsing (best case)
            try:
                return json.loads(response.strip())
            except json.JSONDecodeError:
                pass

            # Strategy 2: Extract JSON block
            start_idx = response.find("{")
            end_idx = response.rfind("}") + 1

            if start_idx != -1 and end_idx > start_idx:
                json_str = response[start_idx:end_idx]
                logger.debug("📝 [%s] Extracted JSON: %s", self.role, json_str)

                try:
                    return json.loads(json_str)
                except json.JSONDecodeError as e:
                    logger.warning("⚠️ [%s] JSON parsing failed: %s", self.role, e)

                    # Strategy 3: Try to fix incomplete JSON
                    return self._find_and_fix_json(json_str)

            # Strategy 4: No JSON found, return fallback
            logger.warning(
                "⚠️ [%s] No valid JSON structure found in response", self.role
            )
            return self._create_partial_response(json_str)

        except Exception as error:
            logger.error("❌ [%s] JSON parsing exception: %s", self.role, error)
            return self._get_fallback_response()

    def _create_partial_response(self, partial_json: str) -> Dict[str, Any]:
        """Create a response from partial JSON data"""
        logger.info("🔨 [%s] Creating partial response from incomplete data", self.role)

        # Extract what we can from the partial response
        result = {}

        # Try to extract individual fields using regex
        patterns = {
            "image_description": (r'"image_description"\s*:\s*"([^"]*)"'),
            "soil_visual_indicators": (r'"soil_visual_indicators"\s*:\s*"([^"]*)"'),
            "environmental_context": (r'"environmental_context"\s*:\s*"([^"]*)"'),
            "plant_health_indicators": (r'"plant_health_indicators"\s*:\s*"([^"]*)"'),
            "recommended_focus_areas": (
                r'"recommended_focus_areas"\s*:\s*\[([^\]]*)\]'
            ),
            "confidence": r'"confidence"\s*:\s*([0-9.]+)',
        }

        for field, pattern in patterns.items():
            match = re.search(pattern, partial_json)
            if match:
                if field == "confidence":
                    try:
                        result[field] = float(match.group(1))
                    except (ValueError, AttributeError):
                        result[field] = 0.5
                elif field == "recommended_focus_areas":
                    try:
                        # Parse array content
                        array_content = match.group(1)
                        items = re.findall(r'"([^"]*)"', array_content)
                        result[field] = (
                            items
                            if items
                            else [
                                "análisis visual",
                                "condiciones ambientales",
                            ]
                        )
                    except (ValueError, AttributeError):
                        result[field] = [
                            "análisis visual",
                            "condiciones ambientales",
                        ]
                else:
                    result[field] = match.group(1)
            else:
                # Provide fallback values
                if field == "confidence":
                    result[field] = 0.3
                elif field == "recommended_focus_areas":
                    result[field] = [
                        "análisis visual",
                        "condiciones ambientales",
                    ]
                else:
                    result[field] = f"Información parcial - {field}"

        result["parsing_status"] = "partial_recovery"
        logger.info(
            "🔨 [%s] Partial response created with %s fields", self.role, len(result)
        )
        return result

    def _get_fallback_response(self) -> Dict[str, Any]:
        """Respuesta por defecto si falla el parsing"""
        return {"error": "No se pudo procesar la respuesta", "confidence": 0.0}
