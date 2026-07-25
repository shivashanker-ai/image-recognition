"""
==========================================
Module 9 - Convolutional Neural Networks
Lesson 5 - Flatten Layer
==========================================
"""

import tensorflow as tf

print("========== FLATTEN LAYER ==========\n")

# -----------------------------------------
# Create a Flatten Layer
# -----------------------------------------

flatten_layer = tf.keras.layers.Flatten()

print("Flatten Layer Created Successfully!")
print()

print("Layer Configuration:")
print(flatten_layer)
print()

print("AI Connection:")
print("The Flatten Layer converts")
print("multi-dimensional feature")
print("maps into a one-dimensional")
print("vector for classification.")
print()

print("Module 9 - Lesson 5 Completed Successfully!")