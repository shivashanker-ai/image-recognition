"""
==========================================
Module 9 - Convolutional Neural Networks
Lesson 2 - Convolution Layer
==========================================
"""

import tensorflow as tf

print("========== CONVOLUTION LAYER ==========\n")

# -----------------------------------------
# Create a Convolution Layer
# -----------------------------------------

convolution_layer = tf.keras.layers.Conv2D(
    filters=32,
    kernel_size=(3, 3),
    activation="relu",
    input_shape=(128, 128, 3)
)

print("Convolution Layer Created Successfully!")
print()

print("Layer Configuration:")
print(convolution_layer)
print()

print("AI Connection:")
print("The Convolution Layer scans")
print("an image using small filters")
print("to detect edges, textures,")
print("patterns, and shapes.")
print()

print("Module 9 - Lesson 2 Completed Successfully!")