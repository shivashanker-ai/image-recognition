"""
==========================================
Module 9 - Convolutional Neural Networks
Lesson 9 - Image Classification
==========================================
"""

import tensorflow as tf
import numpy as np

print("========== IMAGE CLASSIFICATION ==========\n")

# -----------------------------------------
# Build CNN Model
# -----------------------------------------

model = tf.keras.Sequential([

    tf.keras.layers.Input(shape=(128, 128, 3)),

    tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),

    tf.keras.layers.MaxPooling2D((2, 2)),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(128, activation="relu"),

    tf.keras.layers.Dense(5, activation="softmax")

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

# -----------------------------------------
# Create a Dummy Image
# -----------------------------------------

image = np.random.rand(1, 128, 128, 3)

print("Input Image Shape:")

print(image.shape)

print()

# -----------------------------------------
# Predict
# -----------------------------------------

prediction = model.predict(image)

print("Prediction Shape:")

print(prediction.shape)

print()

# -----------------------------------------
# Class Names
# -----------------------------------------

classes = [
    "Cat",
    "Dog",
    "Flower",
    "Car",
    "Bird"
]

predicted_index = np.argmax(prediction)

print("Predicted Class:")

print(classes[predicted_index])

print()

print("Prediction Probabilities:")

print(prediction)

print()

print("Module 9 - Lesson 9 Completed Successfully!")