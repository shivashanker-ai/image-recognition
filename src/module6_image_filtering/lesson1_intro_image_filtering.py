"""
==========================================
Module 6 - Image Filtering
Lesson 1 - Introduction to Image Filtering
==========================================
"""

print("========== IMAGE FILTERING ==========\n")

# -----------------------------------------
# What is Image Filtering?
# -----------------------------------------

print("Definition:")
print("Image Filtering is the process of improving")
print("or modifying an image before it is analyzed.")
print()

print("Why is it Important?")
print("- Remove noise")
print("- Improve image quality")
print("- Highlight important features")
print("- Prepare images for AI")
print()

print("Real-World Applications:")
print("- Face Recognition")
print("- Self-Driving Cars")
print("- OCR")
print("- Medical Imaging")
print()

# -----------------------------------------
# Practical Example
# -----------------------------------------

import cv2

# Load image
image = cv2.imread("dataset/flower.jpg")

# Display image
cv2.imshow("Original Image", image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

# -----------------------------------------
# AI Connection
# -----------------------------------------

print("\nAI Connection:")
print("Filtering improves image quality before")
print("AI models perform prediction.")

print("\nLesson 1 Completed Successfully!")