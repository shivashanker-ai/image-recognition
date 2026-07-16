"""
==========================================
Module 3 - OpenCV Basics
Lesson 6 - Resizing Images
==========================================

This lesson demonstrates how to resize
an image using OpenCV.
"""

import cv2

# Read the image
image = cv2.imread("dataset/flower.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    print("========== IMAGE RESIZING ==========\n")

    # Display original image properties
    print("Original Shape :", image.shape)

    # Resize the image to 224 x 224
    resized_image = cv2.resize(image, (224, 224))

    # Display resized image properties
    print("Resized Shape :", resized_image.shape)

    # Show both images
    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image (224x224)", resized_image)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

    print("\nLesson 6 completed successfully!")