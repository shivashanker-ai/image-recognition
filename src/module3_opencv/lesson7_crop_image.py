"""
==========================================
Module 3 - OpenCV Basics
Lesson 7 - Cropping Images
==========================================

This lesson demonstrates how to crop
an image using NumPy slicing.
"""

import cv2

# Read the image
image = cv2.imread("dataset/flower.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    print("========== IMAGE CROPPING ==========\n")

    # Crop the image (rows, columns)
    cropped_image = image[100:400, 150:450]

    # Display both images
    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped Image", cropped_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Lesson 7 completed successfully!")