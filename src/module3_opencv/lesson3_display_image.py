"""
==========================================
Module 3 - OpenCV Basics
Lesson 3 - Displaying an Image
==========================================
"""

import cv2

# Read the image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
else:
    cv2.namedWindow("Flower Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Flower Image", image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()