"""
==========================================
Module 1 - Image Fundamentals
Lesson 7 - Image as a Matrix
==========================================
"""

import numpy as np

# A grayscale image represented as a matrix

image = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("Image Matrix:\n")
print(image)

print("\nRows :", image.shape[0])
print("Columns :", image.shape[1])

print("\nAccessing Pixels")

print("Top Left :", image[0, 0])
print("Top Right :", image[0, 3])
print("Bottom Left :", image[3, 0])
print("Bottom Right :", image[3, 3])

print("\nEvery image is simply a matrix of pixel values.")