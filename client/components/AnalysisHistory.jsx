import React, { useState, useEffect } from 'react';
import { History, Eye, Calendar, FileImage, CheckCircle, Clock, XCircle } from 'lucide-react';
import axios from 'axios';

const AnalysisHistory = ({ onAnalysisSelect }) => {
  const [analyses, setAnalyses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedAnalysis, setSelectedAnalysis] = useState(null);

  useEffect(() => {
    fetchAnalyses();
  }, []);

  const fetchAnalyses = async () => {
    try {
      setLoading(true);
      const response = await axios.get('http://localhost:8000/api/analyses?limit=20');
      setAnalyses(response.data);
      setError(null);
    } catch (err) {
      setError('Error cargando historial de análisis');
      console.error('Error fetching analyses:', err);
    } finally {
      setLoading(false);
    }
  };

  const getStatusIcon = (status) => {
    switch (status) {
      case 'completed':
        return <CheckCircle className="h-4 w-4 text-green-500" />;
      case 'processing':
        return <Clock className="h-4 w-4 text-blue-500" />;
      case 'failed':
        return <XCircle className="h-4 w-4 text-red-500" />;
      default:
        return <Clock className="h-4 w-4 text-gray-500" />;
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'completed':
        return 'bg-green-100 text-green-800';
      case 'processing':
        return 'bg-blue-100 text-blue-800';
      case 'failed':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('es-ES', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const handleAnalysisClick = async (analysisId) => {
    try {
      const response = await axios.get(`http://localhost:8000/api/analyses/${analysisId}`);
      setSelectedAnalysis(response.data);
      
      if (onAnalysisSelect) {
        onAnalysisSelect(response.data);
      }
    } catch (err) {
      setError('Error cargando análisis');
    }
  };

  const refreshHistory = () => {
    fetchAnalyses();
  };

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold text-gray-800 flex items-center">
            <History className="h-5 w-5 mr-2" />
            Historial de Análisis
          </h3>
          <button
            onClick={refreshHistory}
            className="text-gray-400 hover:text-gray-600 transition-colors"
          >
            <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-gray-600"></div>
          </button>
        </div>
        <div className="text-center py-8 text-gray-500">Cargando historial...</div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-800 flex items-center">
          <History className="h-5 w-5 mr-2" />
          Historial de Análisis
        </h3>
        <button
          onClick={refreshHistory}
          className="text-gray-400 hover:text-gray-600 transition-colors"
        >
          <div className="w-4 h-4 border-2 border-gray-300 border-t-gray-600 rounded-full animate-spin"></div>
        </button>
      </div>

      {error && (
        <div className="mb-4 bg-red-50 border border-red-200 rounded-lg p-3">
          <span className="text-red-700 text-sm">{error}</span>
        </div>
      )}

      {analyses.length === 0 ? (
        <div className="text-center py-8 text-gray-500">
          <FileImage className="h-12 w-12 mx-auto mb-3 text-gray-300" />
          <p>No hay análisis previos</p>
          <p className="text-sm">Sube tu primera imagen para comenzar</p>
        </div>
      ) : (
        <div className="space-y-3 max-h-96 overflow-y-auto">
          {analyses.map((analysis) => (
            <div
              key={analysis.id}
              className={`border rounded-lg p-3 cursor-pointer transition-all hover:shadow-md ${
                selectedAnalysis?.id === analysis.id
                  ? 'border-green-500 bg-green-50'
                  : 'border-gray-200 hover:border-gray-300'
              }`}
              onClick={() => handleAnalysisClick(analysis.id)}
            >
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-3">
                  {analysis.image_url ? (
                    <img
                      src={analysis.image_url}
                      alt="Thumbnail"
                      className="w-12 h-12 object-cover rounded-lg"
                    />
                  ) : (
                    <div className="w-12 h-12 bg-gray-200 rounded-lg flex items-center justify-center">
                      <FileImage className="h-6 w-6 text-gray-400" />
                    </div>
                  )}
                  
                  <div>
                    <p className="font-medium text-gray-800 truncate max-w-32">
                      {analysis.filename || 'Sin nombre'}
                    </p>
                    <div className="flex items-center space-x-2 text-sm text-gray-500">
                      <Calendar className="h-3 w-3" />
                      <span>{formatDate(analysis.analysis_date)}</span>
                    </div>
                  </div>
                </div>

                <div className="flex items-center space-x-2">
                  <span className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(analysis.status)}`}>
                    {getStatusIcon(analysis.status)}
                    <span className="ml-1">{analysis.status}</span>
                  </span>
                  
                  <button className="text-gray-400 hover:text-gray-600 transition-colors">
                    <Eye className="h-4 w-4" />
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Detalles del Análisis Seleccionado */}
      {selectedAnalysis && (
        <div className="mt-6 border-t pt-6">
          <h4 className="font-medium text-gray-800 mb-3">Detalles del Análisis #{selectedAnalysis.id}</h4>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <h5 className="text-sm font-medium text-gray-600 mb-2">Información de la Imagen</h5>
              <div className="space-y-1 text-sm">
                <div className="flex justify-between">
                  <span className="text-gray-500">Nombre:</span>
                  <span className="font-medium">{selectedAnalysis.image.filename}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-500">Estado:</span>
                  <span className={`px-2 py-1 rounded-full text-xs ${getStatusColor(selectedAnalysis.status)}`}>
                    {selectedAnalysis.status}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-500">Fecha:</span>
                  <span className="font-medium">{formatDate(selectedAnalysis.analysis_date)}</span>
                </div>
              </div>
            </div>

            <div>
              <h5 className="text-sm font-medium text-gray-600 mb-2">Resultados</h5>
              <div className="space-y-1 text-sm">
                {selectedAnalysis.results.map((result, index) => (
                  <div key={index} className="flex justify-between">
                    <span className="text-gray-500">{result.agent}:</span>
                    <span className="font-medium">{result.confidence ? `${(result.confidence * 100).toFixed(1)}%` : 'N/A'}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {selectedAnalysis.image.url && (
            <div className="mt-4">
              <h5 className="text-sm font-medium text-gray-600 mb-2">Vista Previa</h5>
              <img
                src={selectedAnalysis.image.url}
                alt="Análisis"
                className="w-full max-w-xs rounded-lg border"
              />
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default AnalysisHistory;
