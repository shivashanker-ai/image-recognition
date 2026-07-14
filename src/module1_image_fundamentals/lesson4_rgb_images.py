"""
==========================================
Module 1 - Image Fundamentals
Lesson 4 - RGB Images
==========================================
"""

import numpy as np

# Create RGB pixels

red = np.array([255, 0, 0])
green = np.array([0, 255, 0])
blue = np.array([0, 0, 255])
white = np.array([255, 255, 255])
black = np.array([0, 0, 0])

print("Red Pixel:", red)
print("Green Pixel:", green)
print("Blue Pixel:", blue)
print("White Pixel:", white)
print("Black Pixel:", black)

print("\nCreating a Small RGB Image")

rgb_image = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 255]]
])

print(rgb_image)

print("\nImage Shape:", rgb_image.shape)

print("\nHeight :", rgb_image.shape[0])
print("Width  :", rgb_image.shape[1])
print("Channels:", rgb_image.shape[2])

print("\nEach RGB pixel stores 3 values (Red, Green, Blue).")