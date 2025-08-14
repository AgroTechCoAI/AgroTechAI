"""
WebSocket handler for real-time agricultural monitoring
"""
import asyncio
from fastapi import WebSocket
from typing import Dict, Any
from agents import AgriVisionAgent, SoilSenseAgent, CropMasterAgent, check_ollama_connection


class WebSocketHandler:
    """Handles WebSocket connections and agent orchestration"""
    
    def __init__(self):
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
        
        if message_type == "custom_scenario":
            await self.handle_custom_scenario(websocket, message)
        else:
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
            
            # Paso 1: AgriVision
            await websocket.send_json({
                "type": "status", 
                "message": "🔍 AgriVision procesando imagen..."
            })
            
            vision_result = await self.agri_vision.analyze_image(image_description)
            await websocket.send_json({
                "type": "agent_result",
                "agent": "AgriVision",
                "data": vision_result
            })
            
            await asyncio.sleep(2)
            
            # Paso 2: SoilSense
            await websocket.send_json({
                "type": "status", 
                "message": "🌍 SoilSense analizando condiciones ambientales..."
            })
            
            soil_result = await self.soil_sense.analyze_environment(environment_description)
            await websocket.send_json({
                "type": "agent_result",
                "agent": "SoilSense",
                "data": soil_result
            })
            
            await asyncio.sleep(2)
            
            # Paso 3: CropMaster (decisión final)
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
