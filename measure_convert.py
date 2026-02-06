# Converts among distances and areas in images
# chuan134@jh.edu

"""
    Created on Jul 8 2025
    Author: Caoze Huang
    This module provides functions to convert distances and areas in images
"""
# Main functions to convert distances and areas
def main(dpi=300, zoom_value=1.0, unit='mm'):
    
    if unit == 'mum' :             # Micrometer
        area_unit = 'mum^2' 
    elif unit == 'cm' :            # Centimeter
        area_unit = 'cm^2'
    elif unit == 'inch' :          # Inch
        area_unit = 'inch^2'
    else:
        area_unit = 'mm^2'      # Assumes area is in square millimeters by default
    
    pixel_size = calculate_dpi(dpi) / zoom_value
    pixel_area = calculate_area(pixel_size)
    
    return pixel_area, area_unit


# Supplementary functions to calculate distance and area of each pixel
def calculate_area(pixel_size):
    """
    Calculate the area of each pixel based on DPI.
    """
    area = pixel_size ** 2  # Area
    return area

def calculate_dpi(dpi):
    """
    Calculate the pixel size based on DPI.
    """
    pixel_size = 25.4 / dpi  # Convert DPI to mm
    return pixel_size