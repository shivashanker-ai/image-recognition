"""
==========================================
Module 8 - Deep Learning with TensorFlow
Lesson 7 - Building Your First Neural Network
==========================================
"""

import tensorflow as tf

print("========== FIRST NEURAL NETWORK ==========\n")

# -----------------------------------------
# Build Neural Network
# -----------------------------------------

model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation="relu", input_shape=(4,)),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax")
])

# -----------------------------------------
# Display Model Summary
# -----------------------------------------

model.summary()

print()

print("AI Connection:")
print("This Neural Network is the foundation")
print("of Deep Learning models. More advanced")
print("networks like CNNs are built using")
print("similar layers.")

print()

print("Module 8 - Lesson 7 Completed Successfully!")