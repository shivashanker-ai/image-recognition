"""
==========================================
Module 1 - Image Fundamentals
Lesson 8 - NumPy Bridge
==========================================
"""

import numpy as np

# Python List

image_list = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Python List:")
print(image_list)

# Convert list into NumPy array

image = np.array(image_list)

print("\nNumPy Array:")
print(image)

print("\nType:", type(image))

print("\nShape:", image.shape)

print("\nRows:", image.shape[0])
print("Columns:", image.shape[1])

print("\nWhy NumPy?")
print("- Fast computations")
print("- Easy image manipulation")
print("- Used by TensorFlow, OpenCV and other AI libraries")
