"""
==========================================
Module 9 - Convolutional Neural Networks
Lesson 4 - Activation Functions
==========================================
"""

import tensorflow as tf

print("========== ACTIVATION FUNCTIONS ==========\n")

# -----------------------------------------
# Create Activation Layers
# -----------------------------------------

relu_layer = tf.keras.layers.ReLU()

sigmoid_layer = tf.keras.layers.Activation("sigmoid")

softmax_layer = tf.keras.layers.Activation("softmax")

print("ReLU Layer:")
print(relu_layer)
print()

print("Sigmoid Layer:")
print(sigmoid_layer)
print()

print("Softmax Layer:")
print(softmax_layer)
print()

print("AI Connection:")
print("Activation Functions help")
print("Neural Networks learn")
print("complex patterns from data.")
print()

print("Module 9 - Lesson 4 Completed Successfully!")