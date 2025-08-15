from fastapi import FastAPI, WebSocket, UploadFile, File, HTTPException, Depends, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests
import json
import asyncio
from typing import Dict, Any, List
import os
from datetime import datetime
import uuid
import sys
import os

# Agregar el directorio actual al path de Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar nuevos módulos
from database import get_db, create_tables, create_default_user, Analysis, Image, AnalysisResult, User
from image_processor import ImageProcessor
from sqlalchemy.orm import Session

app = FastAPI(title="AgroTech AI - Sistema de Análisis de Imágenes Agrícolas")

# Montar archivos estáticos
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Configuración de Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:latest"  # Modelo disponible en tu sistema

# Inicializar procesador de imágenes
image_processor = ImageProcessor()

# Crear tablas y usuario demo al iniciar
@app.on_event("startup")
async def startup_event():
    create_tables()
    create_default_user()
    print("✅ Sistema AgroTech AI iniciado")

class OllamaAgent:
    def __init__(self, role: str, expertise: str):
        self.role = role
        self.expertise = expertise
    
    async def generate_response(self, prompt: str) -> Dict[str, Any]:
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
    def __init__(self):
        super().__init__("AgriVision", "análisis visual de cultivos")
    
    async def analyze_image(self, image_path: str, image_features: Dict[str, Any]) -> Dict[str, Any]:
        # Combinar análisis de OpenCV con IA
        prompt = f"""Eres AgriVision, un experto en análisis visual de cultivos agrícolas.

ANÁLISIS TÉCNICO DE LA IMAGEN:
{json.dumps(image_features, indent=2)}

TAREA: Analiza esta imagen del cultivo basándote en el análisis técnico y tu experiencia.

RESPONDE ÚNICAMENTE CON UN JSON VÁLIDO en este formato exacto:
{{
    "crop_health": "healthy",
    "pest_detected": false,
    "leaf_condition": "good",
    "disease_probability": 0.2,
    "visual_symptoms": ["hojas verdes", "sin manchas"],
    "recommendations": ["continuar monitoreo", "revisar en 2 días"],
    "confidence": 0.85,
    "ai_insights": "Análisis basado en características visuales detectadas"
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
            "confidence": 0.0,
            "ai_insights": "Análisis fallido - usar datos técnicos básicos"
        }

class SoilSenseAgent(OllamaAgent):
    def __init__(self):
        super().__init__("SoilSense", "condiciones ambientales y del suelo")
    
    async def analyze_environment(self, image_features: Dict[str, Any]) -> Dict[str, Any]:
        prompt = f"""Eres SoilSense, especialista en condiciones ambientales y del suelo para agricultura.

ANÁLISIS DE LA IMAGEN:
{json.dumps(image_features, indent=2)}

TAREA: Analiza las condiciones ambientales visibles en la imagen.

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
    "confidence": 0.88,
    "visual_indicators": "Análisis basado en características visuales del suelo"
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
            "confidence": 0.0,
            "visual_indicators": "Análisis fallido"
        }

class CropMasterAgent(OllamaAgent):
    def __init__(self):
        super().__init__("CropMaster", "toma de decisiones agrícolas integrales")
    
    async def make_decision(self, vision_data: Dict, soil_data: Dict, image_features: Dict) -> Dict[str, Any]:
        prompt = f"""Eres CropMaster, el sistema inteligente que toma decisiones agrícolas basado en datos de múltiples sensores.

DATOS DE ENTRADA:
- AgriVision: {json.dumps(vision_data, indent=2)}
- SoilSense: {json.dumps(soil_data, indent=2)}
- Análisis Técnico: {json.dumps(image_features, indent=2)}

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
    "confidence": 0.92,
    "decision_factors": "Análisis basado en múltiples fuentes de datos"
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
            "confidence": 0.0,
            "decision_factors": "Análisis fallido"
        }

# Endpoints de API REST
@app.post("/api/upload-image")
async def upload_image(
    file: UploadFile = File(...),
    user_id: int = Form(1),  # Por defecto usuario demo
    db: Session = Depends(get_db)
):
    """Subir imagen para análisis"""
    try:
        # Validar tipo de archivo
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="Solo se permiten archivos de imagen")
        
        # Validar tamaño (máximo 10MB)
        if file.size > 10 * 1024 * 1024:
            raise HTTPException(status_code=400, detail="Archivo demasiado grande. Máximo 10MB")
        
        # Generar nombre único
        file_extension = os.path.splitext(file.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        
        # Leer contenido del archivo
        file_content = await file.read()
        
        # Guardar imagen
        image_path = image_processor.save_uploaded_image(file_content, unique_filename)
        
        # Crear análisis en base de datos
        analysis = Analysis(
            user_id=user_id,
            image_path=image_path,
            status="pending"
        )
        db.add(analysis)
        db.commit()
        db.refresh(analysis)
        
        # Crear registro de imagen
        image_record = Image(
            analysis_id=analysis.id,
            filename=file.filename,
            file_path=image_path,
            file_size=file.size,
            mime_type=file.content_type
        )
        db.add(image_record)
        db.commit()
        
        return {
            "message": "Imagen subida exitosamente",
            "analysis_id": analysis.id,
            "filename": unique_filename,
            "status": "pending"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error subiendo imagen: {str(e)}")

@app.get("/api/analyses")
async def get_analyses(
    user_id: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Obtener historial de análisis"""
    analyses = db.query(Analysis).filter(Analysis.user_id == user_id).order_by(Analysis.analysis_date.desc()).limit(limit).all()
    
    result = []
    for analysis in analyses:
        # Obtener imagen asociada
        image = db.query(Image).filter(Image.analysis_id == analysis.id).first()
        
        result.append({
            "id": analysis.id,
            "status": analysis.status,
            "analysis_date": analysis.analysis_date,
            "filename": image.filename if image else "N/A",
            "image_url": f"/uploads/{os.path.basename(analysis.image_path)}" if analysis.image_path else None
        })
    
    return result

