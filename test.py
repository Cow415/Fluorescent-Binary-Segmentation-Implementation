# Tests functions by calling on them in this script
# Deletable after verification

import grayscale_image as gi
import binary_image as bi

import caller

result = bi.convert_to_binary('fluorescent_image_gray.png', threshold=50, save_path='fluorescent_image_results')
print(result)