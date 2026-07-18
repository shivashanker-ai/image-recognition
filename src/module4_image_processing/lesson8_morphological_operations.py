"""
==========================================
Module 4 - Image Processing
Lesson 8 - Morphological Operations
==========================================
"""

import cv2
import numpy as np

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Binary Threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Kernel
kernel = np.ones((5,5), np.uint8)

# Morphological Opening
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# Display Images
cv2.imshow("Binary Image", binary)
cv2.imshow("After Opening", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Lesson 8 Completed Successfully!")