# AgroTech AI - Agricultural Monitoring System

An intelligent agricultural monitoring system powered by AI agents that analyze crop images, soil health, and environmental factors in real-time. The system uses multiple specialized AI agents to provide comprehensive agricultural insights and automated decision-making through image analysis.

## 🌟 Features

- **Multi-Agent AI System**: Four specialized AI agents working together
  - **ImageVision**: Advanced image analysis of uploaded agricultural photos
  - **AgriVision**: Visual analysis of crop health and pest detection
  - **SoilSense**: Environmental conditions and soil analysis  
  - **CropMaster**: Integrated decision-making and recommendations
- **Image Upload & Analysis**: Drag-and-drop image upload with real-time AI analysis
- **Real-time Monitoring**: Live data processing and WebSocket communication
- **Interactive Dashboard**: React-based frontend with real-time visualizations
- **Docker Support**: Containerized deployment with docker-compose
- **Advanced Logging**: Comprehensive logging system for monitoring and debugging

## 🏗️ Architecture

This project follows a client-server architecture:

```
AgroTech AI/
├── client/              # React frontend application
│   ├── app.jsx          # Main React component with agent coordination
│   ├── ScenarioForm.jsx # Image upload and environment input form
│   ├── ImageUpload.jsx  # Drag-and-drop image upload component
│   ├── main.jsx         # React entry point
│   ├── index.html       # HTML template
│   ├── styles.css       # Tailwind CSS styles
│   └── package.json     # Frontend dependencies
├── server/              # FastAPI backend application
│   ├── main.py          # FastAPI server with WebSocket support
│   ├── agents.py        # AI agents implementation
│   ├── websocket_handler.py # WebSocket communication handler
│   ├── requirements.txt # Python dependencies
│   └── Dockerfile       # Docker container configuration
└── docker-compose.yml   # Multi-service Docker orchestration
```

## 🚀 Getting Started

### Prerequisites

- **Node.js** v20.18.3 or higher
- **Python** 3.8 or higher
- **Ollama** (AI model server)
- **Docker** and **Docker Compose** (for containerized deployment)

## 🐳 Quick Start with Docker (Recommended)

The easiest way to run the entire system is using Docker Compose:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd reto2
   ```

2. **Start all services**:
   ```bash
   docker-compose up
   ```

   This will automatically:
   - Build and start the FastAPI server
   - Start the React client with hot reload
   - Download and run Ollama with the required model
   - Set up networking between all services

3. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Ollama API: http://localhost:11434

## 🔧 Manual Installation

### 🤖 Ollama Setup

Ollama is a local AI model server that runs large language models on your machine. It provides the AI capabilities for our agricultural agents.

1. **Install Ollama**:
   ```bash
   # On macOS
   brew install ollama
   
   # On Linux
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # On Windows
   # Download from https://ollama.ai/download
   ```

2. **Start Ollama server**:
   ```bash
   ollama serve
   ```

3. **Install the required model**:
   ```bash
   ollama pull gemma3:4b
   ```

   > **Note**: The system is configured to use the `gemma3:4b` model for better performance and image analysis capabilities. You can also use other models by updating the `MODEL_NAME` variable in `server/agents.py`.

### 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd reto2
   ```

2. **Install server dependencies**:
   ```bash
   cd server
   pip install -r requirements.txt
   ```

3. **Install client dependencies**:
   ```bash
   cd ../client
   npm install
   ```

### 🏃‍♂️ Running the Application

#### Start the Backend Server

1. **Navigate to server directory**:
   ```bash
   cd server
   ```

2. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

   The server will be available at: `http://localhost:8000`

#### Start the Frontend Client

1. **Navigate to client directory**:
   ```bash
   cd client
   ```

2. **Start the React development server**:
   ```bash
   npm start
   ```

   The client will be available at: `http://localhost:3000`

### 🔍 API Endpoints

- **GET** `/` - Health check and API information
- **GET** `/health` - Server and Ollama status check
- **WebSocket** `/ws` - Real-time communication for AI agent data

## 🧠 AI Agents Overview

### ImageVision Agent
- **Purpose**: Advanced image analysis of agricultural photos
- **Capabilities**: 
  - Real-time image processing and optimization
  - Detailed visual crop description generation
  - Soil condition assessment from visual cues
  - Plant health indicator identification
  - Environmental context analysis from images

### AgriVision Agent
- **Purpose**: Visual analysis of crop conditions based on image descriptions
- **Capabilities**: 
  - Crop health assessment
  - Pest and disease detection
  - Leaf condition analysis
  - Visual symptom identification

### SoilSense Agent
- **Purpose**: Environmental and soil monitoring
- **Capabilities**:
  - Soil moisture analysis
  - pH level monitoring
  - Temperature and humidity tracking
  - Irrigation recommendations

### CropMaster Agent
- **Purpose**: Integrated decision-making
- **Capabilities**:
  - Data fusion from multiple agents
  - Risk assessment
  - Yield estimation
  - Priority action recommendations

## 📊 Image Analysis Workflow

The system now features an advanced image analysis workflow:

