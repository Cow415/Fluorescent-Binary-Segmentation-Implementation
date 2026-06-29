# Process output array and produce a csv file
# chuan134@jh.edu

""" 
    Created on Jul 8 2025
    Author: Caoze Huang
    This module provides functions to quantify segmented droplets
"""

import numpy as np
import pandas as pd

# Main function to process segmented data and save to csv
def process_and_save(segmented_data, pixel_size, area_unit, output_path):
    """
    Process the segmented data and save the results to a CSV file.
    Parameters:
        segmented_data (list): List of areas of each droplet in pixels.
        area (float): Area per pixel in mm^2.
        output_path (str): Path to save the output CSV file.
    """
    # Convert pixel areas to real-world areas
    real_world_areas = [pixels * pixel_size for pixels in segmented_data]
    
    # Create a DataFrame to store results
    df = pd.DataFrame({
        'Droplet_ID': range(1, len(segmented_data) + 1),
        'Area_in_Pixels': segmented_data,
        'Area_in_' + area_unit: real_world_areas
    })
    
    # Save DataFrame to CSV
    df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")
    fin_statement = "CSV Output completed"
    
    return fin_statement