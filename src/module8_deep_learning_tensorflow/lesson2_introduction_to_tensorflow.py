"""
==========================================
Module 8 - Deep Learning with TensorFlow
Lesson 2 - Introduction to TensorFlow
==========================================
"""

import tensorflow as tf

print("========== TENSORFLOW ==========\n")

# -----------------------------------------
# TensorFlow Version
# -----------------------------------------

print("TensorFlow Version:")
print(tf.__version__)

print()

# -----------------------------------------
# Create a Constant Tensor
# -----------------------------------------

tensor = tf.constant([10, 20, 30, 40, 50])

print("Tensor:")
print(tensor)

print()

# -----------------------------------------
# Tensor Shape
# -----------------------------------------

print("Tensor Shape:")
print(tensor.shape)

print()

# -----------------------------------------
# Tensor Data Type
# -----------------------------------------

print("Tensor Data Type:")
print(tensor.dtype)

print()

print("Real-World Applications:")
print("- Image Recognition")
print("- Face Detection")
print("- Self-Driving Cars")
print("- Medical AI")
print("- Speech Recognition")

print()

print("AI Connection:")
print("TensorFlow is one of the world's most")
print("popular Deep Learning frameworks used")
print("to build Neural Networks and AI models.")

print()

print("Module 8 - Lesson 2 Completed Successfully!")