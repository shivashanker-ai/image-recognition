"""
==========================================
Module 1 - Image Fundamentals
Lesson 3 - Pixel Values
==========================================
"""

import numpy as np

# Create a grayscale image
image = np.array([
    [0, 50, 100],
    [150, 200, 255],
    [25, 125, 225]
])

print("Image:\n")
print(image)

print("\nAccessing Individual Pixels")

print("Pixel at (0,0):", image[0, 0])
print("Pixel at (1,2):", image[1, 2])
print("Pixel at (2,1):", image[2, 1])

print("\nChanging Pixel Values")

image[0, 0] = 255
image[2, 2] = 0

print(image)

print("\nA pixel value can be read and modified using indexing.")