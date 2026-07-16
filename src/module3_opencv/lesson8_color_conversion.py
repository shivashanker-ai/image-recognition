"""
==========================================
Module 3 - OpenCV Basics
Lesson 8 - Color Conversion
==========================================

This lesson demonstrates how to convert
a color image to grayscale using OpenCV.
"""

import cv2

# Read the image
image = cv2.imread("dataset/flower.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    print("========== COLOR CONVERSION ==========\n")

    # Convert BGR image to Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display image properties
    print("Original Shape :", image.shape)
    print("Grayscale Shape:", gray.shape)

    # Display both images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

    print("\nLesson 8 completed successfully!")