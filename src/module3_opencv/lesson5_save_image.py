"""
==========================================
Module 3 - OpenCV Basics
Lesson 5 - Saving Images
==========================================

This lesson demonstrates how to save
an image using OpenCV.
"""

import cv2

# Read the image
image = cv2.imread("dataset/flower.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully!")

    # Save the image with a new name
    success = cv2.imwrite("saved_flower.jpg", image)

    if success:
        print("Image saved successfully!")
        print("New file created: saved_flower.jpg")
    else:
        print("Failed to save the image.")

print("\nLesson 5 completed successfully!")