"""
==========================================
Module 5 - Image Transformations
Lesson 2 - Image Resizing
==========================================
"""

import cv2

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Resize image
resized = cv2.resize(image, (400, 300))

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()