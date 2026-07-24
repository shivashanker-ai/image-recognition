"""
==========================================
Module 8 - Deep Learning with TensorFlow
Lesson 3 - Understanding Tensors
==========================================
"""

import tensorflow as tf

print("========== UNDERSTANDING TENSORS ==========\n")

# -----------------------------------------
# Scalar Tensor (0D)
# -----------------------------------------

scalar = tf.constant(100)

print("Scalar Tensor:")
print(scalar)
print("Shape:", scalar.shape)
print()

# -----------------------------------------
# Vector Tensor (1D)
# -----------------------------------------

vector = tf.constant([10, 20, 30, 40])

print("Vector Tensor:")
print(vector)
print("Shape:", vector.shape)
print()

# -----------------------------------------
# Matrix Tensor (2D)
# -----------------------------------------

matrix = tf.constant([
    [1, 2, 3],
    [4, 5, 6]
])

print("Matrix Tensor:")
print(matrix)
print("Shape:", matrix.shape)
print()

# -----------------------------------------
# 3D Tensor
# -----------------------------------------

tensor3d = tf.constant([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("3D Tensor:")
print(tensor3d)
print("Shape:", tensor3d.shape)
print()

print("AI Connection:")
print("Images, videos, and datasets are stored")
print("as tensors before they are processed")
print("by Deep Learning models.")

print()

print("Module 8 - Lesson 3 Completed Successfully!")