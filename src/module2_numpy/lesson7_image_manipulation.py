"""
==========================================
Module 2 - NumPy for Computer Vision
Lesson 7 - Image Manipulation
==========================================
"""

import numpy as np

print("=== Image Manipulation ===\n")

# Create a sample image
image = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original Image:")
print(image)

# Horizontal Flip
horizontal = np.fliplr(image)

print("\nHorizontal Flip:")
print(horizontal)

# Vertical Flip
vertical = np.flipud(image)

print("\nVertical Flip:")
print(vertical)

# Rotate 90 Degrees Counterclockwise
rotated = np.rot90(image)

print("\nRotate 90°:")
print(rotated)

print("\nImage manipulation changes the position of pixels, not their values.")