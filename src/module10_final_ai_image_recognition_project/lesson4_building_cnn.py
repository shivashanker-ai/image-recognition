# ============================================================
# MODULE 10 - LESSON 4
# BUILDING CNN
# ============================================================

# ------------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import (
    Input,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense
)

# ------------------------------------------------------------
# MODEL CONFIGURATION
# ------------------------------------------------------------

IMAGE_SIZE = (150, 150)

# ------------------------------------------------------------
# DISPLAY PROJECT INFORMATION
# ------------------------------------------------------------

print("=" * 60)
print("                BUILDING CNN")
print("=" * 60)

print("\nCreating Convolutional Neural Network...")

# ------------------------------------------------------------
# BUILD CNN MODEL
# ------------------------------------------------------------

model = Sequential([

    Input(shape=(150, 150, 3)),

    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        activation="relu"
    ),

    MaxPooling2D(
        pool_size=(2, 2)
    ),

    Conv2D(
        filters=64,
        kernel_size=(3, 3),
        activation="relu"
    ),

    MaxPooling2D(
        pool_size=(2, 2)
    ),

    Conv2D(
        filters=128,
        kernel_size=(3, 3),
        activation="relu"
    ),

    MaxPooling2D(
        pool_size=(2, 2)
    ),

    Flatten(),

    Dense(
        units=128,
        activation="relu"
    ),

    Dense(
        units=1,
        activation="sigmoid"
    )

])

# ------------------------------------------------------------
# MODEL SUMMARY
# ------------------------------------------------------------

print("\nCNN Created Successfully!")

print("\n" + "=" * 60)
print("MODEL SUMMARY")
print("=" * 60)

model.summary()

print("\nInput Image Size :", IMAGE_SIZE)
print("Output Classes   : 2")
print("Output Layer     : Sigmoid")

print("\nLesson 4 Completed Successfully!")