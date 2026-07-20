"""
==========================================
Module 6 - Image Filtering
Lesson 2 - Convolution (Kernel)
==========================================
"""

import cv2
import numpy as np

# Load the image
image = cv2.imread("dataset/flower.jpg")

# Create an Identity Kernel
kernel = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
], dtype=np.float32)

# Apply Convolution
filtered_image = cv2.filter2D(image, -1, kernel)

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Convolution Output", filtered_image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print("Module 6 - Lesson 2 Completed Successfully!")