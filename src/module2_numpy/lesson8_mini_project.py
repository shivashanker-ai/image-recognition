"""
==========================================
Module 2 - NumPy for Computer Vision
Lesson 8 - Mini Project
Image Transformation Simulator
==========================================
"""

import numpy as np

print("=== Mini Project: Image Transformation Simulator ===\n")

# Step 1: Create a grayscale image
image = np.array([
    [20, 40, 60, 80],
    [100, 120, 140, 160],
    [180, 200, 220, 240],
    [30, 50, 70, 90]
])

print("Original Image:")
print(image)

# Step 2: Image Shape
print("\nShape:", image.shape)

# Step 3: Access a pixel
print("\nPixel at Row 1 Column 2:", image[1, 2])

# Step 4: Crop the center
cropped = image[1:3, 1:3]

print("\nCropped Image:")
print(cropped)

# Step 5: Increase brightness
bright = np.clip(cropped + 30, 0, 255)

print("\nBrightness Increased:")
print(bright)

# Step 6: Horizontal Flip
flip = np.fliplr(bright)

print("\nHorizontal Flip:")
print(flip)

# Step 7: Rotate 90 Degrees
rotated = np.rot90(flip)

print("\nRotated Image:")
print(rotated)

print("\nMini Project Completed Successfully!")