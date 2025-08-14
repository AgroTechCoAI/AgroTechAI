"""
AgroTech AI - Main FastAPI Application
Agricultural Monitoring System with Multi-Agent AI
"""
from fastapi import FastAPI, WebSocket
from agents import check_ollama_connection, MODEL_NAME
from websocket_handler import websocket_handler

app = FastAPI(
    title="AgroTech AI Agents",
    description="Agricultural Monitoring System powered by AI agents",
    version="1.0.0"
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time agricultural monitoring"""
    await websocket_handler.handle_connection(websocket)

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "AgroTech AI Agents Demo - Powered by Ollama", 
        "model": MODEL_NAME,
        "version": "1.0.0",
        "endpoints": {
            "websocket": "/ws",
            "health": "/health",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    ollama_status = check_ollama_connection()
    return {
        "status": "healthy" if ollama_status else "error",
        "ollama": "running" if ollama_status else "not_running",
        "model": MODEL_NAME
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
