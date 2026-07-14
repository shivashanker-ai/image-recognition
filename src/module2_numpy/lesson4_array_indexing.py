"""
==========================================
Module 2 - NumPy for Computer Vision
Lesson 4 - Array Indexing
==========================================
"""

import numpy as np

print("=== Array Indexing ===\n")

image = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Image:\n")
print(image)

print("\nAccessing Individual Elements")

print("Top Left:", image[0, 0])
print("Center:", image[1, 1])
print("Bottom Right:", image[2, 2])

print("\nUpdating Pixel Values")

image[0, 0] = 255
image[2, 2] = 0

print(image)

print("\nIndexing allows us to read and modify any pixel.")