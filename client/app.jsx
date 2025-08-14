// App.jsx
import React, { useState, useEffect } from 'react';
import {Line} from 'react-chartjs-2';
import ScenarioForm from './ScenarioForm.jsx';
import './styles.css';

function App() {
  const [agentData, setAgentData] = useState({
    AgriVision: null,
    SoilSense: null, 
    CropMaster: null
  });
  
  const [isConnected, setIsConnected] = useState(false);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [ws, setWs] = useState(null);

  useEffect(() => {
    const websocket = new WebSocket('ws://localhost:8000/ws');
    
    websocket.onopen = () => {
      setIsConnected(true);
      setWs(websocket);
    };
    
    websocket.onmessage = (event) => {
      const message = JSON.parse(event.data);
      
      if (message.type === 'agent_result') {
        setAgentData(prev => ({
          ...prev,
          [message.agent]: message.data
        }));
      } else if (message.type === 'status') {
        if (message.message.includes('completado')) {
          setIsAnalyzing(false);
        }
      }
    };
    
    websocket.onclose = () => {
      setIsConnected(false);
      setWs(null);
    };
    
    return () => websocket.close();
  }, []);

  const handleCustomScenario = (imageDescription, environmentDescription) => {
    if (ws && ws.readyState === WebSocket.OPEN) {
      setIsAnalyzing(true);
      setAgentData({
        AgriVision: null,
        SoilSense: null, 
        CropMaster: null
      });
      
      ws.send(JSON.stringify({
        type: 'custom_scenario',
        image_description: imageDescription,
        environment_description: environmentDescription
      }));
    }
  };

  return (
    <div className="min-h-screen bg-green-50 p-8">
      <h1 className="text-4xl font-bold text-center mb-8 text-green-800">
        🌱 AgroTech AI Agents Demo
      </h1>
      
      {/* Custom Scenario Form */}
      <ScenarioForm 
        onSubmit={handleCustomScenario}
        isConnected={isConnected}
        isAnalyzing={isAnalyzing}
      />
      
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
  );
}

function AgentCard({ title, data, color }) {
  return (
    <div className={`bg-white rounded-lg shadow-lg p-6 border-l-4 border-${color}-500`}>
      <h3 className="text-xl font-semibold mb-4">{title}</h3>
      {data ? (
        <div className="space-y-2">
          {Object.entries(data).map(([key, value]) => (
            <div key={key} className="flex justify-between">
              <span className="text-gray-600">{key}:</span>
              <span className="font-medium">
                {typeof value === 'object' ? JSON.stringify(value) : String(value)}
              </span>
            </div>
          ))}
        </div>
      ) : (
        <div className="animate-pulse">Analizando...</div>
      )}
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
          <span className={`px-4 py-2 rounded-full ${statusColors[data.overall_status]}`}>
            {data.overall_status?.toUpperCase()}
          </span>
        </div>
        
        <div>
          <h3 className="text-lg font-semibold mb-3">Acciones Prioritarias</h3>
          <ul className="list-disc list-inside space-y-1">
            {data.priority_actions?.map((action, index) => (
              <li key={index} className="text-gray-700">{action}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default App;