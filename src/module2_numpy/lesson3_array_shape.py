"""
==========================================
Module 2 - NumPy for Computer Vision
Lesson 3 - Understanding Array Shape
==========================================
"""

import numpy as np

print("=== Understanding Array Shape ===\n")

# Create a 3x4 array
image = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Array:\n")
print(image)

print("\nShape:", image.shape)
print("Rows (Height):", image.shape[0])
print("Columns (Width):", image.shape[1])

print("\nNumber of Dimensions:", image.ndim)
print("Total Elements:", image.size)

print("\nIn Computer Vision:")
print("Height = Rows")
print("Width = Columns")