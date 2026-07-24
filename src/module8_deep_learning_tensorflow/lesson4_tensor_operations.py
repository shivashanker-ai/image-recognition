"""
==========================================
Module 8 - Deep Learning with TensorFlow
Lesson 4 - Tensor Operations
==========================================
"""

import tensorflow as tf

print("========== TENSOR OPERATIONS ==========\n")

# -----------------------------------------
# Create Two Tensors
# -----------------------------------------

tensor1 = tf.constant([10, 20, 30])

tensor2 = tf.constant([1, 2, 3])

print("Tensor 1:")
print(tensor1)
print()

print("Tensor 2:")
print(tensor2)
print()

# -----------------------------------------
# Addition
# -----------------------------------------

addition = tf.add(tensor1, tensor2)

print("Addition:")
print(addition)
print()

# -----------------------------------------
# Subtraction
# -----------------------------------------

subtraction = tf.subtract(tensor1, tensor2)

print("Subtraction:")
print(subtraction)
print()

# -----------------------------------------
# Multiplication
# -----------------------------------------

multiplication = tf.multiply(tensor1, tensor2)

print("Multiplication:")
print(multiplication)
print()

# -----------------------------------------
# Division
# -----------------------------------------

division = tf.divide(tensor1, tensor2)

print("Division:")
print(division)
print()

print("AI Connection:")
print("Tensor operations are used during")
print("training to calculate predictions,")
print("loss values, and update neural")
print("network weights.")

print()

print("Module 8 - Lesson 4 Completed Successfully!")