1. **📸 Image Upload**: Drag-and-drop interface for agricultural photos
2. **🔍 Image Processing**: Automatic optimization and base64 encoding
3. **🤖 AI Analysis**: Multi-agent analysis pipeline:
   - ImageVision extracts detailed visual descriptions
   - AgriVision analyzes crop health from descriptions
   - SoilSense evaluates environmental conditions
   - CropMaster provides integrated recommendations

## 📊 Pre-configured Environmental Conditions

The system includes four pre-configured environmental scenarios:

1. **🌱 Ideal Conditions**: Optimal growing environment
2. **🐛 High Humidity**: Conditions favorable for pest development
3. **💧 Dry Conditions**: Drought stress monitoring
4. **🧪 High pH**: Alkaline soil conditions

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI server
- **WebSockets**: Real-time communication
- **Requests**: HTTP client for Ollama integration
- **Ollama**: Local AI model server (gemma3:4b)
- **PIL (Pillow)**: Image processing and optimization
- **asyncio**: Asynchronous processing for better performance

### Frontend
- **React 18**: User interface framework
- **Vite**: Build tool and development server
- **Tailwind CSS**: Utility-first CSS framework
- **Chart.js**: Data visualization
- **Native WebSocket API**: Real-time communication

### DevOps
- **Docker**: Containerization platform
- **Docker Compose**: Multi-service orchestration
- **Ollama Container**: Containerized AI model serving

## 🔧 Development

### Server Development
```bash
cd server
# Install dependencies
pip install -r requirements.txt

# Run with auto-reload
uvicorn main:app --reload
```

### Client Development
```bash
cd client
# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build
```

## 🧪 Testing the System

### With Docker (Recommended)
1. **Start with Docker Compose**: `docker-compose up`
2. **Open your browser** to `http://localhost:3000`
3. **Upload an agricultural image** using the drag-and-drop interface
4. **Select environmental conditions** or use predefined scenarios
5. **Watch real-time AI analysis** from all four agents

### Manual Setup
1. **Ensure Ollama is running** with the gemma3:4b model
2. **Start the backend server** on port 8000
3. **Start the frontend client** on port 3000
4. **Open your browser** to `http://localhost:3000`
5. **Upload images and analyze** agricultural conditions in real-time

### Sample Workflow
1. **Drag and drop** an agricultural image (JPG, PNG, WebP)
2. **Choose environmental conditions** from presets or custom input
3. **Click "Analyze Image"** to start the AI analysis
4. **Monitor progress** as each agent processes the data:
   - ImageVision analyzes the uploaded image
   - AgriVision evaluates crop health
   - SoilSense assesses environmental factors
   - CropMaster provides final recommendations

## 📝 Configuration

### Model Configuration
To change the AI model, edit `server/agents.py`:
```python
MODEL_NAME = "gemma3:4b"  # Change to other Ollama models
VISION_MODEL_NAME = "gemma3:4b"  # Model for image analysis
```

### Port Configuration
- **Backend**: Change port in uvicorn command or `main.py`
- **Frontend**: Change port in `vite.config.js`

## 🚨 Troubleshooting

### Common Issues

1. **"Could not connect to Ollama"**:
   - Ensure Ollama is running: `ollama serve`
   - Check if the model is installed: `ollama list`
   - For Docker: Check if ollama service is healthy

2. **"Error loading ASGI app"**:
   - Run uvicorn from the server directory
   - Use: `uvicorn main:app --reload`
   - Check if all Python dependencies are installed

3. **Frontend connection issues**:
   - Ensure backend is running on port 8000
   - Check WebSocket connection in browser console
   - Verify network connectivity between containers (if using Docker)

4. **Image upload problems**:
   - Check file size (large images are automatically optimized)
   - Supported formats: JPG, PNG, WebP
   - Clear browser cache if upload interface doesn't respond

5. **AI analysis failures**:
   - Check Ollama model availability: `ollama list`
   - Monitor server logs for detailed error messages
   - Ensure sufficient system resources (RAM/GPU) for model inference

### Port Conflicts
- Backend default: `8000`
- Frontend default: `3000`
- Ollama default: `11434`

## 🔍 API Reference

### WebSocket Events

The system uses WebSocket communication for real-time AI agent interaction:

#### Client → Server Events
```javascript
// Image analysis request
{
  "type": "image_analysis",
  "image_data": "base64_encoded_image",
  "environment_description": "Environmental conditions text"
}
```

#### Server → Client Events
```javascript
// Agent result
{
  "type": "agent_result",
  "agent": "ImageVision|AgriVision|SoilSense|CropMaster",
  "data": {
    // Agent-specific response data
  }
}

// Status update
{
  "type": "status",
  "message": "Analysis status message"
}
```

### REST Endpoints
- **GET** `/` - API information and health check
- **GET** `/health` - Detailed system health including Ollama connectivity
- **WebSocket** `/ws` - Real-time agent communication

### Image Processing
- **Supported formats**: JPG, PNG, WebP
- **Automatic optimization**: Images larger than 1024px are resized
- **Quality optimization**: JPEG compression at 85% quality
- **Base64 encoding**: All images converted for WebSocket transmission

## 📄 License

This project is for educational purposes as part of EAFIT University coursework.

## 🤝 Contributing

This is an academic project. For improvements or suggestions, please create an issue or submit a pull request.

---

**Built with ❤️ for sustainable agriculture and AI innovation**
