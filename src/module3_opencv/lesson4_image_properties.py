"""
==========================================
Module 3 - OpenCV Basics
Lesson 4 - Image Properties
==========================================

This lesson demonstrates how to inspect
the properties of an image using OpenCV.
"""

import cv2

# Read the image
image = cv2.imread("dataset/flower.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    print("========== IMAGE PROPERTIES ==========\n")

    # Shape of the image
    print("Shape:", image.shape)

    # Height
    print("Height:", image.shape[0], "pixels")

    # Width
    print("Width:", image.shape[1], "pixels")

    # Number of color channels
    print("Channels:", image.shape[2])

    # Total number of values
    print("Total Values:", image.size)

    # Data type of the image
    print("Data Type:", image.dtype)

    print("\nLesson 4 completed successfully!")