@app.get("/api/analyses/{analysis_id}")
async def get_analysis(
    analysis_id: int,
    db: Session = Depends(get_db)
):
    """Obtener análisis específico con resultados"""
    analysis = db.query(Analysis).filter(Analysis.id == analysis_id).first()
    if not analysis:
        raise HTTPException(status_code=404, detail="Análisis no encontrado")
    
    # Obtener imagen
    image = db.query(Image).filter(Image.analysis_id == analysis_id).first()
    
    # Obtener resultados
    results = db.query(AnalysisResult).filter(AnalysisResult.analysis_id == analysis_id).all()
    
    return {
        "id": analysis.id,
        "status": analysis.status,
        "analysis_date": analysis.analysis_date,
        "image": {
            "filename": image.filename if image else "N/A",
            "url": f"/uploads/{os.path.basename(analysis.image_path)}" if analysis.image_path else None
        },
        "results": [
            {
                "agent": result.agent_name,
                "data": json.loads(result.result_data) if result.result_data else {},
                "confidence": result.confidence,
                "created_at": result.created_at
            }
            for result in results
        ]
    }

@app.post("/api/analyses/{analysis_id}/analyze")
async def analyze_image(
    analysis_id: int,
    db: Session = Depends(get_db)
):
    """Ejecutar análisis completo de una imagen"""
    try:
        # Obtener análisis
        analysis = db.query(Analysis).filter(Analysis.id == analysis_id).first()
        if not analysis:
            raise HTTPException(status_code=404, detail="Análisis no encontrado")
        
        # Actualizar estado
        analysis.status = "processing"
        db.commit()
        
        # Obtener imagen
        image = db.query(Image).filter(Image.analysis_id == analysis_id).first()
        if not image:
            raise HTTPException(status_code=404, detail="Imagen no encontrada")
        
        # Analizar características de la imagen
        image_features = image_processor.analyze_image_features(image.file_path)
        
        # Inicializar agentes
        agri_vision = AgriVisionAgent()
        soil_sense = SoilSenseAgent()
        crop_master = CropMasterAgent()
        
        # Paso 1: AgriVision
        vision_result = await agri_vision.analyze_image(image.file_path, image_features)
        
        # Guardar resultado
        vision_db_result = AnalysisResult(
            analysis_id=analysis_id,
            agent_name="AgriVision",
            result_data=json.dumps(vision_result),
            confidence=vision_result.get("confidence", 0.0)
        )
        db.add(vision_db_result)
        
        # Paso 2: SoilSense
        soil_result = await soil_sense.analyze_environment(image_features)
        
        # Guardar resultado
        soil_db_result = AnalysisResult(
            analysis_id=analysis_id,
            agent_name="SoilSense",
            result_data=json.dumps(soil_result),
            confidence=soil_result.get("confidence", 0.0)
        )
        db.add(soil_db_result)
        
        # Paso 3: CropMaster
        final_decision = await crop_master.make_decision(vision_result, soil_result, image_features)
        
        # Guardar resultado
        crop_db_result = AnalysisResult(
            analysis_id=analysis_id,
            agent_name="CropMaster",
            result_data=json.dumps(final_decision),
            confidence=final_decision.get("confidence", 0.0)
        )
        db.add(crop_db_result)
        
        # Actualizar estado
        analysis.status = "completed"
        db.commit()
        
        return {
            "message": "Análisis completado exitosamente",
            "analysis_id": analysis_id,
            "results": {
                "AgriVision": vision_result,
                "SoilSense": soil_result,
                "CropMaster": final_decision
            }
        }
        
    except Exception as e:
        # Actualizar estado a fallido
        analysis.status = "failed"
        db.commit()
        raise HTTPException(status_code=500, detail=f"Error en análisis: {str(e)}")

# WebSocket para tiempo real
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Verificar que Ollama esté funcionando
    try:
        test_response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if test_response.status_code != 200:
            await websocket.send_json({"type": "error", "message": "Ollama no está ejecutándose. Ejecuta 'ollama serve'"})
            return
    except requests.exceptions.RequestException:
        await websocket.send_json({"type": "error", "message": "No se puede conectar a Ollama. Asegúrate de que esté ejecutándose en el puerto 11434"})
        return
    
    await websocket.send_json({"type": "status", "message": "✅ Conectado al sistema AgroTech AI"})
    
    try:
        while True:
            # Mantener conexión activa
            await asyncio.sleep(30)
            await websocket.send_json({"type": "ping", "message": "Conexión activa"})
            
    except Exception as e:
        await websocket.send_json({"type": "error", "message": f"Error en WebSocket: {str(e)}"})

@app.get("/")
async def root():
    return {"message": "AgroTech AI - Sistema de Análisis de Imágenes Agrícolas", "model": MODEL_NAME}

@app.get("/health")
async def health_check():
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return {"status": "healthy", "ollama": "running" if response.status_code == 200 else "error"}
    except:
        return {"status": "error", "ollama": "not_running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)