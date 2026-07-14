"""
==========================================
Module 1 - Image Fundamentals
Lesson 2 - Grayscale Images
==========================================
"""

import numpy as np

# Create a small grayscale image

grayscale_image = np.array([
    [0, 50, 100],
    [150, 200, 255],
    [30, 120, 220]
])

print("Grayscale Image:\n")
print(grayscale_image)

print("\nImage Shape:", grayscale_image.shape)

print("\nImage Size:", grayscale_image.size)

print("\nNumber of Dimensions:", grayscale_image.ndim)

print("\nPixel Values")

for row in grayscale_image:
    for pixel in row:
        print(pixel, end=" ")
    print()

print("\nEvery grayscale pixel contains ONE value (0-255).")