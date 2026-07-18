"""
==========================================
Module 4 - Image Processing
Lesson 7 - Image Sharpening
==========================================
"""

import cv2
import numpy as np

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Sharpening Kernel
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Apply Sharpening
sharpened = cv2.filter2D(image, -1, kernel)

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Lesson 7 Completed Successfully!")