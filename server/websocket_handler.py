"""
WebSocket handler for real-time agricultural monitoring
"""
import asyncio
import logging
from fastapi import WebSocket
from typing import Dict, Any
from agents import ImageVisionAgent, AgriVisionAgent, SoilSenseAgent, CropMasterAgent, check_ollama_connection

logger = logging.getLogger(__name__)


class WebSocketHandler:
    """Handles WebSocket connections and agent orchestration"""
    
    def __init__(self):
        self.image_vision = ImageVisionAgent()
        self.agri_vision = AgriVisionAgent()
        self.soil_sense = SoilSenseAgent()
        self.crop_master = CropMasterAgent()
    
    async def handle_connection(self, websocket: WebSocket):
        """Main WebSocket connection handler"""
        await websocket.accept()
        
        # Verificar que Ollama esté funcionando
        if not check_ollama_connection():
            await websocket.send_json({
                "type": "error", 
                "message": "No se puede conectar a Ollama. Asegúrate de que esté ejecutándose en el puerto 11434"
            })
            return
        
        try:
            while True:
                # Esperar mensaje del cliente
                message = await websocket.receive_json()
                await self.process_message(websocket, message)
                
        except Exception as e:
            await websocket.send_json({
                "type": "error", 
                "message": f"Error en WebSocket: {str(e)}"
            })
    
    async def process_message(self, websocket: WebSocket, message: Dict[str, Any]):
        """Process incoming WebSocket messages"""
        message_type = message.get("type")
        logger.info(f"📨 Received message type: {message_type}")
        
        if message_type == "ping":
            logger.info("📸 Processing ping")
            await websocket.send_json({
                "type": "pong",
                "message": "connection success"
            })
        elif message_type == "custom_scenario":
            logger.info("🔍 Processing custom scenario")
            await self.handle_custom_scenario(websocket, message)
        elif message_type == "image_analysis":
            logger.info("📸 Processing image analysis")
            await self.handle_image_analysis(websocket, message)
        else:
            logger.warning(f"❓ Unknown message type: {message_type}")
            await websocket.send_json({
                "type": "error",
                "message": f"Tipo de mensaje no reconocido: {message_type}"
            })
    
    async def handle_custom_scenario(self, websocket: WebSocket, message: Dict[str, Any]):
        """Handle custom user-defined scenarios"""
        image_description = message.get("image_description", "")
        environment_description = message.get("environment_description", "")
        
        if not image_description or not environment_description:
            await websocket.send_json({
                "type": "error",
                "message": "Se requieren tanto la descripción de imagen como las condiciones ambientales"
            })
            return
        
        await self.analyze_scenario(
            websocket,
            image_description,
            environment_description,
            "🔍 Escenario Personalizado"
        )
    
    async def handle_image_analysis(self, websocket: WebSocket, message: Dict[str, Any]):
        """Handle image analysis with ImageVision agent"""
        image_base64 = message.get("image_data", "")
        environment_description = message.get("environment_description", "")
        
        if not image_base64:
            await websocket.send_json({
                "type": "error",
                "message": "Se requiere una imagen para el análisis"
            })
            return
        
        if not environment_description:
            await websocket.send_json({
                "type": "error", 
                "message": "Se requiere descripción de condiciones ambientales"
            })
            return
        
        await self.analyze_image_scenario(
            websocket,
            image_base64,
            environment_description,
            "📸 Análisis de Imagen"
        )
    
    async def analyze_image_scenario(self, websocket: WebSocket, image_base64: str,
                                   environment_description: str, scenario_name: str):
        """Analyze a scenario starting with image analysis using ImageVision"""
        try:
            # Informar escenario actual
            await websocket.send_json({
                "type": "scenario",
                "data": {
                    "name": scenario_name,
                    "description": f"Analizando: {scenario_name}"
                }
            })
            
            # Paso 1: ImageVision (análisis de imagen)
            await websocket.send_json({
                "type": "status",
                "message": "📸 ImageVision procesando imagen..."
            })
            
            image_analysis = await self.image_vision.analyze_image(image_base64)
            await websocket.send_json({
                "type": "agent_result",
                "agent": "ImageVision", 
                "data": image_analysis
            })
            
            await asyncio.sleep(2)
            
            # Extraer descripción de la imagen para AgriVision
            image_description = image_analysis.get("image_description", "Error en análisis")
            
            # Preparar datos para SoilSense
            soil_indicators = image_analysis.get("soil_visual_indicators", "")
            environmental_context = image_analysis.get("environmental_context", "")
            combined_environment = f"{environment_description}. Indicadores visuales: {soil_indicators}. Contexto: {environmental_context}"
            
            # Paso 2: Ejecutar AgriVision y SoilSense CONCURRENTEMENTE
            await websocket.send_json({
                "type": "status",
                "message": "🔍🌍 Analizando salud del cultivo y condiciones ambientales concurrentemente..."
            })
            
            # Ejecutar ambos agentes en paralelo
            vision_task = self.agri_vision.analyze_image(image_description)
            soil_task = self.soil_sense.analyze_environment(combined_environment)
            
            # Esperar a que ambos terminen
            vision_result, soil_result = await asyncio.gather(vision_task, soil_task)
            
            # Enviar resultados tan pronto como estén listos
            await websocket.send_json({
                "type": "agent_result",
                "agent": "AgriVision",
                "data": vision_result
            })
            
            await websocket.send_json({
                "type": "agent_result",
                "agent": "SoilSense",
                "data": soil_result
            })
            
            await asyncio.sleep(1)  # Reduced delay since they ran concurrently
            
            # Paso 3: CropMaster (decisión final integrando todos los datos)
            await websocket.send_json({
                "type": "status",
                "message": "🧠 CropMaster fusionando datos y decidiendo..."
            })
            
            final_decision = await self.crop_master.make_decision(vision_result, soil_result)
            await websocket.send_json({
                "type": "agent_result",
                "agent": "CropMaster",
                "data": final_decision
            })
            
            await websocket.send_json({
                "type": "status",
                "message": "✅ Análisis completado"
            })
            
        except Exception as e:
            await websocket.send_json({
                "type": "error",
                "message": f"Error en análisis de imagen: {str(e)}"
            })
    
    async def analyze_scenario(self, websocket: WebSocket, image_description: str, 
                              environment_description: str, scenario_name: str):
        """Analyze a scenario using all three AI agents"""
        try:
            # Informar escenario actual
            await websocket.send_json({
                "type": "scenario",
                "data": {
                    "name": scenario_name,
                    "description": f"Analizando: {scenario_name}"
                }
            })
            
            # Paso 1: Ejecutar AgriVision y SoilSense CONCURRENTEMENTE
            await websocket.send_json({
                "type": "status", 
                "message": "🔍🌍 Analizando imagen y condiciones ambientales concurrentemente..."
            })
            
            # Ejecutar ambos agentes en paralelo
            vision_task = self.agri_vision.analyze_image(image_description)
            soil_task = self.soil_sense.analyze_environment(environment_description)
            
            # Esperar a que ambos terminen
            vision_result, soil_result = await asyncio.gather(vision_task, soil_task)
            
            # Enviar resultados tan pronto como estén listos
            await websocket.send_json({
                "type": "agent_result",
                "agent": "AgriVision",
                "data": vision_result
            })
            
            await websocket.send_json({
                "type": "agent_result",
                "agent": "SoilSense",
                "data": soil_result
            })
            
            await asyncio.sleep(1)  # Reduced delay since they ran concurrently
            
            # Paso 2: CropMaster (decisión final)
            await websocket.send_json({
                "type": "status", 
                "message": "🧠 CropMaster fusionando datos y decidiendo..."
            })
            
            final_decision = await self.crop_master.make_decision(vision_result, soil_result)
            await websocket.send_json({
                "type": "agent_result",
                "agent": "CropMaster",
                "data": final_decision
            })
            
            await websocket.send_json({
                "type": "status", 
                "message": "✅ Análisis completado"
            })
            
        except Exception as e:
            await websocket.send_json({
                "type": "error", 
                "message": f"Error en análisis: {str(e)}"
            })


# Global WebSocket handler instance
websocket_handler = WebSocketHandler()
