"""
AgroTech AI - Main FastAPI Application
Agricultural Monitoring System with Multi-Agent AI
"""
import logging
import sys
import os
from datetime import datetime
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from agents import check_ollama_connection, MODEL_NAME
from websocket_handler import websocket_handler

# Configure logging
def setup_logging():
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Create console handler with custom formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    
    # Create file handler for more detailed logs
    file_handler = logging.FileHandler('agrotech.log')
    file_handler.setLevel(logging.DEBUG)
    
    # Create formatters
    console_formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-5s | %(message)s',
        datefmt='%H:%M:%S'
    )
    
    file_formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Add formatters to handlers
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AgroTech AI Agents",
    description="Agricultural Monitoring System powered by AI agents",
    version="1.0.0"
)

# Configure CORS
# Get allowed origins from environment variable or use frontend defaults
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000"
).split(",")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time agricultural monitoring"""
    client_host = websocket.client.host if websocket.client else "unknown"
    logger.info(f"🔌 WebSocket connection from {client_host}")
    try:
        await websocket_handler.handle_connection(websocket)
    except Exception as e:
        logger.error(f"❌ WebSocket error for {client_host}: {e}")
    finally:
        logger.info(f"🔌 WebSocket disconnected for {client_host}")

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
    logger.info("🔍 Health check requested")
    ollama_status = check_ollama_connection()
    
    status = "healthy" if ollama_status else "error"
    ollama_text = "running" if ollama_status else "not_running"
    
    logger.info(f"💊 Health check result: {status} (Ollama: {ollama_text})")
    
    return {
        "status": status,
        "ollama": ollama_text,
        "model": MODEL_NAME
    }

if __name__ == "__main__":
    import uvicorn
    logger.info("🚀 Starting AgroTech AI Server...")
    logger.info(f"🤖 Using model: {MODEL_NAME}")
    logger.info("📱 Server will be available at: http://localhost:8000")
    logger.info("📊 API docs available at: http://localhost:8000/docs")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
