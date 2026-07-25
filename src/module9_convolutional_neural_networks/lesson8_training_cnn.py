"""
==========================================
Module 9 - Convolutional Neural Networks
Lesson 8 - Training a CNN
==========================================
"""

import tensorflow as tf

print("========== TRAINING A CNN ==========\n")

# -----------------------------------------
# Build CNN Model
# -----------------------------------------

model = tf.keras.Sequential([

    tf.keras.layers.Input(shape=(128, 128, 3)),

    tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D((2, 2)),

    tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D((2, 2)),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(128, activation="relu"),

    tf.keras.layers.Dense(10, activation="softmax")

])

# -----------------------------------------
# Compile the Model
# -----------------------------------------

model.compile(

    optimizer="adam",

    loss="sparse_categorical_crossentropy",

    metrics=["accuracy"]

)

print("CNN Model Compiled Successfully!\n")

print("Model Summary:\n")
model.summary()

print("\nReady for Training!")
print("\nModule 9 - Lesson 8 Completed Successfully!")