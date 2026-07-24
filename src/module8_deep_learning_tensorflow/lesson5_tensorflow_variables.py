"""
==========================================
Module 8 - Deep Learning with TensorFlow
Lesson 5 - TensorFlow Variables
==========================================
"""

import tensorflow as tf

print("========== TENSORFLOW VARIABLES ==========\n")

# -----------------------------------------
# Create a Variable
# -----------------------------------------

variable = tf.Variable([10, 20, 30])

print("Original Variable:")
print(variable)
print()

# -----------------------------------------
# Update Variable
# -----------------------------------------

variable.assign([100, 200, 300])

print("Updated Variable:")
print(variable)
print()

# -----------------------------------------
# Add to Variable
# -----------------------------------------

variable.assign_add([10, 10, 10])

print("After assign_add():")
print(variable)
print()

# -----------------------------------------
# Subtract from Variable
# -----------------------------------------

variable.assign_sub([20, 20, 20])

print("After assign_sub():")
print(variable)
print()

print("AI Connection:")
print("TensorFlow Variables store the")
print("weights and biases of Neural")
print("Networks. During training,")
print("these values are continuously")
print("updated to improve predictions.")

print()

print("Module 8 - Lesson 5 Completed Successfully!")