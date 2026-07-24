"""
==========================================
Module 8 - Deep Learning with TensorFlow
Lesson 6 - TensorFlow Mathematical Operations
==========================================
"""

import tensorflow as tf

print("========== TENSORFLOW MATHEMATICAL OPERATIONS ==========\n")

# -----------------------------------------
# Create a Tensor
# -----------------------------------------

tensor = tf.constant([4.0, 9.0, 16.0, 25.0])

print("Original Tensor:")
print(tensor)
print()

# -----------------------------------------
# Square Root
# -----------------------------------------

sqrt_tensor = tf.sqrt(tensor)

print("Square Root:")
print(sqrt_tensor)
print()

# -----------------------------------------
# Square
# -----------------------------------------

square_tensor = tf.square(tensor)

print("Square:")
print(square_tensor)
print()

# -----------------------------------------
# Reduce Sum
# -----------------------------------------

sum_tensor = tf.reduce_sum(tensor)

print("Sum of Elements:")
print(sum_tensor)
print()

# -----------------------------------------
# Reduce Mean
# -----------------------------------------

mean_tensor = tf.reduce_mean(tensor)

print("Mean of Elements:")
print(mean_tensor)
print()

# -----------------------------------------
# Maximum Value
# -----------------------------------------

max_tensor = tf.reduce_max(tensor)

print("Maximum Value:")
print(max_tensor)
print()

# -----------------------------------------
# Minimum Value
# -----------------------------------------

min_tensor = tf.reduce_min(tensor)

print("Minimum Value:")
print(min_tensor)
print()

print("AI Connection:")
print("TensorFlow mathematical operations")
print("are used during model training to")
print("calculate loss, averages, and")
print("evaluate predictions.")

print()

print("Module 8 - Lesson 6 Completed Successfully!")