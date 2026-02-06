# Grayscale Image Conversion Module + Pipelines
# chuan134@jh.edu

"""
    Created on Jul 8 2025
    Author: Caoze Huang 
    This module provides the functionality to convert images to 
grayscale and apply various image processing techniques.
"""

from PIL import Image
import cv2
import os

def pipeline_process(image_path, save_path="Barman_results"):
    """
    Pipeline to convert an image to grayscale and save it.
    
    Args:
        image_path (str): Path to the input image.
        save_path (str): Directory to the subfolder to save the grayscale image.
    Returns:
        gray_image_path (str): Path to the saved grayscale image.
            
    """
    # Pipeline
    # Original RGB Image
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not found or unable to read.")
    except Exception as e:
        print(f"Error reading image {image_path}: {e}")
        return None
    
    #Split Channels (R,G,B)
    b, g, r = cv2.split(img)
        
    #Green Enhancement (G - 0.5R - 0.5B)
    green_enhanced = cv2.subtract(g, cv2.addWeighted(r, 0.5, b, 0.5, 0))

    # Normalize Intensities (0-255)
    green_norm = cv2.normalize(green_enhanced, None, 0, 255, cv2.NORM_MINMAX)
        
    # Contrast Enhancement (CLAHE)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    contrast_enhanced = clahe.apply(green_norm)
        
    # Grayscale Output (Green stands out)
    gray_image = contrast_enhanced

    # Save the grayscale image to subfolder
    gray_image_path = image_path.replace('.jpg', '_gray.jpg').replace('.png', '_gray.png')
    full_path = os.path.join(save_path, gray_image_path)
    Image.fromarray(gray_image).save(full_path)
    print(f"Grayscale image saved to {full_path}")
    return gray_image_path