import React, { useState, useRef } from 'react';

function ImageUpload({ onImageSelect, selectedImage, disabled }) {
  const [dragActive, setDragActive] = useState(false);
  const inputRef = useRef(null);

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const handleChange = (e) => {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  };

  const handleFile = (file) => {
    if (file && file.type.startsWith('image/')) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const imageData = e.target.result;
        onImageSelect(imageData, file);
      };
      reader.readAsDataURL(file);
    } else {
      alert('Por favor selecciona un archivo de imagen válido');
    }
  };

  const onButtonClick = () => {
    inputRef.current?.click();
  };

  const removeImage = () => {
    onImageSelect(null, null);
  };

  return (
    <div className="w-full">
      <label className="block text-sm font-medium text-gray-700 mb-2">
        📸 Imagen del Cultivo
      </label>
      
      {selectedImage ? (
        <div className="relative">
          <img
            src={selectedImage}
            alt="Imagen seleccionada"
            className="w-full h-64 object-cover rounded-lg border-2 border-gray-300"
          />
          <button
            type="button"
            onClick={removeImage}
            disabled={disabled}
            className="absolute top-2 right-2 bg-red-500 hover:bg-red-600 text-white rounded-full p-2 disabled:opacity-50"
          >
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
      ) : (
        <div
          className={`relative border-2 border-dashed rounded-lg p-6 transition-colors ${
            dragActive 
              ? 'border-green-400 bg-green-50' 
              : 'border-gray-300 hover:border-gray-400'
          } ${disabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer'}`}
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
          onClick={onButtonClick}
        >
          <input
            ref={inputRef}
            type="file"
            className="hidden"
            accept="image/*"
            onChange={handleChange}
            disabled={disabled}
          />
          
          <div className="text-center">
            <svg
              className="mx-auto h-12 w-12 text-gray-400"
              stroke="currentColor"
              fill="none"
              viewBox="0 0 48 48"
            >
              <path
                d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            <div className="mt-4">
              <p className="text-sm text-gray-600">
                <span className="font-medium text-green-600 hover:text-green-500">
                  Haz clic para subir
                </span>{' '}
                o arrastra y suelta
              </p>
              <p className="text-xs text-gray-500 mt-1">
                PNG, JPG, GIF hasta 10MB
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default ImageUpload;
