"""
==========================================
Module 9 - Convolutional Neural Networks
Lesson 6 - Dense Layer
==========================================
"""

import tensorflow as tf

print("========== DENSE LAYER ==========\n")

# -----------------------------------------
# Create Dense Layers
# -----------------------------------------

hidden_layer = tf.keras.layers.Dense(
    units=128,
    activation="relu"
)

output_layer = tf.keras.layers.Dense(
    units=10,
    activation="softmax"
)

print("Hidden Dense Layer:")
print(hidden_layer)
print()

print("Output Dense Layer:")
print(output_layer)
print()

print("AI Connection:")
print("Dense Layers combine")
print("all extracted features")
print("and make the final")
print("classification decision.")
print()

print("Module 9 - Lesson 6 Completed Successfully!")