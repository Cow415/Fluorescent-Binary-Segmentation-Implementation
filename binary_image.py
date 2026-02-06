# Converts processed grayscale images to binary mask arrays
# chuan134@jh.edu

"""
    Created on Jul 8 2025
    Author: Caoze Huang
    This module converts processed grayscale images into a binary mask
"""

from PIL import Image
import cv2
import os

def convert_to_binary(image_path, threshold=128, save_path="Barman_results"):
    """
    Convert a grayscale image to a binary mask using a specified threshold.
    
    Args:
        image_path (str): Path to the input grayscale image.
        threshold (int): Threshold value for binarization.
        
    Returns:
        binary_image_path (str.): Path to saved binary image.
    """
    # Load the grayscale image
    access_path = save_path + '/' + image_path 
    print(access_path)
    gray_image = cv2.imread(access_path, cv2.IMREAD_GRAYSCALE)
    if gray_image is None:
        raise ValueError("Image not found or unable to read.")
    
    # Apply thresholding to create a binary image
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    
    # Save the binary image 
    binary_image_path = image_path.replace('_gray.jpg', '_binary.jpg').replace('_gray.png', '_binary.png')
    full_path = os.path.join(save_path, binary_image_path)
    Image.fromarray(binary_image).save(full_path)
    print(f"Binary image saved to {full_path}")

    return binary_image_path