import { useState } from 'react';
import PropTypes from 'prop-types';
import ImageUpload from './ImageUpload';

function ScenarioForm({ onSubmit, isConnected, isAnalyzing }) {
  const [selectedImage, setSelectedImage] = useState(null);
  const [environmentDescription, setEnvironmentDescription] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (selectedImage && environmentDescription.trim()) {
      // Convert image to base64 for transmission
      const base64Image = selectedImage.split(',')[1]; // Remove data:image/...;base64, prefix
      onSubmit(base64Image, environmentDescription);
    }
  };

  const handleImageSelect = (imageData) => {
    setSelectedImage(imageData);
  };

  const predefinedEnvironments = [
    {
      name: "🌱 Condiciones Ideales",
      environment: "Humedad del suelo 65%, Temperatura 23°C, pH 6.7, sin viento fuerte"
    },
    {
      name: "🐛 Alta Humedad",
      environment: "Humedad del suelo 80%, Temperatura 28°C, pH 6.4, alta humedad relativa"
    },
    {
      name: "💧 Condiciones Secas",
      environment: "Humedad del suelo 15%, Temperatura 35°C, pH 7.1, viento fuerte"
    },
    {
      name: "🧪 pH Elevado",
      environment: "Humedad del suelo 55%, Temperatura 25°C, pH 8.2, condiciones normales"
    }
  ];

  const loadPredefinedEnvironment = (scenario) => {
    setEnvironmentDescription(scenario.environment);
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-8 mb-8">
      <h2 className="text-2xl font-bold mb-6 text-center text-green-800">
        📸 Análisis de Imagen Agrícola
      </h2>
      
      {/* Quick Load Predefined Environments */}
      <div className="mb-6">
        <h3 className="text-lg font-semibold mb-3">Condiciones Ambientales Predefinidas:</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-2">
          {predefinedEnvironments.map((scenario) => (
            <button
              key={scenario.name}
              onClick={() => loadPredefinedEnvironment(scenario)}
              className="p-2 text-sm bg-green-100 hover:bg-green-200 rounded-lg transition-colors"
              disabled={isAnalyzing}
            >
              {scenario.name}
            </button>
          ))}
        </div>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Image Upload and Environment Description in one row */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Image Upload - 50% width */}
          <div>
            <ImageUpload
              onImageSelect={handleImageSelect}
              selectedImage={selectedImage}
              disabled={isAnalyzing}
            />
          </div>

          {/* Environment Description - 50% width */}
          <div>
            <label htmlFor="environment-description" className="block text-sm font-medium text-gray-700 mb-2">
              🌍 Condiciones Ambientales
            </label>
            <textarea
              id="environment-description"
              value={environmentDescription}
              onChange={(e) => setEnvironmentDescription(e.target.value)}
              placeholder="Describe las condiciones del entorno: humedad del suelo, temperatura, pH, clima, etc."
              className="w-full h-64 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent resize-none"
              disabled={isAnalyzing}
              required
            />
          </div>
        </div>

        {/* Submit Button */}
        <div className="flex justify-center">
          <button
            type="submit"
            disabled={!isConnected || isAnalyzing || !selectedImage || !environmentDescription.trim()}
            className={`px-8 py-3 rounded-lg font-semibold transition-all ${
              !isConnected || isAnalyzing || !selectedImage || !environmentDescription.trim()
                ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                : 'bg-green-600 hover:bg-green-700 text-white shadow-lg hover:shadow-xl'
            }`}
          >
            {isAnalyzing ? (
              <span className="flex items-center">
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Analizando...
              </span>
            ) : (
              '🚀 Analizar Imagen'
            )}
          </button>
        </div>

        {/* Connection Status */}
        <div className="text-center">
          <span className={`text-sm ${isConnected ? 'text-green-600' : 'text-red-600'}`}>
            {isConnected ? '🟢 Conectado al servidor' : '🔴 Desconectado del servidor'}
          </span>
        </div>
      </form>
    </div>
  );
}

ScenarioForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  isConnected: PropTypes.bool.isRequired,
  isAnalyzing: PropTypes.bool.isRequired
};

export default ScenarioForm;
