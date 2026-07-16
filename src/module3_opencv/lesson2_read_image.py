"""
==========================================
Module 3 - OpenCV Basics
Lesson 2 - Reading an Image
==========================================
"""

import cv2

# Read the image
image = cv2.imread("dataset/flower.jpg")

# Check if the image loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully!")
    print("\nImage Data:")
    print(image)