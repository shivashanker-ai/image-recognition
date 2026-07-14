"""
==========================================
Module 2 - NumPy for Computer Vision
Lesson 2 - Creating NumPy Arrays
==========================================
"""

import numpy as np

print("=== Creating NumPy Arrays ===\n")

# 1D Array
array1 = np.array([1, 2, 3, 4, 5])

print("1D Array:")
print(array1)

# 2D Array
array2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(array2)

# Array of zeros
zeros = np.zeros((3, 3))

print("\nArray of Zeros:")
print(zeros)

# Array of ones
ones = np.ones((2, 4))

print("\nArray of Ones:")
print(ones)

# Identity Matrix
identity = np.eye(3)

print("\nIdentity Matrix:")
print(identity)

print("\nSummary")
print("np.array() -> Create an array")
print("np.zeros() -> Create zeros")
print("np.ones() -> Create ones")
print("np.eye() -> Create identity matrix")