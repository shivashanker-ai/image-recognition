"""
==========================================
Module 4 - Image Processing
Lesson 3 - Image Thresholding
==========================================
"""

import cv2

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Binary Threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Binary Image", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Lesson 3 Completed Successfully!")