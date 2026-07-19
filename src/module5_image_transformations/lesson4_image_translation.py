"""
==========================================
Module 5 - Image Transformations
Lesson 4 - Image Translation
==========================================
"""

import cv2
import numpy as np

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Translation values
tx = 100   # Move right
ty = 50    # Move down

# Translation matrix
M = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])

# Apply translation
translated = cv2.warpAffine(
    image,
    M,
    (image.shape[1], image.shape[0])
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Translated Image", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()