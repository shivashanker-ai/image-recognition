"""
==========================================
Module 6 - Image Filtering
Lesson 3 - Averaging Filter
==========================================
"""

import cv2
import numpy as np

# Load the image
image = cv2.imread("dataset/flower.jpg")

# Create a 3x3 Averaging Kernel
kernel = np.ones((3, 3), dtype=np.float32) / 9

# Apply the Averaging Filter
filtered_image = cv2.filter2D(image, -1, kernel)

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Averaging Filter", filtered_image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print("Module 6 - Lesson 3 Completed Successfully!")