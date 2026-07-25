"""
==========================================
Module 9 - Convolutional Neural Networks
Lesson 3 - Pooling Layer
==========================================
"""

import tensorflow as tf

print("========== POOLING LAYER ==========\n")

# -----------------------------------------
# Create a Max Pooling Layer
# -----------------------------------------

pooling_layer = tf.keras.layers.MaxPooling2D(
    pool_size=(2, 2),
    strides=2
)

print("Max Pooling Layer Created Successfully!")
print()

print("Layer Configuration:")
print(pooling_layer)
print()

print("AI Connection:")
print("The Pooling Layer reduces")
print("the size of feature maps")
print("while preserving the most")
print("important information.")
print()

print("Module 9 - Lesson 3 Completed Successfully!")