"""
==========================================
Module 4 - Image Processing
Lesson 1 - Introduction to Image Processing
==========================================

"""

import cv2

print("========== MODULE 4 : IMAGE PROCESSING ==========\n")

# Load image
image = cv2.imread("dataset/flower.jpg")

# Check whether image exists
if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Original Image Shape :", image.shape)
print("Grayscale Shape      :", gray.shape)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("\nLesson 1 Completed Successfully!")