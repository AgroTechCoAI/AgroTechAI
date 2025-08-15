import React, { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, X, Image as ImageIcon, CheckCircle, AlertCircle } from 'lucide-react';
import axios from 'axios';

const ImageUpload = ({ onImageUploaded, onAnalysisComplete }) => {
  const [uploadedImage, setUploadedImage] = useState(null);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [error, setError] = useState(null);
  const [analysisId, setAnalysisId] = useState(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const onDrop = useCallback(async (acceptedFiles) => {
    const file = acceptedFiles[0];
    if (!file) return;

    // Validar tipo de archivo
    if (!file.type.startsWith('image/')) {
      setError('Solo se permiten archivos de imagen');
      return;
    }

    // Validar tamaño (máximo 10MB)
    if (file.size > 10 * 1024 * 1024) {
      setError('Archivo demasiado grande. Máximo 10MB');
      return;
    }

    setError(null);
    setUploadedImage(file);
    await uploadImage(file);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png', '.gif', '.bmp']
    },
    multiple: false
  });

  const uploadImage = async (file) => {
    setIsUploading(true);
    setUploadProgress(0);

    try {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('user_id', 1); // Usuario demo

      const response = await axios.post('http://localhost:8000/api/upload-image', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        onUploadProgress: (progressEvent) => {
          const progress = Math.round((progressEvent.loaded * 100) / progressEvent.total);
          setUploadProgress(progress);
        }
      });

      setAnalysisId(response.data.analysis_id);
      setUploadProgress(100);
      
      // Notificar al componente padre
      if (onImageUploaded) {
        onImageUploaded(response.data);
      }

      // Iniciar análisis automáticamente
      setTimeout(() => {
        startAnalysis(response.data.analysis_id);
      }, 1000);

    } catch (err) {
      setError(err.response?.data?.detail || 'Error subiendo imagen');
      setUploadProgress(0);
    } finally {
      setIsUploading(false);
    }
  };

  const startAnalysis = async (id) => {
    setIsAnalyzing(true);
    try {
      const response = await axios.post(`http://localhost:8000/api/analyses/${id}/analyze`);
      
      if (onAnalysisComplete) {
        onAnalysisComplete(response.data);
      }
      
    } catch (err) {
      setError(err.response?.data?.detail || 'Error en análisis');
    } finally {
      setIsAnalyzing(false);
    }
  };

  const removeImage = () => {
    setUploadedImage(null);
    setAnalysisId(null);
    setError(null);
    setUploadProgress(0);
  };

  const retryAnalysis = () => {
    if (analysisId) {
      startAnalysis(analysisId);
    }
  };

  return (
    <div className="w-full max-w-2xl mx-auto">
      {/* Área de Drop */}
      {!uploadedImage && (
        <div
          {...getRootProps()}
          className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors ${
            isDragActive
              ? 'border-green-500 bg-green-50'
              : 'border-gray-300 hover:border-green-400 hover:bg-green-50'
          }`}
        >
          <input {...getInputProps()} />
          <Upload className="mx-auto h-12 w-12 text-gray-400 mb-4" />
          <p className="text-lg font-medium text-gray-700 mb-2">
            {isDragActive ? 'Suelta la imagen aquí' : 'Arrastra una imagen o haz clic'}
          </p>
          <p className="text-sm text-gray-500">
            PNG, JPG, GIF hasta 10MB
          </p>
        </div>
      )}

      {/* Imagen Subida */}
      {uploadedImage && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-semibold text-gray-800">Imagen Subida</h3>
            <button
              onClick={removeImage}
              className="text-gray-400 hover:text-gray-600 transition-colors"
            >
              <X className="h-5 w-5" />
            </button>
          </div>

          {/* Preview de Imagen */}
          <div className="relative mb-4">
            <img
              src={URL.createObjectURL(uploadedImage)}
              alt="Preview"
              className="w-full h-64 object-cover rounded-lg"
            />
            <div className="absolute top-2 right-2 bg-white rounded-full p-2 shadow-md">
              <ImageIcon className="h-4 w-4 text-green-600" />
            </div>
          </div>

          {/* Información del Archivo */}
          <div className="space-y-2 mb-4">
            <div className="flex justify-between text-sm">
              <span className="text-gray-600">Nombre:</span>
              <span className="font-medium">{uploadedImage.name}</span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-gray-600">Tamaño:</span>
              <span className="font-medium">
                {(uploadedImage.size / 1024 / 1024).toFixed(2)} MB
              </span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-gray-600">Tipo:</span>
              <span className="font-medium">{uploadedImage.type}</span>
            </div>
          </div>

          {/* Barra de Progreso */}
          {isUploading && (
            <div className="mb-4">
              <div className="flex justify-between text-sm mb-2">
                <span>Subiendo...</span>
                <span>{uploadProgress}%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div
                  className="bg-green-600 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${uploadProgress}%` }}
                ></div>
              </div>
            </div>
          )}

          {/* Estado del Análisis */}
          {analysisId && !isUploading && (
            <div className="mb-4">
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">ID de Análisis:</span>
                <span className="font-mono text-sm bg-gray-100 px-2 py-1 rounded">
                  #{analysisId}
                </span>
              </div>
              
              {isAnalyzing && (
                <div className="mt-2 flex items-center text-blue-600">
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-blue-600 mr-2"></div>
                  <span className="text-sm">Analizando imagen...</span>
                </div>
              )}
            </div>
          )}

          {/* Botones de Acción */}
          <div className="flex space-x-3">
            {analysisId && !isAnalyzing && (
              <button
                onClick={retryAnalysis}
                className="flex-1 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
              >
                Reanalizar
              </button>
            )}
            
            <button
              onClick={removeImage}
              className="flex-1 bg-gray-200 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-300 transition-colors"
            >
              Nueva Imagen
            </button>
          </div>
        </div>
      )}

      {/* Mensajes de Error */}
      {error && (
        <div className="mt-4 bg-red-50 border border-red-200 rounded-lg p-4">
          <div className="flex items-center">
            <AlertCircle className="h-5 w-5 text-red-400 mr-2" />
            <span className="text-red-700">{error}</span>
          </div>
        </div>
      )}

      {/* Mensaje de Éxito */}
      {uploadProgress === 100 && !isUploading && !error && (
        <div className="mt-4 bg-green-50 border border-green-200 rounded-lg p-4">
          <div className="flex items-center">
            <CheckCircle className="h-5 w-5 text-green-400 mr-2" />
            <span className="text-green-700">Imagen subida exitosamente</span>
          </div>
        </div>
      )}
    </div>
  );
};

export default ImageUpload;
