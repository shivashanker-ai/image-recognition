"""
==========================================
Module 9 - Convolutional Neural Networks
Lesson 7 - CNN Architecture
==========================================
"""

import tensorflow as tf

print("========== CNN ARCHITECTURE ==========\n")

# -----------------------------------------
# Build Complete CNN Architecture
# -----------------------------------------

model = tf.keras.Sequential([

    # Input Layer
    tf.keras.layers.Input(shape=(128, 128, 3)),

    # First Convolution Block
    tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        activation="relu"
    ),

    tf.keras.layers.MaxPooling2D(
        pool_size=(2, 2)
    ),

    # Second Convolution Block
    tf.keras.layers.Conv2D(
        filters=64,
        kernel_size=(3, 3),
        activation="relu"
    ),

    tf.keras.layers.MaxPooling2D(
        pool_size=(2, 2)
    ),

    # Classification Part
    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(
        units=128,
        activation="relu"
    ),

    tf.keras.layers.Dense(
        units=10,
        activation="softmax"
    )

])

print("CNN Architecture Created Successfully!\n")

print("Model Summary:\n")

model.summary()

print("\nModule 9 - Lesson 7 Completed Successfully!")