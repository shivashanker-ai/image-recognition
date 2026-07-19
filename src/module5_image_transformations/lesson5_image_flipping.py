"""
==========================================
Module 5 - Image Transformations
Lesson 5 - Image Flipping
==========================================
"""

import cv2

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Flip horizontally
horizontal = cv2.flip(image, 1)

# Flip vertically
vertical = cv2.flip(image, 0)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Horizontal Flip", horizontal)
cv2.imshow("Vertical Flip", vertical)

cv2.waitKey(0)
cv2.destroyAllWindows()