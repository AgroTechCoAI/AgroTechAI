// App.jsx
import React, { useState, useEffect } from 'react';
import {Line} from 'react-chartjs-2';
import './styles.css';

// Importar nuevos componentes
import ImageUpload from './components/ImageUpload';
import AnalysisHistory from './components/AnalysisHistory';

function App() {
  const [agentData, setAgentData] = useState({
    AgriVision: null,
    SoilSense: null, 
    CropMaster: null
  });
  
  const [isConnected, setIsConnected] = useState(false);
  const [currentAnalysis, setCurrentAnalysis] = useState(null);
  const [showHistory, setShowHistory] = useState(false);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws');
    
    ws.onopen = () => setIsConnected(true);
    ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      if (message.type === 'agent_result' && message.agent) {
        setAgentData(prev => ({
          ...prev,
          [message.agent]: message.data
        }));
      }
    };
    
    return () => ws.close();
  }, []);

  const handleImageUploaded = (uploadData) => {
    console.log('Imagen subida:', uploadData);
    // Limpiar datos previos
    setAgentData({
      AgriVision: null,
      SoilSense: null,
      CropMaster: null
    });
  };

  const handleAnalysisComplete = (analysisData) => {
    console.log('Análisis completado:', analysisData);
    setCurrentAnalysis(analysisData);
    
    // Actualizar datos de agentes
    setAgentData({
      AgriVision: analysisData.results.AgriVision,
      SoilSense: analysisData.results.SoilSense,
      CropMaster: analysisData.results.CropMaster
    });
  };

  const handleAnalysisSelect = (analysisData) => {
    setCurrentAnalysis(analysisData);
    
    // Actualizar datos de agentes si hay resultados
    if (analysisData.results && analysisData.results.length > 0) {
      const newAgentData = {};
      analysisData.results.forEach(result => {
        newAgentData[result.agent] = result.data;
      });
      setAgentData(newAgentData);
    }
  };

  return (
    <div className="min-h-screen bg-green-50 p-8">
      <h1 className="text-4xl font-bold text-center mb-8 text-green-800">
        🌱 AgroTech AI - Análisis de Imágenes Agrícolas
      </h1>
      
      {/* Barra de Estado */}
      <div className="flex items-center justify-center mb-6">
        <div className={`flex items-center space-x-2 px-4 py-2 rounded-full ${
          isConnected ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
        }`}>
          <div className={`w-2 h-2 rounded-full ${
            isConnected ? 'bg-green-500' : 'bg-red-500'
          }`}></div>
          <span className="text-sm font-medium">
            {isConnected ? 'Conectado' : 'Desconectado'}
          </span>
        </div>
      </div>

      {/* Componente de Subida de Imágenes */}
      <div className="mb-8">
        <ImageUpload 
          onImageUploaded={handleImageUploaded}
          onAnalysisComplete={handleAnalysisComplete}
        />
      </div>

      {/* Botón para Mostrar/Ocultar Historial */}
      <div className="text-center mb-6">
        <button
          onClick={() => setShowHistory(!showHistory)}
          className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors"
        >
          {showHistory ? 'Ocultar Historial' : 'Ver Historial de Análisis'}
        </button>
      </div>

      {/* Historial de Análisis */}
      {showHistory && (
        <div className="mb-8">
          <AnalysisHistory onAnalysisSelect={handleAnalysisSelect} />
        </div>
      )}

      {/* Resultados del Análisis */}
      {currentAnalysis && (
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-center mb-6 text-green-800">
            📊 Resultados del Análisis #{currentAnalysis.analysis_id}
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            {/* Agente AgriVision */}
            <AgentCard 
              title="🔍 AgriVision" 
              data={agentData.AgriVision}
              color="blue"
            />
            
            {/* Agente SoilSense */}
            <AgentCard 
              title="🌍 SoilSense" 
              data={agentData.SoilSense}
              color="brown"
            />
            
            {/* Agente CropMaster */}
            <AgentCard 
              title="🧠 CropMaster" 
              data={agentData.CropMaster}
              color="green"
            />
          </div>
          
          {/* Panel de Decisión Final */}
          <DecisionPanel data={agentData.CropMaster} />
        </div>
      )}

      {/* Mensaje cuando no hay análisis */}
      {!currentAnalysis && !showHistory && (
        <div className="text-center py-12 text-gray-500">
          <div className="text-6xl mb-4">🌱</div>
          <h3 className="text-xl font-medium mb-2">Bienvenido a AgroTech AI</h3>
          <p className="text-gray-600">
            Sube una imagen de tu cultivo para comenzar el análisis inteligente
          </p>
        </div>
      )}
    </div>
  );
}

