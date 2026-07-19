"""
==========================================
Module 5 - Image Transformations
Lesson 3 - Image Rotation
==========================================
"""

import cv2

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Rotate image by 90 degrees clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()