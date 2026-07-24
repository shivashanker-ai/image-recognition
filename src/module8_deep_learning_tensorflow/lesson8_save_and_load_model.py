"""
==========================================
Module 8 - Deep Learning with TensorFlow
Lesson 8 - Saving and Loading a Model
==========================================
"""

import tensorflow as tf

print("========== SAVE & LOAD MODEL ==========\n")

# -----------------------------------------
# Build Neural Network
# -----------------------------------------

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax")
])

# -----------------------------------------
# Save Model
# -----------------------------------------

model.save("my_first_model.keras")

print("Model Saved Successfully!")
print()

# -----------------------------------------
# Load Model
# -----------------------------------------

loaded_model = tf.keras.models.load_model("my_first_model.keras")

print("Model Loaded Successfully!")
print()

# -----------------------------------------
# Display Model Summary
# -----------------------------------------

loaded_model.summary()

print()

print("AI Connection:")
print("Trained AI models are saved so they")
print("can be reused without training again.")
print("This is how real-world AI applications")
print("deploy models into production.")

print()

print("Module 8 - Lesson 8 Completed Successfully!")