function AgentCard({ title, data, color }) {
  if (!data) return null;

  return (
    <div className={`bg-white rounded-lg shadow-lg p-6 border-l-4 border-${color}-500`}>
      <h3 className="text-xl font-semibold mb-4">{title}</h3>
      <div className="space-y-2">
        {Object.entries(data).map(([key, value]) => (
          <div key={key} className="flex justify-between">
            <span className="text-gray-600 capitalize">{key.replace(/_/g, ' ')}:</span>
            <span className="font-medium">
              {typeof value === 'object' ? JSON.stringify(value) : String(value)}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

function DecisionPanel({ data }) {
  if (!data) return null;
  
  const statusColors = {
    excellent: 'bg-green-100 text-green-800',
    good: 'bg-blue-100 text-blue-800', 
    warning: 'bg-yellow-100 text-yellow-800',
    critical: 'bg-red-100 text-red-800'
  };
  
  return (
    <div className="bg-white rounded-lg shadow-lg p-8">
      <h2 className="text-2xl font-bold mb-6 text-center">📊 Decisión Final del Sistema</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <h3 className="text-lg font-semibold mb-3">Estado General</h3>
          <span className={`px-4 py-2 rounded-full ${statusColors[data.overall_status] || 'bg-gray-100 text-gray-800'}`}>
            {data.overall_status?.toUpperCase() || 'UNKNOWN'}
          </span>
        </div>
        
        <div>
          <h3 className="text-lg font-semibold mb-3">Acciones Prioritarias</h3>
          <ul className="list-disc list-inside space-y-1">
            {data.priority_actions?.map((action, index) => (
              <li key={index} className="text-gray-700">{action}</li>
            )) || <li className="text-gray-500">No hay acciones definidas</li>}
          </ul>
        </div>
      </div>

      {/* Información Adicional */}
      <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="text-center">
          <h4 className="text-sm font-medium text-gray-600 mb-1">Rendimiento Estimado</h4>
          <span className="text-lg font-semibold text-green-600">
            {data.estimated_yield?.toUpperCase() || 'N/A'}
          </span>
        </div>
        
        <div className="text-center">
          <h4 className="text-sm font-medium text-gray-600 mb-1">Nivel de Riesgo</h4>
          <span className="text-lg font-semibold text-orange-600">
            {data.risk_assessment?.toUpperCase() || 'N/A'}
          </span>
        </div>
        
        <div className="text-center">
          <h4 className="text-sm font-medium text-gray-600 mb-1">Próxima Inspección</h4>
          <span className="text-lg font-semibold text-blue-600">
            {data.next_inspection_hours ? `${data.next_inspection_hours}h` : 'N/A'}
          </span>
        </div>
      </div>

      {/* Alertas Urgentes */}
      {data.urgent_alerts && data.urgent_alerts.length > 0 && (
        <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg">
          <h4 className="text-sm font-medium text-red-800 mb-2">🚨 Alertas Urgentes</h4>
          <ul className="list-disc list-inside space-y-1">
            {data.urgent_alerts.map((alert, index) => (
              <li key={index} className="text-red-700 text-sm">{alert}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;