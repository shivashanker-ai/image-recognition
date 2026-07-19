"""
==========================================
Module 5 - Image Transformations
Lesson 6 - Affine Transformation
==========================================
"""

import cv2
import numpy as np

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

rows, cols = image.shape[:2]

# Three points from original image
pts1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

# Three new points
pts2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

# Create affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply transformation
affine = cv2.warpAffine(image, matrix, (cols, rows))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformation", affine)

cv2.waitKey(0)
cv2.destroyAllWindows()