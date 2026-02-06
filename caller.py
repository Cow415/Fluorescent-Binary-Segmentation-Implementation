# Main interaction file to call functions from other modules
# chuan134@jh.edu

"""
    Created on Jul 8 2025
    Author: Caoze Huang 
    Runs the whole packages, requires user inputs
    Creates subfolders to store intermediate results
"""

import cv2
import os
import grayscale_image as gi
import binary_image as bi
import quantification as qt
import image_segmentation as seg
import measure_convert as mc

# Main script to run the image processing pipelines
def main(image_path, threshold=128, dpi=300, zoom_value=1.0, unit='mm', min_size=50):
    # Create necessary folders
    subfolder_name = create_folder(image_path)
    
    # Measurement Conversion
    pixel_size, area_unit = mc.main(dpi, zoom_value, unit) 
    print(f"Pixel size: {pixel_size} {unit}, Area unit: {area_unit}")    

    # Grayscale Conversion
    gray_image = gi.pipeline_process(image_path, subfolder_name)
    
    # Binary Conversion
    binary_image = bi.convert_to_binary(gray_image, threshold, subfolder_name)
    print(f"Binary image saved at: {subfolder_name}/{binary_image}")
    # Image Segmentation
    segmented_data = seg.segment_image(binary_image, min_size, subfolder_name)
    print(f"Segmented {len(segmented_data)} droplets.")
    print(f"Droplet areas (in pixels): {segmented_data}")                 ### To be discussed/Review later

    # Quantification
    qt.process_and_save(segmented_data, pixel_size, area_unit, subfolder_name)
    print("Quantification completed.")

    # Final statement
    print("Ready to export folder.")
    print("Unit of measurement:" + area_unit)

    complete_statement = "Segmentation completed; results saved in " + subfolder_name
    return complete_statement

# Supplementary function to create folders for results
def create_folder(image_path='Barman'):
    """
    Create necessary folders to store intermediate and final results.
    """
    
    # Subfolder name(image.jpg -> image_results)
    basename = os.path.basename(image_path).removesuffix('.png').removesuffix('.jpg')
    subfolder_name = os.path.splitext(basename)[0].__add__('_results')
    try: 
        os.makedirs(subfolder_name, exist_ok=True)
        print(f"Created folder: {subfolder_name}")
    except Exception as e:
        print(f"Error creating folder {subfolder_name}: {e}")
    return subfolder_name

if __name__ == "__main__":
    # Example usage
    image_path = 'fluorescent_image.png'  # Replace with your image path
    result = main(image_path, threshold=50, dpi=100, zoom_value=1.0, unit='mum')
    print(result)