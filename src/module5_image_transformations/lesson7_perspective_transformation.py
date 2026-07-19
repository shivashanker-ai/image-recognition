"""
==========================================
Module 5 - Image Transformations
Lesson 7 - Perspective Transformation
==========================================
"""

import cv2
import numpy as np

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

height, width = image.shape[:2]

# Four points from original image
pts1 = np.float32([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
])

# Four new points
pts2 = np.float32([
    [20, 100],
    [280, 20],
    [80, 280],
    [320, 320]
])

# Create transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply transformation
perspective = cv2.warpPerspective(image, matrix, (width, height))

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()