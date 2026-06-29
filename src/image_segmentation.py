# Segments binary mask into an array of pixel sizes
# chuan134@j.edu

""" 
    Created on Jul 8 2025
    Author: Caoze Huang
    This module provides functions to segment binary masks
"""
import numpy as np
import cv2
from skimage import measure, morphology
from skimage.measure import label, regionprops

# Segmentation function
# Extracts numbers of droplets and the numbers of pixels in each droplet
def segment_image(binary_image, min_size=50, save_path="Barman_results"):
    """
    Segments the binary image to identify individual droplets.
    Parameters:
        binary_image (ndarray): The binary image to be segmented.
        min_size (int): Minimum size of droplets to keep.
    Returns:
        data_array (list): List of areas of each droplet.
    """
    # Declare results array, 
    sizes_array = []

    # Opens the binary image as a NumPy array of boolean type
    access_path = save_path + '/' + binary_image 
    print(f"Accessing binary image at: {access_path}")
    print(access_path)
    binary_image_array = cv2.imread(access_path, cv2.IMREAD_GRAYSCALE).astype(bool)
    if binary_image_array is None:
        raise ValueError("Binary image not found or unable to read.")

    # Label connected components
    labeled_image = label(binary_image)
    
    # Remove small objects
    cleaned_image = morphology.remove_small_objects(labeled_image, min_size=min_size)
    regions = regionprops(cleaned_image)
    print("Droplets labeled and small objects removed.")

    # Extract area of each region in pixels
    for region in regions:
        sizes_array.append(region.area)    

    print(f"Identified {len(sizes_array)} droplets after removing small objects.")
    return sizes_array