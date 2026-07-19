"""
==========================================
Module 5 Mini Project
Image Transformation Studio
==========================================
"""

import cv2
import numpy as np

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Image not found!")
    exit()

height, width = image.shape[:2]

# Resize
resized = cv2.resize(image, (400, 300))

# Rotate
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Translation
tx = 80
ty = 50

M = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])

translated = cv2.warpAffine(image, M, (width, height))

# Flip
flipped = cv2.flip(image, 1)

# Affine Transformation
pts1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

pts2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

affine_matrix = cv2.getAffineTransform(pts1, pts2)

affine = cv2.warpAffine(image, affine_matrix, (width, height))

# Perspective Transformation
pts1 = np.float32([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
])

pts2 = np.float32([
    [20, 100],
    [280, 20],
    [80, 280],
    [320, 320]
])

perspective_matrix = cv2.getPerspectiveTransform(pts1, pts2)

perspective = cv2.warpPerspective(image, perspective_matrix, (width, height))

# Display all images
cv2.imshow("Original", image)
cv2.imshow("Resized", resized)
cv2.imshow("Rotated", rotated)
cv2.imshow("Translated", translated)
cv2.imshow("Flipped", flipped)
cv2.imshow("Affine", affine)
cv2.imshow("Perspective", perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()