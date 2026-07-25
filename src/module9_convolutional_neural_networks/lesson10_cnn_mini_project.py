"""
==========================================
Module 9 - Convolutional Neural Networks
Lesson 10 - CNN Mini Project
==========================================
"""

import tensorflow as tf
import numpy as np

print("========== CNN MINI PROJECT ==========\n")

# -----------------------------------------
# Build CNN Model
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

    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Second Convolution Block
    tf.keras.layers.Conv2D(
        filters=64,
        kernel_size=(3, 3),
        activation="relu"
    ),

    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Flatten
    tf.keras.layers.Flatten(),

    # Hidden Dense Layer
    tf.keras.layers.Dense(
        units=128,
        activation="relu"
    ),

    # Output Layer
    tf.keras.layers.Dense(
        units=5,
        activation="softmax"
    )

])

# -----------------------------------------
# Compile Model
# -----------------------------------------

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("CNN Model Created Successfully!\n")

print("Model Summary:\n")
model.summary()

# -----------------------------------------
# Create Dummy Image
# -----------------------------------------

image = np.random.rand(1, 128, 128, 3)

print("\nInput Image Shape:")
print(image.shape)

# -----------------------------------------
# Predict
# -----------------------------------------

prediction = model.predict(image)

classes = [
    "Cat",
    "Dog",
    "Flower",
    "Car",
    "Bird"
]

predicted_index = np.argmax(prediction)

print("\nPrediction Probabilities:")
print(prediction)

print("\nPredicted Class:")
print(classes[predicted_index])

print("\nModule 9 - CNN Mini Project Completed Successfully!")