"""
==========================================
Module 2 - NumPy for Computer Vision
Lesson 5 - Array Slicing
==========================================
"""

import numpy as np

print("=== Array Slicing ===\n")

# Create a 4x4 image
image = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("Original Image:\n")
print(image)

# Extract first two rows
print("\nFirst Two Rows:")
print(image[0:2])

# Extract first two columns
print("\nFirst Two Columns:")
print(image[:, 0:2])

# Extract center 2x2 region
center = image[1:3, 1:3]

print("\nCenter Region:")
print(center)

print("\nArray slicing is used to crop images in Computer Vision.")