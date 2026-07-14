"""
==========================================
Module 2 - NumPy for Computer Vision
Lesson 1 - Introduction to NumPy
==========================================
"""

import numpy as np

print("=== Introduction to NumPy ===\n")

# Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50])

print("NumPy Array:")
print(numbers)

print("\nType:")
print(type(numbers))

print("\nNumber of Dimensions:")
print(numbers.ndim)

print("\nShape:")
print(numbers.shape)

print("\nSize:")
print(numbers.size)

print("\nData Type:")
print(numbers.dtype)

print("\nWhy NumPy?")
print("- Faster than Python lists")
print("- Uses less memory")
print("- Supports mathematical operations")
print("- Used by TensorFlow and OpenCV")