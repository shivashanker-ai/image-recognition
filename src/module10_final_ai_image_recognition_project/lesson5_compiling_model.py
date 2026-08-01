# ============================================================
# MODULE 10 - LESSON 5
# COMPILING THE MODEL
# ============================================================

# ------------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Input,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense
)

# ------------------------------------------------------------
# IMAGE SIZE
# ------------------------------------------------------------

IMAGE_SIZE = (150, 150)

# ------------------------------------------------------------
# BUILD CNN MODEL
# ------------------------------------------------------------

model = Sequential([

    Input(shape=(150, 150, 3)),

    Conv2D(
        filters=32,
        kernel_size=(3,3),
        activation="relu"
    ),

    MaxPooling2D(pool_size=(2,2)),

    Conv2D(
        filters=64,
        kernel_size=(3,3),
        activation="relu"
    ),

    MaxPooling2D(pool_size=(2,2)),

    Conv2D(
        filters=128,
        kernel_size=(3,3),
        activation="relu"
    ),

    MaxPooling2D(pool_size=(2,2)),

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
# COMPILE MODEL
# ------------------------------------------------------------

print("=" * 60)
print("               COMPILING MODEL")
print("=" * 60)

print("\nConfiguring Optimizer...")
print("Optimizer : Adam")

print("\nConfiguring Loss Function...")
print("Loss Function : Binary Crossentropy")

print("\nConfiguring Evaluation Metric...")
print("Metric : Accuracy")

model.compile(

    optimizer="adam",

    loss="binary_crossentropy",

    metrics=["accuracy"]

)

print("\nModel Compiled Successfully!")

# ------------------------------------------------------------
# COMPILE SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("MODEL CONFIGURATION")
print("=" * 60)

print(f"Optimizer      : Adam")
print(f"Loss Function  : Binary Crossentropy")
print(f"Metric         : Accuracy")

print("\nModel is Ready for Training!")

print("\nLesson 5 Completed Successfully!")