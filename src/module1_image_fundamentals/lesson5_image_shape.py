"""
==========================================
Module 1 - Image Fundamentals
Lesson 5 - Image Shape
==========================================
"""

import numpy as np

# Create a grayscale image
image = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Image:\n")
print(image)

print("\nImage Shape:", image.shape)

height = image.shape[0]
width = image.shape[1]

print("Height:", height)
print("Width:", width)

print("\nAn image shape tells us the dimensions of the image.")