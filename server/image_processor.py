import cv2
import numpy as np
from PIL import Image
import os
import json
from typing import Dict, Any, Tuple
import base64
from io import BytesIO

class ImageProcessor:
    def __init__(self):
        self.upload_dir = "uploads"
        self.ensure_upload_dir()
    
    def ensure_upload_dir(self):
        """Crear directorio de uploads si no existe"""
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)
    
    def save_uploaded_image(self, file_content: bytes, filename: str) -> str:
        """Guardar imagen subida y retornar ruta"""
        file_path = os.path.join(self.upload_dir, filename)
        with open(file_path, "wb") as f:
            f.write(file_content)
        return file_path
    
    def analyze_image_features(self, image_path: str) -> Dict[str, Any]:
        """Analizar características básicas de la imagen usando OpenCV"""
        try:
            # Leer imagen con OpenCV
            image = cv2.imread(image_path)
            if image is None:
                return {"error": "No se pudo leer la imagen"}
            
            # Convertir a RGB para análisis
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Análisis básico
            height, width = image.shape[:2]
            
            # Análisis de color
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            
            # Detectar verde (plantas)
            lower_green = np.array([35, 50, 50])
            upper_green = np.array([85, 255, 255])
            green_mask = cv2.inRange(hsv, lower_green, upper_green)
            green_percentage = (np.sum(green_mask > 0) / (height * width)) * 100
            
            # Detectar marrón (suelo)
            lower_brown = np.array([10, 50, 50])
            upper_brown = np.array([20, 255, 255])
            brown_mask = cv2.inRange(hsv, lower_brown, upper_brown)
            brown_percentage = (np.sum(brown_mask > 0) / (height * width)) * 100
            
            # Detectar amarillo (enfermedad/estres)
            lower_yellow = np.array([20, 50, 50])
            upper_yellow = np.array([30, 255, 255])
            yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
            yellow_percentage = (np.sum(yellow_mask > 0) / (height * width)) * 100
            
            # Análisis de textura (gradiente)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
            texture_score = np.mean(gradient_magnitude)
            
            # Detección de bordes
            edges = cv2.Canny(gray, 50, 150)
            edge_density = (np.sum(edges > 0) / (height * width)) * 100
            
            return {
                "image_dimensions": {"width": width, "height": height},
                "color_analysis": {
                    "green_percentage": round(green_percentage, 2),
                    "brown_percentage": round(brown_percentage, 2),
                    "yellow_percentage": round(yellow_percentage, 2)
                },
                "texture_analysis": {
                    "texture_score": round(float(texture_score), 2),
                    "edge_density": round(edge_density, 2)
                },
                "health_indicators": {
                    "plant_coverage": round(green_percentage, 2),
                    "stress_indicators": round(yellow_percentage, 2),
                    "soil_visibility": round(brown_percentage, 2)
                }
            }
            
        except Exception as e:
            return {"error": f"Error en análisis de imagen: {str(e)}"}
    
    def create_image_thumbnail(self, image_path: str, size: Tuple[int, int] = (200, 200)) -> str:
        """Crear thumbnail de la imagen"""
        try:
            with Image.open(image_path) as img:
                img.thumbnail(size, Image.Resampling.LANCZOS)
                thumbnail_path = image_path.replace(".", "_thumb.")
                img.save(thumbnail_path)
                return thumbnail_path
        except Exception as e:
            print(f"Error creando thumbnail: {e}")
            return image_path
    
    def encode_image_to_base64(self, image_path: str) -> str:
        """Convertir imagen a base64 para envío por WebSocket"""
        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                return encoded_string
        except Exception as e:
            print(f"Error codificando imagen: {e}")
            return ""
    
    def get_image_info(self, image_path: str) -> Dict[str, Any]:
        """Obtener información básica de la imagen"""
        try:
            with Image.open(image_path) as img:
                return {
                    "format": img.format,
                    "mode": img.mode,
                    "size": img.size,
                    "file_size": os.path.getsize(image_path)
                }
        except Exception as e:
            return {"error": f"Error obteniendo información: {str(e)}"}
    
    def cleanup_old_images(self, max_age_hours: int = 24):
        """Limpiar imágenes antiguas"""
        import time
        current_time = time.time()
        
        for filename in os.listdir(self.upload_dir):
            file_path = os.path.join(self.upload_dir, filename)
            if os.path.isfile(file_path):
                file_age = current_time - os.path.getmtime(file_path)
                if file_age > (max_age_hours * 3600):
                    try:
                        os.remove(file_path)
                        print(f"Imagen eliminada: {filename}")
                    except Exception as e:
                        print(f"Error eliminando {filename}: {e}")
