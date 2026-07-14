"""
==========================================
Module 1 - Image Fundamentals
Lesson 6 - Height, Width and Channels
==========================================
"""

import numpy as np

# Create a small RGB image
rgb_image = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 255, 255], [0, 0, 0]]
])

print("RGB Image:\n")
print(rgb_image)

print("\nImage Shape:", rgb_image.shape)

height = rgb_image.shape[0]
width = rgb_image.shape[1]
channels = rgb_image.shape[2]

print("\nHeight :", height)
print("Width  :", width)
print("Channels:", channels)

print("\nExplanation:")
print("Height  -> Number of rows")
print("Width   -> Number of columns")
print("Channels -> RGB = 3")