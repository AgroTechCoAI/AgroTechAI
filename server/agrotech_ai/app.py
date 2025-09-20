"""
AgroTech AI - Main FastAPI Application
Agricultural Monitoring System with Multi-Agent AI
"""

import logging
import os
import sys

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from .agents import MODEL_NAME
from .ollama_client import check_ollama_connection
from .websocket_handler import websocket_handler


# Configure logging
def setup_logging():
    """Configure logging with console and file handlers."""
    # Create logger
    app_logger = logging.getLogger()
    app_logger.setLevel(logging.DEBUG)

    # Create console handler with custom formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)

    # Create file handler for more detailed logs
    file_handler = logging.FileHandler("agrotech.log")
    file_handler.setLevel(logging.DEBUG)

    # Create formatters
    console_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-5s | %(message)s", datefmt="%H:%M:%S"
    )

    file_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Add formatters to handlers
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)

    # Add handlers to logger
    app_logger.addHandler(console_handler)
    app_logger.addHandler(file_handler)

    return app_logger


# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AgroTech AI Agents",
    description="Agricultural Monitoring System powered by AI agents",
    version="1.0.0",
)

# Configure CORS
# Get allowed origins from environment variable or use frontend defaults
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time agricultural monitoring"""
    client_host = websocket.client.host if websocket.client else "unknown"
    logger.info("🔌 WebSocket connection from %s", client_host)
    try:
        await websocket_handler.handle_connection(websocket)
    except Exception as error:
        logger.error("❌ WebSocket error for %s: %s", client_host, error)
    finally:
        logger.info("🔌 WebSocket disconnected for %s", client_host)


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
            "docs": "/docs",
        },
    }


@app.options("/")
async def root_options():
    """Handle OPTIONS request for root endpoint"""
    return {"message": "OK"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    logger.info("🔍 Health check requested")
    ollama_status = check_ollama_connection()

    status = "healthy" if ollama_status else "error"
    ollama_text = "running" if ollama_status else "not_running"

    logger.info("💊 Health check result: %s (Ollama: %s)", status, ollama_text)

    return {"status": status, "ollama": ollama_text, "model": MODEL_NAME}


def main():
    """Main entry point for the application."""
    import uvicorn  # pylint: disable=import-outside-toplevel

    logger.info("🚀 Starting AgroTech AI Server...")
    logger.info("🤖 Using model: %s", MODEL_NAME)
    logger.info("📱 Server will be available at: http://localhost:8000")
    logger.info("📊 API docs available at: http://localhost:8000/docs")

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
