"""
==========================================
Module 2 - NumPy for Computer Vision
Lesson 6 - Mathematical Operations
==========================================
"""

import numpy as np

print("=== Mathematical Operations ===\n")

image = np.array([
    [20, 40, 60],
    [80, 100, 120],
    [140, 160, 180]
])

print("Original Image:\n")
print(image)

# Increase brightness
bright = image + 30

print("\nBrightness Increased:")
print(bright)

# Decrease brightness
dark = image - 20

print("\nBrightness Decreased:")
print(dark)

# Multiply pixel values
contrast = image * 2

print("\nContrast Increased:")
print(contrast)

# Keep pixel values between 0 and 255
safe_image = np.clip(contrast, 0, 255)

print("\nAfter Clipping (0-255):")
print(safe_image)

print("\nNumPy makes mathematical operations on images very easy.")
